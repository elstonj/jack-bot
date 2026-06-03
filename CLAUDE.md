# Jack Bot - Development Guide

## Project Overview
Jack Bot is an AI-powered project management assistant for Black Swift Technologies (BST). It synthesizes data from Asana, Toggl, Google Workspace, Slack, and Rippling into prioritized daily briefings posted to Slack, and answers ad-hoc questions about projects, contacts, finances, and team activity.

## Vision & Build Order
Jack Bot is meant to **replace the head of operations and project managers** at BST — keep projects on time and under budget without a human in the loop. The daily briefing is one small read-only feature; the broader goal is budget Q&A, autonomous Asana hygiene from email/Slack evidence, interim-report composition, and eventual invoice generation (cost-reimbursable + fixed-cost milestone). Committed build order: (1) structured project-state model + spend-to-budget reconciliation, (2) auto-propose Asana closures from evidence, (3) proactive observer daemon posting a PM-only digest, (4) report composer, (5) contract-terms parsing + invoicing. Prefer changes that unlock multiple phases over single-use features.

## Architecture

### Core Pipeline (`daily_research.py`)
- Runs daily at 8am MT weekdays via APScheduler (`scheduler.py`)
- Reads pre-distilled knowledge files for historical context
- Fetches live data: today's calendar, last workday's Toggl, 24h email/Slack
- Detects OOO via Rippling PTO calendar (ICS feed)
- ALL employees in the user map get a section — not just those with Asana tasks
- Claude synthesizes top 3 AI-interpreted priorities per person from all sources
- Detects completed tasks via email/Slack/Drive signals; suggests closing in Asana
- OOO users get a palm tree note instead of tasks
- Synthesis prompt treats CORRECTION / FEEDBACK entries as absolute: if a correction says a task is done / handled externally, it's excluded from both the team summary and per-person priorities even when stale knowledge files still list it as overdue
- `_sync_operations_feedback()` mirrors non-bot replies in #operations into `[FEEDBACK]` entries each run (dedup by Slack `ts`), so feedback persists even if the `message.channels` event isn't reaching the bot
- Operations-channel history passed to Claude is sliced `[-30:]` (newest messages), not `[:30]`
- Missing-section guard (after `_parse_per_user`): compares parsed slack IDs against every mapped team member; if any are missing, logs a `[DEBUG]` entry, runs a targeted Sonnet retry for just those people, and falls back to a visible `:warning:` placeholder section so no one is silently dropped downstream

### Knowledge Layer (`knowledge/`, `scanners/`, `scan.py`)
- ~200+ distilled markdown files covering 11 data sources
- `scan.py` CLI: `python scan.py <source> --mode full|1yr|incremental`
- Scanners: asana, toggl, contacts, slack, email, drive, proposals, budgets, quickbooks, financial, projects
- Knowledge files are committed to git and deployed via Railway
- Scan state tracked in `knowledge/.scan_state.json`

### Q&A System (`knowledge_qa.py`)
- Routes questions to relevant knowledge files via keyword matching
- Includes recent knowledge channel entries (corrections, feedback, insights)
- Searches project registry files for company/contact lookups
- **Live API fallback**: if knowledge files can't answer, Claude Haiku plans which live sources to search (Gmail, Slack, Calendar, Asana), executes the searches, then Claude Sonnet re-answers with the combined context
- Triggered by questions in @mentions or DMs (contains `?`, question words, or `ask:` prefix)
- `answer_question()` accepts `user_id` and resolves it via `user_map.get_user_by_slack_id()` (fallback `users_info`). An `ASKER:` block is injected into the prompt so first-person pronouns ("do *I* have tasks today") bind to the right person; the system prompt forbids addressing the asker by any other name

