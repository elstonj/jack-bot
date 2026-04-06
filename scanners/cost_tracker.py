"""Project cost tracker — computes actual project costs from Toggl + rates + expenses.

Cross-references:
  - Toggl hours per person per project
  - Labor rates from budget/contract docs (extracted via Claude)
  - Material/equipment purchases from QuickBooks expenses
  - Subcontractor costs from QuickBooks

Produces:
  knowledge/financial/costs/{project_code}.md — per-project cost breakdown
  Updates knowledge/financial/by_project/{code}.md with cost section

Run after toggl, budgets, and quickbooks scanners.
"""

import os
import re
import glob
from pathlib import Path

from .base import (
    KNOWLEDGE_DIR,
    get_claude_client,
    update_scan_timestamp,
    DISTILL_MODEL,
)

COSTS_DIR = KNOWLEDGE_DIR / "financial" / "costs"
FINANCIAL_DIR = KNOWLEDGE_DIR / "financial" / "by_project"
TOGGL_DIR = KNOWLEDGE_DIR / "toggl" / "by_project"
BUDGETS_DIR = KNOWLEDGE_DIR / "budgets"
QB_DIR = KNOWLEDGE_DIR / "quickbooks" / "by_project"
PROJECTS_DIR = KNOWLEDGE_DIR / "projects"

MAX_CONTEXT = 60_000


def _read_file(path, max_chars=None):
    try:
        text = Path(path).read_text()
        return text[:max_chars] if max_chars else text
    except Exception:
        return ""


def _find_toggl_for_project(code):
    """Find Toggl time tracking file for a project code."""
    if not TOGGL_DIR.exists():
        return ""
    code_dash = code.replace("_", "-")
    for f in TOGGL_DIR.glob("*.md"):
        if code_dash in f.name or code in f.name:
            return _read_file(f, max_chars=5000)
    return ""


def _find_budget_for_project(code):
    """Find budget file for a project code."""
    if not BUDGETS_DIR.exists():
        return ""
    code_underscore = code.replace("-", "_")
    path = BUDGETS_DIR / f"project_{code_underscore}.md"
    if path.exists():
        return _read_file(path, max_chars=8000)
    # Try variations
    for f in BUDGETS_DIR.glob(f"*{code_underscore}*"):
        return _read_file(f, max_chars=8000)
    return ""


def _find_qb_expenses_for_project(code):
    """Search QuickBooks files for expense transactions related to this project."""
    if not QB_DIR.exists():
        return ""
    # QB files are grouped by category (commercial, government, etc.)
    # Search all for the project code
    code_dash = code.replace("_", "-")
    snippets = []
    for f in QB_DIR.glob("*.md"):
        content = _read_file(f, max_chars=10000)
        if code_dash in content or f"[{code_dash}]" in content or code in content:
            # Extract just the relevant sections
            lines = content.split("\n")
            relevant = []
            capture = False
            for line in lines:
                if code_dash in line.lower() or code in line.lower():
                    capture = True
                if capture:
                    relevant.append(line)
                    if len(relevant) > 30:
                        break
                if capture and line.strip() == "" and len(relevant) > 5:
                    capture = False
            if relevant:
                snippets.append(f"From {f.name}:\n" + "\n".join(relevant))
    return "\n\n".join(snippets) if snippets else ""


def _find_project_registry(code):
    """Get project registry entry."""
    if not PROJECTS_DIR.exists():
        return ""
    path = PROJECTS_DIR / f"{code}.md"
    if path.exists():
        return _read_file(path, max_chars=3000)
    return ""


