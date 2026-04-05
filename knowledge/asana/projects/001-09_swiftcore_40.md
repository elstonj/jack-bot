# [001-09] SwiftCore 4.0

## Overview
- **Client/Customer**: Internal BST development project
- **Dollar Value**: Not specified
- **Timeline**: Started January 19, 2015 - ongoing development project with no defined end date
- **Status**: Active but low priority - extensive development backlog with 0% completion rate
- **Team Members**: Jack Elston (project owner), Maciej Stachura (flight control systems), Ben Busby (ground station/tablet development)
- **Risk Signals**: All 168 tasks remain open with 0% completion rate; no due dates assigned to any tasks; project shows signs of being a long-term wishlist rather than active development

## Key Deliverables & Milestones
Major architectural improvements planned (all unassigned and undated):
- **Conversion to RTOS** - Real-time operating system migration
- **Better payload system** - Multiple camera support and flight plan loading
- **Official VTOL/tailsitter support** - Vertical takeoff and landing capabilities
- **SBC Autopilot companion** - Single board computer integration
- **New GCS** - Ground control station redesign
- **MAVLink support** - Industry standard protocol integration
- **UAVCAN support** - CAN bus communication protocol
- **Multi-vehicle support** - Control multiple aircraft simultaneously
- **User authentication** - Security and access control
- **Automated log file handling and OTA firmware updates** - Remote maintenance capabilities
- **Full Geofencing Support** - No-fly zone enforcement

## Task Summary
- **Total Tasks**: 168 open, 0 completed (0% completion rate)
- **Tasks by Assignee**:
  - Jack Elston: ~80 tasks (autopilot core, communications, system architecture, cybersecurity)
  - Maciej Stachura: ~50 tasks (flight control algorithms, vehicle dynamics, simulation, landing systems)
  - Ben Busby: ~38 tasks (ground station, tablet UI, mapping features, gazebo simulation)
  - Unassigned: 11 major milestones
- **Notable Patterns**: Heavy focus on architectural improvements; many tasks reference GitLab integration; extensive simulation and testing infrastructure development; strong emphasis on multi-vehicle operations and payload integration

## Recent Activity
Last status update was November 28, 2023, but shows no completed tasks or milestones. Project appears to be in planning/backlog phase with extensive feature wishlist compiled over nearly a decade of development ideas.

## Notes & Context
- **Project Scope**: Comprehensive next-generation autopilot system covering flight control, ground station, and tablet interfaces
- **Technical Focus**: RTOS migration, VTOL support, multi-vehicle operations, advanced payload integration, cybersecurity improvements
- **Development Approach**: Feature branches noted for unified estimator (`unified_est`), yaw mixing (`yaw_mix`), and VTOL development (`vtol`)
- **Integration**: Strong emphasis on simulation (Gazebo, X-Plane), GitLab issue tracking via Unito synchronization
- **Priority Level**: Custom field shows "Low" priority despite comprehensive scope
- **Hardware Integration**: Extensive focus on CAN bus systems, ESC communication, smart battery boards, and sensor fusion
- **User Experience**: Major emphasis on tablet-based controls, multi-UAS support, and automated systems

This appears to be a long-term development roadmap and feature collection rather than an active project with immediate deliverables. The extensive backlog suggests this serves as a repository for future development ideas across BST's entire autopilot ecosystem.