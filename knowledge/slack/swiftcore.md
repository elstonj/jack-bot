# #swiftcore

## Overview
This channel serves as the primary technical communication hub for Black Swift Technologies' SwiftCore drone system development. It covers firmware development, tablet application updates, flight testing coordination, bug fixes, feature implementation, and release management. The channel shows very active usage with 4400+ messages across 28+ batches, spanning approximately 2020-2025, with key participants including Jack Elston, Ben Busby, Danny Troke, Maciej, Frank Strazzabosco, Cory Dixon, Dan Prendergast, Caleb Bishop, Alex Lomis, Spencer Hoehl, and Ali Sulehria.

**Key Participants:** 
- Jack Elston (autopilot/firmware/simulation lead, UI/packaging, release management, code review)
- Ben Busby (comms/GCS/tablet app, infrastructure/Jenkins, submodule management)
- Maciej (autopilot/VTOL/simulation testing lead, clog detection specialist, GPS-out hover fix specialist, flight testing)
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

**Lost GPS Landing Timer Fix (November 13, 2026 - APPROVED & REFINED):**
- **Issue Identified:** Code change to lost-GPS hover fix inadvertently removed the landing time gate (`landing_time == -FLT_MAX || (landing_time-now) > 5.0`), creating a separate issue
- **Problem:** Removing this gate affected landing behavior during lost-GPS TERMINATE conditions
- **Root Cause Analysis by Maciej (November 13, 16:41):** Removal of `vz < cutoff_velocity` gate during lost_gps prevented proper landing detection
  - Vertical velocity estimate remains accurate with pressure-only sensors (S10022 flight testing showed <5% error vs. laser-based measurements)
  - Without vz cutoff check, aircraft couldn't properly trigger landing in TERMINATE mode during GPS loss
- **Solution Decision (Jack Elston, November 13, 05:54):**
  - Keep the landing time gate `(landing_time == -FLT_MAX || (landing_time-now) > 5.0)` to maintain landing time protections
  - Add additional check of `lost_gps` flag to prevent landing-time issues during GPS-out scenarios
  - This is a more conservative, lower-risk approach than removing the gate entirely
- **Additional Pre-Existing Bug Identified (Jack Elston, November 13, 05:56):**
  - isLanded() returns true 8 seconds after isTryingToLand() goes true regardless of altitude
  - Landing countdown timer never resets during lost_gps conditions
  - isNearTheGround() returns true after just 1 second
  - In lost-GPS TERMINATE scenario: aircraft transitions to LANDED state ~9 seconds in, reverting to not-flying branch even if airborne
  - Assessment: Edge case but potentially dangerous
  - Status: Deferred for future fix; noted as existing in MR and TS vehicles too
- **Validation & Testing (Maciej, November 13, 16:41):**
  - Updated hotfix pushed with both lost_gps gate and vz cutoff check restoration
  - Simulated both failure scenario and recovery scenario successfully
  - Spencer Hoehl previously tested regular landing with this code and confirmed it works correctly
  - No failures in re-testing after fixes applied
  - Approach confirmed as safest conservative path forward
- **Scope Applicability:** Sign change requirement and landing timer improvements also need to be applied to multi-rotor and tailsitter aircraft

**Jenkins Tablet Build Configuration (November 13, 2026 - FIXED):**
- **Issue:** Jenkins tablet build was failing due to outdated libcanard fork repository URL
- **Resolution by Ben Busby (November 13, 19:36):** Updated Jenkins build configuration with new libcanard fork URL
- **Prerequisite for Future Maintenance:** bstjenkins user must be added to all required submodules to prevent authentication errors during cloning
- **Status:** Tablet build now operational in Jenkins pipeline

## Projects & Initiatives

**SwiftCore 3.3.0 Release (COMPLETED - November 10, 2026):**
- Master branch release officially announced
- Flight testing completed with multiple failure scenario validation
- Autopilot 3.3 release candidate firmware successfully validated
- GPS-out VTOL hover fix validated, merged, and post-release refined (November 2, 2026; updated November 13, 2026)
- All critical features and bug fixes integrated
- 4+ years of development work consolidated into single release
- **Post-Release Refinements (November 13, 2026):**
  - Lost GPS landing timer issue identified and resolved with conservative gating approach
  - Vertical velocity cutoff check restored to ensure proper landing detection during GPS-loss TERMINATE
  - Sign changes pending application to multi-rotor and tailsitter aircraft
  - Pre-existing isLanded() edge case documented for future fix (affects landing timer reset under GPS loss)
