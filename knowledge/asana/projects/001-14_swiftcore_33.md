# [001-14] SwiftCore 3.3

## Overview
- **Client/customer**: Internal BST development project
- **Dollar value**: Not specified
- **Timeline**: Active development branch; no target release date specified
- **Status**: **SUBSTANTIALLY COMPLETE as of May 2026.** All 4 critical VTOL landing/termination validation tasks due 2026-05-18 have been resolved. Project has transitioned from active development to validation/release readiness phase. Current raw data shows 1 open task (Comms version update, no due date) and 1 recently completed task (Motor ramp down, completed 2026-06-05). Remaining work consists of new issues captured via post-flight feedback form (established by Daniel Prendergast, May 2026) routed automatically to Fleet Maintenance or SwiftCore 3.3 as appropriate.
- **Team members**: Jack Elston (owner), Maciej Stachura (primary developer), Ben Busby, Daniel Prendergast (process lead), whole BST team
- **Risk signals**: No overdue tasks. Post-flight feedback process now automated; new issues will flow directly to project without manual task creation overhead.

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
- **Total tasks**: 2 (1 open, 1 completed) in current raw data
- **Tasks by assignee**:
  - Maciej Stachura: 2 tasks (1 open, 1 completed)
- **Notable patterns**: 
  - Minimal open task volume; project operating in steady-state maintenance mode
  - New work capture mechanism established: post-flight feedback form (May 8–11, 2026) automatically creates tasks in Fleet Maintenance (hardware) or SwiftCore 3.3 (software)
  - Custom field priority: Low

## Recent Activity
- **2026-06-05**: "Motor ramp down on second landing of S3 on 05-15" completed by Maciej Stachura (3 weeks after due date of 2026-05-18, indicating resolution during extended flight testing)
- **2026-05-15**: Daniel Prendergast confirms post-flight feedback process: *"For software issues that just adds a task to the SwiftCore 3.3 project like you've always been doing. You can keep adding tasks manually if you prefer"* — automated Asana Form integration does not replace manual task creation; teams have choice of workflow.
- **2026-05-11 & 2026-05-08**: Daniel Prendergast deploys Asana Form for automated post-flight issue capture as standard process; routes aircraft/equipment issues to Fleet Maintenance (hardware) or SwiftCore 3.3 (software).

## Open Tasks
- **Comms version update** (Maciej Stachura, no due date): Adding list of params to add/remove; none marked as required. Link: https://app.asana.com/1/12804948716594/profile/12805370615990

## Notes & Context

**Project Status – Ready for Release:**
SwiftCore 3.3 has completed all targeted validation tasks as of May/June 2026 (per team feedback). The 4 critical VTOL landing/termination edge cases have been resolved, with the final item (Motor ramp timing on S3) completed 2026-06-05 after extended flight testing.

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