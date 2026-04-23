"""Project-state scanner: consolidates Asana + QBO + Toggl + corrections into
structured per-project JSON at `knowledge/project_state/{code}.json`.

This is the phase-1 deliverable. It assumes `scanners/qbo_by_class.py` has
already run (reads its JSON output); Asana/Toggl are fetched live.

Week-1 limitations (deferred to later phases):
  - `budget.approved` is left null for projects where the Asana custom field
    "Total Budget"/"Total Funding to Black Swift" is absent. Drive SOW parsing
    lands in week 2 to fill these in.
  - `budget.spent.purchases` is 0 (not yet parsing purchasing@ emails).
  - Labor rate is a flat $125/hr placeholder until Rippling is wired.
  - `committed` stays 0 until purchasing-email + open-PO tracking is added.
"""

from __future__ import annotations

import base64
import json
import os
import re
import requests
import time
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Optional

from project_state import (
    ProjectState, Customer, Contract, Budget, BudgetLineItem,
    BudgetSpent, SpendBreakdown, Milestone, TeamMember, Override,
    Category, code_to_filename, load_categories, save_project_state,
    PROJECT_STATE_DIR,
)
from asana_client import get_projects as asana_get_projects, get_workspaces as asana_get_workspaces
from .base import KNOWLEDGE_DIR, update_scan_timestamp
from . import sow_parser

QBO_BY_CLASS_DIR = KNOWLEDGE_DIR / "quickbooks" / "by_class"
PURCHASES_DIR = KNOWLEDGE_DIR / "purchases"

# Placeholder loaded labor rate until Rippling pull is wired.
LABOR_RATE_USD_PER_HR = 125.0

# How many months back to pull Toggl hours for budget math.
TOGGL_LOOKBACK_MONTHS = 24

# Purchases newer than this window are treated as "committed" (in-flight); older
# purchases are treated as "spent" (likely reflected in QBO already, but count
# them until we have a clean dedup against QBO bank transactions).
COMMITTED_WINDOW_DAYS = 30


# ---------------------------------------------------------------------------
# Asana
# ---------------------------------------------------------------------------


ASANA_BASE = "https://app.asana.com/api/1.0"


def _asana_headers():
    return {"Authorization": f"Bearer {os.environ['ASANA_ACCESS_TOKEN']}"}


def _asana_project_detail(project_gid: str) -> dict:
    resp = requests.get(
        f"{ASANA_BASE}/projects/{project_gid}",
        headers=_asana_headers(),
        params={
            "opt_fields": (
                "name,notes,archived,owner.name,current_status,custom_fields,"
                "due_on,start_on,team.name,permalink_url"
            )
        },
        timeout=15,
    )
    resp.raise_for_status()
    return resp.json().get("data", {})


def _asana_project_milestones(project_gid: str) -> list[dict]:
    """Fetch incomplete milestone tasks for a project."""
    resp = requests.get(
        f"{ASANA_BASE}/tasks",
        headers=_asana_headers(),
        params={
            "project": project_gid,
            "opt_fields": (
                "name,assignee.name,due_on,completed,completed_at,"
                "resource_subtype,custom_fields,notes"
            ),
            "completed_since": "now",  # incomplete only
            "limit": 100,
        },
        timeout=30,
    )
    resp.raise_for_status()
    tasks = resp.json().get("data", [])
    return [t for t in tasks if t.get("resource_subtype") == "milestone"]


def _asana_project_assignees(project_gid: str) -> list[str]:
    """Distinct assignee names across incomplete tasks (rough team list)."""
    resp = requests.get(
        f"{ASANA_BASE}/tasks",
        headers=_asana_headers(),
        params={
            "project": project_gid,
            "opt_fields": "assignee.name,completed",
            "completed_since": "now",
            "limit": 100,
        },
        timeout=30,
    )
    if resp.status_code != 200:
        return []
    names = set()
    for t in resp.json().get("data", []):
        assignee = t.get("assignee") or {}
        if assignee.get("name"):
            names.add(assignee["name"])
    return sorted(names)


# ---------------------------------------------------------------------------
# Custom-field parsing from Asana
# ---------------------------------------------------------------------------


