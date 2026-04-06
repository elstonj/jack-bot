import os
import re
import threading
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from flask import Flask, request

from weather import format_weather
from personality import get_response
from research_cache import get_full_summary, get_user_summary, get_team_summary, get_per_user_sections, is_stale
from knowledge import store_correction, store_entry, store_feedback, store_bug, store_feature, list_items
from knowledge_qa import answer_question
from finances import get_project_finances
from scheduler import start_scheduler

load_dotenv()

app = App(
    token=os.environ["SLACK_BOT_TOKEN"],
    signing_secret=os.environ["SLACK_SIGNING_SECRET"],
)

flask_app = Flask(__name__)
handler = SlackRequestHandler(app)


@app.command("/refresh-tasks")
def handle_refresh_tasks(ack, respond, client, command):
    knowledge_channel = os.environ.get("KNOWLEDGE_CHANNEL", "")
    if knowledge_channel and command.get("channel_id") != knowledge_channel:
        ack()
        respond("This command can only be run in the #jackbot-knowledge channel.")
        return
    ack()
    respond("Running daily research pipeline... this may take 30-60 seconds.")

    def _run():
        try:
            import time as _time
            from daily_research import run_daily_pipeline
            channel = os.environ.get("DAILY_TASKS_CHANNEL", "#general")
            run_daily_pipeline(client)

            # Post team summary first, then each person separately
            team = get_team_summary()
            if team:
                client.chat_postMessage(channel=channel, text=team)
                _time.sleep(0.5)
            per_user = get_per_user_sections()
            for section in per_user.values():
                client.chat_postMessage(channel=channel, text=section)
                _time.sleep(0.3)
        except Exception as e:
            respond(f"Pipeline failed: {e}")
            try:
                store_entry(client, "ERROR", f"/refresh-tasks failed: {e}")
            except Exception:
                pass

    threading.Thread(target=_run, daemon=True).start()


QUESTION_PREFIXES = ("ask:", "question:", "q:")
QUESTION_STARTERS = (
    "who", "what", "when", "where", "how", "which",
    "can", "does", "is", "are", "has", "have",
)


def is_teaching(text):
    """Return True if the message is teaching the bot something (acronym, fact, correction).

    Detects patterns like:
    - "KS = Krateo Sky"
    - "KS is Krateo Sky"
    - "KS stands for Krateo Sky"
    - "KS means Krateo Sky"
    - "by the way, KS is Krateo Sky"
    - "fyi Daniel handles DCAA"
    """
    lower = text.lower().strip()
    # Direct definition patterns: "X = Y", "X == Y"
    if re.search(r"^[A-Za-z\s]{1,30}\s*=\s*.{2,}", text):
        return True
    # "X is/are Y" patterns (but not questions)
    if "?" not in text and re.search(r"^[A-Za-z\s]{1,30}\s+(?:is|are|means?|stands?\s+for|refers?\s+to)\s+.{2,}", text, re.IGNORECASE):
        return True
    # "fyi", "btw", "for reference", "just so you know" prefixed statements
    if re.match(r"^(?:fyi|btw|by the way|for reference|just so you know|for context)[,:\s]", lower):
        return True
    return False


def is_question(text):
    """Return True if the message should be routed to knowledge Q&A."""
    lower = text.lower().strip()
    # Explicit Q&A prefix
    if any(lower.startswith(p) for p in QUESTION_PREFIXES):
        return True
    # Contains a question mark
    if "?" in text:
        return True
    # Starts with a question word
    first_word = lower.split()[0] if lower.split() else ""
    if first_word in QUESTION_STARTERS:
        return True
    return False


def strip_qa_prefix(text):
    """Remove ask:/question:/q: prefix if present."""
    for prefix in QUESTION_PREFIXES:
        if text.lower().startswith(prefix):
            return text[len(prefix):].strip()
    return text


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

    route_message(message, say, client, event["user"], event.get("channel", ""))


