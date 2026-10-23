"""Asana deep scanner — fetches all projects and tasks, distills into knowledge files.

Produces:
  knowledge/asana/projects/{project_name}.md  — per-project knowledge
  knowledge/asana/summary.md                  — cross-project overview

Modes:
  full        — rebuild every project: open tasks + all completed tasks
  1yr         — rebuild every project: open tasks + tasks completed in the last year
  incremental — rebuild only projects with a task modified since the last scan

Every write is a complete snapshot (open tasks plus recently completed ones),
never just the tasks that changed. Incremental mode uses `modified_since` only
to decide *whether* to rebuild a project. It used to distill the changed tasks
alone, so a project where one task moved was overwritten as a one-task project
and the full task list was gone until the next full scan.
"""

import json
import os
import re
import time
import requests
from datetime import date, datetime, timedelta

from .base import (
    KNOWLEDGE_DIR,
    distill_to_markdown,
    get_last_scan,
    time_range_for_mode,
    update_scan_timestamp,
    write_knowledge_file,
    get_claude_client,
    DISTILL_MODEL,
)

ASANA_BASE = "https://app.asana.com/api/1.0"
ASANA_KNOWLEDGE_DIR = KNOWLEDGE_DIR / "asana"
PROJECTS_DIR = ASANA_KNOWLEDGE_DIR / "projects"
# Per-project counts and as-of dates, so summary.md covers every project and
# not just the ones rebuilt this run.
INDEX_FILE = ASANA_KNOWLEDGE_DIR / ".index.json"

# How far back an incremental snapshot keeps completed tasks.
SNAPSHOT_COMPLETED_DAYS = 90

# Rate limit: Asana allows ~150 requests/minute. Be conservative.
REQUEST_DELAY = 0.4  # seconds between requests


def _headers():
    return {"Authorization": f"Bearer {os.environ['ASANA_ACCESS_TOKEN']}"}


def _get_paginated(url, params=None, delay=REQUEST_DELAY):
    """Fetch all pages from an Asana endpoint."""
    if params is None:
        params = {}
    params.setdefault("limit", 100)

    all_data = []
    offset = None

    while True:
        if offset:
            params["offset"] = offset
        elif "offset" in params:
            del params["offset"]

        resp = requests.get(url, headers=_headers(), params=params, timeout=30)
        resp.raise_for_status()
        body = resp.json()

        all_data.extend(body.get("data", []))

        next_page = body.get("next_page")
        if next_page and next_page.get("offset"):
            offset = next_page["offset"]
            time.sleep(delay)
        else:
            break

    return all_data


def _get_project_details(project_gid):
    """Get full project metadata."""
    resp = requests.get(
        f"{ASANA_BASE}/projects/{project_gid}",
        headers=_headers(),
        params={"opt_fields": "name,notes,status,current_status,due_on,start_on,owner.name,team.name,created_at,modified_at,archived,public,custom_fields"},
        timeout=15,
    )
    resp.raise_for_status()
    return resp.json()["data"]


def _get_all_tasks_for_project(project_gid, include_completed=True, modified_since=None,
                               completed_since=None):
    """Get all tasks for a project, with pagination.

    Args:
        project_gid: Asana project GID
        include_completed: If True, fetch completed tasks too
        modified_since: ISO date string — only tasks modified after this date
        completed_since: ISO date string — incomplete tasks plus tasks
            completed after this date (overrides include_completed)
    """
    params = {
        "project": project_gid,
        "opt_fields": "name,assignee.name,assignee.email,due_on,due_at,completed,completed_at,created_at,modified_at,custom_fields,notes,tags.name,resource_subtype,num_subtasks",
    }

    if completed_since:
        params["completed_since"] = completed_since
    elif not include_completed:
        params["completed_since"] = "now"

    if modified_since:
        params["modified_since"] = modified_since

    tasks = _get_paginated(f"{ASANA_BASE}/tasks", params)
    time.sleep(REQUEST_DELAY)
    return tasks


def _get_subtasks(task_gid):
    """Get subtasks for a task."""
    try:
        return _get_paginated(
            f"{ASANA_BASE}/tasks/{task_gid}/subtasks",
            {"opt_fields": "name,assignee.name,due_on,completed,custom_fields,notes"},
        )
    except Exception:
        return []


