"""Project cost tracker — renders each project's cost picture from structured data.

Sources, all read from disk (run after toggl, qbo_by_class and project_state):
  - knowledge/project_state/{code}.json      — approved budget, spend by source
  - knowledge/quickbooks/by_class/{code}.json — exact QBO revenue / expenses
  - knowledge/toggl/.monthly_totals.json     — hours per person per project

Produces:
  knowledge/financial/costs/{project_code}.md — per-project cost breakdown

Every figure is computed or copied in code and labelled with its source; no
model is involved. The previous version handed Toggl prose, budget docs and
QBO rollups to Haiku and asked it to "estimate where reasonable" with invented
default rates. It produced numbers like "untracked labor value ~$126.5k" for
550-1, counted only the first Toggl file whose name contained the code
("001-1" also matched 001-10..001-16), and truncated Toggl data at 5,000 chars.
Per-person rates aren't available anywhere structured, so labor dollars come
from project_state and keep its placeholder label rather than a guessed rate.
"""

import json
import re
from datetime import date

from project_state import code_to_filename, list_project_states

from .base import KNOWLEDGE_DIR, update_scan_timestamp

COSTS_DIR = KNOWLEDGE_DIR / "financial" / "costs"
QBO_BY_CLASS_DIR = KNOWLEDGE_DIR / "quickbooks" / "by_class"
TOGGL_DIR = KNOWLEDGE_DIR / "toggl"


def _money(x):
    return "unknown" if x is None else f"${x:,.2f}"


def _load_json(path):
    try:
        return json.loads(path.read_text())
    except (FileNotFoundError, ValueError):
        return None


def _code_pattern(code):
    """Matches a project code in a Toggl project name: 550-1 but not 550-10."""
    m = re.match(r"^(\d{3})[-_](\d+)$", code)
    if not m:
        return None
    return re.compile(rf"(?<!\d){m.group(1)}[-_ ]0?{int(m.group(2))}(?!\d)")


def _toggl_hours(code, monthly, names):
    """{person: hours} summed over every Toggl project carrying this code."""
    pat = _code_pattern(code)
    if not pat or not monthly or not names:
        return {}
    pids = {pid for pid, name in names.get("projects", {}).items() if pat.search(name)}
    hours = {}
    for users in monthly.values():
        for uid, pm in users.items():
            secs = sum(s for pid, s in pm.items() if pid in pids)
            if secs:
                person = names.get("users", {}).get(uid, f"User {uid}")
                hours[person] = hours.get(person, 0) + secs / 3600
    return hours


def render_costs(state, qbo, hours, as_of):
    """Markdown cost breakdown for one ProjectState. Pure function."""
    b = state.budget
    s = b.spent
    lines = [
        f"# Project {state.project_code} — Cost Breakdown",
        "",
        f"_Computed in code from structured sources as of {as_of}. No figure here "
        f"was estimated by a model._",
        "",
        f"**{state.name}** ({state.category}, status: {state.status})",
        "",
        "## Budget",
        f"- Approved: {_money(b.approved)} (source: {b.approved_source or 'unknown'})",
    ]
    if state.contract.total_value is not None:
        lines.append(f"- Contract value: {_money(state.contract.total_value)}"
                     f" ({state.contract.type})")
    lines += [
        "",
        f"## Spend to date (project_state, reconciled {b.last_reconciled or 'never'})",
    ]
    for label, part in (("Labor", s.labor), ("Purchases", s.purchases),
                        ("Other QuickBooks", s.other_qbo)):
        lines.append(f"- {label}: {_money(part.amount)} — {part.source} "
                     f"[{part.confidence}, as of {part.last_updated or 'unknown'}]")
    lines.append(f"- Total: {_money(s.total)}")
    if b.remaining is not None:
        lines.append(f"- Remaining against approved: {_money(b.remaining)}")

    if qbo:
        t = qbo.get("totals", {})
        period = qbo.get("period", {})
        lines += ["", f"## QuickBooks ({period.get('start')} to {period.get('end')})",
                  f"- Revenue: {_money(t.get('revenue'))}",
                  f"- Expenses: {_money(t.get('expenses'))}"]
        for cat, amt in list((t.get("by_category") or {}).items())[:8]:
            lines.append(f"  - {cat}: {_money(amt)}")

    if hours:
        total = sum(hours.values())
        lines += ["", f"## Hours by person (Toggl, all time): {total:,.1f} h"]
        for person, h in sorted(hours.items(), key=lambda kv: -kv[1]):
            lines.append(f"- {person}: {h:,.1f} h")

    gaps = []
    if s.labor.confidence == "placeholder":
        gaps.append("Labor dollars use a flat placeholder rate; per-person loaded "
                    "rates are not available, so treat labor cost as approximate.")
    if not qbo:
        gaps.append("No QuickBooks transactions are attributed to this project code.")
    if not hours:
        gaps.append("No Toggl hours are tagged with this project code.")
    if b.approved is None:
        gaps.append("No approved budget on record.")
    if gaps:
        lines += ["", "## Data gaps"] + [f"- {g}" for g in gaps]
    return "\n".join(lines) + "\n"


