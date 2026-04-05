"""Google Contacts deep scanner — fetches directory and external contacts with pagination.

Produces:
  knowledge/contacts/directory.md — internal BST team directory
  knowledge/contacts/external.md  — external contacts grouped by organization

Modes:
  Contacts are always a full snapshot (no incremental mode), but the mode
  parameter is accepted for consistency with other scanners.
"""

import os
import time
from collections import defaultdict

from google.oauth2 import service_account
from googleapiclient.discovery import build

from .base import (
    KNOWLEDGE_DIR,
    distill_to_markdown,
    update_scan_timestamp,
    write_knowledge_file,
)

CONTACTS_KNOWLEDGE_DIR = KNOWLEDGE_DIR / "contacts"

DEFAULT_DELEGATE_EMAIL = "jack.elston@blackswifttech.com"

DIRECTORY_READ_MASK = "names,emailAddresses,organizations,phoneNumbers,biographies"
EXTERNAL_READ_MASK = "names,emailAddresses,phoneNumbers"

# Google People API allows up to 1000 per page for directory, 200 for otherContacts
DIRECTORY_PAGE_SIZE = 200
EXTERNAL_PAGE_SIZE = 200

# Be polite with API calls
REQUEST_DELAY = 0.3


def _get_delegate_email(delegate_email=None):
    """Resolve which email to delegate as."""
    if delegate_email:
        return delegate_email
    return os.environ.get("GOOGLE_DELEGATE_EMAIL", DEFAULT_DELEGATE_EMAIL)


def _get_credentials(user_email):
    """Create delegated credentials for a specific user."""
    import json
    import base64

    key_json = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON", "")
    if not key_json:
        return None
    key_data = json.loads(base64.b64decode(key_json))
    scopes = [
        "https://www.googleapis.com/auth/contacts.other.readonly",
        "https://www.googleapis.com/auth/directory.readonly",
    ]
    creds = service_account.Credentials.from_service_account_info(key_data, scopes=scopes)
    return creds.with_subject(user_email)


def _parse_person(person):
    """Extract structured contact info from a People API person resource."""
    names = person.get("names", [])
    emails = person.get("emailAddresses", [])
    orgs = person.get("organizations", [])
    phones = person.get("phoneNumbers", [])
    bios = person.get("biographies", [])

    return {
        "name": names[0].get("displayName", "") if names else "",
        "email": emails[0].get("value", "") if emails else "",
        "organization": orgs[0].get("name", "") if orgs else "",
        "title": orgs[0].get("title", "") if orgs else "",
        "phone": phones[0].get("value", "") if phones else "",
        "bio": bios[0].get("value", "").strip() if bios else "",
    }


def fetch_directory_contacts(delegate_email):
    """Fetch all directory contacts (coworkers) with pagination.

    Returns:
        list[dict]: contacts with name, email, organization, title, phone, bio
    """
    creds = _get_credentials(delegate_email)
    if not creds:
        print("[ERROR] No Google credentials available")
        return []

    service = build("people", "v1", credentials=creds, cache_discovery=False)
    contacts = []
    page_token = None

    while True:
        kwargs = {
            "readMask": DIRECTORY_READ_MASK,
            "sources": ["DIRECTORY_SOURCE_TYPE_DOMAIN_PROFILE"],
            "pageSize": DIRECTORY_PAGE_SIZE,
        }
        if page_token:
            kwargs["pageToken"] = page_token

        results = service.people().listDirectoryPeople(**kwargs).execute()

        for person in results.get("people", []):
            parsed = _parse_person(person)
            if parsed["name"] or parsed["email"]:
                contacts.append(parsed)

        page_token = results.get("nextPageToken")
        if not page_token:
            break
        time.sleep(REQUEST_DELAY)

    return contacts


