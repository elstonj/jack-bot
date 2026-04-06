# [001-03] S0 IRAD & Fleet Maintenance

## Overview
- **Client/Customer**: Internal BST research and development
- **Dollar Value**: No specific dollar amounts identified, but includes 2026 funding scope items
- **Timeline**: Long-term project with 2026 funding items; two near-term deadlines (Jan 2-9, 2026); heavy focus on 2026 season readiness
- **Status**: Active - extensive development backlog with 168 open tasks vs 3 completed (1.8% completion rate). Marked "Low" priority despite substantial scope.
- **Team Members**: Josh Fromm (project owner/lead), Jack Elston (avionics/firmware), Nate Straus (airframe/AD), 165 unassigned tasks
- **Risk Signals**:
  - Massive backlog with minimal completion traction
  - 165 unassigned tasks with no due dates
  - Critical issue: "PSNS not reliably entering low power mode" marked as "Required" minimum viable
  - Two imminent deadlines (Jan 2-9, 2026) with single assignees
  - Heavy dependency on unassigned work for 2026 deployment readiness

## Key Deliverables & Milestones
- **Follow up with Molicel on M65A cell samples/production** (Josh Fromm, Due: 2026-01-02) — Battery engineering for extended endurance
- **Construct BST owned S0 AD for 2025 season** (Nate Straus, Due: 2026-01-09) — Airworthiness documentation
- **2026 Funding Scope Suite** — Major system upgrades across all subsystems (sensors, power, comms, flight control, airframe)

## Task Summary
- **Total Tasks**: 168 open, 3 completed (1.8% completion rate)
- **Tasks by Assignee**:
  - Unassigned: 165 tasks (98.2%)
  - Josh Fromm: 2 tasks (Molicel follow-up, project ownership)
  - Jack Elston: 1 task (RH calculation implementation)
  - Nate Straus: 1 task (S0 airworthiness document)
- **Task Distribution by Subject** (all open tasks):
  - **Power Systems** (20+ tasks): Battery engineering, PSNS low-power mode, charging, ESC integration, BMS design, UN38.3 testing
  - **Sensors** (25+ tasks): Dual GPS, magnetometer upgrades, radar optimization, IR SST relocation, GNSS passthrough, wind calculations, NDAA compliance
  - **Flight Control** (15+ tasks): Pressure/radar altitude modes, wind thresholds, dithering, station-keep, glide path recalculation, new mission types
  - **Communications** (10+ tasks): Data buffering, low-power radio mode, NetCDF file generation, comms pauses/buffer fixes
  - **Data Handling** (10+ tasks): 10Hz met data, automated file creation, data dissemination, rsync server, compression
  - **Airframe/Mechanical** (15+ tasks): Wing tunnel testing, elevator control horn, tail boom redesign, antenna improvements, conformal coating
  - **Documentation** (5+ tasks): Training materials, construction documents, QC marks specification, inspection procedures
  - **GCS/UI** (10+ tasks): Mobile GCS lockup, tablet display improvements, heading display, weather radar overlay
  - **Avionics & Autopilot** (8+ tasks): Firmware updates over USB, mag cal logging, servo feedback issue, parameter loading consistency
  - **Tube/Deployment** (10+ tasks): Integrated power switch, parachute module, shrinkage, rotary latch modifications
  - **Other Subsystems**: HDOB improvements, checklist automation, radar alt consistency, IAS detection, sim comms
- **Fix vs Feature Split**: Roughly 40% malfunction fixes, 60% new features/improvements (mostly 2026 funding scope)

## Recent Activity
- **Recently Completed** (late 2025):
  - Conformal coating fix on antenna PCB connector (Jack Elston, completed 2026-03-18) — flagged as date anomaly; likely data entry error
  - Anduril Tasks (completed 2025-12-15)
  - ALTIUS MHTP improvements (completed 2025-12-15)
- **Approaching Deadlines**:
  - Molicel cell follow-up (2026-01-02) — assigned to Josh Fromm
  - S0 AD construction (2026-01-09) — assigned to Nate Straus

## Notes & Context

### Project Scope & Objectives
This is a comprehensive internal R&D project optimizing the S0 (subscale uncrewed aircraft system) for 2026 hurricane research operations. The "IRAD" designation indicates Internal Research & Advanced Development. Project notes emphasize "streamlining operations and ensuring compliance with standard operating procedures."

### Critical Issues (Minimum Viable = "Required")
- **PSNS not reliably entering low power mode** — Blocking power management strategy; essential for extended endurance missions

### Major 2026 Funding Initiatives
1. **Power & Endurance**: Battery cell upgrade (Amprius/Molicel M65A), ESC integration onto PSNS board, regenerative charging, improved low-power modes, UN38.3 compliance
2. **Sensors**: Dual GPS for heading, magnetometer improvements, radar rain optimization, GNSS passthrough, IR SST relocation to PSNS, Skyfora PTH integration alongside Vaisala
3. **Flight Operations**: Pressure altitude mode, radar altitude mode, wind threshold management, new mission types (position hold, asset overflight), glide path recalculation
4. **Data & Communications**: 10Hz meteorological data, automated NetCDF generation, data dissemination pipeline (rsync/compression), CARCAH status messaging via IRC
5. **Autonomy & UX**: Firmware/comms/UI improvements for intuitive scientist operation, training materials, automated checklists
6. **Airframe**: Wing tunnel testing, control horn modifications, tail boom redesign, improved waterproofing, antenna durability

### Compliance & Standards
- **NDAA Component Origin**: Requirement to check all components and replace non-compliant items
- **UN38.3 Battery Testing**: Required for international shipping
- **Documentation**: Construction documents, inspection QC marks, GCS QC process

### Operational Context — Hurricane Research
System is optimized for Center of Circulation (COC) operations with specialized requirements:
- Wind measurement during storm center penetration
- High-altitude profiles (pressure/radar altitude modes)
- Extended endurance for multi-profile missions
- Robust communications in extreme weather
- Data quality assurance for meteorological research (NHOP/AOC standards)

### Technical Challenges Identified
- **Power Management**: Charging edge cases (max charge state), sleep mode stability, quiescent current, low-voltage charging
- **Communications**: Radio interference (430 MHz with GPS/RS421), comms pauses, buffer overflow, need for low-power radio mode inside P-3
- **Sensor Integration**: Port clogs (MHP), bad dynamic port detection (5 affected), GPS velocity detection, magnetometer calibration logging
- **Flight Control**: IAS detection overshoots, wind estimation robustness, engine-out recovery, glide path optimization
- **GCS/UI**: Lockup issues (mobile GCS, gcsDaemon), slow power telemetry updates, display bugs (TAS missing, heading missing)
- **Mechanical**: Wing pivot damping, tail boom warping, antenna moisture ingress, servo feedback-induced power-on

### Integration Points
- **Deployment Tube**: Shares power domain with S0; CAN communications (firmware update path); requires coordinated power sequencing
- **P-3 Integration**: AVAPS interference avoidance, pressurization checklist, radio power management inside airframe
- **Ground Station**: Rack-mount system at BST, mobile tablet option, requires robustness for field operations
- **External Partners**: Molicel (battery cells), ERAU (wind tunnel), Skyfora (sensor integration)

### Custom Fields Usage
- **Funding Scope**: "2026" marks items in 2026 budget allocation
- **Fix or Feature**: Distinguishes malfunction fixes from enhancements
- **Minimum