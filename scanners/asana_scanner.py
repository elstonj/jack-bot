"""Asana deep scanner — fetches all projects and tasks, distills into knowledge files.

Produces:
  knowledge/asana/projects/{project_name}.md  — per-project knowledge
  knowledge/asana/summary.md                  — cross-project overview

Modes:
  full        — all tasks including completed (entire history)
  1yr         — tasks modified in the last year
  incremental — tasks modified since last scan
"""

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


def _get_all_tasks_for_project(project_gid, include_completed=True, modified_since=None):
    """Get all tasks for a project, with pagination.

    Args:
        project_gid: Asana project GID
        include_completed: If True, fetch completed tasks too
        modified_since: ISO date string — only tasks modified after this date
    """
    params = {
        "project": project_gid,
        "opt_fields": "name,assignee.name,assignee.email,due_on,due_at,completed,completed_at,created_at,modified_at,custom_fields,notes,tags.name,resource_subtype,num_subtasks",
    }

    if not include_completed:
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
If the project is clearly archived or inactive, note that prominently."""


def scan_project(project, mode="full", modified_since=None):
    """Scan a single Asana project and distill into a knowledge file.

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

    # Determine task fetch parameters
    include_completed = mode == "full"
    mod_since = None
    if mode == "1yr":
        mod_since = (date.today() - timedelta(days=365)).isoformat()
        include_completed = True
    elif modified_since:
        mod_since = modified_since
        include_completed = True

    # Fetch tasks
    try:
        tasks = _get_all_tasks_for_project(
            project_gid,
            include_completed=include_completed,
            modified_since=mod_since,
        )
    except Exception as e:
        print(f"  [WARN] Could not fetch tasks for {project_name}: {e}")
        return None

    if not tasks and not details.get("notes"):
        print(f"  [SKIP] {project_name}: no tasks")
        return None

    # In incremental mode, skip re-distillation if no tasks were modified
    # and a knowledge file already exists
    if modified_since and not tasks:
        filename = _safe_filename(project_name) + ".md"
        existing_path = PROJECTS_DIR / filename
        if existing_path.exists():
            print(f"  [SKIP] {project_name}: no changes since last scan")
            return None

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

    raw_text = "\n".join(lines)

    # Distill into knowledge file
    filename = _safe_filename(project_name) + ".md"
    output_path = PROJECTS_DIR / filename

    # For very small projects, just write a simple summary without Claude
    if len(tasks) <= 3 and not details.get("notes"):
        simple = f"# {project_name}\n\nSmall project with {len(tasks)} tasks.\n"
        for t in tasks:
            assignee = (t.get("assignee") or {}).get("name", "Unassigned")
            status = "Done" if t.get("completed") else "Open"
            simple += f"- [{status}] {t['name']} — {assignee}\n"
        write_knowledge_file(output_path, simple)
        return project_name, len(tasks), output_path

    print(f"  Distilling {project_name} ({len(tasks)} tasks)...")
    distill_to_markdown(raw_text, PROJECT_DISTILL_PROMPT, output_path, max_tokens=2000)
    return project_name, len(tasks), output_path


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

    results = []
    for i, project in enumerate(projects):
        if progress_callback:
            progress_callback(project["name"], i, len(projects))
        else:
            print(f"[{i+1}/{len(projects)}] {project['name']}")

        result = scan_project(project, mode=mode, modified_since=modified_since)
        if result:
            results.append(result)
        # Pace API calls (both Asana and Claude)
        time.sleep(1)

    # Generate cross-project summary
    if results:
        _generate_summary(results)

    update_scan_timestamp("asana")
    return results


def _generate_summary(results):
    """Generate a cross-project summary from all scanned projects."""
    # Read all project knowledge files and create an index
    lines = ["# Asana Projects Overview\n"]
    lines.append(f"Last scanned: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    lines.append(f"Total projects scanned: {len(results)}\n")

    lines.append("## Projects\n")
    for name, task_count, path in sorted(results, key=lambda r: r[0]):
        lines.append(f"- **{name}** — {task_count} tasks — [{path.name}]({path.name})")

    # Also generate a Claude-distilled strategic summary
    project_snippets = []
    for name, task_count, path in results:
        if path.exists():
            content = path.read_text()
            # Take first 500 chars of each project file
            project_snippets.append(f"### {name}\n{content[:500]}")

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
