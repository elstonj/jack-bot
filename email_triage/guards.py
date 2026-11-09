"""Deterministic safety rules applied on top of the email-triage classifier.

`classify.classify()` is a model call; it is right most of the time and wrong
in ways that cost real money or trust when it isn't. `apply()` runs after it,
is pure (no Gmail, no network, no clock other than `time.time()`), and can only
make a decision *safer*: block spam, force a keep, or strip forward
recipients. It never adds a recipient and never turns a keep into an archive.
Addresses are compared after alias canonicalization (config alias_map,
bst.aero -> blackswifttech.com), so Cory writing from krateosky.com counts as
Cory. Every override is written to `guard_notes` so the daily summary shows Jack
exactly where code overruled the model.

Rules, in the order they run:

  1. Forced keep. Subject + first 1500 body chars matched against account-
     security and payment-fraud patterns (new sign-in, unrecognized device,
     suspicious activity, new/changed bank details, password expiry, wire
     transfer, domain expiry, ...). Jack is head of IT; these are his. The
     2026-11-09 manual review of 457 unread messages found the must-keep misses
     were exactly this class: Capital One "suspicious activity", four QuickBooks
     "New bank details added", Deel "entity could not be verified" and
     "new login from an unrecognized device", Google "Security alert", PIEE and
     NASA password expirations. A payee bank-detail change archived or
     forwarded by mistake is how invoice fraud succeeds, so this cannot be left
     to a probability. Forced keep also blocks spam: a real security alert can
     look like a phishing blast, and Jack is the one who should tell them apart.
  2. Spam gate. Moving mail to Spam trains Gmail's filter for *everyone* in the
     domain, and Gmail's spam filter already ate ~500 purchasing@ messages a
     month before Jack's filters were tuned. So spam is allowed only for a
     high-confidence (>= 0.9) cold solicitation from a stranger: sender never
     written to (`ctx["known_sender"]`), not internal / Krateo Sky / gov / mil /
     edu / ac.xx / mod.uk, not delivered via a Google group, not a thread Jack
     replied in, and not addressed to a group alias. A blocked spam falls back
     to archive when it has List-Unsubscribe (bulk mail) and keep otherwise.
  3. Forward filtering. Recipients must be in config.people; Jack, the sender,
     and anyone who already has the message (To/Cc/Delivered-To, or a member of
     a group it went through) are dropped so nobody gets a duplicate; non-BST
     addresses must be on the external greenlist (Shelly, Pam); Pam only for
     major media; hiring goes only to Cory, who owns all of it.
  4. Age limit. Nothing older than FORWARD_MAX_AGE_DAYS (default 14) is
     forwarded — a teammate getting a three-week-old email "from Jack" reads as
     a stale ask, not a handoff.
  5. Live conversation. An archive becomes a keep when Jack has already
     replied in the thread and this message is addressed To him: it is a reply
     to Jack, whoever else is cc'd. Only ever adds a keep.
  6. Archive fallback. Not kept, not spam, no recipients left -> archive
     (spec rule 4). The guard notes say which recipients were dropped and why,
     so an archive that should have been a forward shows up in the daily
     summary for Jack to correct.
"""

import copy
import os
import re
import time

_DEFAULT_JACK = {"elstonj@blackswifttech.com", "jack.elston@blackswifttech.com",
                 "elstonj@bst.aero"}
_DEFAULT_INTERNAL = ("blackswifttech.com", "bst.aero")
_DEFAULT_GREENLIST = ("shelly@krateosky.com", "pam@krateosky.com")
_PARTNER_DOMAINS = ("krateosky.com",)
_DEFAULT_CORY = "cory.dixon@blackswifttech.com"
_DEFAULT_PAM = "pam@krateosky.com"

SPAM_MIN_CONFIDENCE = 0.9
KEEP_SCAN_CHARS = 1500