def _custom_field_map(project_detail: dict) -> dict[str, str]:
    out: dict[str, str] = {}
    for cf in project_detail.get("custom_fields") or []:
        if not cf:
            continue
        name = (cf.get("name") or "").strip()
        val = cf.get("display_value")
        if name and val is not None:
            out[name] = str(val).strip()
    return out


_MONEY_RE = re.compile(r"[-+]?\$?\s?([\d,]+(?:\.\d+)?)")


def _parse_money(val: str) -> Optional[float]:
    if not val:
        return None
    m = _MONEY_RE.search(val.replace(",", ""))
    if not m:
        return None
    try:
        return float(m.group(1).replace(",", ""))
    except ValueError:
        return None


def _classify_customer_type(raw: str) -> Optional[str]:
    if not raw:
        return None
    low = raw.lower()
    if "gov" in low or "fed" in low or "state" in low:
        return "government"
    if "commer" in low:
        return "commercial"
    if "academ" in low or "univ" in low:
        return "academic"
    return raw


def _extract_customer(cf: dict[str, str]) -> Optional[Customer]:
    name = cf.get("Organization/Customer")
    if not name or name == "—":
        return None
    ctype = _classify_customer_type(cf.get("Customer Type", ""))
    return Customer(name=name, type=ctype)


def _extract_contract(cf: dict[str, str], project_detail: dict) -> Contract:
    total = _parse_money(cf.get("Total Funding to Black Swift") or cf.get("Total Budget") or "")
    due = cf.get("Due") or project_detail.get("due_on") or None
    start = project_detail.get("start_on") or None
    pop = cf.get("Project Period of Performance")
    # "Subcontrator Name" [sic in Asana]
    sub = cf.get("Subcontrator Name")
    ctype: str = "unknown"
    if sub and sub != "—":
        ctype = "unknown"  # subcontract type unknown; weeks-later SOW parse fills this
    return Contract(
        type=ctype,  # type: ignore[arg-type]
        number=cf.get("Contract Number") or None,
        total_value=total,
        start_date=str(start) if start else None,
        end_date=str(due)[:10] if due else None,
        payment_cadence=None,
        documents=[],
    )


# ---------------------------------------------------------------------------
# QBO per-class JSON consumption
# ---------------------------------------------------------------------------


def _canonicalize_code(code: str) -> str:
    """`001-01` / `001_1` / `[001-7]` → `001-1`. Matches qbo_by_class form."""
    s = code.strip().strip("[]()")
    m = re.match(r"^(\d{3})[-_](\d+)$", s)
    if not m:
        return s
    return f"{m.group(1)}-{int(m.group(2))}"


def _load_qbo_by_class(project_code: str) -> Optional[dict]:
    # QBO file is written with canonical (leading-zero-stripped) form; try that
    # first, then the raw form from categories.md.
    for variant in (_canonicalize_code(project_code), project_code):
        path = QBO_BY_CLASS_DIR / f"{code_to_filename(variant)}.json"
        if path.exists():
            try:
                return json.loads(path.read_text())
            except Exception:
                continue
    return None


def _load_purchase_totals(project_code: str) -> tuple[float, float]:
    """Sum purchasing@ email records for this project.

    Returns (spent_older_than_window, committed_within_window). Records with
    `is_purchase=false` or missing amounts are ignored. Matches both dash and
    underscore forms of the canonical code.
    """
    if not PURCHASES_DIR.exists():
        return (0.0, 0.0)
    canon = _canonicalize_code(project_code)
    variants = {canon, canon.replace("-", "_")}
    cutoff = date.today() - timedelta(days=COMMITTED_WINDOW_DAYS)
    spent = 0.0
    committed = 0.0
    for p in sorted(PURCHASES_DIR.glob("20*.json")):
        try:
            recs = json.loads(p.read_text())
        except Exception:
            continue
        for r in recs:
            if not r.get("is_purchase"):
                continue
            raw_code = (r.get("project_code") or "").strip()
            if not raw_code:
                continue
            if _canonicalize_code(raw_code) not in variants:
                continue
            amt = r.get("amount_usd")
            try:
                amt = float(amt or 0)
            except (TypeError, ValueError):
                continue
            d = r.get("date") or ""
            try:
                d_parsed = date.fromisoformat(d) if d else None
            except Exception:
                d_parsed = None
            if d_parsed and d_parsed >= cutoff:
                committed += amt
            else:
                spent += amt
    return (round(spent, 2), round(committed, 2))


