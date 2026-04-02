import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from flask import Flask, request

from weather import format_weather

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


@app.event("app_mention")
def handle_mention(event, say):
    text = event.get("text", "").lower()
    # Strip the bot mention to get the actual message
    # Mentions look like: <@U12345> weather
    import re
    message = re.sub(r"<@[A-Z0-9]+>\s*", "", text).strip()

    if "weather" in message:
        say(format_weather())
    else:
        say(f"Hi <@{event['user']}>! Try asking me about `weather`.")


@app.event("message")
def handle_dm(event, say):
    # Only respond to DMs (not channel messages without mention)
    if event.get("channel_type") != "im":
        return
    text = event.get("text", "").lower()

    if "weather" in text:
        say(format_weather())
    else:
        say("Hi! Try asking me about `weather`.")


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
