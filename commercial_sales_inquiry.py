"""Inquiry handler for #commercial-sales.

Top-level (non-threaded) messages in #commercial-sales asking about a specific
build/case — shipping address, parts, point of contact, payment status, etc. —
should never fall through to personality or get stored as a blind [INSIGHT].
This module gives those inquiries a deterministic answer:

  1. Detect the inquiry intent (`is_inquiry_intent`).
  2. Resolve which customer/build the asker is talking about (Haiku match against
     existing Build + SupportCase records).
  3. Branch on the result:
     - No match: ask the user for customer/product/ship_date and drop a stub
       JSON under `knowledge/commercial_sales/builds/_stubs/` so the next scan
       picks it up. Log a [KNOWLEDGE_GAP] (record=unmatched).
     - Match + field has a value: answer with the value.
     - Match + field empty: tell the asker the field is unset, @-ping the right
       owner (Beck/Meredith/Nate per `BUILD_FIELD_ROLES`), and log a
       [KNOWLEDGE_GAP] with field + record id.

KNOWLEDGE_GAP entries accumulate in #jackbot-knowledge and become the to-do
list for tightening the scanner — repeated missing fields tell us where the
scan needs more reach (PDF parsing, additional email regex, etc.).

PENDING state mirrors the same propose-and-confirm pattern used by
commercial_sales_admin.py / commercial_sales_reply.py — in-memory keyed on
(user_id, channel_id) with a TTL. Lost on Railway restart, which is fine: any
state-bearing reply is short-lived.
"""

from __future__ import annotations

import json
import os
import re
import time
from datetime import datetime
from pathlib import Path
from typing import Optional

import anthropic

from commercial_sales import (
    KNOWLEDGE_DIR as CS_DIR,
    BUILD_FIELD_ROLES,
    SUPPORT_FIELD_ROLES,
    DEFAULT_OWNERS,
    load_builds,
    load_support_cases,
)


STUBS_DIR = CS_DIR / "builds" / "_stubs"

PENDING_TTL = 600  # 10 minutes
PENDING: dict[tuple[str, str], dict] = {}

_client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", ""))


# --- Intent detection -----------------------------------------------------
#
# Permissive keyword gate. Anything that mentions a tracked topic in
# #commercial-sales is worth handing to Haiku for resolution. Haiku is the
# precision layer; this is just the funnel.

_INQUIRY_KEYWORDS = (
    # Shipping / logistics
    "ship", "shipping", "shipped", "address", "addresses", "tracking",
    "carrier", "ship-to", "ship to", "deliver", "delivery",
    # Parts / build
    "part", "parts", "component", "assembly", "build status", "build state",
    # Contacts
    "contact", "point of contact", "poc", "customer contact",
    "email address", "phone",
    # Payment / invoicing
    "invoice", "payment", "paid", "estimate", "quote",
    # Order timing
    "due date", "receive by", "deadline",
    # Hardware identification
    "serial", "serial number", "s/n", "rma",
    # Status
    "status", "where is", "where are", "when will", "when does",
)


def is_inquiry_intent(text: str) -> bool:
    """Permissive gate — return True if the message looks like a customer-build
    inquiry. Specificity is left to Haiku downstream."""
    if not text:
        return False
    low = text.lower()
    return any(kw in low for kw in _INQUIRY_KEYWORDS)


# --- Pending state --------------------------------------------------------


def _now() -> float:
    return time.time()


def _get_pending(user_id: str, channel_id: str) -> Optional[dict]:
    entry = PENDING.get((user_id, channel_id))
    if not entry:
        return None
    if _now() - entry["created"] > PENDING_TTL:
        PENDING.pop((user_id, channel_id), None)
        return None
    return entry


def _set_pending(user_id: str, channel_id: str, state: dict) -> None:
    state["created"] = _now()
    PENDING[(user_id, channel_id)] = state


def _clear_pending(user_id: str, channel_id: str) -> None:
    PENDING.pop((user_id, channel_id), None)


def has_pending(user_id: str, channel_id: str) -> bool:
    p = _get_pending(user_id, channel_id)
    return bool(p) and p.get("kind") == "inquiry"


# --- Haiku helpers --------------------------------------------------------


