"""Offline regression suite for email triage (email_triage/).

The triage job acts on Jack's real mailbox: it forwards mail to teammates,
archives it, and moves solicitations to Spam. A wrong guard sends a payroll
letter to a vendor or buries a bank-detail-change alert, so every deterministic
rule in guards.py is pinned here, along with the runner's write ordering
(Reviewed before the send, rollback when the send fails, UNREAD never touched),
dryrun making zero writes, the daily summary's grouping and counts, and the
forward note text Jack asked for.

Gmail and the classifier are replaced with fakes, and sockets are blocked, so
nothing here can reach the network or the real mailbox. Needs no credentials.
Run: python test_email_triage.py
"""

import base64
import copy
import email
import email.policy
import html as html_lib
import json
import os
import re
import socket
import tempfile
import time

os.environ.pop("FORWARD_MAX_AGE_DAYS", None)
os.environ.pop("JACKBOT_EMAIL_TRIAGE", None)

from email_triage import classify, config, gmail_ops, guards, runner, summary  # noqa: E402

# Belt and braces: even if a module loaded .env on import, nothing below may
# build real credentials or open a socket.
for _var in ("GOOGLE_SERVICE_ACCOUNT_JSON", "ANTHROPIC_API_KEY"):
    os.environ.pop(_var, None)


def _no_network(*a, **k):
    raise OSError("network blocked in test_email_triage")


socket.socket.connect = _no_network
socket.create_connection = _no_network

FAILURES = []


def check(label, got, want):
    ok = got == want
    print(f"  {'ok  ' if ok else 'FAIL'} {label}")
    if not ok:
        print(f"       got:  {got!r}\n       want: {want!r}")
        FAILURES.append(label)


JACK = "elstonj@blackswifttech.com"
LYNN = "lynn.regnier@blackswifttech.com"
MEREDITH = "meredith.needham@blackswifttech.com"
CORY = "cory.dixon@blackswifttech.com"
BECK = "beck.cotter@blackswifttech.com"
STACHURA = "stachura@blackswifttech.com"
SAM = "sam.hild@blackswifttech.com"
BEN = "ben.busby@blackswifttech.com"
JOSH = "josh.fromm@blackswifttech.com"
SHELLY = "shelly@krateosky.com"
PAM = "pam@krateosky.com"

GROUPS = {
    "purchasing@blackswifttech.com": [JACK, LYNN, MEREDITH],
    "invoices@blackswifttech.com": [JACK, MEREDITH],
    "sales@blackswifttech.com": [BECK, JACK, STACHURA],
    "info@blackswifttech.com": [BECK, CORY, JACK, MEREDITH],
    "careers@blackswifttech.com": [CORY, JACK],
    "operations@blackswifttech.com": [JACK, MEREDITH],
}

NOTE = ("Forwarded automatically from Jack's inbox. Please take a look — "
        "disregard it if it's not relevant, act on it if it is. If I'm sending "
        "you things that aren't relevant to you, please message me about it. "
        "I'm trying my best to remove myself as a blocker on the information "
        "flowing into and out of Black Swift.")

CFG = config.load_config()


def norm(text):
    return re.sub(r"\s+", " ", text or "").strip()


def html_to_text(markup):
    return norm(html_lib.unescape(re.sub(r"<[^>]+>", " ", markup or "")))


def make_msg(**kw):
    m = {
        "id": "m1", "thread_id": "t1", "internal_ts": int(time.time()) - 60,
        "from_name": "Vendor Rep", "from_email": "rep@vendor-example.com",
        "to": [JACK], "cc": [], "delivered_to": [JACK], "reply_to": None,
        "subject": "Hello", "date": "Mon, 9 Nov 2026 08:00:00 -0700",
        "label_ids": ["INBOX", "UNREAD"], "label_names": ["INBOX", "UNREAD"],
        "in_inbox": True, "is_unread": True, "via_group": None,
        "list_unsubscribe": False, "body_text": "", "attachment_names": [],
        "jack_in_thread": False,
    }
    m.update(kw)
    if not m["in_inbox"]:
        m["label_ids"] = [x for x in m["label_ids"] if x != "INBOX"]
        m["label_names"] = [x for x in m["label_names"] if x != "INBOX"]
    return m


def make_dec(**kw):
    d = {"keep_for_jack": False, "forward_to": [], "is_spam": False,
         "spam_confidence": 0.0, "major_media": False, "category": "misc",
         "reason": "test reason", "summary": "test summary"}
    d.update(kw)
    return d


def ctx(known=False, cfg=None):
    return {"known_sender": known, "group_members": GROUPS,
            "config": cfg if cfg is not None else CFG}


