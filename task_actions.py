"""Conversational Asana task-update agent.

Flow:
1. User @mentions Jack in a project channel with an intent like "what tasks
   should be updated now that the flight test moved to June?"
2. `propose_task_updates()` fetches that project's open tasks, feeds the
   question + recent channel conversation + task list to Claude Sonnet, and
   gets back either clarifying questions or a structured list of proposed
   field changes.
3. Proposals are stashed in PENDING keyed by (user_id, channel_id) with a
   10-minute TTL, and a numbered list is posted to Slack.
4. The user's next reply ("yes" / "apply 1 and 3" / "push them all one more
   week" / "cancel") is parsed by `apply_task_updates()`, which either calls
   Asana, modifies the pending proposal, or clears it.

State is in-memory — acceptable because proposals are short-lived; a Railway
restart just makes the user ask again.
"""

import json
import os
import re
import time

import anthropic

from asana_client import get_tasks_for_project, update_task
from channel_context import format_recent_messages

PENDING_TTL = 600  # 10 minutes
PENDING = {}  # (user_id, channel_id) -> state dict

STATE_AWAIT_CONFIRM = "await_confirm"
STATE_AWAIT_CLARIFY = "await_clarify"

ALLOWED_FIELDS = {"due_on", "due_at", "assignee", "completed"}

_client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", ""))

_INTENT_PATTERNS = [
    r"\btask(?:s)?\s+(?:should|need(?:s)?|to|that|we)\b.*\bupdate",
    r"\bupdate\b.*\btask",
    r"\bshift\b.*\b(?:task|due|deadline|schedule)",
    r"\bpush\b.*\b(?:task|due|deadline|back|out)",
    r"\bmove\b.*\b(?:due|deadline|task)",
    r"\breschedule\b",
    r"\bmark\b.*\b(?:complete|done|finished)",
    r"\breassign\b",
    r"\bassign\b.*\bto\b",
    r"\bchange\b.*\b(?:due|deadline|assignee)",
    r"\bpropose\b.*\b(?:change|update)",
]
_INTENT_RE = re.compile("|".join(_INTENT_PATTERNS), re.IGNORECASE)


def is_task_update_intent(text):
    """Return True if the message is asking to update Asana tasks."""
    if not text:
        return False
    return bool(_INTENT_RE.search(text))


def _now():
    return time.time()


def _get_pending(user_id, channel_id):
    entry = PENDING.get((user_id, channel_id))
    if not entry:
        return None
    if _now() - entry["created"] > PENDING_TTL:
        PENDING.pop((user_id, channel_id), None)
        return None
    return entry


def _clear_pending(user_id, channel_id):
    PENDING.pop((user_id, channel_id), None)


def has_pending(user_id, channel_id):
    return _get_pending(user_id, channel_id) is not None


PROPOSE_SYSTEM_PROMPT = """\
You are Jack Bot helping update tasks in Asana. You will be given:
- The current project (code, name)
- The full list of OPEN tasks in that Asana project
- Recent channel conversation for context
- A user request describing something that changed (a pushed deadline, a
  reassignment, work that's actually done, etc.)

Decide what specific field changes on specific tasks would keep Asana in sync
with the new reality.

Allowed field changes:
- "due_on"      — a date in YYYY-MM-DD
- "due_at"      — an ISO datetime if a task has a specific time
- "assignee"    — a person's name (the caller resolves name → Asana gid)
- "completed"   — true or false

Rules:
- One proposed_change per (task, field) pair. If a task needs two fields
  changed, emit two entries.
- Only propose changes that are directly implied by the user's request or the
  channel conversation. Don't invent scope.
- If you're uncertain (ambiguous task, unknown date shift, unclear who to
  assign to), put a clarifying question in `clarifying_questions` and return
  an EMPTY `proposed_changes` list. Ask before proposing.
- If the user asks about dates shifting, infer the NEW absolute date from
  conversation if possible. If you only have a relative shift ("a month"),
  calculate from the current due_on. If the current due_on is null, ask.
- Include the task's Asana gid exactly as given.
- For `current_value` on dates use the current `due_on` from the task data, or
  "(unset)" if missing.
- For `current_value` on assignee, use the current assignee name or
  "(unassigned)".
- For `current_value` on completed, use "false" (these are all open tasks).

Return STRICT JSON ONLY — no prose, no code fences:
{
  "clarifying_questions": ["..."],
  "proposed_changes": [
    {
      "task_gid": "1234567890",
      "task_name": "Ship AeroPod",
      "field": "due_on",
      "current_value": "2026-04-25",
      "proposed_value": "2026-05-25",
      "reason": "Shipping must land before the new flight test window."
    }
  ]
}

If clarifying_questions is non-empty, proposed_changes MUST be empty."""


