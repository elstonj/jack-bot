# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; critical orders due May 1–6, 2026; backlog due Jul 3, 2026
- **Status:** Active — **31 open tasks** (spike from 8 in prior snapshot). Task volume increased significantly; workload remains heavily concentrated on Meredith O'hara Needham. Two distinct deadline tiers: **urgent May 1–6 orders (13 tasks, mostly assigned)** and **backlog Jul 3 orders (18 tasks, mostly unassigned)**. Order fulfillment progressing: 3 tasks show "Order Shipped," 1 shows "Order Received," 23 show "Order Placed" or "Order Placed in Inventory."
- **Team members involved:**
  - Meredith O'hara Needham (processor/project owner; 13 assigned tasks — 41.9% of workload)
  - Nate Straus (receiving/verification; 1 assigned task — 3.2% of workload)
  - Unassigned: 17 tasks (54.8% — significant increase from prior snapshot)
- **Risk signals:**
  - **Task count spike from 8 to 31 (+23 tasks).** Prior snapshot showed only May 1–3 critical orders; this snapshot includes full backlog visible again (18 Jul 3 tasks, unassigned). Suggests intake resumed or earlier Jun 30 backlog reclassified to Jul 3.
  - **Unassigned backlog (18 tasks, 54.8%).** All Jul 3 due date tasks unassigned — potential workflow bottleneck if Meredith must process these after May 1–6 critical orders. No clear assignment plan visible.
  - **Two-tier deadline structure:** May 1–6 (urgent, 13 assigned) vs. Jul 3 (backlog, 18 unassigned) — temporal separation suggests different processing workflows or priority levels.
  - **Meredith bottleneck persists:** 13 of 13 critical May orders assigned to Meredith (100% for urgent tier); Nate handles 1 task only (Amazon XT90, flux pen). If issues arise with May orders, no coverage visible.
  - **Jawstec consolidation incomplete:** 4 Jawstec orders visible across both tiers (#68490, #68514, #68439, #68200, #67125) — vendor appears 5 times in full list; earlier backlog consolidation may not have completed.
  - **Historical request dates past placement windows:** Several unassigned backlog tasks show "When should this order be placed?" dates of Mar 2–30, Apr 14–29, 2026 — already past; status "Order Placed in Inventory" suggests these were placed earlier but remain open in Asana (stale task closure issue).
  - **Approval requirements split:** 2 of 13 critical May orders require approval ([001-7] IRAD S3 tasks: Laser/900MHz BPF, ADS-B for S30002) — potential approval blockers if not expedited.

## Key Deliverables & Milestones

### **Critical Orders — Due May 1–6, 2026** (13 tasks, all assigned to Meredith or Nate)

#### **General Sales (No Specific Project)** — 6 tasks
- **tmotor for s3 sales (2026050283273)** | Due May 3, 2026 | Meredith O'hara Needham | Status: Order Placed | Requester: Joshua Fromm | Tax Exempt: YES
- **jawstec for s3 parts (#68490)** | Due May 3, 2026 | Meredith O'hara Needham | Status: Order Placed | Requester: Joshua Fromm | Tax Exempt: YES
- **pololu for s3 (#1J585099)** | Due May 3, 2026 | Meredith O'hara Needham | Status: **Order Shipped** | Requester: Joshua Fromm | Tax Exempt: YES
- **pcbway for s3 sales (#YX1724706)** | Due May 6, 2026 | Meredith O'hara Needham | Status: Order Placed | Requester: Joshua Fromm | Tax Exempt: YES
- **jawstec for s3 parts (#68439)** | Due May 1, 2026 | Meredith O'hara Needham | Status: **Order Shipped** | Requester: Joshua Fromm | Tax Exempt: YES
- **Amazon XT90, flux pen** | Due May 6, 2026 | Nate Straus | Status: **Order Received** | Requester: Nate | Tax Exempt: NO

#### **[001-7] IRAD S3** — 2 tasks (both require approval)
- **Laser and 900MHz BPF for S30002 (#99012523)** | Due May 6, 2026 | Meredith O'hara Needham | Status: **Order Shipped** | Requester: Sam | **Requires Approval: YES** | Tax Exempt: NO
- **ADS-B for S30002 (#106880)** | Due May 6, 2026 | Meredith O'hara Needham | Status: Order Placed | Requester: Sam | **Requires Approval: YES** | Tax Exempt: NO

#### **[001-4] IRAD S0 VTOL** — 3 tasks
- **Amazon S0 VTOL Instrumenting** | Due May 6, 2026 | Meredith O'hara Needham | Status: Order Placed | Requester: Alex Lomis | Tax Exempt: NO
- **Offshore Electrics optical rpm probes (#100531902)** | Due May 6, 2026 | Meredith O'hara Needham | Status: Order Placed | Requester: Alex Lomis | Tax Exempt: NO (note: field shows "Tyto robotics optical rpm probes" in description)
- **Helidirect eRPM motor probes (#HDR653461)** | Due May 6, 2026 | Meredith O'hara Needham | Status: Order Placed | Requester: Alex Lomis | Tax Exempt: NO
- **Servocity (#300043410)** | Due May 6, 2026 | Meredith O'hara Needham | Status: **Order Shipped** | Requester: Alex Lomis | Tax Exempt: NO

#### **[300-3] 2026 IDIQ (Hurricane)** — 2 tasks
- **sendcutsend order for s0 tooling (#SW65S791)** | Due May 6, 2026 | Meredith O'hara Needham | Status: Order Placed | Requester: Joshua Fromm | Tax Exempt: YES
- **jawstec for s0 parts (#68514)** | Due May 6, 2026 | Meredith O'hara Needham | Status: Order Placed | Requester: Joshua Fromm | Tax Exempt: YES

### **Backlog Orders — Due Jul 3, 2026** (18 tasks, all unassigned)

#### **[043-3] Mustang Pt. 2** — 4 tasks
- **Jawstec (#68200)** | Unassigned | Status: Order Placed in Inventory | Requester: Alex | Tax Exempt: NO
- **JawsTec- Mustang/Chilli/M2 (#68231)** | Unassigned | Status: Order Placed in Inventory | Requester: Ethan Domagala | Tax Exempt: NO
- **ReadyMadeRC- TBS ESCs for Mustang/Chilli/M2 (#420240)** | Unassigned | Status: Order Placed in Inventory | Requester: Ethan Domagala | Tax Exempt: NO
- **KDE