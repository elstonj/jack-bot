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
_DEDUP_LOOKBACK_DAYS = 14  # don't re-suggest a topic we've already pitched recently

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

CADENCE CALIBRATION — read this carefully:
BST has, on average, 1-2 marketing-worthy moments PER WEEK, not per day.
Most weekdays you should return ZERO items. A normal week looks like:
3-4 days with zero items, 1-2 days with one item, occasionally a day with
two. If you find yourself returning items every day, your bar is too low.
When in doubt, return zero. It is much better to miss a borderline event
than to post about a non-event.

You are given:
- "slack_messages": recent posts across monitored Slack channels (~30h)
- "knowledge_entries": recent substantive knowledge-channel entries (~3 days)
- "already_pitched": headlines this bot has ALREADY suggested in #marketing
  in the last 2 weeks. NEVER re-suggest the same event under any rephrasing.

WHAT QUALIFIES — post-tense, concrete, named, public-facing:
- Contract WON or grant FUNDED (not submitted, not pending — actually awarded)
- Hardware DELIVERED to a named customer (not "preparing to deliver")
- Flight test or demo COMPLETED with a notable result (range, endurance,
  payload, conditions). "Successful flight test of S0 in [conditions]."
- Customer or partner visit that ALREADY HAPPENED (post-event recap with
  something concrete to say — names, what was shown, takeaways)
- Talk GIVEN at a conference, panel, or event (after the fact)
- Press hit that's actually been published
- New hire whose start has already been announced internally
- Capability or product launch that has actually shipped

WHAT DOES NOT QUALIFY — refuse these even if they're in the data:
- "Preparing for", "looking forward to", "next week", "this Friday" — any
  upcoming event. Wait until it has happened.
- Proposals SUBMITTED (those are routine; only WINS qualify).
- "Opportunities emerging", contacts in early conversation, leads,
  potential demos under discussion.
- Internal task assignments, logistics, scheduling, time tracking.
- Bug reports, debugging, code review, internal meetings, agenda items.
- Questions, status checks, "where are we on Y".
- Procurement, shipping notifications, vendor coordination.
- Anything you'd describe as "in progress" or "continuing" rather than "done".
- Anything substantively similar to an "already_pitched" headline, even if
  the new framing differs.

Output ONE JSON object — no fences, no preamble, no closing prose:

{
  "items": [
    {
      "headline": "one short line on what happened (past tense)",
      "suggested_post": "draft social post in BST's professional-but-warm
        voice (max ~280 chars, partner names OK, light on hashtags)",
      "details": ["pertinent detail 1", "pertinent detail 2", ...],
      "sources": ["short pointer to which input signals informed this", ...]
    },
    ...
  ]
}

Rules:
- Empty "items" is the EXPECTED output. Quiet days post nothing. Do NOT
  manufacture content from in-progress work.
- Each item is ONE distinct event. Merge duplicates.
- Cap at 3 items per day. Realistically you'll almost never hit that.
- Headlines must be past tense ("Delivered S3 to USGS", "Hosted SOCOM at
  Boulder facility") — never future tense ("Preparing for...", "Will host...").
- Never invent facts. Every concrete detail (names, dates, customers,
  values) must trace to the input signals.
- BST's voice: precise, technical when relevant, never breathless. Avoid
  "thrilled" / "excited to announce" — let the news carry itself.
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


def _gather_recent_pitches(slack_client, channel: str) -> list[str]:
    """Pull headlines this bot has already pitched to #marketing in the
    last `_DEDUP_LOOKBACK_DAYS` days.

    Headlines are extracted from our own marker-bearing posts. We hand
    these back to Claude as `already_pitched` so it can refuse to
    re-pitch the same event under a new framing.
    """
    oldest = str(int(time.time() - _DEDUP_LOOKBACK_DAYS * 86400))
    try:
        res = slack_client.conversations_history(
            channel=channel, limit=200, oldest=oldest,
        )
    except Exception:
        return []
    headlines: list[str] = []
    # Match either "*1.* <headline>" / "*2.* ..." (multi-item posts) or
    # "*•* <headline>" (single-item posts). Both shapes are produced by
    # _format_post.
    pattern = re.compile(r"^\*(?:\d+\.|•)\*\s+(.+?)$", re.MULTILINE)
    for m in res.get("messages", []) or []:
        text = m.get("text") or ""
        if _MARKER not in text:
            continue
        for hit in pattern.findall(text):
            hit = hit.strip()
            if hit:
                headlines.append(hit[:200])
    return headlines


def _ask_claude(signals: dict) -> dict:
    try:
        client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
        msg = client.messages.create(
            model="claude-sonnet-5",
            thinking={"type": "disabled"},
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
    already_pitched = _gather_recent_pitches(slack_client, channel)

    verdict = _ask_claude({
        "slack_messages": slack_signals,
        "knowledge_entries": knowledge_signals,
        "already_pitched": already_pitched,
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
