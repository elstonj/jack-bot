"""Privacy / HR screen for anything Jack Bot posts to a shared channel.

The daily pipeline impersonates every employee's Gmail, Calendar and Drive, so
material that is private by default — compensation, medical, personnel actions,
legal, M&A — reaches the synthesis prompt as a matter of course. Nothing in the
pipeline used to stop it from coming back out in a public #operations post, and
the calendar line was the worst offender: `_calendar_line()` renders event
titles verbatim with no model in the loop at all.

Two layers keep it out of shared channels:

  1. `redact_field()` / `redact_calendar_title()` — deterministic pattern
     redaction applied at INGESTION, before the prompt is assembled. This is
     data minimisation: the model cannot leak what it was never shown.
  2. `screen_public_text()` — a Haiku pass over assembled output that returns
     the LINE NUMBERS to redact. It never rewrites text; the code does the
     redaction. That preserves the deterministic-rendering contract that makes
     the identity header, calendar and hours lines trustworthy, and it means a
     screener failure can never scramble a section.

DMs are never screened — a person's own data going back to that person is not a
leak, and screening it would make `tasks` less useful than reading Asana.
"""

import os
import re

# What a redacted line/field looks like in a public post. The marker is
# deliberately visible: a silently dropped line gives nobody a chance to notice
# the screen misfired.
REDACTION_MARKER = ":lock: _Private — withheld from this channel_"
FIELD_MARKER = "(private)"
CALENDAR_MARKER = ":lock: Private"

# Deterministic patterns. These are the floor, not the ceiling — they catch
# material that announces itself ("Termination letter", "Q3 comp review") and
# the model screen catches the rest. Written to avoid this company's vocabulary:
# bare "acquisition" is excluded because *data acquisition* is everyday sensor
# work here, and "raise" only counts as "pay raise".
_SENSITIVE_PATTERNS = [
    # Personnel actions
    r"\b(?:terminat(?:e|ed|ion|ing)|fired|firing|laid off|lay ?offs?|severance"
    r"|resignation|resigning|performance improvement plan|PIPs?"
    r"|disciplinary|written warning|final warning|corrective action"
    r"|grievance|misconduct|harassment|discriminat(?:ion|ory)|hostile work"
    r"|exit interview|offboarding|reduction in force|RIF)\b",
    # Compensation
    r"\b(?:salar(?:y|ies)|compensation|comp review|pay raise|merit increase"
    r"|bonus(?:es)?|equity grant|stock options?|RSUs?|payroll|W-?2|1099"
    r"|401\(?k\)?|offer letter|pay stub|pay band|market adjustment)\b",
    # Medical / protected leave
    r"\b(?:medical|doctor'?s? (?:appt|appointment|note)|physician|therapy"
    r"|therapist|counsel+ing|surgery|diagnosis|oncolog\w*|chemo\w*|MRI"
    r"|hospital|clinic|prescription|FMLA|disabilit(?:y|ies)|workers'? comp"
    r"|sick leave|medical leave|mental health|bereavement|hospice)\b",
    # Legal
    r"\b(?:attorney|lawyer|legal counsel|outside counsel|litigation|lawsuit"
    r"|subpoena|deposition|settlement agreement|legal hold|privileged"
    r"|cease and desist|arbitration)\b",
    # Personal
    r"\b(?:divorce|custody|funeral|immigration|visa status|green card|I-9"
    r"|bankruptcy|garnishment|personal loan)\b",
    # Corporate confidential / M&A
    r"\b(?:due diligence|diligence|merger|M&A|term sheet|data ?room"
    r"|cap table|definitive agreement|letter of intent|acquisition target"
    r"|acquisition discussions)\b",
]

_SENSITIVE_RE = re.compile("|".join(_SENSITIVE_PATTERNS), re.I)

# Company-specific confidential terms, comma-separated, via env. No wordlist can
# infer that a codename like "KrateoSky process" means an M&A workstream, and the
# model pass only catches euphemisms probabilistically — naming the term here
# makes it a deterministic redaction instead of a coin flip.
#   PRIVACY_EXTRA_TERMS="krateosky process,revenue questions,project atlas"
_EXTRA_ENV = "PRIVACY_EXTRA_TERMS"
_extra_cache = (None, None)  # (raw env value, compiled regex or None)


def _extra_re():
    global _extra_cache
    raw = os.environ.get(_EXTRA_ENV, "")
    if _extra_cache[0] == raw:
        return _extra_cache[1]
    terms = [re.escape(t.strip()) for t in raw.split(",") if t.strip()]
    compiled = re.compile("|".join(terms), re.I) if terms else None
    _extra_cache = (raw, compiled)
    return compiled

