"""Offline regression suite for the cost tracker and authoritative figures.

The cost tracker used to hand prose to Haiku with invented default rates and
take the first Toggl file whose name contained the code, so "001-1" also
matched 001-10..001-16. It now renders in code. Needs no credentials.
Run: python test_costs.py
"""

import pathlib
import tempfile

import scanners.cost_tracker as ct
from project_state import ProjectState

FAILURES = []


def check(label, got, want):
    ok = got == want
    print(f"  {'ok  ' if ok else 'FAIL'} {label}")
    if not ok:
        print(f"       got:  {got!r}\n       want: {want!r}")
        FAILURES.append(label)


def state():
    s = ProjectState(project_code="550-1", category="contract", name="NAVY SBIR: Magnetometer")
    s.budget.approved = 242540.0
    s.budget.approved_source = "asana_custom_field"
    s.budget.spent.labor.amount = 1000.0
    s.budget.spent.labor.confidence = "placeholder"
    s.budget.spent.total = 1000.0
    s.budget.remaining = 241540.0
    return s


def test_code_matching():
    print("Toggl hours match the exact project code")
    monthly = {"2026-10": {1: {10: 3600, 11: 7200, 12: 1800}}}
    names = {"users": {1: "Maciej Stachura"},
             "projects": {10: "[001-1] IRAD General", 11: "[001-10] Other IRAD",
                          12: "001_01 legacy name"}}
    check("001-1 excludes 001-10", ct._toggl_hours("001-1", monthly, names),
          {"Maciej Stachura": 1.5})
    check("non-numeric code ignored", ct._toggl_hours("socom-s0-ad", monthly, names), {})


def test_render_labels_placeholders():
    print("render keeps sources and confidence labels")
    md = ct.render_costs(state(), {"period": {"start": "2024-10-23", "end": "2026-10-23"},
                                   "totals": {"revenue": 10.0, "expenses": 5.0,
                                              "by_category": {"Travel": 5.0}}},
                         {"Maciej Stachura": 2.0}, "2026-10-23")
    check("approved with source", "$242,540.00 (source: asana_custom_field)" in md, True)
    check("placeholder labelled", "[placeholder" in md, True)
    check("placeholder gap called out", "flat placeholder rate" in md, True)
    check("no model disclaimer missing", "No figure here was estimated by a model" in md, True)


def test_stamp_is_idempotent():
    print("authoritative block replaces itself instead of stacking")
    with tempfile.TemporaryDirectory() as d:
        ct.FINANCIAL_DIR = pathlib.Path(d)
        path = ct.FINANCIAL_DIR / "550_1.md"
        path.write_text("# 550-1 financials\n\nContract value: $1,700,000\n")
        block = ct.authoritative_block(state(), None, "2026-10-23")
        ct._stamp_financial_file("550-1", block)
        ct._stamp_financial_file("550-1", block)
        text = path.read_text()
        check("one block", text.count(ct._BLOCK_START), 1)
        check("block first", text.startswith(ct._BLOCK_START), True)
        check("original content kept", "Contract value: $1,700,000" in text, True)


if __name__ == "__main__":
    test_code_matching()
    test_render_labels_placeholders()
    test_stamp_is_idempotent()
    if FAILURES:
        raise SystemExit(f"\n{len(FAILURES)} failure(s)")
    print("\nall cost checks passed")
