# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project. **CRITICAL SURGE CONTINUES: 23 open tasks as of latest pull** (up 35% from 17 tasks in prior cycle). **ALL tasks due JUL 1–9, 2026 (0–9 days from pull date).** Workload remains in emergency state with extended deadline window.
- **Status:** 🔴 **CRITICAL OPERATIONAL STRESS — WORKLOAD FURTHER ACCELERATED. Task volume surged from 17 → 23 open tasks (+35%) in latest pull, continuing trend of explosion.** Workload redistribution now shows: **Meredith O'hara Needham owns 13/23 tasks (56.5%, up sharply from 41.2%), while Nate Straus owns 10/23 tasks (43.5%, down from 58.8%).** This reversal indicates **Meredith is re-accumulating bottleneck load after brief relief.** Nate's 10 tasks remain ALL "Order Received" — critical workflow stage still missing reconciliation/closure pathway. **Multiple "Order Shipped" tasks now visible (8 tasks) — indicating receipt verification backlog is building.** No overdue tasks formally recorded in Asana, but **"instrumart for sales" (#1083722) requested Jun 3, 2026 — now 35+ days in backlog**, remains stalled in "Order Received" state assigned to Nate.
- **Team members involved:**
  - **Meredith O'hara Needham** (13/23 open tasks = 56.5%, **up from 41.2% — relief period ended, bottleneck re-concentrating**)
  - **Nate Straus** (10/23 open tasks = 43.5%, down from 58.8% — but all 10 remain "Order Received", no downstream workflow)
  - **Requesters:** Joshua Fromm (13 tasks — 56.5%), Alex (4 tasks — 17.4%), Ethan (3 tasks — 13%), Kareem ahmed (1 task — 4.3%), Nate (1 task — 4.3%)
- **Risk signals:**
  - 🔴 **WORKLOAD RE-CONCENTRATION ACCELERATING:** Meredith's load bounced back from 41.2% → 56.5% in single cycle (+37% increase in absolute tasks assigned to her: 7 → 13). **Redistribution to Nate was temporary or incomplete.** If trend continues, will exceed prior crisis load of 88.9%.
  - 🔴 **BOTTLENECK SHIFTED UPSTREAM NOT RESOLVED:** 8 tasks now show "Order Shipped" status (Jawstec #69694, digikey #100222302, jawstec #SF311738, servocity #300045463, uavionix #107082, OpenUPS #139935, McMaster Carr, sendcutsend hurricane). **These are assigned to Meredith and indicate items have left vendor but receipt/verification hasn't happened.** Building backlog of unverified receipts. **Nate's "Order Received" queue (10 tasks) suggests he may be receiving items but with no guidance on three-way reconciliation, invoice matching, or project billing.**
  - 🔴 **CRITICAL WORKFLOW GAP STILL UNRESOLVED:** Nate owns 10 "Order Received" tasks. **Zero visible subtasks, no receipt verification checklist, no invoice matching process, no three-way reconciliation visible.** 35-day-old task ("instrumart for sales") suggests tasks can languish indefinitely without closure process.
  - 🟠 **REQUESTER CONCENTRATION CRITICAL:** Joshua Fromm now owns 13/23 tasks (56.5%, up from 47% in prior cycle). **Single requester drives majority of purchasing volume.** Unknown if he is initiating redundant orders, if batching is occurring, or if prioritization exists.
  - 🟡 **MULTI-PROJECT BILLING STILL UNRESOLVED (NOW 3 TASKS):** 
    - jawstec for sales - see details (#69738) — "MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN IN THE DESCRIPTION" — **No breakdown provided; cannot bill.**
    - digikey for various projects (#100222302) — "MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN IN THE DESCRIPTION" — **No breakdown provided; cannot bill. Order has shipped but unresolved.**
    - jawstec for various projects (#SF311738) — "MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN IN THE DESCRIPTION" — **No breakdown provided; cannot bill. Order has shipped but unresolved.**
    - **All 3 assigned to Meredith, 2 of 3 from Joshua Fromm. Represents billing risk and audit exposure.**
  - 🟡 **AGING BACKLOG CRITICAL:** "instrumart for sales" (#1083722) requested Jun 3, 2026 — **now 35+ days old, due Jul 8, assigned to Nate, Status: Order Received.** Indicates zero closure velocity on received orders. **If 1 task can age 35+ days, other "Order Received" tasks (assigned Jun 30 - Jul 1) could face same fate.**
  - 🟡 **TAX EXEMPTION TRACKING GAPS:** 16/23 tasks are tax-exempt (69.6%); 7 are not. No evidence of exemption certificate management, vendor account setup with tax ID, or payment method tracking in task notes.
  - 🟡 **NEW PROJECTS ADDED TO LOAD:** sendcutsend orders added for [300-3] 2026 IDIQ (Hurricane) and [212-2] NASA S2 & Parts — **indicates purchasing is supporting new contract ramps, increasing volume pressure.**

## Key Deliverables & Milestones

### **DUE JUL 1–9, 2026 — ALL 23 TASKS (IMMEDIATE ACTION WINDOW, 0–9 DAYS)**

| Task | Due | Vendor | Assigned | Project | Requester | Status | Tax Exempt? | Notes |
|------|-----|--------|----------|---------|-----------|--------|------------|-------|
| sendcutsend for hurricane (SP128831) | Jul 7, 2026 | SendCutSend | Meredith | [300-3] 2026 IDIQ (Hurricane) | Alex | Order Placed | NO | New project in pipeline |
| Jawstec (#69694) | Jul 4, 2026 | Jawstec | Meredith | General Sales | Alex | Order Shipped | YES | **Receipt verification pending** |
| digikey for various projects (#100222302) | Jul 8, 2026 | Digikey | Meredith | **MULTIPLE PROJECTS** | Joshua Fromm | Order Shipped | YES | **UNRESOLVED:** No project breakdown; cannot bill. Receipt verification pending. |
| jawstec for various projects (#SF311738) | Jul 4, 2026 | Jawstec | Meredith | **MULTIPLE PROJECTS** | Joshua Fromm | Order Shipped | YES | **UNRESOLVED:** No project breakdown; cannot bill. Receipt verification pending. |
| servocity for s3 sales (#300045463) | Jul 8, 2026 | Servocity | Meredith | [451-1] INSTAAR S3 x2 | Joshua Fromm | Order Shipped | YES | **Receipt verification pending** |
| uavionix for general sales (#107082) | Jul 8, 2026 | UAVionix | Meredith | General Sales | Joshua Fromm | Order Shipped | YES | **Receipt verification pending** |
| OpenUPS (#139935) | Jul 8, 2026 | OpenUPS | Meredith | [001-16] IRAD Swiftstation | Alex | Order Shipped | NO | **Receipt verification pending** |
| McMaster Carr- ByLight Motor Pods (0707JELSTON) | Jul 9, 2026 | McMaster Carr | Meredith | [043-3