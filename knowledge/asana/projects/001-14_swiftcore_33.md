# [001-14] SwiftCore 3.3

## Overview
- **Client/customer**: Internal BST development project
- **Dollar value**: Not specified
- **Timeline**: Active development branch; no target release date specified
- **Status**: **SUBSTANTIALLY COMPLETE as of May–June 2026.** All 4 critical VTOL landing/termination validation tasks due 2026-05-18 have been resolved. Project has transitioned from active development to validation/release readiness phase. **Current snapshot shows 2 open maintenance tasks** related to GCS comms disconnections. These represent normal post-validation issue intake via the automated feedback process deployed May 2026. Remaining work consists of ongoing issue capture and low-priority enhancements.
- **Team members**: Jack Elston (owner), Maciej Stachura (primary developer), Ben Busby, Daniel Prendergast (process lead), whole BST team
- **Risk signals**: No overdue tasks. 2 open QC issues (Xtend GCS comms, Joystick mode GCS disconnection) assigned to Jack Elston with no due dates—both marked operational issues awaiting investigation/fix. These reflect normal maintenance workflow rather than release blockers.

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
- **Total tasks**: 2 open, 0 completed (current snapshot)
- **Tasks by assignee**:
  - Jack Elston: 2 tasks (Xtend GCS comms, Joystick mode GCS disconnection)
- **Notable patterns**:
  - Both open tasks are GCS comms stability issues (`Work Type: Fix`)
  - Both assigned to Jack Elston for investigation
  - Both are operationally low-impact (comms recovered automatically or with workaround)
  - Both have no due dates, consistent with post-validation steady-state issue intake
  - Issues captured via automated feedback process deployed May 2026

## Current Open Work

**1. Xtend GCS losing comms**
- **Assignee**: Jack Elston
- **Due date**: No due date
- **Priority**: Low
- **Aircraft**: S10020
- **Work Type**: Fix
- **Notes**: Xtend ground station lost comms (completely disconnected) at the end of preflighting aircraft during the auto surfaces checks. Fix was for app to be closed and reopened. Appears to be intermittent; only occurred once.

**2. Investigate Joystick mode GCS disconnection - occurred 9/28/26**
- **Assignee**: Jack Elston
- **Due date**: No due date
- **Priority**: Low
- **Aircraft**: S10005
- **Work Type**: Fix
- **Notes**: S10005 briefly disconnected from GCS (GCS 25) when switching to joystick mode. Params immediately started redownloading and issue resolved quickly. Transient issue requiring investigation.

## Recent Activity
- **Current snapshot**: 2 new GCS comms stability tasks assigned to Jack Elston for investigation
- **2026-07-20**: "GPS terminate dives and tries transitioning" completed by Maciej Stachura (original due date 2026-05-18, resolved 2 months later as part of extended VTOL validation phase)
- **2026-06-05**: "Motor ramp down on second landing of S3 on 05-15" completed by Maciej Stachura
- **2026-05-15**: Daniel Prendergast confirms post-flight feedback routing to SwiftCore 3.3 or Fleet Maintenance
- **2026-05-11**: Asana Form deployed for automated post-flight issue capture
- **2023-11-28**: Status snapshot showed 80 open tasks; majority now resolved

## Work Intake Process
As of May 2026, the team operates on a **hybrid issue capture model**:
- **Automated**: Post-flight feedback form routes issues directly to Fleet Maintenance (hardware) or SwiftCore 3.3 (software)
- **Manual**: Team members may continue adding tasks directly if preferred
- **Responsibility**: Daniel Prendergast (process lead) owns form deployment and routing logic

## Notes & Context
- **Project maturity**: SwiftCore 3.3 has progressed from heavy active development (80+ open tasks in Nov 2023) to a substantially complete, operationally validated system. All critical VTOL landing and flight termination validation objectives completed by June 2026.
- **GCS stability**: The 2 current open tasks focus on rare GCS disconnection events. Both show recovery mechanisms in place (automatic param reload, app restart). Neither represents a mission-critical blocker.
- **Current maintenance phase**: The 2 open tasks represent normal post-validation issue capture. Fixes are low-priority stability improvements rather than release blockers.
- **Quality assurance**: System operationally validated; current work consists of GCS comms reliability tuning, parameter handling, and edge-case investigation.
- **Release readiness**: No target release date assigned; milestones remain open pending final hardware/software alignment and community release decision.