def _call_claude_json(system: str, user: str, max_tokens: int = 600) -> dict:
    resp = _client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    text = resp.content[0].text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    return json.loads(text)


# Canonical list of fields Haiku is allowed to nominate. Anything not in this
# list gets caught downstream as "unknown_field" so we don't pretend to look up
# things the data model doesn't track.
_BUILD_FIELDS = list(BUILD_FIELD_ROLES.keys()) + [
    "items",  # contents — handled specially
]
_SUPPORT_FIELDS = list(SUPPORT_FIELD_ROLES.keys()) + ["state", "linked_build_gid", "notes"]


EXTRACT_SYSTEM = f"""\
The user is asking a question in BST's #commercial-sales Slack channel about a
customer order or support case. Pull out what they're asking about. Output one
JSON object — no fences, no commentary:

{{
  "customer_hint": "<customer name / product mention from the message, or empty>",
  "product_hint":  "<product or item mention (e.g. 'S0 display unit', 'S3'), or empty>",
  "topic":         "<one short phrase: 'shipping address', 'parts status', 'point of contact', 'invoice', etc.>",
  "field":         "<exact internal field name>",
  "record_kind":   "build" | "support"
}}

`field` MUST be one of these exact strings:
  Build fields:   {", ".join(sorted(set(_BUILD_FIELDS)))}
  Support fields: {", ".join(sorted(set(_SUPPORT_FIELDS)))}

Map natural language → field:
  shipping address / where it ships → ship_to
  tracking / tracking number → tracking_number
  carrier (FedEx, UPS, etc.) → carrier
  when did/does it ship → shipped_date
  parts / part status / parts ordered → parts
  point of contact / customer contact / who at customer → customer_contact
  customer email → customer_email
  invoice / invoice number → invoice_number
  invoice amount / total → invoice_amount
  invoice date → invoice_date
  paid / payment → payment_state
  estimate → estimate_date
  due date / receive by / delivery deadline → receive_by
  build state / where in build → build_state
  ship state / shipped / in transit → ship_state
  customer name → customer
  contents / what's in the order / items → items
  serial number / S/N → serial_number
  RMA → rma_number
  device / what's broken → device
  reported issue → reported_issue
  current status (support case) → state

`record_kind`:
  - "support" if the question is clearly about a unit being repaired / RMA / diagnose / fix
  - "build" otherwise (new orders, shipping out, payment, etc.)
"""


MATCH_SYSTEM = """\
Match a user inquiry to ONE customer build (or support case) from the candidate
list. The candidates are existing records in BST's commercial sales pipeline.

The user mentioned a customer or product (often loosely). Find the best matches
by checking:
  - Customer name (fuzzy: "USAF SOCOM" matches "SOCOM")
  - Asana task name (often contains the product, e.g. "S0 VTOL (Oklahoma)")
  - Items / contents of the order
  - Notes

Output one JSON object — no fences, no commentary:

{
  "matches": [
    {
      "id": "<asana_gid for builds, or case_id for support cases>",
      "label": "<short label: 'Embry-Riddle — 4 S0 VTOL'>",
      "kind": "build" | "support",
      "confidence": "high" | "medium" | "low",
      "why": "<one sentence — what about the candidate matched the inquiry>"
    }
  ]
}

Rules:
- 0 matches → return {"matches": []}.
- 1 confident match → return one entry, confidence "high".
- Multiple plausible matches → return up to 3, sorted by confidence.
- Don't fabricate. If the customer_hint matches nothing, return empty.
- "low" confidence is reserved for very loose matches (e.g. only the product
  type matched, no customer mention).
"""


STUB_CONFIRM_SYSTEM = """\
The user is providing details to stub a new customer build that didn't already
exist in BST's commercial sales pipeline. They typed something like:
"Acme Atmospherics, two S0 display units, needs to ship by June 1"
or maybe just "cancel".

Output one JSON object — no fences, no commentary:

{
  "intent": "fill" | "cancel" | "unrelated",
  "customer":     "<customer name, or empty>",
  "product":      "<short product/items description, or empty>",
  "ship_by":      "<YYYY-MM-DD or empty>",
  "notes":        "<anything else relevant, or empty>"
}

- "cancel" — user said cancel / no / never mind
- "unrelated" — reply is clearly not about this stub
- "fill" — they're providing information (even partial)
"""


