# #flight-testing

## Overview

The #flight-testing channel serves as Black Swift Technologies' primary hub for coordinating flight test operations, troubleshooting aircraft and payload issues, and tracking firmware/software development across their fleet of fixed-wing (S-series), multirotor (E2, Flamewheel), and VTOL (S0, S1-VTOL, S3) platforms.

**Key Participants:** Maciej (lead flight testing/analysis), Jack Elston (firmware development), Joshua Fromm (QA/component sourcing), Ben Busby (tablet/GCS software), Nate (videography/pilot), Alex Lomis (field operations/media/pilot), Sam Hild (Remote ID integration/test pilot), Dan Prendergast (autopilot/control systems/operations), Danny Troke (data management), Ethan Domagala (pilot), Beck Cotter (operations support), Paige Smith (media/video curation), Sunny Slope Sod Farm (external airspace contact), Chris & Kevin (external clients/stakeholders), Christoph & Angie (internal stakeholders)

**Activity Level:** Extremely high — 5,600+ messages across June 2020 through April 2026. Daily operations with multiple aircraft flights, rapid issue turnaround, continuous firmware iterations, and intensive VTOL transition testing. Recent activity (April 2026) shows intensive multi-aircraft testing cycles with frequent coordination requirements. Latest activity (April 28, 2026) documents post-S3-MASS first full flight analysis, client communications preparation, and concurrent S1-22 landing profile optimization testing.

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
- **April 23, 2026:** S3-MASS left pivot servo grounding issue resolved with added grounding strap; aircraft approved for flight testing with monitoring contingency
- **April 24, 2026:** S1-22 cleared for extended flight testing (1+ hour accumulated with no observed issues); S3-MASS and S30001 scheduled for continued hover testing pending wind conditions
- **April 25, 2026:** E-MASS project training data collection scheduled Monday; confirmed two relatively charged E2 batteries available for mission; waypoint plan phases configured for sequential loading during flight to maximize training data capture across one or two flights
- **April 27, 2026:** S3-MASS approved for first full autonomous flight after successful hover tests; motor_out_yaw branch deferred from S3_mass_model (integral gain tuning concerns and motor failure mitigation strategy requires further development; rudder damping gains require aircraft-specific tuning vs. S0 baseline)
- **April 28, 2026:** S3-MASS successful first full autonomous flight completed; S1-22 landing profile optimization scheduled for concurrent testing to inform S3 future flights

### Firmware & Code Management
- **October 2020:** Angle-to-rate loop gains critical safety parameter — develop (8,8,3) vs. master (4,4,1.5) discrepancy required close monitoring
- **February 2021:** Tablet app parameter validation feature added as non-intrusive compromise after initial disagreement on comparison button inclusion
- **February 2021:** S1-5 reverted from develop to master code due to IAS calculation stall/launch problems
- **March 2024:** Feature branches (feature/ias_clog_new_detector, feature/dronetag) approved for testing; feature/s3_mass_model branch merged into develop with identified firmware bugs fixed (3/24)
- **February 2025:** S0-VTOL takeoff default set to 50m for testing; S1-22 tail offset mechanically adjusted to 4.5-5 degrees rather than electronic trim
- **April 2026:** S10022 DroneCAN firmware deployment; S10020 updated to latest code with yaw gyro diagnostics required before further flights; S3 firmware issues identified requiring feature branch merge for actuator board fixes
- **April 20, 2026:** S10022 motor control issue resolved via canard firmware modification to free memory allocation even when system doesn't flag necessity
- **April 21, 2026:** RTK bug identified in S10022 requiring return to facility; GNSS board orientation critical (perfect square bolt pattern requires correct alignment matching previous flights)
- **April 23, 2026:** 
  - S10022 comms firmware updated to latest develop branch (previous version: fd427ad); no watchdog reset (WWDG) detected in logs indicating non-reset source; Jack Elston added extra debugging to catch other reset sources
  - New S10022 autopilot binary compiled with additional reboot diagnostics; verified with most recent actuator code reflashed
  - S1-21 (2030 hardware + XTend) build compiled; pushed to develop repository
  - S3-MASS build standardized using `./make S3` option to ensure all compiler flags included correctly
  - Identical firmware code across S10022, S1-22, and S1-21 planned for April 24 testing to verify no reset bugs introduced in recent code updates
- **April 24, 2026:** S1-22 firmware confirmed stable (develop + comms develop branches); autopilot and power board updated prior to testing; additional reset diagnostics added to codebase by Jack Elston for future troubleshooting
- **April 27, 2026:**
  - No firmware updates required for S10022 or S3-MASS over weekend (Jack Elston confirmed motor_out_yaw branch not relevant to VTOL testing)
  - Joshua Fromm set S1-22 motor volts limit starting voltage to 0V (no other settings changed)

### Safety & Flight Operations
- **February 2021:** RC field hours moved to 9:30 AM start (from 10 AM)
- **July 2024:** For non-production test aircraft, mandated short manual hover on first flight of day to catch critical issues quickly
- **March 2025:** Fleet maintenance system reinstated using Asana project tracking per-aircraft repairs/inspections
- **April 2026:** Dead IMU (Z-axis gyro) on S10021 identified as critical grounding condition; aircraft should not fly without functional yaw gyro reporting; lost motor events on S1-VTOL during transition require investigation before subsequent flights
- **April 20, 2026:** S1-22 pre-flight checklist formalized: (1) Manual hover with GPS PDOP <3 verification; (2) Joystick hover with 90° yaw confirmation and full stick forward test; (3) Motor failure contingency protocol — pilot must switch to manual throttle-down immediately if single motor loss detected in forward flight
- **April 22, 2026:** S1-22 in-flight autopilot reset event occurred during takeoff orbit (5+ min prior to motor failure); AP reset disables engines requiring manual re-enable via tablet or "force flying" button; motor failure mitigation testing resumed with dual logging (flight log + GCS log backup)
- **April 20, 2026:** Nose tape requirement enfor