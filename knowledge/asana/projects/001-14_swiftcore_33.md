# [001-14] SwiftCore 3.3

## Overview
- **Client/customer**: Internal BST development project
- **Dollar value**: Not specified
- **Timeline**: Active development branch; no target release date specified
- **Status**: **SUBSTANTIALLY COMPLETE as of May–June 2026.** All 4 critical VTOL landing/termination validation tasks due 2026-05-18 have been resolved. Project has transitioned from active development to validation/release readiness phase. **Current snapshot (Nov 2024 or later) shows 2 open maintenance tasks** related to S1-19 GCS communications and V_rate command failures—both operational issues captured from QC flights. These represent normal post-validation issue intake via the automated feedback process deployed May 2026. Remaining work consists of ongoing issue capture and low-priority enhancements.
- **Team members**: Jack Elston (owner), Maciej Stachura (primary developer), Ben Busby, Daniel Prendergast (process lead), whole BST team
- **Risk signals**: No overdue tasks. 2 open QC issues (S1-19 GCS comms, V_rate command) assigned or unassigned with no due dates—both marked "Up (Operational)" and awaiting QC review/fix. These reflect normal maintenance workflow rather than release blockers.

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
  - Jack Elston: 1 task (V_rate command failure)
  - Unassigned: 1 task (S1-19/Mini-GCS Comm Issues)
- **Notable patterns**:
  - Both open tasks are QC-flagged maintenance issues (`QC Required: Yes`)
  - Both marked `Aircraft Status: Up (Operational)` — aircraft remain mission-capable
  - Both are `Work Type: Fix` with no due dates, consistent with post-validation steady-state intake
  - Issues captured via automated feedback process deployed May 2026

## Current Open Work

**1. S1-19/Mini-GCS Comm Issues**
- **Assignee**: Unassigned
- **Due date**: No due date
- **Priority**: Low
- **QC Required**: Yes
- **Hardware/Software**: Software
- **Aircraft Status**: Up (Operational)
- **Work Type**: Fix
- **Notes**: Maintenance issue from QC. GCS would disconnect and time out during preflight wait windows (S1-19). Likely a comms timeout or heartbeat tuning issue.

**2. V_rate command failure**
- **Assignee**: Jack Elston
- **Due date**: No due date
- **Priority**: Low
- **QC Required**: Yes
- **Hardware/Software**: Software
- **VTOL Only**: No
- **Aircraft Status**: Up (Operational)
- **Work Type**: Fix
- **Notes**: Maintenance issue from firmware QC flights on S10011 and S10005. V_rate parameter not settable via flight script or manual comms. Likely a parameter binding or command routing issue in scripting interface.

## Recent Activity
- **Current snapshot** (Nov 2024 or later): 2 new maintenance tasks captured from QC flights, routed via automated feedback process
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
- **Current maintenance phase**: The 2 open QC tasks represent normal post-validation issue capture. Both aircraft remain operational; fixes are low-priority enhancements rather than release blockers.
- **Quality assurance**: Aircraft operationally validated; current work consists of parameter tuning, comms reliability, and scripting interface refinement.
- **Release readiness**: No target release date assigned; milestones remain open pending final hardware/software alignment and community release decision.