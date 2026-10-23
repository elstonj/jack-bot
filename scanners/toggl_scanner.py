"""Toggl deep scanner — fetches time entry data, distills into knowledge files.

Produces:
  knowledge/toggl/summary.md                    — overall time tracking overview
  knowledge/toggl/by_person/{name}.md           — per-person time allocation history
  knowledge/toggl/by_project/{project_name}.md  — per-project time history

Modes:
  full        — refetch every month from 2020-01-01
  1yr         — refetch the last 12 months
  incremental — refetch the current and previous month

Hours are cached per month in .monthly_totals.json and totals are summed in
code; each refetched month replaces its cached value. Files used to be merged
by the model from a "since last scan" slice, so totals drifted run to run
(550-1 went 390.2 -> "390.2+4.8=395.0" -> "396.5+2.0"). The model now writes
only the narrative, and the totals block is stamped by code.
"""

import json
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

MONTHLY_CACHE = TOGGL_KNOWLEDGE_DIR / ".monthly_totals.json"
NAMES_FILE = TOGGL_KNOWLEDGE_DIR / ".names.json"
HISTORY_START = date(2020, 1, 1)
# Detailed entries (descriptions) feed the narrative; totals don't need them.
NARRATIVE_DAYS = 60

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
    """Generate (chunk_start, chunk_end) date pairs, one month each.

    Both ends are inclusive, matching the Reports API v3 (a query for
    2026-10-01..2026-10-01 returns that day's hours). Chunks used to end on
    the 1st of the next month, which counted every month boundary twice.
    """
    chunks = []
    current = start_date
    while current <= end_date:
        if current.month == 12:
            next_month = date(current.year + 1, 1, 1)
        else:
            next_month = date(current.year, current.month + 1, 1)
        chunk_end = min(next_month - timedelta(days=1), end_date)
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


def _load_monthly():
    """{"YYYY-MM": {user_id: {project_id: seconds}}} from the cache file."""
    try:
        raw = json.loads(MONTHLY_CACHE.read_text())
    except (FileNotFoundError, ValueError):
        return {}
    return {
        month: {int(u): {(None if p == "null" else int(p)): s for p, s in pm.items()}
                for u, pm in users.items()}
        for month, users in raw.items()
    }


def _save_monthly(monthly):
    raw = {
        month: {str(u): {("null" if p is None else str(p)): s for p, s in pm.items()}
                for u, pm in users.items()}
        for month, users in sorted(monthly.items())
    }
    MONTHLY_CACHE.parent.mkdir(parents=True, exist_ok=True)
    MONTHLY_CACHE.write_text(json.dumps(raw, indent=1, sort_keys=True))


def _sum_monthly(monthly):
    """All-time {user_id: {project_id: seconds}}, summed in code."""
    totals = {}
    for users in monthly.values():
        for uid, pm in users.items():
            for pid, secs in pm.items():
                totals.setdefault(uid, {})
                totals[uid][pid] = totals[uid].get(pid, 0) + secs
    return totals


