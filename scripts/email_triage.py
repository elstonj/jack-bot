#!/usr/bin/env python3
"""Run email triage by hand, or render the daily recap.

    python scripts/email_triage.py --mode dryrun --lookback 2 --limit 50
    python scripts/email_triage.py --summary --print     # render, don't insert
    python scripts/email_triage.py --summary             # insert recap into Jack's inbox

`--mode` defaults to env JACKBOT_EMAIL_TRIAGE (off unless set), so a bare
invocation does nothing. dryrun classifies and logs without touching Gmail;
live forwards, labels and moves mail for real.
"""

import argparse
import json
import os
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_DIR))

from dotenv import load_dotenv  # noqa: E402

load_dotenv(PROJECT_DIR / ".env")

from email_triage import runner, summary  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--mode", choices=runner.MODES, default=None)
    ap.add_argument("--lookback", type=int, default=2, help="days")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--summary", action="store_true", help="daily recap instead of a triage run")
    ap.add_argument("--hours", type=int, default=24, help="recap window")
    ap.add_argument("--print", dest="print_only", action="store_true",
                    help="with --summary: print the recap, don't insert it")
    ap.add_argument("--log", help="action log path (overrides EMAIL_TRIAGE_LOG)")
    args = ap.parse_args()

    if args.log:
        os.environ["EMAIL_TRIAGE_LOG"] = args.log

    if args.summary:
        (subject, _html, text), records = summary.build_summary(args.hours)
        if args.print_only:
            print(subject)
            print("=" * len(subject))
            print(text)
            return
        msg_id = summary.send_daily_summary(args.hours, force=True)
        print(f"inserted {msg_id}: {subject}" if msg_id else "nothing to summarize")
        return

    mode = args.mode or runner.current_mode()
    if mode == "off":
        print("mode is off (set --mode or JACKBOT_EMAIL_TRIAGE)")
        return
    records = runner.run_triage(mode=mode, lookback_days=args.lookback, limit=args.limit)
    for r in records:
        dest = f" -> {', '.join(r['forward_to'])}" if r.get("forward_to") else ""
        print(f"{r['action']:<13} {r['subject'][:70]!r}{dest}")
        print(f"              {r.get('reason', '')}"
              + (f"  [{'; '.join(r['guard_notes'])}]" if r.get("guard_notes") else "")
              + (f"  ERROR {r['error']}" if r.get("error") else ""))
    counts = {}
    for r in records:
        counts[r["action"]] = counts.get(r["action"], 0) + 1
    print(json.dumps({"mode": mode, "log": runner.log_path(), **counts}))


if __name__ == "__main__":
    main()
