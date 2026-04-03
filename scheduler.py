import os
from apscheduler.schedulers.background import BackgroundScheduler
from slack_sdk import WebClient

from daily_research import run_daily_pipeline


def post_daily_tasks():
    """Run the daily research pipeline and post results to Slack."""
    channel = os.environ.get("DAILY_TASKS_CHANNEL", "#general")
    client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
    try:
        summary = run_daily_pipeline(client)
        client.chat_postMessage(channel=channel, text=summary)
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
