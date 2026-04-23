"""purchasing@blackswifttech.com Gmail scanner.

`purchasing@blackswifttech.com` is a distribution group, not a Gmail user we
can impersonate. Instead we scan a known recipient's mailbox (the admin user)
filtering for `to/from/cc/bcc:purchasing@blackswifttech.com`. The admin is on
the group and is cc'd on most purchase activity; this gives ~90% coverage for
week 2 without requiring additional OAuth scopes.

Pulls those messages, extracts (vendor, amount, project) tuples via Haiku, and
writes per-month JSON at `knowledge/purchases/{YYYY-MM}.json`.

Output feeds `scanners/project_state_scanner.py`:
  - budget.spent.purchases  — sum of amounts older than COMMITTED_WINDOW_DAYS
  - budget.committed        — sum newer than that (still in-flight, not yet
                              reliably reflected in QBO bank transactions)
"""

from __future__ import annotations

import base64
import json
import os
import re
import time
from collections import defaultdict
from datetime import datetime, date, timedelta
from pathlib import Path
from typing import Optional

from googleapiclient.discovery import build

from .base import KNOWLEDGE_DIR, get_last_scan, update_scan_timestamp, get_claude_client, DISTILL_MODEL
from google_client import _get_credentials


PURCHASES_DIR = KNOWLEDGE_DIR / "purchases"

# The group address we filter Gmail on — not impersonated directly.
PURCHASING_GROUP = "purchasing@blackswifttech.com"

LIST_PAGE_SIZE = 100
MSG_FETCH_DELAY = 0.15
BATCH_SIZE = 25  # messages per Haiku call


def _impersonation_user() -> str:
    """Return the real Gmail user to impersonate (admin default)."""
    return os.environ.get("GOOGLE_ADMIN_EMAIL") or "elstonj@blackswifttech.com"

MODE_LIMITS = {
    "full": 2000,
    "1yr": 800,
    "incremental": 300,
}


# ---------------------------------------------------------------------------
# Gmail fetch
# ---------------------------------------------------------------------------


def _build_service() -> Optional[object]:
    creds = _get_credentials(_impersonation_user())
    if not creds:
        return None
    return build("gmail", "v1", credentials=creds, cache_discovery=False)


def _build_query(mode: str) -> str:
    """Filter to messages that touch the purchasing group in any header."""
    addr_filter = (
        f"(to:{PURCHASING_GROUP} OR from:{PURCHASING_GROUP} "
        f"OR cc:{PURCHASING_GROUP} OR bcc:{PURCHASING_GROUP})"
    )
    if mode == "full":
        return addr_filter
    if mode == "1yr":
        return f"{addr_filter} newer_than:365d"
    if mode == "incremental":
        last = get_last_scan("purchasing")
        if last:
            days = max(1, (datetime.now() - last).days + 1)
            return f"{addr_filter} newer_than:{days}d"
        return f"{addr_filter} newer_than:180d"
    return addr_filter


def _list_message_ids(service, query: str, max_results: int) -> list[str]:
    ids: list[str] = []
    page_token = None
    while len(ids) < max_results:
        kwargs = {
            "userId": "me",
            "maxResults": min(LIST_PAGE_SIZE, max_results - len(ids)),
        }
        if query:
            kwargs["q"] = query
        if page_token:
            kwargs["pageToken"] = page_token
        resp = service.users().messages().list(**kwargs).execute()
        for m in resp.get("messages", []) or []:
            ids.append(m["id"])
        page_token = resp.get("nextPageToken")
        if not page_token:
            break
    return ids


def _decode_body_part(part: dict) -> str:
    body = part.get("body", {})
    data = body.get("data")
    if not data:
        return ""
    try:
        return base64.urlsafe_b64decode(data + "===").decode("utf-8", errors="replace")
    except Exception:
        return ""


