"""Offline regression suite for Toggl totals.

Covers the two ways hours drifted: monthly chunks ended on the 1st of the next
month while the Reports API treats end_date as inclusive, so every month
boundary was counted twice; and each incremental run had the model add a
"since last scan" slice onto the totals in the existing file. Totals are now
cached per month, a refetched month replaces its value, and the sum is done in
code. Needs no credentials. Run: python test_toggl_totals.py
"""

import pathlib
import tempfile
from datetime import date

import scanners.toggl_scanner as ts

FAILURES = []


def check(label, got, want):
    ok = got == want
    print(f"  {'ok  ' if ok else 'FAIL'} {label}")
    if not ok:
        print(f"       got:  {got!r}\n       want: {want!r}")
        FAILURES.append(label)


def test_month_chunks_do_not_overlap():
    print("month chunks are inclusive and never share a day")
    chunks = ts._month_chunks(date(2026, 8, 15), date(2026, 10, 23))
    check("chunks", chunks, [
        (date(2026, 8, 15), date(2026, 8, 31)),
        (date(2026, 9, 1), date(2026, 9, 30)),
        (date(2026, 10, 1), date(2026, 10, 23)),
    ])
    check("december rolls over",
          ts._month_chunks(date(2025, 12, 1), date(2026, 1, 5))[0],
          (date(2025, 12, 1), date(2025, 12, 31)))
    check("single day", ts._month_chunks(date(2026, 10, 1), date(2026, 10, 1)),
          [(date(2026, 10, 1), date(2026, 10, 1))])


def test_refetch_replaces_month():
    print("refetching a month replaces its totals instead of adding")
    hours = {"2026-09": 4.0, "2026-10": 2.0}

    def summary(start, end):
        h = hours[start[:7]]
        return {"groups": [{"id": 7, "sub_groups": [{"id": 550, "seconds": h * 3600}]}]}

    ts._fetch_users = lambda: {7: {"name": "Maciej Stachura", "email": ""}}
    ts._fetch_projects = lambda: {550: {"name": "[550-1]"}}
    ts._fetch_clients = lambda: {}
    ts._fetch_summary_chunk = summary
    ts._fetch_detailed_chunk = lambda s, e: []
    ts.time.sleep = lambda s: None

    with tempfile.TemporaryDirectory() as d:
        ts.MONTHLY_CACHE = pathlib.Path(d) / ".monthly_totals.json"
        ts.NAMES_FILE = pathlib.Path(d) / ".names.json"
        ts._save_monthly({"2026-08": {7: {550: 390.2 * 3600}}})
        run = lambda: ts._collect_all_data(date(2026, 9, 1), date(2026, 10, 23))
        first = run()
        check("all-time sum", first["summary_by_user"][7][550] / 3600, 396.2)
        check("previous totals reported", first["previous_summary_by_user"][7][550] / 3600, 390.2)
        second = run()  # same months again: must not grow
        check("rerun is idempotent", second["summary_by_user"][7][550] / 3600, 396.2)
        hours["2026-10"] = 3.5  # late edit to the current month
        third = run()
        check("late edit replaces month", third["summary_by_user"][7][550] / 3600, 397.7)
        check("cache round-trips None project ids",
              ts._load_monthly() == ts._load_monthly(), True)


if __name__ == "__main__":
    test_month_chunks_do_not_overlap()
    test_refetch_replaces_month()
    if FAILURES:
        raise SystemExit(f"\n{len(FAILURES)} failure(s)")
    print("\nall toggl totals checks passed")
