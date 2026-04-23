"""Structured per-project state for Jack Bot.

One JSON file per project at `knowledge/project_state/{code}.json`. This is the
single consolidated record the bot reasons over for budget Q&A, reports, and
(later) invoicing. Populated by `scanners/project_state_scanner.py` from Asana,
QuickBooks (via `scanners/qbo_by_class.py`), Toggl, Drive, and the knowledge
channel corrections overlay.

See CLAUDE.md "Vision & Build Order" — this is phase 1.
"""

from __future__ import annotations

import json
import re
from datetime import date, datetime
from pathlib import Path
from typing import Literal, Optional

from pydantic import BaseModel, Field, ConfigDict


SCHEMA_VERSION = "1.0"

Category = Literal["contract", "irad", "customer_support", "admin", "bd"]
Status = Literal["active", "on_hold", "delayed", "complete", "archived", "unknown"]
MilestoneStatus = Literal["open", "complete", "cancelled", "unknown"]
ContractType = Literal[
    "fixed_price", "cost_reimbursable", "t_and_m", "internal", "unknown"
]


PROJECT_STATE_DIR = Path(__file__).parent / "knowledge" / "project_state"
CATEGORIES_FILE = Path(__file__).parent / "knowledge" / "projects" / "categories.md"


class Contact(BaseModel):
    name: str
    email: Optional[str] = None
    role: Optional[str] = None


class Customer(BaseModel):
    name: str
    type: Optional[str] = None  # government | commercial | academic
    contacts: list[Contact] = Field(default_factory=list)


class Contract(BaseModel):
    type: ContractType = "unknown"
    number: Optional[str] = None
    total_value: Optional[float] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    payment_cadence: Optional[str] = None  # milestone | monthly | net_30 | etc.
    documents: list[str] = Field(default_factory=list)  # drive:// links


class BudgetLineItem(BaseModel):
    category: str
    amount: float
    description: Optional[str] = None
    source_doc: Optional[str] = None


class SpendBreakdown(BaseModel):
    amount: float = 0.0
    source: str = ""
    confidence: Literal["exact", "estimate", "placeholder"] = "estimate"
    last_updated: Optional[str] = None


class BudgetSpent(BaseModel):
    labor: SpendBreakdown = Field(default_factory=lambda: SpendBreakdown(source="toggl × loaded_rate"))
    purchases: SpendBreakdown = Field(default_factory=lambda: SpendBreakdown(source="purchasing@ emails"))
    other_qbo: SpendBreakdown = Field(default_factory=lambda: SpendBreakdown(source="QBO by-class"))
    total: float = 0.0
    by_line_item: dict[str, float] = Field(default_factory=dict)


class Budget(BaseModel):
    approved: Optional[float] = None
    approved_source: Optional[str] = None  # e.g. "SOW_pending" | "drive://..." | "manual"
    line_items: list[BudgetLineItem] = Field(default_factory=list)
    spent: BudgetSpent = Field(default_factory=BudgetSpent)
    committed: float = 0.0
    remaining: Optional[float] = None
    burn_rate_monthly: Optional[float] = None
    last_reconciled: Optional[str] = None


class Milestone(BaseModel):
    name: str
    asana_task_gid: Optional[str] = None
    due_on: Optional[str] = None
    original_due: Optional[str] = None
    status: MilestoneStatus = "unknown"
    invoice_trigger: Optional[float] = None  # $ value released on completion
    evidence: list[str] = Field(default_factory=list)  # slack://, drive://, email links


class Deliverable(BaseModel):
    name: str
    due_on: Optional[str] = None
    submitted_on: Optional[str] = None
    accepted_on: Optional[str] = None
    document: Optional[str] = None  # drive:// link
    acceptance_criteria: Optional[str] = None


class TeamMember(BaseModel):
    name: str
    role: Optional[str] = None
    allocation_pct: Optional[float] = None
    hours_last_30d: Optional[float] = None


class Risk(BaseModel):
    description: str
    impact: Literal["low", "medium", "high"] = "medium"
    owner: Optional[str] = None
    mitigation: Optional[str] = None


class Override(BaseModel):
    """A correction or feedback entry from the knowledge channel that affects this project."""
    source: Literal["CORRECTION", "FEEDBACK"]
    author: str
    date: Optional[str] = None
    text: str


