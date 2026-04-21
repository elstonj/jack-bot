# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; current orders span Apr 13–22, 2026
- **Status:** Active - **significant backlog re-emergence** (2 open tasks in prior snapshot → 9 open tasks now). All orders in "Order Placed," "Order Shipped," or "Order Received" states, indicating active fulfillment cycle.
- **Team members involved:** 
  - Meredith O'hara Needham (primary processor - 8 assigned tasks)
  - Nate Straus (secondary processor - 1 assigned task)
  - 0 unassigned tasks
- **Risk signals:** 
  - **Dramatic task volume increase:** Prior knowledge file showed 2 open tasks; current snapshot shows 9 open tasks. Suggests new batch of orders submitted or prior tasks re-opened.
  - **Compressed timeline:** All 9 tasks due Apr 19–22, 2026 (within 1 week) — high execution density.
  - **Status progression:** 5 tasks in "Order Placed" (pending vendor confirmation), 3 tasks in "Order Shipped" (awaiting receipt), 1 task in "Order Received" (awaiting inventory intake). All in actionable states.
  - **Mustang Pt. 2 concentration:** 5 of 9 orders (56%) bill to [043-3] Mustang Pt. 2 — single project dependency risk.

## Key Deliverables & Milestones

### **[043-3] Mustang Pt. 2** — 5 open orders
- **JawsTec - Mustang/Chilli/M2 (#68231)** | Due Apr 22 | Meredith O'hara Needham | Status: Order Placed | Requester: Ethan Domagala
- **KDE Direct - Motors for M2/Mustang/Chilli (KDE17135)** | Due Apr 22 | Meredith O'hara Needham | Status: Order Placed | Requester: Ethan Domagala
- **JawsTec (#68200)** | Due Apr 22 | Meredith O'hara Needham | Status: Order Placed | Requester: Alex | *Placed Apr 17*
- **ReadyMadeRC - TBS ESCs for Mustang/Chilli/M2 (#420240)** | Due Apr 22 | Meredith O'hara Needham | Status: Order Shipped | Requester: Ethan Domagala
- **Sendcutsend (#S834G264)** | Due Apr 22 | Meredith O'hara Needham | Status: Order Shipped | Requester: Alex | *Placed Apr 17*

### **[300-3] 2026 IDIQ (Hurricane)** — 1 open order
- **Digikey hurricane / shop supplies (#98710410)** | Due Apr 19 | Meredith O'hara Needham | Status: Order Shipped | Requester: Nate | *Placed Apr 17*

### **[001-7] IRAD S3** — 1 open order
- **Amazon for S3** | Due Apr 22 | Meredith O'hara Needham | Status: Order Placed | Requester: Joshua Fromm | *Placed Apr 20*

### **General Sales (No Specific Project)** — 1 open order
- **SendCutSend for S3 parts / sales (SW02L252)** | Due Apr 22 | Meredith O'hara Needham | Status: Order Placed | Requester: Joshua Fromm | *Placed Apr 21*

### **[001-1] IRAD General** — 1 open order
- **APC prop (#52654)** | Due Apr 22 | Nate Straus | Status: Order Received | Requester: Nate | *Placed Apr 13*

## Task Summary
- **Total tasks:** 9 open, 0 completed (100% open rate)
- **Tasks by assignee:**
  - Meredith O'hara Needham: 8 tasks (89% of workload)
  - Nate Straus: 1 task (11% of workload)
  - Unassigned: 0 tasks
- **Order status breakdown:**
  - Order Placed: 5 tasks (56%) — awaiting vendor confirmation
  - Order Shipped: 3 tasks (33%) — in transit, pending receipt
  - Order Received: 1 task (11%) — awaiting inventory intake
- **Notable patterns:**
  - **Meredith heavily loaded:** 8 of 9 tasks assigned to single team member; potential bottleneck risk if she becomes unavailable.
  - **Mustang Pt. 2 dominance:** 5 orders (56% of total) concentrated on single project; delayed orders from multiple vendors could stall Mustang Pt. 2 build.
  - **Compressed execution window:** All orders due Apr 19–22; order placement dates span Apr 13–21 (9-day submission window suggests batch request).
  - **Tax status:** All 9 tasks marked "NO" for tax exempt — no government IDIQ exemptions flagged in current batch (contrast with prior Hurricane S0 data).
  - **All form-compliant:** All tasks include full custom field data (project, requester, status, due date), suggesting form-driven submission adherence.

## Recent Activity
- **New batch submitted:** 9 orders submitted between Apr 13–21, 2026 (prior snapshot showed only 2 open tasks). Indicates either:
  - Batch order request received from engineering team (Ethan Domagala, Joshua Fromm, Alex, Nate)
  - Prior tasks re-opened due to vendor delays or specification changes
  - System refresh or re-population of prior week's orders
- **Shipment progress:** 3 of 9 orders already shipped (ReadyMadeRC ESCs, Sendcutsend #S834G264, Digikey hurricane supplies) as of current snapshot — rapid vendor fulfillment.
- **Immediate intake workload:** APC prop (Nate's task) already at "Order Received" status; awaiting inventory transaction.

## Notes & Context

1. **Workload concentration risk:** Meredith assigned 8 of 9 tasks (89% of pipeline). If delays occur, consider load balancing to Nate or other team members to maintain throughput.

2. **Mustang Pt. 2 critical path:** 5 concurrent orders (JawsTec ×2, KDE Direct motors, ReadyMadeRC ESCs, Sendcutsend) all due Apr 22. Multiple vendor dependencies; any single vendor delay cascades to build schedule. Recommend:
   - Daily status checks with Meredith through Apr 22
   - Ethan Domagala (primary requester) should have visibility into shipping status
   - Contingency vendor contacts for critical items (motors, ESCs)

3. **Tax exemption discrepancy resolved:** Current batch shows all "Tax Exempt?: NO"; prior knowledge file flagged Hurricane S0 as government IDIQ with 8/12 tax-exempt orders. Current Digikey hurricane order also marked "NO." **Verify whether Hurricane S0 exemption status changed or if this task requires correction** (may impact cost accounting to [300-3]).

4. **Form compliance:** All 9 tasks submitted via Asana form (contain required fields: project, requester, placement date, status, tax flag). Project notes warn of auto-delete for non-compliant tasks — no compliance issues detected.

5. **Data reconciliation note:** Prior snapshot showed 2 open tasks (Digikey, SoaringUSA M2 props). Current snapshot shows 9 open tasks, including the Digikey task (now marked "Order Shipped" vs. prior "Order Placed"). SoaringUSA M2 props task absent from current list — either completed, deleted, or consolidated. No team corrections provided to explain 2→9 task jump; recommend confirming batch order