def run_guard(msg=None, known=False, cfg=None, **dec):
    return guards.apply(msg or make_msg(), make_dec(**dec), ctx(known, cfg))


def fwd(d):
    return sorted(a.lower() for a in d.get("forward_to") or [])


def is_archive(d):
    return (not d["keep_for_jack"] and not d["is_spam"]
            and not d.get("forward_to"))


# --- guard rule 1: spam --------------------------------------------------

SPAMMY = dict(is_spam=True, spam_confidence=0.97, category="cold-financing")


def test_spam_guards():
    print("spam guard")
    spam_from = make_msg(from_email="kyle@firstlinecap-example.biz",
                         list_unsubscribe=True,
                         subject="Is Existing Business Debt Limiting Your Cash Flow?")
    d = run_guard(spam_from, **SPAMMY)
    check("cold solicitation from unknown sender stays spam", d["is_spam"], True)

    d = run_guard(spam_from, **dict(SPAMMY, spam_confidence=0.85))
    check("confidence below 0.9 blocked", d["is_spam"], False)
    check("blocked spam w/ unsubscribe archives", is_archive(d), True)
    check("blocked spam leaves guard note", bool(d.get("guard_notes")), True)

    d = run_guard(spam_from, known=True, **SPAMMY)
    check("known sender never spam", d["is_spam"], False)
    check("known sender w/ unsubscribe archives", is_archive(d), True)

    no_unsub = make_msg(from_email="kyle@firstlinecap-example.biz",
                        list_unsubscribe=False)
    d = run_guard(no_unsub, known=True, **SPAMMY)
    check("blocked spam w/o unsubscribe kept for Jack", d["keep_for_jack"], True)
    check("blocked spam w/o unsubscribe not spam", d["is_spam"], False)

    for addr in ("ops@noaa.gov", "contracting@navy.mil", "prof@colorado.edu",
                 "office@dstl.gov.uk", "buyer@des.mod.uk", "lab@ox.ac.uk",
                 "beck.cotter@blackswifttech.com", "someone@bst.aero",
                 "pam@krateosky.com", "intern@krateosky.com"):
        d = run_guard(make_msg(from_email=addr, list_unsubscribe=True), **SPAMMY)
        check(f"{addr} never spam", d["is_spam"], False)

    d = run_guard(make_msg(from_email="kyle@spam-example.biz", list_unsubscribe=True,
                           via_group="purchasing@blackswifttech.com"), **SPAMMY)
    check("via_group never spam", d["is_spam"], False)

    d = run_guard(make_msg(from_email="kyle@spam-example.biz", list_unsubscribe=True,
                           jack_in_thread=True), **SPAMMY)
    check("jack_in_thread never spam", d["is_spam"], False)

    d = run_guard(make_msg(from_email="kyle@spam-example.biz", list_unsubscribe=True,
                           to=["sales@blackswifttech.com"]), **SPAMMY)
    check("addressed to group alias (To) never spam", d["is_spam"], False)
    d = run_guard(make_msg(from_email="kyle@spam-example.biz", list_unsubscribe=True,
                           cc=["info@blackswifttech.com"]), **SPAMMY)
    check("addressed to group alias (Cc) never spam", d["is_spam"], False)


# --- guard rule 2: forced keep -------------------------------------------

MUST_KEEP = [
    ("'Deel' via Operations", "operations@blackswifttech.com",
     "Your entity could not be verified"),
    ("Capital One", "capitalone@notification.capitalone.com",
     "Call us ASAP to resolve suspicious activity on your account"),
    ("Quickbooks Bill Pay", "sales@blackswifttech.com",
     "Black Swift Technologies LLC: New bank details added for Robert Powell"),
    ("Quickbooks Bill Pay", "sales@blackswifttech.com",
     "Black Swift Technologies LLC: New bank details added for Accordion Partners LLC"),
    ("PIEE", "operations@blackswifttech.com",
     "ACTION REQUIRED - PIEE Password Expires in 4 Days"),
    ("ICAM.Manager@nasa.gov", "icam.manager@nasa.gov",
     "[IdMAX] ACTION REQUIRED: Your profile password will expire in 5 day(s)."),
    ("Google", "no-reply@accounts.google.com", "Security alert"),
    ("Deel", "no-reply@deel.support", "New login from an unrecognized device"),
]


