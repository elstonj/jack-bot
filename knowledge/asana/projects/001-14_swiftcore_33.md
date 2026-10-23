# [001-14] SwiftCore 3.3

## Overview
- **Client/customer**: Internal BST development project
- **Dollar value**: Not specified
- **Timeline**: Active development branch (develop); no target release date specified
- **Status**: **ACTIVE DEVELOPMENT.** As of Nov 28, 2023: **14 open tasks, 21 completed**. Project shows ongoing simulator-driven bug intake and resolution across autopilot, ground station, and tablet code. Note: timestamp inconsistency in raw data (Nov 2023 status vs. Oct 2026 task completion dates) suggests data import lag or concurrent development cycles. Current work dominated by S3/S2 simulator sensor/flight logic issues, UI state management bugs in ground station app, and mission planning edge cases.
- **Team members**: Jack Elston (owner), Maciej Stachura (primary developer), Ben Busby (tablet/GCS app), BST team
- **Risk signals**: 
  - **14 open tasks with no due dates** — work is unscheduled; priority custom field marked "Low," but many represent flight-critical behavior
  - **4 UI state bugs** (Ben Busby, Ready for Testing status): user mode changes during flight can lock out aircraft control window, telemetry menu, and nav-way app until app restart
  - **6 S3 sensor loss scenarios** (Maciej Stachura): GPS, pitot (clogged/loss), mags, static pressure — all marked "unexpected response" with no clarity on intended behavior
  - **3 mission planning bugs**: waypoint skip (SIM-0025), Dubins path fishhook artifact (SIM-0019), goto failure with point under aircraft (SIM-0021)
  - **Lost comms joystick mode** not yet validated (Maciej Stachura)

## Key Deliverables & Milestones

**Open Milestones:**
- Adds initial VTOL support (unassigned, no due date) — related tasks: fishhook artifact in Dubins path (SIM-0019), lost comms joystick check

**Completed Milestones (Oct 2026):**
- Multiple S3 simulator robustness items: killed engine stall response, climbout clogged pitot, ground contact carry-over, BAD IAS false alarm at altitude (all Maciej Stachura, 2026-10-22)
- Preflight check validation: landing plan altitude warning, mission start waypoint autocheck, zero sensors warning (all Ben Busby, 2026-10-23)
- Communications & actuator fixes: Xtend GCS comms loss, PWM channel config, actuator values ACK bug (Jack Elston, 2026-10-22)
- Flight mode transitions: joystick takeover, manual takeover, landing plan switch, turnrate/waypoint transition (Maciej Stachura, 2026-10-22)

## Task Summary
- **Total tasks**: 14 open, 21 completed (Nov 28, 2023 snapshot; data current through Oct 2026 activity)
- **Tasks by assignee**:
  - **Maciej Stachura**: 9 open (6 S3 sensor loss, 1 waypoint skip, 1 fishhook artifact, 1 goto failure, 1 lost comms joystick check); 14 completed
  - **Ben Busby**: 4 open (all UI state bugs: aircraft control window, telemetry menu, user mode mode/app opening race conditions); 3 completed
  - **Unassigned**: 1 open (VTOL support milestone)
  
- **Notable patterns**:
  - **UI stability issue cluster**: 4 of 14 open tasks are ground station app state management bugs under Ben Busby, all marked "Ready for Testing" on release/3.3.0 branch — suggests these may be pre-release validation findings
  - **Sensor failure focus**: 6 of 9 Maciej tasks are S3 simulator sensor loss/degradation (GPS, pitot, mags, static pressure) — shifted to broader mission planning bugs (waypoint skip, Dubins artifact, goto failure)
  - **VTOL emergence**: New theme in open work (fishhook artifact, lost comms joystick) aligns with open VTOL support milestone
  - **Completion velocity**: 21 completed tasks in same period shows high resolution rate; most recent activity 2026-10-22 to 2026-10-23

## Recent Activity
**Completed (2026-10-22 to 2026-10-23):**
- **Preflight validation** (Ben Busby, 3 tasks): fixed landing plan altitude warning display, mission start waypoint autocheck behavior, zero sensors warning visibility — all marked "Ready for Testing" (SIM-0029)
- **S3 sensor robustness** (Maciej Stachura, 2 tasks): killed engine stall response, climbout clogged pitot
- **S3 model builder**: ground contact carry-over for belly/tail-fin (prevents loss on S3.xml regeneration)
- **S3 dynamics**: BAD IAS false alarm at 4–5 km altitude (SIM-0028) — confirmed no active simulator faults
- **Communications**: Xtend GCS comms loss during auto surfaces check (Jack Elston); PWM channel config issue S00001 (Jack Elston)
- **Flight dynamics**: joystick takeover on tablet (S2), manual takeover bug, landing plan spiral switch, turnrate/waypoint turn recomputation (Maciej Stachura)
- **Actuator control**: surfaces not responding to ACKed packet (Jack Elston)
- **Flight termination & sensor dropout**: flight terminate bug S10011 (2024-03-08), dynamic pressure dropout with IAS freeze (SIM-0040), unprompted dynamic pressure error cleared on descent/climb (SIM-0022)

**Unresolved open issues:**
- **UI app state**: User mode changes during flight lock out aircraft control window, telemetry menu, and nav-way app — requires full app exit (not close) to recover (4 tasks, Ben Busby, SIM-0017, SIM-0030)
- **Mission planning**: Waypoint skip (9→11, missed 10 on northbound leg, SIM-0025), Dubins path fishhook artifact before initial VTOL holding loop (SIM-0019), goto failure under aircraft (SIM-0021)
- **S3 sensor loss**: 6 open tasks (GPS loss in flying mode joystick lockup, clogged pitot, pitot loss, mags loss, static pressure loss on climbout) — all marked "unexpected response"; no clarity on intended behavior or acceptance criteria
- **Lost comms validation**: joystick mode behavior in lost comms scenario (VTOL test QC plan context)

## Notes & Context
- **Data timestamp anomaly**: Status update dated Nov 28, 2023 but task completion dates Oct 2026 (same pattern as prior knowledge file). Task dates (Oct 2026) are authoritative work timeline.
- **Simulator-driven development**: All open and recent work stems from S3/S2 JSBSim simulator testing (sim 0.9.0~rc17 to rc22). Test harness includes automated preflight checks, mission planning, and dynamic failure injection.
- **Release branch activity**: Multiple Ben Busby UI bugs are marked "Ready for Testing" on release/3.3.0 branch — suggests 3.3.0 release candidate is under validation
- **Critical vs. marked priority**: Custom field priority is "Low," but UI state bugs block app interaction (app restart workaround), sensor loss tasks have safety implications, and waypoint skip/fishhook are mission-critical path errors
- **Scope clarity**: S3 sensor loss tasks lack detail on expected behavior; Dubins path fishhook and goto failure suggest mission planning logic needs review under edge conditions
- **VTOL support emergence**: Open milestone shows new feature incoming; related bugs (SIM-0019, fishhook; lost comms joystick) are blocking acceptance
- **Release readiness**: No ETA. Current work is stabilization (preflight validation, UI state, sensor robustness) and new feature blocking item triage (VTOL). Completed tasks show high resolution velocity; open work appears ready for active sprint.