CONFIRM_PARSE_SYSTEM_PROMPT = """\
You are parsing a user's reply to a numbered list of proposed Asana task
changes. Decide what they want.

Possible intents:
- "accept_all": apply every proposal
- "accept_subset": apply only specific numbered items
- "reject": cancel the whole thing
- "modify": change something about the proposal (push dates further, swap
  assignee, add/remove a task)
- "unrelated": the reply is clearly NOT about these proposals (a new question,
  chat, off-topic)

Return STRICT JSON ONLY:
{
  "intent": "accept_all" | "accept_subset" | "reject" | "modify" | "unrelated",
  "accepted_indices": [1, 3],        // 1-based; only for accept_subset
  "modification_request": "..."       // only for modify; a short instruction
}"""


def _format_tasks_for_prompt(tasks):
    lines = []
    for t in tasks:
        gid = t.get("gid", "")
        name = t.get("name", "")
        assignee = (t.get("assignee") or {}).get("name") or "(unassigned)"
        due = t.get("due_on") or "(no date)"
        notes = (t.get("notes") or "").replace("\n", " ")[:200]
        line = f"- gid:{gid} | {name} | assignee: {assignee} | due_on: {due}"
        if notes:
            line += f" | notes: {notes}"
        lines.append(line)
    return "\n".join(lines) if lines else "(no open tasks)"


def _build_propose_user_prompt(question, channel_context, recent_messages, asker_name=None, asker_user_id=None):
    code = channel_context.get("project_code")
    pname = channel_context.get("project_name") or ""
    tasks = get_tasks_for_project(channel_context["project_gid"], enriched=True)
    open_tasks = [t for t in tasks if not t.get("completed")]
    transcript = format_recent_messages(recent_messages or [])
    today = __import__("datetime").date.today().isoformat()
    parts = [
        f"Today's date: {today}",
        f"Project: [{code}] {pname}",
        "",
        "OPEN TASKS IN THIS PROJECT:",
        _format_tasks_for_prompt(open_tasks),
        "",
    ]
    if transcript:
        parts += ["RECENT CHANNEL CONVERSATION (oldest first):", transcript, ""]
    if asker_name:
        parts += [
            f"ASKER: {asker_name} (Slack <@{asker_user_id}>). "
            f"Treat 'I', 'me', 'my' in the user request as referring to them.",
            "",
        ]
    elif asker_user_id:
        parts += [
            f"ASKER: Slack <@{asker_user_id}> (name unresolved). "
            f"Treat 'I', 'me', 'my' in the user request as referring to them.",
            "",
        ]
    parts += ["USER REQUEST:", question]
    return "\n".join(parts), open_tasks


def _call_claude_json(system, user, max_tokens=2000):
    resp = _client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    text = resp.content[0].text.strip()
    # Strip code fences if the model wrapped the JSON
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text, flags=re.MULTILINE)
    return json.loads(text)


def _format_proposal_for_slack(project_code, project_name, proposals):
    lines = [f"*Proposed Asana updates for [{project_code}] {project_name}:*", ""]
    for i, p in enumerate(proposals, start=1):
        field = p["field"]
        if field == "due_on" or field == "due_at":
            summary = f"due date {p['current_value']} → *{p['proposed_value']}*"
        elif field == "assignee":
            summary = f"assign to *{p['proposed_value']}* (was {p['current_value']})"
        elif field == "completed":
            val = str(p["proposed_value"]).lower()
            summary = "*mark complete*" if val == "true" else "*reopen*"
        else:
            summary = f"{field}: {p['current_value']} → *{p['proposed_value']}*"
        lines.append(f"{i}. *{p['task_name']}* — {summary}")
        if p.get("reason"):
            lines.append(f"   _{p['reason']}_")
    lines += [
        "",
        "Reply *yes* to apply all, *no* to cancel, or tell me which "
        "(e.g. _apply 1 and 3_) or what to change (_push them all one more week_).",
    ]
    return "\n".join(lines)


