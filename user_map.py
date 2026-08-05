import json
import os
import re
import base64
from pathlib import Path
import requests

ASANA_BASE = "https://app.asana.com/api/1.0"
TOGGL_BASE = "https://api.track.toggl.com/api/v9"

_user_map = []

UID_MAP_PATH = Path(__file__).parent / "knowledge" / "contacts" / "uid_map.json"


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


def _extract_first_name(email):
    """Try to extract a first name from first.last@ format."""
    local = _extract_alias(email)
    if "." in local:
        return local.split(".")[0]
    return None


def _aliases_match(email1, email2):
    """Check if two emails likely belong to the same person.

    Matches on: exact alias, or shared last name within same domain family.
    Rejects matches where both emails have explicit but different first names
    (e.g. jack.elston@ vs tiffany.elston@).
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
    # If both have first.last format with different first names, reject
    first1 = _extract_first_name(email1)
    first2 = _extract_first_name(email2)
    if first1 and first2 and first1 != first2:
        return False
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

    # Excluded emails (contractors, external, non-employees, etc.)
    # Hard-coded exclusions for known non-employee accounts
    excluded_emails = {
        "tiffany.elston@blackswifttech.com",
        "todd.elston@blackswifttech.com",
        "jameel.barkat@blackswifttech.com",
    }
    exclude_json = os.environ.get("EXCLUDED_USERS", "")
    if exclude_json:
        try:
            excluded_emails |= {e.lower() for e in json.loads(exclude_json)}
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
        entry = {"email": email, "name": "", "slack_user_id": None, "asana_user_gid": None,
                 "toggl_user_id": None, "source_names": []}
        if email in slack_users:
            entry["slack_user_id"] = slack_users[email]["slack_user_id"]
            entry["name"] = slack_users[email]["name"]
            _add_source_name(entry, slack_users[email]["name"])
        if email in asana_users:
            entry["asana_user_gid"] = asana_users[email]["asana_user_gid"]
            _add_source_name(entry, asana_users[email]["name"])
            if not entry["name"]:
                entry["name"] = asana_users[email]["name"]
        if email in toggl_users:
            entry["toggl_user_id"] = toggl_users[email]["toggl_user_id"]
            _add_source_name(entry, toggl_users[email]["name"])
            if not entry["name"]:
                entry["name"] = toggl_users[email]["name"]
        unified[email] = entry

    # Second pass: fuzzy matching for unmatched entries
    # Match by alias or last name within same domain family.
    # If a fuzzy match points to another entry already in unified, merge the
    # IDs from that entry (handles e.g. elstonj@ + jack.elston@).
    matched_asana = {e for e, ent in unified.items() if ent["asana_user_gid"]}
    matched_toggl = {e for e, ent in unified.items() if ent["toggl_user_id"]}
    matched_slack = {e for e, ent in unified.items() if ent["slack_user_id"]}
    merged_away = set()  # emails absorbed into another entry

    for email, entry in list(unified.items()):
        if email in merged_away:
            continue

        if not entry["asana_user_gid"]:
            for asana_email, asana_data in asana_users.items():
                if asana_email in excluded_emails:
                    continue
                # Skip if already matched, UNLESS it's in unified (merge opportunity)
                if asana_email in matched_asana and asana_email not in unified:
                    continue
                if _aliases_match(email, asana_email):
                    entry["asana_user_gid"] = asana_data["asana_user_gid"]
                    _add_source_name(entry, asana_data["name"])
                    if not entry["name"]:
                        entry["name"] = asana_data["name"]
                    matched_asana.add(asana_email)
                    # If the matched email has its own entry in unified, absorb it
                    if asana_email in unified and asana_email != email:
                        other = unified[asana_email]
                        if not entry["toggl_user_id"] and other["toggl_user_id"]:
                            entry["toggl_user_id"] = other["toggl_user_id"]
                        if not entry["slack_user_id"] and other["slack_user_id"]:
                            entry["slack_user_id"] = other["slack_user_id"]
                        if not entry["name"] and other["name"]:
                            entry["name"] = other["name"]
                        merged_away.add(asana_email)
                    break

        if not entry["toggl_user_id"]:
            for toggl_email, toggl_data in toggl_users.items():
                if toggl_email in excluded_emails:
                    continue
                if toggl_email in matched_toggl and toggl_email not in unified:
                    continue
                if _aliases_match(email, toggl_email):
                    entry["toggl_user_id"] = toggl_data["toggl_user_id"]
                    _add_source_name(entry, toggl_data["name"])
                    if not entry["name"]:
                        entry["name"] = toggl_data["name"]
                    matched_toggl.add(toggl_email)
                    if toggl_email in unified and toggl_email != email:
                        other = unified[toggl_email]
                        if not entry["asana_user_gid"] and other["asana_user_gid"]:
                            entry["asana_user_gid"] = other["asana_user_gid"]
                        if not entry["slack_user_id"] and other["slack_user_id"]:
                            entry["slack_user_id"] = other["slack_user_id"]
                        if not entry["name"] and other["name"]:
                            entry["name"] = other["name"]
                        merged_away.add(toggl_email)
                    break

        if not entry["slack_user_id"]:
            for slack_email, slack_data in slack_users.items():
                if slack_email in excluded_emails:
                    continue
                if slack_email in matched_slack and slack_email not in unified:
                    continue
                if _aliases_match(email, slack_email):
                    entry["slack_user_id"] = slack_data["slack_user_id"]
                    _add_source_name(entry, slack_data["name"])
                    if not entry["name"]:
                        entry["name"] = slack_data["name"]
                    matched_slack.add(slack_email)
                    if slack_email in unified and slack_email != email:
                        other = unified[slack_email]
                        if not entry["asana_user_gid"] and other["asana_user_gid"]:
                            entry["asana_user_gid"] = other["asana_user_gid"]
                        if not entry["toggl_user_id"] and other["toggl_user_id"]:
                            entry["toggl_user_id"] = other["toggl_user_id"]
                        if not entry["name"] and other["name"]:
                            entry["name"] = other["name"]
                        merged_away.add(slack_email)
                    break

    # Remove entries that were absorbed into another
    for email in merged_away:
        unified.pop(email, None)

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
            for src_name in entry.get("source_names") or []:
                _add_source_name(existing, src_name)
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

    # Graft canonical multi-ID lists from uid_map.json onto live entries.
    # Several people have multiple Toggl IDs (legacy + current accounts);
    # the live workspace API only returns one entry per email, so without
    # this step time entries logged under the "other" Toggl ID would not
    # resolve back to the user.
    _apply_uid_map_overrides(merged)

    # Pin every entry to ONE canonical name and record every spelling the
    # source systems use for that person.  Downstream (especially the daily
    # briefing) must never have to guess whether "Josh Fromm", "Joshua" and
    # "Dan Prendergast" are three people or two.
    _apply_canonical_names(merged)

    # Only include users who have ALL THREE: Slack, Asana, and at least one Toggl ID
    result = [e for e in merged.values()
              if e.get("slack_user_id") and e.get("asana_user_gid")
              and (e.get("toggl_user_ids") or e.get("toggl_user_id"))]
    _user_map = result
    _build_alias_index(result)
    return result


def _apply_uid_map_overrides(merged):
    """Augment live-built entries with canonical IDs from uid_map.json.

    Adds a `toggl_user_ids` list (full set of legitimate Toggl IDs per user)
    and ensures `toggl_user_id` is set to the canonical primary even if the
    live Toggl API returned a different ID for that email.
    """
    try:
        with UID_MAP_PATH.open() as f:
            uid_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return

    by_slack = {entry.get("slack_user_id"): entry
                for entry in uid_data.get("users", []) if entry.get("slack_user_id")}

    for entry in merged.values():
        sid = entry.get("slack_user_id")
        canonical = by_slack.get(sid)
        if not canonical:
            # Fall back to populating toggl_user_ids from the singular field
            if entry.get("toggl_user_id"):
                entry["toggl_user_ids"] = [entry["toggl_user_id"]]
            continue
        ids = list(canonical.get("toggl_user_ids") or [])
        if entry.get("toggl_user_id") and entry["toggl_user_id"] not in ids:
            ids.append(entry["toggl_user_id"])
        entry["toggl_user_ids"] = ids
        if ids:
            # Pin to the canonical primary so downstream display is stable
            entry["toggl_user_id"] = ids[0]


# ---------------------------------------------------------------------------
# Canonical identity + alias resolution
#
# Every source system spells people differently — Slack shows display names
# ("Ben", "Beck"), Asana shows account names ("Josh Fromm", "Dan Prendergast",
# "Meredith O'hara Needham"), Rippling uses formal names ("Nathaniel Straus").
# The daily briefing used to hand all of those spellings to an LLM and ask it
# to reconcile them against opaque Slack IDs, which is how Josh Fromm ended up
# with Jack Elston's tasks.  These helpers make the resolution deterministic.
# ---------------------------------------------------------------------------

_alias_index = {}         # normalized full-name string -> slack_user_id
_token_index = {}         # normalized single token -> set of slack_user_ids
_token_owner = {}         # normalized single token -> slack_user_id (unambiguous only)


def _norm_name(text):
    """Lowercase, strip punctuation, collapse whitespace."""
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]+", " ", (text or "").lower())).strip()


def _add_source_name(entry, name):
    """Record a spelling of this person's name as seen in a source system."""
    if not name:
        return
    names = entry.setdefault("source_names", [])
    if name not in names:
        names.append(name)


