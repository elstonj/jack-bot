import os
import re
import threading
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from flask import Flask, request

from weather import format_weather, is_weather_intent, match_sites
from purchase_check import is_purchase_check_intent, handle_purchase_check
from personality import get_response
from research_cache import get_full_summary, get_user_summary, get_team_summary, get_per_user_sections, is_stale
from knowledge import store_correction, store_entry, store_feedback, store_bug, store_feature, list_items
from knowledge_qa import answer_question
from finances import get_project_finances
from channel_context import get_channel_context
from task_actions import (
    has_pending,
    is_task_update_intent,
    propose_task_updates,
    apply_task_updates,
)
from commercial_sales_reply import (
    has_pending as cs_has_pending,
    handle_thread_reply as cs_handle_thread_reply,
    handle_thread_followup as cs_handle_thread_followup,
    lookup_record_for_thread as cs_lookup_record_for_thread,
)
from commercial_sales_admin import (
    has_pending as cs_admin_has_pending,
    is_show_filtered_intent,
    parse_force_include_target,
    parse_create_task_target,
    handle_show_filtered,
    handle_force_include_propose,
    handle_force_include_followup,
    handle_create_task_propose,
    handle_create_task_followup,
)
from commercial_sales_inquiry import (
    has_pending as cs_inquiry_has_pending,
    handle_followup as cs_inquiry_handle_followup,
    is_inquiry_intent,
    handle_inquiry,
    is_update_intent as cs_is_update_intent,
    handle_update_propose,
)
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
            from scheduler import _bot_dm_footer
            channel = os.environ.get("DAILY_TASKS_CHANNEL", "#general")
            run_daily_pipeline(client)

            # Post team summary only. Per-user sections still go into the
            # cache so DM `tasks` works, but they don't get broadcast.
            team = get_team_summary()
            if team:
                client.chat_postMessage(channel=channel, text=team)
                _time.sleep(0.5)
                client.chat_postMessage(channel=channel, text=_bot_dm_footer(client))
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


_WORK_SIGNALS = (
    "milestone", "deliverable", "deadline", "due ", "next week", "this week",
    "last week", "next month", "yesterday", "today", "tomorrow", "kickoff",
    "kick-off", "kick off", "go/no-go", "go no go", "launch", "demo",
    "review", "status update",
)
_PLAN_VERBS = (
    # planning / ongoing
    "we have", "we need", "we're going", "we are going", "we'll",
    "planning to", "plan to", "plan is", "goal is", "goals for",
    "working on", "focus on", "focused on", "priorities ", "priority is",
    # past-tense status
    "wrapped up", "finished", "completed", "shipped", "delivered",
    "went well", "got done", "landed", "merged", "pushed", "deployed",
    "reviewed", "tested", "demo'd", "demoed",
    # coordination
    "let me know", "let us know", "flag me", "heads up",
)


def is_work_update(text):
    """Return True for informational work content that deserves a terse ack +
    store, not a personality monologue.

    Qualifies on:
      - ≥2 signals from the list below, OR
      - 1 signal AND length >= 100 chars (longer messages with any work
        indicator are almost always status-adjacent).

    Signals:
      - numbered list (1. / 2. / 3.) or bullet list (-, *)
      - @-mentions of team members
      - BST project code reference like [350-4] or 001-7
      - milestone/deliverable/deadline/kickoff keywords
      - plan verbs ("we have", "planning to", "goal is", ...)
    """
    lower = text.lower()
    signals = 0

    if re.search(r"(?m)^[\s>]*(?:\d+[.)]|[-*•])\s", text):
        signals += 1
    if re.search(r"<@[UW][A-Z0-9]+>", text):
        signals += 1
    if re.search(r"\[\d{3}[-_]\d+\]|\b\d{3}[-_]\d+\b", text):
        signals += 1
    if any(kw in lower for kw in _WORK_SIGNALS):
        signals += 1
    if any(kw in lower for kw in _PLAN_VERBS):
        signals += 1

    if signals >= 2:
        return True
    if signals >= 1 and len(text) >= 80:
        return True
    return False


