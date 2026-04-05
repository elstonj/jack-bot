"""Google Drive deep scanner — fetches all files from shared drives, distills into knowledge files.

Produces:
  knowledge/drive/{drive_name}.md  — per-drive knowledge
  knowledge/drive/summary.md      — cross-drive overview

Modes:
  full        — all files in configured shared drives (no time filter)
  1yr         — files modified in the last year
  incremental — files modified since last scan
"""

import os
import re
import time
from datetime import date, datetime, timedelta, timezone

from google.oauth2 import service_account
from googleapiclient.discovery import build

from .base import (
    KNOWLEDGE_DIR,
    distill_to_markdown,
    get_last_scan,
    update_scan_timestamp,
    write_knowledge_file,
    get_claude_client,
    DISTILL_MODEL,
)

DRIVE_KNOWLEDGE_DIR = KNOWLEDGE_DIR / "drive"

# Google Drive API rate limiting
PAGE_LIST_DELAY = 0.1    # seconds between list pagination requests
EXPORT_DELAY = 0.5       # seconds between file content exports
MAX_CONTENT_EXPORTS_PER_DRIVE = 50  # cap doc exports in full mode

# File fields to request from the Drive API
FILE_FIELDS = (
    "id,name,mimeType,modifiedTime,createdTime,webViewLink,"
    "parents,owners,lastModifyingUser"
)

# Google Workspace MIME types that can be exported as text
EXPORTABLE_MIME_TYPES = {
    "application/vnd.google-apps.document": "text/plain",
    "application/vnd.google-apps.spreadsheet": "text/csv",
    "application/vnd.google-apps.presentation": "text/plain",
}

SCOPES = [
    "https://www.googleapis.com/auth/drive.readonly",
]


def _get_credentials(user_email):
    """Create delegated credentials for a specific user via service account."""
    import json
    import base64

    key_json = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON", "")
    if not key_json:
        return None
    key_data = json.loads(base64.b64decode(key_json))
    creds = service_account.Credentials.from_service_account_info(key_data, scopes=SCOPES)
    return creds.with_subject(user_email)


def _get_drive_service(user_email):
    """Build a Google Drive v3 service for the given user."""
    creds = _get_credentials(user_email)
    if not creds:
        raise RuntimeError("No Google service account credentials configured (GOOGLE_SERVICE_ACCOUNT_JSON)")
    return build("drive", "v3", credentials=creds, cache_discovery=False)


def _get_shared_drive_ids(service):
    """Get IDs of configured shared drives."""
    target_drives = os.environ.get("GOOGLE_SHARED_DRIVES", "Sales,Federal Projects")
    target_names = [n.strip().lower() for n in target_drives.split(",")]
    drive_ids = []
    try:
        results = service.drives().list(pageSize=50).execute()
        for drive in results.get("drives", []):
            if drive["name"].lower() in target_names:
                drive_ids.append({"id": drive["id"], "name": drive["name"]})
    except Exception as e:
        print(f"  [ERROR] Could not list shared drives: {e}")
    return drive_ids


def _list_all_files(service, drive_id, time_filter=None):
    """List all files in a shared drive with pagination.

    Args:
        service: Drive API service instance
        drive_id: ID of the shared drive
        time_filter: optional ISO datetime string — only files modified after this time

    Returns:
        list[dict]: file metadata dicts
    """
    query_parts = ["trashed = false"]
    if time_filter:
        query_parts.append(f"modifiedTime > '{time_filter}'")
    query = " and ".join(query_parts)

    all_files = []
    page_token = None

    while True:
        params = {
            "q": query,
            "fields": f"nextPageToken,files({FILE_FIELDS})",
            "orderBy": "modifiedTime desc",
            "pageSize": 1000,
            "corpora": "drive",
            "driveId": drive_id,
            "includeItemsFromAllDrives": True,
            "supportsAllDrives": True,
        }
        if page_token:
            params["pageToken"] = page_token

        result = service.files().list(**params).execute()
        all_files.extend(result.get("files", []))

        page_token = result.get("nextPageToken")
        if not page_token:
            break
        time.sleep(PAGE_LIST_DELAY)

    return all_files


