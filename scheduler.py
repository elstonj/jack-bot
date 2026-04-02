import os
import threading
from apscheduler.schedulers.background import BackgroundScheduler
from slack_sdk import WebClient

from asana_client import get_daily_summary


def post_daily_tasks():
    """Post daily task summary to Slack."""
    channel = os.environ.get("DAILY_TASKS_CHANNEL", "#general")
    client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
    summary = get_daily_summary()
    client.chat_postMessage(channel=channel, text=summary)


def start_scheduler():
    """Start the background scheduler for cron jobs."""
    scheduler = BackgroundScheduler(timezone="America/Denver")
    # Post daily task summary at 8am Denver time on weekdays
    scheduler.add_job(post_daily_tasks, "cron", day_of_week="mon-fri", hour=8, minute=0)
    scheduler.start()
    return scheduler
