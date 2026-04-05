"""Google Drive proposals & reports scanner — extracts full text from proposals,
reports, and technical documents, distills into searchable knowledge files.

Produces:
  knowledge/proposals/{safe_filename}.md  — per-document knowledge
  knowledge/proposals/catalog.md          — master catalog of all scanned documents

Handles:
  - Google Docs (exported as text/plain via Drive API)
  - PDFs (downloaded and extracted via pypdf)
  - DOCX files (downloaded and extracted via python-docx)

Modes:
  full        — all matching documents (no time filter)
  1yr         — documents modified in the last year
  incremental — documents modified since last scan
"""

import io
import os
import re
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

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

PROPOSALS_KNOWLEDGE_DIR = KNOWLEDGE_DIR / "proposals"

# Rate limiting
PAGE_LIST_DELAY = 0.1
EXPORT_DELAY = 0.5
DOWNLOAD_DELAY = 0.5

# Max chars to extract per document before sending to Claude
MAX_DOC_CHARS = 60000

SCOPES = [
    "https://www.googleapis.com/auth/drive.readonly",
]

# MIME types we can extract text from
GOOGLE_DOC_MIME = "application/vnd.google-apps.document"
GOOGLE_SLIDES_MIME = "application/vnd.google-apps.presentation"
PDF_MIME = "application/pdf"
DOCX_MIME = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"

# Filename/folder keywords that indicate a proposal or report
PROPOSAL_KEYWORDS = [
    "proposal", "rfp", "rfi", "rfo", "solicitation", "bid",
    "report", "deliverable", "final report", "technical report",
    "white paper", "whitepaper", "concept", "conops",
    "capability", "capabilities", "overview", "briefing",
    "sow", "statement of work", "technical volume",
    "quad chart", "quadchart",
]