# Lines the screen must never touch, because they carry identity or are
# generated from source records rather than written by a model.
_PROTECTED_PREFIXES = ("*<@", ":clock1:", ":mega:")


def is_shared_channel(channel_id):
    """True if `channel_id` is a channel other people can read.

    Slack DM channel IDs start with `D`. Everything else — public channels,
    private channels, group DMs — is shared and gets screened.
    """
    return bool(channel_id) and not str(channel_id).startswith("D")


# Whole documents that are personnel records: payroll journals, cost-share
# "match documentation" (full payroll registers), offer letters, HR/leave
# projects. These sit in knowledge/proposals/ alongside ordinary proposals, so
# Q&A could quote a coworker's salary to anyone who asked. Matched by filename
# and, because registers turn up under arbitrary names, by content.
_PERSONNEL_FILENAME = re.compile(
    r"payroll|expense_documentation|cash_requirements|withholding|timesheet"
    r"|pay_?stub|w-?2\b|1099|offer_letter|hr_general|_pto\b|pto\.md|sick_leave"
    r"|compensation|benefits|match_documentation",
    re.I,
)
_PERSONNEL_CONTENT = re.compile(
    r"net pay\b|gross (?:pay|salary|wages)\b|withholdings? (?:&|and) deductions",
    re.I,
)


def is_personnel_record(filename, text=""):
    """True if a knowledge file is a payroll/HR record that must never be
    quoted to anyone (Q&A context, shared exports)."""
    return bool(_PERSONNEL_FILENAME.search(filename or "")
                or _PERSONNEL_CONTENT.search(text or ""))


def contains_sensitive(text):
    """True if `text` trips a deterministic sensitivity pattern."""
    if not text:
        return False
    text = str(text)
    if _SENSITIVE_RE.search(text):
        return True
    extra = _extra_re()
    return bool(extra and extra.search(text))


def redact_field(text, marker=FIELD_MARKER):
    """Redact a whole short field (email subject, filename, project name).

    Subjects and filenames are short enough that the sensitive part usually *is*
    the whole field, so this replaces rather than masks in place.
    """
    if not text:
        return text
    return marker if contains_sensitive(text) else text


def redact_calendar_title(title):
    """Redact a calendar event title, keeping the slot itself visible.

    The time still renders, so the availability signal — the reason the calendar
    line exists — survives redaction.
    """
    if not title:
        return title
    return CALENDAR_MARKER if contains_sensitive(title) else title


_CAL_PREFIX = ":calendar: "
_CAL_SEP = " · "


def _is_protected(line):
    return line.strip().startswith(_PROTECTED_PREFIXES)


def _to_units(lines):
    """Flatten lines into independently screenable units.

    A calendar line packs a whole day into one string, so screening it whole
    means one sensitive appointment blanks every other meeting on it. Splitting
    per event gives both the pattern screen and the model event-level
    granularity — "Revenue Questions 09:00-09:30" can be pulled while "Friday
    Flyday 10:00-14:00" stays.

    Returns a list of (line_index, event_index_or_None, text).
    """
    units = []
    for i, line in enumerate(lines):
        if _is_protected(line):
            continue
        stripped = line.strip()
        if stripped.startswith(_CAL_PREFIX):
            body = stripped[len(_CAL_PREFIX):]
            for j, event in enumerate(body.split(_CAL_SEP)):
                units.append((i, j, event))
        else:
            units.append((i, None, line))
    return units


def _apply(lines, units, redacted_idx):
    """Rebuild `lines` with the flagged units replaced by their marker."""
    out = list(lines)
    calendar_events = {}  # line_index -> [event text or CALENDAR_MARKER]

    for u, (line_i, event_i, text) in enumerate(units):
        hit = u in redacted_idx
        if event_i is None:
            if hit:
                out[line_i] = REDACTION_MARKER
        else:
            calendar_events.setdefault(line_i, []).append(
                CALENDAR_MARKER if hit else text
            )

    for line_i, events in calendar_events.items():
        # Collapse consecutive redacted events so a bad day isn't a wall of locks.
        collapsed = [e for k, e in enumerate(events)
                     if e != CALENDAR_MARKER or k == 0 or events[k - 1] != CALENDAR_MARKER]
        out[line_i] = _CAL_PREFIX + _CAL_SEP.join(collapsed)

    return out


SCREEN_TOOL = {
    "name": "flag_private_lines",
    "description": "Report which numbered lines must not be posted to a shared "
                   "company Slack channel.",
    "input_schema": {
        "type": "object",
        "properties": {
            "private_line_numbers": {
                "type": "array",
                "items": {"type": "integer"},
                "description": "1-based numbers of lines that would expose "
                               "private personnel, medical, legal, compensation "
                               "or confidential-corporate information. Empty if none.",
            },
        },
        "required": ["private_line_numbers"],
    },
}

