"""Eldora overnight snow-report bulletin.

At 6:30 AM MT on weekdays we query Open-Meteo at Eldora's coordinates and
sum hourly snowfall across the window from 4 PM yesterday through the
current hour.  If the total clears 6 inches we post a tongue-in-cheek
bulletin calling a mandatory 8 AM meeting at "BST Mountain Operations"
(the running joke for Eldora).  Over 12 inches the tone escalates into
no-friends powder day territory.

Messages are generated via Claude in Jack Bot voice so phrasing varies;
static fallbacks keep the alert firing if the API call fails.  Dedup is
done by scanning today's channel history for a stable marker trailer —
same pattern as `snow_day.py`.
"""

import os
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import anthropic
import requests

# Eldora Mountain Resort base area
ELDORA_LAT = 39.9372
ELDORA_LON = -105.5822

_MIN_MEETING_INCHES = 6.0
_MIN_POWDER_INCHES = 12.0

_MARKER = "_— eldora snow report_"

_PERSONA_SYSTEM = (
    "You are Jack Bot, a bitter old-school Unix programmer in Boulder, "
    "Colorado. You absolutely love winter and skiing — Eldora is a short "
    "drive up the hill and a powder day there is the best thing in your "
    "week. Your humor is dry, sarcastic, and short. You never use emojis. "
    "You occasionally reference classic Unix commands, man pages, or "
    "old-school programming concepts. Keep output tight."
)

# Fallbacks used when the Claude call fails.  Format-string interpolates inches.
_MEETING_FALLBACK = (
    "*Mandatory BST Mountain Operations meeting — 8:00 AM sharp.* {inches:.1f}\" "
    "fell at Eldora overnight. All personnel are directed to report to the "
    "BST Mountain Operations site for an all-hands hazard survey. Bring "
    "skis or a board. Non-attendance will be noted in your /etc/passwd entry."
)

_POWDER_FALLBACK = (
    "*STOKE IS HIGH.* {inches:.1f}\" at Eldora overnight. This is not a drill "
    "and it is not a meeting — it's a no-friends powder day. Clear the "
    "calendar, ignore your inbox, and get to the hill. BST Mountain "
    "Operations is convening on first chair."
)

_anthropic_client = None


def _get_anthropic_client():
    global _anthropic_client
    if _anthropic_client is None:
        _anthropic_client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    return _anthropic_client


def overnight_snowfall_inches():
    """Sum hourly Open-Meteo snowfall at Eldora from 4 PM yesterday to now.

    Returns inches as a float, or None if the API call fails.  Open-Meteo
    reports snowfall in centimeters; we convert at 1 cm = 0.3937 in.
    """
    denver = ZoneInfo("America/Denver")
    now_mt = datetime.now(denver)
    window_start = (now_mt - timedelta(days=1)).replace(
        hour=16, minute=0, second=0, microsecond=0
    )
    # +1 so the current hour bucket is fetched; forecast_hours=1 ensures
    # we get the upcoming bucket even if "now" is mid-hour.
    past_hours = int((now_mt - window_start).total_seconds() // 3600) + 1

    try:
        resp = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": ELDORA_LAT,
                "longitude": ELDORA_LON,
                "hourly": "snowfall",
                "timezone": "America/Denver",
                "past_hours": past_hours,
                "forecast_hours": 1,
            },
            timeout=10,
        )
        resp.raise_for_status()
    except Exception:
        return None

    data = resp.json()
    hourly = data.get("hourly") or {}
    times = hourly.get("time") or []
    snow_cm = hourly.get("snowfall") or []

    total_cm = 0.0
    for i, t in enumerate(times):
        try:
            bucket = datetime.fromisoformat(t).replace(tzinfo=denver)
        except Exception:
            continue
        if bucket < window_start or bucket > now_mt:
            continue
        if i < len(snow_cm) and snow_cm[i]:
            total_cm += snow_cm[i]
    return total_cm * 0.3937


def _generate_flavor(user_prompt: str, fallback: str) -> str:
    try:
        client = _get_anthropic_client()
        resp = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=400,
            system=_PERSONA_SYSTEM,
            messages=[{"role": "user", "content": user_prompt}],
        )
        text = (resp.content[0].text or "").strip()
        return text or fallback
    except Exception:
        return fallback


def _meeting_message(inches: float) -> str:
    prompt = (
        f"{inches:.1f} inches of snow fell overnight at Eldora Mountain Resort "
        "(a short drive up the canyon from Boulder). In 3–5 sentences, write a "
        "deadpan Slack bulletin for the BST #operations channel ordering all "
        "employees to attend a mandatory 8:00 AM sharp meeting at BST's "
        "'Mountain Operations' site. The running joke at BST: 'Mountain "
        "Operations' is a tongue-in-cheek euphemism for Eldora — the 'meeting' "
        "is skiing. Play it completely straight as if it were a real corporate "
        "directive. Mention the snowfall total explicitly. Stay in Jack Bot "
        "character (dry, sarcastic, old-school Unix). No emojis. Vary the "
        "phrasing — write it fresh every time."
    )
    return _generate_flavor(prompt, _MEETING_FALLBACK.format(inches=inches))


def _powder_message(inches: float) -> str:
    prompt = (
        f"{inches:.1f} inches of snow fell overnight at Eldora Mountain Resort. "
        "This is a genuine, rare, no-friends powder day. In 3–5 sentences, "
        "write a Slack post for BST's #operations channel. Jack Bot is "
        "*barely* in character here — the love-of-snow side is winning and "
        "he's urgently telling the whole company to drop what they're doing "
        "and get to Eldora immediately. The 'BST Mountain Operations' joke "
        "(Mountain Operations = Eldora, the 'meeting' is skiing) still "
        "applies but the powder urgency leads. Mention the snowfall total "
        "explicitly. Dry, sarcastic, short, no emojis. Vary the phrasing — "
        "write it fresh every time."
    )
    return _generate_flavor(prompt, _POWDER_FALLBACK.format(inches=inches))


def _already_posted_today(slack_client, channel: str) -> bool:
    denver = ZoneInfo("America/Denver")
    today_start = datetime.now(denver).replace(
        hour=0, minute=0, second=0, microsecond=0
    )
    oldest = str(today_start.timestamp())
    try:
        result = slack_client.conversations_history(
            channel=channel, limit=100, oldest=oldest,
        )
    except Exception:
        # If we can't tell, don't post — avoid spam over robustness.
        return True
    for msg in result.get("messages", []) or []:
        if _MARKER in (msg.get("text") or ""):
            return True
    return False


def check_and_post(slack_client) -> bool:
    """Post an Eldora bulletin if overnight snowfall clears the 6" threshold."""
    channel = os.environ.get("DAILY_TASKS_CHANNEL", "")
    if not channel:
        return False
    inches = overnight_snowfall_inches()
    if inches is None or inches <= _MIN_MEETING_INCHES:
        return False
    if _already_posted_today(slack_client, channel):
        return False
    body = (
        _powder_message(inches)
        if inches > _MIN_POWDER_INCHES
        else _meeting_message(inches)
    )
    text = f"{body}\n\n{_MARKER}"
    try:
        slack_client.chat_postMessage(channel=channel, text=text)
        return True
    except Exception:
        return False
