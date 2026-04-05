"""Toggl deep scanner — fetches time entry data, distills into knowledge files.

Produces:
  knowledge/toggl/summary.md                    — overall time tracking overview
  knowledge/toggl/by_person/{name}.md           — per-person time allocation history
  knowledge/toggl/by_project/{project_name}.md  — per-project time history

Modes:
  full        — all data from 2020-01-01 to now (chunked by month)
  1yr         — last 365 days (chunked by month)
  incremental — since last scan timestamp
"""

import os
import re
import time
import base64
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

TOGGL_BASE = "https://api.track.toggl.com"
TOGGL_KNOWLEDGE_DIR = KNOWLEDGE_DIR / "toggl"
BY_PERSON_DIR = TOGGL_KNOWLEDGE_DIR / "by_person"
BY_PROJECT_DIR = TOGGL_KNOWLEDGE_DIR / "by_project"

# Toggl allows ~1 request/sec
REQUEST_DELAY = 1.0


def _headers():
    token = os.environ.get("TOGGL_API_TOKEN", "")
    encoded = base64.b64encode(f"{token}:api_token".encode()).decode()
    return {"Authorization": f"Basic {encoded}", "Content-Type": "application/json"}


def _workspace_id():
    return os.environ.get("TOGGL_WORKSPACE_ID", "")


def _safe_filename(name):
    """Convert a name to a safe filename."""
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'\s+', '_', name.strip())
    return name[:80].lower()


# ---------------------------------------------------------------------------
# API helpers
# ---------------------------------------------------------------------------


def _fetch_users():
    """Fetch all workspace users. Returns {user_id: {name, email}}."""
    wid = _workspace_id()
    resp = requests.get(
        f"{TOGGL_BASE}/api/v9/workspaces/{wid}/users",
        headers=_headers(),
        timeout=15,
    )
    resp.raise_for_status()
    users = {}
    for u in resp.json():
        users[u["id"]] = {
            "name": u.get("fullname") or u.get("name") or u.get("email", "Unknown"),
            "email": u.get("email", ""),
        }
    return users


def _fetch_projects():
    """Fetch all workspace projects. Returns {project_id: {name, client, active, ...}}."""
    wid = _workspace_id()
    resp = requests.get(
        f"{TOGGL_BASE}/api/v9/workspaces/{wid}/projects",
        headers=_headers(),
        params={"active": "both"},
        timeout=15,
    )
    resp.raise_for_status()
    projects = {}
    for p in resp.json():
        projects[p["id"]] = {
            "name": p.get("name", "Unknown"),
            "active": p.get("active", True),
            "client_id": p.get("client_id"),
            "color": p.get("color", ""),
            "billable": p.get("billable"),
        }
    return projects


def _fetch_clients():
    """Fetch all workspace clients. Returns {client_id: name}."""
    wid = _workspace_id()
    resp = requests.get(
        f"{TOGGL_BASE}/api/v9/workspaces/{wid}/clients",
        headers=_headers(),
        timeout=15,
    )
    resp.raise_for_status()
    return {c["id"]: c.get("name", "Unknown") for c in resp.json()}


def _month_chunks(start_date, end_date):
    """Generate (chunk_start, chunk_end) date pairs, one month each."""
    chunks = []
    current = start_date
    while current < end_date:
        # End of this chunk: start of next month or end_date, whichever is sooner
        if current.month == 12:
            next_month = date(current.year + 1, 1, 1)
        else:
            next_month = date(current.year, current.month + 1, 1)
        chunk_end = min(next_month, end_date)
        chunks.append((current, chunk_end))
        current = next_month
    return chunks