def test_forced_keep():
    print("forced keep")
    for name, sender, subject in MUST_KEEP:
        m = make_msg(from_name=name, from_email=sender, subject=subject,
                     list_unsubscribe=True)
        d = run_guard(m, keep_for_jack=False, category="automated")
        check(f"kept: {subject[:55]}", d["keep_for_jack"], True)
        check(f"  guard note recorded: {subject[:40]}", bool(d.get("guard_notes")), True)

    # A forced keep must also override a confident spam verdict.
    m = make_msg(from_email="no-reply@accounts.google.com", subject="Security alert",
                 list_unsubscribe=True)
    d = run_guard(m, **SPAMMY)
    check("forced keep beats spam: kept", d["keep_for_jack"], True)
    check("forced keep beats spam: not spam", d["is_spam"], False)

    for body_hit in ("We detected a new sign-in to your account from Linux.",
                     "Please initiate the wire transfer today.",
                     "Your payment failed for the Workspace subscription.",
                     "Your domain expires soon: renew blackswifttech.com"):
        d = run_guard(make_msg(subject="Notice", body_text=body_hit))
        check(f"body pattern forces keep: {body_hit[:40]}", d["keep_for_jack"], True)

    late = "x" * 1600 + " security alert"
    d = run_guard(make_msg(subject="Notice", body_text=late))
    check("pattern past first 1500 body chars ignored", d["keep_for_jack"], False)

    d = run_guard(make_msg(subject="Lunch on Friday", body_text="Tacos?"))
    check("ordinary mail not forced", d["keep_for_jack"], False)


# --- guard rule 3: forward filtering -------------------------------------

def test_forward_filtering():
    print("forward filtering")
    d = run_guard(forward_to=[MEREDITH])
    check("plain forward survives", fwd(d), [MEREDITH])

    d = run_guard(forward_to=["random.person@blackswifttech.com", "x@vendor.com", SAM])
    check("non-people dropped", fwd(d), [SAM])

    d = run_guard(forward_to=[JACK, "jack.elston@blackswifttech.com",
                              "elstonj@bst.aero", BEN])
    check("Jack's own addresses dropped", fwd(d), [BEN])

    d = run_guard(make_msg(from_email=SAM, from_name="Sam Hild"), forward_to=[SAM, BEN])
    check("original sender dropped", fwd(d), [BEN])

    d = run_guard(make_msg(to=[JACK, JOSH]), forward_to=[JOSH, SAM])
    check("already in To dropped", fwd(d), [SAM])
    d = run_guard(make_msg(cc=[JOSH]), forward_to=[JOSH, SAM])
    check("already in Cc dropped", fwd(d), [SAM])
    d = run_guard(make_msg(delivered_to=[JACK, JOSH]), forward_to=[JOSH, SAM])
    check("already in Delivered-To dropped", fwd(d), [SAM])

    d = run_guard(make_msg(to=["purchasing@blackswifttech.com"]),
                  forward_to=[MEREDITH, LYNN, SAM])
    check("purchasing@ members (Meredith, Lynn) dropped", fwd(d), [SAM])
    d = run_guard(make_msg(via_group="invoices@blackswifttech.com",
                           to=["invoices@blackswifttech.com"]),
                  forward_to=[MEREDITH, LYNN])
    check("invoices@ member Meredith dropped, Lynn kept", fwd(d), [LYNN])
    d = run_guard(make_msg(via_group="sales@blackswifttech.com"),
                  forward_to=[BECK, STACHURA, MEREDITH])
    check("via_group sales@ members dropped", fwd(d), [MEREDITH])
    d = run_guard(make_msg(cc=["operations@blackswifttech.com"]),
                  forward_to=[MEREDITH, LYNN])
    check("Cc operations@ member Meredith dropped", fwd(d), [LYNN])

    # Inject an external person who is not greenlisted; only the greenlist
    # may receive forwards outside BST.
    cfg = copy.deepcopy(CFG)
    outsider = {"name": "Outside Contractor", "email": "contractor@outside-example.com",
                "title": "Contractor", "handles": ["everything"]}
    people = cfg.get("people")
    if isinstance(people, dict):
        people[outsider["email"]] = outsider
    elif isinstance(people, list):
        people.append(outsider)
    d = run_guard(cfg=cfg, forward_to=["contractor@outside-example.com", SAM])
    check("external non-greenlist dropped", fwd(d), [SAM])

    d = run_guard(forward_to=[SHELLY])
    check("Shelly (greenlist) allowed", fwd(d), [SHELLY])
    d = run_guard(forward_to=[PAM, SHELLY], major_media=False)
    check("Pam dropped without major_media", fwd(d), [SHELLY])
    d = run_guard(forward_to=[PAM, SHELLY], major_media=True)
    check("Pam allowed with major_media", fwd(d), [PAM, SHELLY])

    d = run_guard(category="hiring", forward_to=[CORY, BECK, SAM])
    check("hiring forwards only to Cory", fwd(d), [CORY])


# --- guard rules 4 & 5: archive fallback, age limit ----------------------

