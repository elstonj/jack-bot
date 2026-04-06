# [001-04] S0 VTOL IRAD

## Overview
- **Client/Customer:** Multiple customers including Barbados, ERAU, NOAA, and Janet
- **Dollar Value:** Not explicitly stated in task data
- **Timeline:** Active project with key customer deliveries in April–June 2025; several 2026 due dates on open technical tasks indicate timeline extensions
- **Status:** Active (High Priority) — 73% completion rate (95 completed, 35 open tasks). Hover testing initiated late February 2024; transitioning from prototype development to manufacturing/delivery phase
- **Team Members:** Alex Lomis (primary engineer), Jack Elston (design/testing), Maciej Stachura (transition testing)
- **Risk Signals:** 
  - 2 critical milestones unassigned with imminent due dates (ERAU Apr 30, 2025; Barbados/Commercial-Ready Jun 13, 2025)
  - Motor imbalance bug unresolved (due 2026-02-20)
  - 27 of 35 open tasks lack due dates, mostly assigned to Alex Lomis (workload concentration)
  - Build-up task unscheduled (due 2026-03-04)

## Key Deliverables & Milestones
| Milestone | Due Date | Assignee | Status |
|-----------|----------|----------|--------|
| **ERAU S0 Delivery** | 2025-04-30 | Unassigned | OPEN — critical |
| **Barbados S0 Delivery (1)** | 2025-06-13 | Unassigned | OPEN — critical |
| **First Commercially-Ready S0 VTOL** | 2025-06-13 | Unassigned | OPEN — critical |
| **NOAA (2)** | No due date | Alex Lomis | OPEN |
| **Janet (1)** | No due date | Alex Lomis | OPEN |
| S0 VTOL Transition | 2025-04-11 | Jack Elston | ✅ Completed 2025-04-22 |
| Transition Test S1 VTOL | 2024-11-22 | Maciej Stachura | ✅ Completed 2025-01-02 |

## Task Summary
- **Total Tasks:** 130 (35 open, 95 completed)
- **Completion Rate:** 73%
- **Tasks by Assignee:**
  - **Alex Lomis:** 31 open (88% of open work), vast majority of completed tasks — clear workload concentration and critical bottleneck
  - **Jack Elston:** 2 open (design updates, Remote ID solution)
  - **Unassigned:** 2 critical milestones + motor imbalance bug fix
- **Due Date Coverage:** Only 8 of 35 open tasks have assigned due dates; 27 tasks (77%) lack deadline visibility

## Recent Activity
**Status Update (Feb 21, 2024):** Hover testing to begin following week. Project flagged as high priority with yellow status indicator.

**Recent Completions (Sept 2025 – Jan 2025):**
- ESC programming (10-min inactivity beep removal, capacitor re-soldering) — Jul 2025
- Kit component determination & carry case orders — May–Jul 2025
- S0 VTOL Transition milestone — Apr 2025
- Hub board updates & motor mount improvements (single bushing design) — Mar–Apr 2025
- CAN wiring redesign & ESC distribution board integration — Feb–Mar 2025
- AP power board testing & ESC overheating resolution — Sep–Oct 2024
- NDAA-compliant component sourcing (servo, ESC) — Oct–Nov 2024
- Motor mount redesigns, waterproofing improvements, ADONIS integration — Oct–Nov 2024

## Notes & Context

### Project Phase
- **IRAD (Internal R&D)** transitioning from prototype to early production with commercial customer deliveries Q2 2025
- Emphasis shifting from core technical development to manufacturing optimization, assembly standardization, and regulatory compliance

### Technical Priorities (Open Tasks)
1. **Manufacturing & Assembly Standardization** (8 tasks)
   - Assembly guides and wiring channel integration
   - Drill jigs for motor boom alignment
   - Wire harness improvements (color-coding, straightening, routing)
   - Sonde breakout board redesign (single combined version for VTOL/Air-Deployed)

2. **Electronic Integration & Packaging** (8 tasks)
   - Autopilot mounting component (consolidate IR, Radar, Remote ID power)
   - ESC telemetry reading (temperature monitoring)
   - AP power connections (solid-core wire, wire bulkhead standardization with Josh)
   - Wire splitter PCB design (tiny solderable multi-row design)
   - ESC breakout board signal wire routing to prevent spar interference

3. **Mechanical Design Evolution** (7 tasks)
   - Aileron control horn mount improvement
   - Non-yellowing nose material for S0
   - Radar-based landing (replace laser to free fuselage space)
   - AP mounting methods (move away from nose bonding dependency)
   - Autopilot-to-airframe attachment improvements
   - Dual GPS accommodation & rear motor concerns
   - Battery pack configuration (4s2p vs 2x2 design options)

4. **Sensor & Compliance** (2 tasks)
   - Remote ID tag solution (Jack Elston)
   - IR surface temperature necessity evaluation

5. **Unresolved Technical Issues** (2 critical)
   - Motor imbalance bug investigation (due 2026-02-20) — **unassigned**
   - Build-up another S0-VTOL (due 2026-03-04) — **unassigned**

### Key Technical Decisions Made
- **Servo/Actuator:** Switched to KST servo (NDAA-compliant, waterproof options identified)
- **ESC Integration:** CAN-PWM logic consolidated onto breakout board; dual-channel capability for telemetry
- **Power System:** Transitioned to AP power board design; evaluated Amprius cells (SA17/SA03/SA08); thermal pad on heatsink (moved from bonding)
- **Wiring:** CAN network simplified; UART expansion for Remote ID resolved
- **Battery:** 4s2p standard; exploring 2x2 alternative for balance without split design

### Manufacturing Readiness Indicators
- Kit component list completed (charger parts, tablet, spare props)
- Motor mounts refined to single bushing with reamable plastic contact
- Wing lock mechanism standardized (aligned with Josh's S3 design)
- Carry cases ordered/adapted for new design
- CG markings applied (+/- 10% center point limits)
- Component sampling via CraftCloud3D in progress

### Risk & Dependency Notes
- **Critical path risk:** Two major milestones (ERAU, Barbados, Commercial-Ready) have zero assignee coverage despite Apr–Jun 2025 due dates
- **Workload concentration:** Alex Lomis owns 88% of remaining work with no identified backup
- **Design freeze risk:** 27 open tasks lack deadlines; unclear which technical items are prerequisites for customer deliveries vs. post-delivery refinement
- **Regulatory compliance:** Remote ID solution in-progress (Jack); NDAA-compliant components sourced but integration ongoing
- **Supplier dependencies:** ADONIS integration ongoing; CraftCloud3D sampling; polyjet supplier transition completed

### Quality & Refinement Focus
- Waterproofing improvements across tail servos, linkages, power button
- Assembly ergonomics (top opening enlargement, wiring guides, straightened harnesses)
- Thermal management (ESC overheating resolved; AP FET heating addressed)
- Structural fit optimization (tail OD tuning, air gap creation for tail fin axle)

---

**Overall Assessment:** S0 VTOL is in critical delivery phase. Three major customer milestones due Q2 2025 are currently unassigned while Alex Lomis carries 88% of remaining technical work. Motor imbalance bug and build-up task are deferred to 2026. Success depends on either rapid task assignment/delegation or elimination of non-critical 2025 features.