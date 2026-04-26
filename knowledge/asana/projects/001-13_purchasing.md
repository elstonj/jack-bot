# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; current orders due Apr 21–26, 2026
- **Status:** Active - **3 open tasks** (down from 5 in prior snapshot). Order status breakdown: Order Shipped (1), Order Received (2). **Significant task reduction suggests orders are being closed externally after receipt.** SoaringUSA fuselage and north american survival systems orders have disappeared from queue — likely received and closed.
- **Team members involved:** 
  - Meredith O'hara Needham (processor - 1 assigned task)
  - Nate Straus (secondary processor - 2 assigned tasks)
- **Risk signals:** 
  - **All 3 remaining orders due within 1–5 days (Apr 25–26):** Digikey (due Apr 25), ReadyMadeRC (due Apr 25), KDE Direct (due Apr 26). **No slack.**
  - **Shipped and Received orders still in open queue:** 1 "Order Shipped" (Digikey) and 2 "Order Received" (KDE Direct, ReadyMadeRC) remain open. **Closure workflow persists as pattern.** Received orders indicate items have arrived but tasks remain open pending verification or intake.
  - **SoaringUSA order (due Apr 21) has been closed:** No longer visible in queue. **Likely received on Apr 21 as scheduled.** Confirms closure pattern: orders marked "Order Shipped" → received physically → task closed externally → removed from Asana queue.
  - **north american survival systems order (due Apr 24) has been closed:** Was "Order Placed" status; now removed. Suggests it was either placed and received, or cancelled/rerouted.

## Key Deliverables & Milestones

### **[043-3] Mustang Pt. 2** — 2 open orders
- **KDE Direct - Motors for M2/Mustang/Chilli (#KDE17135)** | Due Apr 26, 2026 | Nate Straus | Status: Order Received | Requester: Ethan Domagala | Tax Exempt: NO | Requested: Apr 20, 2026
- **ReadyMadeRC - TBS ESCs for Mustang/Chilli/M2 (#420240)** | Due Apr 25, 2026 | Nate Straus | Status: Order Received | Requester: Ethan Domagala | Tax Exempt: NO | Requested: Apr 20, 2026

### **[001-1] IRAD General** — 1 open order
- **Digikey (db9) (#98825513)** | Due Apr 25, 2026 | Meredith O'hara Needham | Status: Order Shipped | Requester: Nate | Tax Exempt: NO | Requested: Apr 22, 2026

## Task Summary
- **Total tasks:** 3 open, 0 completed (100% open rate; **decreased from 5 in prior snapshot**)
- **Tasks by assignee:**
  - Meredith O'hara Needham: 1 task (33% of workload)
  - Nate Straus: 2 tasks (67% of workload)
  - Unassigned: 0 tasks
- **Order status breakdown:**
  - Order Shipped: 1 task (33%)
  - Order Received: 2 tasks (67%)
- **Notable patterns:**
  - **Further workload consolidation:** Nate Straus now owns 67% of tasks (2 of 3), both marked "Order Received." **Nate is handling receiving/intake verification workflow for arrived orders.** Meredith retained only 1 task ("Order Shipped" — in-transit phase).
  - **Project distribution:** Mustang Pt. 2 (67%), IRAD General (33%). **Mustang Pt. 2 heavily weighted; 2 of 3 orders for this project.**
  - **Compressed due dates:** All orders due within 1–5 days (Apr 25–26); requested dates Apr 20–22 (standard 2–6 day lead times).

## Recent Activity
- **Task reduction: 5 → 3 open tasks (2 orders closed)**
  - **SoaringUSA fuselage (Mustang Pt. 2, due Apr 21)** — CLOSED. Was "Order Shipped" status. **Likely received Apr 21 as scheduled and verified by Meredith; task closed and removed from queue.**
  - **north american survival systems (#11385) (IRAD S3, due Apr 24)** — CLOSED. Was "Order Placed" status, assigned to Meredith. **Likely placed and received, or cancelled; task removed from queue.**
  - **Hypothesis confirmed:** Orders transition through Asana (Placed → Shipped → Received) then are closed externally after physical receipt verification, removing them from the task queue. **This is working as intended for closed orders.**
  
- **Nate Straus now owns both "Order Received" tasks:**
  - KDE Direct motors (due Apr 26) — Order Received
  - ReadyMadeRC ESCs (due Apr 25) — Order Received
  - **Role clarity:** Nate handles receiving/intake verification for orders that have physically arrived. Both orders requested Apr 20; due Apr 25–26 indicates 5–6 day lead time from vendor.
  
- **Digikey order (Meredith) critical:** Due Apr 25 (4 days out), status "Order Shipped" (in transit). **No slack time — confirm receipt/delivery within 4 days.**

## Notes & Context

1. **Closure workflow is functioning as designed**
   - Orders are intentionally closed after physical receipt and verification.
   - SoaringUSA and north american survival systems were successfully closed after arrival.
   - Remaining 3 orders on track with 1–5 day delivery windows; closure expected once received.

2. **Nate Straus ownership shift to receiving/verification**
   - Clear role: Nate assigned to "Order Received" tasks (2 of 3 remaining orders).
   - Meredith retains procurement/shipment-phase task (Digikey, "Order Shipped").
   - **Workflow:** Meredith → place order → shipment → Nate (receives & verifies) → closes task.

3. **Project focus remains Mustang Pt. 2**
   - 2 of 3 open orders (67%) are for Mustang Pt. 2 (KDE Direct motors, ReadyMadeRC ESCs).
   - Both assigned to Nate; both "Order Received" status.
   - Ethan Domagala is requester for both.

4. **Form submission reminder in project notes**
   - Project notes explicitly warn: "USE THIS FORM PLEASE OR YOUR TASK WILL AUTO DELETE"
   - Form link: https://form.asana.com/?k=AYO2EiBus4sRY0G_cbPmHw&d=12804948716594
   - **Implication:** Form submissions may trigger auto-deletion of completed orders or create/update tasks. Monitor for unintended task loss via form misconfiguration.