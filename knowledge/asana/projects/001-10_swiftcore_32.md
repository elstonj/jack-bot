# [001-10] SwiftCore 3.2

## Overview
- **Client/Customer**: Internal maintenance project for BST autopilot system
- **Dollar Value**: Not specified
- **Timeline**: Active maintenance project with tasks spanning 2022-2023, last activity November 2023
- **Status**: Active maintenance (99% completion rate, 302 of 305 tasks complete)
- **Team Members**: Jack Elston (Owner), Ben Busby, Maciej Stachura, with whole BST team involvement
- **Risk Signals**: 3 open tasks ready for testing with no due dates; generally low risk given low priority rating

## Key Deliverables & Milestones
- Master branch (3.2) autopilot and tablet code maintenance
- Multiple hotfix branches deployed: master, hotfix/area_popup, 3.2.9, 3.2.8, 3.2.7, 3.2.6, world_velocity, fp_handshaking, engineout_land_detect, fixedwing_land_detect
- Documentation updates completed March 2023
- Simulator updates completed November 2023
- Comprehensive testing across S1 2030/2040, FW 2030/2040, Xplane, and Gazebo platforms

## Task Summary
- **Total Tasks**: 305 (3 open, 302 completed = 99% completion rate)
- **Tasks by Assignee**:
  - Jack Elston: Primary contributor with majority of completed tasks
  - Ben Busby: 3 open tasks, focused on UI/tablet issues
  - Maciej Stachura: Significant contributor, flight testing and bug fixes
  - 1 unassigned task (completed)
- **Notable Patterns**: Heavy use of custom fields for tracking hotfix branches and testing status across multiple platforms; extensive testing requirements with specific hardware configurations

## Recent Activity
- Last major activity in November 2023 with simulator updates and documentation refresh
- Recent completions include syncing flight plans, landing plan issues, and voltage monitoring
- All 3 remaining open tasks are in "Ready for Testing" status, indicating near completion:
  - Lost comms waypoint text input issue (Ben Busby, master branch)
  - Level 2 error warning popup issues (Ben Busby, master branch)  
  - Map corridor area menu tap issue (Ben Busby, hotfix/area_popup branch)

## Notes & Context
This is a critical maintenance project for BST's core autopilot technology (SwiftCore 3.2). The project demonstrates comprehensive quality assurance with extensive testing across multiple hardware platforms (S1 2030/2040, FW 2030/2040) and simulators (Xplane, Gazebo). 

Key technical areas addressed include:
- **Flight safety systems**: Voltage monitoring, propulsion failure detection, landing protocols, static pressure failure detection
- **Communication systems**: Flight plan transmission, tablet connectivity, waypoint handshaking improvements
- **Security vulnerabilities**: Multiple GCS denial of service fixes, remote authentication issues
- **User interface improvements**: Mission planning, joystick control, preflight mode forcing, mapping corridor functionality
- **Hardware integration**: SD card handling, sensor data processing, GNSS data reliability, pitot tube monitoring

Recent focus areas based on completed tasks:
- **Power management**: Under-voltage detection and monitoring systems with operator options for "Return to Land" or "Terminate Flight"
- **Flight plan synchronization**: Improvements to mission upload reliability and waypoint transmission
- **Landing detection**: Enhanced algorithms for various failure scenarios including propulsion loss
- **Joystick control**: Improved deadband/range settings and world velocity control implementation

The project shows strong engineering discipline with hotfix branch tracking and multi-platform testing requirements for each fix. Priority is set to "Low" reflecting its maintenance nature, with status updates indicating good project health as of November 28, 2023. The high completion rate and "Ready for Testing" status of remaining tasks suggests the project is in a stable maintenance phase.