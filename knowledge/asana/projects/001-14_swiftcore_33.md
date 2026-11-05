_Asana snapshot as of 2026-11-05: 7 open tasks, 60 completed (last 90 days)._

# [001-14] SwiftCore 3.3

## Overview
- **Owner:** Jack Elston
- **Team:** BST (Whole Team)
- **Project Focus:** Development of the 3.3 (develop) branch of autopilot, ground station, and tablet code
- **Status:** **ARCHIVED** (as of Nov 28, 2023)
- **Priority:** Low
- **Dollar Value:** Not specified in project data
- **Task Completion:** 60 completed, 7 open (89.6% complete)

## Key Deliverables & Milestones
Seven unassigned milestone/feature tasks remain open with no due dates:
1. Final release supporting 2030, 2040, 2050, and 3000 hardware
2. Final release supporting commercial S1
3. Initial VTOL support
4. Official scripting release (payload control)
5. Control through payload serial interface
6. App support (payload, flight parameters, scripting)
7. Motor throttle idle response bug (surfaces tab)

## Task Summary
- **Total:** 67 tasks (60 completed, 7 open)
- **Primary Assignees:**
  - **Ben Busby** – App/tablet UI issues (preflight warnings, telemetry menu, AGL elevation display, node panel) — high completion rate
  - **Maciej Stachura** – Autopilot path/navigation logic, sensor failure handling, VTOL testing, flight diversion issues — high completion rate
  - **Jack Elston** – System integration, PWM configuration, USB bootloader, joystick mode, sensor alerts, CAN bus MHP integration — high completion rate
- **Pattern:** Most work concentrated on bug fixes and integration testing across autopilot (AP), ground station (GCS/Xtend), and tablet (SwiftTab) components

## Recent Activity
Latest completed tasks (Oct 21–26, 2026):
- Multiple simulator bug fixes from SIM-0017 through SIM-0040 (aircraft control window, telemetry menu, preflight warnings, sensor failures)
- S3 simulator model refinements (ground contact points, airspeed loss detection at altitude, pitot/static pressure issues)
- Joystick mode fixes (takeover logic, manual mode transitions, climbout prevention)
- Commands and scripting validation (VTOL scripting support, fixed-wing climb/descent commands)
- Hardware integration (PWM channel setup for S00001, MHP CAN bus integration, USB bootloader flag for hardware 2050)

## Notes & Context
- **Completion Timeline:** Most work completed Oct 21–26, 2026; project marked archived Nov 28, 2023 (date inconsistency in Asana data)
- **Test Coverage:** Heavy use of simulator (JSBSim models S0, S2, S3) for QC, with cross-validation on hardware (S1-22, S10011, S10020)
- **Open Milestones:** Remain unassigned and without due dates, suggesting post-release feature roadmap rather than active blockers
- **Bug Pattern:** Concentrate in app state management (menu/window failures after mode changes), sensor error handling (airspeed, pressure dropouts), and path computation (Dubins curves, waypoint sequencing)
- **No Dollar Amount:** Custom field Priority is "Low"; no budget/revenue tracking visible