_Asana snapshot as of 2026-10-29: 39 open tasks, 0 completed (last 90 days)._

# [001-04] S0 VTOL IRAD

## Overview
- **Owner:** Alex Lomis
- **Team:** BST (Whole Team)
- **Status:** Active (in development; hover testing planned to begin week of Feb 26, 2024)
- **Priority:** Low
- **Dollar Value:** Not specified in project data
- **Timeline:** 
  - Status update: Feb 21, 2024
  - Key testing milestones: 2026 (Visual Observation Bench Test Apr 30, Instrumented Bench Test May 15, Instrumented Flight Test Jun 5)
  - Deliveries: ERAU (Apr 30, 2025), Barbados (Jun 13, 2025)

## Key Deliverables & Milestones
- **New Power Board** (Jack Elston) — Due date TBD
- **Hover Test With Updated Avionics** (Alex Lomis) — Due date TBD; ready to begin week of Feb 26
- **Visual Observation Bench Test** (Alex Lomis) — Due Apr 30, 2026
  - 15 min sinusoidal command test (visual observation)
  - 15 min crashed flight replay (visual observation)
- **Instrumented Bench Test** (Alex Lomis) — Due May 15, 2026
  - Select eRPM sensors and logging device
  - Write Teensy firmware for 9 PWM + 3 eRPM logging
  - Install, validate, and run 1hr+ sinusoidal test
  - Log analysis and repeat testing
- **Instrumented Flight Test** (Alex Lomis) — Due Jun 5, 2026
  - Integrate instrumentation into flight-capable S0
  - Ground and flight testing with instrumentation
  - Investigate and integrate parachute recovery system
  - Full flight test validation
- **Autopilot-Based Bench Test Rig for Future Testing** (Alex Lomis) — Due date TBD
- **ERAU S0 Delivery** — Due Apr 30, 2025
- **Barbados S0 Delivery (1)** — Due Jun 13, 2025
- **NOAA (2)** (Alex Lomis) — Due date TBD

## Task Summary
- **Total tasks:** 39 open, 0 completed
- **Primary assignee:** Alex Lomis (dominates task list with design, integration, and testing work)
- **Secondary assignee:** Jack Elston (Power Board, Remote ID, design updates)
- **Unassigned:** ISR Payload, most bench/flight test subtasks, both delivery milestones
- **Completion rate:** 0% (no tasks closed as of data snapshot)
- **Notable pattern:** Heavy concentration of unassigned work in the instrumented bench/flight test pipelines despite these being critical path items

## Recent Activity
- **Feb 21, 2024:** Status update posted; two tasks marked completed (links provided but details not shown)
- **Immediate next step:** Hover testing scheduled for week of Feb 26, 2024
- No other recent activity visible in task list

## Notes & Context
- **Risk signals:** 
  - Task "Identify motor imbalance bug" is overdue (due Feb 20, 2026 — likely a typo for 2024, making it past due as of Feb 21)
  - "Build up another S0-VTOL" due Mar 4, 2026 (likely also a typo; possibly Mar 2024) is approaching
  - Many critical testing subtasks (instrumented bench/flight) are unassigned with no due dates, despite milestone parents having 2026 deadlines
  - Large backlog of design/integration tasks (wire management, autopilot mounting, sonde redesign, etc.) assigned to Alex Lomis with no due dates; unclear priority relative to near-term hover testing

- **Project structure:** Organized as nested milestones + supporting engineering tasks; appears to be a phased development (bench test → instrumented bench → flight → delivery)
- **Custom field:** Priority marked "Low" — may not reflect actual urgency given delivery commitments in 2025
- **Clients implied:** ERAU, Barbados, NOAA (from delivery milestone names)