SCREEN_PROMPT = """You screen messages before an assistant posts them to a \
company-wide Slack channel at an aerospace/UAS company. Every employee can read \
that channel.

You are given numbered lines. Return the line numbers that must NOT be posted \
publicly because they would expose information that is private to an individual \
or restricted to leadership.

FLAG a line if it reveals:
- Personnel matters: performance concerns, discipline, termination, resignation, \
  hiring/offer decisions, complaints or investigations about a person
- Compensation: salary, bonus, equity, payroll, benefits specific to a person
- Medical or protected leave: appointments, conditions, treatment, sick/medical \
  leave, disability, accommodations
- Legal exposure: litigation, counsel, subpoenas, settlements, privileged matters
- Personal life: family, immigration, finances, bereavement
- Confidential corporate activity not yet public: acquisition or merger \
  discussions, financial due diligence, investor diligence, valuation, cap table

Do NOT flag ordinary work. Engineering, flight tests, hardware builds, customer \
orders, proposals, grants, shipping, purchasing, budgets and project deadlines \
are the normal business of this channel and belong there. Government and defense \
customer work (SBIR, SOCOM, NOAA, Navy, USGS) is routine here — do not flag it \
merely for sounding sensitive.

A line naming a meeting with an outside accounting, banking or law firm is worth \
flagging when the subject reads as diligence, valuation or legal exposure.

When genuinely unsure, do not flag it — over-redaction makes the briefing \
useless. Flag only what a reasonable HR lead would pull out of a public post."""


def _client():
    import anthropic
    return anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))


def _model_flagged_units(units, client=None):
    """Ask Haiku which units are private. Returns a set of 0-based unit indices.

    Raises on API failure so the caller can fall back to deterministic-only
    screening rather than posting unscreened text.
    """
    numbered = "\n".join(f"{i}. {text}" for i, (_l, _e, text) in enumerate(units, 1))
    if not numbered.strip():
        return set()

    client = client or _client()
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=500,
        system=SCREEN_PROMPT,
        tools=[SCREEN_TOOL],
        tool_choice={"type": "tool", "name": SCREEN_TOOL["name"]},
        messages=[{"role": "user", "content": numbered}],
    )
    for block in message.content:
        if getattr(block, "type", "") == "tool_use":
            raw = (block.input or {}).get("private_line_numbers") or []
            flagged = set()
            for n in raw:
                try:
                    idx = int(n) - 1
                except (TypeError, ValueError):
                    continue
                if 0 <= idx < len(units):
                    flagged.add(idx)
            return flagged
    return set()


def screen_public_text(text, client=None, use_model=True):
    """Screen `text` for a shared channel. Returns the redacted text.

    Deterministic patterns run first and always. The model pass runs on top and
    only ever *adds* redactions — if it errors, the deterministic result still
    stands, so an API blip degrades the screen instead of disabling it.
    """
    if not text or not str(text).strip():
        return text

    lines = str(text).split("\n")
    units = _to_units(lines)

    flagged = {u for u, (_l, _e, body) in enumerate(units) if contains_sensitive(body)}

    if use_model:
        try:
            flagged |= _model_flagged_units(units, client=client)
        except Exception as exc:  # noqa: BLE001 — never let the screen block a post
            print(f"[WARN] privacy screen model pass failed, "
                  f"pattern screen still applied: {exc}")

    lines = _apply(lines, units, flagged)

    # Collapse a run of adjacent redactions into one marker.
    collapsed = []
    for line in lines:
        if line == REDACTION_MARKER and collapsed and collapsed[-1] == REDACTION_MARKER:
            continue
        collapsed.append(line)
    return "\n".join(collapsed)


def screen_for_channel(text, channel_id, client=None):
    """Screen `text` only if `channel_id` is a shared channel. DMs pass through."""
    if not is_shared_channel(channel_id):
        return text
    return screen_public_text(text, client=client)


def guarded_say(say, channel_id, client=None):
    """Wrap a Slack Bolt `say` so every message to a shared channel is screened.

    Wrapping the transport is what makes coverage complete — `route_message`
    alone has ~29 `say()` call sites, and a screen that has to be remembered at
    each one is a screen that will be missed at one of them.
    """
    if not is_shared_channel(channel_id):
        return say

    def _guarded(text=None, *args, **kwargs):
        if isinstance(text, str):
            text = screen_public_text(text, client=client)
        if isinstance(kwargs.get("text"), str):
            kwargs["text"] = screen_public_text(kwargs["text"], client=client)
        return say(text, *args, **kwargs) if text is not None else say(*args, **kwargs)

    return _guarded
