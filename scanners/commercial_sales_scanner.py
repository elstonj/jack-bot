"""Commercial sales & support pipeline scanner.

Populates knowledge/commercial_sales/{builds,support}/ from:
  - Asana Commercial Sales project (canonical anchor for each Build)
  - Gmail mailboxes info@, sales@, support@ (impersonated via service account)
  - Slack #commercial-sales channel history
  - Inferred linkage to purchases/ records (for the parts checklist)

Per-build Haiku extraction: for each Asana task we gather the task fields,
related emails, related Slack messages, and the existing JSON record, then ask
Haiku to produce an updated structured Build record. The same flow is used for
support cases (anchored on support@ email threads, with optional Asana tasks).

Customers seen in email but with no matching Asana task are logged in
knowledge/commercial_sales/_unmapped_customers.md so the user can decide
whether to create Asana tasks for them. This scanner never creates Asana
tasks itself (that's Phase 2 — propose-and-confirm via Slack).
"""

from __future__ import annotations

import base64
import json
import os
import re
import time
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Optional

import requests
from googleapiclient.discovery import build

from .base import (
    KNOWLEDGE_DIR,
    get_claude_client,
    get_last_scan,
    update_scan_timestamp,
    DISTILL_MODEL,
)
from google_client import _get_credentials
from commercial_sales import (
    Build,
    Item,
    Part,
    SupportCase,
    BUILD_STATES,
    PAYMENT_STATES,
    SHIP_STATES,
    SUPPORT_STATES,
    load_builds,
    load_support_cases,
    save_build,
    save_support,
    BUILDS_DIR,
    SUPPORT_DIR,
)


ASANA_BASE = "https://app.asana.com/api/1.0"
CS_KNOWLEDGE_DIR = KNOWLEDGE_DIR / "commercial_sales"

# Pre-distilled knowledge files used as additional evidence for each Build
QBO_COMMERCIAL_FILE = KNOWLEDGE_DIR / "quickbooks" / "by_project" / "commercial.md"
CONTACTS_EXTERNAL_FILE = KNOWLEDGE_DIR / "contacts" / "external.md"
PROJECT_REGISTRY_DIR = KNOWLEDGE_DIR / "projects"
ASANA_PROJECTS_DIR = KNOWLEDGE_DIR / "asana" / "projects"

# Email window — older threads rarely have useful new signal
EMAIL_WINDOW_DAYS = 90
SLACK_WINDOW_DAYS = 60

# Extra Slack channels to scan beyond #commercial-sales. The user constraint:
# stay BOUNDED — these are obvious-signal places where customer/build context
# leaks (post-delivery flight testing, ops chatter, internal coordination).
# Don't auto-expand further; rely on missing-info callouts for unfilled gaps.
EXTRA_SLACK_CHANNELS = ["flight-testing", "operations", "general"]
EXTRA_SLACK_PER_CHANNEL = 50  # cap per channel — total combined search space stays modest

# Per-build direct email search (Fix 3b). Bounded:
#   - only fires when the existing record has a non-generic customer name or
#     a known customer_email
#   - 5 messages per build, single Gmail query, no pagination
PER_BUILD_DIRECT_EMAIL_CAP = 5
DIRECT_EMAIL_WINDOW_DAYS = 180

# Customer names too generic to use as a search anchor without risking massive
# false-positive sweeps of unrelated traffic. Skip direct-email search for these.
GENERIC_CUSTOMER_TOKENS = {
    "usaf", "army", "navy", "marines", "dod", "dow", "nasa", "noaa", "usgs",
    "darpa", "socom", "uscg", "afrl", "afit", "uk", "us", "customer",
    "university", "research", "institute", "laboratory", "lab",
}

# Shared addresses we treat as customer-conversation sources.
#
# These are distribution groups, not direct-impersonable Gmail mailboxes
# (same situation as purchasing@ — see scanners/purchasing_scanner.py). We
# impersonate the admin user (GOOGLE_ADMIN_EMAIL, default elstonj@) and
# search their mailbox for messages where any of these addresses appear in
# to:/from:/cc:/bcc:. The admin is on each of these groups, so coverage is
# ~complete for messages actually delivered to the group.
SHARED_ADDRESSES = [
    "sales@blackswifttech.com",
    "info@blackswifttech.com",
    "support@blackswifttech.com",
]


def _admin_impersonation_user() -> str:
    return os.environ.get("GOOGLE_ADMIN_EMAIL") or "elstonj@blackswifttech.com"

# Per-mailbox per-scan cap to keep token cost and runtime sane
EMAILS_PER_MAILBOX_CAP = 400

# How many emails to feed Haiku per Build (most recent first)
EVIDENCE_EMAILS_PER_BUILD = 12
EVIDENCE_SLACK_PER_BUILD = 15


# ---------------------------------------------------------------------------
# Asana
# ---------------------------------------------------------------------------


def _asana_headers():
    return {"Authorization": f"Bearer {os.environ['ASANA_ACCESS_TOKEN']}"}


def _find_commercial_sales_project() -> Optional[dict]:
    """Locate the Commercial Sales project in Asana.

    Resolution order:
      1. ASANA_COMMERCIAL_SALES_PROJECT_GID env var
      2. Substring "commercial sales" or "commercial-sales" in project name
    """
    gid = os.environ.get("ASANA_COMMERCIAL_SALES_PROJECT_GID")
    if gid:
        try:
            resp = requests.get(
                f"{ASANA_BASE}/projects/{gid}",
                headers=_asana_headers(),
                params={"opt_fields": "name,gid,permalink_url"},
                timeout=10,
            )
            resp.raise_for_status()
            return resp.json()["data"]
        except Exception as e:
            print(f"  [WARN] ASANA_COMMERCIAL_SALES_PROJECT_GID set but lookup failed: {e}")

    # Fall back to name search
    resp = requests.get(f"{ASANA_BASE}/workspaces", headers=_asana_headers(), timeout=10)
    resp.raise_for_status()
    workspaces = resp.json()["data"]
    if not workspaces:
        return None
    workspace_gid = workspaces[0]["gid"]

    resp = requests.get(
        f"{ASANA_BASE}/projects",
        headers=_asana_headers(),
        params={
            "workspace": workspace_gid,
            "limit": 100,
            "opt_fields": "name,gid,permalink_url,archived",
        },
        timeout=15,
    )
    resp.raise_for_status()
    for p in resp.json()["data"]:
        if p.get("archived"):
            continue
        name = (p.get("name") or "").lower()
        if "commercial sales" in name or "commercial-sales" in name:
            return p
    return None


def _fetch_commercial_sales_tasks(project_gid: str) -> list[dict]:
    """Fetch all open tasks in the Commercial Sales project, plus tasks
    completed in the last 60 days (so we can keep delivered builds visible
    briefly before pruning).
    """
    cutoff = (datetime.utcnow() - timedelta(days=60)).strftime("%Y-%m-%dT%H:%M:%S.000Z")
    resp = requests.get(
        f"{ASANA_BASE}/tasks",
        headers=_asana_headers(),
        params={
            "project": project_gid,
            "opt_fields": (
                "name,assignee.name,assignee.email,due_on,due_at,completed,"
                "completed_at,created_at,modified_at,custom_fields,notes,"
                "permalink_url,tags.name"
            ),
            "completed_since": cutoff,
            "limit": 100,
        },
        timeout=20,
    )
    resp.raise_for_status()
    return resp.json().get("data", [])


# ---------------------------------------------------------------------------
# Gmail (one Gmail service per mailbox)
# ---------------------------------------------------------------------------


def _build_gmail_service(user_email: str):
    creds = _get_credentials(user_email)
    if not creds:
        return None
    return build("gmail", "v1", credentials=creds, cache_discovery=False)


def _build_admin_gmail_service():
    """Service impersonating the admin user — used to scan shared-address traffic."""
    return _build_gmail_service(_admin_impersonation_user())


