# #swiftcore

## Overview
This channel serves as the primary technical communication hub for Black Swift Technologies' SwiftCore drone system development. It covers firmware development, tablet application updates, flight testing coordination, bug fixes, feature implementation, and release management. The channel shows very active usage with 4397+ messages across 23 batches, spanning approximately 2020-2025, with key participants including Jack Elston, Ben Busby, Danny Troke, Maciej, Frank Strazzabosco, Cory, Dan Prendergast, Caleb Bishop, and Alex Lomis.

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

**UI Architecture & Platform Strategy (April 2026):**
- Decision to transition web controller as primary UI for both desktop and mobile use (via browser) rather than supporting separate native tablet app
- Plan to maintain Android tablet UI temporarily for legacy support but focus development effort on unified web controller
- Identified potential future TAK (Team Awareness Kit) app integration for military/DoD users as separate parallel effort if needed
- Parameter file restructuring to align web controller packet definitions more closely with comms packets (new format while maintaining backwards compatibility temporarily)
- Commitment to mobile-first web UI design with equal usability on phone and laptop

**Multi-Radio GCS Support (April 2026):**
- Approved feature/multi_radio_gcs branch development to support dual UAS operation with single ground control station
- Implementation spans autopilot, comms_protocol, and web_controller repositories

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
- **Status:** Completed and ready for testing; active validation ongoing (April 2026)
- **Features:** Dynamic GFS overlay (10m wind speed, mean sea level pressure), storm data interface
- **Team:** Dan Prendergast working on storm data interface
- **Recent Activity:** Jack Elston validating changes; testing scheduled with Maciej and Alex (April 8, 2026)

**App Architecture Framework (2022-2024):**
- **Status:** Completed and merged
- **Purpose:** Replace old sensors folder approach with XML-based app configuration
- **Features:** Payload serial configuration, command interfaces, sensor definitions

**Multi-Radio GCS Support (April 2026):**
- **Status:** Active development in feature/multi_radio_gcs branch
- **Objective:** Enable single GCS to manage two UAS simultaneously
- **Scope:** Requires changes to autopilot, comms_protocol, and web_controller repositories
- **Challenge:** Legacy codebase not originally designed for multiple connections; addressing issues with per-aircraft addressing and system initialization packets
- **Team:** Jack Elston (autopilot/comms), Ben Busby (web controller), Maciej and Alex (testing April 8-9, 2026)
- **Current Issues Resolved:** Transmit command buffer overflow errors, per-aircraft system_init packet routing, redundant multi-device initialization requests

**Web Controller UI Redesign (April 2026):**
- **Status:** Active development with modular layout system in progress
- **Current Focus:** Replacing legacy tablet-centric UAS window with command-centric interface inspired by RTS game design
- **Design Goals:** 
  - Mobile-first responsive design usable on phone and laptop
  - Low-click-density finger-friendly mobile interface
  - Command window popup for quick local commands and status checking
  - Replacement of cumbersome multi-layer OOP tablet architecture
- **Timeline:** Modular UI layout system expected soon
- **Team:** Ben Busby leading design; Maciej suggesting split of web (flight ops focus) vs Android (config/tuning)
- **Philosophy:** Unified web UI long-term rather than maintaining separate tablet app

**Parameter File Restructuring (April 2026):**
- **Status:** Planning phase, not urgent
- **Objective:** Restructure XML parameter files to map 1:1 with comms packet definitions instead of requiring custom conversion logic
- **Current Issue:** Param files don't align with packet structure, creating parsing overhead
- **Approach:** Maintain both old and new file formats temporarily; develop converter utility while transitioning
- **Decision-makers:** Maciej approved new format approach; Ben Busby investigating implementation

## Action Items & Commitments

**Current Outstanding (April 2026):**
- **Jack Elston:** 
  - Finalize feature/multi_radio_gcs branch (multiple radio connections with per-aircraft addressing) - validation in progress
  - Continue validation of hurricane web controller changes
  - Clarify PayloadNodeView indentation/formatting in feature/emass branch
  - Testing double autopilot with GCS after pulling recent fixes
  - Debug Transmit Command Buffer Overflow errors in multi-radio implementation
  - Investigate web controller and swil high CPU usage

- **Ben Busby:** 
  - Review and integrate multi-radio GCS changes from Jack's commits
  - Push web controller CPU usage optimizations (in progress - improvement made April 8-10)
  - Implement modular UI layout system for web controller redesign
  - Design mobile-first responsive web UI for equal phone/desktop usability
  - Fix aircraft selection feature in web controller (broken by HTMX hook, deferred until after PTO return)
  - Investigate and fix parameter file structure mapping to comms packets
  - Review tablet changes for feature/emass branch (SDK state machine updates)
  - PTO scheduled (April 9, 2026) - expects code changes during absence
  - Implement claude.md coding guidelines in autopilot and web controller repos

- **Maciej & Alex:** 
  - Flight test feature/multi_radio_gcs branch with dual