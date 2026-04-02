import os
import json
import base64
from datetime import datetime, timedelta, timezone

from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/gmail.readonly",
]


def _get_credentials(user_email):
    """Create delegated credentials for a specific user."""
    key_json = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON", "")
    if not key_json:
        return None
    key_data = json.loads(base64.b64decode(key_json))
    creds = service_account.Credentials.from_service_account_info(key_data, scopes=SCOPES)
    return creds.with_subject(user_email)


def get_recent_drive_activity(user_email):
    """Get files modified in the last 24 hours visible to a user.

    Returns:
        list[dict]: [{"name": str, "mimeType": str, "modifiedTime": str, "webViewLink": str}]
    """
    creds = _get_credentials(user_email)
    if not creds:
        return []
    service = build("drive", "v3", credentials=creds, cache_discovery=False)
    yesterday = (datetime.now(timezone.utc) - timedelta(hours=24)).isoformat()
    results = service.files().list(
        q=f"modifiedTime > '{yesterday}' and trashed = false",
        fields="files(id,name,mimeType,modifiedTime,webViewLink)",
        orderBy="modifiedTime desc",
        pageSize=20,
    ).execute()
    return results.get("files", [])


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
