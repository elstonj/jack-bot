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
    channels_ok = 0
    channels_empty = 0

    for channel_id in channels:
        channel_name = channel_id
        try:
            info = slack_client.conversations_info(channel=channel_id)
            channel_name = f"#{info['channel']['name']}"
        except Exception:
            # Non-fatal — we can still read history without the name
            pass

        try:
            result = slack_client.conversations_history(
                channel=channel_id, limit=50, oldest=oldest,
            )
            raw_msgs = result.get("messages", [])
            if not raw_msgs:
                channels_empty += 1
            else:
                channels_ok += 1
            for msg in raw_msgs:
                if msg.get("bot_id") or msg.get("subtype"):
                    continue
                user_id = msg.get("user", "")
                user_name = id_to_name.get(user_id, "unknown")
                all_messages.append({
                    "channel": channel_name,
                    "user_name": user_name,
                    "text": msg.get("text", ""),
                })
        except Exception as e:
            errors.append(f"history({channel_id}/{channel_name}): {e}")
            continue

        if len(all_messages) >= 100:
            break

    # Always return diagnostic info if no messages
    if not all_messages:
        parts = [f"[Slack: {len(channels)} channels configured, {channels_ok} readable, {channels_empty} empty in last 24h]"]
        if errors:
            parts.append(f"[Errors: {'; '.join(errors)}]")
        return " ".join(parts)

    return all_messages
