import re
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import requests

SITES = [
    {"name": "Boulder Model Airport", "lat": 40.085236, "lon": -105.232711},
    {"name": "Sunny Slope Sod Farm", "lat": 40.135964, "lon": -105.069176},
]

# Aliases people actually use when talking about each site in Slack. Keep these
# distinctive — single-word matches like "boulder" or "sod" alone are too broad.
SITE_ALIASES = {
    "Boulder Model Airport": [
        "boulder model airport", "boulder model", "model airport", "bma",
    ],
    "Sunny Slope Sod Farm": [
        "sunny slope sod farm", "sunny slope", "sod farm", "the sod farm",
    ],
}

# Words that, combined with a known site name, indicate a weather/flying-
# conditions request.
_WEATHER_KEYWORDS = (
    "weather", "wind", "gust", "gusts", "gusty", "forecast", "rain",
    "snow", "precip", "precipitation", "temperature", "temp ", "cloud",
    "cloudy", "conditions", "fly", "flying", "flyable", "flight",
)

# "weather" is also a proper-noun component in many phrases that have
# nothing to do with the forecast (e.g. "53rd Weather Squadron", "weather
# report meeting"). Reject those before treating the lone word as a topic.
_WEATHER_BLOCKLIST = re.compile(
    r"\bweather\s+(squadron|service|channel|station|company|bureau|"
    r"underground|report|update|briefing|brief|vane|deck|man|men|woman|"
    r"women|balloon|balloons)\b"
)


def match_sites(text: str):
    """Return the SITES whose name or alias appears in `text` (empty if none)."""
    tl = text.lower()
    matched = []
    for site in SITES:
        aliases = SITE_ALIASES.get(site["name"], [site["name"].lower()])
        if any(a in tl for a in aliases):
            matched.append(site)
    return matched


def is_weather_intent(text: str) -> bool:
    """Return True if `text` looks like a weather / flying-conditions request.

    The lone word "weather" is *not* enough — it appears in plenty of
    proper-noun phrases ("53rd Weather Squadron", "weather report meeting")
    that should not trigger a forecast post. We require one of:
      - a known site name/alias plus a weather keyword
        ("wind at the sod farm", "can we fly at BMA today")
      - explicit flying-conditions phrasing ("can we fly", "flyable")
      - "weather" used as the actual topic ("weather today",
        "what's the weather", message starting with "weather")
    """
    tl = text.lower().strip()

    if match_sites(text) and any(kw in tl for kw in _WEATHER_KEYWORDS):
        return True

    if any(p in tl for p in (
        "can we fly", "are we flying", "flyable", "flight conditions"
    )):
        return True

    if "weather" not in tl:
        return False
    if _WEATHER_BLOCKLIST.search(tl):
        return False

    if tl.startswith("weather"):
        return True
    if re.search(r"\bthe\s+weather\b", tl):
        return True
    if re.search(r"\bweather\s+(today|tomorrow|tonight|forecast|outside|like)\b", tl):
        return True
    if re.search(r"\bwhat'?s\s+the\s+weather\b", tl):
        return True
    if re.search(r"\bhow'?s\s+the\s+weather\b", tl):
        return True
    return False

# Open-Meteo WMO weather codes
WMO_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    77: "Snow grains",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm w/ slight hail",
    99: "Thunderstorm w/ heavy hail",
}


def fetch_weather(lat: float, lon: float) -> dict:
    """Fetch current and hourly weather from Open-Meteo API."""
    resp = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": lat,
            "longitude": lon,
            "current": ",".join([
                "temperature_2m",
                "relative_humidity_2m",
                "weather_code",
                "wind_speed_10m",
                "wind_gusts_10m",
                "wind_direction_10m",
            ]),
            "hourly": ",".join([
                "wind_speed_10m",
                "wind_gusts_10m",
                "wind_direction_10m",
                "precipitation_probability",
                "precipitation",
            ]),
            "temperature_unit": "fahrenheit",
            "wind_speed_unit": "mph",
            "timezone": "America/Denver",
            "forecast_hours": 24,
        },
        timeout=10,
    )
    resp.raise_for_status()
    return resp.json()


def wind_direction_label(degrees: float) -> str:
    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                   "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    idx = round(degrees / 22.5) % 16
    return directions[idx]


def format_hourly_forecast(hourly: dict) -> str:
    """Format the next 6 hours of wind and precip."""
    denver = ZoneInfo("America/Denver")
    now = datetime.now(denver)
    lines = []
    count = 0
    for i, time_str in enumerate(hourly["time"]):
        hour_dt = datetime.fromisoformat(time_str).replace(tzinfo=denver)
        if hour_dt <= now:
            continue
        wind = hourly["wind_speed_10m"][i]
        gusts = hourly["wind_gusts_10m"][i]
        wind_dir = wind_direction_label(hourly["wind_direction_10m"][i])
        precip_prob = hourly["precipitation_probability"][i]
        precip = hourly["precipitation"][i]
        label = hour_dt.strftime("%-I%p").lower()
        precip_str = f"{precip_prob}%"
        if precip > 0:
            precip_str += f" ({precip}in)"
        lines.append(f"  {label}: {wind} mph {wind_dir} (G{gusts}) | precip {precip_str}")
        count += 1
        if count >= 6:
            break
    return "\n".join(lines)


def format_weather(sites=None) -> str:
    """Build a formatted weather string.

    Args:
        sites: Optional list of SITE dicts to include. When None or empty,
            reports on every configured site.
    """
    target = sites if sites else SITES
    blocks = []
    for site in target:
        try:
            data = fetch_weather(site["lat"], site["lon"])
            current = data["current"]
            hourly = data["hourly"]
            code_desc = WMO_CODES.get(current["weather_code"], "Unknown")
            wind_dir = wind_direction_label(current["wind_direction_10m"])
            forecast = format_hourly_forecast(hourly)
            blocks.append(
                f"*{site['name']}*\n"
                f"  {code_desc} | {current['temperature_2m']}°F\n"
                f"  Wind: {current['wind_speed_10m']} mph {wind_dir} "
                f"(gusts {current['wind_gusts_10m']} mph)\n"
                f"  Humidity: {current['relative_humidity_2m']}%\n"
                f"  _Next 6 hours:_\n{forecast}"
            )
        except Exception as e:
            blocks.append(f"*{site['name']}*\n  Error fetching weather: {e}")
    blocks.append("Detailed site info: https://weather.bst.aero")
    return "\n\n".join(blocks)