# --- Record matching ------------------------------------------------------


def _build_candidate_block(builds, cases) -> str:
    """One line per candidate — customer, label, items summary. Keeps the
    Haiku context window small even with many records."""
    lines = []
    for b in builds:
        items_summary = ""
        if b.items:
            chunks = []
            for it in b.items[:4]:
                q = f"{it.quantity}× " if it.quantity > 1 else ""
                chunks.append(f"{q}{it.description}")
            items_summary = "; items=" + ", ".join(chunks)
        label = b.asana_task_name or b.customer or b.asana_gid
        lines.append(
            f"- kind=build id={b.asana_gid} customer={b.customer!r} "
            f"label={label!r}{items_summary}"
        )
    for c in cases:
        device = c.device or "(device tbd)"
        lines.append(
            f"- kind=support id={c.case_id} customer={c.customer!r} "
            f"device={device!r} state={c.state}"
        )
    return "\n".join(lines)


def _match_record(extracted: dict, builds, cases) -> list[dict]:
    if not builds and not cases:
        return []
    candidate_block = _build_candidate_block(builds, cases)
    if not candidate_block:
        return []
    user_block = (
        f"User inquiry:\n  customer_hint={extracted.get('customer_hint','')!r}\n"
        f"  product_hint={extracted.get('product_hint','')!r}\n"
        f"  topic={extracted.get('topic','')!r}\n\n"
        f"Candidates:\n{candidate_block}"
    )
    try:
        resp = _call_claude_json(MATCH_SYSTEM, user_block, max_tokens=600)
    except Exception:
        return []
    return resp.get("matches", []) or []


# --- Field lookup ---------------------------------------------------------


def _record_by_id(record_id: str, builds, cases):
    for b in builds:
        if b.asana_gid == record_id:
            return ("build", b)
    for c in cases:
        if c.case_id == record_id:
            return ("support", c)
    return (None, None)


def _field_value(record, kind: str, field: str):
    """Return the value of a field on the record, or None if empty/unset.

    `items` and `parts` are lists — return None if empty, else the list.
    """
    if field == "items":
        items = getattr(record, "items", None) or []
        return items or None
    if field == "parts":
        parts = getattr(record, "parts", None) or []
        return parts or None
    val = getattr(record, field, None)
    if val in (None, "", "none"):
        return None
    return val


def _format_value(field: str, value) -> str:
    """Render a field value for display in the answer."""
    if field == "ship_to":
        # ship_to is multi-line; show as-is
        return value.strip()
    if field == "items":
        chunks = []
        for it in value:
            q = f"{it.quantity}× " if it.quantity > 1 else ""
            chunks.append(f"  • {q}{it.description}")
        return "\n".join(chunks)
    if field == "parts":
        chunks = []
        for p in value:
            mark = "✓" if p.received else ("~" if p.ordered else " ")
            v = f" _(from {p.vendor})_" if p.vendor else ""
            chunks.append(f"  [{mark}] {p.name}{v}")
        return "\n".join(chunks)
    if isinstance(value, (list, tuple)):
        return ", ".join(str(v) for v in value)
    return str(value)


# --- Owner resolution -----------------------------------------------------


def _field_owner_role(kind: str, field: str) -> str:
    if kind == "support":
        return SUPPORT_FIELD_ROLES.get(field, "support")
    return BUILD_FIELD_ROLES.get(field, "interface")


def _owner_mention(record, role: str) -> str:
    """Owner name → Slack mention via user_map. Falls back to plain name.

    user_map._user_map is populated by build_user_map(client), which the
    scheduler runs at 8:02am Mon-Fri before the digest. Between Railway
    restart and the first scheduled run, the map is empty and we render
    plain text instead of a @-mention — acceptable (the message still
    reads "Meredith, can you fill it in?"), and the cache warms up
    automatically once any pipeline job runs.
    """
    name = record.owner(role) if record else DEFAULT_OWNERS.get(role, "")
    if not name:
        return "_(unowned)_"
    try:
        from user_map import get_all_users
        users = get_all_users()
    except Exception:
        return name
    lower = name.lower()
    for u in users:
        u_name = (u.get("name") or "").lower()
        if not u_name:
            continue
        if u_name == lower or u_name.split()[0] == lower:
            sid = u.get("slack_user_id")
            if sid:
                return f"<@{sid}>"
    return name