def fetch_external_contacts(delegate_email):
    """Fetch all 'other contacts' (external) with pagination.

    Returns:
        list[dict]: contacts with name, email, organization, title, phone, bio
    """
    creds = _get_credentials(delegate_email)
    if not creds:
        print("[ERROR] No Google credentials available")
        return []

    service = build("people", "v1", credentials=creds, cache_discovery=False)
    contacts = []
    page_token = None

    while True:
        kwargs = {
            "readMask": EXTERNAL_READ_MASK,
            "pageSize": EXTERNAL_PAGE_SIZE,
        }
        if page_token:
            kwargs["pageToken"] = page_token

        results = service.otherContacts().list(**kwargs).execute()

        for person in results.get("otherContacts", []):
            parsed = _parse_person(person)
            if parsed["name"] or parsed["email"]:
                contacts.append(parsed)

        page_token = results.get("nextPageToken")
        if not page_token:
            break
        time.sleep(REQUEST_DELAY)

    return contacts


def _format_contact_line(contact):
    """Format a single contact as a text line for distillation."""
    parts = [contact["name"] or "(no name)"]
    if contact["email"]:
        parts.append(f"<{contact['email']}>")
    if contact["title"]:
        parts.append(f"— {contact['title']}")
    if contact["organization"]:
        parts.append(f"@ {contact['organization']}")
    if contact["phone"]:
        parts.append(f"| Phone: {contact['phone']}")
    if contact["bio"]:
        # Truncate long bios
        bio = contact["bio"][:200]
        parts.append(f"| Bio: {bio}")
    return " ".join(parts)


def _build_directory_text(contacts):
    """Build raw text from directory contacts for distillation."""
    lines = [
        f"BST INTERNAL DIRECTORY — {len(contacts)} people\n",
    ]
    for c in sorted(contacts, key=lambda x: x.get("name", "")):
        lines.append(_format_contact_line(c))
    return "\n".join(lines)


def _build_external_text(contacts):
    """Build raw text from external contacts, grouped by organization."""
    # Group by organization
    by_org = defaultdict(list)
    for c in contacts:
        org = c.get("organization") or "Unknown / No Organization"
        by_org[org].append(c)

    lines = [
        f"EXTERNAL CONTACTS — {len(contacts)} people across {len(by_org)} organizations\n",
    ]

    # Sort orgs by number of contacts (most first)
    for org, members in sorted(by_org.items(), key=lambda x: -len(x[1])):
        lines.append(f"\n--- {org} ({len(members)} contacts) ---")
        for c in sorted(members, key=lambda x: x.get("name", "")):
            lines.append(f"  {_format_contact_line(c)}")

    return "\n".join(lines)


DIRECTORY_DISTILL_PROMPT = """\
You are distilling a raw Google Workspace directory dump into a structured team directory \
for Black Swift Technologies (BST).

This file will be used by an AI assistant to understand who works at BST, their roles, \
and how to reach them.

Output a markdown file with:

# BST Team Directory

## Team Members
For each person, list:
- **Name** — Title/Role (if available)
  - Email: ...
  - Phone: ... (if available)
  - Notes: any relevant bio info

Group people by department or team if the data makes that possible (e.g., engineering, \
business development, operations). If department is unclear, list alphabetically.

## Summary
- Total headcount
- Key leadership (CEO, VP, directors, etc.)
- Team structure observations

Be factual. Include all contacts — don't drop anyone. Preserve all email addresses and phone numbers exactly."""


EXTERNAL_DISTILL_PROMPT = """\
You are distilling external contacts into a structured relationship file \
for Black Swift Technologies (BST).

This file will be used by an AI assistant to understand BST's external network — clients, \
partners, government contacts, vendors, etc.

Output a markdown file organized by organization:

# External Contacts

## Organizations

For each organization (NASA, USGS, NOAA, universities, etc.), create a section:

### {Organization Name}
- Relationship context (client, partner, government sponsor, vendor, etc.) — infer from \
titles and organization names
- Key contacts:
  - **Name** — Title
    - Email: ...
    - Phone: ... (if available)
    - Bio/notes: ... (if available)

## Summary
- Total external contacts
- Key organizations by contact count
- Notable relationship clusters (e.g., heavy NASA connections, university partnerships)

Group "Unknown / No Organization" contacts at the end. For contacts with no name but an \
email, still include them — the email domain often reveals the organization.

Be factual. Include all contacts. Preserve all email addresses and phone numbers exactly."""


