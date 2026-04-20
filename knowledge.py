"""Persistent knowledge base for company priorities, project context, and strategic insights.

Uses a dedicated Slack channel as persistent storage (survives deploys).
Entries are structured with tags for easy retrieval and reasoning.

Entry types:
  [PRIORITY]    - Company/team priority rankings and why
  [PROJECT]     - Project metadata: dollar value, client, timeline, risk level
  [CLIENT]      - Client relationship context
  [DELIVERABLE] - Upcoming deliverables with dates
  [TEAM]        - Team member context: strengths, capacity, preferences
  [CORRECTION]  - User corrections to task prioritization
  [FEEDBACK]    - Implicit feedback from team member replies
  [INSIGHT]     - Forward-looking strategic observations
  [SOURCE]      - Where recurring useful info lives (drives, channels, projects)
  [BUG]         - Bug reports for Jack Bot or BST systems
  [FEATURE]     - Feature requests for Jack Bot or BST systems
  [ERROR]       - Pipeline errors and data source failures
"""

import os
import time

import anthropic


def _get_channel():
    return os.environ.get("KNOWLEDGE_CHANNEL", "")


def store_entry(slack_client, entry_type, content):
    """Store a knowledge entry in the knowledge channel."""
    channel = _get_channel()
    if not channel:
        return
    slack_client.chat_postMessage(
        channel=channel,
        text=f"*[{entry_type}]*\n{content}",
    )


def store_correction(slack_client, user_name, correction):
    """Store a user correction."""
    store_entry(slack_client, "CORRECTION", f"From {user_name}: {correction}")


def store_feedback(slack_client, user_name, feedback):
    """Store implicit feedback from a team member's reply in the tasks channel."""
    store_entry(slack_client, "FEEDBACK", f"From {user_name}: {feedback}")


def store_bug(slack_client, user_name, description):
    """Store a bug report."""
    store_entry(slack_client, "BUG", f"From {user_name}: {description}")


def store_feature(slack_client, user_name, description):
    """Store a feature request."""
    store_entry(slack_client, "FEATURE", f"From {user_name}: {description}")


def list_items(slack_client, item_type):
    """List all open BUG or FEATURE entries, formatted for Slack output."""
    entries = get_knowledge(slack_client, [item_type])
    if not entries:
        label = "bugs" if item_type == "BUG" else "feature requests"
        return f"No {label} on file."

    label = ":bug: *Open Bugs*" if item_type == "BUG" else ":sparkles: *Feature Requests*"
    lines = [label]
    for i, entry in enumerate(entries, 1):
        lines.append(f"{i}. {entry['content']}")
    return "\n".join(lines)


def store_daily_snapshot(slack_client, summary):
    """Store the daily summary for comparison."""
    store_entry(slack_client, "SNAPSHOT", summary)


def get_knowledge(slack_client, entry_types=None, days=None):
    """Retrieve knowledge entries, optionally filtered by type and time.

    Args:
        slack_client: Slack WebClient
        entry_types: list of types to filter (e.g. ["PRIORITY", "PROJECT"]) or None for all
        days: only get entries from last N days, or None for all time

    Returns:
        list[dict]: [{"type": str, "content": str, "ts": str}]
    """
    channel = _get_channel()
    if not channel:
        return []

    oldest = str(time.time() - (days * 86400)) if days else "0"
    entries = []
    cursor = None

    def _history_with_retry(kwargs, max_attempts=5):
        """Call conversations_history with rate-limit retry.

        The daily pipeline fires several concurrent reads of this channel,
        which hits Slack's per-method rate limit. Without retry, the loop
        returned 0 entries mid-pagination and silently dropped the rest —
        which is why status overrides came back empty despite corrections
        being present. Retry on 429 using the Retry-After header.
        """
        from slack_sdk.errors import SlackApiError
        for attempt in range(max_attempts):
            try:
                return slack_client.conversations_history(**kwargs)
            except SlackApiError as e:
                status = getattr(getattr(e, "response", None), "status_code", None)
                if status == 429:
                    retry_after = int(e.response.headers.get("Retry-After", 2))
                    time.sleep(min(retry_after, 15))
                    continue
                raise
        return None

    while True:
        try:
            kwargs = {"channel": channel, "limit": 200, "oldest": oldest}
            if cursor:
                kwargs["cursor"] = cursor
            result = _history_with_retry(kwargs)
            if result is None:
                break
            for msg in result.get("messages", []):
                text = msg.get("text", "")
                for tag in ["PRIORITY", "PROJECT", "CLIENT", "DELIVERABLE",
                            "TEAM", "CORRECTION", "FEEDBACK", "INSIGHT", "SNAPSHOT",
                            "SOURCE", "BUG", "FEATURE", "ERROR", "DEBUG"]:
                    if text.startswith(f"*[{tag}]*"):
                        if entry_types is None or tag in entry_types:
                            content = text.replace(f"*[{tag}]*\n", "", 1)
                            entries.append({
                                "type": tag,
                                "content": content,
                                "ts": msg.get("ts", ""),
                            })
                        break
            cursor = result.get("response_metadata", {}).get("next_cursor")
            if not cursor:
                break
        except Exception:
            break

    entries.reverse()  # chronological
    return entries


