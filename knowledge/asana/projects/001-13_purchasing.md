# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; current orders span Mar 2026 - Jun 2026
- **Status:** Active - high operational load with 24 open tasks, 0 completed (100% open rate)
- **Team members involved:** 
  - Meredith O'hara Needham (primary processor - ~11 assigned tasks)
  - Nate Straus (secondary processor - ~5 assigned tasks)
  - ~8 unassigned tasks
- **Risk signals:** 
  - All 24 tasks currently open with no closures (100% backlog rate suggests possible processing bottleneck or workflow issue)
  - Most imminent deadlines: Apr 8-18, 2026 (next 1-2 weeks)
  - Heavy concentration on three core projects (Hurricane S0, NASA S2, IRAD S3) plus emerging Mustang Pt. 2 activity
  - Multiple orders in "Order Received" status but still open (awaiting inventory placement closure)
  - Large cluster of 8 unassigned tasks with Jun 6, 2026 due dates stuck in "Order Placed in Inventory" status

## Key Deliverables & Milestones
This is a purchasing workflow project rather than deliverable-based. It processes structured purchase requests through mandatory Asana forms (auto-delete if form not used).

**Current procurement focus areas:**

- **Hurricane S0 [300-3]:** 6 open orders
  - Digikey electronics (hurricane/GCS parts)
  - Jawstec parts
  - Props (IC-155926)
  - GCS antennas (Amazon)
  - All tax exempt; requester: Joshua Fromm / Nate
  - Due dates: Mar 29 - Apr 17, 2026

- **NASA S2 [212-2]:** 6 open orders
  - Motors (KDE17071)
  - Digikey components
  - Servos (multiple)
  - Cases
  - Tripods
  - SendCutSend fabrication
  - All tax exempt; requester: Joshua Fromm
  - Due dates: Mar 29 - Jun 6, 2026

- **IRAD S3 [001-7]:** 2 open orders
  - Amazon USB A extenders (Volcano payload)
  - Amainhobbies parts
  - Requester: Ethan Domagala / Joshua Fromm
  - Due dates: Apr 15

- **Mustang Pt. 2 [043-3]:** 2 new orders (emerging project activity)
  - SoaringUSA ByLight M2 props
  - Espirit prop hubs
  - Requester: Ethan Domagala
  - Due dates: Apr 17-18, 2026

- **IRAD General [001-1]:** 1 order
  - APC prop + Amazon shop supplies

- **IRAD S1 [001-5]:** 1 order
  - Amazon soft cases (due Jun 13)

- **EMASS Chip Integration [044-1]:** 1 order
  - Raspberry Pi Pico 2 with headers

- **Shop Supplies:** 3 orders
  - Amazon, ST-Links, general supplies

## Task Summary
- **Total tasks:** 24 open, 0 completed (100% open rate indicates potential workflow stall or newly pulled data)
- **Tasks by assignee:**
  - Meredith O'hara Needham: 6 tasks (primary processor, handles near-term orders Mar 29 - Apr 18)
  - Nate Straus: 5 tasks (secondary processor, mostly "Order Received" status Apr 8-18)
  - Unassigned: 13 tasks (majority in "Order Placed in Inventory" status, all due Jun 6 or later)
- **Notable patterns:**
  - **Order status distribution:** 
    - "Order Placed": 6 tasks (most active/immediate)
    - "Order Shipped": 2 tasks (en route)
    - "Order Received": 5 tasks (delivered, awaiting inventory closure)
    - "Order Placed in Inventory": 11 tasks (future-dated, awaiting processing)
  - **Due date clustering:** 
    - Immediate (Mar 29 - Apr 18): 11 tasks assigned to Meredith/Nate
    - Future-dated (Jun 6): 8 unassigned tasks in "Order Placed in Inventory"
    - Outlier: Jun 13 (S1 soft cases)
  - **Tax exemption:** 12 of 24 orders marked tax exempt (government contracts: Hurricane S0, NASA S2, and related)
  - **Primary requesters:** 
    - Joshua Fromm: 13 tasks (Hurricane, NASA, IRAD S3, shop supplies)
    - Ethan Domagala: 5 tasks (Mustang Pt. 2, S3 Volcano, S1, shop supplies)
    - Nate: 4 tasks (Hurricane, IRAD General, shop supplies)
    - Sam: 1 task (ST-Links)
    - Dan Prendergast: 1 task (EMASS Pico 2)

## Recent Activity
**Current operational snapshot (as of data pull):**

**Immediate action items (Mar 29 - Apr 18):**
- Meredith processing 6 tasks: Digikey Hurricane/shop supplies, S0 Digikey order, NASA motor, Digikey GCS parts, APC prop (all with 1-2 week windows)
- Nate processing 5 received orders: NASA S2 Digikey, S0 Digikey, S3 Amainhobbies, M2 props (SoaringUSA & Espirit hubs) awaiting inventory closure

**Future inventory pipeline (Jun 6 due date — 8 unassigned tasks):**
- NASA S2: Tripods, servos (2), case, SendCutSend fabrication
- Hurricane S0: GCS antennas
- IRAD S1: Soft cases
- EMASS: Raspberry Pi Pico 2
- Shop Supplies: Amazon, ST-Links

**Emerging activity:**
- **Mustang Pt. 2 [043-3]:** New airframe project (M2/ByLight) with prop component sourcing (SoaringUSA, Espirit) - assigned to Nate for processing

## Notes & Context

- **Workflow concern:** 100% open rate with 0 completions suggests either:
  - Data pulled during bulk task creation (form submissions)
  - Possible backlog in closing "Order Received" and "Order Placed in Inventory" tasks
  - Recommend verifying whether Meredith/Nate are closing tasks once orders hit inventory vs. leaving them open for tracking

- **Processing bottleneck risk:** 8 unassigned tasks in "Order Placed in Inventory" status all due Jun 6 need assignment to move forward. Likely require inventory receiving/placement by Meredith or Nate before closure.

- **Mandatory form usage:** All purchases must use Asana form or tasks auto-delete per project guidelines (noted in project notes)

- **Order status lifecycle:** 
  1. Order Placed (sourced, awaiting shipment)
  2. Order Shipped (en route)
  3. Order Received (arrived, awaiting inventory placement)
  4. Order Placed in Inventory (stocked, future-dated operations)

- **Project focus concentration:**
  - Hurricane S0 [300-3]: 6 orders (government contract, tax exempt)
  - NASA S2 [212-2]: 6 orders (government contract, tax exempt)
  - Supporting projects: IRAD S3, Mustang Pt. 2, IRAD General, IRAD S1, EMASS, Shop Supplies

- **Vendor ecosystem:** Active sourcing from:
  - Electronics: Digikey, Mouser (not visible in current snapshot)
  - Hobb