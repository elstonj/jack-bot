_Asana snapshot as of 2026-10-23: 219 open tasks, 3 completed (last 365 days)._

# [001-09] SwiftCore 4.0

## Overview
- **Project Type**: Future development roadmap for Black Swift Technologies autopilot, ground station, and tablet systems
- **Owner**: Jack Elston
- **Team**: Whole BST team (Jack Elston, Maciej Stachura, Ben Busby)
- **Status**: Active — long-term development backlog with no dollar value or timeline constraints specified
- **Priority**: Low (custom field)
- **Risk Signal**: 219 open tasks with no due dates; milestone structure is aspirational rather than scheduled

## Key Deliverables & Milestones
All milestones are unassigned with no due dates. Major planned features include:

1. **Conversion to RTOS** — Real-time operating system refactor
2. **Better payload system** — Support multiple cameras and flight plan loading
3. **Official VTOL/tailsitter support** — Expanded vehicle type support
4. **SBC Autopilot companion** — Single-board computer integration
5. **New GCS** — Ground control station redesign
6. **MAVLink support** — Third-party protocol integration
7. **UAVCAN support** — CAN bus protocol
8. **Multi-vehicle support** — Simultaneous control of multiple aircraft
9. **User authentication** — Security layer for tablet/GCS
10. **Automated log file handling and OTA firmware updates** — Deployment automation
11. **Full Geofencing Support** — Boundary enforcement

## Task Summary

- **Total tasks**: 222 (219 open, 3 completed)
- **Completion rate**: 1.4% (3 of 222)
- **Tasks by assignee**:
  - **Jack Elston**: ~120 tasks (bugs, calibration issues, system architecture, protocol design, documentation)
  - **Maciej Stachura**: ~60 tasks (autopilot control, estimator, VTOL/tailsitter dynamics, TECS improvements, testing/simulation)
  - **Ben Busby**: ~40 tasks (tablet UI, GCS, flight planning, mapping, data logging)
  - **Unassigned**: 11 milestones

- **Notable patterns**:
  - **Bug/issue tracking dominates**: Most tasks are incremental fixes and enhancements, not major features
  - **No time-boxing**: No due dates enable prioritization flexibility but signal long-term backlog vs. sprint work
  - **Technical debt**: Heavy focus on refactoring (RTOS conversion, unified estimator, removing dead code/FIXMEs)
  - **System-wide scope**: Tasks span firmware, autopilot control loops, communications, ground station, tablet UI, simulation, and documentation

## Recent Activity

As of **November 28, 2023**:
- **Status update**: Green status reported; summary notes overdue and completed milestones but provides no details
- **Completed tasks** (3 total, all from April 9, 2026):
  - Look into multiple UAS from a single ground station
  - Add GPS year, month, day, and mag declination
  - Use UAVCAN
- **No overdue tasks or milestones** explicitly listed in the status update

## Notes & Context

### Critical Issues Assigned to Jack Elston
Several field bugs affecting flight safety and operations:
- **ERROR_NO_BATTERY** error caused aircraft to miss mapping leg (E2)
- **TELEMETRY_POSITION.height scale mismatch** — documentation/code disagreement (100x vs 1000x scaling in comm_handler_base.cpp vs comm_packets.h)
- **Calibration mode surface limits** — tablet/AP not allowing full range in calibrate mode
- **Payload door issues** — opens during pre-flight when sent to mapping; doesn't hold position consistently
- **Lost GPS emergency descent** — aborts blocked by critical error logic
- **Joystick mode GCS disconnection** — S10005 briefly lost connection when switching modes; params redownloaded
- **Motor power loss detection lag** — S2 throttle kill response only warns after ~30m altitude loss in sim

### Autopilot Control Focus (Maciej Stachura)
Heavy emphasis on:
- **Estimator robustness**: Handling GPS/pressure/pitot sensor failures; unified estimator design
- **VTOL enhancements**: Transition logic, clog detection (MHP dual-probe), wind-aligned landing
- **Controller improvements**: Flare energy-based (not pitch-based), IAS limits with flaps, wind-based climb limits
- **Motor/rotor refactoring**: Unified parameters; power-based clog detection vs. thrust-setting
- **Gazebo simulation**: E2 model update, fixedwing and multirotor simulation needed

### Tablet/GCS Development (Ben Busby)
Primary work areas:
- **Flight planning & mapping**: DEM integration (SRTM), altitude defaults, sensor selection UI
- **Telemetry & logging**: Log file download/upload to logparse.bst.aero, flight notes, hashing
- **UI/UX**: Wind barbs, plot windows, multi-aircraft support, joystick visualization, parameter dropdowns
- **OTA updates**: Autopilot and GCS firmware over-the-air updates via tablet
- **Missing map backend migration**: MapBox evaluation

### Architectural/Protocol Debt
- Remove ifdef macros for vehicle types; move to unified codebase
- Rethink comms architecture; move back to object-based design
- CAN protocol/firmware updates
- Service discovery for WiFi
- Remove payload parameters packet; consolidate channel/payload type signaling
- Add system time to all packets

### Simulation & Testing Infrastructure
- Gazebo models incomplete (E2 needs update, fixedwing & MR photogrammetry sim needed)
- X-Plane plugin refactoring (move to separate directory, use SDK)
- Joystick mode improvements for sim

---

**Project Maturity**: This is an established development roadmap with deep technical specification. The lack of due dates and low priority classification suggest it functions as a **living backlog** where work is triaged and prioritized by immediate field feedback and customer needs rather than a scheduled release plan. The 1.4% completion rate (3 of 222 tasks) reflects the aspirational nature of the backlog.