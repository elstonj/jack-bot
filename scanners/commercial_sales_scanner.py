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
from google_client import _get_credentials, search_calendar_events
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
    merge_builds_by_invoice,
    merge_build_cluster,
    is_stale_lead,
    is_order,
    STALE_LEAD_DAYS,
    _norm_invoice,
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
    """Return [{name, mime, size, attachment_id}] for each attachment (file-only, no inline).

    attachment_id lets us later fetch the actual bytes via
    `service.users().messages().attachments().get(...)` — kept lazy so we
    only pay for the PDFs we actually use as evidence on a Build.
    """
    out = []

    def walk(p):
        filename = p.get("filename") or ""
        mime = p.get("mimeType") or ""
        body = p.get("body") or {}
        size = body.get("size") or 0
        attachment_id = body.get("attachmentId") or ""
        if filename and size > 1000:  # skip tiny inline parts
            out.append({
                "name": filename,
                "mime": mime,
                "size": size,
                "attachment_id": attachment_id,
            })
        for sub in p.get("parts") or []:
            walk(sub)

    walk(payload)
    return out


# --- PDF document handling --------------------------------------------------
# Customer-facing invoices/estimates/quotes/POs sit on customer-thread emails
# as PDF attachments. Fetching their bytes and passing them to Haiku as
# document content blocks lets the extraction fill in ship_to, line items,
# and dollar amounts that text bodies don't carry. Bounded by per-Build caps
# to keep cost predictable.

# Filename substrings that strongly suggest a financial/order doc.
PDF_INTEREST_KEYWORDS = (
    "invoice", "estimate", "quote", "pricing",
    "purchase order", "order confirmation", "sales order",
)
# Additional regex patterns for tokens like "PO" that need word-boundary care
# so we don't match unrelated filenames containing "po" as a substring.
PDF_INTEREST_REGEXES = (
    re.compile(r"\bpo\b", re.IGNORECASE),       # "PO J20265067", "PO-1234"
    re.compile(r"\bp\.o\.", re.IGNORECASE),     # "P.O. 1234"
)
PDF_MAX_BYTES_PER_DOC = 5 * 1024 * 1024   # skip PDFs >5 MB (cost guard)
PDF_MAX_DOCS_PER_BUILD = 3                # per Haiku call
PDF_MAX_TOTAL_BYTES_PER_BUILD = 8 * 1024 * 1024


def _is_interesting_pdf(attachment: dict) -> bool:
    """Decide whether this attachment is a PDF worth fetching as evidence."""
    fn_lower = (attachment.get("name") or "").lower()
    fn_orig = attachment.get("name") or ""
    mime = (attachment.get("mime") or "").lower()
    size = attachment.get("size") or 0
    if not (mime == "application/pdf" or fn_lower.endswith(".pdf")):
        return False
    if size > PDF_MAX_BYTES_PER_DOC:
        return False
    if any(kw in fn_lower for kw in PDF_INTEREST_KEYWORDS):
        return True
    return any(rx.search(fn_orig) for rx in PDF_INTEREST_REGEXES)


def _candidate_invoice_numbers(filename: str) -> list[str]:
    """Pull every plausible invoice-number-like digit run from a PDF filename.

    Returns a list (preserving order) of digit runs of length 4-8 that aren't
    obvious years. Lets the caller try each against QBO since some filenames
    contain multiple numbers (e.g. "PO J20265067 - Invoice 1754.pdf").

    Uses non-word-character separators rather than `\\b` because `\\b` treats
    underscore as a word char, breaking patterns like "invoice_1754.pdf".
    """
    if not filename:
        return []
    out = []
    # (?<![0-9]) ... (?![0-9]) is a hand-rolled boundary that ignores _ and -
    for m in re.finditer(r"(?<![0-9])(\d{4,8})(?![0-9])", filename):
        n = m.group(1)
        # Skip obvious years
        if len(n) == 4 and 1900 <= int(n) <= 2099:
            continue
        out.append(n)
    return out


def _qbo_project_hint_for_pdf(filename: str) -> Optional[str]:
    """If a PDF's filename references a QBO invoice number, return the project
    line that invoice was billed to (e.g. '[043-3] By Light Halo'). None when
    no match — Haiku then has only the filename + email context to work with.

    QBO customer strings already carry the project-code prefix when applicable,
    so the project alignment falls out for free.
    """
    candidates = _candidate_invoice_numbers(filename)
    if not candidates:
        return None
    invoices = _load_qbo_invoices()
    for cand in candidates:
        stripped = cand.lstrip("0")
        for inv in invoices:
            num = inv.get("number", "").lstrip("0")
            if num and num == stripped:
                return inv.get("customer")
    return None


def _fetch_pdf_bytes(service, msg_id: str, attachment_id: str) -> Optional[bytes]:
    """Pull a Gmail attachment's raw bytes. Returns None on any failure."""
    if not (service and msg_id and attachment_id):
        return None
    try:
        att = service.users().messages().attachments().get(
            userId="me", messageId=msg_id, id=attachment_id,
        ).execute()
    except Exception as e:
        print(f"  [WARN] PDF fetch failed for msg {msg_id}: {e}")
        return None
    data = att.get("data")
    if not data:
        return None
    try:
        return base64.urlsafe_b64decode(data + "===")
    except Exception:
        return None


