_Asana snapshot as of 2026-10-27: 6 open tasks, 60 completed (last 90 days)._

# [001-14] SwiftCore 3.3

## Overview
- **Project**: Development of the 3.3 (develop) branch of autopilot, ground station, and tablet code
- **Owner**: Jack Elston
- **Team**: BST (Whole Team)
- **Status**: **ARCHIVED** (as of Nov 28, 2023)
- **Priority**: Low
- **Key Personnel**: Jack Elston, Ben Busby, Maciej Stachura

## Key Deliverables & Milestones
Six open milestone categories remain (all unassigned, no due dates):
1. Final release supporting 2030, 2040, likely 2050 and 3000 hardware
2. Final release supporting commercial S1
3. Adds initial VTOL support
4. Official scripting release (including payload control)
5. Control through the payload serial interface
6. Adds app support (payload, flight parameters, scripting)

## Task Summary
- **Total**: 66 tasks (6 open, 60 completed)
- **Completion Rate**: 91%
- **Assignment Breakdown**:
  - Maciej Stachura: 17 completed tasks (mostly simulator testing, flight dynamics issues, VTOL testing)
  - Ben Busby: 11 completed tasks (primarily tablet/app UI bugs, preflight checks, XML configuration)
  - Jack Elston: 8 completed tasks (autopilot logic, sensor configuration, hardware issues, communications)
  - Unassigned: 6 open milestones

## Recent Activity
**Last recorded activity: October 26, 2026** (dates in Asana appear to be from 2026, likely data error or simulator environment)

Recent completed tasks focused on bug fixes:
- Altitude change/landing descent glitches (Elston, 10/26)
- Script execution failures for altitude commands (Elston, 10/26)
- AGL display precision bugs in tablet app (Busby, 10/24)
- Autopilot path planning issues (Stachura, 10/23)
- Preflight check logic bugs (Busby, 10/23)
- Sensor handling and failover responses (Stachura, 10/22-10/23)
- Manual takeover/joystick mode bugs (Stachura, Busby, 10/22)
- Dynamic pressure sensor false alarms (Stachura, 10/22)

## Notes & Context

### Work Patterns
- **Heavy simulator testing** with formal bug reports (SIM-0017 through SIM-0040) logged during 0.9.0~rc17-rc22 cycles
- **Broad coverage**: Autopilot flight dynamics, tablet UI, scripting, sensor handling, VTOL operations, manual control modes
- **No assigned owners for remaining milestones** suggests these are aspirational goals rather than active work items

### Key Completed Areas
- Joystick/manual takeover modes
- Scripting and command execution
- Preflight validation logic
- Sensor failover and error handling
- Multi-aircraft support (S0-S3 variants, S1-22, S10011, S10020)
- VTOL flight testing and path planning
- App telemetry and node status UI reliability

### Archive Context
Project marked ARCHIVED with status from Nov 28, 2023. The completed task dates (2026) appear anomalous and may reflect simulator timestamps or data inconsistency. The six open milestones are unassigned and have no due dates, indicating they are parked or rolled into future planning outside this project structure.