def _format_task(task, indent=0):
    """Format a single task as text for distillation."""
    prefix = "  " * indent
    assignee = (task.get("assignee") or {}).get("name", "Unassigned")
    status = "DONE" if task.get("completed") else "OPEN"
    due = task.get("due_on") or "no due date"
    completed_at = task.get("completed_at", "")
    subtype = task.get("resource_subtype", "")
    marker = " [MILESTONE]" if subtype == "milestone" else ""

    custom_fields = ""
    for cf in task.get("custom_fields", []) or []:
        if cf and cf.get("display_value"):
            custom_fields += f" [{cf.get('name', '')}: {cf['display_value']}]"

    notes = (task.get("notes") or "").strip()
    notes_snippet = ""
    if notes:
        notes_snippet = f"\n{prefix}  Notes: {notes[:200]}"

    completed_info = ""
    if completed_at:
        completed_info = f" (completed {completed_at[:10]})"

    return f"{prefix}- [{status}]{marker} {task['name']} | {assignee} | Due: {due}{completed_info}{custom_fields}{notes_snippet}"


def _safe_filename(name):
    """Convert a project name to a safe filename."""
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'\s+', '_', name.strip())
    return name[:80].lower()


PROJECT_DISTILL_PROMPT = """\
You are distilling raw Asana project data into a structured knowledge file for Black Swift Technologies (BST).

This file will be used by an AI assistant to understand project context, make prioritization decisions, \
and answer questions about the project. It should be comprehensive but concise.

Output a markdown file with these sections:

# {Project Name}

## Overview
- Client/customer (if apparent from task names, notes, or custom fields)
- Dollar value (from custom fields, milestone subtasks, or task names)
- Timeline (start date, due date, key dates)
- Status (active, completed, on-hold — infer from task completion rates)
- Team members involved (from assignees)
- Risk signals (overdue tasks, approaching deadlines with incomplete work)

## Key Deliverables & Milestones
List major milestones and deliverables with dates and dollar amounts.

## Task Summary
- Total tasks (open vs completed)
- Tasks by assignee with completion rates
- Notable patterns (e.g. "most tasks assigned to X", "heavy custom field usage for tracking $")

## Recent Activity
What's been happening lately — recently completed tasks, approaching deadlines.

## Notes & Context
Any important context from task notes, custom fields, or patterns.

Be factual. Include dollar amounts, dates, and names. Skip empty sections. \
If the project is clearly archived or inactive, note that prominently.

TEAM CORRECTIONS ARE AUTHORITATIVE:
If the raw data includes a `TEAM CORRECTIONS & FEEDBACK` block, those messages from \
team members OVERRIDE the Asana task list. Asana often has stale due dates or tasks \
that were not closed out after a real-world change. If a correction says a project is \
delayed, complete, cancelled, or handled externally, reflect that in the Status line \
and Recent Activity — do not describe stale Asana dates as current truth. Quote the \
correction author and date when you override Asana data."""


def _fetch_recent_corrections(days=30):
    """Pull recent CORRECTION/FEEDBACK entries from the Slack knowledge channel.

    Returns a list of dicts: [{"author": str, "content": str, "date": str, "type": str}].
    Returns [] if no Slack token or channel configured.
    """
    channel = os.environ.get("KNOWLEDGE_CHANNEL", "")
    token = os.environ.get("SLACK_BOT_TOKEN", "")
    if not channel or not token:
        return []

    try:
        from slack_sdk import WebClient
    except Exception:
        return []

    try:
        client = WebClient(token=token)
        oldest = str(time.time() - (days * 86400))
        entries = []
        cursor = None
        while True:
            kwargs = {"channel": channel, "limit": 200, "oldest": oldest}
            if cursor:
                kwargs["cursor"] = cursor
            result = client.conversations_history(**kwargs)
            for msg in result.get("messages", []):
                text = msg.get("text", "")
                for tag in ("CORRECTION", "FEEDBACK"):
                    if text.startswith(f"*[{tag}]*"):
                        body = text.replace(f"*[{tag}]*\n", "", 1)
                        ts = msg.get("ts", "")
                        try:
                            msg_date = datetime.fromtimestamp(float(ts)).strftime("%Y-%m-%d")
                        except Exception:
                            msg_date = ""
                        entries.append({
                            "type": tag,
                            "content": body,
                            "date": msg_date,
                        })
                        break
            cursor = result.get("response_metadata", {}).get("next_cursor")
            if not cursor:
                break
        return entries
    except Exception as e:
        print(f"  [WARN] Could not fetch corrections from Slack: {e}")
        return []