def test_archive_and_age():
    print("archive fallback and age limit")
    d = run_guard(forward_to=["nobody@vendor.com", JACK])
    check("all forwards filtered -> archive", is_archive(d), True)
    d = run_guard()
    check("no keep, no forward, no spam -> archive", is_archive(d), True)
    d = run_guard(keep_for_jack=True, forward_to=[JACK])
    check("keep with no surviving forward stays kept", d["keep_for_jack"], True)

    old = make_msg(internal_ts=int(time.time()) - 20 * 86400)
    d = run_guard(old, forward_to=[MEREDITH])
    check("older than 14d never forwards", fwd(d), [])
    check("old unforwarded mail archives", is_archive(d), True)
    check("age limit noted", bool(d.get("guard_notes")), True)
    d = run_guard(old, keep_for_jack=True, forward_to=[MEREDITH])
    check("old mail can still be kept", d["keep_for_jack"], True)
    check("old kept mail still not forwarded", fwd(d), [])
    d = run_guard(make_msg(internal_ts=int(time.time()) - 13 * 86400),
                  forward_to=[MEREDITH])
    check("13d-old mail still forwards", fwd(d), [MEREDITH])
    old_spam = make_msg(internal_ts=int(time.time()) - 20 * 86400,
                        from_email="kyle@spam-example.biz", list_unsubscribe=True)
    d = run_guard(old_spam, **SPAMMY)
    check("age limit does not block spam", d["is_spam"], True)


# --- runner --------------------------------------------------------------

GMAIL_API = ("service", "group_members", "ensure_labels", "list_candidates",
             "fetch_message", "sender_is_known", "forward", "modify",
             "insert_summary")
WRITES = ("forward", "modify", "insert_summary", "ensure_labels")
# install() swaps these for fakes; test_forward_format restores the real ones.
REAL_GMAIL = {n: getattr(gmail_ops, n) for n in GMAIL_API}


class FakeGmail:
    def __init__(self, msgs, fail_send=(), known=()):
        self.msgs = {m["id"]: m for m in msgs}
        self.fail_send = set(fail_send)
        self.known = set(known)
        self.events = []

    def service(self, *a, **k):
        raise AssertionError("real Gmail service requested in a runner test")

    def group_members(self, *a, **k):
        return copy.deepcopy(GROUPS)

    def ensure_labels(self, names, *a, **k):
        self.events.append(("ensure_labels", list(names)))
        return {n: n for n in names}

    def list_candidates(self, *a, **k):
        self.events.append(("list_candidates",))
        return list(self.msgs)

    def fetch_message(self, msg_id, *a, **k):
        return copy.deepcopy(self.msgs[msg_id])

    def sender_is_known(self, addr, *a, **k):
        return (addr or "").lower() in self.known

    def forward(self, msg, recipients, note=None, *a, **k):
        mid = msg["id"] if isinstance(msg, dict) else msg
        self.events.append(("forward", mid, list(recipients), note))
        if mid in self.fail_send:
            raise RuntimeError("simulated send failure")
        return "sent-" + mid

    def modify(self, msg_id, add=None, remove=None, *a, **k):
        self.events.append(("modify", msg_id, list(add or []), list(remove or [])))

    def insert_summary(self, subject, html, text, *a, **k):
        self.events.append(("insert_summary", subject, html, text))
        return "summary-1"

    def writes(self):
        return [e for e in self.events if e[0] in WRITES]

    def final_labels(self, mid):
        labels = set(self.msgs[mid]["label_ids"])
        for e in self.events:
            if e[0] == "modify" and e[1] == mid:
                labels |= set(e[2])
                labels -= set(e[3])
        return labels

    def forwards(self, mid=None):
        return [e for e in self.events if e[0] == "forward" and (mid is None or e[1] == mid)]


def install(fake, decisions):
    """Swap Gmail and the classifier for fakes in every module that holds a
    reference, whether it imported the module or the function itself."""
    for name in GMAIL_API:
        repl = getattr(fake, name)
        setattr(gmail_ops, name, repl)
        for mod in (runner, summary):
            cur = getattr(mod, name, None)
            if callable(cur) and getattr(cur, "__module__", "") in (
                    gmail_ops.__name__, __name__):
                setattr(mod, name, repl)

    def fake_classify(msg, ctx=None, *a, **k):
        return copy.deepcopy(decisions[msg["id"]])

    classify.classify = fake_classify
    cur = getattr(runner, "classify", None)
    if callable(cur) and getattr(cur, "__module__", "") in (classify.__name__, __name__):
        runner.classify = fake_classify