def _decode_part(part: dict) -> str:
    body = part.get("body", {})
    data = body.get("data")
    if not data:
        return ""
    try:
        return base64.urlsafe_b64decode(data + "===").decode("utf-8", errors="replace")
    except Exception:
        return ""


def _extract_body(payload: dict) -> str:
    """Best-effort plain-text body from a Gmail payload (recursively walks parts)."""
    mime = payload.get("mimeType", "")
    if mime == "text/plain":
        return _decode_part(payload)
    if mime == "text/html":
        html = _decode_part(payload)
        return re.sub(r"<[^>]+>", " ", html)
    plain, html = "", ""
    for p in payload.get("parts") or []:
        sub_mime = p.get("mimeType", "")
        if sub_mime == "text/plain" and not plain:
            plain = _decode_part(p)
        elif sub_mime == "text/html" and not html:
            html = _decode_part(p)
        elif sub_mime.startswith("multipart/"):
            nested = _extract_body(p)
            if nested and not plain:
                plain = nested
    if plain:
        return plain
    if html:
        return re.sub(r"<[^>]+>", " ", html)
    return ""


def _extract_attachments(payload: dict) -> list[dict]:
    """Return [{name, mime, size}] for each attachment (file-only, no inline)."""
    out = []

    def walk(p):
        filename = p.get("filename") or ""
        mime = p.get("mimeType") or ""
        body = p.get("body") or {}
        size = body.get("size") or 0
        if filename and size > 1000:  # skip tiny inline parts
            out.append({"name": filename, "mime": mime, "size": size})
        for sub in p.get("parts") or []:
            walk(sub)

    walk(payload)
    return out


def _fetch_admin_query_emails(query: str, mailbox_label: str, cap: int) -> list[dict]:
    """Pull emails matching `query` from the admin's mailbox (impersonated).

    Used to scan shared distribution groups (info@/sales@/support@) which
    aren't directly impersonable. The admin is on each group, so a `to/from/
    cc/bcc:` filter on the admin's mailbox covers traffic delivered to the
    group. `mailbox_label` is what we tag each email with so downstream
    grouping knows which logical inbox the message belongs to.

    Returns list of dicts: {id, mailbox, date, from, to, subject, snippet,
    body, attachments}. Returns [] on auth failure.
    """
    admin = _admin_impersonation_user()
    service = _build_gmail_service(admin)
    if not service:
        print(f"  [WARN] Could not impersonate admin {admin} — skipping {mailbox_label}")
        return []

    ids: list[str] = []
    page_token = None
    while len(ids) < cap:
        kwargs = {"userId": "me", "q": query, "maxResults": min(100, cap - len(ids))}
        if page_token:
            kwargs["pageToken"] = page_token
        try:
            resp = service.users().messages().list(**kwargs).execute()
        except Exception as e:
            print(f"  [WARN] Gmail list failed for {mailbox_label}: {e}")
            break
        for m in resp.get("messages", []) or []:
            ids.append(m["id"])
        page_token = resp.get("nextPageToken")
        if not page_token:
            break

    messages = []
    for mid in ids:
        try:
            msg = service.users().messages().get(
                userId="me", id=mid, format="full"
            ).execute()
        except Exception:
            continue
        payload = msg.get("payload") or {}
        headers = {h["name"].lower(): h["value"] for h in payload.get("headers") or []}
        body = _extract_body(payload)
        attachments = _extract_attachments(payload)
        try:
            ts = int(msg.get("internalDate", "0")) / 1000
            iso = datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
        except Exception:
            iso = ""
        messages.append({
            "id": mid,
            "mailbox": mailbox_label,
            "date": iso,
            "subject": headers.get("subject", "")[:300],
            "from": headers.get("from", "")[:300],
            "to": headers.get("to", "")[:400],
            "cc": headers.get("cc", "")[:400],
            "snippet": (msg.get("snippet") or "")[:400],
            "body": body[:6000],  # cap body size to bound Haiku tokens
            "attachments": attachments,
        })
        time.sleep(0.05)
    return messages


def _build_shared_address_query(shared_address: str, days: int) -> str:
    return (
        f"(to:{shared_address} OR from:{shared_address} "
        f"OR cc:{shared_address} OR bcc:{shared_address}) "
        f"newer_than:{days}d -category:promotions -category:social"
    )


# ---------------------------------------------------------------------------
# Slack
# ---------------------------------------------------------------------------


def _find_commercial_sales_channel(slack_client) -> Optional[str]:
    """Resolve the #commercial-sales channel ID."""
    env_id = os.environ.get("COMMERCIAL_SALES_CHANNEL")
    if env_id:
        return env_id
    try:
        cursor = None
        for _ in range(10):
            kwargs = {
                "types": "public_channel,private_channel",
                "limit": 200,
            }
            if cursor:
                kwargs["cursor"] = cursor
            result = slack_client.conversations_list(**kwargs)
            for ch in result.get("channels", []):
                if ch.get("name") in ("commercial-sales", "commercial_sales"):
                    return ch["id"]
            cursor = result.get("response_metadata", {}).get("next_cursor")
            if not cursor:
                break
    except Exception as e:
        print(f"  [WARN] Could not search Slack channels: {e}")
    return None


def _fetch_slack_history(slack_client, channel_id: str, days: int,
                         channel_name: str = "", cap: Optional[int] = None) -> list[dict]:
    """Pull recent messages from one Slack channel.

    Each message is tagged with `channel` so downstream prompts can show
    `--- SLACK [#channel] {date} {text}` and Haiku knows the source context.
    """
    if not channel_id:
        return []
    oldest = str(int(time.time() - (days * 86400)))
    messages: list[dict] = []
    cursor = None
    for _ in range(10):
        kwargs = {"channel": channel_id, "limit": 200, "oldest": oldest}
        if cursor:
            kwargs["cursor"] = cursor
        try:
            result = slack_client.conversations_history(**kwargs)
        except Exception as e:
            print(f"  [WARN] Slack history failed for #{channel_name or channel_id}: {e}")
            break
        for msg in result.get("messages", []) or []:
            text = (msg.get("text") or "").strip()
            if not text:
                continue
            if msg.get("subtype") in ("channel_join", "channel_leave", "channel_topic", "channel_purpose"):
                continue
            try:
                msg_date = datetime.fromtimestamp(float(msg.get("ts", "0"))).strftime("%Y-%m-%d")
            except Exception:
                msg_date = ""
            messages.append({
                "ts": msg.get("ts"),
                "user": msg.get("user", ""),
                "date": msg_date,
                "channel": channel_name or "",
                "text": text[:600],
            })
            if cap and len(messages) >= cap:
                break
        cursor = result.get("response_metadata", {}).get("next_cursor")
        if not cursor or (cap and len(messages) >= cap):
            break
    return messages


def _find_channel_id_by_name(slack_client, name: str) -> Optional[str]:
    """Look up a channel ID by name. Returns None if not found or bot not a member."""
    try:
        cursor = None
        for _ in range(10):
            kwargs = {
                "types": "public_channel,private_channel",
                "limit": 200,
                "exclude_archived": True,
            }
            if cursor:
                kwargs["cursor"] = cursor
            result = slack_client.conversations_list(**kwargs)
            for ch in result.get("channels", []):
                if ch.get("name") == name and ch.get("is_member"):
                    return ch["id"]
            cursor = result.get("response_metadata", {}).get("next_cursor")
            if not cursor:
                break
    except Exception:
        pass
    return None


