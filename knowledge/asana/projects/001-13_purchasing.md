# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; current orders due Apr 12–30, 2026
- **Status:** Active - **6 open tasks**. Queue expanded with new order (rockwest for S3, due Apr 30). One task (jawstec for S0 parts) is in "Order Shipped" status and approaching due date (Apr 12). All others tracking normally on schedule.
- **Team members involved:** 
  - Meredith O'hara Needham (processor/project owner; 2 assigned tasks)
  - Nate Straus (receiving/verification; 4 assigned tasks)
- **Risk signals:** 
  - **CRITICAL:** jawstec for S0 parts (#68057) is **due Apr 12, 2026** with status "Order Shipped" — this is likely **overdue or imminent** (order placed Apr 10; 2-day lead time). Assigned to Meredith; requires immediate verification/closure.
  - Rockwest order (due Apr 30) just entered queue with "Order Placed" status (Meredith); normal progression.

## Key Deliverables & Milestones

### **[300-3] 2026 IDIQ (Hurricane)** — 1 open order
- **jawstec for S0 parts (#68057)** | **Due Apr 12, 2026** ⚠️ | Meredith O'hara Needham | Status: Order Shipped | Requester: Joshua Fromm | Tax Exempt: YES | Requested: Apr 10, 2026

### **[043-3] Mustang Pt. 2** — 1 open order
- **Jawstec (#68200)** | Due Apr 29, 2026 | Nate Straus | Status: Order Received | Requester: Alex | Tax Exempt: NO | Requested: Apr 17, 2026

### **[001-7] IRAD S3** — 1 open order
- **north american survival systems (#11385)** | Due Apr 29, 2026 | Nate Straus | Status: Order Received | Requester: Joshua Fromm | Tax Exempt: YES | Requested: Apr 22, 2026

### **[001-1] IRAD General** — 1 open order
- **Digikey (db9) (#98825513)** | Due Apr 30, 2026 | Nate Straus | Status: Order Received | Requester: Nate | Tax Exempt: NO | Requested: Apr 22, 2026

### **General Sales (No Specific Project)** — 2 open orders
- **sendcutsend for S3 parts / sales (SW02L252)** | Due Apr 29, 2026 | Nate Straus | Status: Order Received | Requester: Joshua Fromm | Tax Exempt: NO | Requested: Apr 21, 2026
- **rockwest for S3 (#Z100698536)** | Due Apr 30, 2026 | Meredith O'hara Needham | Status: Order Placed | Requester: Joshua Fromm | Tax Exempt: YES | Requested: Apr 28, 2026

## Task Summary
- **Total tasks:** 6 open, 0 completed (100% open rate; **increased from 4 in prior snapshot**)
- **Tasks by assignee:**
  - Nate Straus: 4 tasks (67% of workload) — 4 "Order Received" status
  - Meredith O'hara Needham: 2 tasks (33% of workload) — 1 "Order Shipped" (overdue), 1 "Order Placed"
- **Order status breakdown:**
  - Order Received: 4 tasks (67%)
  - Order Shipped: 1 task (17%) — ⚠️ **OVERDUE**
  - Order Placed: 1 task (17%)
- **Notable patterns:**
  - **Queue grew by 2 tasks** since last snapshot (added rockwest for General Sales and jawstec for Hurricane IDIQ).
  - **Jawstec for S0 parts is critical:** Shipped status with Apr 12 due date suggests order cycle complete; needs immediate closure or escalation.
  - **Nate dominates receiving (4 of 6 tasks):** All assigned to "Order Received" status; typical for receiving/verification workflow.
  - **Meredith carries execution risk:** 1 overdue shipping task + 1 new order placed task.
  - **Project distribution:** General Sales (2 orders), [043-3] Mustang (1), [001-7] IRAD S3 (1), [300-3] Hurricane (1), [001-1] IRAD General (1).

## Recent Activity
- **Queue expanded from 4 to 6 tasks:**
  - **NEW:** rockwest for S3 (General Sales) — Order Placed, due Apr 30 | Requested Apr 28 (2-day lead time, Meredith assigned).
  - **NEW (or previously untracked):** jawstec for S0 parts ([300-3] Hurricane) — Order Shipped, due Apr 12 | Requested Apr 10 (2-day order cycle; **now overdue or at deadline**).
  
- **Retained from prior snapshot:**
  - Jawstec (Mustang Pt. 2) — Order Received, due Apr 29 (no change).
  - sendcutsend (General Sales) — Order Received, due Apr 29 (no change).
  - north american survival systems (IRAD S3) — Order Received, due Apr 29 (no change).
  - Digikey (IRAD General) — Order Received, due Apr 30 (no change).

- **⚠️ CRITICAL ACTION REQUIRED:**
  - **jawstec for S0 parts** task is in "Order Shipped" status with a **Apr 12, 2026 due date.** This is either **overdue** (if current date is past Apr 12) or at immediate deadline. Meredith must verify receipt and transition task to closure or escalate if order is delayed.

## Notes & Context

1. **Jawstec vendor appears twice in queue**
   - "Jawstec" (#68200, Mustang Pt. 2, Nate, Order Received, due Apr 29)
   - "jawstec for s0 parts" (#68057, Hurricane IDIQ, Meredith, Order Shipped, **due Apr 12**)
   - Same vendor but different orders/projects/requesters. Not a duplicate; monitor for separate tracking.

2. **Overdue order — immediate escalation needed**
   - **jawstec for S0 parts** requested Apr 10 with 2-day lead time; marked "Order Shipped" with Apr 12 due date.
   - If current date is >= Apr 12, this task requires **immediate verification and closure** or **escalation** if order delayed.
   - Assigned to Meredith (processor); should be flagged for same-day resolution.

3. **New project entry: [300-3] 2026 IDIQ (Hurricane)**
   - First appearance in purchasing queue; indicates Hurricane IDIQ project is actively sourcing parts.
   - jawstec for S0 parts is high-priority (overdue status).

4. **Receiving/verification workflow steady**
   - Nate assigned to 4 "Order Received" tasks; standard progression.
   - Expected closure within 2–3 days as orders arrive/verify.
   - Meredith responsible for order placement and shipping task follow-up.

5. **Form submission compliance maintained**
   - All 6 tasks properly structured with required custom fields (vendor, requester, request date, project, approval, tax exempt).
   - Form link remains: https://form.asana.com/?k=AYO2EiBus4sRY0G_cbPmHw&d=12804948716594

6. **Tax exemption tracking**