def run(fake, decisions, mode, log_path):
    install(fake, decisions)
    os.environ["EMAIL_TRIAGE_LOG"] = log_path
    if mode is None:
        os.environ.pop("JACKBOT_EMAIL_TRIAGE", None)
    else:
        os.environ["JACKBOT_EMAIL_TRIAGE"] = mode
    return runner.run_triage(mode=mode, lookback_days=2)


SPAM_SENDER = "kyle@firstlinecap-example.biz"


def scenario():
    msgs = [
        make_msg(id="in_fwd", thread_id="t_in_fwd", subject="Invoice 4411 from Acme Supply"),
        make_msg(id="in_keep", thread_id="t_in_keep", subject="Board agenda for Thursday"),
        make_msg(id="in_keepfwd", thread_id="t_in_keepfwd",
                 subject="Customer asking about S2 pricing"),
        make_msg(id="in_arch", thread_id="t_in_arch", subject="Weekly drone industry newsletter",
                 list_unsubscribe=True),
        make_msg(id="in_spam", thread_id="t_in_spam", from_email=SPAM_SENDER,
                 from_name="First Line Capital", list_unsubscribe=True,
                 subject="Is Existing Business Debt Limiting Your Cash Flow?"),
        make_msg(id="in_fail", thread_id="t_in_fail", subject="Vercel usage report"),
        make_msg(id="f_fwd", thread_id="t_f_fwd", in_inbox=False, subject="DigiKey quote 9981"),
        make_msg(id="f_keep", thread_id="t_f_keep", in_inbox=False,
                 subject="Partner wants Jack's decision on teaming"),
        make_msg(id="f_arch", thread_id="t_f_arch", in_inbox=False, subject="Conference promo",
                 list_unsubscribe=True),
        make_msg(id="f_spam", thread_id="t_f_spam", in_inbox=False, from_email=SPAM_SENDER,
                 from_name="First Line Capital", list_unsubscribe=True,
                 subject="Reminder: Explore SBA Financing"),
    ]
    decisions = {
        "in_fwd": make_dec(forward_to=[MEREDITH], category="finance-ap"),
        "in_keep": make_dec(keep_for_jack=True, category="ceo"),
        "in_keepfwd": make_dec(keep_for_jack=True, forward_to=[BECK], category="sales"),
        "in_arch": make_dec(category="newsletter"),
        "in_spam": make_dec(**SPAMMY),
        "in_fail": make_dec(forward_to=[BEN], category="cloud"),
        "f_fwd": make_dec(forward_to=[SAM], category="components"),
        "f_keep": make_dec(keep_for_jack=True, category="ceo"),
        "f_arch": make_dec(category="event-marketing"),
        "f_spam": make_dec(**SPAMMY),
    }
    return msgs, decisions


