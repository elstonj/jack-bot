#!/usr/bin/env python3
"""Dry-run the commercial-sales / support digest end-to-end.

Reads pre-scanned knowledge/commercial_sales/ records and prints the rendered
Slack post to stdout — nothing is sent to #commercial-sales.

With --scan, runs the scanner first (live Gmail + Asana + Slack reads). This
calls Anthropic Haiku once per Asana task and per support thread, so it costs
real API tokens; without --scan the script is read-only and free.

Usage:
    python test_commercial_sales.py               # render from existing JSON
    python test_commercial_sales.py --scan        # refresh records, then render
    python test_commercial_sales.py --raw         # also print raw JSON records
"""

import argparse
import os
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--scan", action="store_true",
                        help="Run the commercial_sales scanner before rendering.")
    parser.add_argument("--raw", action="store_true",
                        help="Also print the raw JSON Build/SupportCase records.")
    args = parser.parse_args()

    # Load env before importing modules that read environment at import time
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

    if args.scan:
        from scanners.commercial_sales_scanner import scan_all
        slack_client = None
        try:
            from slack_sdk import WebClient
            if os.environ.get("SLACK_BOT_TOKEN"):
                slack_client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
        except Exception:
            pass
        print("Running scanner (mode=incremental)...\n", file=sys.stderr)
        result = scan_all(mode="incremental", slack_client=slack_client)
        print(f"\nScanner result: {result}\n", file=sys.stderr)

    from commercial_sales import load_builds, load_support_cases, render_digest

    builds = load_builds()
    cases = load_support_cases()

    print(f"# Loaded {len(builds)} builds, {len(cases)} support cases", file=sys.stderr)

    if args.raw:
        import json
        for b in builds:
            print(f"\n=== BUILD {b.asana_gid} ({b.customer}) ===", file=sys.stderr)
            print(json.dumps(b.to_dict(), indent=2, default=str), file=sys.stderr)
        for c in cases:
            print(f"\n=== CASE {c.case_id} ({c.customer}) ===", file=sys.stderr)
            print(json.dumps(c.to_dict(), indent=2, default=str), file=sys.stderr)

    # Build a name → slack_id map so the rendered output shows mentions
    name_to_slack = {}
    try:
        from slack_sdk import WebClient
        from user_map import build_user_map
        client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
        users = build_user_map(client)
        for u in users:
            if u.get("name") and u.get("slack_user_id"):
                name_to_slack[u["name"]] = u["slack_user_id"]
                first = u["name"].split()[0] if u["name"] else ""
                if first and first not in name_to_slack:
                    name_to_slack[first] = u["slack_user_id"]
    except Exception as e:
        print(f"# (Couldn't build user_map for mentions: {e})", file=sys.stderr)

    print(render_digest(builds, cases, name_to_slack=name_to_slack))


if __name__ == "__main__":
    main()
