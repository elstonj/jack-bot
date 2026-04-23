"""Per-project SOW / proposal / budget extractor.

Given a project code (e.g. "350-4"), searches the shared drives for a folder
matching the code, pulls the most likely contract-defining documents (SOW,
proposal, budget, subcontract), extracts their text, and asks Haiku to emit
structured budget + contract terms the project-state scanner can use.

Called from `scanners/project_state_scanner.py` — this module does NOT write
its own knowledge files. It's a pure extractor, not a scanner with persisted
output. The extracted data lives inside each `knowledge/project_state/{code}.json`.
"""

from __future__ import annotations

import json
import re
import time
from typing import Optional

from .base import get_claude_client, DISTILL_MODEL
from .proposals_scanner import (
    _get_drive_service,
    _get_shared_drive_ids,
    _extract_text,
    _fetch_folder_map,
    _resolve_parent_path,
    GOOGLE_DOC_MIME, GOOGLE_SLIDES_MIME, PDF_MIME, DOCX_MIME,
)


# Priority keywords for document selection — top of the list wins if many match
_DOC_KEYWORDS = [
    ("sow", 10),
    ("statement of work", 10),
    ("subcontract", 9),
    ("contract", 8),
    ("budget", 7),
    ("proposal", 6),
    ("cost proposal", 10),
    ("cost volume", 9),
    ("price proposal", 9),
]

MAX_CANDIDATE_DOCS = 3
MAX_COMBINED_CHARS = 80000


# Module-level caches so repeated calls (one per project) don't refetch
# drive-wide folder maps and file lists. Keyed by (user_email, drive_id).
_FOLDER_MAP_CACHE: dict[tuple[str, str], dict] = {}
_FILE_LIST_CACHE: dict[tuple[str, str], list[dict]] = {}
_DRIVE_LIST_CACHE: dict[str, list[dict]] = {}


def clear_caches() -> None:
    _FOLDER_MAP_CACHE.clear()
    _FILE_LIST_CACHE.clear()
    _DRIVE_LIST_CACHE.clear()


def _cached_folder_map(service, drive_id: str, user_email: str) -> dict:
    key = (user_email, drive_id)
    if key not in _FOLDER_MAP_CACHE:
        _FOLDER_MAP_CACHE[key] = _fetch_folder_map(service, drive_id)
    return _FOLDER_MAP_CACHE[key]


def _cached_file_list(service, drive_id: str, user_email: str) -> list[dict]:
    key = (user_email, drive_id)
    if key in _FILE_LIST_CACHE:
        return _FILE_LIST_CACHE[key]

    target_mimes = [GOOGLE_DOC_MIME, GOOGLE_SLIDES_MIME, PDF_MIME, DOCX_MIME]
    mime_clauses = " or ".join(f"mimeType = '{m}'" for m in target_mimes)
    query = f"trashed = false and ({mime_clauses})"

    files: list[dict] = []
    page_token = None
    while True:
        params: dict = {
            "q": query,
            "fields": "nextPageToken,files(id,name,mimeType,parents,modifiedTime)",
            "pageSize": 1000,
            "corpora": "drive",
            "driveId": drive_id,
            "includeItemsFromAllDrives": True,
            "supportsAllDrives": True,
        }
        if page_token:
            params["pageToken"] = page_token
        result = service.files().list(**params).execute()
        files.extend(result.get("files", []))
        page_token = result.get("nextPageToken")
        if not page_token:
            break

    _FILE_LIST_CACHE[key] = files
    return files


_CODE_IN_NAME = re.compile(r"(?<!\d)(\d{3})[-_](\d{1,2})(?!\d)")


def _code_matches(label: str, code: str) -> bool:
    """True if `label` contains the canonical code (dash or underscore form)."""
    low = label.lower()
    # Match both dash and underscore forms; don't care about surrounding chars
    variants = {code.lower(), code.replace("-", "_").lower()}
    for m in _CODE_IN_NAME.finditer(low):
        found = f"{m.group(1)}-{int(m.group(2))}"
        if found in {code.lower(), code.replace("_", "-").lower()}:
            return True
        # Also accept the literal string variants (no leading-zero stripping)
        raw = f"{m.group(1)}-{m.group(2)}"
        if raw in variants or raw.replace("-", "_") in variants:
            return True
    return False


def _score_doc(name: str, parent_path: str) -> int:
    """Higher score = more likely to contain contract/budget terms."""
    hay = f"{parent_path}/{name}".lower()
    return sum(weight for kw, weight in _DOC_KEYWORDS if kw in hay)


def _find_project_folder(
    service, drive_id: str, code: str, user_email: str
) -> Optional[dict]:
    """Find the most specific folder whose name contains the project code."""
    folder_map = _cached_folder_map(service, drive_id, user_email)
    candidates = []
    for fid, f in folder_map.items():
        if _code_matches(f["name"], code):
            candidates.append({"id": fid, "name": f["name"]})
    if not candidates:
        return None
    def specificity(c: dict) -> int:
        n = c["name"].lower()
        score = 0
        if f"[{code.lower()}]" in n or f"({code.lower()}) " in n:
            score += 100
        if code.lower() in n:
            score += 10
        return score + len(n)
    candidates.sort(key=specificity, reverse=True)
    return candidates[0]


