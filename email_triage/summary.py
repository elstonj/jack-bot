"""Morning recap of what email triage did, delivered to Jack's own inbox.

This is the review loop: instead of reading every forward, Jack reads one
message listing what was kept for him, what went to whom and why, what was
spammed and what was archived, and corrects the routing from there. It is
inserted with `messages.insert` (a local write to his mailbox), so nothing is
sent anywhere and nothing appears in Slack.

Built from the JSONL action log. Railway's filesystem is wiped on redeploy, so
when the log is missing or empty the recap is rebuilt from the Jackbot/*
labels and from Sent forwards carrying `X-Jackbot-Source-Id` — the actions
are recoverable that way, the model's reasons are not, and the recap says so.
"""

import html
import json
import os
import time
from datetime import datetime
from zoneinfo import ZoneInfo

from email_triage import runner

TZ = ZoneInfo("America/Denver")
MAIL_LINK = "https://mail.google.com/mail/u/0/#all/{id}"
RECONSTRUCTED_REASON = "reason unavailable (rebuilt from labels after a restart)"


def load_records(hours=24, path=None):
    """Log records from the last `hours`, one per message (latest wins, so a
    message that errored and was retried shows its final outcome)."""
    path = path or runner.log_path()
    cutoff = time.time() - hours * 3600
    by_id = {}
    try:
        with open(path) as f:
            for line in f:
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                if r.get("ts", 0) >= cutoff and r.get("id"):
                    by_id[r["id"]] = r
    except OSError:
        return []
    return list(by_id.values())


def _header(meta, name):
    for h in meta.get("payload", {}).get("headers", []):
        if h.get("name", "").lower() == name.lower():
            return h.get("value", "")
    return ""