def _export_content_snippet(service, file_id, mime_type, max_chars=500):
    """Export the first max_chars of a Google Workspace file as plain text.

    Returns the text snippet or None on failure.
    """
    export_mime = EXPORTABLE_MIME_TYPES.get(mime_type)
    if not export_mime:
        return None
    try:
        content = service.files().export(fileId=file_id, mimeType=export_mime).execute()
        text = content.decode("utf-8") if isinstance(content, bytes) else str(content)
        return text[:max_chars]
    except Exception:
        return None


def _build_folder_tree(files):
    """Build a folder tree structure from the flat file list.

    Builds the tree in memory from parent references rather than making
    additional API calls. Returns (tree_dict, path_map).

    tree_dict: {folder_id: {"name": str, "children": [folder_id, ...], "files": [file_dict, ...]}}
    path_map: {file_or_folder_id: "Folder/Subfolder/..." path string}
    """
    folders = {}
    non_folders = []

    for f in files:
        fid = f["id"]
        if f["mimeType"] == "application/vnd.google-apps.folder":
            folders[fid] = {
                "name": f["name"],
                "children": [],
                "files": [],
                "parent": (f.get("parents") or [None])[0],
            }
        else:
            non_folders.append(f)

    # Assign children to parents
    for fid, info in folders.items():
        parent_id = info["parent"]
        if parent_id and parent_id in folders:
            folders[parent_id]["children"].append(fid)

    # Assign files to their parent folders
    for f in non_folders:
        parent_id = (f.get("parents") or [None])[0]
        if parent_id and parent_id in folders:
            folders[parent_id]["files"].append(f)

    # Build path map
    path_map = {}

    def _resolve_path(folder_id, seen=None):
        if folder_id in path_map:
            return path_map[folder_id]
        if seen is None:
            seen = set()
        if folder_id in seen or folder_id not in folders:
            return ""
        seen.add(folder_id)
        parent_id = folders[folder_id]["parent"]
        if parent_id and parent_id in folders:
            parent_path = _resolve_path(parent_id, seen)
            path = f"{parent_path}/{folders[folder_id]['name']}" if parent_path else folders[folder_id]["name"]
        else:
            path = folders[folder_id]["name"]
        path_map[folder_id] = path
        return path

    for fid in folders:
        _resolve_path(fid)

    # Also map file IDs to their full paths
    for f in non_folders:
        parent_id = (f.get("parents") or [None])[0]
        parent_path = path_map.get(parent_id, "")
        path_map[f["id"]] = f"{parent_path}/{f['name']}" if parent_path else f["name"]

    return folders, path_map


def _format_folder_tree_text(folders, path_map):
    """Render the folder tree as indented text for distillation."""
    # Find root folders (parent not in folders dict)
    roots = [fid for fid, info in folders.items() if info["parent"] not in folders]

    lines = []

    def _render(folder_id, indent=0):
        info = folders[folder_id]
        prefix = "  " * indent
        file_count = len(info["files"])
        lines.append(f"{prefix}📁 {info['name']}/ ({file_count} files)")
        for child_id in sorted(info["children"], key=lambda c: folders[c]["name"].lower()):
            _render(child_id, indent + 1)

    for root_id in sorted(roots, key=lambda r: folders[r]["name"].lower()):
        _render(root_id)

    return "\n".join(lines)


def _categorize_file(name, mime_type):
    """Heuristic categorization of a file by name and type."""
    name_lower = name.lower()

    if any(kw in name_lower for kw in ["proposal", "rfp", "rfi", "rfo"]):
        return "Proposals & RFPs"
    if any(kw in name_lower for kw in ["contract", "agreement", "nda", "msa"]):
        return "Contracts & Agreements"
    if any(kw in name_lower for kw in ["sow", "statement of work", "scope"]):
        return "Statements of Work"
    if any(kw in name_lower for kw in ["report", "summary", "analysis", "findings"]):
        return "Reports & Analysis"
    if any(kw in name_lower for kw in ["template", "boilerplate"]):
        return "Templates"
    if any(kw in name_lower for kw in ["budget", "invoice", "cost", "pricing", "quote"]):
        return "Financial"
    if any(kw in name_lower for kw in ["presentation", "deck", "slides"]):
        return "Presentations"
    if mime_type == "application/vnd.google-apps.presentation":
        return "Presentations"
    if any(kw in name_lower for kw in ["meeting", "minutes", "agenda", "notes"]):
        return "Meeting Notes"
    if mime_type == "application/vnd.google-apps.spreadsheet":
        return "Spreadsheets"
    if mime_type == "application/vnd.google-apps.document":
        return "Documents"
    return "Other"


