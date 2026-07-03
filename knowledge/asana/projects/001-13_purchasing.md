# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; **CRITICAL SURGE CONTINUES: 21 open tasks as of latest pull (up from 17 tasks 3 days prior).** Immediate deadlines **JUN 25 – JUL 4, 2026** (18 of 21 tasks due within 7 days; 2 overdue as of pull date).
- **Status:** 🔴 **CRITICAL OPERATIONAL STRESS — ESCALATING & UNSUSTAINABLE.** Task volume spiked from 17 to **21 open tasks** (+24% in ~3 days). **Meredith O'hara Needham now owns 19/21 tasks (90.5%), up from 76%.** Severe bottleneck at single person. **Two tasks are NOW OVERDUE** (due Jun 25 & Jun 5, 2026). Form discipline remains strong, but execution risk is ACUTE: 13 of 21 tasks show "Order Placed" or "Order Shipped" status with **zero downstream workflow for receipt verification, invoice matching, or project reconciliation.** One task requires approval but was not flagged for escalation. **No visible delegation despite Nate Straus availability.** Workload concentration is unsustainable and creates silent-failure risk.

- **Team members involved:**
  - **Meredith O'hara Needham** (project owner; 19/21 open tasks = **90.5%** — **CRITICAL INCREASE from 76%**)
  - **Nate Straus** (2/21 open tasks = 9.5% — **SEVERE DECREASE from 24%**)
  - **Jack Elston** (1/21 open tasks = 4.8% — **NEW ASSIGNEE**)
  - **Requesters:** Joshua Fromm (9 tasks — 43%), Alex (6), Ethan (2), Sam (2), Nate (1), Dan (1)

- **Risk signals:**
  - 🔴 **TWO OVERDUE TASKS (CRITICAL):**
    - *JawsTec- ByLight Gimbal (69507)* — **Due Jun 25, 2026** (OVERDUE by ~6 days as of Jul 2 pull). Status: "Order Shipped" — **no follow-up recorded.** Assigned to Meredith; requested by Ethan for [043-3] Mustang Pt. 2 (active project).
    - *instrumart for sales (#1083722)* — **Due Jun 5, 2026** (OVERDUE by ~27 days). Status: "Order Shipped" — **no receipt or invoice verification visible.** Assigned to Meredith; requested by Joshua Fromm for General Sales.
  - 🔴 **CATASTROPHIC WORKLOAD CONCENTRATION:** Meredith O'hara Needham carries **19 of 21 tasks (90.5%)** — up from 76% in prior cycle. **Zero meaningful delegation to Nate (2 tasks) or Jack (1 task).** If Meredith is unavailable, all 21 tasks stall. **No visible plan to redistribute.**
  - 🔴 **VOLUME SPIKE PATTERN & NO AUDIT TRAIL:** Tasks increased from 17 → 21 in ~3 days. No team correction, no explanation for rebound. New requesters include Dan (Nvidia Jetson order, requires approval, flagged but not escalated). **Batch submission pattern suggests backlog clearing or bulk request dump.** Unknown if orders were genuinely requested fresh or queued.
  - 🔴 **APPROVAL WORKFLOW BROKEN:** 1 of 21 tasks requires approval (Nvidia Jetson Orin Nano, requested by Dan, due Jul 2, assigned to Jack Elston). **No evidence of approval step or escalation.** Task is live and due in 48 hours. **Risk: Meredith may be unaware Jack owns an approval-required purchase.**
  - 🔴 **TASK CLOSURE WORKFLOW MISSING:** 13 of 21 tasks show "Order Placed" or "Order Shipped" — **none have downstream subtasks for:**
    - Receipt confirmation / three-way match (PO ↔ invoice ↔ receipt)
    - Tax exemption certificate storage or verification
    - Project billing reconciliation
    - Invoice approval / payment authorization
    - **Silent failures likely:** If a shipment is delayed, invoice doesn't match, or receipt is lost, no one will know until project reconciliation or audit.
  - 🟡 **TAX EXEMPTION & PAYMENT TRACKING GAPS:** 15 of 21 tasks are tax-exempt (70%); 6 are not. No evidence of exemption certificates, vendor account setup, or payment method tracking. "Requires Approval" custom field exists but is unenforced — single task flagged "Yes" was not routed to approver.
  - 🟡 **MULTI-PROJECT BILLING CONFUSION:** One task (jawstec for various projects, #SF311738) is assigned to MULTIPLE PROJECTS with note "PLEASE PROVIDE BREAKDOWN IN THE DESCRIPTION" — **no breakdown provided.** Assigned to Meredith; cannot be billed correctly. Joshua Fromm (requester) may not know this is unresolved.

## Key Deliverables & Milestones

### **OVERDUE — IMMEDIATE ACTION REQUIRED**

| Task | Due | Vendor | Assigned | Project | Requester | Status | Notes |
|------|-----|--------|----------|---------|-----------|--------|-------|
| JawsTec- ByLight Gimbal (69507) | Jun 25, 2026 ⚠️ **OVERDUE ~6 days** | Jawstec | Meredith O'hara Needham | [043-3] Mustang Pt. 2 | Ethan | Order Shipped | Requested Jun 23; No follow-up recorded; Active project affected |
| instrumart for sales (#1083722) | Jun 5, 2026 ⚠️ **OVERDUE ~27 days** | Instrumart | Meredith O'hara Needham | General Sales | Joshua Fromm | Order Shipped | Requested Jun 3; No receipt/invoice verification; Long overdue |

### **DUE JUN 25 – JUL 4, 2026 — 19 TASKS (IMMEDIATE ACTION WINDOW, 1–7 DAYS)**

| Task | Due | Vendor | Assigned | Project | Requester | Status | Requires Approval? | Notes |
|------|-----|--------|----------|---------|-----------|--------|-----|-------|
| Nvidia Jetson Orin Nano Super Developer Kit | Jul 2, 2026 | Nvidia | Jack Elston | [001-7] IRAD S3 | Dan | OPEN | **YES** | **ESCALATION REQUIRED:** Approval-required task due in 48 hrs; assigned to Jack (not typical approver); no approval visible; not routed to Meredith or manager |
| Digikey- Bylight Order (#100124240) | Jul 2, 2026 | Digikey/ByLight | Meredith O'hara Needham | [043-3] Mustang Pt. 2 | Ethan | Order Shipped | No | Requested Jun 30; Status shows shipped but no receipt confirmation |
| Digikey / Protektive Pak (#100117933) | Jul 2, 2026 | Digikey/Protektive Pak | Meredith O'hara Needham | [001-1] IRAD General | Nate | Order Shipped | No | Requested Jun 30; Status shows shipped but no receipt confirmation |
| compositeenvisions for s3 sales | Jul 2, 2026 | Composite Envisions | Nate Straus | General Sales | Joshua Fromm | Order Received | No | Requested Jun 16 (oldest current request); Tax Exempt; One of only 2 tasks assigned to Nate |
| amazon for shop supplies | Jul 3