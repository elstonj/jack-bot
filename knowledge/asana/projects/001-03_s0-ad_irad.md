_Asana snapshot as of 2026-10-31: 180 open tasks, 0 completed (last 90 days)._

# [001-03] S0-AD IRAD

## Overview

- **Client/Customer:** Internal R&D (IRAD — Internal Research and Development)
- **Owner:** Josh Fromm
- **Team:** BST (Whole Team)
- **Priority:** Low
- **Dollar Value:** Not specified in custom fields
- **Status:** **ACTIVE — heavily backlogged.** 180 open tasks, 0 completed. This is a sustained internal development roadmap, not a time-bound project.
- **Timeline:** Spans 2025–2026; a few near-term items due in 2026 Q1 (see Recent Activity below)

---

## Key Deliverables & Milestones

| Deliverable | Assignee | Due Date | Notes |
|---|---|---|---|
| IAS fail investigation & fix | Maciej Stachura, Ben Busby | 2026-03-31 | Detector throttle malfunction on 2025-10-26 flights; missed wind measurements, lost UA. "LED" and telemetry field shouldn't be red during takeoff. |
| Molicel M65A cell follow-up | Josh Fromm | 2026-01-02 | Battery cell samples/production inquiry. |
| S0 Packing Guide / SOP | Beck Cotter | 2026-10-30 | Standard Operating Procedure for packing; guidance for vendor returns. |

**2026 Phase II & 2026 Projects** (no specific dates):
- Tunnel testing to characterize wing effect
- Data buffering and re-transmission (comms)
- NetCDF file auto-creation on P3 ground station
- 10Hz meteorological data
- Pressure altitude & radar altitude flight modes
- Extended endurance (battery engineering)
- Sensor improvements (radar rain optimization, dual GPS, Skyfora PTH integration)
- Power system overhaul (low-power mode, battery tolerance, motor/prop/ESC updates, Amprius/Molicel cells)
- Flight controller enhancements (new mission types, dithering, station-keep, asset overfly)
- GCS & UI improvements
- Data dissemination & automated reporting
- Airframe & mechanical refinements

---

## Task Summary

- **Total Open Tasks:** 180
- **Completed Tasks:** 0
- **Completion Rate:** 0%

### By Assignee

| Assignee | Count | Status |
|---|---|---|
| Unassigned | ~170 | Open (vast majority) |
| Maciej Stachura | 1 | IAS fail investigation (due 2026-03-31) |
| Ben Busby | 1 | IAS LED telemetry fix (due 2026-03-31) |
| Jack Elston | 5 | RH calculation, GCS power, LCD, channel switch, power logic updates |
| Josh Fromm | 2 | Molicel follow-up (due 2026-01-02); NDAA compliance check |
| Beck Cotter | 1 | S0 Packing Guide (due 2026-10-30) |

### Task Distribution by Subject

- **Power (PSNS, battery):** ~20 tasks — low-power mode, charge/discharge logic, BMS, cell upgrades, quiescent current
- **Flight controller:** ~15 tasks — new mission types, wind estimation, engine-out handling, glide path logic
- **Sensors:** ~15 tasks — GPS, radar, wind calculations, port clogs, dynamic port detection
- **Comms:** ~8 tasks — data buffering, radio power modes, buffer fixes, protocol integration
- **Data pipeline:** ~10 tasks — NetCDF, rsync, automated dissemination, NHOP/AOC compliance, wind plots
- **GCS & UI:** ~12 tasks — lockup issues, tablet display (battery %, power readings, distance), heading/altitude controls
- **Airframe & mechanical:** ~12 tasks — elevator control horn, wing tip folding, tail boom warping, waterproofing, antenna mount
- **Deployment tube & boards:** ~15 tasks — power switches, shrinkage, connector updates, firmware updates over USB/CAN
- **Core boards & avionics:** ~8 tasks — RM3100 removal, integrated GNSS, SD card removal, mag cal saving
- **Docs & training:** ~5 tasks — construction documents, QC markers, loctite specs, training materials
- **IAS (air speed sensor):** ~3 tasks — detection malfunction, LED/telemetry display
- **Other (sim, checklist, test):** ~10 tasks — simulator comms, checklist automation, ERAU wind tunnel collaboration

### Notable Patterns

