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

# Root of the general knowledge layer (knowledge/) and the subdirectories worth
# searching when no Build/SupportCase matches an inquiry. Many commercial
# hardware orders are documented here (project registry, budgets, financials)
# but never made it into the commercial-sales pipeline — e.g. Stanford/Acellent
# (project 042-1) lives in its own Asana project and corresponds through
# personal mailboxes, so the commercial-sales scanner (which only walks the
# Commercial Sales Asana project + info@/sales@/support@) never built a record.
# This fallback lets Jack answer from what BST already knows, and seed a stub so
# the next scan promotes it into a tracked Build.
KNOWLEDGE_ROOT = CS_DIR.parent
GENERAL_KNOWLEDGE_DIRS = ["financial/by_project", "budgets", "projects"]
_GK_MAX_FILES = 3          # how many candidate files to feed Haiku
_GK_MAX_CHARS = 6000       # per-file truncation
_PROJECT_CODE_RX = re.compile(r"(\d{3}[_-]\d{1,2})")

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


# --- Update intent detection ---------------------------------------------
#
# Action verbs that suggest the user wants to mutate a record. Followed by
# Haiku to extract the structured {target, field, value} tuples. Gate stays
# permissive so we don't drop legitimate updates phrased loosely.

_UPDATE_VERB_PATTERNS = [
    r"\badd\s+\S.*\b(?:as|to|on)\b",        # "add Dan as owner to X"
    r"\bset\s+\S",                          # "set ship_to for X to ..."
    r"\bmark\s+\S.*\b(?:complete|completed|done|finished|shipped|delivered|paid|invoiced)\b",
    r"\bchange\s+\S.*\bto\b",
    r"\bupdate\s+\S",
    r"\breplace\s+\S.*\bwith\b",
    r"\breassign\s+\S",
    r"\b(?:invoice|invoiced|paid|shipped|delivered|complete[d]?)\b\s+(?:the|on|for)?\s*\S+",
    r"\btracking\s+\S",                     # "tracking 1Z999... for X"
    r"\bshift\s+\S.*\b(?:due|deadline|ship)\b",
    r"\bmove\s+\S.*\b(?:due|deadline|ship)\b",
    # Implicit items/contents updates — "the NASA S2 simulator includes X, Y, Z"
    # or "S3 comes with EO/IR gimbal". Haiku maps these to the items field.
    r"\b(?:includes|including|contains|consists\s+of|comes\s+with|comprised\s+of)\b",
]
_UPDATE_INTENT_RE = re.compile("|".join(_UPDATE_VERB_PATTERNS), re.IGNORECASE)


def is_update_intent(text: str) -> bool:
    """Permissive gate — return True if the message looks like an update
    command targeted at a customer build/case in #commercial-sales.

    Strictly excludes questions (those go to is_inquiry_intent). The verb
    pattern requires an action word + a target token, so "let's mark it done"
    in chat won't fire unless followed by a record reference.
    """
    if not text:
        return False
    if "?" in text:
        return False
    return bool(_UPDATE_INTENT_RE.search(text))


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


_PENDING_KINDS = ("inquiry", "update_proposal")


def has_pending(user_id: str, channel_id: str) -> bool:
    """True when this module is waiting on a follow-up from this user in this
    channel — either an inquiry disambiguation/stub flow OR an update propose-
    and-confirm. Routing layer calls this before normal intent dispatch so the
    follow-up text doesn't get misclassified."""
    p = _get_pending(user_id, channel_id)
    return bool(p) and p.get("kind") in _PENDING_KINDS


def handle_followup(
    text: str,
    user_id: str,
    channel_id: str,
    slack_client,
    asker_name: str,
) -> Optional[str]:
    """Dispatcher for any pending follow-up from this module. Returns the
    Slack-ready response, or None if the pending state didn't match (caller
    should fall through to normal routing).
    """
    pending = _get_pending(user_id, channel_id)
    if not pending:
        return None
    kind = pending.get("kind")
    if kind == "inquiry":
        return handle_inquiry_followup(
            text, user_id, channel_id, slack_client, asker_name
        )
    if kind == "update_proposal":
        return handle_update_followup(
            text, user_id, channel_id, slack_client, asker_name
        )
    return None


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
    return _loads_tolerant(text)


