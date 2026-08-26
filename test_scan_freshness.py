#!/usr/bin/env python3
"""Offline regression suite for the scan-staleness alarm.

The alarm exists because a scan that never runs posts no failure of its own —
the 2026-08-04 stall went unnoticed for three weeks. These checks pin the
behavior that matters: a stalled scan warns, a healthy one stays quiet, and a
missing or corrupt state file warns rather than silently reading as "fresh".

    python test_scan_freshness.py
"""

import json
import sys
import tempfile
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from scan_freshness import STALE_AFTER_HOURS, scan_age_hours, staleness_warning

FAILURES = []


def check(label, cond):
    if cond:
        print(f"  ok    {label}")
    else:
        print(f"  FAIL  {label}")
        FAILURES.append(label)


def write_state(**sources):
    path = Path(tempfile.mkdtemp()) / ".scan_state.json"
    path.write_text(json.dumps({k: v.isoformat() for k, v in sources.items()}))
    return path


NOW = datetime(2026, 8, 26, 8, 0, 0)


def test_fresh_is_silent():
    print("\nhealthy scan stays quiet")
    p = write_state(asana=NOW - timedelta(hours=6), slack=NOW - timedelta(hours=5))
    check("age is the stalest source", abs(scan_age_hours(p, NOW) - 6) < 0.1)
    check("no warning", staleness_warning(p, NOW) is None)


def test_partial_stall_detected():
    """The 2026-08-26 case: a mid-run abort leaves later sources untouched.

    `scan.py all` died at Asana distillation on a DNS blip. Three sources
    advanced, thirteen never ran. Aging the NEWEST timestamp reported "fresh"
    while most of the knowledge base was three weeks old — so the stalest
    source is what counts.
    """
    print("\npartial stall is not 'fresh'")
    p = write_state(
        asana=NOW - timedelta(minutes=10),          # ran
        cost_tracker=NOW - timedelta(minutes=5),    # ran
        slack=NOW - timedelta(days=22),             # never ran
        quickbooks=NOW - timedelta(days=24),        # never ran
    )
    check("ages the stalest source", abs(scan_age_hours(p, NOW) - 24 * 24) < 1)
    w = staleness_warning(p, NOW)
    check("warns despite fresh sources", w is not None)
    check("counts stale vs total", "2 of 4 sources stale" in (w or ""))
    check("names a stale source", "quickbooks" in (w or ""))
    check("does not name a fresh source", "asana" not in (w or ""))


def test_stalled_scan_warns():
    print("\nstalled scan warns")
    p = write_state(asana=NOW - timedelta(days=21, hours=22))
    w = staleness_warning(p, NOW)
    check("warning produced", w is not None)
    check("states how stale", "21.9 days" in (w or ""))
    check("flags every source stale", "all 1 sources stale" in (w or ""))
    check("says what's affected", "Briefings" in (w or ""))


def test_threshold_boundary():
    print("\nthreshold boundary")
    just_under = write_state(a=NOW - timedelta(hours=STALE_AFTER_HOURS - 1))
    just_over = write_state(a=NOW - timedelta(hours=STALE_AFTER_HOURS + 1))
    check(f"quiet at {STALE_AFTER_HOURS - 1}h", staleness_warning(just_under, NOW) is None)
    check(f"warns at {STALE_AFTER_HOURS + 1}h", staleness_warning(just_over, NOW) is not None)


def test_unreadable_state_warns():
    """Silence on a missing file would recreate the original bug."""
    print("\nmissing / corrupt state warns")
    missing = Path(tempfile.mkdtemp()) / "nope.json"
    check("missing file -> age unknown", scan_age_hours(missing, NOW) is None)
    check("missing file -> warns", staleness_warning(missing, NOW) is not None)

    corrupt = Path(tempfile.mkdtemp()) / "bad.json"
    corrupt.write_text("{not json")
    check("corrupt file -> warns", staleness_warning(corrupt, NOW) is not None)

    empty = Path(tempfile.mkdtemp()) / "empty.json"
    empty.write_text("{}")
    check("empty state -> warns", staleness_warning(empty, NOW) is not None)


def test_junk_values_ignored():
    print("\nmalformed entries tolerated")
    p = Path(tempfile.mkdtemp()) / ".scan_state.json"
    p.write_text(json.dumps({
        "asana": (NOW - timedelta(hours=3)).isoformat(),
        "broken": "not-a-timestamp",
        "numeric": 12345,
        "nested": {"a": 1},
    }))
    check("skips junk, uses valid entry", abs(scan_age_hours(p, NOW) - 3) < 0.1)
    check("no warning", staleness_warning(p, NOW) is None)


if __name__ == "__main__":
    test_fresh_is_silent()
    test_partial_stall_detected()
    test_stalled_scan_warns()
    test_threshold_boundary()
    test_unreadable_state_warns()
    test_junk_values_ignored()

    print()
    if FAILURES:
        print(f"{len(FAILURES)} FAILED:")
        for f in FAILURES:
            print(f"  - {f}")
        sys.exit(1)
    print("All scan-freshness checks passed.")