def _list_docs_in_folder(
    service, drive_id: str, folder_id: str, user_email: str
) -> list[dict]:
    """List all extractable docs anywhere under `folder_id` — cached per drive."""
    files = _cached_file_list(service, drive_id, user_email)
    folder_map = _cached_folder_map(service, drive_id, user_email)

    descendants: list[dict] = []
    for f in files:
        parents = f.get("parents") or []
        if not parents:
            continue
        seen = set()
        cur = parents[0]
        while cur and cur not in seen:
            seen.add(cur)
            if cur == folder_id:
                parent_path = _resolve_parent_path(f, folder_map)
                out = dict(f)
                out["_parent_path"] = parent_path
                descendants.append(out)
                break
            info = folder_map.get(cur)
            cur = info["parent"] if info else None

    return descendants


# ---------------------------------------------------------------------------
# Haiku extraction
# ---------------------------------------------------------------------------


EXTRACTION_PROMPT = """\
You extract contract and budget terms from SOW/proposal/subcontract documents \
for Black Swift Technologies (BST). BST is typically the performer or subcontractor.

Given one or more concatenated documents for a single project, output a STRICT \
JSON object with the following shape — no markdown fences, no prose:

{
  "budget_approved": number | null,              // total dollars TO BST (not prime total)
  "approved_source_snippet": string | null,      // quoted fragment showing where you got it
  "line_items": [                                // budget breakdown from the cost proposal
    {"category": "Labor"|"Travel"|"Materials"|"Equipment"|"Subcontracts"|"Other",
     "amount": number, "description": string | null}
  ],
  "contract_type": "fixed_price" | "cost_reimbursable" | "t_and_m" | null,
  "contract_number": string | null,              // e.g. "FA8649-23P-1076"
  "start_date": "YYYY-MM-DD" | null,
  "end_date": "YYYY-MM-DD" | null,
  "payment_cadence": string | null,              // e.g. "monthly", "milestone", "net 30", "on acceptance"
  "notes": string | null                          // anything unusual: caps, holdbacks, exceptions
}

Rules:
- budget_approved is the funding going TO BST, not the prime contract total. If only \
the prime amount is stated, set budget_approved to null and note it.
- Favor explicit cost-proposal totals over narrative text.
- If ambiguous, prefer null over guessing. Output valid JSON only.
- Line items should sum to approximately budget_approved when present; if the \
document only gives percentages or incomplete data, return an empty list.
"""


def _extract_terms_from_text(combined_text: str) -> Optional[dict]:
    """Run Haiku on concatenated document text → structured terms dict."""
    if not combined_text.strip():
        return None
    try:
        client = get_claude_client()
        msg = client.messages.create(
            model=DISTILL_MODEL,
            max_tokens=1500,
            system=EXTRACTION_PROMPT,
            messages=[{"role": "user", "content": combined_text[:MAX_COMBINED_CHARS]}],
        )
        raw = msg.content[0].text.strip()
        # Be forgiving if model wraps in fences despite instructions
        raw = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw, flags=re.MULTILINE).strip()
        return json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"    [WARN] SOW JSON parse failed: {e}; raw={raw[:200]!r}")
        return None
    except Exception as e:
        print(f"    [WARN] SOW extraction failed: {e}")
        return None


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------


def extract_for_project(user_email: str, code: str) -> Optional[dict]:
    """Find a project's Drive folder, pull top contract docs, extract terms.

    Returns the Haiku-structured terms dict, or None if no folder/docs found.
    """
    try:
        service = _get_drive_service(user_email)
    except Exception as e:
        print(f"    [WARN] Drive service unavailable: {e}")
        return None

    if user_email not in _DRIVE_LIST_CACHE:
        _DRIVE_LIST_CACHE[user_email] = _get_shared_drive_ids(service)
    drives = _DRIVE_LIST_CACHE[user_email]
    if not drives:
        print(f"    [WARN] No shared drives configured")
        return None

    folder = None
    chosen_drive_id = None
    for d in drives:
        folder = _find_project_folder(service, d["id"], code, user_email)
        if folder:
            chosen_drive_id = d["id"]
            break
    if not folder:
        print(f"    [{code}] No project folder found in shared drives")
        return None
    print(f"    [{code}] Found folder: {folder['name']}")

    docs = _list_docs_in_folder(service, chosen_drive_id, folder["id"], user_email)
    if not docs:
        print(f"    [{code}] Folder empty / no extractable docs")
        return None

    # Score + pick top N
    scored = []
    for d in docs:
        s = _score_doc(d["name"], d.get("_parent_path", ""))
        if s > 0:
            scored.append((s, d))
    scored.sort(key=lambda sd: (-sd[0], sd[1]["name"]))
    chosen = [d for _, d in scored[:MAX_CANDIDATE_DOCS]]

    if not chosen:
        print(f"    [{code}] No SOW/proposal/budget-keyworded docs in folder")
        return None

    combined_chunks = []
    for d in chosen:
        text = _extract_text(service, d)
        if not text:
            continue
        combined_chunks.append(f"=== {d['name']} ===\n{text}")
        time.sleep(0.3)
    if not combined_chunks:
        print(f"    [{code}] No text extractable from candidate docs")
        return None

    combined = "\n\n".join(combined_chunks)
    terms = _extract_terms_from_text(combined)
    if not terms:
        return None

    doc_names = [d["name"] for d in chosen]
    terms["_source_docs"] = doc_names
    print(
        f"    [{code}] Extracted: approved=${terms.get('budget_approved') or 0:,.0f}, "
        f"type={terms.get('contract_type')}, items={len(terms.get('line_items') or [])}"
    )
    return terms
