# [001-14] SwiftCore 3.3

## Overview
- **Client/customer**: Internal BST development project
- **Dollar value**: Not specified
- **Timeline**: Active development branch; no target release date specified
- **Status**: **ACTIVE DEVELOPMENT with high task volume.** As of Nov 28, 2023: **29 open tasks, 19 completed.** Project shows substantial recent activity (many tasks completed 2026-10-21 to 2026-10-22) across autopilot, ground station, and tablet code. Note: timestamp inconsistency in raw data (Nov 2023 status vs. Oct 2026 task dates) suggests either data import lag or concurrent development cycles. Current work dominated by simulator bug fixes, sensor/telemetry issues, and app UI stability problems.
- **Team members**: Jack Elston (owner), Maciej Stachura (primary developer), Ben Busby (app/UI focus), Daniel Prendergast (process lead), whole BST team
- **Risk signals**: 
  - **29 open tasks with no due dates** — work is unscheduled; priority unclear beyond "Low" custom field rating
  - Heavy simulator bug report intake (SIM-0017 through SIM-0040 represented in open tasks) — suggests rapid testing and issue discovery
  - Multiple app/UI issues preventing normal operation (aircraft control window failures, mode switching bugs, preflight check state issues)
  - Critical sensor/telemetry bugs (GPS/PDOP error escalation, IAS false alarms, dynamic pressure dropouts, scale mismatch in telemetry position height)
  - Mission planning failures (waypoint skip, goto failures, landing descent altitude changes not honored)

## Key Deliverables & Milestones

**Open Milestones (no due dates assigned):**
- Adds initial VTOL support (milestone-level task, unassigned)
- Final release supporting 2030, 2040, 2050, and 3000 hardware
- Final release supporting commercial S1
- Adds initial tailsitter support
- Official scripting release (including payload control)
- Control through the payload serial interface
- Adds app support (payload, flight parameters, scripting)

**Completed Milestones:**
- Adds initial VTOL support (completed 2026-02-03) — *Note: conflicts with open "Adds initial VTOL support" milestone; may be duplicate or rolling milestone*
- Unified Estimator (completed 2026-02-03)

## Task Summary
- **Total tasks**: 29 open, 19 completed (as of Nov 28, 2023 snapshot)
- **Tasks by assignee**:
  - **Maciej Stachura**: ~10 open (simulator sensor/flight logic issues: GPS, pitot, mags, pressure, dynamic pressure, mission planning); 2 completed (S3 model, IAS false alarm)
  - **Jack Elston**: ~4 open (critical telemetry/sensor issues: GPS error escalation, throttle kill response, telemetry scale mismatch, joystick mode); 6 completed (sensor alerts, IAS flag, logging, bootloader, CAN integration, battery indication)
  - **Ben Busby**: ~10 open (app/UI state bugs: landing plan altitude checks, aircraft control window failures, mode switching, scripting/commands, preflight validation, waypoint display, telemetry menu); 7 completed (XML fixes, test sensor app, log parsing, commands/scripting testing, USB bootloader, scale factors)
  
- **Notable patterns**:
  - **Simulator-driven intake**: Majority of open tasks reference simulator bug reports (SIM-0017, 0019–0022, 0025, 0028–0032, 0037–0038) from rc17/rc18 test runs on 2026-10-21
  - **App/UI dominance among open work**: ~10 of 29 open tasks are UI/tablet app issues (preflight checks, window state, mode switching)
  - **Sensor/telemetry cluster**: ~8 open tasks focus on airspeed, pressure, GPS, and dynamic pressure sensing
  - **Batch completion pattern**: 19 tasks completed on 2026-10-21, 2 on 2026-10-22 — indicates focused testing/fix cycle
  - **No due dates across all tasks** — work prioritized by team triage, not formal schedule

## Recent Activity
**Batch completion (2026-10-21 to 2026-10-22):**
- Maciej Stachura: S3 model ground contact carry-over, S3 BAD IAS false alarm at altitude (SIM-0028)
- Jack Elston: Joystick mode climbout prevention, flight timer check, backup static pressure alert, IAS error flag automation, trigger packet logging, takeoff waypoint altitude, USB bootloader, MHP/CAN integration, command packet logging reduction, battery percentage indication
- Ben Busby: XML safe height duplicate removal, test sensor app XML, log parsing waypoint timing, commands/scripting integration testing, scale factor review

**Active open issues (unresolved):**
- GPS/PDOP error escalation blocking joystick mode abort (Jack Elston)
- S2 throttle kill response delayed warning + emergency descent + "bad flight plan" error (Jack Elston)
- Telemetry position height scale mismatch: packed ×100 vs. documented ×1000 (Jack Elston)
- Dynamic pressure sensor dropouts with state persistence issues (Maciej Stachura)
- Waypoint skip on northbound mission, goto failures, landing altitude changes not honored (Maciej Stachura/Ben Busby)
- App window state fragility across mode switches, preflight check validation inconsistencies (Ben Busby)
- Script/command ACK failures for VTOL/fixed-wing climb/descent (Ben Busby)

## Work Intake Process
As of May 2026 (from prior knowledge), the team operates on a **hybrid issue capture model**:
- **Automated**: Post-flight feedback form routes issues directly to Fleet Maintenance (hardware) or SwiftCore 3.3 (software)
- **Manual**: Team members may continue adding tasks directly (reflected in high open count)
- **Responsibility**: Daniel Prendergast (process lead) owns form deployment and routing logic

Current snapshot (Nov 2023 update) shows heavy simulator-driven intake; integration of post-flight feedback form appears in-flight or ramping up.

## Notes & Context
- **Data timestamp anomaly**: Status update dated Nov 28, 2023 but task completion dates span Oct 2026. Likely indicates stale Asana snapshot label with current work data imported; treat task dates (Oct 2026) as authoritative.
- **Project maturity vs. task volume**: Prior knowledge noted SwiftCore 3.3 "substantially complete" by June 2026; current snapshot shows **29 open tasks**, suggesting either:
  - Rapid expansion of simulator test coverage uncovering latent bugs (SIM-0017–0040 integration)
  - Development cycle refresh toward next release candidate
  - Backlog accumulation without formal triage/closure
- **Priority**: Low (custom field), but task volume and severity (sensor false alarms, mission planning failures, app state bugs) suggests tactical medium priority for near-term rc18+ stabilization
- **Quality assurance**: Heavy reliance on simulator testing (9+ distinct SIM-#### bug reports in open tasks); real-world flight data ("simulator bug report" notes reference "from BST's test simulator box" 2026-10-21). App UI issues suggest tablet/ground station testing lagging autopilot core work.
- **Release readiness**: No target date assigned. Current work prioritizes rc17/rc18 stability over new feature delivery (all open work is bug/fix/validation scope).