def _collect_all_data(start_date, end_date, progress_callback=None, narrative_start=None):
    """Refresh monthly totals from start_date and fetch recent detailed entries.

    Each fetched month *replaces* its cached totals, so re-fetching a month
    never double-counts it, and summary_by_user is the all-time sum computed
    from the cache, never a model's running total. Detailed entries (for the
    narrative) are fetched only for months on or after narrative_start.

    Returns:
        dict with keys: users, projects, clients, summary_by_user,
        previous_summary_by_user, detailed_entries
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

    monthly = _load_monthly()
    previous = _sum_monthly(monthly)
    all_detailed = []

    for i, (chunk_start, chunk_end) in enumerate(chunks):
        label = chunk_start.strftime("%Y-%m")
        if progress_callback:
            progress_callback(f"Toggl {label}", i, len(chunks))
        else:
            print(f"  [{i+1}/{len(chunks)}] {label}")

        # Fetch summary. A failed month keeps its cached totals.
        try:
            summary_data = _fetch_summary_chunk(chunk_start.isoformat(), chunk_end.isoformat())
            month = {}
            for group in summary_data.get("groups", []):
                user_id = group.get("id")
                for sub in group.get("sub_groups", []):
                    proj_id = sub.get("id")
                    month.setdefault(user_id, {})
                    month[user_id][proj_id] = (
                        month[user_id].get(proj_id, 0) + sub.get("seconds", 0)
                    )
            monthly[label] = month
        except Exception as e:
            print(f"    [WARN] Summary fetch failed for {label}: {e}")

        time.sleep(REQUEST_DELAY)

        # Fetch detailed entries
        if narrative_start and chunk_end < narrative_start:
            continue
        try:
            detailed = _fetch_detailed_chunk(chunk_start.isoformat(), chunk_end.isoformat())
            all_detailed.extend(detailed)
        except Exception as e:
            print(f"    [WARN] Detailed fetch failed for {label}: {e}")

        time.sleep(REQUEST_DELAY)

    _save_monthly(monthly)
    # Names for the cached ids, so offline consumers (cost tracker) can read
    # hours per person per project without calling Toggl.
    NAMES_FILE.write_text(json.dumps({
        "users": {str(u): v["name"] for u, v in users.items()},
        "projects": {str(p): v["name"] for p, v in projects.items()},
    }, indent=1, sort_keys=True))
    print(f"  Collected {len(all_detailed)} detailed time entries")

    return {
        "users": users,
        "projects": projects,
        "clients": clients,
        "summary_by_user": _sum_monthly(monthly),
        "previous_summary_by_user": previous,
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
    lines.append(f"All-time tracked hours (computed from monthly totals since {HISTORY_START}; authoritative, do not recompute): {total_seconds / 3600:.1f} hours\n")

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
            # Toggl's detailed report returns tag_ids as ints, not strings
            raw_tags = entry.get("tag_ids") or []
            tags = ", ".join(str(t) for t in raw_tags)
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

    lines.append(f"All-time tracked hours (computed from monthly totals since {HISTORY_START}; authoritative, do not recompute): {total_seconds / 3600:.1f} hours\n")

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

    # Months to refetch. Every other month comes from the cache unchanged.
    end_date = date.today()
    first_of_month = end_date.replace(day=1)
    if mode == "incremental" and not MONTHLY_CACHE.exists():
        print("No monthly cache yet — backfilling from full history")
        mode = "full"
    if mode == "full":
        start_date = HISTORY_START
    elif mode == "1yr":
        start_date = (first_of_month - timedelta(days=335)).replace(day=1)
    else:
        start_date = (first_of_month - timedelta(days=1)).replace(day=1)
    narrative_start = end_date - timedelta(days=NARRATIVE_DAYS)

    data = _collect_all_data(start_date, end_date, progress_callback,
                             narrative_start=narrative_start)

    users = data["users"]
    projects = data["projects"]
    summary_by_user = data["summary_by_user"]
    previous = data["previous_summary_by_user"]
    detailed_entries = data["detailed_entries"]
    as_of = end_date.isoformat()

    def project_total(totals, proj_id):
        return sum(pm.get(proj_id, 0) for pm in totals.values())

    output_paths = []

    # --- Per-person knowledge files ---
    # Rebuilt only when that person's totals changed (or the file is missing).
    print("\nDistilling per-person knowledge files...")
    persons_with_data = [uid for uid in users if summary_by_user.get(uid)]
    for i, user_id in enumerate(persons_with_data):
        user_info = users[user_id]
        name = user_info["name"]
        output_path = BY_PERSON_DIR / (_safe_filename(name) + ".md")
        if summary_by_user.get(user_id) == previous.get(user_id) and output_path.exists():
            continue
        print(f"  [{i+1}/{len(persons_with_data)}] {name}")

        raw_text = _format_person_data(user_id, user_info, summary_by_user, detailed_entries, projects)
        hours = sum(summary_by_user[user_id].values()) / 3600
        stamp = (f"_Computed from Toggl as of {as_of}: {hours:.1f} h tracked since "
                 f"{HISTORY_START}._\n\n")
        content = distill_to_markdown(raw_text, PERSON_DISTILL_PROMPT, output_path,
                                      max_tokens=1500, merge=False)
        if content is not None:
            write_knowledge_file(output_path, stamp + content)
            output_paths.append(output_path)
        time.sleep(1)  # Pace Claude calls

    # --- Per-project knowledge files ---
    print("\nDistilling per-project knowledge files...")
    # Toggl projects whose names differ only in case ("[550-1] Navy SBIR" and
    # "[550-1] NAVY SBIR") share one filename; each used to overwrite the
    # other, so 550-1's file showed 100 h of its 933.9 h. Group them and write
    # one combined file under the first project's id.
    groups = {}
    for pid in projects:
        if project_total(summary_by_user, pid) > 0:
            groups.setdefault(_safe_filename(projects[pid]["name"]) + ".md", []).append(pid)

    def merged(totals, pids, rep):
        return {u: {**pm, rep: sum(pm.get(p, 0) for p in pids)} for u, pm in totals.items()}

    for i, (filename, pids) in enumerate(sorted(groups.items())):
        rep = pids[0]
        proj_info = projects[rep]
        name = proj_info["name"]
        output_path = BY_PROJECT_DIR / filename
        current, before = merged(summary_by_user, pids, rep), merged(previous, pids, rep)
        unchanged = all(
            current.get(u, {}).get(rep, 0) == before.get(u, {}).get(rep, 0)
            for u in set(current) | set(before)
        )
        if unchanged and output_path.exists():
            continue
        print(f"  [{i+1}/{len(groups)}] {name}" + (f" (+{len(pids) - 1} same-name)" if len(pids) > 1 else ""))

        entries = [dict(e, project_id=rep) if e.get("project_id") in pids else e
                   for e in detailed_entries]
        raw_text = _format_project_data(rep, proj_info, current, entries, users)
        by_member = sorted(
            ((users.get(u, {}).get("name", f"User {u}"), pm.get(rep, 0) / 3600)
             for u, pm in current.items() if pm.get(rep)),
            key=lambda x: -x[1],
        )
        stamp = (f"_Computed from Toggl as of {as_of}: "
                 f"{project_total(current, rep) / 3600:.1f} h total since "
                 f"{HISTORY_START} — "
                 + ", ".join(f"{n} {h:.1f} h" for n, h in by_member) + "._\n\n")
        content = distill_to_markdown(raw_text, PROJECT_DISTILL_PROMPT, output_path,
                                      max_tokens=1500, merge=False)
        if content is not None:
            write_knowledge_file(output_path, stamp + content)
            output_paths.append(output_path)
        time.sleep(1)

    # --- Overall summary ---
    print("\nDistilling overall summary...")
    summary_lines = _build_summary_raw(users, projects, summary_by_user, detailed_entries,
                                       HISTORY_START, end_date)
    summary_path = TOGGL_KNOWLEDGE_DIR / "summary.md"
    grand = sum(sum(pm.values()) for pm in summary_by_user.values()) / 3600
    content = distill_to_markdown(summary_lines, SUMMARY_DISTILL_PROMPT, summary_path,
                                  max_tokens=2000, merge=False)
    if content is not None:
        write_knowledge_file(
            summary_path,
            f"_Computed from Toggl as of {as_of}: {grand:.1f} h tracked since {HISTORY_START}._\n\n"
            + content,
        )
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
