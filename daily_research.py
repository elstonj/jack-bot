import json
import os
import re
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import anthropic

from user_map import (
    build_user_map,
    canonical_name,
    get_all_users,
    get_user_by_email,
    get_user_by_toggl_id,
    resolve_person,
)
from asana_client import get_enriched_tasks, get_key_project_data, get_workspaces
from toggl_client import NO_PROJECT, get_time_summary
from google_client import get_recent_drive_activity, get_recent_emails, get_todays_calendar, get_contacts, get_meeting_notes_content
from slack_data_client import get_recent_slack_messages
from research_cache import set_cache
from knowledge import get_knowledge_summary, auto_extract_knowledge, store_daily_snapshot, store_entry, get_knowledge, get_status_overrides

KNOWLEDGE_DIR = Path(__file__).parent / "knowledge"

# Operations channel for previous task summaries
OPERATIONS_CHANNEL = "C015QR6P5S4"

SYNTHESIS_PROMPT = """\
You are a project manager AI for Black Swift Technologies (BST), a small aerospace/UAS company. \
You are given data from multiple sources: Asana tasks, time tracking (Toggl), Google Calendar, \
Google Drive activity, meeting notes, Gmail subjects, Slack messages, team feedback, and a \
company knowledge base.

Your job is to synthesize ALL of these sources into each person's TOP 3 PRIORITIES for today. \
Do NOT simply list their Asana tasks — use your judgment across every data source to determine \
what each person should actually focus on.

You also receive a COMPANY KNOWLEDGE BASE with accumulated context about projects, clients, \
priorities, and team dynamics, plus FEEDBACK from team members. User corrections and feedback \
override your default reasoning.

PRIORITIZATION RULES (in order of weight):
1. User corrections and feedback from the knowledge base — always honor these
2. OVERDUE tasks or tasks due today
3. High-dollar projects (use milestone amounts, BD Pipeline, and knowledge base)
4. Risk signals: blockers in Slack, client emails about deadlines, low hours vs. approaching due dates
5. Upcoming deliverables from the knowledge base
6. Everything else by due date proximity

CORRECTIONS AND FEEDBACK ARE ABSOLUTE:
A CORRECTION or FEEDBACK entry, or a reply in #OPERATIONS, ALWAYS overrides whatever \
Asana / Toggl / distilled knowledge files say. The knowledge files are refreshed \
periodically and lag real-world state; live human input always wins. Apply EVERY \
correction faithfully — not just the obvious ones:
- "complete / cancelled / handled externally / done / dropped" → exclude entirely \
  from the team summary AND per-person priorities. Never call it "overdue".
- "caught up / back on track / no longer blocked / no longer behind" → do NOT flag it \
  as :rotating_light:, :warning:, "behind", "critical", or "catching up" in the team \
  summary. It's healthy; treat it like routine in-progress work and likely OMIT it \
  from the team summary entirely (which is reserved for behind / critical items).
- "now priority #1 / elevated / higher priority this month" → SURFACE it in the team \
  summary as a top item even if Asana hasn't been updated yet. The team needs to know \
  what to rally around.
- Date shifts ("moved to Friday", "delayed to Fall") → use the override date, not the \
  Asana date. Don't flag as overdue if the override sets a future date.
- Reassignments ("Beck is handling X now") → surface under the new owner's section.

The user message may begin with a `PROJECT STATUS OVERRIDES` block — treat every line \
as hard truth and apply ALL of it, not just the lines that match the obvious "complete / \
delayed" pattern. If an override says something is caught up, don't flag it as critical. \
If an override elevates something, surface it.

COMPLETED TASK DETECTION:
If email subjects, Slack messages, or Drive activity suggest a task is already DONE (e.g. \
"submitted", "delivered", "sent to client", "completed", review comments indicate finished work), \
do NOT list it as a priority. Instead, add a brief note like: \
":white_check_mark: [Task] appears complete — remember to close it in Asana"

OUT OF OFFICE:
For people marked as OOO, just produce a single line noting they are out. No tasks.

If a YESTERDAY'S SUMMARY is provided, note what changed — completed tasks, shifted priorities, \
new items. Briefly mention key changes in the team summary.

OUTPUT FORMAT:
Return your answer by calling the `submit_daily_briefing` tool. Write no prose \
outside the tool call. Fill the tool's fields with real structured values — \
`team_summary` and `sections` are arrays, not strings. Never JSON-encode the \
briefing into a single field.

`team_summary` — 4-6 bullet strings. This is what gets posted to #operations and is \
the ONLY part most of the team will read — make it count. Frame it as "what does the \
team need to rally around right now?":
- Lead with anything *behind / overdue / critical* (use :rotating_light: for true blockers, \
  :warning: for at-risk). Call out who owns it and what's blocking forward motion.
- Then upcoming deadlines in the next 1-2 weeks that need cross-team coordination \
  (deliveries, customer demos, proposal due dates, milestone payments). Name the \
  date and the owner.
- Then any company-wide events affecting today (visits, all-hands, flydays) that \
  shape the day's available work hours.
- Skip routine in-progress work — if it's on track and on one person, it doesn't \
  belong in the team summary.
- Be specific. "S3 IRAD UMES delivery 2026-05-31 — Josh+Jack on PCB run" beats \
  "S3 work continuing".

The team summary contains NO per-person task lists — those go in `sections`.

`sections` — ONE entry per ACTIVE person in the REQUIRED PEOPLE list at the end of \
the user message. Each entry has:
- `person`: that person's name copied EXACTLY as written in the REQUIRED PEOPLE \
  list. Never invent a name, never substitute a nickname or a different spelling, \
  and never use a name that isn't on that list.
- `priorities`: 1-3 short strings, each "[Priority] — [why this matters today] \
  (Due: [date])".
- `notes`: optional extra lines, e.g. ":white_check_mark: [Task] appears complete — \
  remember to close it in Asana".

IDENTITY RULES — these matter more than anything else in this prompt:
- Exactly ONE entry per person. Never emit two entries for the same person.
- Every entry must contain THAT PERSON'S OWN work. Never put one person's tasks \
  under another person's name. If you are unsure whose work something is, leave it \
  out rather than guessing.
- Never write "already covered above", "see below", "same as X", or any other \
  cross-reference in place of real priorities. Every person gets their own \
  independently written priorities, even when two people share a meeting or a \
  project — describe each person's own stake in it.
- The source data spells people's names several ways. Treat the REQUIRED PEOPLE \
  list as the only valid set of people, and map every name you see in the data \
  onto it before deciding whose section something belongs in.
- Do NOT produce entries for anyone marked OUT OF OFFICE — those are handled \
  automatically.

Other rules:
- Each person gets their TOP 3 priorities synthesized from ALL sources — not just Asana
- Priorities can come from emails, Slack threads, Drive activity, knowledge base, etc.
- If a task looks done based on evidence, put a `notes` line about closing it in \
  Asana instead of listing it as a priority
- Be terse
- Do NOT list anyone's meetings and do NOT mention how many hours anyone tracked. \
  A calendar line and an hours line are appended to every section automatically \
  from the raw Google Calendar and Toggl data — writing your own would duplicate \
  or contradict them. Specifically: never write a ":clock1:" or ":calendar:" line, \
  never restate the "No time tracked yesterday" roster, and never turn time \
  tracking itself into a priority ("tag your hours", "log time to projects"). \
  The TIME TRACKING block is context for judging what someone is ACTUALLY working \
  on — use it to inform which priorities you pick, never to report hours back.
- Any "today" meeting/event you mention in the TEAM SUMMARY must come ONLY from \
  the `=== TODAY'S CALENDAR ===` section, whose events all carry real start \
  datetimes. Do NOT infer "today's" meetings from email subjects or Slack \
  chatter: a meeting referenced in a thread may have happened yesterday or be \
  scheduled for a future day.

YOU MUST PRODUCE AN ENTRY FOR EVERY SINGLE ACTIVE PERSON IN THE REQUIRED LIST. \
Do not stop until every required person has one."""


# Structured output contract. The model returns names from a closed list and
# never touches Slack IDs — the code maps name -> ID and writes the header, so
# a section can no longer be attributed to the wrong person.
BRIEFING_TOOL = {
    "name": "submit_daily_briefing",
    "description": "Submit the daily team briefing: a team-level summary plus one "
                   "entry per active team member.",
    "input_schema": {
        "type": "object",
        "properties": {
            "team_summary": {
                "type": "array",
                "items": {"type": "string"},
                "description": "4-6 team-level bullet points. No per-person task lists.",
            },
            "sections": {
                "type": "array",
                "description": "Exactly one entry per ACTIVE person in the required list.",
                "items": {
                    "type": "object",
                    "properties": {
                        "person": {
                            "type": "string",
                            "description": "Name copied EXACTLY from the REQUIRED PEOPLE list.",
                        },
                        "priorities": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "1-3 priorities that belong to THIS person.",
                        },
                        "notes": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional extra lines, e.g. close-in-Asana reminders.",
                        },
                    },
                    "required": ["person", "priorities"],
                },
            },
        },
        "required": ["team_summary", "sections"],
    },
}


