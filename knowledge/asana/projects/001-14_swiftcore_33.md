# [001-14] SwiftCore 3.3

## Overview
- **Client/customer**: Internal BST development project
- **Dollar value**: Not specified
- **Timeline**: Active development branch; no target release date specified
- **Status**: **SUBSTANTIALLY COMPLETE as of May–June 2026.** All 4 critical VTOL landing/termination validation tasks resolved by 2026-06-05. Project transitioned to validation/release readiness phase with ongoing refinement work. **Current status (Oct 2026): 1 open task** (pitch instability investigation), **5 recently completed** (nav/landing refinements, sensor fixes). Latest activity: multiple landing and navigation fixes completed 2026-10-09; pitch instability issue opened 2026-10-08.
- **Team members**: Jack Elston (owner), Maciej Stachura (primary developer), Ben Busby, Daniel Prendergast (process lead), whole BST team
- **Risk signals**: 1 active investigation (S10021 pitch instability during hover, possible GPS issue) with no due date assigned. No overdue tasks in current snapshot.

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

**Critical Tasks Resolved by 2026-06-05:**
1. GPS termination behavior (dive/transition logic) — resolved
2. Motor ramp timing on repeated landings (S3 aircraft) — **completed 2026-06-05** by Maciej Stachura
3. Battery flight termination threshold (S1-22 aggressiveness) — resolved
4. Velocity discontinuity at TRANS2HOVER → LANDING transition — resolved

## Task Summary
- **Total tasks**: 1 open, 5 completed (current snapshot)
- **Tasks by assignee**:
  - Maciej Stachura: 1 open, 5 completed (all nav, landing, and sensor refinements)
- **Notable patterns**:
  - Recent work focused on navigation path overlap fixes, landing direction stability, and VTOL sensor support
  - All tasks completed 2026-10-09 (batch refinement day)
  - Pitch instability task (S10021) opened 2026-10-08 but no due date assigned—suggests investigation phase pending diagnostic confirmation

## Recent Activity
- **2026-10-09**: Batch completion of 5 refinement tasks by Maciej Stachura:
  - "Nav makes a bad path when non-fly through waypoints are on top of each other"
  - "Make sure on landing it keeps pointing in the landing direction even outside the wpt_capture_dist"
  - "Implement nav overlap fix"
  - "Increase glide path angles on S0-VTOL for faster landing"
  - "In sensors.cpp, BAD IAS is #defined for only FIXED_WING. Needs VTOL too"
- **2026-10-08**: S10021 pitch instability issue opened — poor pitch stability in joystick hover, lost altitude with forward pitch commands; notes possible GPS-related cause
- **2026-10-05**: "Add forward flight yaw damping" completed by Maciej Stachura
- **Previously (May–June 2026)**: 4 critical VTOL landing/termination validation tasks resolved; project transitioned to refinement phase

## Work Intake Process
As of May 2026, the team operates on a **hybrid issue capture model**:
- **Automated**: Post-flight feedback form routes issues directly to Fleet Maintenance (hardware) or SwiftCore 3.3 (software)
- **Manual**: Team members may continue adding tasks directly if preferred
- **Responsibility**: Daniel Prendergast (process lead) owns form deployment and routing logic

## Notes & Context
- **Project maturity**: SwiftCore 3.3 has progressed from heavy active development (80+ open tasks in Nov 2023) to a substantially complete, operationally validated system. Current work consists of refinement tasks and active flight issue investigation.
- **Current status (Oct 2026)**: 1 open investigation (S10021 pitch instability), likely captured from post-flight feedback. No overdue work.
- **Release readiness**: No target release date assigned; milestones remain open pending final hardware/software alignment and community release decision.
- **Quality assurance**: System operationally validated; continuous refinement based on flight feedback and sensor validation across VTOL and fixed-wing modes.
- **Priority setting**: Low (as of Nov 2023), reflecting mature, stable project status with focused refinement work.