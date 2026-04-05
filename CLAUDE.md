# Jack Bot - Development Guide

## Project Overview
Jack Bot is an AI-powered project management assistant for Black Swift Technologies (BST). It synthesizes data from Asana, Toggl, Google Workspace, and Slack into prioritized daily briefings posted to Slack, and answers ad-hoc questions about projects, contacts, and team activity.

## Architecture

### Core Pipeline (`daily_research.py`)
- Runs daily at 8am MT via APScheduler (`scheduler.py`)
- Reads pre-distilled knowledge files for historical context
- Fetches only live/time-sensitive data: today's calendar, yesterday's Toggl, 24h email/Slack
- Sends combined context to Claude for synthesis into per-person task briefings
- Falls back to full live data fetch if knowledge files don't exist

### Knowledge Layer (`knowledge/`, `scanners/`, `scan.py`)
- 161 distilled markdown files covering 6 data sources
- `scan.py` CLI: `python scan.py <source> --mode full|1yr|incremental`
- Scanners fetch raw data, distill via Claude (Haiku) into structured markdown
- Knowledge files are committed to git and deployed via Railway
- Scan state tracked in `knowledge/.scan_state.json`

### Q&A System (`knowledge_qa.py`)
- Routes questions to relevant knowledge files via keyword matching
- Loads matched files (capped at ~50k tokens), sends to Claude for answers
- Triggered by questions in @mentions or DMs (contains `?`, question words, or `ask:` prefix)

### Slack Integration (`app.py`)
- Slack Bolt app with Flask adapter for Railway
- Commands: `tasks`, `correct:`, `note:`, `weather`, `/refresh-tasks`
- Questions route to knowledge Q&A; non-questions route to personality chat
- Corrections stored in Slack knowledge channel, used in next pipeline run (rule #1 priority)

### Personality (`personality.py`)
- "Jack Bot" - bitter old-school Unix programmer persona
- Used for non-question conversational messages

## Key Data Sources
| Source | Client | Scanner |
|--------|--------|---------|
| Asana | `asana_client.py` | `scanners/asana_scanner.py` |
| Toggl | `toggl_client.py` | `scanners/toggl_scanner.py` |
| Google (Drive/Gmail/Calendar/Contacts) | `google_client.py` | `scanners/contacts_scanner.py`, `email_scanner.py`, `drive_scanner.py` |
| Slack | `slack_data_client.py` | `scanners/slack_scanner.py` |

## User Identity
- `user_map.py` builds unified user directory matching across Slack, Asana, and Toggl
- Requires all 3 IDs for inclusion; supports manual overrides via `USER_MAP_OVERRIDES` env var
- Email domain: `blackswifttech.com`

## Knowledge Files
- Stored in `knowledge/` directory, committed to git
- Scans run locally, not on Railway (Railway filesystem is ephemeral)
- Update workflow: `python scan.py all --mode incremental && git add knowledge/ && git commit && git push`

## Environment Variables
See `.env.example` for required variables. Key ones:
- `ANTHROPIC_API_KEY` - Claude API
- `ASANA_ACCESS_TOKEN` - Asana personal access token
- `SLACK_BOT_TOKEN` / `SLACK_SIGNING_SECRET` - Slack Bolt
- `TOGGL_API_TOKEN` / `TOGGL_WORKSPACE_ID` - Toggl
- `GOOGLE_SERVICE_ACCOUNT_JSON` - Base64-encoded service account key (domain-wide delegation)
- `KNOWLEDGE_CHANNEL` - Slack channel ID used as persistent knowledge store
- `DAILY_TASKS_CHANNEL` - Where daily briefings are posted
- `SLACK_MONITORED_CHANNELS` - Comma-separated channel IDs to scan

## Deployment
- Railway auto-deploys from `master` branch
- `Procfile`: `web: gunicorn app:flask_app --bind 0.0.0.0:${PORT:-8080}`
- Knowledge files deploy with the code via git

## Models Used
- Daily synthesis: `claude-sonnet-4-20250514` (8000 max tokens)
- Knowledge distillation: `claude-haiku-4-5-20251001` (cost-efficient for bulk processing)
- Q&A: `claude-sonnet-4-20250514`
- Personality chat: `claude-sonnet-4-20250514` (300 max tokens)
