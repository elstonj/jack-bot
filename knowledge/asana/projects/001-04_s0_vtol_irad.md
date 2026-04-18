# [001-04] S0 VTOL IRAD

## Overview
- **Client/Customer:** Multiple customers including Barbados, ERAU, NOAA, and Janet
- **Dollar Value:** Not explicitly stated in task data
- **Timeline:** Active project with critical customer deliveries in Q2 2025 (ERAU Apr 30, Barbados/Commercial-Ready Jun 13); extended testing phase through mid-2026
- **Status:** Active (High Priority) — 73% completion rate (95 completed, 35 open tasks). Hover testing initiated late February 2024; transitioning from prototype development to manufacturing/delivery phase with parallel instrumented testing campaign
- **Team Members:** Alex Lomis (primary engineer, project owner), Jack Elston (design/testing), Maciej Stachura (transition testing)
- **Risk Signals:** 
  - 2 critical milestones unassigned with imminent due dates (ERAU Apr 30, 2025; Barbados/Commercial-Ready Jun 13, 2025)
  - Motor imbalance bug unresolved (due 2026-02-20)
  - 27 of 35 open tasks lack due dates, mostly assigned to Alex Lomis (workload concentration)
  - Build-up task unscheduled (due 2026-03-04)
  - **NEW:** 4 major instrumented testing milestones added with 2026 deadlines, all unassigned (Apr 20, Apr 30, May 15, no date) — significant scope addition post-customer delivery phase

## Key Deliverables & Milestones
| Milestone | Due Date | Assignee | Status |
|-----------|----------|----------|--------|
| **ERAU S0 Delivery** | 2025-04-30 | Unassigned | OPEN — critical |
| **Barbados S0 Delivery (1)** | 2025-06-13 | Unassigned | OPEN — critical |
| **First Commercially-Ready S0 VTOL** | 2025-06-13 | Unassigned | OPEN — critical |
| **Visual Observation Bench Test** | 2026-04-20 | Alex Lomis | OPEN — 2 subtasks, both unassigned |
| **Instrumented Bench Test** | 2026-04-30 | Alex Lomis | OPEN — 8 subtasks, all unassigned |
| **Instrumented Flight Test** | 2026-05-15 | Alex Lomis | OPEN — 8 subtasks, all unassigned |
| **Autopilot-Based Bench Test Rig for Future Testing** | No due date | Alex Lomis | OPEN — 2 subtasks, both unassigned |
| **NOAA (2)** | No due date | Alex Lomis | OPEN |
| **Janet (1)** | No due date | Alex Lomis | OPEN |
| S0 VTOL Transition | 2025-04-11 | Jack Elston | ✅ Completed 2025-04-22 |
| Transition Test S1 VTOL | 2024-11-22 | Maciej Stachura | ✅ Completed 2025-01-02 |

## Task Summary
- **Total Tasks:** 130 (39 open, 95 completed) — *+4 new instrumented testing milestones with 20 subtasks added*
- **Completion Rate:** 73%
- **Tasks by Assignee:**
  - **Alex Lomis:** 31 open technical tasks (original) + 4 milestone owner assignments (instrumented testing) = primary workload concentration; 88% of open work
  - **Jack Elston:** 2 open (design updates, Remote ID solution)
  - **Unassigned:** 2 critical Q2 2025 customer milestones + 20 instrumented testing subtasks (2026) + motor imbalance bug fix
- **Due Date Coverage:** Only 12 of 39 open tasks have assigned due dates; 27 tasks (69%) lack deadline visibility

## Recent Activity
**NEW (Feb 21, 2024):** Four major instrumented testing milestones added to project scope, spanning April–May 2026:
- Visual Observation Bench Test (Apr 20)
- Instrumented Bench Test (Apr 30) — includes eRPM sensor selection, Teensy firmware development, 1hr+ sinusoidal testing, log analysis
- Instrumented Flight Test (May 15) — includes flight-capable integration, 30-min hover testing, parachute system investigation & integration
- Autopilot-Based Bench Test Rig (no due date) — includes control surface encoders, current & temperature sensor investigation

All 20 subtasks are unassigned. Combined with parallel customer delivery work (Q2 2025), this represents significant additional scope on already-concentrated workload.

**Earlier Activity Summary (Sept 2024–Jan 2025):**
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
- Parallel instrumented testing campaign (2026) appears to be post-delivery validation/root-cause analysis effort, likely driven by motor imbalance bug and performance validation needs
- Emphasis shifting from core technical development to manufacturing optimization, assembly standardization, regulatory compliance, AND long-term reliability/performance characterization

### Technical Priorities (Open Tasks)

**Tier 1: Q2 2025 Customer Delivery (Critical Path)**
- ERAU S0 Delivery (Apr 30, 2025) — unassigned
- Barbados S0 Delivery (Jun 13, 2025) — unassigned
- First Commercially-Ready S0 VTOL (Jun 13, 2025) — unassigned
- Manufacturing & Assembly Standardization (8 tasks)
- Electronic Integration & Packaging (8 tasks)
- Mechanical Design Evolution (7 tasks)
- Remote ID tag solution (Jack Elston)

**Tier 2: 2026 Instrumented Testing & Validation**
- Visual Observation Bench Test (Apr 20, 2026) — 2 subtasks
  - 15-min sinusoidal command test (visual observation)
  - 15-min crashed flight replay (visual observation)
- Instrumented Bench Test (Apr 30, 2026) — 8 subtasks
  - eRPM sensor & logging device selection
  - Teensy firmware for 9 PWM + 3 eRPM channels to SD card
  - Hardware installation & validation
  - 1hr+ sinusoidal test
  - Log import & autopilot command comparison
  - Repeat testing iteration
- Instrumented Flight Test (May 15, 2026) — 8 subtasks
  - Flight-capable instrumentation integration
  - 30-min bench test with flight-capable S0
  - Log comparison & discrepancy analysis
  - Parachute system investigation (standalone handset trigger)
  - Parachute integration
  - Repeated hover testing with instrumentation & parachute
  - Full S0 VTOL flight test with instrumentation & parachute
- Autopilot-Based Bench Test Rig (TBD, 2026+) — 2 subtasks
  - Automated long-endurance hardware bench testing methodology
  - Additional sensor investigation (encoders, current, temperature)

**Tier 3: Customer Deliverables (No Due Date)**
- NOAA (2 units) — Alex Lomis
- Janet (1 unit