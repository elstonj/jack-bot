_Asana snapshot as of 2026-11-12: 229 open tasks, 5 completed (last 90 days)._

# SwiftCore 4.0

## Overview
- **Client/Customer:** Internal R&D (whole BST team)
- **Project Owner:** Jack Elston
- **Status:** [GREEN] Active development (as of Nov 28, 2023)
- **Priority:** Low
- **Team Members:** Jack Elston, Maciej Stachura, Ben Busby, and broader BST team
- **Dollar Value:** Not specified in project data
- **Timeline:** Ongoing; started 2015 (per Gantt notes in legacy tasks)

## Key Deliverables & Milestones
Strategic capability milestones (all currently unassigned, no due dates):
- Conversion to RTOS
- Official VTOL / tailsitter support
- Better payload system (multiple cameras, flight plan loading)
- SBC Autopilot companion
- New Ground Control Station (GCS)
- MAVLink support
- UAVCAN support
- Multi-vehicle support
- User authentication
- Automated log file handling and OTA firmware updates
- Full Geofencing Support

## Task Summary
- **Total tasks:** 229 open, 5 completed (99.8% open rate)
- **Completion velocity:** Very low (5 tasks completed as of Nov 28, 2023)

**Tasks by assignee:**
- **Jack Elston:** ~120 tasks (primary focus on autopilot core, calibration, comms, safety systems, GCS integration, hardware)
- **Maciej Stachura:** ~85 tasks (flight control tuning, estimators, VTOL/tailsitter features, simulation, advanced control)
- **Ben Busby:** ~20 tasks (tablet UI, GCS, flight planning, visualization, web integration)
- **Unassigned:** ~13 milestone-level strategic features

**Notable pattern:** No task has a due date; all work is backlog-driven without time-boxed delivery commitments.

## Recent Activity
**Completed (Oct 30, 2026):**
- 5 tablet UI / flight plan display bugs fixed (Ben Busby):
  - Mag declination display format (radians vs degrees)
  - Waypoint plan overwrite issue
  - Drop menu persistence
  - Flight plan mode labels (113 → "takeoff", 118 → "ERROR")

**Currently Open & Active Issues:**
- **Flight control tuning** (Maciej Stachura): Yaw oscillation on landing, roll hover gains (sea-level vibration), forward roll loop re-tuning on S3
- **Safety/error handling** (Jack Elston): Battery error logic, GPS loss behavior, emergency descent issues, joystick mode restrictions, throttle/power loss detection
- **Calibration bugs** (Jack Elston): Surface range limits in calibrate mode, initial XML deflections, payload door behavior
- **VTOL/transition** (Maciej Stachura): Clog detection, wind alignment, engine-out handling, transition timeouts, landing modes
- **Estimator improvements** (Maciej Stachura): GPS/pressure outage handling, unified estimator, gyro feedback, sensor initialization
- **GCS/tablet** (Ben Busby): Log file handling, parameter UI, map backends (MapBox), multi-vehicle support, real-time plotting

## Notes & Context

### Code Quality & Architecture
- Large volume of cleanup work: FIXME removal, ifdef macro refactoring (vehicle type branches), legacy code removal
- Ongoing modularization: CAN/comm protocols, sensor driver architecture, filter initialization
- Feature branches in use: `unified_est`, `yaw_mix`, `vtol`
- GitLab issue sync active (e.g., thrust cutoff task linked to GitLab #5)

### Critical Issues Observed
Multiple cascading failure modes documented:
- Lost GPS + low PDOP combination triggers auto-emergency descent, blocking joystick recovery
- Motor power loss detection lag (~30m altitude loss before warning)
- Battery error (ERROR_NO_BATTERY) causing mission leg abort
- Telemetry height scale mismatch (x100 vs x1000) in comm packets

### Instrumentation Gaps
- No logging of WDT (watchdog timer) trips on addon boards
- Sensor starting values not validated before logging
- Hot shoe (camera trigger) packets not logged
- System time not added to all packets (planned)

### Simulation & Testing
- Gazebo models for E2 and S2 need updates (inertia, motors, new configurations)
- X-Plane plugin for simulation; simulator bug reports active (e.g., SIM-0037)
- S0 AD and S2 throttle kill behavior issues found in sim, repeatable

### Payloads & Hardware
- Dual pitot setup integration needed with drained version
- Smart battery board firmware pending completion
- Addon board WDT expansion needed (sensor-quality based)
- Payload door logic errors (opens in pre-flight, doesn't hold position in calibrate)

### No Team Corrections Provided
This summary reflects Asana data only; no override feedback from team was included in the source.