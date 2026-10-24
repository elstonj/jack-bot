_Asana snapshot as of 2026-10-24: 219 open tasks, 0 completed (last 90 days)._

# SwiftCore 4.0

## Overview

- **Project Owner:** Jack Elston
- **Team:** Whole BST team (Jack Elston, Maciej Stachura, Ben Busby assigned to tasks)
- **Status:** Active — low priority long-term development
- **Client/Value:** Internal R&D. No explicit dollar value noted.
- **Timeline:** Ongoing backlog project (no defined end date; start noted as 2015-01-19 in Gantt data)
- **Risk Signals:** 219 open tasks with zero completions; no due dates assigned; backlog-style project with no immediate delivery pressure

## Description

SwiftCore 4.0 is BST's core software platform roadmap covering future development of autopilot firmware, ground control station (GCS), and tablet applications. The project encompasses major architectural improvements (RTOS conversion, unified estimator, new GCS) and incremental feature/bug fixes across all three software domains.

## Key Deliverables & Milestones

Major unstarted milestones (all unassigned, no due dates):

1. **Conversion to RTOS** — Fundamental architecture shift for autopilot
2. **Better payload system** — Support multiple cameras and flight plan loading
3. **Official VTOL / tailsitter support** — Vehicle variant expansion
4. **SBC Autopilot companion** — Single-board computer integration
5. **New GCS** — Ground control station redesign
6. **MAVLink support** — Industry-standard protocol
7. **UAVCAN support** — CAN-based communication protocol
8. **Multi-vehicle support** — Manage multiple UAS simultaneously
9. **User authentication** — Security/multi-user support
10. **Automated log file handling and OTA firmware updates**
11. **Full Geofencing Support**

No dollar amounts or completion milestones defined.

## Task Summary

- **Total:** 219 open, 0 completed
- **Assignment breakdown:**
  - **Jack Elston:** ~120 tasks (mostly bug reports, infrastructure improvements, comms/payload work, UI/tablet features)
  - **Maciej Stachura:** ~65 tasks (flight control, estimator, VTOL/tailsitter logic, simulation, documentation)
  - **Ben Busby:** ~25 tasks (tablet UI, GCS, flight planning, simulation)
  - **Unassigned:** 11 milestone tasks

- **Notable patterns:**
  - No completion tracking; pure backlog state
  - Heavy focus on bug fixes and missing features across flight phases (takeoff, transition, landing, joystick mode, lost comms scenarios)
  - Significant VTOL/multirotor work (Maciej's branch)
  - Tablet/UI features growing (Ben's work)
  - No time estimates or priority rankings beyond the "Low" custom field for the project itself

## Task Categories & Themes

### Critical Known Issues (Jack Elston)
- Roll command logging error on takeoff
- `ERROR_NO_BATTERY` causing missed flight legs
- Calibration mode surface limiting bugs
- Telemetry height scale mismatch (APacking x100 vs. documented m*1000)
- Payload door premature opening
- Joystick control edge cases (kill switch, lost comms, throttle after flare)
- GPS/battery-related flight terminate logic gaps

### Flight Control & Estimation (Maciej Stachura)
- Estimator improvements (GPS/pressure outage handling, unified estimator across vehicle types)
- VTOL-specific logic (transition failures, landing alignment, clog detection)
- Controller tuning (flare energy-based, wind-aware climb limits, dubins path planning)
- Sensor initialization and WDT monitoring
- Engine-out and emergency descent scenarios

### Tablet/UI & Ground Station (Ben Busby)
- Log file management (download, upload to logparse.bst.aero, checksums)
- OTA updates for GCS and autopilot
- Flight planning UX (altitude limits, lost-comm waypoint clarity, multiple sensor selection)
- Plotting and telemetry visualization (system time, wind barbs, scalar plots)
- Multi-UAS support and handset/tablet control switching

### Infrastructure & Comms
- Modular architecture (CAN, comms, ESC protocols as modules)
- Protocol updates (MIMO radio, RTK, PPK, PPS integration)
- Smart battery board firmware
- Xplane simulation plugin
- Service discovery for WiFi
- Payload parameter rethinking

## Recent Activity

No recent completion data; task list appears to be a curated long-term backlog. Last status note dated **Nov 28, 2023** marked project as **[green]** but provided no detail on work completed or near-term priorities.

## Notes & Context

1. **No Due Dates:** Entire project lacks due dates, suggesting this is a prioritized wish-list rather than a committed delivery schedule.

2. **Feature Branches Noted:**
   - `unified_est` — Maciej's estimator unification work
   - `yaw_mix` — Rudder control rethinking
   - `vtol` — Vehicle controller refactor

3. **Duplicate Tasks:** Some tasks appear twice (e.g., "Add comm and can protocol as modules," "Remove FIXMEs," "Add addressing for aircraft and ground stations"), possibly from view/section duplication.

4. **External Tool Integration:** Multiple references to GitLab issues (e.g., Autopilot issue #5), Gazebo simulation, X-Plane plugin, logparse.bst.aero integration.

5. **Gantt Start Date:** "2015-01-19" appears in task notes, indicating this project has been in backlog form for many years.

6. **Zero Completions:** Despite 219 tasks, no completed tasks recorded — suggests this is a live development list, not a retrospective, and tasks are completed outside Asana or not marked done.