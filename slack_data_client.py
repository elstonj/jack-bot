import os
import time


def get_recent_slack_messages(slack_client, user_map):
    """Fetch recent messages from monitored channels (last 24 hours).

    Returns:
        list[dict]: [{"channel": str, "user_name": str, "text": str}]
        If errors occur, returns a string with error details.
    """
    channel_ids = os.environ.get("SLACK_MONITORED_CHANNELS", "")
    if not channel_ids:
        return "[No SLACK_MONITORED_CHANNELS configured]"

    channels = [c.strip() for c in channel_ids.split(",") if c.strip()]
    oldest = str(time.time() - 86400)  # 24 hours ago

    # Build quick lookup from Slack user ID to name
    id_to_name = {}
    for user in user_map:
        if user.get("slack_user_id"):
            id_to_name[user["slack_user_id"]] = user["name"]

    all_messages = []
    errors = []
    for channel_id in channels:
        channel_name = channel_id
        try:
            info = slack_client.conversations_info(channel=channel_id)
            channel_name = f"#{info['channel']['name']}"
        except Exception as e:
            errors.append(f"conversations_info({channel_id}): {e}")

        try:
            result = slack_client.conversations_history(
                channel=channel_id, limit=50, oldest=oldest,
            )
            msg_count = 0
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
                msg_count += 1
        except Exception as e:
            errors.append(f"conversations_history({channel_id}): {e}")
            continue

        if len(all_messages) >= 100:
            break

    # If we got no messages but had errors, return error info
    if not all_messages and errors:
        return f"[Slack errors: {'; '.join(errors)}]"

    return all_messages
