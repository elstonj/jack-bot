"""Per-message triage loop: fetch -> classify -> guard -> act -> log.

Ordering is what makes forwards at-most-once. `Jackbot/Reviewed` is the only
thing that keeps a message out of the next run's candidate list, so it is
written *before* a forward is sent; if the send fails it is removed again so
the next run retries. A crash between the two leaves a message reviewed but
not forwarded (it shows up in the daily summary) rather than forwarded twice
— a missed forward is recoverable, a duplicate one in a colleague's inbox
every 15 minutes is not.

Never touches UNREAD (Jack's read state is his) and never deletes or trashes:
the most destructive action is moving a cold solicitation to Spam.

Mode comes from env `JACKBOT_EMAIL_TRIAGE` (off | dryrun | live, default off)
and is re-read every run, so it can be flipped on Railway without a deploy.
"""

import fcntl
import json
import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor

MODES = ("off", "dryrun", "live")
DEFAULT_LOG = "/tmp/email_triage_actions.jsonl"
LOCK_PATH = "/tmp/email_triage.lock"
CLASSIFY_WORKERS = 6

LABEL_REVIEWED = "Jackbot/Reviewed"
LABEL_FORWARDED = "Jackbot/Forwarded"
LABEL_ARCHIVED = "Jackbot/Archived"
LABEL_SPAM = "Jackbot/Spam"
LABEL_KEPT = "Jackbot/Kept"
ALL_LABELS = [LABEL_REVIEWED, LABEL_FORWARDED, LABEL_ARCHIVED, LABEL_SPAM, LABEL_KEPT]

# Read state and deletion are off-limits regardless of what a decision says.
_FORBIDDEN = {"UNREAD", "TRASH"}

_run_lock = threading.Lock()


def current_mode():
    mode = os.environ.get("JACKBOT_EMAIL_TRIAGE", "off").strip().lower()
    return mode if mode in MODES else "off"


def log_path():
    return os.environ.get("EMAIL_TRIAGE_LOG", DEFAULT_LOG)


def _fallback_decision(reason):
    return {"keep_for_jack": True, "forward_to": [], "is_spam": False,
            "spam_confidence": 0.0, "major_media": False, "category": "error",
            "reason": reason, "summary": "", "guard_notes": []}


def decide_action(msg, decision):
    """Map a final decision onto (action, add_labels, remove_labels).

    Pure, so tests can pin the label contract without a mailbox.
    """
    in_inbox = bool(msg.get("in_inbox"))
    forward = bool(decision.get("forward_to")) and not decision.get("is_spam")
    keep = bool(decision.get("keep_for_jack"))
    add, remove = [LABEL_REVIEWED], []

    if decision.get("is_spam"):
        action = "spam"
        add += [LABEL_SPAM, "SPAM"]
        if in_inbox:
            remove.append("INBOX")
    elif keep:
        action = "keep+forward" if forward else "keep"
        add.append(LABEL_KEPT)
        if forward:
            add.append(LABEL_FORWARDED)
        if not in_inbox:
            add.append("INBOX")  # filtered mail Jack needs to see
    elif forward:
        action = "forward"
        add.append(LABEL_FORWARDED)
        if in_inbox:
            remove.append("INBOX")
    elif in_inbox:
        action = "archive"
        add.append(LABEL_ARCHIVED)
        remove.append("INBOX")
    else:
        action = "reviewed"  # already filtered out of the inbox; leave it there

    add = [l for l in add if l not in _FORBIDDEN]
    remove = [l for l in remove if l not in _FORBIDDEN]
    return action, add, remove


def _record(msg, decision, action, mode, error=None):
    rec = {
        "ts": int(time.time()),
        "id": msg.get("id"),
        "thread_id": msg.get("thread_id"),
        "from": (f"{msg.get('from_name')} <{msg.get('from_email')}>"
                 if msg.get("from_name") else msg.get("from_email", "")),
        "subject": msg.get("subject", ""),
        "action": action,
        # Kept on errors too, so the summary can say who a failed forward was for.
        "forward_to": (list(decision.get("forward_to") or [])
                       if action in ("forward", "keep+forward", "error", "skipped", "pending")
                       else []),
        "keep": bool(decision.get("keep_for_jack")),
        "spam": bool(decision.get("is_spam")),
        "reason": decision.get("reason", ""),
        "summary": decision.get("summary", ""),
        "category": decision.get("category", ""),
        "guard_notes": list(decision.get("guard_notes") or []),
        "in_inbox": bool(msg.get("in_inbox")),
        "mode": mode,
    }
    if error:
        rec["error"] = error
    return rec


def append_log(records, path=None):
    path = path or log_path()
    try:
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, "a") as f:
            for r in records:
                f.write(json.dumps(r) + "\n")
    except OSError as e:
        print(f"[email_triage] action log write failed: {e}")


def _already_reviewed(gmail_ops, msg_id, reviewed_id):
    """Re-read labels right before sending — narrows the window in which two
    runners (Railway + a laptop CLI) could both forward the same message."""
    try:
        meta = gmail_ops.service().users().messages().get(
            userId="me", id=msg_id, format="minimal").execute(num_retries=5)
        return reviewed_id in (meta.get("labelIds") or [])
    except Exception:
        return False


