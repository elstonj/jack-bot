# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; current orders due June 20–21, 2026
- **Status:** **ACTIVE — CRITICAL IMPROVEMENT SUSTAINED.** Assignment concentration remains normalized: Meredith O'hara Needham 1/3 (33%), Nate Straus 2/3 (67%). **Delegation strategy holding.** However, **URGENT REGRESSION: 3/3 tasks show status "Order Placed" or "Order Received" but remain open — form-based auto-closure still not functioning.** Task count collapsed from 7 to 3 (4 tasks successfully closed since last cycle). **⚠️ CRITICAL: All three remaining tasks require immediate manual closure.**
- **Team members involved:**
  - **Nate Straus** (2/3 assigned tasks; sendcutsend #SC51C906, Microhard; delegation maintained)
  - **Meredith O'hara Needham** (1/3 assigned tasks; compositeenvisions; project owner; concentration further reduced from 43%)
  - **Joshua Fromm** (2/3 as requester; compositeenvisions, sendcutsend #SC51C906)
  - **Nate** (1/3 as requester; Microhard)

- **Risk signals:**
  - 🔴 **CRITICAL CLOSURE FAILURE — ALL 3 REMAINING TASKS "COMPLETED" BUT OPEN:**
    - "Order Placed": compositeenvisions (Jun 20)
    - "Order Received": sendcutsend #SC51C906 (Jun 21, placed Jun 3 — **18 days stale**), Microhard (Jun 20, placed May 11 — **40+ days stale**)
    - **Form-based auto-closure is NOT functioning.** Manual closure required **immediately** for all 3 tasks before June 20.
    - **Stale order-received timestamps suggest daily audit process is not being performed.**
  
  - 🟢 **POSITIVE: TASK REDUCTION ACCELERATING** — 4/7 tasks from prior cycle successfully closed (57% reduction). Indicates improved process compliance despite closure mechanism lag.
  
  - 🟢 **DELEGATION SUSTAINED** — Nate Straus holding 67% of remaining tasks; single-point-of-failure risk remains low.
  
  - 🟡 **BILLING AMBIGUITY PERSISTS — 2/3 TASKS ASSIGNED TO "General Sales":**
    - compositeenvisions (due Jun 20) — assigned to "General Sales (No Specific Project)" but requester is Joshua Fromm (S3 focus); expect [001-7] IRAD S3 billing.
    - sendcutsend #SC51C906 (due Jun 21) — assigned to "General Sales (No Specific Project)" but requester is Joshua Fromm (S3 focus); likely [001-7] IRAD S3.
    - **Both must be reassigned to [001-7] IRAD S3 in project field before final billing.**

## Key Deliverables & Milestones

### **DUE JUNE 20–21, 2026 — 3 Tasks (Status: All "Completed" but Open)**

| Task | Due | Status | Assigned | Project | Requester | Tax Exempt | Notes |
|------|-----|--------|----------|---------|-----------|-----------|-------|
| compositeenvisions for s3 sales | Jun 20, 2026 | Order Placed | Meredith O'hara Needham | General Sales (No Specific Project) | Joshua Fromm | YES | Order placement date Jun 16, 2026 (completed 4+ days ago). Status "Order Placed" — **CLOSE IMMEDIATELY.** Update project field to [001-7] IRAD S3 before billing. |
| Microhard / Hurricane GCS | Jun 20, 2026 | Order Received | **Nate Straus** | [300-3] 2026 IDIQ (Hurricane) | Nate | NO | Order placed May 11, 2026 — **40+ days stale.** Status "Order Received" — **CLOSE IMMEDIATELY.** Critical process failure: order received in early May but task remains open. Implement daily audit of "Order Received" tasks >3 days old. |
| sendcutsend for s3 sales (#SC51C906) | Jun 21, 2026 | Order Received | **Nate Straus** | General Sales (No Specific Project) | Joshua Fromm | YES | Order placement date Jun 3, 2026 (completed 18 days ago). Status "Order Received" — **CLOSE IMMEDIATELY.** Update project field to [001-7] IRAD S3 before billing. |

## Task Summary

- **Total tasks:** 3 open, 0 completed (down from 7 in prior cycle; **57% reduction**)
- **Tasks by assignee:**
  - **Nate Straus:** 2/3 (67%) — sendcutsend #SC51C906, Microhard. Both "Order Received" — **both ready for immediate closure.**
  - **Meredith O'hara Needham:** 1/3 (33%) — compositeenvisions. Status "Order Placed" — **ready for immediate closure.**
- **Requester distribution:**
  - **Joshua Fromm:** 2/3 (compositeenvisions, sendcutsend #SC51C906) — both need [001-7] IRAD S3 project reassignment
  - **Nate:** 1/3 (Microhard) — correctly assigned to [300-3]

## Recent Activity

- **Dramatic task closure:** 4 of 7 tasks from prior cycle have been successfully closed/removed (57% reduction). Process compliance is improving.
- **All remaining tasks show "completed" status (Order Placed or Order Received) but remain open in task list.** This indicates:
  - Orders are physically received/placed (real-world status is current).
  - Form-based auto-closure mechanism is **not triggering closures** in Asana.
  - Tasks will stale out and risk auto-deletion per project notes ("USE THIS FORM PLEASE OR YOUR TASK WILL AUTO DELETE").
- **Critical stale orders identified:**
  - Microhard placed May 11, 2026 (40+ days ago) — status "Order Received" since at least last cycle review.
  - sendcutsend placed Jun 3, 2026 (18 days ago, 3 days past last cycle review) — status remains "Order Received."
- **Delegation momentum sustained:** Nate Straus now holds 67% of open tasks; single-point-of-failure risk reduced compared to prior cycle's 82% Meredith concentration.

## Notes & Context

- **URGENT ACTION REQUIRED:**
  1. **Close all 3 remaining tasks manually immediately** — do not rely on form-based auto-closure (clearly non-functional).
  2. **Implement daily audit process** for any task with status "Order Received" >3 days old. Current 40-day stale order (Microhard) indicates audit is not being performed.
  3. **Reassign compositeenvisions and sendcutsend #SC51C906 to [001-7] IRAD S3 project** in Asana before billing cycle.
  4. **Contact Asana/IT re: form-based auto-closure failure** — investigate why completed orders (marked "Order Received"/"Order Placed") are not auto-closing per project form settings.

- **Form-based closure mechanism:** Project notes reference a form (https://form.asana.com/?k=AYO2EiBus4sRY0G_cbPmHw&d=12804948716594) that should auto-delete tasks if not submitted. This appears to be non-functional; all new data reflects manual task creation/updates rather than form-triggered auto-management.

- **Billing ambiguity:** Two tasks (compositeenvisions, sendcutsend #SC51C906) show