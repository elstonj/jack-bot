"""Slack deep scanner — fetches full channel history, distills into knowledge files.

Produces:
  knowledge/slack/{channel_name}.md  — per-channel knowledge

Modes:
  full        — all messages (entire history)
  1yr         — messages from the last 365 days
  incremental — messages since last scan
"""

import os
import re
import time
from datetime import datetime, timedelta

from slack_sdk import WebClient

from .base import (
    KNOWLEDGE_DIR,
    distill_to_markdown,
    get_last_scan,
    update_scan_timestamp,
    write_knowledge_file,
    get_claude_client,
    DISTILL_MODEL,
)

SLACK_KNOWLEDGE_DIR = KNOWLEDGE_DIR / "slack"

# Rate limit: Slack allows ~1 req/sec for most endpoints. Be conservative.
REQUEST_DELAY = 1.2  # seconds between paginated calls

# Messages per distillation batch (larger = fewer API calls, cheaper)
BATCH_SIZE = 500

# System message subtypes to skip
SKIP_SUBTYPES = {
    "channel_join",
    "channel_leave",
    "channel_topic",
    "channel_purpose",
    "channel_name",
    "channel_archive",
    "channel_unarchive",
    "group_join",
    "group_leave",
    "group_topic",
    "group_purpose",
    "group_name",
    "group_archive",
    "group_unarchive",
    "bot_message",
    "bot_add",
    "bot_remove",
    "pinned_item",
    "unpinned_item",
}


def _get_slack_client():
    """Create a Slack WebClient from env var."""
    return WebClient(token=os.environ["SLACK_BOT_TOKEN"])


def _get_monitored_channels():
    """Return list of channel IDs from env var."""
    channel_ids = os.environ.get("SLACK_MONITORED_CHANNELS", "")
    return [c.strip() for c in channel_ids.split(",") if c.strip()]


def _get_channel_name(client, channel_id):
    """Fetch channel name via conversations_info."""
    try:
        info = client.conversations_info(channel=channel_id)
        return info["channel"]["name"]
    except Exception as e:
        print(f"  [WARN] Could not get name for channel {channel_id}: {e}")
        return channel_id


def _fetch_channel_history(client, channel_id, oldest="0", progress_callback=None):
    """Fetch full message history for a channel using cursor-based pagination.

    Args:
        client: Slack WebClient
        channel_id: Channel to fetch
        oldest: Unix timestamp string — fetch messages newer than this
        progress_callback: optional fn(msg_count) for progress updates

    Returns:
        list of message dicts, oldest first
    """
    all_messages = []
    cursor = None
    page = 0

    while True:
        kwargs = {
            "channel": channel_id,
            "limit": 200,
            "oldest": oldest,
        }
        if cursor:
            kwargs["cursor"] = cursor

        try:
            result = client.conversations_history(**kwargs)
        except Exception as e:
            print(f"  [ERROR] conversations_history failed: {e}")
            break

        messages = result.get("messages", [])
        all_messages.extend(messages)
        page += 1

        if progress_callback:
            progress_callback(len(all_messages))

        # Check for more pages
        metadata = result.get("response_metadata", {})
        next_cursor = metadata.get("next_cursor", "")
        if not next_cursor:
            break
        cursor = next_cursor
        time.sleep(REQUEST_DELAY)

    # Slack returns newest first; reverse to chronological order
    all_messages.reverse()
    return all_messages


def _resolve_user(client, user_id, user_cache):
    """Resolve a Slack user ID to a display name, with caching.

    Args:
        client: Slack WebClient
        user_id: Slack user ID (e.g. U01ABC123)
        user_cache: dict mapping user_id -> name (mutated in place)

    Returns:
        Display name string
    """
    if user_id in user_cache:
        return user_cache[user_id]

    try:
        info = client.users_info(user=user_id)
        user = info["user"]
        # Prefer real_name, fall back to display_name, then name
        name = (
            user.get("real_name")
            or user.get("profile", {}).get("display_name")
            or user.get("name")
            or user_id
        )
        user_cache[user_id] = name
        time.sleep(REQUEST_DELAY)
        return name
    except Exception:
        user_cache[user_id] = user_id
        return user_id