- Status: RELEASED to master branch with critical post-release hotfix refinements

**SwiftTab App Development:**
- Current version: SwiftTab-staging.apk on 3.3 branch
- Issue identified: App crashes when loading saved aircraft params files onto aircraft running SwiftCore AP 3.3 RC firmware (reported October 23, 2026 by Spencer Hoehl)
- Bug report functionality working, reports being received by Ben Busby
- Jenkins build infrastructure updated for proper repository URL and submodule authentication (November 13, 2026)
- Status: May transition to web controller primary UI (April 2026 decision) with legacy Android support

**Failure Scenario Testing (October-November 2026 - COMPLETED for 3.3):**
- Loss of GPS in joystick mode: Appears to be working normally; may have been handset setup issue
- Loss of pitot: Functioning correctly in both fail app and GUI
- Static sensor loss: Expected Level 2 failure behavior confirmed; no issues found
- Mag failures: Showing normal/expected behavior
- Waypoint skipping at higher altitudes: Reproduced by Ali Sulehria (has 20-minute screen recording for review)
- **GPS-out in hover:** Validated with parameter changes, refined with landing timer fixes (November 13, 2026), manual testing confirms proper behavior; fix merged into 3.3.0 with post-release refinements

**S3 Model Aircraft Configuration:**
- Default S3 XML files added by Maciej (October 23, 2026)
- Propulsion model updates completed affecting clog detector parameters
- PSNS smart battery, GNSS, actuator and heated MHP boards supported in 3.3.0 release

**Navy STTR Project (October 27, 2026 - ONGOING):**
- Separate development initiative tracked in local git server (not on primary GitLab)
- Maciej managing repository setup and initial commits
- Status: Repository established and first project pushed to local server

## Action Items & Commitments

**Pending Review/Action:**
- **Jack Elston & Maciej:** Apply sign change from GPS-out hover fix to multi-rotor and tailsitter aircraft (identified November 13, 2026) - Pending implementation
- **Jack Elston & Maciej:** Address pre-existing isLanded() timer reset bug affecting MR and TS vehicles during GPS loss (identified November 13, 2026) - Deferred for future release but documented as potentially dangerous
- **Development Team:** Monitor and document any additional edge cases or behavioral issues with lost-GPS landing scenarios from field operations

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
- Simulator validation used before flight testing (GPS-out hover fix example; landing timer verification November 13)
- Flight test validation critical for landing behavior confirmation with pressure-only vertical velocity estimation

**Vertical Velocity Estimation & Sensor Fusion:**
- Critical for GPS-loss landing detection with pressure sensors alone
- Flight testing has validated <5% error vs. laser-based measurements (S10022 aircraft)
- Proper vz cutoff checks essential for reliable TERMINATE landing transitions

**Clog Detection:**
- Recurring issue with parameters based on incorrect propulsion model
- Trade-off between detection capabilities and operational flexibility
- Selective enablement strategy for rain missions
- Deferred to SwiftCore 4.0 for full implementation with S3 model corrections

**Infrastructure & Repository Management:**
- Evolution of development infrastructure beyond GitLab
- Local git server now supporting additional project repositories (Navy STTR)
- Jenkins build maintenance and authentication configuration for submodules
- Post-release hotfix procedures for Master branch
- Ben Busby managing Jenkins infrastructure updates and submodule access controls

**VTOL Platform Support:**
- Expanding aircraft and hardware platform support (S0-S3 VTOL variants)
- New autopilot hardware (STM32H7, HW 3000, HW 2050)
- Drop launch and air-deployment capabilities
- Transition control improvements
- GPS-loss hover handling refinements with systematic testing across multi-rotor and tailsitter platforms

**Post-Release Maintenance & Code Review:**
- Jack Elston conducting detailed code review of hotfixes post-release
- Identification of edge cases and pre-existing bugs through systematic review
- Conservative decision-making approach for post-release changes (keeping protective gates rather than removing them)
- Thorough testing methodology combining simulation and flight validation

## Important Resources

**XML Configuration Files:**
- SwiftCore AP 3.3 Estimator page XML (parameter configuration)
- S3 model default XML files (added October 23, 2026)
- Payload configuration spreadsheet (flagged for refresh, June 2026)

**Testing Artifacts:**
- Screen recording of waypoint skipping scenario (20 minutes, held by Ali Sulehria)
- SwiftTab-staging.apk crash reports and logs (collected by Ben Busby)
- S10022 flight logs with lost-GPS scenarios (Maciej - laser altimeter reference data vs. pressure-based vz estimates)

