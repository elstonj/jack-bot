"""Gmail deep scanner — fetches email metadata and distills into knowledge files.

Produces:
  knowledge/email/{person_name}.md  — per-person email patterns and relationships

Modes:
  full        — all email metadata (up to 500 messages per person)
  1yr         — last 365 days (up to 200 messages per person)
  incremental — since last scan (up to 100 messages per person)

Only fetches metadata (subjects, senders, recipients, dates, labels).
Does NOT fetch email bodies — just patterns from headers.
"""

import os
import re
import time
from datetime import datetime, timedelta

from googleapiclient.discovery import build

from .base import (
    KNOWLEDGE_DIR,
    distill_to_markdown,
    get_last_scan,
    update_scan_timestamp,
)

# Import credential helper from google_client
import sys
from pathlib import Path

# Ensure project root is importable
_project_root = Path(__file__).parent.parent
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

from google_client import _get_credentials

EMAIL_KNOWLEDGE_DIR = KNOWLEDGE_DIR / "email"

# Per-mode message limits
MODE_LIMITS = {
    "full": 500,
    "1yr": 200,
    "incremental": 100,
}

# Rate limiting
MSG_FETCH_DELAY = 0.2   # seconds between individual message fetches
USER_DELAY = 2.0         # seconds between users

# Gmail list page size (max 500)
LIST_PAGE_SIZE = 100

METADATA_HEADERS = ["Subject", "From", "To", "Date"]


def _build_gmail_service(user_email):
    """Build a Gmail API service for the given user."""
    creds = _get_credentials(user_email)
    if not creds:
        return None
    return build("gmail", "v1", credentials=creds, cache_discovery=False)


def _build_query(mode):
    """Build a Gmail search query string for the given scan mode.

    Args:
        mode: 'full', '1yr', or 'incremental'

    Returns:
        Gmail query string, or empty string for full scan.
    """
    if mode == "full":
        return ""
    elif mode == "1yr":
        return "newer_than:365d"
    elif mode == "incremental":
        last = get_last_scan("email")
        if last:
            days = max(1, (datetime.now() - last).days)
            return f"newer_than:{days}d"
        else:
            # No previous scan — fall back to 1yr
            return "newer_than:365d"
    return ""


def _fetch_message_ids(service, query, max_results):
    """Fetch message IDs using Gmail list API with pagination.

    Args:
        service: Gmail API service
        query: Gmail search query
        max_results: Maximum number of message IDs to return

    Returns:
        list of message ID strings
    """
    all_ids = []
    page_token = None

    while len(all_ids) < max_results:
        page_size = min(LIST_PAGE_SIZE, max_results - len(all_ids))
        kwargs = {
            "userId": "me",
            "maxResults": page_size,
        }
        if query:
            kwargs["q"] = query
        if page_token:
            kwargs["pageToken"] = page_token

        result = service.users().messages().list(**kwargs).execute()
        messages = result.get("messages", [])
        all_ids.extend(msg["id"] for msg in messages)

        page_token = result.get("nextPageToken")
        if not page_token or not messages:
            break

    return all_ids[:max_results]


def _fetch_message_metadata(service, msg_id):
    """Fetch metadata for a single message.

    Returns:
        dict with subject, from, to, date, labels or None on error.
    """
    try:
        detail = service.users().messages().get(
            userId="me",
            id=msg_id,
            format="metadata",
            metadataHeaders=METADATA_HEADERS,
        ).execute()

        headers = {
            h["name"]: h["value"]
            for h in detail.get("payload", {}).get("headers", [])
        }

        return {
            "subject": headers.get("Subject", "(no subject)"),
            "from": headers.get("From", ""),
            "to": headers.get("To", ""),
            "date": headers.get("Date", ""),
            "labels": detail.get("labelIds", []),
        }
    except Exception as e:
        print(f"    [WARN] Could not fetch message {msg_id}: {e}")
        return None


def fetch_email_metadata(user_email, mode="full"):
    """Fetch email metadata for a single user.

    Args:
        user_email: Email address to scan
        mode: 'full', '1yr', or 'incremental'

    Returns:
        list of dicts with subject, from, to, date, labels
    """
    service = _build_gmail_service(user_email)
    if not service:
        print(f"  [ERROR] Could not build Gmail service for {user_email}")
        return []

    query = _build_query(mode)
    max_results = MODE_LIMITS.get(mode, 100)

    print(f"  Listing messages (query={query!r}, limit={max_results})...")
    try:
        msg_ids = _fetch_message_ids(service, query, max_results)
    except Exception as e:
        print(f"  [ERROR] Could not list messages for {user_email}: {e}")
        return []

    print(f"  Found {len(msg_ids)} messages, fetching metadata...")
    emails = []
    for i, msg_id in enumerate(msg_ids):
        meta = _fetch_message_metadata(service, msg_id)
        if meta:
            emails.append(meta)

        # Rate limit between fetches
        if i < len(msg_ids) - 1:
            time.sleep(MSG_FETCH_DELAY)

        # Progress logging every 50 messages
        if (i + 1) % 50 == 0:
            print(f"    Fetched {i + 1}/{len(msg_ids)} messages...")

    return emails


def _safe_filename(name):
    """Convert a person name to a safe filename."""
    name = re.sub(r"[^\w\s-]", "", name)
    name = re.sub(r"\s+", "_", name.strip())
    return name[:80].lower()