def _collect_asana():
    try:
        return get_enriched_tasks()
    except Exception as e:
        return f"[Asana data unavailable: {e}]"


def _collect_toggl():
    try:
        return get_time_summary()
    except Exception as e:
        return f"[Toggl data unavailable: {e}]"


def _collect_key_projects():
    try:
        workspaces = get_workspaces()
        if not workspaces:
            return {}
        return get_key_project_data(workspaces[0]["gid"])
    except Exception as e:
        return f"[Key project data unavailable: {e}]"


def _collect_meeting_notes(users):
    """Fetch the most recent BST Internal Update Meeting notes."""
    for user in users:
        try:
            docs = get_meeting_notes_content(user["email"], max_docs=1)
            if docs:
                return docs
        except Exception:
            continue
    return []


def _collect_operations_history(slack_client):
    """Fetch recent messages from #operations for task context."""
    import time
    try:
        oldest = str(int(time.time() - (14 * 86400)))  # last 14 days
        result = slack_client.conversations_history(
            channel=OPERATIONS_CHANNEL, limit=100, oldest=oldest,
        )
        raw = result.get("messages", [])
        messages = []
        for msg in raw:
            text = msg.get("text", "").strip()
            if not text or msg.get("subtype") in ("channel_join", "channel_leave", "channel_topic", "channel_purpose"):
                continue
            messages.append(text[:300])
        messages.reverse()
        if not messages:
            return [f"[Operations: {len(raw)} raw messages, all filtered out or empty]"]
        return messages
    except Exception as e:
        return [f"[Operations channel error: {e}]"]


def _sync_operations_feedback(slack_client):
    """Mirror recent human replies in #operations into the knowledge channel as FEEDBACK.

    The Slack app may not be subscribed to message.channels, in which case the
    real-time event handler never fires for non-mention replies.  This pipeline-
    time sync ensures the bot doesn't silently lose team feedback that shows up
    as plain replies in #operations.  Dedup is by Slack ts, embedded in each
    stored FEEDBACK entry.
    """
    import time

    try:
        existing = get_knowledge(slack_client, ["FEEDBACK"], days=14)
    except Exception:
        existing = []
    seen_ts = set()
    for entry in existing:
        m = re.search(r"ts=([\d.]+)", entry.get("content", ""))
        if m:
            seen_ts.add(m.group(1))

    bot_user_id = None
    try:
        bot_user_id = slack_client.auth_test().get("user_id")
    except Exception:
        pass

    # Page through the full 14-day window. A single 200-message page only
    # covers a few days in a busy channel, so older replies (including
    # important @-mentions from earlier in the week) silently dropped off
    # before this loop ever saw them.
    oldest = str(int(time.time() - (14 * 86400)))
    all_msgs: list[dict] = []
    cursor = None
    for _ in range(10):  # hard cap so a Slack API quirk can't spin us forever
        kwargs = {"channel": OPERATIONS_CHANNEL, "limit": 200, "oldest": oldest}
        if cursor:
            kwargs["cursor"] = cursor
        try:
            result = slack_client.conversations_history(**kwargs)
        except Exception:
            break
        all_msgs.extend(result.get("messages", []) or [])
        cursor = result.get("response_metadata", {}).get("next_cursor")
        if not cursor:
            break

    for msg in all_msgs:
        if msg.get("bot_id") or msg.get("subtype") in (
            "channel_join", "channel_leave", "channel_topic", "channel_purpose",
            "bot_message",
        ):
            continue
        user_id = msg.get("user")
        if not user_id or user_id == bot_user_id:
            continue
        text = (msg.get("text") or "").strip()
        if not text:
            continue
        ts = msg.get("ts", "")
        if not ts or ts in seen_ts:
            continue
        # Skip explicit commands — those have their own storage paths
        tl = text.lower()
        if any(tl.startswith(p) for p in (
            "correct:", "correction:", "bug:", "feature:", "request:",
            "note:", "remember:",
        )):
            continue
        try:
            user_name = slack_client.users_info(user=user_id)["user"]["profile"].get(
                "display_name"
            ) or slack_client.users_info(user=user_id)["user"].get("real_name", "someone")
        except Exception:
            user_name = "someone"
        try:
            store_entry(
                slack_client,
                "FEEDBACK",
                f"From {user_name} (ts={ts}): {text[:600]}",
            )
            seen_ts.add(ts)
        except Exception:
            continue


def _collect_drive(users, known_file_ids=None):
    results = {}
    for user in users:
        email = user["email"]
        try:
            files = get_recent_drive_activity(email, known_file_ids)
            if files:
                results[user["name"]] = files
        except Exception:
            continue
    return results


def _collect_gmail(users):
    results = {}
    for user in users:
        email = user["email"]
        try:
            emails = get_recent_emails(email)
            if emails:
                results[user["name"]] = emails
        except Exception:
            continue
    return results


def _collect_calendar(users):
    results = {}
    for user in users:
        email = user["email"]
        try:
            events = get_todays_calendar(email)
            if events:
                results[user["name"]] = events
        except Exception:
            continue
    return results


def _collect_contacts(users):
    """Collect contacts from the first user (typically admin) to get client/org context."""
    if not users:
        return []
    # Only need to pull contacts once — directory is shared across the org
    for user in users:
        try:
            contacts = get_contacts(user["email"])
            if contacts:
                return contacts
        except Exception:
            continue
    return []


def _collect_slack(slack_client, users):
    try:
        return get_recent_slack_messages(slack_client, users)
    except Exception as e:
        return f"[Slack data unavailable: {e}]"


# The bot is named "Jack Bot" and the CEO is named Jack Elston. Left as-is, the
# briefing prompt is full of lines like "per Jack" and "reminded Jack Bot",
# which is exactly the ambiguity that put Jack's tasks under Josh's name.
_BOT_NAME_RE = re.compile(r"\bjack\s*bot\b", re.I)


def _scrub_bot_identity(text, bot_user_id=None):
    """Replace references to the bot itself so "Jack" only ever means the CEO."""
    if not text:
        return text
    scrubbed = _BOT_NAME_RE.sub("the assistant", text)
    if bot_user_id:
        scrubbed = re.sub(rf"<@{re.escape(bot_user_id)}(?:\|[^>]*)?>", "the assistant", scrubbed)
    return scrubbed