# ---------------------------------------------------------------------------
# Toggl hours per project (over lookback window)
# ---------------------------------------------------------------------------


TOGGL_BASE = "https://api.track.toggl.com"


def _toggl_headers():
    token = os.environ.get("TOGGL_API_TOKEN", "")
    encoded = base64.b64encode(f"{token}:api_token".encode()).decode()
    return {"Authorization": f"Basic {encoded}", "Content-Type": "application/json"}


def _toggl_hours_by_project(months_back: int = TOGGL_LOOKBACK_MONTHS) -> dict[str, float]:
    """Return {toggl_project_name: total_hours} over the last `months_back` months.

    Toggl's summary report is capped per request; fetch in monthly chunks and
    sum. Matches BST project codes later via regex on the Toggl project name.
    """
    wid = os.environ.get("TOGGL_WORKSPACE_ID")
    if not wid:
        return {}

    # Build monthly windows
    today = date.today()
    start = (today.replace(day=1) - timedelta(days=months_back * 31)).replace(day=1)

    totals: dict[str, float] = defaultdict(float)
    cursor = start
    while cursor <= today:
        next_cursor = (cursor.replace(day=1) + timedelta(days=32)).replace(day=1)
        end = min(next_cursor - timedelta(days=1), today)
        try:
            resp = requests.post(
                f"{TOGGL_BASE}/reports/api/v3/workspace/{wid}/summary/time_entries",
                headers=_toggl_headers(),
                json={
                    "start_date": cursor.isoformat(),
                    "end_date": (end + timedelta(days=1)).isoformat(),
                    "grouping": "projects",
                    "sub_grouping": "users",
                },
                timeout=30,
            )
            if resp.status_code == 200:
                data = resp.json()
                # Need to resolve project_id → project_name. Fetch projects once.
                for group in data.get("groups", []):
                    pid = group.get("id")
                    seconds = sum(sg.get("seconds", 0) for sg in group.get("sub_groups", []))
                    totals[str(pid)] += seconds / 3600.0
        except Exception as e:
            print(f"  [WARN] Toggl chunk {cursor}..{end}: {e}")
        time.sleep(0.5)
        cursor = next_cursor

    # Resolve project IDs to names
    try:
        projects_resp = requests.get(
            f"{TOGGL_BASE}/api/v9/workspaces/{wid}/projects",
            headers=_toggl_headers(),
            timeout=15,
        )
        projects_resp.raise_for_status()
        id_to_name = {str(p["id"]): p.get("name", f"#{p['id']}") for p in projects_resp.json()}
    except Exception:
        id_to_name = {}

    return {id_to_name.get(pid, pid): round(h, 2) for pid, h in totals.items() if h > 0}


_CODE_IN_NAME_RE = re.compile(r"\[?(\d{3}[-_]\d+)\]?")


def _match_toggl_hours_to_code(hours_by_project: dict[str, float], code: str) -> float:
    """Sum hours for any Toggl project whose name contains this code."""
    code_variants = {code, code.replace("-", "_"), code.replace("_", "-")}
    total = 0.0
    for name, h in hours_by_project.items():
        m = _CODE_IN_NAME_RE.search(name)
        if m and m.group(1).replace("_", "-") in {c.replace("_", "-") for c in code_variants}:
            total += h
    return round(total, 2)


# ---------------------------------------------------------------------------
# Corrections overlay
# ---------------------------------------------------------------------------


_STATUS_WORDS = (
    "delay", "delayed", "push", "pushed", "moved", "complete", "completed",
    "done", "archived", "cancel", "cancelled", "canceled", "handled externally",
    "priority", "critical", "no longer", "instead of",
)