def test_runner_live():
    print("runner (live, fakes)")
    msgs, decisions = scenario()
    fake = FakeGmail(msgs, fail_send={"in_fail"})
    with tempfile.TemporaryDirectory() as d:
        log = os.path.join(d, "actions.jsonl")
        try:
            records = run(fake, decisions, "live", log)
        except Exception as e:  # a send failure must not sink the run
            check("run_triage survives a failed send", repr(e), None)
            return
        check("one record per message", len(records or []), len(msgs))
        lines = [json.loads(l) for l in open(log)] if os.path.exists(log) else []
        # A forward also writes a "pending" line before the send (so a crash
        # mid-send shows up in the summary); the last line per id is final.
        final = {l["id"]: l for l in lines}
        check("one final log line per message", len(final), len(msgs))
        check("no message left pending",
              [i for i, l in final.items() if l["action"] == "pending"], [])
        want_keys = {"ts", "id", "thread_id", "from", "subject", "action", "forward_to",
                     "keep", "spam", "reason", "summary", "category", "guard_notes", "mode"}
        check("log lines carry every spec field",
              all(want_keys <= set(l) for l in lines) and bool(lines), True)

    ev = fake.events
    for mid in ("in_fwd", "in_keepfwd", "f_fwd", "in_fail"):
        f_idx = next((i for i, e in enumerate(ev) if e[0] == "forward" and e[1] == mid), None)
        r_idx = next((i for i, e in enumerate(ev) if e[0] == "modify" and e[1] == mid
                      and "Jackbot" in e[2]), None)
        check(f"{mid}: Reviewed added before forward",
              f_idx is not None and r_idx is not None and r_idx < f_idx, True)

    check("in_fwd forwarded to Meredith", [e[2] for e in fake.forwards("in_fwd")], [[MEREDITH]])
    lab = fake.final_labels("in_fwd")
    check("inbox forward: Forwarded added", "Jackbot/Forwarded" in lab, True)
    check("inbox forward: INBOX removed", "INBOX" in lab, False)
    check("inbox forward: Reviewed kept", "Jackbot" in lab, True)

    lab = fake.final_labels("in_keep")
    check("inbox keep: stays in INBOX", "INBOX" in lab, True)
    check("inbox keep: Kept added", "Jackbot/Kept" in lab, True)
    check("inbox keep: no forward", fake.forwards("in_keep"), [])

    lab = fake.final_labels("in_keepfwd")
    check("keep+forward: forwarded to Beck",
          [e[2] for e in fake.forwards("in_keepfwd")], [[BECK]])
    check("keep+forward: stays in INBOX", "INBOX" in lab, True)
    check("keep+forward: Kept + Forwarded",
          {"Jackbot/Kept", "Jackbot/Forwarded"} <= lab, True)

    lab = fake.final_labels("in_arch")
    check("inbox archive: Archived added", "Jackbot/Archived" in lab, True)
    check("inbox archive: INBOX removed", "INBOX" in lab, False)

    for mid in ("in_spam", "f_spam"):
        lab = fake.final_labels(mid)
        check(f"{mid}: SPAM + Jackbot/Spam", {"SPAM", "Jackbot/Spam"} <= lab, True)
        check(f"{mid}: not in INBOX", "INBOX" in lab, False)
        check(f"{mid}: never forwarded", fake.forwards(mid), [])

    lab = fake.final_labels("in_fail")
    check("send failure: forward attempted", len(fake.forwards("in_fail")), 1)
    check("send failure: Reviewed rolled back", "Jackbot" in lab, False)

    check("filtered forward sent", [e[2] for e in fake.forwards("f_fwd")], [[SAM]])
    check("filtered forward: not pulled into INBOX", "INBOX" in fake.final_labels("f_fwd"), False)
    check("filtered keep: INBOX added", "INBOX" in fake.final_labels("f_keep"), True)
    lab = fake.final_labels("f_arch")
    check("filtered archive: not pulled into INBOX", "INBOX" in lab, False)
    check("filtered archive: Reviewed", "Jackbot" in lab, True)

    for mid in fake.msgs:
        if mid != "in_fail":
            check(f"{mid}: Reviewed", "Jackbot" in fake.final_labels(mid), True)

    touched_unread = [e for e in ev if e[0] == "modify" and ("UNREAD" in e[2] or "UNREAD" in e[3])]
    check("UNREAD never added or removed", touched_unread, [])
    check("no summary inserted by the runner",
          [e for e in ev if e[0] == "insert_summary"], [])

    notes = [norm(e[3]) for e in fake.forwards()]
    check("every forward carries the note verbatim",
          bool(notes) and all(norm(NOTE) in n for n in notes), True)


def test_send_uncertain():
    """A send whose outcome is unknown (5xx / timeout) must keep Reviewed, or
    the next run forwards the same message again."""
    print("ambiguous send failure")

    class Uncertain(FakeGmail):
        FORWARD_PREAMBLE = gmail_ops.FORWARD_PREAMBLE

        def forward(self, msg, recipients, note=None, *a, **k):
            self.events.append(("forward", msg["id"], list(recipients), note))
            raise gmail_ops.SendUncertain("simulated 503 after delivery")

    fake = Uncertain([])
    msg = make_msg(id="u1", in_inbox=True, label_ids=["INBOX"])
    with tempfile.TemporaryDirectory() as d:
        os.environ["EMAIL_TRIAGE_LOG"] = os.path.join(d, "a.jsonl")
        rec = runner.apply_actions(fake, msg, make_dec(forward_to=[MEREDITH]), "live",
                                   {n: n for n in runner.ALL_LABELS})
    check("uncertain send: recorded as pending", rec["action"], "pending")
    mods = [e for e in fake.events if e[0] == "modify"]
    check("uncertain send: Reviewed not rolled back",
          any("Jackbot" in e[2] for e in mods)
          and not any("Jackbot" in e[3] for e in mods), True)
    check("uncertain send: message left in INBOX",
          any("INBOX" in e[3] for e in mods), False)


def test_runner_dryrun_and_off():
    print("runner dryrun / off")
    msgs, decisions = scenario()
    fake = FakeGmail(msgs)
    with tempfile.TemporaryDirectory() as d:
        log = os.path.join(d, "actions.jsonl")
        records = run(fake, decisions, "dryrun", log)
        check("dryrun: records for every message", len(records or []), len(msgs))
        check("dryrun: actions logged",
              sum(1 for _ in open(log)) if os.path.exists(log) else 0, len(msgs))
    check("dryrun: no forward/modify/insert",
          [e for e in fake.events if e[0] in ("forward", "modify", "insert_summary")], [])
    check("dryrun: no label creation", [e for e in fake.events if e[0] == "ensure_labels"], [])

    for mode in ("off", None):
        fake = FakeGmail(msgs)
        with tempfile.TemporaryDirectory() as d:
            run(fake, decisions, mode, os.path.join(d, "actions.jsonl"))
        check(f"mode {mode!r}: zero writes", fake.writes(), [])


