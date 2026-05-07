# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; critical orders due May 3–8, 2026; one overdue item (Mar 25, 2026)
- **Status:** Active — **13 open tasks** (increase from 11 in prior snapshot). Significant shift in task assignment: 6 tasks now assigned to Nate Straus (46.2%), 7 to Meredith O'hara Needham (53.8%). Multiple orders already shipped or received; workload distribution improving.
- **Team members involved:**
  - Meredith O'hara Needham (7 tasks — 53.8%)
  - Nate Straus (6 tasks — 46.2%, newly visible in active workload)
  - Requesters: Joshua Fromm, Alex Lomis, Sam, Ethan Domagala, Nate
- **Risk signals:**
  - **One overdue task:** RCDrone.top C-Astral SQA Motors/ESCs (#12503) due Mar 25, 2026 (62+ days past due) — marked "Order Shipped" but remains open. Requires approval. Critical: verify if this was erroneously re-opened or if closure was incomplete.
  - **Approval bottleneck intensified:** 3 of 13 tasks require approval (23.1%); 2 are [001-7] IRAD S3 orders (Laser/BPF, ADS-B), 1 is [001-1] IRAD General (RCDrone.top). Two approval-required orders already show "Order Received" status — may need approval sign-off before closure.
  - **Multiple orders shipped/received but unclosed:** 6 of 13 tasks (46.2%) show "Order Shipped" or "Order Received" status yet remain open. Indicates receiving/verification workflow incomplete or task closure discipline lax.
  - **Nate assignment pattern unclear:** 6 of Nate's 7 tasks are follow-up actions (Laser/BPF shows "Order Received," sendcutsend for s3 shows "Order Received"). Suggests Nate may be handling receiving/verification or approval sign-offs post-shipment.

## Key Deliverables & Milestones

### **Critical Orders — Due May 3–8, 2026** (12 tasks)

#### **[001-7] IRAD S3** — 2 tasks (both require approval)
- **Laser and 900MHz BPF for S30002 (#99012523)** | Due May 8, 2026 | Nate Straus | Status: **Order Received** | Requester: Sam | **Requires Approval: YES** | Tax Exempt: NO
- **ADS-B for S30002 (#106880)** | Due May 6, 2026 | Meredith O'hara Needham | Status: Order Placed | Requester: Sam | **Requires Approval: YES** | Tax Exempt: NO

#### **[001-4] IRAD S0 VTOL** — 4 tasks
- **Offshore Electrics optical rpm probes (#100531902)** | Due May 6, 2026 | Meredith O'hara Needham | Status: **Order Shipped** | Requester: Alex Lomis | Tax Exempt: NO
- **Helidirect eRPM motor probes (#HDR653461)** | Due May 6, 2026 | Meredith O'hara Needham | Status: **Order Shipped** | Requester: Alex Lomis | Tax Exempt: NO
- **Amazon S0 VTOL Instrumenting** | Due May 6, 2026 | Meredith O'hara Needham | Status: **Order Shipped** | Requester: Alex Lomis | Tax Exempt: NO
- **Servocity (#300043410)** | Due May 6, 2026 | Meredith O'hara Needham | Status: **Order Shipped** | Requester: Alex Lomis | Tax Exempt: NO

#### **[300-3] 2026 IDIQ (Hurricane)** — 2 tasks
- **sendcutsend order for s0 tooling (#SW65S791)** | Due May 6, 2026 | Meredith O'hara Needham | Status: Order Placed | Requester: Joshua Fromm | Tax Exempt: YES
- **jawstec for s0 parts (#68514)** | Due May 6, 2026 | Meredith O'hara Needham | Status: Order Placed | Requester: Joshua Fromm | Tax Exempt: YES

#### **General Sales & [001-12] Customer Support** — 4 tasks
- **pcbway for s3 sales (#YX1724706)** | Due May 6, 2026 | Meredith O'hara Needham | Status: Order Placed | Requester: Joshua Fromm | Tax Exempt: YES | Project: General Sales
- **tmotor for s3 sales (2026050283273)** | Due May 3, 2026 | Meredith O'hara Needham | Status: **Order Shipped** | Requester: Joshua Fromm | Tax Exempt: YES | Project: General Sales
- **Hitec (#HVHNB9)** | Due May 7, 2026 | Meredith O'hara Needham | Status: **Order Shipped** | Requester: Nate | Tax Exempt: NO | Project: [001-12] Customer Support
- **sendcutsend for s3 (#SX79V088)** | Due May 8, 2026 | Nate Straus | Status: **Order Received** | Requester: Joshua Fromm | Tax Exempt: YES | Project: General Sales

### **Overdue / Non-Standard Timeline** — 1 task
- **RCDrone.top C-Astral SQA Motors and ESCs (#12503)** | Due Mar 25, 2026 (62+ days overdue) | Meredith O'hara Needham | Status: **Order Shipped** | Requester: Ethan Domagala | **Requires Approval: YES** | Tax Exempt: NO | Project: [001-1] IRAD General
  - **Critical anomaly:** Original placement date May 23, 2026; due date Mar 25, 2026 (inverted logic or data entry error). Now shows "Order Shipped" but remains open with pending approval. **Action: Verify status with Meredith/Ethan immediately — this may be a stale task that should have been closed.**

## Task Summary
- **Total tasks:** 13 open, 0 completed
- **Tasks by assignee:**
  - Meredith O'hara Needham: 7 tasks (53.8%)
  - Nate Straus: 6 tasks (46.2%)
- **Completion rates:** 0% (all open); however, 6 of 13 tasks (46.2%) show "Order Shipped" or "Order Received" status, indicating advanced progress toward closure.
- **Notable patterns:**
  - **Workload distribution improved:** Nate now carries 46.2% of active tasks (up from near-zero in prior snapshot). All 6 Nate tasks relate to receiving/verification or post-placement follow-up (4 show "Order Received," 1 shows "Order Shipped").
  - **Receiving/verification workflow visible:** Nate's tasks (Laser/BPF, sendcutsend for s3) show "Order Received" while Meredith's parallel tasks show "Order Placed" or "Order Shipped." Suggests Nate handles receiving/approval sign-off phase.
  - **Approval bottleneck:** 3 of 13 tasks (23.1%) require approval. Two are [001-7] IRAD S3 (both high-priority); one is [001-1] IRAD General (overdue