def _project_keywords(project_name):
    """Extract searchable keywords from a project name.

    Returns lowercase tokens: project code (e.g., '350-4', '350_4'), and
    significant name tokens (>=4 chars, non-generic).
    """
    name = project_name.lower()
    keywords = set()

    code_match = re.search(r"\[?(\d{3}[-_]\d+)\]?", name)
    if code_match:
        code = code_match.group(1)
        keywords.add(code)
        keywords.add(code.replace("-", "_"))
        keywords.add(code.replace("_", "-"))

    stopwords = {
        "the", "and", "for", "with", "from", "project", "irad", "phase",
        "view", "fleet", "maintenance", "general", "operations", "support",
        "pipeline", "pipeline.", "part", "new", "old",
    }
    cleaned = re.sub(r"[\[\]\(\)\-_,]", " ", name)
    for token in cleaned.split():
        token = token.strip(".")
        if len(token) >= 4 and token not in stopwords and not token.isdigit():
            keywords.add(token)

    return keywords


def _corrections_for_project(project_name, all_corrections):
    """Return corrections whose text mentions this project by code or name tokens."""
    keywords = _project_keywords(project_name)
    if not keywords:
        return []
    matched = []
    for entry in all_corrections:
        content_lower = entry["content"].lower()
        if any(kw in content_lower for kw in keywords):
            matched.append(entry)
    return matched


def _format_corrections_block(corrections):
    """Format matched corrections as a prepended block for the distillation prompt."""
    if not corrections:
        return ""
    lines = [
        "",
        "=== TEAM CORRECTIONS & FEEDBACK (authoritative — override Asana if conflicting) ===",
    ]
    for entry in corrections:
        date_str = f" [{entry['date']}]" if entry.get("date") else ""
        lines.append(f"[{entry['type']}]{date_str} {entry['content'][:500]}")
    lines.append("=== END CORRECTIONS ===")
    return "\n".join(lines)