def apply_actions(gmail_ops, msg, decision, mode, label_ids=None):
    """Carry out one decision. Returns the log record."""
    action, add, remove = decide_action(msg, decision)
    if mode != "live":
        return _record(msg, decision, action, mode)

    label_ids = label_ids or {}
    ids = lambda names: [label_ids.get(n, n) for n in names]  # noqa: E731
    recipients = list(decision.get("forward_to") or [])

    if action in ("forward", "keep+forward"):
        if _already_reviewed(gmail_ops, msg["id"], label_ids.get(LABEL_REVIEWED, LABEL_REVIEWED)):
            return _record(msg, decision, "skipped", mode,
                           error="already reviewed by a concurrent run")
        pre = [l for l in add if l.startswith("Jackbot/")]
        try:
            gmail_ops.modify(msg["id"], add=ids(pre), remove=[])
        except Exception as e:
            # The add may have landed despite the error; undo it so the next
            # run retries instead of silently treating this as done.
            try:
                gmail_ops.modify(msg["id"], add=[], remove=ids(pre))
            except Exception:
                pass
            return _record(msg, decision, "error", mode, error=f"label update failed: {e}")
        # Logged before the send so a crash between here and the final record
        # still surfaces in the summary (Reviewed is set, so it won't retry).
        append_log([_record(msg, decision, "pending", mode,
                            error="forward started but never confirmed (run died?); "
                                  "check Sent before re-forwarding")])
        from email_triage.gmail_ops import SendUncertain
        try:
            gmail_ops.forward(msg, recipients, gmail_ops.FORWARD_PREAMBLE)
        except Exception as e:
            if isinstance(e, SendUncertain):
                # May have been delivered: keep Reviewed so it is never re-sent.
                return _record(msg, decision, "pending", mode,
                               error=f"{e}; not retried — check Sent before re-forwarding")
            try:
                gmail_ops.modify(msg["id"], add=[], remove=ids(pre))
            except Exception as e2:
                return _record(msg, decision, "error", mode,
                               error=f"forward failed ({e}); rollback failed ({e2})")
            return _record(msg, decision, "error", mode, error=f"forward failed: {e}")
        rest_add = [l for l in add if l not in pre]
        if rest_add or remove:
            try:
                gmail_ops.modify(msg["id"], add=ids(rest_add), remove=ids(remove))
            except Exception as e:
                return _record(msg, decision, action, mode,
                               error=f"forwarded, but inbox move failed: {e}")
        return _record(msg, decision, action, mode)

    try:
        gmail_ops.modify(msg["id"], add=ids(add), remove=ids(remove))
    except Exception as e:
        return _record(msg, decision, "error", mode, error=f"label update failed: {e}")
    return _record(msg, decision, action, mode)


def _classify_one(classify, guards, msg, ctx):
    try:
        decision = classify.classify(msg, ctx)
    except Exception as e:
        print(f"[email_triage] classify failed for {msg.get('id')}: {e}")
        decision = _fallback_decision("classifier error")
    try:
        return guards.apply(msg, decision, ctx)
    except Exception as e:
        # Guards are the safety layer; if they break, nothing leaves the inbox.
        d = _fallback_decision("guard error")
        d["guard_notes"] = [f"guards failed: {e}"]
        return d


def _triage(mode, lookback_days, limit):
    from email_triage import classify, config, gmail_ops, guards

    cfg = config.load_config()
    label_ids = gmail_ops.ensure_labels(ALL_LABELS) if mode == "live" else {}
    try:
        groups = gmail_ops.group_members()
    except Exception as e:
        # Group membership is what stops spam on mail sent to a group alias
        # and duplicate forwards to people already on it; without it, a live
        # run would fail open. Skip the pass; the next tick retries.
        print(f"[email_triage] group lookup failed: {e}")
        if mode == "live":
            return []
        groups = {}

    jack = {a.lower() for a in (cfg.get("jack") or {}).get("addresses", [])}
    ids = gmail_ops.list_candidates(lookback_days)
    if limit:
        ids = ids[:limit]

    # Gmail calls stay on this thread (googleapiclient's http isn't
    # thread-safe); only the model calls fan out.
    items = []
    for mid in ids:
        try:
            msg = gmail_ops.fetch_message(mid)
            known = gmail_ops.sender_is_known(msg.get("from_email", ""))
        except Exception as e:
            print(f"[email_triage] fetch failed for {mid}: {e}")
            continue
        # Jack's own post echoed back by a group ("'Jack Elston' via
        # Operations") slips past -from:me; never forward Jack's own mail.
        if (msg.get("from_email") or "").lower() in jack:
            continue
        items.append((msg, {"known_sender": known, "group_members": groups, "config": cfg}))

    with ThreadPoolExecutor(max_workers=CLASSIFY_WORKERS) as pool:
        decisions = list(pool.map(lambda it: _classify_one(classify, guards, *it), items))

    records = []
    for (msg, _ctx), decision in zip(items, decisions):
        try:
            rec = apply_actions(gmail_ops, msg, decision, mode, label_ids)
        except Exception as e:
            rec = _record(msg, decision, "error", mode, error=str(e))
        records.append(rec)
        append_log([rec])
    return records


def run_triage(mode=None, lookback_days=2, limit=None):
    """One triage pass. No-op (returns []) when mode is off or a run is
    already in progress in this process or another one on the same host."""
    mode = (mode or current_mode()).lower()
    if mode not in MODES:
        raise ValueError(f"unknown mode {mode!r}")
    if mode == "off":
        return []
    if not _run_lock.acquire(blocking=False):
        print("[email_triage] previous run still in progress; skipping")
        return []
    try:
        # gunicorn workers each start a scheduler; the file lock keeps them
        # from racing each other into duplicate forwards.
        with open(LOCK_PATH, "w") as lf:
            try:
                fcntl.flock(lf, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError:
                print("[email_triage] another process is triaging; skipping")
                return []
            return _triage(mode, lookback_days, limit)
    finally:
        _run_lock.release()