def _fetch_project_corrections(code: str, project_name: str) -> list[Override]:
    """Pull recent CORRECTION/FEEDBACK from Slack knowledge channel mentioning this project.

    Returns empty list if Slack isn't reachable. Re-implemented here rather than
    imported from scanners/asana_scanner so this module stays self-contained.
    """
    try:
        from slack_sdk import WebClient
    except Exception:
        return []
    token = os.environ.get("SLACK_BOT_TOKEN", "")
    channel = os.environ.get("KNOWLEDGE_CHANNEL", "")
    if not (token and channel):
        return []

    # Keywords: the code itself (both dash and underscore forms) + significant
    # lower-cased tokens from the project name (>=4 chars).
    kws = {code.lower(), code.replace("-", "_").lower(), code.replace("_", "-").lower()}
    stopwords = {"phase", "irad", "view", "project", "bst", "the", "and"}
    for tok in re.split(r"[\s\[\]\-_,()/]+", project_name.lower()):
        if len(tok) >= 4 and tok not in stopwords and not tok.isdigit():
            kws.add(tok)

    client = WebClient(token=token)
    oldest = str(int(time.time() - 30 * 86400))
    out: list[Override] = []
    seen_ts: set[str] = set()  # dedup — Slack pagination can return dupes
    cursor = None
    while True:
        try:
            kwargs: dict = {"channel": channel, "limit": 200, "oldest": oldest}
            if cursor:
                kwargs["cursor"] = cursor
            resp = client.conversations_history(**kwargs)
        except Exception:
            break
        for msg in resp.get("messages", []):
            ts = msg.get("ts", "")
            if ts in seen_ts:
                continue
            seen_ts.add(ts)
            text = msg.get("text", "")
            tag = None
            for t in ("CORRECTION", "FEEDBACK"):
                if text.startswith(f"*[{t}]*"):
                    tag = t
                    break
            if not tag:
                continue
            body = text.replace(f"*[{tag}]*\n", "", 1)
            low = body.lower()
            if not any(kw in low for kw in kws):
                continue
            # Pull author (`From X: ...` or `From X (ts=...): ...`)
            author = "unknown"
            m = re.match(r"From ([^:]+?)(?:\s*\(ts=[^)]+\))?:", body)
            if m:
                author = m.group(1).strip()
            when = ""
            try:
                when = datetime.fromtimestamp(float(ts)).strftime("%Y-%m-%d") if ts else ""
            except Exception:
                pass
            out.append(Override(source=tag, author=author, date=when or None, text=body[:500]))
        cursor = resp.get("response_metadata", {}).get("next_cursor")
        if not cursor:
            break
    return out


# ---------------------------------------------------------------------------
# Status inference
# ---------------------------------------------------------------------------


_DELAY_KWS = ("delay", "delayed", "push", "pushed", "moved", "shifted to")
_COMPLETE_KWS = ("complete", "completed", "archived", "closed out", "wrapped up")
_HOLD_KWS = ("on hold", "paused")


def _classify_override(text: str) -> Optional[str]:
    """Return one of 'delayed' | 'complete' | 'on_hold' | None for an override.

    Order matters: delay signals win over complete/done, because combined
    messages like "Mexico delayed; Navy tasks done" shouldn't classify Mexico
    as complete. And we require a stronger signal than the bare word "done"
    (which shows up constantly in unrelated contexts).
    """
    low = text.lower()
    if any(kw in low for kw in _DELAY_KWS):
        return "delayed"
    if any(kw in low for kw in _HOLD_KWS):
        return "on_hold"
    if any(kw in low for kw in _COMPLETE_KWS):
        return "complete"
    return None


def _infer_status(asana_detail: dict, overrides: list[Override]) -> tuple[str, Optional[str]]:
    """Return (status, status_notes) from Asana archived flag + corrections.

    Overrides trump Asana. If multiple overrides disagree, the *most recent*
    one wins (overrides are chronological from the channel). Within a single
    override, delay signals beat completion signals — see `_classify_override`.
    """
    if asana_detail.get("archived"):
        return "archived", "Asana project is archived"

    # Most recent override first (list comes in chronological order)
    for ov in reversed(overrides):
        cls = _classify_override(ov.text)
        if cls:
            return cls, f"{ov.source} {ov.date or ''}: {ov.text[:200]}"

    cs = asana_detail.get("current_status") or {}
    color = (cs.get("color") or "").lower()
    title = (cs.get("title") or "")
    if color == "red":
        return "delayed", title or None
    if color == "green":
        return "active", title or None
    return "active", title or None


# ---------------------------------------------------------------------------
# Milestone extraction
# ---------------------------------------------------------------------------


def _format_milestones(tasks: list[dict]) -> list[Milestone]:
    out: list[Milestone] = []
    for t in tasks:
        due = t.get("due_on")
        out.append(
            Milestone(
                name=t.get("name", "")[:200],
                asana_task_gid=t.get("gid"),
                due_on=due,
                original_due=None,  # set later when we track historical dates
                status="complete" if t.get("completed") else "open",
            )
        )
    # sort by due date ascending, None last
    out.sort(key=lambda m: (m.due_on is None, m.due_on or ""))
    return out


