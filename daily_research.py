import os
import re
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime
from zoneinfo import ZoneInfo

import anthropic

from user_map import build_user_map, get_all_users, get_user_by_email
from asana_client import get_enriched_tasks, get_key_project_data, get_workspaces
from toggl_client import get_time_summary
from google_client import get_recent_drive_activity, get_recent_emails, get_todays_calendar, get_contacts, get_meeting_notes_content
from slack_data_client import get_recent_slack_messages
from research_cache import set_cache
from knowledge import get_knowledge_summary, auto_extract_knowledge, store_daily_snapshot, store_entry, get_knowledge

# Operations channel for previous task summaries
OPERATIONS_CHANNEL = "C015QR6P5S4"

SYNTHESIS_PROMPT = """\
You are a project manager AI for Black Swift Technologies (BST), a small aerospace/UAS company. \
You are given data from multiple sources: Asana tasks (including BD Pipeline, Proposals, and \
milestones with dollar amounts), time tracking (Toggl), Google Calendar, Google Drive activity \
(from Sales and Federal Projects shared drives), weekly all-hands meeting notes, Gmail subjects, \
Slack messages (including #operations channel history), and a company knowledge base.

Your job is to synthesize this into a prioritized daily briefing.

You also receive a COMPANY KNOWLEDGE BASE with accumulated context about projects, clients, \
priorities, and team dynamics. Use this to inform your prioritization. If there are corrections \
from users, respect those — they override your default reasoning.

PRIORITIZATION RULES (in order of weight):
1. User corrections from the knowledge base — if someone said "X is more important", honor that
2. OVERDUE tasks or tasks due today — always top priority
3. Tasks on high-dollar projects (use milestone subtask dollar amounts, BD Pipeline, and knowledge base)
4. Tasks with risk signals: mentioned blockers in Slack, client emails about deadlines, \
low hours tracked vs. approaching due date
5. Tasks where someone tracked 0 hours yesterday but has upcoming deadlines
6. Upcoming deliverables from the knowledge base
7. Everything else by due date proximity

If a YESTERDAY'S SUMMARY is provided, note what changed — completed tasks, shifted priorities, \
new items. Briefly mention key changes in the team summary.

OUTPUT FORMAT:
First, produce a TEAM SUMMARY section (3-5 bullet points of the most important things \
for today across the whole team).

Then, for EACH team member, produce a section with EXACTLY this format:

### [Person Name]
*Top 3 priorities today:*
1. [Task name] -- [why this is priority] (Due: [date])
2. [Task name] -- [why this is priority] (Due: [date])
3. [Task name] -- [why this is priority] (Due: [date])

_Calendar:_ [List today's meetings if any, note conflicts with focus time]

_Context:_ [1-2 sentences noting relevant emails, Drive activity, or Slack threads \
that relate to their tasks]

_Yesterday:_ [Hours tracked] hours ([project breakdown])

Use Slack mrkdwn formatting (*bold*, _italic_). Be concise and actionable.
Do not speculate -- only reference information present in the data.
If a team member has fewer than 3 tasks, list what they have.

IMPORTANT: Include a section for EVERY team member who has tasks assigned in Asana. \
Do not skip anyone. If the team has 12 people with tasks, produce 12 sections."""


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
        oldest = str(time.time() - (7 * 86400))  # last 7 days
        result = slack_client.conversations_history(
            channel=OPERATIONS_CHANNEL, limit=50, oldest=oldest,
        )
        messages = []
        for msg in result.get("messages", []):
            if msg.get("subtype"):
                continue
            messages.append(msg.get("text", "")[:300])
        messages.reverse()
        return messages
    except Exception as e:
        return [f"[Operations channel error: {e}]"]


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