### Slack Integration (`app.py`)
- Slack Bolt app with Flask adapter for Railway
- Unified `route_message()` handles all natural language commands
- Commands: `help`, `tasks`, `finances`, `company finances`, `bug:`, `feature:`, `bugs`, `features`, `correct:`, `note:`, `weather`
- Weather intent is matched on more than `startswith("weather")` — `is_weather_intent()` catches natural-language variants (e.g. "wind at the sod farm", "can we fly at BMA") and `match_sites()` filters to a specific site when one is named. Site aliases are configured in `weather.py` `SITE_ALIASES`
- `handle_mention()` only strips the leading bot mention; embedded `@user` mentions in commands like `correct: @Joshua has time tracked` are preserved. The strip regex accepts both `<@U…>` and the pipe form `<@U…|Display Name>` Slack delivers in some contexts
- Teaching moments auto-detected ("KS = Krateo Sky", "FYI...", "X stands for Y") and stored as knowledge
- Routing order inside `route_message()` (after pending-proposal check): help → weather → tasks → company finances → finances → purchase check → bug/feature/note/correct → teaching → **task-update intent** → **(in #commercial-sales) commercial-sales update intent** → **(in #commercial-sales) commercial-sales inquiry intent** → question → personality fallback
- Questions route to knowledge Q&A with live search fallback
- Non-questions route to personality chat
- Replies in #operations (daily tasks channel) stored as implicit feedback (via real-time event + pipeline-time sync fallback)
- Explicit commands in #operations (correct:, bug:, etc.) route normally
- Admin only: `/refresh-tasks` (in #jackbot-knowledge)

### Channel Context (`channel_context.py`)
- `get_channel_context(client, channel_id)` is the unified entry point every bot-addressed message runs through
- Returns `{channel_name, topic, purpose, project_code, project_gid, project_name, project_summary, project_file, financial_file, recent_messages, is_dm}`
- 5-min TTL in-memory cache per channel (name + project metadata); `recent_messages` is refreshed on every call since conversations move fast
- DMs (channel_id starting with `D`) skip the `conversations_info` call — no channel name, no project, but recent messages still fetched
- Project resolution order: explicit `channel_projects.md` mapping → regex project code in channel name/topic/purpose → fuzzy channel-name match against `knowledge/projects/*.md` headers
- `project_gid` is extracted by parsing the Asana URL (`app.asana.com/.../project/<gid>`) out of the project registry file — powers the live Asana task fetch in Q&A and the task-update agent
- Channel name + project info is injected into personality prompts (skipped for DMs) and the Q&A prompt, along with ~10 recent messages — so "pushing the flight test back" in `#usgs-volcano` resolves to project 350_4 with context
- Q&A live search force-adds `asana` to the plan whenever a project is identified and calls `asana_client.get_tasks_for_project(project_gid)` directly (not just workspace text search)

### Task-Update Agent (`task_actions.py`)
- Conversational propose-and-confirm flow for modifying Asana tasks from a project channel — never writes without explicit user confirmation
- Intent matched by `is_task_update_intent()` (regex over "update tasks", "shift/push/move due", "reschedule", "mark complete", "reassign", "assign X to", etc.)
- Supported fields: `due_on`, `due_at`, `assignee`, `completed`
- Flow:
  1. `propose_task_updates()` fetches the project's open tasks, feeds them + the question + ~10 recent channel messages to Claude Sonnet, which returns structured JSON with either `clarifying_questions` or `proposed_changes`
  2. Proposals stashed in `PENDING` dict keyed by `(user_id, channel_id)` with a 10-min TTL; numbered list posted to Slack
  3. `apply_task_updates()` parses the user's next reply via Claude Haiku into `accept_all` / `accept_subset` / `reject` / `modify` / `unrelated`. `unrelated` falls through to normal routing
  4. On accept, calls `asana_client.update_task(gid, updates)`; on modify, re-runs the propose call with the modification instruction; on reject, clears pending
- Assignee names → Asana gids resolved via `user_map.get_all_users()` (exact then token-subset match)
- Propose prompt gets an `ASKER:` block (resolved from `user_id` via user_map) so "my tasks" / "push my due dates" bind to the requester rather than being inferred from context
- Every successful write is logged as a `[FEEDBACK]` entry in the knowledge channel for audit trail
- State is in-memory — lost on Railway restart (acceptable; proposals are short-lived)
- Safety gate: no task-update flow without a project resolved from the channel

### Commercial Sales Pipeline (`commercial_sales.py`, `commercial_sales_inquiry.py`, `commercial_sales_reply.py`, `commercial_sales_admin.py`, `scanners/commercial_sales_scanner.py`)
- Tracks customer orders (`Build`) and repairs (`SupportCase`) for BST's commercial side. Two parallel state machines per Build (payment / build / ship) plus one for SupportCase. Persisted as JSON under `knowledge/commercial_sales/{builds,support}/`. Anchor: Asana gid (Build) or `SC-YYYY-NNN` (SupportCase).
- **Morning digest** — `scheduler.py::post_commercial_sales_digest` runs at 8:02am Mon-Fri, loads JSONs only (no LLM at post-time). Posts **two umbrella threads** to `#commercial-sales` — **"Active Orders — <date>"** and **"Customer Leads — <date>"** — each a top-level header with its cards threaded beneath (so leads and committed orders stay visually separate). `commercial_sales.py::is_order(b)` is the split: an *Active Order* = PO issued / invoice sent / paid, OR any build/ship work started; everything earlier (estimate-only) is a *Lead*. Support cases thread under Active Orders. The render is a flat `sequence` of entries; every `kind=="header"` entry starts a new top-level message and the scheduler threads subsequent cards/dividers/footer beneath it. Cards still carry owner pings, state, contents, parts checklist, and missing-info callouts routing each gap to its responsible owner (Beck/Meredith/Nate per `BUILD_FIELD_ROLES` in `commercial_sales.py`). The scheduler writes `_message_map.json` with `umbrella_ts` (first header, back-compat), `umbrellas: [...]` (every header ts), an ordered `cards: [{ts, kind, id, customer, label}]` list (global across both threads), and a flat `messages: {ts → {kind, id}}` map (used for both per-card direct lookup and content-match routing in the reply handler).
- **Formal-proposal exclusion** — the commercial-sales scanner's `BUILD_EXTRACTION_PROMPT` STEP 0B drops formal funding-proposal/solicitation bids (SBIR/STTR/BAA/RFP/RFI/LOI/white-paper/IDIQ competitive bids) even when there's recent activity — these belong in `#grants-and-funding` (no digest built for that channel yet). Commercial hardware procurement is kept even when the customer is federal or grant-funded (PO, RFQ/quote for a specific aircraft/sensor, hardware invoice). The test: *selling a product/system* (keep) vs *bidding to win a funded R&D effort* (drop). Note: a **funded demo** (e.g. the NexTech / Canadian Rangers "S3 Canada" demo — selling/demonstrating an S3 system) is commercial and stays in the digest; it is *not* the same as the SBIR-funded Aug magnetometer demo (25.1 SBIR Phase II, project `550_1`), which is an R&D effort and belongs in `#grants-and-funding`.
- **Filter** — `_is_active_build(b)` keeps a build on the digest until BOTH delivery and payment are confirmed: `not (ship_state=="delivered" and payment_state=="paid")`. There is **no** time-based fallback — an unpaid *delivered* build stays visible (with a "still on digest: awaiting payment" callout via `_why_still_active`) so an "is this done?" card never silently disappears. A record only drops off the active list once it's both `ship_state="delivered"` **and** `payment_state="paid"`.
- **Thread replies** (`commercial_sales_reply.py`) — Slack threads are flat, so a user "replying in thread" to any of the day's cards actually lands the reply directly under the umbrella header. `lookup_record_for_thread` resolves the target with a 3-tier fallback: (1) per-card direct match if the reply's `thread_ts` happens to be a card's `ts` (legacy threads from older digests, before umbrella threading), (2) **umbrella content-match** — when `thread_ts` is one of the day's umbrella parents (`thread_ts in umbrellas` — either the Active Orders or Customer Leads header), Haiku via `UMBRELLA_MATCH_SYSTEM` picks the best card from the day's full list by customer/product mention; low-confidence matches return None and the bot stays silent rather than guessing, (3) parse the hidden `build:<gid>` / `case:<id>` token out of the parent message text when the JSON map is gone (Railway redeploy). Once a record is resolved, Haiku via `PARSE_REPLY_SYSTEM` extracts structured `{field, value}` updates. Prompt explicitly enumerates enum values and maps common phrases (e.g. "this is done / completed / shipped" on a Build → emit `ship_state=delivered + shipped_date=today + build_state=complete`). Without the synonyms, "this has been completed" used to set `ship_state="completed"` (invalid) and reject the whole update. Validated updates are then **partitioned** (`_is_safe_fact`): plain factual fields — `SAFE_FACT_FIELDS_BUILD`/`SAFE_FACT_FIELDS_CASE` (invoice #/amount/date, tracking, carrier, ship_to, contact, dates, notes, …) — are **applied immediately** via `_commit_updates` with a "✓ Recorded — reply *undo* to revert" message; state-machine fields (`payment_state`/`build_state`/`ship_state`/case `state`), list fields (`items`/`parts`), and `owners` still go through propose-and-confirm. A mixed reply does both (facts land now, the state change waits for *yes*). This fixes the silent-drop class: corrections like Meredith's "Invoice 1766 for $3,900" or "delivered in person in Boulder" used to sit as an unconfirmed proposal in the 10-min in-memory `PENDING` dict and evaporate (nobody replies "yes", and it's wiped on Railway redeploy). The auto-apply path stashes a `STATE_AUTO_APPLIED` pending entry holding an `undo` buffer (prior flat-field values); a follow-up `undo` reverts via `_revert_updates`, and any *non-undo* follow-up is reprocessed as a fresh correction (`handle_thread_reply`) rather than dropped. The propose-and-confirm accept path shares `_commit_updates` (load → apply → save → Asana audit comment + `[FEEDBACK]`).
- **Pending state in the umbrella thread** — keyed on `(thread_ts, user_id)` so concurrent proposals by different users in the same umbrella thread don't collide (Beck can propose an ERAU update while Meredith proposes a NASA update). This replaces the older cross-user-confirm pattern; each proposer now confirms their own.
- **Tolerant JSON parsing** — `_loads_tolerant` in both `commercial_sales_reply.py` and `commercial_sales_inquiry.py` finds the first balanced `{...}` block in Haiku's response, so trailing prose doesn't kill the whole update with `JSONDecodeError: Extra data`. This bug previously surfaced as a visible "couldn't parse that update" reply in the channel.
- **Top-level inquiry** (`commercial_sales_inquiry.py::handle_inquiry`) — `#commercial-sales` messages asking about shipping/address/parts/POC/payment/serial/RMA/status (`is_inquiry_intent`) route here instead of falling through to `is_work_update`. Three branches:
  1. **No match** → *first* try the general knowledge layer (`_try_general_knowledge_answer`): the inquiry handler searches `financial/by_project`, `budgets`, and `projects` for the customer/product hints (Slack mentions + owner names stripped from the hint tokens so they don't match the whole corpus), and if a documented order is found, answers from it via Haiku AND auto-stubs a seeded Build (carrying `project_code` + `source_files`) so the scanner promotes it. This is the fix for the Stanford/Acellent case — project 042-1 is documented in financials/budgets but lives in its own Asana project + personal mailboxes, so the commercial-sales scanner never built a record and the bot used to answer "I don't have a record." Only if the general-knowledge search comes up empty does it fall back to → ask for customer + product + ship date, stub a placeholder JSON under `knowledge/commercial_sales/builds/_stubs/`, log `[KNOWLEDGE_GAP]` (`record=unmatched`).
  2. **Match + field has value** → answer directly.
  3. **Match + field empty** → @-ping the right owner via `BUILD_FIELD_ROLES` / `SUPPORT_FIELD_ROLES`, log `[KNOWLEDGE_GAP]` with the specific field + record id.
- **Top-level updates** (`commercial_sales_inquiry.py::handle_update_propose`) — `#commercial-sales` messages with action verbs (`is_update_intent`: "add X as owner to Y", "mark Z complete", "set ship_to for W to ...", "tracking 1Z999... for V", and implicit-items phrasings like "the NASA S2 simulator includes X, Y, Z" / "S3 comes with EO/IR gimbal") route here. Haiku via `UPDATE_PARSE_SYSTEM` extracts `(target, field, value)` tuples, supports multi-target ("to A and B"), defaults `add … as owner` without a role to `interface`. Each target is resolved via the same `_match_record` matcher as the inquiry flow, validated via `commercial_sales_reply._validate_update`, then proposed with before→after diffs for owner edits. On accept, applies + saves + logs `[FEEDBACK]` for audit.
- **Pending state** is in-memory (lost on Railway restart, acceptable). The `commercial_sales_inquiry.PENDING` dict is keyed on `(user_id, channel_id)` with `kind ∈ {"inquiry", "update_proposal"}`. The unified `has_pending` + `handle_followup` dispatcher in that module is the single entry point `app.py` calls before normal intent routing.
- **Admin commands** (`commercial_sales_admin.py`) — `show filtered` lists records the scanner dropped, `track this: <ref>` force-includes one from the filtered list, `create task for: <customer>` drafts a BD Pipeline Asana task. All propose-and-confirm.
- **Phase 1 scanner** — `python scan.py commercial_sales --mode incremental` walks Asana commercial-sales tasks + impersonates `info@`/`sales@`/`support@` via the service account + reads `#commercial-sales` and runs Haiku per-record to update JSONs. The `_filtered.md` + `_unmapped_customers.md` files surface what didn't fit.
- **Discovery source #2 — documented orders** (`_discover_documented_orders`, scanner step 4b) — promotes orders that never entered the Commercial Sales Asana project. Two inputs, both synthesizing a pseudo-Asana-task and running the SAME `_haiku_extract_build` (so STEP 0B funding-proposal filtering + the is_customer_build gate still apply, and is_active/is_order/state-inference keep dormant historical sales out of the digest): **(a)** promotes `_stubs/*.json` written by the inquiry handler (unconditional — the inquiry is the live signal; the stub is consumed/deleted unless Haiku transiently fails); **(b)** sweeps `financial/by_project` for projects whose "Contract Type" reads as commercial-equipment (`_is_commercial_equipment_contract`), **gated on recent Slack/email token activity** so years-old completed sales aren't resurrected, and skipping codes already referenced by a tracked Build (`_tracked_project_codes`). Discovered Builds are keyed on a synthetic gid `proj-<code>` (or `doc-<slug>`); `_post_asana_comment` just no-ops on these. Note: stub *promotion* itself was previously missing entirely — stubs were written but nothing consumed them.

### Financial System (`finances.py`)
- `finances` in a project channel looks up financial data via:
  1. Channel-to-project mapping (`knowledge/channel_projects.md`)
  2. Project codes in channel name/topic/purpose
  3. Channel name matching against project registry files
- Raw financial markdown is summarized by Claude Haiku into clean Slack-formatted output
- `company finances` returns the company-wide overview
- Channel mapping auto-generated by project registry scanner, with manual overrides preserved

### Project Registry (`scanners/project_registry_scanner.py`)
- `python scan.py projects` — fetches all Asana project overviews
- Extracts custom fields: budget, customer, contacts, contract type, period of performance
- Cross-references with Slack channels and financial knowledge files
- Produces per-project files (`knowledge/projects/{code}.md`) and master registry
- Auto-generates `channel_projects.md` for the finances command
- `MANUAL_CHANNEL_HINTS` dict handles non-obvious channel-to-project associations

### Personality (`personality.py`)
- "Jack Bot" - bitter old-school Unix programmer persona
- Used for non-question, non-command conversational messages
- Accepts a `channel_context` kwarg; when present and not a DM, appends a CONTEXT block to the system prompt so Jack can reference the channel and resolved project naturally ("#usgs-volcano... project [350_4] 2024 USGS - Chile (Mexico)")

### Bug & Feature Tracking (`knowledge.py`)
- `[BUG]` and `[FEATURE]` knowledge entry types stored in Slack knowledge channel
- `bug:` / `feature:` to log; `bugs` / `features` to list
- Persists across deploys via Slack channel storage

### Knowledge Entry Types (`knowledge.py`)
The knowledge channel is the persistent store for everything that needs to survive a Railway redeploy. Each entry is `*[TYPE]*\n<content>`. Types: `PRIORITY`, `PROJECT`, `CLIENT`, `DELIVERABLE`, `TEAM`, `CORRECTION`, `FEEDBACK`, `INSIGHT`, `SOURCE`, `BUG`, `FEATURE`, `ERROR`, `SNAPSHOT`, `DEBUG`, `KNOWLEDGE_GAP`.
- `[KNOWLEDGE_GAP]` is written by the commercial-sales inquiry handler whenever it can't fully answer — either `record=unmatched` (no Build/SupportCase resolved) or `field=<name> record=<gid>` (record matched but the field is empty). Body format: `field=… record=… asker=… inquiry=…`. These accumulate as the to-do list for tightening scanners — repeated misses on the same field tell you where the scanner needs more reach (PDF parsing, additional email regex, etc.).

## Key Data Sources
| Source | Client | Scanner |
|--------|--------|---------|
| Asana | `asana_client.py` | `scanners/asana_scanner.py` |
| Toggl | `toggl_client.py` | `scanners/toggl_scanner.py` |
| Google (Drive/Gmail/Calendar/Contacts) | `google_client.py` | `scanners/contacts_scanner.py`, `email_scanner.py`, `drive_scanner.py` |
| Slack | `slack_data_client.py` | `scanners/slack_scanner.py` |
| Proposals & Reports | `google_client.py` | `scanners/proposals_scanner.py` |
| Budgets | `google_client.py` | `scanners/budget_scanner.py` |
| QuickBooks | `scanners/quickbooks_scanner.py` | `scanners/quickbooks_scanner.py` |
| Financial Index | — | `scanners/financial_index.py` |
| Project Registry | `asana_client.py` | `scanners/project_registry_scanner.py` |
| Rippling PTO | Direct ICS fetch | — (fetched live in `daily_research.py`) |

## User Identity
- `user_map.py` builds unified user directory matching across Slack, Asana, and Toggl
- Requires all 3 IDs for inclusion; supports manual overrides via `USER_MAP_OVERRIDES` env var
- Fuzzy matching by email alias and last name; first-name guard prevents false merges
- Hard-coded exclusions for non-employees (tiffany.elston, todd.elston, jameel.barkat)
- Employee roster sanity check: compares user map against `knowledge/contacts/employees.md`
- Email domain: `blackswifttech.com` (and `blackswifttechnologies.com` equivalent)

## Knowledge Files
- Stored in `knowledge/` directory, committed to git
- `employees.md` is the canonical employee roster — pipeline uses this to ensure full coverage
- `channel_projects.md` maps Slack channels to project codes (auto-generated + manual overrides)
- Scans run locally, not on Railway (Railway filesystem is ephemeral)
- Update workflow: `python scan.py all --mode incremental && git add knowledge/ && git commit && git push`

## Environment Variables
See `.env.example` for required variables. Key ones:
- `ANTHROPIC_API_KEY` - Claude API
- `ASANA_ACCESS_TOKEN` - Asana personal access token
- `SLACK_BOT_TOKEN` / `SLACK_SIGNING_SECRET` - Slack Bolt
- `TOGGL_API_TOKEN` / `TOGGL_WORKSPACE_ID` - Toggl
- `GOOGLE_SERVICE_ACCOUNT_JSON` - Base64-encoded service account key (domain-wide delegation)
- `GOOGLE_ADMIN_EMAIL` - Email for Gmail search fallback (default: elstonj@blackswifttech.com)
- `KNOWLEDGE_CHANNEL` - Slack channel ID used as persistent knowledge store
- `DAILY_TASKS_CHANNEL` - Where daily briefings are posted (#operations)
- `SLACK_MONITORED_CHANNELS` - Comma-separated channel IDs to scan

## Deployment
- Railway auto-deploys from `master` branch
- `Procfile`: `web: gunicorn app:flask_app --bind 0.0.0.0:${PORT:-8080}`
- Knowledge files deploy with the code via git

## Local Testing
- `python test_pipeline.py` — runs the full daily pipeline end-to-end with live Asana/Toggl/Google/Slack reads, but intercepts every Slack write (no posts to #operations, no knowledge-channel entries). Prints the team summary and per-user sections to stdout
- `--verbose` echoes the suppressed writes so you can see what *would* have been posted (DEBUG, FEEDBACK, etc.)
- `--full` appends Claude's raw pre-parse output
- `python test_commercial_sales.py` — dry-run the commercial-sales digest render against current JSONs; `--scan` refreshes the JSONs first
- `python test_commercial_sales_inquiry.py` — exercises `is_inquiry_intent`, `is_update_intent`, the no-match / matched-field / empty-field inquiry branches, and the multi-target update propose flow against live JSONs with intercepted Slack writes. `--verbose` dumps the captured posts (KNOWLEDGE_GAP, FEEDBACK)

## Models Used
- Daily synthesis: `claude-sonnet-4-20250514` (8000 max tokens)
- Knowledge distillation: `claude-haiku-4-5-20251001` (cost-efficient for bulk processing)
- Q&A: `claude-sonnet-4-20250514` (with Haiku for search planning)
- Financial formatting: `claude-haiku-4-5-20251001` (converts markdown to Slack format)
- Personality chat: `claude-sonnet-4-20250514` (300 max tokens)

## OOO Detection
- Uses Rippling PTO calendar ICS feed (URL hardcoded in `daily_research.py`)
- Fetches live on each pipeline run; checks for events covering today
- Parses `SUMMARY: [Name] on [Type]` with `DTSTART`/`DTEND` date ranges
- Matches ICS names to user map by first/last name fuzzy matching

## Toggl Time Tracking
- `_last_workday()` returns the most recent Mon-Fri day (Friday on Monday, etc.)
- Prevents "no time tracked" false alarms on weekends and Mondays
