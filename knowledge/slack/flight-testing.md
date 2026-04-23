# #flight-testing

## Overview

The #flight-testing channel serves as Black Swift Technologies' primary hub for coordinating flight test operations, troubleshooting aircraft and payload issues, and tracking firmware/software development across their fleet of fixed-wing (S-series), multirotor (E2, Flamewheel), and VTOL (S0, S1-VTOL, S3) platforms.

**Key Participants:** Maciej (lead flight testing/analysis), Jack Elston (firmware development), Joshua Fromm (QA/component sourcing), Ben Busby (tablet/GCS software), Nate (videography/pilot), Alex Lomis (field operations/media), Sam Hild (Remote ID integration/test pilot), Dan Prendergast (autopilot/control systems), Danny Troke (data management), Ethan Domagala (pilot), Beck Cotter (operations support)

**Activity Level:** Extremely high — 5,600+ messages across June 2020 through April 2026. Daily operations with multiple aircraft flights, rapid issue turnaround, continuous firmware iterations, and intensive VTOL transition testing.

---

## Key Decisions

### Aircraft Development & Configuration
- **October 2020:** SwiftTab APK versioning standardized — staging for internal testing, release for customer delivery
- **2021:** GNSS updates deployed fleet-wide (FW-1, S1-5, S2-9, E2-7, E2-6) following board firmware issues
- **May 2021:** Decided to integrate BluFlux payload testing with full mission prep (4-battery requirement)
- **March 2022:** Servo voltage drop issue on S20003 deemed acceptable risk with precautions; incorporated fix into newer S2 VTOL design
- **May 2022:** Altum camera GPS interference acknowledged as non-critical (post-processing geotag workaround acceptable); future VTOL design will separate payloads from GNSS
- **September 2022:** Heated pitot firmware compatibility issue identified; decision to update S20009 to latest master code
- **March 2024:** COA applications submitted for two 2500' airspace blocks (RC field and Caribou ranch); actual line-of-sight limits altitude to ~1500-2000'
- **April 2026:** S3 conversion to PWM-only control approved to address motor control issues; S1-VTOL 2030 hardware concurrent testing approved; S10020 firmware update baseline set (build hash: bf20b0b7)
- **April 20-23, 2026:** S10022 DroneCAN firmware deployment approved and completed; aircraft returned to flight status with nose tape requirement reinforced for airspeed sensor protection

### Firmware & Code Management
- **October 2020:** Angle-to-rate loop gains critical safety parameter — develop (8,8,3) vs. master (4,4,1.5) discrepancy required close monitoring
- **February 2021:** Tablet app parameter validation feature added as non-intrusive compromise after initial disagreement on comparison button inclusion
- **February 2021:** S1-5 reverted from develop to master code due to IAS calculation stall/launch problems
- **March 2024:** Feature branches (feature/ias_clog_new_detector, feature/dronetag) approved for testing; feature/s3_mass_model branch merged into develop with identified firmware bugs fixed (3/24)
- **February 2025:** S0-VTOL takeoff default set to 50m for testing; S1-22 tail offset mechanically adjusted to 4.5-5 degrees rather than electronic trim
- **April 2026:** S10022 DroneCAN firmware deployment; S10020 updated to latest code with yaw gyro diagnostics required before further flights; S3 firmware issues identified requiring feature branch merge for actuator board fixes
- **April 20, 2026:** S10022 motor control issue resolved via canard firmware modification to free memory allocation even when system doesn't flag necessity
- **April 21, 2026:** RTK bug identified in S10022 requiring return to facility; GNSS board orientation critical (perfect square bolt pattern requires correct alignment matching previous flights)

### Safety & Flight Operations
- **February 2021:** RC field hours moved to 9:30 AM start (from 10 AM)
- **July 2024:** For non-production test aircraft, mandated short manual hover on first flight of day to catch critical issues quickly
- **March 2025:** Fleet maintenance system reinstated using Asana project tracking per-aircraft repairs/inspections
- **April 2026:** Dead IMU (Z-axis gyro) on S10021 identified as critical grounding condition; aircraft should not fly without functional yaw gyro reporting; lost motor events on S1-VTOL during transition require investigation before subsequent flights
- **April 20, 2026:** S1-22 pre-flight checklist formalized: (1) Manual hover with GPS PDOP <3 verification; (2) Joystick hover with 90° yaw confirmation and full stick forward test; (3) Motor failure contingency protocol — pilot must switch to manual throttle-down immediately if single motor loss detected in forward flight
- **April 22, 2026:** S1-22 in-flight autopilot reset event occurred during takeoff orbit (5+ min prior to motor failure); AP reset disables engines requiring manual re-enable via tablet or "force flying" button; motor failure mitigation testing resumed with dual logging (flight log + GCS log backup)
- **April 20, 2026:** Nose tape requirement enforced for S1-VTOL airspeed sensor protection

### Payload Integration & Testing
- **July 2020:** S20003 30km comms range test: 20km 900MHz achieved (below 30km requirement) — cable quality issues identified, Pasternack cable needed
- **2021:** USGS payload specs documented in shared spreadsheet; multiple payload configurations (SMM, trace gas, photogrammetry, CO2, methane) standardized
- **May 2022:** CO2 payload underslinging considered as fix for moment-of-inertia issues; wind cap 15-20 mph with payload confirmed
- **August 2022:** LDCR firmware updates and AP telemetry logging verification made mandatory pre-flight
- **September 2024:** MicaSense Altum camera image failures escalated — image files shared for manufacturer investigation
- **April 21, 2026:** INSTAAR (Institute for Arctic and Alpine Research, University of Colorado) guest operations conducted; payload data successfully collected despite partial flight log loss

### Data Logging & Management
- **April 21, 2026:** Critical protocol established — do NOT rename files on aircraft SD cards post-flight; renaming creates high probability of overwriting existing logs; all file management must occur post-download on ground station; GCS log serves as lower-rate telemetry backup when flight logs are corrupted/incomplete
- **April 22, 2026:** Tablet logging validated as error detection tool; SYSTEM_POWER_ON events indicate in-flight resets; GCS logs preserve lower-rate flight telemetry when aircraft logs truncate

---

## Projects & Initiatives

### Active Aircraft Platforms

**S-Series Fixed Wing:**
- S1 variants (S10005, S10011, S10018, S10019, S10020, S10022, S10023): Primary fixed-wing platform with continuous firmware testing
  - **S10020 (April 2026):** 5 flights completed; degraded GPS error (yellow) detected during landing orbit despite RTK availability; otherwise flew well; firmware updated to bf20b0b7
  - **S10021 (April 2026):** XTEND yaw sensitivity issue — yaw gyro (Z-axis) not reporting; mag alignment slow (20+ seconds); diagnostics show mag reading 0.001 gain correct but Z gyro stuck at 0; aircraft grounded pending hardware repair/replacement
  - **S10022 (April 20-23, 2026):** 
    - DroneCAN firmware deployment completed (4/20)
    - Motor control memory allocation issue resolved via canard firmware modification (4/20)
    - RTK bug identified requiring return to base (4/21)
    - Repaired and reassembled with reinforced nose tape; weight 3291g with marginal glue addition; ready to return to flight testing (4/22-4/23)
    - Comms code verified as v3.22; potential XT90 battery connector issue flagged for inspection
    - In