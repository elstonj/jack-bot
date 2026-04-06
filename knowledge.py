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
  [INSIGHT]     - Forward-looking strategic observations
  [SOURCE]      - Where recurring useful info lives (drives, channels, projects)
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

    while True:
        try:
            kwargs = {"channel": channel, "limit": 200, "oldest": oldest}
            if cursor:
                kwargs["cursor"] = cursor
            result = slack_client.conversations_history(**kwargs)
            for msg in result.get("messages", []):
                text = msg.get("text", "")
                for tag in ["PRIORITY", "PROJECT", "CLIENT", "DELIVERABLE",
                            "TEAM", "CORRECTION", "FEEDBACK", "INSIGHT", "SNAPSHOT", "SOURCE", "ERROR", "DEBUG"]:
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