def _extract_body(payload: dict) -> str:
    """Best-effort plain-text body from a Gmail message payload."""
    mime = payload.get("mimeType", "")
    if mime == "text/plain":
        return _decode_body_part(payload)
    if mime == "text/html":
        html = _decode_body_part(payload)
        return re.sub(r"<[^>]+>", " ", html)
    parts = payload.get("parts") or []
    plain = ""
    html = ""
    for p in parts:
        if p.get("mimeType") == "text/plain" and not plain:
            plain = _decode_body_part(p)
        elif p.get("mimeType") == "text/html" and not html:
            html = _decode_body_part(p)
        else:
            nested = _extract_body(p)
            if nested and not plain:
                plain = nested
    if plain:
        return plain
    if html:
        return re.sub(r"<[^>]+>", " ", html)
    return ""


def _fetch_message(service, msg_id: str) -> Optional[dict]:
    try:
        msg = service.users().messages().get(
            userId="me", id=msg_id, format="full"
        ).execute()
    except Exception:
        return None
    headers = {h["name"].lower(): h["value"]
               for h in (msg.get("payload", {}).get("headers") or [])}
    body = _extract_body(msg.get("payload") or {})
    # Internal date (ms since epoch)
    try:
        ts = int(msg.get("internalDate", "0")) / 1000
        iso_date = datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
    except Exception:
        iso_date = ""
    return {
        "id": msg_id,
        "date": iso_date,
        "subject": headers.get("subject", "")[:300],
        "from": headers.get("from", "")[:200],
        "to": headers.get("to", "")[:400],
        "snippet": (msg.get("snippet") or "")[:500],
        "body": body[:4000],  # Haiku doesn't need more than this for a purchase
    }


# ---------------------------------------------------------------------------
# Haiku extraction
# ---------------------------------------------------------------------------


EXTRACTION_PROMPT = """\
You extract purchase records from emails forwarded to/from \
purchasing@blackswifttech.com. BST is a small aerospace company; these emails \
include purchase requests, vendor quotes, PO confirmations, shipping notices, \
and invoices.

For each email I send you, emit ONE JSON object per line (JSONL, no wrapper \
array, no commentary):

{"id": "<echo input id>",
 "is_purchase": true|false,
 "status": "requested"|"approved"|"ordered"|"received"|"invoiced"|"other",
 "amount_usd": number | null,
 "vendor": string | null,
 "project_code": string | null,  // e.g. "350-4" or "001-7" — only if explicitly mentioned
 "description": string | null,   // brief — what's being bought
 "notes": string | null           // anything unusual: approval chain, holds, splits
}

Rules:
- is_purchase=false for calendar invites, spam, newsletters, shipping chatter \
with no $ anchor, reply-all noise.
- amount_usd: the actual cost total as a number. If only a quote range, pick the \
high end. If VAT or tax is separate, use the grand total. Null if unknown.
- project_code: match `XXX-Y` patterns. If the email mentions a project by name \
(e.g. "Mexico" or "INSTAAR") without the code, leave null — we'll match later.
- status: "requested" = initial ask; "approved" = reply approving; "ordered" = PO \
issued or vendor confirmation; "received" = delivery confirmed; "invoiced" = \
invoice attached; "other" if ambiguous.
- Output ONE line per input email, JSONL format. No code fences, no prose.
"""


def _chunk(seq: list, n: int):
    for i in range(0, len(seq), n):
        yield seq[i:i + n]


def _extract_records(messages: list[dict]) -> list[dict]:
    """Send a batch of messages to Haiku, parse JSONL records.

    Returns a list of records (each with the `id` echoed back for correlation).
    """
    if not messages:
        return []
    user_blob = "\n\n".join(
        f"---\nid: {m['id']}\ndate: {m['date']}\nsubject: {m['subject']}\n"
        f"from: {m['from']}\nto: {m['to']}\n---\n{(m['snippet'] or '') + (chr(10)+m['body'] if m.get('body') else '')}"
        for m in messages
    )
    try:
        client = get_claude_client()
        resp = client.messages.create(
            model=DISTILL_MODEL,
            max_tokens=4000,
            system=EXTRACTION_PROMPT,
            messages=[{"role": "user", "content": user_blob[:100000]}],
        )
        raw = resp.content[0].text.strip()
    except Exception as e:
        print(f"    [WARN] Haiku batch failed: {e}")
        return []

    out: list[dict] = []
    for line in raw.splitlines():
        line = line.strip().strip(",")
        if not line or line.startswith("```") or line.startswith("//"):
            continue
        try:
            rec = json.loads(line)
            if isinstance(rec, dict) and rec.get("id"):
                out.append(rec)
        except json.JSONDecodeError:
            continue
    return out


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------


