# [001-10] SwiftCore 3.2

## Overview
- **Client/Customer**: Internal maintenance project for BST autopilot system
- **Dollar Value**: Not specified
- **Timeline**: Active maintenance project with tasks spanning 2022–2023; last activity November 2023
- **Status**: **Stable maintenance phase.** Per Daniel Prendergast (May 11–15, 2026), **new software issues should be routed to SwiftCore 3.3 project going forward.** SwiftCore 3.2 remains in stable maintenance with 3 open tasks in "Ready for Testing" status. No overdue items.
- **Team Members**: Jack Elston (Owner), Ben Busby, Maciej Stachura, with whole BST team involvement
- **Risk Signals**: None. 3 open tasks awaiting testing with no due dates; low priority rating reflects stable maintenance status.

## Key Deliverables & Milestones
- Master branch (3.2) autopilot and tablet code maintenance
- Multiple hotfix branches deployed: master, hotfix/area_popup, 3.2.9, 3.2.8, 3.2.7, 3.2.6, world_velocity, fp_handshaking, engineout_land_detect, fixedwing_land_detect
- Documentation updates (completed November 22, 2023)
- Simulator updates (completed November 17, 2023)
- Comprehensive testing across S1 2030/2040, FW 2030/2040, Xplane, and Gazebo platforms

## Task Summary
- **Total Tasks**: 308 (3 open, 305 completed = 99% historical completion rate)
- **Current Open Tasks** (all assigned to Ben Busby, all "Ready for Testing", no due dates):
  1. Can't change text to set lost comms waypoint to a number in mission tab (master branch)
  2. Warning for some level 2 errors doesn't create pop up window — mission limits violation with waypoint, static pressure failure (master branch)
  3. Tapping on an area made through the "map corridor" option doesn't bring up the mapping menu (hotfix/area_popup branch)
- **Key Contributors**:
  - Jack Elston: Primary contributor, owner
  - Ben Busby: Current focus on open UI/tablet issues; historical work on preflight mode, joystick control, NAV bug fixes
  - Maciej Stachura: Flight testing, bug fixes, landing detection, propulsion failure scenarios
- **Notable Patterns**: Heavy use of custom fields for tracking hotfix branches and testing status across multiple platforms; extensive platform-specific testing (S1 2030/2040, FW 2030/2040, Xplane, Gazebo); low priority rating reflecting maintenance nature

## Recent Activity
- **Last update**: November 28, 2023 (green status update)
- **Recently completed** (November 17–22, 2023):
  - Simulator updates (Jack Elston, November 17)
  - Documentation updates (Jack Elston, November 22)
  - Flight plan synchronization and related fixes (Maciej Stachura, earlier)
- **Current work**: All 3 remaining open tasks assigned to Ben Busby, all in "Ready for Testing" status with no due dates

## Notes & Context
This is a critical maintenance project for BST's core autopilot technology (SwiftCore 3.2). The project demonstrates comprehensive quality assurance with extensive testing across multiple hardware platforms and simulators.

**Workflow Directive (May 2026)**: Per Daniel Prendergast (May 11–15, 2026), **new software issues should be routed to the SwiftCore 3.3 project going forward, not SwiftCore 3.2.** SwiftCore 3.2 is in stable maintenance mode. Teams may continue adding tasks manually to SwiftCore 3.3 if preferred. An Asana Form has been created as part of standard post-flight process to capture aircraft and equipment issues, automatically routing them to Fleet Maintenance (for hardware issues) or the appropriate software project (SwiftCore 3.3 for software issues).

**Key technical areas addressed in completed work**:
- **Flight safety systems**: Voltage monitoring, propulsion failure detection, landing protocols, static pressure failure detection, watchdog timers for GNSS and dynamic pressure
- **Communication systems**: Flight plan transmission, tablet connectivity, waypoint handshaking improvements, kill switch detection timing
- **Security vulnerabilities**: Multiple GCS denial of service fixes (Mission Plan Delete, checkFD memory corruption, 3-packet crash sequence), remote authentication issues
- **User interface improvements**: Mission planning, joystick control, preflight mode forcing, mapping corridor functionality, "null island" display fixes
- **Hardware integration**: SD card handling (full card lockup, bootloader hang), sensor data processing, GNSS data reliability, pitot tube monitoring, power board ESC control reconnection
- **Power Management & Flight Control**: Under-voltage detection, joystick range/deadband improvements, flight path angle limitations, auto-takeoff and manual control improvements
- **Landing & Propulsion Systems**: Landing detection enhancements for propulsion loss scenarios, landing flare behavior on engine failure, flight plan synchronization improvements
- **Data Logging & Monitoring**: Power-on and system initialization packet logging, static pressure stabilization, GNSS reliability with watchdog monitoring

The project shows strong engineering discipline with hotfix branch tracking and multi-platform testing requirements for each fix. All 3 open tasks are awaiting testing with no identified blockers or critical issues.