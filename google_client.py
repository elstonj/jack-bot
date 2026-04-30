import os
import json
import base64
from datetime import datetime, timedelta, timezone

from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/calendar.readonly",
    "https://www.googleapis.com/auth/contacts.other.readonly",
    "https://www.googleapis.com/auth/directory.readonly",
]


def _get_credentials(user_email):
    """Create delegated credentials for a specific user."""
    key_json = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON", "")
    if not key_json:
        return None
    key_data = json.loads(base64.b64decode(key_json))
    creds = service_account.Credentials.from_service_account_info(key_data, scopes=SCOPES)
    return creds.with_subject(user_email)


def _get_shared_drive_ids(service):
    """Get IDs of configured shared drives (Sales, Federal Projects)."""
    target_drives = os.environ.get("GOOGLE_SHARED_DRIVES", "Sales,Federal Projects")
    target_names = [n.strip().lower() for n in target_drives.split(",")]
    drive_ids = []
    try:
        results = service.drives().list(pageSize=50).execute()
        for drive in results.get("drives", []):
            if drive["name"].lower() in target_names:
                drive_ids.append({"id": drive["id"], "name": drive["name"]})
    except Exception:
        pass
    return drive_ids


def get_recent_drive_activity(user_email, known_file_ids=None):
    """Get files modified in the last 24 hours from targeted shared drives.

    Only scans Sales and Federal Projects shared drives, plus meeting notes.
    If known_file_ids is provided, skip files already in the knowledge base.

    Returns:
        list[dict]: [{"name": str, "mimeType": str, "modifiedTime": str, "webViewLink": str, "driveId": str}]
    """
    creds = _get_credentials(user_email)
    if not creds:
        return []
    service = build("drive", "v3", credentials=creds, cache_discovery=False)
    yesterday = (datetime.now(timezone.utc) - timedelta(hours=24)).isoformat()

    known = set(known_file_ids or [])
    all_files = []

    # Search targeted shared drives
    shared_drives = _get_shared_drive_ids(service)
    for drive in shared_drives:
        try:
            results = service.files().list(
                q=f"modifiedTime > '{yesterday}' and trashed = false",
                fields="files(id,name,mimeType,modifiedTime,webViewLink)",
                orderBy="modifiedTime desc",
                pageSize=20,
                corpora="drive",
                driveId=drive["id"],
                includeItemsFromAllDrives=True,
                supportsAllDrives=True,
            ).execute()
            for f in results.get("files", []):
                if f["id"] not in known:
                    f["driveName"] = drive["name"]
                    all_files.append(f)
        except Exception:
            continue

    # Always search for meeting notes across all drives
    try:
        results = service.files().list(
            q=f"name contains 'BST Internal Update Meeting' and modifiedTime > '{yesterday}' and trashed = false",
            fields="files(id,name,mimeType,modifiedTime,webViewLink)",
            orderBy="modifiedTime desc",
            pageSize=5,
            corpora="allDrives",
            includeItemsFromAllDrives=True,
            supportsAllDrives=True,
        ).execute()
        for f in results.get("files", []):
            if f["id"] not in known and f["id"] not in {x["id"] for x in all_files}:
                f["driveName"] = "Meeting Notes"
                all_files.append(f)
    except Exception:
        pass

    return all_files


def get_meeting_notes_content(user_email, max_docs=2):
    """Fetch the content of the most recent BST Internal Update Meeting notes.

    Returns:
        list[dict]: [{"name": str, "content": str}]
    """
    creds = _get_credentials(user_email)
    if not creds:
        return []
    service = build("drive", "v3", credentials=creds, cache_discovery=False)

    results = service.files().list(
        q="name contains 'BST Internal Update Meeting' and mimeType = 'application/vnd.google-apps.document'",
        fields="files(id,name,modifiedTime)",
        orderBy="modifiedTime desc",
        pageSize=max_docs,
        corpora="allDrives",
        includeItemsFromAllDrives=True,
        supportsAllDrives=True,
    ).execute()

    docs = []
    for f in results.get("files", []):
        try:
            content = service.files().export(
                fileId=f["id"], mimeType="text/plain"
            ).execute()
            text = content.decode("utf-8") if isinstance(content, bytes) else str(content)
            # Truncate to keep prompt manageable
            docs.append({"name": f["name"], "content": text[:3000]})
        except Exception:
            continue

    return docs


def get_recent_emails(user_email, max_results=20):
    """Get recent email subjects and senders (last 24 hours, no bodies).

    Returns:
        list[dict]: [{"subject": str, "from": str, "date": str}]
    """
    creds = _get_credentials(user_email)
    if not creds:
        return []
    service = build("gmail", "v1", credentials=creds, cache_discovery=False)

    results = service.users().messages().list(
        userId="me",
        q="is:inbox newer_than:1d",
        maxResults=max_results,
    ).execute()

    messages = results.get("messages", [])
    emails = []
    for msg in messages:
        detail = service.users().messages().get(
            userId="me",
            id=msg["id"],
            format="metadata",
            metadataHeaders=["Subject", "From", "Date"],
        ).execute()
        headers = {h["name"]: h["value"] for h in detail.get("payload", {}).get("headers", [])}
        emails.append({
            "subject": headers.get("Subject", "(no subject)"),
            "from": headers.get("From", ""),
            "date": headers.get("Date", ""),
        })

    return emails


