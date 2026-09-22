# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across 10+ active projects
- **Timeline:** Ongoing operational project
  - **Current active window (Sep 10–16, 2026):** 4 open tasks (all assigned to Meredith)
- **Status:** 🟢 **STABILIZED — OPERATIONAL.** Open task count increased to 4 (new intake from Joshua Fromm). All tasks assigned, tracked, and current.
- **Team members involved:**
  - **Meredith O'hara Needham** (owner, 4/4 = 100%) — all current tasks assigned to her
  - **Requesters:** Alex (2 tasks — Magnetometer/Navy SBIR), Sam (1 task — S3 IRAD), Joshua Fromm (1 task — S3 IRAD)
- **Risk signals:**
  - 🟡 **JAWSTEC TASK OVERDUE:** jawstec for s3 irad parts (#71063) due Sep 12, 2026 — **2 days past deadline** (current snapshot date inferred ~Sep 14). Status: "Order Received" (may indicate fulfillment complete, but requires verification). Recommend immediate check-in with Meredith/Joshua Fromm.
  - ⏳ **Sep 16 DEADLINE IMMINENT:** 3 tasks (Getfpv, Amazon, S3 Backup Regulators) converge on Sep 16; confirm no delays expected.
  - ⏳ **MINOR STATUS DRIFT:** Mixed fulfillment stages across 4 tasks (2× "Order Received", 1× "Order Placed", 1× "Order Shipped"). Meredith should reconcile by Sep 14 to clarify which orders are in-transit vs. complete.

## Key Deliverables & Milestones

| Task | Vendor | Project | Requester | Requested | Due | Status | Tax Exempt |
|------|--------|---------|-----------|-----------|-----|--------|-----------|
| Getfpv (#858020) | Getfpv | [550-1] Navy SBIR: Magnetometer | Alex | Sep 11, 2026, 3:18pm | Sep 16, 2026 | Order Received | NO |
| Amazon | Amazon | [550-1] Navy SBIR: Magnetometer | Alex | Sep 11, 2026, 3:15pm | Sep 16, 2026 | Order Placed | NO |
| jawstec for s3 irad parts (#71063) | jawstec | [001-7] IRAD S3 | Joshua Fromm | Sep 10, 2026 | **Sep 12, 2026** ⚠️ | Order Received | NO |
| S3 Backup Regulators (#1J597401) | S3 Backup Regulators | [001-7] IRAD S3 | Sam | Sep 14, 2026 | Sep 16, 2026 | Order Shipped | NO |

## Task Summary
- **Total open tasks:** 4 (↑ 1 from prior snapshot; new intake from Joshua Fromm)
- **All assigned to Meredith O'hara Needham** (100% assignment rate)
- **Completion pattern by project:**
  - [550-1] Navy SBIR: Magnetometer — 2 tasks (Getfpv, Amazon)
  - [001-7] IRAD S3 — 2 tasks (jawstec for s3 irad parts, S3 Backup Regulators)
- **Status breakdown:**
  - Order Received — 2 tasks (Getfpv, jawstec)
  - Order Placed — 1 task (Amazon)
  - Order Shipped — 1 task (S3 Backup Regulators)
- **No tax-exempt items in current queue**
- **No approval required for any tasks**

## Recent Activity
- **Sep 10–14 active intake window:** 4 tasks in queue. New intake from Joshua Fromm (jawstec for s3 irad parts) added to pipeline since last snapshot.
- **Status shift noted:** Getfpv remains "Order Received"; jawstec newly shows "Order Received" (order arrived; awaiting fulfillment or inventory entry). Amazon remains "Order Placed"; S3 Backup Regulators remains "Order Shipped".
- **⚠️ OVERDUE TASK:** jawstec for s3 irad parts due Sep 12, 2026 — now 2+ days past deadline with status "Order Received". Requires immediate escalation/clarification.

## Notes & Context
- **Data model confirmed:** System operating in normalized state. Current snapshot reflects 4 active fulfillment tasks.
- **Project allocation clean:** All 4 tasks correctly allocated to billable projects ([550-1] Navy SBIR, [001-7] IRAD S3).
- **Intake process working:** All tasks submitted via standardized Asana form; form link embedded in project notes.
- **Status reconciliation urgent:** jawstec overdue status unclear (marked "Order Received" but past due date). Meredith should contact Joshua Fromm immediately to clarify whether order was received and if fulfillment is complete, or if delivery is delayed. Sep 16 deadline pressure on remaining 3 tasks may mask resolution delays.