# --- Stub creation --------------------------------------------------------


def _write_stub(payload: dict) -> Path:
    """Drop a placeholder Build JSON the next scan can promote to a real record."""
    STUBS_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    safe_customer = re.sub(r"[^a-zA-Z0-9_-]", "_", payload.get("customer", "stub"))[:40]
    path = STUBS_DIR / f"{stamp}_{safe_customer}.json"
    path.write_text(json.dumps(payload, indent=2))
    return path


# --- Main entry point -----------------------------------------------------


def handle_inquiry(
    text: str,
    user_id: str,
    channel_id: str,
    slack_client,
    asker_name: str,
) -> Optional[str]:
    """Resolve an inquiry. Returns a Slack-ready response string.

    Always returns a response — silent fallthrough was the old failure mode.
    """
    # Extract topic + field
    try:
        extracted = _call_claude_json(EXTRACT_SYSTEM, text, max_tokens=400)
    except Exception:
        return (
            "I couldn't parse that. Try restating with the customer name "
            "and what you want to know (e.g. 'shipping address for the UMES S3')."
        )

    field = (extracted.get("field") or "").strip()
    record_kind_hint = extracted.get("record_kind", "build")

    # Load records
    builds = load_builds()
    cases = load_support_cases()

    # Match
    matches = _match_record(extracted, builds, cases)

    # ----- Branch: no match -> stub flow -----------------------------------
    if not matches:
        topic = extracted.get("topic") or "the order"
        try:
            from knowledge import store_knowledge_gap
            store_knowledge_gap(
                slack_client, field or "unknown", "unmatched", asker_name, text
            )
        except Exception:
            pass

        _set_pending(user_id, channel_id, {
            "kind": "inquiry",
            "stage": "await_stub_details",
            "field": field,
            "topic": topic,
            "original": text,
        })
        hint = extracted.get("customer_hint") or extracted.get("product_hint") or "that order"
        return (
            f"I don't have a record for *{hint}* in the commercial sales pipeline yet — "
            f"so I can't answer about {topic} directly.\n\n"
            f"Reply with: customer name, what they're ordering, and an expected "
            f"ship date — I'll stub it and the next nightly scan will fill in details. "
            f"Or reply *cancel* to skip."
        )

    # ----- Branch: multiple matches -> ask user to pick --------------------
    if len(matches) > 1 and matches[0].get("confidence") != "high":
        _set_pending(user_id, channel_id, {
            "kind": "inquiry",
            "stage": "await_pick_match",
            "field": field,
            "matches": matches,
            "original": text,
            "asker_name": asker_name,
        })
        lines = [f"A few builds could match — which one?"]
        for i, m in enumerate(matches, 1):
            lines.append(f"  {i}. *{m.get('label','?')}* `{m.get('id','?')}`")
            if m.get("why"):
                lines.append(f"     _{m['why']}_")
        lines.append("\nReply with a number, or *cancel*.")
        return "\n".join(lines)

    # ----- Branch: one match -> look up the field --------------------------
    top = matches[0]
    return _answer_for_match(
        top, field, builds, cases, slack_client, asker_name, text
    )


