import os
import time

import anthropic


def get_feedback_channel():
    return os.environ.get("FEEDBACK_CHANNEL", "")


def store_feedback(slack_client, user_name, feedback_text):
    """Store user feedback in the feedback channel."""
    channel = get_feedback_channel()
    if not channel:
        return
    slack_client.chat_postMessage(
        channel=channel,
        text=f"*[Correction] {user_name}:*\n{feedback_text}",
    )


def store_insight(slack_client, insight_text):
    """Store a strategic insight (future contracts, deliverables, etc.)."""
    channel = get_feedback_channel()
    if not channel:
        return
    slack_client.chat_postMessage(
        channel=channel,
        text=f"*[Insight]*\n{insight_text}",
    )


def store_daily_summary(slack_client, summary):
    """Store the daily summary in the feedback channel for next-day comparison."""
    channel = get_feedback_channel()
    if not channel:
        return
    slack_client.chat_postMessage(
        channel=channel,
        text=f"*[Daily Summary]*\n{summary}",
    )


def get_recent_feedback(slack_client, days=7):
    """Pull recent feedback, insights, and previous summary.

    Returns:
        dict with keys: corrections, insights, previous_summary
    """
    channel = get_feedback_channel()
    if not channel:
        return {"corrections": [], "insights": [], "previous_summary": None}

    oldest = str(time.time() - (days * 86400))
    try:
        result = slack_client.conversations_history(
            channel=channel, limit=200, oldest=oldest,
        )
    except Exception:
        return {"corrections": [], "insights": [], "previous_summary": None}

    messages = result.get("messages", [])
    messages.reverse()

    corrections = []
    insights = []
    previous_summary = None

    for msg in messages:
        text = msg.get("text", "")
        if text.startswith("*[Daily Summary]*"):
            previous_summary = text.replace("*[Daily Summary]*\n", "", 1)
        elif text.startswith("*[Correction]"):
            corrections.append(text)
        elif text.startswith("*[Insight]*"):
            insights.append(text)

    return {
        "corrections": corrections,
        "insights": insights,
        "previous_summary": previous_summary,
    }


def get_all_insights(slack_client):
    """Pull ALL insights (no time limit) for long-term memory."""
    channel = get_feedback_channel()
    if not channel:
        return []

    insights = []
    cursor = None
    while True:
        try:
            kwargs = {"channel": channel, "limit": 200}
            if cursor:
                kwargs["cursor"] = cursor
            result = slack_client.conversations_history(**kwargs)
            for msg in result.get("messages", []):
                text = msg.get("text", "")
                if text.startswith("*[Insight]*"):
                    insights.append(text.replace("*[Insight]*\n", "", 1))
            cursor = result.get("response_metadata", {}).get("next_cursor")
            if not cursor:
                break
        except Exception:
            break

    insights.reverse()
    return insights


def extract_insights_from_data(context_text):
    """Use Claude to extract strategic insights from the daily data.

    Looks for things like: future contracts, upcoming deliverables,
    budget mentions, staffing changes, client relationship signals.
    """
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=500,
        system=(
            "You extract strategic business insights from daily work data. "
            "Look for: future contracts or proposals, upcoming deliverables with dates, "
            "budget/dollar amounts mentioned, client relationship signals (positive or negative), "
            "staffing or capacity concerns, and risk factors. "
            "Only output insights that are forward-looking and actionable. "
            "If nothing notable, respond with exactly: NONE"
        ),
        messages=[{"role": "user", "content": context_text}],
    )
    result = message.content[0].text.strip()
    if result == "NONE":
        return None
    return result
