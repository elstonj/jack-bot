"""Snow Day Beer alerts — the one thing Jack Bot is genuinely happy about.

Two alerts fire per snow day, dedup'd via channel-history scan:
  - Morning: the first hour we detect active snow between 9am–5pm MT, fire a
    "snow day beer is required" heads-up.
  - EOD: at 3:30 PM MT, if snow has fallen any time today (or is still falling),
    fire a dramatic shutdown notice telling the humans to just go to the pub.

Both messages are generated through Claude so the phrasing varies each time;
if the API call fails we fall back to a static message so the alert always
fires.  Dedup markers are embedded as short italic trailers in the message
text, which is stable regardless of how Claude phrases the rest.
"""

import os
from datetime import datetime
from zoneinfo import ZoneInfo

import anthropic
import requests

# 2840 Wilderness Pl, Boulder CO 80301 (BST HQ)
BST_HQ_LAT = 40.0291
BST_HQ_LON = -105.2549

# WMO weather codes that mean snow is currently falling.
# 71/73/75 = slight/moderate/heavy snow fall, 77 = snow grains,
# 85/86 = slight/heavy snow showers.  Excludes freezing rain (66/67)
# and rime fog (48) — those aren't snow-day-beer worthy.
_ACTIVE_SNOW_CODES = {71, 73, 75, 77, 85, 86}

# Stable trailers appended to each message; also used as dedup markers when
# scanning today's channel history.
_MORNING_MARKER = "_— snow-day beer alert_"
_EOD_MARKER = "_— snow-day shutdown notice_"

_BREWERY_FOOTER = (
    "Preferred watering holes within walking distance:\n"
    "• *Vision Quest Brewing* — https://visionquestbrewery.com\n"
    "• *Twisted Pine Brewing* — https://twistedpinebrewing.com"
)

# Persona for generated snow-day messages.  Deliberately shorter than the
# main chat system prompt — no help-menu boilerplate, just the voice.
_PERSONA_SYSTEM = (
    "You are Jack Bot, a bitter old-school Unix programmer living in Boulder, "
    "Colorado. You absolutely love winter and snow — it's the one thing that "
    "makes you genuinely happy. Your humor is dry, sarcastic, and short. You "
    "never use emojis. You occasionally reference classic Unix commands, man "
    "pages, or old-school programming concepts. Keep output tight — you're "
    "not writing an essay."
)

_MORNING_FALLBACK = (
    "*Snow Day Beer* — it's actively snowing at BST HQ. Finally, weather "
    "worth respecting. Grab a pint at lunch, or head out at the end of the "
    "day when you're wrapping up."
)

_EOD_FALLBACK = (
    "*Computing resources: going down.* Snow fell today at BST HQ, which "
    "means the natural order has been restored. I'm shutting down Slack, "
    "the servers, and every other machine with a power button. Give up, "
    "humans. Go find a Snow Day Beer."
)

_anthropic_client = None


def _get_anthropic_client():
    global _anthropic_client
    if _anthropic_client is None:
        _anthropic_client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    return _anthropic_client


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


def snowed_today() -> bool:
    """Return True if any active-snow signal appeared today in MT."""
    denver = ZoneInfo("America/Denver")
    now_mt = datetime.now(denver)
    # +1 so the current hour's bucket is included in past_hours.
    past_hours = max(now_mt.hour + 1, 1)

    try:
        resp = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": BST_HQ_LAT,
                "longitude": BST_HQ_LON,
                "hourly": "weather_code,snowfall",
                "timezone": "America/Denver",
                "past_hours": past_hours,
                "forecast_hours": 1,
            },
            timeout=10,
        )
        resp.raise_for_status()
    except Exception:
        return False

    data = resp.json()
    hourly = data.get("hourly") or {}
    times = hourly.get("time") or []
    codes = hourly.get("weather_code") or []
    snow = hourly.get("snowfall") or []
    today_prefix = now_mt.strftime("%Y-%m-%d")
    for i, t in enumerate(times):
        if not t.startswith(today_prefix):
            continue
        if i < len(codes) and codes[i] in _ACTIVE_SNOW_CODES:
            return True
        if i < len(snow) and (snow[i] or 0) > 0:
            return True
    return False


def _generate_flavor(user_prompt: str, fallback: str) -> str:
    """Ask Claude to write the body in Jack Bot voice; fall back on failure."""
    try:
        client = _get_anthropic_client()
        resp = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=300,
            system=_PERSONA_SYSTEM,
            messages=[{"role": "user", "content": user_prompt}],
        )
        text = (resp.content[0].text or "").strip()
        return text or fallback
    except Exception:
        return fallback


def _morning_message() -> str:
    flavor = _generate_flavor(
        "Snow has started falling at BST HQ in Boulder. In 2–4 sentences, "
        "announce to the #operations Slack channel that Snow Day Beer is now "
        "required. Stay in character. Do not list brewery names or links — "
        "those are appended afterward. Vary the phrasing; write it fresh.",
        _MORNING_FALLBACK,
    )
    return f"{flavor}\n\n{_BREWERY_FOOTER}\n\n{_MORNING_MARKER}"


def _eod_message() -> str:
    flavor = _generate_flavor(
        "It snowed today at BST HQ in Boulder and the workday is winding "
        "down. In 3–5 sentences, melodramatically announce to the "
        "#operations Slack channel that you — Jack Bot — are now shutting "
        "down BST's Slack, the servers, and every other computing resource, "
        "so the humans might as well give up and head out for Snow Day "
        "Beers. Dry, sarcastic, a little theatrical. Do not list brewery "
        "names or links — those are appended afterward. Vary the phrasing; "
        "write it fresh.",
        _EOD_FALLBACK,
    )
    return f"{flavor}\n\n{_BREWERY_FOOTER}\n\n{_EOD_MARKER}"


def _already_posted_today(slack_client, channel: str, marker: str) -> bool:
    """Return True if a message containing `marker` was posted to `channel` today."""
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
        if marker in (msg.get("text") or ""):
            return True
    return False


def check_and_post(slack_client) -> bool:
    """Morning alert: post a Snow Day Beer heads-up if it's snowing now."""
    channel = os.environ.get("DAILY_TASKS_CHANNEL", "")
    if not channel:
        return False
    if not is_snowing_now():
        return False
    if _already_posted_today(slack_client, channel, _MORNING_MARKER):
        return False
    try:
        slack_client.chat_postMessage(channel=channel, text=_morning_message())
        return True
    except Exception:
        return False


def check_and_post_eod(slack_client) -> bool:
    """EOD alert: dramatic shutdown notice if snow fell any time today."""
    channel = os.environ.get("DAILY_TASKS_CHANNEL", "")
    if not channel:
        return False
    if not (snowed_today() or is_snowing_now()):
        return False
    if _already_posted_today(slack_client, channel, _EOD_MARKER):
        return False
    try:
        slack_client.chat_postMessage(channel=channel, text=_eod_message())
        return True
    except Exception:
        return False
