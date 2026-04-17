#!/usr/bin/env python3
"""Dry-run the daily briefing pipeline and print the task list to stdout.

Runs the full synthesis end-to-end using real Asana/Toggl/Google/Slack reads,
but intercepts every Slack *write* — nothing is posted to #operations, no
DEBUG/FEEDBACK/SNAPSHOT entries are written to the knowledge channel.

Usage:
    python test_pipeline.py               # print team summary + per-user sections
    python test_pipeline.py --verbose     # also show writes that were suppressed
    python test_pipeline.py --full        # also show the raw Claude output
"""

import argparse
import os
import sys


class DryRunSlackClient:
    """Wraps WebClient so reads pass through but chat_postMessage is a no-op."""

    def __init__(self, real_client, knowledge_channel, daily_channel, verbose=False):
        self._real = real_client
        self._knowledge_channel = knowledge_channel
        self._daily_channel = daily_channel
        self._verbose = verbose
        self.suppressed = []  # list of (channel, text)

    def chat_postMessage(self, channel=None, text="", **kwargs):
        self.suppressed.append((channel, text))
        if self._verbose:
            label = "knowledge" if channel == self._knowledge_channel else (
                "daily" if channel == self._daily_channel else str(channel)
            )
            preview = (text or "")[:500].replace("\n", " ")
            print(f"[suppressed post → {label}] {preview}", file=sys.stderr)
        return {"ok": True, "ts": "0.0", "channel": channel or "", "message": {"text": text}}

    def __getattr__(self, name):
        return getattr(self._real, name)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Show every Slack write that was suppressed.")
    parser.add_argument("--full", action="store_true",
                        help="Also print the raw Claude output (pre-parse).")
    args = parser.parse_args()

    # Load env before importing modules that read environment at import time.
    from dotenv import load_dotenv
    load_dotenv()

    token = os.environ.get("SLACK_BOT_TOKEN")
    if not token:
        print("SLACK_BOT_TOKEN not set in environment.", file=sys.stderr)
        sys.exit(1)

    from slack_sdk import WebClient
    real = WebClient(token=token)
    knowledge_ch = os.environ.get("KNOWLEDGE_CHANNEL", "")
    daily_ch = os.environ.get("DAILY_TASKS_CHANNEL", "")
    client = DryRunSlackClient(real, knowledge_ch, daily_ch, verbose=args.verbose)

    from daily_research import run_daily_pipeline
    from research_cache import get_team_summary, get_per_user_sections, get_full_summary

    print("Running pipeline in dry-run mode (no Slack posts will be sent)...",
          file=sys.stderr)
    full = run_daily_pipeline(client)

    team = get_team_summary()
    per_user = get_per_user_sections()

    bar = "=" * 72
    print(f"\n{bar}\nTEAM SUMMARY\n{bar}")
    print(team or "(empty)")

    print(f"\n{bar}\nPER-USER SECTIONS ({len(per_user)})\n{bar}")
    for slack_id, section in per_user.items():
        print(f"\n--- <@{slack_id}> ---")
        print(section)

    if args.full:
        print(f"\n{bar}\nRAW CLAUDE OUTPUT\n{bar}")
        print(full)

    # Summarize what was suppressed so the user knows the side-effects were skipped.
    kn = sum(1 for c, _ in client.suppressed if c == knowledge_ch)
    dl = sum(1 for c, _ in client.suppressed if c == daily_ch)
    other = len(client.suppressed) - kn - dl
    print(f"\n[dry-run] suppressed {kn} knowledge-channel writes, "
          f"{dl} daily-channel writes, {other} other.", file=sys.stderr)


if __name__ == "__main__":
    main()
