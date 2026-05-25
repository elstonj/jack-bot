# [001-09] SwiftCore 4.0

## Overview
- **Client/Customer**: Internal BST development project
- **Dollar Value**: Not specified
- **Timeline**: Started January 19, 2015 — no defined end date
- **Status**: **ARCHIVED/DEPRECATED** (per Daniel Prendergast, May 14–15, 2026). All new software issues should be added to **SwiftCore 3.3 project** instead. Raw Asana data (Nov 2023 snapshot) shows 165 open tasks with zero due dates and zero completions. Project is no longer the active development branch.
- **Team Members**: 
  - Jack Elston (project owner, primary contributor — ~65 tasks)
  - Maciej Stachura (flight control systems — ~40 tasks)
  - Ben Busby (ground station/tablet development — ~35 tasks)
- **Risk Signals**: 
  - **Team has officially pivoted to SwiftCore 3.3** — Daniel Prendergast directive: *"For software issues that just adds a task to the SwiftCore 3.3 project like you've always been doing"* (May 14–15, 2026)
  - Data staleness (Nov 2023 Asana snapshot vs. May 2026 team directives)
  - Large unmanaged backlog (165 open tasks); zero due dates across entire project
  - No active status updates since November 28, 2023

## Key Deliverables & Milestones
All major milestones remain unassigned with no due dates. Listed for historical context only:

- **Conversion to RTOS** — Real-time operating system migration
- **Better payload system** — Multiple camera support and flight plan loading
- **Official VTOL/tailsitter support** — Vertical takeoff and landing
- **SBC Autopilot companion** — Single board computer integration
- **New GCS** — Ground control station redesign
- **MAVLink support** — Industry standard protocol
- **UAVCAN support** — *(noted complete April 2026 by Jack Elston)*
- **Multi-vehicle support** — *(partial completion noted April 2026 by Jack Elston)*
- **User authentication** — Security and access control
- **Automated log file handling and OTA firmware updates** — Remote maintenance
- **Full Geofencing Support** — Height-aware no-fly zones

## Task Summary
- **Total Tasks**: 165 open, 0 completed (per Nov 2023 Asana data; conflicts with April 2026 completion reporting)
- **Tasks by Assignee**:
  - **Jack Elston** (~65 tasks): Autopilot core architecture, communications protocol design, power management, sensor fusion, ESC integration, smart battery firmware, simulation (Gazebo, X-Plane), ECAMS diagnostics, RTOS conversion, CAN/UART modules, parameter management
  - **Maciej Stachura** (~40 tasks): Flight control algorithms, VTOL/tailsitter landing modes, estimator development (unified estimator, wind estimation, failover logic), filter optimization, Gazebo modeling (E2, fixed-wing), terrain following, QRH/MMEL documentation
  - **Ben Busby** (~35 tasks): Tablet UI (SwiftTab), GCS features, mapping/DEM integration, OTA updates, log handling, multi-vehicle coordination, plot windows, joystick control, preflight tasks, X-Plane integration, Gazebo multirotor photogrammetry
  - **Unassigned**: 11 major milestones

- **Notable Patterns**:
  - Extensive feature backlog with no prioritization or sequencing
  - Heavy GitLab integration (Unito synchronization with GitLab issues noted on select tasks)
  - Strong simulation focus (Gazebo E2/multirotor/fixed-wing models, X-Plane plugin with joystick support)
  - **Zero due dates on all 165 tasks** — operates as aspirational wishlist, not scheduled roadmap
  - Duplicate task entries (e.g., "Add addressing for aircraft and ground stations", "Remove FIXMEs" each appear twice)
  - Feature branches noted for some tasks (unified_est, yaw_mix, vtol)
  - Custom field: Priority = Low

## Recent Activity
**Team Directive (May 14–15, 2026)** — Daniel Prendergast:
> "Cool. For software issues that just adds a task to the SwiftCore 3.3 project like you've always been doing. You can keep adding tasks manually if you prefer."

This supersedes the SwiftCore 4.0 project for all new software work.

**Earlier Activity (April 9, 2026)**: Jack Elston completed three tasks:
- UAVCAN support
- Multi-vehicle ground station analysis
- GPS time/declination tracking

**Last official Asana update**: November 28, 2023 (green status; zero completions reported)

## Notes & Context

### Critical Status: Project Archived in Favor of SwiftCore 3.3
- **Raw Asana shows 165 open/0 completed** (Nov 2023 snapshot — stale)
- **Team is now routing all new software work to SwiftCore 3.3**, not 4.0 (Daniel Prendergast, May 14–15, 2026)
- **Interpretation**: SwiftCore 4.0 is a **legacy aspirational backlog**; active development has shifted to the SwiftCore 3.3 branch

### Project Scope & Technical Areas
Next-generation autopilot architecture spanning 11+ years of feature development:

**Core Architecture**:
- RTOS migration and modular design (comm/CAN as pluggable modules)
- Unified flight estimator for all vehicle types (fixed-wing, multirotor, VTOL/tailsitter)
- Wind estimation and adaptive parameter tuning
- Advanced sensor fusion with failover logic (GPS/pitot/pressure interpolation for gaps)

**Communications & Integration**:
- MAVLink and UAVCAN protocol support
- CAN-based firmware architecture with UART/CAN ESC control (Castle Creations support noted)
- Service discovery for WiFi communication
- Multi-UAS coordination from single ground station
- Handset/tablet hybrid joystick control with loss-of-signal fallback
- Serial numbers in EEPROM on MHP boards

**Flight Control & Safety**:
- Landing modes based on wind estimation
- Geofencing with height-aware keep-outs
- Battery termination logic (mAh-based, energy-aware; Wh calculations)
- Icing detection and emergency engine shutdown
- Laser terrain following with low-laser flagging
- Preflight motor test and multirotor attitude check
- Ground effect flag and TECS engine-out detection review

**Ground Station & Tablet (SwiftTab)**:
- Log file management and download via tablet
- OTA firmware updates for autopilot and GCS
- Real-time telemetry visualization with custom plot windows (scalar vs. scalar)
- Graphical flight planning (waypoints, Dubins paths, altitude profiling, LOS calculation)
- DEM (Digital Elevation Model) integration for terrain mapping (SRTM files, MapBox investigation)
- Payload control and sensor assignment UI (camera orientation, trigger timing, pulse-to-capture delay)
- Wind barbs, system time display, flight notes capture
- Multi-sensor mapping support (dropdown instead of "skip")

**Hardware Integration**:
- Power management board with backup power ECAMS
- Smart battery board firmware with capacity-based percentage
- Addon board watchdog timers (WDT) based on sensor quality
- 5V DCDC for payload power (lasers, cameras)
- Multi-sensor mapping with camera orientation and trigger metadata
- USB access to aircraft through tablet
- Payload verification UI and communications

**Simulation & Testing**:
- Gazebo integration (E2, fixed-wing, multirotor photogrammetry models)
- X-Plane plugin with joystick support and user-positioned start location
- Preflight motor test and MR attitude check

### Priority & Resource Allocation
- **Priority Level**: Low (custom field)
- **Actual Status**: ARCHIVED (per team directive, May 14–15, 2026)
- **Owner**: Jack Elston (formal), but active development has migrated to SwiftCore 3.3
- **Resource