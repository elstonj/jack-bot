import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from flask import Flask, request

from weather import format_weather
from personality import get_response

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


@app.event("app_mention")
def handle_mention(event, say, client):
    import re
    text = event.get("text", "")
    message = re.sub(r"<@[A-Z0-9]+>\s*", "", text).strip()

    if message.lower().startswith("weather"):
        say(format_weather())
    else:
        user_name = resolve_user_name(client, event["user"])
        say(get_response(message, user_name))


@app.event("message")
def handle_dm(event, say, client):
    if event.get("channel_type") != "im":
        return
    if event.get("bot_id"):
        return
    text = event.get("text", "").strip()

    if text.lower().startswith("weather"):
        say(format_weather())
    else:
        user_name = resolve_user_name(client, event["user"])
        say(get_response(text, user_name))


@flask_app.route("/slack/commands", methods=["POST"])
def slack_commands():
    return handler.handle(request)


@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)


@flask_app.route("/health", methods=["GET"])
def health():
    return "OK"


if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