def get_knowledge_summary(slack_client):
    """Get a formatted knowledge summary for inclusion in the daily prompt.

    Returns structured context: long-term priorities, project info, corrections, insights.
    """
    # Long-term knowledge (all time): priorities, projects, clients, team
    strategic = get_knowledge(slack_client, ["PRIORITY", "PROJECT", "CLIENT", "DELIVERABLE", "TEAM", "SOURCE"])

    # Recent corrections, feedback, and insights (last 30 days)
    recent = get_knowledge(slack_client, ["CORRECTION", "FEEDBACK", "INSIGHT"], days=30)

    # Previous day's snapshot
    snapshots = get_knowledge(slack_client, ["SNAPSHOT"], days=2)
    previous_summary = snapshots[-1]["content"] if snapshots else None

    sections = []

    if strategic:
        lines = ["=== COMPANY KNOWLEDGE BASE ==="]
        for entry in strategic:
            lines.append(f"[{entry['type']}] {entry['content']}")
        sections.append("\n".join(lines))

    if recent:
        lines = ["=== RECENT CORRECTIONS & INSIGHTS ==="]
        for entry in recent:
            lines.append(f"[{entry['type']}] {entry['content']}")
        sections.append("\n".join(lines))

    if previous_summary:
        sections.append(f"=== YESTERDAY'S SUMMARY ===\n{previous_summary}")

    return "\n\n".join(sections)


STATUS_OVERRIDE_PROMPT = (
    "You extract structured project/task status deltas from team corrections and feedback "
    "posted in a Slack knowledge channel. Each entry is tagged [CORRECTION] or [FEEDBACK] and "
    "may contain natural-language updates like 'Mexico is moved to the Fall', 'ADONIS is done, "
    "UMEX is handling the final report', 'the Navy kickoff is tomorrow, not today'.\n\n"
    "Your output will be pinned at the top of the daily briefing prompt as authoritative overrides "
    "that WIN over stale Asana tasks and distilled knowledge files. So precision matters.\n\n"
    "RULES:\n"
    "- Only extract durable status changes that affect prioritization: delays, completions, "
    "cancellations, reassignments, 'handled externally', date shifts.\n"
    "- Ignore casual chat, jokes, reactions, meta-comments about the bot itself.\n"
    "- If two entries contradict, trust the most recent one.\n"
    "- Quote the author and date ('per Maciej, Apr 17') so the reader can trust the source.\n"
    "- Identify the specific project or task by the name actually used in Asana when possible.\n"
    "- Output ONLY a bulleted markdown list. One line per override. No preamble, no headers.\n"
    "- If there are no meaningful overrides, output exactly: NONE\n\n"
    "Example good output:\n"
    "- Mexico USGS deployment (350-4): DELAYED to Fall 2026 — not departing April 20 (per Maciej, "
    "Apr 17; reconfirmed by Jack, Apr 20)\n"
    "- ADONIS (035-1): COMPLETE — UMEX is handling the final report, not BST. Project archived "
    "and final invoice sent (per Meredith & Alex, Apr 17)\n"
    "- Joshua Fromm priority: S3 delivery to UMES before end of May is now priority #1 "
    "(per Jack, Apr 20)"
)


_STATUS_KEYWORDS = (
    "delay", "delayed", "push", "pushed", "pushing", "moved", "move ",
    "complete", "completed", "done", "finish", "finished", "archived",
    "cancel", "cancelled", "canceled", "drop ", "dropped", "handled",
    "externally", "priority", "priorities", "priority #1", "first priority",
    "top priority", "most important", "critical", "asap",
    "reassign", "reassigned", "no longer", "instead of",
    "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep",
    "oct", "nov", "dec", "spring", "summer", "fall", "autumn", "winter",
    "end of", "by the end",
    "not departing", "not flying", "not going",
)


def _looks_like_status_change(text):
    low = text.lower()
    return any(kw in low for kw in _STATUS_KEYWORDS)


