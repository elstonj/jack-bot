_Asana snapshot as of 2026-10-30: 180 open tasks, 0 completed (last 90 days)._

# [001-03] S0-AD IRAD

## Overview
- **Client/Customer:** Internal R&D (IRAD — Independent Research and Development)
- **Owner:** Josh Fromm
- **Team:** BST (whole team)
- **Priority:** Low
- **Status:** **Active / In Development** — 180 open tasks, 0 completed. This is a long-term internal platform development project with continuous feature and malfunction fixes across hardware, firmware, and operations.
- **Timeline:** Work spans 2025–2026; specific milestones tied to 2025 Phase II and 2026 phases
- **Risk Signals:**
  - IAS (Indicated Airspeed) sensor failures on 2025-10-26 flights causing data loss and vehicle loss (high priority)
  - Multiple power management issues (PSNS not entering low-power mode reliably, charging logic bugs)
  - GCS daemon lockup (Aug 7–8, unresponsive despite solid green LED)
  - Heavy reliance on unassigned tasks (most tasks have no owner)

## Key Deliverables & Milestones

| Item | Due Date | Status | Notes |
|------|----------|--------|-------|
| IAS fail investigation (detector during freefall, 3D velocity) | 2026-03-31 | OPEN | Malfunction fix; affecting 2025 Phase II flights |
| IAS "LED" and telemetry field red during takeoff fix | 2026-03-31 | OPEN | Assigned to Ben Busby |
| Follow up with Molicel re: M65A cell samples/production | 2026-01-02 | OPEN | Assigned to Josh Fromm; battery upgrade for power subsystem |
| S0 Packing Guide / SOP | 2026-10-30 | OPEN | Assigned to Beck Cotter; operational/vendor documentation |
| Tunnel testing to characterize wing effect | 2026 | OPEN | Unassigned; 2026 funding scope |
| 2026 phase II hardware/firmware roadmap | 2026 | OPEN | ~100+ unassigned feature/improvement tasks spanning airframe, sensors, power, comms, flight control, data handling |

## Task Summary

### Counts
- **Total:** 180 open, 0 completed
- **0% project completion** — this is a backlog-style project

### Breakdown by Assignee
| Assignee | Task Count | Notes |
|----------|-----------|-------|
| Unassigned | ~165 | Majority of tasks; spanning all subsystems |
| Maciej Stachura | 1 | IAS sensor malfunction investigation |
| Ben Busby | 1 | IAS telemetry display fix |
| Jack Elston | 5 | Power, GCS UI/LCD, channel switching logic |
| Josh Fromm | 1 | Molicel battery supplier follow-up |
| Beck Cotter | 1 | S0 packing guide / SOP |

### Notable Patterns
- **Heavy unassignment:** ~92% of tasks lack an owner, indicating planning/backlog stage rather than active sprint execution
- **Subject-driven organization:** Tasks tagged by subsystem (power, comms, flight control, sensors, airframe, avionics, etc.)
- **2025 vs. 2026 split:** A few near-term malfunction fixes (2025 Phase II, due early 2026); bulk are 2026 feature roadmap items
- **Mix of malfunction fixes and new features:** Tagged with `Fix or Feature` custom field; malfunction fixes cluster around power, IAS, GCS, and sensor reliability
- **Custom fields in use:** Funding Scope, Subject, Fix or Feature, Minimum Viable, Priority, Task Type, Risk Level — suggests active project management but incomplete task assignment

## Recent Activity

### Recent Issues (Inferred from Task Notes)
- **2025-10-26 flights:** IAS detector failed to throttle; missed wind measurements, lost aircraft. Failure is recurring.
- **Aug 7–8 GCS daemon:** GPS ran all night, morning status showed solid green LED but no response — likely a lockup.
- **Charge/power edge cases:** Aircraft powered on at max charge when plugging in charger; PSNS not reliably entering low-power mode (marked as "Minimum Viable: Required").
- **Servo feedback issue:** Servos feed back voltage during manual movement, applies power to autopilot, risks unwanted firing.

### Approaching/Recent Milestones
- **2026-01-02:** Molicel cell sample follow-up (Josh Fromm) — coming up soon
- **2026-03-31:** IAS fixes (both tasks) — two critical sensor/display fixes due Q1 2026
- **2026-10-30:** S0 packing guide (Beck Cotter)

## Notes & Context

### Project Scope
This is a **continuous R&D and product hardening effort** for the S0 atmospheric sensing UAS. The project consolidates:
- **Hardware design improvements** (airframe, power systems, sensors, deployment tube, boards)
- **Firmware/software features** (flight control, GCS, data handling, comms, autonomy)
- **Operational procedures** (packing guides, QC processes, checklists)
- **Integration/testing** (wind tunnel work with ERAU, sensor calibration, validation)

### Key Technical Concerns
1. **Power subsystem is fragile:** Multiple low-priority charging bugs, PSNS reliability, BMS decisions pending. Battery upgrade (Molicel) and ESC integration are high on the roadmap but unassigned.
2. **IAS sensor is a critical blocker:** Recurring failures on recent flights; two fixes in flight (both due 2026-03-31) but root cause investigation ongoing.
3. **GCS stability issues:** Lockups, comms pauses, and mobile platform crashes need resolution before scaling operations.
4. **Data/comms infrastructure gaps:** Missing buffering, re-transmission, live rsync, NetCDF auto-generation, status messaging to CARCAH.
5. **Sensor reliability:** Multiple malfunction fixes needed (GPS accuracy, dynamic ports, radar consistency, IR sensor ghost readings, pressure sensor location).

### Operational Context (from task notes)
- Aircraft operates in **high-wind/hurricane environments** (references to wind thresholds, lost comms procedures, glide-slope recalculation during storms).
- **Deployment via P3 aircraft** (references to P3 depressurization, integration with AVAPS instruments, launch/recovery procedures).
- **Multi-mission capability emerging:** Position hold, asset overfly, station-keeping, inflow/RMW profiles.
- **NHOP/AOC compliance expected:** References to NHOP 6.2.3.8 status messaging, HDOBS data QC, Kathryn email re: time offset.

### Organizational Notes
- **No completed tasks:** Suggests this is a rolling backlog that gets groomed but not formally closed out in Asana. Real progress may be tracked in Git commits, weekly standups, or external systems.
- **Wide team involvement:** Sensor engineers (Maciej), flight control (Jack), operations (Beck), procurement/partnerships (Josh), displays/UI (Ben) all represented, but most subsystems lack clear owners.
- **Funding tracked:** 2025 Phase II (near-term malfunction fixes) and 2026 (feature roadmap) split suggests staged investment.

---

**Overall Assessment:** This is a **mature but under-resourced R&D project**. Core platform is flying and generating data, but reliability issues (IAS, GCS, power) and feature gaps (data handling, comms) are holding back operational scaling. Assignment of owners and sprint planning needed to move items from backlog to completion.