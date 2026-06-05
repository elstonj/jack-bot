# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; current cycle showing orders due June 3–6, 2026, with significant backlog of "Order Placed in Inventory" items now showing Aug 3, 2026 due date
- **Status:** **ACTIVE with major structural change.** Current dataset shows **22 open tasks** (up from 17 in prior cycle). ⚠️ **CRITICAL SHIFTS:**
  - **COMPLETE REASSIGNMENT REVERSAL:** The three tasks previously reassigned to Nate Straus with "Order Received" status (pcbway #YX1724706, sendcutsend #SS97A80, batteries #3058) are now **UNASSIGNED** with status changed to **"Order Placed in Inventory"** and due date shifted to **Aug 3, 2026**. This indicates either: (1) orders were not actually received, (2) closure verification failed, or (3) task status was reset. **ESCALATE FOR CLARIFICATION.**
  - **Meredith remains primary executor:** Still carries 9/22 open tasks (41%)
  - **Massive unassigned backlog:** **13/22 tasks (59%) now unassigned** — all with Aug 3, 2026 due date and "Order Placed in Inventory" status. This represents either pending receipt/closure or a system reset.
  - **jawstec #68821 still missing** from prior cycle — no closure documentation.
  - **New tasks added:** jawstec s3 parts (#69104 — General Sales, due June 6), ARK Electronics (#260604 — S0 VTOL, due June 6), and multiple others in June cycle

- **Team members involved:**
  - **Meredith O'hara Needham** (primary assignee; 9/22 open tasks; all near-term June deadlines)
  - **Unassigned:** **13/22 tasks** (59% of workload) — includes previously reassigned items and incoming backlog
  - **Requesters:** Joshua Fromm (10/22 — 45% of all requests), Nate (4/22), Alex (4/22), Ethan (2/22), Sam (2/22)

- **Risk signals:**
  - 🔴 **CRITICAL: Three previously "Order Received" tasks now show "Order Placed in Inventory" with Aug 3 due date:**
    - **pcbway #YX1724706** (originally due May 4 — 90+ days past original date; now Aug 3)
    - **sendcutsend #SS97A80** (originally due May 28; now Aug 3)
    - **batteries #3058** (originally due May 27; now Aug 3)
    - **ACTION REQUIRED:** Verify actual order status in real world. Asana status does not match prior "Order Received" state.
  - 🔴 **CRITICAL: 13/22 tasks (59%) now unassigned** — all backlog items with identical Aug 3 due date and "Order Placed in Inventory" status. Indicates either pending receipt confirmation or mass task reset. **Requires immediate assignment and status verification.**
  - 🔴 **CRITICAL: jawstec #68821 from prior cycle (was due May 22) remains MISSING** — no closure or reference in current dataset. Escalate if order is unresolved.
  - ⚠️ **Form-based auto-deletion persists:** Project notes warn "USE THIS FORM PLEASE OR YOUR TASK WILL AUTO DELETE" — explains task volatility and status resets.
  - ⚠️ **High concentration of near-term deadlines:** 9/22 tasks due June 3–6, 2026; 13/22 deferred to Aug 3 (potential bottleneck).
  - ⚠️ **Requester bottleneck:** Joshua Fromm requesting 10/22 tasks (45%) — monitor for approval/direction delays.

## Key Deliverables & Milestones

### **Immediate Cycle (June 3–6, 2026) — 9 Assigned Tasks**

**[001-7] IRAD S3 — 3 tasks (Meredith)**
1. **jawstec for s3 demo (#69038)** | Due June 3, 2026 | Requester: Joshua Fromm | Status: Order Shipped | Tax Exempt: NO
2. **SendCutSend- S3 Gimbal (SW46G546)** | Due June 4, 2026 | Requester: Ethan | Status: Order Placed | Tax Exempt: NO
3. **jawstec for s3 / murphys pond (#69060)** | Due June 4, 2026 | Requester: Joshua Fromm | Status: Order Shipped | Tax Exempt: NO

**[001-1] IRAD General — 2 tasks**
1. **Amazon S3** | Due June 5, 2026 | Requester: Nate | Status: Order Placed | Tax Exempt: NO | Assigned: Meredith O'hara Needham
2. **Wirecare (#6098749)** | Due June 4, 2026 | Requester: Nate | Status: Order Shipped | Tax Exempt: NO | Assigned: Meredith O'hara Needham

**[001-4] IRAD S0 VTOL — 1 task**
1. **ARK Electronics (#260604)** | Due June 6, 2026 | Requester: Alex | Status: Order Shipped | Tax Exempt: NO | Assigned: Meredith O'hara Needham

**General Sales — 3 tasks (Meredith)**
1. **instrumart for sales (#1083722)** | Due June 5, 2026 | Requester: Joshua Fromm | Status: Order Placed | Tax Exempt: YES
2. **sendcutsend for s3 sales (#SC51C906)** | Due June 5, 2026 | Requester: Joshua Fromm | Status: Order Placed | Tax Exempt: YES
3. **pcbway parts for s3 sales (YW1744139)** | Due June 5, 2026 | Requester: Joshua Fromm | Status: Order Placed | Tax Exempt: YES
4. **jawstec s3 parts (#69104)** | Due June 6, 2026 | Requester: Joshua Fromm | Status: Order Placed | Tax Exempt: YES | Assigned: Meredith O'hara Needham

### **Backlog Cycle (Aug 3, 2026) — 13 Unassigned Tasks** ⚠️

**[001-7] IRAD S3 — 6 tasks (UNASSIGNED)**
1. **sendcutsend for s3 (#SS97A80)** | Originally due May 28 | Status: **Order Placed in Inventory** | 🔴 *Was "Order Received" assigned to Nate; now reset*
2. **Classicmuscleparts / quick-latches (#3001681172)** | Status: Order Placed in Inventory | Requester: Nate
3. **Digikey (#99376023)** | Status: Order Placed in Inventory | Requester: Alex
4. **L-com (#WL5294244)** | Status: Order Placed in Inventory | Requester: Alex
5. **Pasternack (# 393639)** | Status: Order Placed in Inventory | Requester: Alex
6. **sendcutsend for s3 (#S424H298)** | Status: Order Placed in Inventory | Requester: Joshua Fromm

**[300-3] 2026 IDIQ (Hurricane) — 2 tasks (UNASSIGNED)**
1. **Digikey Gateworks / Hurricane GCS (#99157746)** | Status: Order Placed in Inventory | Requester: Nate
2. **Extra Power Switch IC for Hurricane G