_PUBLIC_SECTOR = re.compile(
    r"(\.(gov|mil|edu)$)|(\.(gov|mil|ac|edu)\.[a-z]{2}$)|((^|\.)mod\.uk$)")

FORCED_KEEP_PATTERNS = [
    ("security alert", r"security alert"),
    ("new sign-in", r"new sign[- ]?in"),
    ("unrecognized device", r"unrecogni[sz]ed device"),
    ("suspicious activity", r"suspicious activity"),
    ("account restricted", r"account (is )?restricted"),
    ("new bank details", r"new bank details"),
    ("bank details changed", r"bank details (were |have been )?(added|changed)"),
    ("could not be verified", r"could not be verified"),
    ("password expiring", r"password (will )?expir"),
    ("signature required", r"action required.*(signature|sign)"),
    ("wire transfer", r"wire transfer"),
    ("payment failed", r"payment (has )?failed"),
    ("domain expiry", r"domain (expir|renew)"),
]
_FORCED_KEEP = [(label, re.compile(p, re.I | re.S))
                for label, p in FORCED_KEEP_PATTERNS]

_HIRING = re.compile(r"hir(e|ing)|recruit|candidate|interview|applicant", re.I)


def _lower(s):
    return (s or "").strip().lower()


def _domain(email):
    email = _lower(email)
    return email.rsplit("@", 1)[1] if "@" in email else ""


def _in_domains(domain, domains):
    return any(domain == d or domain.endswith("." + d) for d in domains)


def _emails_in(value):
    """Every address-looking string in a config value (str / list / dict)."""
    out = set()
    if isinstance(value, str):
        if "@" in value:
            out.add(_lower(value))
    elif isinstance(value, dict):
        for v in value.values():
            out |= _emails_in(v)
    elif isinstance(value, (list, tuple, set)):
        for v in value:
            out |= _emails_in(v)
    return out


def _people(cfg):
    people = cfg.get("people") or []
    if isinstance(people, dict):
        people = [dict(v, name=v.get("name", k)) if isinstance(v, dict) else
                  {"name": k, "email": v} for k, v in people.items()]
    return [p for p in people if isinstance(p, dict) and p.get("email")]


def _person_email(people, first_name, default):
    for p in people:
        if _lower(p.get("name")).split(" ")[:1] == [first_name]:
            return _lower(p["email"])
    return default


def _settings(ctx):
    cfg = (ctx or {}).get("config") or {}
    jack = set(_DEFAULT_JACK)
    for k, v in cfg.items():
        if k.lower().startswith("jack"):
            jack |= _emails_in(v)
    people = _people(cfg)
    aliases = {_lower(k): _lower(v) for k, v in (cfg.get("alias_map") or {}).items()}
    for p in people:
        for a in p.get("aliases") or []:
            aliases.setdefault(_lower(a), _lower(p["email"]))
    return {
        "aliases": aliases,
        "domain_aliases": {_lower(k): _lower(v) for k, v in
                           (cfg.get("domain_aliases") or {}).items()},
        "jack": jack,
        "internal": tuple(_lower(d) for d in
                          (cfg.get("internal_domains") or _DEFAULT_INTERNAL)),
        "greenlist": {_lower(e) for e in
                      (cfg.get("external_greenlist") or _DEFAULT_GREENLIST)},
        "people": {_lower(p["email"]) for p in people},
        "cory": _person_email(people, "cory", _DEFAULT_CORY),
        "pam": _person_email(people, "pam", _DEFAULT_PAM),
    }


def _canon(addr, s):
    """One spelling per mailbox: person aliases -> routing address, bst.aero ->
    blackswifttech.com. Cory writes from cory@krateosky.com; comparing raw
    strings let a thread he was already on (or sent) be forwarded back to
    cory.dixon@ — 10 such forwards in the 2026-11-09 unread replay."""
    a = _lower(addr)
    if a in s["aliases"]:
        return s["aliases"][a]
    if "@" in a:
        local, dom = a.rsplit("@", 1)
        if dom in s["domain_aliases"]:
            a = f"{local}@{s['domain_aliases'][dom]}"
    return s["aliases"].get(a, a)