def get_latest_email_by_subject(user_email, subject, sender=None, max_age_hours=36):
    """Fetch the most recent email matching `subject` (and optional `sender`).

    Returns the parsed body text, or None if no match within `max_age_hours`.
    """
    creds = _get_credentials(user_email)
    if not creds:
        return None
    service = build("gmail", "v1", credentials=creds, cache_discovery=False)

    days = max(1, max_age_hours // 24 + (1 if max_age_hours % 24 else 0))
    q = f'subject:"{subject}" newer_than:{days}d'
    if sender:
        q += f" from:{sender}"

    results = service.users().messages().list(
        userId="me", q=q, maxResults=1
    ).execute()
    messages = results.get("messages", [])
    if not messages:
        return None

    detail = service.users().messages().get(
        userId="me", id=messages[0]["id"], format="full"
    ).execute()

    # Walk the MIME parts and return the first text/plain (fallback to text/html stripped)
    def _walk(part):
        mime = part.get("mimeType", "")
        body = part.get("body", {})
        data = body.get("data")
        if data:
            decoded = base64.urlsafe_b64decode(data + "==").decode("utf-8", errors="replace")
            yield mime, decoded
        for sub in part.get("parts", []) or []:
            yield from _walk(sub)

    text_plain = None
    text_html = None
    for mime, content in _walk(detail.get("payload", {})):
        if mime == "text/plain" and text_plain is None:
            text_plain = content
        elif mime == "text/html" and text_html is None:
            text_html = content

    if text_plain:
        return text_plain.strip()
    if text_html:
        # Crude HTML strip — fine for an internal summary email
        import re as _re
        stripped = _re.sub(r"<br\s*/?>", "\n", text_html, flags=_re.I)
        stripped = _re.sub(r"</p\s*>", "\n\n", stripped, flags=_re.I)
        stripped = _re.sub(r"<[^>]+>", "", stripped)
        return stripped.strip()
    return None


def get_todays_calendar(user_email):
    """Get today's calendar events for a user.

    Returns:
        list[dict]: [{"summary": str, "start": str, "end": str, "attendees": list[str]}]
    """
    creds = _get_credentials(user_email)
    if not creds:
        return []
    service = build("calendar", "v3", credentials=creds, cache_discovery=False)

    now = datetime.now(timezone.utc)
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_day = start_of_day + timedelta(days=1)

    results = service.events().list(
        calendarId="primary",
        timeMin=start_of_day.isoformat(),
        timeMax=end_of_day.isoformat(),
        singleEvents=True,
        orderBy="startTime",
        maxResults=20,
    ).execute()

    events = []
    for event in results.get("items", []):
        start = event.get("start", {}).get("dateTime") or event.get("start", {}).get("date", "")
        end = event.get("end", {}).get("dateTime") or event.get("end", {}).get("date", "")
        attendees = [a.get("email", "") for a in event.get("attendees", [])]
        events.append({
            "summary": event.get("summary", "(no title)"),
            "start": start,
            "end": end,
            "attendees": attendees,
        })
    return events


def get_contacts(user_email, max_results=100):
    """Get contacts from Google People API — useful for client/project context.

    Returns directory contacts (coworkers) and other contacts (external clients).

    Returns:
        list[dict]: [{"name": str, "email": str, "organization": str, "title": str}]
    """
    creds = _get_credentials(user_email)
    if not creds:
        return []

    contacts = []

    # Workspace directory (coworkers)
    try:
        service = build("people", "v1", credentials=creds, cache_discovery=False)
        results = service.people().listDirectoryPeople(
            readMask="names,emailAddresses,organizations",
            sources=["DIRECTORY_SOURCE_TYPE_DOMAIN_PROFILE"],
            pageSize=min(max_results, 200),
        ).execute()
        for person in results.get("people", []):
            names = person.get("names", [{}])
            emails = person.get("emailAddresses", [{}])
            orgs = person.get("organizations", [{}])
            contacts.append({
                "name": names[0].get("displayName", "") if names else "",
                "email": emails[0].get("value", "") if emails else "",
                "organization": orgs[0].get("name", "") if orgs else "",
                "title": orgs[0].get("title", "") if orgs else "",
            })
    except Exception:
        pass

    # Other contacts (external people they've interacted with)
    try:
        service = build("people", "v1", credentials=creds, cache_discovery=False)
        results = service.otherContacts().list(
            readMask="names,emailAddresses,organizations",
            pageSize=min(max_results, 200),
        ).execute()
        for person in results.get("otherContacts", []):
            names = person.get("names", [{}])
            emails = person.get("emailAddresses", [{}])
            orgs = person.get("organizations", [{}])
            contacts.append({
                "name": names[0].get("displayName", "") if names else "",
                "email": emails[0].get("value", "") if emails else "",
                "organization": orgs[0].get("name", "") if orgs else "",
                "title": orgs[0].get("title", "") if orgs else "",
            })
    except Exception:
        pass

    return contacts
