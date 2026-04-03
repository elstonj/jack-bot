import json
import os
import base64
import requests

ASANA_BASE = "https://app.asana.com/api/1.0"
TOGGL_BASE = "https://api.track.toggl.com/api/v9"

_user_map = []


def _asana_headers():
    return {"Authorization": f"Bearer {os.environ['ASANA_ACCESS_TOKEN']}"}


def _toggl_headers():
    token = os.environ.get("TOGGL_API_TOKEN", "")
    encoded = base64.b64encode(f"{token}:api_token".encode()).decode()
    return {"Authorization": f"Basic {encoded}"}


def _get_slack_users(slack_client):
    """Get all Slack users with emails."""
    users = {}
    result = slack_client.users_list()
    for member in result.get("members", []):
        if member.get("deleted") or member.get("is_bot"):
            continue
        email = member.get("profile", {}).get("email", "").lower()
        if email:
            users[email] = {
                "slack_user_id": member["id"],
                "name": member.get("profile", {}).get("display_name")
                    or member.get("real_name", ""),
            }
    return users


def _get_asana_users():
    """Get all Asana users with emails."""
    token = os.environ.get("ASANA_ACCESS_TOKEN")
    if not token:
        return {}
    # Get first workspace
    resp = requests.get(f"{ASANA_BASE}/workspaces", headers=_asana_headers(), timeout=10)
    resp.raise_for_status()
    workspaces = resp.json()["data"]
    if not workspaces:
        return {}
    wgid = workspaces[0]["gid"]

    resp = requests.get(
        f"{ASANA_BASE}/users",
        headers=_asana_headers(),
        params={"workspace": wgid, "opt_fields": "name,email"},
        timeout=10,
    )
    resp.raise_for_status()
    users = {}
    for user in resp.json()["data"]:
        email = user.get("email", "").lower()
        if email:
            users[email] = {"asana_user_gid": user["gid"], "name": user.get("name", "")}
    return users


def _get_toggl_users():
    """Get all Toggl workspace users."""
    token = os.environ.get("TOGGL_API_TOKEN")
    wid = os.environ.get("TOGGL_WORKSPACE_ID")
    if not token or not wid:
        return {}
    resp = requests.get(
        f"{TOGGL_BASE}/organizations/{wid}/users",
        headers=_toggl_headers(),
        timeout=10,
    )
    if resp.status_code != 200:
        # Try workspace endpoint instead
        resp = requests.get(
            f"{TOGGL_BASE}/workspaces/{wid}/users",
            headers=_toggl_headers(),
            timeout=10,
        )
    resp.raise_for_status()
    users = {}
    for user in resp.json():
        email = user.get("email", "").lower()
        if email:
            users[email] = {"toggl_user_id": user.get("id"), "name": user.get("name", "")}
    return users


def _extract_alias(email):
    """Extract the local part before @ as an alias for fuzzy matching."""
    return email.split("@")[0].lower() if "@" in email else ""


def _extract_last_name(email):
    """Try to extract a last name from the email local part.

    Handles: first.last@, firstlast@, flast@, last@
    Returns the last component after splitting on dots, or None.
    """
    local = _extract_alias(email)
    if "." in local:
        return local.split(".")[-1]
    return None


def _same_domain(email1, email2):
    """Check if two emails share the same domain (or known equivalent domains)."""
    domain1 = email1.split("@")[1] if "@" in email1 else ""
    domain2 = email2.split("@")[1] if "@" in email2 else ""
    equiv = {"blackswifttech.com", "blackswifttechnologies.com"}
    if domain1 in equiv and domain2 in equiv:
        return True
    return domain1 == domain2


def _aliases_match(email1, email2):
    """Check if two emails likely belong to the same person.

    Matches on: exact alias, or shared last name within same domain family.
    """
    if not _same_domain(email1, email2):
        return False
    alias1 = _extract_alias(email1)
    alias2 = _extract_alias(email2)
    if alias1 == alias2:
        return True
    # Last name matching: jack.elston matches elstonj (both contain "elston")
    last1 = _extract_last_name(email1)
    last2 = _extract_last_name(email2)
    if last1 and last2 and last1 == last2:
        return True
    # Check if one alias contains the other's last name or vice versa
    if last1 and last1 in alias2:
        return True
    if last2 and last2 in alias1:
        return True
    return False


