"""Marketing assist morning check.

Each weekday morning we sweep the last ~30 hours of company activity —
recent messages from monitored Slack channels, plus substantive knowledge-
channel entries — and ask Claude whether anything is marketing-worthy:
contracts won, deliveries completed, flight tests succeeded, demos /
visits, hires, press hits, customer wins.

If yes, we post a draft suggestion to #marketing pinging Paige (BST's
Communications & Digital Marketing Specialist) — she'll be the one
shipping the actual social post. Quiet days post nothing.

Same trailing-marker dedup pattern eldora.py / snow_day.py use: once
we've posted today, we won't post again.
"""

from __future__ import annotations

import json
import os
import re
import time
from datetime import datetime
from zoneinfo import ZoneInfo

import anthropic

from knowledge import get_knowledge

# Paige Smith — Communications & Digital Marketing Specialist. We ping
# her on the resulting post; she's NOT the trigger / filter for content.
# Stable ID sourced from knowledge/contacts/uid_map.json. If it changes,
# the symptom is a broken @-mention, not a wrong-content post.
PAIGE_SLACK_ID = "U083AAM8E9Y"

_MARKER = "_— marketing assist suggestion_"
_LOOKBACK_HOURS = 30  # cover overnight + late posts from yesterday afternoon
_MAX_SLACK_MESSAGES = 200
_MAX_KNOWLEDGE_ENTRIES = 60

# Knowledge entry types worth scanning. We exclude DEBUG / ERROR / SOURCE /
# SNAPSHOT (pipeline-trace noise) and BUG / FEATURE (internal issue tracking).
_RELEVANT_KNOWLEDGE_TYPES = {
    "PROJECT", "CLIENT", "DELIVERABLE", "TEAM",
    "CORRECTION", "FEEDBACK", "INSIGHT", "PRIORITY",
}


GATE_PROMPT = """\
You are scanning the last ~30 hours of internal activity at BST (Black
Swift Technologies, a small Boulder-based aerospace / UAS company) for
moments worth posting about on the company's social channels. The post
will be drafted for Paige Smith — BST's Communications & Digital Marketing
Specialist — to edit and ship.

You are given a JSON blob containing:
- "slack_messages": recent posts across monitored Slack channels
- "knowledge_entries": recent substantive entries from the bot's knowledge
  channel (project updates, feedback, insights, deliverables, corrections)

Look for ANY of the following — across ALL data, regardless of who posted
or who was tagged:

MARKETING-WORTHY:
- Contract won, award announced, grant funded, RFP / proposal accepted
- Project milestone completed, hardware delivered, customer accepted
- Successful flight test, capability demonstrated, range / endurance record
- Customer or partner visit (DOD/USAF/NASA/SOCOM, university, primes)
- Demo, talk, or conference attendance
- Product or capability launch
- New hire announcement
- Press hit, quote in an article, podcast appearance
- Notable photo / video opportunity (good visual that should be captured)
- Public-facing customer quote or testimonial

NOT MARKETING-WORTHY (skip these even if they came up):
- Routine task assignments, "@person can you do X" requests
- Internal logistics, scheduling, time-tracking discussions
- Bug reports, debugging conversations, code review
- Questions / status checks / "where are we on Y"
- Generic in-progress updates with no concrete achievement
- Internal meeting prep, agenda items, draft documents
- Procurement / shipping discussions unless tied to a milestone

Output ONE JSON object — no fences, no preamble, no closing prose:

{
  "items": [
    {
      "headline": "one short line on what happened",
      "suggested_post": "draft social post in BST's professional-but-warm
        voice (max ~280 chars, partner names OK, light on hashtags)",
      "details": ["pertinent detail 1", "pertinent detail 2", ...],
      "sources": ["short pointer to which input signals informed this", ...]
    },
    ...
  ]
}

Rules:
- Return an empty "items" array if nothing in the window is marketing-worthy.
  Quiet days are normal — do NOT manufacture content.
- Each item is ONE distinct event. If two messages describe the same
  milestone, merge them into one item.
- Cap at 3 items. If more than 3 events qualify, pick the top 3 by impact.
- Never invent facts. Every concrete detail (names, dates, contract values,
  customer names) must trace to the input signals.
- BST's voice: precise, technical when relevant, never breathless. Mention
  partners and customers by name when they're public. Avoid "thrilled" /
  "excited to announce" if you can carry the news on its own merit.
"""