def _write_monthly(records: list[dict]) -> list[Path]:
    """Bucket records by YYYY-MM and write each bucket to disk.

    Existing month files are merged (by record id) so re-running incremental
    scans doesn't lose older records and de-duplicates on replay.
    """
    by_month: dict[str, list[dict]] = defaultdict(list)
    for r in records:
        d = r.get("date") or ""
        if len(d) >= 7:
            by_month[d[:7]].append(r)
        else:
            by_month["unknown"].append(r)

    PURCHASES_DIR.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for month, recs in by_month.items():
        path = PURCHASES_DIR / f"{month}.json"
        existing: dict[str, dict] = {}
        if path.exists():
            try:
                existing = {r["id"]: r for r in json.loads(path.read_text())
                            if isinstance(r, dict) and r.get("id")}
            except Exception:
                existing = {}
        for r in recs:
            existing[r["id"]] = r
        merged = sorted(existing.values(), key=lambda r: r.get("date", ""))
        path.write_text(json.dumps(merged, indent=2))
        written.append(path)
    return written


def _rewrite_index() -> Path:
    """Rebuild the purchases _index.json summary from the monthly files."""
    totals: dict[str, dict] = defaultdict(lambda: {"count": 0, "total_amount": 0.0})
    all_records: list[dict] = []
    if PURCHASES_DIR.exists():
        for p in sorted(PURCHASES_DIR.glob("20*.json")):
            try:
                recs = json.loads(p.read_text())
            except Exception:
                continue
            for r in recs:
                if not r.get("is_purchase"):
                    continue
                all_records.append(r)
                code = r.get("project_code") or "_unattributed"
                amt = r.get("amount_usd") or 0
                totals[code]["count"] += 1
                try:
                    totals[code]["total_amount"] += float(amt or 0)
                except (TypeError, ValueError):
                    pass

    index_path = PURCHASES_DIR / "_index.json"
    index_path.write_text(json.dumps({
        "generated_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "total_records": len(all_records),
        "by_project": {
            k: {"count": v["count"], "total_amount": round(v["total_amount"], 2)}
            for k, v in sorted(totals.items())
        },
    }, indent=2))
    return index_path


def scan_all(mode: str = "1yr") -> list[Path]:
    service = _build_service()
    if not service:
        print("[ERROR] Could not build Gmail service — check domain delegation")
        return []

    query = _build_query(mode)
    max_n = MODE_LIMITS.get(mode, MODE_LIMITS["1yr"])
    print(f"Impersonating: {_impersonation_user()}")
    print(f"Query: {query}  |  cap: {max_n}")

    msg_ids = _list_message_ids(service, query, max_n)
    print(f"Found {len(msg_ids)} message IDs")

    messages: list[dict] = []
    for i, mid in enumerate(msg_ids):
        m = _fetch_message(service, mid)
        if m:
            messages.append(m)
        if i % 50 == 0 and i > 0:
            print(f"  fetched {i}/{len(msg_ids)}")
        time.sleep(MSG_FETCH_DELAY)
    print(f"Fetched {len(messages)} messages")

    # Haiku batching
    all_records: list[dict] = []
    # Build id→meta lookup so we can enrich records with the email's date
    meta_by_id = {m["id"]: m for m in messages}
    for batch in _chunk(messages, BATCH_SIZE):
        recs = _extract_records(batch)
        for r in recs:
            meta = meta_by_id.get(r.get("id"), {})
            r.setdefault("date", meta.get("date", ""))
            r.setdefault("subject", meta.get("subject", "")[:200])
        all_records.extend(recs)
        print(f"  Haiku batch: {len(recs)}/{len(batch)} records extracted")
        time.sleep(0.3)

    written = _write_monthly(all_records)
    _rewrite_index()
    update_scan_timestamp("purchasing")
    print(f"Wrote {len(written)} monthly files + _index.json → {PURCHASES_DIR}")
    return written