def _collect_pdf_docs_for_build(service, emails: list[dict]) -> list[dict]:
    """Across the emails picked for a Build, fetch up to PDF_MAX_DOCS_PER_BUILD
    interesting PDF attachments and return them as Anthropic document content
    blocks ready to drop into the messages list.

    Newest emails are inspected first. Stops at the per-Build doc and byte caps.
    """
    if not service or not emails:
        return []
    sorted_emails = sorted(emails, key=lambda e: e.get("date") or "", reverse=True)
    docs: list[dict] = []
    total_bytes = 0
    for e in sorted_emails:
        for att in (e.get("attachments") or []):
            if len(docs) >= PDF_MAX_DOCS_PER_BUILD:
                return docs
            if not _is_interesting_pdf(att):
                continue
            blob = _fetch_pdf_bytes(service, e.get("id", ""), att.get("attachment_id", ""))
            if not blob:
                continue
            if total_bytes + len(blob) > PDF_MAX_TOTAL_BYTES_PER_BUILD:
                return docs
            total_bytes += len(blob)
            b64 = base64.standard_b64encode(blob).decode("ascii")
            qbo_hint = _qbo_project_hint_for_pdf(att.get("name", ""))
            context = (
                f"Attachment '{att.get('name','')}' from email dated "
                f"{e.get('date','')} ({e.get('mailbox','')}), "
                f"subject: {e.get('subject','')[:120]}"
            )
            if qbo_hint:
                context += (
                    f". QBO records this invoice/document under project line "
                    f"'{qbo_hint}'. If that line doesn't match the current Build, "
                    f"treat the PDF as background reference only — do NOT extract "
                    f"items, ship_to, or amounts from it for this Build."
                )
            docs.append({
                "type": "document",
                "source": {
                    "type": "base64",
                    "media_type": "application/pdf",
                    "data": b64,
                },
                "title": att.get("name", "")[:80],
                "context": context,
            })
    return docs


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
    """Extract DISTINCTIVE tokens we can match emails/slack against for one
    Asana task.

    Filters out generic words like "university", "research", "national" —
    without this, a Michigan Tech task matches every email mentioning any
    university, and the per-Build evidence gets flooded with noise.
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
    return tokens - GENERIC_CUSTOMER_TOKENS


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

    Token matching filters out generic words ("university", "research", "national",
    "laboratory", etc.) before comparing — without this, "Michigan Technological
    University" matches Stanford / Embry-Riddle / UMD / etc. on the shared
    "university" token and causes Haiku to falsely conclude a QBO invoice exists.
    """
    invoices = _load_qbo_invoices()
    if not invoices:
        return []
    # Distinctive customer tokens — strip generic words to avoid false matches
    # on common nouns shared across customers.
    customer_tokens = _tokens_for_match(customer) - GENERIC_CUSTOMER_TOKENS
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
        # Token overlap on *distinctive* tokens only (length >= 4, not generic).
        if customer_tokens:
            inv_tokens = _tokens_for_match(inv_cust) - GENERIC_CUSTOMER_TOKENS
            if customer_tokens & inv_tokens:
                matched.append(inv)
                seen.add(key)
                continue
        # Substring fallback for short / single-word customer names
        # ("ByLight" → "By Light"). Skipped when customer has no distinctive
        # tokens left after filtering — otherwise "research" would match
        # any customer with "research" in the name.
        if customer and len(customer) >= 4 and customer_tokens:
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
  - (Possibly) PDF attachments from those emails — typically invoices,
    estimates, quotes, or POs. These are the source documents for
    ship-to address, itemized line items, dollar amounts, and invoice
    numbers. Read them as authoritative for those fields. IMPORTANT:
    each PDF's `context` says which BST project line QBO has it under
    (e.g. "project line '[043-3] By Light Halo'"). If that project line
    is clearly different from the current Asana task / Build (e.g. the
    task is "ByLight Mustang Follow-on" but the PDF is for "[043-3] By
    Light Halo"), treat the PDF as background only and DO NOT extract
    items, ship_to, or amounts from it. When in doubt, prefer NOT to
    populate fields rather than carrying over data from a sibling
    project — the missing-info callout will prompt humans to fill in.

Produce ONE JSON object as your reply — a complete updated Build record. Output
ONLY valid JSON, no commentary, no markdown fences.

FIRST: decide whether this Asana task represents a real, ACTIVE customer
build worth surfacing in tomorrow's #commercial-sales digest. If NOT, output:
  {"is_customer_build": false, "asana_gid": "<gid>", "reason": "<1-sentence>"}
and stop. Otherwise output is_customer_build=true and the full schema below.

Decision tree — evaluate in THIS order, first match wins:

STEP 0 (HARD DROP — no carve-outs). If ALL of these are true, the BST team
has explicitly closed this opportunity at $0 value. The QBO invoices you
see in the evidence belong to a DIFFERENT task for the same customer
entity. DROP without exception:
  • Asana custom field "Next Steps (Sales)" is "Closed", "Lost", or
    "No action needed"
  • Asana custom field "Closed Value" is "0.00" or "$0.00"
  • Asana custom field "Estimated/Quoted Value" is "0.00" or "$0.00"
If you find these three together, drop and cite all three in `reason`. Do
NOT keep on the basis of QBO invoices for the customer entity — those
belong to a different task.

STEP 0B (FUNDING-PROPOSAL DROP — overrides the STEP 1 KEEP signals). This is a
commercial-HARDWARE pipeline. If the opportunity is a formal funding proposal —
BST responding to a solicitation to win a research/development award or grant
(SBIR, STTR, BAA, RFP, RFI, LOI / letter of intent, white paper, topic response,
IDIQ bid, "preparing a cost breakdown / proposal for a competitive bid", or
selection "via open competitive bid") — it does NOT belong in this digest; it's
tracked separately in #grants-and-funding. DROP it even when there is recent
email/Slack activity (proposal prep is noisy) or a future receive_by date. Cite
reason "funding proposal — belongs in #grants-and-funding".

This does NOT apply to commercial hardware procurement, which is a KEEP even when
the customer is a government agency or the money is grant-funded. A purchase
order, an RFQ/quote for specific aircraft or sensors, an invoice for hardware, or
a system sale are all commercial. The test: are we *selling a product/system*
(KEEP) or *bidding to win a funded R&D effort* (DROP)?

STEP 1 (KEEP overrides — only when Step 0 and Step 0B didn't fire). If ANY of these is
true, KEEP the build regardless of what other Asana custom fields say. These are the load-bearing signals
that "BST has skin in the game":
  • A QBO invoice exists that corresponds to THIS task's product/scope (paid
    or unpaid). BST is on the hook to deliver or to collect. Stale Asana
    fields, "Closed" statuses, and $0 closed-values are all overridden by an
    actual QBO invoice for this order. ERAU-style "paid but legal settlement
    pending" is KEEP.
    CRITICAL: the invoice must match THIS task's order — same product line /
    system / campaign — not merely the same customer entity. A customer can
    have several distinct orders; a paid invoice for a DIFFERENT, already-
    delivered order (e.g. a refurbished S2 shipped last year) does NOT keep an
    unrelated, never-advanced estimate alive, and must NOT be cited in `notes`
    as justification for this record. When the only invoice on the account is
    for a different deliverable, treat this task on its own merits (Step 2).
    NOTE: when QBO INVOICES evidence is provided above, use those entries — if
    1+ rows plausibly reference THIS task's product/scope, KEEP.
  • Substantive email/Slack activity in the last 90 days about this specific
    customer (not generic newsletter / partner traffic). Implies live
    engagement even when Asana hasn't been updated.
  • An explicit receive_by date in the future within the next 6 months
    (someone is on the hook for a near-term delivery).

STEP 2 (DROP signals). If none of the KEEP overrides apply, drop when ANY
of these is true:
  (a) Task is an internal action item ("Send slides", "Cleanup deck",
      "Develop concept", "Internal review") — no customer-facing scope.
  (b) Asana custom field "Next Steps (Sales)" is "Lost", "Closed", or
      "No action needed".
  (c) Asana custom field "Closed Value" is "0.00" or "$0.00".
  (d) Asana custom field "Lead Response" is "No Response".
  (e) STALE: last contact in Asana > 6 months ago AND no recent email/Slack
      activity. Having a filled-in customer_email or detailed Sales Notes
      from a year+ ago is NOT engagement — engagement means recent traffic.

The DROP rules apply by default to anything not caught by STEP 1. Cold
leads with no traction are excluded — the user trusts real opportunities
will pop back in once they get traction (recent email/Slack/QBO).

When dropping, the `reason` should cite the specific signal (custom field
value, days since last contact, lack of QBO match). When keeping despite
a "Closed" Asana field, the `reason` block isn't needed but `notes` should
mention which KEEP signal applied (e.g. "kept due to QBO invoice 1667").

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
- items: when an invoice/estimate/quote PDF is attached, read the line items
  out of the PDF directly. Otherwise parse from email subject lines and
  quoted body text. Filename alone (no content) is not enough to invent items.
- ship_to: when an invoice/estimate PDF carries a Bill-To / Ship-To block,
  use the Ship-To address verbatim (multi-line OK). Otherwise leave as-is.
- invoice_number / invoice_amount: read from the invoice PDF when present;
  otherwise rely on QBO INVOICES evidence above.
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
                         knowledge_evidence: str = "",
                         gmail_service=None,
                         force_include: bool = False) -> tuple[Optional[Build], bool]:
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

    # Fetch up to PDF_MAX_DOCS_PER_BUILD interesting PDF attachments
    # (invoices/estimates/quotes) from the picked emails. Bounded by per-Build
    # doc + byte caps. Empty list if no PDFs match or no service available.
    pdf_docs = _collect_pdf_docs_for_build(gmail_service, emails)
    pdf_note = ""
    if pdf_docs:
        names = ", ".join(d.get("title", "") for d in pdf_docs)[:300]
        pdf_note = (
            f"\nPDF ATTACHMENTS PROVIDED (read for ship-to address, line items, "
            f"dollar amounts, invoice/estimate numbers): {names}\n"
        )

    force_note = ""
    if force_include:
        force_note = (
            "\nFORCE-INCLUDE OVERRIDE: a BST team member has explicitly told the "
            "bot to track this build in the digest. SKIP the is_customer_build "
            "filter (Step 0 hard-drop and Step 2 drop signals). Always return "
            "`is_customer_build: true`. Still produce the full structured "
            "record — just don't filter it out.\n"
        )

    user_content = (
        "CURRENT JSON RECORD:\n"
        f"{json.dumps(existing_json, indent=2)}\n\n"
        + (knowledge_evidence + "\n\n" if knowledge_evidence else "")
        + f"{task_block}\n\n"
        + ("RECENT EMAILS:\n" + "\n\n".join(email_blocks) + "\n\n" if email_blocks else "")
        + ("RECENT SLACK:\n" + slack_note + "\n".join(slack_blocks) + "\n\n" if slack_blocks else "")
        + pdf_note
        + force_note
        + "Produce the updated JSON Build record now."
    )

    # Cap user_content
    if len(user_content) > 90000:
        user_content = user_content[:90000] + "\n[TRUNCATED]"

    # Build the message content list. When PDFs are present we use the multi-
    # block format; otherwise stay with the single string for simplicity.
    if pdf_docs:
        message_content = pdf_docs + [{"type": "text", "text": user_content}]
    else:
        message_content = user_content

    try:
        client = get_claude_client()
        resp = client.messages.create(
            model=DISTILL_MODEL,
            max_tokens=2500,
            system=BUILD_EXTRACTION_PROMPT,
            messages=[{"role": "user", "content": message_content}],
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


# --- Dedup & stale-lead pass -----------------------------------------------
# The scanner anchors one Build per Asana task gid, so two Asana tasks for the
# same physical order produce two records that the manual "delete the JSON"
# approach can't fix (the next scan re-creates them). This pass collapses true
# duplicates and retires cold leads automatically, every run:
#   a. deterministic merge of records sharing an invoice number (shared with
#      the digest renderer via commercial_sales.merge_builds_by_invoice)
#   b. product-aware Haiku clustering for invoice-less duplicates
#   c. stale-lead retirement (commercial_sales.is_stale_lead)
# Everything removed is unlink()ed on disk and logged to _filtered.md (so it's
# visible via `show filtered` and recoverable via `track this:`).

CLUSTER_DEDUP_SYSTEM = """\
You are deduplicating commercial-sales order records. You are given 2+ Build
records whose customer names are similar. Some pairs are the SAME physical
order entered as two Asana tasks; others are GENUINELY DISTINCT orders for the
same/related customer (different product line, different department, different
campaign, a separate follow-on order).

Group ONLY records that are the same physical order. The SAME order requires
BOTH (a) the same buyer — same customer CONTACT / person / PI / department /
integrator org (a shared email domain or named individual) — AND (b) the same
described project, campaign, or deliverable. Examples of the same order: ERAU's
two tasks both on invoice #1667, or two tasks tracking one named demo program
for the same integrator.

Records are DISTINCT when ANY of these holds, even if other fields look alike:
  • Different customer contacts / PIs (e.g. two different professors at the
    same university each requesting their own quote) — almost always two orders.
  • Different product/system (an S2 system vs an S3 airframe).
  • Different project, campaign, end-use, or department.

CRITICAL: identical line items are NOT evidence of one order. The same
off-the-shelf product (e.g. a standard "E2 UAS Flight System" config) gets
quoted to many different buyers. A coincidental shared receive-by date (common
academic timelines) is likewise NOT evidence. Require a shared BUYER + shared
PROJECT before merging.

Be CONSERVATIVE: when unsure, keep them separate. NEVER merge an S2 with an S3,
two different professors/PIs, or two different departments of one university.

Return JSON only, no prose:
{"clusters": [["gid1","gid2"], ...]}
Each cluster must list 2+ gids that are the same order. Omit singletons. If no
duplicates exist, return {"clusters": []}."""


def _customer_match_tokens(name: str) -> set[str]:
    """Significant (non-generic) tokens from a customer name, for grouping
    plausibly-same-customer records before the LLM adjudication step."""
    toks = set()
    for t in re.sub(r"[^\w\s]", " ", (name or "").lower()).split():
        if len(t) < 3 or t.isdigit() or t in GENERIC_CUSTOMER_TOKENS:
            continue
        toks.add(t)
    return toks


def _candidate_customer_clusters(builds: list[Build]) -> list[list[Build]]:
    """Connected-components grouping of builds whose customer names share a
    non-generic token. Returns only groups with 2+ members — the candidates
    Haiku adjudicates for same-order duplication."""
    token_sets = [(_customer_match_tokens(b.customer), b) for b in builds]
    parent = list(range(len(token_sets)))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        parent[find(a)] = find(b)

    tok_to_idx: dict[str, list[int]] = {}
    for i, (toks, _) in enumerate(token_sets):
        for t in toks:
            tok_to_idx.setdefault(t, []).append(i)
    for idxs in tok_to_idx.values():
        for j in idxs[1:]:
            union(idxs[0], j)

    groups: dict[int, list[Build]] = {}
    for i, (_, b) in enumerate(token_sets):
        groups.setdefault(find(i), []).append(b)
    return [g for g in groups.values() if len(g) >= 2]


def _haiku_cluster_duplicates(builds: list[Build]) -> list[list[str]]:
    """Ask Haiku which of these same-customer builds are the SAME physical
    order. Returns a list of gid-lists (each 2+ gids). Empty on any failure
    (fail-safe: no merge rather than a wrong merge)."""
    lines = []
    for b in builds:
        items = "; ".join(f"{i.quantity}x {i.description}" for i in (b.items or []))
        lines.append(
            f"- gid {b.asana_gid}: customer={b.customer!r} task={b.asana_task_name!r}\n"
            f"  contact={b.customer_contact or '-'} <{b.customer_email or '-'}>\n"
            f"  items=[{items}] payment={b.payment_state} build={b.build_state} ship={b.ship_state}\n"
            f"  invoice={b.invoice_number or '-'} estimate_date={b.estimate_date or '-'} receive_by={b.receive_by or '-'}\n"
            f"  notes={(b.notes or '')[:300]}"
        )
    user = "RECORDS:\n" + "\n".join(lines) + "\n\nReturn the clusters JSON now."
    try:
        client = get_claude_client()
        resp = client.messages.create(
            model=DISTILL_MODEL,
            max_tokens=600,
            system=CLUSTER_DEDUP_SYSTEM,
            messages=[{"role": "user", "content": user}],
        )
        text = resp.content[0].text.strip()
    except Exception as e:
        print(f"  [WARN] dedup clustering call failed: {e}")
        return []
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    try:
        from commercial_sales_reply import _loads_tolerant
        data = _loads_tolerant(text)
    except Exception:
        print("  [WARN] dedup clustering produced invalid JSON")
        return []
    out = []
    for cl in data.get("clusters", []):
        gids = [str(g) for g in cl if g]
        if len(gids) >= 2:
            out.append(gids)
    return out


def _dedup_and_age_builds(builds: list[Build],
                          force_include_gids: Optional[set] = None) -> list[Build]:
    """Collapse duplicate builds and retire stale leads, deleting the removed
    JSONs and logging them to _filtered.md. Force-included gids are exempt."""
    force_include_gids = force_include_gids or set()
    today = date.today()

    # Force-included records are never merged away or retired.
    protected = [b for b in builds if b.asana_gid in force_include_gids]
    working = [b for b in builds if b.asana_gid not in force_include_gids]

    labels = {b.asana_gid: (b.asana_task_name or b.customer or b.asana_gid)
              for b in working}
    reasons: dict[str, str] = {}
    modified_gids: set = set()  # only merge winners — re-saved to persist folds

    # a. Deterministic invoice merge.
    before = list(working)
    working = merge_builds_by_invoice(working)
    survived = {b.asana_gid for b in working}
    winner_by_inv = {_norm_invoice(b.invoice_number): b.asana_gid
                     for b in working if _norm_invoice(b.invoice_number)}
    for b in before:
        if b.asana_gid not in survived:
            inv = _norm_invoice(b.invoice_number)
            winner_gid = winner_by_inv.get(inv, "?")
            reasons[b.asana_gid] = f"merged into {winner_gid} — duplicate invoice #{inv}"
            modified_gids.add(winner_gid)

    # b. Product-aware LLM clustering for invoice-less duplicates.
    for group in _candidate_customer_clusters(working):
        by_gid = {b.asana_gid: b for b in working}
        for gid_set in _haiku_cluster_duplicates(group):
            members = [by_gid[g] for g in gid_set if g in by_gid]
            if len(members) < 2:
                continue
            # Deterministic safety veto: two distinct concrete contacts (e.g.
            # two different professors at the same university) are two orders,
            # not one — no matter how alike the standard product config looks.
            # A shared invoice is the only thing that overrides this.
            emails = {(m.customer_email or "").strip().lower()
                      for m in members if (m.customer_email or "").strip()}
            invoices = {_norm_invoice(m.invoice_number)
                        for m in members if _norm_invoice(m.invoice_number)}
            if len(emails) >= 2 and len(invoices) != 1:
                print(f"  dedup veto: {[m.asana_gid for m in members]} have "
                      f"distinct contacts {sorted(emails)} — kept separate")
                continue
            winner = merge_build_cluster(members)
            loser_gids = {m.asana_gid for m in members if m.asana_gid != winner.asana_gid}
            for g in loser_gids:
                reasons[g] = f"merged into {winner.asana_gid} — same order (LLM dedup)"
            modified_gids.add(winner.asana_gid)
            working = [b for b in working if b.asana_gid not in loser_gids
                       and b.asana_gid != winner.asana_gid]
            working.append(winner)
            by_gid = {b.asana_gid: b for b in working}

    # c. Retire stale leads.
    kept = []
    for b in working:
        if is_stale_lead(b, today):
            reasons[b.asana_gid] = (
                f"stale lead — estimate {b.estimate_date} >{STALE_LEAD_DAYS}d, no movement"
            )
        else:
            kept.append(b)
    working = kept

    # Persist only the merge winners (their folded-in fields need writing — the
    # main scan loop already saved every other record). Then delete the removed
    # JSONs and log every removal to _filtered.md.
    final_gids = {b.asana_gid for b in working}
    for b in working:
        if b.asana_gid in modified_gids:
            save_build(b)
    for gid, reason in reasons.items():
        if gid in final_gids:
            continue  # safety: never delete a surviving record
        path = BUILDS_DIR / f"{gid}.json"
        if path.exists():
            path.unlink()
        _FILTERED_THIS_SCAN.append({
            "kind": "build",
            "label": labels.get(gid, gid)[:120],
            "gid": gid,
            "reason": reason[:200],
            "date": today.isoformat(),
        })
        print(f"  dedup/age removed {gid}: {reason}")

    return protected + working


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


# --- "Last touch" computation (email + calendar) ---------------------------
# A lead's staleness is judged from genuine customer engagement, not Slack
# noise or the estimate date alone. We compute the most recent of: customer
# emails (from the shared sales mailboxes + direct search, already gathered per
# build) and calendar meetings with the customer (searched across the sales
# team's calendars). See commercial_sales.is_stale_lead.

# DEFAULT_OWNERS first names whose calendars we search for customer meetings,
# plus the admin. These are the commercial-sales interface/invoicing/build
# owners (Beck / Meredith / Nate).
_SALES_TEAM_FIRST_NAMES = {"beck", "meredith", "nate"}


def _sales_team_emails(slack_client=None) -> set[str]:
    """Resolve the sales team's emails (admin + Beck/Meredith/Nate) once per
    scan, via user_map. Best-effort: degrades to just the admin on any failure
    (calendar is a supplementary signal; email coverage is the strong one)."""
    emails = {_admin_impersonation_user().lower()}
    try:
        import user_map
        if slack_client is not None and not user_map.get_all_users():
            user_map.build_user_map(slack_client)
        for u in user_map.get_all_users():
            name = (u.get("name") or "").lower()
            email = (u.get("email") or "").lower()
            first = name.split()[0] if name else ""
            if email and first in _SALES_TEAM_FIRST_NAMES:
                emails.add(email)
    except Exception as e:
        print(f"  [WARN] sales-team calendar resolution failed ({e}); admin only")
    return emails


def _customer_email_dates(emails: list[dict], customer_email: Optional[str]) -> list[str]:
    """ISO dates of emails that are genuine customer correspondence. When we
    know the customer's domain, require it in from/to/cc; otherwise fall back to
    every gathered email (they come from customer-facing mailboxes already)."""
    dom = _sender_domain(customer_email) if customer_email else ""
    dates = []
    for e in emails:
        d = e.get("date") or ""
        if not d:
            continue
        if dom:
            hay = " ".join([e.get("from", ""), e.get("to", ""), e.get("cc", "")]).lower()
            if dom in hay:
                dates.append(d)
        else:
            dates.append(d)
    return dates


def _fetch_customer_meeting_dates(customer: str, customer_email: Optional[str],
                                  team_emails: set[str]) -> list[str]:
    """ISO dates of calendar meetings with this customer across the sales team's
    calendars. Matches when the customer domain is among attendees, or a
    distinctive customer-name token is in the event title. Best-effort."""
    toks = [t for t in re.sub(r"[^\w\s]", " ", (customer or "").lower()).split()
            if len(t) >= 4 and not t.isdigit() and t not in GENERIC_CUSTOMER_TOKENS]
    query = toks[0] if toks else (customer or "").strip()
    if not query:
        return []
    dom = _sender_domain(customer_email) if customer_email else ""
    dates = []
    for cal in team_emails:
        for ev in search_calendar_events(cal, query=query, days_back=400):
            summary = (ev.get("summary") or "").lower()
            attendees = " ".join(ev.get("attendees") or [])
            if (dom and dom in attendees) or any(t in summary for t in toks):
                dates.append(ev["date"])
    return dates


def _set_last_contact_date(build: Build, matched_emails: list[dict],
                           team_emails: set[str], prior: Optional[str] = None) -> None:
    """Stamp build.last_contact_date with the most recent genuine touch. Email
    is checked for every build; calendar meetings are searched only for leads
    (committed orders age on terminal states, not on contact recency). `prior`
    (the previous scan's value) is folded in as a floor so a real contact isn't
    lost when it ages out of this scan's email/calendar window."""
    dates = _customer_email_dates(matched_emails, build.customer_email)
    if not is_order(build):
        dates += _fetch_customer_meeting_dates(
            build.customer, build.customer_email, team_emails)
    if prior:
        dates.append(prior)
    dates = [d for d in dates if d]
    if dates:
        build.last_contact_date = max(dates)


# ---------------------------------------------------------------------------
# Discovery source #2 — orders documented in the general knowledge layer but
# never entered the Commercial Sales Asana project. The canonical example is
# Stanford / Acellent (project 042-1): it lives in its own Asana project and
# corresponds through personal mailboxes, so the primary discovery path (the
# Commercial Sales Asana project + info@/sales@/support@) never sees it.
#
# Two inputs, both of which synthesize a pseudo-Asana-task and run the SAME
# `_haiku_extract_build` extractor — so the STEP 0B funding-proposal filter and
# the is_customer_build gate still apply, and is_active/is_order/state inference
# keep dormant historical orders out of the digest:
#   (a) Stubs written by the #commercial-sales inquiry handler when someone asks
#       about an untracked-but-documented order. Promoted unconditionally — the
#       inquiry itself is the live signal.
#   (b) A sweep of projects classified "commercial equipment purchase" in the
#       financial knowledge, GATED on recent Slack/email activity so we don't
#       resurrect years-old completed sales.
# ---------------------------------------------------------------------------

GENERAL_KNOWLEDGE_ROOT = KNOWLEDGE_DIR
_STUBS_DIR = CS_KNOWLEDGE_DIR / "builds" / "_stubs"
_CONTRACT_TYPE_RX = re.compile(r"contract type:\**\s*(.+)", re.IGNORECASE)
_CLIENT_RX = re.compile(r"(?:client/agency|client|customer):\**\s*(.+)", re.IGNORECASE)
_CODE_IN_TEXT_RX = re.compile(r"(\d{3}[-_]\d{1,2})")

_COMMERCIAL_CT_KEYWORDS = (
    "commercial", "equipment purchase", "purchase order", "materials/inventory",
)
# Contract types that are funding vehicles, not product sales — excluded unless
# the line ALSO clearly reads as an equipment/commercial sale.
_FUNDING_CT_KEYWORDS = (
    "sbir", "sttr", "baa", "grant", "cooperative agreement", "other transaction",
)
_GENERIC_CUSTOMER_WORDS = {
    "university", "college", "institute", "research", "department", "services",
    "service", "technologies", "technology", "systems", "system", "company",
    "corporation", "laboratory", "lab", "school", "center", "centre", "group",
    "the", "and", "for", "inc", "llc", "ltd", "national", "state", "of",
}


def _is_commercial_equipment_contract(content: str) -> bool:
    m = _CONTRACT_TYPE_RX.search(content)
    if not m:
        return False
    ct = m.group(1).strip().lower()
    if not any(k in ct for k in _COMMERCIAL_CT_KEYWORDS):
        return False
    if any(k in ct for k in _FUNDING_CT_KEYWORDS) and "equipment" not in ct and "commercial" not in ct:
        return False
    return True


def _client_from_doc(content: str) -> str:
    m = _CLIENT_RX.search(content)
    if not m:
        return ""
    return m.group(1).strip().strip("*").strip()


def _name_tokens(*names: str) -> set[str]:
    toks: set[str] = set()
    for name in names:
        for w in re.findall(r"[A-Za-z]{4,}", name or ""):
            wl = w.lower()
            if wl not in _GENERIC_CUSTOMER_WORDS:
                toks.add(wl)
    return toks


def _tracked_project_codes(existing_builds: dict) -> set[str]:
    """Project codes already represented by a tracked Build (from its notes /
    gid / task name) — so the sweep doesn't duplicate an order we already
    surface under a real Asana task."""
    codes: set[str] = set()
    for b in existing_builds.values():
        blob = " ".join([b.notes or "", b.asana_gid or "", b.asana_task_name or ""])
        for m in _CODE_IN_TEXT_RX.findall(blob):
            codes.add(m.replace("_", "-"))
    return codes


def _slug_gid(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", (text or "order").lower()).strip("-")[:40]
    return f"doc-{slug or 'order'}"


def _discover_documented_orders(existing_builds, slack_msgs, sales_info_emails,
                                admin_gmail) -> list[Build]:
    """Promote documented/stubbed orders into Builds. See section header."""
    discovered: list[Build] = []
    processed_gids: set[str] = set()

    def _process(code, customer_hint, name, notes, require_recent):
        gid = f"proj-{code}" if code else _slug_gid(name or customer_hint)
        if gid in processed_gids:
            return None
        processed_gids.add(gid)
        tokens = _name_tokens(customer_hint, name)
        matched_slack = _filter_slack_for_tokens(slack_msgs, tokens, EVIDENCE_SLACK_PER_BUILD)
        matched_emails = _filter_emails_for_tokens(sales_info_emails, tokens, EVIDENCE_EMAILS_PER_BUILD)
        if require_recent and not matched_slack and not matched_emails:
            return "skip"  # dormant — no live signal, don't resurrect it
        evidence = _gather_knowledge_evidence(customer_hint or name, code)
        task = {
            "gid": gid,
            "name": name or (f"{customer_hint} [{code}]" if code else customer_hint),
            "notes": (notes or "")[:6000],
            "custom_fields": [],
            "due_on": None,
            "assignee": None,
        }
        existing = existing_builds.get(gid)
        updated, drop = _haiku_extract_build(
            task, existing, matched_emails, matched_slack,
            knowledge_evidence=evidence, gmail_service=admin_gmail,
        )
        if updated:
            updated.asana_task_name = task["name"]
            _set_last_contact_date(
                updated, matched_emails, set(),
                prior=existing.last_contact_date if existing else None)
            save_build(updated)
            discovered.append(updated)
            time.sleep(0.3)
            return "ok"
        if drop:
            stale = BUILDS_DIR / f"{gid}.json"
            if stale.exists():
                stale.unlink()
            return "drop"
        return "fail"

    # (a) Promote inquiry-handler stubs (unconditional).
    if _STUBS_DIR.is_dir():
        for stub_path in sorted(_STUBS_DIR.glob("*.json")):
            try:
                stub = json.loads(stub_path.read_text())
            except Exception:
                continue
            code = (stub.get("project_code") or "").replace("_", "-")
            customer = stub.get("customer") or ""
            product = stub.get("product") or ""
            doc_text = ""
            for rel in stub.get("source_files") or []:
                p = GENERAL_KNOWLEDGE_ROOT / rel
                if p.exists():
                    doc_text += f"\n--- {rel} ---\n" + p.read_text(errors="ignore")[:4000]
            notes = "\n".join(
                x for x in (stub.get("notes"), stub.get("origin_inquiry")) if x
            ) + doc_text
            name = (f"{customer} {product}".strip()) or customer or product
            res = _process(code, customer, name, notes, require_recent=False)
            # Consume the stub unless Haiku transiently failed (so a flaky call
            # gets retried next scan rather than silently dropping the order).
            if res and res != "fail":
                try:
                    stub_path.unlink()
                except Exception:
                    pass

    # (b) Recency-gated sweep of commercial-equipment-purchase projects.
    tracked = _tracked_project_codes(existing_builds)
    fin_dir = GENERAL_KNOWLEDGE_ROOT / "financial" / "by_project"
    if fin_dir.is_dir():
        for path in sorted(fin_dir.glob("*.md")):
            code = path.stem.replace("_", "-")
            if code in tracked:
                continue
            try:
                content = path.read_text(errors="ignore")
            except Exception:
                continue
            if not _is_commercial_equipment_contract(content):
                continue
            customer = _client_from_doc(content)
            notes = content[:4000]
            bud = GENERAL_KNOWLEDGE_ROOT / "budgets" / f"project_{path.stem}.md"
            if bud.exists():
                notes += "\n--- budget ---\n" + bud.read_text(errors="ignore")[:3000]
            _process(code, customer, f"{customer} [{code}]".strip(), notes,
                     require_recent=True)

    return discovered


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

    # Admin Gmail service — used for shared-address scans AND for lazy PDF
    # attachment fetching during per-Build Haiku extraction. Built once and
    # passed through so we don't pay the auth/setup cost per Build.
    admin_gmail = _build_admin_gmail_service()

    # Sales-team calendars searched for customer meetings (a "last touch" signal
    # for leads). Resolved once; degrades to admin-only if user_map is unavailable.
    team_emails = _sales_team_emails(slack_client)
    print(f"  Sales-team calendars for meeting lookup: {len(team_emails)}")

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

    # Force-include override: gids the user has explicitly told the bot to
    # surface in the digest, bypassing the is_customer_build filter. Set via
    # the `track this: ...` admin command.
    try:
        from commercial_sales_admin import get_force_include_gids
        force_include_gids = get_force_include_gids()
        if force_include_gids:
            print(f"  Force-include list: {len(force_include_gids)} gids")
    except Exception:
        force_include_gids = set()

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
        is_forced = task["gid"] in force_include_gids
        updated, drop_existing = _haiku_extract_build(
            task, existing, matched_emails, matched_slack,
            knowledge_evidence=evidence, gmail_service=admin_gmail,
            force_include=is_forced,
        )
        if updated is not None:
            # Stamp the Asana task name so the renderer can disambiguate
            # same-customer cards via the subtitle.
            updated.asana_task_name = task.get("name") or None
            # Genuine "last touch" from customer email + (for leads) meetings —
            # drives lead aging in is_stale_lead.
            _set_last_contact_date(
                updated, matched_emails, team_emails,
                prior=existing.last_contact_date if existing else None)
        if updated:
            save_build(updated)
            new_builds.append(updated)
            time.sleep(0.3)  # gentle pacing for Anthropic
        elif drop_existing:
            # Haiku explicitly said this isn't a customer build. Force-include
            # gids should never hit this branch (the filter is bypassed by the
            # force_include flag) — but defensively, if a forced gid lands
            # here anyway, preserve any existing record rather than deleting.
            if is_forced and existing:
                new_builds.append(existing)
                continue
            stale = BUILDS_DIR / f"{task['gid']}.json"
            if stale.exists():
                stale.unlink()
            dropped_gids.append(task["gid"])
        else:
            # Transient Haiku failure — preserve prior record if we had one
            if existing:
                new_builds.append(existing)

    # 4b. Discovery source #2 — promote documented/stubbed orders that never
    # entered the Commercial Sales Asana project (e.g. Stanford/Acellent 042-1).
    try:
        documented = _discover_documented_orders(
            existing_builds, slack_msgs, sales_info_emails, admin_gmail,
        )
        if documented:
            print(f"  Discovered {len(documented)} documented order(s) outside the Asana project")
            existing_new_gids = {b.asana_gid for b in new_builds}
            for b in documented:
                if b.asana_gid not in existing_new_gids:
                    new_builds.append(b)
    except Exception as e:
        print(f"  [WARN] documented-order discovery failed: {e}")

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

    # 6b. Collapse duplicate builds + retire stale leads (deletes removed JSONs,
    # logs them to _filtered.md). Force-included gids are exempt.
    new_builds = _dedup_and_age_builds(new_builds, force_include_gids)

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
