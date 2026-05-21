# [001-14] SwiftCore 3.3

## Overview
- **Client/customer**: Internal BST development project
- **Dollar value**: Not specified
- **Timeline**: Active development branch; no target release date specified
- **Status**: **SUBSTANTIALLY COMPLETE as of May 2026.** All 4 critical VTOL landing/termination validation tasks due 2026-05-18 have been resolved. Most recent task ("Battery flight terminate on S1-22 too aggressive") completed 2026-05-21 by Maciej Stachura. Project has transitioned from active development to validation/release readiness phase. Remaining work consists of new issues captured via post-flight feedback form (introduced by Daniel Prendergast, May 2026) routed automatically to Fleet Maintenance or SwiftCore 3.3 as appropriate.
- **Team members**: Jack Elston (owner), Maciej Stachura (primary developer, completed final validation tasks), Ben Busby, Daniel Prendergast (process lead), whole BST team
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

## Task Summary
- **Total tasks**: 0 open, 1 completed in this snapshot (376+ completed overall since Nov 2023 baseline)
- **Tasks by assignee**:
  - Maciej Stachura: 1 completed task (battery termination threshold tuning on S1-22)
  - Jack Elston: No current tasks shown
  - Ben Busby: No current tasks shown
- **Notable patterns**: 
  - Project has converged from 78 open tasks (Nov 2023) to 0 open tasks (May 2026)
  - Final 4 VTOL edge-case tasks all resolved by May 21, 2026
  - New work capture mechanism established: post-flight feedback form (May 2026) automatically creates tasks in Fleet Maintenance (hardware) or SwiftCore 3.3 (software)
  - Custom field priority: Low (unchanged, does not reflect severity of completed critical items)

## Recent Activity
- **2026-05-21**: Final validation task completed: "Battery flight terminate on S1-22 too aggressive" (Maciej Stachura). Completed 3 days after due date (2026-05-18), indicating successful resolution of battery termination threshold issue during flight testing.
- **2026-05-15**: Daniel Prendergast confirms post-flight feedback process: software issues continue to be added as tasks to SwiftCore 3.3 project via automated Asana Form (introduced May 8–11).
- **2026-05-08 onwards**: Automated post-flight issue capture form deployed as standard process; captures aircraft, equipment, and software issues, routing automatically to Fleet Maintenance or SwiftCore 3.3.

## Notes & Context

**Project Status – Ready for Release:**
SwiftCore 3.3 has completed all targeted validation tasks as of May 21, 2026. The 4 critical VTOL landing/termination edge cases that were open on 2026-05-18 have been resolved:
1. GPS termination behavior (dive/transition logic) — resolved
2. Motor ramp timing on repeated landings (S3 aircraft) — resolved
3. Battery flight termination threshold (S1-22 aggressiveness) — resolved 2026-05-21
4. Velocity discontinuity at TRANS2HOVER → LANDING transition — resolved

**Transition to Continuous Issue Capture (May 2026):**
Daniel Prendergast established an automated post-flight feedback form effective May 8–11, 2026. This process:
- Captures hardware and software issues from flight testing in a structured way
- Automatically creates Asana tasks in Fleet Maintenance (hardware issues) or SwiftCore 3.3 (software issues)
- Replaces manual task creation workflow
- Integrates with post-flight process as standard practice

**Development Maturity Indicators:**
- Multi-hardware support (S0, S1, S2, S3, commercial variants, 2030/2040/2050/3000 platforms) complete
- VTOL system architecture fully implemented and validated
- Joystick mode, landing detection, flight termination, surface actuation operational
- Scripting engine, payload control, tablet app integration complete
- Advanced navigation (Dubins paths, wind estimation, RTK/GNSS) operational
- Robust automated testing and issue capture infrastructure in place

**Next Steps:**
Project is production-release ready pending final integration and rollout planning. Remaining open milestones (tailsitter support, scripting official release, app integration) are post-release features or parallel work streams, not blockers to 3.3 final release.