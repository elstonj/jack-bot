import os
import base64
from datetime import date, timedelta
import requests

TOGGL_BASE = "https://api.track.toggl.com"

# Label for time logged without a project. Downstream (daily_research) treats
# this exact label as "unassigned" — nothing else should ever carry it.
NO_PROJECT = "No project"


def _headers():
    token = os.environ.get("TOGGL_API_TOKEN", "")
    encoded = base64.b64encode(f"{token}:api_token".encode()).decode()
    return {"Authorization": f"Basic {encoded}", "Content-Type": "application/json"}


def _last_workday():
    """Return the most recent workday (Mon-Fri). On Mon returns Fri, on weekends returns Fri."""
    today = date.today()
    # weekday(): Mon=0 ... Sun=6
    offset = {0: 3, 6: 1, 5: 1}.get(today.weekday(), 1)  # Mon->Fri(3), Sat->Fri(1), Sun->Fri(1 day? no, Sat)
    # More explicit:
    wd = today.weekday()
    if wd == 0:    # Monday -> Friday
        offset = 3
    elif wd == 6:  # Sunday -> Friday
        offset = 2
    elif wd == 5:  # Saturday -> Friday
        offset = 1
    else:          # Tue-Fri -> previous day
        offset = 1
    return today - timedelta(days=offset)


def get_time_summary():
    """Get the last workday's time entries grouped by user and project.

    Keyed by Toggl user ID so downstream lookups don't depend on email parity
    between Toggl and the user map (e.g., Jack's Toggl email is `elstonj@...`
    while the user map has `jack.elston@...`).

    Returns:
        dict: {toggl_user_id: {
            "email": str,
            "total_hours": float,
            "projects": {name: hours},
        }}
    """
    wid = os.environ.get("TOGGL_WORKSPACE_ID")
    if not wid:
        return {}

    workday = _last_workday()
    next_day = (workday + timedelta(days=1)).isoformat()
    yesterday = workday.isoformat()
    today = next_day

    # Use the summary report endpoint
    resp = requests.post(
        f"{TOGGL_BASE}/reports/api/v3/workspace/{wid}/summary/time_entries",
        headers=_headers(),
        json={
            "start_date": yesterday,
            "end_date": today,
            "grouping": "users",
            "sub_grouping": "projects",
        },
        timeout=15,
    )
    resp.raise_for_status()
    data = resp.json()

    # Also fetch workspace users to map user IDs to emails (for display)
    users_resp = requests.get(
        f"{TOGGL_BASE}/api/v9/workspaces/{wid}/users",
        headers=_headers(),
        timeout=10,
    )
    users_resp.raise_for_status()
    user_email_map = {u["id"]: u.get("email", "").lower() for u in users_resp.json()}

    # The v3 summary report identifies each sub-group by project ID only — it
    # carries no `title`. Resolve IDs to names here; without this every entry
    # falls back to the "No project" label and the whole team looks untagged.
    project_names = {}
    try:
        for project in get_toggl_projects():
            if project.get("id"):
                project_names[project["id"]] = project.get("name") or ""
    except requests.RequestException:
        pass  # fall back to "Project <id>" labels — never to "No project"

    summary = {}
    for group in data.get("groups", []):
        user_id = group.get("id")
        if not user_id:
            continue

        total_seconds = 0
        project_seconds = {}
        for sub_group in group.get("sub_groups", []):
            seconds = sub_group.get("seconds") or 0
            total_seconds += seconds
            project_id = sub_group.get("id")
            if project_id is None:
                # Genuinely untagged time — this is the only thing downstream
                # code should count as unassigned.
                project_name = NO_PROJECT
            else:
                project_name = (
                    sub_group.get("title")
                    or project_names.get(project_id)
                    or f"Project {project_id}"
                )
            # Several sub-groups can share a name, so accumulate rather than
            # overwrite — a plain assignment kept only the last one's hours.
            project_seconds[project_name] = project_seconds.get(project_name, 0) + seconds

        summary[user_id] = {
            "email": user_email_map.get(user_id, ""),
            "total_hours": round(total_seconds / 3600, 1),
            "projects": {n: round(s / 3600, 1) for n, s in project_seconds.items()},
        }

    return summary


def get_toggl_projects():
    """Get all Toggl projects for mapping to Asana."""
    wid = os.environ.get("TOGGL_WORKSPACE_ID")
    if not wid:
        return []
    resp = requests.get(
        f"{TOGGL_BASE}/api/v9/workspaces/{wid}/projects",
        headers=_headers(),
        timeout=10,
    )
    resp.raise_for_status()
    return resp.json()