def _assemble_context(asana_tasks, toggl_summary, drive_activity, gmail_data, calendar_data, contacts, slack_messages, users, key_projects=None, meeting_notes=None, operations_history=None, bot_user_id=None):
    """Build the context document for Claude."""
    sections = []

    # Team overview
    names = [u["name"] for u in users if u["name"]]
    sections.append(f"=== TEAM OVERVIEW ===\nUsers: {', '.join(names)}")

    # Asana — filter to assigned tasks only, prioritize by due date
    if isinstance(asana_tasks, str):
        sections.append(f"=== ASANA TASKS ===\n{asana_tasks}")
    else:
        assigned = [t for t in asana_tasks if t.get("assignee_name", "Unassigned") != "Unassigned"]
        # Sort: tasks with due dates first (soonest first), then no due date
        def sort_key(t):
            due = t.get("due_on") or "9999-99-99"
            return due
        assigned.sort(key=sort_key)
        # Limit to top 10 tasks per person to keep prompt manageable
        # Group by CANONICAL name — Asana says "Josh Fromm" / "Dan Prendergast"
        # while the roster says "Joshua Fromm" / "Dan Prendergast". Feeding both
        # spellings to the model invites it to treat them as different people.
        from collections import defaultdict
        per_person = defaultdict(list)
        for t in assigned:
            name = canonical_name(t.get("assignee_name"))
            if len(per_person[name]) < 10:
                per_person[name].append(t)

        lines = [f"=== ASANA TASKS ({len(assigned)} assigned, {len(asana_tasks) - len(assigned)} unassigned filtered out) ==="]
        for person_name in sorted(per_person.keys()):
            tasks_for_person = per_person[person_name]
            lines.append(f"\n*{person_name}:*")
            for task in tasks_for_person:
                due = task.get("due_on", "No due date")
                project = task.get("project_name", "")
                custom = ""
                for cf in task.get("custom_fields", []) or []:
                    if cf and cf.get("display_value"):
                        custom += f" [{cf.get('name', '')}: {cf['display_value']}]"
                lines.append(f"  - {task['name']} | {project} | Due: {due}{custom}")
        sections.append("\n".join(lines))

    # Key projects — limit to items with due dates in next 30 days
    if key_projects and isinstance(key_projects, dict):
        if key_projects.get("bd_pipeline"):
            items = key_projects["bd_pipeline"][:20]  # top 20
            lines = [f"=== BD PIPELINE ({len(key_projects['bd_pipeline'])} total, showing top 20) ==="]
            for t in items:
                custom = ""
                for cf in t.get("custom_fields", []) or []:
                    if cf and cf.get("display_value"):
                        custom += f" [{cf.get('name', '')}: {cf['display_value']}]"
                lines.append(f"- {t['name']} | Due: {t.get('due_on', 'N/A')}{custom}")
            sections.append("\n".join(lines))

        if key_projects.get("proposals"):
            items = key_projects["proposals"][:15]  # top 15
            lines = [f"=== PROPOSALS ({len(key_projects['proposals'])} total, showing top 15) ==="]
            for t in items:
                custom = ""
                for cf in t.get("custom_fields", []) or []:
                    if cf and cf.get("display_value"):
                        custom += f" [{cf.get('name', '')}: {cf['display_value']}]"
                lines.append(f"- {t['name']} | Due: {t.get('due_on', 'N/A')}{custom}")
            sections.append("\n".join(lines))

        if key_projects.get("milestones"):
            # Only milestones with due dates, sorted soonest first
            ms = [m for m in key_projects["milestones"] if m.get("due_on")]
            ms.sort(key=lambda m: m.get("due_on", "9999"))
            ms = ms[:15]
            lines = [f"=== UPCOMING MILESTONES ({len(ms)} with dates) ==="]
            for m in ms:
                dollar_info = ""
                for st in m.get("subtasks", [])[:3]:
                    for cf in st.get("custom_fields", []) or []:
                        if cf and cf.get("display_value") and "$" in str(cf.get("display_value", "")):
                            dollar_info += f" ${cf['display_value']}"
                lines.append(f"- {m['name']} | {m.get('project_name', '')} | Due: {m['due_on']}{dollar_info}")
            sections.append("\n".join(lines))

    # Meeting notes — truncate to key points
    if meeting_notes:
        lines = ["=== RECENT ALL-HANDS MEETING NOTES ==="]
        for doc in meeting_notes:
            lines.append(f"*{doc['name']}*")
            lines.append(doc["content"][:1500])  # trim to 1500 chars
        sections.append("\n".join(lines))

    # Operations channel history — take the NEWEST 30 (already chronological, oldest→newest)
    if operations_history:
        lines = ["=== #OPERATIONS CHANNEL (recent task context) ==="]
        for msg in operations_history[-30:]:
            lines.append(f"  - {_scrub_bot_identity(msg, bot_user_id)}")
        sections.append("\n".join(lines))

    # Toggl
    from toggl_client import _last_workday
    toggl_day = _last_workday().strftime("%A %b %d")
    if isinstance(toggl_summary, str):
        sections.append(f"=== TIME TRACKING ({toggl_day}) ===\n{toggl_summary}")
    else:
        lines = [f"=== TIME TRACKING ({toggl_day}) ==="]
        # Aggregate entries by user — a single person may have multiple
        # Toggl IDs (legacy + current accounts) and we want one consolidated
        # row per person rather than two anonymous "toggl#NNN" rows.
        by_user_name = {}  # name -> {"total_hours": float, "projects": {name: hours}}
        unmapped = []      # entries whose toggl_id didn't resolve to a user
        for toggl_id, data in toggl_summary.items():
            user = get_user_by_toggl_id(toggl_id)
            if user and user.get("name"):
                bucket = by_user_name.setdefault(
                    user["name"], {"total_hours": 0.0, "projects": {}}
                )
                bucket["total_hours"] += data["total_hours"]
                for proj, hrs in data["projects"].items():
                    bucket["projects"][proj] = bucket["projects"].get(proj, 0) + hrs
            else:
                unmapped.append((toggl_id, data))

        for name, data in by_user_name.items():
            proj_parts = [f"{p}: {round(h, 1)}h" for p, h in data["projects"].items()]
            lines.append(f"{name}: {round(data['total_hours'], 1)}h total ({', '.join(proj_parts)})")
        for toggl_id, data in unmapped:
            label = data.get("email") or f"toggl#{toggl_id}"
            proj_parts = [f"{p}: {h}h" for p, h in data["projects"].items()]
            lines.append(f"{label}: {data['total_hours']}h total ({', '.join(proj_parts)})")

        # Explicitly note team members with no tracked time so Claude
        # doesn't inherit stale hours from Asana assignee names alone.
        # Compare against the full toggl_user_ids list per user, not just
        # the primary, so people who logged time under a secondary ID don't
        # get falsely flagged as untracked.
        tracked_ids = set(toggl_summary.keys())
        untracked = []
        for u in users:
            if not u.get("name"):
                continue
            user_toggl_ids = set(u.get("toggl_user_ids") or [])
            if u.get("toggl_user_id"):
                user_toggl_ids.add(u["toggl_user_id"])
            if not user_toggl_ids:
                continue
            if not (user_toggl_ids & tracked_ids):
                untracked.append(u["name"])
        if untracked:
            lines.append(f"No time tracked yesterday: {', '.join(sorted(untracked))}")
        sections.append("\n".join(lines))

    # Drive
    if drive_activity:
        lines = ["=== RECENT GOOGLE DRIVE ACTIVITY ==="]
        for name, files in drive_activity.items():
            lines.append(f"{name}:")
            for f in files[:10]:
                lines.append(f"  - \"{f['name']}\" ({f.get('mimeType', '')}, modified {f.get('modifiedTime', '')})")
        sections.append("\n".join(lines))

    # Calendar
    if calendar_data:
        lines = ["=== TODAY'S CALENDAR ==="]
        for name, events in calendar_data.items():
            lines.append(f"{name}:")
            for ev in events:
                attendee_str = ""
                if ev["attendees"]:
                    attendee_str = f" (with: {', '.join(ev['attendees'][:5])})"
                lines.append(f"  - {ev['start']} - {ev['end']}: {ev['summary']}{attendee_str}")
        sections.append("\n".join(lines))

    # Contacts (client/org context)
    if contacts:
        lines = ["=== KEY CONTACTS & CLIENTS ==="]
        # Only include contacts with organization info for context
        orgs_seen = set()
        for c in contacts:
            org = c.get("organization", "")
            if org and org not in orgs_seen:
                orgs_seen.add(org)
                lines.append(f"  - {org}: {c['name']} ({c.get('title', '')})")
        if len(lines) > 1:
            sections.append("\n".join(lines))

    # Gmail
    if gmail_data:
        lines = ["=== RECENT EMAILS (Subject lines only) ==="]
        for name, emails in gmail_data.items():
            lines.append(f"{name}:")
            for e in emails[:10]:
                lines.append(f"  - \"{e['subject']}\" from {e['from']}")
        sections.append("\n".join(lines))

    # Slack
    if isinstance(slack_messages, str):
        sections.append(f"=== RECENT SLACK ACTIVITY ===\n{slack_messages}")
    elif slack_messages:
        lines = ["=== RECENT SLACK ACTIVITY ==="]
        by_channel = {}
        for msg in slack_messages:
            ch = msg["channel"]
            by_channel.setdefault(ch, []).append(msg)
        for ch, msgs in by_channel.items():
            lines.append(f"{ch}:")
            for m in msgs[:20]:
                speaker = canonical_name(m["user_name"])
                text = _scrub_bot_identity(m["text"][:200], bot_user_id)
                lines.append(f"  - {speaker}: {text}")
        sections.append("\n".join(lines))

    return "\n\n".join(sections)


# A Slack mention, tolerating the pipe form Slack echoes back (<@U123|Name>).
_MENTION_RE = re.compile(r"<@([A-Z0-9]+)(?:\|[^>]*)?>")

# A per-user section header is a line that *leads* with a Slack mention,
# optionally wrapped in bold/heading markers. Anything may follow on that line —
# Claude sometimes appends the plain name ("*<@U123>* (Alex Lomis)"), which an
# end-anchored pattern rejected, collapsing every section into the team summary.
_HEADER_MENTION_RE = re.compile(r"^[*_#\s]{0,4}<@[A-Z0-9]+(?:\|[^>]*)?>")
_HEADER_LEGACY_RE = re.compile(r"^(?:---\s*@|###\s)")


def _is_section_start(line):
    """True if `line` starts a per-user section rather than team-summary prose."""
    stripped = line.strip()
    return bool(_HEADER_MENTION_RE.match(stripped) or _HEADER_LEGACY_RE.match(stripped))