def _filter_messages(messages):
    """Filter out bot messages and system messages."""
    filtered = []
    for msg in messages:
        # Skip bot messages
        if msg.get("bot_id"):
            continue
        # Skip system subtypes
        subtype = msg.get("subtype")
        if subtype and subtype in SKIP_SUBTYPES:
            continue
        filtered.append(msg)
    return filtered


def _format_message(msg, user_cache, client):
    """Format a single message as a text line for distillation."""
    user_id = msg.get("user", "")
    user_name = _resolve_user(client, user_id, user_cache) if user_id else "unknown"

    ts = msg.get("ts", "0")
    try:
        dt = datetime.fromtimestamp(float(ts))
        date_str = dt.strftime("%Y-%m-%d %H:%M")
    except (ValueError, OSError):
        date_str = "unknown-date"

    text = msg.get("text", "").strip()
    # Truncate extremely long messages
    if len(text) > 1000:
        text = text[:1000] + "..."

    return f"[{date_str}] {user_name}: {text}"


def _safe_filename(name):
    """Convert a channel name to a safe filename."""
    name = re.sub(r"[^\w\s-]", "", name)
    name = re.sub(r"\s+", "_", name.strip())
    return name[:80].lower()


BATCH_DISTILL_PROMPT = """\
You are extracting key information from a batch of Slack messages from a workspace channel.

Summarize the following into structured notes. Focus on:
- Key decisions made
- Project discussions and status updates
- Client/external references (company names, contacts)
- Action items and commitments people made
- Important links or resources shared
- Technical discussions and conclusions

Be concise but preserve specific names, dates, and details. \
Skip small talk, greetings, and trivial messages. \
If this batch has no substantive content, say "No significant content in this batch." \
Output plain text notes, not markdown."""


FINAL_DISTILL_PROMPT = """\
You are creating a structured knowledge file from Slack channel history for Black Swift Technologies (BST).

This file will be used by an AI assistant to understand what has been discussed in this channel, \
track decisions, and answer questions. It should be comprehensive but well-organized.

Output a markdown file with these sections:

# #{channel_name}

## Overview
- What this channel is primarily used for (infer from content)
- Key participants
- Activity level and time range covered

## Key Decisions
Important decisions that were made, with approximate dates and who was involved.

## Projects & Initiatives
Ongoing projects or initiatives discussed, with current status if apparent.

## Action Items & Commitments
Things people committed to doing, with names and dates where available.

## Client & External References
Any mentions of clients, partners, external companies, or contacts.

## Recurring Topics & Themes
Patterns in what gets discussed — regular standups, repeated concerns, etc.

## Important Resources
Links, documents, tools, or references that were shared.

## Recent Activity
Notable recent discussions and their outcomes.

Be factual and specific. Include names, dates, and concrete details. \
Skip empty sections. Merge and deduplicate information from the batch summaries."""