**Software Branches/Versions:**
- **SwiftCore 3.3.0** (Master branch - RELEASED November 10, 2026; post-release hotfixes applied November 13, 2026 for landing timer fix)
- SwiftTab-staging.apk (3.3 branch)
- release/3.3.0 (merged GPS-out hover fix with landing timer refinements)
- hotfix/no_gps_vtol_hover_fix (Maciej's original fix, refined by Jack Elston November 2, further refined November 13)
- Lost GPS hover improvement hotfix (pushed to Master November 12, further refined November 13, 2026)

**Infrastructure:**
- Local git server (established October 27, 2026)
- Navy STTR project repository (hosted on local server, not GitLab)
- Jenkins tablet build pipeline (updated November 13, 2026 for proper libcanard fork URL and submodule authentication)

## Recent Activity

**November 13, 2026 - Post-Release Code Review & Hotfix Refinement:**

**Code Review & Issue Identification (Jack Elston, 05:47-05:56 UTC):**
- Jack Elston thoroughly reviewed Maciej's post-release hotfix code
- **Critical Finding:** Removal of landing time gate `(landing_time == -FLT_MAX || (landing_time-now) > 5.0)` creates a problem for lost-GPS landing behavior
- **Concern:** Gate removal impacts multiple failure scenarios; needs investigation before finalizing fix
- **Secondary Finding:** Sign change from GPS-out fix requires application to multi-rotor and tailsitter aircraft (currently only in VTOL)
- **Pre-existing Bug Discovered (concerning):** isLanded() state machine issue:
  - Returns true 8 seconds after landing sequence begins, regardless of actual altitude
  - Landing countdown timer never resets during lost_gps
  - Combined with 1-second isNearTheGround() gate creates edge case where aircraft prematurely reports LANDED while still airborne
  - Particularly dangerous in lost-GPS TERMINATE scenario where aircraft transitions to non-flying state at 9 seconds even if still flying

**Root Cause Analysis & Solution (Maciej, 08:47 UTC):**
- Confirms isLanded() bug exists in multi-rotor and tailsitter too; not critical since v_body usually zero in that condition
- Agrees with Jack's conservative approach: keep landing time gate and add `lost_gps` condition check instead of removing gate
- Rationale: Spencer Hoehl previously tested regular landing with this code and confirmed it works correctly; full gate removal is too risky
- Defers pre-existing isLanded() bug for future fix; acknowledges it's potentially dangerous

**Updated Hotfix & Validation (Maciej, 16:41 UTC - November 13):**
- Pushes new hotfix iteration addressing landing timer issue
- **Root Cause (confirmed through logs):** Removal of `vz < cutoff_velocity` gate during lost_gps prevented proper landing detection in TERMINATE mode
- **Validation Data (from S10022 flights):** Pressure-based vertical velocity estimate highly accurate with <5% error vs. laser altimeter reference measurements
- **Solution:** Restore vz cutoff check while keeping lost_gps gate active
- **Testing Results:**
  - Simulated both failure scenario and recovery successfully
  - Reproduced original failures with old code
  - Re-tested with updated code; no failures observed
- **Conclusion:** Conservative approach with both gates (landing time + vz cutoff + lost_gps condition) is safest path forward

**Jenkins Infrastructure Update (Ben Busby, 19:36 UTC - November 13):**
- Fixed Jenkins tablet build pipeline that was failing due to stale libcanard fork URL
- Updated repository reference to new fork version
- **Important Note for Future Maintenance:** bstjenkins user must be explicitly added to all required submodules to prevent authentication errors during cloning
- Tablet build now operational and deployable through Jenkins

**Overall Context:**
- Demonstrates rigorous post-release code review process catching edge cases not apparent in initial flight testing
- Shows collaborative debugging approach with rapid iteration on fixes based on flight log analysis
- Conservative decision-making prioritizes safety over aggressive optimization
- Infrastructure and deployment pipeline kept current to support ongoing hotfix releases

---

# Summary of Updates

The new data from November 13, 2026 captures critical post-release refinements to the SwiftCore 3.3.0 GPS-out landing handling. Jack Elston's detailed code review identified subtle but potentially dangerous edge cases in the lost-GPS landing timer logic, prompting Maciej to refine the hotfix approach. The team validated pressure-based vertical velocity estimation accuracy through flight logs and opted for a conservative gating strategy that preserves multiple safety checks rather than aggressive simplification. Ben Busby updated Jenkins infrastructure to support ongoing hotfix deployment. This reflects a mature development process balancing rapid iteration with safety-critical control system rigor.