# --- daily summary -------------------------------------------------------

def test_summary():
    print("daily summary")
    msgs = [
        make_msg(id="s_f1", subject="Alpha invoice from Acme"),
        make_msg(id="s_f2", subject="Bravo PCB quote"),
        make_msg(id="s_k1", subject="Charlie investor update request"),
        make_msg(id="s_a1", subject="Delta newsletter", list_unsubscribe=True),
        make_msg(id="s_a2", subject="Echo webinar promo", list_unsubscribe=True),
        make_msg(id="s_a3", subject="Foxtrot digest", list_unsubscribe=True),
        make_msg(id="s_s1", subject="Golf business line of credit", from_email=SPAM_SENDER,
                 from_name="First Line Capital", list_unsubscribe=True),
    ]
    decisions = {
        "s_f1": make_dec(forward_to=[MEREDITH], reason="AP bill for Meredith"),
        "s_f2": make_dec(forward_to=[SAM], reason="component quote"),
        "s_k1": make_dec(keep_for_jack=True, reason="investor asking Jack directly",
                         summary="Investor wants Q3 numbers by Friday"),
        "s_a1": make_dec(), "s_a2": make_dec(), "s_a3": make_dec(),
        "s_s1": make_dec(**SPAMMY),
    }
    fake = FakeGmail(msgs)
    with tempfile.TemporaryDirectory() as d:
        log = os.path.join(d, "actions.jsonl")
        run(fake, decisions, "live", log)
        summary.send_daily_summary(hours=24)
    inserts = [e for e in fake.events if e[0] == "insert_summary"]
    check("exactly one summary inserted", len(inserts), 1)
    if not inserts:
        return
    _, subject, html, text = inserts[0]
    check("subject prefix", subject.startswith("Email triage"), True)
    check("subject counts", "2 forwarded, 1 kept for you, 3 archived, 1 spam" in subject, True)

    pos = {h: text.find(h) for h in ("Kept for you", "Forwarded", "Spam", "Archived")}
    check("all sections present", all(v >= 0 for v in pos.values()), True)
    check("section order Kept < Forwarded < Spam < Archived",
          pos["Kept for you"] < pos["Forwarded"] < pos["Spam"] < pos["Archived"], True)

    def section_of(needle):
        i = text.find(needle)
        if i < 0:
            return None
        if i > pos["Archived"]:
            return "Archived"
        if i > pos["Spam"]:
            return "Spam"
        if i > pos["Forwarded"]:
            return "Forwarded"
        if i > pos["Kept for you"]:
            return "Kept for you"
        return "header"

    check("kept item under Kept", section_of("Charlie investor update request"), "Kept for you")
    check("kept item shows summary", section_of("Investor wants Q3 numbers by Friday"),
          "Kept for you")
    check("kept item shows reason", section_of("investor asking Jack directly"), "Kept for you")
    for s in ("Alpha invoice from Acme", "Bravo PCB quote"):
        check(f"forward under Forwarded: {s}", section_of(s), "Forwarded")
    check("forward recipient shown", "meredith" in text[pos["Forwarded"]:pos["Spam"]].lower(), True)
    check("spam under Spam", section_of("Golf business line of credit"), "Spam")
    check("spam shows sender",
          "firstline" in text[pos["Spam"]:pos["Archived"]].lower().replace(" ", ""), True)
    for s in ("Delta newsletter", "Echo webinar promo", "Foxtrot digest"):
        check(f"archive under Archived: {s}", section_of(s), "Archived")
    for mid in decisions:
        check(f"html links {mid}",
              f"https://mail.google.com/mail/u/0/#all/{mid}" in (html or ""), True)


# --- forward message format (gmail_ops.forward against a fake service) ----

ORIGINAL_RAW = (
    "From: Vendor Rep <rep@vendor-example.com>\r\n"
    f"To: {JACK}\r\n"
    "Subject: Widget quote\r\n"
    "Date: Mon, 9 Nov 2026 08:00:00 -0700\r\n"
    "Message-ID: <orig-1@vendor-example.com>\r\n"
    "Content-Type: text/plain; charset=utf-8\r\n\r\n"
    "Hello Jack, here is the widget quote.\r\n"
)


def _b64(s):
    return base64.urlsafe_b64encode(s.encode() if isinstance(s, str) else s).decode()


class _Req:
    def __init__(self, result):
        self.result = result

    def execute(self, *a, **k):
        return self.result


