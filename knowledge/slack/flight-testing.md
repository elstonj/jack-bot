# #flight-testing

## Overview

The #flight-testing channel serves as Black Swift Technologies' primary hub for coordinating flight test operations, troubleshooting aircraft and payload issues, and tracking firmware/software development across their fleet of fixed-wing (S-series), multirotor (E2, Flamewheel), and VTOL (S0, S1-VTOL, S3) platforms.

**Key Participants:** Maciej (lead flight testing/analysis/firmware development), Jack Elston (firmware development/debugging support), Joshua Fromm (QA/component sourcing), Ben Busky (tablet/GCS software), Nate (videography/pilot), Alex Lomis (field operations/media/pilot), Sam Hild (Remote ID integration/test pilot/magnetometer troubleshooting), Dan Prendergast (autopilot/control systems/operations), Danny Troke (data management), Ethan Domagala (pilot/tablet operator), Beck Cotter (operations support), Paige Smith (media/video curation), Meredith Needham (logistics/administrative support), Scott (equipment/field operations), Stefan (payload data processing - CH4/CO2), Spencer Hoehl (QA/maintenance workflow coordination/process formalization lead/flight readiness review automation lead/test pilot), Ali Sulehria (flight sim operator/tester), Sunny Slope Sod Farm (external airspace contact/CU training partner), Chris & Kevin (external clients/stakeholders), Christoph & Angie (internal stakeholders), Dan H. (external contact/AUVSI show), Ken Jochim (BAS airfield operator), Boulder Emergency Squad (external visitor/stakeholder), NRL/Naval Research Laboratory (external client/payload testing), Matt at NRL (external contact/gimbal payload lead/battery support), Brian (external stakeholder/SOCOM demo operator), ERAU (external partner - isarra project), NREL (external contact - equipment/batteries), Eryan (ERAU contact - E2 testing/SMM data evaluation)

**Activity Level:** Extremely high — 5,600+ messages across June 2020 through November 2026. Daily operations with multiple aircraft flights, rapid issue turnaround, continuous firmware iterations, and intensive VTOL transition testing. November 2026 activity shows S1-22 estimator gain optimization testing executed with follow-up S2 VTOL preflight troubleshooting identified and resolved; S2 flight test successfully conducted November 6; continued transition flight campaign ongoing.

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
- **April 25, 2026:** E-MASS project training data collection scheduled; confirmed two relatively charged E2 batteries available for mission; waypoint plan phases configured for sequential loading during flight to maximize training data capture
- **April 27, 2026:** S3-MASS approved for first full autonomous flight after successful hover tests; motor_out_yaw branch deferred from S3_mass_model (integral gain tuning concerns and motor failure mitigation strategy requires further development)
- **April 28, 2026:** S3-MASS successful first full autonomous flight completed; S1-22 landing profile optimization scheduled for concurrent testing
- **April 29, 2026:** S3 prioritized for continued tuning flights with S10022 and S-MASS as lower priority backup options; E-MASS controller binary expected with afternoon E2 testing contingent on simulation validation
- **April 30, 2026:** S1-22 pitch fix flight testing approved; takeoff pitch trim adjusted to 5 and 10 degrees for evaluation; Remote ID (RID) update scheduled for S3-MASS testing
- **May 1, 2026:** S10022 flight completed successfully with identified vibration on hover and RID baud rate issue requiring investigation
- **May 4, 2026:** S1-22 flight testing contingent on wind conditions; Remote ID warnings identified in both flight and ground modes — Sam Hild deprioritized RID fix vs. S0-VTOL work
- **May 7, 2026:** S3-MASS flight testing scheduled for May 8 with 9am departure; Mavic drone video documentation requested
- **May 8, 2026:** E-MASS payload testing shifted from Sunny Slope Sod Farm to model airfield location; Jack Elston to lead; controller showing drift issues in simulation (65-80% completion before failure)
- **May 11, 2026:** S3-MASS flight testing scheduled for May 12; Maciej planned 1 tuning flight (~35 minutes) + potential second flight for time-on-float testing; 5-6 S1-22 flights possible with additional personnel
- **May 12, 2026:**
  - S3-MASS flight testing plan confirmed: 2 flights after CU S2 training operations (9am start)
  - 4 additional S3 flights scheduled for Friday Fly day (May 17)
  - S1-VTOL failure testing stretch goal approved: flight terminate, pitot cover left on, lost GPS transition, lost mags, etc.
  - Concurrent dual-aircraft operations approved: CU training with S2 at Sod Farm while Maciej runs S1-22 and S3 flights on separate channel
  - S1-22 pitch up maneuver code change and rotor dump forward timing adjustment approved
