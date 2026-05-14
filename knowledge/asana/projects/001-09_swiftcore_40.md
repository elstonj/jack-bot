# [001-09] SwiftCore 4.0

## Overview
- **Client/Customer**: Internal BST development project
- **Dollar Value**: Not specified
- **Timeline**: Started January 19, 2015 - ongoing development project with no defined end date
- **Status**: Active but low priority. **DISCREPANCY ALERT**: Asana shows 165 open tasks with 0 completions as of the raw data snapshot (appears to be from Nov 2023 or earlier), conflicting with earlier knowledge file reporting 0 open/3 completed as of April 9, 2026. The raw data is stale. Current actual status unknown pending clarification.
- **Team Members**: Jack Elston (project owner/primary contributor), Maciej Stachura (flight control systems), Ben Busby (ground station/tablet development)
- **Risk Signals**: Large unmanaged backlog (165 open tasks); no due dates on any tasks; last official status update November 28, 2023 (stale); data consistency issues suggest project tracking may have diverged from actual development state

## Key Deliverables & Milestones
Major architectural improvements (all unassigned, no due dates):
- **Conversion to RTOS** - Real-time operating system migration
- **Better payload system** - Multiple camera support and flight plan loading
- **Official VTOL/tailsitter support** - Vertical takeoff and landing capabilities
- **SBC Autopilot companion** - Single board computer integration
- **New GCS** - Ground control station redesign
- **MAVLink support** - Industry standard protocol integration
- **UAVCAN support** - CAN bus communication protocol *(marked complete 2026-04-09 in earlier data)*
- **Multi-vehicle support** - Control multiple aircraft simultaneously *(partial completion noted 2026-04-09)*
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
**Raw Asana data is stale** (appears to be Nov 2023 snapshot). Earlier knowledge file indicates:
- Three tasks completed on April 9, 2026 (UAVCAN support, multi-vehicle ground station analysis, GPS time/declination tracking) — all assigned to Jack Elston
- Last official status update: November 28, 2023 ([green] status, zero completions reported at that time)

**Team feedback** (May 2026) from Daniel Prendergast references post-flight process forms and "Fleet Maintenance" project but does not directly address SwiftCore 4.0 status.

## Notes & Context

### Data Consistency Issues
- **Critical Discrepancy**: Raw Asana data shows 165 open/0 completed; earlier knowledge file (apparently from May 2026) shows 0 open/3 completed. This suggests either:
  - Asana data export is stale and does not reflect actual project state
  - Project was archived or major backlog purge occurred between Nov 2023 and Apr 2026
  - Duplicate projects or data sync failure
  - **Recommendation**: Request current Asana project export or clarify with Jack Elston on actual backlog status

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
- **Actual Status**: Unclear. Raw Asana snapshot is stale. If April 2026 data is current, project has shifted from long-term backlog to active completion phase with focus on multi-vehicle systems and communications protocols. If raw Asana data is current, project is in large backlog state with minimal execution.
- **Owner Activity**: Jack Elston remains primary active contributor; April 2026 completions all assigned to him.

### Recommendations for AI Assistant
- **Verify current status** before making prioritization decisions—this project has conflicting data points (Nov 2023 stale snapshot vs. Apr 2026 active phase)
- Treat 165-task list as aspirational backlog; actual in-flight work likely much smaller
- Jack Elston is authoritative source for current roadmap priorities
- Assume low resource allocation given "Low" priority flag and 11-year development timeline
- Multi-vehicle support appears to be active focus area (April 2026 completions)