"""Every Gmail / Admin SDK call the email-triage job makes goes through here.

Jack's mailbox is the one place a bug does real damage — a wrong forward
leaks mail outside the company, a wrong label hides something he needed — so
all writes funnel through four functions (forward, modify, ensure_labels,
insert_summary) that each re-check the invariants the spec relies on, rather
than trusting callers:

- forward() refuses any recipient outside BST that isn't on the greenlist,
  even if classify/guards let one through.
- modify() refuses to touch UNREAD/TRASH; triage never changes read state and
  never deletes.
- insert_summary() uses messages.insert, so the daily summary never leaves
  the mailbox.

Credentials are built here with the triage scopes (gmail.modify, gmail.send,
admin.directory.group.readonly) instead of widening google_client.SCOPES,
which every other read-only pipeline shares.

googleapiclient service objects are not thread-safe (httplib2), and the
runner classifies in a thread pool, so services are cached per thread.
"""

import base64
import email
import html as _html
import json
import os
import re
import threading
import time
from email import policy
from email.message import EmailMessage, MIMEPart
from email.utils import formatdate, getaddresses, make_msgid, parseaddr

from google.oauth2 import service_account
from googleapiclient.discovery import build

JACK = "elstonj@blackswifttech.com"

SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/admin.directory.group.readonly",
]

FREEMAIL = {"gmail.com", "yahoo.com", "outlook.com", "hotmail.com",
            "icloud.com", "protonmail.com"}

_DEFAULTS = {
    "jack": JACK,
    "jack_aliases": ["jack.elston@blackswifttech.com", "elstonj@bst.aero"],
    "internal_domains": ["blackswifttech.com", "bst.aero"],
    "external_greenlist": ["shelly@krateosky.com", "pam@krateosky.com"],
    "skip_labels": ["Filters/Purchasing", "Junk/*"],
}

BODY_LIMIT = 6000
GROUP_TTL = 3600
FORWARD_PREAMBLE = (
    "Forwarded automatically from Jack's inbox. Please take a look — disregard "
    "it if it's not relevant, act on it if it is. If I'm sending you things "
    "that aren't relevant to you, please message me about it. I'm trying my "
    "best to remove myself as a blocker on the information flowing into and "
    "out of Black Swift."
)

_local = threading.local()
_lock = threading.Lock()
_creds = {}
_label_cache = {"ts": 0, "by_name": {}, "by_id": {}}
_group_cache = {"ts": 0, "data": None}
_known_cache = {}
_jack_thread_cache = {}


# ---------- config ----------

def _cfg():
    """Merge the routing builder's config over spec defaults (config.py may
    not exist yet, or may name Jack's addresses differently)."""
    cfg = dict(_DEFAULTS)
    try:
        from email_triage.config import load_config
        cfg.update(load_config() or {})
    except Exception:
        pass
    return cfg


def _jack_addresses():
    cfg = _cfg()
    jack = cfg.get("jack")
    out = set()
    if isinstance(jack, dict):
        out.add(jack.get("email", JACK))
        out.update(jack.get("aliases", []) or [])
    elif isinstance(jack, str):
        out.add(jack)
    out.update(cfg.get("jack_aliases", []) or [])
    out.add(JACK)
    return {a.lower() for a in out if a}


def _internal_domains():
    return {d.lower() for d in _cfg().get("internal_domains") or _DEFAULTS["internal_domains"]}


def _greenlist():
    return {a.lower() for a in _cfg().get("external_greenlist") or _DEFAULTS["external_greenlist"]}


def _domain(addr):
    return addr.rsplit("@", 1)[-1].lower() if "@" in addr else ""


# ---------- services ----------

def _credentials(scopes):
    key = tuple(scopes)
    with _lock:
        if key not in _creds:
            raw = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON", "")
            if not raw:
                raise RuntimeError("GOOGLE_SERVICE_ACCOUNT_JSON not set")
            info = json.loads(base64.b64decode(raw))
            _creds[key] = service_account.Credentials.from_service_account_info(
                info, scopes=list(scopes)).with_subject(JACK)
        return _creds[key]