def _safe_filename(name):
    """Convert a drive name to a safe filename."""
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'\s+', '_', name.strip())
    return name[:80].lower()


DRIVE_DISTILL_PROMPT = """\
You are distilling raw Google Drive shared drive data into a structured knowledge file for Black Swift Technologies (BST).

This file will be used by an AI assistant to understand the company's document organization, find relevant files, \
and understand project/client document relationships.

Output a markdown file with these sections:

# {Drive Name} — Shared Drive

## Overview
- Total files and folder count
- Date range of content (oldest to newest)
- Primary purpose of this drive

## Folder Structure
Describe the organizational structure — top-level folders and what they contain.

## Key Documents by Category
Group important documents into categories:
- **Proposals & RFPs** — client proposals, solicitation responses
- **Contracts & Agreements** — signed contracts, NDAs, MSAs
- **Statements of Work** — SOWs, scope documents
- **Reports & Analysis** — deliverable reports, analysis docs
- **Financial** — budgets, invoices, pricing
- **Presentations** — slide decks, pitch materials
- **Templates** — reusable templates and boilerplates

For each category, list key documents with their path, last modified date, and who last edited them.

## Recent Activity Patterns
- Who is most active (by last-modifying-user frequency)
- What areas are seeing the most recent edits
- Any notable patterns (e.g., heavy proposal activity, contract renewals)

## Client/Project Document Mapping
Map documents to clients or projects based on folder names, file names, and content snippets. \
Group by client/project where possible.

## Important Templates & Shared Resources
Call out any templates, shared trackers, or reference documents that appear to be used across projects.

Be factual. Include file paths, dates, and names. Skip empty sections."""


SUMMARY_DISTILL_PROMPT = """\
You are creating a strategic overview of Google Drive shared drives for Black Swift Technologies (BST).

Summarize across all drives:
- Total document volume and organization quality
- Key clients/projects with the most documentation
- Cross-drive patterns (e.g., Sales drive has proposals, Federal drive has contracts)
- Important shared resources and templates
- Document management observations (naming conventions, organization patterns)
- Areas that may need attention (stale documents, disorganized folders)

Be concise and factual. Output markdown."""


