"""Project registry scanner — builds a unified project-to-systems mapping.

Fetches all Asana project overviews (custom fields, notes) and cross-references
with Slack channels and financial knowledge files to produce:
  knowledge/projects/registry.md  — master index of all projects
  knowledge/projects/{code}.md    — per-project summary with all system links

This replaces the simpler channel_projects.md mapping with a richer data source.
"""

import os
import re
import time
import requests
from pathlib import Path

from .base import (
    KNOWLEDGE_DIR,
    update_scan_timestamp,
    write_knowledge_file,
    get_claude_client,
    DISTILL_MODEL,
)

ASANA_BASE = "https://app.asana.com/api/1.0"
PROJECTS_DIR = KNOWLEDGE_DIR / "projects"
FINANCIAL_DIR = KNOWLEDGE_DIR / "financial" / "by_project"

REQUEST_DELAY = 0.4

# Custom fields we want from Asana project overviews
DESIRED_FIELDS = {
    "Organization/Customer",
    "Contact",
    "Admin:  Notes/Context",
    "Engineering Notes",
    "Products/Services",
    "Total Budget",
    "Total Funding to Black Swift",
    "Customer Type",
    "Subcontrator Name",
    "Subcontract $ Amount",
    "General Point of Contact:",
    "Billing Point of Contact",
    "Priority",
    "Due",
    "Delivery Date",
    "Project Period of Performance",
}


def _headers():
    return {"Authorization": f"Bearer {os.environ['ASANA_ACCESS_TOKEN']}"}


def _extract_project_code(name):
    """Extract project code from Asana project name like '[301-3] S0 Hurricane Phase II'."""
    m = re.match(r"\[(\d{3}[-_]\d{1,2})\]", name)
    if m:
        return m.group(1).replace("-", "_")
    m = re.match(r"\[(\d{3})\]", name)
    if m:
        return m.group(1)
    return None


def _get_all_projects():
    """Fetch all Asana projects with custom fields and notes."""
    resp = requests.get(f"{ASANA_BASE}/workspaces", headers=_headers(), timeout=10)
    resp.raise_for_status()
    workspace_gid = resp.json()["data"][0]["gid"]

    resp = requests.get(
        f"{ASANA_BASE}/projects",
        headers=_headers(),
        params={
            "workspace": workspace_gid,
            "limit": 100,
            "opt_fields": "name,notes,custom_fields,permalink_url,archived,owner.name,team.name",
        },
        timeout=15,
    )
    resp.raise_for_status()
    skip_patterns = ["previously assigned", "my tasks"]
    return [
        p for p in resp.json()["data"]
        if not p.get("archived")
        and not any(pat in p.get("name", "").lower() for pat in skip_patterns)
    ]


def _get_slack_channels(slack_client):
    """Get all Slack channels the bot is in, for cross-referencing."""
    channels = {}
    try:
        result = slack_client.conversations_list(
            types="public_channel,private_channel", limit=200
        )
        for ch in result.get("channels", []):
            if ch.get("is_member"):
                channels[ch["id"]] = {
                    "name": ch.get("name", ""),
                    "topic": ch.get("topic", {}).get("value", ""),
                    "purpose": ch.get("purpose", {}).get("value", ""),
                }
    except Exception:
        pass
    return channels


# Known project-to-channel associations that keyword matching can't infer
MANUAL_CHANNEL_HINTS = {
    # project code -> list of channel name substrings to match
    "301_3": ["hurricane", "s0-vtol"],
    "300_3": ["hurricane"],
    "026_03": ["sbir-hurricane"],
    "044_1": ["emass"],
    "550_1": ["sbir"],
    "550_2": ["sbir"],
    "025_07": ["soil-moisture", "sbir-volcano"],
    "350_4": ["sbir-volcano"],
    "018_1": ["sbir-volcano"],
}