def _fetch_extra_slack_history(slack_client) -> list[dict]:
    """Pull bounded history from the EXTRA_SLACK_CHANNELS list.

    Per channel: 60-day window, 50-message cap, silent skip when channel is
    missing or bot isn't a member. Each message is tagged with its source.
    """
    out: list[dict] = []
    for name in EXTRA_SLACK_CHANNELS:
        ch_id = _find_channel_id_by_name(slack_client, name)
        if not ch_id:
            continue
        msgs = _fetch_slack_history(
            slack_client, ch_id, SLACK_WINDOW_DAYS,
            channel_name=name, cap=EXTRA_SLACK_PER_CHANNEL,
        )
        if msgs:
            print(f"  Slack #{name}: {len(msgs)} messages")
            out.extend(msgs)
    return out


# ---------------------------------------------------------------------------
# Customer-evidence matching
# ---------------------------------------------------------------------------


INTERNAL_DOMAINS = {"blackswifttech.com", "bst.aero"}


def _sender_domain(addr: str) -> str:
    """Extract the domain from a From: header like 'Beck Foo <beck@acme.com>'."""
    m = re.search(r"@([\w.-]+)", addr or "")
    return m.group(1).lower() if m else ""


def _is_internal(addr: str) -> bool:
    return _sender_domain(addr) in INTERNAL_DOMAINS


def _customer_tokens(task: dict) -> set[str]:
    """Extract tokens we can match emails/slack against for one Asana task.

    Uses the task name and any custom-field that names a customer/organization.
    """
    tokens = set()
    name = (task.get("name") or "").lower()
    # Strip leading bracketed codes, then take word tokens of length>=4
    cleaned = re.sub(r"\[[^\]]+\]", " ", name)
    cleaned = re.sub(r"[^\w\s]", " ", cleaned)
    for tok in cleaned.split():
        if len(tok) >= 4 and not tok.isdigit():
            tokens.add(tok)
    # Custom field hints
    for cf in task.get("custom_fields") or []:
        if not cf:
            continue
        val = (cf.get("display_value") or "").lower()
        cf_name = (cf.get("name") or "").lower()
        if not val:
            continue
        if any(k in cf_name for k in ("customer", "organization", "contact", "company")):
            for tok in re.sub(r"[^\w\s]", " ", val).split():
                if len(tok) >= 4 and not tok.isdigit():
                    tokens.add(tok)
    return tokens


def _filter_emails_for_tokens(emails: list[dict], tokens: set[str], limit: int) -> list[dict]:
    """Return up to `limit` emails (newest first) that mention any token.

    Only matches non-internal senders to avoid pulling in pure internal noise,
    unless the body text references one of the tokens (Beck forwarding from
    a customer thread inside an internal email, for instance).
    """
    if not tokens:
        return []
    scored = []
    for e in emails:
        haystack = " ".join((
            e.get("subject") or "",
            e.get("from") or "",
            e.get("to") or "",
            e.get("snippet") or "",
            (e.get("body") or "")[:2000],
        )).lower()
        hits = sum(1 for t in tokens if t in haystack)
        if hits == 0:
            continue
        scored.append((hits, e.get("date") or "", e))
    scored.sort(key=lambda x: (x[1], x[0]), reverse=True)
    return [e for _, _, e in scored[:limit]]


def _tokens_for_match(s: str) -> set[str]:
    """Tokenize a customer/project string for fuzzy matching.

    Strips bracketed codes and punctuation, keeps lowercase tokens of length
    >= 4 that aren't pure digits. Same shape as `_customer_tokens` but for
    arbitrary strings rather than Asana tasks.
    """
    if not s:
        return set()
    cleaned = re.sub(r"\[[^\]]+\]|\([^)]+\)", " ", s.lower())
    cleaned = re.sub(r"[^\w\s]", " ", cleaned)
    return {t for t in cleaned.split() if len(t) >= 4 and not t.isdigit()}


# --- Knowledge-file evidence helpers ----------------------------------------
# Cached once per scan_all() invocation


_QBO_CACHE: list[dict] = []
_QBO_LOADED = False

# Per-scan accumulator of filter decisions. Cleared at the top of scan_all().
# Each entry: {"kind": "build"|"support", "label": str, "gid": str|None,
#              "reason": str, "date": ISO}
_FILTERED_THIS_SCAN: list[dict] = []


def _load_qbo_invoices() -> list[dict]:
    """Parse knowledge/quickbooks/by_project/commercial.md into invoice dicts.

    Returns [{'number': str, 'date': str, 'amount': float, 'customer': str,
              'balance': str, 'paid': bool}, ...]
    """
    global _QBO_CACHE, _QBO_LOADED
    if _QBO_LOADED:
        return _QBO_CACHE
    _QBO_LOADED = True
    if not QBO_COMMERCIAL_FILE.exists():
        return []
    invoices = []
    in_table = False
    for line in QBO_COMMERCIAL_FILE.read_text().splitlines():
        stripped = line.strip()
        if "| Invoice" in stripped and "Customer" in stripped:
            in_table = True
            continue
        if in_table and stripped.startswith("|----"):
            continue
        if in_table and stripped.startswith("|"):
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            if len(cells) >= 5:
                num, dt, amt, cust, bal = cells[:5]
                amt_clean = amt.replace("$", "").replace(",", "")
                try:
                    amount = float(amt_clean)
                except ValueError:
                    amount = 0.0
                invoices.append({
                    "number": num,
                    "date": dt,
                    "amount": amount,
                    "customer": cust,
                    "balance": bal,
                    "paid": ("Paid" in bal) or ("Voided" in bal),
                })
        elif in_table and not stripped.startswith("|"):
            in_table = False
    _QBO_CACHE = invoices
    return invoices


def _qbo_invoices_for_customer(customer: str, project_code: Optional[str]) -> list[dict]:
    """Find QBO invoices that match either the customer name tokens or
    the project code (extracted from QBO 'customer' fields like '[043-3] By Light Halo').
    """
    invoices = _load_qbo_invoices()
    if not invoices:
        return []
    customer_tokens = _tokens_for_match(customer)
    matched = []
    seen = set()
    for inv in invoices:
        key = inv["number"] + "|" + inv["date"]
        if key in seen:
            continue
        inv_cust = inv["customer"]
        inv_cust_lower = inv_cust.lower()
        # Project-code match (handles [XXX-Y] and (XXX-Y) styles)
        if project_code:
            code_hyphen = project_code.replace("_", "-")
            if code_hyphen in inv_cust:
                matched.append(inv)
                seen.add(key)
                continue
        # Token overlap (need at least 1 token of length >= 4)
        if customer_tokens:
            inv_tokens = _tokens_for_match(inv_cust)
            if customer_tokens & inv_tokens:
                matched.append(inv)
                seen.add(key)
                continue
        # Substring fallback for short customer names ("ByLight" → "By Light")
        if customer and len(customer) >= 4:
            cust_squashed = re.sub(r"\s+", "", customer.lower())
            inv_squashed = re.sub(r"\s+", "", inv_cust_lower)
            if cust_squashed in inv_squashed or inv_squashed in cust_squashed:
                matched.append(inv)
                seen.add(key)
    # Newest first
    matched.sort(key=lambda i: i.get("date", ""), reverse=True)
    return matched[:20]  # cap to avoid token bloat


def _contacts_block_for_customer(customer: str) -> Optional[str]:
    """Search knowledge/contacts/external.md for the customer's section."""
    if not CONTACTS_EXTERNAL_FILE.exists():
        return None
    tokens = _tokens_for_match(customer)
    if not tokens and not customer:
        return None
    text = CONTACTS_EXTERNAL_FILE.read_text()
    # Sections delimited by `### ` headers
    sections = re.split(r"^### ", text, flags=re.MULTILINE)
    for section in sections[1:]:  # skip preamble
        header = section.split("\n", 1)[0].lower()
        if customer.lower() in header:
            return ("### " + section)[:2500]
        if tokens and any(t in header for t in tokens):
            return ("### " + section)[:2500]
    return None


