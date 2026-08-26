"""Detect a knowledge scan that has silently stopped running.

The nightly scan's only alarm was a `[BUG]` entry posted when a run *fails*. A
run that never happens reports nothing, so when the scan stopped after
2026-08-04 the knowledge files went three weeks stale while every downstream
feature — briefings, Q&A, the commercial-sales digest — kept answering
confidently from data nobody was updating. Absence needs its own alarm.

`knowledge/.scan_state.json` holds an ISO timestamp per source, written at the
end of each successful scan, so the newest value is the last time *anything*
scanned. That's what we age.
"""

import json
import os
from datetime import datetime
from pathlib import Path

STATE_PATH = Path(__file__).parent / "knowledge" / ".scan_state.json"

# A daily scan that hasn't run in two days has missed at least one window and
# is no longer just "late". Weekend-tolerant without hiding a real stall.
STALE_AFTER_HOURS = 48


def last_scan_time(path=None):
    """Newest per-source timestamp in the scan state file, or None."""
    p = Path(path) if path else STATE_PATH
    try:
        data = json.loads(p.read_text())
    except (OSError, ValueError):
        return None
    newest = None
    for value in (data or {}).values():
        if not isinstance(value, str):
            continue
        try:
            ts = datetime.fromisoformat(value)
        except ValueError:
            continue
        if newest is None or ts > newest:
            newest = ts
    return newest


def source_ages(path=None, now=None):
    """{source: age_in_hours} for every readable timestamp in the state file."""
    p = Path(path) if path else STATE_PATH
    try:
        data = json.loads(p.read_text())
    except (OSError, ValueError):
        return {}
    now = now or datetime.now()
    ages = {}
    for source, value in (data or {}).items():
        if not isinstance(value, str):
            continue
        try:
            ts = datetime.fromisoformat(value)
        except ValueError:
            continue
        # Timestamps are written naive-local by the scanners; compare like for like.
        if ts.tzinfo is not None:
            ts = ts.replace(tzinfo=None)
        ages[source] = (now - ts).total_seconds() / 3600.0
    return ages


def scan_age_hours(path=None, now=None):
    """Age of the STALEST source, or None if unknown.

    Deliberately the oldest and not the newest. `scan.py all` runs the sources
    in sequence, so a mid-run abort leaves the earlier ones current and every
    later one untouched — exactly what happened on 2026-08-26, when a DNS blip
    killed the run at Asana distillation and 13 of 16 sources never executed.
    Aging the newest timestamp reported "fresh" while most of the knowledge base
    was three weeks old. A partial scan has to read as stale, because the
    briefing is only as good as its oldest input.
    """
    ages = source_ages(path, now)
    if not ages:
        return None
    return max(ages.values())


def staleness_warning(path=None, now=None, threshold_hours=None):
    """Return a Slack-ready warning if the scan is overdue, else None."""
    threshold = threshold_hours if threshold_hours is not None else STALE_AFTER_HOURS
    age = scan_age_hours(path, now)

    if age is None:
        return (
            ":rotating_light: *Knowledge scan state unreadable* — "
            f"`{STATE_PATH.name}` is missing or corrupt, so I can't tell when the "
            "knowledge files were last refreshed. Everything I answer from may be stale."
        )
    if age < threshold:
        return None

    ages = source_ages(path, now)
    stale = sorted(
        ((s, a) for s, a in ages.items() if a >= threshold),
        key=lambda kv: kv[1], reverse=True,
    )
    fresh_count = len(ages) - len(stale)
    days = age / 24.0

    # Name the stale sources. A partial stall ("13 of 16 sources are three weeks
    # old") is invisible if the message only reports a single overall age.
    shown = ", ".join(f"{s} ({a / 24:.0f}d)" for s, a in stale[:6])
    if len(stale) > 6:
        shown += f", +{len(stale) - 6} more"

    scope = (
        f"{len(stale)} of {len(ages)} sources stale"
        if fresh_count else f"all {len(ages)} sources stale"
    )
    return (
        f":rotating_light: *Knowledge scan is stale — {scope}*, oldest {days:.1f} days.\n"
        f"Stale: {shown}\n"
        f"Briefings, Q&A and the commercial-sales digest answer from these files. "
        f"A partial run counts as stale: `scan.py all` runs sources in sequence, so an "
        f"abort leaves everything after it untouched. "
        f"Check `journalctl --user -u jackbot-scan.service` and `scripts/nightly_scan.log`."
    )


if __name__ == "__main__":  # quick manual check
    age = scan_age_hours()
    print(f"last scan: {last_scan_time()}")
    print(f"age: {age:.1f}h" if age is not None else "age: unknown")
    print(staleness_warning() or "fresh — no warning")