- **September 15, 2026:** S20009 QC flight completed and passed; aircraft approved for operations (SW v3028, HW v2050, code revision 4fb65e96)
- **September 17, 2026:** ByLight external client test flight planned for September 18 at Sunny Slope Sod Farm
- **October 12, 2026:** S1-VTOL midpoint hover readjustment approved; yaw control confirmed improved after manual hover testing by Spencer Hoehl and Ethan Domagala; aircraft cleared for flight testing October 13; pitot tube issue resolved and approved for deployment
- **October 12, 2026:** Internal AP repo pull-based approach approved for firmware distribution; packaging method for customer deployment deferred for later decision
- **October 13, 2026:** S10021 (Xtend) transition flight conducted on existing binary from previous week (no new binary required)
- **October 15, 2026:** S10011 passed flight readiness review and approved for flight testing with new firmware (S1-VTOL platform)
- **October 16, 2026:** `feature/commands_fix` branch approved for merge per code review; release candidate testing campaign structured into four phases (sim testing, QC flights on all platforms, fail testing, S2/E2 QC flights)
- **October 28, 2026:** Clogged pitot calibration approved to proceed in sustained 10.5-13.5 knot winds (winds do not affect calibration data validity); S10022 parameter updates for loss of IAS approved (NO_IAS_A = -1.1932, NO_IAS_B = 1.5509); Flamewheel to be deployed for additional lost GPS failure mode testing observation
- **October 29, 2026:** Release candidate testing focus shifted away from S20003 and E20006 flights; instead prioritizing failure test data review; S20003 and E20006 flight preparation deferred to early next week (conditional on S3 hover testing readiness)
- **November 3, 2026:** S1-22 (serial 0x70246dd9) multi-stage testing protocol approved for estimator gain optimization and GPS aborted takeoff forward velocity issue validation
- **November 4, 2026 (AM):** S1-22 hover tests completed successfully; Spencer Hoehl cleared to proceed to step #5 of multi-stage testing protocol (GPS aborted takeoff test after accelerometer gain restoration)
- **November 6, 2026:** S1-22 new firmware binary (hash: 0x02510451) approved for deployment; strategy clarified — new binary scheduled for final flight session rather than mid-campaign; Spencer Hoehl authorized to conduct additional transition flights if battery remains above 55% after primary tests
- **November 6, 2026:** S2 VTOL GCS connection issue resolved; S2 flight test successfully conducted with personnel support from field operations team; additional transition flight testing scheduled contingent on battery state

