"""Marketing assist morning check.

Each weekday morning we look across the last ~30 hours for signals where
Paige Smith (BST's Communications & Digital Marketing Specialist) has
been tagged or mentioned — Slack pings in monitored channels and
knowledge-channel entries about milestones, customer wins, demos, etc.

If anything looks marketing-worthy we hand the signals to Claude and ask
for: a one-line "why this matters", a draft social post in BST's voice,
and the supporting details. The result lands in #marketing for Paige to
edit and ship. Quiet mornings are silent — `check_and_post` returns
without posting if nothing in the window is noteworthy.

Dedup uses the same trailing-marker pattern eldora.py / snow_day.py do:
once we've posted today, we won't post again.
"""

from __future__ import annotations

import json
import os
import re
import time
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import anthropic

from knowledge import get_knowledge

# Paige Smith — Communications & Digital Marketing Specialist.
# Stable IDs sourced from knowledge/contacts/uid_map.json. If they ever
# change the symptom is silent no-ops, not bad posts.
PAIGE_SLACK_ID = "U083AAM8E9Y"
PAIGE_EMAIL = "paige.smith@blackswifttech.com"
PAIGE_NAME_TOKENS = ("paige", "smith")

_MARKER = "_— marketing assist suggestion_"
_LOOKBACK_HOURS = 30  # cover overnight + late posts from yesterday afternoon

# Knowledge entry types worth scanning for marketing signal. We exclude
# DEBUG / ERROR / SOURCE / SNAPSHOT (pipeline-trace noise that often dumps
# the full user roster — including Paige's email — into the channel).
_RELEVANT_KNOWLEDGE_TYPES = {
    "PROJECT", "CLIENT", "DELIVERABLE", "TEAM",
    "CORRECTION", "FEEDBACK", "INSIGHT", "PRIORITY",
}


GATE_PROMPT = """\
You are screening recent BST (Black Swift Technologies, an aerospace / UAS
company) internal signals for content that Paige Smith — Communications &
Digital Marketing Specialist — should know about and potentially post on
the company's social channels.

You are given a JSON blob of:
- Slack mentions / messages where @Paige was tagged or named in monitored
  channels in the last ~30 hours
- Recent knowledge-channel entries (milestones, project updates, feedback,
  insights) that mention Paige or marketing-relevant events

Decide whether ANY of these signals describes a moment worth posting about
externally. Marketing-worthy means: a customer milestone, a flight test or
delivery achievement, a contract / award announcement, an event (visit,
demo, talk), a product or capability launch, a hiring announcement, a
press hit, or a notable photo / video opportunity.

Routine internal logistics, day-to-day task assignments, or generic
"@paige can you handle X" pings with no concrete event attached are NOT
marketing-worthy on their own.

Output ONE JSON object — no fences, no preamble, no closing prose:

{
  "noteworthy": true | false,
  "headline": "one short line on what happened" | null,
  "suggested_post": "draft social post in BST's professional-but-warm voice
    (max ~280 chars, partner names OK, avoid hashtag spam)" | null,
  "details": ["pertinent detail 1", "pertinent detail 2", ...],
  "sources": ["short pointer to which input signals informed this", ...]
}

If noteworthy is false, set headline and suggested_post to null and use
empty arrays for details and sources. Never invent facts — every concrete
detail must trace to the input signals.
"""


def _gather_slack_mentions(slack_client) -> list[dict]:
    """Recent messages in monitored channels that tag/mention Paige."""
    raw_channels = os.environ.get("SLACK_MONITORED_CHANNELS", "")
    if not raw_channels:
        return []
    channels = [c.strip() for c in raw_channels.split(",") if c.strip()]
    oldest = str(int(time.time() - _LOOKBACK_HOURS * 3600))
    mention_token = f"<@{PAIGE_SLACK_ID}>"
    out: list[dict] = []
    for channel_id in channels:
        try:
            info = slack_client.conversations_info(channel=channel_id)
            channel_name = f"#{info['channel']['name']}"
        except Exception:
            channel_name = channel_id
        try:
            res = slack_client.conversations_history(
                channel=channel_id, limit=80, oldest=oldest,
            )
        except Exception:
            continue
        for msg in res.get("messages", []) or []:
            if msg.get("subtype") or msg.get("bot_id"):
                continue
            text = (msg.get("text") or "").strip()
            if not text:
                continue
            low = text.lower()
            if (mention_token in text
                    or "paige" in low
                    or all(t in low for t in PAIGE_NAME_TOKENS)):
                out.append({
                    "channel": channel_name,
                    "user_id": msg.get("user", ""),
                    "text": text[:600],
                    "ts": msg.get("ts", ""),
                })
        if len(out) >= 50:
            break
    return out


