_Asana snapshot as of 2026-10-25: 8 open tasks, 58 completed (last 90 days)._

# [001-14] SwiftCore 3.3

## Overview
- **Project**: Development of the 3.3 (develop) branch of autopilot, ground station, and tablet code
- **Owner**: Jack Elston
- **Team**: BST (Whole Team) — primary contributors: Jack Elston, Ben Busby, Maciej Stachura
- **Priority**: Low
- **Status**: **ACTIVE** — Heavy bug-fix and testing phase. 58 tasks completed, 8 open milestones and bugs remaining. Project shows significant recent activity (Oct 21–24, 2026) with simulator testing and bug fixes ongoing.
- **Risk Signal**: Two open simulator bugs remain unassigned (SIM-0032, SIM-0020) with no due dates. Multiple overdue milestones noted as of Nov 28, 2023 (per Asana status update), but completion date metadata suggests active work continuing into Oct 2026.

## Key Deliverables & Milestones
All open milestones are unassigned and lack due dates:

1. **Final release supporting 2030, 2040, and likely 2050 and 3000 hardware**
2. **Final release supporting commercial S1**
3. **Adds initial VTOL support**
4. **Official scripting release** (including payload control)
5. **Control through the payload serial interface**
6. **Adds app support** (payload, flight parameters, scripting)

## Task Summary
- **Total**: 66 tasks (8 open, 58 completed)
- **Completion rate**: 88%

### By Assignee:
- **Ben Busby**: 15 completed tasks (app/tablet UI bugs: AGL elevation display, telemetry menu, aircraft control window, preflight validation, landing plan switching, log parsing)
- **Maciej Stachura**: 22 completed tasks (autopilot logic, sensor failures, VTOL path planning, simulator QC: goto failures, waypoint skipping, Dubins path issues, engine/sensor stall responses, takeover bugs)
- **Jack Elston**: 13 completed tasks (hardware integration, comms, commands/scripting, sensor logic, USB bootloader, CAN bus MHP, command logging)
- **Unassigned**: 8 tasks (6 open milestones + 2 open bugs from simulator)

### Notable Patterns:
- Heavy reliance on **simulator bug reporting** (SIM-0017 through SIM-0040)
- **Ben Busby** concentrated on tablet/app UI stability
- **Maciej Stachura** focused on autopilot navigation and sensor handling
- **Jack Elston** handling firmware-level integration and comms
- All completed tasks lack due dates; tracking appears milestone-based rather than date-driven

## Recent Activity
**As of Oct 21–24, 2026** (most recent completion timestamps):

### Recently Completed (Oct 23–24):
- Ben Busby: Fixed AGL elevation display bug in app (m/100 scaling), resolved telemetry menu failures, aircraft control window failures, preflight validation (landing plan altitude, zero sensors checks)
- Maciej Stachura: Resolved goto failures (point directly under aircraft), waypoint skipping (flight diversion), Dubins path fishhook artifact in VTOL, S3 sensor losses (pitot, mags, static pressure, GPS), joystick mode lockup
- Jack Elston: PWM channel setup (S00001), actuator values ACK without surface movement, Xtend GCS comms loss, prevented joystick mode activation in climbout

### Still Open (No Due Date):
1. **SIM-0032**: Altitude change to 3500 m during landing descent flashes green then drops (no error, landing not cancelled) — assigned to Jack Elston
2. **SIM-0020**: Script goto 350 m @ 5 m/s then 20 m/s returns ACK failed; aircraft proceeds straight to landing — assigned to Jack Elston

## Notes & Context

### Data Quality Flag
The Asana project references a status update dated **Nov 28, 2023** noting "Overdue milestones" and "Overdue tasks," but **all task completion dates in the data are from Oct 2026**. This suggests either:
- The Nov 2023 status was outdated or archived
- Asana data was not cleaned up after real-world project completion or pivoting
- Timeline may span 2023–2026 with intermittent activity

**Recommendation**: Verify with Jack Elston whether this project remains active or if it has transitioned to maintenance/legacy status.

### Technical Context
- **Hardware targets**: E2, S0, S1, S1-22, S2, S2-9, S3, S10011, S10020 (various fixed-wing and VTOL platforms)
- **Key systems under development**:
  - VTOL support (initial implementation, path planning)
  - Scripting engine for autopilot commands and payload control
  - Tablet/app UI (SwiftTab) for flight monitoring and control
  - Sensor fusion (pitot, static pressure, magnetometer, GPS, dynamic pressure)
  - Joystick takeover in flight
  - Landing plan strategies (vertical vs. spiral)
  - Payload serial interface control
- **Testing infrastructure**: JSBSim simulator (sim 0.9.0~rc17 → rc22 versions referenced)

### Known Unresolved Issues
Both remaining open bugs involve scripting and altitude commands in flying/landing modes—suggest potential interaction between autopilot state machine and command processing that may affect VTOL or commercial S1 release readiness.