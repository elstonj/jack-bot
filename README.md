# Jack Bot

AI-powered project management assistant for Black Swift Technologies. Synthesizes data from Asana, Toggl, Google Workspace, and Slack into prioritized daily briefings and answers questions about projects, contacts, and team activity.

## Features

- **Daily Briefings** — Prioritized task summaries posted to Slack at 8am MT, personalized per team member
- **Knowledge Q&A** — Ask questions about projects, contacts, budgets, time tracking, and more via Slack
- **Corrections** — Team members can correct priorities with `correct: <feedback>` and the bot learns
- **Knowledge Base** — 161 distilled files covering Asana projects, Toggl time tracking, Google contacts, Slack channel histories, email patterns, and shared drive contents
- **Incremental Updates** — Knowledge files updated with only new data since last scan

## Quick Start

```bash
# Install dependencies
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API keys

# Run locally
python app.py
```

## Knowledge Scanning

Deep historical scans distill data from all connected sources into markdown knowledge files:

```bash
# Full scan of a source (all historical data)
python scan.py asana --mode full
python scan.py toggl --mode full
python scan.py contacts --mode full
python scan.py slack --mode full
python scan.py email --mode full
python scan.py drive --mode full

# Scan everything
python scan.py all --mode full

# Last year only
python scan.py all --mode 1yr

# Only changes since last scan
python scan.py all --mode incremental
```

Knowledge files are stored in `knowledge/` and committed to git for deployment.

## Slack Commands

| Command | Description |
|---------|-------------|
| `tasks` or `tasks all` | Show today's prioritized task briefing |
| `correct: <feedback>` | Submit a correction to task prioritization |
| `note: <info>` | Store a note in the knowledge base |
| `weather` | Flying site weather conditions |
| `/refresh-tasks` | Manually trigger the daily pipeline |
| Any question | Ask about projects, contacts, budgets, etc. |

## Architecture

```
app.py                  Slack Bolt server, event handlers, Flask routes
daily_research.py       Core pipeline: knowledge + live data -> Claude synthesis
knowledge_qa.py         Q&A: routes questions to relevant knowledge files
knowledge.py            Slack channel as persistent knowledge store
scan.py                 CLI for deep historical data scanning
scanners/               Per-source scanners (Asana, Toggl, Slack, Email, Drive, Contacts)
knowledge/              Distilled markdown knowledge files (161 files, ~850KB)
  asana/projects/       Per-project summaries (65 files)
  toggl/                Time tracking by person (24) and project (34)
  contacts/             BST directory + 8,220 external contacts
  slack/                Per-channel history summaries (19 channels)
  email/                Per-person email patterns (12 people)
  drive/                Shared drive contents (Federal Projects + Sales)
```

## Data Sources

- **Asana** — Tasks, projects, milestones, BD pipeline, proposals, dollar amounts
- **Toggl** — Time tracking by person and project
- **Google Drive** — Sales and Federal Projects shared drives
- **Gmail** — Email metadata (subjects, senders, recipients)
- **Google Calendar** — Today's meetings and attendees
- **Google Contacts** — Team directory and external contacts
- **Slack** — Channel histories and real-time messages

## Deployment

Deployed on Railway. Auto-deploys from `master` branch.

```
Procfile: web: gunicorn app:flask_app --bind 0.0.0.0:${PORT:-8080}
```

Knowledge files are part of the repo and deploy with the code. Scans run locally; push updated knowledge files via git.
