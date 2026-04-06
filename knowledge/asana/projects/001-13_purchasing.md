# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; current orders span Feb 2025 - Jun 2026
- **Status:** Active - extremely heavy operational load with 104 open tasks, 1 completed (99% open rate)
- **Team members involved:** 
  - Meredith O'hara Needham (primary processor - ~60 assigned tasks)
  - Nate Straus (secondary processor - ~35 assigned tasks)
  - ~9 unassigned tasks
- **Risk signals:** 
  - Massive backlog of 104 open purchase requests
  - Many orders with March-June 2026 due dates suggest advance planning or significant project ramp-up
  - Multiple high-approval-threshold orders (Vertiq motors, SKB cases, specialty components)
  - Heavy concentration of orders for three projects (Hurricane S0, NASA S2, IRAD S3)

## Key Deliverables & Milestones
This is a purchasing workflow project rather than deliverable-based. It processes structured purchase requests through mandatory Asana forms (auto-delete if form not used).

**Major procurement focus areas:**
- **Hurricane S0 [300-3]:** Heaviest volume - motors, servos, electronics, fabrication, batteries, props, latches, cables, memory cards, carbon spars
- **NASA S2 [212-2]:** Significant volume - components, cases, batteries, servos, fabrics, tripods, strobes, digikey parts
- **IRAD S3 [001-7]:** Active development purchases - CAN boards, actuator parts, power boards, Vertiq motors, PCB fabrication, RPi components
- **Soil Moisture [001-18]:** Ongoing component sourcing from Amazon, SendCutSend, Jawstec
- **EMASS Chip Integration [044-1]:** New project with Raspberry Pi Pico orders
- **IRAD General [001-1]:** Shop supplies, equipment, tools
- **Shop Supplies:** General inventory across all projects

## Task Summary
- **Total tasks:** 104 open, 1 completed (99% open rate indicates massive operational backlog)
- **Tasks by assignee:**
  - Meredith O'hara Needham: ~60 tasks (primary processor, handles most incoming orders)
  - Nate Straus: ~35 tasks (secondary processor, handles mixed project orders)
  - Unassigned: ~9 tasks (mostly "Order Placed in Inventory" status, awaiting processing)
- **Notable patterns:**
  - **Order status lifecycle:** Order Placed → Order Shipped → Order Received → Order Placed in Inventory
  - **Heavy custom field usage:** Requires Approval (yes/no), Status, Tax Exempt, Name of requester, Project billing
  - **Tax exemption tracking:** Government contracts (NASA S2, Hurricane S0) marked tax exempt; IRAD projects mostly non-exempt
  - **Approval threshold:** Orders >$200 or specialty items (Vertiq motors, SKB cases) require approval
  - **Order status distribution:** Many tasks in "Order Shipped" stage (approaching delivery), some in "Order Placed in Inventory" (future-dated through Jun 2026)
  - **Most active requesters:** Joshua Fromm (Hurricane/NASA work), Sam (IRAD S3 development), Ethan Domagala (Soil Moisture, new components)

## Recent Activity
Current purchasing momentum shows sustained high activity across three core projects:

**Hurricane S0 [300-3]** (Highest priority):
- Extensive ongoing parts sourcing: Digikey electronics, Vertiq motors, Bluebird servos, Craftcloud fabrication, Bisco latches, Jawstec parts, props (IC-155926), cables, memory cards, carbon spars, composite components, batteries (Amprius), MCP components
- Multiple Digikey orders for electronics pipeline
- Status: Orders actively shipping and in inventory
- Requester: Joshua Fromm (primary)

**NASA S2 [212-2]** (Sustained volume):
- Components from Digikey, Jawstec, Pasternack, Aloft, SendCutSend, Mouser
- Servos, batteries, motors (KDE17071), fabrics, cases, strobes, tripods
- Status: Orders shifted to "Order Shipped" and "Order Received" stages
- Requester: Joshua Fromm (primary)

**IRAD S3 [001-7]** (Development-focused):
- CAN board fixes (S3 CAN Fix, S3 CAN Fix 2), actuator board parts, extra DroneCAN boards, S3 power board parts
- Vertiq motors (high-value approval item), Digikey components, SendCutSend fabrication
- SKB cases (approval required), replacement pivots, RPi for Dronecan logger
- Status: Mix of recent shipments and inventory placements
- Requesters: Sam (primary development), Ethan Domagala, Joshua Fromm, Nate Straus

**Soil Moisture [001-18]**:
- Amazon components, SendCutSend, Jawstec parts
- Requester: Ethan Domagala

**New/Emerging**:
- **EMASS Chip Integration [044-1]:** Raspberry Pi Pico 2 orders (Dan Prendergast)
- **USGS Mexico Volcano [350-4]:** Sensors for mission (Joshua Fromm, future-dated)

## Notes & Context
- **Mandatory form usage:** All purchases must use Asana form or tasks auto-delete per project guidelines
- **Order status tracking:** Sophisticated lifecycle from placement through inventory receipt; enables forecasting and supply chain management
- **Vendor ecosystem:** Diverse supplier base including:
  - Electronics: Digikey, Mouser, Pasternack
  - Fabrication: SendCutSend, PCBWay, Craftcloud, Protolabs
  - Specialized parts: Jawstec, RCDrone.top, Aloft Hobbies, Skygeek
  - General supply: Amazon, McMaster-Carr, Powerwerx, Bisco
  - Aerospace/specialty: Vaisala, Amprius, Composite Envisions
- **Project billing discipline:** Careful tracking of which project to bill each purchase; some multi-project orders (McMaster bundles) require breakdown notes
- **Tax exemption strategy:** Government contracts (Hurricane S0, NASA S2) properly flagged tax exempt for cost optimization
- **Approval workflow:** High-value items and specialty components (Vertiq motors S3, SKB cases, specialty fabrication) flagged for approval pathway
- **High-volume requesters:** 
  - Joshua Fromm: Dominates Hurricane and NASA orders (~50+ tasks)
  - Sam: IRAD S3 development and fixes (~15 tasks)
  - Ethan Domagala: Soil Moisture and emerging projects (~15 tasks)
  - Nate Straus: Shop supplies and general inventory (~10 tasks)
- **Massive future pipeline:** Orders extending through June 2026 (9+ months out) indicate:
  - Advance project planning and procurement strategy
  - Potential long-lead-time components being ordered early
  - Or possible workflow bottleneck with orders queuing without closure

**Critical context:** The 104 open tasks with 99% completion rate represents either massive upcoming project execution (Hurricane S0 and NASA S2 ramping hard in March-April 2026) or a processing backlog issue. The volume of "Order Placed in Inventory" items with June 2026 due dates suggests advance inventory planning for Q2 2026 project activity. Recommend monitoring whether tasks are being closed as orders are received/inventoried, or if they're accumulating without resolution.