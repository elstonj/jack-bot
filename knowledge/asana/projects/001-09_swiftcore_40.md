_Asana snapshot as of 2026-10-31: 226 open tasks, 5 completed (last 90 days)._

# [001-09] SwiftCore 4.0

## Overview
- **Owner:** Jack Elston
- **Team:** BST (Whole Team)
- **Project Type:** Future development of autopilot, ground station, and tablet code
- **Client/Customer:** Internal (Black Swift Technologies)
- **Dollar Value:** Not specified
- **Timeline:** Long-term / ongoing (started 2015-01-19)
- **Status:** Active (low priority)
- **Priority:** Low

**Risk Signals:**
- 226 open tasks with only 5 completed — extremely backlogged
- No due dates on any tasks; no structured timeline
- 11 major unassigned milestones with no target dates
- Indicates this is a long-term roadmap rather than an active sprint project

## Key Deliverables & Milestones

All major milestones are currently unassigned and have no due dates:

1. **Conversion to RTOS**
2. **Better payload system** (multiple cameras, flight plan loading)
3. **Official VTOL / tailsitter support**
4. **SBC Autopilot companion**
5. **New GCS** (Ground Control Station)
6. **MAVLink support**
7. **UAVCAN support**
8. **Multi-vehicle support**
9. **User authentication**
10. **Automated log file handling & OTA firmware updates**
11. **Full Geofencing Support**

## Task Summary

### Totals
- **Open:** 226 tasks
- **Completed:** 5 tasks
- **Completion Rate:** 2.2%

### Breakdown by Assignee

| Assignee | Open Tasks | Completion Rate | Focus Areas |
|----------|-----------|-----------------|------------|
| **Jack Elston** | ~120 | Very low | Autopilot core, comms, payload, calibration, emergency systems, GCS integration, firmware architecture |
| **Maciej Stachura** | ~70 | Very low | VTOL/tailsitter control, estimator, landing modes, sensor handling, simulation, wind estimation |
| **Ben Busby** | ~30 | Very low | Tablet UI, ground station features, flight planning, log handling, simulation |
| **Unassigned** | ~11 (milestones) | N/A | Strategic features |

### Notable Patterns
- **Heavy task concentration on Jack Elston** — indicates he is the core autopilot architect
- **Bug reports mixed with feature requests** — ~30 open bugs (calibration, comms, sensor issues, emergency handling) alongside architectural work
- **No custom field tracking for dollar amounts or priority breakdown** — all tasks flagged "Low" priority
- **Long feature branches in use:** `unified_est`, `yaw_mix`, `vtol` (indicates active development areas)
- **GitLab issue sync active** — some tasks linked to autopilot GitLab repo for traceability

## Recent Activity

As of **Nov 28, 2023** status update:
- **Completed milestones:** None noted
- **Overdue milestones:** None tracked (no due dates set)
- **Overdue tasks:** None tracked (no due dates set)
- **Upcoming milestones:** None scheduled

**Recent completions (all from Oct 30, 2026):**
- Fixed mag declination display format (radians → degrees)
- Fixed waypoint overwrite bug (now replaces whole plan)
- Fixed air-deployed UAS drop menu persistence
- Fixed waypoint display codes (113→"Takeoff", 118→"Error")

*Note: The Oct 2026 dates appear to be testing/demo data from simulator bug reports; the project status note is from Nov 2023.*

## Notes & Context

### Architecture & Development Areas
1. **Control & Estimation:** Significant work on VTOL transitions, landing modes, wind estimation, unified estimator across vehicle types
2. **Safety & Fault Handling:** Multiple tasks around emergency descent, lost GPS/comms handling, battery management, watchdog timers
3. **Hardware Integration:** Payload systems, sensor fusion, addon board management, ESC/motor control, smart battery firmware
4. **Ground Systems:** Tablet UI (SwiftTab) enhancements, GCS improvements, flight planning, OTA updates, log management
5. **Simulation:** Gazebo models for S2, fixedwing, multirotor photogrammetry; X-Plane plugin

### Known Issues (Open Bugs)
- **Critical:** ERROR_NO_BATTERY triggers unexpectedly; Lost GPS blocks emergency descent in joystick mode; S2 throttle kill response slow in sim
- **Calibration:** Surface control limits to max/min in calibrate mode (both tablet and AP); Initial XML load causes odd deflections
- **Payload:** Door opens unintentionally in pre-flight; doesn't hold position in calibrate mode
- **Telemetry:** Height scale mismatch (AP packs x100 vs docs say x1000); RSSI not reported by SWIL
- **Communications:** Joystick mode disconnections during GCS switches; Comms version updates pending
- **Navigation:** Joystick transition/landing for VTOL; No flight tracking on orbit with tailsitter

### Code Quality Observations
- Multiple tasks to remove deprecated/unused code (FIXMEs, rate limiters, termination functions)
- Filter initialization and sensor startup timing needs review
- Firmware warnings accumulating (C++ ODR violations)
- Significant refactoring planned (vehicle controllers, comm architecture, module separation)

### External Dependencies
- SRTM DEM data (need better global coverage, higher resolution)
- MapBox integration investigation for map backend
- Service discovery for WiFi connections
- Handset integration with new VTOL control modes

### Project Maturity
This is a **long-term feature roadmap** rather than a sprint-based project. The low priority designation, absence of due dates, and massive backlog suggest this captures aspirational work and known issues that will be triaged into actual sprints as capacity and customer needs dictate. Real prioritization likely happens elsewhere (in sprint planning or customer requests).