"""Base scanner infrastructure for knowledge extraction.

Each scanner:
1. Fetches raw data from a source (Asana, Toggl, Slack, etc.)
2. Distills it into structured markdown knowledge files via Claude
3. Tracks scan state (last run timestamp) for incremental updates
"""

import json
import os
import time
from datetime import datetime, date, timedelta
from pathlib import Path

import anthropic

KNOWLEDGE_DIR = Path(__file__).parent.parent / "knowledge"
SCAN_STATE_FILE = KNOWLEDGE_DIR / ".scan_state.json"

# Distillation model — use haiku for cost efficiency on large volumes
DISTILL_MODEL = "claude-haiku-4-5-20251001"


def get_claude_client():
    return anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


def get_scan_state():
    """Load scan state (last run timestamps per source)."""
    if SCAN_STATE_FILE.exists():
        return json.loads(SCAN_STATE_FILE.read_text())
    return {}


def save_scan_state(state):
    """Persist scan state."""
    SCAN_STATE_FILE.write_text(json.dumps(state, indent=2))


def update_scan_timestamp(source_name):
    """Record that a source was just scanned."""
    state = get_scan_state()
    state[source_name] = datetime.now().isoformat()
    save_scan_state(state)


def get_last_scan(source_name):
    """Get the last scan timestamp for a source, or None."""
    state = get_scan_state()
    ts = state.get(source_name)
    if ts:
        return datetime.fromisoformat(ts)
    return None


def time_range_for_mode(mode):
    """Return (start_date, end_date) for the given scan mode.

    Modes:
        'full'        — all data (start_date=None means no time filter)
        '1yr'         — last 365 days
        'incremental' — since last scan (caller must handle this)
    """
    end_date = date.today()
    if mode == "full":
        return None, end_date
    elif mode == "1yr":
        return end_date - timedelta(days=365), end_date
    else:
        return None, end_date  # incremental handled by caller


def distill_to_markdown(raw_text, system_prompt, output_path, max_tokens=2000):
    """Use Claude to distill raw data into a structured markdown knowledge file.

    If the file already exists, Claude is told to update/merge rather than replace.
    """
    client = get_claude_client()

    existing = ""
    if output_path.exists():
        existing = output_path.read_text()

    user_content = raw_text
    if existing:
        user_content = (
            f"EXISTING KNOWLEDGE FILE (update/merge with new data, don't lose info):\n"
            f"---\n{existing}\n---\n\n"
            f"NEW RAW DATA:\n{raw_text}"
        )

    # Truncate if excessively large (rough token estimate: 4 chars/token, stay under 25k tokens)
    max_chars = 90000
    if len(user_content) > max_chars:
        user_content = user_content[:max_chars] + "\n\n[TRUNCATED — data was too large]"

    # Retry with backoff for rate limits
    for attempt in range(5):
        try:
            message = client.messages.create(
                model=DISTILL_MODEL,
                max_tokens=max_tokens,
                system=system_prompt,
                messages=[{"role": "user", "content": user_content}],
            )
            break
        except anthropic.RateLimitError:
            wait = 30 * (attempt + 1)
            print(f"    Rate limited, waiting {wait}s (attempt {attempt + 1}/5)...")
            time.sleep(wait)
    else:
        print(f"    [ERROR] Rate limit exceeded after 5 retries, skipping {output_path.name}")
        return None

    content = message.content[0].text
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content)
    return content


def write_knowledge_file(path, content):
    """Write a knowledge file directly (no Claude distillation)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
