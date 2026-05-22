# [001-10] SwiftCore 3.2

## Overview
- **Client/Customer**: Internal maintenance project for BST autopilot system
- **Dollar Value**: Not specified
- **Timeline**: Active maintenance project with tasks spanning 2022–2023; last activity November 2023
- **Status**: Active maintenance (99% completion rate, 302 of 305 tasks complete). **Workflow Update (May 2026): Per Daniel Prendergast (May 8–15, 2026), new software issues should be added to the SwiftCore 3.3 project going forward, not SwiftCore 3.2.** SwiftCore 3.2 itself remains in stable maintenance phase.
- **Team Members**: Jack Elston (Owner), Ben Busby, Maciej Stachura, with whole BST team involvement
- **Risk Signals**: 3 open tasks in "Ready for Testing" status with no due dates; generally low risk given low priority rating and stable completion history. No overdue items.

## Key Deliverables & Milestones
- Master branch (3.2) autopilot and tablet code maintenance
- Multiple hotfix branches deployed: master, hotfix/area_popup, 3.2.9, 3.2.8, 3.2.7, 3.2.6, world_velocity, fp_handshaking, engineout_land_detect, fixedwing_land_detect
- Documentation updates (completed November 22, 2023)
- Simulator updates (completed November 17, 2023)
- Comprehensive testing across S1 2030/2040, FW 2030/2040, Xplane, and Gazebo platforms

## Task Summary
- **Total Tasks**: 305 (3 open, 302 completed = 99% completion rate)
- **Tasks by Assignee**:
  - Jack Elston: Primary contributor with majority of completed tasks
  - Ben Busby: 3 open tasks, focused on UI/tablet issues; multiple completed tasks in preflight mode, joystick control, and NAV bug fixes
  - Maciej Stachura: Significant contributor; completed tasks in flight testing, bug fixes, landing detection, and propulsion failure scenarios
  - 1 unassigned task (completed)
- **Notable Patterns**: Heavy use of custom fields for tracking hotfix branches and testing status across multiple platforms; extensive platform-specific testing (S1 2030/2040, FW 2030/2040, Xplane, Gazebo) with granular completion tracking; low priority rating reflecting maintenance nature

## Recent Activity
- **Last update**: November 28, 2023 (green status update)
- **Recently completed** (November 17–22, 2023):
  - Simulator updates (Jack Elston, November 17)
  - Documentation updates (Jack Elston, November 22)
  - Flight plan synchronization and related fixes (Maciej Stachura, earlier)
- **All 3 remaining open tasks are in "Ready for Testing" status, assigned to Ben Busby**:
  - Lost comms waypoint text input issue (master branch) – can't change text to set waypoint to number
  - Level 2 error warning popup issues (master branch) – mission limits violation with waypoint, static pressure failure
  - Map corridor area menu tap issue (hotfix/area_popup branch) – tapping area doesn't bring up mapping menu
- No overdue milestones or tasks as of November 28, 2023

## Notes & Context
This is a critical maintenance project for BST's core autopilot technology (SwiftCore 3.2). The project demonstrates comprehensive quality assurance with extensive testing across multiple hardware platforms and simulators.

**Workflow Update (May 2026)**: Per Daniel Prendergast (May 8–15, 2026), new software issues should be added to the **SwiftCore 3.3 project** going forward, not SwiftCore 3.2. SwiftCore 3.2 is in stable maintenance mode. An Asana Form has been created as part of standard post-flight process to capture aircraft and equipment issues, automatically routing them to Fleet Maintenance (hardware) or appropriate software projects.

**Key technical areas addressed in completed work**:
- **Flight safety systems**: Voltage monitoring, propulsion failure detection, landing protocols, static pressure failure detection, watchdog timers for GNSS and dynamic pressure
- **Communication systems**: Flight plan transmission, tablet connectivity, waypoint handshaking improvements, kill switch detection timing
- **Security vulnerabilities**: Multiple GCS denial of service fixes (Mission Plan Delete, checkFD memory corruption, 3-packet crash sequence), remote authentication issues
- **User interface improvements**: Mission planning, joystick control, preflight mode forcing, mapping corridor functionality, "null island" display fixes
- **Hardware integration**: SD card handling (full card lockup, bootloader hang), sensor data processing, GNSS data reliability, pitot tube monitoring, power board ESC control reconnection
- **Power Management & Flight Control**: Under-voltage detection, joystick range/deadband improvements, flight path angle limitations, auto-takeoff and manual control improvements
- **Landing & Propulsion Systems**: Landing detection enhancements for propulsion loss scenarios, landing flare behavior on engine failure, flight plan synchronization improvements
- **Data Logging & Monitoring**: Power-on and system initialization packet logging, static pressure stabilization, GNSS reliability with watchdog monitoring

The project shows strong engineering discipline with hotfix branch tracking and multi-platform testing requirements for each fix. The high completion rate and "Ready for Testing" status of remaining tasks indicates stable maintenance phase. All 3 open tasks are awaiting testing—no blockers or critical issues identified.