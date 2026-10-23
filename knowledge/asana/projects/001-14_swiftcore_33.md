_Asana snapshot as of 2026-10-23: 9 open tasks, 103 completed (last 365 days)._

# [001-14] SwiftCore 3.3

## Overview
- **Project**: Development of the 3.3 (develop) branch of the autopilot, ground station, and tablet code
- **Owner**: Jack Elston
- **Team**: BST (Whole Team) — primary contributors include Ben Busby, Maciej Stachura, Jack Elston
- **Dollar value**: Not specified in project data
- **Timeline**: 
  - As of status update Nov 28, 2023, project had overdue milestones and tasks
  - Recent completed work dated October 21–23, 2026 (note: dates appear to be simulator/test data from future scenario)
- **Status**: [YELLOW] Active with overdue work; 103 completed tasks, 9 open tasks (mostly unassigned milestone features)
- **Priority**: Low (per custom field)

## Risk Signals
- **Overdue milestones and tasks as of Nov 28, 2023** (per project status update)
- Six milestone-level features remain unassigned with no due dates:
  - Final release supporting 2030, 2040, and 2050/3000 hardware
  - Final release supporting commercial S1
  - Adds initial VTOL support
  - Official scripting release (including payload control)
  - Control through payload serial interface
  - Adds app support (payload, flight parameters, scripting)
- Three active bug tasks assigned to Ben Busby with no due dates:
  - Script goto command ACK failures and unintended landing (SIM-0020)
  - Altitude change during landing descent causes green flash, no error, landing not cancelled (SIM-0032)
  - AGL elevation in node panel sometimes displays incorrectly (m/100 scaling issue)

## Key Deliverables & Milestones
Six major feature milestones listed, all open/unassigned with no due dates:

1. **Final release supporting 2030, 2040, 2050, 3000 hardware**
2. **Final release supporting commercial S1**
3. **Adds initial VTOL support**
4. **Official scripting release** (including payload control)
5. **Control through payload serial interface**
6. **Adds app support** (payload, flight parameters, scripting)

## Task Summary
- **Total**: 9 open, 103 completed (91.6% completion rate)
- **Tasks by assignee** (completed, recent):
  - Ben Busby: 5 open + multiple completed (app/tablet issues, preflight checks, telemetry, altitude handling)
  - Maciej Stachura: 2 open + multiple completed (simulator QC, autopilot path planning, loss-of-signal scenarios, dynamic pressure issues)
  - Jack Elston: 0 open + multiple completed (communications, autopilot configuration, logging, battery indication)
  - Unassigned: 2 open (both are milestones)

- **Notable patterns**:
  - Heavy simulator testing focus (SIM-xxxx bug reports from sim 0.9.0~rc17, rc18, rc22)
  - Bug fixes cluster around preflight checks, telemetry/app UI, joystick mode, landing plans, and sensor handling
  - Many tasks reference feature branches (release/3.3.0, develop)
  - No tasks have due dates; work appears tracked by simulator test cycles and field testing (S0, S1, S2, S3, S10011, S10020, etc.)

## Recent Activity
**Completed (Oct 21–23, 2026)** — Recent fixes include:
- App UI/UX: telemetry menu failures, aircraft control window opening issues, user mode switching bugs (all marked "Passed")
- Simulator QC: VTOL Dubins path fishhook, goto waypoint failures, flight plan diversion (waypoint skipping), sensor loss scenarios
- Autopilot: landing plan altitude checks, joystick takeover, preflight warnings, dynamic pressure dropout handling, airspeed error recovery
- Hardware: PWM channel configuration (S00001), actuator surface response, GCS/Xtend comms dropout
- Scripting: commands and scripting issues for VTOL and fixed-wing (climb/descend commands)
- Configuration: USB bootloader flag for hardware 2050, MHP CAN bus integration

**In progress (Ben Busby)** — Three active bugs related to scripting, altitude handling, and AGL display.

## Notes & Context
- Project status as of Nov 28, 2023 flagged **[yellow] with overdue milestones and tasks**, but the bulk of completed work is dated Oct 21–23, 2026 (future scenario or test data labeling)
- Six major feature milestones remain backlog items with no assigned owners or due dates; these likely represent the 3.3 release roadmap rather than immediate blockers
- High volume of simulator-based QC testing and bug discovery (SIM-0017 through SIM-0040+), suggesting active development/test cycle
- Extensive testing across multiple aircraft variants (S0, S1, S2, S3, S10011, S10020, E2)
- No custom field usage for dollar tracking or budget; priority marked "Low"
- **Conflict in timeline data**: Project notes show Nov 28, 2023 status, but completed tasks dated Oct 2026 — Asana data may be stale or mislabeled

**TEAM CORRECTIONS & FEEDBACK**: None provided in source data.