def _match_channels(project_name, project_code, channels):
    """Try to match a project to Slack channels by name keywords and hints."""
    matched = []

    # Build keywords from the project name (skip the code prefix)
    clean_name = re.sub(r"^\[\d{3}[-_]?\d*\]\s*", "", project_name)
    keywords = [w.lower() for w in clean_name.split() if len(w) > 2]

    for ch_id, ch_info in channels.items():
        ch_name = ch_info["name"].lower()
        ch_text = f"{ch_name} {ch_info['topic']} {ch_info['purpose']}".lower()

        # Check if channel name/topic contains project code
        if project_code and project_code.replace("_", "-") in ch_text:
            matched.append((ch_id, ch_info["name"]))
            continue

        # Check manual hints
        if project_code and project_code in MANUAL_CHANNEL_HINTS:
            hints = MANUAL_CHANNEL_HINTS[project_code]
            if any(hint in ch_name for hint in hints):
                matched.append((ch_id, ch_info["name"]))
                continue

        # Check for strong keyword overlap (need 2+ hits to avoid false positives)
        hits = sum(1 for kw in keywords if kw in ch_name)
        if hits >= 2:
            matched.append((ch_id, ch_info["name"]))

    return matched


def _find_financial_files(project_code):
    """Find financial knowledge files matching this project code."""
    if not FINANCIAL_DIR.exists() or not project_code:
        return []
    matches = []
    for f in sorted(FINANCIAL_DIR.glob(f"{project_code}*.md")):
        matches.append(f.name)
    if not matches and "_" in project_code:
        prefix = project_code.split("_")[0]
        for f in sorted(FINANCIAL_DIR.glob(f"{prefix}_*.md")):
            matches.append(f.name)
    return matches


def _build_project_entry(project, channels):
    """Build a structured project entry from Asana data + cross-references."""
    code = _extract_project_code(project["name"])
    clean_name = re.sub(r"^\[\d{3}[-_]?\d*\]\s*", "", project["name"]).strip()

    # Extract custom fields
    fields = {}
    for cf in project.get("custom_fields", []):
        name = cf.get("name", "")
        value = cf.get("display_value", "")
        if value and name in DESIRED_FIELDS:
            fields[name] = value

    # Cross-reference
    matched_channels = _match_channels(project["name"], code, channels)
    financial_files = _find_financial_files(code) if code else []

    return {
        "code": code,
        "name": clean_name,
        "full_name": project["name"],
        "asana_url": project.get("permalink_url", ""),
        "asana_gid": project.get("gid", ""),
        "notes": project.get("notes", ""),
        "fields": fields,
        "slack_channels": matched_channels,
        "financial_files": financial_files,
        "owner": project.get("owner", {}).get("name", "") if project.get("owner") else "",
        "team": project.get("team", {}).get("name", "") if project.get("team") else "",
    }


def _render_project_file(entry):
    """Render a per-project markdown file."""
    lines = [f"# {entry['full_name']}", ""]

    # Quick reference table
    lines.append("## Quick Reference")
    lines.append("| Field | Value |")
    lines.append("|-------|-------|")
    if entry["code"]:
        lines.append(f"| **Project Code** | {entry['code']} |")
    lines.append(f"| **Asana** | {entry['asana_url']} |")
    if entry["owner"]:
        lines.append(f"| **Owner** | {entry['owner']} |")

    for field_name in ["Organization/Customer", "Customer Type", "Contact",
                       "General Point of Contact:", "Billing Point of Contact",
                       "Products/Services", "Total Budget",
                       "Total Funding to Black Swift", "Subcontrator Name",
                       "Subcontract $ Amount", "Priority", "Due",
                       "Delivery Date", "Project Period of Performance"]:
        if field_name in entry["fields"]:
            lines.append(f"| **{field_name}** | {entry['fields'][field_name]} |")

    if entry["slack_channels"]:
        ch_list = ", ".join(f"#{name} (`{cid}`)" for cid, name in entry["slack_channels"])
        lines.append(f"| **Slack Channels** | {ch_list} |")

    if entry["financial_files"]:
        f_list = ", ".join(entry["financial_files"])
        lines.append(f"| **Financial Files** | {f_list} |")

    # Notes
    if entry["notes"]:
        lines.extend(["", "## Project Notes", entry["notes"]])

    # Admin/Engineering notes from custom fields
    for notes_field in ["Admin:  Notes/Context", "Engineering Notes"]:
        if notes_field in entry["fields"]:
            lines.extend(["", f"## {notes_field}", entry["fields"][notes_field]])

    return "\n".join(lines)


