#!/usr/bin/env python3
"""Knowledge scanner CLI — deep historical data collection and distillation.

Usage:
    python scan.py asana --mode full        # All Asana data, all time
    python scan.py asana --mode 1yr         # Last year only
    python scan.py asana --mode incremental # Since last scan

    python scan.py toggl --mode full
    python scan.py contacts
    python scan.py slack --mode 1yr
    python scan.py email --mode 1yr
    python scan.py drive --mode full

    python scan.py all --mode 1yr           # Scan everything
"""

import argparse
import sys
import os
import time
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

# Load .env if present
env_path = Path(__file__).parent / ".env"
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key and key not in os.environ:
                os.environ[key] = value


AVAILABLE_SOURCES = ["asana", "toggl", "contacts", "slack", "email", "drive", "proposals", "budgets", "quickbooks", "financial", "projects", "enrich-contacts"]


def scan_asana(mode):
    from scanners.asana_scanner import scan_all
    print(f"\n{'='*60}")
    print(f"ASANA SCAN — mode: {mode}")
    print(f"{'='*60}\n")

    start = time.time()
    results = scan_all(mode=mode)
    elapsed = time.time() - start

    print(f"\nAsana scan complete: {len(results)} projects scanned in {elapsed:.0f}s")
    for name, count, path in results:
        print(f"  {name}: {count} tasks → {path.name}")


def scan_toggl(mode):
    from scanners.toggl_scanner import scan_all
    print(f"\n{'='*60}")
    print(f"TOGGL SCAN — mode: {mode}")
    print(f"{'='*60}\n")

    start = time.time()
    results = scan_all(mode=mode)
    elapsed = time.time() - start

    print(f"\nToggl scan complete: {len(results)} files in {elapsed:.0f}s")


def scan_contacts(mode):
    from scanners.contacts_scanner import scan_all
    print(f"\n{'='*60}")
    print(f"CONTACTS SCAN — mode: {mode}")
    print(f"{'='*60}\n")

    start = time.time()
    results = scan_all(mode=mode)
    elapsed = time.time() - start

    print(f"\nContacts scan complete: {len(results)} files in {elapsed:.0f}s")
    for name, count, path in results:
        print(f"  {name}: {count} contacts → {path.name}")


def scan_slack(mode):
    from scanners.slack_scanner import scan_all
    print(f"\n{'='*60}")
    print(f"SLACK SCAN — mode: {mode}")
    print(f"{'='*60}\n")

    start = time.time()
    results = scan_all(mode=mode)
    elapsed = time.time() - start

    print(f"\nSlack scan complete in {elapsed:.0f}s")
    if isinstance(results, list):
        for name, count, path in results:
            print(f"  {name}: {count} messages → {path.name}")


def scan_email(mode):
    from scanners.email_scanner import scan_all
    print(f"\n{'='*60}")
    print(f"EMAIL SCAN — mode: {mode}")
    print(f"{'='*60}\n")

    # Build user list from Asana workspace users (no Slack needed)
    users = None
    try:
        from asana_client import get_workspaces
        import requests
        workspaces = get_workspaces()
        if workspaces:
            wid = workspaces[0]["gid"]
            resp = requests.get(
                f"https://app.asana.com/api/1.0/workspaces/{wid}/users",
                headers={"Authorization": f"Bearer {os.environ['ASANA_ACCESS_TOKEN']}"},
                params={"opt_fields": "name,email"},
                timeout=15,
            )
            resp.raise_for_status()
            excluded = set()
            try:
                import json
                excluded = set(json.loads(os.environ.get("EXCLUDED_USERS", "[]")))
            except Exception:
                pass
            users = [
                {"email": u["email"], "name": u["name"]}
                for u in resp.json()["data"]
                if u.get("email") and u["email"] not in excluded
                and "blackswifttech" in u.get("email", "")
            ]
            print(f"Found {len(users)} BST users from Asana")
    except Exception as e:
        print(f"[WARN] Could not build user list from Asana: {e}")

    start = time.time()
    results = scan_all(mode=mode, users=users)
    elapsed = time.time() - start

    print(f"\nEmail scan complete: {len(results)} files in {elapsed:.0f}s")
    for name, count, path in results:
        print(f"  {name}: {count} emails → {path.name}")


def scan_drive(mode):
    from scanners.drive_scanner import scan_all
    print(f"\n{'='*60}")
    print(f"DRIVE SCAN — mode: {mode}")
    print(f"{'='*60}\n")

    start = time.time()
    results = scan_all(mode=mode)
    elapsed = time.time() - start

    print(f"\nDrive scan complete: {len(results)} files in {elapsed:.0f}s")
    for name, count, path in results:
        print(f"  {name}: {count} files → {path.name}")


def scan_budgets(mode):
    from scanners.budget_scanner import scan_all
    print(f"\n{'='*60}")
    print(f"BUDGET SCAN — mode: {mode}")
    print(f"{'='*60}\n")

    start = time.time()
    results = scan_all(mode=mode)
    elapsed = time.time() - start

    print(f"\nBudget scan complete: {len(results)} projects in {elapsed:.0f}s")
    for code, doc_count, path in results:
        print(f"  {code}: {doc_count} docs → {path.name}")


