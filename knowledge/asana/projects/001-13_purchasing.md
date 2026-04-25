# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; current orders due Apr 21–26, 2026
- **Status:** Active - **5 open tasks** (down from 7 in prior snapshot). Mix of statuses: Order Placed (1), Order Shipped (2), Order Received (2). **Task count decline indicates some orders were closed or removed.** Shipped/Received orders remain open — closure workflow issue persists.
- **Team members involved:** 
  - Meredith O'hara Needham (primary processor - 3 assigned tasks)
  - Nate Straus (secondary processor - 2 assigned tasks)
- **Risk signals:** 
  - **Shipped and Received orders still in open queue:** 2 "Order Shipped" (SoaringUSA, Digikey) and 2 "Order Received" (KDE Direct, ReadyMadeRC) remain open. **Closure workflow broken or missing.** Orders should auto-close or have defined receipt verification step.
  - **Meredith workload decreased but still concentrated:** 3 of 5 tasks (60%) assigned to Meredith; Nate now owns 2 of 5 (40%). **Shift toward Nate on received orders suggests he may be handling intake/verification.**
  - **Multiple orders due imminently or overdue:** SoaringUSA (due Apr 21 — TODAY or OVERDUE), north american survival systems (due Apr 24), Digikey (due Apr 25), ReadyMadeRC (due Apr 25), KDE Direct (due Apr 26). **All within 5 days.**
  - **SoaringUSA fuselage order now "Order Shipped" but due TODAY (Apr 21):** Requested Apr 21 for Apr 21 delivery — zero lead time. Status "Order Shipped" suggests it departed vendor; **confirm receipt expected today.**

## Key Deliverables & Milestones

### **[043-3] Mustang Pt. 2** — 3 open orders
- **SoaringUSA - Mustang/M2/Chilli New fuselage** | Due Apr 21, 2026 | Meredith O'hara Needham | Status: Order Shipped | Requester: Ethan Domagala | Tax Exempt: NO | Requested: Apr 21, 2026 | **DUE TODAY (Apr 21) — OVERDUE IF NOT RECEIVED**
- **KDE Direct - Motors for M2/Mustang/Chilli (#KDE17135)** | Due Apr 26, 2026 | Nate Straus | Status: Order Received | Requester: Ethan Domagala | Tax Exempt: NO | Requested: Apr 20, 2026
- **ReadyMadeRC - TBS ESCs for Mustang/Chilli/M2 (#420240)** | Due Apr 25, 2026 | Nate Straus | Status: Order Received | Requester: Ethan Domagala | Tax Exempt: NO | Requested: Apr 20, 2026

### **[001-7] IRAD S3** — 1 open order
- **north american survival systems (#11385)** | Due Apr 24, 2026 | Meredith O'hara Needham | Status: Order Placed | Requester: Joshua Fromm | Tax Exempt: YES | Requested: Apr 22, 2026

### **[001-1] IRAD General** — 1 open order
- **Digikey (db9) (#98825513)** | Due Apr 25, 2026 | Meredith O'hara Needham | Status: Order Shipped | Requester: Nate | Tax Exempt: NO | Requested: Apr 22, 2026

## Task Summary
- **Total tasks:** 5 open, 0 completed (100% open rate; **decreased from 7 in prior snapshot**)
- **Tasks by assignee:**
  - Meredith O'hara Needham: 3 tasks (60% of workload)
  - Nate Straus: 2 tasks (40% of workload)
  - Unassigned: 0 tasks
- **Order status breakdown:**
  - Order Placed: 1 task (20%)
  - Order Shipped: 2 tasks (40%)
  - Order Received: 2 tasks (40%)
- **Notable patterns:**
  - **Task closure gap:** 7 → 5 open tasks. **Closed orders:** Jawstec (was "Order Shipped"), sendcutsend (was "Order Shipped"), Amazon (was "Order Shipped"), and ReadyMadeRC's prior instance (was "Order Received" due Apr 25 — now reappeared with Nate as assignee). **Confirm whether these were intentionally closed or auto-deleted via form submission.**
  - **Workload rebalance:** Nate Straus now assigned 2 of 5 tasks (40%), both marked "Order Received." Suggests Nate is handling **receiving intake/verification workflow** for orders that have arrived.
  - **Meredith owns "Order Placed" and "Order Shipped" tasks:** She retains 3 tasks covering procurement-to-shipment phases; Nate handles post-receipt phase.
  - **Project distribution:** Mustang Pt. 2 (60%), IRAD General (20%), IRAD S3 (20%). **Mustang Pt. 2 dominance — 3 of 5 tasks.**
  - **Tax exemption:** 1 task marked "Tax Exempt: YES" (north american survival systems for IRAD S3).
  - **Compressed due dates:** All orders due within 6 days (Apr 21–26); requested dates span Apr 20–22 (standard 1–5 day lead times).

## Recent Activity
- **Task reduction: 7 → 5 open tasks**
  - **Disappeared orders (likely closed):**
    - Jawstec (#68200) — was "Order Shipped," due Apr 22 (overdue); no longer visible
    - sendcutsend (SW02L252) — was "Order Shipped," due Apr 22; no longer visible
    - Amazon Shop supplies — was "Order Shipped," due Apr 23; no longer visible
    - Craftcloud (Hurricane IDIQ) — was "Order Placed," due Apr 23; no longer visible
  - **Hypothesis:** Orders marked "Order Shipped" were closed after physical receipt (external to Asana), and Craftcloud was cancelled or placed on hold. **Confirm closure with Meredith.**
  
- **New/reappeared orders:**
  - SoaringUSA fuselage (Mustang Pt. 2) — new to current snapshot; due TODAY (Apr 21); "Order Shipped" status suggests vendor shipment in transit or delivered.
  - KDE Direct motors (Mustang Pt. 2) — new to current snapshot; due Apr 26; "Order Received" status (requested Apr 20 — 6-day lead); assigned to Nate (intake verification).
  
- **Assignment shift to Nate Straus:**
  - Nate now owns **both "Order Received" tasks** (KDE Direct, ReadyMadeRC). **Role clarity:** Nate is handling receiving/intake for orders that have arrived. Meredith retains procurement and shipment-phase tasks.
  
- **SoaringUSA order critical:** Due Apr 21 (today), status "Order Shipped" (in transit or arrived). **No slack time — confirm receipt immediately.**

## Notes & Context

1. **CRITICAL: Closure workflow still broken for shipped/received orders**
   - 4 of 5 open tasks are marked "Order Shipped" or "Order Received" yet remain open.
   - Prior snapshot showed same issue; current snapshot confirms it persists despite 3 orders being closed.
   - **Clear pattern:** Orders marked "Order Shipped" → task remains open → eventually closed (likely outside Asana, after physical receipt).
   - **