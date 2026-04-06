#!/usr/bin/env python3
"""Daily bug/feature digest — posts summary to knowledge channel and updates knowledge files.

Intended for crontab: 30 7 * * 1-5 (7:30am MT weekdays)

Collects all BUG and FEATURE entries from the knowledge channel,
posts a formatted digest, and writes them to knowledge files for reference.
"""

import os
import sys
from pathlib import Path
from datetime import datetime

# Setup
PROJECT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_DIR))

# Load .env
env_path = PROJECT_DIR / ".env"
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key and key not in os.environ:
                os.environ[key] = value

from slack_sdk import WebClient
from knowledge import get_knowledge, store_entry

client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
knowledge_channel = os.environ.get("KNOWLEDGE_CHANNEL", "")

if not knowledge_channel:
    print("KNOWLEDGE_CHANNEL not set")
    sys.exit(1)


def format_digest():
    """Build the bug/feature digest message."""
    bugs = get_knowledge(client, ["BUG"])
    features = get_knowledge(client, ["FEATURE"])

    if not bugs and not features:
        return None

    lines = [f":clipboard: *Daily Bug & Feature Digest — {datetime.now().strftime('%b %d, %Y')}*\n"]

    if bugs:
        lines.append(f":bug: *Open Bugs ({len(bugs)})*")
        for i, bug in enumerate(bugs, 1):
            lines.append(f"  {i}. {bug['content']}")
        lines.append("")

    if features:
        lines.append(f":sparkles: *Feature Requests ({len(features)})*")
        for i, feat in enumerate(features, 1):
            lines.append(f"  {i}. {feat['content']}")
        lines.append("")

    lines.append(f"_Total: {len(bugs)} bugs, {len(features)} feature requests_")
    return "\n".join(lines)


def update_knowledge_files(bugs, features):
    """Write current bugs and features to knowledge files for reference."""
    knowledge_dir = PROJECT_DIR / "knowledge"

    # Bugs file
    if bugs:
        lines = [
            "# Open Bug Reports",
            f"_Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}_\n",
        ]
        for i, bug in enumerate(bugs, 1):
            lines.append(f"{i}. {bug['content']}")
        (knowledge_dir / "bugs.md").write_text("\n".join(lines))
    else:
        bugs_path = knowledge_dir / "bugs.md"
        if bugs_path.exists():
            bugs_path.unlink()

    # Features file
    if features:
        lines = [
            "# Feature Requests",
            f"_Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}_\n",
        ]
        for i, feat in enumerate(features, 1):
            lines.append(f"{i}. {feat['content']}")
        (knowledge_dir / "features.md").write_text("\n".join(lines))
    else:
        features_path = knowledge_dir / "features.md"
        if features_path.exists():
            features_path.unlink()


def main():
    bugs = get_knowledge(client, ["BUG"])
    features = get_knowledge(client, ["FEATURE"])

    # Post digest to knowledge channel
    digest = format_digest()
    if digest:
        client.chat_postMessage(channel=knowledge_channel, text=digest)
        print(f"Posted digest: {len(bugs)} bugs, {len(features)} features")
    else:
        print("No bugs or features to report.")

    # Update knowledge files
    update_knowledge_files(bugs, features)
    print("Knowledge files updated.")


if __name__ == "__main__":
    main()
