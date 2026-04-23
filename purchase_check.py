"""Budget-aware purchase check ("can I buy $X of Y for project Z?").

Reads a project's structured state from `knowledge/project_state/{code}.json`,
parses the user's question via Haiku for amount/description, fuzzy-matches
the description to SOW budget line items, and applies the approval policy:

  - Unscoped (no project resolved): amount ≤ $50 → approved; else needs approval
  - Scoped + amount > $200 AND not in budget line items → needs approval
  - Over remaining budget (approved − spent − committed) → denied with math
  - Otherwise → approved with budget math

Needs-approval requests should go to Meredith (finance/admin).
"""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Optional

import anthropic


PROJECT_STATE_DIR = Path(__file__).parent / "knowledge" / "project_state"

APPROVAL_OWNER = "Meredith"  # routes "needs approval" messages to her
APPROVAL_OWNER_SLACK_ID = "U06KRHPQSRH"  # Meredith Needham

# Policy thresholds from CLAUDE.md / user direction (2026-04-21):
# - Unscoped purchases > $50 need approval
# - Scoped purchases > $200 that aren't explicitly in the project budget need approval
UNSCOPED_APPROVAL_CEILING = 50.0
SCOPED_UNLISTED_APPROVAL_CEILING = 200.0


# ---------------------------------------------------------------------------
# Intent detection
# ---------------------------------------------------------------------------


_PURCHASE_VERBS = (
    "buy", "bought", "purchase", "spend", "order", "pay for", "expense",
    "charge", "get approved for", "approval for",
)
_PURCHASE_PHRASES = (
    "can i", "can we", "may i", "should i", "do we have budget",
    "is there budget", "is there room", "fit in the budget",
    "cover the cost", "approve",
)
# A $ amount OR "X dollars" OR "X bucks" is required
_MONEY_RE = re.compile(
    r"(?:\$\s?([\d,]+(?:\.\d{1,2})?)(?!\s*(?:k|m)\b)|(?<!\w)([\d,]+(?:\.\d{1,2})?)\s*(?:dollars?|bucks?|usd)\b|\$\s?([\d,]+(?:\.\d+)?)\s*(k|m)\b)",
    re.IGNORECASE,
)


def is_purchase_check_intent(message: str) -> bool:
    low = message.lower()
    if not _MONEY_RE.search(low):
        return False
    has_verb = any(v in low for v in _PURCHASE_VERBS)
    has_phrase = any(p in low for p in _PURCHASE_PHRASES)
    return has_verb or has_phrase


def _parse_amount_from_text(message: str) -> Optional[float]:
    """Best-effort local parse of a dollar amount from the message.

    Haiku handles the canonical extraction; this is a fallback if Haiku is
    unavailable or returns null.
    """
    m = _MONEY_RE.search(message)
    if not m:
        return None
    raw = m.group(1) or m.group(2) or m.group(3)
    if not raw:
        return None
    try:
        val = float(raw.replace(",", ""))
    except ValueError:
        return None
    suffix = (m.group(4) or "").lower()
    if suffix == "k":
        val *= 1_000
    elif suffix == "m":
        val *= 1_000_000
    return val


# ---------------------------------------------------------------------------
# Haiku parse
# ---------------------------------------------------------------------------


PARSE_PROMPT = """\
Extract purchase details from a Slack message. Output ONLY a JSON object:

{
  "amount_usd": number | null,        // the dollar amount being asked about
  "description": string,              // what they want to buy (2-12 words)
  "project_code_override": string|null // if they explicitly name a different project (e.g. "for 350-4"), else null
}

Rules:
- amount_usd is a single number. "$3k" → 3000. "$200 each, need 3" → 600.
- description should be concrete. "propellers for the S3" > "parts".
- Output JSON only, no fences, no prose.
"""


MATCH_LINE_ITEM_PROMPT = """\
You are matching a purchase description to a project budget line item.

I give you:
1. A purchase description (what's being bought)
2. A list of budget line items from the project's SOW/proposal

Output ONE JSON object:
{"matched_category": string|null, "match_reason": string|null}

Rules:
- Match if the description clearly falls within a line item's scope. "propellers" matches "Equipment: props, motors, batteries". "hotel" matches "Travel".
- Return null for matched_category if no line item fits — don't stretch. "Subcontractor support" doesn't match "Materials".
- If there are no line items, return null.
- Output JSON only.
"""


def _haiku_parse(message: str) -> dict:
    """Extract amount + description from the message."""
    try:
        client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
        msg = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=300,
            system=PARSE_PROMPT,
            messages=[{"role": "user", "content": message[:2000]}],
        )
        raw = msg.content[0].text.strip().strip("`")
        raw = re.sub(r"^json\s*", "", raw, flags=re.IGNORECASE)
        return json.loads(raw)
    except Exception:
        return {
            "amount_usd": _parse_amount_from_text(message),
            "description": "unspecified purchase",
            "project_code_override": None,
        }


def _haiku_match_line_item(description: str, line_items: list[dict]) -> dict:
    if not line_items:
        return {"matched_category": None, "match_reason": "no line items in budget"}
    items_blob = "\n".join(
        f"- [{li.get('category','')}] ${float(li.get('amount') or 0):,.0f}: {li.get('description') or ''}"
        for li in line_items
    )
    user_blob = f"Purchase description: {description}\n\nLine items:\n{items_blob}"
    try:
        client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
        msg = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=200,
            system=MATCH_LINE_ITEM_PROMPT,
            messages=[{"role": "user", "content": user_blob[:4000]}],
        )
        raw = msg.content[0].text.strip().strip("`")
        raw = re.sub(r"^json\s*", "", raw, flags=re.IGNORECASE)
        return json.loads(raw)
    except Exception:
        return {"matched_category": None, "match_reason": "match check failed"}