def get_status_overrides(slack_client, days=30):
    """Extract structured project-status overrides from recent CORRECTION/FEEDBACK.

    Runs the last `days` of knowledge-channel corrections through Haiku to distill
    them into a short, authoritative list of status deltas that the daily synthesis
    prompt can pin at the top. Returns an empty string if nothing meaningful.

    CORRECTION entries are always included. FEEDBACK is pre-filtered to messages
    that mention a status-change keyword, because the channel otherwise fills with
    casual chat that dilutes Haiku's signal and occasionally makes it return NONE.
    """
    entries = get_knowledge(slack_client, ["CORRECTION", "FEEDBACK"], days=days)
    if not entries:
        return ""

    # CORRECTION is explicit — keep all. FEEDBACK is noisy — keyword-filter.
    filtered = [
        e for e in entries
        if e["type"] == "CORRECTION" or _looks_like_status_change(e["content"])
    ]
    if not filtered:
        return ""

    # Build the source text with timestamps so Haiku can cite dates and resolve conflicts
    import datetime as _dt
    lines = []
    for entry in filtered:
        ts = entry.get("ts", "")
        try:
            when = _dt.datetime.fromtimestamp(float(ts)).strftime("%Y-%m-%d") if ts else ""
        except Exception:
            when = ""
        prefix = f"[{entry['type']}]"
        if when:
            prefix += f" [{when}]"
        lines.append(f"{prefix} {entry['content'][:600]}")
    source = "\n".join(lines)

    # Cap to ~60k chars, keeping the most recent (tail wins for conflict resolution)
    if len(source) > 60000:
        source = source[-60000:]

    try:
        client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1200,
            system=STATUS_OVERRIDE_PROMPT,
            messages=[{"role": "user", "content": source}],
        )
        result = message.content[0].text.strip()
    except Exception as e:
        return f"[Status override extraction failed: {e}]"

    if not result or result == "NONE":
        # If Haiku dismissed everything but we clearly have CORRECTION entries,
        # pass them through verbatim rather than losing the signal entirely.
        corrections_only = [e for e in filtered if e["type"] == "CORRECTION"]
        if corrections_only:
            fallback = []
            for e in corrections_only:
                when = ""
                try:
                    import datetime as _dt2
                    ts = e.get("ts", "")
                    when = _dt2.datetime.fromtimestamp(float(ts)).strftime("%Y-%m-%d") if ts else ""
                except Exception:
                    pass
                suffix = f" (stored {when})" if when else ""
                fallback.append(f"- {e['content']}{suffix}")
            return "\n".join(fallback)
        return ""
    return result


def auto_extract_knowledge(slack_client, context_text):
    """Use Claude to extract durable knowledge from daily data.

    Identifies: project valuations, client signals, priority shifts,
    upcoming deliverables, team capacity issues.
    """
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    # Get existing knowledge to avoid duplicates
    existing = get_knowledge(slack_client, ["PRIORITY", "PROJECT", "CLIENT", "DELIVERABLE"])
    existing_text = "\n".join(e["content"] for e in existing[-50:]) if existing else "None yet."

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=800,
        system=(
            "You extract durable business knowledge from daily work data for Black Swift Technologies (BST). "
            "Look for NEW information not already in the existing knowledge base. "
            "This knowledge persists and is used in future daily briefings, so focus on durable facts. "
            "Output ONLY new findings, one per line, prefixed with the type tag:\n"
            "  [PROJECT] - project name, dollar value, client, timeline, status, Asana project name, "
            "shared drive location if known. Include contract values from milestone subtasks.\n"
            "  [CLIENT] - client relationship signals, satisfaction, risk, key contacts\n"
            "  [DELIVERABLE] - specific deliverable with date, owner, and dollar amount if known\n"
            "  [PRIORITY] - shifts in company/team priorities and why (from meeting notes, emails, slack)\n"
            "  [TEAM] - capacity, skills, workload observations\n"
            "  [INSIGHT] - forward-looking strategic observations (upcoming contracts, proposals, "
            "competitive intel, funding opportunities)\n"
            "  [SOURCE] - where useful recurring info lives (e.g. 'Sales shared drive has client SOWs', "
            "'BD Pipeline project tracks all active opportunities')\n\n"
            "Be specific and include dates, names, dollar amounts, and Asana/Drive references. "
            "If nothing genuinely new, respond with exactly: NONE"
        ),
        messages=[{
            "role": "user",
            "content": (
                f"Existing knowledge:\n{existing_text}\n\n"
                f"Today's data:\n{context_text}"
            ),
        }],
    )

    result = message.content[0].text.strip()
    if result == "NONE":
        return

    # Parse and store each line
    for line in result.split("\n"):
        line = line.strip()
        if not line:
            continue
        for tag in ["PROJECT", "CLIENT", "DELIVERABLE", "PRIORITY", "TEAM", "INSIGHT", "SOURCE"]:
            if line.startswith(f"[{tag}]"):
                content = line[len(f"[{tag}]"):].strip().lstrip("-").strip()
                if content:
                    store_entry(slack_client, tag, content)
                break