def _project_registry_for_customer(customer: str, project_code: Optional[str]) -> Optional[str]:
    """Return contents of a matching knowledge/projects/{code}.md if found."""
    if not PROJECT_REGISTRY_DIR.exists():
        return None
    if project_code:
        candidate = PROJECT_REGISTRY_DIR / f"{project_code.replace('-', '_')}.md"
        if candidate.exists():
            return candidate.read_text()[:3000]
    if not customer:
        return None
    tokens = _tokens_for_match(customer)
    if not tokens:
        return None
    best_score = 0
    best_text = None
    for f in PROJECT_REGISTRY_DIR.glob("*.md"):
        if f.name == "registry.md":
            continue
        try:
            text = f.read_text()
        except Exception:
            continue
        head = text[:4000].lower()
        score = sum(1 for t in tokens if t in head)
        if score >= 2 and score > best_score:
            best_score = score
            best_text = text[:3000]
    return best_text


def _looks_generic_customer(customer: str) -> bool:
    """Skip direct-email search if the customer name is too generic to anchor.

    Returns True for: empty, single short token, or anything where every token
    is in the GENERIC_CUSTOMER_TOKENS denylist or is shorter than 4 chars.
    """
    if not customer:
        return True
    tokens = [t.lower() for t in re.split(r"[\s,/\-_]+", customer) if t]
    substantive = [t for t in tokens if len(t) >= 4 and t not in GENERIC_CUSTOMER_TOKENS]
    return len(substantive) < 2


def _fetch_direct_customer_emails(customer: str, customer_email: Optional[str],
                                  days: int = DIRECT_EMAIL_WINDOW_DAYS) -> list[dict]:
    """Single bounded Gmail query on admin mailbox, hunting for direct
    correspondence about this customer that didn't go through the shared groups.

    Bounded:
      - Caps at PER_BUILD_DIRECT_EMAIL_CAP messages, no pagination
      - Only runs when we have customer_email OR a non-generic customer name
      - One query per build per scan
    """
    if not customer_email and _looks_generic_customer(customer):
        return []
    # Build query: from:<email> OR subject:"<2-3 tokens>"
    clauses = []
    if customer_email:
        clauses.append(f"(from:{customer_email})")
    if customer:
        tokens = [t for t in re.split(r"[\s,/\-_]+", customer)
                  if t and len(t) >= 4 and t.lower() not in GENERIC_CUSTOMER_TOKENS]
        if len(tokens) >= 2:
            phrase = " ".join(tokens[:3])
            clauses.append(f'(subject:"{phrase}")')
    if not clauses:
        return []
    query = f"({' OR '.join(clauses)}) newer_than:{days}d"
    return _fetch_admin_query_emails(
        query, mailbox_label=f"direct:{customer[:40]}", cap=PER_BUILD_DIRECT_EMAIL_CAP,
    )


def _format_qbo_evidence(invoices: list[dict]) -> str:
    if not invoices:
        return ""
    lines = ["QBO INVOICES (truth source for payment state):"]
    for inv in invoices:
        amt = f"${inv['amount']:,.2f}" if inv['amount'] else "$0"
        status = "PAID" if inv['paid'] else f"balance {inv['balance']}"
        lines.append(
            f"  - Inv #{inv['number']} ({inv['date']}) {amt} → {inv['customer']} [{status}]"
        )
    return "\n".join(lines)


def _extract_project_code_from_task(task: dict) -> Optional[str]:
    """Look for a [XXX-Y] code in the task name or custom fields."""
    name = task.get("name") or ""
    m = re.search(r"\[(\d{3}[-_]\d{1,2})\]", name)
    if m:
        return m.group(1).replace("_", "-")
    for cf in task.get("custom_fields") or []:
        val = (cf.get("display_value") or "") if cf else ""
        m = re.search(r"\[(\d{3}[-_]\d{1,2})\]", val)
        if m:
            return m.group(1).replace("_", "-")
    return None


def _gather_knowledge_evidence(customer: str, project_code: Optional[str]) -> str:
    """Build the KNOWLEDGE EVIDENCE block for the Haiku prompt.

    Pulls QBO invoices, external contacts, project registry — all matched to
    the customer name and/or project code. Returns empty string if nothing
    matched, otherwise a single multi-section block.
    """
    pieces = []

    invoices = _qbo_invoices_for_customer(customer, project_code)
    if invoices:
        pieces.append(_format_qbo_evidence(invoices))

    contact = _contacts_block_for_customer(customer)
    if contact:
        pieces.append("EXTERNAL CONTACT RECORD:\n" + contact)

    registry = _project_registry_for_customer(customer, project_code)
    if registry:
        pieces.append("PROJECT REGISTRY FILE:\n" + registry)

    if not pieces:
        return ""
    return "KNOWLEDGE EVIDENCE (pre-distilled — treat QBO as authoritative for payment state):\n\n" + "\n\n".join(pieces)


def _filter_slack_for_tokens(messages: list[dict], tokens: set[str], limit: int) -> list[dict]:
    if not tokens:
        return []
    matched = []
    for m in messages:
        text = (m.get("text") or "").lower()
        if any(t in text for t in tokens):
            matched.append(m)
    matched.sort(key=lambda m: m.get("date") or "", reverse=True)
    return matched[:limit]


# ---------------------------------------------------------------------------
# Haiku extraction
# ---------------------------------------------------------------------------


BUILD_EXTRACTION_PROMPT = """\
You extract structured "Build" records for Black Swift Technologies (BST), a small
aerospace company that builds and sells small unmanned aircraft and sensor systems
to commercial customers.

You are given:
  - The current JSON record (may be mostly empty for a new Build).
  - Asana task details: name, notes, custom fields, due date, assignee.
  - Recent emails from sales@/info@ that mention this customer.
  - Recent Slack #commercial-sales messages that mention this customer.

Produce ONE JSON object as your reply — a complete updated Build record. Output
ONLY valid JSON, no commentary, no markdown fences.

FIRST: decide whether this Asana task represents a real customer build. Some
BD Pipeline tasks are internal action items (e.g. "Send slides", "Cleanup
deck", "Develop concept", "Internal review") rather than tracked sales. If
it's NOT a real customer build, output:
  {"is_customer_build": false, "asana_gid": "<gid>", "reason": "<1-sentence>"}
and stop. Otherwise output is_customer_build=true and the full schema below.

Schema (omit any field you can't infer, keep existing values when no new evidence):
{
  "is_customer_build": true,
  "asana_gid": "<keep the existing gid>",
  "customer": "...",
  "customer_contact": "...",
  "customer_email": "...",
  "receive_by": "YYYY-MM-DD" | null,
  "ship_to": "...",
  "items": [ {"description": "...", "quantity": N}, ... ],
  "payment_state": "none" | "estimate_sent" | "invoice_sent" | "paid",
  "build_state": "none" | "parts_ordered" | "in_assembly" | "in_qc" | "complete" | "packaged",
  "ship_state": "none" | "awaiting_pickup" | "in_transit" | "delivered",
  "estimate_date": "YYYY-MM-DD" | null,
  "invoice_date": "YYYY-MM-DD" | null,
  "invoice_amount": <number> | null,
  "invoice_number": "...",
  "paid_date": "YYYY-MM-DD" | null,
  "parts": [ {"name": "...", "ordered": bool, "received": bool, "vendor": "..."}, ... ],
  "tracking_number": "...",
  "carrier": "...",
  "shipped_date": "YYYY-MM-DD" | null,
  "owners": { "interface": "Beck", "invoicing": "Meredith", "build": "Nate" },
  "notes": "1-2 sentence freeform context if useful",
  "missing_fields": [ "ship_to", "receive_by", ... ],
  "last_evidence_date": "YYYY-MM-DD"
}

Rules:
- payment_state: QBO INVOICES are the truth source — if there's a QBO invoice
  matching this customer, payment_state is at least "invoice_sent". If the
  invoice balance shows "Paid" it's "paid". If no QBO invoice but an estimate
  is mentioned in email/Slack/Asana, use "estimate_sent". Otherwise "none".
  When you find a matching QBO invoice, populate invoice_number, invoice_date,
  invoice_amount from that record.
- build_state: only advance if you see explicit signal. Specifically:
  * "parts_ordered" requires an actual PO / vendor order confirmation in
    Meredith's emails or QBO purchases. "We need to order X" doesn't qualify.
  * "in_assembly" requires evidence of physical assembly work in progress at
    BST (workshop discussions, "started build of S20009", "soldering ESC").
  * "in_qc" REQUIRES explicit BST-internal QC / acceptance-test language —
    "QC complete", "passed acceptance test", "internal validation", "ATP".
    *Customer-side "flight testing" is NOT QC* — that's post-delivery use, so
    build_state should be "complete" or "packaged" and ship_state should be
    "delivered" (or earlier if it shipped recently).
  * "complete" / "packaged" require evidence the build is done; "shipped"
    requires tracking / pickup confirmation.
  Default to the existing state if evidence is ambiguous — don't speculate.
- ship_state: only "in_transit" if you see a tracking number or carrier confirmation;
  "delivered" if explicit delivery confirmation.
- items: parse from estimate or invoice attachments mentioned in the email body
  (subject lines, line items in quoted body text). If you only have an attachment
  filename like "Estimate-2026-018.pdf" with no body content, leave items as-is.
- parts: small-aerospace components like "flight controllers", "ESCs", "servos",
  "cameras", "airframe shells". Mark `ordered` when a purchase email is visible;
  `received` only when a delivery is confirmed.
- owners: default to Beck/Meredith/Nate. Only override if a recent email/Slack
  message says someone else is handling that role for this build.
- missing_fields: list the schema fields that aren't filled in yet AND that
  would matter for the morning digest (ship_to, receive_by, items, parts).
  Don't list optional fields like tracking_number if shipping hasn't started.
- last_evidence_date: the date of the most recent email/Slack message used.
- Be conservative. If evidence conflicts (e.g. an old email says "estimate sent"
  but a newer one says "invoice sent and paid"), use the newer signal.
- NEVER fabricate. If you can't determine the customer name, leave it blank
  rather than guessing.
"""


