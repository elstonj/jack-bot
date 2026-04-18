# #sbir-hurricane

## Overview
The #sbir-hurricane channel is the primary workspace for Black Swift Technologies' SBIR Hurricane project, focused on developing the S0 unmanned aircraft system for hurricane reconnaissance missions. The channel is highly active with extensive technical discussions, operational updates, and mission planning spanning 2020-2026. Key participants include Joshua Fromm, Jack Elston, Maciej, Danny Troke, Dan Prendergast, Alex Lomis, Nate, and Sam Hild.

## Key Decisions

**Aircraft Design & Configuration:**
- User panel positioned on bottom of NOAA S0 for easier access through outer tube (June 2020)
- Selected T-Motor F60 for propulsion due to discontinued KDE motor (September 2020)
- Switched from Castle ESC to 36A version for improved reliability (November 2020)
- Spring steel antenna wrapped around fuselage confirmed as optimal design (November 2020)
- Wing pivot system designed to "fall away" after deployment to save weight (December 2020)
- Deployment timing set at 5 seconds (parachute flap) and 10 seconds (tube release) (April 2021)

**Sensor & Electronics:**
- Selected SF20 laser altimeter over SF22 due to Ardupilot/PX4 integration issues (January 2021)
- Eliminated datalogging requirement after presentation feedback (April 2021)
- Selected MLX90614ESF-DCH thermal sensor per Terry's recommendation (December 2021)
- Direct soldering battery/ESC to AP due to space constraints (November 2021)
- Dual USB-A ports on front panel instead of USB-C for GCS (May 2022)

**Manufacturing & Components:**
- 50/50 cost split between Air Force and Hurricane for KMac tubes (June 2020)
- Lee selected for deployment tube machining at $700 NRE, $95 per additional tube (March 2022)
- Aluminum caps chosen over 3D printed ones after high-Q deployment failure (May 2022)
- Switched to Samsung INR21700-50S cells replacing Panasonic NCR18650GA (February 2024)
- Decision to use 76gsm wing skins instead of 160gsm for 50g weight savings (October 2024)

**Ground Control Station Operations (April 2026):**
- Single operator per aircraft confirmed as acceptable by NOAA operational rules (April 2026)
- GCS firmware updates for dual-channel radio control implemented (April 2026)
- Use of Channel 1 designated for flight operations over Avon Park (April 2026)
- Channel 1 selected for operational use after RF cable replacement on Channel 2 (April 2026)

**Humidity Sensor Configuration (April 2026):**
- Vaisala RSS421 heating mode confirmed as critical for accurate readings (April 2026)
- New PSNS firmware with corrected humidity reference validation implemented (April 8, 2026)
- Battery tracking logging enabled on all PSNS boards for sleep mode diagnostics (April 8, 2026)
- Sensor boom compatibility identified as critical - older booms incompatible with newer sensors (April 10, 2026)
- Reconditioning cycle confirmed effective for correcting humidity sensor bias (April 17, 2026)

## Projects & Initiatives

**S0 Hurricane Aircraft System:**
- Primary deliverable: 16-18 complete S0 systems for NOAA hurricane reconnaissance (expanded to 25-30 additional for 2025 season)
- Specifications: 2.6 lbs GTOW, 32.8" wingspan, 22.5 m/s cruise speed, 2+ hour endurance
- Sensors: Vaisala RSS421, MLX90614ESF thermal sensor, 9-hole pressure system
- Communication: 400MHz licensed band with 150+ nautical mile range demonstrated
- 2026 Avon Park operations: Dual S0 deployments from P3 aircraft with coordinated multi-UAS capability

**Multi-UAS Operations (April 2026):**
- Dual-aircraft capability for simultaneous operations with single operator demonstrated
- GCS infrastructure supporting multiple aircraft from NOAA P3 platform
- Closest approach between S0s: 70m achieved (April 8, 2026)
- Range testing: S0-72 tested 80+ mile communication range (April 7, 2026)
- Coordinated flight operations with 5km x 5km box patterns and precision altitude hold testing

**Hurricane Flight Controllers:**
- Dan Prendergast developed eyewall tracking algorithms with left/right turn capabilities
- Inflow controller for spiral trajectory patterns
- Center fix controller for eye navigation (first successful automated center fix achieved)
- Controllers tested extensively in X-Plane simulation and live hurricane flights
- Dual-aircraft operation tested with lost communications handling (battery suppression warnings confirmed as design limitation)

**Ground Control Station (GCS) - Critical Issues Resolved (April 2026):**
- Dual Swift Station systems (SwiftStation-400001 "top" and SwiftStation-400002 "bottom") for multi-channel operations
- Rack-mounted system with HDMI output, powered USB hub
- 400MHz radio integration with tablet interface and hot-swappable USB radio modules
- Real-time telemetry and flight plan generation capabilities
- Channel 1 and Channel 2 radio configuration with dynamic switching capability

**GCS Issues Identified and Fixed (April 7-8, 2026):**
- Power shutdown bug: UPS driver incorrectly reporting -0.000001A causing premature power-off at 100% battery charge
  - Root cause: Threshold set below normal noise level when transitioning from charging to AC power
  - Fix: Replaced current-based check with VIN + state detection (charging/discharge/USB modes)
  - Modified HIDOpenUPS2.cpp with new getters: getInputVoltage(), getState()
- Flight plan transmission failures: 36 failed commands during April 7 flight due to duplicate handling gap
  - Issue: UAS receiving retransmitted COMMAND while in WAITING_FOR_WAYPOINTS state causes reset
  - Duplicate handling exists for WAITING_FOR_FINAL_MAP_RX but missing for WAITING_FOR_WAYPOINTS
  - Requires code fix to handle retransmitted commands gracefully
- Tablet connectivity losses: SYSTEM_INIT requests flooding at 574 attempts with only 1 response during 10-minute disconnect
  - Root cause: Met data rate increased from 1Hz (pre-flight) to 5Hz (flight) consuming ~90% bandwidth
  - Impact: Nearly saturated communications bandwidth preventing proper tablet reconnection handshakes
  - Mitigation: Requires bandwidth optimization; science team communication essential for balancing data needs
- RSSI reporting issue: Ch2 showing -1 values while still transmitting telemetry (signal degradation masked)
- RF cable quality: Channel 2 showing 15dB worse RSSI than Channel 1 initially, improved to 1.7dB loss (Ch1) vs 2.5dB (Ch2) after cable replacement by AOC

**Vaisala RSS421 Humidity Sensor Resolution (April 8-17, 2026):**
- Initial issue: Systematic RH readings 20-30% lower than reference measurements affecting all 2025 aircraft
- Root cause investigation completed:
  - Issue isolated to PCB and individual unit configuration variations, not sensor boom or connectors
  - Heating mode critical: must be ON for accurate readings
  - Older sensor booms incompatible with newer sensors causing heating mode to disable
  - New and old sensors read identically when tested on compatible boom/airframe combinations
  - Firmware versions with undefined status bits 11-12 (newer Vaisala manual may clarify)
  - Reconditioning cycle (heating time) affects stabilization but not core accuracy
  - Post-reconditioning, some units that read low initially began reading correctly
  - First reading often correct, then rapidly reduces (possible heater control issue)
- **Recent Resolution (April 17, 2026):**
  - Jack Elston identified ~3% RH bias in "new" units compared to reference units
  - Reconditioning cycle successfully removed the 3% bias across affected units
  - All units now reading consistently after reconditioning
  - Status: Issue appears resolved; units can return to service
- Actions taken:
  - Technical support tickets opened with Vaisala requesting updated