COST_PROMPT = """\
You are computing actual project costs for a Black Swift Technologies (BST) project.

Given: Toggl time tracking data (hours per person), budget documents (labor rates, \
indirect rates), QuickBooks transactions (expenses, purchases), and project metadata, \
produce a structured cost breakdown.

Compute:
1. **Direct Labor**: For each person, multiply their hours by their hourly rate. \
   If exact rates aren't in the budget, use these BST defaults: \
   Principal (CEO/CTO): $105/hr, Senior Engineer: $90/hr, Engineer: $75/hr, \
   Technician/Admin: $55/hr, Intern: $35/hr.
2. **Indirect Costs**: Apply fringe (29.28%) + overhead (46.67%) to direct labor \
   if the project is a government contract. Skip for IRAD/commercial unless rates are specified.
3. **Fully Loaded Labor**: Direct labor + indirects
4. **Materials & Equipment**: From QuickBooks expenses/purchases
5. **Subcontractor Costs**: From QuickBooks if present
6. **Total Actual Cost**: Sum of all above

Output clean markdown with:
- Summary table: budget vs actual cost vs remaining
- Labor breakdown by person (hours, rate, cost)
- Materials/equipment if any
- Subcontractor costs if any
- Burn rate assessment (are we on track?)

Use bullet points, not markdown tables (output is for Slack). Be specific with numbers. \
If data is missing, note what's unavailable and estimate where reasonable."""


def compute_project_costs(project_code, progress_callback=None):
    """Compute costs for a single project."""
    sections = []

    # Gather all available data
    toggl = _find_toggl_for_project(project_code)
    if toggl:
        sections.append(f"=== TOGGL TIME TRACKING ===\n{toggl}")

    budget = _find_budget_for_project(project_code)
    if budget:
        sections.append(f"=== BUDGET DOCUMENT ===\n{budget}")

    qb = _find_qb_expenses_for_project(project_code)
    if qb:
        sections.append(f"=== QUICKBOOKS EXPENSES ===\n{qb}")

    registry = _find_project_registry(project_code)
    if registry:
        sections.append(f"=== PROJECT REGISTRY ===\n{registry}")

    # Also include existing financial summary for revenue context
    fin_path = FINANCIAL_DIR / f"{project_code}.md"
    if fin_path.exists():
        sections.append(f"=== EXISTING FINANCIAL SUMMARY (revenue side) ===\n{_read_file(fin_path, max_chars=4000)}")

    if not sections:
        return None

    context = "\n\n".join(sections)
    if len(context) > MAX_CONTEXT:
        context = context[:MAX_CONTEXT]

    client = get_claude_client()
    response = client.messages.create(
        model=DISTILL_MODEL,
        max_tokens=2000,
        system=COST_PROMPT,
        messages=[{"role": "user", "content": f"Project: {project_code}\n\n{context}"}],
    )

    return response.content[0].text


def scan(progress_callback=None):
    """Compute costs for all projects that have Toggl data."""
    COSTS_DIR.mkdir(parents=True, exist_ok=True)

    if not TOGGL_DIR.exists():
        print("No Toggl project data available. Run toggl scanner first.")
        return []

    # Find all projects with time tracking data
    results = []
    toggl_files = sorted(TOGGL_DIR.glob("*.md"))
    print(f"Found {len(toggl_files)} projects with time tracking data")

    for i, toggl_file in enumerate(toggl_files):
        # Extract project code from filename like "001-04_s0_vtol_irad.md"
        fname = toggl_file.stem
        code_match = re.match(r"(\d{3}-\d{1,2})", fname)
        if not code_match:
            continue
        code = code_match.group(1).replace("-", "_")

        if progress_callback:
            progress_callback(f"Computing costs for {code} ({i+1}/{len(toggl_files)})...")
        print(f"  [{i+1}/{len(toggl_files)}] {code}...")

        try:
            cost_text = compute_project_costs(code)
            if cost_text:
                output_path = COSTS_DIR / f"{code}.md"
                output_path.write_text(f"# Project {code} — Cost Breakdown\n\n{cost_text}")
                results.append((code, output_path))
        except Exception as e:
            print(f"    Error: {e}")
            continue

    update_scan_timestamp("cost_tracker")
    print(f"Cost tracking complete: {len(results)} projects analyzed")
    return results