def _haiku_extract_build(task: dict, existing: Optional[Build],
                         emails: list[dict], slack_msgs: list[dict],
                         knowledge_evidence: str = "") -> tuple[Optional[Build], bool]:
    """Call Haiku to produce/update a Build record from raw evidence.

    Returns (build, drop_existing):
      (Build, False)  — normal update; save and use.
      (None,  True)   — Haiku said is_customer_build=false; caller should
                        delete any prior JSON file for this gid.
      (None,  False)  — Haiku failed (network / malformed JSON); caller
                        should keep any existing record intact.
    """
    existing_json = existing.to_dict() if existing else {"asana_gid": task["gid"]}

    # Compact custom-field rendering
    cf_lines = []
    for cf in task.get("custom_fields") or []:
        if cf and cf.get("display_value"):
            cf_lines.append(f"  - {cf.get('name', '')}: {cf['display_value']}")

    task_block = (
        f"ASANA TASK\n"
        f"  gid: {task['gid']}\n"
        f"  name: {task.get('name', '')}\n"
        f"  due_on: {task.get('due_on') or '(no due date)'}\n"
        f"  assignee: {(task.get('assignee') or {}).get('name', 'unassigned')}\n"
        f"  notes: {(task.get('notes') or '')[:1500]}\n"
        + ("  custom_fields:\n" + "\n".join(cf_lines) if cf_lines else "")
    )

    email_blocks = []
    for e in emails:
        att_str = ""
        if e.get("attachments"):
            att_str = " attachments=" + ", ".join(a["name"] for a in e["attachments"][:5])
        email_blocks.append(
            f"--- EMAIL [{e.get('mailbox','')}] {e.get('date','')} "
            f"from {e.get('from','')} → {e.get('to','')}{att_str}\n"
            f"Subject: {e.get('subject','')}\n"
            f"{(e.get('body') or e.get('snippet') or '')[:2500]}"
        )

    slack_blocks = []
    for m in slack_msgs:
        ch = m.get("channel") or ""
        ch_tag = f"[#{ch}] " if ch else ""
        slack_blocks.append(f"--- SLACK {ch_tag}{m.get('date','')} {m.get('text','')[:500]}")

    slack_note = ""
    if slack_blocks:
        slack_note = (
            "(Slack channel tags: [#commercial-sales] = sales coordination, "
            "[#flight-testing] = post-delivery flight ops, [#operations] = "
            "team daily ops, [#general] = company-wide. Flight-testing/ops "
            "chatter on a delivered unit is post-delivery — NOT QC.)\n"
        )

    user_content = (
        "CURRENT JSON RECORD:\n"
        f"{json.dumps(existing_json, indent=2)}\n\n"
        + (knowledge_evidence + "\n\n" if knowledge_evidence else "")
        + f"{task_block}\n\n"
        + ("RECENT EMAILS:\n" + "\n\n".join(email_blocks) + "\n\n" if email_blocks else "")
        + ("RECENT SLACK:\n" + slack_note + "\n".join(slack_blocks) + "\n\n" if slack_blocks else "")
        + "Produce the updated JSON Build record now."
    )

    # Cap user_content
    if len(user_content) > 90000:
        user_content = user_content[:90000] + "\n[TRUNCATED]"

    try:
        client = get_claude_client()
        resp = client.messages.create(
            model=DISTILL_MODEL,
            max_tokens=2500,
            system=BUILD_EXTRACTION_PROMPT,
            messages=[{"role": "user", "content": user_content}],
        )
        text = resp.content[0].text.strip()
    except Exception as e:
        print(f"  [WARN] Haiku call failed for task {task['gid']}: {e}")
        return None, False  # keep existing

    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        print(f"  [WARN] Haiku produced invalid JSON for task {task['gid']}: {e}")
        return None, False  # keep existing

    # Explicit "not a customer build" — caller should drop any prior record
    if data.get("is_customer_build") is False:
        reason = (data.get("reason") or "")[:300]
        print(f"    skip (not a customer build): {reason[:120]}")
        _FILTERED_THIS_SCAN.append({
            "kind": "build",
            "label": task.get("name", "")[:120],
            "gid": task.get("gid"),
            "reason": reason,
            "date": date.today().isoformat(),
        })
        return None, True

    data["asana_gid"] = task["gid"]
    if data.get("payment_state") not in PAYMENT_STATES:
        data["payment_state"] = (existing.payment_state if existing else "none")
    if data.get("build_state") not in BUILD_STATES:
        data["build_state"] = (existing.build_state if existing else "none")
    if data.get("ship_state") not in SHIP_STATES:
        data["ship_state"] = (existing.ship_state if existing else "none")
    data.pop("is_customer_build", None)
    data.pop("reason", None)
    try:
        return Build.from_dict(data), False
    except Exception as e:
        print(f"  [WARN] Build.from_dict failed for task {task['gid']}: {e}")
        return None, False  # keep existing


# Support case extraction — similar shape, anchored on support@ email threads
# (or Asana tasks if any exist in a future Support project).


