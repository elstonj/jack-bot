_Asana snapshot as of 2026-11-03: 226 open tasks, 5 completed (last 90 days)._

# [001-09] SwiftCore 4.0

## Overview

- **Client/Customer:** Black Swift Technologies (internal development)
- **Dollar Value:** Not specified in project data
- **Timeline:** Ongoing since 2015-01-19; no defined end date
- **Status:** Active (Low Priority) — Heavy backlog with 226 open tasks and only 5 completed tasks as of Nov 28, 2023
- **Team Members:** 
  - Jack Elston (Owner, primary assignee)
  - Maciej Stachura (Control systems, estimator, simulation)
  - Ben Busby (Ground Control Station/tablet UI, GCS integration)
- **Risk Signals:** 
  - Massive open task count (226) with minimal completion rate suggests backlog management issues
  - Multiple unassigned milestones with no due dates
  - Low-priority classification despite core platform work
  - Bug reports span critical systems (emergency descent, battery failsafe, calibration) suggesting stability concerns

## Key Deliverables & Milestones

All milestones are currently **unassigned and have no due dates**:

1. **Conversion to RTOS** — Future modularization of real-time kernel
2. **Better payload system** — Multi-camera and flight plan loading support
3. **Official VTOL / tailsitter support** — Enhanced vertical takeoff configurations
4. **SBC Autopilot companion** — Single-board computer integration
5. **New GCS** — Ground control station modernization
6. **MAVLink support** — Standard UAV protocol integration
7. **UAVCAN support** — CAN bus protocol for modular hardware
8. **Multi-vehicle support** — Simultaneous control of multiple aircraft
9. **User authentication** — Security feature for GCS access
10. **Automated log file handling and OTA firmware updates** — Field update capability
11. **Full Geofencing Support** — Boundary enforcement and keep-out zones

## Task Summary

- **Total:** 226 open, 5 completed (2.2% completion rate)
- **Assignee Breakdown:**
  - **Jack Elston:** ~120 tasks (core autopilot, comms, hardware integration, security, firmware)
  - **Maciej Stachura:** ~60 tasks (flight control algorithms, estimator, VTOL, simulation, sensor fusion)
  - **Ben Busby:** ~35 tasks (GCS UI/UX, tablet app, mission planning, visualization)
  - **Unassigned:** 11 milestones
- **Completion Rate by Assignee:** All showing <1% (5 completed tasks total, all from Ben Busby, all closed on 2026-10-30)

## Recent Activity

- **Last Completed Tasks (2026-10-30):** Five tablet/GCS UI bug fixes closed by Ben Busby:
  - Mag declination display format fix
  - Flight plan overwrite behavior
  - Air-deployed UAS drop menu clearing
  - Waypoint type display (takeoff/error labels)

- **No open task completions** logged between Nov 28, 2023 status update and present, indicating stalled progress on core development items.

- **Critical Active Bugs** assigned to Jack Elston (all no due date):
  - Roll command logging error on takeoff
  - Battery failsafe triggering ERROR_NO_BATTERY mid-mission
  - Calibration mode surface command limiting
  - Telemetry height scale mismatch (scale factor discrepancy)
  - Payload door premature opening in pre-flight
  - Kill switch not responding if left engaged
  - Emergency descent blocking when GPS lost
  - Motor power loss warnings delayed during descent (40+ meter altitude loss)

## Notes & Context

### Architecture & Scope
SwiftCore 4.0 is a multi-platform autopilot and ground station system supporting fixed-wing, VTOL, tailsitter, and multirotor aircraft. Development spans three major subsystems:
- **Autopilot firmware** (AP) — Flight control, estimator, failsafe logic
- **Ground Control Station** (GCS) — Desktop/web interface
- **SwiftTab** — Tablet/mobile ground control interface

### Known Technical Debt
- Extensive use of `#ifdef` macros for vehicle type selection (Jack Elston flagged for removal)
- VTOL transition failures and clog detection incomplete
- Estimator sensor fusion incomplete for GPS/pressure outages
- Multiple FIXMEs scattered through codebase requiring cleanup
- Wind estimation and automated parameter tuning not implemented
- Unified estimator across vehicle types still pending

### Feature Branches in Development
- `unified_est` — Unified estimator for all vehicle types (Maciej Stachura)
- `yaw_mix` — Controller-based turn-rate to rudder mapping (Maciej Stachura)
- `vtol` — VTOL controller refactor (Jack Elston)

### Integration & Hardware
- Dual pitot setup integration in progress
- SBC companion autopilot for modularity
- Smart battery board firmware incomplete
- Addon board watchdog (WDT) integration needed
- ESC communication via UART/CAN in design phase
- Laser-based terrain following not yet implemented

### Simulation & Testing
- Gazebo models incomplete (S2 model pending, fixedwing simulation in progress)
- X-Plane plugin needs SDK migration
- Joystick mode simulation has known disconnect issues
- Motor power loss and GPS loss failsafes need validation across vehicle types

### GCS/Tablet Known Issues
- Mission altitude limits not defaulting correctly (Ben Busby)
- Landing plan creation UI incomplete
- Multi-UAS support framework not implemented
- OTA upgrades blocked at tablet level
- Log file download/upload through tablet not complete
- Wind visualization (barbs) not yet added to UI

### Priority Assessment
Despite "Low Priority" classification, this backlog contains **critical flight safety items** (battery failsafe, emergency descent logic, GPS loss handling) alongside aspirational features. The 226:5 task ratio and lack of due dates suggests either:
1. Continuous maintenance mode with episodic feature development
2. Backlog not being actively triaged or retired
3. Resource constraints limiting active development capacity