- **Extreme backlog:** 180 open tasks with no closure suggests this is a long-term R&D roadmap rather than a sprint-based project.
- **Heavy unassignment:** ~170 of 180 tasks are unassigned, indicating planning-stage work or awaiting resource allocation.
- **2025 Phase II urgent items:** IAS malfunction on recent flights (2025-10-26) is actively impacting operations; two related tasks are assigned and due 2026-03-31.
- **2026 feature-heavy:** Bulk of work is new feature development (airframe, power, flight control, data pipeline) targeting 2026.
- **Power system is a bottleneck:** Battery tolerance, low-power mode, charge logic, cell selection, and BMS are recurring themes across many tasks.

---

## Recent Activity

### Urgent (2025 Phase II)
- **IAS detector failures on 2025-10-26 flights:** Multiple incidents of sensor throttle malfunction causing missed wind measurements and loss of aircraft. Tasks assigned to Maciej Stachura (investigation) and Ben Busby (LED/telemetry display fix), due 2026-03-31.
  - *Notes from task:* "IAS fail happening increasingly frequently on 2025-10-26 flights until missed a lot of wind measurements, lost UA."

### Near-term (Q1 2026)
- **Molicel M65A cell follow-up:** Josh Fromm to contact Molicel re: M65A cell samples/production. Due 2026-01-02.
- **S0 Packing Guide (SOP):** Beck Cotter, due 2026-10-30. Needed for internal operations and vendor returns.

### Ongoing / Backlog
- No tasks have moved to completion; no closed-out work reported.
- All remaining 180 tasks remain in planning/development phase.

---

## Notes & Context

### Project Type & Scope
This is an **internal IRAD (Internal Research and Development)** project focused on optimizing the S0 uncrewed aircraft system across all subsystems:
- **Airframe & mechanics:** Folding wings, tail boom, control surfaces, waterproofing
- **Avionics & flight control:** Autopilot, wind estimation, new mission types (position hold, asset overfly)
- **Power:** Battery technology upgrade (Amprius/Molicel cells), low-power modes, charging logic, BMS
- **Sensors:** GPS, radar altitude, wind calculation, IR, magnetometer, pressure sensors
- **Comms:** Radio buffering, data dissemination, GCS heartbeat
- **Data pipeline:** Live rsync, automated NetCDF generation, NHOP/AOC compliance, flight metrics reporting
- **Deployment tube:** USB-C firmware updates, power switches, shrinkage tolerance
- **Operations:** Packing guides, QC processes, training materials

### Critical Issue: IAS (Airspeed Sensor) Malfunction
Recent flights in October 2025 have revealed a **recurring IAS detector failure** that causes:
- Loss of wind measurement capability
- Loss of aircraft (apparent total loss on at least one flight)
- Increasing frequency of incidents

This is flagged as a **Malfunction Fix** (not a feature) and is the only work with near-term assigned owners and due dates. Fix is targeted for 2026-03-31.

### Funding & Phase
- **2025 Phase II:** Covers IAS fix and recent ops issues
- **2026:** Bulk of new features, improvements, and upgrades
- **Type of Project:** At least one task is marked "Funded Grant" (construction documents for fuselage pivot)

### Power System Complexity
Battery/power management is a major focus area with ~20 open tasks covering:
- Low-power mode (quiescent current, sleep mode, charge initialization)
- Battery tolerance (length, cell selection)
- Charge/discharge logic (max charge behavior, cutoff current, low-voltage charging)
- BMS (dedicated PCB, UN38.3 testing, fusing)
- Cell upgrades (Amprius vs. Molicel vs. current)
- Integration (ESC on PSNS board, regenerative charging)

This suggests ongoing challenges with endurance, reliability, or compliance.

### Data Dissemination & NHOP Compliance
Multiple tasks reference NHOP (National Hurricane Operations Platform), AOC (Aerial Observation Center), and CARCAH, suggesting this system operates within hurricane operations. Tasks include:
- Automated IRC/in-app status messages
- NetCDF file generation & compression
- Time synchronization with HDOBS data
- QC flagging per NHOP 6.2.3.8

### No External Corrections Provided
No `TEAM CORRECTIONS & FEEDBACK` block was included in the source data, so all information reflects the current Asana task state.

---

## Risk Signals

1. **IAS Detector Failures (Active):** Causing loss of aircraft and wind data. Assigned fix due 2026-03-31 but already impacting 2025 operations.
2. **Extreme Backlog (180 open, 0 closed):** Suggests either this is a planning artifact, resource constraints, or the project has not yet entered execution phase.
3. **Heavy Unassignment (170/180 tasks):** Indicates work is not yet allocated; unclear when execution will begin.
4. **Power System Instability:** Multiple low-priority issues (low-power mode, charge logic, BMS) suggest the power subsystem is not yet mature.
5. **2026-03-31 Deadline (IAS):** Very soon relative to the depth of investigation required; may slip.