def _apply_canonical_names(merged):
    """Set `name` to the canonical full name and build each entry's alias set.

    uid_map.json is the source of truth when the person is listed there.
    Anyone missing from it keeps their live name and gets aliases derived from
    that name plus their email local part.
    """
    try:
        with UID_MAP_PATH.open() as f:
            uid_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        uid_data = {"users": []}

    by_slack = {u.get("slack_user_id"): u
                for u in uid_data.get("users", []) if u.get("slack_user_id")}

    for entry in merged.values():
        canonical = by_slack.get(entry.get("slack_user_id")) or {}
        aliases = set()

        for src_name in entry.get("source_names") or []:
            aliases.add(src_name)
        if entry.get("name"):
            aliases.add(entry["name"])

        preferred = canonical.get("preferred_first") or ""
        formal = canonical.get("formal_first") or ""
        last = canonical.get("last") or ""
        full_name = canonical.get("canonical_name") or entry.get("name") or ""

        if full_name:
            entry["name"] = full_name
            aliases.add(full_name)
        if canonical.get("rippling_name"):
            aliases.add(canonical["rippling_name"])
        # Explicitly pinned spellings — nicknames and source-system names that
        # shouldn't depend on every API being reachable at map-build time.
        for alias in canonical.get("aliases") or []:
            aliases.add(alias)
        for first in (preferred, formal):
            if first and last:
                aliases.add(f"{first} {last}")

        # Email local part: "josh.fromm" -> "josh fromm". Skip smashed-together
        # forms like "elstonj" that aren't real name spellings.
        for email in [entry.get("email", "")] + list(canonical.get("email_aliases") or []):
            local = _extract_alias(email)
            if "." in local:
                aliases.add(local.replace(".", " "))

        entry["aliases"] = sorted(a for a in aliases if a)
        # First/last tokens used for single-token ("Josh", "Elston") lookups.
        tokens = set()
        for part in (preferred, formal, last):
            if part:
                tokens.add(_norm_name(part))
        for alias in entry["aliases"]:
            for tok in _norm_name(alias).split():
                tokens.add(tok)
        entry["name_tokens"] = sorted(t for t in tokens if t)


