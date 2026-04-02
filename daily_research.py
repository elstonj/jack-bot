import os
import re
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime
from zoneinfo import ZoneInfo

import anthropic

from user_map import build_user_map, get_all_users, get_user_by_email
from asana_client import get_enriched_tasks
from toggl_client import get_time_summary
from google_client import get_recent_drive_activity, get_recent_emails
from slack_data_client import get_recent_slack_messages
from research_cache import set_cache

SYNTHESIS_PROMPT = """\
You are a project manager AI for a small team. You are given data from multiple sources: \
Asana tasks, time tracking (Toggl), Google Drive activity, Gmail subjects, and Slack messages.

Your job is to synthesize this into a prioritized daily briefing.

PRIORITIZATION RULES (in order of weight):
1. OVERDUE tasks or tasks due today -- always top priority
2. Tasks on high-dollar projects (look at custom fields or project context for $ indicators)
3. Tasks with risk signals: mentioned blockers in Slack, client emails about deadlines, \
low hours tracked vs. approaching due date
4. Tasks where someone tracked 0 hours yesterday but has upcoming deadlines
5. Everything else by due date proximity

OUTPUT FORMAT:
First, produce a TEAM SUMMARY section (3-5 bullet points of the most important things \
for today across the whole team).

Then, for EACH team member, produce a section with EXACTLY this format:

### [Person Name]
*Top 3 priorities today:*
1. [Task name] -- [why this is priority] (Due: [date])
2. [Task name] -- [why this is priority] (Due: [date])
3. [Task name] -- [why this is priority] (Due: [date])

_Context:_ [1-2 sentences noting relevant emails, Drive activity, or Slack threads \
that relate to their tasks]

_Yesterday:_ [Hours tracked] hours ([project breakdown])

Use Slack mrkdwn formatting (*bold*, _italic_). Be concise and actionable.
Do not speculate -- only reference information present in the data.
If a team member has fewer than 3 tasks, list what they have."""


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


def _collect_drive(users):
    results = {}
    for user in users:
        email = user["email"]
        try:
            files = get_recent_drive_activity(email)
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


def _collect_slack(slack_client, users):
    try:
        return get_recent_slack_messages(slack_client, users)
    except Exception as e:
        return f"[Slack data unavailable: {e}]"


def _assemble_context(asana_tasks, toggl_summary, drive_activity, gmail_data, slack_messages, users):
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
    users = build_user_map(slack_client)

    with ThreadPoolExecutor(max_workers=5) as executor:
        asana_future = executor.submit(_collect_asana)
        toggl_future = executor.submit(_collect_toggl)
        drive_future = executor.submit(_collect_drive, users)
        gmail_future = executor.submit(_collect_gmail, users)
        slack_future = executor.submit(_collect_slack, slack_client, users)

        asana_tasks = asana_future.result()
        toggl_summary = toggl_future.result()
        drive_activity = drive_future.result()
        gmail_data = gmail_future.result()
        slack_messages = slack_future.result()

    context = _assemble_context(asana_tasks, toggl_summary, drive_activity, gmail_data, slack_messages, users)

    # Add Slack @mentions instruction
    mention_map = ""
    for user in users:
        if user["slack_user_id"] and user["name"]:
            mention_map += f"  {user['name']} = <@{user['slack_user_id']}>\n"

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2000,
        system=SYNTHESIS_PROMPT,
        messages=[{
            "role": "user",
            "content": (
                f"Today's date is {date.today().isoformat()}.\n\n"
                f"When referring to team members in the output, use their Slack mention format:\n{mention_map}\n\n"
                f"{context}"
            ),
        }],
    )
    full_summary = message.content[0].text

    per_user = _parse_per_user(full_summary, users)
    set_cache(full_summary, per_user)

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