def _format_email_data(emails, person_name, person_email):
    """Format raw email metadata into text for distillation.

    Args:
        emails: list of email metadata dicts
        person_name: display name
        person_email: email address

    Returns:
        Formatted text string for Claude distillation.
    """
    lines = [
        f"EMAIL METADATA FOR: {person_name} ({person_email})",
        f"Total messages scanned: {len(emails)}",
        "",
    ]

    if not emails:
        lines.append("No emails found in the scanned period.")
        return "\n".join(lines)

    # Sort by date (most recent first) for the raw listing
    lines.append("--- EMAIL HEADERS (most recent first) ---")
    for e in emails:
        label_str = ""
        if e.get("labels"):
            # Filter to meaningful labels (skip internal IDs)
            meaningful = [
                lbl for lbl in e["labels"]
                if not lbl.startswith("Label_") and lbl not in ("CATEGORY_PERSONAL",)
            ]
            if meaningful:
                label_str = f" [{', '.join(meaningful)}]"

        lines.append(
            f"Date: {e['date']}\n"
            f"  From: {e['from']}\n"
            f"  To: {e['to']}\n"
            f"  Subject: {e['subject']}{label_str}"
        )

    return "\n".join(lines)


EMAIL_DISTILL_PROMPT = """\
You are distilling raw email metadata (headers only — no bodies) into a structured \
knowledge file for a team member at Black Swift Technologies (BST).

This file will be used by an AI assistant to understand the person's communication patterns, \
key contacts, and work focus areas. You only have subjects, senders, recipients, and dates — \
extract as much signal as possible from this metadata.

Output a markdown file with these sections:

# {Person Name} — Email Patterns

## Communication Volume
- Total messages scanned and date range covered
- Approximate daily/weekly email volume

## Key Correspondents
- Top senders (who emails them most)
- Top recipients (who they email most)
- Internal vs external breakdown
- Key external contacts/organizations

## Topic Patterns
- Recurring subject line themes (projects, clients, topics)
- Client/vendor names that appear frequently
- Project names or codenames visible in subjects

## Communication Patterns
- Time patterns if visible (e.g. heavy on certain days)
- Mailing lists or group emails they participate in
- Newsletter/automated email patterns (separate from human correspondence)

## Key Relationships
- Who are their closest collaborators (by email frequency)?
- External relationships that appear important (clients, partners, vendors)

## Notable Observations
- Anything unusual or notable about their email patterns
- Key projects or deals visible from subject lines

Be factual. Only report what the metadata shows. Skip empty sections. \
Do NOT speculate about email content — you only have headers."""


def scan_user(user, mode="full"):
    """Scan email for a single user and distill into a knowledge file.

    Args:
        user: dict with at least {"email": str, "name": str}
        mode: 'full', '1yr', or 'incremental'

    Returns:
        (person_name, message_count, output_path) or None on failure.
    """
    email = user["email"]
    name = user["name"]

    print(f"Scanning email for {name} ({email})...")

    # Fetch metadata
    emails = fetch_email_metadata(email, mode=mode)
    if not emails:
        print(f"  No emails found for {name}")
        return None

    # Format for distillation
    raw_text = _format_email_data(emails, name, email)

    # Determine output path
    filename = _safe_filename(name) + ".md"
    output_path = EMAIL_KNOWLEDGE_DIR / filename

    # For very few emails, write a simple summary without Claude
    if len(emails) <= 5:
        simple_lines = [f"# {name} — Email Patterns\n"]
        simple_lines.append(f"Only {len(emails)} emails found in scanned period.\n")
        for e in emails:
            simple_lines.append(f"- {e['date']}: {e['subject']} (from: {e['from']})")
        from .base import write_knowledge_file
        write_knowledge_file(output_path, "\n".join(simple_lines))
        return name, len(emails), output_path

    print(f"  Distilling {name} ({len(emails)} messages)...")
    distill_to_markdown(raw_text, EMAIL_DISTILL_PROMPT, output_path, max_tokens=2000)
    return name, len(emails), output_path


def scan_all(mode="full", users=None, progress_callback=None):
    """Scan email for all specified users.

    Args:
        mode: 'full', '1yr', or 'incremental'
        users: list of dicts with {"email": str, "name": str}.
               If None, falls back to SCAN_EMAILS env var (comma-separated emails,
               names derived from the email local part).
        progress_callback: optional fn(person_name, index, total) called per user

    Returns:
        list of (person_name, message_count, output_path) tuples
    """
    if users is None:
        env_emails = os.environ.get("SCAN_EMAILS", "")
        if not env_emails:
            print(
                "[ERROR] No users provided and SCAN_EMAILS env var not set.\n"
                "Pass users=[{'email': ..., 'name': ...}, ...] or set SCAN_EMAILS=email1@co.com,email2@co.com"
            )
            return []
        users = []
        for addr in env_emails.split(","):
            addr = addr.strip()
            if addr:
                # Derive display name from email local part
                local = addr.split("@")[0]
                name = local.replace(".", " ").replace("_", " ").title()
                users.append({"email": addr, "name": name})

    if not users:
        print("[ERROR] No users to scan")
        return []

    # Handle incremental mode fallback
    if mode == "incremental":
        last = get_last_scan("email")
        if not last:
            print("No previous email scan found — falling back to 1yr mode")
            mode = "1yr"

    print(f"Email scan: mode={mode}, users={len(users)}")

    results = []
    for i, user in enumerate(users):
        if progress_callback:
            progress_callback(user["name"], i, len(users))
        else:
            print(f"\n[{i + 1}/{len(users)}] {user['name']}")

        result = scan_user(user, mode=mode)
        if result:
            results.append(result)

        # Pace between users
        if i < len(users) - 1:
            time.sleep(USER_DELAY)

    update_scan_timestamp("email")
    print(f"\nEmail scan complete: {len(results)}/{len(users)} users scanned successfully")
    return results