# ---------------------------------------------------------------------------
# Main assembly
# ---------------------------------------------------------------------------


def _find_asana_project(all_projects: list[dict], code: str, name: str) -> Optional[dict]:
    # exact bracketed code match first
    for p in all_projects:
        if re.search(rf"\[{re.escape(code)}\]", p.get("name", "")):
            return p
    # underscore/dash flip
    alt = code.replace("-", "_") if "-" in code else code.replace("_", "-")
    for p in all_projects:
        if re.search(rf"\[{re.escape(alt)}\]", p.get("name", "")):
            return p
    # name-substring fallback (lower)
    lower_name = name.lower()
    for p in all_projects:
        if lower_name in p.get("name", "").lower():
            return p
    return None


def _apply_sow_terms(state: ProjectState, terms: dict) -> None:
    """Merge Haiku-extracted SOW/proposal terms into a ProjectState.

    SOW data wins over Asana custom fields — the SOW is the authoritative
    contract document, Asana fields are human-entered and often stale. When
    SOW gives None we keep Asana's value.
    """
    approved = terms.get("budget_approved")
    if approved is not None:
        state.budget.approved = float(approved)
        state.budget.approved_source = "sow_drive"

    line_items = terms.get("line_items") or []
    state.budget.line_items = [
        BudgetLineItem(
            category=str(li.get("category", "Other")),
            amount=float(li.get("amount") or 0),
            description=li.get("description"),
        )
        for li in line_items
        if li.get("amount") is not None
    ]

    ctype = terms.get("contract_type")
    if ctype in ("fixed_price", "cost_reimbursable", "t_and_m"):
        state.contract.type = ctype  # type: ignore[assignment]
    if terms.get("contract_number"):
        state.contract.number = terms["contract_number"]
    if terms.get("start_date"):
        state.contract.start_date = terms["start_date"]
    if terms.get("end_date"):
        state.contract.end_date = terms["end_date"]
    if terms.get("payment_cadence"):
        state.contract.payment_cadence = terms["payment_cadence"]

    for doc in terms.get("_source_docs") or []:
        if doc not in state.contract.documents:
            state.contract.documents.append(f"drive://{doc}")


