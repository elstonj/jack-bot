import html
import os
import time
from apscheduler.schedulers.background import BackgroundScheduler
from slack_sdk import WebClient

import anthropic

from daily_research import run_daily_pipeline
from research_cache import get_team_summary, get_per_user_sections  # noqa: F401  per_user still used by DM path via cache
from snow_day import check_and_post as check_snow_day
from snow_day import check_and_post_eod as check_snow_day_eod
from eldora import check_and_post as check_eldora
from marketing_check import check_and_post as check_marketing
from weather import format_weather
from google_client import get_latest_email_by_subject


PURCHASING_REFORMAT_PROMPT = """\
You are reformatting a daily purchasing summary email for Slack. The input is the body of
a Gemini-generated report. It may arrive in any of these shapes — handle them all:
  (a) markdown with pipe-delimited tables (| Vendor | Order ID | ... |)
  (b) one long run-on line where field labels are concatenated with no separators
      ("Vendor: XOrder Date: YItems Ordered: Z...") — split on the labels
  (c) loose prose with one entry per paragraph

Rules:
- Decode any HTML entities you see (&#39; → ', &quot; → ", &amp; → &, etc.)
- Drop preamble like "Here is the summary..." / "Below is a summary..." and any
  date-range header — the parent message already has a title
- Use *bold* for section headers and vendor names (Slack mrkdwn, not markdown headings)
- Group entries under section headers like *New / Confirmed Orders*,
  *Shipped / In Transit*, *Delivered*. If the source has no sections, infer them
  from each entry's status. Skip empty sections.
- Format each order as exactly:
    *<Vendor>* — Order `<id>`
    • Items: <short summary, ≤ 120 chars; collapse long part lists>
    • Total: $X    (omit this line if no amount given)
    • Status: <tracking #, ETA, backorder note, etc.>
- Drop fields that say "Not provided", "Not specified", "N/A", "Unknown", or are empty
- Preserve concrete data: dollar amounts, tracking numbers, expected ship/delivery dates
- Don't add commentary, recommendations, or invent details
- One blank line between entries; no horizontal rules; no markdown headings (#, ##)
- Output the formatted body only — no preamble, no closing remarks, no code fences"""


def _reformat_purchasing_for_slack(raw_body: str) -> str:
    """Convert the purchasing email body into Slack-friendly mrkdwn.

    Falls back to the (entity-decoded) raw body if Claude is unavailable.
    """
    decoded = html.unescape(raw_body)
    try:
        client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
        msg = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=3000,
            system=PURCHASING_REFORMAT_PROMPT,
            messages=[{"role": "user", "content": decoded[:15000]}],
        )
        return msg.content[0].text.strip()
    except Exception:
        return decoded


def _bot_dm_footer(client) -> str:
    """One-line nudge telling the team how to get their personal top 3 via DM.

    Per-user sections are still generated and cached every run — they're just
    no longer broadcast to #operations. Anyone can pull their own list (and
    leave feedback) by DMing the bot.
    """
    try:
        bot_user_id = client.auth_test()["user_id"]
        mention = f"<@{bot_user_id}>"
    except Exception:
        mention = "@Jack Bot"
    return (
        f":speech_balloon: _DM {mention} `tasks` for your personal top 3 today — "
        f"or just chat to give feedback / corrections._"
    )


def post_daily_tasks():
    """Run the daily research pipeline and post the team summary to #operations.

    Per-user sections are still generated (DM `tasks` command pulls them from
    the cache) but are no longer broadcast — the channel post is now strictly
    a team-level overview.
    """
    channel = os.environ.get("DAILY_TASKS_CHANNEL", "#general")
    client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
    try:
        run_daily_pipeline(client)

        team = get_team_summary()
        if team:
            client.chat_postMessage(channel=channel, text=team)
            time.sleep(0.5)
            client.chat_postMessage(channel=channel, text=_bot_dm_footer(client))

    except Exception as e:
        from knowledge import store_entry
        try:
            store_entry(client, "ERROR", f"Scheduled daily pipeline failed: {e}")
        except Exception:
            pass


def tick_snow_day():
    """Hourly check for active snowfall at BST HQ; post a beer call-out if so."""
    client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
    try:
        check_snow_day(client)
    except Exception:
        from knowledge import store_entry
        try:
            store_entry(client, "ERROR", "snow_day check failed")
        except Exception:
            pass


def tick_snow_day_eod():
    """EOD shutdown notice if snow fell any time today."""
    client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
    try:
        check_snow_day_eod(client)
    except Exception:
        from knowledge import store_entry
        try:
            store_entry(client, "ERROR", "snow_day EOD check failed")
        except Exception:
            pass