def _group_members(ctx, s=None):
    raw = (ctx or {}).get("group_members") or {}
    c = (lambda a: _canon(a, s)) if s else _lower
    return {c(g): {c(m) for m in (members or [])} for g, members in raw.items()}


def _recipients(msg, s=None):
    c = (lambda a: _canon(a, s)) if s else _lower
    return {c(a) for field in ("to", "cc", "delivered_to")
            for a in (msg.get(field) or []) if a}


def _forced_keep_hits(msg):
    text = f"{msg.get('subject') or ''}\n{(msg.get('body_text') or '')[:KEEP_SCAN_CHARS]}"
    return [label for label, rx in _FORCED_KEEP if rx.search(text)]


def _spam_blockers(msg, ctx, s, groups):
    """Reasons a spam verdict may not stand; empty list means spam is allowed."""
    reasons = []
    d = (ctx or {}).get("_decision", {})
    try:
        conf = float(d.get("spam_confidence") or 0)
    except (TypeError, ValueError):
        conf = 0.0
    if conf < SPAM_MIN_CONFIDENCE:
        reasons.append(f"confidence {conf:.2f} < {SPAM_MIN_CONFIDENCE}")
    # Missing known_sender is treated as known: unknown must be affirmative.
    if (ctx or {}).get("known_sender", True):
        reasons.append("sender is known (Jack has written to them)")
    dom = _domain(msg.get("from_email"))
    if not dom:
        reasons.append("no sender domain")
    elif _in_domains(dom, s["internal"]):
        reasons.append(f"internal sender ({dom})")
    elif _in_domains(dom, _PARTNER_DOMAINS):
        reasons.append(f"Krateo Sky sender ({dom})")
    elif _PUBLIC_SECTOR.search(dom):
        reasons.append(f"public-sector sender ({dom})")
    if msg.get("via_group"):
        reasons.append(f"arrived via group {msg['via_group']}")
    if msg.get("jack_in_thread"):
        reasons.append("Jack replied in this thread")
    group_hits = sorted(_recipients(msg, s) & set(groups))
    if group_hits:
        reasons.append(f"addressed to group {', '.join(group_hits)}")
    return reasons


def _is_old(msg, now):
    ts = msg.get("internal_ts")
    if not ts:
        return False, 0.0
    try:
        max_days = float(os.environ.get("FORWARD_MAX_AGE_DAYS", "14"))
    except ValueError:
        max_days = 14.0
    age_days = (now - float(ts)) / 86400.0
    return age_days > max_days, age_days


