_Asana snapshot as of 2026-10-24: 9 open tasks, 57 completed (last 90 days)._

# [001-14] SwiftCore 3.3

## Overview
- **Client/Customer:** Internal (BST whole team)
- **Project Type:** Development of autopilot, ground station, and tablet code (3.3 develop branch)
- **Owner:** Jack Elston
- **Status:** [YELLOW] Active with overdue milestones as of Nov 28, 2023
- **Priority:** Low (custom field)
- **Team Members:** Jack Elston, Ben Busby, Maciej Stachura
- **Risk Signals:** Multiple overdue milestones with no due dates assigned; 9 open tasks including critical simulator bug fixes and feature milestones; significant backlog of unscheduled work

## Key Deliverables & Milestones
All milestones are currently open with no due dates assigned:
- Final release supporting 2030, 2040, 2050, and 3000 hardware
- Final release supporting commercial S1
- Initial VTOL support
- Official scripting release (including payload control)
- Control through payload serial interface
- App support (payload, flight parameters, scripting)

## Task Summary
- **Total:** 9 open, 57 completed (86% completion rate)
- **Open Tasks by Assignee:**
  - Ben Busby: 3 tasks (altitude change during landing descent, AGL elevation display bug, script goto issue)
  - Maciej Stachura: 0 tasks
  - Unassigned: 6 tasks (all milestone definitions)
  
- **Notable Patterns:** 
  - Heavy focus on bug fixes from simulator test reports (SIM-series bugs)
  - Recent completion spike around 2026-10-21 to 2026-10-23 (57 tasks completed in rapid succession)
  - Bug fixes span autopilot behavior, tablet UI, communications, and sensor handling
  - No dollar amounts tracked in custom fields

## Recent Activity
**Completed (2026-10-23, most recent):** 11 tasks closed in single day including aircraft control window UI fixes, telemetry menu fixes, user mode switching bugs, and sensor failure response validation (S3 simulator tests for pitot loss, mag loss, static pressure, GPS loss).

**Completed (2026-10-22):** Bug fixes for joystick mode transitions, landing plan switching, Dubins path computation, surface actuation, manual takeover, and dynamic pressure sensor errors.

**Completed (2026-10-21):** Commands and scripting issues, flight timer validation, sensor alerts, IAS error handling, USB bootloader flag update, CAN bus MHP integration.

**Currently Open (No Recent Movement):**
- Script goto 350m at 5m/s then 20m/s ACK failure + unintended landing (SIM-0020)
- Altitude change to 3500m during landing descent flashes green then drops without error (SIM-0032)
- AGL elevation display in node panel shows m/100 scaling error until app restart (custom field link included)

## Notes & Context
- **Data Quality Issue:** All completed tasks show completion date 2026-10-21 to 2026-10-23, but project status was last updated Nov 28, 2023. This suggests either data from the future or significant timestamp inconsistency in the Asana project.
- **Testing Approach:** Heavy reliance on simulator-based QC (JSBSim models for S0, S1, S2, S3 variants). Bug reports reference specific simulator versions (0.9.0~rc17, 0.9.0~rc18, 0.9.0~rc22).
- **Feature Branches:** Some completed tasks reference `release/3.3.0` branch, suggesting version preparation is underway.
- **Unscheduled Work:** All milestone tasks lack due dates, making timeline planning difficult. 3 critical open bugs (scripting, altitude control, display scaling) also lack target resolution dates.
- **Communication Channels:** Notes reference separate simulator repo commits, suggesting distributed development across autopilot, ground station (GCS/Xtend), tablet (SwiftTab), and simulator codebases.