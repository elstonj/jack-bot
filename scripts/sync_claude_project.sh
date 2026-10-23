#!/bin/bash
# Rebuild the scrubbed knowledge export and, if it changed, replace the files
# in the team's "Ask Black Swift Technologies" claude.ai project.
#
# claude.ai has no API for project files, and its Drive/GitHub sync only works
# in private projects, so the upload is driven through Claude in Chrome by a
# headless `claude -p` run. That needs Chrome open with the extension connected
# to the Black Swift account; if it isn't, this exits non-zero and the nightly
# scan reports it as a BUG. The last uploaded digest is recorded so an
# unchanged export never triggers an upload.

set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
EXPORT_DIR="$PROJECT_DIR/export/claude_project"
UPLOADED="$PROJECT_DIR/export/.uploaded_digest"
CLAUDE_BIN="${CLAUDE_BIN:-$HOME/.local/bin/claude}"

cd "$PROJECT_DIR"
python scripts/export_claude_project.py

if [ -f "$UPLOADED" ] && cmp -s "$EXPORT_DIR/.digest" "$UPLOADED"; then
    echo "Claude project export unchanged; skipping upload."
    exit 0
fi

PROMPT="$(sed "s#EXPORT_DIR#$EXPORT_DIR#g" scripts/claude_project_sync_prompt.md)"
OUTPUT="$("$CLAUDE_BIN" -p --chrome \
    --allowedTools "mcp__claude-in-chrome__*" \
    --add-dir "$EXPORT_DIR" \
    "$PROMPT" 2>&1)" || true
echo "$OUTPUT"

if [ "$(printf '%s\n' "$OUTPUT" | grep -v '^\s*$' | tail -1)" = "SYNC_OK" ]; then
    cp "$EXPORT_DIR/.digest" "$UPLOADED"
    echo "Claude project updated."
else
    echo "Claude project upload failed." >&2
    exit 1
fi