def service(scopes=None):
    """Gmail v1 service delegated as Jack, cached per thread."""
    scopes = tuple(scopes or SCOPES)
    cache = getattr(_local, "gmail", None)
    if cache is None:
        cache = _local.gmail = {}
    if scopes not in cache:
        cache[scopes] = build("gmail", "v1", credentials=_credentials(scopes),
                              cache_discovery=False)
    return cache[scopes]


def _directory():
    svc = getattr(_local, "directory", None)
    if svc is None:
        svc = _local.directory = build("admin", "directory_v1",
                                       credentials=_credentials(SCOPES),
                                       cache_discovery=False)
    return svc


# ---------- labels ----------

def _labels(refresh=False):
    with _lock:
        fresh = time.time() - _label_cache["ts"] < 600
    if refresh or not fresh:
        resp = service().users().labels().list(userId="me").execute(num_retries=5)
        by_name = {l["name"]: l["id"] for l in resp.get("labels", [])}
        with _lock:
            _label_cache.update(ts=time.time(), by_name=by_name,
                                by_id={v: k for k, v in by_name.items()})
    return _label_cache


def ensure_labels(names):
    """Return {name: id}, creating missing labels (parents first, so
    "Jackbot/Forwarded" nests under "Jackbot")."""
    cache = _labels()
    out = {}
    for name in names:
        if name in cache["by_name"]:
            out[name] = cache["by_name"][name]
            continue
        parts = name.split("/")
        for i in range(1, len(parts) + 1):
            sub = "/".join(parts[:i])
            if sub in _labels()["by_name"]:
                continue
            try:
                service().users().labels().create(userId="me", body={
                    "name": sub, "labelListVisibility": "labelShow",
                    "messageListVisibility": "show"}).execute(num_retries=5)
            except Exception:
                # Lost a race with another worker, or it already exists.
                pass
            _labels(refresh=True)
        out[name] = _labels()["by_name"][name]
    return out


def _resolve_label_ids(values):
    cache = _labels()
    ids = []
    for v in values or []:
        if v in cache["by_id"]:
            ids.append(v)
        elif v in cache["by_name"]:
            ids.append(cache["by_name"][v])
        else:
            ids.append(ensure_labels([v])[v])
    return ids


def _skip_label_ids():
    # config.json splits these into skip_labels (exact) and
    # skip_label_prefixes ("Junk/"); its skip_labels replaces the default
    # list, so without the prefixes and the defaults every Junk/* label
    # would be triaged (and could be forwarded or pulled into the inbox).
    cfg = _cfg()
    patterns = set(_DEFAULTS["skip_labels"]) | set(cfg.get("skip_labels") or [])
    patterns |= {p.rstrip("/") + "/*" for p in cfg.get("skip_label_prefixes") or []}
    names = _labels()["by_name"]
    ids = set()
    for pat in patterns:
        if pat.endswith("/*"):
            root = pat[:-2]
            for n, i in names.items():
                if n == root or n.startswith(root + "/"):
                    ids.add(i)
        elif pat in names:
            ids.add(names[pat])
    return ids


def _search_name(label):
    return re.sub(r"[\s/]+", "-", label.lower())


# ---------- message parsing ----------

def _headers(payload):
    out = {}
    for h in payload.get("headers", []) or []:
        out.setdefault(h["name"].lower(), []).append(h["value"])
    return out


def _first(hdrs, name, default=""):
    vals = hdrs.get(name.lower())
    return vals[0] if vals else default


def _addrs(values):
    return [a.lower() for _, a in getaddresses(values or []) if a and "@" in a]


def _walk(part):
    yield part
    for sub in part.get("parts", []) or []:
        yield from _walk(sub)


def _decode(data):
    return base64.urlsafe_b64decode(data + "=" * (-len(data) % 4)).decode("utf-8", errors="replace")