SUPPORT_EXTRACTION_PROMPT = """\
You extract structured "SupportCase" records for Black Swift Technologies (BST).
A SupportCase is one customer-reported issue with a *delivered* BST device that
flows through: intake → diagnosing → RMA issued → received back → under repair
→ in QC → complete → shipped back to customer.

Inputs: current JSON record (may be empty), an email thread (one or more emails
from support@), and any related Slack messages.

FIRST: decide whether this email thread represents a real support case. Real
support cases involve a customer who already has a BST device that needs
diagnosis, repair, RMA, or troubleshooting. NOT real support cases:
  - Pre-sales technical inquiries ("what's the radio spec?", "what's the
    mounting interface?", "tell me about the autopilot architecture")
  - Quote / spec / capability requests from prospects
  - Partnership pitches, distributor inquiries, recruiting
  - General questions about BST products from someone who doesn't have one

If it's NOT a real support case, output exactly:
  {"is_real_support_case": false, "case_id": "<echo case_id>", "reason": "<1-sentence>"}
and stop.

Otherwise, set "is_real_support_case": true and produce the full schema below.

Produce ONE JSON object — the full updated SupportCase record. Output ONLY
valid JSON, no commentary, no markdown fences.

Schema:
{
  "case_id": "<keep existing or use the suggested id>",
  "asana_gid": null,
  "customer": "...",
  "customer_contact": "...",
  "customer_email": "...",
  "device": "SuperSwift S/N 2024-018" | null,
  "serial_number": "...",
  "reported_issue": "1-sentence summary of the problem",
  "state": "intake" | "diagnosing" | "rma_issued" | "received" | "under_repair" | "in_qc" | "complete" | "shipped",
  "rma_number": "...",
  "received_date": "YYYY-MM-DD" | null,
  "shipped_back_date": "YYYY-MM-DD" | null,
  "tracking_number": "...",
  "carrier": "...",
  "linked_build_gid": null,
  "owners": { "interface": "Beck", "support": "Nate", "invoicing": "Meredith" },
  "notes": "...",
  "missing_fields": [ "serial_number", "rma_number", ... ],
  "last_evidence_date": "YYYY-MM-DD"
}

Rules:
- state: only advance based on explicit evidence in the emails. "intake" =
  customer just reported an issue; "diagnosing" = BST is investigating;
  "rma_issued" = BST has sent an RMA #; "received" = unit is back at BST;
  "under_repair" = work in progress; "shipped" = sent back to customer.
- serial_number: look for patterns like "S/N", "SN", or year-NNN suffixes in
  email body/subject. Don't fabricate.
- missing_fields: list things needed to move the case forward (serial_number
  for diagnosing, rma_number for an issued RMA, tracking_number when shipping).
- Be conservative. If unsure, leave fields null.
- NEVER fabricate. If the customer's identity can't be determined, leave blank.
"""


def _haiku_extract_support_case(thread_emails: list[dict], existing: Optional[SupportCase],
                                slack_msgs: list[dict], case_id: str) -> tuple[Optional[SupportCase], bool]:
    """Returns (case, drop_existing). Mirrors _haiku_extract_build:
      (SupportCase, False) — normal update; save and use.
      (None,        True)  — Haiku said is_real_support_case=false; drop any prior file.
      (None,        False) — Haiku failed transiently; keep existing record intact.
    """
    existing_json = existing.to_dict() if existing else {"case_id": case_id, "asana_gid": None}

    email_blocks = []
    for e in thread_emails:
        att_str = ""
        if e.get("attachments"):
            att_str = " attachments=" + ", ".join(a["name"] for a in e["attachments"][:5])
        email_blocks.append(
            f"--- EMAIL [{e.get('mailbox','')}] {e.get('date','')} "
            f"from {e.get('from','')} → {e.get('to','')}{att_str}\n"
            f"Subject: {e.get('subject','')}\n"
            f"{(e.get('body') or e.get('snippet') or '')[:2500]}"
        )

    slack_blocks = [
        f"--- SLACK {m.get('date','')} {m.get('text','')[:500]}" for m in slack_msgs
    ]

    user_content = (
        f"CURRENT JSON RECORD:\n{json.dumps(existing_json, indent=2)}\n\n"
        + ("EMAIL THREAD:\n" + "\n\n".join(email_blocks) + "\n\n" if email_blocks else "")
        + ("RECENT SLACK:\n" + "\n".join(slack_blocks) + "\n\n" if slack_blocks else "")
        + f"Suggested case_id if creating new: {case_id}\n"
        + "Produce the updated JSON SupportCase record now."
    )
    if len(user_content) > 90000:
        user_content = user_content[:90000] + "\n[TRUNCATED]"

    try:
        client = get_claude_client()
        resp = client.messages.create(
            model=DISTILL_MODEL,
            max_tokens=2000,
            system=SUPPORT_EXTRACTION_PROMPT,
            messages=[{"role": "user", "content": user_content}],
        )
        text = resp.content[0].text.strip()
    except Exception as e:
        print(f"  [WARN] Haiku call failed for support thread: {e}")
        return None, False  # keep existing

    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        print(f"  [WARN] Haiku invalid JSON for support: {e}")
        return None, False  # keep existing

    if data.get("is_real_support_case") is False:
        reason = (data.get("reason") or "")[:300]
        print(f"    skip (not a real support case): {reason[:120]}")
        # Label this filtered case with the customer/subject info we have
        first_email = thread_emails[0] if thread_emails else {}
        label = first_email.get("from", "") or first_email.get("subject", "") or case_id
        _FILTERED_THIS_SCAN.append({
            "kind": "support",
            "label": label[:120],
            "gid": None,
            "reason": reason,
            "date": date.today().isoformat(),
        })
        return None, True

    if data.get("state") not in SUPPORT_STATES:
        data["state"] = (existing.state if existing else "intake")
    data.setdefault("case_id", case_id)
    data.pop("is_real_support_case", None)
    data.pop("reason", None)
    try:
        return SupportCase.from_dict(data), False
    except Exception as e:
        print(f"  [WARN] SupportCase.from_dict failed: {e}")
        return None, False  # keep existing


# ---------------------------------------------------------------------------
# Support thread grouping
# ---------------------------------------------------------------------------


def _group_support_threads(support_emails: list[dict]) -> dict[str, list[dict]]:
    """Group support@ emails into threads by external sender + subject root.

    A "thread" here is loosely all support@ messages from the same external
    address with the same normalized subject (ignoring Re:/Fwd: prefixes).
    Phase 1 doesn't try to use Gmail thread IDs because internal forwards
    (Beck → support@) split a single conversation into separate Gmail threads.
    """
    threads: dict[str, list[dict]] = defaultdict(list)
    for e in support_emails:
        sender = e.get("from") or ""
        # Use the *external* party as the thread anchor — if the email is
        # FROM an internal BST address, look at the TO header for the customer
        if _is_internal(sender):
            customer_addr = ""
            for addr_field in ("to", "cc"):
                v = e.get(addr_field) or ""
                for m in re.finditer(r"<([^>]+)>|([\w.+-]+@[\w.-]+)", v):
                    candidate = (m.group(1) or m.group(2) or "").strip()
                    if candidate and not _is_internal(candidate):
                        customer_addr = candidate
                        break
                if customer_addr:
                    break
            sender = customer_addr or sender
        else:
            # Pull the bare email out of "Name <addr@domain>"
            m = re.search(r"<([^>]+)>", sender)
            if m:
                sender = m.group(1)
        sender = sender.lower().strip()

        # Normalize subject root
        subj = (e.get("subject") or "").lower()
        subj_root = re.sub(r"^(?:re:|fwd?:|fw:)\s*", "", subj).strip()[:120]

        if not sender:
            continue
        key = f"{sender}::{subj_root}"
        threads[key].append(e)

    # Sort each thread oldest→newest
    for key in threads:
        threads[key].sort(key=lambda e: e.get("date") or "")
    return threads


def _suggest_support_case_id(thread_emails: list[dict]) -> str:
    """Generate a stable case_id like SC-2026-<seq> from the oldest email date."""
    if not thread_emails:
        return f"SC-{date.today().year}-000"
    oldest = thread_emails[0]
    year = (oldest.get("date") or "")[:4] or str(date.today().year)
    # Short stable hash of the from+subject so re-scans produce the same id
    seed = f"{oldest.get('from','')}|{oldest.get('subject','')}"
    h = abs(hash(seed)) % 1000
    return f"SC-{year}-{h:03d}"


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------


