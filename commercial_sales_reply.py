"""Reply-to-update flow for the #commercial-sales digest.

When a user replies in a Slack thread under one of Jack's per-build cards,
this module:
  1. Identifies which Build / SupportCase the thread belongs to (via the
     `_message_map.json` written by the scheduler, with a fallback to the
     hidden `build:<gid>` / `case:<id>` token at the bottom of each card).
  2. Calls Haiku to parse the freeform reply into structured field updates
     against the current record.
  3. Posts a propose-and-confirm message in the same thread (mirrors the
     pattern in task_actions.py).
  4. On a follow-up "yes" / "accept 1 and 3" / "actually it's..." reply,
     applies the updates: writes to the JSON record AND posts an Asana
     comment on the task for an audit trail.

State is in-memory keyed on thread_ts — short-lived; a Railway restart
just makes the user re-state the change.
"""

from __future__ import annotations

import json
import os
import re
import time
from pathlib import Path
from typing import Optional

import anthropic
import requests

from commercial_sales import (
    Build,
    SupportCase,
    BUILDS_DIR,
    SUPPORT_DIR,
    PAYMENT_STATES,
    BUILD_STATES,
    SHIP_STATES,
    SUPPORT_STATES,
)


KNOWLEDGE_DIR = Path(__file__).parent / "knowledge" / "commercial_sales"
MESSAGE_MAP_PATH = KNOWLEDGE_DIR / "_message_map.json"

ASANA_BASE = "https://app.asana.com/api/1.0"

PENDING_TTL = 600  # 10 minutes
PENDING: dict[str, dict] = {}  # thread_ts -> state

STATE_AWAIT_CONFIRM = "await_confirm"

_client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", ""))
DISTILL_MODEL = "claude-haiku-4-5-20251001"


# Fields the reply-handler is allowed to update on a Build / SupportCase.
# Anything else (system fields like asana_gid, last_evidence_date) is rejected.
BUILD_WRITABLE = {
    "customer", "customer_contact", "customer_email",
    "receive_by", "ship_to",
    "items", "parts",
    "payment_state", "build_state", "ship_state",
    "estimate_date", "invoice_date", "invoice_amount", "invoice_number", "paid_date",
    "tracking_number", "carrier", "shipped_date",
    "owners", "notes",
}
SUPPORT_WRITABLE = {
    "customer", "customer_contact", "customer_email",
    "device", "serial_number", "reported_issue",
    "state", "rma_number", "received_date", "shipped_back_date",
    "tracking_number", "carrier",
    "linked_build_gid", "owners", "notes",
}


# --- Pending state ---------------------------------------------------------


def _now() -> float:
    return time.time()


def _get_pending(thread_ts: str) -> Optional[dict]:
    entry = PENDING.get(thread_ts)
    if not entry:
        return None
    if _now() - entry["created"] > PENDING_TTL:
        PENDING.pop(thread_ts, None)
        return None
    return entry


def _set_pending(thread_ts: str, state: dict) -> None:
    state["created"] = _now()
    PENDING[thread_ts] = state


def _clear_pending(thread_ts: str) -> None:
    PENDING.pop(thread_ts, None)


def has_pending(thread_ts: str) -> bool:
    return _get_pending(thread_ts) is not None


# --- Record lookup ---------------------------------------------------------


def _load_message_map() -> dict:
    """Return ts → {kind, id} from the scheduler-written map. Empty when
    Railway has just redeployed and the file's gone — caller should fall
    back to parsing the hidden token from the parent message text."""
    if not MESSAGE_MAP_PATH.exists():
        return {}
    try:
        data = json.loads(MESSAGE_MAP_PATH.read_text())
        return data.get("messages", {}) or {}
    except Exception:
        return {}


_TOKEN_RX = re.compile(r"`(build|case):([A-Za-z0-9_\-]+)`")