def html_to_text(s):
    s = re.sub(r"(?is)<(style|script|head|title)\b.*?</\1\s*>", " ", s)
    s = re.sub(r"(?s)<!--.*?-->", " ", s)
    s = re.sub(r"(?i)<br\s*/?>", "\n", s)
    s = re.sub(r"(?i)</(p|div|li|tr|h[1-6]|table|section|blockquote)\s*>", "\n", s)
    s = re.sub(r"(?i)</td\s*>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = _html.unescape(s).replace("\xa0", " ")
    s = re.sub(r"[ \t\r\f\v]+", " ", s)
    s = re.sub(r" *\n *", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def _body_and_attachments(payload):
    plain, htm, names = None, None, []
    for part in _walk(payload):
        mime = part.get("mimeType", "")
        fname = part.get("filename") or ""
        data = (part.get("body") or {}).get("data")
        if fname:
            names.append(fname)
            continue
        if not data:
            continue
        if mime == "text/plain" and plain is None:
            plain = _decode(data)
        elif mime == "text/html" and htm is None:
            htm = _decode(data)
    text = plain.strip() if plain and plain.strip() else (html_to_text(htm) if htm else "")
    return text[:BODY_LIMIT], names


_VIA_RE = re.compile(r"^\s*['\"]?(.*?)['\"]?\s+via\s+(.+?)\s*$", re.I)


def _parse_from(hdrs):
    """Return (from_name, from_email, via_group).

    Google Groups rewrites "Bob <bob@vendor.com>" posted to purchasing@ as
    "'Bob' via Purchasing <purchasing@...>", with the real sender in
    X-Original-Sender / Reply-To. via_group is the group address; from_email
    is the real sender when we can recover it, so known-sender checks and
    "drop the original sender" apply to the person, not the group.
    """
    name, addr = parseaddr(_first(hdrs, "From"))
    addr = addr.lower()
    m = _VIA_RE.match(name or "")
    if not m:
        return name, addr, None
    via = addr
    real_name = m.group(1).strip()
    orig = _first(hdrs, "X-Original-Sender").strip().lower()
    if not orig:
        rt = _addrs([_first(hdrs, "Reply-To")])
        orig = rt[0] if rt and rt[0] != via else ""
    return real_name, (orig or addr), via


def _jack_in_thread(thread_id, before_ts_ms):
    key = (thread_id, before_ts_ms)
    if key in _jack_thread_cache:
        return _jack_thread_cache[key]
    jack = _jack_addresses()
    t = service().users().threads().get(
        userId="me", id=thread_id, format="metadata",
        metadataHeaders=["From"]).execute(num_retries=5)
    found = False
    for m in t.get("messages", []):
        if int(m.get("internalDate", 0)) >= before_ts_ms:
            continue
        sender = parseaddr(_first(_headers(m.get("payload", {})), "From"))[1].lower()
        if "SENT" in (m.get("labelIds") or []) or sender in jack:
            found = True
            break
    _jack_thread_cache[key] = found
    return found


def fetch_message(msg_id):
    """Normalize one Gmail message into the spec's Msg dict."""
    m = service().users().messages().get(
        userId="me", id=msg_id, format="full").execute(num_retries=5)
    payload = m.get("payload", {})
    hdrs = _headers(payload)
    from_name, from_email, via = _parse_from(hdrs)
    label_ids = m.get("labelIds", []) or []
    by_id = _labels()["by_id"]
    if any(l not in by_id for l in label_ids):
        by_id = _labels(refresh=True)["by_id"]
    body, attachments = _body_and_attachments(payload)
    internal_ms = int(m.get("internalDate", 0))
    reply_to = _addrs([_first(hdrs, "Reply-To")])
    return {
        "id": m["id"],
        "thread_id": m.get("threadId", ""),
        "internal_ts": internal_ms // 1000,
        "from_name": from_name or "",
        "from_email": from_email,
        "to": _addrs(hdrs.get("to")),
        "cc": _addrs(hdrs.get("cc")),
        "delivered_to": _addrs(hdrs.get("delivered-to")),
        "reply_to": reply_to[0] if reply_to else None,
        "subject": _first(hdrs, "Subject"),
        "date": _first(hdrs, "Date"),
        "label_ids": label_ids,
        "label_names": [by_id.get(l, l) for l in label_ids],
        "in_inbox": "INBOX" in label_ids,
        "is_unread": "UNREAD" in label_ids,
        "via_group": via,
        "list_unsubscribe": bool(_first(hdrs, "List-Unsubscribe")),
        "body_text": body,
        "attachment_names": attachments,
        "jack_in_thread": _jack_in_thread(m.get("threadId", m["id"]), internal_ms),
    }


# ---------- candidates ----------

def list_candidates(lookback_days):
    """Unreviewed mail from the last `lookback_days` that is in the inbox or
    under one of Jack's alias filters (Filters/*), oldest first. Skip labels are excluded in the query and again by label
    id, since a Gmail search-name mismatch would otherwise let Jack's
    filtered purchasing/junk mail through."""
    skip_ids = _skip_label_ids()
    by_id = _labels()["by_id"]
    q = [f"newer_than:{int(lookback_days)}d", "-label:jackbot",
         "-in:sent", "-in:drafts", "-in:chats", "-in:spam", "-in:trash", "-from:me"]
    q += [f"-from:{a}" for a in sorted(_jack_addresses())]
    q += [f"-label:{_search_name(by_id[i])}" for i in sorted(skip_ids) if i in by_id]
    query = " ".join(q)

    ids, token = [], None
    while True:
        resp = service().users().messages().list(
            userId="me", q=query, maxResults=500, pageToken=token,
            includeSpamTrash=False).execute(num_retries=5)
        ids += [m["id"] for m in resp.get("messages", [])]
        token = resp.get("nextPageToken")
        if not token:
            break

    reviewed = _labels()["by_name"].get("Jackbot")
    out = []
    for mid in ids:
        try:
            meta = service().users().messages().get(
                userId="me", id=mid, format="minimal").execute(num_retries=5)
        except Exception as e:
            # Deleted between list and get, or a transient error: skip it
            # (the next run retries) rather than abort the whole pass.
            print(f"[email_triage] candidate {mid} unreadable: {e}")
            continue
        labels = set(meta.get("labelIds") or [])
        if labels & skip_ids or labels & {"SENT", "DRAFT", "SPAM", "TRASH"}:
            continue
        if reviewed and reviewed in labels:
            continue
        # Only the inbox and Jack's alias filters (Filters/*). Anything else
        # outside the inbox is mail Jack archived himself; the 2026-11-09
        # backlog run "kept" 471 of those and pulled them back into his inbox.
        if "INBOX" not in labels and not any(
                by_id.get(l, "").startswith("Filters/") for l in labels):
            continue
        out.append((int(meta.get("internalDate", 0)), mid))
    return [mid for _, mid in sorted(out)]


# ---------- directory ----------

def _domain_users():
    """Every internal address in the Workspace directory (People API, under
    the directory.readonly scope google_client already uses). Falls back to
    the internal addresses in config.people."""
    internal = _internal_domains()
    try:
        creds = _credentials(("https://www.googleapis.com/auth/directory.readonly",))
        people = build("people", "v1", credentials=creds, cache_discovery=False).people()
        out, token = set(), None
        while True:
            resp = people.listDirectoryPeople(
                sources=["DIRECTORY_SOURCE_TYPE_DOMAIN_PROFILE"],
                readMask="emailAddresses", pageSize=500,
                pageToken=token).execute(num_retries=5)
            for person in resp.get("people", []):
                for e in person.get("emailAddresses", []):
                    addr = (e.get("value") or "").lower()
                    if _domain(addr) in internal:
                        out.add(addr)
            token = resp.get("nextPageToken")
            if not token:
                break
        if out:
            return sorted(out)
    except Exception:
        pass
    return sorted({(p.get("email") or "").lower() for p in _cfg().get("people", []) or []
                   if _domain(p.get("email") or "") in internal})


def group_members():
    """{group address or alias: [member emails]} for every Workspace group,
    nested groups flattened. Cached for an hour."""
    with _lock:
        if _group_cache["data"] is not None and time.time() - _group_cache["ts"] < GROUP_TTL:
            return _group_cache["data"]
    d = _directory()
    groups, token = [], None
    while True:
        resp = d.groups().list(customer="my_customer", maxResults=200,
                               pageToken=token).execute(num_retries=5)
        groups += resp.get("groups", [])
        token = resp.get("nextPageToken")
        if not token:
            break

    direct = {}
    for g in groups:
        members, token = [], None
        while True:
            resp = d.members().list(groupKey=g["id"], maxResults=200,
                                    pageToken=token).execute(num_retries=5)
            members += resp.get("members", [])
            token = resp.get("nextPageToken")
            if not token:
                break
        emails = [(m.get("email") or "").lower() for m in members if m.get("email")]
        # A CUSTOMER member (all@) means "everyone in the org" and has no
        # address; expand it, or all@ looks like a 5-person list.
        if any(m.get("type") == "CUSTOMER" for m in members):
            emails += _domain_users()
        direct[g["email"].lower()] = emails

    def flatten(addr, seen):
        out = set()
        for m in direct.get(addr, []):
            if m in direct and m not in seen:
                out |= flatten(m, seen | {m})
            else:
                out.add(m)
        return out

    data = {}
    for g in groups:
        primary = g["email"].lower()
        members = sorted(flatten(primary, {primary}))
        for a in [primary] + list(g.get("aliases", [])) + list(g.get("nonEditableAliases", [])):
            data[a.lower()] = members
    with _lock:
        _group_cache.update(ts=time.time(), data=data)
    return data


# ---------- known senders ----------

def _sent_exists(target):
    q = f"in:sent {{to:{target} cc:{target} bcc:{target}}}"
    resp = service().users().messages().list(
        userId="me", q=q, maxResults=1).execute(num_retries=5)
    return bool(resp.get("messages"))


def sender_is_known(email_addr):
    """True if Jack has ever sent mail to this address, or (for non-freemail
    domains) to anyone at its domain. Internal senders are always known."""
    addr = (email_addr or "").strip().lower()
    if "@" not in addr:
        return False
    with _lock:
        if addr in _known_cache:
            return _known_cache[addr]
    dom = _domain(addr)
    if dom in _internal_domains():
        known = True
    else:
        known = _sent_exists(addr)
        if not known and dom not in FREEMAIL:
            key = "@" + dom
            with _lock:
                cached = _known_cache.get(key)
            if cached is None:
                cached = _sent_exists(dom)
                with _lock:
                    _known_cache[key] = cached
            known = cached
    with _lock:
        _known_cache[addr] = known
    return known


# ---------- writes ----------

def _check_recipients(recipients):
    if not recipients:
        raise ValueError("forward() called with no recipients")
    internal, green = _internal_domains(), _greenlist()
    bad = [r for r in recipients
           if _domain(r) not in internal and r.lower() not in green]
    if bad:
        raise ValueError(f"refusing to forward outside BST to non-greenlisted: {bad}")


def _forward_bodies(msg, note):
    intro = note.strip() if note and note.strip() else FORWARD_PREAMBLE
    fields = [
        ("From", f"{msg.get('from_name') or ''} <{msg.get('from_email', '')}>".strip()),
        ("Date", msg.get("date", "")),
        ("Subject", msg.get("subject", "")),
        ("To", ", ".join(msg.get("to") or [])),
    ]
    if msg.get("cc"):
        fields.append(("Cc", ", ".join(msg["cc"])))
    body = msg.get("body_text", "")
    text = (intro + "\n\n---------- Forwarded message ---------\n"
            + "\n".join(f"{k}: {v}" for k, v in fields) + "\n\n" + body + "\n")
    esc = _html.escape
    htm = (
        "<div>" + "<br><br>".join(esc(p).replace("\n", "<br>") for p in intro.split("\n\n"))
        + "</div><br><div>---------- Forwarded message ---------<br>"
        + "<br>".join(f"{k}: {esc(v)}" for k, v in fields)
        + "</div><br><div style=\"white-space:pre-wrap\">" + esc(body) + "</div>"
    )
    return text, htm


def build_forward_mime(msg, recipients, note, raw_bytes):
    """The forward as RFC 822 bytes: text+HTML body, original attached as
    message/rfc822 (original.eml) so attachments and formatting survive."""
    _check_recipients(recipients)
    out = EmailMessage(policy=policy.SMTP)
    out["From"] = f"Jack Elston <{JACK}>"
    out["To"] = ", ".join(recipients)
    out["Subject"] = "Fwd: " + (msg.get("subject") or "")
    out["Date"] = formatdate(localtime=False)
    out["Message-ID"] = make_msgid(domain="blackswifttech.com")
    out["X-Jackbot-Source-Id"] = msg["id"]
    text, htm = _forward_bodies(msg, note)
    out.set_content(text)
    out.add_alternative(htm, subtype="html")
    out.make_mixed()

    att = MIMEPart(policy=policy.SMTP)
    att["Content-Type"] = "message/rfc822"
    att["Content-Disposition"] = 'attachment; filename="original.eml"'
    att.set_payload([email.message_from_bytes(raw_bytes, policy=policy.compat32)])
    out.attach(att)
    return out.as_bytes()


def _raw(msg_id):
    m = service().users().messages().get(
        userId="me", id=msg_id, format="raw").execute(num_retries=5)
    return base64.urlsafe_b64decode(m["raw"] + "=" * (-len(m["raw"]) % 4))


class SendUncertain(Exception):
    """The send request went out but its outcome is unknown (5xx, timeout,
    dropped connection). Gmail may have delivered it, so the caller must not
    retry — that is how a teammate gets the same forward twice."""


def forward(msg, recipients, note=None):
    """Send `msg` to `recipients` from Jack. Returns the sent message id.

    The send itself is never retried: googleapiclient's num_retries replays a
    POST after a 5xx or a socket error, either of which can follow a
    successful delivery. A 4xx is a definite rejection and raises HttpError
    (safe to retry next run); anything ambiguous raises SendUncertain."""
    from googleapiclient.errors import HttpError

    _check_recipients(recipients)
    raw = build_forward_mime(msg, recipients, note, _raw(msg["id"]))
    req = service().users().messages().send(userId="me", body={
        "raw": base64.urlsafe_b64encode(raw).decode()})
    try:
        sent = req.execute(num_retries=0)
    except HttpError as e:
        status = getattr(getattr(e, "resp", None), "status", 0) or 0
        if 400 <= int(status) < 500:
            raise
        raise SendUncertain(f"send outcome unknown: {e}") from e
    except Exception as e:
        raise SendUncertain(f"send outcome unknown: {e}") from e
    return sent["id"]


_FORBIDDEN = {"UNREAD", "TRASH"}


def modify(msg_id, add=None, remove=None):
    """Add/remove labels by id or name. UNREAD and TRASH are off-limits."""
    add_ids = _resolve_label_ids(add)
    remove_ids = _resolve_label_ids(remove)
    if _FORBIDDEN & (set(add_ids) | set(remove_ids)):
        raise ValueError("email triage never changes UNREAD or TRASH")
    if not add_ids and not remove_ids:
        return
    service().users().messages().modify(userId="me", id=msg_id, body={
        "addLabelIds": add_ids, "removeLabelIds": remove_ids}).execute(num_retries=5)


def build_summary_mime(subject, html, text):
    out = EmailMessage(policy=policy.SMTP)
    out["From"] = f"Jack Bot (email triage) <{JACK}>"
    out["To"] = JACK
    out["Subject"] = subject
    out["Date"] = formatdate(localtime=False)
    out["Message-ID"] = make_msgid(domain="blackswifttech.com")
    out.set_content(text)
    out.add_alternative(html, subtype="html")
    return out.as_bytes()


def insert_summary(subject, html, text):
    """Drop the daily summary into Jack's inbox, unread. messages.insert never
    sends anything outside the mailbox."""
    raw = build_summary_mime(subject, html, text)
    resp = service().users().messages().insert(
        userId="me", internalDateSource="dateHeader",
        body={"raw": base64.urlsafe_b64encode(raw).decode(),
              "labelIds": ["INBOX", "UNREAD"]}).execute(num_retries=5)
    return resp["id"]
