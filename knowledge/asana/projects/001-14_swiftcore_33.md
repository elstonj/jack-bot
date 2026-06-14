# [001-14] SwiftCore 3.3

## Overview
- **Client/customer**: Internal BST development project
- **Dollar value**: Not specified
- **Timeline**: Active development branch; no target release date specified
- **Status**: **SUBSTANTIALLY COMPLETE as of May–June 2026.** All 4 critical VTOL landing/termination validation tasks due 2026-05-18 have been resolved. Project has transitioned from active development to validation/release readiness phase. **Team corrections (May 2026) override stale Asana snapshot (Nov 2023).** Remaining work consists of ongoing issue capture via automated post-flight feedback form (deployed May 2026, routed to Fleet Maintenance or SwiftCore 3.3).
- **Team members**: Jack Elston (owner), Maciej Stachura (primary developer), Ben Busby, Daniel Prendergast (process lead), whole BST team
- **Risk signals**: Raw Asana snapshot (80 open tasks, Nov 2023) is stale; actual current workload much lighter per team feedback. No active overdue tasks. Post-flight feedback process now operational; new issues flow automatically without manual overhead.

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
- **Total tasks**: 80 open in raw Asana snapshot (Nov 2023). **Current reality per team (May–June 2026):** minimal open task volume; project operating in steady-state maintenance mode.
- **Tasks by assignee (from raw Nov 2023 snapshot)**:
  - Jack Elston: ~35 tasks (owner focus: tablet interface, surface control, payloads, diagnostics, integration, comms)
  - Maciej Stachura: ~30 tasks (primary developer: VTOL, scripting, navigation, sensors, control, estimator, flight termination)
  - Ben Busby: ~4 tasks (XML, scripting, logging, commands, comms)
  - Unassigned: 6 milestones
- **Notable patterns**:
  - Raw Asana snapshot is stale (Nov 2023); current work captured via team feedback (May–June 2026)
  - New work capture mechanism: automated post-flight feedback form (deployed May 8–11, 2026) creates tasks in Fleet Maintenance (hardware) or SwiftCore 3.3 (software)
  - Manual task creation option remains available per team preference (Daniel Prendergast, May 15, 2026)
  - Custom field Priority: Low
  - Most tasks lack due dates, consistent with flexible development roadmap

## Recent Activity
- **2026-06-05**: "Motor ramp down on second landing of S3 on 05-15" completed by Maciej Stachura (3 weeks after due date of 2026-05-18, resolved during extended flight testing)
- **2026-05-15**: Daniel Prendergast confirms post-flight feedback routing: *"For software issues that just adds a task to the SwiftCore 3.3 project like you've always been doing. You can keep adding tasks manually if you prefer"*
- **2026-05-14**: Same guidance reiterated by Daniel Prendergast
- **2026-05-11**: Daniel Prendergast deploys Asana Form for automated post-flight issue capture; routes aircraft/equipment issues to Fleet Maintenance (hardware) or SwiftCore 3.3 (software)

## Work Intake Process
As of May 2026, the team operates on a **hybrid issue capture model**:
- **Automated**: Post-flight feedback form (deployed May 8–11, 2026) routes issues directly to Fleet Maintenance (hardware) or SwiftCore 3.3 (software)
- **Manual**: Team members may continue adding tasks directly if preferred
- **Responsibility**: Daniel Prendergast (process lead) owns form deployment and routing logic

This replaces prior manual task creation, reducing overhead while maintaining visibility into emerging issues.

## Open Tasks (Current — From Nov 2023 Snapshot)
80 tasks in Asana. Key categories (likely stale; verify via team feedback for current priorities):

**VTOL/Navigation (Maciej Stachura focus, ~30 tasks):**
- S0 clog detection
- S2 manual takeover bug
- Front motors throttle up after landed mode on S1-22 ground tests
- Increase glide path angles on S0-VTOL for faster landing
- Switching from turnrate to waypoint turns very hard (Dubins recompute issue)
- IAS sensor definition for VTOL
- Set trims for VTOL
- Force transition capability (joystick mode)
- Wind alignment for flight termination and landing
- Remove extra orbit on landing for VTOL
- Pivot/motor feedback during holdRotorsLow phase
- Forward flight yaw damping
- Nav overlap fix
- Nav path generation with overlapping non-fly-through waypoints
- Joystick mode checks (lost comms, takeover bugs)
- Estimator updates for GPS/pressure outage (multirotor)
- Thrust table bug (tilt addition)
- Open-loop control for multirotor termination/landing
- GCS/Tablet failure (2024-04-03) investigation
- Landing detection failure (2024-01-19)
- Flight termination bug (2024-03-08)
- TECS gamma calculations (small angle assumptions)
- Flight timer/engine timer logic check (VTOL conflicts)
- Comms version update
- Joystick mode in lost comms
- Add test sensor app XML for QC flights
- Make sure suggested ECAMS tree is implemented
- Consider timer for flight terminate with ERROR_NO_BATT

**Tablet/Comms/Payload (Jack Elston focus, ~35 tasks):**
- Add description to payload window control documentation
- Set IAS error flag from autopilot, not tablet
- Allow handset throttle after flare
- Actuator values packet ACK but surfaces didn't move
- Deployment tube shouldn't send turn off if flap never closed
- Initial XML load sets surfaces to odd deflections
- Prevent joystick mode activation in climbout
- S00001 takeoff waypoint above max altitude
- Undefined code/variable cleanup (rate limiters, terminate functions)
- PWM channel configuration (S00001)
- Battery error (ERROR_NO_BATTERY) causing missed flight legs
- Surface calibration: can't command past max/min
- Flight plan ACK timing (updates not showing)
- Handset joystick control in lost comms
- Trigger packet logging
- Payload door behavior (pre-flight, calibrate mode)
- Command packet logging optimization
- Roll command logging error on takeoff
- Kill switch activation issue
- Calibrate mode surface range limits
- Joystick takeover bug (2024-05-30, S2)
- Payload shouldn't turn off on lost comms unless flying
- Add system time to all packets
- Dual pitot setup integration
- Backup static pressure sensor alert
- USB bootloader flag for hardware 2050
- Param file backup before comms
- Hot shoe packet logging
- Timer-based trigger verification
- Flight termination fault tree (joystick allowance)
- Controller rate consistency (quad)
- MHP/CAN bus integration
- Sensor startup time/value validation

**Scripting/