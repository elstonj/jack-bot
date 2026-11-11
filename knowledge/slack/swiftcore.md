# #swiftcore

## Overview
This channel serves as the primary technical communication hub for Black Swift Technologies' SwiftCore drone system development. It covers firmware development, tablet application updates, flight testing coordination, bug fixes, feature implementation, and release management. The channel shows very active usage with 4400+ messages across 28+ batches, spanning approximately 2020-2025, with key participants including Jack Elston, Ben Busby, Danny Troke, Maciej, Frank Strazzabosco, Cory Dixon, Dan Prendergast, Caleb Bishop, Alex Lomis, Spencer Hoehl, and Ali Sulehria.

**Key Participants:** 
- Jack Elston (autopilot/firmware/simulation lead, UI/packaging, release management)
- Ben Busby (comms/GCS/tablet app, infrastructure/Jenkins)
- Maciej (autopilot/VTOL/simulation testing lead, clog detection specialist, GPS-out hover fix specialist)
- Spencer Hoehl (simulator testing lead, QC flight procedures, flight test validation)
- Ali Sulehria (software and use case testing)
- Dan Prendergast (infrastructure/GitLab access)
- Cory Dixon
- Other team members

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

**GCS Hardware Platform Selection (July 7-10, 2026 - FINALIZED):**
- **Initial Decision (July 7-8, 2026):** Use exact setup from NOAA GCS regarding Gateworks board and expansion configuration
  - Two-slot board selected to provide more options for future expansion
  - Alternative approach considered: Using onboard UART for GPS and USB for secondary expansion

**Clog Detector Parameter Update (October 23, 2026):**
- Decision to move remaining clog detector fixes to version 4.0
- SwiftCore 3.3 will operate without clog detection by default
- Clog detection will be enabled selectively for BST missions in rain conditions
- Rationale: Clog detector parameters were based on incorrect propulsion model; parameters now corrected for S3 model update
- Action: Zero out clog detector parameters on simulator (Estimator page XML update by Maciej)
- Approved by: Jack Elston (October 23, 2026)

**Local Git Server Infrastructure (October 27, 2026):**
- Maciej established local git server setup (thanked @U0151201DMY for assistance)
- Navy STTR project repository hosted on local server (not on GitLab)
- Indicates expansion of internal repository management beyond primary GitLab infrastructure

**GPS-Out VTOL Hover Fix (November 2, 2026 - APPROVED & MERGED):**
- Maciej's no-GPS hover fix merged into release/3.3.0 with refinements by Jack Elston
- **Changes by Jack Elston:**
  - cf_acc_gain 1/10 cut now only applies while aircraft is flying (vehicle.isFlying()), preventing 10x slower attitude convergence after power-on for vertical-launch VTOL
  - Consolidated cf_acc_gain cut and lost-GPS vff reset into same conditional branch for consistency
  - Removed redundant `!hasTransitionedToForward()` term from vff reset logic (updateLatAngCtrl already excludes TRANSITION_TO_HOVER)
- **Validation Required:** Spencer Hoehl to run simulator tests before hover flight test
- **Test Plan:** Manual hover for ~30s with parameter change before/after, then aborted takeoff test
- **Merge Status:** Code merged and compiled (VT/FW/MR SWIL builds successful, no simulation testing yet as of November 2)

**SwiftCore 3.3.0 Master Release (November 10, 2026 - RELEASED):**
- **Official Release Date:** November 10, 2026
- **Last Master Release:** Version 3.2.8 (January 2023)
- **Development Scope:** Nearly 4 years of work with 2,192 commits in autopilot repo, 1,000+ commits across comms_protocols, SDK, and simulator
- **Total Impact:** 3,200+ commits, 4,000+ files modified
- **Major Features Now in Master:**
  - New aircraft & platforms: S3 tilt-rotor VTOL fully supported (PSNS smart battery, GNSS, actuator and heated MHP boards); S0-VTOL, S1-VTOL, S2-VTOL support
  - S0 air-deployed tube/drop launch: launch pin detection, automatic takeoff waypoint, engine enable in the tube, aircraft power control from deployment tube
  - New STM32H7 (HW 3000) and HW 2050 autopilots with USB bootloader
  - Completely reworked VTOL transitions in both directions with controlled deceleration and pivot maneuvers
- **Announcement By:** Jack Elston (November 10, 2026, 12:18 UTC)

## Projects & Initiatives

