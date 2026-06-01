"""Admin commands for #commercial-sales: show-filtered + force-include.

These are top-level (not threaded) messages in #commercial-sales that let
the BST team:

  - Ask "what got filtered?" → bot reads knowledge/commercial_sales/_filtered.md
    and posts the table so users can spot anything that was filtered too
    aggressively.
  - Force-include a build: "track this: <customer or gid>" → bot adds the
    Asana gid to knowledge/commercial_sales/_force_include.json. The
    scanner reads this list on its next run and bypasses the
    is_customer_build filter for those gids — so opportunities the bot
    would normally drop appear in the morning digest.

Force-include uses the same propose-and-confirm pattern as
commercial_sales_reply.py — PENDING is keyed on (user_id, channel_id)
since these are top-level messages, not threaded replies.
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

from commercial_sales import KNOWLEDGE_DIR as CS_DIR


FILTERED_PATH = CS_DIR / "_filtered.md"
FORCE_INCLUDE_PATH = CS_DIR / "_force_include.json"
FORCE_EXCLUDE_PATH = CS_DIR / "_force_exclude.json"
UNMAPPED_PATH = CS_DIR / "_unmapped_customers.md"

PENDING_TTL = 600  # 10 minutes
PENDING: dict[tuple[str, str], dict] = {}

_client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", ""))


# --- intent detection ------------------------------------------------------


SHOW_FILTERED_RX = re.compile(
    r"\b(?:show|what|which|list).*\bfilter(?:ed)?\b"
    r"|\bfiltered\s+(?:builds?|opportunities|leads?)\b"
    r"|\bwhat\s+got\s+filtered\b",
    re.IGNORECASE,
)

FORCE_INCLUDE_RX = re.compile(
    r"^(?:track|include|force[-_ ]include|surface)\s+(?:this|that)?\s*:?\s*(.+)$",
    re.IGNORECASE,
)

CREATE_TASK_RX = re.compile(
    r"^(?:create|add|new)\s+(?:an?\s+)?(?:asana\s+)?(?:bd\s+pipeline\s+)?task\s*"
    r"(?:for|:)?\s*(.+)$",
    re.IGNORECASE,
)


def is_show_filtered_intent(text: str) -> bool:
    return bool(SHOW_FILTERED_RX.search(text or ""))


def parse_force_include_target(text: str) -> Optional[str]:
    """Return the target string ('INSTAAR S3', '1208663032843969', etc.)
    when the message looks like a force-include command. None otherwise."""
    if not text:
        return None
    m = FORCE_INCLUDE_RX.match(text.strip())
    if not m:
        return None
    target = (m.group(1) or "").strip()
    return target or None


def parse_create_task_target(text: str) -> Optional[str]:
    """Return the customer/domain string when the message looks like a
    create-task command ('create task for Acme', 'add task: nutshell.com').
    None otherwise."""
    if not text:
        return None
    m = CREATE_TASK_RX.match(text.strip())
    if not m:
        return None
    target = (m.group(1) or "").strip()
    return target or None


# --- pending state ---------------------------------------------------------


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
    return _get_pending(user_id, channel_id) is not None


# --- _filtered.md parsing --------------------------------------------------


def _parse_filtered_table() -> list[dict]:
    """Return [{gid, date, label, reason}] from the builds-filtered table."""
    if not FILTERED_PATH.exists():
        return []
    out: list[dict] = []
    in_builds_section = False
    in_table = False
    for line in FILTERED_PATH.read_text().splitlines():
        stripped = line.strip()
        if stripped.startswith("## Builds filtered"):
            in_builds_section = True
            in_table = False
            continue
        if stripped.startswith("##") and in_builds_section:
            # Hit the next section (e.g. support filter)
            break
        if not in_builds_section:
            continue
        if stripped.startswith("| Gid") or stripped.startswith("| Date"):
            in_table = True
            continue
        if in_table and stripped.startswith("|----"):
            continue
        if in_table and stripped.startswith("|"):
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            if len(cells) >= 4:
                gid = cells[0].strip("`").strip()
                if gid in ("—", ""):
                    gid = None
                out.append({
                    "gid": gid,
                    "date": cells[1],
                    "label": cells[2],
                    "reason": cells[3],
                })
    return out


# --- force_include persistence ---------------------------------------------


def _load_force_include() -> dict:
    """Return {gid: {added_at, added_by_slack_id, label}} from the JSON file.

    Empty dict if file doesn't exist. The scanner uses this to override the
    is_customer_build filter for specific Asana task gids.
    """
    if not FORCE_INCLUDE_PATH.exists():
        return {}
    try:
        data = json.loads(FORCE_INCLUDE_PATH.read_text())
        return data.get("force_include", {}) or {}
    except Exception:
        return {}


def _save_force_include(force_map: dict) -> None:
    CS_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "updated_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "force_include": force_map,
    }
    FORCE_INCLUDE_PATH.write_text(json.dumps(payload, indent=2))


def get_force_include_gids() -> set[str]:
    """Public helper for the scanner — returns the set of gids to force-include."""
    return set(_load_force_include().keys())


# --- force_exclude persistence ---------------------------------------------


def _load_force_exclude() -> dict:
    """Return {gid: {added_at, added_by, reason}} from the JSON file.

    Empty dict if file doesn't exist. The scanner uses this to hard-drop
    specific Asana task gids that the is_customer_build filter would otherwise
    KEEP — e.g. a hardware-looking opportunity that is actually part of an
    SBIR/grant effort and belongs in #grants-and-funding, not this digest.
    """
    if not FORCE_EXCLUDE_PATH.exists():
        return {}
    try:
        data = json.loads(FORCE_EXCLUDE_PATH.read_text())
        return data.get("force_exclude", {}) or {}
    except Exception:
        return {}


def _save_force_exclude(exclude_map: dict) -> None:
    CS_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "updated_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "force_exclude": exclude_map,
    }
    FORCE_EXCLUDE_PATH.write_text(json.dumps(payload, indent=2))


def get_force_exclude_gids() -> set[str]:
    """Public helper for the scanner — returns the set of gids to force-drop."""
    return set(_load_force_exclude().keys())


# --- show-filtered handler -------------------------------------------------


def handle_show_filtered() -> str:
    """Render the current _filtered.md content for posting to Slack.

    Slack hard-caps individual messages at 40k chars. We keep the response
    compact: build a top-N table of the most recent filter decisions plus
    a hint about how to force-include.
    """
    entries = _parse_filtered_table()
    if not entries:
        return (
            "_No filter decisions on disk yet — `knowledge/commercial_sales/_filtered.md` "
            "is empty. Run a scan first._"
        )

    # Sort: most recent date first, then by label
    def _sort_key(e):
        return (e.get("date") or "", e.get("label") or "")

    sorted_entries = sorted(entries, key=_sort_key, reverse=True)
    top = sorted_entries[:25]
    lines = [
        f"*Filtered-out builds* ({len(entries)} total, showing {len(top)} most recent):",
        "",
    ]
    for e in top:
        gid_chip = f" `{e['gid']}`" if e.get("gid") else ""
        label = (e.get("label") or "?")[:60]
        reason = (e.get("reason") or "")[:140]
        lines.append(f"• *{label}*{gid_chip}\n   _{reason}_")
    if len(entries) > len(top):
        lines.append(f"\n_(+{len(entries) - len(top)} older entries — see `knowledge/commercial_sales/_filtered.md`)_")
    lines.append(
        "\nTo bring one back into the morning digest, reply with "
        "`track this: <customer name or gid>` — the scanner will honor that "
        "override on its next run."
    )
    return "\n".join(lines)


# --- force-include handler -------------------------------------------------


RESOLVE_TARGET_SYSTEM = """\
You're matching a free-form user query like "track this: INSTAAR S3" against
a list of filtered-out Asana tasks. The user wants to force-include the
match they meant in tomorrow's #commercial-sales digest.

