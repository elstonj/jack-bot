_Asana snapshot as of 2026-10-27: 231 open tasks, 0 completed (last 90 days)._

# [001-09] SwiftCore 4.0

## Overview

**Internal Development Project** — Future development of the autopilot, ground station, and tablet code for Black Swift Technologies.

- **Owner:** Jack Elston
- **Team:** Whole BST team (Jack Elston, Maciej Stachura, Ben Busby primary contributors)
- **Status:** ACTIVE — Low priority backlog with no scheduled milestones or due dates
- **Dollar Value:** Not specified
- **Timeline:** Ongoing; no start or end dates defined

## Key Deliverables & Milestones

All major milestones are currently **unscheduled and unassigned**:

1. **Conversion to RTOS**
2. **Better payload system** — Support multiple cameras and loading flight plans
3. **Official VTOL / tailsitter support**
4. **SBC Autopilot companion**
5. **New GCS** (Ground Control Station)
6. **MAVLink support**
7. **UAVCAN support**
8. **Multi-vehicle support**
9. **User authentication**
10. **Automated log file handling and OTA firmware updates**
11. **Full Geofencing Support**

## Task Summary

- **Total Tasks:** 231 open, 0 completed
- **Priority:** Low (custom field)
- **Assignment distribution:**
  - **Jack Elston:** ~130+ tasks (bug fixes, calibration issues, hardware integration, comms, simulation, documentation)
  - **Maciej Stachura:** ~70+ tasks (estimator, VTOL control, TECS, simulation, wind alignment, filters)
  - **Ben Busby:** ~30+ tasks (GCS/tablet UI, mapping, flight planning, logging, sensor integration)
  - **Unassigned:** 11 major milestones

- **Completion Rate:** 0% — No tasks have been closed in this project view

## Task Patterns & Organization

This is a long-term feature and bug backlog organized by **system area**:

### By System:

**Autopilot / Flight Control (Jack Elston dominant)**
- Surface calibration issues (can't command past max/min, initial XML deflections, etc.)
- Emergency descent and lost GPS edge cases
- Joystick mode behavior (lost comms, flare, GPS loss)
- Battery and power management (ERROR_NO_BATTERY, low battery termination)
- Payload door and deployment tube logic
- Telemetry scale mismatches and logging

**Estimator & Control (Maciej Stachura dominant)**
- Wind estimation and automated parameter changes
- VTOL transitions and failure handling
- Clog detection (standard and MHP)
- Motor/thrust mapping improvements
- Sensor initialization and filter tuning
- Unified estimator across vehicle types

**GCS / Tablet UI (Ben Busby dominant)**
- Mission planning improvements (altitude limits, waypoint handling, dubins paths)
- Plot and telemetry display enhancements
- Device discovery and multi-aircraft support
- OTA firmware updates from tablet
- Log file management and download

**Simulation (Gazebo)**
- E2 model updates
- Fixed-wing and multirotor photogrammetry sims
- Payload control integration

**Infrastructure & Architecture**
- RTOS migration
- Removal of `#ifdef` vehicle type macros
- Comm and CAN protocol modularity
- Security improvements
- Documentation and QRH/MMEL

### Notable Feature Branches:
- `unified_est` — Unified estimator work
- `yaw_mix` — Controller-based turn-rate to rudder
- `vtol` — Vehicle controller refactoring

## Recent Activity

**No recent activity recorded.** The project notes indicate a status update from **Nov 28, 2023** with sections for:
- Overdue milestones (not detailed)
- Overdue tasks (not detailed)
- Completed milestones (not detailed)
- Completed tasks (not detailed)

However, **all 231 tasks remain open with no due dates or timestamps**. This suggests the project is in **long-term planning mode** rather than active execution.

## Notes & Context

### Key Observations:

1. **No Scheduled Work** — Despite 231 tasks, there are no assigned due dates, no milestones with deadlines, and no clear sprint structure. This is a **backlog capture**, not an active roadmap.

2. **Bug + Feature Mix** — Tasks range from critical bugs (ERROR_NO_BATTERY on flights, calibration blockers) to aspirational features (RTOS, new GCS, moving baseline RTK). No triage or severity ranking is evident.

3. **System Debt** — Significant architectural cleanup needed:
   - Remove `#ifdef` macros for vehicle types
   - Remove old code markers (FIXMEs, deprecated functions)
   - RTOS migration
   - Comm protocol restructuring

4. **Integration Points** — Heavy interdependence between:
   - Autopilot and estimator (sensor initialization, switching, failover logic)
   - Tablet UI and autopilot params (OTA, calibration, mission planning)
   - Simulation and flight control (validation loops)

5. **Documentation Gaps** — Several tasks note incomplete or conflicting documentation (e.g., TELEMETRY_POSITION.height scale mismatch, inconsistent parameter descriptions).

6. **Vehicle Coverage** — Work spans:
   - Fixed-wing (E2)
   - VTOL/tailsitter (S2)
   - Multirotor (quads)
   - Tube-launched (S0)

### Recommendation:
This backlog would benefit from prioritization, milestone assignment, and dependency mapping before execution. Current state is suitable for long-term reference but not actionable without further triage.