# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; current orders span Apr 17–24, 2026
- **Status:** Active - **high-volume backlog sustained** (11 open tasks in prior snapshot → 9 open tasks now). All orders in "Order Placed" or "Order Shipped" states, indicating active fulfillment cycle. **Task volume decreased by 2 orders** (likely completed/closed out-of-system).
- **Team members involved:** 
  - Meredith O'hara Needham (primary processor - 9 assigned tasks, 100% of workload)
- **Risk signals:** 
  - **Meredith single-point-of-failure:** All 9 tasks assigned to one person; no backup capacity.
  - **Compressed timeline:** 8 of 9 tasks due Apr 22–24, 2026 (within 3 days); 1 outlier (north american survival systems) due Apr 24 but ordered Apr 22 (possible shipping delay).
  - **Status progression:** 7 tasks in "Order Placed" (pending vendor confirmation), 2 tasks in "Order Shipped" (in transit).
  - **Mustang Pt. 2 concentration:** 4 of 9 orders (44%) bill to [043-3] Mustang Pt. 2 — single project dependency persists but slightly reduced from prior 45%.
  - **Orders closed from prior snapshot:** SoaringUSA fuselage, Craftcloud S0, APC prop, and Amazon shop supplies no longer visible. **Confirm whether completed/received or moved to inventory hold.** Digikey hurricane order from prior snapshot also absent.

## Key Deliverables & Milestones

### **[043-3] Mustang Pt. 2** — 4 open orders
- **JawsTec - Mustang/Chilli/M2 (#68231)** | Due Apr 22 | Meredith O'hara Needham | Status: Order Placed | Requester: Ethan Domagala
- **Jawstec (#68200)** | Due Apr 22 | Meredith O'hara Needham | Status: Order Placed | Requester: Alex
- **KDE Direct - Motors for M2/Mustang/Chilli (KDE17135)** | Due Apr 22 | Meredith O'hara Needham | Status: Order Shipped | Requester: Ethan Domagala
- **ReadyMadeRC - TBS ESCs for Mustang/Chilli/M2 (#420240)** | Due Apr 22 | Meredith O'hara Needham | Status: Order Shipped | Requester: Ethan Domagala
- **Sendcutsend (#S834G264)** | Due Apr 22 | Meredith O'hara Needham | Status: Order Shipped | Requester: Alex

### **[001-7] IRAD S3** — 2 open orders
- **north american survival systems (#11385)** | Due Apr 24 | Meredith O'hara Needham | Status: Order Placed | Requester: Joshua Fromm | **Tax Exempt: YES**
- **amazon for s3** | Due Apr 22 | Meredith O'hara Needham | Status: Order Placed | Requester: Joshua Fromm

### **[001-1] IRAD General** — 1 open order
- **Digikey (db9)** | Due Apr 22 | Meredith O'hara Needham | Status: Order Placed | Requester: Nate

### **General Sales (No Specific Project)** — 1 open order
- **sendcutsend for s3 parts / sales (SW02L252)** | Due Apr 22 | Meredith O'hara Needham | Status: Order Placed | Requester: Joshua Fromm

## Task Summary
- **Total tasks:** 9 open, 0 completed (100% open rate)
- **Tasks by assignee:**
  - Meredith O'hara Needham: 9 tasks (100% of workload)
  - Unassigned: 0 tasks
- **Order status breakdown:**
  - Order Placed: 7 tasks (78%)
  - Order Shipped: 2 tasks (22%)
  - *(Note: All "Order Shipped" orders are KDE Direct and ReadyMadeRC for Mustang Pt. 2 — critical path items in transit)*
- **Notable patterns:**
  - **Meredith exclusively assigned:** All 9 tasks remain with single team member; no capacity distribution. Bottleneck risk is **critical**.
  - **Mustang Pt. 2 concentration:** 5 orders (56% of total) — **increased from 44% when counting 3 shipments plus 2 pending orders**. Ethan Domagala has 3 direct requests; Alex has 2. 
  - **Orders closed from prior snapshot:** SoaringUSA fuselage, Craftcloud S0 (Hurricane IDIQ), APC prop, Amazon shop supplies, and Digikey hurricane order **no longer visible in queue**. Suggests 5 tasks completed, received into inventory, or moved to hold status. **Reconcile with closed task list to confirm completion.**
  - **Tax exemption:** north american survival systems marked "Tax Exempt: YES" (IRAD S3 project exemption confirmed).
  - **Compressed due dates:** 8 of 9 tasks due Apr 22–24; all scheduled to place Apr 17–24. Tight execution window with minimal buffer.

## Recent Activity
- **Task volume decreased:** 11 → 9 open tasks (2 orders closed/resolved). Likely completions:
  - SoaringUSA fuselage (was due Apr 21, earliest deadline)
  - Craftcloud S0 (was due Apr 23, Hurricane IDIQ)
  - APC prop (was due Jun 20, unassigned outlier)
  - Amazon shop supplies (was due Apr 23, IRAD General)
  - Digikey hurricane (#98710410) order from prior snapshot
- **KDE Direct and ReadyMadeRC now shipped:** 3 Mustang Pt. 2 orders (KDE, ReadyMadeRC, Sendcutsend) have transitioned to "Order Shipped" status — critical path components for Ethan Domagala's builds moving on schedule.
- **Digikey db9 order NEW to queue:** Requester Nate, due Apr 22, billed to IRAD General. Appears to be replacement for or separate from prior Digikey hurricane order.
- **north american survival systems NEW to queue:** Requester Joshua Fromm, IRAD S3 project, tax-exempt, due Apr 24 (latest deadline in current batch).
- **No unassigned tasks:** APC prop reassignment resolved (no longer appears in queue).

## Notes & Context

1. **Task closure reconciliation required**
   - 5 orders from prior snapshot (SoaringUSA fuselage, Craftcloud S0, APC prop, Amazon shop supplies, Digikey hurricane) no longer visible.
   - **Action:** Confirm whether closed in Asana (completed/received), moved to separate inventory tracking, or archived. If closed, validate closure dates and receiving documentation to ensure orders integrated into supply chain successfully.

2. **Meredith single-point-of-failure persists**
   - All 9 tasks remain assigned to Meredith O'hara Needham (100% vs 91% in prior snapshot).
   - **Recommendation:** Distribute purchasing workload to secondary approver/processor immediately. Even 20–30% load shift to Joshua Fromm or Nate Straus would reduce bottleneck risk.

3. **Mustang Pt. 2 critical path tightening**
   - 5 concurrent orders (including 3 now shipped) due Apr 22; Ethan Domagala's build timeline dependent on completion.
   - Two orders still in "