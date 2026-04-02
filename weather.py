import requests

SITES = [
    {"name": "Boulder Model Airport", "lat": 40.085236, "lon": -105.232711},
    {"name": "Sunny Slope Sod Farm", "lat": 40.135964, "lon": -105.069176},
]

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
    """Fetch current weather from Open-Meteo API."""
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
            "temperature_unit": "fahrenheit",
            "wind_speed_unit": "mph",
        },
        timeout=10,
    )
    resp.raise_for_status()
    return resp.json()["current"]


def wind_direction_label(degrees: float) -> str:
    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                   "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    idx = round(degrees / 22.5) % 16
    return directions[idx]


def format_weather() -> str:
    """Build a formatted weather string for all flying sites."""
    blocks = []
    for site in SITES:
        try:
            data = fetch_weather(site["lat"], site["lon"])
            code_desc = WMO_CODES.get(data["weather_code"], "Unknown")
            wind_dir = wind_direction_label(data["wind_direction_10m"])
            blocks.append(
                f"*{site['name']}*\n"
                f"  {code_desc} | {data['temperature_2m']}°F\n"
                f"  Wind: {data['wind_speed_10m']} mph {wind_dir} "
                f"(gusts {data['wind_gusts_10m']} mph)\n"
                f"  Humidity: {data['relative_humidity_2m']}%"
            )
        except Exception as e:
            blocks.append(f"*{site['name']}*\n  Error fetching weather: {e}")
    return "\n\n".join(blocks)
