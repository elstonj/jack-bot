"""Truthful answers about the bot's own data access.

Exists because of the 2026-08-25 #operations exchange: Joshua Fromm asked "how
did you know about the email from munro in my tasks" — an email that had landed
in *his* inbox 30 minutes earlier and was never sent to Jack. The question
matched `is_question()` on its leading "how" and went to knowledge Q&A, but
nothing in the knowledge layer describes the pipeline's own data sources, so the
model confabulated a denial: "I don't go rummaging through inboxes, I just
remember what's been reported to me." His follow-up, "explain yourself", started
with no question word and carried no "?", so it missed `is_question()` entirely
and fell through to the personality handler, which brushed him off.

The failure was structural, not a bad generation: the bot had no self-knowledge,
and the fallback for "not a question" is a persona that improvises. So questions
about where information came from are routed here *before* Q&A or personality
can see them, and answered from a fixed fact block that mirrors what the code
actually does.

Keep FACTS in sync with `daily_research._collect_gmail` /
`google_client.get_recent_emails` / `get_recent_drive_activity` /
`get_meeting_notes_content` / `get_todays_calendar`. If the pipeline's reach
changes and this file doesn't, the bot resumes lying about itself.
"""

import os
import re

import anthropic

MODEL = "claude-sonnet-5"

# Verified against the code on 2026-08-26. Every line here is something the
# pipeline demonstrably does, not something it is permitted to do.
FACTS = """WHAT JACK BOT READS

Google Workspace, via a service account with domain-wide delegation. It
impersonates each employee individually — it is not limited to Jack Elston's
account, and it does not need to be a recipient of an email to see it.

- Gmail: for EVERY employee in the user map, the pipeline reads that person's
  own inbox each weekday morning — query `is:inbox newer_than:1d`, up to 20
  messages. It takes SUBJECT LINE, SENDER and DATE only. It does NOT read
  message bodies. Subject lines are labeled by person in the briefing prompt,
  which is how an email that arrived shortly before 8am can appear in that
  person's priorities.
- Google Calendar: each person's events for today.
- Google Drive: files modified in the last 24 hours, limited to the Sales and
  Federal Projects shared drives — file names and links, not contents.
- Meeting notes: the full text (first ~3000 characters) of the most recent
  "BST Internal Update Meeting" document.
- Google Contacts: contact directory entries.
- Shared mailboxes info@, sales@ and support@ are read by the commercial-sales
  scanner.

All Google access is read-only: gmail.readonly, drive.readonly,
calendar.readonly, contacts.other.readonly, directory.readonly.

Other sources: Asana tasks and assignees; Toggl time entries; recent messages in
the Slack channels the bot is configured to monitor; the Rippling PTO calendar
feed for who is out of office.

The bot cannot send email, modify Drive files, or change calendars. It can write
to Asana (task updates), but only after a person explicitly confirms a proposal.

WHO TO ASK: Jack Elston owns the configuration and the service-account access."""

PROVENANCE_SYSTEM = """You are Jack Bot, answering a question about your own data access.

Answer ONLY from the FACTS block provided. These facts are authoritative.

Hard rules:
- NEVER deny a capability that appears in the FACTS. If the FACTS say you read
  something, say so plainly, even if the question is accusatory.
- NEVER claim a person told you something, or that it was "reported to you", when
  the FACTS show you read it directly from a system.
- If the question asks about something the FACTS don't cover, say you don't know
  and point them to Jack Elston. Do not speculate.
- Drop the persona completely. No jokes, no grumpiness, no deflection, no
  rhetorical questions. This is a question about surveillance of a colleague's
  data and it deserves a straight answer.
- Lead with the direct answer to what was asked, then add only the detail that
  matters. Be specific about the distinction between metadata and content when
  email comes up.
- Under 200 words. Slack formatting: *bold*, bullets with •."""

# Anchored on "you" so ordinary questions ("how do I ...") don't match, and kept
# to phrasings that are asking about the bot's sourcing or access.
_PATTERNS = [
    r"\bhow (?:did|do|does|would) (?:you|jack ?bot) (?:know|find out|hear|learn|get)\b",
    r"\bhow (?:did|do) (?:you|jack ?bot) (?:see|read|access)\b",
    r"\bwhere (?:did|do) (?:you|jack ?bot) (?:get|find|hear|see|read)\b",
    r"\bwho told (?:you|jack ?bot)\b",
    r"\b(?:are|do|can|did) you (?:read|reading|see|seeing|access|accessing|look|looking|go|going) "
    r"(?:at |through |into )?(?:my|our|his|her|their|people'?s|everyone'?s|the team'?s)\b",
    r"\b(?:are|do|can) you (?:monitor|monitoring|watch|watching|spy|spying|snoop|snooping|track|tracking)\b",
    r"\bdo you have access to\b",
    r"\bwhat (?:data )?(?:sources|access|permissions) do you\b",
    r"\bhow (?:much|many) (?:of )?(?:my|our) .{0,20}\b(?:can|do) you\b",
    r"\bexplain yourself\b",
    r"\bprove it\b",
    r"\bwhy do you (?:know|have)\b",
    r"\byou (?:weren'?t|were not|aren'?t) (?:on|copied on|cc'?d on|a recipient)\b",
    r"\bwasn'?t sent to you\b",
    r"\bnobody told you\b|\bno one told you\b",
]
_RE = [re.compile(p, re.IGNORECASE) for p in _PATTERNS]


def is_provenance_question(text):
    """True if the message is asking how the bot knows something, or what it can see."""
    if not text:
        return False
    return any(r.search(text) for r in _RE)


def _fallback():
    """Used when the API is unavailable. Truth matters more than phrasing here."""
    return (
        "*Where my information comes from:*\n"
        "• I read each employee's own Gmail inbox directly — *subject lines and "
        "senders only, never message bodies* — for anything received in the last "
        "24 hours. I don't need to be a recipient to see it.\n"
        "• Also: your calendar for today, file names in the Sales and Federal "
        "Projects shared drives, the latest BST Internal Update Meeting notes, "
        "Asana, Toggl, monitored Slack channels, and the Rippling PTO feed.\n"
        "• All Google access is read-only.\n\n"
        "If an email showed up in your priorities, it's because I read the "
        "subject line out of your inbox. Jack Elston owns this configuration."
    )


def answer_provenance(question, asker_name=None):
    """Answer a data-access question from the fixed fact block."""
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        return _fallback()

    asker = f"\n\nASKER: {asker_name}" if asker_name else ""
    try:
        client = anthropic.Anthropic(api_key=api_key)
        resp = client.messages.create(
            model=MODEL,
            max_tokens=600,
            system=PROVENANCE_SYSTEM,
            messages=[{
                "role": "user",
                "content": f"FACTS:\n{FACTS}\n\nQUESTION: {question}{asker}",
            }],
        )
        text = "".join(b.text for b in resp.content if getattr(b, "type", "") == "text").strip()
        return text or _fallback()
    except Exception:
        return _fallback()
