_Asana snapshot as of 2026-10-30: 231 open tasks, 0 completed (last 90 days)._

# [001-09] SwiftCore 4.0

## Overview

- **Client/Customer:** Internal BST development (whole team)
- **Project Type:** Future development platform for autopilot, ground station (GCS), and tablet software
- **Owner:** Jack Elston
- **Status:** ACTIVE – Long-term roadmap with 231 open tasks, 0 completed
- **Priority:** Low (custom field)
- **Team:** Whole BST team (Jack Elston, Maciej Stachura, Ben Busby primary assignees)
- **Timeline:** Initiated 2015-01-19; no target completion date
- **Risk Signals:** 
  - No due dates on any tasks (milestone or subtask level)
  - No completion tracking — all 231 tasks remain open
  - Large backlog suggests deprioritization or long-term foundational work

## Key Deliverables & Milestones

All milestones are unassigned with no due dates. Major feature areas:

1. **Conversion to RTOS** — Autopilot architecture refactor
2. **Better payload system** — Multi-camera support, flight plan loading
3. **Official VTOL / tailsitter support** — Vehicle platform expansion
4. **SBC Autopilot companion** — Single-board computer integration
5. **New GCS** — Ground control station redesign
6. **MAVLink support** — Standard protocol integration
7. **UAVCAN support** — CAN-based communication
8. **Multi-vehicle support** — Fleet management
9. **User authentication** — Security/access control
10. **Automated log file handling & OTA firmware updates** — System management
11. **Full Geofencing Support** — Safety/regulatory compliance

## Task Summary

- **Total Tasks:** 231 open, 0 completed
- **Primary Assignees:**
  - **Jack Elston** — ~120 tasks (autopilot core, comms, hardware integration, payload, UI/GCS)
  - **Maciej Stachura** — ~70 tasks (control systems, estimators, VTOL, simulation, physics)
  - **Ben Busby** — ~40 tasks (tablet/GCS UI, flight planning, mapping, simulation)

- **Task Categories (inferred):**
  - **Bug fixes & refinements** (~30 tasks) — Flight termination logic, calibration, telemetry scaling, surface control, comms sync
  - **Control & estimation** (~40 tasks) — TECS, wind alignment, flare logic, gyro feedback, clog detection, VTOL transitions
  - **Hardware & comms** (~35 tasks) — UART/CAN integration, ESC communication, battery management, RTK/PPK, radio
  - **Simulation & testing** (~20 tasks) — Gazebo models, X-Plane plugin, preflight checks
  - **UI/Tablet features** (~45 tasks) — Plot windows, joystick mode, log management, parameter dialogs, mapping UI
  - **Architecture & refactor** (~25 tasks) — Remove ifdef macros, unified estimator, protocol modules, code cleanup
  - **Long-term roadmap** (~16 tasks) — RTOS conversion, geofencing, authentication, new GCS

- **Completion Rate:** 0% (no closed tasks)

## Recent Activity

No recent activity visible from task completion. Project appears to be a working backlog rather than an actively tracked sprint. Status update dated **Nov 28, 2023** references:
- Overdue milestones as of Nov 28
- Overdue tasks as of Nov 28
- Completed milestones as of Nov 28
- Completed tasks as of Nov 28

However, no specific overdue items or completions are listed in the summary. The presence of "Ready for Testing" status labels on a few tablet UI tasks (error waypoint display, takeoff menu display, drop menu, heading hold) suggests some recent work, but these remain open.

## Notes & Context

1. **Architectural Scope:** This is a comprehensive autopilot/ground station platform supporting fixed-wing, VTOL, multirotor, and tailsitter vehicles with payloads, communications, simulation, and tablet/handset control.

2. **Known Bugs & Issues:** Many tasks document specific failure modes (e.g., "Lost GPS error doesn't allow for aborting emergency descent," "S0 AD SIM motor power loss critical error," "ERROR_NO_BATTERY occured on E2 causing it to miss a mapping flight leg"). These appear to be integration/testing discoveries rather than new feature work.

3. **Integration Points:** Heavy emphasis on dual-layer control (handset + tablet), comms protocol (MAVLink, UAVCAN, UART), sensor fusion (GPS, pitot, pressure, laser altitude), and failsafe logic (lost comms, lost GPS, lost power, motor failure).

4. **Code Quality:** Multiple tasks address technical debt (remove ifdef macros, remove FIXMEs, code cleanup, firmware warnings, test coverage).

5. **Feature Branching:** Two tasks reference feature branches:
   - `unified_est` — Unified estimator for all vehicle types
   - `yaw_mix` — Controller-based rudder mixing
   - `vtol` — Vehicle controller refactor

6. **External Dependencies:** GitLab issue sync on at least one VTOL motor/rotor thrust cutoff task. X-Plane plugin and Gazebo simulation suggest development/test infrastructure outside Asana.

7. **No Budget Tracking:** No dollar amounts visible in task data; priority is "Low" despite scope, suggesting this is foundational work not tied to immediate revenue.

---

**Assessment:** This is a mature, multi-year backlog for a complex autonomous vehicle platform. The lack of due dates, assignee discipline on open tasks, and zero completion suggests it is either:
- A long-term vision document (roadmap) rather than an active sprint backlog
- Actively developed in parallel systems (GitLab, etc.) with Asana serving as a reference

Recommend clarification on which tasks are in-flight vs. aspirational.