class ProjectState(BaseModel):
    """Canonical structured state for a single BST project.

    Written by scanners/project_state_scanner.py. Read by finances.py, Q&A,
    budget-check flows, daily briefing context, and (later) report composer +
    invoice generator.
    """

    model_config = ConfigDict(extra="forbid")

    schema_version: str = SCHEMA_VERSION
    project_code: str  # e.g. "350-4" or slug like "socom-s0-ad"
    category: Category
    asana_gid: Optional[str] = None
    name: str

    status: Status = "unknown"
    status_notes: Optional[str] = None

    customer: Optional[Customer] = None
    contract: Contract = Field(default_factory=Contract)
    budget: Budget = Field(default_factory=Budget)
    milestones: list[Milestone] = Field(default_factory=list)
    deliverables: list[Deliverable] = Field(default_factory=list)
    team: list[TeamMember] = Field(default_factory=list)
    risks: list[Risk] = Field(default_factory=list)
    overrides: list[Override] = Field(default_factory=list)

    last_full_rebuild: Optional[str] = None
    last_incremental_update: Optional[str] = None


def code_to_filename(code: str) -> str:
    """`[350-4]` / `350-4` / `SOCOM S0-AD` → safe filename stem."""
    code = code.strip().strip("[]").strip()
    if re.match(r"^\d{3}[-_]\d+$", code):
        return code.replace("_", "-")
    # slugify
    slug = re.sub(r"[^\w\-]+", "-", code.lower()).strip("-")
    return slug[:60] or "unknown"


def load_project_state(code: str) -> Optional[ProjectState]:
    path = PROJECT_STATE_DIR / f"{code_to_filename(code)}.json"
    if not path.exists():
        return None
    try:
        return ProjectState.model_validate_json(path.read_text())
    except Exception:
        return None


def save_project_state(state: ProjectState) -> Path:
    PROJECT_STATE_DIR.mkdir(parents=True, exist_ok=True)
    path = PROJECT_STATE_DIR / f"{code_to_filename(state.project_code)}.json"
    path.write_text(state.model_dump_json(indent=2, exclude_none=False))
    return path


def list_project_states() -> list[ProjectState]:
    if not PROJECT_STATE_DIR.exists():
        return []
    out = []
    for path in sorted(PROJECT_STATE_DIR.glob("*.json")):
        try:
            out.append(ProjectState.model_validate_json(path.read_text()))
        except Exception:
            continue
    return out


# ---------------------------------------------------------------------------
# categories.md parser
# ---------------------------------------------------------------------------


_CATEGORY_HEADER = re.compile(r"^##\s+([a-z_]+)\s*$")
_CODE_PREFIX = re.compile(r"^\s*\[(?P<code>[^\]]+)\]\s*(?P<name>.*?)\s*$")


def load_categories(path: Path = CATEGORIES_FILE) -> list[tuple[str, str, Category]]:
    """Parse `knowledge/projects/categories.md` → list of (code, name, category).

    Lines under a `## <category>` header are project entries. Codes in brackets
    like `[350-4]` are preferred; bare names (e.g. `SOCOM S0-AD`) get slugified.
    """
    if not path.exists():
        return []

    valid_categories = {"contract", "irad", "customer_support", "admin", "bd"}
    out: list[tuple[str, str, Category]] = []
    current: Optional[Category] = None

    for raw in path.read_text().splitlines():
        line = raw.rstrip()
        if not line or line.lstrip().startswith("# "):  # blank or top H1
            continue
        m = _CATEGORY_HEADER.match(line)
        if m:
            cat = m.group(1)
            if cat in valid_categories:
                current = cat  # type: ignore[assignment]
            else:
                current = None
            continue
        if not current or line.lstrip().startswith("#"):
            continue

        cm = _CODE_PREFIX.match(line)
        if cm:
            code = cm.group("code").strip()
            name = cm.group("name").strip() or code
        else:
            stripped = line.strip()
            if not stripped:
                continue
            code = stripped  # no bracketed code; the whole line is the identifier
            name = stripped

        out.append((code, name, current))
    return out


if __name__ == "__main__":
    # smoke test
    entries = load_categories()
    print(f"Parsed {len(entries)} entries from categories.md")
    for code, name, cat in entries[:5]:
        print(f"  [{cat}] {code} — {name}")