def _id_from_parent_text(parent_text: str) -> Optional[tuple[str, str]]:
    """Pull `build:<gid>` or `case:<id>` token out of a parent message."""
    if not parent_text:
        return None
    m = _TOKEN_RX.search(parent_text)
    if not m:
        return None
    return (m.group(1), m.group(2))  # ('build', '1213...') or ('case', 'SC-2026-001')


def lookup_record_for_thread(slack_client, channel_id: str, thread_ts: str) -> Optional[dict]:
    """Find which Build/SupportCase a thread reply is updating.

    Returns {'kind': 'build'|'case', 'id': str, 'record': Build|SupportCase}
    or None when the thread isn't under one of Jack's cards.
    """
    # Primary path: scheduler-written map
    msg_map = _load_message_map()
    entry = msg_map.get(thread_ts)
    if entry:
        rec = _load_record(entry.get("kind"), entry.get("id"))
        if rec:
            return {"kind": entry["kind"], "id": entry["id"], "record": rec}

    # Fallback: read the parent message and parse its hidden token
    try:
        result = slack_client.conversations_replies(
            channel=channel_id, ts=thread_ts, limit=1,
        )
        msgs = result.get("messages", []) or []
        if not msgs:
            return None
        parent_text = msgs[0].get("text", "")
    except Exception:
        return None
    parsed = _id_from_parent_text(parent_text)
    if not parsed:
        return None
    kind, rec_id = parsed
    rec = _load_record(kind, rec_id)
    if not rec:
        return None
    return {"kind": kind, "id": rec_id, "record": rec}


def _load_record(kind: str, rec_id: str):
    if not kind or not rec_id:
        return None
    if kind == "build":
        path = BUILDS_DIR / f"{rec_id}.json"
        if not path.exists():
            return None
        try:
            return Build.from_dict(json.loads(path.read_text()))
        except Exception:
            return None
    if kind == "case":
        path = SUPPORT_DIR / f"{rec_id}.json"
        if not path.exists():
            return None
        try:
            return SupportCase.from_dict(json.loads(path.read_text()))
        except Exception:
            return None
    return None


def _save_record(kind: str, record) -> None:
    if kind == "build":
        path = BUILDS_DIR / f"{record.asana_gid}.json"
        path.write_text(json.dumps(record.to_dict(), indent=2, default=str))
    elif kind == "case":
        path = SUPPORT_DIR / f"{record.case_id}.json"
        path.write_text(json.dumps(record.to_dict(), indent=2, default=str))


# --- Haiku helpers ---------------------------------------------------------


PARSE_REPLY_SYSTEM = """\
You parse a Slack thread reply about a customer Build/SupportCase into
structured field updates. The reply is from a BST team member trying to
add or correct information on the record shown above the thread.

Output a single JSON object with this shape — no markdown fences, no commentary:

{
  "updates": [
    {"field": "<field_name>", "value": <new_value>, "rationale": "<why this update>"}
  ],
  "ambiguous": [ "<things you couldn't resolve confidently>" ]
}

Rules:
- `field` must be one of the writable fields on the record (caller will validate).
  For Build: customer, customer_contact, customer_email, receive_by, ship_to,
  items, parts, payment_state, build_state, ship_state, estimate_date,
  invoice_date, invoice_amount, invoice_number, paid_date, tracking_number,
  carrier, shipped_date, owners, notes.
  For SupportCase: customer, customer_contact, customer_email, device,
  serial_number, reported_issue, state, rma_number, received_date,
  shipped_back_date, tracking_number, carrier, linked_build_gid, owners, notes.
- Dates: emit ISO format "YYYY-MM-DD" — parse natural language like "Jun 1"
  or "next Friday" into a specific date. Today's date is provided below.
- State machines: emit the lowercase enum value (e.g. "invoice_sent",
  "in_assembly", "delivered"). Reject values not in the enum.
- For lists (items, parts): emit the WHOLE new list, preserving any items
  the reply doesn't change. Use the current value from the JSON record as
  the starting point and modify from there.
- For `owners`: emit a partial dict containing only the role(s) being
  overridden, e.g. {"build": "Joshua"}. Caller will merge.
- For `notes`: emit the FULL new notes block — if the user is adding to
  existing notes, prepend the new context but preserve old context too.
- If you can't tell what field a piece of the reply maps to, put it in
  `ambiguous` rather than guessing.
- Never invent values not present in the reply.
"""