def tick_eldora_report():
    """6:30 AM MT weekday check for overnight snow at Eldora."""
    client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
    try:
        check_eldora(client)
    except Exception:
        from knowledge import store_entry
        try:
            store_entry(client, "ERROR", "eldora report check failed")
        except Exception:
            pass


def tick_marketing_check():
    """Morning scan for marketing-worthy signals tagging Paige; post to #marketing if any."""
    client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
    try:
        check_marketing(client)
    except Exception as e:
        from knowledge import store_entry
        try:
            store_entry(client, "ERROR", f"marketing check failed: {e}")
        except Exception:
            pass


def post_purchasing_summary():
    """Re-post Jack's daily purchasing summary email to #operations."""
    channel = os.environ.get("DAILY_TASKS_CHANNEL", "#general")
    sender = os.environ.get("PURCHASING_SUMMARY_SENDER", "elstonj@blackswifttech.com")
    client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
    try:
        body = get_latest_email_by_subject(
            sender, "Daily Purchasing Summary", sender=sender, max_age_hours=20
        )
        if not body:
            return
        formatted = _reformat_purchasing_for_slack(body.strip())
        text = f":package: *Daily Purchasing Summary*\n{formatted}"
        # Slack hard-limits a single message at 40k chars; trim with a marker.
        if len(text) > 39000:
            text = text[:39000] + "\n…(truncated)"
        client.chat_postMessage(channel=channel, text=text)
    except Exception as e:
        from knowledge import store_entry
        try:
            store_entry(client, "ERROR", f"purchasing summary post failed: {e}")
        except Exception:
            pass


def post_flight_weather():
    """Daily 8 AM MT weather report for the flight-testing channel."""
    channel = os.environ.get("FLIGHT_TESTING_CHANNEL", "#flight-testing")
    client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
    try:
        client.chat_postMessage(channel=channel, text=format_weather())
    except Exception as e:
        from knowledge import store_entry
        try:
            store_entry(client, "ERROR", f"flight-testing weather post failed: {e}")
        except Exception:
            pass


def start_scheduler():
    """Start the background scheduler for cron jobs."""
    scheduler = BackgroundScheduler(timezone="America/Denver")
    # Grace window so a Railway redeploy that straddles a scheduled fire time
    # still runs the job once it comes up, instead of silently skipping it.
    scheduler.add_job(
        post_daily_tasks,
        "cron",
        day_of_week="mon-fri",
        hour=8,
        minute=0,
        misfire_grace_time=1800,  # 30 min: briefing is still useful a bit late
    )
    # Snow-day check: top of every hour during typical working hours, Mon-Fri.
    # No point in telling the team to go get a beer at 3am.
    scheduler.add_job(
        tick_snow_day,
        "cron",
        day_of_week="mon-fri",
        hour="9-17",
        minute=0,
        misfire_grace_time=900,  # 15 min: still relevant within the hour
    )
    # EOD shutdown notice: 3:30 PM MT Mon-Fri if snow fell today.
    scheduler.add_job(
        tick_snow_day_eod,
        "cron",
        day_of_week="mon-fri",
        hour=15,
        minute=30,
        misfire_grace_time=1800,  # 30 min
    )
    # Eldora overnight snow-report bulletin: 6:30 AM MT Mon-Fri.
    scheduler.add_job(
        tick_eldora_report,
        "cron",
        day_of_week="mon-fri",
        hour=6,
        minute=30,
        misfire_grace_time=1800,  # 30 min: still useful a bit late
    )
    # Daily 8 AM MT weather report posted to #flight-testing.
    scheduler.add_job(
        post_flight_weather,
        "cron",
        hour=8,
        minute=0,
        misfire_grace_time=1800,  # 30 min: forecast is still useful a bit late
    )
    # Daily purchasing summary re-post to #operations. The source email
    # arrives ~07:56 MDT, so fire at 8:05 to give it slack to land.
    scheduler.add_job(
        post_purchasing_summary,
        "cron",
        day_of_week="mon-fri",
        hour=8,
        minute=5,
        misfire_grace_time=3600,  # 1 hr: still useful later in the morning
    )
    # Marketing assist scan to #marketing. Fires after the 8:00 daily
    # pipeline so it sees fresh knowledge entries from this morning's run,
    # but stays cheap by re-using the same data sources.
    scheduler.add_job(
        tick_marketing_check,
        "cron",
        day_of_week="mon-fri",
        hour=8,
        minute=15,
        misfire_grace_time=3600,  # 1 hr: still useful later in the morning
    )
    scheduler.start()
    return scheduler
