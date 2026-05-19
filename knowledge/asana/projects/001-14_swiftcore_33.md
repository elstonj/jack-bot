# [001-14] SwiftCore 3.3

## Overview
- **Client/customer**: Internal BST development project
- **Dollar value**: Not specified
- **Timeline**: Active development branch; no target release date specified
- **Status**: Active development. **CRITICAL UPDATE (May 2026)**: New data shows project has converged to 4 open tasks (down from 78 in Nov 2023), all assigned to Maciej Stachura with due date 2026-05-18. One task completed as of that date. This represents dramatic progress on flight-critical systems since November 2023 snapshot. However, remaining open items all relate to VTOL landing and termination edge cases—core safety systems still in refinement.
- **Team members**: Jack Elston (owner), Maciej Stachura (primary active contributor on current tasks), Ben Busby, whole BST team
- **Risk signals**: All 4 remaining open tasks due 2026-05-18 (same date) and relate to VTOL landing/transition/termination behavior—suggests concentrated final validation push on critical flight modes; GPS termination behavior, motor ramp timing on repeated landings, battery termination aggressiveness, and velocity anomalies during TRANS2HOVER→LANDING transition all require resolution before release

## Key Deliverables & Milestones
**Open Milestones (no due dates assigned):**
- Final release supporting 2030, 2040 and likely 2050 and 3000 hardware
- Final release supporting commercial S1
- Adds initial tailsitter support
- Official scripting release (including payload control)
- Control through the payload serial interface
- Adds app support (payload, flight parameters, scripting)

**Completed Milestones:**
- Adds initial VTOL support (completed 2026-02-03)
- Unified Estimator (completed 2026-02-03)

## Task Summary
- **Total tasks**: 4 open, 1 completed (shown in this snapshot; 376 completed overall from Nov 2023 baseline)
- **Tasks by assignee**:
  - Maciej Stachura: 4 open tasks (100% of current workload; all VTOL landing/termination validation)
  - Jack Elston: No current open tasks in this view
  - Ben Busby: No current open tasks in this view
- **Notable patterns**: 
  - Dramatic task reduction from 78 open (Nov 2023) to 4 open (May 2026) indicates major completion cycle
  - All 4 remaining tasks are high-severity VTOL edge cases: GPS dive/transition logic, motor ramp behavior on repeated landings, battery termination threshold tuning, velocity discontinuity during mode transition
  - All tasks share identical due date (2026-05-18), suggesting final validation sprint or coordinated test campaign
  - Custom field priority: Low (appears inconsistent with severity of remaining open items, same as Nov 2023 snapshot)

## Recent Activity
- **2026-05-18**: One task completed: "Battery 1 launch #4 tried to dubins back to a waypoint for some reason" (Maciej Stachura). Task was due same day it was completed, suggesting real-time issue identification and closure during flight testing.
- **Current open tasks (all due 2026-05-18)**:
  - GPS termination behavior causing dives and attempted transitions (Maciej Stachura)
  - Motor ramp timing issue on second landing of S3 aircraft (05-15 flight) (Maciej Stachura)
  - Battery flight termination thresholds too aggressive on S1-22 (Maciej Stachura)
  - Velocity spike (vx/vy bump) at TRANS2HOVER → LANDING mode transition boundary (Maciej Stachura)

## Notes & Context

**Development Status - Major Progress:**
The 78 open tasks from November 2023 have been reduced to 4 by May 2026. This represents successful completion of the vast majority of SwiftCore 3.3 development work, including:
- Multi-hardware support (S0, S1, S2, S3, commercial variants, 2030/2040/2050/3000 platforms)
- VTOL system architecture (initial support milestones completed Feb 2026)
- Joystick mode, landing detection, flight termination, and surface actuation systems
- Scripting engine, payload control, tablet app integration
- Advanced navigation (Dubins paths, wind estimation, RTK/GNSS)

**Final Validation Focus (May 2026):**
Remaining 4 open tasks all relate to VTOL landing and termination edge cases discovered during flight testing:

1. **GPS Termination Logic**: GPS-based flight termination is triggering dives and attempting transitions—possible conflict between termination policy and mode transition logic, or GPS loss handling during critical phases
2. **Motor Ramp Behavior**: Second landing of S3 aircraft shows improper motor ramp-down—may indicate state machine not properly resetting after first landing cycle or mishandling of repeated landing sequences
3. **Battery Termination Sensitivity**: S1-22 aircraft battery termination triggering too aggressively—threshold tuning or voltage estimation issue under load
4. **Mode Transition Velocity Anomaly**: Velocity spikes (vx/vy bump) at TRANS2HOVER → LANDING boundary—possible estimator discontinuity, control mode mismatch, or acceleration command artifact at transition

**Custom Field Inconsistency Note:**
Priority field remains set to "Low" despite these 4 items being flight-critical and having immediate due dates. This may reflect system configuration rather than actual priority assessment.

**Risk Assessment:**
With only 4 tasks remaining and all due on same date (2026-05-18), the project appears to be in final validation/bug-fix phase. Completion of these items would enable production release. The concentration on VTOL edge cases suggests robust testing infrastructure has been developed and real-world flight testing has uncovered final refinements needed in landing and termination logic—expected outcome of mature development cycle.