CONFIRM_PARSE_SYSTEM = """\
The user just replied to a proposed update. Decide whether they:
  - "accept_all"  — yes, apply everything
  - "accept_subset" — apply only some items; return accepted_indices [1, 2, ...]
  - "reject"      — cancel, change nothing
  - "modify"      — they want different values; return modification_request as a string
  - "unrelated"   — message is off-topic, leave the proposal pending

Output one JSON object:
{
  "intent": "accept_all" | "accept_subset" | "reject" | "modify" | "unrelated",
  "accepted_indices": [int, ...],
  "modification_request": "string"
}

No markdown fences. No commentary.
"""


def _call_claude_json(system: str, user: str, max_tokens: int = 1000) -> dict:
    resp = _client.messages.create(
        model=DISTILL_MODEL,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    text = resp.content[0].text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    return json.loads(text)


# --- Update validation -----------------------------------------------------


def _validate_update(kind: str, update: dict) -> tuple[bool, str]:
    """Return (ok, reason). Caller drops invalid updates with a note."""
    field = update.get("field")
    value = update.get("value")
    if kind == "build":
        if field not in BUILD_WRITABLE:
            return False, f"not a writable Build field: {field}"
        if field == "payment_state" and value not in PAYMENT_STATES:
            return False, f"payment_state must be one of {PAYMENT_STATES}"
        if field == "build_state" and value not in BUILD_STATES:
            return False, f"build_state must be one of {BUILD_STATES}"
        if field == "ship_state" and value not in SHIP_STATES:
            return False, f"ship_state must be one of {SHIP_STATES}"
    elif kind == "case":
        if field not in SUPPORT_WRITABLE:
            return False, f"not a writable SupportCase field: {field}"
        if field == "state" and value not in SUPPORT_STATES:
            return False, f"state must be one of {SUPPORT_STATES}"
    else:
        return False, f"unknown kind: {kind}"
    return True, ""


def _apply_update_to_record(kind: str, record, update: dict):
    """Apply one validated update to a Build or SupportCase in-place."""
    field = update["field"]
    value = update["value"]

    # `owners` is merged not replaced — preserves any roles the reply didn't touch
    if field == "owners" and isinstance(value, dict):
        merged = dict(record.owners or {})
        merged.update(value)
        record.owners = merged
        return

    # Items and parts come as full replacement lists — keep what Haiku produced.
    if kind == "build" and field == "items":
        from commercial_sales import Item
        record.items = [Item.from_dict(x) if isinstance(x, dict) else x for x in (value or [])]
        return
    if kind == "build" and field == "parts":
        from commercial_sales import Part
        record.parts = [Part.from_dict(x) if isinstance(x, dict) else x for x in (value or [])]
        return

    # Everything else is a flat field assignment.
    setattr(record, field, value)


# --- Asana audit comment ---------------------------------------------------


def _post_asana_comment(asana_gid: str, text: str) -> tuple[bool, Optional[str]]:
    """Post a comment to an Asana task for audit. Best-effort — silent on auth
    failure or missing gid, the JSON record write is the source of truth."""
    if not asana_gid:
        return False, "no gid"
    token = os.environ.get("ASANA_ACCESS_TOKEN")
    if not token:
        return False, "no asana token"
    try:
        resp = requests.post(
            f"{ASANA_BASE}/tasks/{asana_gid}/stories",
            headers={"Authorization": f"Bearer {token}"},
            json={"data": {"text": text}},
            timeout=10,
        )
        if resp.status_code >= 400:
            return False, f"HTTP {resp.status_code}: {resp.text[:200]}"
        return True, None
    except Exception as e:
        return False, str(e)


# --- Format helpers --------------------------------------------------------


def _format_value(value) -> str:
    """Render a proposed value compactly for the Slack proposal message."""
    if value is None:
        return "_(none)_"
    if isinstance(value, (list, dict)):
        try:
            return f"`{json.dumps(value, default=str)[:200]}`"
        except Exception:
            return str(value)[:200]
    return str(value)


def _record_label(rec) -> str:
    if isinstance(rec, Build):
        return rec.customer or rec.asana_task_name or rec.asana_gid
    if isinstance(rec, SupportCase):
        return f"{rec.customer or 'support'} ({rec.case_id})"
    return "record"


def _format_proposal(record_label: str, updates: list[dict], ambiguous: list[str]) -> str:
    lines = [f"Proposed updates for *{record_label}*:"]
    for i, u in enumerate(updates, 1):
        lines.append(f"  {i}. `{u['field']}` → {_format_value(u['value'])}")
        if u.get("rationale"):
            lines.append(f"     _{u['rationale']}_")
    if ambiguous:
        lines.append("\n_Couldn't tell where these belong:_")
        for a in ambiguous:
            lines.append(f"  • {a}")
    lines.append("\nReply *yes* to apply, *no* to cancel, or restate to correct.")
    return "\n".join(lines)


# --- Entry points called from app.py ---------------------------------------


def handle_thread_reply(slack_client, event) -> Optional[str]:
    """Process a fresh threaded reply (no pending proposal yet).

    Returns the text of the bot's response to post in-thread, or None if
    the reply doesn't look like a meaningful update request and should be
    silently ignored.
    """
    channel_id = event.get("channel", "")
    thread_ts = event.get("thread_ts", "")
    user_id = event.get("user", "")
    text = (event.get("text") or "").strip()
    if not (channel_id and thread_ts and user_id and text):
        return None

    info = lookup_record_for_thread(slack_client, channel_id, thread_ts)
    if not info:
        return None

    record = info["record"]
    kind = info["kind"]
    record_dict = record.to_dict()
    today = __import__("datetime").date.today().isoformat()

    # Ask Haiku what fields to update
    user_block = (
        f"Today is {today}.\n\n"
        f"Record kind: {kind}\n"
        f"Current JSON:\n{json.dumps(record_dict, indent=2, default=str)}\n\n"
        f"User reply in thread:\n{text}"
    )
    try:
        parsed = _call_claude_json(PARSE_REPLY_SYSTEM, user_block)
    except Exception as e:
        return f"_(I couldn't parse that — try again? Error: {e})_"

    raw_updates = parsed.get("updates") or []
    ambiguous = parsed.get("ambiguous") or []

    # Validate each update
    valid_updates = []
    rejected = []
    for u in raw_updates:
        ok, err = _validate_update(kind, u)
        if ok:
            valid_updates.append(u)
        else:
            rejected.append(f"`{u.get('field','?')}`: {err}")

    if not valid_updates:
        body = "I couldn't pull any valid updates out of that."
        if ambiguous:
            body += "\n\n_Things I wasn't sure about:_\n" + "\n".join(f"  • {a}" for a in ambiguous)
        if rejected:
            body += "\n\n_Rejected:_\n" + "\n".join(f"  • {r}" for r in rejected)
        return body

    # Stash and propose
    _set_pending(thread_ts, {
        "state": STATE_AWAIT_CONFIRM,
        "kind": kind,
        "id": info["id"],
        "updates": valid_updates,
        "ambiguous": ambiguous,
        "rejected": rejected,
        "user_id": user_id,
        "channel_id": channel_id,
        "original_reply": text,
    })

    label = _record_label(record)
    msg = _format_proposal(label, valid_updates, ambiguous)
    if rejected:
        msg += "\n\n_(Rejected: " + "; ".join(rejected) + ")_"
    return msg


def handle_thread_followup(slack_client, event) -> Optional[str]:
    """Process a follow-up reply when there's a pending proposal for this thread.

    Returns the response text, or None if the reply is unrelated (caller
    should leave the proposal pending and ignore the message).
    """
    thread_ts = event.get("thread_ts", "")
    user_id = event.get("user", "")
    text = (event.get("text") or "").strip()
    pending = _get_pending(thread_ts)
    if not pending:
        return None
    if not text:
        return None

    # Allow any user in the thread to confirm — not just the original proposer.
    # Beck may propose, Meredith confirms. (Pending state stores user_id for
    # audit, but doesn't gate confirm.)

    numbered = "\n".join(
        f"{i+1}. {u['field']} → {_format_value(u['value'])}"
        for i, u in enumerate(pending["updates"])
    )
    parse_input = f"Pending updates:\n{numbered}\n\nUser reply:\n{text}"
    try:
        intent_obj = _call_claude_json(CONFIRM_PARSE_SYSTEM, parse_input, max_tokens=300)
    except Exception:
        return None  # don't hijack on parse failure; user can re-state

    intent = intent_obj.get("intent", "unrelated")

    if intent == "unrelated":
        return None

    if intent == "reject":
        _clear_pending(thread_ts)
        return "Cancelled — no changes made."

    if intent == "modify":
        modification = intent_obj.get("modification_request", "")
        # Re-run the parse with the modification text replacing the original reply.
        # We need the record again — load it fresh.
        record = _load_record(pending["kind"], pending["id"])
        if not record:
            _clear_pending(thread_ts)
            return "_(I lost track of the record — try replying again.)_"
        # Reuse the propose path with a synthesized event
        new_event = {
            "channel": pending["channel_id"],
            "thread_ts": thread_ts,
            "user": user_id,
            "text": modification or text,
        }
        return handle_thread_reply(slack_client, new_event)

    # accept_all or accept_subset
    if intent == "accept_all":
        selected = pending["updates"]
    elif intent == "accept_subset":
        indices = intent_obj.get("accepted_indices") or []
        selected = [pending["updates"][i - 1] for i in indices
                    if 1 <= i <= len(pending["updates"])]
        if not selected:
            return "I couldn't tell which items you meant. Try again with numbers (e.g. _apply 1 and 2_)."
    else:
        return None

    # Load the current record and apply
    record = _load_record(pending["kind"], pending["id"])
    if not record:
        _clear_pending(thread_ts)
        return "_(Record disappeared between propose and apply — please retry.)_"

    for u in selected:
        _apply_update_to_record(pending["kind"], record, u)

    # Update last_evidence_date to today since a human just touched it
    if hasattr(record, "last_evidence_date"):
        record.last_evidence_date = __import__("datetime").date.today().isoformat()

    _save_record(pending["kind"], record)

    # Asana comment audit
    asana_gid = getattr(record, "asana_gid", None)
    comment = (
        f"Jack Bot: {len(selected)} update(s) from Slack #commercial-sales thread:\n"
        + "\n".join(f"  - {u['field']} → {_format_value(u['value'])}" for u in selected)
        + f"\n\nSubmitted by Slack user <@{user_id}>."
    )
    if asana_gid:
        ok, err = _post_asana_comment(asana_gid, comment)
        comment_status = "Posted Asana audit comment." if ok else f"_(Couldn't post Asana comment: {err})_"
    else:
        comment_status = ""

    # Knowledge-channel audit
    try:
        from knowledge import store_entry
        store_entry(slack_client, "FEEDBACK", comment)
    except Exception:
        pass

    _clear_pending(thread_ts)
    applied_lines = "\n".join(
        f"  ✓ `{u['field']}` → {_format_value(u['value'])}" for u in selected
    )
    rejected_count = len(pending["updates"]) - len(selected)
    header = f"Applied {len(selected)} update(s)."
    if rejected_count:
        header += f" Skipped {rejected_count} item(s)."
    body = header + "\n" + applied_lines
    if comment_status:
        body += "\n" + comment_status
    return body