**SwiftCore 3.3.0 Release (COMPLETED - November 10, 2026):**
- Master branch release officially announced
- Flight testing completed with multiple failure scenario validation
- Autopilot 3.3 release candidate firmware successfully validated
- GPS-out VTOL hover fix validated and merged (November 2, 2026)
- All critical features and bug fixes integrated
- 4+ years of development work consolidated into single release
- Status: RELEASED to master branch

**SwiftTab App Development:**
- Current version: SwiftTab-staging.apk on 3.3 branch
- Issue identified: App crashes when loading saved aircraft params files onto aircraft running SwiftCore AP 3.3 RC firmware (reported October 23, 2026 by Spencer Hoehl)
- Bug report functionality working, reports being received by Ben Busby
- Status: May transition to web controller primary UI (April 2026 decision) with legacy Android support

**Failure Scenario Testing (October-November 2026 - COMPLETED for 3.3):**
- Loss of GPS in joystick mode: Appears to be working normally; may have been handset setup issue
- Loss of pitot: Functioning correctly in both fail app and GUI
- Static sensor loss: Expected Level 2 failure behavior confirmed; no issues found
- Mag failures: Showing normal/expected behavior
- Waypoint skipping at higher altitudes: Reproduced by Ali Sulehria (has 20-minute screen recording for review)
- **GPS-out in hover:** Validated with parameter changes and manual testing; fix merged into 3.3.0 (November 2, 2026)

**S3 Model Aircraft Configuration:**
- Default S3 XML files added by Maciej (October 23, 2026)
- Propulsion model updates completed affecting clog detector parameters
- PSNS smart battery, GNSS, actuator and heated MHP boards supported in 3.3.0 release

**Navy STTR Project (October 27, 2026 - ONGOING):**
- Separate development initiative tracked in local git server (not on primary GitLab)
- Maciej managing repository setup and initial commits
- Status: Repository established and first project pushed to local server

## Action Items & Commitments

**No open action items identified in latest communication (November 10, 2026).** Previous action items related to GPS-out hover fix validation and SwiftTab crash investigation appear to have been completed or resolved as part of the 3.3.0 release cycle.

## Client & External References
- **Navy STTR Project:** Separate development initiative (infrastructure established October 27, 2026)

## Recurring Topics & Themes

**Failure Scenario Testing:**
- Regular validation of autopilot failure modes including:
  - GPS loss in various flight modes (including hover scenarios)
  - Pitot pressure sensor failures
  - Static pressure sensor failures (blocked vs. off)
  - Magnetometer failures
  - Waypoint navigation anomalies
- Completed for SwiftCore 3.3.0 release validation

**Simulator vs. Real Hardware Testing:**
- Ongoing discussion of simulation discrepancies vs. actual aircraft behavior
- Handset/USB joystick configuration issues affecting test repeatability
- Firmware version consistency between simulator and test platforms
- Simulator validation used before flight testing (GPS-out hover fix example)

**Clog Detection:**
- Recurring issue with parameters based on incorrect propulsion model
- Trade-off between detection capabilities and operational flexibility
- Selective enablement strategy for rain missions
- Deferred to SwiftCore 4.0 for full implementation with S3 model corrections

**Infrastructure & Repository Management:**
- Evolution of development infrastructure beyond GitLab
- Local git server now supporting additional project repositories (Navy STTR)

**VTOL Platform Support:**
- Expanding aircraft and hardware platform support (S0-S3 VTOL variants)
- New autopilot hardware (STM32H7, HW 3000, HW 2050)
- Drop launch and air-deployment capabilities
- Transition control improvements

## Important Resources

**XML Configuration Files:**
- SwiftCore AP 3.3 Estimator page XML (parameter configuration)
- S3 model default XML files (added October 23, 2026)
- Payload configuration spreadsheet (flagged for refresh, June 2026)

**Testing Artifacts:**
- Screen recording of waypoint skipping scenario (20 minutes, held by Ali Sulehria)
- SwiftTab-staging.apk crash reports and logs (collected by Ben Busby)

**Software Branches/Versions:**
- **SwiftCore 3.3.0** (Master branch - RELEASED November 10, 2026)
- SwiftTab-staging.apk (3.3 branch)
- release/3.3.0 (merged GPS-out hover fix and all critical features)
- hotfix/no_gps_vtol_hover_fix (Maciej's original fix, merged with Jack's refinements)

**Infrastructure:**
- Local git server (established October 27, 2026)
- Navy STTR project repository (hosted on local server, not GitLab)

## Recent Activity