_TERSE_ACKS = (
    "Noted.",
    "Got it — stored.",
    "Filed. Will surface it in context.",
    "Recorded.",
)


def _terse_ack() -> str:
    """Rotate through a few short acknowledgments — still dry, not a monologue."""
    import random
    return random.choice(_TERSE_ACKS)


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
    # Strip only the leading bot mention so embedded @user mentions are preserved
    # (otherwise "correction: @Joshua has time tracked" loses its subject).
    # Slack sometimes delivers the pipe form `<@U…|Display Name>` (e.g. from
    # mobile or search-derived contexts) — accept both `<@U…>` and `<@U…|…>`.
    message = re.sub(r"^\s*<@[A-Z0-9]+(?:\|[^>]*)?>\s*", "", text).strip()

    route_message(
        message, say, client, event["user"], event.get("channel", ""),
        event_ts=event.get("ts", ""),
    )


def route_message(message, say, client, user_id, channel_id, event_ts=""):
    """Unified routing for all natural language commands."""
    msg_lower = message.lower().strip()
    cs_channel = os.environ.get("COMMERCIAL_SALES_CHANNEL", "")

    # If a commercial-sales inquiry/update proposal is pending for this
    # user+channel, try to interpret the reply (disambiguation pick /
    # stub-details / yes-no-modify / cancel). On unrelated, fall through.
    if cs_inquiry_has_pending(user_id, channel_id):
        asker_name = resolve_user_name(client, user_id)
        resp = cs_inquiry_handle_followup(
            message, user_id, channel_id, client, asker_name
        )
        if resp:
            say(resp)
            return

    # If a task-update proposal is pending for this user+channel, try to
    # interpret the reply as a confirmation/modification/rejection. If it
    # isn't, fall through to normal routing.
    if has_pending(user_id, channel_id):
        handled, response = apply_task_updates(message, user_id, channel_id, slack_client=client)
        if handled:
            say(response)
            return

    if msg_lower in ("help", "commands", "what can you do"):
        say(
            "*Here's what I can do:*\n"
            "\n"
            ":clipboard: *tasks* — your prioritized task list (`tasks all` for the team)\n"
            ":partly_sunny: *weather* — flying conditions at local RC sites\n"
            ":dollar: *finances* — project financial summary (in a project channel)\n"
            ":money_with_wings: *can we buy $X of Y?* — budget check + approval routing\n"
            ":bug: *bug: [description]* — report a bug\n"
            ":sparkles: *feature: [description]* — request a feature\n"
            ":clipboard: *bugs* / *features* — list open items\n"
            ":arrows_counterclockwise: *correct: [feedback]* — fix task priorities\n"
            ":memo: *note: [info]* — teach me something about projects\n"
            ":question: Just ask a question naturally — I'll search the knowledge base\n"
            "\n"
            "_Or just talk to me. I'll be grumpy about it._"
        )
    elif is_weather_intent(message):
        matched = match_sites(message)
        say(format_weather(sites=matched if matched else None))
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
    elif is_purchase_check_intent(message):
        channel_ctx = get_channel_context(client, channel_id)
        say(handle_purchase_check(message, channel_ctx))
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
    elif is_task_update_intent(message):
        channel_ctx = get_channel_context(client, channel_id)
        if channel_ctx and channel_ctx.get("project_gid"):
            say(propose_task_updates(
                strip_qa_prefix(message), channel_ctx, user_id, channel_id
            ))
        else:
            # No project resolved — fall back to Q&A so the user gets some
            # answer instead of silence.
            say(answer_question(
                strip_qa_prefix(message),
                slack_client=client,
                channel_id=channel_id,
                channel_context=channel_ctx,
                user_id=user_id,
            ))
    elif cs_channel and channel_id == cs_channel and cs_is_update_intent(message):
        # #commercial-sales: top-level update requests ("add Dan as owner to
        # X", "mark CU IRISS complete", "set ship_to for SOCOM to ..."). These
        # used to route through is_work_update and get a fake "Got it —
        # stored." ack while losing the actual write — see Beck's 2026-05-18
        # "add Dan as owner..." which never persisted to either Build JSON.
        asker_name = resolve_user_name(client, user_id)
        resp = handle_update_propose(
            message, user_id, channel_id, client, asker_name
        )
        if resp:
            say(resp)
        # else: fall through silently — Haiku found nothing actionable
    elif cs_channel and channel_id == cs_channel and is_inquiry_intent(message):
        # #commercial-sales: shipping / parts / contact / payment questions
        # resolve to a specific Build/SupportCase and either answer, ping the
        # owner for missing info, or stub a new record. Avoids the old
        # is_work_update silent-INSIGHT trap that swallowed Josh's
        # "do the two s0 display units…" question on 2026-05-18.
        asker_name = resolve_user_name(client, user_id)
        resp = handle_inquiry(message, user_id, channel_id, client, asker_name)
        if resp:
            say(resp)
        else:
            # Defensive fallthrough — handle_inquiry always returns a string
            # today, but if it ever returns None we want to answer something
            # rather than ack with "Noted."
            say(answer_question(
                strip_qa_prefix(message),
                slack_client=client,
                channel_id=channel_id,
                channel_context=get_channel_context(client, channel_id),
                user_id=user_id,
            ))
    elif is_question(message):
        question = strip_qa_prefix(message)
        channel_ctx = get_channel_context(client, channel_id)
        say(answer_question(
            question,
            slack_client=client,
            channel_id=channel_id,
            channel_context=channel_ctx,
            user_id=user_id,
        ))
    elif is_work_update(message):
        # Legitimate work content (plans, milestones, status updates) — take
        # the terse-ack-and-store path instead of subjecting the user to a
        # sysadmin monologue. Personality is reserved for genuine off-topic
        # chatter below.
        #
        # When the work update landed in #operations, store as FEEDBACK with
        # a (ts=...) tag so:
        #   1. STATUS_OVERRIDE_PROMPT picks it up and pins it at the top of
        #      the next morning's synthesis prompt as a hard override (the
        #      synthesis prompt's "ABSOLUTE" rule applies to CORRECTION /
        #      FEEDBACK only — INSIGHT lacks that weight).
        #   2. Tomorrow's _sync_operations_feedback dedups against the
        #      embedded ts and doesn't double-mirror the message.
        # Outside #operations (DMs, project channels), keep storing as
        # INSIGHT — the channel-context isn't team-wide feedback there.
        user_name = resolve_user_name(client, user_id)
        ops_channel = os.environ.get("DAILY_TASKS_CHANNEL", "")
        if channel_id and ops_channel and channel_id == ops_channel:
            ts_part = f" (ts={event_ts})" if event_ts else ""
            store_entry(client, "FEEDBACK", f"From {user_name}{ts_part}: {message}")
        else:
            store_entry(client, "INSIGHT", f"From {user_name}: {message}")
        say(_terse_ack())
    else:
        user_name = resolve_user_name(client, user_id)
        bot_id = get_bot_user_id(client)
        channel_ctx = get_channel_context(client, channel_id)
        history = channel_ctx["recent_messages"] if channel_ctx else fetch_history(client, channel_id)
        say(get_response(message, user_name, history, bot_id, channel_context=channel_ctx))


