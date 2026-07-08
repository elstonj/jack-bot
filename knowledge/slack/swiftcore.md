# #swiftcore

## Overview
This channel serves as the primary technical communication hub for Black Swift Technologies' SwiftCore drone system development. It covers firmware development, tablet application updates, flight testing coordination, bug fixes, feature implementation, and release management. The channel shows very active usage with 4400+ messages across 25+ batches, spanning approximately 2020-2025, with key participants including Jack Elston, Ben Busby, Danny Troke, Maciej, Frank Strazzabosco, Cory, Dan Prendergast, Caleb Bishop, and Alex Lomis.

**Key Participants:** Jack Elston, Ben Busby, Danny Troke, Maciej, Frank Strazzabosco, Cory, Dan Prendergast, Caleb Bishop, Alex Lomis

**Activity Level:** Highly active with daily technical discussions, bug reports, and project coordination

## Key Decisions

**Aviation Compliance & Safety (2020-2021):**
- Changed flight mode terminology from "emergency landing" to "emergency descent" for aviation compliance
- Restricted Commands page to Developer Mode only for safety reasons
- Updated all "Flight Terminate" text to "Emergency Descent" throughout system including ECAMS actions

**Hardware Platform Support (2021-2022):**
- Android 8.0+ requirement established for tablet compatibility (dropped Android 7.0 support due to crashes)
- Decision to retire Samsung Galaxy Tab S2 tablets due to battery fire risk
- Version 3.4 designated as last release supporting older hardware (2030, 2040, 2050, 3000)

**Communications Protocol (2021-2023):**
- Major communications update with reduced rate communications to optimize bandwidth
- Replaced variables with smallest possible data types requiring multiplication/division scaling
- Communications bandwidth reduction project with packet optimization

**Comms Version Bump for CAN Deployment (April 2026):**
- Approved comms version bump due to new state added to CAN_DeploymentTubeState_t enum
- Rationale: Required for proper log parsing
- Approval: Ben Busby confirmed no concerns with version bump

**Weather Data Migration (2021):**
- Weather API migration from DarkSky (discontinued by Apple) to alternative services
- Evaluated tomorrow.io and meteostat APIs as replacements

**Battery Monitoring (2022-2023):**
- Implemented fallback system switching from SOC to integrated current measurement when BMS discrepancy exceeds 50-20%
- Battery tracking converted to watt-hours measurement with decimal precision requirements

**Terrain Data (2022-2024):**
- Moved from free USGS data to paid terrain services (MapBox) due to accuracy concerns
- Arctic DEM integration implemented for Fairbanks area operations
- Fixed significant terrain height discrepancies (50m difference between USGS and Google Earth in Alaska)

**UI Architecture & Platform Strategy (April 2026):**
- Decision to transition web controller as primary UI for both desktop and mobile use (via browser) rather than supporting separate native tablet app
- Plan to maintain Android tablet UI temporarily for legacy support but focus development effort on unified web controller
- Identified potential future TAK (Team Awareness Kit) app integration for military/DoD users as separate parallel effort if needed
- Parameter file restructuring to align web controller packet definitions more closely with comms packets (new format while maintaining backwards compatibility temporarily)
- Commitment to mobile-first web UI design with equal usability on phone and laptop

**Multi-Radio GCS Support (April 2026):**
- Approved feature/multi_radio_gcs branch development to support dual UAS operation with single ground control station
- Implementation spans autopilot, comms_protocol, and web_controller repositories
- Feature merged into main branch after flight testing and GCS validation (May 8, 2026)

**VTOL Landing Plan Calculation Update (April 28, 2026):**
- Landing plan final length calculation coefficient updated from `3 * land_ias * nav_lookahead` to `4 * land_ias * nav_lookahead`
- Rationale: Code changes made to autopilot required parameter adjustment
- Future consideration: May transition to dynamic parameter-based calculation once new param is available
- Decision made by: Maciej (autopilot lead)
- Implementation by: Ben Busby

