import os
import time
from apscheduler.schedulers.background import BackgroundScheduler
from slack_sdk import WebClient

from daily_research import run_daily_pipeline
from research_cache import get_team_summary, get_per_user_sections


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


def start_scheduler():
    """Start the background scheduler for cron jobs."""
    scheduler = BackgroundScheduler(timezone="America/Denver")
    scheduler.add_job(post_daily_tasks, "cron", day_of_week="mon-fri", hour=8, minute=0)
    scheduler.start()
    return scheduler
