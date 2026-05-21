# [001-09] SwiftCore 4.0

## Overview
- **Client/Customer**: Internal BST development project
- **Dollar Value**: Not specified
- **Timeline**: Started January 19, 2015 - ongoing development project with no defined end date
- **Status**: **ACTIVE BUT STALE DATA**. Raw Asana snapshot shows 165 open tasks, 0 completions (appears to be Nov 2023 or earlier). Earlier knowledge file from April 9, 2026 reported 0 open/3 completed (UAVCAN support, multi-vehicle ground station analysis, GPS time/declination tracking). **Team feedback (May 2026) from Daniel Prendergast directs all new software issues to SwiftCore 3.3 project, not 4.0**, suggesting SwiftCore 4.0 is not the active development branch. **Current actual status unknown—requires clarification from Jack Elston.**
- **Team Members**: Jack Elston (project owner/primary contributor), Maciej Stachura (flight control systems), Ben Busby (ground station/tablet development)
- **Risk Signals**: 
  - Data consistency conflict (Nov 2023 snapshot vs. Apr 2026 active phase)
  - Large unmanaged backlog (165 open tasks); no due dates on any tasks
  - Last official status update November 28, 2023 (stale)
  - Team is routing new software issues to **SwiftCore 3.3**, not 4.0, per Daniel Prendergast (May 2026)
  - Possible project pivot or deprecation in favor of 3.3 branch

## Key Deliverables & Milestones
Major architectural improvements (all unassigned, no due dates):
- **Conversion to RTOS** - Real-time operating system migration
- **Better payload system** - Multiple camera support and flight plan loading
- **Official VTOL/tailsitter support** - Vertical takeoff and landing capabilities
- **SBC Autopilot companion** - Single board computer integration
- **New GCS** - Ground control station redesign
- **MAVLink support** - Industry standard protocol integration
- **UAVCAN support** - *(marked complete April 9, 2026 in earlier data; assigned Jack Elston)*
- **Multi-vehicle support** - *(partial completion noted April 9, 2026; assigned Jack Elston)*
- **User authentication** - Security and access control
- **Automated log file handling and OTA firmware updates** - Remote maintenance capabilities
- **Full Geofencing Support** - No-fly zone enforcement

## Task Summary
- **Total Tasks**: 165 open, 0 completed (per raw Asana data; conflicts with April 2026 data showing 3 completions)
- **Tasks by Assignee** (from raw data):
  - **Jack Elston**: ~65 tasks covering autopilot core, communications, power management, sensor fusion, ESC integration, smart battery firmware, simulation, ECAMS diagnostics
  - **Maciej Stachura**: ~40 tasks focused on flight control algorithms, VTOL/tailsitter enhancements, estimator development, wind estimation, landing logic, filter optimization, Gazebo modeling
  - **Ben Busby**: ~35 tasks covering tablet UI, GCS features, mapping, DEM integration, OTA updates, log file handling, multi-vehicle coordination
  - **Unassigned**: 11 major milestone subtasks

- **Notable Patterns**:
  - Extensive feature backlog with no prioritization or sequencing
  - Heavy GitLab integration via Unito (tasks synchronized with GitLab issues)
  - Strong emphasis on simulation infrastructure (Gazebo, X-Plane plugins)
  - Feature branches tracked for some tasks (unified_est, yaw_mix, vtol)
  - All tasks lack due dates—suggests project operates as feature wishlist rather than scheduled roadmap
  - Multiple duplicate task entries (e.g., "Add addressing for aircraft and ground stations", "Remove FIXMEs" appear twice)
  - Project notes include Gantt data references (start dates 2015-01-19 and 2014-12-29) but no structured timeline

## Recent Activity
**Raw Asana data is stale** (appears to be Nov 2023 snapshot). 

**Earlier activity (April 9, 2026)**: Three tasks completed—all assigned to Jack Elston:
  - UAVCAN support
  - Multi-vehicle ground station analysis
  - GPS time/declination tracking

**Team Direction Change (May 2026)**: Daniel Prendergast explicitly directs team members to **add new software issues to SwiftCore 3.3 project**, not 4.0. Quote: *"For software issues that just adds a task to the SwiftCore 3.3 project like you've always been doing."* (May 14 & 15, 2026)

**Last official Asana status update**: November 28, 2023 ([green] status, zero completions reported at that time)

## Notes & Context

### Critical Data Discrepancy & Team Directive
- **Raw Asana shows 165 open/0 completed** (Nov 2023 snapshot)
- **Earlier data shows 0 open/3 completed** (April 9, 2026)
- **Team is now directing new work to SwiftCore 3.3**, not 4.0 (Daniel Prendergast, May 2026)

**Interpretation**: SwiftCore 4.0 appears to be **archived or deprioritized** in favor of SwiftCore 3.3 as the active development branch. Asana backlog is aspirational/legacy. New development should be tracked in SwiftCore 3.3.

### Project Scope & Technical Focus
- **Comprehensive next-generation autopilot** covering flight control, ground station, and tablet interfaces
- Essentially a 11+ year feature roadmap spanning core architecture, vehicle types, communications, and user interface
- **Key technical areas**:
  - RTOS migration and modular architecture
  - Unified flight estimator for mixed vehicle types (fixed-wing, multirotor, VTOL/tailsitter)
  - Wind estimation and adaptive parameter tuning
  - CAN bus/UAVCAN/UART ESC communication
  - Smart battery board and power management
  - Advanced sensor fusion with failover logic
  - GPS time tracking, magnetic declination, RTK/PPK support
  - Geofencing with height-aware keep-outs
  - OTA firmware updates (autopilot and GCS)
  - Integrated tablet/handset control with loss-of-signal fallback

### Hardware Integration Focus
- CAN-based boards (power, smart battery, radio candidates)
- ESC communication (UART and CAN variants; Castle Creations support noted)
- Addon board watchdog timers (WDT) based on sensor quality
- Payload power distribution (5V DCDC for lasers/cameras)
- Multi-sensor mapping (camera orientation, trigger timing, pulse-to-capture delay)
- Serial numbers on MHP boards

### Integration Points
- SwiftTab (tablet app) for log file handling, DEM management, OTA updates
- Handset/tablet hybrid control with joystick arbitration
- X-Plane and Gazebo simulation environments
- DEM (Digital Elevation Model) data for mapping and terrain following
- Multi-UAS coordination from single ground station
- Service discovery for WiFi communication
- Mapbox investigation for map backend

### Priority & Status Assessment
- **Priority Level**: Low (custom field)
- **Actual Status**: **DEPRECATED/ARCHIVED** per team directive (May 2026). SwiftCore 3.3 is now the active development branch. This project should be treated as a legacy aspirational backlog, not active work.
- **Owner**: Jack Elston (formal owner), but active development has shifted to SwiftCore 3.3
- **Resource Allocation**: Minimal; feature backlog with 11-year timeline and zero due dates

### Recommendations for AI Assistant
- **Do NOT prioritize SwiftCore 4.0 tasks**—team is now routing all new work to SwiftCore 3.3 (Daniel Prendergast, May 2026)
- Treat 165-task list as **legacy aspirational backlog**, not active work queue
- When questions arise about autopilot development priorities, redirect to **SwiftCore 3.3 project** as the active development branch
- Jack Elston