"""Snow Day Beer alerts — the one thing Jack Bot is genuinely happy about.

Checks the current weather at BST HQ and, if it's actively snowing, posts a
beer call-out in the daily tasks channel.  Runs hourly from the scheduler;
dedup is done by scanning today's messages in the channel so the alert fires
at most once per day, regardless of process restarts.
"""

import os
from datetime import datetime
from zoneinfo import ZoneInfo

import requests

# 2840 Wilderness Pl, Boulder CO 80301 (BST HQ)
BST_HQ_LAT = 40.0291
BST_HQ_LON = -105.2549

# WMO weather codes that mean snow is currently falling.
# 71/73/75 = slight/moderate/heavy snow fall, 77 = snow grains,
# 85/86 = slight/heavy snow showers.  Excludes freezing rain (66/67)
# and rime fog (48) — those aren't snow-day-beer worthy.
_ACTIVE_SNOW_CODES = {71, 73, 75, 77, 85, 86}

# The marker string used both in the post and in the dedup scan.  Keep these
# in sync — if the post text changes, dedup still has to find it.
_DEDUP_MARKER = "Snow Day Beer"

_SNOW_DAY_MESSAGE = (
    "*Snow Day Beer* — it's actively snowing at BST HQ. Finally, weather "
    "worth respecting. Wrap up what you're doing and go find a pint.\n"
    "\n"
    "Preferred watering holes within walking distance:\n"
    "• *Vision Quest Brewing* — https://visionquestbrewery.com\n"
    "• *Twisted Pine Brewing* — https://twistedpinebrewing.com\n"
    "\n"
    "_Don't make me explain why snow is the natural order of things._"
)


def is_snowing_now() -> bool:
    """Return True if Open-Meteo reports active snowfall at BST HQ.

    Open-Meteo's `current` reading can lag by 15–30 minutes during transient
    weather, so we also consult the hourly buckets covering now and the most
    recent past hour.  Any active-snow signal across those three windows is
    enough to fire the alert.
    """
    try:
        resp = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": BST_HQ_LAT,
                "longitude": BST_HQ_LON,
                "current": "weather_code,snowfall,precipitation",
                "hourly": "weather_code,snowfall",
                "timezone": "America/Denver",
                "forecast_hours": 2,
                "past_hours": 1,
            },
            timeout=10,
        )
        resp.raise_for_status()
    except Exception:
        return False

    data = resp.json()
    current = data.get("current") or {}
    if (current.get("snowfall") or 0) > 0:
        return True
    if current.get("weather_code") in _ACTIVE_SNOW_CODES:
        return True

    hourly = data.get("hourly") or {}
    codes = hourly.get("weather_code") or []
    snow = hourly.get("snowfall") or []
    for i in range(len(codes)):
        if codes[i] in _ACTIVE_SNOW_CODES:
            return True
        if i < len(snow) and (snow[i] or 0) > 0:
            return True
    return False


def _already_posted_today(slack_client, channel: str) -> bool:
    """Return True if a Snow Day Beer message was already posted today."""
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
        if _DEDUP_MARKER in (msg.get("text") or ""):
            return True
    return False


def check_and_post(slack_client) -> bool:
    """Post a Snow Day Beer alert if conditions warrant. Returns True if posted."""
    channel = os.environ.get("DAILY_TASKS_CHANNEL", "")
    if not channel:
        return False
    if not is_snowing_now():
        return False
    if _already_posted_today(slack_client, channel):
        return False
    try:
        slack_client.chat_postMessage(channel=channel, text=_SNOW_DAY_MESSAGE)
        return True
    except Exception:
        return False
