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


def scan_age_hours(path=None, now=None):
    """Hours since the last successful scan, or None if unknown."""
    last = last_scan_time(path)
    if last is None:
        return None
    now = now or datetime.now()
    # Timestamps are written naive-local by the scanners; compare like for like.
    if last.tzinfo is not None:
        last = last.replace(tzinfo=None)
    return (now - last).total_seconds() / 3600.0


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

    days = age / 24.0
    last = last_scan_time(path)
    when = last.strftime("%Y-%m-%d %H:%M") if last else "unknown"
    return (
        f":rotating_light: *Knowledge scan is {days:.1f} days stale* — last successful "
        f"run {when}. Briefings, Q&A and the commercial-sales digest are all answering "
        f"from data that old. Check `systemctl --user status jackbot-scan.timer` and "
        f"`scripts/nightly_scan.log`."
    )


if __name__ == "__main__":  # quick manual check
    age = scan_age_hours()
    print(f"last scan: {last_scan_time()}")
    print(f"age: {age:.1f}h" if age is not None else "age: unknown")
    print(staleness_warning() or "fresh — no warning")
