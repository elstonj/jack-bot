#!/bin/bash
# Nightly knowledge scan — runs incremental scan, commits, and pushes.
# Any errors are logged as BUG entries in the knowledge channel via Slack.
#
# Intended for crontab: 0 2 * * * /home/elstonj/Documents/jack_bot/scripts/nightly_scan.sh

set -euo pipefail

PROJECT_DIR="/home/elstonj/Documents/jack_bot"
LOG_FILE="$PROJECT_DIR/scripts/nightly_scan.log"
VENV="$PROJECT_DIR/.venv"

cd "$PROJECT_DIR"

# Load env
set -a
source "$PROJECT_DIR/.env"
set +a

# Activate venv
source "$VENV/bin/activate"

# Timestamp
echo "=== Nightly scan started at $(date) ===" > "$LOG_FILE"

ERRORS=""

# Run incremental scan
echo "Running incremental scan..." >> "$LOG_FILE"
if python scan.py all --mode incremental >> "$LOG_FILE" 2>&1; then
    echo "Scan completed successfully." >> "$LOG_FILE"
else
    ERRORS="$ERRORS\nKnowledge scan failed. Check $LOG_FILE for details."
    echo "SCAN FAILED" >> "$LOG_FILE"
fi

# Run post-scan enrichments (depend on data from other scanners)
echo "Running contact enrichment..." >> "$LOG_FILE"
if python scan.py enrich-contacts >> "$LOG_FILE" 2>&1; then
    echo "Contact enrichment completed." >> "$LOG_FILE"
else
    ERRORS="$ERRORS\nContact enrichment failed."
    echo "ENRICHMENT FAILED" >> "$LOG_FILE"
fi

echo "Running project cost tracking..." >> "$LOG_FILE"
if python scan.py costs >> "$LOG_FILE" 2>&1; then
    echo "Cost tracking completed." >> "$LOG_FILE"
else
    ERRORS="$ERRORS\nCost tracking failed."
    echo "COST TRACKING FAILED" >> "$LOG_FILE"
fi

# Check for changes
CHANGES=$(git status --porcelain knowledge/ | wc -l)
echo "Files changed: $CHANGES" >> "$LOG_FILE"

if [ "$CHANGES" -gt 0 ]; then
    # Commit and push
    echo "Committing knowledge updates..." >> "$LOG_FILE"
    git add knowledge/ knowledge/.scan_state.json
    git commit -m "Nightly knowledge scan update $(date +%Y-%m-%d)" >> "$LOG_FILE" 2>&1

    if git push origin master >> "$LOG_FILE" 2>&1; then
        echo "Pushed to remote." >> "$LOG_FILE"
    else
        ERRORS="$ERRORS\nGit push failed after nightly scan."
        echo "PUSH FAILED" >> "$LOG_FILE"
    fi
else
    echo "No changes to commit." >> "$LOG_FILE"
fi

# Report errors as BUG entries
if [ -n "$ERRORS" ]; then
    echo "Reporting errors to knowledge channel..." >> "$LOG_FILE"
    python -c "
import os
from slack_sdk import WebClient
from knowledge import store_bug

client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])
errors = '''$ERRORS'''
store_bug(client, 'Nightly Scan', errors.strip())
" >> "$LOG_FILE" 2>&1
fi

echo "=== Nightly scan finished at $(date) ===" >> "$LOG_FILE"