**November 10, 2026 - SwiftCore 3.3.0 OFFICIAL MASTER RELEASE (12:18 UTC):**

**Milestone Achievement:**
- SwiftCore 3.3.0 officially merged to master branch
- Previous master release: 3.2.8 (January 2023) - nearly 4-year gap
- Total development effort: 3,200+ commits, 4,000+ files touched

**Major Features in 3.3.0:**

*New Aircraft & Platforms:*
- S3 tilt-rotor VTOL fully supported with:
  - PSNS smart battery integration
  - GNSS support
  - Actuator and heated MHP boards
- S0-VTOL, S1-VTOL, S2-VTOL variants supported
- S0 air-deployed tube/drop launch system:
  - Launch pin detection
  - Automatic takeoff waypoint
  - Engine enable capability in tube
  - Aircraft power control from deployment tube
- New autopilot hardware: STM32H7 (HW 3000), HW 2050 with USB bootloader

*Flight Control & Navigation:*
- Completely reworked VTOL transitions in both directions
- Controlled deceleration capabilities
- Pivot maneuvers

**Contributor Recognition:**
- Jack Elston acknowledged all team members who designed, coded, flight-tested, QC'd and debugged their way to this release

**November 2, 2026 - GPS-Out VTOL Hover Fix Approval & Testing Plan:**

**Code Changes Merged:**
- Maciej's no-GPS hover fix merged into release/3.3.0 (hotfix/no_gps_vtol_hover_fix)
- Jack Elston added two refinements on top of Maciej's work (commit 7e81ed129):
  - cf_acc_gain 1/10 cut restricted to in-flight periods only (vehicle.isFlying() guard)
    - Resolves issue where vertical-launch VTOL had 10x slower attitude convergence after power-on before first GPS fix
    - Consolidated logic into existing conditional branch with lost-GPS vff reset
  - Removed redundant `!hasTransitionedToForward()` term from lost-GPS vff reset
    - No behavioral change (updateLatAngCtrl already excludes TRANSITION_TO_HOVER)
    - Simplifies conditional logic

**Compilation Status:**
- VT/FW/MR SWIL builds compile successfully
- No simulation testing performed yet (as of November 2)

**Testing Requirements:**
- Spencer Hoehl to run simulator tests on release/3.3.0 head:
  - GPS dropout in hover test
  - Jack Elston offered to push simulator update if Spencer prefers
- Manual hover flight test scheduled:
  - ~30 second manual hover with parameter change before/after
  - Aborted takeoff test to follow
- Maciej to walk Spencer through test procedure on November 3, 2026

**October 27, 2026 - Infrastructure Expansion:**
- Maciej acknowledged support from @U0151201DMY for local git server setup
- Navy STTR project repository successfully established on local git server
- First repository pushed to local infrastructure, indicating shift toward distributed repository management for specialized projects

**October 23, 2026 - Version 3.3 Flight Testing Progress:**

**Failure Scenario Validation Results:**
- **Loss of GPS in joystick mode:** Working normally on Maciej's handset; likely simulator setup issue on test system
- **Pitot failure handling:** Functioning correctly in both fail app and GUI; Maciej unable to reproduce "freezing" issue (Spencer to investigate further)
- **Static sensor loss:** Correct Level 2 behavior confirmed; previous "static blocked" test condition changed to "static off" by Jack Elston, causing NaN value behavior
- **Magnetometer failures:** Normal/expected behavior observed by Maciej; insufficient detail provided for debugging
- **Waypoint skipping:** Ali Sulehria initially reproduced but unable to reproduce on second attempt with same flight plan; identified as potentially user-error, will monitor for recurrence; higher altitude scenarios warrant further investigation

**Clog Detector Parameter Management:**
- Decision finalized to defer clog detector fixes to 4.0 release
- Parameters will be zeroed out on simulator for 3.3 operations
- Root cause identified: Parameters were based on incorrect propulsion model; S3 model update now requires recalibration
- Approved by Jack Elston with thanks to Maciej

**SwiftTab App Issue:**
- Critical crash reported: SwiftTab-staging.apk crashes when loading saved aircraft parameter files onto aircraft running SwiftCore AP 3.3 RC firmware (October 23, 11:09 AM)
- Bug report auto-submitted; Ben Busby acknowledged and investigating

**XML Configuration Updates:**
- All XML files updated and pushed by Maciej
- Default S3 aircraft XMLs added for standard configuration reference
- Clog detector parameters awaiting zeroing on Estimator page