def _split_summary(full_summary):
    """Split Claude's output into (team_summary, [per-user section, ...]).

    Single source of truth for where the team-level overview ends — the main
    #operations post uses the first return value, the thread uses the second.
    """
    lines = full_summary.splitlines()
    starts = [i for i, line in enumerate(lines) if _is_section_start(line)]
    if not starts:
        return full_summary.strip(), []
    team = "\n".join(lines[:starts[0]]).strip()
    bounds = starts + [len(lines)]
    sections = ["\n".join(lines[a:b]).strip() for a, b in zip(bounds, bounds[1:])]
    return team, [s for s in sections if s]


def _parse_per_user(full_summary, users):
    """Parse rendered briefing text into per-user sections keyed by Slack user ID.

    Only used for text that didn't come straight out of `_render_section` (e.g.
    a cached summary from an older deploy).  Duplicate headers are kept, not
    overwritten — silently clobbering a real section with a later stub is how
    Alex Lomis lost his priorities on 2026-08-05.
    """
    per_user = {}
    _, parts = _split_summary(full_summary)
    for part in parts:
        # Try to find a Slack mention anywhere in the first line
        first_line = part.split("\n")[0]
        mention_match = _MENTION_RE.search(first_line)
        slack_id = mention_match.group(1) if mention_match else None

        if not slack_id:
            # Fallback: match --- @Name or ### Name
            match = re.match(r"^(?:---\s*@|### )(.+)", first_line)
            if not match:
                continue
            header = match.group(1).strip()
            user = resolve_person(header)
            if not user:
                continue
            slack_id = user["slack_user_id"]

        existing = per_user.get(slack_id)
        if existing and not _is_stub_section(existing):
            # Already have real content for this person; never let a later
            # duplicate overwrite it.
            continue
        per_user[slack_id] = part
    return per_user


# ---------------------------------------------------------------------------
# Deterministic section rendering
#
# The model supplies priority TEXT only. Everything that identifies a person or
# restates raw data — the Slack-mention header, the calendar line, the tracked
# hours — is written here from the source records, so it cannot be misattributed
# or hallucinated.
# ---------------------------------------------------------------------------

_NO_PROJECT_LABELS = {NO_PROJECT.lower(), "(no project)", "without project", "unassigned", ""}


# The calendar and hours lines are generated in code and appended to every
# section. The model is told not to write its own, but it does anyway — most
# often by echoing the "No time tracked yesterday" roster line straight out of
# the TIME TRACKING block. Any model line that restates either generated line is
# dropped here so a section can't carry the same fact twice (or contradict it).
_RESTATEMENT_PREFIXES = (":clock1:", ":clock:", ":stopwatch:", ":hourglass:",
                         ":calendar:", ":date:", ":spiral_calendar_pad:")
_NO_TIME_RE = re.compile(r"\bno (?:time|hours)\b[^.]{0,30}\b(?:track|log)", re.I)
_HOURS_RE = re.compile(r"\b\d+(?:\.\d+)?\s*(?:h|hr|hrs|hours)\b", re.I)
_TRACKING_WORD_RE = re.compile(
    r"\b(?:track(?:ed|ing)?|logg?(?:ed|ing)|unassigned|uncategori[sz]ed|untagged|toggl|"
    r"time entr(?:y|ies)|timesheet)\b", re.I
)


def _restates_generated_line(text):
    """True if a model-written line duplicates the code-generated hours/calendar line."""
    stripped = (text or "").strip()
    if not stripped:
        return False
    if stripped.startswith(_RESTATEMENT_PREFIXES):
        return True
    if _NO_TIME_RE.search(stripped):
        return True
    # e.g. "Tag yesterday's 16.0h (all uncategorized) to correct projects"
    return bool(_HOURS_RE.search(stripped) and _TRACKING_WORD_RE.search(stripped))


def _fmt_event_time(value):
    """Return HH:MM for a timed event, or "" for an all-day event."""
    if not value or "T" not in value:
        return ""
    try:
        return datetime.fromisoformat(value).strftime("%H:%M")
    except ValueError:
        return value[11:16]


def _calendar_line(events):
    """Render the `:calendar:` line straight from today's calendar records."""
    if not events:
        return ":calendar: No meetings"
    parts = []
    for ev in events[:8]:
        summary = (ev.get("summary") or "").strip() or "(no title)"
        start = _fmt_event_time(ev.get("start"))
        end = _fmt_event_time(ev.get("end"))
        parts.append(f"{summary} {start}-{end}" if start and end else summary)
    return ":calendar: " + " · ".join(parts)


def _hours_line(user, toggl_summary):
    """Render the `:clock1:` line straight from the Toggl summary."""
    if not isinstance(toggl_summary, dict):
        return None

    ids = set(user.get("toggl_user_ids") or [])
    if user.get("toggl_user_id"):
        ids.add(user["toggl_user_id"])

    total = 0.0
    unassigned = 0.0
    found = False
    for tid in ids:
        data = toggl_summary.get(tid)
        if not data:
            continue
        found = True
        total += data.get("total_hours") or 0
        for project, hours in (data.get("projects") or {}).items():
            if (project or "").strip().lower() in _NO_PROJECT_LABELS:
                unassigned += hours or 0

    total = round(total, 1)
    unassigned = round(unassigned, 1)
    if not found or total <= 0:
        return ":warning: *No time tracked yesterday*"
    if unassigned >= total:
        return f":clock1: {total}h (all unassigned — flag for project tagging)"
    if unassigned > 0:
        return f":clock1: {total}h ({unassigned}h unassigned)"
    return f":clock1: {total}h"


def _render_section(user, priorities, notes=None, calendar_line=None, hours_line=None):
    """Render one person's section. The header ID comes from the user map."""
    lines = [f"*<@{user['slack_user_id']}>*"]
    kept = [t for t in ((p or "").strip() for p in priorities or [])
            if t and not _restates_generated_line(t)]
    for i, text in enumerate(kept[:3], 1):
        lines.append(f"{i}. {text}")
    for note in notes or []:
        text = (note or "").strip()
        if text and not _restates_generated_line(text):
            lines.append(text)
    if calendar_line:
        lines.append(calendar_line)
    if hours_line:
        lines.append(hours_line)
    return "\n".join(lines)


def _render_ooo_section(user, reason):
    return f"*<@{user['slack_user_id']}>*\n:palm_tree: Out of office — {reason}"


def _render_team_summary(bullets):
    lines = [":mega: *TEAM SUMMARY*"]
    for bullet in bullets or []:
        text = (bullet or "").strip()
        if not text:
            continue
        lines.append(text if text.startswith(("-", "•", ":")) else f"- {text}")
    if len(lines) == 1:
        lines.append(":warning: Jack Bot couldn't generate a team summary this run.")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

_CROSS_REF_RE = re.compile(
    r"already covered|see (?:above|below|\w+'s section)|same as |mention key|"
    r"covered (?:above|below)|no (?:tasks|priorities|updates) (?:for|this)",
    re.I,
)


def _is_stub_section(text):
    """True if a rendered section has a header but no real priority content."""
    body = [ln.strip() for ln in (text or "").splitlines()[1:] if ln.strip()]
    if not body:
        return True
    if any(ln.startswith(":palm_tree:") for ln in body):
        return False  # OOO sections are legitimately short
    return not any(re.match(r"^\d+\.\s*\S", ln) for ln in body)


def _is_stub_priorities(priorities):
    """True if the model returned a placeholder instead of real priorities."""
    joined = " ".join(p.strip() for p in priorities if p and p.strip()).strip()
    # Keep the hard floor low — real priorities are sometimes genuinely terse
    # ("SwiftCore 3.3 release" is 21 chars). Cross-reference phrasing, not
    # length, is what identifies a placeholder.
    if len(joined) < 12:
        return True
    return bool(_CROSS_REF_RE.search(joined)) and len(joined) < 200


def _content_signature(priorities):
    return re.sub(r"[^a-z0-9 ]+", " ", " ".join(priorities).lower())


def _find_copied_sections(accepted):
    """Detect one person's priorities being duplicated under another person.

    `accepted` is an ordered {name: {"priorities": [...]}} mapping. Returns
    [(name_to_drop, name_it_duplicates, ratio)] for near-identical bodies —
    the signature of a mis-assignment (2026-08-05: Jack Elston's whole section
    was emitted a second time under Joshua Fromm's name).
    """
    import difflib

    names = list(accepted.keys())
    signatures = {n: _content_signature(accepted[n]["priorities"]) for n in names}
    copies = []
    for i, first in enumerate(names):
        for second in names[i + 1:]:
            if not signatures[first] or not signatures[second]:
                continue
            ratio = difflib.SequenceMatcher(None, signatures[first], signatures[second]).ratio()
            if ratio >= 0.9:
                copies.append((second, first, round(ratio, 2)))
    return copies