def scan_quickbooks(mode):
    from scanners.quickbooks_scanner import scan_all
    print(f"\n{'='*60}")
    print(f"QUICKBOOKS SCAN — mode: {mode}")
    print(f"{'='*60}\n")

    start = time.time()
    results = scan_all(mode=mode)
    elapsed = time.time() - start

    print(f"\nQuickBooks scan complete: {len(results)} projects in {elapsed:.0f}s")
    for cls_name, txn_count, path in results:
        print(f"  {cls_name}: {txn_count} transactions → {path.name}")


def scan_financial(mode):
    from scanners.financial_index import build_index
    print(f"\n{'='*60}")
    print(f"FINANCIAL INDEX — cross-referencing all sources")
    print(f"{'='*60}\n")

    start = time.time()
    results = build_index()
    elapsed = time.time() - start

    print(f"\nFinancial index complete: {len(results)} projects in {elapsed:.0f}s")
    for code, path in results:
        print(f"  {code} → {path.name}")


def scan_proposals(mode):
    from scanners.proposals_scanner import scan_all
    print(f"\n{'='*60}")
    print(f"PROPOSALS SCAN — mode: {mode}")
    print(f"{'='*60}\n")

    start = time.time()
    results = scan_all(mode=mode)
    elapsed = time.time() - start

    print(f"\nProposals scan complete: {len(results)} documents in {elapsed:.0f}s")
    for name, char_count, path in results:
        print(f"  {name}: {char_count} chars → {path.name}")


def scan_projects(mode):
    from scanners.project_registry_scanner import scan
    print(f"\n{'='*60}")
    print(f"PROJECT REGISTRY SCAN")
    print(f"{'='*60}\n")

    # Get a Slack client for channel cross-referencing
    slack_client = None
    try:
        from slack_sdk import WebClient
        slack_client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
    except Exception as e:
        print(f"[WARN] No Slack client available, skipping channel matching: {e}")

    start = time.time()
    entries = scan(slack_client=slack_client)
    elapsed = time.time() - start

    print(f"\nProject registry complete: {len(entries)} projects in {elapsed:.0f}s")


def scan_enrich_contacts(mode):
    from scanners.contact_enrichment import enrich
    print(f"\n{'='*60}")
    print(f"CONTACT ENRICHMENT")
    print(f"{'='*60}\n")

    start = time.time()
    enrich()
    elapsed = time.time() - start
    print(f"\nContact enrichment complete in {elapsed:.0f}s")


SCANNERS = {
    "asana": scan_asana,
    "toggl": scan_toggl,
    "contacts": scan_contacts,
    "slack": scan_slack,
    "email": scan_email,
    "drive": scan_drive,
    "proposals": scan_proposals,
    "budgets": scan_budgets,
    "quickbooks": scan_quickbooks,
    "financial": scan_financial,
    "projects": scan_projects,
    "enrich-contacts": scan_enrich_contacts,
}


def main():
    parser = argparse.ArgumentParser(
        description="Knowledge scanner — deep historical data collection and distillation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "source",
        choices=AVAILABLE_SOURCES + ["all"],
        help="Data source to scan (or 'all' for everything)",
    )
    parser.add_argument(
        "--mode",
        choices=["full", "1yr", "incremental"],
        default="full",
        help="Scan mode: full (all time), 1yr (last 365 days), incremental (since last scan). Default: full",
    )

    args = parser.parse_args()

    # Verify required env vars
    required = {"ANTHROPIC_API_KEY": "Claude distillation"}
    source_requirements = {
        "asana": {"ASANA_ACCESS_TOKEN": "Asana API"},
        "toggl": {"TOGGL_API_TOKEN": "Toggl API", "TOGGL_WORKSPACE_ID": "Toggl workspace"},
        "contacts": {"GOOGLE_SERVICE_ACCOUNT_JSON": "Google API"},
        "slack": {"SLACK_BOT_TOKEN": "Slack API"},
        "email": {"GOOGLE_SERVICE_ACCOUNT_JSON": "Google API"},
        "drive": {"GOOGLE_SERVICE_ACCOUNT_JSON": "Google API"},
        "proposals": {"GOOGLE_SERVICE_ACCOUNT_JSON": "Google API"},
        "budgets": {"GOOGLE_SERVICE_ACCOUNT_JSON": "Google API"},
        "quickbooks": {
            "QUICKBOOKS_CLIENT_ID": "QuickBooks OAuth",
            "QUICKBOOKS_CLIENT_SECRET": "QuickBooks OAuth",
            "QUICKBOOKS_REFRESH_TOKEN": "QuickBooks OAuth",
            "QUICKBOOKS_REALM_ID": "QuickBooks company ID",
        },
        "financial": {},  # reads other scanner outputs, no external API needed
        "projects": {"ASANA_ACCESS_TOKEN": "Asana API"},
        "enrich-contacts": {},  # reads existing knowledge files + Claude
    }

    sources = AVAILABLE_SOURCES if args.source == "all" else [args.source]

    for source in sources:
        all_required = {**required, **source_requirements.get(source, {})}
        missing = [k for k in all_required if not os.environ.get(k)]
        if missing:
            print(f"[ERROR] Missing env vars for {source}: {', '.join(missing)}")
            if args.source != "all":
                sys.exit(1)
            continue

        SCANNERS[source](args.mode)

    print("\nDone.")


if __name__ == "__main__":
    main()