def apply(msg, decision, ctx):
    """Return the final decision after the deterministic rules. Pure."""
    d = copy.deepcopy(decision or {})
    msg = msg or {}
    ctx = ctx or {}
    notes = list(d.get("guard_notes") or [])
    s = _settings(ctx)
    groups = _group_members(ctx, s)

    d["keep_for_jack"] = bool(d.get("keep_for_jack"))
    d["is_spam"] = bool(d.get("is_spam"))
    d["major_media"] = bool(d.get("major_media"))
    intended = [_canon(a, s) for a in (d.get("forward_to") or []) if a]

    # 1. Forced keep.
    hits = _forced_keep_hits(msg)
    if hits:
        if not d["keep_for_jack"]:
            notes.append(f"forced keep: matched {', '.join(hits)}")
        d["keep_for_jack"] = True
        if d["is_spam"]:
            notes.append(f"spam blocked: forced-keep pattern ({', '.join(hits)})")
            d["is_spam"] = False

    # 2. Spam gate.
    if d["is_spam"]:
        blockers = _spam_blockers(msg, dict(ctx, _decision=d), s, groups)
        if blockers:
            d["is_spam"] = False
            if d["keep_for_jack"]:
                # The model asked for keep as well as spam; a keep is never
                # downgraded, so say so rather than claim an archive.
                fallback = "keep (model also asked to keep)"
            elif msg.get("list_unsubscribe"):
                fallback = "archive (bulk mail)"
            else:
                d["keep_for_jack"] = True
                fallback = "keep"
            notes.append(f"spam blocked -> {fallback}: {'; '.join(blockers)}")

    if d["is_spam"]:
        if intended:
            notes.append(f"spam: dropped forward to {', '.join(intended)}")
        d["keep_for_jack"] = False
        d["forward_to"] = []
        d["action"] = "spam"
        d["guard_notes"] = notes
        return d

    # 3. Forward filtering.
    sender = _canon(msg.get("from_email"), s)
    already = _recipients(msg, s)
    via = _canon(msg.get("via_group"), s) if msg.get("via_group") else ""
    covered = set()
    for g in already | ({via} if via else set()):
        covered |= groups.get(g, set())

    kept = []
    for a in intended:
        if a in kept:
            continue
        if a not in s["people"]:
            notes.append(f"forward: dropped {a} (not in config.people)")
        elif a in s["jack"]:
            notes.append(f"forward: dropped {a} (Jack)")
        elif a == sender:
            notes.append(f"forward: dropped {a} (original sender)")
        elif a in already:
            notes.append(f"forward: dropped {a} (already on To/Cc/Delivered-To)")
        elif a in covered:
            notes.append(f"forward: dropped {a} (member of a group it was sent to)")
        elif (not _in_domains(_domain(a), s["internal"])
              and a not in s["greenlist"]):
            notes.append(f"forward: dropped {a} (external, not greenlisted)")
        elif a == s["pam"] and not d["major_media"]:
            notes.append(f"forward: dropped {a} (not major media)")
        else:
            kept.append(a)

    if kept and _HIRING.search(d.get("category") or ""):
        if kept != [s["cory"]]:
            others = [a for a in kept if a != s["cory"]]
            cory_ok = (s["cory"] in s["people"] and s["cory"] != sender
                       and s["cory"] not in already and s["cory"] not in covered)
            kept = [s["cory"]] if cory_ok else []
            notes.append(f"forward: hiring goes only to Cory "
                         f"(dropped {', '.join(others)}"
                         f"{'' if cory_ok else '; Cory already has it'})")

    # 4. Age limit.
    if kept:
        too_old, age = _is_old(msg, time.time())
        if too_old:
            notes.append(f"forward blocked: message is {age:.0f} days old "
                         f"(> FORWARD_MAX_AGE_DAYS); not sent to {', '.join(kept)}")
            kept = []
    d["forward_to"] = kept

    # 5. Live conversation with Jack. The model often reads "a teammate is on
    # the thread" as "Jack can let go", and rule 3 then drops that teammate as
    # already-on-thread, leaving an archive. When Jack has already replied in
    # the thread and this message is addressed To him (not just Cc), it is a
    # reply to Jack; archiving it hides it from him. The 2026-11-09 keep-recall
    # backtest found 25 of 32 misses were this archive, most answered by Jack
    # within two hours.
    if (not d["keep_for_jack"] and not kept and msg.get("jack_in_thread")
            and not msg.get("list_unsubscribe")
            and {_canon(a, s) for a in (msg.get("to") or [])} & s["jack"]):
        d["keep_for_jack"] = True
        notes.append("kept: Jack is in To on a thread he has replied in")

    # 6. Archive fallback.
    if not d["keep_for_jack"] and not kept and intended:
        notes.append("archived: no forward recipients left")

    if d["keep_for_jack"]:
        d["action"] = "keep+forward" if kept else "keep"
    elif kept:
        d["action"] = "forward"
    else:
        d["action"] = "archive"
    d["guard_notes"] = notes
    return d
