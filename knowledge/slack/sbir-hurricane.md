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

**Display Aircraft Production (April 21-22, 2026):**
- Approved production of 4 display S0 units: 2x 2025 models for near-term delivery (end of May target), 2x 2026 models for early-mid July delivery (April 21, 2026)
- Display units to ship without tripods/mounts/carry cases in cardboard tubes or boxes, shipped folded (April 22, 2026)
- Special thicker-skin wings to be commissioned for display models to improve appearance (April 21, 2026)
- Wing springs and antenna NOT to be pre-installed on display units to reduce shipping damage risk (April 22, 2026)
- Tripod and mount solution added to 2x display units at ~$200 cost (5 min labor) (April 22, 2026)
- Delivery deadline: June 5, 2026 for DC event requirement; shipment to AOC or HQ for redistribution (April 22, 2026)

**Inventory Management (April 23, 2026):**
- SASCWATCH has one S0 left over from previous season; decision made not to allow NOAA to use it (April 23, 2026)
- Jack Elston confirmed awareness of leftover aircraft status (April 23, 2026)

## Projects & Initiatives

**S0 Hurricane Aircraft System:**
- Primary deliverable: 16-18 complete S0 systems for NOAA hurricane reconnaissance (expanded to 25-30 additional for 2025 season)
- 2026 production run: 30 operational S0s plus 5 additional "extras" for testing 2027 features
- Specifications: 2.6 lbs GTOW, 32.8" wingspan, 22.5 m/s cruise speed, 2+ hour endurance
- Sensors: Vaisala RSS421 (RS41), MLX90614ESF thermal sensor, 9-hole pressure system, Vaisala RS41 measurement rate ~5Hz (may vary with temperature)
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
- Dual-radio capability being added to new ground stations under procurement (~1 hour work for firmware/artwork updates) (April 21, 2026)

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
  - Mitigation: Requires bandwidth optimization; science team communication essential for bal