def _write_unmapped_customers(emails_by_domain: dict[str, list[dict]],
                              known_tokens: set[str]) -> Path:
    """Write a markdown report of email-domain customers who aren't yet in Asana."""
    CS_KNOWLEDGE_DIR.mkdir(parents=True, exist_ok=True)
    path = CS_KNOWLEDGE_DIR / "_unmapped_customers.md"

    lines = [
        "# Unmapped Customers",
        "",
        f"_Generated {datetime.now().strftime('%Y-%m-%d %H:%M')} — customers who have "
        f"emailed info@/sales@ but aren't yet tracked as Asana Commercial Sales tasks._",
        "",
    ]
    rows = []
    for domain, emails in sorted(emails_by_domain.items()):
        emails.sort(key=lambda e: e.get("date") or "", reverse=True)
        latest = emails[0].get("date") or "?"
        subjects = list({(e.get("subject") or "")[:80] for e in emails[:5]})
        # Skip if any token from the domain shows up in Asana customer tokens
        dom_tokens = set(re.split(r"[.\-_]", domain.split(".")[0]))
        if any(t in known_tokens for t in dom_tokens if len(t) >= 4):
            continue
        rows.append((latest, domain, len(emails), subjects))

    if not rows:
        lines.append("_None — all email customers match an existing Asana task._")
    else:
        rows.sort(reverse=True)
        lines.append("| Latest | Domain | # Emails | Recent subjects |")
        lines.append("|--------|--------|----------|-----------------|")
        for latest, domain, count, subjects in rows[:60]:
            subj_str = " · ".join(subjects[:3])[:200]
            lines.append(f"| {latest} | {domain} | {count} | {subj_str} |")

    path.write_text("\n".join(lines))
    return path


def _write_filtered_log() -> Optional[Path]:
    """Persist this scan's filter decisions to _filtered.md.

    Existing entries are preserved across scans (a task that flickers in and out
    of the filter retains its earlier reasons). Used by future Phase 2 features:
      - "Show me filtered builds" query
      - "Force-include this opportunity" override
    """
    path = CS_KNOWLEDGE_DIR / "_filtered.md"
    # Read existing entries (by gid for builds, by label for support)
    existing_builds: dict[str, dict] = {}
    existing_support: list[dict] = []
    if path.exists():
        try:
            for line in path.read_text().splitlines():
                # Lines of shape: | gid | YYYY-MM-DD | label | reason |
                if line.startswith("| ") and " | " in line and not line.startswith("|---"):
                    cells = [c.strip() for c in line.split(" | ")]
                    # Skip the header row
                    if len(cells) >= 5 and cells[1] not in ("Gid", "Date"):
                        gid = cells[1].strip("`")
                        existing_builds.setdefault(gid, {
                            "gid": gid if gid else None,
                            "date": cells[2],
                            "label": cells[3],
                            "reason": cells[4].rstrip(" |"),
                        })
        except Exception:
            pass

    # Merge this scan's decisions
    new_builds = [f for f in _FILTERED_THIS_SCAN if f["kind"] == "build"]
    new_support = [f for f in _FILTERED_THIS_SCAN if f["kind"] == "support"]
    for f in new_builds:
        gid = f.get("gid") or ""
        existing_builds[gid] = {
            "gid": f.get("gid"),
            "date": f["date"],
            "label": f["label"],
            "reason": f["reason"],
        }

    lines = [
        "# Commercial Sales — Filtered-out Opportunities",
        "",
        "_Tasks and email threads Haiku flagged as NOT a customer build / NOT a real support case._",
        "_Use this to spot anything that was filtered too aggressively. To force-include a build,_",
        "_reply in #commercial-sales with `track this: <customer or gid>` (Phase 2 feature)._",
        "",
        f"_Last updated {datetime.now().strftime('%Y-%m-%d %H:%M')}._",
        "",
        "## Builds filtered out of the digest",
        "",
        "| Gid | Date | Asana task | Reason |",
        "|-----|------|------------|--------|",
    ]
    for entry in sorted(existing_builds.values(), key=lambda e: e.get("date") or "", reverse=True):
        gid_cell = f"`{entry['gid']}`" if entry.get("gid") else "—"
        lines.append(f"| {gid_cell} | {entry.get('date','')} | {entry.get('label','')[:80]} | {entry.get('reason','')[:200]} |")

    if new_support:
        lines.extend([
            "",
            "## Email threads filtered out of support pipeline",
            "",
            "_Pre-sales technical inquiries, capability questions, marketing pitches — not real support cases._",
            "",
            "| Date | From / Subject | Reason |",
            "|------|----------------|--------|",
        ])
        for f in new_support:
            lines.append(f"| {f.get('date','')} | {f.get('label','')[:80]} | {f.get('reason','')[:200]} |")

    path.write_text("\n".join(lines))
    return path


def _write_index(builds: list[Build], cases: list[SupportCase]) -> Path:
    """Write a human-readable markdown index of all tracked records."""
    CS_KNOWLEDGE_DIR.mkdir(parents=True, exist_ok=True)
    path = CS_KNOWLEDGE_DIR / "_index.md"

    lines = [
        "# Commercial Sales — Pipeline Index",
        "",
        f"_Last scanned {datetime.now().strftime('%Y-%m-%d %H:%M')}_",
        "",
        f"## Builds ({len(builds)})",
        "",
        "| Customer | Receive By | Payment | Build | Ship | Asana |",
        "|----------|------------|---------|-------|------|-------|",
    ]
    for b in builds:
        lines.append(
            f"| {b.customer or '?'} | {b.receive_by or '—'} | "
            f"{b.payment_state} | {b.build_state} | {b.ship_state} | `{b.asana_gid}` |"
        )

    lines.extend([
        "",
        f"## Support Cases ({len(cases)})",
        "",
        "| Case | Customer | Device | State |",
        "|------|----------|--------|-------|",
    ])
    for c in cases:
        lines.append(
            f"| {c.case_id} | {c.customer or '?'} | "
            f"{c.device or '?'} | {c.state} |"
        )

    path.write_text("\n".join(lines))
    return path