def _answer_for_match(
    match: dict,
    field: str,
    builds,
    cases,
    slack_client,
    asker_name: str,
    original_text: str,
) -> str:
    record_id = match.get("id", "")
    label = match.get("label") or record_id
    kind, record = _record_by_id(record_id, builds, cases)
    if not record:
        return f"_Matched {label} but couldn't load the record — likely a scanner sync gap. Logging it._"

    if not field:
        return (
            f"I matched this to *{label}* but I'm not sure exactly what you're asking. "
            f"Try: 'shipping address for {label}', 'point of contact for {label}', etc."
        )

    # Validate field
    allowed = _BUILD_FIELDS if kind == "build" else _SUPPORT_FIELDS
    if field not in allowed:
        return (
            f"I matched *{label}* but `{field}` isn't a field I track. "
            f"Available: {', '.join(sorted(set(allowed)))}."
        )

    value = _field_value(record, kind, field)

    if value is not None:
        formatted = _format_value(field, value)
        # Multi-line answers get a newline; single-line stay inline.
        if "\n" in formatted:
            return f"*{label}* — {field}:\n{formatted}"
        return f"*{label}* — {field}: {formatted}"

    # Empty field — ping owner + log gap
    role = _field_owner_role(kind, field)
    owner = _owner_mention(record, role)

    try:
        from knowledge import store_knowledge_gap
        store_knowledge_gap(
            slack_client, field, record_id, asker_name, original_text
        )
    except Exception:
        pass

    return (
        f"*{label}* — `{field}` isn't captured on that record yet. "
        f"{owner}, can you fill it in? "
        f"(Reply in this thread with the value and I'll record it for the next scan.)"
    )


def handle_inquiry_followup(
    text: str,
    user_id: str,
    channel_id: str,
    slack_client,
    asker_name: str,
) -> Optional[str]:
    """Parse a top-level reply when an inquiry is pending. Returns:
      - a response string when handled
      - None to fall through to other routing (e.g. unrelated message)
    """
    pending = _get_pending(user_id, channel_id)
    if not pending or pending.get("kind") != "inquiry":
        return None

    stage = pending.get("stage")

    # --- Disambiguation reply ---------------------------------------------
    if stage == "await_pick_match":
        low = text.strip().lower()
        if low in ("cancel", "no", "never mind", "nevermind"):
            _clear_pending(user_id, channel_id)
            return "Cancelled."
        # Try a literal number first
        m = re.match(r"^\s*(\d+)\b", text)
        if m:
            idx = int(m.group(1)) - 1
            matches = pending.get("matches", [])
            if 0 <= idx < len(matches):
                _clear_pending(user_id, channel_id)
                builds = load_builds()
                cases = load_support_cases()
                return _answer_for_match(
                    matches[idx], pending.get("field", ""),
                    builds, cases, slack_client, asker_name,
                    pending.get("original", ""),
                )
        # Otherwise, treat as new inquiry — clear pending and re-run
        _clear_pending(user_id, channel_id)
        return None

    # --- Stub-details reply ------------------------------------------------
    if stage == "await_stub_details":
        try:
            parsed = _call_claude_json(STUB_CONFIRM_SYSTEM, text, max_tokens=400)
        except Exception:
            return None

        intent = parsed.get("intent", "unrelated")
        if intent == "unrelated":
            return None
        if intent == "cancel":
            _clear_pending(user_id, channel_id)
            return "Cancelled — nothing recorded."

        customer = (parsed.get("customer") or "").strip()
        product = (parsed.get("product") or "").strip()
        ship_by = (parsed.get("ship_by") or "").strip()
        notes = (parsed.get("notes") or "").strip()

        if not customer and not product:
            return "I still need at least a customer name or a product description — try again."

        original = pending.get("original", "")
        topic = pending.get("topic", "")
        payload = {
            "kind": "stub",
            "created": datetime.now().isoformat(timespec="seconds"),
            "created_by": asker_name,
            "customer": customer,
            "product": product,
            "ship_by": ship_by or None,
            "notes": notes or None,
            "origin_inquiry": original,
            "origin_topic": topic,
        }
        try:
            path = _write_stub(payload)
        except Exception as e:
            return f"_(Couldn't write stub: {e})_"

        # Audit trail
        try:
            from knowledge import store_entry
            store_entry(
                slack_client, "FEEDBACK",
                f"Commercial-sales stub created by {asker_name}: "
                f"customer={customer!r} product={product!r} "
                f"ship_by={ship_by!r} (from inquiry: {original[:120]!r})",
            )
        except Exception:
            pass

        _clear_pending(user_id, channel_id)
        rel = path.relative_to(CS_DIR.parent.parent) if CS_DIR.parent.parent in path.parents else path
        return (
            f"Stubbed *{customer or product}* — the next nightly scan will pick "
            f"it up and try to enrich it from Asana/email.\n"
            f"_Saved to `{rel}`._"
        )

    return None
