import os
import time
from apscheduler.schedulers.background import BackgroundScheduler
from slack_sdk import WebClient

from daily_research import run_daily_pipeline
from research_cache import get_team_summary, get_per_user_sections
from snow_day import check_and_post as check_snow_day
from snow_day import check_and_post_eod as check_snow_day_eod
from eldora import check_and_post as check_eldora
from weather import format_weather
from google_client import get_latest_email_by_subject


def post_daily_tasks():
    """Run the daily research pipeline and post results as ordered messages."""
    channel = os.environ.get("DAILY_TASKS_CHANNEL", "#general")
    client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
    try:
        run_daily_pipeline(client)

        # Post team summary first
        team = get_team_summary()
        if team:
            client.chat_postMessage(channel=channel, text=team)
            time.sleep(0.5)  # Small delay to preserve ordering

        # Post each person's section as a separate message
        per_user = get_per_user_sections()
        for section in per_user.values():
            client.chat_postMessage(channel=channel, text=section)
            time.sleep(0.3)

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
        text = f":package: *Daily Purchasing Summary*\n{body.strip()}"
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
    scheduler.start()
    return scheduler
