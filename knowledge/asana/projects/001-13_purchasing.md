# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; current orders due Apr 22–25, 2026
- **Status:** Active - **task count recovered to 7 open tasks** (was 2 in prior snapshot). Mix of statuses: Order Placed (2), Order Shipped (4), Order Received (1). **Discrepancy from prior snapshot suggests tasks were restored or reappeared in queue** — reconciliation needed to confirm whether these were archived and re-added, or if prior snapshot missed active orders.
- **Team members involved:** 
  - Meredith O'hara Needham (primary processor - 6 assigned tasks)
  - Nate Straus (secondary processor - 1 assigned task)
- **Risk signals:** 
  - **Task reappearance unexplained:** 9 → 2 → 7 open tasks across snapshots. Orders marked "Order Shipped" and "Order Received" remain in open queue — **not being closed after fulfillment**. Critical: Confirm whether open status means awaiting receipt confirmation or if closure workflow is missing.
  - **Meredith near single-point-of-failure:** 6 of 7 tasks assigned to Meredith; only 1 to Nate.
  - **Multiple orders overdue or near-due:** Jawstec (due Apr 22, requested Apr 17 — 5-day slip), sendcutsend (due Apr 22), Amazon (due Apr 23). Orders marked "Order Shipped" should have been closed; lingering in open queue suggests no closure SOP.
  - **Nate Straus assigned ReadyMadeRC (status: Order Received):** First time Nate appears as assignee; unclear if this is hand-off for receiving verification or task ownership shift.

## Key Deliverables & Milestones

### **[043-3] Mustang Pt. 2** — 2 open orders
- **Jawstec (#68200)** | Due Apr 22, 2026 | Meredith O'hara Needham | Status: Order Shipped | Requester: Alex | Tax Exempt: NO | Requested: Apr 17, 2026 | **5-day slip**
- **ReadyMadeRC - TBS ESCs (#420240)** | Due Apr 25, 2026 | Nate Straus | Status: Order Received | Requester: Ethan Domagala | Tax Exempt: NO | Requested: Apr 20, 2026

### **[001-7] IRAD S3** — 1 open order
- **north american survival systems (#11385)** | Due Apr 24, 2026 | Meredith O'hara Needham | Status: Order Placed | Requester: Joshua Fromm | Tax Exempt: YES | Requested: Apr 22, 2026

### **[300-3] 2026 IDIQ (Hurricane)** — 1 open order
- **Craftcloud for S0 parts (#459340813415)** | Due Apr 23, 2026 | Meredith O'hara Needham | Status: Order Placed | Requester: Joshua Fromm | Tax Exempt: YES | Requested: Apr 21, 2026

### **[001-1] IRAD General** — 2 open orders
- **Digikey (db9) (#98825513)** | Due Apr 25, 2026 | Meredith O'hara Needham | Status: Order Shipped | Requester: Nate | Tax Exempt: NO | Requested: Apr 22, 2026
- **Amazon Shop supplies** | Due Apr 23, 2026 | Meredith O'hara Needham | Status: Order Shipped | Requester: Nate | Tax Exempt: NO | Requested: Apr 21, 2026

### **General Sales** — 1 open order
- **sendcutsend for s3 parts / sales (SW02L252)** | Due Apr 22, 2026 | Meredith O'hara Needham | Status: Order Shipped | Requester: Joshua Fromm | Tax Exempt: NO | Requested: Apr 21, 2026

## Task Summary
- **Total tasks:** 7 open, 0 completed (100% open rate; recovered from 2 open tasks in prior snapshot)
- **Tasks by assignee:**
  - Meredith O'hara Needham: 6 tasks (86% of workload)
  - Nate Straus: 1 task (14% of workload)
  - Unassigned: 0 tasks
- **Order status breakdown:**
  - Order Placed: 2 tasks (29%)
  - Order Shipped: 4 tasks (57%)
  - Order Received: 1 task (14%)
- **Notable patterns:**
  - **Meredith concentration:** 6 of 7 tasks assigned to Meredith. Nate Straus assigned only ReadyMadeRC (status: Order Received), suggesting possible hand-off for receiving verification or intake processing.
  - **Shipped orders remain open:** 4 tasks marked "Order Shipped" are still in open queue (Jawstec, sendcutsend, Digikey, Amazon). Indicates either: (a) awaiting receipt confirmation before closure, (b) missing closure workflow, or (c) intentional hold for inventory reconciliation.
  - **Project distribution:** Mustang Pt. 2 (29%), IRAD General (29%), IRAD S3 (14%), Hurricane IDIQ (14%), General Sales (14%).
  - **Tax exemption:** 2 tasks marked "Tax Exempt: YES" (north american survival systems for IRAD S3, Craftcloud for Hurricane IDIQ).
  - **Compressed due dates:** All orders due within 3 days (Apr 22–25); requested dates span Apr 17–22 (standard 2–5 day lead times).

## Recent Activity
- **Task recovery:** 7 open tasks reappeared after prior snapshot showed 2 open. 
  - **Matching prior "disappeared" orders:** Current snapshot includes Jawstec (#68200), sendcutsend (SW02L252), Digikey (#98825513), north american survival systems (#11385), Amazon Shop supplies, and ReadyMadeRC — **all 6 orders that were reported as absent in prior snapshot now visible again.**
  - **Hypothesis:** Tasks were archived (possibly auto-deleted per form submission notice) and recently restored, OR prior snapshot missed active orders due to filter/view issue. **Confirm with Meredith whether these were closed and reopened, or remained active but hidden.**
- **Status shift on Digikey order:** Prior snapshot showed IRAD General Digikey order as "Order Placed"; current snapshot shows "Order Shipped" — order advanced, but task remains open (no closure).
- **Nate Straus assigned ReadyMadeRC (Order Received):** First appearance as assignee. Task marked "Order Received" (due Apr 25) suggests fulfillment arrived or is imminent; hand-off to Nate may indicate receiving verification step.
- **Jawstec overdue (5-day slip):** Requested Apr 17 for Apr 22 delivery; still "Order Shipped" status and open. **If due date Apr 22 has passed, this order is overdue.**

## Notes & Context

1. **Critical: Shipped and Received orders remain in open queue**
   - 4 tasks are marked "Order Shipped" (Jawstec, sendcutsend, Digikey, Amazon) and 1 marked "Order Received" (ReadyMadeRC), yet all remain in open queue.
   - **This breaks the closure workflow.** Expected behavior: orders shipped → await receipt → close task upon receiving confirmation.
   - **Questions:**
     - Are shipped orders intentionally held open pending physical receipt before closure?
     - Is there a separate receiving/inventory intake process (outside Asana) that will close these tasks?
     - Should these be marked "Complete" once shipped, or is open status tracking receipt verification?
   - **Recommendation:**