def _render_registry(entries):
    """Render the master registry index."""
    lines = [
        "# BST Project Registry",
        "",
        "Master index of all active projects with cross-system links.",
        f"_Generated from Asana project overviews. {len(entries)} active projects._",
        "",
        "| Code | Project | Customer | Budget | Slack | Financial |",
        "|------|---------|----------|--------|-------|-----------|",
    ]

    for e in sorted(entries, key=lambda x: x.get("code") or "zzz"):
        code = e["code"] or "—"
        name = e["name"][:40]
        customer = e["fields"].get("Organization/Customer", "—")[:25]
        budget = e["fields"].get("Total Budget", "—")
        slack = ", ".join(f"#{n}" for _, n in e["slack_channels"]) or "—"
        fin = "Yes" if e["financial_files"] else "—"
        lines.append(f"| {code} | {name} | {customer} | {budget} | {slack} | {fin} |")

    # Channel-to-project quick lookup
    lines.extend([
        "",
        "## Channel → Project Lookup",
        "",
        "| Channel ID | Channel | Project Code | Project Name |",
        "|------------|---------|--------------|--------------|",
    ])
    for e in sorted(entries, key=lambda x: x.get("code") or "zzz"):
        for ch_id, ch_name in e["slack_channels"]:
            lines.append(f"| {ch_id} | #{ch_name} | {e['code'] or '—'} | {e['name'][:40]} |")

    return "\n".join(lines)


def scan(slack_client=None, progress_callback=None):
    """Run the project registry scan.

    Args:
        slack_client: Slack WebClient for channel cross-referencing (optional)
        progress_callback: function(str) for progress updates (optional)
    """
    PROJECTS_DIR.mkdir(parents=True, exist_ok=True)

    if progress_callback:
        progress_callback("Fetching Asana projects...")
    print("Fetching Asana project overviews...")
    projects = _get_all_projects()
    print(f"  Found {len(projects)} active projects")

    # Get Slack channels for cross-referencing
    channels = {}
    if slack_client:
        if progress_callback:
            progress_callback("Fetching Slack channels...")
        channels = _get_slack_channels(slack_client)
        print(f"  Found {len(channels)} Slack channels for matching")

    # Build entries
    entries = []
    for i, project in enumerate(projects):
        if progress_callback:
            progress_callback(f"Processing {i + 1}/{len(projects)}: {project['name'][:40]}...")
        entry = _build_project_entry(project, channels)
        entries.append(entry)

        # Write per-project file
        if entry["code"]:
            filename = f"{entry['code']}.md"
        else:
            safe_name = re.sub(r"[^\w\s-]", "", entry["name"]).strip().replace(" ", "_").lower()
            filename = f"{safe_name[:50]}.md"

        content = _render_project_file(entry)
        path = PROJECTS_DIR / filename
        path.write_text(content)
        time.sleep(0.1)

    # Write registry index
    registry_content = _render_registry(entries)
    (PROJECTS_DIR / "registry.md").write_text(registry_content)

    # Also update the channel_projects.md for backwards compat with finances.py
    _update_channel_map(entries)

    update_scan_timestamp("project_registry")
    print(f"Project registry scan complete: {len(entries)} projects, {sum(len(e['slack_channels']) for e in entries)} channel mappings")
    return entries


def _update_channel_map(entries):
    """Regenerate knowledge/channel_projects.md from registry data.

    Preserves any manual overrides that exist below the '## Manual Overrides' header.
    """
    # Read existing manual overrides
    map_path = KNOWLEDGE_DIR / "channel_projects.md"
    manual_lines = []
    if map_path.exists():
        in_manual = False
        for line in map_path.read_text().splitlines():
            if "## Manual Overrides" in line:
                in_manual = True
                continue
            if in_manual:
                manual_lines.append(line)

    lines = [
        "# Slack Channel to Project Code Mapping",
        "",
        "Auto-generated by project registry scanner.",
        "Manual overrides can be added at the bottom.",
        "",
        "## Auto-Generated Mappings",
        "",
    ]
    for e in sorted(entries, key=lambda x: x.get("code") or "zzz"):
        if e["code"] and e["slack_channels"]:
            for ch_id, ch_name in e["slack_channels"]:
                lines.append(f"{ch_id} = {e['code']}   # #{ch_name} -> {e['name'][:50]}")

    lines.extend(["", "## Manual Overrides"])
    if manual_lines:
        lines.extend(manual_lines)
    else:
        lines.extend(["# Add manual channel-to-project mappings below", ""])

    map_path.write_text("\n".join(lines))
