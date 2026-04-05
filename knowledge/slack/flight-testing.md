# #flight-testing

## Overview

The #flight-testing channel serves as Black Swift Technologies' primary hub for coordinating flight test operations, troubleshooting aircraft and payload issues, and tracking firmware/software development across their fleet of fixed-wing (S-series), multirotor (E2, Flamewheel), and VTOL (S0, S1-VTOL, S3) platforms.

**Key Participants:** Maciej (lead flight testing/analysis), Jack Elston (firmware development), Joshua Fromm (QA/component sourcing), Ben Busby (tablet/GCS software), Nate (videography/pilot), Alex Lomis (field operations/media), Sam Hild (Remote ID integration), Dan Prendergast (autopilot/control systems), Danny Troke (data management), Ethan Domagala (pilot)

**Activity Level:** Extremely high — 5,587 messages across June 2020 through April 2025. Daily operations with multiple aircraft flights, rapid issue turnaround, and continuous firmware iterations.

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

### Firmware & Code Management
- **October 2020:** Angle-to-rate loop gains critical safety parameter — develop (8,8,3) vs. master (4,4,1.5) discrepancy required close monitoring
- **February 2021:** Tablet app parameter validation feature added as non-intrusive compromise after initial disagreement on comparison button inclusion
- **February 2021:** S1-5 reverted from develop to master code due to IAS calculation stall/launch problems
- **March 2024:** Feature branches (feature/ias_clog_new_detector, feature/dronetag) approved for testing; feature/s3_mass_model branch merged into develop with identified firmware bugs fixed (3/24)
- **February 2025:** S0-VTOL takeoff default set to 50m for testing; S1-22 tail offset mechanically adjusted to 4.5-5 degrees rather than electronic trim

### Payload Integration & Testing
- **July 2020:** S20003 30km comms range test: 20km 900MHz achieved (below 30km requirement) — cable quality issues identified, Pasternack cable needed
- **2021:** USGS payload specs documented in shared spreadsheet; multiple payload configurations (SMM, trace gas, photogrammetry, CO2, methane) standardized
- **May 2022:** CO2 payload underslinging considered as fix for moment-of-inertia issues; wind cap 15-20 mph with payload confirmed
- **August 2022:** LDCR firmware updates and AP telemetry logging verification made mandatory pre-flight
- **September 2024:** MicaSense Altum camera image failures escalated — image files shared for manufacturer investigation

### Safety & Operational Changes
- **February 2021:** RC field hours moved to 9:30 AM start (from 10 AM)
- **July 2024:** For non-production test aircraft, mandated short manual hover on first flight of day to catch critical issues quickly
- **March 2025:** Fleet maintenance system reinstated using Asana project tracking per-aircraft repairs/inspections

---

## Projects & Initiatives

### Active Aircraft Platforms

**S-Series Fixed Wing:**
- S1 variants (S10005, S10011, S10018, S10019, S10020, S10022): Primary fixed-wing platform with continuous firmware testing
- S2 variants (S20003, S20008, S20009, S20013, S20015): Larger fixed-wing with soil moisture, trace gas, photogrammetry payloads
- S0 (cardboard test platform): High-start bungee launcher testing, avionics integration testbed
- **Status (April 2025):** S1-22 experiencing yaw and motor control issues; S1-19 radar testing over water (30m altitude constraint); S10022 DroneCAN testing ongoing; multiple aircraft undergoing continued firmware validation

**E-Series Multirotors (E2):**
- E20004–E20014: Quad platforms with various gimbal and payload configurations
- **Status (April 2025):** E20014 QC restarted after 2022 hiatus, firmware/params updated to 2050 AP specs; multiple units undergoing Altum camera integration testing

**Flamewheel (FW) Multirotors:**
- FW0001, FW0002: Smaller multirotor test platforms
- **Status (April 2025):** Updated with new comms/logging code; kill switch validation and joystick hover stability testing planned

**S1-VTOL & S0-VTOL Development:**
- S1-20 (S3 avionics variant): Hover testing, transition refinement, landing detection issues
- S0-VTOL (S01006): Landing yaw issues under testing; yaw damping gains being tuned
- S3-Mass Model: Hover testing pending after component installation and magnetometer calibration
- **Status (April 2025):** First S1-VTOL transition flight successful 4/22; S0-VTOL completing initial hover tests; S3 identified 4 critical firmware bugs in actuator board requiring merged feature branch

**Specialized Platforms:**
- Creare Ring Wing, Creare Titan: Alternative test airframes for specialized missions
- Chilli: Large wing aircraft; car test showed significant lift at 40 mph, deemed unsafe above that speed

### Payload Integration Programs

**Soil Moisture Mapping (SMM):**
- Radiometer SN003, SN007 integrated with S2 aircraft
- **Status (April 2025):** Air Force project deadline March 11, 2025; collection paused due to snow on ground; three test boxes selected at Sod Farm (Eryan managing); mag calibration showing ~50nT higher reading over tank area; do not fly above 20 mph winds

**Trace Gas Payloads:**
- CO2 sensor (LiCOR): Calibration to 1 ppm accuracy; 30+ minute flight stability
- Methane sensor (CH4): Flight tested, signal detection confirmed; post-flight analysis ongoing
- **Status (April 2025):** S2 with CH4 payload completed flight in 30+ mph gusty conditions; sensor data being processed

**Photogrammetry/Imaging:**
- Sony a5100, FLIR Vue Pro R, MicaSense Altum integrated across S1, S2, E2 platforms
- **Critical Issue:** Altum camera experiencing channel failures, image saturation, and trigger timing problems at 75% overlap (causes seizures); MicaSense contacted for support
- **Status (April 2025):** Altum camera strobe interfering with DLS measurements; recommendation to disable or cover with aluminum tape; tag locations confirmed good on multiple flights

**Thermal Imaging:**
- FLIR camera and Sony a5100 for volcano mission and NASA photogrammetry payload flights
- Gimbal pitch control and pointing issues previously noted; IMU installation on gimbal board required

**Remote ID / Dronetag Integration:**
- feature/dronetag branch ready for S0 integration (March 2025)
- **Status (April 2025):** Multiple Remote ID errors on S1-20 and other aircraft; latest fixes from Sam Hild address baudrate reset issues and CAN bus configuration; latest theory involves GCS lat/lon update