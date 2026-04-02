import os
import re
import threading
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from flask import Flask, request

from weather import format_weather
from personality import get_response
from research_cache import get_full_summary, get_user_summary, is_stale
from scheduler import start_scheduler

load_dotenv()

app = App(
    token=os.environ["SLACK_BOT_TOKEN"],
    signing_secret=os.environ["SLACK_SIGNING_SECRET"],
)

flask_app = Flask(__name__)
handler = SlackRequestHandler(app)


@app.command("/weather")
def handle_weather(ack, respond):
    ack()
    respond(response_type="in_channel", text=format_weather())


def resolve_user_name(client, user_id):
    try:
        result = client.users_info(user=user_id)
        return result["user"]["profile"].get("display_name") or result["user"]["real_name"]
    except Exception:
        return "someone"


def get_bot_user_id(client):
    try:
        return client.auth_test()["user_id"]
    except Exception:
        return None


def fetch_history(client, channel, limit=20):
    """Fetch recent messages from a channel/DM for context."""
    try:
        result = client.conversations_history(channel=channel, limit=limit)
        messages = result.get("messages", [])
        messages.reverse()
        return messages
    except Exception:
        return []


def handle_tasks_command(say, message, user_id):
    """Serve cached task summary."""
    full, generated_at = get_full_summary()

    if full is None or is_stale():
        say("No daily briefing available yet. The morning research runs at 8am MT on weekdays.")
        return

    timestamp = generated_at.strftime("%-I:%M %p MT")

    if "all" in message.lower() or "team" in message.lower():
        say(f"_Daily briefing generated at {timestamp}_\n\n{full}")
    else:
        user_summary = get_user_summary(user_id)
        if user_summary:
            say(f"_Generated at {timestamp}_\n\n{user_summary}")
        else:
            say(f"_Daily briefing generated at {timestamp}_\n\n{full}")


@app.event("app_mention")
def handle_mention(event, say, client):
    text = event.get("text", "")
    message = re.sub(r"<@[A-Z0-9]+>\s*", "", text).strip()

    if message.lower().startswith("weather"):
        say(format_weather())
    elif message.lower().startswith("tasks"):
        handle_tasks_command(say, message, event["user"])
    else:
        user_name = resolve_user_name(client, event["user"])
        history = fetch_history(client, event["channel"])
        bot_id = get_bot_user_id(client)
        say(get_response(message, user_name, history, bot_id))


@app.event("message")
def handle_dm(event, say, client):
    if event.get("channel_type") != "im":
        return
    if event.get("bot_id"):
        return
    text = event.get("text", "").strip()

    if text.lower().startswith("weather"):
        say(format_weather())
    elif text.lower().startswith("tasks"):
        handle_tasks_command(say, text, event["user"])
    else:
        user_name = resolve_user_name(client, event["user"])
        history = fetch_history(client, event["channel"])
        bot_id = get_bot_user_id(client)
        say(get_response(text, user_name, history, bot_id))


@flask_app.route("/slack/commands", methods=["POST"])
def slack_commands():
    return handler.handle(request)


@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)


@flask_app.route("/health", methods=["GET"])
def health():
    return "OK"


if os.environ.get("ASANA_ACCESS_TOKEN"):
    start_scheduler()
    # Populate cache on startup during work hours
    from daily_research import maybe_run_on_startup
    from slack_sdk import WebClient
    _startup_client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
    threading.Thread(target=maybe_run_on_startup, args=(_startup_client,), daemon=True).start()

if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