def _run_proposal(question, channel_context, recent_messages, user_id, channel_id, prior_clarification=None):
    """Run the propose-call and return (slack_message, set_pending_state).

    If Claude asks clarifying questions, returns the question text plus sets
    state = await_clarify so the next user reply gets combined back in.
    """
    asker_name = None
    try:
        from user_map import get_user_by_slack_id
        asker = get_user_by_slack_id(user_id)
        if asker and asker.get("name"):
            asker_name = asker["name"]
    except Exception:
        pass
    user_prompt, _open_tasks = _build_propose_user_prompt(
        question, channel_context, recent_messages,
        asker_name=asker_name, asker_user_id=user_id,
    )
    if prior_clarification:
        user_prompt += f"\n\nPRIOR CLARIFICATION FROM USER:\n{prior_clarification}"
    try:
        result = _call_claude_json(PROPOSE_SYSTEM_PROMPT, user_prompt)
    except Exception as e:
        return f"Couldn't plan the changes: {e}", None

    clarifying = result.get("clarifying_questions") or []
    proposals = result.get("proposed_changes") or []

    # Validate proposals
    proposals = [p for p in proposals if _valid_proposal(p)]

    if clarifying and not proposals:
        text = "Before I propose changes, I need to know:\n" + "\n".join(
            f"• {q}" for q in clarifying
        )
        PENDING[(user_id, channel_id)] = {
            "state": STATE_AWAIT_CLARIFY,
            "original_question": question,
            "created": _now(),
            "project_code": channel_context.get("project_code"),
            "project_name": channel_context.get("project_name"),
            "project_gid": channel_context.get("project_gid"),
        }
        return text, STATE_AWAIT_CLARIFY

    if not proposals:
        _clear_pending(user_id, channel_id)
        return "I couldn't find any tasks that need updating based on that.", None

    PENDING[(user_id, channel_id)] = {
        "state": STATE_AWAIT_CONFIRM,
        "proposals": proposals,
        "original_question": question,
        "created": _now(),
        "project_code": channel_context.get("project_code"),
        "project_name": channel_context.get("project_name"),
        "project_gid": channel_context.get("project_gid"),
    }
    return (
        _format_proposal_for_slack(
            channel_context.get("project_code", ""),
            channel_context.get("project_name", ""),
            proposals,
        ),
        STATE_AWAIT_CONFIRM,
    )


def _valid_proposal(p):
    if not isinstance(p, dict):
        return False
    required = {"task_gid", "task_name", "field", "proposed_value"}
    if not required.issubset(p.keys()):
        return False
    if p["field"] not in ALLOWED_FIELDS:
        return False
    if p["field"] == "due_on" and not re.match(r"^\d{4}-\d{2}-\d{2}$", str(p["proposed_value"])):
        return False
    if p["field"] == "completed" and str(p["proposed_value"]).lower() not in ("true", "false"):
        return False
    return True


def propose_task_updates(question, channel_context, user_id, channel_id):
    """Entry point from app.py — project must already be resolved."""
    if not channel_context or not channel_context.get("project_gid"):
        return (
            "I can't match this channel to an Asana project, so I don't know "
            "which tasks to look at. Ask from a project channel."
        )
    recent = channel_context.get("recent_messages") or []
    text, _state = _run_proposal(
        question, channel_context, recent, user_id, channel_id
    )
    return text


def _resolve_assignee_gid(name):
    """Match a name to an Asana user gid via user_map (fuzzy)."""
    if not name:
        return None, "no name given"
    try:
        from user_map import get_all_users
        users = get_all_users() or []
    except Exception:
        users = []
    if not users:
        return None, "user map not loaded"
    n = name.strip().lower()
    # Exact full-name match
    for u in users:
        if (u.get("name") or "").lower() == n and u.get("asana_user_gid"):
            return u["asana_user_gid"], None
    # First + last token match
    tokens = n.split()
    for u in users:
        un = (u.get("name") or "").lower()
        if un and all(tok in un for tok in tokens) and u.get("asana_user_gid"):
            return u["asana_user_gid"], None
    return None, f"no Asana user matching '{name}'"


