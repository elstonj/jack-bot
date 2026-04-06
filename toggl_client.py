import os
import base64
from datetime import date, timedelta
import requests

TOGGL_BASE = "https://api.track.toggl.com"


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

    Returns:
        dict: {email: {"total_hours": float, "projects": {name: hours}}}
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

    # Also fetch workspace users to map user IDs to emails
    users_resp = requests.get(
        f"{TOGGL_BASE}/api/v9/workspaces/{wid}/users",
        headers=_headers(),
        timeout=10,
    )
    users_resp.raise_for_status()
    user_email_map = {u["id"]: u.get("email", "").lower() for u in users_resp.json()}

    summary = {}
    for group in data.get("groups", []):
        user_id = group.get("id")
        email = user_email_map.get(user_id, "")
        if not email:
            continue

        total_seconds = 0
        projects = {}
        for sub_group in group.get("sub_groups", []):
            project_name = sub_group.get("title", "No project")
            seconds = sub_group.get("seconds", 0)
            total_seconds += seconds
            projects[project_name] = round(seconds / 3600, 1)

        summary[email] = {
            "total_hours": round(total_seconds / 3600, 1),
            "projects": projects,
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