# Folder names that typically contain proposals/reports
PROPOSAL_FOLDER_KEYWORDS = [
    "proposal", "deliverable", "report", "rfp", "rfi",
    "submissions", "submitted", "technical volume",
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
        raise RuntimeError("No Google service account credentials configured")
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


def _is_proposal_or_report(file_name, parent_path=""):
    """Check if a file looks like a proposal, report, or technical document."""
    combined = f"{parent_path}/{file_name}".lower()
    return any(kw in combined for kw in PROPOSAL_KEYWORDS)


def _list_candidate_files(service, drive_id, time_filter=None):
    """List all files that could be proposals/reports from a shared drive.

    Returns files that are Google Docs, PDFs, or DOCX and match keyword heuristics.
    """
    target_mimes = [GOOGLE_DOC_MIME, GOOGLE_SLIDES_MIME, PDF_MIME, DOCX_MIME]

    # Build query: non-trashed files of target types
    mime_clauses = " or ".join(f"mimeType = '{m}'" for m in target_mimes)
    query_parts = [f"trashed = false", f"({mime_clauses})"]
    if time_filter:
        query_parts.append(f"modifiedTime > '{time_filter}'")
    query = " and ".join(query_parts)

    file_fields = (
        "id,name,mimeType,modifiedTime,createdTime,webViewLink,"
        "parents,owners,lastModifyingUser"
    )

    all_files = []
    page_token = None

    while True:
        params = {
            "q": query,
            "fields": f"nextPageToken,files({file_fields})",
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

    # Also fetch all folders so we can resolve paths for keyword matching
    folder_map = _fetch_folder_map(service, drive_id)

    # Filter to files that match proposal/report heuristics
    candidates = []
    for f in all_files:
        parent_path = _resolve_parent_path(f, folder_map)
        if _is_proposal_or_report(f["name"], parent_path):
            f["_parent_path"] = parent_path
            candidates.append(f)

    return candidates


def _fetch_folder_map(service, drive_id):
    """Build a folder_id -> {name, parent} map for path resolution."""
    folder_map = {}
    page_token = None
    while True:
        params = {
            "q": "trashed = false and mimeType = 'application/vnd.google-apps.folder'",
            "fields": "nextPageToken,files(id,name,parents)",
            "pageSize": 1000,
            "corpora": "drive",
            "driveId": drive_id,
            "includeItemsFromAllDrives": True,
            "supportsAllDrives": True,
        }
        if page_token:
            params["pageToken"] = page_token

        result = service.files().list(**params).execute()
        for folder in result.get("files", []):
            folder_map[folder["id"]] = {
                "name": folder["name"],
                "parent": (folder.get("parents") or [None])[0],
            }

        page_token = result.get("nextPageToken")
        if not page_token:
            break
        time.sleep(PAGE_LIST_DELAY)

    return folder_map


def _resolve_parent_path(file_dict, folder_map, max_depth=10):
    """Resolve the folder path for a file using the folder map."""
    parts = []
    parent_id = (file_dict.get("parents") or [None])[0]
    depth = 0
    while parent_id and parent_id in folder_map and depth < max_depth:
        folder = folder_map[parent_id]
        parts.append(folder["name"])
        parent_id = folder["parent"]
        depth += 1
    parts.reverse()
    return "/".join(parts)


def _extract_google_doc(service, file_id):
    """Export a Google Doc as plain text."""
    try:
        content = service.files().export(fileId=file_id, mimeType="text/plain").execute()
        text = content.decode("utf-8") if isinstance(content, bytes) else str(content)
        return text[:MAX_DOC_CHARS]
    except Exception as e:
        print(f"    [WARN] Could not export Google Doc {file_id}: {e}")
        return None


def _extract_google_slides(service, file_id):
    """Export Google Slides as plain text."""
    try:
        content = service.files().export(fileId=file_id, mimeType="text/plain").execute()
        text = content.decode("utf-8") if isinstance(content, bytes) else str(content)
        return text[:MAX_DOC_CHARS]
    except Exception as e:
        print(f"    [WARN] Could not export Google Slides {file_id}: {e}")
        return None


def _download_file_bytes(service, file_id):
    """Download a binary file from Drive."""
    try:
        content = service.files().get_media(fileId=file_id).execute()
        return content
    except Exception as e:
        print(f"    [WARN] Could not download file {file_id}: {e}")
        return None


def _extract_pdf_text(file_bytes):
    """Extract text from a PDF using pypdf."""
    try:
        from pypdf import PdfReader
        reader = PdfReader(io.BytesIO(file_bytes))
        pages = []
        for page in reader.pages:
            text = page.extract_text()
            if text:
                pages.append(text)
            if sum(len(p) for p in pages) > MAX_DOC_CHARS:
                break
        full_text = "\n\n".join(pages)
        return full_text[:MAX_DOC_CHARS]
    except ImportError:
        print("    [WARN] pypdf not installed — skipping PDF extraction (pip install pypdf)")
        return None
    except Exception as e:
        print(f"    [WARN] PDF extraction failed: {e}")
        return None


def _extract_docx_text(file_bytes):
    """Extract text from a DOCX file using python-docx."""
    try:
        from docx import Document
        doc = Document(io.BytesIO(file_bytes))
        paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
        full_text = "\n\n".join(paragraphs)
        return full_text[:MAX_DOC_CHARS]
    except ImportError:
        print("    [WARN] python-docx not installed — skipping DOCX extraction (pip install python-docx)")
        return None
    except Exception as e:
        print(f"    [WARN] DOCX extraction failed: {e}")
        return None


def _extract_text(service, file_dict):
    """Extract full text from a file based on its MIME type."""
    mime = file_dict["mimeType"]
    file_id = file_dict["id"]

    if mime == GOOGLE_DOC_MIME:
        return _extract_google_doc(service, file_id)
    elif mime == GOOGLE_SLIDES_MIME:
        return _extract_google_slides(service, file_id)
    elif mime in (PDF_MIME, DOCX_MIME):
        file_bytes = _download_file_bytes(service, file_id)
        if not file_bytes:
            return None
        if mime == PDF_MIME:
            return _extract_pdf_text(file_bytes)
        else:
            return _extract_docx_text(file_bytes)
    return None


def _safe_filename(name):
    """Convert a document name to a safe filename."""
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'\s+', '_', name.strip())
    return name[:80].lower()


DOCUMENT_DISTILL_PROMPT = """\
You are distilling a proposal, report, or technical document from Black Swift Technologies (BST) \
into a structured knowledge file. This file will be used by an AI assistant to answer questions about \
BST's products, capabilities, proposed uses, technical approaches, and project history.

Extract and organize the following information:

# {Document Title}

## Document Metadata
- Type: (proposal / report / white paper / capability brief / etc.)
- Client/Agency: (who this was written for)
- Program/Solicitation: (SBIR topic, contract number, RFP name if applicable)
- Date: (when written/submitted)
- BST Products/Systems Referenced: (S2, S3, SwiftCore, MultiScat, AeroPod, etc.)
- Key Personnel: (BST team members named)

## Executive Summary
2-3 sentence summary of what this document proposes or reports on.

## Technical Approach
Key technical details: what BST proposed to do, how, and with what systems/technology.

## Products & Capabilities Described
For each BST product or system mentioned, capture:
- What it is
- How it was proposed to be used in this context
- Any specifications or performance claims

## Use Cases & Applications
Specific use cases, missions, or applications described (e.g., arctic operations, \
volcano monitoring, hurricane sampling, methane detection, etc.)

## Key Results (for reports)
If this is a report with results, capture key findings, data, and conclusions.

## Notable Details
Any other noteworthy information: partnerships, unique capabilities, competitive advantages, \
client requirements addressed.

Be thorough but concise. Preserve specific numbers, dates, and technical details. \
Skip boilerplate (cover pages, tables of contents, compliance matrices). \
If the document is too short or lacks substance, note that."""


CATALOG_PROMPT = """\
You are creating a master catalog of BST proposals, reports, and technical documents. \
This catalog helps users quickly find documents by topic, product, client, or application.

Create a markdown catalog organized as:

# BST Document Catalog

## By Product/System
Group documents by which BST product they feature (S2, S3, SwiftCore, MultiScat, AeroPod, etc.)

## By Client/Agency
Group by client (NASA, NOAA, Navy, USGS, etc.)

## By Application Area
Group by use case (arctic ops, volcano monitoring, hurricane, methane detection, precision ag, etc.)

## By Document Type
Group by type (proposals, reports, white papers, capability briefs)

For each entry, include: document name, client, date, and a one-line description. \
Include the knowledge file name in parentheses so users can find the full document.

Be comprehensive — include every document provided."""


def scan_document(service, file_dict, progress_callback=None):
    """Scan a single document: extract text, distill into knowledge file.

    Returns:
        (doc_name, char_count, output_path) or None on failure
    """
    name = file_dict["name"]
    mime = file_dict["mimeType"]
    parent_path = file_dict.get("_parent_path", "")

    def _progress(msg):
        if progress_callback:
            progress_callback(msg)
        else:
            print(f"    {msg}")

    # Skip if output file already exists (resume support)
    filename = _safe_filename(name) + ".md"
    output_path = PROPOSALS_KNOWLEDGE_DIR / filename
    if output_path.exists() and output_path.stat().st_size > 100:
        _progress(f"[SKIP] Already scanned — {filename}")
        return name, 0, output_path

    _progress(f"Extracting: {name}")

    text = _extract_text(service, file_dict)
    if not text or len(text.strip()) < 100:
        _progress(f"[SKIP] {name}: insufficient text extracted")
        return None

    # Build metadata header for the distillation input
    owner = ""
    if file_dict.get("owners"):
        owner = file_dict["owners"][0].get("displayName", "")
    last_editor = ""
    if file_dict.get("lastModifyingUser"):
        last_editor = file_dict["lastModifyingUser"].get("displayName", "")
    mod_date = file_dict.get("modifiedTime", "")[:10]
    created_date = file_dict.get("createdTime", "")[:10]
    link = file_dict.get("webViewLink", "")

    raw_input = (
        f"DOCUMENT: {name}\n"
        f"Location: {parent_path}/{name}\n"
        f"Type: {mime}\n"
        f"Created: {created_date}\n"
        f"Modified: {mod_date}\n"
        f"Owner: {owner}\n"
        f"Last editor: {last_editor}\n"
        f"Link: {link}\n"
        f"\n--- DOCUMENT TEXT ---\n\n"
        f"{text}"
    )

    filename = _safe_filename(name) + ".md"
    output_path = PROPOSALS_KNOWLEDGE_DIR / filename

    _progress(f"Distilling: {name} ({len(text)} chars)")
    result = distill_to_markdown(raw_input, DOCUMENT_DISTILL_PROMPT, output_path, max_tokens=3000)

    if result is None:
        return None

    return name, len(text), output_path


def _generate_catalog(results):
    """Generate a master catalog from all scanned documents."""
    doc_summaries = []
    for name, char_count, path in results:
        if path.exists():
            content = path.read_text()
            # Take first 500 chars of each for the catalog input
            doc_summaries.append(f"### {name}\nFile: {path.name}\n{content[:500]}")

    if not doc_summaries:
        return

    combined = "\n\n".join(doc_summaries)
    if len(combined) > 90000:
        combined = combined[:90000] + "\n\n[TRUNCATED]"

    client = get_claude_client()
    for attempt in range(5):
        try:
            message = client.messages.create(
                model=DISTILL_MODEL,
                max_tokens=4000,
                system=CATALOG_PROMPT,
                messages=[{"role": "user", "content": f"Documents to catalog:\n\n{combined}"}],
            )
            catalog_path = PROPOSALS_KNOWLEDGE_DIR / "catalog.md"
            write_knowledge_file(catalog_path, message.content[0].text)
            print(f"  Catalog written to {catalog_path}")
            return
        except Exception as e:
            if "rate_limit" in str(e).lower():
                wait = 30 * (attempt + 1)
                print(f"  Rate limited on catalog, waiting {wait}s...")
                time.sleep(wait)
            else:
                print(f"  [WARN] Catalog generation failed: {e}")
                return


def scan_all(mode="full", delegate_email=None, progress_callback=None):
    """Scan all proposals and reports from configured shared drives.

    Args:
        mode: 'full', '1yr', or 'incremental'
        delegate_email: Google user email to impersonate
        progress_callback: optional fn(message) for status updates

    Returns:
        list of (doc_name, char_count, output_path) tuples
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

    # Determine time filter
    time_filter = None
    if mode == "1yr":
        one_year_ago = datetime.now(timezone.utc) - timedelta(days=365)
        time_filter = one_year_ago.isoformat()
        print(f"1yr mode: scanning docs modified since {time_filter[:10]}")
    elif mode == "incremental":
        last = get_last_scan("proposals")
        if last:
            time_filter = last.isoformat()
            print(f"Incremental mode: scanning changes since {time_filter}")
        else:
            print("No previous scan found — falling back to full scan")
            mode = "full"

    # Collect candidates from all drives
    all_candidates = []
    for drive_info in shared_drives:
        print(f"\n  Searching {drive_info['name']} for proposals & reports...")
        candidates = _list_candidate_files(service, drive_info["id"], time_filter=time_filter)
        print(f"  Found {len(candidates)} candidate documents in {drive_info['name']}")
        all_candidates.extend(candidates)

    if not all_candidates:
        print("No proposal/report documents found")
        update_scan_timestamp("proposals")
        return []

    print(f"\nTotal candidates: {len(all_candidates)} documents")

    # Sort by modifiedTime descending (most recent first)
    all_candidates.sort(key=lambda f: f.get("modifiedTime", ""), reverse=True)

    # Process each document
    results = []
    for i, file_dict in enumerate(all_candidates):
        print(f"\n[{i + 1}/{len(all_candidates)}] {file_dict['name']}")

        result = scan_document(service, file_dict, progress_callback=progress_callback)
        if result:
            results.append(result)

        time.sleep(EXPORT_DELAY)

    # Generate master catalog
    if results:
        print(f"\nGenerating catalog from {len(results)} documents...")
        _generate_catalog(results)

    update_scan_timestamp("proposals")
    return results