def scan_drive(service, drive_info, mode="full", time_filter=None, export_content=False,
               progress_callback=None):
    """Scan a single shared drive and distill into a knowledge file.

    Args:
        service: Drive API service instance
        drive_info: {"id": str, "name": str}
        mode: scan mode (full/1yr/incremental)
        time_filter: ISO datetime string for modified-since filtering
        export_content: if True, export content snippets for Google Workspace docs
        progress_callback: optional fn(message) for status updates

    Returns:
        (drive_name, file_count, output_path) or None on failure
    """
    drive_id = drive_info["id"]
    drive_name = drive_info["name"]

    def _progress(msg):
        if progress_callback:
            progress_callback(msg)
        else:
            print(f"  {msg}")

    _progress(f"Listing files in {drive_name}...")

    try:
        files = _list_all_files(service, drive_id, time_filter=time_filter)
    except Exception as e:
        _progress(f"[ERROR] Could not list files in {drive_name}: {e}")
        return None

    if not files:
        _progress(f"[SKIP] {drive_name}: no files found")
        return None

    _progress(f"Found {len(files)} files in {drive_name}")

    # Build folder tree in memory from file list
    folders, path_map = _build_folder_tree(files)
    folder_tree_text = _format_folder_tree_text(folders, path_map)

    # Categorize files
    categories = {}
    for f in files:
        if f["mimeType"] == "application/vnd.google-apps.folder":
            continue
        cat = _categorize_file(f["name"], f["mimeType"])
        categories.setdefault(cat, []).append(f)

    # Optionally export content snippets (full mode only, capped)
    content_snippets = {}
    if export_content:
        exportable = [
            f for f in files
            if f["mimeType"] in EXPORTABLE_MIME_TYPES
        ]
        # Sort by modifiedTime descending to get most recent docs first
        exportable.sort(key=lambda f: f.get("modifiedTime", ""), reverse=True)
        export_count = min(len(exportable), MAX_CONTENT_EXPORTS_PER_DRIVE)
        _progress(f"Exporting content snippets for {export_count} docs...")

        for i, f in enumerate(exportable[:export_count]):
            snippet = _export_content_snippet(service, f["id"], f["mimeType"])
            if snippet:
                content_snippets[f["id"]] = snippet
            time.sleep(EXPORT_DELAY)

    # Build raw text for distillation
    non_folder_files = [f for f in files if f["mimeType"] != "application/vnd.google-apps.folder"]
    folder_count = len(files) - len(non_folder_files)

    lines = [
        f"SHARED DRIVE: {drive_name}",
        f"Total files: {len(non_folder_files)}, Folders: {folder_count}",
        "",
    ]

    # Date range
    mod_times = [f.get("modifiedTime", "") for f in non_folder_files if f.get("modifiedTime")]
    if mod_times:
        lines.append(f"Oldest modified: {min(mod_times)[:10]}")
        lines.append(f"Newest modified: {max(mod_times)[:10]}")

    created_times = [f.get("createdTime", "") for f in non_folder_files if f.get("createdTime")]
    if created_times:
        lines.append(f"Oldest created: {min(created_times)[:10]}")

    # Folder structure
    lines.append("\n--- FOLDER STRUCTURE ---")
    lines.append(folder_tree_text)

    # Files by category
    lines.append("\n--- FILES BY CATEGORY ---")
    for cat in sorted(categories.keys()):
        cat_files = categories[cat]
        lines.append(f"\n## {cat} ({len(cat_files)} files)")
        # Show up to 30 files per category, sorted by modifiedTime desc
        cat_files.sort(key=lambda f: f.get("modifiedTime", ""), reverse=True)
        for f in cat_files[:30]:
            owner = ""
            if f.get("owners"):
                owner = f["owners"][0].get("displayName", "")
            last_editor = ""
            if f.get("lastModifyingUser"):
                last_editor = f["lastModifyingUser"].get("displayName", "")
            path = path_map.get(f["id"], f["name"])
            mod = f.get("modifiedTime", "")[:10]
            line = f"  - {path} | Modified: {mod}"
            if last_editor:
                line += f" | Editor: {last_editor}"
            if owner:
                line += f" | Owner: {owner}"
            # Add content snippet if available
            snippet = content_snippets.get(f["id"])
            if snippet:
                # Compact the snippet to a single line
                snippet_oneline = " ".join(snippet.split())[:200]
                line += f"\n    Content: {snippet_oneline}"
            lines.append(line)
        if len(cat_files) > 30:
            lines.append(f"  ... and {len(cat_files) - 30} more")

    # Activity patterns — who edits most
    editor_counts = {}
    for f in non_folder_files:
        editor = (f.get("lastModifyingUser") or {}).get("displayName", "Unknown")
        editor_counts[editor] = editor_counts.get(editor, 0) + 1

    lines.append("\n--- ACTIVITY BY USER ---")
    for editor, count in sorted(editor_counts.items(), key=lambda x: -x[1])[:15]:
        lines.append(f"  {editor}: {count} files last edited")

    raw_text = "\n".join(lines)

    # Distill into knowledge file
    filename = _safe_filename(drive_name) + ".md"
    output_path = DRIVE_KNOWLEDGE_DIR / filename

    # For very small drives, write a simple summary without Claude
    if len(non_folder_files) <= 5:
        simple = f"# {drive_name} — Shared Drive\n\nSmall drive with {len(non_folder_files)} files.\n\n"
        for f in non_folder_files:
            mod = f.get("modifiedTime", "")[:10]
            simple += f"- {f['name']} (modified {mod})\n"
        write_knowledge_file(output_path, simple)
        return drive_name, len(non_folder_files), output_path

    _progress(f"Distilling {drive_name} ({len(non_folder_files)} files)...")
    distill_to_markdown(raw_text, DRIVE_DISTILL_PROMPT, output_path, max_tokens=3000)
    return drive_name, len(non_folder_files), output_path


