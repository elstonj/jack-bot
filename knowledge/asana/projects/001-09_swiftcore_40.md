# [001-09] SwiftCore 4.0

## Overview
- **Client/Customer**: Internal BST development project
- **Dollar Value**: Not specified
- **Timeline**: Started January 19, 2015 — no defined end date
- **Status**: **ARCHIVED/DEPRECATED** (per Daniel Prendergast, May 15, 2026). **All new software issues should be added to SwiftCore 3.3 project instead.** Raw Asana data shows 51 open tasks (as of Nov 2023), zero completions, zero due dates. Project is no longer the active development branch.
- **Team Members**: 
  - Jack Elston (project owner, primary contributor — 33 tasks assigned)
  - Maciej Stachura (flight control systems, VTOL refinements — 17 tasks assigned)
  - Ben Busby (ground station/tablet development — 1 task assigned)
- **Risk Signals**: 
  - **Team has officially pivoted to SwiftCore 3.3** — Daniel Prendergast directive (May 15, 2026): *"For software issues that just adds a task to the SwiftCore 3.3 project like you've always been doing. You can keep adding tasks manually if you prefer."*
  - Data staleness (Nov 2023 Asana snapshot vs. May 2026 team directives)
  - 51 open tasks, 0 completed; no due dates; no priority milestones
  - No active status updates since November 28, 2023
  - **Priority**: Low

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
- **Total Tasks**: 51 open, 0 completed (as of Nov 2023)
- **Tasks by Assignee**:
  - **Jack Elston** (33 tasks, 0% complete):
    - Logging & telemetry issues (roll_cmd logging error, telemetry height scale mismatch, hot shoe packet logging, system time to packets)
    - Flight safety & failsafe behavior (ERROR_NO_BATTERY event, lost GPS descent abort, emergency descent logic, motor power loss critical errors)
    - Calibration & control surface limits (tablet/AP calibration range limits, surface deflection limits, initial XML load deflections)
    - Payload & deployment systems (door opens in preflight, deployment tube logic, payload comms loss behavior)
    - Flight plan & goto logic (ACK placement in flight plan module, goto outside flying mode, flight plan altitude toggle)
    - Joystick & handset control (lost comms joystick behavior, throttle after flare, GCS disconnection 9/28/26, joystick mode investigation)
    - Sensor & estimator initialization (sensor startup times/values, sensor rotation matrix, constant controller rate for quad)
    - Code cleanup (rate limiters, terminate functions removal)
    - Documentation (SwiftTab payload window control description)
    - Hardware integration (dual pitot setup, handset joystick)
    - Parameter & config management (save param files before comms)
    - Trigger validation (timer-based triggers)
    - Fault analysis (flight terminate conditions)

  - **Maciej Stachura** (17 tasks, 0% complete):
    - VTOL-specific flight control refinements:
      - Set trims for VTOL, force transition (joystick mode)
      - Wind alignment for flight terminate and transition
      - Remove extra orbit on landing, rotor feedback during holdRotorsLow phase
      - Joystick transition land and lost GPS transition for VTOL
      - Wind alignment on VTOL landing
    - Multirotor failsafe & diagnostics:
      - GPS/pressure outage handling, open loop control for multirotor
      - Transition failure timeout, clog detection during transition
      - MHP clog detector (port comparison)
      - Engine out throttle-to-power mapping, clog detector power-based switching
    - Flight control tuning:
      - TECS small angle assumption inconsistency (gamma_c vs. gamma_a)
      - Gyro feedback manual mode
      - ERROR_NO_BATT timer (isfinite() check failure)
      - TECSalt_Land removal
    - Communications:
      - Comms version update (optional parameter additions/removals, none required)

  - **Ben Busby** (1 task, 0% complete):
    - Cannot uncheck "landing plan altitude set" after checking it (SwiftTab UI bug)

  - **Unassigned**: 11 major milestones (no due dates)

- **Notable Patterns**:
  - Jack Elston carries 65% of open work (33/51 tasks) — broad scope spanning logging, safety, payload, control, and hardware integration
  - Maciej Stachura carries 33% (17/51) — concentrated on VTOL and multirotor flight control refinements
  - Ben Busby has 1 low-priority UI bug
  - Zero due dates on any task; no priority differentiation
  - Zero completion history despite project spanning 11+ years (2015–2026)
  - Project priority set to **Low** — reflects archived status

## Recent Activity
**Team Directive (May 15, 2026)** — Daniel Prendergast (authoritative):
> "Cool. For software issues that just adds a task to the SwiftCore 3.3 project like you've always been doing. You can keep adding tasks manually if you prefer."

**This supersedes SwiftCore 4.0 for all new software work.** Any new features, bug fixes, or enhancements should be created in SwiftCore 3.3, not here.

**Earlier Activity (April 9, 2026)**: Jack Elston completed three tasks:
- UAVCAN support
- Multi-vehicle ground station analysis
- GPS time/declination tracking

**Last official Asana update**: November 28, 2023 (green status; zero completions reported; 51 open tasks, no overdue milestones or tasks noted)

## Notes & Context

### Critical Status: Project Archived in Favor of SwiftCore 3.3
- **Raw Asana shows 51 open / 0 completed** (Nov 2023 snapshot)
- **Team is now routing all new software work to SwiftCore 3.3**, not 4.0 (Daniel Prendergast, May 15, 2026)
- **Interpretation**: SwiftCore 4.0 is a **legacy aspirational backlog**; active development has shifted to the SwiftCore 3.3 branch. The 51 open tasks represent residual work not yet migrated, closed, or prioritized.

### Task Scope Overview
SwiftCore 4.0 represents a next-generation autopilot architecture with ambitious feature scope spanning 11+ years (2015–2026):

**Flight Control & Estimation** (Maciej Stachura lead):
- VTOL/tailsitter mode refinements (trims, transition logic, wind-aware landing, rotor feedback)
- Multirotor failsafe (GPS/pressure outage handling, open-loop control, clog detection)
- Engine-out throttle-to-power mapping
- TECS tuning (small angle inconsistencies)
- Sensor fusion & initialization (gyro feedback, sensor startup validation)

**Telemetry, Logging & Communications** (Jack Elston lead):
- Telemetry packet architecture (height scale mismatch in TELEMETRY_POSITION, system time injection)
- Logging infrastructure (roll_cmd takeoff error,