def scan_channel(client, channel_id, mode="full", user_cache=None, progress_callback=None):
    """Scan a single Slack channel and distill into a knowledge file.

    Args:
        client: Slack WebClient
        channel_id: Slack channel ID
        mode: 'full', '1yr', or 'incremental'
        user_cache: shared dict for user ID->name cache (mutated in place)
        progress_callback: optional fn(status_str)

    Returns:
        (channel_name, msg_count, output_path) or None on skip
    """
    if user_cache is None:
        user_cache = {}

    # Get channel name
    channel_name = _get_channel_name(client, channel_id)
    time.sleep(REQUEST_DELAY)

    # Determine oldest timestamp based on mode
    if mode == "full":
        oldest = "0"
    elif mode == "1yr":
        oldest = str(int((datetime.now() - timedelta(days=365)).timestamp()))
    elif mode == "incremental":
        last = get_last_scan("slack")
        if last:
            oldest = str(int(last.timestamp()))
        else:
            print(f"  No previous scan found — falling back to full for #{channel_name}")
            oldest = "0"
    else:
        oldest = "0"

    # Fetch messages
    if progress_callback:
        progress_callback(f"Fetching #{channel_name} history...")

    def fetch_progress(count):
        if progress_callback:
            progress_callback(f"Fetching #{channel_name}: {count} messages...")

    raw_messages = _fetch_channel_history(client, channel_id, oldest=oldest, progress_callback=fetch_progress)

    # Filter out bots and system messages
    messages = _filter_messages(raw_messages)

    if not messages:
        print(f"  [SKIP] #{channel_name}: no messages after filtering")
        return None

    print(f"  #{channel_name}: {len(messages)} messages ({len(raw_messages)} raw)")

    # Format messages in batches and distill
    if progress_callback:
        progress_callback(f"Resolving users for #{channel_name}...")

    # Process in batches
    batches = []
    for i in range(0, len(messages), BATCH_SIZE):
        batch = messages[i : i + BATCH_SIZE]
        batches.append(batch)

    batch_summaries = []
    for batch_idx, batch in enumerate(batches):
        if progress_callback:
            progress_callback(
                f"Distilling #{channel_name} batch {batch_idx + 1}/{len(batches)}..."
            )

        # Format this batch of messages
        formatted_lines = []
        for msg in batch:
            line = _format_message(msg, user_cache, client)
            formatted_lines.append(line)

        batch_text = f"Channel: #{channel_name}\nBatch {batch_idx + 1} of {len(batches)}\n\n"
        batch_text += "\n".join(formatted_lines)

        # For a single small batch, skip the intermediate distillation
        if len(batches) == 1 and len(messages) <= BATCH_SIZE:
            # Go straight to final distillation
            final_prompt = FINAL_DISTILL_PROMPT.replace("{channel_name}", channel_name)
            filename = _safe_filename(channel_name) + ".md"
            output_path = SLACK_KNOWLEDGE_DIR / filename

            print(f"  Distilling #{channel_name} ({len(messages)} messages, single pass)...")
            distill_to_markdown(batch_text, final_prompt, output_path, max_tokens=2000)
            return channel_name, len(messages), output_path

        # Distill this batch via Claude
        claude_client = get_claude_client()
        summary = None
        for attempt in range(5):
            try:
                response = claude_client.messages.create(
                    model=DISTILL_MODEL,
                    max_tokens=1500,
                    system=BATCH_DISTILL_PROMPT,
                    messages=[{"role": "user", "content": batch_text}],
                )
                summary = response.content[0].text
                break
            except Exception as e:
                if "rate_limit" in str(e).lower():
                    wait = 30 * (attempt + 1)
                    print(f"    Rate limited, waiting {wait}s (attempt {attempt + 1}/5)...")
                    time.sleep(wait)
                else:
                    print(f"    [ERROR] Batch distill failed: {e}")
                    break

        if summary:
            batch_summaries.append(f"=== Batch {batch_idx + 1} ===\n{summary}")

        # Pace Claude API calls
        time.sleep(1)

    if not batch_summaries:
        print(f"  [SKIP] #{channel_name}: all batch distillations failed")
        return None

    # Final distillation pass — merge batch summaries into one cohesive file
    if progress_callback:
        progress_callback(f"Final distillation for #{channel_name}...")

    combined_summaries = "\n\n".join(batch_summaries)
    final_input = (
        f"Channel: #{channel_name}\n"
        f"Total messages: {len(messages)}\n"
        f"Batches processed: {len(batch_summaries)}\n\n"
        f"BATCH SUMMARIES:\n\n{combined_summaries}"
    )

    final_prompt = FINAL_DISTILL_PROMPT.replace("{channel_name}", channel_name)
    filename = _safe_filename(channel_name) + ".md"
    output_path = SLACK_KNOWLEDGE_DIR / filename

    print(f"  Final distillation for #{channel_name}...")
    distill_to_markdown(final_input, final_prompt, output_path, max_tokens=2000)

    return channel_name, len(messages), output_path


