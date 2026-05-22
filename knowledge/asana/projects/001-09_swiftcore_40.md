# [001-09] SwiftCore 4.0

## Overview
- **Client/Customer**: Internal BST development project
- **Dollar Value**: Not specified
- **Timeline**: Started January 19, 2015 — no defined end date
- **Status**: **ARCHIVED/DEPRECATED** (per team directive, May 2026). Daniel Prendergast has directed all new software issues to **SwiftCore 3.3 project** instead. Raw Asana data (Nov 2023 snapshot) shows 165 open tasks with no due dates; earlier data (April 2026) reported 3 completions. Project is no longer the active development branch.
- **Team Members**: 
  - Jack Elston (project owner, primary contributor)
  - Maciej Stachura (flight control systems)
  - Ben Busby (ground station/tablet development)
- **Risk Signals**: 
  - **Team has pivoted to SwiftCore 3.3** — new software work should not be added here
  - Data staleness (Nov 2023 Asana snapshot vs. May 2026 team directives)
  - Large unmanaged backlog (165 open tasks); zero due dates
  - No active status updates since November 28, 2023

## Key Deliverables & Milestones
All major milestones remain unassigned with no due dates. Listed for historical context only:

- **Conversion to RTOS** — Real-time operating system migration
- **Better payload system** — Multiple camera support and flight plan loading
- **Official VTOL/tailsitter support** — Vertical takeoff and landing
- **SBC Autopilot companion** — Single board computer integration
- **New GCS** — Ground control station redesign
- **MAVLink support** — Industry standard protocol
- **UAVCAN support** — *(noted complete April 2026)*
- **Multi-vehicle support** — *(partial completion noted April 2026)*
- **User authentication** — Security and access control
- **Automated log file handling and OTA firmware updates** — Remote maintenance
- **Full Geofencing Support** — Height-aware no-fly zones

## Task Summary
- **Total Tasks**: 165 open, 0 completed (per raw Nov 2023 data; conflicts with April 2026 reporting 3 completions)
- **Tasks by Assignee** (from raw Asana data):
  - **Jack Elston**: ~65 tasks — autopilot core, communications, power management, sensor fusion, ESC integration, smart battery firmware, simulation, ECAMS diagnostics
  - **Maciej Stachura**: ~40 tasks — flight control algorithms, VTOL/tailsitter, estimator development, wind estimation, landing logic, filter optimization, Gazebo modeling
  - **Ben Busby**: ~35 tasks — tablet UI, GCS features, mapping, DEM integration, OTA updates, log handling, multi-vehicle coordination
  - **Unassigned**: 11 major milestones

- **Notable Patterns**:
  - Extensive feature backlog with no prioritization or sequencing
  - Heavy GitLab integration (Unito synchronization with GitLab issues)
  - Strong simulation focus (Gazebo, X-Plane plugins)
  - **Zero due dates on all 165 tasks** — operates as aspirational wishlist, not scheduled roadmap
  - Duplicate task entries (e.g., "Add addressing for aircraft and ground stations", "Remove FIXMEs" each appear twice)
  - Feature branches noted for some tasks (unified_est, yaw_mix, vtol)

## Recent Activity
**Team Directive (May 2026)** — Daniel Prendergast, May 14 & 15, 2026:
> "For software issues that just adds a task to the SwiftCore 3.3 project like you've always been doing. You can keep adding tasks manually if you prefer."

**Earlier completions (April 9, 2026)**: Jack Elston completed three tasks:
- UAVCAN support
- Multi-vehicle ground station analysis
- GPS time/declination tracking

**Last official Asana update**: November 28, 2023 (green status; zero completions reported at that time)

## Notes & Context

### Critical Status: Project Archived in Favor of SwiftCore 3.3
- **Raw Asana shows 165 open/0 completed** (Nov 2023 snapshot — stale)
- **Team is now routing all new software work to SwiftCore 3.3**, not 4.0 (Daniel Prendergast, May 14–15, 2026)
- **Interpretation**: SwiftCore 4.0 is a **legacy aspirational backlog**; development has shifted to the active SwiftCore 3.3 branch

### Project Scope & Technical Areas
Next-generation autopilot architecture spanning 11+ years of feature development:

**Core Architecture**:
- RTOS migration and modular design (comm/CAN as pluggable modules)
- Unified flight estimator for all vehicle types (fixed-wing, multirotor, VTOL/tailsitter)
- Wind estimation and adaptive parameter tuning
- Advanced sensor fusion with failover logic

**Communications & Integration**:
- MAVLink and UAVCAN protocol support
- CAN-based firmware architecture
- UART/CAN ESC control (Castle Creations support noted)
- Service discovery for WiFi communication
- Multi-UAS coordination from single ground station
- Handset/tablet hybrid joystick control with loss-of-signal fallback

**Flight Control & Safety**:
- Landing modes based on wind estimation
- Geofencing with height-aware keep-outs
- Battery termination logic (mAh-based, energy-aware)
- Icing detection and emergency engine shutdown
- Laser terrain following
- GPS/pitot/pressure failover and interpolation for gaps

**Ground Station & Tablet (SwiftTab)**:
- Log file management and download via tablet
- OTA firmware updates (autopilot and GCS)
- Real-time telemetry visualization with custom plot windows
- Graphical flight planning (waypoints, Dubins paths, altitude profiling)
- DEM (Digital Elevation Model) integration for terrain mapping
- Payload control and sensor assignment UI

**Hardware Integration**:
- Power management board with backup power ECAMS
- Smart battery board firmware
- Addon board watchdog timers (WDT) based on sensor quality
- Serial numbers in EEPROM on MHP boards
- 5V DCDC for payload power (lasers, cameras)
- Multi-sensor mapping with camera orientation, trigger timing, pulse-to-capture delay

**Simulation & Testing**:
- Gazebo integration (E2, fixed-wing, multirotor photogrammetry models)
- X-Plane plugin with joystick support
- Preflight motor test and MR attitude check

### Priority & Resource Allocation
- **Priority Level**: Low (custom field)
- **Actual Status**: ARCHIVED (per team directive, May 2026)
- **Owner**: Jack Elston (formal), but active development has migrated to SwiftCore 3.3
- **Resource Allocation**: Minimal; legacy backlog with 11-year timeline and zero due dates

### Recommendations for AI Assistant
1. **Do NOT prioritize SwiftCore 4.0 tasks** — team has moved all new software work to SwiftCore 3.3 (Daniel Prendergast, May 2026)
2. Treat the 165-task list as **legacy aspirational backlog**, not active work
3. When autopilot development priorities arise, redirect to **SwiftCore 3.3** as the active development branch
4. Reference this project only for historical context or long-term vision; do not use for sprint planning or status reporting
5. If a task is requested for SwiftCore 4.0, confirm whether it should be added to SwiftCore 3.3 instead