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


def get_tasks_for_project(project_gid, enriched=False):
    opt_fields = "name,assignee.name,due_on,completed,custom_fields,notes"
    if enriched:
        opt_fields = "name,assignee.name,assignee.email,due_on,due_at,completed,custom_fields,notes,tags"
    resp = requests.get(
        f"{ASANA_BASE}/tasks",
        headers=_headers(),
        params={
            "project": project_gid,
            "opt_fields": opt_fields,
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


def get_subtasks(task_gid):
    """Get subtasks for a task (used for milestones with dollar amounts)."""
    resp = requests.get(
        f"{ASANA_BASE}/tasks/{task_gid}/subtasks",
        headers=_headers(),
        params={
            "opt_fields": "name,assignee.name,assignee.email,due_on,completed,custom_fields,notes",
            "limit": 50,
        },
        timeout=10,
    )
    resp.raise_for_status()
    return resp.json()["data"]


def search_project_by_name(workspace_gid, name_prefix):
    """Search for projects matching a name prefix."""
    projects = get_projects(workspace_gid)
    return [p for p in projects if p["name"].lower().startswith(name_prefix.lower())]


def get_milestones_for_project(project_gid):
    """Get milestone tasks with their subtasks (which often have dollar amounts)."""
    resp = requests.get(
        f"{ASANA_BASE}/tasks",
        headers=_headers(),
        params={
            "project": project_gid,
            "opt_fields": "name,assignee.name,due_on,completed,custom_fields,notes,resource_subtype",
            "completed_since": "now",
            "limit": 100,
        },
        timeout=10,
    )
    resp.raise_for_status()

    milestones = []
    for task in resp.json()["data"]:
        if task.get("resource_subtype") == "milestone":
            subtasks = []
            try:
                subtasks = get_subtasks(task["gid"])
            except Exception:
                pass
            task["subtasks"] = subtasks
            milestones.append(task)
    return milestones


def get_enriched_tasks():
    """Get all incomplete tasks with full metadata for the daily research pipeline."""
    workspaces = get_workspaces()
    if not workspaces:
        return []
    workspace_gid = workspaces[0]["gid"]
    projects = get_projects(workspace_gid)
    all_tasks = []
    for project in projects:
        tasks = get_tasks_for_project(project["gid"], enriched=True)
        for task in tasks:
            task["project_name"] = project["name"]
            assignee = task.get("assignee") or {}
            task["assignee_name"] = assignee.get("name", "Unassigned")
            task["assignee_email"] = assignee.get("email", "")
        all_tasks.extend(tasks)
    return all_tasks


def get_key_project_data(workspace_gid):
    """Get data from key Asana projects: BD Pipeline, Proposals, and milestones.

    Returns:
        dict with keys: bd_pipeline, proposals, milestones
    """
    result = {"bd_pipeline": [], "proposals": [], "milestones": []}
    projects = get_projects(workspace_gid)

    for project in projects:
        name_lower = project["name"].lower()
        # BD Pipeline project
        if "bd pipeline" in name_lower:
            tasks = get_tasks_for_project(project["gid"], enriched=True)
            for t in tasks:
                t["project_name"] = project["name"]
            result["bd_pipeline"] = tasks
        # Proposals project
        elif "proposals" in name_lower and "[001-13]" in project["name"]:
            tasks = get_tasks_for_project(project["gid"], enriched=True)
            for t in tasks:
                t["project_name"] = project["name"]
            result["proposals"] = tasks

        # Collect milestones from all projects
        try:
            milestones = get_milestones_for_project(project["gid"])
            for m in milestones:
                m["project_name"] = project["name"]
            result["milestones"].extend(milestones)
        except Exception:
            continue

    return result


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


ALLOWED_UPDATE_FIELDS = {"due_on", "due_at", "assignee", "completed", "name", "notes"}


def update_task(task_gid, updates):
    """Update fields on an Asana task.

    `updates` is a dict of Asana API field names → values. Only fields in
    ALLOWED_UPDATE_FIELDS are sent. Returns (ok: bool, error: str|None).
    """
    payload = {k: v for k, v in updates.items() if k in ALLOWED_UPDATE_FIELDS}
    if not payload:
        return False, "no updatable fields"
    try:
        resp = requests.put(
            f"{ASANA_BASE}/tasks/{task_gid}",
            headers=_headers(),
            json={"data": payload},
            timeout=10,
        )
        if resp.status_code >= 400:
            return False, f"HTTP {resp.status_code}: {resp.text[:300]}"
        return True, None
    except Exception as e:
        return False, str(e)


def get_daily_summary():
    """Generate the full daily task summary."""
    workspaces = get_workspaces()
    if not workspaces:
        return "No Asana workspaces found."
    # Use the first workspace
    workspace_gid = workspaces[0]["gid"]
    tasks = get_team_tasks(workspace_gid)
    return format_task_summary(tasks)