**OpenWRT Build Infrastructure (May 7, 2026):**
- Added comms_utils stub for OpenWRT-specific builds in web controller repository
- Stub provides binary data reading functions for little-endian integer and float conversions (Uint16, Int16, Uint32, Int32, Uint64, Int64, Float32, Float64)
- No changes to core web controller repository; stub is isolated to OpenWRT builds only
- Implementation by: Jack Elston

**Comms Code Generation Refactoring (May 13, 2026):**
- Decision to create feature branch `feature/fix_type_resolution` for standardizing comms code generation syntax
- Objective: Fix enum vs struct type definition syntax inconsistencies across C/Java/Python code generators
- Rationale: Recent Go generation changes exposed mixing of syntax styles; affecting C code generation used for flight testing
- Approach: Use consistent syntax across all language generators regardless of namespace
- Implementation by: Ben Busby
- Status: Fix completed and available for testing (May 13, 2026); Jack Elston to validate

**Device Blocking Feature Review (May 27, 2026):**
- Device blocking/validation feature in tablet app identified as problematic and potentially obsolete
- Current deployment model (manual APK loading followed by in-app updates via "About" page) makes device-level blocking unnecessary
- Ben Busby to deactivate feature for customer Galaxy Tab Active5 5G testing

**Flight Plan Map Packet Redesign (May 28, 2026 - Pending):**
- Proposed simplification: Keep `FLIGHT_PLAN_MAP` request as-is for waypoint discovery, but refactor device behavior to request individual `FLIGHT_PLAN_WAYPOINT` packets only for missing waypoints
- Rationale: Current tablet implementation may not align with autopilot expectations; occasional error messages on AP SWIL side related to FLIGHT_PLAN_MAP exchange state tracking
- Additional benefit: Better optimization for low-rate communications scenarios
- Proposed by: Ben Busby
- Status: Awaiting discussion with autopilot lead to evaluate feasibility

**VTOL Hardcoded Defines to Parameters Conversion (June 5, 2026):**
- Decision to convert hardcoded #defines in VTOL code to parameters
- Rationale: Accumulation of numerous hardcoded #defines in VTOL code; potential for cleanup of unused legacy variables
- Created Asana task "Comms version update" in SwiftCore 3.3 to track this work
- Decision made by: Maciej
- Approach: Team to identify items worth adding or removing as they encounter them during development

**Payload Channel Configuration & Behavior Clarification (June 16, 2026 - Pending):**
- Issue identified: `CMD_TRIGGER_PAYLOAD` with specific payload channel triggers both cameras instead of individual channel
- Individual payload triggering is possible via max usec from surfaces tab (`ACTUATORS_CALIBRATION` packet)
- Ben Busby investigating whether dual-camera trigger behavior is intentional or requires fix
- Consideration: May update preflight trigger behavior to use actuator calibration test instead
- Status: Awaiting clarification from Jack Elston and Maciej

**Payload Configuration Documentation Update (June 16, 2026):**
- Confirmed: Surface 15 (Payload 5) designated as payload power supply
- Confirmed: Channel 13 reserved for heated pitot
- Action: Payload setup spreadsheet identified as needing refresh (Jack Elston referenced existing configuration sheet)

**GCS Hardware Platform Selection (July 7-8, 2026 - In Progress):**
- Evaluating Gateworks board options for GCS hardware with significant cost differences ($350 vs $550 for lowest vs highest spec)
- Comparing processors: i.MX8M Mini vs i.MX8M Plus variants
- Initial preference identified: GW7101-21 (i.MX8M Plus, 4GB/64GB) with GW16112 in Mini-PCIe slot and GW17054 Wi-Fi AP stacked on top
- Consideration: Whether tall stacking configuration is optimal or if boards with two expansion slots would be preferable
- Participants: Alex Lomis (evaluating options), Jack Elston (providing technical guidance)

## Projects