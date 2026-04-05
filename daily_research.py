import os
import re
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import anthropic

from user_map import build_user_map, get_all_users, get_user_by_email
from asana_client import get_enriched_tasks, get_key_project_data, get_workspaces
from toggl_client import get_time_summary
from google_client import get_recent_drive_activity, get_recent_emails, get_todays_calendar, get_contacts, get_meeting_notes_content
from slack_data_client import get_recent_slack_messages
from research_cache import set_cache
from knowledge import get_knowledge_summary, auto_extract_knowledge, store_daily_snapshot, store_entry, get_knowledge

KNOWLEDGE_DIR = Path(__file__).parent / "knowledge"

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
First, produce a team summary with header `:mega: *TEAM SUMMARY*` followed by \
3-5 bullet points of the most critical items for today.

Then produce a section for EACH team member. Use their Slack mention (e.g. <@U12345>) as the \
section header — NOT their plain name. Format:

*<@SLACK_ID>*
1. [Task] — [reason] (Due: [date])
2. [Task] — [reason] (Due: [date])
3. [Task] — [reason] (Due: [date])
:calendar: [meetings] · :clock1: [hours] or :warning: *No time tracked*

Rules:
- Each person MAX 5 lines
- Simple numbered list
- If 0 hours tracked: :warning: *No time tracked*
- Be terse

YOU MUST PRODUCE A SECTION FOR EVERY SINGLE PERSON IN THE REQUIRED LIST BELOW. \
There will be approximately 12 people. If you have produced fewer than 12 sections, \
you are not done. Keep going until every required person has a section."""


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
        from collections import defaultdict
        per_person = defaultdict(list)
        for t in assigned:
            name = t.get("assignee_name")
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
    # Split on any line that contains a Slack mention as a header
    # Matches: *<@U12345>*, ### <@U12345>, --- @Name, ### Name
    parts = re.split(r"(?=^\*?<@[A-Z0-9]+>\*?$|^---\s*@|^### )", full_summary, flags=re.MULTILINE)
    for part in parts:
        part = part.strip()
        if not part:
            continue
        # Try to find a Slack mention anywhere in the first line
        first_line = part.split("\n")[0]
        mention_match = re.search(r"<@([A-Z0-9]+)>", first_line)
        if mention_match:
            slack_id = mention_match.group(1)
            per_user[slack_id] = part
            continue

        # Fallback: match --- @Name or ### Name
        match = re.match(r"^(?:---\s*@|### )(.+)", first_line)
        if match:
            header = match.group(1).strip()
            for user in users:
                if user["name"] and user["slack_user_id"]:
                    if user["name"].lower() in header.lower():
                        per_user[user["slack_user_id"]] = part
                        break
    return per_user


def _has_knowledge_files():
    """Check whether pre-distilled knowledge files are available."""
    # Require at least the contacts directory and toggl summary to consider
    # knowledge files usable.  asana/summary.md may not exist yet.
    return (
        (KNOWLEDGE_DIR / "contacts" / "directory.md").exists()
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
                # Try a few filename patterns
                candidates = [
                    name.lower().replace(" ", "_") + ".md",
                    name.split()[0].lower() + ".md" if " " in name else None,
                ]
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

    # --- Team directory ---
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
            debug_lines.append(f"  {u['name']} | email: {u['email']} | slack: {u['slack_user_id']} | asana: {u['asana_user_gid']} | toggl: {u['toggl_user_id']}")
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

    context = _assemble_context(
        asana_tasks, toggl_summary, drive_activity, gmail_data, calendar_data,
        contacts, slack_messages, users,
        key_projects=key_projects, meeting_notes=meeting_notes,
        operations_history=operations_history,
    )

    # Build set of known user names (from user map) for filtering
    known_names = {u["name"].lower() for u in users if u["name"]}

    # Build list of active team members (those with Asana tasks AND in user map)
    assignees_in_asana = set()
    if isinstance(asana_tasks, list):
        for t in asana_tasks:
            name = t.get("assignee_name", "")
            if name and name != "Unassigned" and name.lower() in known_names:
                assignees_in_asana.add(name)

    mention_map = ""
    active_list = ""
    for user in users:
        if user["slack_user_id"] and user["name"]:
            mention_map += f"  {user['name']} = <@{user['slack_user_id']}>\n"
    for name in sorted(assignees_in_asana):
        active_list += f"  - {name}\n"

    # Combine: distilled knowledge + Slack knowledge channel + live data
    full_context = context
    if distilled_context:
        full_context = f"{distilled_context}\n\n{full_context}"
    if knowledge_context:
        full_context = f"{knowledge_context}\n\n{full_context}"

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=8000,
        system=SYNTHESIS_PROMPT,
        messages=[{
            "role": "user",
            "content": (
                f"Today's date is {date.today().isoformat()}.\n\n"
                f"Slack mention mapping:\n{mention_map}\n\n"
                f"{full_context}\n\n"
                f"===== IMPORTANT =====\n"
                f"You MUST produce a section for ALL {len(assignees_in_asana)} of these people:\n{active_list}\n"
                f"That means {len(assignees_in_asana)} sections total. Do not stop until all are done."
            ),
        }],
    )
    full_summary = message.content[0].text

    per_user = _parse_per_user(full_summary, users)

    # Extract team summary (everything before the first ### section)
    team_summary = re.split(r"(?=^\*?<@[A-Z0-9]+>\*?$|^---\s*@|^### )", full_summary, maxsplit=1, flags=re.MULTILINE)
    team_summary_text = team_summary[0].strip() if team_summary else full_summary

    set_cache(full_summary, per_user, team_summary_text)

    # Debug: log what was parsed
    try:
        parse_debug = [f"Parsed {len(per_user)} user sections from summary"]
        for sid, section in per_user.items():
            first_line = section.split("\n")[0][:80]
            parse_debug.append(f"  {sid}: {first_line}")
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