def _loads_tolerant(text: str) -> dict:
    """Parse the first complete JSON object out of `text`, ignoring trailing
    prose. Strict json.loads() raises 'Extra data' when Haiku appends a
    sentence after the JSON; this finds the first balanced {...} block."""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    start = text.find("{")
    if start < 0:
        return json.loads(text)
    depth = 0
    in_str = False
    escape = False
    for i in range(start, len(text)):
        ch = text[i]
        if in_str:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return json.loads(text[start:i + 1])
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


def _match_record(extracted: dict, builds, cases, recent_context: str = "") -> list[dict]:
    if not builds and not cases:
        return []
    candidate_block = _build_candidate_block(builds, cases)
    if not candidate_block:
        return []
    context_block = ""
    if recent_context.strip():
        # Lets the matcher resolve vague references ("the shipment", "it") to the
        # order the channel was just discussing.
        context_block = (
            "\n\nRecent #commercial-sales discussion (newest last) — use this to "
            "resolve vague references like 'the shipment' to the customer being "
            "talked about:\n" + recent_context.strip()[-2000:]
        )
    user_block = (
        f"User inquiry:\n  customer_hint={extracted.get('customer_hint','')!r}\n"
        f"  product_hint={extracted.get('product_hint','')!r}\n"
        f"  topic={extracted.get('topic','')!r}\n\n"
        f"Candidates:\n{candidate_block}"
        f"{context_block}"
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


# --- General-knowledge fallback -------------------------------------------


GENERAL_KB_SYSTEM = """\
The user asked a question in BST's #commercial-sales Slack channel, but it
didn't match any tracked customer Build or SupportCase. Below is BST project
documentation (financials, budgets, project registry) that mentions the
customer/product the user named. Use ONLY this documentation to answer.

Output one JSON object — no fences, no commentary:

{
  "found":              true | false,
  "answer":             "<a concise Slack-ready answer to the user's question, or empty if the docs don't cover it>",
  "is_commercial_order":true | false,
  "customer":           "<customer/organization name>",
  "product":            "<short product/items description, e.g. 'S2 UAS kit: wing, fuselage, nosecone'>",
  "project_code":       "<project code like 042-1 if visible, else empty>",
  "notes":              "<one-line context worth seeding a tracking record with>"
}

Rules:
- "found"=true only if the documentation actually addresses the customer/order
  the user asked about. If the files are unrelated, return found=false.
- "is_commercial_order"=true when this is BST SELLING hardware/a system to a
  customer (PO, invoice, equipment purchase, kit, build) — NOT a funded R&D
  proposal / SBIR / grant effort.
- Keep "answer" factual and short. If the specific field the user wants (e.g. a
  shipping address) isn't in the docs, say what IS known and note the gap.
- Never invent values not present in the documentation.
"""


def _gk_hints(extracted: dict, text: str, recent_context: str = "") -> list[str]:
    """Distinct lowercase hint tokens to match against knowledge files."""
    raw = " ".join([
        extracted.get("customer_hint") or "",
        extracted.get("product_hint") or "",
    ]).strip()
    toks = set()
    for w in re.findall(r"[A-Za-z]{3,}", raw):
        toks.add(w.lower())
    # A couple of salient proper nouns from the message itself (capitalized
    # words), which often carry the customer name even when extraction missed
    # it. Strip Slack mentions first — `<@U…|Meredith Needham>` would otherwise
    # leak the owner's name as a hint and match half the corpus. Also fold in
    # proper nouns from recent channel discussion so a context-only reference
    # ("FedEx will pick up the shipment tomorrow" right after a Stanford thread)
    # still resolves.
    dementioned = re.sub(r"<@[^>]+>", " ", (text or "") + " " + (recent_context or ""))
    for w in re.findall(r"\b([A-Z][a-zA-Z]{2,})\b", dementioned):
        toks.add(w.lower())
    # Drop generic words + BST employee/owner names (those match everywhere and
    # don't identify a customer).
    stop = {"the", "for", "and", "ship", "shipment", "order", "build", "uas",
            "customer", "delivery", "deliver", "address", "status", "invoice",
            "payment", "parts", "contact", "tracking", "system", "research"}
    for name in DEFAULT_OWNERS.values():
        stop.add(name.lower())
    stop.update({"meredith", "beck", "nate", "dan", "josh", "joshua", "jack",
                 "maciej", "alex", "needham", "cotter", "fromm", "elston",
                 "prendergast", "stachura", "lomis"})
    return [t for t in toks if t not in stop]


def _search_general_knowledge(hints: list[str]) -> list[Path]:
    """Rank knowledge files by how many distinct hint tokens they contain
    (filename matches weighted higher). Returns the top _GK_MAX_FILES paths."""
    if not hints:
        return []
    scored: list[tuple[int, Path]] = []
    for sub in GENERAL_KNOWLEDGE_DIRS:
        d = KNOWLEDGE_ROOT / sub
        if not d.is_dir():
            continue
        for path in d.glob("*.md"):
            try:
                content = path.read_text(errors="ignore").lower()
            except Exception:
                continue
            name = path.name.lower()
            score = 0
            for h in hints:
                if h in content:
                    score += 1
                if h in name:
                    score += 2
            if score:
                scored.append((score, path))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [p for _, p in scored[:_GK_MAX_FILES]]


def _try_general_knowledge_answer(
    extracted: dict, text: str, user_id: str, channel_id: str,
    slack_client, asker_name: str, recent_context: str = "",
) -> Optional[str]:
    """Answer an unmatched inquiry from the general knowledge layer and, when it
    looks like a real commercial order, seed a stub so the next scan tracks it.
    Returns a Slack-ready string, or None to let the normal stub flow run."""
    hints = _gk_hints(extracted, text, recent_context)
    files = _search_general_knowledge(hints)
    if not files:
        return None

    doc_blocks = []
    for p in files:
        try:
            body = p.read_text(errors="ignore")[:_GK_MAX_CHARS]
        except Exception:
            continue
        doc_blocks.append(f"--- FILE: {p.relative_to(KNOWLEDGE_ROOT)} ---\n{body}")
    if not doc_blocks:
        return None

    user_block = (
        f"User question:\n{text}\n\n"
        f"What they're asking about: {extracted.get('topic','')!r}\n\n"
        f"Documentation:\n" + "\n\n".join(doc_blocks)
    )
    try:
        obj = _call_claude_json(GENERAL_KB_SYSTEM, user_block, max_tokens=600)
    except Exception:
        return None

    if not obj.get("found"):
        return None

    answer = (obj.get("answer") or "").strip()
    customer = (obj.get("customer") or "").strip()
    product = (obj.get("product") or "").strip()
    project_code = (obj.get("project_code") or "").strip()
    if not project_code:
        # Recover the code from the top filename (e.g. 042_1.md → 042-1).
        m = _PROJECT_CODE_RX.search(files[0].name)
        if m:
            project_code = m.group(1).replace("_", "-")
    notes = (obj.get("notes") or "").strip()

    parts = []
    if answer:
        parts.append(answer)
    else:
        parts.append(
            f"I don't have *{customer or 'that'}* in the commercial-sales pipeline, "
            f"but it's documented in BST's project records"
            + (f" (project {project_code})" if project_code else "")
            + " — though that file doesn't cover what you asked."
        )

    # Seed a stub so the next scan promotes it into a tracked Build, but only
    # when it actually reads as a commercial hardware order.
    if obj.get("is_commercial_order") and (customer or product):
        payload = {
            "kind": "stub",
            "created": datetime.now().isoformat(timespec="seconds"),
            "created_by": "jack-bot (general-knowledge fallback)",
            "customer": customer,
            "product": product,
            "ship_by": None,
            "project_code": project_code or None,
            "notes": notes or None,
            "origin": "general_knowledge",
            "origin_inquiry": text,
            "source_files": [str(p.relative_to(KNOWLEDGE_ROOT)) for p in files],
        }
        try:
            _write_stub(payload)
            parts.append(
                f"_I've stubbed *{customer or product}*"
                + (f" (project {project_code})" if project_code else "")
                + " so the next nightly scan can pull it into the pipeline._"
            )
            from knowledge import store_entry
            store_entry(
                slack_client, "FEEDBACK",
                f"Commercial-sales stub auto-created from general knowledge for "
                f"{customer!r} (project {project_code or '?'}) — was documented in "
                f"{', '.join(payload['source_files'])} but missing from the pipeline. "
                f"Triggered by inquiry from {asker_name}: {text[:120]!r}",
            )
        except Exception:
            pass

    return "\n\n".join(parts)


# --- Main entry point -----------------------------------------------------


def _recent_channel_text(slack_client, channel_id: str, exclude_ts: str = "",
                         limit: int = 12) -> str:
    """Concatenated text of the last few #commercial-sales messages (oldest
    first), used to resolve context-dependent references. Best-effort — returns
    '' on any failure."""
    try:
        resp = slack_client.conversations_history(channel=channel_id, limit=limit)
        msgs = resp.get("messages", []) or []
    except Exception:
        return ""
    lines = []
    for m in reversed(msgs):  # oldest → newest
        if m.get("ts") == exclude_ts:
            continue
        t = (m.get("text") or "").strip()
        if t:
            lines.append(t[:300])
    return "\n".join(lines)


def handle_inquiry(
    text: str,
    user_id: str,
    channel_id: str,
    slack_client,
    asker_name: str,
    respond_when_unresolved: bool = True,
) -> Optional[str]:
    """Resolve an inquiry. Returns a Slack-ready response string, or None.

    `respond_when_unresolved` controls the terminal branch: when the message
    can't be matched to a tracked record AND the general knowledge layer can't
    answer it, we either prompt to stub it (True — the asker clearly addressed
    the bot) or stay SILENT (False — ambient channel chatter / jokes). Emitting
    the canned "I don't have a record…" deflection to undirected chatter is what
    made the bot mockable; silence is strictly better when we can't help.
    """
    # Cheap guard: never respond to a paste/echo of the bot's own deflection.
    if text.lstrip().lower().startswith("i don't have a record"):
        return None

    # Recent channel discussion — lets vague references resolve to the order
    # under active discussion ("the shipment" → the customer named 5 min ago).
    recent_context = _recent_channel_text(slack_client, channel_id, exclude_ts="")

    # Extract topic + field
    try:
        extracted = _call_claude_json(EXTRACT_SYSTEM, text, max_tokens=400)
    except Exception:
        return (
            "I couldn't parse that. Try restating with the customer name "
            "and what you want to know (e.g. 'shipping address for the UMES S3')."
        ) if respond_when_unresolved else None

    field = (extracted.get("field") or "").strip()
    record_kind_hint = extracted.get("record_kind", "build")

    # Load records
    builds = load_builds()
    cases = load_support_cases()

    # Match (with recent context to resolve vague references)
    matches = _match_record(extracted, builds, cases, recent_context=recent_context)

    # ----- Branch: no match -> general knowledge, then stub flow -----------
    if not matches:
        # Before giving up, check the broader knowledge layer — many real
        # commercial orders (e.g. Stanford/Acellent 042-1) are documented in
        # financials/budgets/registry but never entered the pipeline.
        gk = _try_general_knowledge_answer(
            extracted, text, user_id, channel_id, slack_client, asker_name,
            recent_context=recent_context,
        )
        if gk:
            return gk

        # Couldn't resolve it anywhere. Stay silent on undirected chatter rather
        # than firing the canned deflection that gets the bot mocked.
        if not respond_when_unresolved:
            return None

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


# --- Update propose-and-confirm flow -------------------------------------
#
# Top-level #commercial-sales messages like "add Dan as owner to Canadian
# Defense Forces" used to fall through to is_work_update and get a fake
# "Got it — stored." ack while losing the actual write. This flow gives
# those messages the same propose-and-confirm treatment as a threaded
# reply — Haiku extracts (target, field, value) tuples, we resolve each
# target via the inquiry matcher, then propose the edits and wait for
# confirmation. On accept, we apply via the reply module's validated
# apply/save plumbing.

UPDATE_PARSE_SYSTEM = """\
You parse a Slack message in BST's #commercial-sales channel that is asking
to UPDATE one or more customer builds or support cases. The message may
reference multiple records ("add Dan as owner to A and B" = two updates).

Output one JSON object — no fences, no commentary:

{
  "updates": [
    {
      "target": "<customer or product or task name as written in the message>",
      "field":  "<field name from allowed list>",
      "value":  <new value>,
      "rationale": "<one short sentence>"
    }
  ],
  "ambiguous": ["<things you couldn't resolve>"]
}

Allowed fields (Build):  customer, customer_contact, customer_email,
  receive_by, ship_to, items, parts, payment_state, build_state, ship_state,
  estimate_date, invoice_date, invoice_amount, invoice_number, paid_date,
  tracking_number, carrier, shipped_date, owners, notes.
Allowed fields (SupportCase): customer, customer_contact, customer_email,
  device, serial_number, reported_issue, state, rma_number, received_date,
  shipped_back_date, tracking_number, carrier, linked_build_gid, owners, notes.

State-machine enums (MUST match exactly, never invent):
  payment_state: none, estimate_sent, invoice_sent, paid
  build_state:   none, parts_ordered, in_assembly, in_qc, complete, packaged
  ship_state:    none, awaiting_pickup, in_transit, delivered
  (case) state:  intake, diagnosing, rma_issued, received, under_repair,
                 in_qc, complete, shipped

Multi-target patterns:
  "add Dan as owner to A and B" → emit two entries, same field/value, target=A and target=B
  "mark A and B complete" → two entries (or four if you also emit shipped_date / build_state)

Owners — value is a PARTIAL dict containing only the roles to override:
  - "add X as owner" (no role specified) → {"interface": "X"} (interface is
    the customer-relationship role; this is the right default when the user
    doesn't say "as build owner" or "as billing contact")
  - "add X as build owner" / "X is doing assembly" → {"build": "X"}
  - "X handles billing" / "X is the invoice owner" → {"invoicing": "X"}
  - "X owns support" → {"support": "X"}

Common-phrase interpretation for Build records (when no other context):
  "mark X complete / done / shipped / delivered" →
    Emit BOTH:
      {field: "ship_state", value: "delivered"}
      {field: "shipped_date", value: "<today>"}  (caller injects today's date)
    If user implies the build (not just the order) is finished, ALSO emit:
      {field: "build_state", value: "complete"}
    If user implies payment was received ("paid / settled"), ALSO emit:
      {field: "payment_state", value: "paid"}
      {field: "paid_date", value: "<today>"}

For SupportCase: "mark X complete" → {field: "state", value: "complete"};
  "shipped back to customer" → {field: "state", value: "shipped"}.

Dates: emit "YYYY-MM-DD". For "today" use the date the caller injects.

When the target is ambiguous (no record reference at all), put a note in
`ambiguous` and emit no update for that piece.

Never invent values not present in the message. If unsure, leave it for
the user to clarify rather than fabricating.
"""


UPDATE_CONFIRM_SYSTEM = """\
The user just replied to a proposed-updates message. Decide their intent.
Output one JSON object — no fences, no commentary:

{
  "intent": "accept_all" | "accept_subset" | "reject" | "modify" | "unrelated",
  "accepted_indices": [int, ...],
  "modification_request": "string"
}

- "accept_all"  — yes / confirm / apply
- "accept_subset" — pick by number (1-based); fill accepted_indices
- "reject"      — cancel / no / never mind
- "modify"      — restated; fill modification_request with the new phrasing
- "unrelated"   — message is off-topic for this proposal
"""


def _to_reply_kind(k: str) -> str:
    """commercial_sales_inquiry uses 'support' for SupportCase, but the
    reply module's _validate_update + _apply_update_to_record use 'case'.
    Convert at the boundary so both modules stay independent."""
    return "case" if k == "support" else k


def _match_target_to_record(target: str, builds, cases) -> list[dict]:
    """Run the inquiry matcher with target as the customer/product hint."""
    extracted = {"customer_hint": target, "product_hint": target, "topic": "update"}
    return _match_record(extracted, builds, cases)


def _format_update_value(value) -> str:
    if value is None:
        return "_(none)_"
    if isinstance(value, dict):
        return ", ".join(f"{k}={v!r}" for k, v in value.items())
    if isinstance(value, (list, tuple)):
        return ", ".join(str(v) for v in value)
    return str(value)


def _format_owner_change(record, value) -> str:
    """Render owner updates as before→after for clarity."""
    if not isinstance(value, dict):
        return _format_update_value(value)
    parts = []
    current = dict(record.owners or {}) if record else {}
    for role, new_name in value.items():
        old = current.get(role) or DEFAULT_OWNERS.get(role, "—")
        parts.append(f"{role}: {old} → {new_name}")
    return "; ".join(parts)


def handle_update_propose(
    text: str,
    user_id: str,
    channel_id: str,
    slack_client,
    asker_name: str,
) -> Optional[str]:
    """Parse an update message, resolve targets, propose changes.

    Returns the proposal text to post, or a clarification request if
    targets couldn't be resolved.
    """
    today = datetime.now().strftime("%Y-%m-%d")
    user_block = f"Today is {today}.\n\nUser message:\n{text}"
    try:
        parsed = _call_claude_json(UPDATE_PARSE_SYSTEM, user_block, max_tokens=800)
    except Exception as e:
        return f"_(I couldn't parse that update — try again? Error: {e})_"

    raw_updates = parsed.get("updates") or []
    ambiguous = parsed.get("ambiguous") or []
    if not raw_updates and not ambiguous:
        return None  # Haiku said nothing — let routing fall through

    builds = load_builds()
    cases = load_support_cases()

    # Resolve each (target, field, value) → concrete (record, field, value).
    # When a target matches multiple candidates, stash an ambiguity entry
    # rather than silently picking the top result.
    resolved: list[dict] = []
    unresolved: list[str] = list(ambiguous)
    target_cache: dict[str, list[dict]] = {}

    for u in raw_updates:
        target = (u.get("target") or "").strip()
        field = (u.get("field") or "").strip()
        value = u.get("value")
        rationale = (u.get("rationale") or "").strip()
        if not target or not field:
            unresolved.append(f"missing target or field on update {u!r}")
            continue

        # Per-target match cache so "add Dan to A and B" doesn't re-call Haiku
        # for each field-tuple on the same target.
        if target not in target_cache:
            target_cache[target] = _match_target_to_record(target, builds, cases)
        matches = target_cache[target]

        if not matches:
            unresolved.append(f"no record matched '{target}'")
            continue
        if len(matches) > 1 and matches[0].get("confidence") != "high":
            label_list = ", ".join(
                f"{m.get('label','?')} ({m.get('id','?')})" for m in matches[:3]
            )
            unresolved.append(
                f"'{target}' could match multiple: {label_list} — re-state with a more specific name"
            )
            continue

        top = matches[0]
        kind, record = _record_by_id(top.get("id", ""), builds, cases)
        if not record:
            unresolved.append(f"matched '{target}' to {top.get('id')} but couldn't load it")
            continue

        # Validate up front so we don't propose junk
        validator_kind = _to_reply_kind(kind)
        try:
            from commercial_sales_reply import _validate_update
        except Exception as e:
            return f"_(Couldn't import update validator: {e})_"
        ok, reason = _validate_update(validator_kind, {"field": field, "value": value})
        if not ok:
            unresolved.append(f"{top.get('label','?')}: {reason}")
            continue

        resolved.append({
            "record_id": top.get("id"),
            "record_kind": kind,           # "build" | "support"
            "validator_kind": validator_kind,  # "build" | "case"
            "label": top.get("label") or top.get("id"),
            "field": field,
            "value": value,
            "rationale": rationale,
        })

    if not resolved:
        body = "_I couldn't resolve any of that to a record I track."
        if unresolved:
            body += "_\n\n_Issues:_\n" + "\n".join(f"  • {u}" for u in unresolved)
        else:
            body += "_"
        return body

    _set_pending(user_id, channel_id, {
        "kind": "update_proposal",
        "stage": "await_confirm",
        "resolved": resolved,
        "unresolved": unresolved,
        "original": text,
    })

    # Build proposal message — group by record so two changes to the same
    # Build show under one heading.
    by_record: dict[str, list[dict]] = {}
    for r in resolved:
        by_record.setdefault(r["record_id"], []).append(r)

    lines = ["Proposed updates:"]
    idx = 1
    for record_id, items in by_record.items():
        label = items[0]["label"]
        lines.append(f"\n*{label}* `{record_id}`")
        # Reload the record so we can render owner diffs nicely
        kind, record = _record_by_id(record_id, builds, cases)
        for r in items:
            if r["field"] == "owners":
                value_str = _format_owner_change(record, r["value"])
            else:
                value_str = _format_update_value(r["value"])
            lines.append(f"  {idx}. `{r['field']}` → {value_str}")
            if r["rationale"]:
                lines.append(f"     _{r['rationale']}_")
            idx += 1
    if unresolved:
        lines.append("\n_Couldn't resolve:_")
        for u in unresolved:
            lines.append(f"  • {u}")
    lines.append("\nReply *yes* to apply, *no* to cancel, *1,3* to apply specific items, or restate to refine.")
    return "\n".join(lines)


def handle_update_followup(
    text: str,
    user_id: str,
    channel_id: str,
    slack_client,
    asker_name: str,
) -> Optional[str]:
    """Apply, reject, or refine a pending update proposal.

    Returns the response text, or None if the reply is unrelated (router
    falls through to normal handling).
    """
    pending = _get_pending(user_id, channel_id)
    if not pending or pending.get("kind") != "update_proposal":
        return None

    resolved = pending.get("resolved") or []
    if not resolved:
        _clear_pending(user_id, channel_id)
        return None

    summary = "\n".join(
        f"{i+1}. {r['label']} — {r['field']} = {r['value']}"
        for i, r in enumerate(resolved)
    )
    parse_input = f"Pending update proposal:\n{summary}\n\nUser reply:\n{text}"
    try:
        intent_obj = _call_claude_json(UPDATE_CONFIRM_SYSTEM, parse_input, max_tokens=300)
    except Exception:
        return None

    intent = intent_obj.get("intent", "unrelated")
    if intent == "unrelated":
        return None
    if intent == "reject":
        _clear_pending(user_id, channel_id)
        return "Cancelled — no changes applied."

    if intent == "modify":
        mod = (intent_obj.get("modification_request") or text).strip()
        _clear_pending(user_id, channel_id)
        # Re-run the propose flow with the modified instruction
        return handle_update_propose(mod, user_id, channel_id, slack_client, asker_name)

    if intent == "accept_subset":
        indices = intent_obj.get("accepted_indices") or []
        to_apply = [resolved[i-1] for i in indices if 1 <= i <= len(resolved)]
    else:
        # accept_all
        to_apply = resolved

    if not to_apply:
        _clear_pending(user_id, channel_id)
        return "Nothing to apply."

    # Apply each — load fresh record, mutate, save.
    try:
        from commercial_sales_reply import _apply_update_to_record, _save_record
    except Exception as e:
        return f"_(Couldn't import update apply: {e})_"

    builds = load_builds()
    cases = load_support_cases()
    applied: list[str] = []
    failures: list[str] = []
    seen_records: dict[str, tuple[str, object]] = {}

    for r in to_apply:
        rid = r["record_id"]
        if rid not in seen_records:
            kind, record = _record_by_id(rid, builds, cases)
            if not record:
                failures.append(f"{r['label']}: record gone")
                continue
            seen_records[rid] = (kind, record)
        kind, record = seen_records[rid]
        try:
            _apply_update_to_record(
                r["validator_kind"], record,
                {"field": r["field"], "value": r["value"]},
            )
            applied.append(f"{r['label']} — {r['field']}")
        except Exception as e:
            failures.append(f"{r['label']} — {r['field']}: {e}")

    # Save each touched record once
    for kind, record in seen_records.values():
        try:
            _save_record(_to_reply_kind(kind), record)
        except Exception as e:
            failures.append(f"save failed: {e}")

    _clear_pending(user_id, channel_id)

    # Audit trail
    try:
        from knowledge import store_entry
        original = pending.get("original", "")[:160]
        store_entry(
            slack_client, "FEEDBACK",
            f"Commercial-sales top-level update by {asker_name}: "
            f"applied=[{', '.join(applied) or 'none'}] "
            f"failed=[{', '.join(failures) or 'none'}] "
            f"(from: {original!r})",
        )
    except Exception:
        pass

    lines = []
    if applied:
        lines.append(f":white_check_mark: Applied:")
        for a in applied:
            lines.append(f"  • {a}")
    if failures:
        lines.append(f":warning: Failed:")
        for f in failures:
            lines.append(f"  • {f}")
    lines.append("_Next nightly scan will pick up the JSON changes; tomorrow's digest will reflect them._")
    return "\n".join(lines)