def _validate_sections(raw_sections, allowed_names):
    """Map model output onto real people, rejecting anything unsafe.

    Returns (ordered {canonical_name: {"priorities", "notes"}}, [issue strings]).
    """
    accepted = {}
    issues = []
    for entry in raw_sections or []:
        if not isinstance(entry, dict):
            issues.append(f"non-object section entry: {entry!r:.80}")
            continue
        raw_name = (entry.get("person") or "").strip()
        priorities = [p for p in (entry.get("priorities") or []) if isinstance(p, str)]
        notes = [n for n in (entry.get("notes") or []) if isinstance(n, str)]

        user = resolve_person(raw_name)
        if not user:
            issues.append(f"unresolvable person {raw_name!r} — section dropped")
            continue
        name = user["name"]
        if name not in allowed_names:
            issues.append(f"{raw_name!r} resolved to {name} who isn't an active member — dropped")
            continue
        if name in accepted:
            issues.append(f"duplicate section for {name} — kept the first, dropped the later one")
            continue
        if _is_stub_priorities(priorities):
            issues.append(f"stub/cross-reference section for {name} ({priorities!r:.80}) — dropped")
            continue
        accepted[name] = {"priorities": priorities, "notes": notes}

    return accepted, issues


def _loads_tolerant(text):
    """Parse JSON, falling back to the first balanced {...} / [...] block."""
    if not isinstance(text, str):
        return None
    try:
        return json.loads(text)
    except (ValueError, TypeError):
        pass
    # Try whichever bracket opens first — an array with trailing prose must not
    # be mis-parsed as the first object nested inside it.
    candidates = [(text.find(o), o, c) for o, c in (("{", "}"), ("[", "]"))]
    for start, opener, closer in sorted(c for c in candidates if c[0] != -1):
        depth = 0
        in_str = False
        escape = False
        for i, ch in enumerate(text[start:], start):
            if escape:
                escape = False
                continue
            if ch == "\\":
                escape = True
                continue
            if ch == '"':
                in_str = not in_str
                continue
            if in_str:
                continue
            if ch == opener:
                depth += 1
            elif ch == closer:
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(text[start:i + 1])
                    except (ValueError, TypeError):
                        break
    return None


def _coerce_briefing(raw):
    """Normalize the tool payload to {"team_summary": [...], "sections": [...]}.

    Sonnet sometimes JSON-encodes the whole briefing into one field instead of
    filling the schema (seen 2026-08-05 in production: the entire object came
    back as a 6KB string under `sections`, while `stop_reason` was a clean
    `tool_use`). The content is intact — just nested — so unwrap it rather than
    throwing away a briefing the model actually produced.
    """
    if isinstance(raw, str):
        raw = _loads_tolerant(raw)
    if not isinstance(raw, dict):
        return {}

    out = dict(raw)
    for key in ("sections", "team_summary"):
        value = out.get(key)
        if not isinstance(value, str):
            continue
        parsed = _loads_tolerant(value)
        if isinstance(parsed, list):
            out[key] = parsed
        elif isinstance(parsed, dict):
            # The whole briefing was stringified into this single field.
            for inner in ("sections", "team_summary"):
                if isinstance(parsed.get(inner), list) and not isinstance(out.get(inner), list):
                    out[inner] = parsed[inner]

    # Anything still not a list is unusable. Drop it rather than handing a bare
    # string downstream — iterating one yields single characters, which is how
    # the 2026-08-05 run logged 13 "non-object section entry" issues.
    for key in ("sections", "team_summary"):
        if key in out and not isinstance(out[key], list):
            out[key] = []
    return out


def _assemble_sections(all_team_members, user_by_name, accepted, ooo_users,
                       calendar_data, toggl_summary):
    """Render every team member's section from the source records.

    The Slack-mention header, the calendar line and the hours line are all
    written here from the user map / Google Calendar / Toggl, never by the
    model. Anyone without an accepted section gets a visible placeholder rather
    than being silently dropped — or worse, inheriting someone else's tasks.

    Returns (per_user {slack_id: text}, [section text in display order], issues).
    """
    per_user = {}
    rendered = []
    issues = []

    for name in sorted(all_team_members):
        user = user_by_name.get(name)
        if not user:
            issues.append(f"{name} has no Slack ID in the user map — no section posted")
            continue
        if name in ooo_users:
            section = _render_ooo_section(user, ooo_users[name])
        elif name in accepted:
            section = _render_section(
                user,
                accepted[name]["priorities"],
                notes=accepted[name].get("notes"),
                calendar_line=_calendar_line((calendar_data or {}).get(name)),
                hours_line=_hours_line(user, toggl_summary),
            )
        else:
            issues.append(f"no usable section for {name} — placeholder posted")
            lines = [
                f"*<@{user['slack_user_id']}>*",
                f":warning: Jack Bot didn't generate priorities for {name} this run — "
                f"check Asana directly. Retry also failed.",
                _calendar_line((calendar_data or {}).get(name)),
            ]
            hours = _hours_line(user, toggl_summary)
            if hours:
                lines.append(hours)
            section = "\n".join(lines)
        per_user[user["slack_user_id"]] = section
        rendered.append(section)

    return per_user, rendered, issues


def _request_briefing(client, user_content, max_tokens=10000):
    """Ask Claude for the briefing as a forced tool call and return its input.

    Forcing the tool means the model can't drift into free-form prose with
    hand-written section headers — the shape is validated by the API before we
    ever see it.
    """
    message = client.messages.create(
        model="claude-sonnet-5",
        thinking={"type": "disabled"},
        max_tokens=max_tokens,
        system=SYNTHESIS_PROMPT,
        tools=[BRIEFING_TOOL],
        tool_choice={"type": "tool", "name": BRIEFING_TOOL["name"]},
        messages=[{"role": "user", "content": user_content}],
    )
    # A truncated tool call comes back with an empty `input`, so surface the
    # cause instead of letting it look like the model returned nothing.
    if message.stop_reason == "max_tokens":
        raise RuntimeError(
            f"briefing truncated at max_tokens={max_tokens} "
            f"({message.usage.output_tokens} output tokens) — raise max_tokens"
        )
    for block in message.content:
        if getattr(block, "type", "") == "tool_use":
            return _coerce_briefing(block.input or {})
    return {}


def _load_employee_roster():
    """Load the canonical employee roster from knowledge/contacts/employees.md.

    Returns a set of employee names (lowercase) for sanity-checking coverage.
    """
    path = KNOWLEDGE_DIR / "contacts" / "employees.md"
    if not path.exists():
        return set()
    names = set()
    for line in path.read_text().splitlines():
        line = line.strip()
        if line.startswith("- **") and "**" in line[4:]:
            name = line.split("**")[1]
            if name:
                names.add(name.lower())
    return names


RIPPLING_PTO_URL = (
    "https://app.rippling.com/api/feed/calendar/pto/company/"
    "5m0bzx1y0kkj3p1o/fcfe907c8ebaecb9f70456be1c62a14b50672e94ae3004d360be9fff2310b732/"
    "calendar.ics?company=5e973eb93ca04e04172697e5"
)