Output one JSON object — no fences, no commentary:

{
  "matches": [
    {"gid": "<asana_gid>", "label": "<task label>", "reason_for_match": "<why this matches>"}
  ]
}

Rules:
- Return AT MOST 3 candidates, ranked best first.
- Only include candidates from the provided filtered-tasks list. Never invent gids.
- If the user query is a literal gid that exists, return only that one with
  100% confidence.
- If nothing matches, return {"matches": []}.
"""


def _call_claude_json(system: str, user: str, max_tokens: int = 500) -> dict:
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


def handle_force_include_propose(target: str, user_id: str, channel_id: str) -> str:
    """Phase 1 of force-include: resolve target → matches → propose."""
    filtered = _parse_filtered_table()
    candidates = [e for e in filtered if e.get("gid")]
    if not candidates:
        return (
            "_No filtered builds available to force-include — "
            "`knowledge/commercial_sales/_filtered.md` has no entries with gids._"
        )

    # Quick direct-gid match shortcut
    target_clean = target.strip().strip("`").strip("'\"")
    direct = next((c for c in candidates if c.get("gid") == target_clean), None)
    if direct:
        match_list = [{"gid": direct["gid"], "label": direct["label"], "reason_for_match": "exact gid"}]
    else:
        # Haiku resolution
        candidate_block = "\n".join(
            f"- gid={c['gid']} label={c['label']!r} reason={c['reason'][:100]!r}"
            for c in candidates
        )
        user_block = (
            f"User query: {target!r}\n\n"
            f"Filtered tasks (candidates):\n{candidate_block}"
        )
        try:
            parsed = _call_claude_json(RESOLVE_TARGET_SYSTEM, user_block, max_tokens=600)
        except Exception:
            return f"_(Couldn't resolve '{target}' — try a more specific name or the literal gid.)_"
        match_list = parsed.get("matches") or []

    if not match_list:
        return (
            f"_Couldn't find a filtered build matching '{target}'. Try `show filtered` "
            f"to see what's available, or use a specific Asana gid._"
        )

    _set_pending(user_id, channel_id, {
        "state": "await_confirm",
        "kind": "force_include",
        "matches": match_list,
        "original_target": target,
    })

    if len(match_list) == 1:
        m = match_list[0]
        return (
            f"I'll force-include this build in the next morning digest:\n"
            f"  • *{m['label']}* `{m['gid']}`\n"
            f"  _{m.get('reason_for_match', '')}_\n\n"
            f"Reply *yes* to confirm, *no* to cancel."
        )

    lines = [f"Multiple matches for *{target}* — which one?"]
    for i, m in enumerate(match_list, 1):
        lines.append(f"  {i}. *{m['label']}* `{m['gid']}`")
        if m.get("reason_for_match"):
            lines.append(f"     _{m['reason_for_match']}_")
    lines.append("\nReply with a number, or *cancel*.")
    return "\n".join(lines)


CONFIRM_SYSTEM = """\
The user just replied to a confirm prompt for force-including a build.
Decide their intent. Output one JSON object — no fences, no commentary:

