"""Financial summary lookup for project channels.

When a user says "finances" in a channel, this module:
1. Checks the channel-to-project mapping file
2. Falls back to extracting project codes from channel name/topic/purpose
3. Returns the financial summary for that project
"""

import re
from pathlib import Path

FINANCIAL_DIR = Path(__file__).parent / "knowledge" / "financial" / "by_project"
OVERVIEW_PATH = Path(__file__).parent / "knowledge" / "financial" / "overview.md"
CHANNEL_MAP_PATH = Path(__file__).parent / "knowledge" / "channel_projects.md"


def _load_channel_map():
    """Load channel ID -> project code mapping from knowledge/channel_projects.md."""
    mapping = {}
    if not CHANNEL_MAP_PATH.exists():
        return mapping
    for line in CHANNEL_MAP_PATH.read_text().splitlines():
        line = line.split("#")[0].strip()  # strip comments
        if "=" in line:
            parts = line.split("=", 1)
            channel_id = parts[0].strip()
            project_code = parts[1].strip()
            if channel_id and project_code:
                mapping[channel_id] = project_code
    return mapping


def _extract_project_codes(text):
    """Extract project codes from text (e.g., '024-01', '301_3', '024.01')."""
    codes = set()
    for match in re.finditer(r"\b(\d{3})[_\-.](\d{1,2})\b", text):
        codes.add(f"{match.group(1)}_{match.group(2)}")
    for match in re.finditer(r"\b(\d{3})\b", text):
        codes.add(match.group(1))
    return codes


def _find_financial_file(project_code):
    """Find the financial knowledge file for a project code."""
    if not FINANCIAL_DIR.exists():
        return None
    path = FINANCIAL_DIR / f"{project_code}.md"
    if path.exists():
        return path
    for f in FINANCIAL_DIR.glob(f"{project_code}*.md"):
        return f
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


def _format_financial_content(path):
    """Read and truncate a financial file for Slack output."""
    content = path.read_text()
    if len(content) > 3800:
        content = content[:3800] + "\n\n_(truncated — full report in knowledge files)_"
    return content


def get_project_finances(slack_client, channel_id):
    """Look up financial info for the project associated with a Slack channel."""
    if not channel_id:
        return "I can't determine the project for this channel."

    # 1. Check the explicit channel-to-project mapping
    channel_map = _load_channel_map()
    if channel_id in channel_map:
        code = channel_map[channel_id]
        path = _find_financial_file(code)
        if path:
            return _format_financial_content(path)
        return f"Channel mapped to project `{code}` but no financial data found. Run `python scan.py financial`."

    # 2. Try extracting project codes from channel name/topic/purpose
    info = _get_channel_info(slack_client, channel_id)
    search_text = f"{info['name']} {info['topic']} {info['purpose']}"
    codes = _extract_project_codes(search_text)

    for code in sorted(codes, key=len, reverse=True):
        path = _find_financial_file(code)
        if path:
            return _format_financial_content(path)

    # 3. No match — return company overview
    if OVERVIEW_PATH.exists():
        overview = OVERVIEW_PATH.read_text()
        if len(overview) > 3800:
            overview = overview[:3800] + "\n\n_(truncated)_"
        return f"No project mapped to this channel. Here's the company overview:\n\n{overview}"

    return (
        "No project code found for this channel. "
        "Add a mapping in `knowledge/channel_projects.md` or set the channel topic to include the project code."
    )