def scan_all(mode: str = "incremental", slack_client=None) -> dict:
    """Run the commercial sales scanner.

    Args:
        mode: 'full', '1yr', or 'incremental' — controls email window
        slack_client: optional Slack WebClient for #commercial-sales history

    Returns dict with counts: {builds, support, unmapped_domains, mode}
    """
    CS_KNOWLEDGE_DIR.mkdir(parents=True, exist_ok=True)
    BUILDS_DIR.mkdir(parents=True, exist_ok=True)
    SUPPORT_DIR.mkdir(parents=True, exist_ok=True)

    # Reset the filter accumulator — populated as Haiku flags drops during scan.
    _FILTERED_THIS_SCAN.clear()

    # Email window depends on mode (incremental ≈ since last scan + slack)
    if mode == "full":
        days = 365
    elif mode == "1yr":
        days = 365
    else:
        last = get_last_scan("commercial_sales")
        if last:
            days = max(7, (datetime.now() - last).days + 2)
        else:
            days = EMAIL_WINDOW_DAYS

    print(f"\n[commercial_sales] Email window: last {days} days")

    # 1. Find Asana project
    project = _find_commercial_sales_project()
    if not project:
        print("  [ERROR] Could not find Commercial Sales project in Asana. "
              "Set ASANA_COMMERCIAL_SALES_PROJECT_GID or create a project with "
              "'Commercial Sales' in its name.")
        return {"builds": 0, "support": 0, "unmapped_domains": 0, "mode": mode}

    print(f"  Asana project: {project.get('name')} ({project.get('gid')})")
    asana_tasks = _fetch_commercial_sales_tasks(project["gid"])
    print(f"  Fetched {len(asana_tasks)} Commercial Sales tasks")

    # 2. Pull emails for each shared address from the admin mailbox
    # (info@/sales@/support@ are distribution groups, not directly impersonable —
    # see SHARED_ADDRESSES comment).
    all_emails: list[dict] = []
    emails_by_mailbox: dict[str, list[dict]] = {}
    for shared in SHARED_ADDRESSES:
        query = _build_shared_address_query(shared, days)
        msgs = _fetch_admin_query_emails(query, shared, cap=EMAILS_PER_MAILBOX_CAP)
        # De-dup against earlier shared addresses (a customer can be CC'd on
        # info@ AND sales@ at once; same gmail message id either way)
        seen_ids = {e["id"] for e in all_emails}
        new_msgs = [m for m in msgs if m["id"] not in seen_ids]
        emails_by_mailbox[shared] = new_msgs
        print(f"  {shared}: {len(new_msgs)} emails ({len(msgs) - len(new_msgs)} dup)")
        all_emails.extend(new_msgs)
    # Newest first
    all_emails.sort(key=lambda e: e.get("date") or "", reverse=True)
    sales_info_emails = [
        e for e in all_emails if e.get("mailbox") in (
            "sales@blackswifttech.com", "info@blackswifttech.com",
        )
    ]
    support_emails = emails_by_mailbox.get("support@blackswifttech.com", [])

    # 3. Slack history — #commercial-sales (primary) + bounded extra channels
    slack_msgs: list[dict] = []
    if slack_client:
        channel_id = _find_commercial_sales_channel(slack_client)
        if channel_id:
            primary = _fetch_slack_history(
                slack_client, channel_id, SLACK_WINDOW_DAYS,
                channel_name="commercial-sales",
            )
            print(f"  Slack #commercial-sales: {len(primary)} messages")
            slack_msgs.extend(primary)
        else:
            print("  [WARN] Could not resolve #commercial-sales channel")
        # Extra channels (flight-testing, operations, general) for post-delivery
        # and ops-coordination signal. Bounded per channel.
        slack_msgs.extend(_fetch_extra_slack_history(slack_client))

    # 4. For each Asana task, extract/update a Build via Haiku
    existing_builds = {b.asana_gid: b for b in load_builds()}
    all_customer_tokens: set[str] = set()
    new_builds: list[Build] = []

    dropped_gids: list[str] = []
    for i, task in enumerate(asana_tasks):
        print(f"  [{i + 1}/{len(asana_tasks)}] {task.get('name','?')[:60]}")
        tokens = _customer_tokens(task)
        all_customer_tokens.update(tokens)
        matched_emails = _filter_emails_for_tokens(
            sales_info_emails, tokens, EVIDENCE_EMAILS_PER_BUILD
        )
        matched_slack = _filter_slack_for_tokens(
            slack_msgs, tokens, EVIDENCE_SLACK_PER_BUILD
        )
        # Knowledge-file evidence: QBO invoices, contacts, project registry.
        # Customer name from existing record if we have one; otherwise infer
        # from the task name + custom fields via the same logic Haiku uses.
        existing_record = existing_builds.get(task["gid"])
        customer_hint = existing_record.customer if existing_record else ""
        customer_email_hint = existing_record.customer_email if existing_record else None
        if not customer_hint:
            # Best-effort guess from custom fields
            for cf in task.get("custom_fields") or []:
                if cf and (cf.get("name") or "").lower() in (
                    "customer", "organization/customer", "full name of entity"
                ) and cf.get("display_value"):
                    customer_hint = cf["display_value"]
                    break
        if not customer_hint:
            customer_hint = task.get("name", "")
        project_code = _extract_project_code_from_task(task)
        evidence = _gather_knowledge_evidence(customer_hint, project_code)

        # Bounded per-customer direct email search on admin mailbox (Fix 3b).
        # Catches direct correspondence (e.g. Beck ↔ customer) that doesn't
        # route through info@/sales@/support@.
        direct_emails = _fetch_direct_customer_emails(customer_hint, customer_email_hint)
        if direct_emails:
            # Merge with matched_emails, dedup by Gmail id, newest first, cap
            seen = {e["id"] for e in matched_emails}
            for e in direct_emails:
                if e["id"] not in seen:
                    matched_emails.append(e)
                    seen.add(e["id"])
            matched_emails.sort(key=lambda e: e.get("date") or "", reverse=True)
            matched_emails = matched_emails[:EVIDENCE_EMAILS_PER_BUILD + PER_BUILD_DIRECT_EMAIL_CAP]

        existing = existing_record
        updated, drop_existing = _haiku_extract_build(
            task, existing, matched_emails, matched_slack, knowledge_evidence=evidence
        )
        if updated is not None:
            # Stamp the Asana task name so the renderer can disambiguate
            # same-customer cards via the subtitle.
            updated.asana_task_name = task.get("name") or None
        if updated:
            save_build(updated)
            new_builds.append(updated)
            time.sleep(0.3)  # gentle pacing for Anthropic
        elif drop_existing:
            # Haiku explicitly said this isn't a customer build — delete any
            # stale JSON file for it so it stops appearing in the digest.
            stale = BUILDS_DIR / f"{task['gid']}.json"
            if stale.exists():
                stale.unlink()
            dropped_gids.append(task["gid"])
        else:
            # Transient Haiku failure — preserve prior record if we had one
            if existing:
                new_builds.append(existing)

    # 5. Support cases — group support@ threads, one Haiku call per thread
    existing_cases = {c.case_id: c for c in load_support_cases()}
    threads = _group_support_threads(support_emails)
    new_cases: list[SupportCase] = []

    print(f"  Grouping support@ into threads: {len(threads)} candidate threads")
    for thread_key, thread_emails in threads.items():
        if not thread_emails:
            continue
        # Skip noise: threads with only internal senders and no obvious customer
        first = thread_emails[0]
        if _is_internal(first.get("from", "")) and not first.get("to"):
            continue
        case_id = _suggest_support_case_id(thread_emails)
        existing = existing_cases.get(case_id)
        # Match Slack messages to this thread's customer tokens (best effort)
        customer_addr = first.get("from", "")
        sender_dom = _sender_domain(customer_addr)
        tokens = set()
        if sender_dom and sender_dom not in INTERNAL_DOMAINS:
            tokens.add(sender_dom.split(".")[0])
        if first.get("subject"):
            for tok in re.sub(r"[^\w\s]", " ", first["subject"].lower()).split():
                if len(tok) >= 4 and not tok.isdigit():
                    tokens.add(tok)
        matched_slack = _filter_slack_for_tokens(slack_msgs, tokens, EVIDENCE_SLACK_PER_BUILD)

        updated, drop_existing = _haiku_extract_support_case(
            thread_emails[-EVIDENCE_EMAILS_PER_BUILD:],
            existing,
            matched_slack,
            case_id,
        )
        if updated:
            save_support(updated)
            new_cases.append(updated)
            time.sleep(0.3)
        elif drop_existing:
            stale = SUPPORT_DIR / f"{case_id}.json"
            if stale.exists():
                stale.unlink()
        elif existing:
            # Transient Haiku failure — preserve prior record
            new_cases.append(existing)

    # 6. Unmapped customers report
    emails_by_domain: dict[str, list[dict]] = defaultdict(list)
    for e in sales_info_emails:
        dom = _sender_domain(e.get("from", ""))
        if dom and dom not in INTERNAL_DOMAINS:
            emails_by_domain[dom].append(e)
    _write_unmapped_customers(emails_by_domain, all_customer_tokens)

    # 7. Index + filter log
    _write_index(new_builds, new_cases)
    _write_filtered_log()

    update_scan_timestamp("commercial_sales")

    return {
        "builds": len(new_builds),
        "support": len(new_cases),
        "unmapped_domains": len(emails_by_domain),
        "mode": mode,
    }
