"""Financial summary lookup for project channels.

When a user says "finances" in a channel, this module:
1. Gets the channel name/topic/purpose
2. Matches it to a project code in the financial knowledge files
3. Returns the financial summary for that project
"""

import re
from pathlib import Path

FINANCIAL_DIR = Path(__file__).parent / "knowledge" / "financial" / "by_project"
OVERVIEW_PATH = Path(__file__).parent / "knowledge" / "financial" / "overview.md"


def _extract_project_codes(text):
    """Extract project codes from text (e.g., '024-01', '301_3', '024.01')."""
    # Match patterns like 024-01, 024_01, 024.01, or just 024
    codes = set()
    for match in re.finditer(r"\b(\d{3})[_\-.](\d{1,2})\b", text):
        codes.add(f"{match.group(1)}_{match.group(2)}")
    # Also match 3-digit codes without suffix
    for match in re.finditer(r"\b(\d{3})\b", text):
        codes.add(match.group(1))
    return codes


def _find_financial_file(project_code):
    """Find the financial knowledge file for a project code."""
    if not FINANCIAL_DIR.exists():
        return None
    # Try exact match first
    path = FINANCIAL_DIR / f"{project_code}.md"
    if path.exists():
        return path
    # Try with zero-padded suffix
    for f in FINANCIAL_DIR.glob(f"{project_code}*.md"):
        return f
    # Try matching just the prefix (e.g., "301" matches "301_3")
    if "_" not in project_code:
        for f in sorted(FINANCIAL_DIR.glob(f"{project_code}_*.md")):
            return f
    return None


def _get_channel_info(slack_client, channel_id):
    """Get channel name, topic, and purpose."""
    try:
        result = slack_client.conversations_info(channel=channel_id)
        ch = result.get("channel", {})
        return {
            "name": ch.get("name", ""),
            "topic": ch.get("topic", {}).get("value", ""),
            "purpose": ch.get("purpose", {}).get("value", ""),
        }
    except Exception:
        return {"name": "", "topic": "", "purpose": ""}


def get_project_finances(slack_client, channel_id):
    """Look up financial info for the project associated with a Slack channel."""
    if not channel_id:
        return "I can't determine the project for this channel."

    info = _get_channel_info(slack_client, channel_id)
    search_text = f"{info['name']} {info['topic']} {info['purpose']}"

    # Extract project codes from channel metadata
    codes = _extract_project_codes(search_text)

    # Try to find a matching financial file
    for code in sorted(codes, key=len, reverse=True):  # longest match first
        path = _find_financial_file(code)
        if path:
            content = path.read_text()
            # Truncate if too long for Slack (4000 char limit per message)
            if len(content) > 3800:
                content = content[:3800] + "\n\n_(truncated — full report available in knowledge files)_"
            return content

    # No project code found — offer the company overview
    if not codes:
        if OVERVIEW_PATH.exists():
            overview = OVERVIEW_PATH.read_text()
            if len(overview) > 3800:
                overview = overview[:3800] + "\n\n_(truncated)_"
            return f"No project code found in this channel's name/topic. Here's the company overview:\n\n{overview}"
        return (
            "I couldn't find a project code in this channel's name or topic. "
            "Try setting the channel topic to include the project code (e.g., `024-01`)."
        )

    return (
        f"Found project code(s) `{'`, `'.join(codes)}` in this channel, "
        f"but no financial data exists for them yet. "
        f"Run the financial scanner to populate: `python scan.py financial`"
    )