@app.event("message")
def handle_dm(event, say, client):
    if event.get("bot_id"):
        return

    cs_channel = os.environ.get("COMMERCIAL_SALES_CHANNEL", "")

    # Commercial-sales top-level admin commands: "show filtered" + "track this: <x>".
    # Threaded replies (the reply-to-update flow) are handled separately below.
    if (
        cs_channel
        and event.get("channel") == cs_channel
        and not event.get("thread_ts")
    ):
        text = (event.get("text") or "").strip()
        user_id = event.get("user", "")
        if text and user_id:
            try:
                resp = None
                # Pending? Route to whichever follow-up handler matches.
                # commercial_sales_admin._get_pending stores kind so both
                # follow-up funcs return None on a mismatch — we try both.
                if cs_admin_has_pending(user_id, cs_channel):
                    resp = (
                        handle_force_include_followup(text, user_id, cs_channel)
                        or handle_create_task_followup(text, user_id, cs_channel)
                    )
                elif cs_inquiry_has_pending(user_id, cs_channel):
                    asker_name = resolve_user_name(client, user_id)
                    resp = cs_inquiry_handle_followup(
                        text, user_id, cs_channel, client, asker_name
                    )
                elif is_show_filtered_intent(text):
                    resp = handle_show_filtered()
                else:
                    # Try the admin command intents first…
                    target = parse_force_include_target(text)
                    if target:
                        resp = handle_force_include_propose(target, user_id, cs_channel)
                    else:
                        target = parse_create_task_target(text)
                        if target:
                            resp = handle_create_task_propose(target, user_id, cs_channel)
                    # …then update intents ("add Dan as owner to X",
                    # "mark X complete"). is_update_intent rejects question
                    # marks, so it won't swallow inquiry-shaped messages.
                    if not resp and cs_is_update_intent(text):
                        asker_name = resolve_user_name(client, user_id)
                        resp = handle_update_propose(
                            text, user_id, cs_channel, client, asker_name
                        )
                    # …then the read-only inquiry handler for shipping/parts/
                    # POC/etc. questions. Without this, top-level messages
                    # like "what's the ship-to for SOCOM?" used to fall
                    # through silently in #commercial-sales (no @-mention
                    # required).
                    if not resp and is_inquiry_intent(text):
                        asker_name = resolve_user_name(client, user_id)
                        # Only emit the "I don't have a record…" stub prompt when
                        # the bot was actually addressed (@-mentioned). Undirected
                        # channel chatter that merely trips an inquiry keyword
                        # stays silent if it can't be answered — the canned
                        # deflection on every passing message is what got Jack
                        # mocked. A confident match still answers regardless.
                        bot_uid = get_bot_user_id(client)
                        addressed = bool(bot_uid) and (bot_uid in text)
                        resp = handle_inquiry(
                            text, user_id, cs_channel, client, asker_name,
                            respond_when_unresolved=addressed,
                        )
                if resp:
                    client.chat_postMessage(channel=cs_channel, text=resp)
                    return
            except Exception as e:
                store_entry(client, "ERROR", f"commercial-sales admin handler: {e}")
        # Fall through if no admin command matched — top-level chatter is silent.

    # Commercial-sales thread replies: route to the reply-to-update flow.
    # Fires only for threaded replies under one of Jack's per-build cards;
    # top-level messages in #commercial-sales fall through to other routing.
    if (
        cs_channel
        and event.get("channel") == cs_channel
        and event.get("thread_ts")
        and event.get("thread_ts") != event.get("ts")  # don't trigger on the parent itself
    ):
        text = (event.get("text") or "").strip()
        if not text:
            return
        thread_ts = event["thread_ts"]
        user_id = event.get("user", "")
        try:
            if cs_has_pending(thread_ts, user_id):
                resp = cs_handle_thread_followup(client, event)
            else:
                # Only respond when the thread is actually under one of our
                # cards OR the umbrella daily thread matches the reply to a
                # specific card (silent on unrelated threads). Lookup is
                # short-circuited by lookup_record_for_thread returning None.
                if not cs_lookup_record_for_thread(client, cs_channel, thread_ts, reply_text=text):
                    return
                resp = cs_handle_thread_reply(client, event)
            if resp:
                client.chat_postMessage(
                    channel=cs_channel,
                    thread_ts=thread_ts,
                    text=resp,
                )
        except Exception as e:
            store_entry(client, "ERROR", f"commercial-sales reply handler: {e}")
        return

    # Capture replies in the daily tasks channel as implicit feedback
    daily_channel = os.environ.get("DAILY_TASKS_CHANNEL", "")
    if daily_channel and event.get("channel") == daily_channel:
        text = event.get("text", "").strip()
        if not text:
            return
        # Explicit commands still route, but questions/chatter stay silent —
        # users must @mention the bot to get a response in #operations.
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