def build_project_state(
    code: str,
    name: str,
    category: Category,
    all_asana_projects: list[dict],
    toggl_hours: dict[str, float],
    drive_user_email: Optional[str] = None,
) -> ProjectState:
    print(f"  [{code}] {name} ({category})")

    # Base record
    state = ProjectState(
        project_code=code,
        category=category,
        name=name,
    )

    asana = _find_asana_project(all_asana_projects, code, name)
    now_iso = datetime.utcnow().isoformat(timespec="seconds") + "Z"
    state.last_full_rebuild = now_iso

    # --- Asana ---
    if asana:
        state.asana_gid = asana.get("gid")
        try:
            detail = _asana_project_detail(asana["gid"])
        except Exception as e:
            print(f"    [WARN] Asana detail fetch failed: {e}")
            detail = asana

        cf = _custom_field_map(detail)

        if category in ("contract", "customer_support", "bd"):
            state.customer = _extract_customer(cf)
            state.contract = _extract_contract(cf, detail)

        # Milestones from tasks (only for categories with meaningful milestones)
        if category in ("contract", "irad", "bd", "customer_support"):
            try:
                ms = _asana_project_milestones(asana["gid"])
                state.milestones = _format_milestones(ms)
            except Exception as e:
                print(f"    [WARN] Milestone fetch failed: {e}")

        # Team
        try:
            for n in _asana_project_assignees(asana["gid"]):
                state.team.append(TeamMember(name=n))
        except Exception:
            pass

        # Budget approved from Asana custom fields (fallback when SOW missing)
        approved = _parse_money(
            cf.get("Total Funding to Black Swift") or cf.get("Total Budget") or ""
        )
        if approved:
            state.budget.approved = approved
            state.budget.approved_source = "asana_custom_field"
        else:
            state.budget.approved_source = "SOW_pending"
    else:
        state.budget.approved_source = "no_asana_project"

    # --- Drive SOW/proposal extraction (wins over Asana fields) ---
    if category in ("contract", "customer_support", "bd") and drive_user_email:
        try:
            terms = sow_parser.extract_for_project(drive_user_email, code)
            if terms:
                _apply_sow_terms(state, terms)
        except Exception as e:
            print(f"    [WARN] SOW parse failed: {e}")

    # --- QBO by-class ---
    qbo = _load_qbo_by_class(code)
    if qbo:
        other_qbo = float(qbo["totals"]["expenses"])
        state.budget.spent.other_qbo = SpendBreakdown(
            amount=round(other_qbo, 2),
            source="QBO by-class (bills + purchases + POs)",
            confidence="exact",
            last_updated=qbo.get("period", {}).get("end"),
        )

    # --- Toggl → labor $ ---
    hours = _match_toggl_hours_to_code(toggl_hours, code)
    if hours > 0:
        state.budget.spent.labor = SpendBreakdown(
            amount=round(hours * LABOR_RATE_USD_PER_HR, 2),
            source=f"toggl × ${LABOR_RATE_USD_PER_HR}/hr placeholder",
            confidence="placeholder",
            last_updated=date.today().isoformat(),
        )

    # --- purchases from purchasing@ emails (week 2) ---
    purch_spent, purch_committed = _load_purchase_totals(code)
    if purch_spent or purch_committed:
        state.budget.spent.purchases = SpendBreakdown(
            amount=purch_spent,
            source=f"purchasing@ emails (older than {COMMITTED_WINDOW_DAYS} days)",
            confidence="estimate",
            last_updated=date.today().isoformat(),
        )
        state.budget.committed = purch_committed
    else:
        state.budget.spent.purchases = SpendBreakdown(
            amount=0.0,
            source="purchasing@ emails (no records matched this project)",
            confidence="placeholder",
        )

    # Totals
    state.budget.spent.total = round(
        state.budget.spent.labor.amount
        + state.budget.spent.purchases.amount
        + state.budget.spent.other_qbo.amount,
        2,
    )
    if state.budget.approved is not None:
        state.budget.remaining = round(
            state.budget.approved - state.budget.spent.total - state.budget.committed, 2
        )

    state.budget.last_reconciled = now_iso

    # --- Corrections overlay ---
    state.overrides = _fetch_project_corrections(code, name)

    # Status inference
    status, notes = _infer_status(
        asana if asana else {}, state.overrides
    )
    state.status = status  # type: ignore[assignment]
    state.status_notes = notes

    return state


def scan_all(
    filter_categories: Optional[list[str]] = None,
    skip_drive: bool = False,
) -> list[Path]:
    """Build project-state JSON for every entry in categories.md.

    Args:
        filter_categories: if provided, only process projects whose category
            is in this list (e.g. ["contract"] for week-1 rollout).
        skip_drive: disable SOW parsing (useful for fast iteration).
    """
    entries = load_categories()
    if filter_categories:
        entries = [e for e in entries if e[2] in filter_categories]
    if not entries:
        print("No projects to scan")
        return []

    print(f"Fetching Asana project list...")
    ws = asana_get_workspaces()
    if not ws:
        print("No Asana workspace found")
        return []
    all_projects = asana_get_projects(ws[0]["gid"], include_archived=True)
    print(f"  {len(all_projects)} Asana projects")

    print(f"Fetching Toggl hours (last {TOGGL_LOOKBACK_MONTHS} months)...")
    toggl_hours = _toggl_hours_by_project()
    print(f"  {len(toggl_hours)} Toggl projects with hours")

    drive_email = None
    if not skip_drive:
        drive_email = (
            os.environ.get("GOOGLE_ADMIN_EMAIL")
            or "elstonj@blackswifttech.com"  # matches daily_research default
        )
        print(f"  SOW parsing via {drive_email}")

    PROJECT_STATE_DIR.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for code, name, category in entries:
        try:
            state = build_project_state(
                code, name, category, all_projects, toggl_hours,
                drive_user_email=drive_email,
            )
            path = save_project_state(state)
            written.append(path)
        except Exception as e:
            print(f"  [ERROR] {code}: {e}")

    update_scan_timestamp("project_state")
    print(f"Wrote {len(written)} project-state files → {PROJECT_STATE_DIR}")
    return written
