# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project. **CRITICAL SURGE ACCELERATING: 17 open tasks as of latest pull** (up 89% from 9 tasks in prior cycle). All tasks due **JUL 1–8, 2026** (0–8 days). Prior cycle showed all tasks due Jul 1–4; workload has extended by 4 days but volume nearly doubled.
- **Status:** 🔴 **CRITICAL OPERATIONAL STRESS — WORKLOAD EXPLOSION AFTER BRIEF RELIEF.** Task volume surged from 9 → 17 open tasks (+89%) in latest pull, erasing prior 40% reduction. **Workload redistribution showing early results but insufficient:** Meredith O'hara Needham now owns 7/17 tasks (41.2%, down sharply from 88.9%), while Nate Straus now owns 10/17 tasks (58.8%, up from 11.1%). However, **Nate's 10 tasks are ALL "Order Received" — ready for closure/reconciliation workflow that remains missing.** No overdue tasks formally recorded, but "instrumart for sales" was requested Jun 3 (over a month backlog).
- **Team members involved:**
  - **Meredith O'hara Needham** (7/17 open tasks = 41.2%, down from 88.9% — **relief, but remains second-largest bottleneck**)
  - **Nate Straus** (10/17 open tasks = 58.8%, up from 11.1% — **now primary executor; ALL tasks are "Order Received" and ready for next workflow stage**)
  - **Requesters:** Joshua Fromm (8 tasks — 47%), Alex (4 tasks — 24%), Ethan (2 tasks — 12%), Kareem ahmed (1 task — 6%), Nate (1 task — 6%), Sam (0 tasks — 0%, down from 22%)
- **Risk signals:**
  - 🔴 **WORKLOAD CONCENTRATION SHIFTED, NOT SOLVED:** Meredith relief (88.9% → 41.2%) came at cost of overloading Nate (11.1% → 58.8%). **If Nate is unavailable, 10 of 17 tasks (59%) stall.** Two-person bottleneck persists; no evidence of broader team adoption.
  - 🔴 **CRITICAL WORKFLOW GAP EXPOSED:** Nate now owns 10 "Order Received" tasks — the exact bottleneck stage where **receipt verification, invoice matching, three-way reconciliation, and project billing should occur.** Zero downstream subtasks visible. **Nate likely has no guidance on what "Order Received" means operationally.** Silent failures almost certain if items don't match PO, invoices arrive late, or receipts are lost.
  - 🟠 **REQUESTER CONCENTRATION WORSENING:** Joshua Fromm now accounts for 8/17 tasks (47%, up from 33% in prior cycle). **Single requester drives half the purchasing volume.** Unknown if batching, prioritization, or escalation is happening at requester level.
  - 🟡 **MULTI-PROJECT BILLING UNRESOLVED (WORSENING):** Now 2 tasks with "MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN" (digikey for various projects #100222302, jawstec for sales #69738). Neither has breakdown provided. **Cannot be billed correctly.** Both assigned to Meredith; both from Joshua Fromm.
  - 🟡 **MONTH-OLD BACKLOG VISIBLE:** "instrumart for sales" (#1083722) assigned to Nate; requested Jun 3, 2026 — **over 1 month old, now due Jul 8.** Indicates tasks may sit in "Order Received" state indefinitely without closure.
  - 🟡 **TAX EXEMPTION & PAYMENT TRACKING GAPS (UNCHANGED):** 12/17 tasks are tax-exempt (71%); 5 are not. No evidence of exemption certificates, vendor account setup, or payment method tracking.

## Key Deliverables & Milestones

### **DUE JUL 1 – 8, 2026 — ALL 17 TASKS (IMMEDIATE ACTION WINDOW, 0–8 DAYS)**

| Task | Due | Vendor | Assigned | Project | Requester | Status | Tax Exempt? | Notes |
|------|-----|--------|----------|---------|-----------|--------|------------|-------|
| OpenUPS (295-498797) | Jul 8, 2026 | OpenUPS | Meredith | [001-16] IRAD Swiftstation | Alex | Order Placed | NO | — |
| servocity for s3 sales (#300045463) | Jul 8, 2026 | Servocity | Meredith | [451-1] INSTAAR S3 x2 | Joshua Fromm | Order Placed | YES | — |
| parts for s0 ground station (0706JELSTON) | Jul 8, 2026 | (TBD) | Meredith | Shop Supplies | Kareem ahmed | Order Placed | NO | — |
| digikey for various projects (#100222302) | Jul 8, 2026 | Digikey | Meredith | **MULTIPLE PROJECTS** | Joshua Fromm | Order Placed | YES | **UNRESOLVED:** No project breakdown provided; cannot bill correctly |
| jawstec for sales - see details (#69738) | Jul 8, 2026 | Jawstec | Meredith | **MULTIPLE PROJECTS** | Joshua Fromm | Order Placed | YES | **UNRESOLVED:** No project breakdown provided; cannot bill correctly |
| uavionix for general sales (#107082) | Jul 8, 2026 | UAVionix | Meredith | General Sales | Joshua Fromm | Order Placed | YES | — |
| jawstec for s3 sales (#69729) | Jul 8, 2026 | Jawstec | Meredith | [451-1] INSTAAR S3 x2 | Joshua Fromm | Order Placed | YES | — |
| mks (22794) | Jul 4, 2026 | MKS | Meredith | [001-4] IRAD S0 VTOL | Alex | Order Shipped | YES | Shipped as of prior pull; no receipt confirmation recorded |
| rockwest for s3 sales (#Z100709106) | Jul 8, 2026 | Rockwest | Nate | General Sales | Joshua Fromm | Order Received | YES | **Ready for reconciliation/closure** |
| amazon for shop supplies | Jul 8, 2026 | Amazon | Nate | Shop Supplies | Joshua Fromm | Order Received | NO | **Ready for reconciliation/closure** |
| RedwingRC (#34416) | Jul 8, 2026 | RedwingRC | Nate | General Sales | Alex | Order Received | YES | **Ready for reconciliation/closure** |
| Chaservo (#07-6668) | Jul 8, 2026 | Chaservo | Nate | General Sales | Alex | Order Received | YES | **Ready for reconciliation/closure** |
| chargers for s3 sales (HDR664888) | Jul 8, 2026 | (Vendor TBD) | Nate | General Sales | Joshua Fromm | Order Received | YES | **Ready for reconciliation/closure** |
| JawsTec- ByLight Gimbal (69507) | Jul 8, 2026 | Jawstec | Nate | [043-3] Mustang Pt. 2 | Ethan | Order Received | NO | **Ready for reconciliation/closure** |
| Digikey- Bylight Order (#100124240) | Jul 8, 2026 | Digikey | Nate | [043-3] Mustang Pt. 2 | Ethan