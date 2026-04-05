# #swiftcore

## Overview
This channel serves as the primary technical communication hub for Black Swift Technologies' SwiftCore drone system development. It covers firmware development, tablet application updates, flight testing coordination, bug fixes, feature implementation, and release management. The channel shows very active usage with 4397 messages across 22 batches, spanning approximately 2020-2025, with key participants including Jack Elston, Ben Busby, Danny Troke, Maciej, Frank Strazzabosco, and Cory.

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

**Hurricane Web Controller (2024-2025):**
- **Status:** Completed and ready for testing
- **Features:** Dynamic GFS overlay (10m wind speed, mean sea level pressure), storm data interface
- **Team:** Dan Prendergast working on storm data interface

**App Architecture Framework (2022-2024):**
- **Status:** Completed and merged
- **Purpose:** Replace old sensors folder approach with XML-based app configuration
- **Features:** Payload serial configuration, command interfaces, sensor definitions

## Action Items & Commitments

**Recent Outstanding Items:**
- **Ben Busby:** Complete SwiftCore 3.3 remaining tasks (commands view refactor, UA window display fixes, XML param file testing)
- **Jack Elston:** Debug rotate bug and prioritize 3.3 release tasks
- **Team:** Test hurricane web controller with S0 payload packets in simulation
- **Infrastructure:** Complete migration from AWS to Hetzner for cost savings

**Historical Completed Items:**
- **Ben Busby:** Fixed app lockup bug caused by invalid longitude values (February 2022)
- **Frank Strazzabosco:** Optimized STM32H743 sensor timing with multiple timer configurations (2021)
- **Danny Troke:** Updated S1 aircraft actuator channels to match standardization
- **Maciej:** Analyzed 200+ E2/S2 flights for voltage cutoff criteria, recommended 2.9V/cell threshold

## Client & External References

**NASA:**
- Mark Motter tablet update issues with 2019 version
- Bruce requiring JSB simulation setup for Cicada payload requirements
- Richard Kolyer and Jay Tomlin requiring logparse website access for payload data over GCS
- Camera payload flights (S20018)
- Training sessions conducted with NASA teams

**NOAA:**
- S1 upgrade with older tablet hardware
- S0 deployment target for SwiftCore 3.3
- Accuracy concerns for pressure measurements

**NREL:**
- Tucker discussing waypoint XML generation and controller architecture
- Customer using scripting feature for RC Field test flights

**University Partners:**
- ERAU (Embry Riddle) training sessions and Oklahoma operations
- OKST training preparation with hardware recommendations
- INSTAAR group requesting Arctic DEM integration for Fairbanks flights

**Other Clients:**
- Alaris PRO partnership discussions ($5K annual manufacturer account, ML collaboration)
- Hector/Oier granted access to logparse site for E2 logs
- Pablo experiencing SDK bug with flight plan map acknowledgments

## Recurring Topics & Themes

**Weekly Development Cycle:**
- Regular SwiftCore team meetings (moved from Mondays to Thursdays for in-person attendance)
- Flight testing schedule requiring bug fixes/features by Wednesday weekly
- Feature branch testing and merge cycles

**Hardware Quality Control:**
- Ongoing issues with board manufacturing quality (soldering, heat sink installation)
- GNSS board QC process enhancements (termination resistance checks)
- Radio board dip switch positioning (OFF position standard)

**Communication Protocol Evolution:**
- Continuous optimization of packet structures and bandwidth usage
- Regular comms version updates (3.18.0, 3.19.0, 3.21.0, 3220)
- Handshaking timing improvements (reduced from 4+ seconds to 30ms max)

**Parameter Management:**
- XML parameter file loading and validation system
- Parameter diff display functionality
- Vehicle-specific configuration management (S1, S2, E2, S0 aircraft types)

**Flight Safety Systems:**
- ECAMS error level management and aviation compliance
- Battery monitoring and failure prevention
- GPS loss handling and lost communications procedures
- Magnetic declination and estimator improvements

## Important Resources

**Development Infrastructure:**
- **Jenkins:** jenkins.bst.aero/binaries (replaced Ben Bot)
- **Log Parse Site:** dev.logparse.bst.aero with 1000+ flights logged
- **Binary Distribution:** Custom build system with web interface
- **Documentation:** Wiki updates for S0 aircraft and JSB simulation

**Technical Documentation:**
- **VTOL State Machine:** https://lucid.app/lucidchart/cef29857-45ca-4ae1-92cd-7bec3d9a2a90/edit
- **ECAMS Error Levels:** https://docs.google.com/spreadsheets/d/1zalkQfdGo6Y4M7P1ZSqfJZ_AmIS_GbK6q-DSee9jGdo/edit
- **Futaba Mapping:** https://docs.google.com/spreadsheets/d/1UAizrzLiIPUrLcyrzHK8SgYEf6w9gJoQaaCq8KSd3xQ/edit
- **Release Notes:** https://docs.google.com/document/d/1CHbNfOXdeRrFyEA28MD5UNOHqFiqyl4nTOUd8ozGCpk/edit

**Hardware