def scan_project(project, mode="full", modified_since=None, corrections=None):
    """Scan a single Asana project and distill into a knowledge file.

    Args:
        project: Asana project dict
        mode: scan mode
        modified_since: ISO date for incremental filter
        corrections: list of recent CORRECTION/FEEDBACK entries already keyword-
            filtered to this project. Injected into the distillation raw text.

    Returns (project_name, task_count, output_path) or None on skip.
    """
    project_gid = project["gid"]
    project_name = project["name"]

    # Get full project details
    try:
        details = _get_project_details(project_gid)
    except Exception as e:
        print(f"  [WARN] Could not get details for {project_name}: {e}")
        details = project

    filename = _safe_filename(project_name) + ".md"
    output_path = PROJECTS_DIR / filename

    # Incremental: modified_since only answers "did anything change?". Skip
    # when nothing did and there are no team corrections; corrections can
    # override stale Asana state ("delayed to fall"), so they force a rebuild.
    if mode == "incremental" and modified_since and output_path.exists():
        try:
            changed = _get_all_tasks_for_project(
                project_gid, include_completed=True, modified_since=modified_since,
            )
        except Exception as e:
            print(f"  [WARN] Could not fetch tasks for {project_name}: {e}")
            return None
        if not changed and not corrections:
            print(f"  [SKIP] {project_name}: no changes since last scan")
            return None

    # Always distill from a complete snapshot of the project.
    if mode == "full":
        completed_since, window = None, "all time"
    else:
        days = 365 if mode == "1yr" else SNAPSHOT_COMPLETED_DAYS
        completed_since = (date.today() - timedelta(days=days)).isoformat()
        window = f"last {days} days"
    try:
        tasks = _get_all_tasks_for_project(
            project_gid, include_completed=True, completed_since=completed_since,
        )
    except Exception as e:
        print(f"  [WARN] Could not fetch tasks for {project_name}: {e}")
        return None

    if not tasks and not details.get("notes"):
        # Overwrite rather than skip: a skipped project kept its old file, so
        # one with nothing open still listed tasks from a previous snapshot.
        print(f"  [EMPTY] {project_name}: no open or recently completed tasks")
        as_of = date.today().isoformat()
        write_knowledge_file(output_path, (
            f"# {project_name}\n\n_Asana snapshot as of {as_of}: 0 open tasks, "
            f"0 completed ({window})._\n\nNo open tasks and none completed in this window.\n"))
        _update_index(filename, project_name, 0, 0, window, as_of)
        return project_name, 0, output_path

    # Fetch subtasks for milestones (they often have dollar amounts)
    milestones = [t for t in tasks if t.get("resource_subtype") == "milestone"]
    for m in milestones[:20]:  # cap subtask fetches
        m["subtasks"] = _get_subtasks(m["gid"])
        time.sleep(REQUEST_DELAY)

    # Build raw text for distillation
    lines = [f"PROJECT: {project_name}"]
    if details.get("notes"):
        lines.append(f"Project Notes: {details['notes'][:500]}")
    if details.get("due_on"):
        lines.append(f"Project Due: {details['due_on']}")
    if details.get("start_on"):
        lines.append(f"Project Start: {details['start_on']}")
    if details.get("owner"):
        lines.append(f"Owner: {details['owner'].get('name', 'Unknown')}")
    if details.get("team"):
        lines.append(f"Team: {details['team'].get('name', 'Unknown')}")
    if details.get("archived"):
        lines.append("STATUS: ARCHIVED")
    if details.get("current_status"):
        cs = details["current_status"]
        lines.append(f"Status Update: [{cs.get('color', '')}] {cs.get('title', '')} — {cs.get('text', '')[:200]}")

    # Custom fields on the project
    for cf in details.get("custom_fields", []) or []:
        if cf and cf.get("display_value"):
            lines.append(f"Custom Field: {cf.get('name', '')}: {cf['display_value']}")

    open_tasks = [t for t in tasks if not t.get("completed")]
    done_tasks = [t for t in tasks if t.get("completed")]
    lines.append(f"\nTASKS: {len(open_tasks)} open, {len(done_tasks)} completed")

    if open_tasks:
        lines.append("\n--- OPEN TASKS ---")
        for t in open_tasks:
            lines.append(_format_task(t))
            if t.get("subtasks"):
                for st in t["subtasks"]:
                    lines.append(_format_task(st, indent=1))

    if done_tasks:
        lines.append(f"\n--- COMPLETED TASKS ({len(done_tasks)} total, showing recent) ---")
        # Sort by completed_at descending, show top 50
        done_sorted = sorted(done_tasks, key=lambda t: t.get("completed_at", ""), reverse=True)
        for t in done_sorted[:50]:
            lines.append(_format_task(t))
            if t.get("subtasks"):
                for st in t["subtasks"]:
                    lines.append(_format_task(st, indent=1))
        if len(done_tasks) > 50:
            lines.append(f"  ... and {len(done_tasks) - 50} more completed tasks")

    # Prepend team corrections so the distillation treats them as authoritative
    # over any stale Asana state (past-due dates, unclosed tasks, etc.)
    corrections_block = _format_corrections_block(corrections or [])
    if corrections_block:
        lines.insert(0, corrections_block)

    raw_text = "\n".join(lines)

    # Stamped by code, not the model, so readers can tell how current it is.
    as_of = date.today().isoformat()
    stamp = (f"_Asana snapshot as of {as_of}: {len(open_tasks)} open tasks, "
             f"{len(done_tasks)} completed ({window})._\n\n")

    # For very small projects, just write a simple summary without Claude
    if len(tasks) <= 3 and not details.get("notes"):
        simple = f"# {project_name}\n\n{stamp}"
        for t in tasks:
            assignee = (t.get("assignee") or {}).get("name", "Unassigned")
            status = "Done" if t.get("completed") else "Open"
            simple += f"- [{status}] {t['name']} — {assignee}\n"
        write_knowledge_file(output_path, simple)
    else:
        print(f"  Distilling {project_name} ({len(tasks)} tasks)...")
        content = distill_to_markdown(raw_text, PROJECT_DISTILL_PROMPT, output_path,
                                      max_tokens=2000, merge=False)
        if content is None:
            return None
        write_knowledge_file(output_path, stamp + content)

    _update_index(filename, project_name, len(open_tasks), len(done_tasks), window, as_of)
    return project_name, len(tasks), output_path


ORPHAN_BANNER = "_Not in Asana's current project list"


def _mark_orphans(current_filenames):
    """Banner project files whose project is gone (renamed or archived).

    Kept rather than deleted so archived projects stay answerable, but marked
    so nobody reads e.g. the pre-rename 001-02 file as today's task list.
    """
    today = date.today().isoformat()
    for path in PROJECTS_DIR.glob("*.md"):
        if path.name in current_filenames:
            continue
        text = path.read_text()
        if ORPHAN_BANNER not in text:
            write_knowledge_file(path, (
                f"{ORPHAN_BANNER} as of {today} (renamed or archived); this file "
                f"is not updated and may be stale._\n\n{text}"))


def _load_index():
    try:
        return json.loads(INDEX_FILE.read_text())
    except (FileNotFoundError, ValueError):
        return {}


