#!/usr/bin/env bash
# Pull the Railway service variables into a local .env so dry runs
# (test_pipeline.py, test_commercial_sales.py, test_identity.py) can hit the
# real APIs without hand-copying secrets.
#
#   railway login && railway link      # once
#   ./scripts/pull_env.sh
#
# .env is gitignored — never commit the output.
set -euo pipefail

cd "$(dirname "$0")/.."

if ! command -v railway >/dev/null 2>&1; then
    echo "railway CLI not found. Install: https://docs.railway.com/guides/cli" >&2
    exit 1
fi

if ! railway whoami >/dev/null 2>&1; then
    echo "Not logged in. Run: railway login" >&2
    exit 1
fi

if [ -f .env ]; then
    cp .env ".env.bak.$(date +%Y%m%d%H%M%S)"
    echo "Backed up existing .env"
fi

railway variables --kv > .env.tmp
mv .env.tmp .env
chmod 600 .env
echo "Wrote .env ($(grep -c . .env) variables)"
