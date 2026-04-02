import os
import requests
import anthropic

ASANA_BASE = "https://app.asana.com/api/1.0"


def _headers():
    return {"Authorization": f"Bearer {os.environ['ASANA_ACCESS_TOKEN']}"}


def get_workspaces():
    resp = requests.get(f"{ASANA_BASE}/workspaces", headers=_headers(), timeout=10)
    resp.raise_for_status()
    return resp.json()["data"]


def get_projects(workspace_gid):
    resp = requests.get(
        f"{ASANA_BASE}/projects",
        headers=_headers(),
        params={"workspace": workspace_gid, "limit": 100},
        timeout=10,
    )
    resp.raise_for_status()
    return resp.json()["data"]


def get_tasks_for_project(project_gid):
    resp = requests.get(
        f"{ASANA_BASE}/tasks",
        headers=_headers(),
        params={
            "project": project_gid,
            "opt_fields": "name,assignee.name,due_on,completed,custom_fields,notes",
            "completed_since": "now",
            "limit": 100,
        },
        timeout=10,
    )
    resp.raise_for_status()
    return resp.json()["data"]


def get_team_tasks(workspace_gid):
    """Get all incomplete tasks across all projects in the workspace."""
    projects = get_projects(workspace_gid)
    all_tasks = []
    for project in projects:
        tasks = get_tasks_for_project(project["gid"])
        for task in tasks:
            task["project_name"] = project["name"]
        all_tasks.extend(tasks)
    return all_tasks


def format_task_summary(tasks):
    """Use Claude to generate a prioritized daily task summary."""
    if not tasks:
        return "No open tasks found."

    task_text = ""
    for t in tasks:
        assignee = t.get("assignee", {})
        assignee_name = assignee.get("name", "Unassigned") if assignee else "Unassigned"
        due = t.get("due_on", "No due date")
        task_text += f"- {t['name']} | Project: {t['project_name']} | Assigned: {assignee_name} | Due: {due}\n"

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        system=(
            "You are a project manager assistant. Given a list of tasks, produce a concise "
            "prioritized daily summary grouped by team member. Highlight overdue or due-today "
            "tasks first. Use Slack markdown formatting (*bold*, _italic_). Be brief and actionable."
        ),
        messages=[
            {"role": "user", "content": f"Today's date is {__import__('datetime').date.today().isoformat()}.\n\nOpen tasks:\n{task_text}"}
        ],
    )
    return message.content[0].text


def get_daily_summary():
    """Generate the full daily task summary."""
    workspaces = get_workspaces()
    if not workspaces:
        return "No Asana workspaces found."
    # Use the first workspace
    workspace_gid = workspaces[0]["gid"]
    tasks = get_team_tasks(workspace_gid)
    return format_task_summary(tasks)