# ---------------------------------------------------------------------------
# State loading
# ---------------------------------------------------------------------------


def _load_state(code: str) -> Optional[dict]:
    if not PROJECT_STATE_DIR.exists():
        return None
    for variant in (code, code.replace("_", "-"), code.replace("-", "_")):
        p = PROJECT_STATE_DIR / f"{variant}.json"
        if p.exists():
            try:
                return json.loads(p.read_text())
            except Exception:
                continue
    return None


# ---------------------------------------------------------------------------
# Policy
# ---------------------------------------------------------------------------


def _format_approved(state: dict, amount: float, description: str, line_match: dict) -> str:
    b = state["budget"]
    remaining = b.get("remaining")
    approved = b.get("approved")
    after = (remaining - amount) if remaining is not None else None
    cat = line_match.get("matched_category")
    lines = [":white_check_mark: *Approved*"]
    lines.append(
        f"Project *[{state['project_code']}] {state['name']}* has ${remaining:,.0f} remaining"
        if remaining is not None and approved is not None
        else f"Project *[{state['project_code']}] {state['name']}*"
    )
    if cat:
        lines.append(f"• Line item match: *{cat}*")
    else:
        lines.append("• No matching budget line item — falls under the unlisted-but-under-$200 threshold")
    lines.append(
        f"• ${amount:,.2f} for {description}"
        + (f" → *${after:,.0f}* remaining after this" if after is not None else "")
    )
    return "\n".join(lines)


def _format_needs_approval(
    state: Optional[dict], amount: float, description: str, reason: str
) -> str:
    lines = [":warning: *Needs approval* — escalating to <@{}|{}>".format(
        APPROVAL_OWNER_SLACK_ID, APPROVAL_OWNER
    )]
    lines.append(f"• ${amount:,.2f} for {description}")
    if state:
        lines.append(f"• Project: *[{state['project_code']}] {state['name']}*")
        rem = state["budget"].get("remaining")
        if rem is not None:
            lines.append(f"• Remaining budget: ${rem:,.0f}")
    lines.append(f"• Reason: {reason}")
    return "\n".join(lines)


def _format_over_budget(state: dict, amount: float, description: str) -> str:
    b = state["budget"]
    remaining = b.get("remaining") or 0
    return (
        f":no_entry: *Over budget*\n"
        f"• ${amount:,.2f} for {description}\n"
        f"• Project *[{state['project_code']}] {state['name']}* has only "
        f"${remaining:,.0f} remaining — this would put us ${amount - remaining:,.0f} over."
    )


def _format_no_budget_data(state: dict, amount: float, description: str) -> str:
    return (
        f":grey_question: *Can't answer yet*\n"
        f"• Project: *[{state['project_code']}] {state['name']}*\n"
        f"• The project's approved budget isn't in the state record yet "
        f"(approved_source=`{state['budget'].get('approved_source')}`).\n"
        f"• Escalating ${amount:,.2f} for {description} to <@{APPROVAL_OWNER_SLACK_ID}|{APPROVAL_OWNER}>."
    )


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------


def handle_purchase_check(
    message: str,
    channel_ctx: Optional[dict],
) -> str:
    parsed = _haiku_parse(message)
    amount = parsed.get("amount_usd") or _parse_amount_from_text(message)
    description = parsed.get("description") or "unspecified purchase"
    override = parsed.get("project_code_override")

    if amount is None:
        return (
            "I see you're asking about a purchase, but I couldn't pull out a dollar amount. "
            "Try: `can we spend $450 on prop hubs for 350-4?`"
        )

    # Resolve project: explicit override in message > channel context
    code = override
    if not code and channel_ctx:
        code = channel_ctx.get("project_code")

    if not code:
        # Unscoped purchase — policy: ≤ $50 auto-approved
        if amount <= UNSCOPED_APPROVAL_CEILING:
            return (
                ":white_check_mark: *Approved* (unscoped)\n"
                f"• ${amount:,.2f} for {description}\n"
                f"• Under the ${UNSCOPED_APPROVAL_CEILING:.0f} unscoped threshold — no approval needed."
            )
        return _format_needs_approval(
            None, amount, description,
            f"unscoped (not tied to a project) and over the ${UNSCOPED_APPROVAL_CEILING:.0f} threshold",
        )

    state = _load_state(code)
    if not state:
        return (
            f":grey_question: Project *{code}* has no structured state record yet. "
            f"Run `python scan.py project_state --mode 1yr` or ask Jack to rebuild it."
        )

    b = state["budget"]
    line_match = _haiku_match_line_item(description, b.get("line_items") or [])

    # Missing approved budget — can't do math; escalate
    if b.get("approved") is None:
        return _format_no_budget_data(state, amount, description)

    remaining = b.get("remaining")
    if remaining is None:
        return _format_no_budget_data(state, amount, description)

    if amount > remaining:
        return _format_over_budget(state, amount, description)

    # Scoped-but-unlisted rule: > $200 AND not matching a line item → escalate
    if amount > SCOPED_UNLISTED_APPROVAL_CEILING and not line_match.get("matched_category"):
        return _format_needs_approval(
            state, amount, description,
            f"over ${SCOPED_UNLISTED_APPROVAL_CEILING:.0f} and not explicitly in the project budget line items",
        )

    return _format_approved(state, amount, description, line_match)