def _build_alias_index(users):
    """Index every alias so an arbitrary name spelling resolves to one person."""
    global _alias_index, _token_index, _token_owner
    _alias_index = {}
    _token_index = {}

    for user in users:
        sid = user.get("slack_user_id")
        if not sid:
            continue
        for alias in (user.get("aliases") or [user.get("name", "")]):
            key = _norm_name(alias)
            if not key:
                continue
            # First writer wins; a collision means two people share a spelling,
            # in which case neither should resolve from it.
            if key in _alias_index and _alias_index[key] != sid:
                _alias_index[key] = None
            else:
                _alias_index.setdefault(key, sid)
        for tok in (user.get("name_tokens") or []):
            _token_index.setdefault(tok, set()).add(sid)

    _token_owner = {tok: next(iter(sids)) for tok, sids in _token_index.items()
                    if len(sids) == 1}


def resolve_person(name):
    """Resolve any spelling of a person's name to their user-map entry.

    Returns None when the name is unknown or ambiguous — callers must treat
    that as "don't guess", never as a silent fallback to some other person.
    """
    key = _norm_name(name)
    if not key:
        return None

    sid = _alias_index.get(key)
    if sid:
        return get_user_by_slack_id(sid)
    if key in _alias_index:  # present but None == ambiguous spelling
        return None

    parts = key.split()
    if len(parts) == 1:
        sid = _token_owner.get(parts[0])
        return get_user_by_slack_id(sid) if sid else None

    # Multi-token: require first AND last token to land on the same single
    # person ("dan prendergast", "meredith o hara needham").
    first_ids = _token_index.get(parts[0], set())
    last_ids = _token_index.get(parts[-1], set())
    both = first_ids & last_ids
    if len(both) == 1:
        return get_user_by_slack_id(next(iter(both)))

    # Fall back to a unique last-name hit, but ONLY when the given first name
    # is a plausible variant of one this person actually uses.  Without that
    # guard an outside contact like "Bob Smith" would resolve to Paige Smith.
    if len(last_ids) == 1:
        candidate = get_user_by_slack_id(next(iter(last_ids)))
        first = parts[0]
        for tok in (candidate.get("name_tokens") or []) if candidate else []:
            if len(tok) >= 3 and len(first) >= 3 and (tok.startswith(first) or first.startswith(tok)):
                return candidate
    return None


def canonical_name(name):
    """Return the canonical full name for any spelling, or the input unchanged."""
    user = resolve_person(name)
    return user["name"] if user and user.get("name") else name


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


def get_user_by_toggl_id(toggl_user_id):
    for user in _user_map:
        if user.get("toggl_user_id") == toggl_user_id:
            return user
        if toggl_user_id in (user.get("toggl_user_ids") or ()):
            return user
    return None