def scan_all(mode="full", progress_callback=None, delegate_email=None):
    """Scan all Google contacts and produce knowledge files.

    Args:
        mode: 'full', '1yr', or 'incremental' (all treated as full for contacts)
        progress_callback: optional fn(step_name, index, total) called per step
        delegate_email: Google user email to impersonate; falls back to
                        GOOGLE_DELEGATE_EMAIL env var or hardcoded default

    Returns:
        list of (source_name, count, output_path) tuples
    """
    email = _get_delegate_email(delegate_email)
    print(f"Scanning Google Contacts as {email}")

    results = []
    steps = ["directory", "external"]

    # Step 1: Directory contacts
    if progress_callback:
        progress_callback("directory contacts", 0, len(steps))
    else:
        print("[1/2] Fetching directory contacts...")

    try:
        directory_contacts = fetch_directory_contacts(email)
        print(f"  Found {len(directory_contacts)} directory contacts")
    except Exception as e:
        print(f"  [ERROR] Failed to fetch directory contacts: {e}")
        directory_contacts = []

    if directory_contacts:
        raw_text = _build_directory_text(directory_contacts)
        output_path = CONTACTS_KNOWLEDGE_DIR / "directory.md"

        # Small directories can skip Claude distillation
        if len(directory_contacts) <= 5:
            lines = [f"# BST Team Directory\n\n{len(directory_contacts)} team members.\n"]
            for c in sorted(directory_contacts, key=lambda x: x.get("name", "")):
                lines.append(f"- **{c['name']}** — {c['title'] or 'No title'}")
                if c["email"]:
                    lines.append(f"  - Email: {c['email']}")
                if c["phone"]:
                    lines.append(f"  - Phone: {c['phone']}")
            write_knowledge_file(output_path, "\n".join(lines))
        else:
            print(f"  Distilling {len(directory_contacts)} directory contacts...")
            distill_to_markdown(raw_text, DIRECTORY_DISTILL_PROMPT, output_path, max_tokens=3000)

        results.append(("directory", len(directory_contacts), output_path))

    # Step 2: External contacts
    if progress_callback:
        progress_callback("external contacts", 1, len(steps))
    else:
        print("[2/2] Fetching external contacts...")

    try:
        external_contacts = fetch_external_contacts(email)
        print(f"  Found {len(external_contacts)} external contacts")
    except Exception as e:
        print(f"  [ERROR] Failed to fetch external contacts: {e}")
        external_contacts = []

    if external_contacts:
        raw_text = _build_external_text(external_contacts)
        output_path = CONTACTS_KNOWLEDGE_DIR / "external.md"

        if len(external_contacts) <= 5:
            lines = [f"# External Contacts\n\n{len(external_contacts)} contacts.\n"]
            for c in sorted(external_contacts, key=lambda x: x.get("name", "")):
                org = c["organization"] or "Unknown"
                lines.append(f"- **{c['name']}** — {c['title'] or 'No title'} @ {org}")
                if c["email"]:
                    lines.append(f"  - Email: {c['email']}")
            write_knowledge_file(output_path, "\n".join(lines))
        else:
            print(f"  Distilling {len(external_contacts)} external contacts...")
            distill_to_markdown(raw_text, EXTERNAL_DISTILL_PROMPT, output_path, max_tokens=4000)

        results.append(("external", len(external_contacts), output_path))

    update_scan_timestamp("contacts")
    total = sum(r[1] for r in results)
    print(f"Contacts scan complete: {total} total contacts")
    return results