def _fetch_summary_chunk(start_str, end_str):
    """Fetch summary time entries for a date range.

    Uses POST /reports/api/v3/workspace/{wid}/summary/time_entries
    grouped by users, sub-grouped by projects.
    """
    wid = _workspace_id()
    resp = requests.post(
        f"{TOGGL_BASE}/reports/api/v3/workspace/{wid}/summary/time_entries",
        headers=_headers(),
        json={
            "start_date": start_str,
            "end_date": end_str,
            "grouping": "users",
            "sub_grouping": "projects",
        },
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def _fetch_detailed_chunk(start_str, end_str):
    """Fetch detailed time entries for a date range.

    Uses POST /reports/api/v3/workspace/{wid}/search/time_entries
    which returns individual entries with descriptions, tags, etc.
    Handles pagination via the returned row_number.
    """
    wid = _workspace_id()
    all_entries = []
    first_row = None

    while True:
        body = {
            "start_date": start_str,
            "end_date": end_str,
        }
        if first_row is not None:
            body["first_row_number"] = first_row

        resp = requests.post(
            f"{TOGGL_BASE}/reports/api/v3/workspace/{wid}/search/time_entries",
            headers=_headers(),
            json=body,
            timeout=30,
        )
        resp.raise_for_status()
        entries = resp.json()

        if not entries:
            break

        all_entries.extend(entries)

        # Toggl search endpoint returns up to 50 entries per page.
        # If we got fewer than 50, we're done.
        if len(entries) < 50:
            break

        # Next page starts after last row_number
        last_entry = entries[-1]
        if "row_number" in last_entry:
            first_row = last_entry["row_number"] + 1
        else:
            break

        time.sleep(REQUEST_DELAY)

    return all_entries


# ---------------------------------------------------------------------------
# Data collection
# ---------------------------------------------------------------------------


def _collect_all_data(start_date, end_date, progress_callback=None):
    """Collect all Toggl data for the given date range.

    Returns:
        dict with keys: users, projects, clients, summary_by_user, detailed_entries
    """
    print("Fetching Toggl users, projects, and clients...")
    users = _fetch_users()
    time.sleep(REQUEST_DELAY)
    projects = _fetch_projects()
    time.sleep(REQUEST_DELAY)
    clients = _fetch_clients()
    time.sleep(REQUEST_DELAY)

    print(f"  Found {len(users)} users, {len(projects)} projects, {len(clients)} clients")

    # Attach client names to projects
    for pid, pdata in projects.items():
        cid = pdata.get("client_id")
        pdata["client_name"] = clients.get(cid, "") if cid else ""

    # Fetch summary data in monthly chunks
    chunks = _month_chunks(start_date, end_date)
    print(f"Fetching time data from {start_date} to {end_date} ({len(chunks)} month chunks)...")

    # Accumulate summary per user per project: {user_id: {project_id: total_seconds}}
    summary_by_user = {}
    all_detailed = []

    for i, (chunk_start, chunk_end) in enumerate(chunks):
        label = chunk_start.strftime("%Y-%m")
        if progress_callback:
            progress_callback(f"Toggl {label}", i, len(chunks))
        else:
            print(f"  [{i+1}/{len(chunks)}] {label}")

        # Fetch summary
        try:
            summary_data = _fetch_summary_chunk(chunk_start.isoformat(), chunk_end.isoformat())
            for group in summary_data.get("groups", []):
                user_id = group.get("id")
                if user_id not in summary_by_user:
                    summary_by_user[user_id] = {}
                for sub in group.get("sub_groups", []):
                    proj_id = sub.get("id")
                    seconds = sub.get("seconds", 0)
                    summary_by_user[user_id][proj_id] = (
                        summary_by_user[user_id].get(proj_id, 0) + seconds
                    )
        except Exception as e:
            print(f"    [WARN] Summary fetch failed for {label}: {e}")

        time.sleep(REQUEST_DELAY)

        # Fetch detailed entries
        try:
            detailed = _fetch_detailed_chunk(chunk_start.isoformat(), chunk_end.isoformat())
            all_detailed.extend(detailed)
        except Exception as e:
            print(f"    [WARN] Detailed fetch failed for {label}: {e}")

        time.sleep(REQUEST_DELAY)

    print(f"  Collected {len(all_detailed)} detailed time entries")

    return {
        "users": users,
        "projects": projects,
        "clients": clients,
        "summary_by_user": summary_by_user,
        "detailed_entries": all_detailed,
    }


# ---------------------------------------------------------------------------
# Formatting helpers
# ---------------------------------------------------------------------------


def _format_person_data(user_id, user_info, summary_by_user, detailed_entries, projects):
    """Format all time data for one person as raw text for distillation."""
    name = user_info["name"]
    email = user_info["email"]
    lines = [f"PERSON: {name} ({email})\n"]

    # Summary by project
    user_projects = summary_by_user.get(user_id, {})
    total_seconds = sum(user_projects.values())
    lines.append(f"Tracked time in this data batch: {total_seconds / 3600:.1f} hours\n")

    if user_projects:
        lines.append("TIME BY PROJECT:")
        sorted_projects = sorted(user_projects.items(), key=lambda x: x[1], reverse=True)
        for proj_id, seconds in sorted_projects:
            proj_name = projects.get(proj_id, {}).get("name", f"Project {proj_id}")
            client = projects.get(proj_id, {}).get("client_name", "")
            client_str = f" (client: {client})" if client else ""
            hours = seconds / 3600
            lines.append(f"  - {proj_name}{client_str}: {hours:.1f} hours")

    # Detailed entries for this user (recent ones for context)
    user_entries = [e for e in detailed_entries if e.get("user_id") == user_id]
    if user_entries:
        # Sort by start time descending
        user_entries.sort(key=lambda e: e.get("start", ""), reverse=True)
        lines.append(f"\nRECENT ENTRIES ({min(len(user_entries), 100)} of {len(user_entries)}):")
        for entry in user_entries[:100]:
            desc = entry.get("description", "").strip() or "(no description)"
            proj_id = entry.get("project_id")
            proj_name = projects.get(proj_id, {}).get("name", "No project") if proj_id else "No project"
            seconds = entry.get("time_entries", [{}])[0].get("seconds", 0) if entry.get("time_entries") else 0
            start = entry.get("start", "")[:10]
            tags = ", ".join(entry.get("tag_ids", []) or []) if entry.get("tag_ids") else ""
            tag_str = f" [tags: {tags}]" if tags else ""
            lines.append(f"  - {start} | {proj_name} | {seconds / 3600:.1f}h | {desc}{tag_str}")

    return "\n".join(lines)


def _format_project_data(proj_id, proj_info, summary_by_user, detailed_entries, users):
    """Format all time data for one project as raw text for distillation."""
    name = proj_info["name"]
    client = proj_info.get("client_name", "")
    active = proj_info.get("active", True)
    billable = proj_info.get("billable")

    lines = [f"PROJECT: {name}"]
    if client:
        lines.append(f"Client: {client}")
    lines.append(f"Active: {'Yes' if active else 'No'}")
    if billable is not None:
        lines.append(f"Billable: {'Yes' if billable else 'No'}")
    lines.append("")

    # Aggregate hours by user for this project
    user_hours = {}
    total_seconds = 0
    for user_id, proj_map in summary_by_user.items():
        seconds = proj_map.get(proj_id, 0)
        if seconds > 0:
            user_name = users.get(user_id, {}).get("name", f"User {user_id}")
            user_hours[user_name] = seconds / 3600
            total_seconds += seconds

    lines.append(f"Tracked time in this data batch: {total_seconds / 3600:.1f} hours\n")

    if user_hours:
        lines.append("TIME BY TEAM MEMBER:")
        for uname, hours in sorted(user_hours.items(), key=lambda x: x[1], reverse=True):
            lines.append(f"  - {uname}: {hours:.1f} hours")

    # Detailed entries for this project
    proj_entries = [e for e in detailed_entries if e.get("project_id") == proj_id]
    if proj_entries:
        proj_entries.sort(key=lambda e: e.get("start", ""), reverse=True)
        lines.append(f"\nRECENT ENTRIES ({min(len(proj_entries), 100)} of {len(proj_entries)}):")
        for entry in proj_entries[:100]:
            desc = entry.get("description", "").strip() or "(no description)"
            uid = entry.get("user_id")
            user_name = users.get(uid, {}).get("name", "Unknown") if uid else "Unknown"
            seconds = entry.get("time_entries", [{}])[0].get("seconds", 0) if entry.get("time_entries") else 0
            start = entry.get("start", "")[:10]
            lines.append(f"  - {start} | {user_name} | {seconds / 3600:.1f}h | {desc}")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Distillation prompts
# ---------------------------------------------------------------------------


SUMMARY_DISTILL_PROMPT = """\
You are distilling raw Toggl time tracking data into a structured knowledge file for Black Swift Technologies (BST).

This file will be used by an AI assistant to understand how the team spends time, identify patterns, \
and answer questions about resource allocation.

Output a markdown file with these sections:

# Toggl Time Tracking Overview

## Key Metrics
- Total hours tracked (across all time)
- Number of active team members
- Number of projects tracked

## Team Time Allocation
- Hours by team member (ranked)
- Utilization patterns

## Project Portfolio
- Hours by project (ranked, include client if known)
- Active vs inactive projects

## Patterns & Insights
- Who works on what
- Largest time investments
- Any notable patterns (e.g., certain people on certain projects, billable vs non-billable)

Be factual and concise. Include actual numbers."""


PERSON_DISTILL_PROMPT = """\
You are distilling raw Toggl time tracking data for one person into a structured knowledge file \
for Black Swift Technologies (BST).

Output a markdown file with these sections:

# {Person Name} — Time Tracking

## Summary
- Total hours tracked
- Primary projects (top 3-5 by hours)
- Time period covered

## Project Breakdown
- Hours per project with client info if available
- Percentage of total time per project

## Recent Activity
- What they've been working on recently
- Any notable patterns in descriptions or tags

## Patterns
- Typical work focus areas
- Any shifts in focus over time (if visible from data)

Be factual and concise. Include actual numbers."""


PROJECT_DISTILL_PROMPT = """\
You are distilling raw Toggl time tracking data for one project into a structured knowledge file \
for Black Swift Technologies (BST).

Output a markdown file with these sections:

# {Project Name} — Time Tracking

## Overview
- Client (if known)
- Active/inactive status
- Billable status
- Total hours tracked

## Team Allocation
- Hours per team member
- Who is the primary contributor

## Activity Timeline
- Recent work entries (descriptions, who, when)
- Work patterns

## Insights
- Types of work being done (from entry descriptions)
- Any notable patterns

Be factual and concise. Include actual numbers."""


# ---------------------------------------------------------------------------
# Main scan logic
# ---------------------------------------------------------------------------


def scan_all(mode="full", progress_callback=None):
    """Scan all Toggl time data and distill into knowledge files.

    Args:
        mode: 'full', '1yr', or 'incremental'
        progress_callback: optional fn(label, index, total) called per chunk

    Returns:
        list of output paths written
    """
    wid = _workspace_id()
    if not wid:
        print("[ERROR] TOGGL_WORKSPACE_ID not set")
        return []

    # Determine date range
    if mode == "incremental":
        last = get_last_scan("toggl")
        if last:
            start_date = last.date()
            print(f"Incremental mode: scanning changes since {start_date}")
        else:
            print("No previous scan found — falling back to full scan")
            mode = "full"

    if mode == "full":
        start_date = date(2020, 1, 1)
    elif mode == "1yr":
        start_date = date.today() - timedelta(days=365)

    end_date = date.today()

    # Collect all data
    data = _collect_all_data(start_date, end_date, progress_callback)

    users = data["users"]
    projects = data["projects"]
    summary_by_user = data["summary_by_user"]
    detailed_entries = data["detailed_entries"]

    output_paths = []

    # --- Per-person knowledge files ---
    print("\nDistilling per-person knowledge files...")
    persons_with_data = [
        uid for uid in users
        if summary_by_user.get(uid) or any(e.get("user_id") == uid for e in detailed_entries[:100])
    ]
    for i, user_id in enumerate(persons_with_data):
        user_info = users[user_id]
        name = user_info["name"]
        print(f"  [{i+1}/{len(persons_with_data)}] {name}")

        raw_text = _format_person_data(user_id, user_info, summary_by_user, detailed_entries, projects)

        # For very small data, write directly
        user_total = sum(summary_by_user.get(user_id, {}).values())
        filename = _safe_filename(name) + ".md"
        output_path = BY_PERSON_DIR / filename

        if user_total == 0:
            simple = f"# {name} — Time Tracking\n\nNo tracked time in the scanned period.\n"
            write_knowledge_file(output_path, simple)
        else:
            distill_to_markdown(raw_text, PERSON_DISTILL_PROMPT, output_path, max_tokens=1500)

        output_paths.append(output_path)
        time.sleep(1)  # Pace Claude calls

    # --- Per-project knowledge files ---
    print("\nDistilling per-project knowledge files...")
    projects_with_data = []
    for proj_id in projects:
        total = sum(
            proj_map.get(proj_id, 0) for proj_map in summary_by_user.values()
        )
        if total > 0:
            projects_with_data.append(proj_id)

    for i, proj_id in enumerate(projects_with_data):
        proj_info = projects[proj_id]
        name = proj_info["name"]
        print(f"  [{i+1}/{len(projects_with_data)}] {name}")

        raw_text = _format_project_data(proj_id, proj_info, summary_by_user, detailed_entries, users)

        filename = _safe_filename(name) + ".md"
        output_path = BY_PROJECT_DIR / filename

        distill_to_markdown(raw_text, PROJECT_DISTILL_PROMPT, output_path, max_tokens=1500)
        output_paths.append(output_path)
        time.sleep(1)

    # --- Overall summary ---
    print("\nDistilling overall summary...")
    summary_lines = _build_summary_raw(users, projects, summary_by_user, detailed_entries, start_date, end_date)
    summary_path = TOGGL_KNOWLEDGE_DIR / "summary.md"
    distill_to_markdown(summary_lines, SUMMARY_DISTILL_PROMPT, summary_path, max_tokens=2000)
    output_paths.append(summary_path)

    update_scan_timestamp("toggl")
    print(f"\nToggl scan complete. Wrote {len(output_paths)} knowledge files.")
    return output_paths


def _build_summary_raw(users, projects, summary_by_user, detailed_entries, start_date, end_date):
    """Build raw text summarizing all Toggl data for the overall summary distillation."""
    lines = [f"TOGGL TIME TRACKING DATA ({start_date} to {end_date})\n"]

    # Total hours by user
    lines.append("HOURS BY TEAM MEMBER:")
    user_totals = {}
    for user_id, proj_map in summary_by_user.items():
        total = sum(proj_map.values())
        name = users.get(user_id, {}).get("name", f"User {user_id}")
        user_totals[name] = total / 3600

    for name, hours in sorted(user_totals.items(), key=lambda x: x[1], reverse=True):
        lines.append(f"  - {name}: {hours:.1f} hours")

    grand_total = sum(user_totals.values())
    lines.append(f"\nTotal tracked in this period: {grand_total:.1f} hours across {len(user_totals)} people\n")

    # Total hours by project
    lines.append("HOURS BY PROJECT:")
    project_totals = {}
    for user_id, proj_map in summary_by_user.items():
        for proj_id, seconds in proj_map.items():
            proj_name = projects.get(proj_id, {}).get("name", f"Project {proj_id}")
            client = projects.get(proj_id, {}).get("client_name", "")
            key = f"{proj_name} ({client})" if client else proj_name
            project_totals[key] = project_totals.get(key, 0) + seconds / 3600

    for pname, hours in sorted(project_totals.items(), key=lambda x: x[1], reverse=True):
        lines.append(f"  - {pname}: {hours:.1f} hours")

    lines.append(f"\nTotal projects with tracked time: {len(project_totals)}")
    lines.append(f"Total projects in workspace: {len(projects)}")

    # Recent detailed entries sample
    if detailed_entries:
        sorted_entries = sorted(detailed_entries, key=lambda e: e.get("start", ""), reverse=True)
        lines.append(f"\nRECENT ENTRIES (sample of {min(50, len(sorted_entries))}):")
        for entry in sorted_entries[:50]:
            desc = entry.get("description", "").strip() or "(no description)"
            uid = entry.get("user_id")
            user_name = users.get(uid, {}).get("name", "Unknown") if uid else "Unknown"
            proj_id = entry.get("project_id")
            proj_name = projects.get(proj_id, {}).get("name", "No project") if proj_id else "No project"
            start = entry.get("start", "")[:10]
            lines.append(f"  - {start} | {user_name} | {proj_name} | {desc}")

    return "\n".join(lines)