def _gather_knowledge_entries(slack_client) -> list[dict]:
    """Knowledge-channel entries from the last 3 days that mention Paige.

    Filters to substantive entry types only — DEBUG and SOURCE entries
    routinely dump the full user roster (including Paige's email), which
    would otherwise match every pipeline run as a false signal.
    """
    try:
        entries = get_knowledge(
            slack_client,
            entry_types=list(_RELEVANT_KNOWLEDGE_TYPES),
            days=3,
        )
    except Exception:
        return []
    matches: list[dict] = []
    for e in entries:
        content = (e.get("content") or "").lower()
        if "paige" in content:
            matches.append({
                "type": e.get("type", ""),
                "content": (e.get("content") or "")[:800],
                "ts": e.get("ts", ""),
            })
    return matches[:50]


def _ask_claude(signals: dict) -> dict:
    try:
        client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
        msg = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1000,
            system=GATE_PROMPT,
            messages=[{"role": "user", "content": json.dumps(signals)[:14000]}],
        )
        raw = msg.content[0].text.strip().strip("`")
        raw = re.sub(r"^json\s*", "", raw, flags=re.IGNORECASE)
        return json.loads(raw)
    except Exception:
        return {"noteworthy": False}


def _already_posted_today(slack_client, channel: str) -> bool:
    denver = ZoneInfo("America/Denver")
    today_start = datetime.now(denver).replace(
        hour=0, minute=0, second=0, microsecond=0
    )
    oldest = str(today_start.timestamp())
    try:
        res = slack_client.conversations_history(
            channel=channel, limit=100, oldest=oldest,
        )
    except Exception:
        # If we can't tell, don't post — we'd rather miss a day than spam.
        return True
    for m in res.get("messages", []) or []:
        if _MARKER in (m.get("text") or ""):
            return True
    return False


def _format_post(verdict: dict) -> str:
    headline = (verdict.get("headline") or "").strip()
    suggested = (verdict.get("suggested_post") or "").strip()
    details = verdict.get("details") or []
    sources = verdict.get("sources") or []
    lines = [f":mega: *Marketing assist* — heads-up <@{PAIGE_SLACK_ID}>"]
    if headline:
        lines.append(f"*Why this matters:* {headline}")
    if suggested:
        lines.append("")
        lines.append("*Suggested post:*")
        for ln in suggested.splitlines():
            lines.append(f"> {ln}")
    if details:
        lines.append("")
        lines.append("*Pertinent details:*")
        for d in details[:8]:
            lines.append(f"• {d}")
    if sources:
        lines.append("")
        lines.append("_Source signals: " + "; ".join(str(s) for s in sources[:5]) + "_")
    lines.append("")
    lines.append(_MARKER)
    return "\n".join(lines)


def check_and_post(slack_client) -> bool:
    """Run the morning marketing scan; post a draft to #marketing if anything is noteworthy.

    Returns True if a post was made, False otherwise (no signals, already
    posted today, Claude said nothing's noteworthy, or post failed).
    """
    channel = os.environ.get("MARKETING_CHANNEL", "")
    if not channel:
        return False
    if _already_posted_today(slack_client, channel):
        return False

    slack_signals = _gather_slack_mentions(slack_client)
    knowledge_signals = _gather_knowledge_entries(slack_client)
    if not slack_signals and not knowledge_signals:
        return False

    verdict = _ask_claude({
        "slack_mentions": slack_signals,
        "knowledge_entries": knowledge_signals,
    })
    if not verdict.get("noteworthy"):
        return False

    text = _format_post(verdict)
    try:
        slack_client.chat_postMessage(channel=channel, text=text)
        return True
    except Exception:
        return False
