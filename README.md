# Jack Bot

AI-powered project management assistant for Black Swift Technologies. Synthesizes data from Asana, Toggl, Google Workspace, Slack, and Rippling into prioritized daily briefings and answers questions about projects, contacts, finances, and team activity.

## Features

- **Daily Briefings** — AI-synthesized top 3 priorities per person from ALL data sources (not just Asana), posted to Slack at 8am MT weekdays
- **OOO Detection** — Pulls PTO/sick leave from Rippling calendar; OOO team members get a palm tree instead of tasks
- **Completed Task Detection** — Cross-references email/Slack/Drive to spot tasks that look done and suggests closing them in Asana
- **Knowledge Q&A** — Ask questions naturally; searches knowledge files first, then falls back to live API search (Gmail, Slack, Calendar, Asana)
- **Financial Summaries** — Say `finances` in a project channel for a clean budget/invoice summary
- **Bug & Feature Tracking** — `bug:` and `feature:` to log items; `bugs` and `features` to list them
- **Implicit Learning** — Any reply in the daily tasks channel is stored as feedback; teaching moments like "KS = Krateo Sky" are auto-detected and stored
- **Project Registry** — Unified mapping of all projects to Asana, Slack channels, financial data, and contacts
- **Personality** — Grumpy old-school Unix programmer persona for non-work chat

## Quick Start

```bash
python -m venv venv
source venv/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API keys
python app.py
```

## Slack Commands

All commands work via @mention or DM (no slash commands needed):

| Command | Description |
|---------|-------------|
| `help` | List all available commands |
| `tasks` / `tasks all` | Your prioritized tasks / full team briefing |
| `finances` | Project financial summary (in a project channel) |
| `company finances` | Company-wide financial overview |
| `bug: <description>` | Report a bug |
| `feature: <description>` | Request a feature |
| `bugs` / `features` | List open bugs or feature requests |
| `correct: <feedback>` | Correct task priorities |
| `note: <info>` | Teach the bot something |
| `weather` | Flying site conditions |
| Any question | Searches knowledge base + live APIs |

Admin only: `/refresh-tasks` (in #jackbot-knowledge)

## Knowledge Scanning

```bash
# Scan everything (incremental — only changes since last scan)
python scan.py all --mode incremental

# Individual sources
python scan.py asana --mode full
python scan.py toggl --mode full
python scan.py contacts --mode full
python scan.py slack --mode 1yr
python scan.py email --mode 1yr
python scan.py drive --mode full
python scan.py proposals --mode full
python scan.py budgets --mode full
python scan.py quickbooks --mode full
python scan.py financial              # Cross-references budgets + QB + Asana
python scan.py projects               # Project registry from Asana overviews

# Update workflow
python scan.py all --mode incremental && git add knowledge/ && git commit && git push
```

## Architecture

```
app.py                  Slack Bolt server, unified message routing
daily_research.py       Core pipeline: knowledge + live data -> Claude synthesis
knowledge_qa.py         Q&A with live API fallback (Gmail, Slack, Calendar, Asana)
knowledge.py            Slack channel as persistent knowledge store
finances.py             Project financial lookups with Claude formatting
personality.py          Jack Bot persona for conversational messages
user_map.py             Unified user directory across Slack/Asana/Toggl
scan.py                 CLI for knowledge scanning
scanners/               Per-source scanners
  asana_scanner.py      Asana projects and tasks
  toggl_scanner.py      Time tracking data
  slack_scanner.py      Channel history
  email_scanner.py      Gmail metadata
  drive_scanner.py      Shared Drive contents
  contacts_scanner.py   Google Contacts
  proposals_scanner.py  Proposals and reports from Drive
  budget_scanner.py     Budget documents from Drive
  quickbooks_scanner.py QuickBooks transactions
  financial_index.py    Cross-referenced financial summaries
  project_registry_scanner.py  Unified project-to-systems mapping
knowledge/              Distilled markdown knowledge files
  asana/projects/       Per-project task summaries
  toggl/                Time tracking by person and project
  contacts/             employees.md (canonical roster) + external contacts
  slack/                Per-channel history summaries
  email/                Per-person email patterns
  drive/                Shared drive contents
  proposals/            Distilled proposals and reports
  budgets/              Per-project budget data from Drive
  quickbooks/           QuickBooks transaction summaries
  financial/            Cross-referenced financial summaries per project
  projects/             Project registry (Asana overview + Slack + financial links)
  channel_projects.md   Slack channel -> project code mapping
```

## Data Sources

| Source | Purpose | Live | Scanned |
|--------|---------|------|---------|
| Asana | Tasks, projects, milestones, BD pipeline, custom fields | Yes | Yes |
| Toggl | Time tracking by person and project | Yes | Yes |
| Google Drive | Sales and Federal Projects shared drives | — | Yes |
| Gmail | Email search (subjects + body snippets in Q&A fallback) | Yes | Yes |
| Google Calendar | Today's meetings and attendees | Yes | — |
| Google Contacts | Team directory and external contacts | — | Yes |
| Slack | Channel messages, real-time activity | Yes | Yes |
| Rippling | PTO/sick leave calendar (ICS feed) | Yes | — |
| QuickBooks | Invoices, expenses, payments | — | Yes |

## Deployment

Deployed on Railway. Auto-deploys from `master` branch.

```
Procfile: web: gunicorn app:flask_app --bind 0.0.0.0:${PORT:-8080}
```

Knowledge files are part of the repo and deploy with the code. Scans run locally; push updated knowledge files via git.
