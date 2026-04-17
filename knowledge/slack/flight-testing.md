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

### Firmware & Code Management
- **October 2020:** Angle-to-rate loop gains critical safety parameter — develop (8,8,3) vs. master (4,4,1.5) discrepancy required close monitoring
- **February 2021:** Tablet app parameter validation feature added as non-intrusive compromise after initial disagreement on comparison button inclusion
- **February 2021:** S1-5 reverted from develop to master code due to IAS calculation stall/launch problems
- **March 2024:** Feature branches (feature/ias_clog_new_detector, feature/dronetag) approved for testing; feature/s3_mass_model branch merged into develop with identified firmware bugs fixed (3/24)
- **February 2025:** S0-VTOL takeoff default set to 50m for testing; S1-22 tail offset mechanically adjusted to 4.5-5 degrees rather than electronic trim
- **April 2026:** S10022 DroneCAN firmware deployment; S10020 updated to latest code with yaw gyro diagnostics required before further flights; S3 firmware issues identified requiring feature branch merge for actuator board fixes

### Safety & Flight Operations
- **February 2021:** RC field hours moved to 9:30 AM start (from 10 AM)
- **July 2024:** For non-production test aircraft, mandated short manual hover on first flight of day to catch critical issues quickly
- **March 2025:** Fleet maintenance system reinstated using Asana project tracking per-aircraft repairs/inspections
- **April 2026:** Dead IMU (Z-axis gyro) on S10021 identified as critical grounding condition; aircraft should not fly without functional yaw gyro reporting; lost motor events on S1-VTOL during transition require investigation before subsequent flights

### Payload Integration & Testing
- **July 2020:** S20003 30km comms range test: 20km 900MHz achieved (below 30km requirement) — cable quality issues identified, Pasternack cable needed
- **2021:** USGS payload specs documented in shared spreadsheet; multiple payload configurations (SMM, trace gas, photogrammetry, CO2, methane) standardized
- **May 2022:** CO2 payload underslinging considered as fix for moment-of-inertia issues; wind cap 15-20 mph with payload confirmed
- **August 2022:** LDCR firmware updates and AP telemetry logging verification made mandatory pre-flight
- **September 2024:** MicaSense Altum camera image failures escalated — image files shared for manufacturer investigation

---

## Projects & Initiatives

### Active Aircraft Platforms

**S-Series Fixed Wing:**
- S1 variants (S10005, S10011, S10018, S10019, S10020, S10022): Primary fixed-wing platform with continuous firmware testing
  - **S10020 (April 2026):** 5 flights completed; degraded GPS error (yellow) detected during landing orbit despite RTK availability; otherwise flew well; firmware updated to bf20b0b7
  - **S10021 (April 2026):** XTEND yaw sensitivity issue — yaw gyro (Z-axis) not reporting; mag alignment slow (20+ seconds); diagnostics show mag reading 0.001 gain correct but Z gyro stuck at 0; aircraft grounded pending hardware repair/replacement
  - **S10022 (April 2026):** DroneCAN firmware deployment in progress
  - **S10023 (April 2026):** Test flight ongoing (4/14)
- S2 variants (S20003, S20008, S20009, S20013, S20015): Larger fixed-wing with soil moisture, trace gas, photogrammetry payloads
- S0 (cardboard test platform): High-start bungee launcher testing, avionics integration testbed
- **Status (April 2026):** Multiple aircraft active in testing rotation; focus on firmware validation and diagnostics before VTOL transition testing

**E-Series Multirotors (E2):**
- E20004–E20014: Quad platforms with various gimbal and payload configurations
- **Status (April 2026):** E20014 QC restarted after 2022 hiatus, firmware/params updated to 2050 AP specs; multiple units undergoing Altum camera integration testing

**Flamewheel (FW) Multirotors:**
- FW0001, FW0002: Smaller multirotor test platforms
- **Status (April 2026):** Updated with new comms/logging code; kill switch validation and joystick hover stability testing planned

**S1-VTOL Development (S1-20):**
- **April 10-13, 2026 Test Campaign - Critical Motor Failure Issues Identified:**
  - Battery 1 (6 flights): Multiple transition anomalies — joystick control warning in full auto, pause before transition, wobbly landing transitions (×2), right pivot pause, vibration on transition; Flight 6 clean
  - Battery 2 (8 flights): Right pivot brief dropout on transition (Flight 8), bounced landing with left roll (Flight 11); **Flight 14: All motors lost at end of hover test** — pilot Ethan able to partially recover and land on belly; simultaneous motor shutdown on all axes; logs show left motor cut out and re-engaged during Flight 3 nose dive; current analysis indicates hard motor out event (3A from ~65A at same throttle levels)
  - **Root Cause Investigation Ongoing:** Maciej analyzing logs; motor out replicated on subsequent hover test; decision to proceed with S3 hover testing regardless while investigating
  - **Decision:** Do NOT proceed with S1-VTOL transition testing until motor failure root cause identified; continue S3 mass model hover testing (4/14-4/15)

**S0-VTOL & S3 Development:**
- S0-VTOL (S01006): Landing yaw issues under testing; yaw damping gains being tuned
- S3-