### Release Candidate Testing
- **October 28-29, 2026:** Release Candidate 3.3 failure testing campaign intensive validation phase:
  - **October 28 Flights Completed:**
    - S10022: QC flight redo and pitot calibration flight both completed with nominal performance
    - FW0001 & FW0002 (Flamewheel): Four failure mode flights each completed testing HW_Fault, Lost GPS, Lost Mags, Lost Static Pressure, and Lost GPS scenarios
  - **October 29 Status Update:** All failure test logs uploaded; detailed results to be compiled in RC 3.3 testing spreadsheet
  - **Identified Minor Code Changes Required:**
    1. Lost GPS dubins path recomputation issue: Aircraft performs sharp turn after returning from lost GPS (observed 1 of 4 Lost GPS tests) — may require code adjustment
    2. Full GPS loss on VTOL climbout: Aircraft flies forward aggressively instead of maintaining zero attitude and drifting with wind — root cause investigation pending
  - **Fail_App Enhancement Requests Identified for Future Versions:**
    - BAD_GPS error currently simulates complete loss of GPS; real-world BAD_GPS has low PDOP zone (3-5) which causes discrepancy in aircraft behavior and rogue lateral motion on Flamewheel tests
    - Motor power loss error feature needed (currently only testable via SwiftTab motor disable, doesn't test AP sensors like real power loss would)
- **November 6, 2026:** RC 3.3 Phase 4 S2/E2 QC flights progressing; S2 VTOL flight test successfully completed (GCS connection issue resolved)

---

## Projects & Initiatives

### Release Candidate 3.3 Testing Campaign (October 2026 — Ongoing)
**Status:** Phase 4 S2/E2 QC flights in progress; S2 flight test successfully conducted November 6; detailed analysis and validation continuing

**Scope:** Structured four-phase testing:
1. ✅ Simulation testing (completed for commands_fix feature branch)
2. ✅ QC flights on all platforms (S10022, S10021, S10011, and others — substantially completed; S2 VTOL QC flight conducted Nov 6)
3. ✅ Failure testing (lost GPS, lost mags, lost static pressure, HW faults — data review and analysis completed Oct 29)
4. **In Progress:** S2/E2 QC flights (S2 flight test completed Nov 6; E2 flights pending)

**October 28-29 Activities:**
- S10022: Completed redo QC flight with new actuator board firmware (nominal performance) + pitot calibration flight (nominal, multiple cruise speeds tested: 16, 17, 19 m/s with full orbits at 1665m and 1700m)
- FW0001 & FW0002 (Flamewheels): Four flights each documenting failure mode responses (HW_Fault on climbout, Lost GPS on climbout, Lost Mags during flying mode, Lost Static Pressure during hover, Lost GPS during flying mode)
- All flight logs uploaded Oct 29; detailed analysis in "Release Candidate 3.3 Testing" spreadsheet
- Results show nominal performance with two identified edge cases requiring investigation

**November 6 Activities:**
- S2 VTOL flight test successfully conducted (GCS connection issue from Nov 4 resolved)
- Transition flight testing approved to continue if battery remains above 55% after primary tests
- New firmware binary (0x02510451) scheduled for final flight session

**Results Summary:** All FAIL tests passed with nominal behavior; two edge cases identified (Lost GPS dubins path recomputation, VTOL GPS loss on climbout response); fail_app enhancement requests logged for future development. Phase 4 actively progressing with S2 VTOL testing complete.

### S1-VTOL Flight Testing Campaign (October-November 2026 — Ongoing)
**Status:** Late-stage development; multi-stage testing protocol execution in progress; transition flight testing active

**Recent Milestones:**
- October 12: Midpoint hover readjustment approved; yaw control improved; pitot tube issue resolved
- October 13: S10021 (Xtend) transition flight conducted successfully
- October 15: S10011 passed flight readiness review; approved for testing with new firmware
- October 28-29: Continued flight readiness; S10022 loss of IAS parameters updated
- November 3: S1-22 multi-stage testing protocol approved
- November 4 (AM): S1-22 hover tests (steps #1-3) completed successfully; acceleration gain tuning validated; cleared to proceed to step #5
- November 6: S1-22 firmware binary updated (0x02510451); transition flight testing campaign authorized to continue with battery above 55%

**Key Platforms:**
- **S1-22 (serial 0x70246dd9)** — Active optimization testing; multi-stage protocol execution in progress:
  1. ✅ Manual hover test (completed Nov 3)
  2. ✅ Switch "Acc" gain to 0.00033 (completed Nov 3)
  3. ✅ Manual hover test (~30s) validation (completed Nov 4 AM)
  4. ✅ Switch gain back to 0.0033 (completed Nov 4 AM)
  5. **In Progress:** GPS aborted takeoff test to validate forward velocity fix; proceeding with new firmware binary (0x02510451) scheduled for final flight session
  6. Pending: Standard VTOL QC flight with second battery (contingent on step #5 passing)
  7. Authorized: Additional transition flights if battery >55% after primary tests
  
- S10021 (Xtend) — Transition testing complete; flight-ready
- S10011 — Approved for testing post-FRR; flight-ready

**Objective:** Resolve forward velocity issue observed during GPS aborted takeoff by optimizing accelerometer gain on estimator; validate fix and conduct extended transition flight testing before proceeding to standard QC flight with full battery complement.

### S2 VTOL Flight Test Operations (November 4-6, 2026 — Ongoing)
**Status:** GCS connection issue resolved November 4-6; flight test successfully completed November 6; continued operations authorized

**Issue Resolution (November 4-6):**
- November 4, 14:03-16:33: Complex preflight issues identified (UI corruption, aircraft loss from GCS display, network connection failures)
- November 4, 16:33: Jack Elston and Spencer Hoehl initiated investigation; suspected dual-GCS or competing radios
- **November 6 Morning:** Issue resolved; root cause analysis completed (indicates successful troubleshooting by team)
- **November 6, 15:33:** Spencer Hoehl acknowledged external personnel support for successful S2 flight test (note to two team members with taco emojis)

**Flight Test Results (November 6):**
- S2 VTOL flight test successfully completed with nominal performance
- New firmware binary (0x02510451) deployment validated
- Personnel support from external field operations team acknowledged
- Transition flight testing authorized to continue based on battery state (>55% threshold)

**Objective:** Validate S2 VTOL firmware performance as part of RC 3.3 Phase 4 testing; complete S2 QC flight requirements for release candidate validation.

---

## Action Items & Commitments

### Immediate (November 6, 2026 — Ongoing)
- **Spencer Hoehl:** Continue S1-22 multi-stage testing protocol execution with new firmware binary (0x02510451)
  - Execute GPS aborted takeoff test (step #5) to validate forward velocity fix
  - Conduct additional transition flights if battery remains above 55% after primary tests
  - Deploy second battery for standard VTOL QC flight upon step #5 completion
- **S1-22 Flight Testing Team:** Maintain transition flight campaign momentum with updated firmware; monitor battery state and optimize flight scheduling
- **E-MASS Project Team (Jack Elston Lead):** Prepare E2 QC flights for RC 3.3 Phase 4 completion (E20006 and other platforms pending)

### Short-term (November 6-7, 2026)
- **Spencer Hoehl & Field Operations Team:** Continue S2 VTOL operations post-successful flight test; execute any additional transition or validation flights as required
- **Flight Testing Coordination:** Monitor S1-22 battery state and transition flight progression; optimize scheduling for both S1-22 and S2 testing

### Ongoing (October 29 — November 6, 2026)
- **Maciej & Engineering Team:** Investigate two edge cases from failure testing:
  1. Lost GPS dubins path recomputation issue (sharp turn after GPS recovery) — assess code change requirement
  2. VTOL full GPS loss on climbout behavior (forward flight vs. zero attitude hold) — root cause analysis
- **Maciej:** Continue firmware integration oversight; monitor estimator gain optimization testing results on S1-22
- **Flight Testing Team:** Complete Phase 4 (S2/E2 QC flights) of RC 3.3 campaign; finalize E2 flight testing
- **Engineering Team:** Identify future fail_app enhancement requirements (BAD_GPS low PDOP simulation, motor power loss error) for roadmap planning

### Ongoing Core Operations
- **Maciej:** Lead flight operations prioritization and firmware integration; oversee S1-22 estimator optimization campaign and firmware deployment
- **Spencer Hoehl:** Continue RC 3.3 QC flight execution and documentation; coordinate aircraft readiness scheduling; drive S1-22 and S2 VTOL transition flight testing
- **Flight Testing Team:** Execute Phase 4 (S2/E2 QC flights) of RC 3.3 campaign to completion
- **Sam Hild:** Remote ID integration and testing (currently deprioritized relative to other VTOL work)

---

## Client & External References

- **CU (University of Colorado):** Training operations partner; S2 VTOL training flights conducted at Sunny Slope Sod Farm in May 2026
- **ByLight:** External client; test flight conducted September 18, 2026 at Sunny Slope Sod Farm
- **Sunny Slope Sod Farm:** Airspace and operations partner; host location for CU training and ByLight testing
- **NRL (Naval Research Laboratory):** External client for payload testing; gimbal and battery support coordination with Matt
- **ERAU (Embry-Riddle Aeronautical University):** Partner on isarra project; E2 testing and SMM data evaluation with Eryan
- **NREL:** Equipment and battery support contacts

---

## Recurring Topics & Themes

### Firmware & Parameter Testing
- Continuous QC flight iterations with new firmware builds
- Parameter optimization for control systems (pitch, yaw, IAS loss response, accelerometer gain estimation)
- Version tracking and deployment across fleet (APK staging/release versioning)
- Estimator calibration and tuning workflows (e.g., accelerometer gain adjustments for GPS/INS integration)
- Multi-stage validation protocols for parameter changes before full deployment
- Strategic firmware deployment timing (final flight session deployment for validation and extended testing)

### Failure Mode Validation
- Systematic testing of error responses: HW faults, lost GPS, lost magnetometers, lost static pressure, lost IAS
- Error classification system tracked in shared Master spreadsheet (Level 1-3 with automatic/manual response types)
- Level 3 errors trigger automatic actions (emergency descent/land) with override capability via secondary action selection
- Identified simulation-to-reality gaps in fail_app (BAD_GPS lacking PDOP degradation simulation, motor power loss testing limitations)
- Edge case identification and root cause analysis for code change assessment

### GCS & Software Troubleshooting
- SwiftTab preflight UI stability and data connection integrity
- Radio/GCS conflict detection and resolution (dual-GCS scenarios identified and resolved)
- Flight plan synchronization between tablet and aircraft
- Network initialization and connection state management
- Systematic debugging protocols for connection failures

### Weather Considerations
- Wind condition assessment for specific test types (e.g., pitot calibration unaffected by 10+ knot winds)
- Flight scheduling contingent on weather windows
- Sustained vs. gusting wind impacts on aircraft capability

### Multi-Platform Operations
- Concurrent testing of fixed-wing (S1-22, S2), VTOL (S1-VTOL, S3-MASS), and multirotor (E2, Flamewheels)
- Coordinated operations with separate communication channels for airspace deconfliction
- Resource allocation across priority aircraft and test phases
- Transmitter availability coordination (e.g., T14SG Futaba tracking for S10005, S10022, FW0001)
- Field operations team support and personnel resource coordination

### Documentation & Data Management
- Systematic logging of flight results in shared Google Sheets tracking documents
- Flight log uploads with structured performance notes
- Parameter and firmware version tracking for reproducibility
- Data review and analysis protocols for failure test campaigns
- Binary version hash tracking (e.g., 0x02510451 for S1-22 Nov 6 deployment)

### Estimator & Control System Optimization
- Accelerometer gain (Acc gain) tuning for improved GPS/INS integration
- Manual hover validation following parameter adjustments
- GPS aborted takeoff scenario testing for forward velocity behavior validation
- Multi-stage testing protocols to isolate and validate specific parameter effects
- Firmware deployment strategy aligned with multi-stage test progression

### Battery State Management
- Battery threshold monitoring (55% cutoff for extended transition flight authorization)
- Battery conditioning and charging protocols for sequential flight operations
- Battery state tracking across multiple test flights and extended campaigns
- Contingent flight authorization based on battery remaining capacity

---

## Important Resources

### Tracking & Documentation
- **Release Candidate 3.3 Testing Spreadsheet:** <https://docs.google.com/spreadsheets/d/11gdvYa65F_zSwpsObmi1FMEAguVonhIpXeoHTrQaeP8/edit?usp=sharing> — Failure mode test results for FW0001, FW0002, S10022, and other platforms; updated Oct 29 with comprehensive flight log data; Phase 4 S2/E2 flights in progress (S2 completed Nov 6)
- **Error Classification Master Spreadsheet:** <https://docs.google.com/spreadsheets/d/1zalkQfdGo6Y4M7P1ZSqfJZ_AmIS_GbK6q-DSee9jGdo/edit?gid=375746326#gid=375746326> — Level 1-3 error types and response behaviors (auto vs. manual)

### Firmware & Controllers
- **S1-22 (serial 0x70246dd9) Estimator Gain Parameters (Nov 3-6, 2026):**
  - Test Acc (Accelerometer) gain: 0.00033 (tested Nov 3, validated Nov 4 AM with successful hover)
  - Baseline Acc gain: 0.0033 (restored Nov 4 AM; deployed with new binary Nov 6)
  - New firmware binary hash: **0x02510451** (deployed Nov 6 for final flight session)
  - Testing objective: Resolve forward velocity issue during GPS aborted takeoff
  - Current status: Steps 1-4 completed; step #5 (GPS aborted takeoff test) in progress with updated firmware; additional transition flights authorized if battery >55%
- **S10022 Loss of IAS Parameters (Oct 28, 2026):** NO_IAS_A = -1.1932, NO_IAS_B = 1.5509
- **S1-22 Loss of IAS Parameters (Oct 28, 2026):** NO_IAS_A = -1.1932, NO_IAS_B = 1.5509 (same as S10022)
- **S20009 Approved Build:** SW v3028, HW v2050, code revision 4fb65e96
- **S10020 Baseline:** Build hash bf20b0b7
- **RC 3.3 Feature Branch:** `feature/commands_fix` (approved for merge)

### Hardware & Equipment
- **T14SG Futaba Transmitter:** Controls S10005, S10022, and FW0001; Jack Elston has custody as of Oct 29

### COA & Airspace
- **Airspace Blocks:** Two 2500' COA blocks submitted (RC field and Caribou ranch); practical line-of-sight altitude limits: 1500-2000'

---

## Recent Activity

### November 4, 2026 — S1-22 Estimator Gain Testing Progression & S2 VTOL Troubleshooting

**Morning (07:25-08:39):**
- **Maciej confirmed completion of initial hover tests (07:25):** S1-22 hover tests from November 3 completed successfully; Spencer Hoehl cleared to proceed from step #5 of multi-stage testing protocol
- **Spencer Hoehl acknowledged (08:39):** Confirmed readiness to proceed with GPS aborted takeoff test (step #5)

**Afternoon (14:03-16:33):**
- **Spencer Hoehl reported S2 VTOL preflight issues (14:03):**
  - Issue: Complex UI and connection corruption during landing plan configuration; detailed symptoms documented
  - Aircraft responded to landing plan setup but UI became corrupted (orbit labels lost, lines disconnected)
  - "Clear all flight plans" command rejected by aircraft
  - Post-refresh: Aircraft completely disappeared from SwiftTab GCS display despite power remaining on
  - Power cycle unsuccessful; 10+ minute power-off reset unsuccessful
  
- **Diagnostic Phase (14:05-16:33):**
  - **Maciej (14:05):** Suspected competing GCS or dual aircraft on same radio loop
  - **Spencer Hoehl (14:06):** Provided flight log for analysis; confirmed no other aircraft/GCS active during preflight
  - **Jack Elston (16:31):** Agreed with dual-GCS hypothesis; offered to perform detailed debugging this evening or tomorrow
  - **Spencer Hoehl (16:33):** Committed to one final troubleshooting attempt before end of day; will report results for Jack's analysis if issue persists

**Status at End of Nov 4:** S1-22 multi-stage testing proceeding to step #5 (GPS aborted takeoff); S2 VTOL operations temporarily halted pending GCS issue resolution. Investigation team mobilized for detailed debugging.

### November 6, 2026 — S1-22 Firmware Deployment & S2 VTOL Flight Test Success

**Morning (13:23-13:30):**
- **Spencer Hoehl requested firmware binary confirmation (13:23):** Asked Maciej for hash of new S1-22 binary
- **Maciej confirmed (13:30):** Binary hash = **0x02510451**

**Mid-day (14:47-15:34):**
- **Spencer Hoehl clarified firmware deployment strategy (14:47):** Questioned reasoning for deploying new binary on final flight vs. mid-campaign; requested clarification on Maciej's intent
  - Follow-up question: Can additional transition flights continue if battery remains above 55% after primary tests?

- **Spencer Hoehl reported successful S2 VTOL operations (15:33-15:34):**
  - Thanked team member U01511MEQ90 for help with S2 flight test (Nov 6)
  - Thanked team member U0CC405PC6R for field operations support Nov 5-6
  - Indicated successful completion of S2 VTOL flight test with GCS issue resolved
  - Transition flight testing campaign proceeding

**Status at End of Nov 6:**
- S1-22: New firmware binary (0x02510451) deployed; multi-stage testing progressing with updated code; authorized for extended transition flights if battery >55%
- S2 VTOL: GCS connection issue successfully resolved; flight test completed successfully; field operations team support acknowledged; continued operations authorized
- RC 3.3 Phase 4: S2 VTOL QC flight completed (Nov 6); E2 flights pending
- Overall Testing: Release candidate testing campaign progressing well through final validation phases

---

**Data updated through November 6, 2026, 15:34 UTC**