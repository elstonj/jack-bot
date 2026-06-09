# [001-14] SwiftCore 3.3

## Overview
- **Client/customer**: Internal BST development project
- **Dollar value**: Not specified
- **Timeline**: Active development branch; no target release date specified
- **Status**: **SUBSTANTIALLY COMPLETE as of May–June 2026.** All 4 critical VTOL landing/termination validation tasks due 2026-05-18 have been resolved. Project has transitioned from active development to validation/release readiness phase. However, raw Asana data shows 80 open tasks with no due dates and reflects older snapshot (Nov 2023 status update visible). **Team corrections (May 2026) are authoritative and override stale Asana dates.** Remaining work consists of new issues captured via post-flight feedback form (established by Daniel Prendergast, May 2026) routed automatically to Fleet Maintenance or SwiftCore 3.3 as appropriate.
- **Team members**: Jack Elston (owner), Maciej Stachura (primary developer), Ben Busby, Daniel Prendergast (process lead), whole BST team
- **Risk signals**: No overdue tasks. Raw Asana snapshot (80 open tasks) appears stale; actual current workload much lighter per team feedback. Post-flight feedback process now automated; new issues will flow directly to project without manual task creation overhead.

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
2. Motor ramp timing on repeated landings (S3 aircraft) — resolved 2026-06-05
3. Battery flight termination threshold (S1-22 aggressiveness) — resolved
4. Velocity discontinuity at TRANS2HOVER → LANDING transition — resolved

## Task Summary
- **Total tasks**: 80 open (raw Asana data). **Current reality:** minimal open task volume per team feedback; project operating in steady-state maintenance mode.
- **Tasks by assignee (from raw data)**:
  - Maciej Stachura: ~30 tasks (primary developer focus: VTOL, scripting, navigation, sensors, control)
  - Jack Elston: ~35 tasks (owner focus: tablet interface, surface control, payloads, diagnostics, integration)
  - Ben Busby: ~4 tasks (XML, scripting, logging)
  - Unassigned: 6 milestones
- **Notable patterns**: 
  - Raw Asana snapshot appears stale (Nov 2023 visible in status update; current work captured May–June 2026 via team feedback)
  - New work capture mechanism established: post-flight feedback form (May 8–11, 2026) automatically creates tasks in Fleet Maintenance (hardware) or SwiftCore 3.3 (software)
  - Custom field priority: Low
  - Most open tasks lack due dates, consistent with flexible development roadmap

## Recent Activity
- **2026-06-05**: "Motor ramp down on second landing of S3 on 05-15" completed by Maciej Stachura (3 weeks after due date of 2026-05-18, indicating resolution during extended flight testing)
- **2026-05-15**: Daniel Prendergast confirms post-flight feedback process: *"For software issues that just adds a task to the SwiftCore 3.3 project like you've always been doing. You can keep adding tasks manually if you prefer"* — automated Asana Form integration does not replace manual task creation; teams have choice of workflow.
- **2026-05-14**: Daniel Prendergast reiterates same guidance on software issue routing.
- **2026-05-11**: Daniel Prendergast deploys Asana Form for automated post-flight issue capture as standard process; routes aircraft/equipment issues to Fleet Maintenance (hardware) or SwiftCore 3.3 (software).

## Open Tasks (Current)
From most recent team feedback (May 2026):
- **Comms version update** (Maciej Stachura, no due date): Adding list of params to add/remove; none marked as required. Link: https://app.asana.com/1/12804948716594/profile/12805370615990

**Note:** Raw Asana data lists 80 open tasks, but this snapshot predates May 2026 completion milestones and the post-flight feedback process deployment. Many of those tasks may be stale, superseded by flight testing results, or captured in the new automated feedback loop. **Treat current task volume as materially lower than raw count suggests.**

## Notes & Context

**Project Status – Ready for Release (Per Team, May–June 2026):**
SwiftCore 3.3 has completed all targeted validation tasks as of May/June 2026 (per Daniel Prendergast and team feedback). The 4 critical VTOL landing/termination edge cases have been resolved:
- GPS termination behavior (dive/transition logic)
- Motor ramp timing on repeated landings (S3 aircraft, completed 2026-06-05)
- Battery flight termination threshold (S1-22 aggressiveness)
- Velocity discontinuity at TRANS2HOVER → LANDING transition

**Data Quality Note:**
Raw Asana snapshot shows 80 open tasks and Nov 2023 status update, but team feedback from May 2026 indicates the project is substantially complete and in steady-state maintenance mode. Team corrections are authoritative and override the stale Asana task count.

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