FINANCIAL_DIR = KNOWLEDGE_DIR / "financial" / "by_project"
_BLOCK_START = "<!-- authoritative-figures:start -->"
_BLOCK_END = "<!-- authoritative-figures:end -->"


def authoritative_block(state, qbo, as_of):
    """Short code-rendered figures block for the top of financial/by_project.

    Those files are model summaries of several sources and disagree with each
    other (301-3's contract value read $1.7M, $747.5k, $879.5k and $969.8k in
    different files). This block gives one sourced, dated answer and Q&A is
    told it wins on conflict.
    """
    b, s = state.budget, state.budget.spent
    lines = [
        _BLOCK_START,
        f"**Authoritative figures** (computed in code as of {as_of}; these win "
        f"over any figure below):",
        f"- Approved budget: {_money(b.approved)} (source: {b.approved_source or 'unknown'})",
        f"- Spent to date: {_money(s.total)} — labor {_money(s.labor.amount)} "
        f"[{s.labor.confidence}], purchases {_money(s.purchases.amount)} "
        f"[{s.purchases.confidence}], other QBO {_money(s.other_qbo.amount)} "
        f"[{s.other_qbo.confidence}]",
    ]
    if b.remaining is not None:
        lines.append(f"- Remaining against approved: {_money(b.remaining)}")
    if qbo:
        t, period = qbo.get("totals", {}), qbo.get("period", {})
        lines.append(f"- QuickBooks {period.get('start')} to {period.get('end')}: "
                     f"revenue {_money(t.get('revenue'))}, expenses {_money(t.get('expenses'))}")
    lines.append(_BLOCK_END)
    return "\n".join(lines)


def _stamp_financial_file(code, block):
    path = FINANCIAL_DIR / f"{code.replace('-', '_')}.md"
    if not path.exists():
        return
    text = path.read_text()
    if _BLOCK_START in text and _BLOCK_END in text:
        before, rest = text.split(_BLOCK_START, 1)
        text = before + rest.split(_BLOCK_END, 1)[1].lstrip("\n")
    path.write_text(block + "\n\n" + text)


def scan(progress_callback=None):
    """Render a cost file for every project that has a project_state record."""
    COSTS_DIR.mkdir(parents=True, exist_ok=True)

    from scanners.toggl_scanner import _load_monthly

    monthly = _load_monthly()
    names = _load_json(TOGGL_DIR / ".names.json") or {}
    if names:
        names = {"users": {int(k): v for k, v in names.get("users", {}).items()},
                 "projects": {int(k): v for k, v in names.get("projects", {}).items()}}
    as_of = date.today().isoformat()

    results = []
    states = [st for st in list_project_states() if _code_pattern(st.project_code)]
    print(f"Rendering costs for {len(states)} projects")
    for i, state in enumerate(states):
        code = state.project_code
        if progress_callback:
            progress_callback(f"Computing costs for {code} ({i+1}/{len(states)})...")
        qbo = _load_json(QBO_BY_CLASS_DIR / f"{code_to_filename(code)}.json")
        hours = _toggl_hours(code, monthly, names)
        output_path = COSTS_DIR / f"{code.replace('-', '_')}.md"
        output_path.write_text(render_costs(state, qbo, hours, as_of))
        _stamp_financial_file(code, authoritative_block(state, qbo, as_of))
        results.append((code, output_path))

    update_scan_timestamp("cost_tracker")
    print(f"Cost tracking complete: {len(results)} projects rendered")
    return results