def _gather_slack_activity(slack_client) -> list[dict]:
    """Pull recent messages across monitored channels — full sweep, no filter."""
    raw_channels = os.environ.get("SLACK_MONITORED_CHANNELS", "")
    if not raw_channels:
        return []
    channels = [c.strip() for c in raw_channels.split(",") if c.strip()]
    oldest = str(int(time.time() - _LOOKBACK_HOURS * 3600))

    out: list[dict] = []
    for channel_id in channels:
        try:
            info = slack_client.conversations_info(channel=channel_id)
            channel_name = f"#{info['channel']['name']}"
        except Exception:
            channel_name = channel_id
        try:
            res = slack_client.conversations_history(
                channel=channel_id, limit=100, oldest=oldest,
            )
        except Exception:
            continue
        for msg in res.get("messages", []) or []:
            if msg.get("subtype") or msg.get("bot_id"):
                continue
            text = (msg.get("text") or "").strip()
            if not text or len(text) < 8:
                continue
            out.append({
                "channel": channel_name,
                "user_id": msg.get("user", ""),
                "text": text[:600],
                "ts": msg.get("ts", ""),
            })
        if len(out) >= _MAX_SLACK_MESSAGES:
            break
    return out[:_MAX_SLACK_MESSAGES]


def _gather_knowledge_entries(slack_client) -> list[dict]:
    """Substantive knowledge-channel entries from the last 3 days."""
    try:
        entries = get_knowledge(
            slack_client,
            entry_types=list(_RELEVANT_KNOWLEDGE_TYPES),
            days=3,
        )
    except Exception:
        return []
    out = []
    for e in entries:
        content = (e.get("content") or "").strip()
        if not content:
            continue
        out.append({
            "type": e.get("type", ""),
            "content": content[:800],
            "ts": e.get("ts", ""),
        })
    return out[-_MAX_KNOWLEDGE_ENTRIES:]  # most recent N


def _ask_claude(signals: dict) -> dict:
    try:
        client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
        msg = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2500,
            system=GATE_PROMPT,
            messages=[{"role": "user", "content": json.dumps(signals)[:30000]}],
        )
        raw = msg.content[0].text.strip().strip("`")
        raw = re.sub(r"^json\s*", "", raw, flags=re.IGNORECASE)
        return json.loads(raw)
    except Exception:
        return {"items": []}


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


def _format_post(items: list[dict]) -> str:
    lines = [
        f":mega: *Marketing assist* — heads-up <@{PAIGE_SLACK_ID}>, "
        f"{'something' if len(items) == 1 else 'a few things'} from the "
        f"last day worth posting about:"
    ]
    for i, item in enumerate(items, start=1):
        headline = (item.get("headline") or "").strip()
        suggested = (item.get("suggested_post") or "").strip()
        details = item.get("details") or []
        sources = item.get("sources") or []
        lines.append("")
        prefix = f"*{i}.*" if len(items) > 1 else "*•*"
        lines.append(f"{prefix} {headline}" if headline else prefix)
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
            lines.append(
                "_Source: " + "; ".join(str(s) for s in sources[:5]) + "_"
            )
    lines.append("")
    lines.append(_MARKER)
    return "\n".join(lines)


def check_and_post(slack_client) -> bool:
    """Sweep recent activity; post a draft to #marketing if anything is noteworthy.

    Returns True if a post was made, False otherwise (no signals, already
    posted today, Claude found nothing noteworthy, or post failed).
    """
    channel = os.environ.get("MARKETING_CHANNEL", "")
    if not channel:
        return False
    if _already_posted_today(slack_client, channel):
        return False

    slack_signals = _gather_slack_activity(slack_client)
    knowledge_signals = _gather_knowledge_entries(slack_client)
    if not slack_signals and not knowledge_signals:
        return False

    verdict = _ask_claude({
        "slack_messages": slack_signals,
        "knowledge_entries": knowledge_signals,
    })
    items = verdict.get("items") or []
    items = [i for i in items if isinstance(i, dict) and i.get("headline")]
    if not items:
        return False

    text = _format_post(items[:3])
    try:
        slack_client.chat_postMessage(channel=channel, text=text)
        return True
    except Exception:
        return False
