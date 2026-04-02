import os
import time


def get_recent_slack_messages(slack_client, user_map):
    """Fetch recent messages from monitored channels (last 24 hours).

    Args:
        slack_client: Slack WebClient instance
        user_map: list of unified user dicts (from user_map module)

    Returns:
        list[dict]: [{"channel": str, "user_name": str, "text": str}]
    """
    channel_ids = os.environ.get("SLACK_MONITORED_CHANNELS", "")
    if not channel_ids:
        return []

    channels = [c.strip() for c in channel_ids.split(",") if c.strip()]
    oldest = str(time.time() - 86400)  # 24 hours ago

    # Build quick lookup from Slack user ID to name
    id_to_name = {}
    for user in user_map:
        if user.get("slack_user_id"):
            id_to_name[user["slack_user_id"]] = user["name"]

    all_messages = []
    for channel_id in channels:
        try:
            # Get channel name
            info = slack_client.conversations_info(channel=channel_id)
            channel_name = f"#{info['channel']['name']}"
        except Exception:
            channel_name = channel_id

        try:
            result = slack_client.conversations_history(
                channel=channel_id, limit=50, oldest=oldest,
            )
            for msg in result.get("messages", []):
                if msg.get("bot_id") or msg.get("subtype"):
                    continue
                user_id = msg.get("user", "")
                user_name = id_to_name.get(user_id, "unknown")
                all_messages.append({
                    "channel": channel_name,
                    "user_name": user_name,
                    "text": msg.get("text", ""),
                })
        except Exception:
            continue

        if len(all_messages) >= 100:
            break

    return all_messages
