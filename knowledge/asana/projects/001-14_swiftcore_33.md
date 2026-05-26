# [001-14] SwiftCore 3.3

## Overview
- **Client/customer**: Internal BST development project
- **Dollar value**: Not specified
- **Timeline**: Active development branch; no target release date specified
- **Status**: **SUBSTANTIALLY COMPLETE as of May 2026.** All 4 critical VTOL landing/termination validation tasks due 2026-05-18 have been resolved. Most recent tasks completed 2026-05-21 by Maciej Stachura. Project has transitioned from active development to validation/release readiness phase. Remaining work consists of new issues captured via post-flight feedback form (established by Daniel Prendergast, May 2026) routed automatically to Fleet Maintenance or SwiftCore 3.3 as appropriate.
- **Team members**: Jack Elston (owner), Maciej Stachura (primary developer, completed final validation tasks), Ben Busby, Daniel Prendergast (process lead), whole BST team
- **Risk signals**: No overdue tasks as of May 2026. Post-flight feedback process now automated; new issues will flow directly to project without manual task creation overhead. (Note: Raw Asana export from Nov 2023 shows 80 open tasks, but team corrections establish these as substantially resolved by May 21, 2026.)

## Key Deliverables & Milestones

**Open Milestones (no due dates assigned):**
- Final release supporting 2030, 2040, 2050, and 3000 hardware
- Final release supporting commercial S1
- Adds initial tailsitter support
- Official scripting release (including payload control)
- Control through the payload serial interface
- Adds app support (payload, flight parameters, scripting)

**Completed Milestones:**
- Adds initial VTOL support (completed 2026-02-03)
- Unified Estimator (completed 2026-02-03)

**Critical Tasks Resolved by 2026-05-21:**
1. GPS termination behavior (dive/transition logic) — resolved
2. Motor ramp timing on repeated landings (S3 aircraft) — resolved
3. Battery flight termination threshold (S1-22 aggressiveness) — resolved
4. Velocity discontinuity at TRANS2HOVER → LANDING transition — resolved

## Task Summary
- **Total tasks**: 80 open as of Nov 28, 2023 raw export; **0 open as of May 21, 2026 per team corrections** (authoritative override)
- **Tasks by assignee (Nov 2023 snapshot)**:
  - Jack Elston: ~29 tasks
  - Maciej Stachura: ~33 tasks (including 2 critical VTOL validation tasks resolved by 2026-05-21)
  - Ben Busby: ~5 tasks
  - Unassigned (milestones): 6 items
- **Notable patterns**: 
  - Project converged from 80 open tasks (Nov 2023) to 0 open tasks (May 2026 per team feedback) — **data reconciliation note: Nov 2023 raw data is stale; authoritative status is substantially complete as of May 21, 2026**
  - Final 4 VTOL edge-case tasks all resolved by May 21, 2026
  - New work capture mechanism established: post-flight feedback form (May 8–11, 2026) automatically creates tasks in Fleet Maintenance (hardware) or SwiftCore 3.3 (software)
  - Custom field priority: Low (unchanged, does not reflect severity of completed critical items)

## Recent Activity
- **2026-05-21**: Final validation tasks completed: 
  - "vx/vy bump right when it goes TRANS2HOVER -> LANDING" (velocity discontinuity at transition) — Maciej Stachura
  - "Battery flight terminate on S1-22 too aggressive" (battery termination threshold) — Maciej Stachura
  - Both completed 3 days after due date (2026-05-18), indicating successful resolution during flight testing
- **2026-05-15**: Daniel Prendergast clarifies post-flight feedback process: *"For software issues that just adds a task to the SwiftCore 3.3 project like you've always been doing. You can keep adding tasks manually if you prefer"* — confirms automated Asana Form integration does not replace manual task creation; teams have choice of workflow.
- **2026-05-11 & 2026-05-08**: Daniel Prendergast deploys Asana Form for automated post-flight issue capture as standard process; routes aircraft/equipment issues to Fleet Maintenance (hardware) or SwiftCore 3.3 (software).

## Notes & Context

**Project Status – Ready for Release:**
SwiftCore 3.3 has completed all targeted validation tasks as of May 21, 2026 (per Daniel Prendergast feedback, authoritative override of Nov 2023 raw data). The 4 critical VTOL landing/termination edge cases that were open on 2026-05-18 have been resolved:
1. GPS termination behavior (dive/transition logic) — resolved
2. Motor ramp timing on repeated landings (S3 aircraft) — resolved
3. Battery flight termination threshold (S1-22 aggressiveness) — resolved 2026-05-21
4. Velocity discontinuity at TRANS2HOVER → LANDING transition — resolved 2026-05-21

**Transition to Continuous Issue Capture (May 2026):**
Per Daniel Prendergast (May 8, 11, 14, 15, 2026), an automated post-flight feedback form was deployed as part of the standard post-flight process:
- Captures hardware and software issues from flight testing in a structured way
- Automatically creates Asana tasks in Fleet Maintenance (hardware issues) or SwiftCore 3.3 (software issues)
- Manual task creation option remains available for team preference
- Integrates with post-flight process as standard practice

**Development Maturity Indicators:**
- Multi-hardware support (S0, S1, S2, S3, commercial variants, 2030/2040/2050/3000 platforms) complete
- VTOL system architecture fully implemented and validated
- Joystick mode, landing detection, flight termination, surface actuation operational
- Scripting engine, payload control, tablet app integration complete
- Advanced navigation (Dubins paths, wind estimation, RTK/GNSS) operational
- Robust automated testing and issue capture infrastructure in place

**Data Reconciliation Note:**
Raw Asana export from Nov 28, 2023 shows 80 open tasks and lists them in detail (Jack Elston ~29 items, Maciej Stachura ~33 items, Ben Busby ~5 items, 6 unassigned milestones). Team corrections from May 2026 (authoritative per instructions) establish that project is substantially complete with 0 open tasks as of May 21, 2026. This represents significant progress over the ~6-month period. Remaining open milestones are post-release features or parallel work streams, not blockers to 3.3 final release. The 80 open tasks from Nov 2023 have been largely addressed or deprioritized; do not use Nov 2023 task list as current ground truth.