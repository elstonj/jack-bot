# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; current orders due Apr 21–23, 2026
- **Status:** Active - **significant workload reduction** (9 open tasks → 2 open tasks). Remaining orders in "Order Placed" state, indicating fulfillment in progress. **7 orders closed/resolved since prior snapshot**, suggesting strong execution velocity or potential external inventory management.
- **Team members involved:** 
  - Meredith O'hara Needham (exclusive processor - 2 assigned tasks, 100% of workload)
- **Risk signals:** 
  - **Meredith single-point-of-failure persists:** All 2 remaining tasks assigned to one person; no backup capacity.
  - **Dramatic task reduction unexplained:** 9 → 2 open tasks. **Critical reconciliation needed:** Were 7 orders completed/received, moved to inventory hold, or archived without closure documentation?
  - **Both remaining orders due Apr 23:** Compressed timeline with minimal buffer.
  - **Lost project visibility:** Prior snapshot tracked 4 Mustang Pt. 2 orders, 2 IRAD S3 orders, 1 IRAD General order, 1 General Sales order. Current snapshot shows only 1 IRAD General (Amazon) and 1 Hurricane IDIQ (Craftcloud) — **Mustang Pt. 2 and most IRAD S3 orders no longer visible**. Confirm whether shipped, received, or moved off-queue.

## Key Deliverables & Milestones

### **[001-1] IRAD General** — 1 open order
- **Amazon Shop supplies** | Due Apr 23, 2026 | Meredith O'hara Needham | Status: Order Placed | Requester: Nate | Tax Exempt: NO | Placed: Apr 21, 2026

### **[300-3] 2026 IDIQ (Hurricane)** — 1 open order
- **Craftcloud for S0 parts (#459340813415)** | Due Apr 23, 2026 | Meredith O'hara Needham | Status: Order Placed | Requester: Joshua Fromm | Tax Exempt: YES | Placed: Apr 21, 2026

## Task Summary
- **Total tasks:** 2 open, 0 completed (100% open rate; significant reduction from 9 open tasks)
- **Tasks by assignee:**
  - Meredith O'hara Needham: 2 tasks (100% of workload)
  - Unassigned: 0 tasks
- **Order status breakdown:**
  - Order Placed: 2 tasks (100%)
  - Order Shipped: 0 tasks
- **Notable patterns:**
  - **Meredith exclusively assigned:** 2 tasks remain with single team member. Bottleneck risk reduced by volume but **dependency remains critical**.
  - **Project concentration shift:** Prior snapshot showed Mustang Pt. 2 (56% of orders), IRAD S3 (22%), IRAD General (11%), General Sales (11%). Current snapshot shows IRAD General (50%) and Hurricane IDIQ (50%) — **Mustang Pt. 2 and most IRAD S3 orders absent from queue**.
  - **Tax exemption:** Craftcloud order marked "Tax Exempt: YES" (Hurricane IDIQ project exemption).
  - **Compressed due dates:** Both tasks due Apr 23; placed Apr 21. Standard 2-day turnaround window.

## Recent Activity
- **Dramatic task volume reduction:** 9 → 2 open tasks since prior snapshot.
  - **Orders no longer visible (likely closed/received):**
    - JawsTec - Mustang/Chilli/M2 (#68231)
    - Jawstec (#68200)
    - KDE Direct - Motors for M2/Mustang/Chilli (shipped)
    - ReadyMadeRC - TBS ESCs for Mustang/Chilli/M2 (shipped)
    - Sendcutsend (#S834G264) for Mustang
    - north american survival systems (#11385) for IRAD S3
    - amazon for s3
    - Digikey (db9) for IRAD General
    - sendcutsend for s3 parts / sales (SW02L252)
  - **Action required:** Confirm closure dates, receiving documentation, and whether orders were moved to separate inventory tracking system or archived. If no records exist, escalate to Meredith for reconciliation.
- **Remaining orders are 2-day-old placements** (ordered Apr 21 for Apr 23 delivery), suggesting normal fulfillment cycle. No overdue tasks visible.

## Notes & Context

1. **Critical reconciliation required: 7 closed orders**
   - Prior snapshot tracked 9 open tasks across Mustang Pt. 2 (5 orders), IRAD S3 (2 orders), IRAD General (1 order), and General Sales (1 order).
   - Current snapshot shows only 2 orders (IRAD General and Hurricane IDIQ).
   - **Questions:**
     - Were the 5 Mustang Pt. 2 orders (KDE Direct, ReadyMadeRC, 3x Sendcutsend, Jawstec) completed/received on schedule (due Apr 22)?
     - Were the 2 IRAD S3 orders (north american survival systems, amazon for s3) completed/received?
     - Was the prior IRAD General Digikey db9 order completed, or replaced by current Amazon order?
     - Were these orders closed in Asana task list, or moved to external inventory system without closure?
   - **Recommendation:** Contact Meredith O'hara Needham and Joshua Fromm to audit closed orders, confirm delivery receipts, and establish whether Asana task list is the source of truth or if external system is handling post-order tracking.

2. **Meredith single-point-of-failure persists (lower urgency due to reduced volume)**
   - All 2 tasks assigned to Meredith O'hara Needham.
   - Current load is manageable (2 tasks with standard timeline), but if volume spikes (e.g., new Mustang Pt. 2 orders), bottleneck risk resurfaces immediately.
   - **Recommendation:** Establish secondary approver protocol before volume increases.

3. **Form submission note flagged in project**
   - Project notes include link to Asana form for task creation: "USE THIS FORM PLEASE OR YOUR TASK WILL AUTO DELETE"
   - Suggests automated task cleanup may be active. **Verify whether closed/archived tasks are being automatically removed from queue without manual audit trail.** This could explain the 7 disappeared orders if they were not submitted via form.

4. **Hurricane IDIQ resurfaced**
   - Craftcloud S0 order reappears in current snapshot (was visible in prior snapshot, then absent, now visible again).
   - Suggests task may have been archived/reopened or duplicate prevention failed.
   - **Confirm:** Is this the same order (459340813415) or a new requisition for same vendor/project?