def _update_index(filename, name, open_count, done_count, window, as_of):
    index = _load_index()
    index[filename] = {"name": name, "open": open_count, "completed": done_count,
                       "window": window, "as_of": as_of}
    INDEX_FILE.parent.mkdir(parents=True, exist_ok=True)
    INDEX_FILE.write_text(json.dumps(index, indent=2, sort_keys=True))


def scan_all(mode="full", progress_callback=None):
    """Scan all Asana projects.

    Args:
        mode: 'full', '1yr', or 'incremental'
        progress_callback: optional fn(project_name, index, total) called per project

    Returns:
        list of (project_name, task_count, output_path) tuples
    """
    from asana_client import get_workspaces, get_projects

    workspaces = get_workspaces()
    if not workspaces:
        print("[ERROR] No Asana workspaces found")
        return []

    workspace_gid = workspaces[0]["gid"]
    projects = get_projects(workspace_gid)
    print(f"Found {len(projects)} Asana projects")

    modified_since = None
    if mode == "incremental":
        last = get_last_scan("asana")
        if last:
            modified_since = last.isoformat()
            print(f"Incremental mode: scanning changes since {modified_since}")
        else:
            print("No previous scan found — falling back to full scan")
            mode = "full"

    # Pull recent team corrections once, then filter per-project by keyword
    all_corrections = _fetch_recent_corrections(days=30)
    if all_corrections:
        print(f"Loaded {len(all_corrections)} recent correction/feedback entries for distillation")

    results = []
    for i, project in enumerate(projects):
        if progress_callback:
            progress_callback(project["name"], i, len(projects))
        else:
            print(f"[{i+1}/{len(projects)}] {project['name']}")

        project_corrections = _corrections_for_project(project["name"], all_corrections)
        result = scan_project(
            project,
            mode=mode,
            modified_since=modified_since,
            corrections=project_corrections,
        )
        if result:
            results.append(result)
        # Pace API calls (both Asana and Claude)
        time.sleep(1)

    _mark_orphans({_safe_filename(p["name"]) + ".md" for p in projects})

    # Generate cross-project summary. Rebuilt whenever anything changed, and
    # always from every project on disk, not just this run's results.
    if results:
        _generate_summary()

    update_scan_timestamp("asana")
    return results


def _generate_summary():
    """Generate a cross-project summary covering every project file."""
    index = _load_index()
    paths = sorted(PROJECTS_DIR.glob("*.md"))

    lines = ["# Asana Projects Overview\n"]
    lines.append(f"Last scanned: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    lines.append(f"Total projects: {len(paths)}\n")

    lines.append("## Projects\n")
    for path in paths:
        entry = index.get(path.name)
        if entry:
            lines.append(
                f"- **{entry['name']}** — {entry['open']} open, {entry['completed']} "
                f"completed ({entry['window']}) as of {entry['as_of']} — [{path.name}]({path.name})"
            )
        else:
            lines.append(f"- [{path.name}]({path.name}) — not rebuilt since snapshot scanning began")

    # Also generate a Claude-distilled strategic summary
    project_snippets = []
    for path in paths:
        name = index.get(path.name, {}).get("name", path.stem)
        # Take first 500 chars of each project file
        project_snippets.append(f"### {name}\n{path.read_text()[:500]}")

    if project_snippets:
        combined = "\n\n".join(project_snippets)
        # Truncate if too large
        if len(combined) > 90000:
            combined = combined[:90000] + "\n\n[TRUNCATED]"
        client = get_claude_client()
        for attempt in range(5):
            try:
                message = client.messages.create(
                    model=DISTILL_MODEL,
                    max_tokens=2000,
                    system=(
                        "You are creating a strategic overview of all projects for Black Swift Technologies (BST). "
                        "Summarize the project portfolio: total value, key active projects, risk areas, "
                        "team allocation patterns, upcoming deadlines. Be concise and factual. "
                        "Output markdown."
                    ),
                    messages=[{"role": "user", "content": f"Project summaries:\n\n{combined}"}],
                )
                lines.append(f"\n## Strategic Summary\n\n{message.content[0].text}")
                break
            except Exception as e:
                if "rate_limit" in str(e).lower():
                    wait = 30 * (attempt + 1)
                    print(f"  Rate limited on summary, waiting {wait}s...")
                    time.sleep(wait)
                else:
                    print(f"  [WARN] Summary generation failed: {e}")
                    break

    summary_path = ASANA_KNOWLEDGE_DIR / "summary.md"
    write_knowledge_file(summary_path, "\n".join(lines))
    print(f"Summary written to {summary_path}")
