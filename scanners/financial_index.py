"""Financial index builder — cross-references budget docs, QuickBooks actuals,
and Asana project data to produce per-project financial summaries.

Produces:
  knowledge/financial/by_project/{project_code}.md  — merged per-project financials
  knowledge/financial/overview.md                   — company-wide financial health

This runs AFTER the budget, quickbooks, and asana scanners have completed.
It reads their output knowledge files and synthesizes them.
"""

import glob
import os
import re
import time
from pathlib import Path

from .base import (
    KNOWLEDGE_DIR,
    get_claude_client,
    write_knowledge_file,
    DISTILL_MODEL,
)

FINANCIAL_DIR = KNOWLEDGE_DIR / "financial"
FINANCIAL_PROJECT_DIR = FINANCIAL_DIR / "by_project"

# Project code patterns
PROJECT_CODE_RE = re.compile(r'(\d{3}-\d{1,2})')


def _find_project_codes_in_file(filepath):
    """Extract all project codes mentioned in a knowledge file."""
    try:
        content = Path(filepath).read_text()
        return set(PROJECT_CODE_RE.findall(content))
    except Exception:
        return set()


def _read_file(path, max_chars=None):
    try:
        content = Path(path).read_text()
        if max_chars and len(content) > max_chars:
            return content[:max_chars] + "\n... [truncated]"
        return content
    except Exception:
        return ""


def _collect_all_project_codes():
    """Scan all knowledge sources to build a master list of project codes."""
    codes = set()

    # From Asana project files
    asana_dir = KNOWLEDGE_DIR / "asana" / "projects"
    if asana_dir.exists():
        for f in asana_dir.glob("*.md"):
            # Filenames like 550-1_navy_sbir_magnetometer.md
            match = PROJECT_CODE_RE.search(f.stem.replace("_", "-"))
            if match:
                codes.add(match.group(1))
            # Also check file content
            codes.update(_find_project_codes_in_file(f))

    # From budget files
    budget_dir = KNOWLEDGE_DIR / "budgets"
    if budget_dir.exists():
        for f in budget_dir.glob("project_*.md"):
            # Filenames like project_550_1.md
            stem = f.stem.replace("project_", "")
            # Convert 550_1 back to 550-1
            parts = stem.split("_")
            if len(parts) >= 2:
                code = f"{parts[0]}-{parts[1]}"
                if PROJECT_CODE_RE.match(code):
                    codes.add(code)

    # From QBO files — extract project codes from content
    qbo_dir = KNOWLEDGE_DIR / "quickbooks" / "by_project"
    if qbo_dir.exists():
        for f in qbo_dir.glob("*.md"):
            codes.update(_find_project_codes_in_file(f))

    return sorted(codes)


def _find_asana_file(code):
    """Find the Asana knowledge file for a project code."""
    asana_dir = KNOWLEDGE_DIR / "asana" / "projects"
    if not asana_dir.exists():
        return None
    code_underscore = code.replace("-", "_")
    # Try exact prefix match
    for f in asana_dir.glob("*.md"):
        if f.stem.startswith(code_underscore) or f.stem.startswith(code.replace("-", "")):
            return f
    # Try content match
    for f in asana_dir.glob("*.md"):
        content = _read_file(f, max_chars=500)
        if code in content or f"[{code}]" in content:
            return f
    return None


def _find_budget_file(code):
    """Find the Drive budget knowledge file for a project code."""
    code_underscore = code.replace("-", "_")
    budget_file = KNOWLEDGE_DIR / "budgets" / f"project_{code_underscore}.md"
    if budget_file.exists():
        return budget_file
    return None


def _find_qbo_data(code):
    """Extract QBO data relevant to a specific project code from QBO knowledge files."""
    qbo_dir = KNOWLEDGE_DIR / "quickbooks" / "by_project"
    if not qbo_dir.exists():
        return ""

    relevant_sections = []
    for f in qbo_dir.glob("*.md"):
        content = _read_file(f)
        if code in content or f"[{code}]" in content:
            # Extract lines mentioning this project code
            lines = content.split("\n")
            project_lines = []
            in_relevant_section = False
            for line in lines:
                if code in line or f"[{code}]" in line:
                    in_relevant_section = True
                    project_lines.append(line)
                elif in_relevant_section:
                    if line.startswith("#") or line.startswith("---"):
                        in_relevant_section = False
                    else:
                        project_lines.append(line)

            if project_lines:
                relevant_sections.append(
                    f"Source: {f.name}\n" + "\n".join(project_lines)
                )

    return "\n\n".join(relevant_sections)