def scan_all(mode="full", progress_callback=None):
    """Scan all monitored Slack channels.

    Args:
        mode: 'full', '1yr', or 'incremental'
        progress_callback: optional fn(status_str) called with progress updates

    Returns:
        list of (channel_name, msg_count, output_path) tuples
    """
    client = _get_slack_client()
    channels = _get_monitored_channels()

    if not channels:
        print("[ERROR] No SLACK_MONITORED_CHANNELS configured")
        return []

    print(f"Scanning {len(channels)} Slack channels (mode={mode})")

    # Shared user cache across all channels
    user_cache = {}
    results = []

    for i, channel_id in enumerate(channels):
        if progress_callback:
            progress_callback(f"Channel {i + 1}/{len(channels)}")
        else:
            print(f"[{i + 1}/{len(channels)}] Channel {channel_id}")

        # In full mode, skip channels that already have a knowledge file
        # (use incremental mode to update existing files)
        if mode == "full":
            try:
                info = client.conversations_info(channel=channel_id)
                ch_name = info["channel"]["name"]
                existing = SLACK_KNOWLEDGE_DIR / f"{ch_name}.md"
                if existing.exists():
                    print(f"  [SKIP] #{ch_name}: knowledge file already exists")
                    results.append((ch_name, 0, existing))
                    continue
            except Exception:
                pass

        result = scan_channel(
            client,
            channel_id,
            mode=mode,
            user_cache=user_cache,
            progress_callback=progress_callback,
        )
        if result:
            results.append(result)

        # Pace between channels
        time.sleep(REQUEST_DELAY)

    # Generate summary if we scanned multiple channels
    if len(results) > 1:
        _generate_summary(results)

    update_scan_timestamp("slack")
    print(f"Slack scan complete: {len(results)} channels processed")
    return results


def _generate_summary(results):
    """Generate a cross-channel summary from all scanned channels."""
    lines = ["# Slack Channels Overview\n"]
    lines.append(f"Last scanned: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    lines.append(f"Total channels scanned: {len(results)}\n")

    lines.append("## Channels\n")
    for name, msg_count, path in sorted(results, key=lambda r: r[0]):
        lines.append(f"- **#{name}** -- {msg_count} messages -- [{path.name}]({path.name})")

    # Distill a strategic summary across channels
    channel_snippets = []
    for name, msg_count, path in results:
        if path.exists():
            content = path.read_text()
            channel_snippets.append(f"### #{name}\n{content[:500]}")

    if channel_snippets:
        combined = "\n\n".join(channel_snippets)
        if len(combined) > 90000:
            combined = combined[:90000] + "\n\n[TRUNCATED]"

        claude_client = get_claude_client()
        for attempt in range(5):
            try:
                message = claude_client.messages.create(
                    model=DISTILL_MODEL,
                    max_tokens=2000,
                    system=(
                        "You are creating a strategic overview of all Slack channels for Black Swift Technologies (BST). "
                        "Summarize cross-channel themes: active projects, key people, decision patterns, "
                        "recurring topics, and anything that connects across channels. Be concise and factual. "
                        "Output markdown."
                    ),
                    messages=[{"role": "user", "content": f"Channel summaries:\n\n{combined}"}],
                )
                lines.append(f"\n## Strategic Summary\n\n{message.content[0].text}")
                break
            except Exception as e:
                if "rate_limit" in str(e).lower():
                    wait = 30 * (attempt + 1)
                    print(f"  Rate limited on summary, waiting {wait}s...")
                    time.sleep(wait)
                else:
                    print(f"  [WARN] Summary generation failed: {e}")
                    break

    summary_path = SLACK_KNOWLEDGE_DIR / "summary.md"
    write_knowledge_file(summary_path, "\n".join(lines))
    print(f"Summary written to {summary_path}")
