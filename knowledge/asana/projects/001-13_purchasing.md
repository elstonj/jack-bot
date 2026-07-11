# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project. **CRITICAL SURGE CONTINUES: 14 open tasks as of latest pull.** **ALL tasks due JUL 8–12, 2026 (immediate action window).**
- **Status:** 🔴 **CRITICAL OPERATIONAL STRESS — WORKLOAD CONCENTRATED ON MEREDITH & NATE.** Meredith owns 5/14 tasks (35.7%); Nate owns 9/14 tasks (64.3%). **Workflow bottleneck persists:** Meredith manages "Order Placed" and "Order Shipped" stages; Nate manages "Order Received" stage with no visible closure process. **MULTI-PROJECT BILLING UNRESOLVED (2 CRITICAL TASKS):** digikey (#100222302) and jawstec (#SF311738) both marked "MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN IN THE DESCRIPTION" with no breakdown provided — cannot bill.
- **Team members involved:**
  - **Nate Straus** (9/14 open tasks = 64.3%) — Order Received pipeline (no closure process visible)
  - **Meredith O'hara Needham** (5/14 open tasks = 35.7%) — Order Placed & Order Shipped pipeline
  - **Requesters:** Joshua Fromm (8 tasks — 57.1%), Alex (4 tasks — 28.6%), Kareem Ahmed (1 task — 7.1%)
- **Risk signals:**
  - 🔴 **NATE WORKLOAD CONCENTRATION INCREASED:** 9/14 tasks (64.3%) now assigned to Nate (up from 43.8% in prior pull). Owns entire "Order Received" pipeline with zero visible closure process. All assigned "Order Received" tasks due Jul 11–12.
  - 🔴 **MULTI-PROJECT BILLING UNRESOLVED (2 CRITICAL TASKS):**
    - digikey for various projects (#100222302) — Status: "Order Received" — assigned to Nate — marked "MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN IN THE DESCRIPTION" — **No breakdown provided; cannot bill.**
    - jawstec for various projects (#SF311738) — Status: "Order Received" — assigned to Nate — marked "MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN IN THE DESCRIPTION" — **No breakdown provided; cannot bill.**
    - Both from Joshua Fromm. **Represents billing risk and audit exposure.**
  - 🟠 **REQUESTER CONCENTRATION EXTREME:** Joshua Fromm owns 8/14 tasks (57.1%). All multi-project billing issues involve Joshua Fromm.
  - 🟠 **TASK SHIFT: MORE "ORDER RECEIVED" BOTTLENECK AT NATE.** Previous pull had 16 tasks with 9 at Meredith and 7 at Nate. Current pull has 14 tasks with 5 at Meredith and 9 at Nate—indicates Orders are moving through Meredith's pipeline faster, but stalling at Nate's "Order Received" stage with no progression visible.
  - 🟡 **TAX EXEMPTION TRACKING:** 9/14 tasks are tax-exempt (64.3%); 5 are not. No evidence of exemption certificate management or vendor tax ID tracking in task notes.
  - 🟡 **REQUESTER CHANGE DETECTED:** "sendcutsend for hurricane (SP128831)" now assigned to **Nate** with status "Order Received" (previously was Meredith with status "Order Shipped"). Suggests task moved across pipeline or reassigned mid-workflow. Alex is requester (not Joshua Fromm).

## Key Deliverables & Milestones

### **DUE JUL 8–12, 2026 — ALL 14 TASKS (IMMEDIATE ACTION WINDOW)**

| Task | Due | Vendor | Assigned | Project | Requester | Status | Tax Exempt? | Notes |
|------|-----|--------|----------|---------|-----------|--------|------------|-------|
| jawstec for s3 sales (#69729) | Jul 8, 2026 | Jawstec | Meredith | [451-1] INSTAAR S3 x2 | Joshua Fromm | Order Shipped | YES | |
| amazon for equipment | Jul 9, 2026 | Amazon | Meredith | Shop Supplies | Joshua Fromm | Order Shipped | NO | Misspelled in notes as "equpiment" |
| jawstec for s0 parts (#69825) | Jul 11, 2026 | Jawstec | Meredith | [300-3] 2026 IDIQ (Hurricane) | Joshua Fromm | Order Placed | YES | Order placement scheduled Jul 9 |
| connectors and power distribution board for s0 gcs | Jul 11, 2026 | (not specified) | Meredith | [300-3] 2026 IDIQ (Hurricane) | Kareem Ahmed | Order Shipped | NO | S0 ground station supply; order placement scheduled Jul 8 |
| McMaster | Jul 11, 2026 | McMaster | Meredith | [550-1] Navy SBIR: Magnetometer | Alex | Order Placed | NO | Order placed date: Jun 22, 2026 (19 days ago) |
| digikey for various projects (#100222302) | Jul 11, 2026 | Digikey | Nate | **MULTIPLE PROJECT** | Joshua Fromm | Order Received | YES | **UNRESOLVED:** No project breakdown; cannot bill. Order placement scheduled Jul 6. |
| Jawstec (#69694) | Jul 11, 2026 | Jawstec | Nate | General Sales (No Specific Project) | Alex | Order Received | YES | Order placement scheduled Jul 2 |
| jawstec for various projects (#SF311738) | Jul 11, 2026 | Jawstec | Nate | **MULTIPLE PROJECT** | Joshua Fromm | Order Received | YES | **UNRESOLVED:** No project breakdown; cannot bill. Order placement scheduled Jul 2. |
| servocity for s3 sales (#300045463) | Jul 11, 2026 | Servocity | Nate | [451-1] INSTAAR S3 x2 | Joshua Fromm | Order Received | YES | Order placement scheduled Jul 6. Receipt verification pending. |
| uavionix for general sales (#107082) | Jul 11, 2026 | UAVionix | Nate | General Sales (No Specific Project) | Joshua Fromm | Order Received | YES | Order placement scheduled Jul 6. Receipt verification pending. |
| apc props for s3 sales (#55048) | Jul 11, 2026 | APC Props | Nate | General Sales (No Specific Project) | Joshua Fromm | Order Received | YES | Order placement scheduled Jul 1 (overdue placement). Receipt verification pending. |
| mks (22794) | Jul 11, 2026 | MKS | Nate | [001-4] IRAD S0 VTOL | Alex | Order Received | YES | Order placement scheduled Jul 2. Receipt verification pending. |
| sendcutsend for hurricane (SP128831) | Jul 12, 2026 | SendCutSend | Nate | [300-3] 2026 IDIQ (Hurricane) | Alex | Order Received | NO | **TASK SHIFT DETECTED:** Previously Meredith (Order Shipped), now Nate (Order Received). Order placement scheduled Jul 7. |
| OpenUPS (#139935) | Jul 12, 2026 | OpenUPS | Nate | [001-16] IRAD Swiftstation | Alex | Order Received | NO | Order placement scheduled Jul 6. |

## Task Summary
- **Total tasks:** 14 open, 0 completed
- **Tasks by assignee:**
  - **Nate Straus:** 9/14 (64