"""Unified channel context resolver.

When the bot is addressed, we want to know:
- What channel it's in (name, topic, purpose)
- Whether that channel maps to a known BST project (code, gid, summary)
- What the recent conversation has been about

Results are cached for 5 minutes per channel to keep latency low.
"""

import re
import time
from pathlib import Path

from finances import (
    _load_channel_map,
    _extract_project_codes,
    _find_financial_file,
)

KNOWLEDGE_DIR = Path(__file__).parent / "knowledge"
PROJECT_DIR = KNOWLEDGE_DIR / "projects"

_ASANA_URL_RE = re.compile(r"app\.asana\.com/\d+/\d+/project/(\d+)")
_PROJECT_HEADER_RE = re.compile(r"^#\s*\[[^\]]+\]\s*(.+)$", re.MULTILINE)

_CACHE = {}
_CACHE_TTL = 300  # 5 minutes


def _channel_info(slack_client, channel_id):
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


def _resolve_project_code(channel_id, info):
    channel_map = _load_channel_map()
    if channel_id in channel_map:
        return channel_map[channel_id]

    search_text = f"{info.get('name', '')} {info.get('topic', '')} {info.get('purpose', '')}"
    codes = _extract_project_codes(search_text)
    if codes:
        # Prefer the most specific code (longest)
        for code in sorted(codes, key=len, reverse=True):
            if (PROJECT_DIR / f"{code}.md").exists():
                return code

    ch_name = (info.get("name") or "").lower().replace("-", " ")
    if ch_name and PROJECT_DIR.exists():
        for f in PROJECT_DIR.glob("*.md"):
            if f.name == "registry.md":
                continue
            try:
                header = f.read_text()[:500].lower()
                if ch_name in header or all(
                    w in header for w in ch_name.split() if len(w) > 2
                ):
                    return f.stem
            except Exception:
                continue
    return None


def _load_project_details(project_code):
    if not project_code:
        return {}
    path = PROJECT_DIR / f"{project_code}.md"
    if not path.exists():
        return {"project_code": project_code}
    content = path.read_text()
    name_match = _PROJECT_HEADER_RE.search(content)
    gid_match = _ASANA_URL_RE.search(content)
    details = {
        "project_code": project_code,
        "project_file": str(path),
        "project_name": name_match.group(1).strip() if name_match else None,
        "project_gid": gid_match.group(1) if gid_match else None,
        "project_summary": content[:2000],
    }
    fin = _find_financial_file(project_code)
    if fin:
        details["financial_file"] = str(fin)
    return details


def _fetch_recent_messages(slack_client, channel_id, limit=15):
    try:
        result = slack_client.conversations_history(channel=channel_id, limit=limit)
        messages = result.get("messages", [])
        messages.reverse()  # oldest first
        return messages
    except Exception:
        return []


def _build(slack_client, channel_id):
    is_dm = channel_id.startswith("D")
    ctx = {
        "channel_id": channel_id,
        "is_dm": is_dm,
        "channel_name": "",
        "topic": "",
        "purpose": "",
        "project_code": None,
        "project_gid": None,
        "project_name": None,
        "project_summary": None,
        "project_file": None,
        "financial_file": None,
        "recent_messages": [],
    }

    if not is_dm:
        info = _channel_info(slack_client, channel_id)
        ctx["channel_name"] = info["name"]
        ctx["topic"] = info["topic"]
        ctx["purpose"] = info["purpose"]
        code = _resolve_project_code(channel_id, info)
        if code:
            ctx.update(_load_project_details(code))

    ctx["recent_messages"] = _fetch_recent_messages(slack_client, channel_id)
    return ctx


def get_channel_context(slack_client, channel_id):
    """Return the unified context for a channel, cached for 5 minutes.

    Returns None if channel_id is missing or the slack client is unavailable.
    The recent_messages field is refreshed on every call (conversation history
    changes fast); the rest of the context hits the TTL cache.
    """
    if not channel_id or not slack_client:
        return None

    now = time.time()
    cached = _CACHE.get(channel_id)
    if cached and now - cached[0] < _CACHE_TTL:
        ctx = dict(cached[1])
        ctx["recent_messages"] = _fetch_recent_messages(slack_client, channel_id)
        return ctx

    ctx = _build(slack_client, channel_id)
    # Cache everything except recent_messages (fast-moving)
    cacheable = {k: v for k, v in ctx.items() if k != "recent_messages"}
    _CACHE[channel_id] = (now, cacheable)
    return ctx


def format_recent_messages(messages, bot_user_id=None, max_messages=10):
    """Render recent Slack messages as a plain-text transcript for prompts."""
    if not messages:
        return ""
    lines = []
    for msg in messages[-max_messages:]:
        if msg.get("subtype") in ("channel_join", "channel_leave", "bot_add"):
            continue
        text = (msg.get("text") or "").strip()
        if not text:
            continue
        user = msg.get("user") or msg.get("bot_id") or "unknown"
        is_bot = msg.get("bot_id") or user == bot_user_id
        label = "Jack Bot" if is_bot else f"<@{user}>"
        lines.append(f"{label}: {text}")
    return "\n".join(lines)