def scan_all(mode="full", delegate_email=None, progress_callback=None):
    """Scan all configured shared drives.

    Args:
        mode: 'full', '1yr', or 'incremental'
        delegate_email: Google user email to impersonate. Falls back to
            GOOGLE_DELEGATE_EMAIL env var, then 'jack.elston@blackswifttechnologies.com'.
        progress_callback: optional fn(drive_name, index, total) called per drive

    Returns:
        list of (drive_name, file_count, output_path) tuples
    """
    if delegate_email is None:
        delegate_email = os.environ.get(
            "GOOGLE_DELEGATE_EMAIL",
            "jack.elston@blackswifttech.com",
        )

    service = _get_drive_service(delegate_email)
    shared_drives = _get_shared_drive_ids(service)

    if not shared_drives:
        print("[ERROR] No matching shared drives found")
        return []

    print(f"Found {len(shared_drives)} shared drives: {', '.join(d['name'] for d in shared_drives)}")

    # Determine time filter based on mode
    time_filter = None
    if mode == "1yr":
        one_year_ago = datetime.now(timezone.utc) - timedelta(days=365)
        time_filter = one_year_ago.isoformat()
        print(f"1yr mode: scanning files modified since {time_filter[:10]}")
    elif mode == "incremental":
        last = get_last_scan("drive")
        if last:
            time_filter = last.isoformat()
            print(f"Incremental mode: scanning changes since {time_filter}")
        else:
            print("No previous scan found — falling back to full scan")
            mode = "full"

    # Only export content in full mode
    export_content = mode == "full"

    results = []
    for i, drive_info in enumerate(shared_drives):
        if progress_callback:
            progress_callback(drive_info["name"], i, len(shared_drives))
        else:
            print(f"\n[{i + 1}/{len(shared_drives)}] {drive_info['name']}")

        def _drive_progress(msg):
            if progress_callback:
                progress_callback(msg, i, len(shared_drives))
            else:
                print(f"  {msg}")

        result = scan_drive(
            service,
            drive_info,
            mode=mode,
            time_filter=time_filter,
            export_content=export_content,
            progress_callback=_drive_progress,
        )
        if result:
            results.append(result)

        # Pace between drives
        time.sleep(1)

    # Generate cross-drive summary
    if results:
        _generate_summary(results)

    update_scan_timestamp("drive")
    return results


def _generate_summary(results):
    """Generate a cross-drive summary from all scanned drives."""
    lines = ["# Google Drive — Shared Drives Overview\n"]
    lines.append(f"Last scanned: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    lines.append(f"Total drives scanned: {len(results)}\n")

    lines.append("## Drives\n")
    for name, file_count, path in sorted(results, key=lambda r: r[0]):
        lines.append(f"- **{name}** — {file_count} files — [{path.name}]({path.name})")

    # Distill a strategic summary from per-drive knowledge files
    drive_snippets = []
    for name, file_count, path in results:
        if path.exists():
            content = path.read_text()
            drive_snippets.append(f"### {name}\n{content[:1000]}")

    if drive_snippets:
        combined = "\n\n".join(drive_snippets)
        if len(combined) > 90000:
            combined = combined[:90000] + "\n\n[TRUNCATED]"

        client = get_claude_client()
        for attempt in range(5):
            try:
                message = client.messages.create(
                    model=DISTILL_MODEL,
                    max_tokens=2000,
                    system=SUMMARY_DISTILL_PROMPT,
                    messages=[{"role": "user", "content": f"Drive summaries:\n\n{combined}"}],
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

    summary_path = DRIVE_KNOWLEDGE_DIR / "summary.md"
    write_knowledge_file(summary_path, "\n".join(lines))
    print(f"Summary written to {summary_path}")
