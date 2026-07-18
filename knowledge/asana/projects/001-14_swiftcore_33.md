# [001-14] SwiftCore 3.3

## Overview
- **Client/customer**: Internal BST development project
- **Dollar value**: Not specified
- **Timeline**: Active development branch; no target release date specified
- **Status**: **SUBSTANTIALLY COMPLETE as of May–June 2026.** All 4 critical VTOL landing/termination validation tasks due 2026-05-18 have been resolved. Project has transitioned from active development to validation/release readiness phase. **Team corrections (May 2026) override stale Asana snapshots (Nov 2023).** Remaining work consists of ongoing issue capture via automated post-flight feedback form (deployed May 2026, routed to Fleet Maintenance or SwiftCore 3.3). Current raw Asana snapshot (Nov 28, 2024) shows only 1 open task.
- **Team members**: Jack Elston (owner), Maciej Stachura (primary developer), Ben Busby, Daniel Prendergast (process lead), whole BST team
- **Risk signals**: No active overdue tasks. Post-flight feedback process operational; new issues flow automatically. Current open task (S10019 autopilot error) requires QC verification and is assigned to Maciej Stachura with no due date.

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
2. Motor ramp timing on repeated landings (S3 aircraft) — **completed 2026-06-05** by Maciej Stachura (3 weeks after original due date 2026-05-18, resolved during extended flight testing)
3. Battery flight termination threshold (S1-22 aggressiveness) — resolved
4. Velocity discontinuity at TRANS2HOVER → LANDING transition — resolved

## Task Summary
- **Total tasks**: 1 open task (as of Nov 28, 2024 snapshot). This represents significant reduction from 80 open tasks in Nov 2023 snapshot.
- **Tasks by assignee (current)**:
  - Maciej Stachura: 1 task (S10019 autopilot error — low takeoff/slow climb)
- **Notable patterns**:
  - Project in steady-state maintenance mode with minimal open task volume
  - Current work captured via automated post-flight feedback form (deployed May 8–11, 2026) creating tasks in Fleet Maintenance (hardware) or SwiftCore 3.3 (software)
  - Manual task creation option remains available per team preference
  - Custom field Priority: Low
  - Custom field Quality Control (QC) Required: Yes (on active task)

## Current Open Work

**S10019 Autopilot Error — Low Takeoff and Slow Rate of Climb**
- **Assignee**: Maciej Stachura
- **Due date**: No due date
- **QC Required**: Yes
- **Work type**: Fix
- **Hardware/Software**: Software
- **Aircraft status**: Up (Operational)
- **Issue**: After hand-launch, S10019 lost altitude and began flying very low (approximately 1 meter off ground) — incomplete task note
- **Status**: Open; awaiting investigation and QC verification

## Recent Activity
- **2026-06-05**: "Motor ramp down on second landing of S3 on 05-15" completed by Maciej Stachura (3 weeks after due date of 2026-05-18, resolved during extended flight testing)
- **2026-05-15**: Daniel Prendergast confirms post-flight feedback routing: *"For software issues that just adds a task to the SwiftCore 3.3 project like you've always been doing. You can keep adding tasks manually if you prefer"*
- **2026-05-14**: Same guidance reiterated by Daniel Prendergast
- **2026-05-11**: Daniel Prendergast deploys Asana Form for automated post-flight issue capture; routes aircraft/equipment issues to Fleet Maintenance (hardware) or SwiftCore 3.3 (software)
- **2023-11-28**: Status snapshot showed 80 open tasks; majority now resolved or transitioned to maintenance workflow

## Work Intake Process
As of May 2026, the team operates on a **hybrid issue capture model**:
- **Automated**: Post-flight feedback form (deployed May 8–11, 2026) routes issues directly to Fleet Maintenance (hardware) or SwiftCore 3.3 (software)
- **Manual**: Team members may continue adding tasks directly if preferred
- **Responsibility**: Daniel Prendergast (process lead) owns form deployment and routing logic

This replaces prior manual task creation, reducing overhead while maintaining visibility into emerging issues.

## Notes & Context
- **Project maturity**: SwiftCore 3.3 has progressed from heavy active development (80+ open tasks in Nov 2023) to a substantially complete, operationally validated system (1 open task as of Nov 28, 2024). All critical VTOL landing and flight termination validation objectives completed by June 2026.
- **Quality assurance**: Current active work includes QC-required fixes (S10019). Aircraft remain operational (status: Up) during validation and refinement phases.
- **Release readiness**: No target release date assigned; milestones remain open pending final hardware/software alignment and community release decision.