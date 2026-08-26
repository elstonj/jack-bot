# systemd user timers

These replaced the crontab entries on 2026-08-26.

## Why

The nightly scan ran under `cron` at 02:03 — a time the laptop is asleep. `cron`
silently skips runs it misses, so the scan simply stopped after 2026-08-04 and
nobody noticed for three weeks while every downstream feature kept answering
from stale knowledge files.

`Persistent=true` fixes that: systemd records the last run and fires as soon as
possible after the machine wakes, turning a missed window into a late run
instead of no run.

The digest was separately broken — its crontab line pointed at `.venv/bin/python`,
which doesn't exist in this repo (it's `venv/`), so it had been failing with
`not found` since at least Aug 4. The unit uses the correct absolute path.

## Install

```bash
cp scripts/systemd/*.service scripts/systemd/*.timer ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now jackbot-scan.timer jackbot-digest.timer
```

Enabling `jackbot-scan.timer` with a missed window will start a full scan
immediately (~20-40 min, ending in a `git push` that redeploys Railway). To
enable without triggering that, seed the stamp first:

```bash
mkdir -p ~/.local/share/systemd/timers
touch ~/.local/share/systemd/timers/stamp-jackbot-scan.timer
```

## Operate

```bash
systemctl --user list-timers 'jackbot-*'      # next/last run
systemctl --user start jackbot-scan.service   # run a scan now
journalctl --user -u jackbot-scan.service -f  # follow output
```

## Note on linger

`Linger=no` for this user, so these timers run only while a login session is
active. That's fine for a daily-driver laptop — it wakes with the session
intact and the catch-up fires. If the machine ever needs to run these while
logged out, enable it (requires root):

```bash
sudo loginctl enable-linger elstonj
```

Neither timer can wake a sleeping machine; that needs `WakeSystem=true` on a
system-level timer. Catch-up-on-wake is the intended behavior here.

## Absence alarm

A scan that never runs can't report its own failure, so `scan_freshness.py`
ages the newest timestamp in `knowledge/.scan_state.json` and warns past 48h.
It's checked in two places: `scripts/daily_digest.py` (local) and
`daily_research.py` (on Railway, which is always up and therefore fires even if
this laptop never wakes).