def _assemble_context(asana_tasks, toggl_summary, drive_activity, gmail_data, calendar_data, contacts, slack_messages, users, key_projects=None, meeting_notes=None, operations_history=None):
    """Build the context document for Claude."""
    sections = []

    # Team overview
    names = [u["name"] for u in users if u["name"]]
    sections.append(f"=== TEAM OVERVIEW ===\nUsers: {', '.join(names)}")

    # Asana
    if isinstance(asana_tasks, str):
        sections.append(f"=== ASANA TASKS ===\n{asana_tasks}")
    else:
        lines = ["=== ASANA TASKS ==="]
        for task in asana_tasks:
            assignee = task.get("assignee_name", "Unassigned")
            due = task.get("due_on", "No due date")
            project = task.get("project_name", "")
            notes = (task.get("notes", "") or "")[:200]
            custom = ""
            for cf in task.get("custom_fields", []) or []:
                if cf and cf.get("display_value"):
                    custom += f" [{cf.get('name', '')}: {cf['display_value']}]"
            lines.append(f"- {task['name']} | Project: {project} | Assigned: {assignee} | Due: {due}{custom}")
            if notes:
                lines.append(f"  Notes: {notes}")
        sections.append("\n".join(lines))

    # Key projects (BD Pipeline, Proposals, Milestones)
    if key_projects and isinstance(key_projects, dict):
        if key_projects.get("bd_pipeline"):
            lines = ["=== BD PIPELINE ==="]
            for t in key_projects["bd_pipeline"]:
                custom = ""
                for cf in t.get("custom_fields", []) or []:
                    if cf and cf.get("display_value"):
                        custom += f" [{cf.get('name', '')}: {cf['display_value']}]"
                lines.append(f"- {t['name']} | Due: {t.get('due_on', 'N/A')}{custom}")
            sections.append("\n".join(lines))

        if key_projects.get("proposals"):
            lines = ["=== PROPOSALS ==="]
            for t in key_projects["proposals"]:
                custom = ""
                for cf in t.get("custom_fields", []) or []:
                    if cf and cf.get("display_value"):
                        custom += f" [{cf.get('name', '')}: {cf['display_value']}]"
                lines.append(f"- {t['name']} | Due: {t.get('due_on', 'N/A')}{custom}")
            sections.append("\n".join(lines))

        if key_projects.get("milestones"):
            lines = ["=== MILESTONES (with subtask dollar amounts) ==="]
            for m in key_projects["milestones"]:
                lines.append(f"- MILESTONE: {m['name']} | Project: {m.get('project_name', '')} | Due: {m.get('due_on', 'N/A')}")
                for st in m.get("subtasks", []):
                    custom = ""
                    for cf in st.get("custom_fields", []) or []:
                        if cf and cf.get("display_value"):
                            custom += f" [{cf.get('name', '')}: {cf['display_value']}]"
                    lines.append(f"  - {st['name']}{custom}")
            sections.append("\n".join(lines))

    # Meeting notes
    if meeting_notes:
        lines = ["=== RECENT ALL-HANDS MEETING NOTES ==="]
        for doc in meeting_notes:
            lines.append(f"*{doc['name']}*")
            lines.append(doc["content"])
        sections.append("\n".join(lines))

    # Operations channel history
    if operations_history:
        lines = ["=== #OPERATIONS CHANNEL (recent task context) ==="]
        for msg in operations_history[:30]:
            lines.append(f"  - {msg}")
        sections.append("\n".join(lines))

    # Toggl
    if isinstance(toggl_summary, str):
        sections.append(f"=== TIME TRACKING (Yesterday) ===\n{toggl_summary}")
    else:
        lines = ["=== TIME TRACKING (Yesterday) ==="]
        for email, data in toggl_summary.items():
            user = get_user_by_email(email)
            name = user["name"] if user else email
            proj_parts = [f"{p}: {h}h" for p, h in data["projects"].items()]
            lines.append(f"{name}: {data['total_hours']}h total ({', '.join(proj_parts)})")
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
                lines.append(f"  - {m['user_name']}: {m['text'][:200]}")
        sections.append("\n".join(lines))

    return "\n\n".join(sections)