def build_user_map(slack_client):
    """Build unified user map from all services, matched by email or alias."""
    global _user_map

    slack_users = _get_slack_users(slack_client)
    asana_users = _get_asana_users()
    toggl_users = _get_toggl_users()

    # Excluded emails (contractors, external, etc.)
    exclude_json = os.environ.get("EXCLUDED_USERS", "")
    excluded_emails = set()
    if exclude_json:
        try:
            excluded_emails = {e.lower() for e in json.loads(exclude_json)}
        except json.JSONDecodeError:
            pass

    # Build alias indexes for fuzzy matching
    # alias -> list of (email, source_dict, source_name)
    all_sources = [
        (slack_users, "slack"),
        (asana_users, "asana"),
        (toggl_users, "toggl"),
    ]

    # First pass: exact email match
    all_emails = set(slack_users.keys()) | set(asana_users.keys()) | set(toggl_users.keys())
    all_emails -= excluded_emails

    unified = {}  # keyed by canonical email
    for email in all_emails:
        if email in excluded_emails:
            continue
        entry = {"email": email, "name": "", "slack_user_id": None, "asana_user_gid": None, "toggl_user_id": None}
        if email in slack_users:
            entry["slack_user_id"] = slack_users[email]["slack_user_id"]
            entry["name"] = slack_users[email]["name"]
        if email in asana_users:
            entry["asana_user_gid"] = asana_users[email]["asana_user_gid"]
            if not entry["name"]:
                entry["name"] = asana_users[email]["name"]
        if email in toggl_users:
            entry["toggl_user_id"] = toggl_users[email]["toggl_user_id"]
            if not entry["name"]:
                entry["name"] = toggl_users[email]["name"]
        unified[email] = entry

    # Second pass: fuzzy matching for unmatched entries
    # Match by alias or last name within same domain family
    matched_asana = {e for e, ent in unified.items() if ent["asana_user_gid"]}
    matched_toggl = {e for e, ent in unified.items() if ent["toggl_user_id"]}
    matched_slack = {e for e, ent in unified.items() if ent["slack_user_id"]}

    for email, entry in list(unified.items()):
        if not entry["asana_user_gid"]:
            for asana_email, asana_data in asana_users.items():
                if asana_email in excluded_emails or asana_email in unified or asana_email in matched_asana:
                    continue
                if _aliases_match(email, asana_email):
                    entry["asana_user_gid"] = asana_data["asana_user_gid"]
                    if not entry["name"]:
                        entry["name"] = asana_data["name"]
                    matched_asana.add(asana_email)
                    break

        if not entry["toggl_user_id"]:
            for toggl_email, toggl_data in toggl_users.items():
                if toggl_email in excluded_emails or toggl_email in unified or toggl_email in matched_toggl:
                    continue
                if _aliases_match(email, toggl_email):
                    entry["toggl_user_id"] = toggl_data["toggl_user_id"]
                    if not entry["name"]:
                        entry["name"] = toggl_data["name"]
                    matched_toggl.add(toggl_email)
                    break

        if not entry["slack_user_id"]:
            for slack_email, slack_data in slack_users.items():
                if slack_email in excluded_emails or slack_email in unified or slack_email in matched_slack:
                    continue
                if _aliases_match(email, slack_email):
                    entry["slack_user_id"] = slack_data["slack_user_id"]
                    if not entry["name"]:
                        entry["name"] = slack_data["name"]
                    matched_slack.add(slack_email)
                    break

    # Apply manual overrides
    overrides_json = os.environ.get("USER_MAP_OVERRIDES", "")
    if overrides_json:
        try:
            overrides = json.loads(overrides_json)
            for override in overrides:
                ov_email = override.get("email", "").lower()
                for email, entry in unified.items():
                    if entry["email"] == ov_email:
                        entry.update({k: v for k, v in override.items() if v and k != "email"})
                        break
        except json.JSONDecodeError:
            pass

    # Merge duplicate users (same person with different emails)
    # After overrides, find entries that now share a slack_user_id and merge them
    merged = {}
    for email, entry in unified.items():
        sid = entry.get("slack_user_id")
        if sid and sid in merged:
            # Merge into existing entry
            existing = merged[sid]
            if not existing["asana_user_gid"] and entry["asana_user_gid"]:
                existing["asana_user_gid"] = entry["asana_user_gid"]
            if not existing["toggl_user_id"] and entry["toggl_user_id"]:
                existing["toggl_user_id"] = entry["toggl_user_id"]
            if not existing["name"] and entry["name"]:
                existing["name"] = entry["name"]
        elif sid:
            merged[sid] = entry
        else:
            # No slack ID — keep if they have Asana tasks
            if entry["asana_user_gid"]:
                merged[email] = entry

    # Only include users who have ALL THREE: Slack, Asana, and Toggl
    result = [e for e in merged.values()
              if e.get("slack_user_id") and e.get("asana_user_gid") and e.get("toggl_user_id")]
    _user_map = result
    return result


def get_all_users():
    return _user_map


def get_user_by_slack_id(slack_id):
    for user in _user_map:
        if user["slack_user_id"] == slack_id:
            return user
    return None


def get_user_by_asana_gid(gid):
    for user in _user_map:
        if user["asana_user_gid"] == gid:
            return user
    return None


def get_user_by_email(email):
    for user in _user_map:
        if user["email"] == email.lower():
            return user
    return None
