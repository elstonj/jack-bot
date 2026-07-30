# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project. **11 open tasks with mixed deadlines: Jul 22 (OVERDUE), Jul 29–31, 2026.**
- **Status:** 🟠 **OPERATIONAL — DEADLINE CRUNCH & OVERDUE TASK PRESENT.** Task count **increased from 8 to 11** (from prior snapshot). Current distribution: **Order Placed 6/11 (55%), Order Shipped 3/11 (27%), Order Received 2/11 (18%).** Notable changes: **jawstec for s0 parts (Jul 22) is OVERDUE by 9 days** (today ~Jul 31). Task list has expanded significantly with new items (FTDI, additional amazon/mouser). Assignee distribution broadened: **Meredith O'hara Needham (8/11 = 73%), Nate Straus (3/11 = 27%)** — Nate's involvement has increased from single springstore task to three tasks (FTDI, digikey, springstore).
- **Team members involved:**
  - **Meredith O'hara Needham** (8/11 open tasks = 73%)
  - **Nate Straus** (3/11 = 27% — FTDI, digikey, springstore)
- **Requesters:** Joshua Fromm (9/11 = 82%), Nathaniel Straus (1/11 = 9%), Alex (1/11 = 9%)
- **Risk signals:**
  - 🔴 **OVERDUE TASK:** jawstec for s0 parts (Jul 22, Order Shipped) is **9 days overdue.** Status "Order Shipped" but due date has passed. Placed Jul 20; requires immediate follow-up/closure.
  - 🔴 **IMMINENT DEADLINES (TODAY or TOMORROW):** 
    - Amazon Shop supplies: Due Jul 31 (today)
    - amazon for SALES: Due Jul 31 (today)
    - FTDI: Due Jul 31 (today)
    - digikey for S0 hurricane: Due Jul 31 (today)
    - springstore for s0 idiq: Due Jul 30 (yesterday)
  - 🟠 **CRITICAL FORM DATA TRUNCATION PERSISTS (WORSE):** 5 of 11 tasks have severely truncated project codes in form capture:
    - **Amazon Shop supplies:** "[001-" (5 chars, incomplete — should be "[001-1] IRAD General" or similar)
    - **jawstec for s3 IRAD:** "[001-7] IR" (truncated from full "[001-7] IRAD S3")
    - **craftcloud:** "Select project to bill purcha" (cut off mid-word)
    - **mouser order for s0 hurricane:** PROJECT FIELD EMPTY in form notes
    - **jawstec for s0 parts:** "[300-3] 2" (truncated)
    - **digikey for S0 hurricane:** "[300-" (5 chars, incomplete)
    - **springstore for s0 idiq:** "[300-3" (6 chars, incomplete)
    - **mouser for shop equipment:** "Shop" (ambiguous; likely internal code missing)
    - **FTDI:** "Requi" (truncated in form, but task title shows project correctly as [001-16] IRAD Swiftstation)
    - **Indicates systematic form character-limit truncation (~30–50 chars in notes section).** Risk: Billing misroute, project code ambiguity.
  - 🟠 **HURRICANE BATCH DOMINANCE PERSISTING:** 5/11 tasks (45%) are [300-3] 2026 IDIQ (Hurricane S0). Single-point-of-failure risk remains high.
  - 🟠 **MULTI-PROJECT FLAGGED, NO BREAKDOWN:** powerwerx task explicitly notes "[Project: MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN IN THE DESCRIPTION]" but notes section is empty of breakdown. Status "Order Shipped" — order may have already placed without clarity. Risk: Incorrect/split billing, possible duplicate charges.
  - 🟠 **NEW ASSIGNEE VARIANCE & TEAM EXPANSION:** Nate Straus now assigned to 3 tasks (FTDI, digikey, springstore) vs. 1 previously. Nate also appears as requester for Amazon Shop supplies (via Nathaniel Straus). Joshua Fromm remains dominant requester (82%), but Alex appears as single requester for FTDI — possible new stakeholder or typo.
  - 🟠 **RECEIVED-BUT-OPEN TASKS:** FTDI, digikey, springstore all show "Order Received" status but remain open. Suggests fulfillment lag, missing closure step, or pending follow-up action (inspection, verification, invoice match).

## Key Deliverables & Milestones

### **OPEN TASKS — MIXED BATCH (Hurricane S0 IDIQ + IRAD S3/S7/Swiftstation + Sales + Shop Supplies + Multi-Project)**

| Task | Vendor | Assigned | Project (Form) | Requester | Status | Placement | Due | Tax Exempt? | Notes |
|------|--------|----------|----------------|-----------|--------|-----------|-----|------------|-------|
| **jawstec for s0 parts** | Jawstec | Meredith | [300-3] 2026 IDIQ (Hurricane) | Joshua Fromm | Order Shipped | Jul 20 | **Jul 22 🔴 OVERDUE (9 days)** | YES | 🔴 **OVERDUE.** Status "Order Shipped" but task due date passed. Requires escalation or closure. |
| **jawstec for s3 IRAD** | Jawstec | Meredith | [001-7] IRAD S3 **(TRUNCATED)** | Joshua Fromm | Order Placed | Jul 27 | Jul 29 | NO | Project field truncated: "[001-7] IR" (should be "[001-7] IRAD S3"). Task name confirms correct project. S3 IRAD (non-Hurricane). Tax exempt = NO (outlier). Due tomorrow. |
| **mouser order for s0 hurricane** | Mouser | Meredith | [300-3] 2026 IDIQ (Hurricane) | Joshua Fromm | Order Placed | Jul 24 | Jul 29 | YES | Project field EMPTY in form. Assumed [300-3] per vendor/context. Due tomorrow. |
| **craftcloud for s0 hurricane parts** | Craftcloud | Meredith | [300-3] 2026 IDIQ (Hurricane) | Joshua Fromm | Order Placed | Jul 24 | Jul 29 | YES | Project field truncated: "Select project to bill purcha..." Due tomorrow. |
| **Amazon Shop supplies** | Amazon | Meredith | Shop Supplies **(TRUNCATED)** | Nathaniel Straus | Order Placed | Jul 29 | **Jul 31 🔴 TODAY** | NO | Project field truncated: "[001-" (5 chars; likely [001-1] IRAD General or Shop Supplies). Requester = Nate (Nathaniel Straus). Due today. |
| **amazon for SALES** | Amazon | Meredith | General Sales (No Specific Project) | Joshua Fromm | Order Placed | Jul 29 | **Jul 31 🔴 TODAY** | YES | ✓ Project field complete ("General Sales"). Tax exempt = YES (first non-project-specific). Due today. |
| **mouser for shop equipment** | Mouser | Meredith | Shop Supplies | Joshua Fromm | Order Shipped | Jul 28 | Jul 30 | NO | Custom field says "Shop Supplies"; notes say "Shop" only. Status "Order Shipped" but task due yesterday (Jul 30). Verify closure. |
| **powerwerx for multiple projects** |