class _Recorder:
    """Permissive stand-in for googleapiclient resources: every method call is
    recorded; Gmail calls forward needs return plausible payloads."""

    def __init__(self, log, path=""):
        self._log = log
        self._path = path

    def __getattr__(self, name):
        path = f"{self._path}.{name}" if self._path else name

        def call(*a, **k):
            self._log.append((path, k))
            if name in ("users", "messages", "labels", "threads", "attachments", "drafts"):
                return _Recorder(self._log, path)
            if path.endswith("messages.get"):
                return _Req({
                    "id": k.get("id", "orig-id"), "threadId": "orig-thread",
                    "raw": _b64(ORIGINAL_RAW), "labelIds": ["INBOX"],
                    "payload": {"mimeType": "text/plain", "headers": [
                        {"name": "From", "value": "Vendor Rep <rep@vendor-example.com>"},
                        {"name": "To", "value": JACK},
                        {"name": "Subject", "value": "Widget quote"},
                        {"name": "Date", "value": "Mon, 9 Nov 2026 08:00:00 -0700"},
                        {"name": "Message-ID", "value": "<orig-1@vendor-example.com>"}],
                        "body": {"data": _b64("Hello Jack, here is the widget quote.")}},
                })
            if path.endswith("messages.send"):
                return _Req({"id": "sent-1", "threadId": "sent-thread"})
            return _Req({})
        return call


def test_forward_format():
    print("forward message format")
    for name, fn in REAL_GMAIL.items():
        setattr(gmail_ops, name, fn)
    log = []
    fake_service = _Recorder(log)
    saved = gmail_ops.service
    gmail_ops.service = lambda *a, **k: fake_service
    msg = make_msg(id="orig-id", from_email="rep@vendor-example.com",
                   from_name="Vendor Rep", subject="Widget quote",
                   body_text="Hello Jack, here is the widget quote.")
    try:
        gmail_ops.forward(msg, [MEREDITH, SAM], NOTE)
    except Exception as e:
        check("gmail_ops.forward runs against fake service", repr(e), None)
        return
    finally:
        gmail_ops.service = saved

    sends = [k for p, k in log if p.endswith("messages.send")]
    check("exactly one send", len(sends), 1)
    bad = [p for p, _ in log if p.endswith(("messages.insert", "messages.modify",
                                             "messages.trash", "messages.delete"))]
    check("forward makes no other mailbox writes", bad, [])
    if not sends:
        return
    raw = (sends[0].get("body") or {}).get("raw", "")
    parsed = email.message_from_bytes(base64.urlsafe_b64decode(raw + "=" * (-len(raw) % 4)),
                                      policy=email.policy.default)
    to = {a.strip().lower() for a in re.findall(r"[\w.+-]+@[\w.-]+", str(parsed["To"] or ""))}
    check("To = recipients", to, {MEREDITH, SAM})
    check("Subject = Fwd: original", str(parsed["Subject"]), "Fwd: Widget quote")
    check("X-Jackbot-Source-Id header", str(parsed["X-Jackbot-Source-Id"]), "orig-id")
    check("From is Jack", JACK in str(parsed["From"] or "").lower(), True)

    plain, html_part, rfc822 = "", "", False
    for part in parsed.walk():
        ctype = part.get_content_type()
        if ctype == "message/rfc822":
            rfc822 = True
            continue
        if part.get_content_maintype() == "multipart" or part.is_attachment():
            continue
        if ctype == "text/plain" and not plain:
            plain = part.get_content()
        elif ctype == "text/html" and not html_part:
            html_part = part.get_content()
    check("plain body has the note verbatim", norm(NOTE) in norm(plain), True)
    check("html body has the note verbatim", norm(NOTE) in html_to_text(html_part), True)
    check("note comes before the forwarded header",
          0 <= norm(plain).find(norm(NOTE)) < norm(plain).find("Forwarded message"), True)
    check("forwarded-message separator", "---------- Forwarded message ---------" in plain, True)
    check("original body included", "here is the widget quote" in plain, True)
    check("original attached as message/rfc822", rfc822, True)


if __name__ == "__main__":
    tests = [test_spam_guards, test_forced_keep, test_forward_filtering,
             test_archive_and_age, test_runner_live, test_send_uncertain,
             test_runner_dryrun_and_off,
             test_summary, test_forward_format]
    for t in tests:
        try:
            t()
        except Exception as e:  # keep going so one broken module doesn't hide the rest
            import traceback
            traceback.print_exc()
            check(f"{t.__name__} raised", repr(e), None)
    if FAILURES:
        raise SystemExit(f"\n{len(FAILURES)} failure(s)")
    print("\nall email triage checks passed")