def _detect_ooo(calendar_data, users):
    """Detect users who are out of office using Rippling PTO calendar.

    Fetches the company ICS feed and checks for events covering today.
    Returns a dict of {name: reason} for users who are OOO today.
    """
    import requests

    ooo_users = {}
    try:
        resp = requests.get(RIPPLING_PTO_URL, timeout=10)
        resp.raise_for_status()
        ics_text = resp.text
    except Exception:
        return ooo_users

    today_str = date.today().strftime("%Y%m%d")

    # Load uid_map.json so a Slack display_name like "Nate" still matches a
    # Rippling ICS entry like "Nathaniel Straus" — we expand each user's
    # token set with preferred_first / formal_first / last from the canonical
    # identity record.
    uid_aliases = {}  # slack_user_id -> set of extra tokens
    uid_full_name = {}  # slack_user_id -> "Preferred Last" canonical full name
    try:
        uid_map_path = KNOWLEDGE_DIR / "contacts" / "uid_map.json"
        with uid_map_path.open() as f:
            uid_data = json.load(f)
        for entry in uid_data.get("users", []):
            sid = entry.get("slack_user_id")
            if not sid:
                continue
            extras = set()
            for key in ("preferred_first", "formal_first", "last", "canonical_name", "rippling_name"):
                val = entry.get(key)
                if val:
                    extras.update(val.lower().split())
            uid_aliases[sid] = extras
            preferred = entry.get("preferred_first") or entry.get("formal_first") or ""
            last = entry.get("last") or ""
            full = f"{preferred} {last}".strip()
            if full:
                uid_full_name[sid] = full
    except Exception:
        pass

    # Build per-user (name, token_set) pairs for tighter matching.
    # We match by exact full-name (case-insensitive) first, then fall back
    # to requiring the ICS first+last tokens both be present in exactly
    # one user's name tokens. Never match on a single token alone.
    user_entries = []  # list of (original_name, lowercase_name, set_of_tokens)
    exact_lookup = {}
    for u in users:
        uname = u.get("name", "")
        if not uname:
            continue
        lower = uname.lower()
        tokens = set(lower.split())
        sid = u.get("slack_user_id")
        if sid and sid in uid_aliases:
            tokens |= uid_aliases[sid]
            # Also let the canonical "Preferred Last" form satisfy the exact-match path
            if sid in uid_full_name:
                exact_lookup[uid_full_name[sid].lower()] = uname
        exact_lookup[lower] = uname
        user_entries.append((uname, lower, tokens))

    def _match_ics_name(person):
        lower = person.lower().strip()
        if not lower:
            return None
        # 1) exact full-name match
        if lower in exact_lookup:
            return exact_lookup[lower]
        # 2) first+last token both present in exactly one user's tokens
        parts = lower.split()
        if len(parts) < 2:
            return None
        first_tok, last_tok = parts[0], parts[-1]
        if first_tok == last_tok:
            # would collapse to a single-token match; refuse
            return None
        candidates = [
            name for (name, _l, toks) in user_entries
            if first_tok in toks and last_tok in toks
        ]
        if len(candidates) == 1:
            return candidates[0]
        # 3) last-name-only fallback, but only if the last token uniquely
        # identifies one user (Rippling sometimes uses formal first names like
        # "Daniel" while the user map has "Dan"). First-name alone is NOT
        # allowed — first names collide too easily.
        last_only = [
            name for (name, _l, toks) in user_entries if last_tok in toks
        ]
        if len(last_only) == 1:
            return last_only[0]
        return None

    # Parse ICS events
    for event_block in ics_text.split("BEGIN:VEVENT")[1:]:
        summary = ""
        dtstart = ""
        dtend = ""
        for line in event_block.splitlines():
            if line.startswith("SUMMARY:"):
                summary = line[8:]
            if "DTSTART" in line:
                m = re.search(r"(\d{8})", line)
                if m:
                    dtstart = m.group(1)
            if "DTEND" in line:
                m = re.search(r"(\d{8})", line)
                if m:
                    dtend = m.group(1)

        if not (dtstart and dtend):
            continue
        # Check if today falls within the event range (DTEND is exclusive in ICS)
        if dtstart <= today_str < dtend:
            # Extract person name from summary like "Sam Hild on Time Off Request"
            match = re.match(r"^(.+?)\s+on\s+(.+)$", summary)
            if match:
                person = match.group(1).strip()
                reason = match.group(2).strip()
                matched_name = _match_ics_name(person)
                if matched_name:
                    ooo_users[matched_name] = reason

    return ooo_users


def _has_knowledge_files():
    """Check whether pre-distilled knowledge files are available."""
    # Require at least the contacts employees list and toggl summary to consider
    # knowledge files usable.
    return (
        (KNOWLEDGE_DIR / "contacts" / "employees.md").exists()
        and (KNOWLEDGE_DIR / "toggl" / "summary.md").exists()
    )


def _read_file(path, max_chars=None):
    """Read a file and return its contents, or empty string on failure."""
    try:
        text = Path(path).read_text()
        if max_chars:
            text = text[:max_chars]
        return text
    except Exception:
        return ""


def _load_knowledge_context(users=None):
    """Load pre-distilled knowledge files into a compact context string.

    This replaces the expensive live-fetch of historical data (full Asana
    project lists, all Toggl history, full contacts list, Drive inventory)
    with pre-scanned summaries that are much smaller.

    Only summaries and team-relevant per-person files are loaded — not every
    single project file.
    """
    sections = []

    # --- Asana strategic overview ---
    asana_summary = _read_file(KNOWLEDGE_DIR / "asana" / "summary.md")
    if asana_summary:
        sections.append(f"=== KNOWLEDGE: ASANA STRATEGIC OVERVIEW ===\n{asana_summary}")
    else:
        # Fall back to loading a handful of key project files for context
        proj_dir = KNOWLEDGE_DIR / "asana" / "projects"
        if proj_dir.exists():
            key_files = ["001-13_bd_pipeline.md", "001-13_proposals.md",
                         "view_major_milestones_tasks.md",
                         "001-13_corporate_strategic_planning.md"]
            loaded = []
            for fname in key_files:
                text = _read_file(proj_dir / fname, max_chars=2000)
                if text:
                    loaded.append(text)
            if loaded:
                sections.append(
                    "=== KNOWLEDGE: KEY ASANA PROJECTS ===\n"
                    + "\n---\n".join(loaded)
                )

    # --- Toggl overview ---
    toggl_summary = _read_file(KNOWLEDGE_DIR / "toggl" / "summary.md")
    if toggl_summary:
        sections.append(f"=== KNOWLEDGE: TIME TRACKING OVERVIEW ===\n{toggl_summary}")

    # --- Per-person Toggl (only for users in the current team) ---
    if users:
        person_dir = KNOWLEDGE_DIR / "toggl" / "by_person"
        if person_dir.exists():
            person_snippets = []
            for u in users:
                name = u.get("name", "")
                if not name:
                    continue
                # Try a few filename patterns, including every known spelling of
                # the name — the canonical name is "Joshua Fromm" but the scanner
                # wrote josh_fromm.md.
                candidates = []
                for spelling in [name] + list(u.get("aliases") or []):
                    candidates.append(spelling.lower().replace(" ", "_") + ".md")
                    if " " in spelling:
                        candidates.append(spelling.split()[0].lower() + ".md")
                for cand in candidates:
                    if cand and (person_dir / cand).exists():
                        text = _read_file(person_dir / cand, max_chars=1500)
                        if text:
                            person_snippets.append(text)
                        break
            if person_snippets:
                sections.append(
                    "=== KNOWLEDGE: TEAM TIME PATTERNS ===\n"
                    + "\n---\n".join(person_snippets)
                )

    # --- Team directory (employees) ---
    employees = _read_file(KNOWLEDGE_DIR / "contacts" / "employees.md")
    if employees:
        sections.append(f"=== KNOWLEDGE: BST CURRENT EMPLOYEES ===\n{employees}")
    else:
        # Fall back to old directory.md
        directory = _read_file(KNOWLEDGE_DIR / "contacts" / "directory.md")
        if directory:
            sections.append(f"=== KNOWLEDGE: BST TEAM DIRECTORY ===\n{directory}")

    # --- External contacts (truncated) ---
    external = _read_file(KNOWLEDGE_DIR / "contacts" / "external.md", max_chars=3000)
    if external:
        sections.append(f"=== KNOWLEDGE: KEY EXTERNAL CONTACTS ===\n{external}")

    # --- Slack channel summaries ---
    slack_dir = KNOWLEDGE_DIR / "slack"
    if slack_dir.exists():
        slack_parts = []
        for f in sorted(slack_dir.glob("*.md")):
            text = _read_file(f, max_chars=1500)
            if text:
                slack_parts.append(text)
        if slack_parts:
            sections.append(
                "=== KNOWLEDGE: SLACK CHANNEL CONTEXT ===\n"
                + "\n---\n".join(slack_parts)
            )

    # --- Email patterns ---
    email_dir = KNOWLEDGE_DIR / "email"
    if email_dir.exists():
        email_parts = []
        for f in sorted(email_dir.glob("*.md")):
            text = _read_file(f, max_chars=1000)
            if text:
                email_parts.append(text)
        if email_parts:
            sections.append(
                "=== KNOWLEDGE: EMAIL PATTERNS ===\n"
                + "\n---\n".join(email_parts)
            )

    # --- Financial overview (merged cross-referenced data) ---
    fin_overview = _read_file(KNOWLEDGE_DIR / "financial" / "overview.md", max_chars=4000)
    if fin_overview:
        sections.append(f"=== KNOWLEDGE: FINANCIAL HEALTH OVERVIEW ===\n{fin_overview}")
    else:
        # Fall back to raw source summaries if financial index hasn't been built
        budget_summary = _read_file(KNOWLEDGE_DIR / "budgets" / "summary.md", max_chars=3000)
        if budget_summary:
            sections.append(f"=== KNOWLEDGE: PROJECT BUDGETS ===\n{budget_summary}")
        qbo_summary = _read_file(KNOWLEDGE_DIR / "quickbooks" / "summary.md", max_chars=3000)
        if qbo_summary:
            sections.append(f"=== KNOWLEDGE: QUICKBOOKS FINANCIALS ===\n{qbo_summary}")

    # --- Proposals catalog ---
    proposals_catalog = _read_file(KNOWLEDGE_DIR / "proposals" / "catalog.md", max_chars=3000)
    if proposals_catalog:
        sections.append(f"=== KNOWLEDGE: PROPOSALS & REPORTS CATALOG ===\n{proposals_catalog}")

    # --- Project registry ---
    registry = _read_file(KNOWLEDGE_DIR / "projects" / "registry.md", max_chars=4000)
    if registry:
        sections.append(f"=== KNOWLEDGE: PROJECT REGISTRY ===\n{registry}")

    return "\n\n".join(sections)