def _find_proposal_files(code):
    """Find proposal/report knowledge files mentioning this project code."""
    proposals_dir = KNOWLEDGE_DIR / "proposals"
    if not proposals_dir.exists():
        return []
    matches = []
    for f in proposals_dir.glob("*.md"):
        if f.name == "catalog.md":
            continue
        content = _read_file(f, max_chars=1000)
        if code in content or f"[{code}]" in content:
            matches.append(f)
    return matches


PROJECT_FINANCIAL_PROMPT = """\
You are creating a comprehensive per-project financial summary for a Black Swift Technologies (BST) \
project by merging data from multiple sources:

1. **Asana** — project details, tasks, milestones, deliverables
2. **Drive Budget Docs** — proposed budgets, contract values, CLINs, invoices from documents
3. **QuickBooks Actuals** — real invoices sent, payments received, expenses incurred
4. **Proposals/Reports** — what was proposed, technical scope

Synthesize into this structure:

# Project {code} — Financial Summary

## Project Overview
- Full project name, client/agency, contract type (SBIR Phase I/II, IDIQ, commercial, etc.)
- Period of performance
- Brief description of scope

## Budget Status
| Category | Amount | Source |
|----------|--------|--------|
| **Proposed Budget** | $X | (from proposal/budget docs) |
| **Approved/Contracted** | $X | (from contract docs, CLINs) |
| **Invoiced to Date** | $X | (from QuickBooks) |
| **Payments Received** | $X | (from QuickBooks) |
| **Expenses Incurred** | $X | (from QuickBooks) |
| **Estimated Remaining** | $X | (approved minus invoiced, or approved minus expenses) |

## CLIN / Line Item Breakdown
If CLINs or budget line items are available, show each with: approved amount, invoiced amount, remaining.

## Budget by Cost Category
Compare proposed/approved budget categories against actual spending from QuickBooks:

| Category | Proposed Budget | Actual Spend | Variance | % Used |
|----------|----------------|--------------|----------|--------|
| Direct Labor | $X | $X | $X | X% |
| Subcontractors | $X | $X | $X | X% |
| Equipment | $X | $X | $X | X% |
| Materials & Supplies | $X | $X | $X | X% |
| Travel | $X | $X | $X | X% |
| Indirect Costs | $X | $X | $X | X% |
| Other | $X | $X | $X | X% |
| **TOTAL** | **$X** | **$X** | **$X** | **X%** |

Use "Proposed Budget" from Drive budget docs and "Actual Spend" from QuickBooks account categories. \
If a category has no proposed budget data, show "N/A" for proposed but still show actuals. \
If a category has no QBO data, show "N/A" for actuals.

## Invoice History
List invoices from QuickBooks: number, date, amount, description, payment status.

## Key Deliverables & Milestones
From Asana: upcoming deliverables with dates and financial implications.

## Financial Health Assessment
- Is the project on budget overall and by category?
- Which categories are overspent vs underspent?
- Burn rate vs remaining period of performance
- Any concerns (cost overruns, late payments, approaching budget ceiling)

**IMPORTANT:** Clearly label where each data point comes from (Budget Doc, QuickBooks, Asana, Proposal). \
If data is missing from a source, note it as "Data not available from [source]". \
Never fabricate numbers — only use what's provided."""


OVERVIEW_PROMPT = """\
Create a company-wide financial health overview by synthesizing per-project financial summaries.

# BST Financial Health Overview

## Portfolio Summary
| Metric | Amount |
|--------|--------|
| Total Contracted Value | $X |
| Total Invoiced | $X |
| Total Received | $X |
| Total Expenses | $X |
| Estimated Remaining (all projects) | $X |

## By Project (sorted by remaining budget, lowest first — these need attention)
For each project: code, name, contracted value, invoiced, remaining, health status (Green/Yellow/Red).

## Projects Needing Attention
- Projects where remaining budget is low relative to remaining work
- Projects with outstanding invoices (large AR balances)
- Projects approaching end of period of performance

## Revenue Pipeline
- Upcoming invoiceable milestones from Asana
- Projects with approved but un-invoiced CLINs

## Cash Flow
- Current accounts receivable total
- Recent payment trends

Be factual. Use actual numbers from the data provided."""