def _apply_one(proposal):
    """Call Asana update_task for a single proposal. Returns (ok, message)."""
    field = proposal["field"]
    value = proposal["proposed_value"]
    updates = {}

    if field == "due_on":
        updates["due_on"] = value
    elif field == "due_at":
        updates["due_at"] = value
    elif field == "completed":
        updates["completed"] = str(value).lower() == "true"
    elif field == "assignee":
        gid, err = _resolve_assignee_gid(value)
        if not gid:
            return False, f"{proposal['task_name']}: can't assign — {err}"
        updates["assignee"] = gid
    else:
        return False, f"{proposal['task_name']}: unsupported field {field}"

    ok, err = update_task(proposal["task_gid"], updates)
    if ok:
        return True, f"✓ {proposal['task_name']} ({field} → {value})"
    return False, f"✗ {proposal['task_name']}: {err}"


def _apply_selected(proposals, slack_client=None, user_id=None):
    """Apply a list of proposals, log successes to the knowledge channel."""
    results = []
    applied = []
    for p in proposals:
        ok, msg = _apply_one(p)
        results.append(msg)
        if ok:
            applied.append(p)

    # Audit trail
    if applied and slack_client:
        try:
            from knowledge import store_entry
            summary = "; ".join(
                f"{p['task_name']}.{p['field']} → {p['proposed_value']}" for p in applied
            )
            store_entry(slack_client, "FEEDBACK", f"Jack applied Asana updates: {summary}")
        except Exception:
            pass
    return results


def apply_task_updates(reply_text, user_id, channel_id, slack_client=None):
    """Parse the user's reply against the pending proposal and act on it.

    Returns a tuple (handled: bool, response_text: str). If handled is False,
    the caller should fall through to normal routing.
    """
    entry = _get_pending(user_id, channel_id)
    if not entry:
        return False, ""

    # Clarification branch: combine original question with the reply and re-propose
    if entry["state"] == STATE_AWAIT_CLARIFY:
        from channel_context import get_channel_context
        ctx = None
        if slack_client:
            ctx = get_channel_context(slack_client, channel_id)
        if not ctx:
            ctx = {
                "project_code": entry.get("project_code"),
                "project_name": entry.get("project_name"),
                "project_gid": entry.get("project_gid"),
                "recent_messages": [],
            }
        text, _state = _run_proposal(
            entry["original_question"],
            ctx,
            ctx.get("recent_messages") or [],
            user_id,
            channel_id,
            prior_clarification=reply_text,
        )
        return True, text

    # Confirmation branch
    proposals = entry.get("proposals", [])
    numbered = "\n".join(
        f"{i+1}. {p['task_name']} | {p['field']} → {p['proposed_value']}"
        for i, p in enumerate(proposals)
    )
    parse_prompt = f"Pending proposals:\n{numbered}\n\nUser reply:\n{reply_text}"

    try:
        parsed = _call_claude_json(CONFIRM_PARSE_SYSTEM_PROMPT, parse_prompt, max_tokens=300)
    except Exception:
        # If we can't parse, don't hijack the conversation
        return False, ""

    intent = parsed.get("intent", "unrelated")

    if intent == "unrelated":
        return False, ""

    if intent == "reject":
        _clear_pending(user_id, channel_id)
        return True, "Cancelled. Nothing changed in Asana."

    if intent == "modify":
        modification = parsed.get("modification_request", "")
        from channel_context import get_channel_context
        ctx = None
        if slack_client:
            ctx = get_channel_context(slack_client, channel_id)
        if not ctx:
            ctx = {
                "project_code": entry.get("project_code"),
                "project_name": entry.get("project_name"),
                "project_gid": entry.get("project_gid"),
                "recent_messages": [],
            }
        combined = (
            f"{entry['original_question']}\n\n"
            f"Modification from user: {modification}\n"
            f"Prior proposals (for context):\n{numbered}"
        )
        text, _state = _run_proposal(
            combined, ctx, ctx.get("recent_messages") or [], user_id, channel_id
        )
        return True, text

    if intent == "accept_all":
        selected = proposals
    elif intent == "accept_subset":
        indices = parsed.get("accepted_indices") or []
        selected = [proposals[i - 1] for i in indices if 1 <= i <= len(proposals)]
        if not selected:
            return True, "I couldn't figure out which items you meant. Try again with numbers (e.g. _apply 1 and 3_)."
    else:
        return False, ""

    results = _apply_selected(selected, slack_client=slack_client, user_id=user_id)
    _clear_pending(user_id, channel_id)
    header = (
        f"Applied {len(selected)} change(s)."
        if len(selected) == len(proposals)
        else f"Applied {len(selected)} of {len(proposals)} change(s)."
    )
    return True, header + "\n" + "\n".join(results)
