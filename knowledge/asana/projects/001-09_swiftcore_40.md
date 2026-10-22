# [001-09] SwiftCore 4.0

## Overview
- **Client/Customer**: Internal BST development project
- **Dollar Value**: Not specified
- **Timeline**: Started January 19, 2015 — no defined end date
- **Status**: **ARCHIVED/DEPRECATED** (per Daniel Prendergast, May 15, 2026). **All new software issues should be added to SwiftCore 3.3 project instead.** Raw Asana data shows 7 open tasks (as of Nov 2023), all assigned to Maciej Stachura for VTOL refinements; zero due dates; zero completions. Project is no longer the active development branch.
- **Team Members**: 
  - Jack Elston (project owner, primary contributor)
  - Maciej Stachura (flight control systems — current active work on VTOL issues)
  - Ben Busby (ground station/tablet development)
- **Risk Signals**: 
  - **Team has officially pivoted to SwiftCore 3.3** — Daniel Prendergast directive (May 15, 2026): *"For software issues that just adds a task to the SwiftCore 3.3 project like you've always been doing. You can keep adding tasks manually if you prefer."*
  - Data staleness (Nov 2023 Asana snapshot vs. May 2026 team directives)
  - 7 open VTOL tasks unscheduled; no due dates
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
- **Total Tasks**: 7 open, 0 completed (as of Nov 2023)
- **Tasks by Assignee**:
  - **Maciej Stachura** (7 tasks, 0% complete, all VTOL-related):
    1. Set trims doesn't seem to work for VTOL
    2. Add ability to force transition (mainly in joystick mode)
    3. Wind alignment for flight terminate
    4. Wind alignment after transition back (or warning if landing is not aligned)
    5. Remove extra orbit on landing for VTOL
    6. Add pivot/motor feedback for go/no go during holdRotorsLow phase
    7. Comms version update *(notes indicate optional param additions/removals, none required)*
  - **Jack Elston**: No currently assigned tasks (owner role)
  - **Ben Busby**: No currently assigned tasks
  - **Unassigned**: 11 major milestones

- **Notable Patterns**:
  - All 7 open tasks are VTOL-specific flight control refinements assigned to Maciej Stachura
  - No due dates on any task
  - Comms version update task links to external documentation (Asana profile links); optional parameter changes (none required)
  - Zero completion history despite project spanning 11+ years (2015–2026)
  - Project priority set to **Low**

## Recent Activity
**Team Directive (May 15, 2026)** — Daniel Prendergast (authoritative):
> "Cool. For software issues that just adds a task to the SwiftCore 3.3 project like you've always been doing. You can keep adding tasks manually if you prefer."

**This supersedes SwiftCore 4.0 for all new software work.** Any new features, bug fixes, or enhancements should be created in SwiftCore 3.3, not here.

**Earlier Activity (April 9, 2026)**: Jack Elston completed three tasks:
- UAVCAN support
- Multi-vehicle ground station analysis
- GPS time/declination tracking

**Last official Asana update**: November 28, 2023 (green status; zero completions reported; 7 VTOL tasks open, no overdue milestones or tasks noted)

## Notes & Context

### Critical Status: Project Archived in Favor of SwiftCore 3.3
- **Raw Asana shows 7 open/0 completed** (Nov 2023 snapshot)
- **Team is now routing all new software work to SwiftCore 3.3**, not 4.0 (Daniel Prendergast, May 15, 2026)
- **Interpretation**: SwiftCore 4.0 is a **legacy aspirational backlog**; active development has shifted to the SwiftCore 3.3 branch. The 7 VTOL tasks represent residual work not yet migrated or closed.

### Active VTOL Work (Maciej Stachura)
Current focus is VTOL refinement and mode transitions:
- Trim and transition control improvements (manual force transition in joystick mode)
- Wind-aware landing and transition logic
- Rotor feedback during pre-takeoff phases
- Communications version parameter updates (optional, non-blocking)

### Historical Project Scope & Technical Areas
Next-generation autopilot architecture spanning 11+ years of feature development (2015–2026):

**Core Architecture**:
- RTOS migration and modular design
- Unified flight estimator for all vehicle types
- Wind estimation and adaptive parameter tuning
- Advanced sensor fusion with failover logic
- Sensor rotation matrix and orthonormal transformation improvements

**Communications & Integration**:
- MAVLink and UAVCAN protocol support
- CAN-based firmware architecture with UART/CAN ESC control
- Service discovery for WiFi communication
- Multi-UAS coordination from single ground station
- Handset/tablet hybrid joystick control

**Flight Control & Safety**:
- VTOL landing modes based on wind estimation
- Geofencing with height-aware keep-outs
- Battery termination logic (energy-aware)
- Icing detection and emergency engine shutdown
- Laser terrain following
- Preflight motor test and attitude checks

**Ground Station & Tablet (SwiftTab)**:
- Log file management and download
- OTA firmware updates
- Real-time telemetry visualization