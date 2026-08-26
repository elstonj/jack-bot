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
- **Identity is deterministic, not model-inferred.** Sonnet returns a forced tool call (`BRIEFING_TOOL` / `submit_daily_briefing`) containing `{team_summary: [...], sections: [{person, priorities, notes}]}`. `person` is a **canonical name** from a closed list — the model never sees or writes Slack IDs. `_assemble_sections()` maps name → Slack ID via `user_map` and writes the `*<@ID>*` header itself. This replaced the old free-form output where Claude hand-copied 11-char Slack IDs into headers and `_parse_per_user` trusted them blindly — the root cause of the 2026-08-05 failure where Jack Elston's whole section was emitted a second time under Joshua Fromm's mention (and of the same bug on 2026-04-23)
- **Calendar and hours lines are rendered in code**, never by the model — `_calendar_line()` from `TODAY'S CALENDAR` records and `_hours_line()` from the Toggl summary (summing all of a user's toggl IDs). The prompt explicitly forbids the model from listing meetings or hours. This kills the hallucinated-meeting class outright and makes a duplicated section impossible to disguise
- The prompt forbidding the model from writing its own hours/calendar line is not enough — it echoed the `No time tracked yesterday:` roster out of the TIME TRACKING block as a priority/note, so every section carried that fact twice (2026-08-07). `_restates_generated_line()` now drops any model line that restates a generated one — leading `:clock1:`/`:calendar:`/`:stopwatch:` emoji, "no time tracked/logged", or an hours figure paired with tracking language ("tag yesterday's 16.0h (all uncategorized)"). Filtering happens *before* the top-3 slice in `_render_section()`, so dropping an echoed line promotes a real priority rather than leaving a gap
- **Toggl project attribution**: the v3 summary report identifies each sub-group by project **`id`** and sends **no `title` key**. `get_time_summary()` read `sub_group.get("title", "No project")`, so every entry fell back to the literal `"No project"` label — and because it *assigned* rather than accumulated, each user's `projects` dict collapsed to one key holding only the last sub-group's hours. `_hours_line()` counts that label as unassigned, so the whole team read as "all unassigned — flag for project tagging" while actually being fully tagged (Ben Busby's 16.0h was 100% on `[001-14] SwiftCore 3.3`). Fixed by resolving ids via `get_toggl_projects()` and summing per name; an unresolvable id renders as `Project <id>`, never `No project`, so a lookup failure can't masquerade as untagged time. `toggl_client.NO_PROJECT` is the single label `daily_research._NO_PROJECT_LABELS` treats as unassigned. `scanners/toggl_scanner.py` keys by `proj_id` and was never affected
- **Three-layer validation** before anything is posted:
  1. `_validate_sections()` — resolves each `person` through `user_map.resolve_person()` (unknown/ambiguous → dropped, never guessed), rejects duplicates **keeping the first** (a later stub can no longer clobber a real section — that's how Alex Lomis lost his priorities), and rejects stub/cross-reference bodies (`_is_stub_priorities`: "already covered above", "see below", <25 chars)
  2. `_find_copied_sections()` — flags two people whose priority bodies are ≥90% identical (difflib) as a mis-assignment and drops the copy for regeneration. This is the check the old ID-keyed guard structurally could not perform
  3. Missing-person guard — checks *content*, not key presence: `[n for n in active_names if n not in accepted]`. Runs one targeted structured retry for just those people, re-runs the contamination check on the merged result, then falls back to a visible `:warning:` placeholder. A visible gap always beats a wrong assignment
- All validation issues are logged as one `[DEBUG]` entry; a second `[DEBUG]` lists `name (slack_id): first priority` per person so a mis-assignment is visible at a glance in the knowledge channel
- `_scrub_bot_identity()` rewrites "Jack Bot" and the bot's own `<@Uxxx>` mention to "the assistant" in the ops history and Slack messages fed to synthesis, so "Jack" in the prompt only ever means Jack Elston
- Offline regression coverage: `python test_identity.py` (no credentials needed) replays the 2026-08-05 failure through the validators and asserts the rendering/assembly contract
- **Posting shape** — `scheduler.py::post_team_summary(client, channel)` is the single post path (used by both the 8am job and `/refresh-tasks`). The team summary is the only message in #operations' main view; each person's top-3 section is a *separate threaded reply* beneath it (ordered by display name via `user_map`), with the DM footer as the last reply — same umbrella-thread pattern as the purchasing summary and commercial-sales digest. Sections are still cached, so DM `tasks` is unchanged; a failed individual post is swallowed so one bad section can't sink the rest of the thread

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
- Routing order inside `route_message()` (after pending-proposal check): help → weather → tasks → company finances → finances → purchase check → bug/feature/note/correct → teaching → **provenance** → **(in #commercial-sales) commercial-sales update intent** → **(in #commercial-sales) commercial-sales inquiry intent** → **task-update intent** → question → personality fallback. The commercial-sales branches are checked *before* the generic task-update intent so an `@mentioned` "mark ERAU complete" in #commercial-sales hits the CS handler rather than `is_task_update_intent` (which resolves no `project_gid` in that channel and would fall to Q&A)
- **#commercial-sales requires an @mention to initiate a reply.** Jack only *starts* a commercial-sales inquiry/update from an `@mention` (routed through `handle_mention`→`route_message`). The `handle_dm` top-level #commercial-sales block no longer fires `is_inquiry_intent`/`is_update_intent` on undirected human-to-human discussion — that ambient behavior made Jack butt into conversations ("I matched this to UMES… but I'm not sure what you're asking"). That block now handles only explicit typed admin commands (`show filtered`, `track this:`, `create task for:`) and follow-ups to a proposal Jack already started (pending-state continuations, no @mention needed). Digest **thread replies** (the reply-to-update capture flow) are unchanged
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
- **Filter** — `_is_active_build(b)` keeps a build on the digest until BOTH fulfillment and payment are confirmed: `not (_is_fulfilled(b) and payment_state=="paid")`. **Fulfillment** (`_is_fulfilled`) is `ship_state=="delivered"` for shipped goods **OR** `build_state=="complete"` for no-ship work — repairs/services never enter the ship pipeline (`ship_state` stays `"none"`), so without this a completed repair could never satisfy `ship_state=="delivered"` and would linger forever (the CU IRISS bug). There is **no** time-based fallback — a *fulfilled but unpaid* build stays visible (with a "still on digest: awaiting payment #inv $amt" callout via `_why_still_active`, which now fires for delivered goods AND completed no-ship repairs) so an "is this done?" card never silently disappears. A record only drops off once it's fulfilled **and** `payment_state="paid"`.
- **Thread replies** (`commercial_sales_reply.py`) — Slack threads are flat, so a user "replying in thread" to any of the day's cards actually lands the reply directly under the umbrella header. `lookup_record_for_thread` resolves the target with a 3-tier fallback: (1) per-card direct match if the reply's `thread_ts` happens to be a card's `ts` (legacy threads from older digests, before umbrella threading), (2) **umbrella content-match** — when `thread_ts` is one of the day's umbrella parents (`thread_ts in umbrellas` — either the Active Orders or Customer Leads header), Haiku via `UMBRELLA_MATCH_SYSTEM` picks the best card from the day's full list by customer/product mention; low-confidence matches return None and the bot stays silent rather than guessing, (3) parse the hidden `build:<gid>` / `case:<id>` token out of the parent message text when the JSON map is gone (Railway redeploy). Once a record is resolved, Haiku via `PARSE_REPLY_SYSTEM` extracts structured `{field, value}` updates. Prompt explicitly enumerates enum values and maps common phrases (e.g. "this is done / completed / shipped" on a Build → emit `ship_state=delivered + shipped_date=today + build_state=complete`). Without the synonyms, "this has been completed" used to set `ship_state="completed"` (invalid) and reject the whole update. Validated updates are then **partitioned** (`_is_safe_fact`): plain factual fields — `SAFE_FACT_FIELDS_BUILD`/`SAFE_FACT_FIELDS_CASE` (invoice #/amount/date, tracking, carrier, ship_to, contact, dates, notes, …) — are **applied immediately** via `_commit_updates` with a "✓ Recorded — reply *undo* to revert" message; state-machine fields (`payment_state`/`build_state`/`ship_state`/case `state`), list fields (`items`/`parts`), and `owners` still go through propose-and-confirm. A mixed reply does both (facts land now, the state change waits for *yes*). This fixes the silent-drop class: corrections like Meredith's "Invoice 1766 for $3,900" or "delivered in person in Boulder" used to sit as an unconfirmed proposal in the 10-min in-memory `PENDING` dict and evaporate (nobody replies "yes", and it's wiped on Railway redeploy). The auto-apply path stashes a `STATE_AUTO_APPLIED` pending entry holding an `undo` buffer (prior flat-field values); a follow-up `undo` reverts via `_revert_updates`, and any *non-undo* follow-up is reprocessed as a fresh correction (`handle_thread_reply`) rather than dropped. The propose-and-confirm accept path shares `_commit_updates` (load → apply → save → Asana audit comment + `[FEEDBACK]`).
- **Pending state in the umbrella thread** — keyed on `(thread_ts, user_id)` so concurrent proposals by different users in the same umbrella thread don't collide (Beck can propose an ERAU update while Meredith proposes a NASA update). This replaces the older cross-user-confirm pattern; each proposer now confirms their own.
- **Tolerant JSON parsing** — `_loads_tolerant` in both `commercial_sales_reply.py` and `commercial_sales_inquiry.py` finds the first balanced `{...}` block in Haiku's response, so trailing prose doesn't kill the whole update with `JSONDecodeError: Extra data`. This bug previously surfaced as a visible "couldn't parse that update" reply in the channel.
- **Top-level inquiry** (`commercial_sales_inquiry.py::handle_inquiry`) — `#commercial-sales` messages asking about shipping/address/parts/POC/payment/serial/RMA/status (`is_inquiry_intent`) route here instead of falling through to `is_work_update`. **These only fire from an `@mention`** (via `route_message`) — the old ambient path in `handle_dm` that answered undirected channel chatter was removed so Jack stops interrupting human discussion. Three branches:
  1. **No match** → *first* try the general knowledge layer (`_try_general_knowledge_answer`): the inquiry handler searches `financial/by_project`, `budgets`, and `projects` for the customer/product hints (Slack mentions + owner names stripped from the hint tokens so they don't match the whole corpus), and if a documented order is found, answers from it via Haiku AND auto-stubs a seeded Build (carrying `project_code` + `source_files`) so the scanner promotes it. This is the fix for the Stanford/Acellent case — project 042-1 is documented in financials/budgets but lives in its own Asana project + personal mailboxes, so the commercial-sales scanner never built a record and the bot used to answer "I don't have a record." Only if the general-knowledge search comes up empty does it fall back to → ask for customer + product + ship date, stub a placeholder JSON under `knowledge/commercial_sales/builds/_stubs/`, log `[KNOWLEDGE_GAP]` (`record=unmatched`).
  2. **Match + field has value** → answer directly.
  3. **Match + field empty** → @-ping the right owner via `BUILD_FIELD_ROLES` / `SUPPORT_FIELD_ROLES`, log `[KNOWLEDGE_GAP]` with the specific field + record id.
- **Top-level updates** (`commercial_sales_inquiry.py::handle_update_propose`) — `#commercial-sales` messages with action verbs (`is_update_intent`: "add X as owner to Y", "mark Z complete", "set ship_to for W to ...", "tracking 1Z999... for V", and implicit-items phrasings like "the NASA S2 simulator includes X, Y, Z" / "S3 comes with EO/IR gimbal") route here. **Also `@mention`-gated** (same reason as top-level inquiry) — served via `route_message`, not the ambient `handle_dm` path. Haiku via `UPDATE_PARSE_SYSTEM` extracts `(target, field, value)` tuples, supports multi-target ("to A and B"), defaults `add … as owner` without a role to `interface`. Each target is resolved via the same `_match_record` matcher as the inquiry flow, validated via `commercial_sales_reply._validate_update`, then proposed with before→after diffs for owner edits. On accept, applies + saves + logs `[FEEDBACK]` for audit.
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
- **Canonical names + alias resolution.** `uid_map.json` is the source of truth: `_apply_canonical_names()` pins every entry's `name` to its `canonical_name` and collects an `aliases` / `name_tokens` set from every spelling the source systems use (Slack display names "Ben"/"Beck", Asana account names "Josh Fromm"/"Dan Prendergast"/"Meredith O'hara Needham", Rippling formal names "Nathaniel Straus", email local parts). People not yet in `uid_map.json` (e.g. Spencer Hoehl, Cory Dixon) keep their live name and get aliases derived from it
- `resolve_person(name)` maps any spelling → the one user entry; `canonical_name(name)` returns the canonical string. Resolution order: exact alias → unique single token → first+last token match → unique last name **guarded by first-name plausibility**. A spelling claimed by two people resolves to `None`. It refuses to guess by design: "Jack Bot" and outside contacts like "Bob Smith" (vs Paige Smith) return `None` rather than binding to an employee
- The daily pipeline canonicalizes Asana assignee names and Slack speaker names before they reach the prompt, so the model never sees three spellings of one person
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

### Provenance / Self-Knowledge (`provenance.py`)
Answers "how did you know that?" and "are you reading my email?" truthfully, from a fixed fact block instead of from a model's guess.
- **Why it exists**: on 2026-08-25 Joshua Fromm asked in #operations why an email from Munro — sent to *him* 30 minutes earlier, never to Jack — appeared in his briefing priorities. `is_question()` matched the leading "how" so it went to knowledge Q&A, but **nothing in the knowledge layer describes the pipeline's own data sources**, so Sonnet confabulated a denial: *"I don't go rummaging through inboxes, I just remember what's been reported to me."* His follow-up "explain yourself" has no question word and no `?`, so it missed `is_question()` entirely and hit the **personality handler**, which deflected. An employee asked a direct question about surveillance and got a false denial followed by a brush-off
- The real answer: `daily_research._collect_gmail()` loops over **every** user in the user map and calls `get_recent_emails(user["email"])`, which uses domain-wide delegation (`creds.with_subject(user_email)`) to impersonate that person's mailbox — `is:inbox newer_than:1d`, ≤20 messages, **Subject/From/Date only, no bodies** — and writes them into the prompt labeled by name
- `is_provenance_question()` is anchored on "you" as the subject (`how did you know`, `where did you get`, `are you reading my …`, `who told you`, `do you have access to`, plus `explain yourself` / `prove it` / `wasn't sent to you` / `nobody told you`), so ordinary work questions ("how did the flight test go", "where is the S3 shipment") still fall through to Q&A
- Routed **before** the commercial-sales, task-update, question and personality branches — the two handlers that failed here can no longer see these messages
- `FACTS` is the single source of truth and is appended to `QA_SYSTEM_PROMPT` as a `=== DATA ACCESS ===` block, so anything that slips past the router still answers honestly. `PROVENANCE_SYSTEM` forbids denying a listed capability, forbids the "someone told me" excuse, and drops the persona. `_fallback()` returns an accurate static answer if the API is down — truth matters more than phrasing on this path
- **Keep `FACTS` in sync with the code.** If the pipeline's reach changes and this file doesn't, the bot resumes lying about itself
- Offline coverage: `python test_provenance.py` — replays both of Josh's verbatim messages, asserts ordinary questions aren't hijacked, and checks the fact block actually states the capability

## Slack Output Guard (`slack_mute.py`)
Two env-driven controls over everything the bot says. Both are re-read on every call, so they can be flipped on Railway without a code change, and importing the module is a no-op when neither is set.
- `JACKBOT_SLACK_MUTE=1` — suppress every outbound Slack write. `JACKBOT_SLACK_REDIRECT=<channel_id>` — reroute every `chat_postMessage` to that channel, tagged `_[→ #origin]_`. Mute wins if both are set. `JACKBOT_SLACK_MUTE_LOG=<path>` also appends every suppressed/redirected call to a file
- **Patches `slack_sdk.WebClient` at the class level** rather than guarding call sites. Slack writes live at ~19 call sites across 9 modules and each builds its own `WebClient`; the class patch is the one choke point they all share, and it covers the client Bolt builds internally so handler `say()` calls are caught without touching `app.py`. `respond()` (slash commands) bypasses WebClient entirely — it POSTs to `response_url` — so it gets its own patch that forwards to the redirect target
- **Reads are never patched.** `conversations_history` / `users_info` / `conversations_info` / `auth_test` must keep working or the nightly scan breaks. Only the 26 write methods in `BLOCKED_METHODS` are intercepted — `conversations_join` among them, since joining posts a visible "…joined the channel" message
- Only `chat_postMessage` is redirectable; rerouting a reaction or file upload is meaningless, so under redirect every other write is suppressed as if muted
- **Threading**: a `thread_ts` is only valid in the channel it came from. The guard tracks ts values it produced *in the target*, so a child whose parent was also redirected keeps real threading (and isn't re-tagged — the parent carries the tag); a `thread_ts` from a foreign channel is dropped and the message marked `· thread reply` rather than being rejected by Slack
- Muted calls return a SlackResponse-shaped dict with a dummy `ts`, so `scheduler.py`'s umbrella-threading logic (`resp.get("ts")` / `resp.data.get("ts")`) runs without blowing up
- Wired in at the entry points only: `app.py`, `scan.py`, `scripts/daily_digest.py`, and the inline Python in `scripts/nightly_scan.sh`
- Offline coverage: `python test_slack_mute.py` (no credentials, no network — redirect is exercised against a fake client)

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
- `python test_identity.py` — offline regression suite for briefing identity handling; needs no credentials. Covers name resolution across every source-system spelling, the 2026-08-05 mis-assignment replay through `_validate_sections` / `_find_copied_sections`, deterministic section rendering (header, calendar, hours), and full team assembly
- `python test_pipeline.py` — runs the full daily pipeline end-to-end with live Asana/Toggl/Google/Slack reads, but intercepts every Slack write (no posts to #operations, no knowledge-channel entries). Prints the team summary and per-user sections to stdout
- `--verbose` echoes the suppressed writes so you can see what *would* have been posted (DEBUG, FEEDBACK, etc.)
- `--full` appends Claude's raw pre-parse output
- `python test_provenance.py` — offline suite for provenance-question routing; replays the 2026-08-25 Munro exchange and guards against ordinary questions being hijacked
- `python test_slack_mute.py` — offline suite for the Slack output guard (mute + redirect); never touches the network
- `python test_commercial_sales.py` — dry-run the commercial-sales digest render against current JSONs; `--scan` refreshes the JSONs first
- `python test_commercial_sales_inquiry.py` — exercises `is_inquiry_intent`, `is_update_intent`, the no-match / matched-field / empty-field inquiry branches, and the multi-target update propose flow against live JSONs with intercepted Slack writes. `--verbose` dumps the captured posts (KNOWLEDGE_GAP, FEEDBACK)

## Models Used
- Daily synthesis: `claude-sonnet-5` (10000 max tokens, thinking disabled, forced tool call via `tool_choice={"type":"tool","name":"submit_daily_briefing"}` for structured output; 3000-token targeted retry for missing people)
- Knowledge distillation: `claude-haiku-4-5-20251001` (cost-efficient for bulk processing)
- Q&A: `claude-sonnet-5` (with Haiku for search planning)
- Financial formatting: `claude-haiku-4-5-20251001` (converts markdown to Slack format)
- Personality chat: `claude-sonnet-5` (120 max tokens)

## OOO Detection
- Uses Rippling PTO calendar ICS feed (URL hardcoded in `daily_research.py`)
- Fetches live on each pipeline run; checks for events covering today
- Parses `SUMMARY: [Name] on [Type]` with `DTSTART`/`DTEND` date ranges
- Matches ICS names to user map by first/last name fuzzy matching

## Toggl Time Tracking
- `_last_workday()` returns the most recent Mon-Fri day (Friday on Monday, etc.)
- Prevents "no time tracked" false alarms on weekends and Mondays
