# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; **CRITICAL SURGE CONTINUES: 9 open tasks as of latest pull.** All tasks due **JUL 1–4, 2026** (immediate deadlines, 0–4 days).
- **Status:** 🔴 **CRITICAL OPERATIONAL STRESS — WORKLOAD CONCENTRATION WORSENING.** Task volume decreased from 15 → 9 open tasks (−40%), BUT **Meredith O'hara Needham now owns 8/9 tasks (88.9%), down from 93.3% in prior cycle.** However, the **single Nate task is already Order Received**, leaving Meredith with 8 active execution items. **No overdue tasks recorded.** 7 of 9 tasks show "Order Placed"; 1 shows "Order Shipped"; 1 shows "Order Received." **CRITICAL GAP PERSISTS: Zero visible downstream workflow for receipt verification, invoice matching, or project reconciliation.** Form discipline remains strong; execution risk remains ACUTE.

- **Team members involved:**
  - **Meredith O'hara Needham** (8/9 open tasks = **88.9%** — slight relief from 93.3%, but still catastrophic concentration)
  - **Nate Straus** (1/9 open tasks = 11.1% — slight increase from 6.7%, but task is already Order Received)
  - **Requesters:** Alex (6 tasks — 67%), Joshua Fromm (1 task — 11%), Sam (2 tasks — 22%)

- **Risk signals:**
  - 🔴 **WORKLOAD CONCENTRATION REMAINS SEVERE:** Meredith O'hara Needham carries **8 of 9 tasks (88.9%)**. Despite a 40% reduction in total open tasks (15 → 9), single-person bottleneck persists. **If Meredith is unavailable, 8 of 9 tasks stall immediately.** No visible plan to redistribute.
  - 🔴 **TASK CLOSURE WORKFLOW MISSING (UNCHANGED):** 7 of 9 tasks show "Order Placed" or "Order Shipped"; **none have downstream subtasks for:**
    - Receipt confirmation / three-way match (PO ↔ invoice ↔ receipt)
    - Tax exemption certificate storage or verification
    - Project billing reconciliation
    - Invoice approval / payment authorization
    - **Silent failures likely:** If shipment is delayed, invoice doesn't match, or receipt is lost, no one will know until project reconciliation or audit.
  - 🟡 **MULTI-PROJECT BILLING UNRESOLVED (UNCHANGED):** Task *jawstec for various projects* (#SF311738) assigned to **MULTIPLE PROJECTS** with note "PLEASE PROVIDE BREAKDOWN IN THE DESCRIPTION" — **no breakdown provided.** Assigned to Meredith; cannot be billed correctly. Joshua Fromm (requester) may not know this is unresolved.
  - 🟡 **TAX EXEMPTION & PAYMENT TRACKING GAPS (UNCHANGED):** 8 of 9 tasks are tax-exempt (89%); 1 is not. No evidence of exemption certificates, vendor account setup, or payment method tracking.
  - 🟡 **REQUESTER CONCENTRATION (WORSENED):** Alex now accounts for 6/9 tasks (67%, up from 47%); Joshua Fromm 1/9 (11%, down from 40%); Sam 2/9 (22%, unchanged). **Alex dominance is increasing.** Unknown if requests are being batched or delayed at requester level.

## Key Deliverables & Milestones

### **DUE JUL 1 – 4, 2026 — ALL 9 TASKS (IMMEDIATE ACTION WINDOW, 0–4 DAYS)**

| Task | Due | Vendor | Assigned | Project | Requester | Status | Tax Exempt? | Notes |
|------|-----|--------|----------|---------|-----------|--------|------------|-------|
| SendCutSend (#SQ29Q224) | Jul 4, 2026 | SendCutSend | Meredith | General Sales | Alex | Order Placed | YES | Updated due date from Jul 1; tax-exempt |
| RedwingRC (#34416) | Jul 4, 2026 | RedwingRC | Meredith | General Sales | Alex | Order Placed | YES | Tax-exempt |
| mks (22794) | Jul 4, 2026 | MKS | Meredith | [001-4] IRAD S0 VTOL | Alex | Order Placed | YES | Tax-exempt |
| Chaservo (#07-6668) | Jul 4, 2026 | Chaservo | Meredith | General Sales | Alex | Order Placed | YES | Tax-exempt |
| Jawstec (#69694) | Jul 4, 2026 | Jawstec | Meredith | General Sales | Alex | Order Placed | YES | Tax-exempt |
| FETTEC (#25867) | Jul 4, 2026 | FETTEC | Meredith | General Sales | Alex | Order Placed | YES | Tax-exempt |
| jawstec for various projects (#SF311738) | Jul 4, 2026 | Jawstec | Meredith | **MULTIPLE PROJECTS** | Joshua Fromm | Order Placed | YES | **UNRESOLVED:** No project breakdown provided; cannot bill correctly |
| Extra AD parts (#100171793) | Jul 4, 2026 | (Vendor name TBD) | Meredith | [300-3] 2026 IDIQ (Hurricane) | Sam | Order Shipped | NO | Shipped — no receipt confirmation recorded |
| Extra FTDI USB boards (#100117560) | Jul 4, 2026 | (Vendor name TBD) | Nate | Shop Supplies | Sam | Order Received | NO | Already received; only task assigned to Nate — should be closable |

## Task Summary
- **Total open tasks:** 9 (down 40% from 15 in prior pull)
- **Completed tasks this cycle:** 0 recorded
- **Tasks by assignee with status:**
  - **Meredith O'hara Needham:** 8/9 (88.9%)
    - Order Placed: 7 tasks
    - Order Shipped: 1 task
  - **Nate Straus:** 1/9 (11.1%)
    - Order Received: 1 task
- **Tasks by requester:**
  - **Alex:** 6/9 (67%) — all Order Placed, all tax-exempt
  - **Sam:** 2/9 (22%) — 1 Order Shipped, 1 Order Received; both non-tax-exempt
  - **Joshua Fromm:** 1/9 (11%) — Order Placed, tax-exempt, multi-project (UNRESOLVED)
- **Notable patterns:**
  - All 9 tasks use the standardized form and custom fields correctly
  - 8/9 are tax-exempt (89%)
  - 7/9 are for General Sales or IRAD projects; 1 for Hurricane IDIQ; 1 for Shop Supplies
  - **No task closure workflow visible:** Tasks move from "Order Placed" → "Order Shipped" → "Order Received" but never to "Closed" or "Billed." No downstream subtasks for receipt, invoice, or reconciliation.

## Recent Activity
- **Task volume reduction:** Dropped from 15 open tasks (prior pull) to 9 (this pull) — **6 tasks resolved or closed externally.** No explanation in task notes or Asana activity log (not provided in raw data). Likely closures: **amazon for shop supplies, rockwest for s3 sales, apc props for s3 sales, tripods for s3 sales, Digikey (clikmate etc), chargers for s3 sales.** Unknown if items were received, invoiced, and project-b