def run_daily_pipeline(slack_client):
    """Run the full daily research pipeline. Returns the full summary text."""
    errors = []

    try:
        users = build_user_map(slack_client)
    except Exception as e:
        errors.append(f"User mapping: {e}")
        users = []

    # Log user map and data source results for debugging
    try:
        debug_lines = [f"Pipeline started at {datetime.now().strftime('%Y-%m-%d %H:%M')} UTC"]
        debug_lines.append(f"Users mapped: {len(users)}")
        for u in users:
            toggl_ids = u.get("toggl_user_ids") or [u.get("toggl_user_id")]
            debug_lines.append(f"  {u['name']} | email: {u['email']} | slack: {u['slack_user_id']} | asana: {u['asana_user_gid']} | toggl: {toggl_ids}")
        store_entry(slack_client, "DEBUG", "\n".join(debug_lines))
    except Exception:
        pass

    # Test knowledge channel access and count all messages
    try:
        knowledge_ch = os.environ.get("KNOWLEDGE_CHANNEL", "")
        if knowledge_ch:
            total = 0
            cursor = None
            while True:
                kwargs = {"channel": knowledge_ch, "limit": 200}
                if cursor:
                    kwargs["cursor"] = cursor
                test = slack_client.conversations_history(**kwargs)
                total += len(test.get("messages", []))
                cursor = test.get("response_metadata", {}).get("next_cursor")
                if not cursor:
                    break
            # Also test get_knowledge
            all_entries = get_knowledge(slack_client)
            corrections = [e for e in all_entries if e["type"] == "CORRECTION"]
            store_entry(slack_client, "DEBUG",
                f"Knowledge channel: {total} total msgs, {len(all_entries)} parsed entries, {len(corrections)} corrections")
    except Exception as e:
        store_entry(slack_client, "DEBUG", f"Knowledge channel error: {e}")

    # Mirror #operations replies → FEEDBACK entries before we read the
    # knowledge summary, so today's prompt honors comments people made as
    # plain replies (not just `correct:` commands).
    try:
        _sync_operations_feedback(slack_client)
    except Exception as e:
        errors.append(f"operations feedback sync: {e}")

    # Determine whether pre-distilled knowledge files are available.
    # When they are, we skip expensive historical fetches (full contacts,
    # full Drive inventory, meeting notes) and rely on the knowledge layer
    # for that context.  We still fetch LIVE / time-sensitive data every run.
    use_knowledge_files = _has_knowledge_files()

    # Get known file IDs from knowledge base to skip already-processed files
    known_file_ids = None
    try:
        known_entries = get_knowledge(slack_client, ["PROJECT"], days=30)
        # Extract any file IDs mentioned in project entries (future optimization)
        known_file_ids = set()
    except Exception:
        pass

    # ------------------------------------------------------------------
    # Fetch data in parallel.
    # ALWAYS fetched (time-sensitive / live delta):
    #   - Asana tasks (current state of assignments & due dates)
    #   - Toggl (yesterday's hours)
    #   - Calendar (today's meetings)
    #   - Gmail (last 24h subject lines)
    #   - Slack (last 24h messages)
    #   - Operations channel (recent context)
    #   - Slack knowledge channel (user corrections / priorities)
    # SKIPPED when knowledge files exist (historical / slow-changing):
    #   - Key projects (BD pipeline, proposals, milestones) — covered by
    #     knowledge/asana/projects/*.md
    #   - Contacts — covered by knowledge/contacts/*.md
    #   - Drive activity — covered by knowledge/drive/*.md
    #   - Meeting notes — covered by knowledge/slack/*.md context
    # ------------------------------------------------------------------
    with ThreadPoolExecutor(max_workers=12) as executor:
        # Always-live futures
        asana_future = executor.submit(_collect_asana)
        toggl_future = executor.submit(_collect_toggl)
        gmail_future = executor.submit(_collect_gmail, users)
        calendar_future = executor.submit(_collect_calendar, users)
        slack_future = executor.submit(_collect_slack, slack_client, users)
        ops_future = executor.submit(_collect_operations_history, slack_client)
        knowledge_future = executor.submit(get_knowledge_summary, slack_client)
        overrides_future = executor.submit(get_status_overrides, slack_client)

        # Conditionally-live futures (skipped when knowledge files exist)
        key_projects_future = None
        drive_future = None
        meeting_notes_future = None
        contacts_future = None
        if not use_knowledge_files:
            key_projects_future = executor.submit(_collect_key_projects)
            drive_future = executor.submit(_collect_drive, users, known_file_ids)
            meeting_notes_future = executor.submit(_collect_meeting_notes, users)
            contacts_future = executor.submit(_collect_contacts, users)

        # Collect results — always-live
        asana_tasks = asana_future.result()
        toggl_summary = toggl_future.result()
        gmail_data = gmail_future.result()
        calendar_data = calendar_future.result()
        slack_messages = slack_future.result()
        operations_history = ops_future.result()
        knowledge_context = knowledge_future.result()
        status_overrides = overrides_future.result()

        # Collect results — conditional
        key_projects = key_projects_future.result() if key_projects_future else {}
        drive_activity = drive_future.result() if drive_future else {}
        meeting_notes = meeting_notes_future.result() if meeting_notes_future else []
        contacts = contacts_future.result() if contacts_future else []

    # Load pre-distilled knowledge context (empty string if files missing)
    distilled_context = ""
    if use_knowledge_files:
        try:
            distilled_context = _load_knowledge_context(users)
        except Exception as e:
            errors.append(f"[Knowledge files load error: {e}]")

    # Log data source results
    try:
        data_lines = [f"Data sources (knowledge_files={'ON' if use_knowledge_files else 'OFF'}):"]
        if isinstance(asana_tasks, list):
            data_lines.append(f"  Asana: {len(asana_tasks)} tasks")
            assignees = set(t.get("assignee_name", "?") for t in asana_tasks)
            data_lines.append(f"  Asana assignees: {', '.join(assignees)}")
        else:
            data_lines.append(f"  Asana: {asana_tasks}")
        if isinstance(key_projects, dict) and key_projects:
            data_lines.append(f"  BD Pipeline: {len(key_projects.get('bd_pipeline', []))} items")
            data_lines.append(f"  Proposals: {len(key_projects.get('proposals', []))} items")
            data_lines.append(f"  Milestones: {len(key_projects.get('milestones', []))} items")
        elif use_knowledge_files:
            data_lines.append("  BD/Proposals/Milestones: using knowledge files")
        data_lines.append(f"  Toggl: {type(toggl_summary).__name__} - {toggl_summary if isinstance(toggl_summary, str) else f'{len(toggl_summary)} users'}")
        data_lines.append(f"  Drive: {'knowledge files' if use_knowledge_files else f'{len(drive_activity)} users with activity'}")
        data_lines.append(f"  Meeting notes: {'knowledge files' if use_knowledge_files else f'{len(meeting_notes)} docs'}")
        data_lines.append(f"  Gmail: {len(gmail_data)} users with emails")
        data_lines.append(f"  Calendar: {len(calendar_data)} users with events")
        data_lines.append(f"  Operations: {len(operations_history)} messages")
        data_lines.append(f"  Slack: {len(slack_messages) if isinstance(slack_messages, list) else slack_messages}")
        if distilled_context:
            data_lines.append(f"  Knowledge context: {len(distilled_context)} chars")
        if status_overrides:
            data_lines.append(f"  Status overrides: {len(status_overrides)} chars")
        else:
            data_lines.append("  Status overrides: none")
        store_entry(slack_client, "DEBUG", "\n".join(data_lines))
    except Exception:
        pass

    # Track which data sources returned errors
    if isinstance(asana_tasks, str) and "unavailable" in asana_tasks:
        errors.append(asana_tasks)
    if isinstance(toggl_summary, str) and "unavailable" in toggl_summary:
        errors.append(toggl_summary)
    if isinstance(slack_messages, str) and "unavailable" in slack_messages:
        errors.append(slack_messages)
    if not use_knowledge_files:
        if not drive_activity:
            errors.append("[Google Drive returned no data]")
    if not gmail_data:
        errors.append("[Gmail returned no data]")
    if not calendar_data:
        errors.append("[Google Calendar returned no data]")

    # Log errors to the knowledge channel
    if errors:
        error_summary = f"Pipeline run at {datetime.now().strftime('%Y-%m-%d %H:%M')} UTC\n" + "\n".join(errors)
        try:
            store_entry(slack_client, "ERROR", error_summary)
        except Exception:
            pass

    bot_user_id = None
    try:
        bot_user_id = slack_client.auth_test().get("user_id")
    except Exception:
        pass

    context = _assemble_context(
        asana_tasks, toggl_summary, drive_activity, gmail_data, calendar_data,
        contacts, slack_messages, users,
        key_projects=key_projects, meeting_notes=meeting_notes,
        operations_history=operations_history, bot_user_id=bot_user_id,
    )

    # Load canonical employee roster for sanity check
    employee_roster = _load_employee_roster()

    # Detect OOO users from calendar
    ooo_users = _detect_ooo(calendar_data, users)

    # Build the FULL team list — every user in the map gets a section.
    # Not just people with Asana tasks — everyone.
    all_team_members = set()
    for u in users:
        if u.get("name") and u.get("slack_user_id"):
            all_team_members.add(u["name"])

    # Sanity check: warn if employee roster has people missing from the user map
    # Match on full name, first name, or last name since user map may use short names
    if employee_roster:
        mapped_lower = {n.lower() for n in all_team_members}
        mapped_parts = set()
        for n in mapped_lower:
            mapped_parts.add(n)
            for part in n.split():
                mapped_parts.add(part)
        missing = [n for n in employee_roster
                   if n not in mapped_parts
                   and not any(part in mapped_parts for part in n.split())]
        if missing:
            try:
                store_entry(slack_client, "DEBUG",
                    f"Employee roster sanity check: {len(missing)} employees not in user map: {', '.join(missing)}\n"
                    f"(They may be missing a Slack, Asana, or Toggl account)")
            except Exception:
                pass

    # The model never sees Slack IDs — it works in canonical names only, and the
    # code maps name -> ID when rendering. That removes the ID-copying step that
    # used to silently attach one person's tasks to another person's mention.
    active_names = [n for n in sorted(all_team_members) if n not in ooo_users]
    ooo_names = [n for n in sorted(all_team_members) if n in ooo_users]
    active_list = "".join(f"  - {n}\n" for n in active_names)
    ooo_list = "".join(f"  - {n} (OOO: {ooo_users[n]})\n" for n in ooo_names)
    user_by_name = {
        u["name"]: u for u in users if u.get("name") and u.get("slack_user_id")
    }

    # Combine: status overrides (top, authoritative) + distilled knowledge +
    # Slack knowledge channel + live data
    full_context = context
    if distilled_context:
        full_context = f"{distilled_context}\n\n{full_context}"
    if knowledge_context:
        full_context = f"{knowledge_context}\n\n{full_context}"
    if status_overrides:
        override_block = (
            "===== PROJECT STATUS OVERRIDES (AUTHORITATIVE — WINS OVER ALL OTHER DATA) =====\n"
            "The following status deltas were extracted from recent team corrections and feedback. "
            "They override Asana task state, distilled knowledge files, and everything below. "
            "If any of these conflict with an Asana task or a knowledge file, the override wins. "
            "Do NOT list overridden items as priorities or as overdue.\n\n"
            f"{status_overrides}\n"
            "===== END OVERRIDES =====\n"
        )
        full_context = f"{override_block}\n{full_context}"

    total_sections = len(active_names)
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    base_prompt = (
        f"Today's date is {date.today().isoformat()}.\n\n"
        f"{full_context}\n\n"
        f"===== REQUIRED PEOPLE =====\n"
        f"Use these names EXACTLY — they are the only valid values for `person`.\n\n"
        f"ACTIVE team members ({total_sections} entries required, one each):\n{active_list}\n"
        + (f"OUT OF OFFICE today (do NOT produce entries for these people):\n{ooo_list}\n"
           if ooo_list else "")
    )

    issues = []
    try:
        briefing = _request_briefing(client, base_prompt, max_tokens=10000)
    except Exception as e:
        briefing = {}
        errors.append(f"Briefing synthesis failed: {e}")
        issues.append(f"synthesis call failed: {e}")

    accepted, section_issues = _validate_sections(
        briefing.get("sections"), set(active_names)
    )
    issues.extend(section_issues)

    # Cross-contamination guard: near-identical bodies under two names mean one
    # person's work got copied onto someone else. Drop the copy and regenerate it.
    for copied_name, source_name, ratio in _find_copied_sections(accepted):
        issues.append(
            f"{copied_name}'s priorities were {int(ratio * 100)}% identical to "
            f"{source_name}'s — dropped as a mis-assignment, will retry"
        )
        accepted.pop(copied_name, None)

    # Missing-person guard: every ACTIVE member must have their own real section.
    # This checks content, not just that a key exists — the old ID-keyed version
    # passed on 2026-08-05 while Joshua Fromm's slot held Jack Elston's tasks.
    missing_names = [n for n in active_names if n not in accepted]
    if missing_names:
        issues.append(f"missing after first pass: {sorted(missing_names)} — retrying")
        retry_list = "".join(f"  - {n}\n" for n in missing_names)
        try:
            retry_briefing = _request_briefing(
                client,
                f"Today's date is {date.today().isoformat()}.\n\n"
                f"{full_context}\n\n"
                f"===== RETRY — MISSING PEOPLE =====\n"
                f"Your previous response did not produce a usable entry for the people "
                f"below. Produce entries for ONLY these people, using their names "
                f"EXACTLY as written. Each entry must contain that person's OWN "
                f"priorities — do not copy another person's work and do not "
                f"cross-reference another section. Return an empty `team_summary`.\n\n"
                f"{retry_list}",
                # Sized for the worst case (every active member missing), not
                # the typical one-or-two — a truncated retry returns nothing.
                max_tokens=max(3000, 700 * len(missing_names)),
            )
            retry_accepted, retry_issues = _validate_sections(
                retry_briefing.get("sections"), set(missing_names)
            )
            issues.extend(f"retry: {msg}" for msg in retry_issues)
            accepted.update(retry_accepted)
            # The retry can copy someone else's work too. If it did, drop it and
            # let the placeholder show — a visible gap beats a wrong assignment.
            for copied_name, source_name, ratio in _find_copied_sections(accepted):
                issues.append(
                    f"retry: {copied_name}'s priorities were {int(ratio * 100)}% "
                    f"identical to {source_name}'s — dropped, no section will be posted"
                )
                accepted.pop(copied_name, None)
        except Exception as e:
            issues.append(f"retry call failed: {e}")

    per_user, rendered, render_issues = _assemble_sections(
        all_team_members, user_by_name, accepted, ooo_users,
        calendar_data, toggl_summary,
    )
    issues.extend(render_issues)

    team_summary_text = _render_team_summary(briefing.get("team_summary"))
    full_summary = "\n\n".join([team_summary_text] + rendered)

    if issues:
        try:
            store_entry(slack_client, "DEBUG",
                        "Briefing validation issues:\n" + "\n".join(f"  - {i}" for i in issues))
        except Exception:
            pass

    set_cache(full_summary, per_user, team_summary_text)

    # Debug: log what was parsed
    try:
        # Log name -> ID -> first priority so a mis-assignment is visible at a
        # glance in the knowledge channel rather than only in #operations.
        parse_debug = [f"Rendered {len(per_user)} user sections"]
        for name in sorted(all_team_members):
            user = user_by_name.get(name)
            if not user:
                continue
            section = per_user.get(user["slack_user_id"], "")
            body = [ln for ln in section.splitlines()[1:] if ln.strip()]
            parse_debug.append(
                f"  {name} ({user['slack_user_id']}): {body[0][:80] if body else '(empty)'}"
            )
        parse_debug.append(f"Team summary length: {len(team_summary_text)} chars")
        store_entry(slack_client, "DEBUG", "\n".join(parse_debug))
    except Exception:
        pass

    # Post-pipeline: extract new knowledge and store snapshot
    try:
        auto_extract_knowledge(slack_client, context)
    except Exception:
        pass
    try:
        store_daily_snapshot(slack_client, full_summary)
    except Exception:
        pass

    # TODO: Trigger incremental knowledge scan after pipeline completes.
    # This should update knowledge/ files with any new data discovered
    # during this run (new Asana tasks, new Toggl entries, new Slack
    # messages since last scan).  For now the scan.py scanner runs
    # separately; integrate a lightweight "since last scan" update here
    # once the scanner supports incremental mode.

    return full_summary


def maybe_run_on_startup(slack_client):
    """Run pipeline on startup if it's a weekday during work hours and cache is empty."""
    from research_cache import is_stale
    denver = ZoneInfo("America/Denver")
    now = datetime.now(denver)
    if now.weekday() < 5 and 8 <= now.hour < 18 and is_stale():
        try:
            run_daily_pipeline(slack_client)
        except Exception:
            pass