{
  "intent": "accept_all" | "accept_one" | "reject" | "unrelated",
  "accepted_index": <int or null>
}

- "accept_all" — they said yes / confirm / go ahead and there was 1 match
- "accept_one" — they picked a number (1-based); fill accepted_index
- "reject" — cancel, no, never mind, don't
- "unrelated" — message is off-topic
"""


def handle_force_include_followup(reply_text: str, user_id: str, channel_id: str) -> Optional[str]:
    """Phase 2 of force-include: parse confirm/pick/cancel and apply."""
    pending = _get_pending(user_id, channel_id)
    if not pending or pending.get("kind") != "force_include":
        return None

    matches = pending["matches"]
    numbered = "\n".join(f"{i+1}. {m['label']} ({m['gid']})" for i, m in enumerate(matches))
    parse_input = f"Pending matches:\n{numbered}\n\nUser reply:\n{reply_text}"

    try:
        intent_obj = _call_claude_json(CONFIRM_SYSTEM, parse_input, max_tokens=200)
    except Exception:
        return None

    intent = intent_obj.get("intent", "unrelated")

    if intent == "unrelated":
        return None
    if intent == "reject":
        _clear_pending(user_id, channel_id)
        return "Cancelled — nothing changed."

    selected = None
    if intent == "accept_all" and len(matches) == 1:
        selected = matches[0]
    elif intent == "accept_one":
        idx = intent_obj.get("accepted_index")
        if isinstance(idx, int) and 1 <= idx <= len(matches):
            selected = matches[idx - 1]
    if not selected:
        return "_(I couldn't tell which one you meant — try `1` or `2` or `cancel`.)_"

    # Apply: add to _force_include.json
    force_map = _load_force_include()
    force_map[selected["gid"]] = {
        "added_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "added_by_slack_id": user_id,
        "label": selected["label"],
    }
    _save_force_include(force_map)
    _clear_pending(user_id, channel_id)

    # Audit
    try:
        from knowledge import store_entry
        from slack_sdk import WebClient
        sc = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
        store_entry(
            sc, "FEEDBACK",
            f"Force-include added: {selected['label']} ({selected['gid']}) "
            f"by <@{user_id}>",
        )
    except Exception:
        pass

    return (
        f"✓ Added *{selected['label']}* `{selected['gid']}` to the force-include list. "
        f"It'll appear in the next morning's digest after the nightly scan."
    )


# --- create-task handler ---------------------------------------------------


def _unmapped_entry_for_target(target: str) -> Optional[dict]:
    """Look up the unmapped customer table for a domain/customer match.

    Returns {'domain', 'latest', 'count', 'subjects'} when found, None otherwise.
    """
    if not UNMAPPED_PATH.exists():
        return None
    text = UNMAPPED_PATH.read_text()
    target_lower = target.lower().strip()
    in_table = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("| Latest"):
            in_table = True
            continue
        if in_table and stripped.startswith("|----"):
            continue
        if in_table and stripped.startswith("|"):
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            if len(cells) >= 4:
                latest, domain, count, subjects = cells[:4]
                if domain.lower() == target_lower or target_lower in domain.lower():
                    return {
                        "latest": latest,
                        "domain": domain,
                        "count": count,
                        "subjects": subjects,
                    }
    return None


CREATE_TASK_DRAFT_SYSTEM = """\
You're helping create an Asana task in BST's [001-13] BD Pipeline for a new
sales opportunity the bot has surfaced. The user typed something like
"create task for nutshell.com" or "create task: Acme Atmospherics".

