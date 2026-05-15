# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project
- **Status:** **MAJOR WORKFLOW DISRUPTION DETECTED.** Raw Asana data now shows 21 open tasks with many reassigned to "Unassigned" and due dates shifted to **July 13, 2026** (bulk change). This contradicts the May 2026 urgent cycle documented in the existing knowledge file. **⚠️ CRITICAL: This appears to be a system reset, bulk task update, or data corruption. The previous May 11–15 Hurricane GCS order cycle and Nate's receiving verification queue are no longer visible in current task statuses.**
  - **Previous status (from existing file):** 15 open tasks, mature two-phase workflow (Meredith: order placement; Nate: receiving/verification), multiple tasks overdue or due within 24–48 hours.
  - **Current status (from new data):** 21 open tasks, most reassigned to Unassigned, statuses changed to "Order Placed in Inventory," all due dates set to July 13, 2026.
  - **Interpretation:** Either (1) a bulk workflow reset occurred (e.g., after May 13–15 deadline passed), (2) tasks were archived and recreated with new timelines, or (3) Asana data is stale. **Recommend immediate clarification with Meredith and Nate.**
- **Team members involved:**
  - Meredith O'hara Needham (2 tasks actively assigned; previously 9)
  - Nate Straus (0 tasks actively assigned; previously 5 with receiving queue)
  - Unassigned (19 tasks — 90% of workload; previously 1)
  - Requesters: Joshua Fromm (10 tasks), Nate (4 tasks), Alex Lomis (4 tasks), Sam (1 task)
- **Risk signals:**
  - **Bulk reassignment to Unassigned:** 19 of 21 tasks now unassigned, suggesting workflow halt or system reset.
  - **Status drift:** All tasks now show "Order Placed in Inventory" or "Order Shipped" but are marked open; no longer tracking receiving/verification phase.
  - **Due date consolidation:** Nearly all tasks now due July 13, 2026 (except 3 due May 14–16); suggests bulk re-dating rather than granular management.
  - **Blocked tasks remain:** jawstec (s3 & s0, #68728) and bhphoto tripods still marked "MULTIPLE PROJECT — PLEASE PROVIDE BREAKDOWN" with no resolution.
  - **Historical items now "in inventory":** Tasks that were marked "Order Received" (Servocity, jawstec s0 parts, Offshore Electrics, jawstec s3) are now "Order Placed in Inventory" — status regression or reclassification.

## Key Deliverables & Milestones

### **Immediate/Recent Cycle (May 2026)** — *Status unclear; see Risk Signals*
From existing knowledge file, critical orders were due:
- **May 13–14:** 7 Hurricane GCS orders (Amazon, Digikey x2, Mouser, RS-Online, DataPro, Startech) — **Status in new data: Unassigned, due July 13**
- **May 14–15:** PCBWay (Alex), jawstec s3 & s0, receiving verification tasks — **Status in new data: Reassigned/Unassigned, due July 13 or May 16**

### **Current Open Tasks (21 total)**
**Note:** New data shows all tasks due July 13, 2026, with "Order Placed in Inventory" status. This represents a significant departure from May urgency documented in existing file.

#### **Assigned to Meredith O'hara Needham (2 tasks)**
1. **Amazon Shop supplies** | Due May 16, 2026 | Status: Order Placed | Project: [001-1] IRAD General | Requester: Nate | Placement target: May 14, 2026
2. **jawstec for s3 & s0 parts (#68728)** | Due May 16, 2026 | Status: Order Placed | Project: MULTIPLE PROJECT — Breakdown required | Requester: Joshua Fromm | Placement target: May 14, 2026 | Tax Exempt: YES
   - **⚠️ BLOCKED:** Requires project breakdown in description.

#### **Unassigned (19 tasks) — Due July 13, 2026**
All show "Order Placed in Inventory" status:

**[300-3] 2026 IDIQ (Hurricane) — 3 tasks**
- Digikey / Hurricane GCS x3 (#99151808) | Requester: Nate | Placement target: May 11, 2026
- RS-Online / Hurricane GCS (#2561507246) | Requester: Nate | Placement target: May 11, 2026
- jawstec for s0 parts (#68514) | Requester: Joshua Fromm | Placement target: May 1, 2026 | Tax Exempt: YES
- sendcutsend order for s0 tooling (#SW65S791) | Requester: Joshua Fromm | Placement target: May 1, 2026 | Tax Exempt: YES

**[001-1] IRAD General — 1 task**
- Startech / Hurricane GCS (#USW554503) | Requester: Nate | Placement target: May 11, 2026

**[001-4] IRAD S0 VTOL — 3 tasks**
- Servocity (#300043410) | Requester: Alex Lomis | Placement target: May 4, 2026
- Helidirect eRPM motor probes (#HDR653461) | Requester: Alex Lomis | Placement target: May 4, 2026
- Offshore Electrics optical rpm probes (#100531902) | Requester: Alex Lomis | Placement target: May 4, 2026

**[001-7] IRAD S3 — 3 tasks**
- PCBWay (#YE1730257) | Due May 14, 2026 | Status: Order Shipped | Requester: Alex | Placement target: May 12, 2026
- north american survival systems (#11385) | Requester: Joshua Fromm | Placement target: Apr 22, 2026 | Tax Exempt: YES
- Laser and 900MHz BPF for S30002 (#99012523) | Requester: Sam | Placement target: May 4, 2026 | Requires Approval: YES

**[001-12] Customer Support — 1 task**
- Hitec (#HVHNB9) | Requester: Nate | Placement target: May 5, 2026

**General Sales (No Specific Project) — 5 tasks**
- sendcutsend for s3 parts / sales (SW02L252) | Requester: Joshua Fromm | Placement target: Apr 21, 2026
- sendcutsend for s3 (#SX79V088) | Requester: Joshua Fromm | Placement target: Apr 30, 2026 | Tax Exempt: YES
- jawstec for s3 parts (#68490) | Requester: Joshua Fromm | Placement target: May 1, 2026 | Tax Exempt: YES
- jawstec for s3 parts (#68439) | Requester: Joshua Fromm | Placement target: Apr 29, 2026 | Tax Exempt: YES
- bearings for s3 (#C80812959) | Requester: Joshua Fromm | Placement target: Apr 30, 2026 | Tax Exempt: YES
- jawstec for s3 (#68473) | Requester: Joshua Fromm | Placement target: Apr 30, 2026 | Tax Exempt: YES

**MULTIPLE PROJECT — Breakdown Required — 1 task**