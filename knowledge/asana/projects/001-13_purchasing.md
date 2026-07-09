# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project. **CRITICAL SURGE CONTINUES: 21 open tasks as of latest pull.** **ALL tasks due JUL 1–9, 2026 (0–9 days from pull date).** Workload remains in emergency state.
- **Status:** 🔴 **CRITICAL OPERATIONAL STRESS — WORKLOAD CONCENTRATED ON MEREDITH. All 21 open tasks remain active with compressed deadline window (0–9 days).** Meredith O'hara Needham owns 13/21 tasks (61.9%); Nate Straus owns 8/21 tasks (38.1%). **Workflow bottleneck persists:** Meredith manages "Order Placed" and "Order Shipped" stages; Nate manages "Order Received" stage with no visible closure process. **Critical aging backlog:** "instrumart for sales" (#1083722) requested Jun 3, 2026 — **now 35+ days in backlog, still in "Order Received" state assigned to Nate.** Zero visible receipt verification, three-way reconciliation, or invoice matching process. **Multi-project billing unresolved:** jawstec (#69738), digikey (#100222302) marked "MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN" with no breakdown provided; cannot bill.
- **Team members involved:**
  - **Meredith O'hara Needham** (13/21 open tasks = 61.9%)
  - **Nate Straus** (8/21 open tasks = 38.1%)
  - **Requesters:** Joshua Fromm (13 tasks — 61.9%), Ethan (2 tasks — 9.5%), Alex (2 tasks — 9.5%), Kareem Ahmed/kareem ahmed (2 tasks — 9.5%), Nate (1 task — 4.8%)
- **Risk signals:**
  - 🔴 **MEREDITH WORKLOAD CONCENTRATION CRITICAL:** 13/21 tasks (61.9%) assigned to Meredith. Owns entire "Order Placed" and "Order Shipped" pipeline. No workload redistribution visible since prior cycle. If she is sole point of contact for vendor communication, receipt staging, and shipping tracking, single-person failure risk is extreme.
  - 🔴 **NATE'S "ORDER RECEIVED" QUEUE HAS ZERO CLOSURE PROCESS:** 8/21 tasks assigned to Nate, all status "Order Received." **No subtasks, no receipt verification checklist, no invoice matching procedure, no project billing confirmation visible.** "instrumart for sales" (#1083722) is **35+ days old (requested Jun 3, now due Jul 8)** with zero progress. **If oldest received order takes 35+ days to process, new received orders (dated Jun 30 - Jul 1) face same timeline.** This is a workflow design failure, not a capacity issue.
  - 🔴 **MULTI-PROJECT BILLING UNRESOLVED (2 TASKS):**
    - jawstec for sales (#69738) — Status: "Order Placed" — marked "MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN IN THE DESCRIPTION" — **No breakdown provided; cannot bill.**
    - digikey for various projects (#100222302) — Status: "Order Shipped" — marked "MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN IN THE DESCRIPTION" — **No breakdown provided; cannot bill. Order has shipped but unresolved.**
    - Both assigned to Meredith, both from Joshua Fromm. **Represents billing risk and audit exposure.**
  - 🟠 **REQUESTER CONCENTRATION EXTREME:** Joshua Fromm owns 13/21 tasks (61.9%). **Single requester drives majority of purchasing volume.** Unknown if he is initiating redundant orders, batching is occurring, or if prioritization exists. All three multi-project issues involve Joshua Fromm.
  - 🟡 **AGING BACKLOG CRITICAL:** "instrumart for sales" (#1083722) requested Jun 3, 2026 — **now 35+ days old, due Jul 8, assigned to Nate, Status: Order Received.** Additional risk: Jawstec gimbal (69507) requested Jun 23, now in "Order Received" assigned to Nate (15 days old). Indicates **zero closure velocity on received orders.** Both assigned to Nate — suggests bottleneck is in his queue.
  - 🟡 **TAX EXEMPTION TRACKING GAPS:** 13/21 tasks are tax-exempt (61.9%); 8 are not. No evidence of exemption certificate management, vendor account setup with tax ID, or payment method tracking in task notes.
  - 🟡 **NEW PROJECTS ADDED TO LOAD:** sendcutsend for NASA S2 (S439K456), connectors for S0 ground station — **indicates purchasing is supporting new/expanding contract ramps, increasing volume pressure.**

## Key Deliverables & Milestones

### **DUE JUL 1–9, 2026 — ALL 21 TASKS (IMMEDIATE ACTION WINDOW, 0–9 DAYS)**

| Task | Due | Vendor | Assigned | Project | Requester | Status | Tax Exempt? | Notes |
|------|-----|--------|----------|---------|-----------|--------|------------|-------|
| connectors and power distribution board for s0 gcs | Jul 8, 2026 | (not specified) | Meredith | [300-3] 2026 IDIQ (Hurricane) | Kareem Ahmed | (not specified) | NO | S0 ground station supply |
| rockwest for s3 sales (Z100709976) | Jul 9, 2026 | Rockwest | Meredith | General Sales | Joshua Fromm | Order Placed | YES | |
| amazon for equipment | Jul 9, 2026 | Amazon | Meredith | Shop Supplies | Joshua Fromm | Order Placed | NO | |
| sendcutsend order for s2 nasa (S439K456) | Jul 9, 2026 | SendCutSend | Meredith | [212-2] NASA S2 & Parts | Joshua Fromm | Order Placed | YES | New project in pipeline |
| jawstec for sales - see details (#69738) | Jul 8, 2026 | Jawstec | Meredith | **MULTIPLE PROJECT** | Joshua Fromm | Order Placed | YES | **UNRESOLVED:** No project breakdown; cannot bill |
| jawstec for s3 sales (#69729) | Jul 8, 2026 | Jawstec | Meredith | [451-1] INSTAAR S3 x2 | Joshua Fromm | Order Placed | YES | |
| McMaster Carr- ByLight Motor Pods (0707JELSTON) | Jul 9, 2026 | McMaster Carr | Meredith | [043-3] Mustang Pt. 2 | Ethan | Order Shipped | NO | Receipt verification pending |
| OpenUPS (#139935) | Jul 8, 2026 | OpenUPS | Meredith | [001-16] IRAD Swiftstation | Alex | Order Shipped | NO | Receipt verification pending |
| digikey for various projects (#100222302) | Jul 8, 2026 | Digikey | Meredith | **MULTIPLE PROJECT** | Joshua Fromm | Order Shipped | YES | **UNRESOLVED:** No project breakdown; cannot bill. Receipt verification pending |
| servocity for s3 sales (#300045463) | Jul 8, 2026 | Servocity | Meredith | [451-1] INSTAAR S3 x2 | Joshua Fromm | Order Shipped | YES | Receipt verification pending |
| uavionix for general sales (#107082) | Jul 8, 2026 | UAVionix | Meredith | General Sales | Joshua Fromm | Order Shipped | YES | Receipt verification pending |
| parts for s0 ground station (0706JELSTON) | Jul 