def reconstruct_records(hours=24):
    """Rebuild records from Gmail state. Read-only calls only."""
    from email_triage import gmail_ops

    svc = gmail_ops.service().users()
    days = max(1, -(-hours // 24))
    names = {l["name"]: l["id"] for l in
             svc.labels().list(userId="me").execute(num_retries=5).get("labels", [])}

    def ids_with(label):
        if label not in names:
            return set()
        out, token = set(), None
        while True:
            resp = svc.messages().list(userId="me", labelIds=[names[label]],
                                       q=f"newer_than:{days}d", includeSpamTrash=True,
                                       pageToken=token, maxResults=500).execute(num_retries=5)
            out |= {m["id"] for m in resp.get("messages", [])}
            token = resp.get("nextPageToken")
            if not token:
                return out

    kept, fwd = ids_with(runner.LABEL_KEPT), ids_with(runner.LABEL_FORWARDED)
    spam, arch = ids_with(runner.LABEL_SPAM), ids_with(runner.LABEL_ARCHIVED)

    recipients = {}
    resp = svc.messages().list(userId="me", q=f"in:sent newer_than:{days}d subject:Fwd",
                               maxResults=500).execute(num_retries=5)
    for m in resp.get("messages", []):
        meta = svc.messages().get(userId="me", id=m["id"], format="metadata",
                                  metadataHeaders=["To", "X-Jackbot-Source-Id"]
                                  ).execute(num_retries=5)
        src = _header(meta, "X-Jackbot-Source-Id")
        if src:
            recipients[src] = [a.strip() for a in _header(meta, "To").split(",") if a.strip()]

    records = []
    for mid in kept | fwd | spam | arch:
        if mid in spam:
            action = "spam"
        elif mid in kept:
            action = "keep+forward" if mid in fwd else "keep"
        elif mid in fwd:
            action = "forward"
        else:
            action = "archive"
        meta = svc.messages().get(userId="me", id=mid, format="metadata",
                                  metadataHeaders=["From", "Subject"]).execute(num_retries=5)
        records.append({
            "ts": int(meta.get("internalDate", 0)) // 1000, "id": mid,
            "thread_id": meta.get("threadId"), "from": _header(meta, "From"),
            "subject": _header(meta, "Subject"), "action": action,
            "forward_to": recipients.get(mid, []), "keep": action.startswith("keep"),
            "spam": action == "spam", "reason": RECONSTRUCTED_REASON, "summary": "",
            "category": "", "guard_notes": [], "mode": "live", "reconstructed": True,
        })
    return records


def _counts(records):
    a = [r["action"] for r in records]
    return {
        "F": sum(x in ("forward", "keep+forward") for x in a),
        "K": sum(x in ("keep", "keep+forward") for x in a),
        "A": sum(x == "archive" for x in a),
        "S": sum(x == "spam" for x in a),
    }


def render(records, now=None):
    """-> (subject, html_body, text_body). Pure; tests call it directly."""
    now = now or datetime.now(TZ)
    c = _counts(records)
    dry = bool(records) and all(r.get("mode") != "live" for r in records)
    subject = (f"Email triage — {now:%a %b %-d}: {c['F']} forwarded, "
               f"{c['K']} kept for you, {c['A']} archived, {c['S']} spam")
    if dry:
        subject = "[dry run] " + subject

    by = lambda *acts: sorted((r for r in records if r["action"] in acts),  # noqa: E731
                              key=lambda r: r.get("ts", 0))
    kept, fwd = by("keep", "keep+forward"), by("forward", "keep+forward")
    spam, arch, filt = by("spam"), by("archive"), by("reviewed")
    issues = [r for r in records if r.get("error") or r.get("guard_notes")
              or r["action"] in ("error", "skipped")]

    h, t = [], []
    esc = html.escape

    def link(r):
        return (f'<a href="{MAIL_LINK.format(id=esc(r["id"]))}">'
                f'{esc(r.get("subject") or "(no subject)")}</a>')

    def section(title, rows_html, rows_text):
        if not rows_html:
            return
        h.append(f"<h3>{esc(title)} ({len(rows_html)})</h3><ul>")
        h.extend(f"<li>{x}</li>" for x in rows_html)
        h.append("</ul>")
        t.append(f"{title} ({len(rows_text)})")
        t.extend(f"  - {x}" for x in rows_text)
        t.append("")

    if dry:
        h.append("<p><b>Dry run:</b> nothing below was actually forwarded, "
                 "labeled or moved.</p>")
        t += ["DRY RUN: nothing below was actually forwarded, labeled or moved.", ""]
    if any(r.get("reconstructed") for r in records):
        note = ("The action log was lost (likely a redeploy), so this was rebuilt "
                "from Gmail labels; reasons are unavailable.")
        h.append(f"<p><i>{esc(note)}</i></p>")
        t += [note, ""]

    def also(r):
        return f" (also forwarded to {', '.join(r['forward_to'])})" if r["action"] == "keep+forward" else ""

    section("Kept for you",
            [f"{link(r)} — {esc(r.get('from', ''))}<br>{esc(r.get('summary', ''))}"
             f"<br><i>{esc(r.get('reason', ''))}{esc(also(r))}</i>" for r in kept],
            [f"{r.get('subject')} — {r.get('from', '')}\n      {r.get('summary', '')}"
             f"\n      why: {r.get('reason', '')}{also(r)}" for r in kept])
    section("Forwarded",
            [f"<b>{esc(', '.join(r['forward_to']) or '?')}</b> — {link(r)} — "
             f"{esc(r.get('reason', ''))}" for r in fwd],
            [f"{', '.join(r['forward_to']) or '?'} — {r.get('subject')} — "
             f"{r.get('reason', '')}" for r in fwd])
    section("Spam",
            [f"{esc(r.get('from', ''))} — {link(r)}" for r in spam],
            [f"{r.get('from', '')} — {r.get('subject')}" for r in spam])
    section("Archived",
            [f"{link(r)} <span style='color:#777'>({esc(r.get('from', ''))})</span>"
             for r in arch],
            [f"{r.get('subject')} ({r.get('from', '')})" for r in arch])
    section("Already filtered, left where it was",
            [f"{link(r)} <span style='color:#777'>({esc(r.get('from', ''))})</span>"
             for r in filt],
            [f"{r.get('subject')} ({r.get('from', '')})" for r in filt])

    def issue_text(r):
        bits = list(r.get("guard_notes") or [])
        if r.get("error"):
            bits.append(f"ERROR: {r['error']}")
        if r["action"] == "error" and r.get("forward_to"):
            bits.append(f"intended for {', '.join(r['forward_to'])}; will retry next run")
        return "; ".join(bits) or r["action"]

    section("Guard notes / errors",
            [f"{link(r)} — {esc(issue_text(r))}" for r in issues],
            [f"{r.get('subject')} — {issue_text(r)}" for r in issues])

    if not records:
        h.append("<p>Nothing was triaged in this window.</p>")
        t.append("Nothing was triaged in this window.")
    footer = ("Something went to the wrong place? Routing lives in "
              "email_triage/config.json.")
    h.append(f"<p style='color:#777'>{esc(footer)}</p>")
    t.append(footer)

    body_html = ("<div style='font-family:sans-serif;font-size:14px'>"
                 + "\n".join(h) + "</div>")
    return subject, body_html, "\n".join(t)


def build_summary(hours=24):
    records = load_records(hours)
    if not records and runner.current_mode() == "live":
        try:
            records = reconstruct_records(hours)
        except Exception as e:
            print(f"[email_triage] summary reconstruction failed: {e}")
    live = [r for r in records if r.get("mode") == "live"]
    return render(live or records), (live or records)


def send_daily_summary(hours=24, force=False):
    """Insert the recap into Jack's inbox. Without `force`, only in live mode
    (dryrun promises no Gmail writes) and only if anything happened."""
    if not force and runner.current_mode() != "live":
        return None
    (subject, body_html, body_text), records = build_summary(hours)
    if not records:
        return None
    from email_triage import gmail_ops
    return gmail_ops.insert_summary(subject, body_html, body_text)