def _parse_per_user(full_summary, users):
    """Parse Claude's response into per-user sections keyed by Slack user ID."""
    per_user = {}
    # Split on ### headers
    parts = re.split(r"(?=^### )", full_summary, flags=re.MULTILINE)
    for part in parts:
        match = re.match(r"^### (.+)", part)
        if not match:
            continue
        name = match.group(1).strip()
        for user in users:
            if user["name"] and user["name"].lower() in name.lower() and user["slack_user_id"]:
                per_user[user["slack_user_id"]] = part.strip()
                break
    return per_user


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
            debug_lines.append(f"  {u['name']} | email: {u['email']} | slack: {u['slack_user_id']} | asana: {u['asana_user_gid']} | toggl: {u['toggl_user_id']}")
        store_entry(slack_client, "DEBUG", "\n".join(debug_lines))
    except Exception:
        pass

    # Get known file IDs from knowledge base to skip already-processed files
    known_file_ids = None
    try:
        known_entries = get_knowledge(slack_client, ["PROJECT"], days=30)
        # Extract any file IDs mentioned in project entries (future optimization)
        known_file_ids = set()
    except Exception:
        pass

    # Fetch knowledge base and live data in parallel
    with ThreadPoolExecutor(max_workers=12) as executor:
        asana_future = executor.submit(_collect_asana)
        key_projects_future = executor.submit(_collect_key_projects)
        toggl_future = executor.submit(_collect_toggl)
        drive_future = executor.submit(_collect_drive, users, known_file_ids)
        meeting_notes_future = executor.submit(_collect_meeting_notes, users)
        gmail_future = executor.submit(_collect_gmail, users)
        calendar_future = executor.submit(_collect_calendar, users)
        contacts_future = executor.submit(_collect_contacts, users)
        slack_future = executor.submit(_collect_slack, slack_client, users)
        ops_future = executor.submit(_collect_operations_history, slack_client)
        knowledge_future = executor.submit(get_knowledge_summary, slack_client)

        asana_tasks = asana_future.result()
        key_projects = key_projects_future.result()
        toggl_summary = toggl_future.result()
        drive_activity = drive_future.result()
        meeting_notes = meeting_notes_future.result()
        gmail_data = gmail_future.result()
        calendar_data = calendar_future.result()
        contacts = contacts_future.result()
        slack_messages = slack_future.result()
        operations_history = ops_future.result()
        knowledge_context = knowledge_future.result()

    # Log data source results
    try:
        data_lines = ["Data sources:"]
        if isinstance(asana_tasks, list):
            data_lines.append(f"  Asana: {len(asana_tasks)} tasks")
            assignees = set(t.get("assignee_name", "?") for t in asana_tasks)
            data_lines.append(f"  Asana assignees: {', '.join(assignees)}")
        else:
            data_lines.append(f"  Asana: {asana_tasks}")
        if isinstance(key_projects, dict):
            data_lines.append(f"  BD Pipeline: {len(key_projects.get('bd_pipeline', []))} items")
            data_lines.append(f"  Proposals: {len(key_projects.get('proposals', []))} items")
            data_lines.append(f"  Milestones: {len(key_projects.get('milestones', []))} items")
        data_lines.append(f"  Toggl: {type(toggl_summary).__name__} - {toggl_summary if isinstance(toggl_summary, str) else f'{len(toggl_summary)} users'}")
        data_lines.append(f"  Drive: {len(drive_activity)} users with activity")
        data_lines.append(f"  Meeting notes: {len(meeting_notes)} docs")
        data_lines.append(f"  Gmail: {len(gmail_data)} users with emails")
        data_lines.append(f"  Calendar: {len(calendar_data)} users with events")
        data_lines.append(f"  Operations: {len(operations_history)} messages")
        data_lines.append(f"  Slack: {len(slack_messages) if isinstance(slack_messages, list) else slack_messages}")
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

    context = _assemble_context(
        asana_tasks, toggl_summary, drive_activity, gmail_data, calendar_data,
        contacts, slack_messages, users,
        key_projects=key_projects, meeting_notes=meeting_notes,
        operations_history=operations_history,
    )

    # Add Slack @mentions instruction
    mention_map = ""
    for user in users:
        if user["slack_user_id"] and user["name"]:
            mention_map += f"  {user['name']} = <@{user['slack_user_id']}>\n"

    # Combine live data with knowledge base
    full_context = context
    if knowledge_context:
        full_context = f"{knowledge_context}\n\n{context}"

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4000,
        system=SYNTHESIS_PROMPT,
        messages=[{
            "role": "user",
            "content": (
                f"Today's date is {date.today().isoformat()}.\n\n"
                f"When referring to team members in the output, use their Slack mention format:\n{mention_map}\n\n"
                f"{full_context}"
            ),
        }],
    )
    full_summary = message.content[0].text

    per_user = _parse_per_user(full_summary, users)
    set_cache(full_summary, per_user)

    # Post-pipeline: extract new knowledge and store snapshot
    try:
        auto_extract_knowledge(slack_client, context)
    except Exception:
        pass
    try:
        store_daily_snapshot(slack_client, full_summary)
    except Exception:
        pass

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
