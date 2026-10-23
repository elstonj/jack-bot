_Asana snapshot as of 2026-10-23: 180 open tasks, 4 completed (last 365 days)._

# [001-03] S0-AD IRAD

## Overview
- **Project**: Internal R&D for S0 Atmospheric Data (AD) uncrewed aircraft system
- **Owner**: Josh Fromm
- **Team**: BST (whole team)
- **Priority**: Low
- **Status**: Active — ongoing development and malfunction fixes. 180 open tasks with only 4 completed. Most work is unassigned and lacks due dates, indicating backlog/roadmap items rather than imminent deliverables.
- **Timeline**: Mixed — some 2025 Phase II fixes carry March 2026 deadlines (IAS detector issues), while bulk of work is scoped to 2026 or unscheduled.

## Key Deliverables & Milestones

| Milestone | Due Date | Notes |
|-----------|----------|-------|
| IAS detector malfunction fix (2025-10-26 flight regression) | 2026-03-31 | Critical — detector failed to throttle, missed wind measurements, lost UA on multiple flights |
| IAS LED/telemetry red status during takeoff | 2026-03-31 | Assigned to Ben Busby |
| Molicel M65A battery cell follow-up | 2026-01-02 | Josh Fromm to coordinate with supplier |
| S0 Packing Guide / SOP | 2026-10-30 | Beck Cotter; medium priority operational doc for vendor shipping |
| Construct BST-owned S0 AD for 2025 season | Completed 2026-04-17 | ✓ Done |

## Task Summary

**Total Tasks**: 180 open, 4 completed (2.2% completion rate)

**By Assignee** (open tasks only):
- **Unassigned**: 173 tasks (96%)
- **Maciej Stachura**: 1 (IAS fail investigation)
- **Ben Busby**: 1 (IAS LED display fix)
- **Jack Elston**: 4 (RH calculation, GCS power, LCD status, channel switching)
- **Josh Fromm**: 1 (Molicel follow-up)
- **Beck Cotter**: 1 (S0 Packing Guide)

**Task Breakdown by Subject** (custom field):
- **Power/Battery** (~30 tasks): PSNS reliability, charge cutoff, low-power mode, battery tolerance, cell upgrades (Amprius/Molicel), BMS design, UN38.3 testing
- **Flight Control** (~20 tasks): Wind thresholds, dithering, lost-comms ceiling, position hold, asset overflight, glide path recalc
- **Sensor/Avionics** (~25 tasks): GNSS, radar consistency, IAS, wind calculations, dynamic port detection, IR SST relocation, conformal coating
- **Communications** (~10 tasks): Data buffering, radio low-power mode, comms pauses, GCS lockup
- **Airframe** (~15 tasks): Wing optimization, tail boom redesign, antenna waterproofing, conformal coating, fuselage pivot CAD
- **Data Processing** (~12 tasks): NetCDF files, 10Hz met data, time sync, wind plots, automated push to servers
- **Documentation** (~8 tasks): Construction docs, QC processes, training materials, log naming convention
- **GCS/UI** (~15 tasks): LCD status display, channel switching, ETA display, mobile lockup, tablet parameter display
- **Deployment Tube** (~12 tasks): USB-C updates, shrinkage, connector redesign, firmware updates
- **Core/Board Design** (~20+ tasks): Component NDAA compliance, GNSS passthrough, IR SST integration, SD card removal, CAN firmware updates

## Recent Activity

**Most Recent Completions**:
- ✓ Construct BST-owned S0 AD for 2025 season (2026-04-17) — major seasonal milestone
- ✓ Conformal coating fix on antenna PCB MMCX connector (Jack Elston, 2026-03-18) — malfunction resolved
- ✓ Anduril Tasks & ALTIUS MHTP improvements (2025-12-15) — external/partnership items closed

**Active Issues** (with flagged dates):
- **2026-03-31 IAS detector failures**: Maciej investigating why detector failed to throttle on 2025-10-26 flights, resulting in lost wind data and loss of one UA. This is a **critical regression**. Ben Busby also addressing related LED/telemetry display issue.
- **2026-01-02 Battery supplier follow-up**: Josh Fromm pending Molicel M65A cell samples/production timeline.
- **2026-04-09 Slow comms event**: Unassigned investigation item logged.

**Pattern**: No due dates on 176/180 open tasks. This is a mature internal R&D backlog with low-priority categorization. Work is organized by subsystem (power, flight, sensors, airframe, etc.) rather than by milestone or delivery date.

## Notes & Context

### Critical/High-Risk Items
1. **IAS Detector Regression (2025 Phase II)**: Multiple failures on 2025-10-26 prevented wind measurements and resulted in loss of aircraft. Root cause investigation (detector running during freefall? 3D velocity issue?) is overdue by 2026-03-31 checkpoint.
2. **Power System Reliability**: PSNS not reliably entering low-power mode (flagged as "Required" under Minimum Viable). Multiple low-power, charging, and quiescent current draw issues across battery, BMS, and power management boards.
3. **GCS Stability**: Lockup issues on mobile GCS and gcsDaemon (GPS ran all night without responding). Rack-mount GCS at BST needs update.

### Design/Engineering Thrust
- **Battery/Power**: Migrating to new cell chemistries (Amprius/Molicel), rethinking BMS topology, UN38.3 compliance testing, charge/discharge control refinement.
- **Airframe**: Fuselage pivot CAD launch, tail boom redesign (warping issue), elevator horn/wing fit, wing tip folding, soft-close damper exploration.
- **Sensors**: Radar port clog investigation, GPS sat count/accuracy, dual-GPS integration, IR SST relocation to PSNS, Skyfora PTH sensor integration alongside Vaisala.
- **Flight Modes**: New mission types (position hold, asset overflight), wind-based station-keeping, glide path recalculation logic.
- **Data & Ops**: Automated NetCDF generation, rsync compression for live data push, IRC chat integration with CARCAH, flight metrics summary at end of mission.

### Compliance & Quality
- NDAA component origin verification and replacement.
- Conformal coating for waterproofing on AP boards.
- QC mark and loctite specifications in construction drawings.
- UN38.3 battery testing planned.

### Unassigned Work
96% of tasks (173) are unassigned. Combined with lack of due dates and "Low" priority categorization, this indicates the project is a **R&D roadmap** for internal optimization rather than a client-driven delivery schedule. Suggests phased adoption of features and fixes as engineering capacity allows.