Output one JSON object — no fences, no commentary:

{
  "name": "<concise Asana task name, e.g. 'Acme Atmospherics - S2 Inquiry'>",
  "notes": "<initial task notes — what we know about the prospect>",
  "confidence": "high" | "medium" | "low"
}

Rules:
- `name` should be short (under 60 chars). Lead with the customer name.
  If you can infer a product/service from the email subjects, include it.
- `notes` should summarize what we know in 2-4 sentences: customer identity,
  the inquiry's nature, contact info if visible. NEVER fabricate.
- If you genuinely can't determine a customer name (just a domain like
  "nutshell.com" with newsletter-style subjects), confidence="low" and use
  the domain in the name.
"""


def handle_create_task_propose(target: str, user_id: str, channel_id: str) -> str:
    """Phase 1: gather context, draft the Asana task, propose."""
    # Pull whatever context we have about this target
    unmapped = _unmapped_entry_for_target(target)
    context_lines = [f"User-typed target: {target!r}"]
    if unmapped:
        context_lines.append(
            f"Unmapped customer record: domain={unmapped['domain']}, "
            f"latest={unmapped['latest']}, count={unmapped['count']}, "
            f"recent subjects: {unmapped['subjects']}"
        )

    try:
        draft = _call_claude_json(
            CREATE_TASK_DRAFT_SYSTEM,
            "\n".join(context_lines),
            max_tokens=600,
        )
    except Exception:
        return f"_(Couldn't draft the task — try `create task: <Customer name>` with more detail.)_"

    name = (draft.get("name") or target).strip()
    notes = (draft.get("notes") or "").strip()
    confidence = draft.get("confidence", "medium")

    _set_pending(user_id, channel_id, {
        "state": "await_confirm",
        "kind": "create_task",
        "name": name,
        "notes": notes,
        "confidence": confidence,
        "target": target,
    })

    lines = [
        f"I'll create a new Asana task in *[001-13] BD Pipeline*:",
        f"  • Name: *{name}*",
    ]
    if notes:
        lines.append(f"  • Notes: _{notes[:300]}_")
    if confidence == "low":
        lines.append("  _(Confidence: low — feel free to provide more detail before confirming.)_")
    lines.append("\nReply *yes* to create, *no* to cancel, or restate to refine.")
    return "\n".join(lines)


def handle_create_task_followup(reply_text: str, user_id: str, channel_id: str) -> Optional[str]:
    """Phase 2: parse confirm/refine/cancel and call Asana."""
    pending = _get_pending(user_id, channel_id)
    if not pending or pending.get("kind") != "create_task":
        return None

    summary = f"Pending Asana task draft:\n  Name: {pending['name']}\n  Notes: {pending.get('notes','')}"
    parse_input = f"{summary}\n\nUser reply:\n{reply_text}"
    try:
        intent_obj = _call_claude_json(CONFIRM_SYSTEM, parse_input, max_tokens=200)
    except Exception:
        return None

    intent = intent_obj.get("intent", "unrelated")
    if intent == "unrelated":
        return None
    if intent == "reject":
        _clear_pending(user_id, channel_id)
        return "Cancelled — no task created."
    if intent not in ("accept_all", "accept_one"):
        return None

    # Apply: call Asana
    project_gid = os.environ.get("ASANA_COMMERCIAL_SALES_PROJECT_GID", "")
    if not project_gid:
        _clear_pending(user_id, channel_id)
        return "_(ASANA_COMMERCIAL_SALES_PROJECT_GID env var not set — can't create task.)_"

    try:
        from asana_client import create_task
    except Exception as e:
        return f"_(Couldn't import asana_client: {e})_"

    new_gid, err = create_task(project_gid, pending["name"], notes=pending.get("notes", ""))
    _clear_pending(user_id, channel_id)
    if err:
        return f"_(Asana task creation failed: {err})_"

    url = f"https://app.asana.com/0/{project_gid}/{new_gid}"

    # Audit
    try:
        from knowledge import store_entry
        from slack_sdk import WebClient
        sc = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
        store_entry(
            sc, "FEEDBACK",
            f"BD Pipeline task created: '{pending['name']}' "
            f"(gid {new_gid}) by <@{user_id}>",
        )
    except Exception:
        pass

    return (
        f"✓ Created Asana task *{pending['name']}* — `{new_gid}`\n"
        f"  {url}\n"
        f"_It'll appear in tomorrow's morning digest after the nightly scan picks it up._"
    )