def build_index():
    """Build the cross-referenced financial index.

    Reads output from budget, quickbooks, asana, and proposals scanners,
    then synthesizes per-project financial summaries.

    Returns list of (project_code, output_path) tuples.
    """
    print("Building financial index...")

    codes = _collect_all_project_codes()
    print(f"Found {len(codes)} project codes across all sources")

    client = get_claude_client()
    results = []

    for i, code in enumerate(codes):
        print(f"\n[{i + 1}/{len(codes)}] Project {code}")

        # Gather data from all sources
        sections = []

        # Asana
        asana_file = _find_asana_file(code)
        if asana_file:
            content = _read_file(asana_file, max_chars=4000)
            sections.append(f"=== ASANA PROJECT DATA ===\n{content}")
            print(f"  Asana: {asana_file.name}")
        else:
            print(f"  Asana: not found")

        # Drive budget docs
        budget_file = _find_budget_file(code)
        if budget_file:
            content = _read_file(budget_file, max_chars=6000)
            sections.append(f"=== DRIVE BUDGET DOCUMENTS ===\n{content}")
            print(f"  Budget: {budget_file.name}")
        else:
            print(f"  Budget: not found")

        # QuickBooks actuals
        qbo_data = _find_qbo_data(code)
        if qbo_data:
            sections.append(f"=== QUICKBOOKS ACTUALS ===\n{qbo_data}")
            print(f"  QBO: {len(qbo_data)} chars")
        else:
            print(f"  QBO: not found")

        # Proposals/reports
        proposal_files = _find_proposal_files(code)
        if proposal_files:
            prop_content = []
            for pf in proposal_files[:3]:  # cap at 3 to avoid token overflow
                prop_content.append(_read_file(pf, max_chars=2000))
            sections.append(
                f"=== PROPOSALS & REPORTS ===\n" + "\n---\n".join(prop_content)
            )
            print(f"  Proposals: {len(proposal_files)} files")
        else:
            print(f"  Proposals: not found")

        # Skip if we have no financial data at all
        if not budget_file and not qbo_data:
            print(f"  [SKIP] No financial data for {code}")
            continue

        # Synthesize
        raw_input = f"PROJECT CODE: {code}\n\n" + "\n\n".join(sections)

        # Truncate if needed
        if len(raw_input) > 85000:
            raw_input = raw_input[:85000] + "\n\n[TRUNCATED]"

        output_path = FINANCIAL_PROJECT_DIR / f"{code.replace('-', '_')}.md"
        output_path.parent.mkdir(parents=True, exist_ok=True)

        for attempt in range(5):
            try:
                message = client.messages.create(
                    model=DISTILL_MODEL,
                    max_tokens=4000,
                    system=PROJECT_FINANCIAL_PROMPT,
                    messages=[{"role": "user", "content": raw_input}],
                )
                write_knowledge_file(output_path, message.content[0].text)
                results.append((code, output_path))
                break
            except Exception as e:
                if "rate_limit" in str(e).lower():
                    wait = 30 * (attempt + 1)
                    print(f"  Rate limited, waiting {wait}s...")
                    time.sleep(wait)
                else:
                    print(f"  [ERROR] Synthesis failed for {code}: {e}")
                    break

        time.sleep(0.5)  # pace between projects

    # Generate company-wide overview
    if results:
        _generate_overview(results, client)

    return results


def _generate_overview(results, client):
    """Generate company-wide financial health overview."""
    snippets = []
    for code, path in results:
        if path.exists():
            content = _read_file(path, max_chars=800)
            snippets.append(f"### Project {code}\n{content}")

    # Also include QBO summary
    qbo_summary = _read_file(KNOWLEDGE_DIR / "quickbooks" / "summary.md", max_chars=3000)
    if qbo_summary:
        snippets.insert(0, f"### QuickBooks Company Overview\n{qbo_summary}")

    combined = "\n\n".join(snippets)
    if len(combined) > 85000:
        combined = combined[:85000] + "\n\n[TRUNCATED]"

    for attempt in range(5):
        try:
            message = client.messages.create(
                model=DISTILL_MODEL,
                max_tokens=4000,
                system=OVERVIEW_PROMPT,
                messages=[{"role": "user", "content": f"Per-project data:\n\n{combined}"}],
            )
            overview_path = FINANCIAL_DIR / "overview.md"
            write_knowledge_file(overview_path, message.content[0].text)
            print(f"\nFinancial overview written to {overview_path}")
            return
        except Exception as e:
            if "rate_limit" in str(e).lower():
                wait = 30 * (attempt + 1)
                print(f"  Rate limited, waiting {wait}s...")
                time.sleep(wait)
            else:
                print(f"  [WARN] Overview generation failed: {e}")
                return
