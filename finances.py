"""Financial summary lookup for project channels.

When a user says "finances" in a channel, this module:
1. Checks the channel-to-project mapping file
2. Falls back to extracting project codes from channel name/topic/purpose
3. Runs the raw data through Claude to produce a clean Slack-formatted summary
"""

import os
import re
from pathlib import Path

import anthropic

FINANCIAL_DIR = Path(__file__).parent / "knowledge" / "financial" / "by_project"
OVERVIEW_PATH = Path(__file__).parent / "knowledge" / "financial" / "overview.md"
CHANNEL_MAP_PATH = Path(__file__).parent / "knowledge" / "channel_projects.md"
PROJECT_DIR = Path(__file__).parent / "knowledge" / "projects"

SUMMARIZE_PROMPT = """\
You are formatting a financial summary for Slack. Given raw project financial data, \
produce a clean, scannable summary using Slack formatting (not markdown tables).

Rules:
- Use *bold* for labels and key numbers
- Use bullet points, not tables (Slack doesn't render markdown tables)
- Skip sections with no data (don't show "N/A" or "Data not available" rows)
- Lead with the most important numbers: budget, invoiced, remaining
- Keep it concise — highlight what matters, skip the noise
- Include invoice history if present (just invoice #, date, amount, status)
- Include key milestones/deliverables if present
- Max ~15 lines"""


def _load_channel_map():
    """Load channel ID -> project code mapping from knowledge/channel_projects.md."""
    mapping = {}
    if not CHANNEL_MAP_PATH.exists():
        return mapping
    for line in CHANNEL_MAP_PATH.read_text().splitlines():
        line = line.split("#")[0].strip()
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


def _summarize_for_slack(raw_content):
    """Use Claude to convert raw financial markdown into clean Slack output."""
    try:
        client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=800,
            system=SUMMARIZE_PROMPT,
            messages=[{"role": "user", "content": raw_content[:6000]}],
        )
        return message.content[0].text
    except Exception:
        # Fall back to truncated raw content if Claude fails
        if len(raw_content) > 3800:
            return raw_content[:3800] + "\n\n_(truncated)_"
        return raw_content


def _find_project_data(channel_id, slack_client):
    """Find the raw financial/project data for a channel. Returns (content, None) or (None, error_msg)."""
    # 1. Explicit channel-to-project mapping
    channel_map = _load_channel_map()
    if channel_id in channel_map:
        code = channel_map[channel_id]
        path = _find_financial_file(code)
        if path:
            return path.read_text(), None
        proj_path = PROJECT_DIR / f"{code}.md"
        if proj_path.exists():
            return proj_path.read_text(), None
        return None, f"Channel mapped to project `{code}` but no financial data found."

    # 2. Project codes in channel name/topic/purpose
    info = _get_channel_info(slack_client, channel_id)
    search_text = f"{info['name']} {info['topic']} {info['purpose']}"
    codes = _extract_project_codes(search_text)

    for code in sorted(codes, key=len, reverse=True):
        path = _find_financial_file(code)
        if path:
            return path.read_text(), None

    # 3. Match channel name against project registry files
    if info.get("name") and PROJECT_DIR.exists():
        ch_name = info["name"].lower().replace("-", " ")
        for f in PROJECT_DIR.glob("*.md"):
            if f.name == "registry.md":
                continue
            try:
                header = f.read_text()[:500].lower()
                if ch_name in header or all(w in header for w in ch_name.split() if len(w) > 2):
                    code = f.stem
                    fin_path = _find_financial_file(code)
                    if fin_path:
                        return fin_path.read_text(), None
                    return f.read_text(), None
            except Exception:
                continue

    return None, "No financial data available for this channel's project."


def get_project_finances(slack_client, channel_id):
    """Look up financial info for the project associated with a Slack channel."""
    if not channel_id:
        return "I can't determine the project for this channel."

    content, error = _find_project_data(channel_id, slack_client)
    if error:
        return error

    return _summarize_for_slack(content)
