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
- Approved comms version bump due to new state added to CAN_DeploymentTubeState_t enum (April 27, 2026)
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

**Multi-Radio Feature Merge (May 8, 2026):**
- Multi-radio GCS feature merged into main branch after completion of flight testing and GCS validation
- Jack Elston notified team of merge; feature ready for production use
- No anticipated impact on parallel development efforts but team advised to report any issues

**Comms Code Generation Refactoring (May 13, 2026):**
- Decision to create feature branch `feature/fix_type_resolution` for standardizing comms code generation syntax
- Objective: Fix enum vs struct type definition syntax inconsistencies across C/Java/Python code generators
- Rationale: Recent Go generation changes exposed mixing of syntax styles; affecting C code generation used for flight testing
- Approach: Use consistent syntax across all language generators regardless of namespace
- Implementation by: Ben Busby
- Status: Fix completed and available for testing (May 13, 2026); Jack Elston to validate

## Projects & Initiatives

**SwiftCore 3.2 Release (2021-2022):**
- **Status:** Completed September 2021
- **Features:** PPK implementation, Dubin's path display, streaming video, look-at points
- **Testing:** End-of-month testing goal achieved December 2021

**SwiftCore 3.3 Release (2022-2024):**
- **Status:** Ongoing, targeting NOAA S0 deployment and S0/S2 VTOL testing
- **Features:** Air deploy capability, payload control, vehicle refactor, separate cruise/hover speed parameters
- **Management:** Structured workflow using Asana for tracking hotfixes/features through simulation, benchtop, and flight testing phases

**VTOL Aircraft Integration (2023-2025):**
- **Status:** Active development with control mixer branch
- **Scope:** Autopilot, tablet, and communications updates for vertical takeoff/landing aircraft
- **Testing:** S3/S10020 aircraft being used for validation
- **Challenges:** Parameter management, UI integration, XML configuration
- **Recent Update (April 28-29, 2026):** Landing plan final length calculation updated and validated; distance display fixed and deployed via APK; vertical landing for S1 aircraft tested with 17m/s IAS and 2.25s lookahead resulting in correct 114m approach length
- **Latest (May 21, 2026):** Maciej pushing additional fixes to branch

**Hurricane Web Controller (2024-2025):**
- **Status:** Completed and ready for testing; active validation ongoing (April 2026)
- **Features:** Dynamic GFS overlay (10m wind speed, mean sea level pressure), storm data interface
- **Team:** Dan Prendergast working on storm data interface
- **Recent Activity:** Jack Elston validating changes; testing scheduled with Maciej and Alex (April 8, 2026)

**App Architecture Framework (2022-2024):**
- **Status:** Completed and merged
- **Purpose:** Replace old sensors folder approach with XML-based app configuration
- **Features:** Payload serial configuration, command interfaces, sensor definitions

**Multi-Radio GCS Support (April 2026-ongoing):**
- **Status:** Merged to main branch (May 8, 2026) after flight testing and GCS validation completed
- **Objective:** Enable single GCS to manage two UAS simultaneously
- **Scope:** Changes to autopilot, comms_protocol, and web_controller repositories
- **Resolved Issues:** Transmit command buffer overflow errors, per-aircraft system_init packet routing, redundant multi-device initialization requests
- **Latest (May 7, 2026):** OpenWRT build infrastructure enhancements with binary utilities stub for proper data format handling
- **Latest (May 8, 2026):** Feature fully merged; no anticipated impact on other development but team monitoring for issues

**Web Controller UI Redesign (April 2026-ongoing):**
- **Status