def route_message(message, say, client, user_id, channel_id):
    """Unified routing for all natural language commands."""
    msg_lower = message.lower().strip()

    if msg_lower in ("help", "commands", "what can you do"):
        say(
            "*Here's what I can do:*\n"
            "\n"
            ":clipboard: *tasks* — your prioritized task list (`tasks all` for the team)\n"
            ":partly_sunny: *weather* — flying conditions at local RC sites\n"
            ":dollar: *finances* — project financial summary (in a project channel)\n"
            ":bug: *bug: [description]* — report a bug\n"
            ":sparkles: *feature: [description]* — request a feature\n"
            ":clipboard: *bugs* / *features* — list open items\n"
            ":arrows_counterclockwise: *correct: [feedback]* — fix task priorities\n"
            ":memo: *note: [info]* — teach me something about projects\n"
            ":question: Just ask a question naturally — I'll search the knowledge base\n"
            "\n"
            "_Or just talk to me. I'll be grumpy about it._"
        )
    elif msg_lower.startswith("weather"):
        say(format_weather())
    elif msg_lower.startswith("tasks"):
        handle_tasks_command(say, message, user_id)
    elif msg_lower in ("company finances", "company financial", "all finances"):
        from finances import OVERVIEW_PATH, _summarize_for_slack
        if OVERVIEW_PATH.exists():
            say(_summarize_for_slack(OVERVIEW_PATH.read_text()))
        else:
            say("No company financial overview available yet.")
    elif msg_lower.startswith(("finances", "financial")):
        say(get_project_finances(client, channel_id))
    elif msg_lower.startswith("bug:"):
        desc = re.sub(r"^bug:\s*", "", message, flags=re.IGNORECASE)
        user_name = resolve_user_name(client, user_id)
        store_bug(client, user_name, desc)
        say(f"Bug logged. I'll track it.")
    elif msg_lower.startswith("feature:") or msg_lower.startswith("request:"):
        desc = re.sub(r"^(?:feature|request):\s*", "", message, flags=re.IGNORECASE)
        user_name = resolve_user_name(client, user_id)
        store_feature(client, user_name, desc)
        say(f"Feature request logged.")
    elif msg_lower in ("bugs", "bug list", "show bugs"):
        say(list_items(client, "BUG"))
    elif msg_lower in ("features", "feature list", "show features", "feature requests"):
        say(list_items(client, "FEATURE"))
    elif msg_lower.startswith("correct:") or msg_lower.startswith("correction:"):
        correction = re.sub(r"^correct(?:ion)?:\s*", "", message, flags=re.IGNORECASE)
        user_name = resolve_user_name(client, user_id)
        store_correction(client, user_name, correction)
        say(f"Got it. I'll factor that into future prioritization.")
    elif msg_lower.startswith(("note:", "remember:")):
        note = re.sub(r"^(?:note|remember):\s*", "", message, flags=re.IGNORECASE)
        entry_type = "PRIORITY" if any(w in msg_lower for w in ["priority", "important", "focus"]) else "INSIGHT"
        store_entry(client, entry_type, note)
        say(f"Noted. Stored as [{entry_type}] in the knowledge base.")
    elif is_teaching(message):
        user_name = resolve_user_name(client, user_id)
        store_entry(client, "INSIGHT", f"From {user_name}: {message}")
        say("Got it, noted for future reference.")
    elif is_question(message):
        question = strip_qa_prefix(message)
        say(answer_question(question, slack_client=client))
    else:
        user_name = resolve_user_name(client, user_id)
        history = fetch_history(client, channel_id)
        bot_id = get_bot_user_id(client)
        say(get_response(message, user_name, history, bot_id))


@app.event("message")
def handle_dm(event, say, client):
    if event.get("bot_id"):
        return

    # Capture replies in the daily tasks channel as implicit feedback
    daily_channel = os.environ.get("DAILY_TASKS_CHANNEL", "")
    if daily_channel and event.get("channel") == daily_channel:
        text = event.get("text", "").strip()
        if not text:
            return
        # If it's an explicit command, route it normally
        text_lower = text.lower()
        if any(text_lower.startswith(p) for p in (
            "correct:", "correction:", "bug:", "feature:", "request:",
            "note:", "remember:",
        )):
            route_message(text, say, client, event["user"], event.get("channel", ""))
        else:
            # Store as implicit feedback (silent — no response)
            user_name = resolve_user_name(client, event["user"])
            store_feedback(client, user_name, text)
        return

    if event.get("channel_type") != "im":
        return
    text = event.get("text", "").strip()
    route_message(text, say, client, event["user"], event.get("channel", ""))


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
