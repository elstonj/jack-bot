# #flight-testing

## Overview

The #flight-testing channel serves as Black Swift Technologies' primary hub for coordinating flight test operations, troubleshooting aircraft and payload issues, and tracking firmware/software development across their fleet of fixed-wing (S-series), multirotor (E2, Flamewheel), and VTOL (S0, S1-VTOL, S3) platforms.

**Key Participants:** Maciej (lead flight testing/analysis/firmware development), Jack Elston (firmware development/debugging support), Joshua Fromm (QA/component sourcing), Ben Busky (tablet/GCS software), Nate (videography/pilot), Alex Lomis (field operations/media/pilot), Sam Hild (Remote ID integration/test pilot/magnetometer troubleshooting), Dan Prendergast (autopilot/control systems/operations), Danny Troke (data management), Ethan Domagala (pilot/tablet operator), Beck Cotter (operations support), Paige Smith (media/video curation), Meredith Needham (logistics/administrative support), Scott (equipment/field operations), Stefan (payload data processing - CH4/CO2), Spencer Hoehl (QA/maintenance workflow coordination/process formalization lead/flight readiness review automation lead/test pilot), Ali Sulehria (flight sim operator/tester), Sunny Slope Sod Farm (external airspace contact/CU training partner), Chris & Kevin (external clients/stakeholders), Christoph & Angie (internal stakeholders), Dan H. (external contact/AUVSI show), Ken Jochim (BAS airfield operator), Boulder Emergency Squad (external visitor/stakeholder), NRL/Naval Research Laboratory (external client/payload testing), Matt at NRL (external contact/gimbal payload lead/battery support), Brian (external stakeholder/SOCOM demo operator), ERAU (external partner - isarra project), NREL (external contact - equipment/batteries), Eryan (ERAU contact - E2 testing/SMM data evaluation)

**Activity Level:** Extremely high — 5,600+ messages across June 2020 through October 2026. Daily operations with multiple aircraft flights, rapid issue turnaround, continuous firmware iterations, and intensive VTOL transition testing. October 2026 activity shows active release candidate firmware testing campaign with focus on failure mode testing, QC flights on all platforms, and pitot calibration operations.

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

### Release Candidate Testing
- **October 28, 2026:** Release Candidate 3.3 failure testing campaign continues:
  - S10022: QC flight redo and pitot calibration flight both completed with nominal performance
  - Flamewheel (FW0001, FW0002): Four failure mode flights each completed testing HW_Fault, Lost GPS, Lost Mags, Lost Static Pressure, and Lost GPS scenarios
  - Results documented in shared "Release Candidate 3.3 Testing" tracking spreadsheet

---

## Projects & Initiatives

### Release Candidate 3.3 Testing Campaign (October 2026 — Ongoing)
**Status:** Active failure mode and performance validation phase
**Scope:** Structured four-phase testing:
1. Simulation testing (completed for commands_fix feature branch)
2. QC flights on all platforms (S10022, S10021, S10011, various others — in progress)
3. Failure testing (lost GPS, lost mags, lost static pressure, HW faults — actively running on Flamewheels)
4. S2/E2 QC flights (pending)

**Recent Activity (Oct 28):**
- S10022: Completed redo QC flight with new actuator board firmware (nominal performance) + pitot calibration flight (nominal, multiple cruise speeds tested: 16, 17, 19 m/s with full orbits at 1665m and 1700m)
- FW0001 & FW0002 (Flamewheels): Four flights each documenting failure mode responses (HW_Fault on climbout, Lost GPS on climbout, Lost Mags during flying mode, Lost Static Pressure during hover, Lost GPS during flying mode)
- Results tracked in "Release Candidate 3.3 Testing" spreadsheet

**Next Steps:** 
- Continue Flamewheel lost GPS failure testing with in-person observation by Maciej
- Deploy additional Flamewheel for expanded lost GPS scenario testing
- S1-22 loss of IAS parameter updates to be tested
- Phase 4 S2/E2 QC flights pending

### S1-VTOL Flight Testing Campaign (October 2026 — Ongoing)
**Status:** Mid-to-late stage development, cleared for flight testing
**Recent Milestones:**
- October 12: Midpoint hover readjustment approved; yaw control improved; pitot tube issue resolved
- October 13: S10021 (Xtend) transition flight conducted successfully
- October 15: S10011 passed flight readiness review; approved for testing with new firmware
- October 28: S1-22 loss of IAS parameters provided for implementation; pitot calibration and QC flights progressing

**Key Platforms:**
- S10021 (Xtend) — active transition testing
- S10011 — approved for testing post-FRR
- S1-22 — continued QC and parameter optimization flights

---

## Action Items & Commitments

### Immediate (October 28-29, 2026)
- **Spencer Hoehl:** Update S10022 parameters for loss of IAS first thing morning (NO_IAS_A = -1.1932, NO_IAS_B = 1.5509) — *Committed Oct 28*
- **Maciej & Team:** Deploy Flamewheel(s) for additional lost GPS failure testing with in-person observation — *Directed Oct 28*

### Ongoing
- **Spencer Hoehl:** Continue RC 3.3 failure mode testing documentation; upload flight logs for all test flights to shared tracking spreadsheet
- **Maciej:** Lead flight operations prioritization and firmware integration; monitor failure testing results
- **Flight Testing Team:** Complete Phase 3 (failure testing) and Phase 4 (S2/E2 QC flights) of RC 3.3 campaign
- **Sam Hild:** Remote ID integration and testing (currently deprioritized relative to other VTOL work)

---

## Client & External References

- **CU (University of Colorado):** Training operations partner; S2 VTOL training flights conducted at Sunny Slope Sod Farm in May 2026
- **ByLight:** External client; test flight scheduled September 18, 2026 at Sunny Slope Sod Farm
- **Sunny Slope Sod Farm:** Airspace and operations partner; host location for CU training and ByLight testing
- **NRL (Naval Research Laboratory):** External client for payload testing; gimbal and battery support coordination with Matt
- **ERAU (Embry-Riddle Aeronautical University):** Partner on isarra project; E2 testing and SMM data evaluation with Eryan
- **NREL:** Equipment and battery support contacts

---

## Recurring Topics & Themes

### Firmware & Parameter Testing
- Continuous QC flight iterations with new firmware builds
- Parameter optimization for control systems (pitch, yaw, IAS loss response)
- Version tracking and deployment across fleet (APK staging/release versioning)

### Failure Mode Validation
- Systematic testing of error responses: HW faults, lost GPS, lost magnetometers, lost static pressure, lost IAS
- Error classification system tracked in shared Master spreadsheet (Level 1-3 with automatic/manual response types)
- Level 3 errors trigger automatic actions (emergency descent/land) with override capability via secondary action selection

### Weather Considerations
- Wind condition assessment for specific test types (e.g., pitot calibration unaffected by 10+ knot winds)
- Flight scheduling contingent on weather windows
- Sustained vs. gusting wind impacts on aircraft capability

### Multi-Platform Operations
- Concurrent testing of fixed-wing (S1-22, S2), VTOL (S1-VTOL, S3-MASS), and multirotor (E2, Flamewheels)
- Coordinated operations with separate communication channels for airspace deconfliction
- Resource allocation across priority aircraft and test phases

### Documentation & Data Management
- Systematic logging of flight results in shared Google Sheets tracking documents
- Flight log uploads with structured performance notes
- Parameter and firmware version tracking for reproducibility

---

## Important Resources

### Tracking & Documentation
- **Release Candidate 3.3 Testing Spreadsheet:** <https://docs.google.com/spreadsheets/d/11gdvYa65F_zSwpsObmi1FMEAguVonhIpXeoHTrQaeP8/edit?usp=sharing> — Failure mode test results for FW0001, FW0002, and other platforms
- **Error Classification Master Spreadsheet:** <https://docs.google.com/spreadsheets/d/1zalkQfdGo6Y4M7P1ZSqfJZ_AmIS_GbK6q-DSee9jGdo/edit?gid=375746326#gid=375746326> — Level 1-3 error types and response behaviors (auto vs. manual)

### Firmware & Controllers
- **S10022 Loss of IAS Parameters (Oct 28, 2026):** NO_IAS_A = -1.1932, NO_IAS_B = 1.5509
- **S20009 Approved Build:** SW v3028, HW v2050, code revision 4fb65e96
- **S10020 Baseline:** Build hash bf20b0b7
- **RC 3.3 Feature Branch:** `feature/commands_fix` (approved for merge)

### COA & Airspace
- **Airspace Blocks:** Two 2500' COA blocks submitted (RC field and Caribou ranch); practical line-of-sight altitude limits: 1500-2000'

---

## Recent Activity

### October 28, 2026 — Release Candidate 3.3 Failure Testing & Pitot Calibration

**Morning:**
- Spencer Hoehl asked about wind conditions for clogged pitot calibration (sustained 10.5 kt, gusting to 13.5 kt)
- Maciej confirmed wind is acceptable for pitot calibration data
- Spencer Hoehl requested error type documentation for tablet screen display (red/yellow indicators)
- Maciej directed to Master spreadsheet error classification reference (Level 1-3 auto/manual responses)
- Spencer Hoehl clarified Level 3 error behavior: automatic action with override capability via secondary action selection

**Afternoon/Evening:**
- Spencer Hoehl uploaded comprehensive flight logs:
  - **S10022:** 
    - Flight 1 (QC Redo): All nominal with new actuator board firmware
    - Flight 2 (Pitot Calibration): All nominal; varied cruise speeds (16, 17, 19 m/s) with full orbits at 1665m and 1700m
  - **FW0001 & FW0002 (Flamewheels):** Four flights each testing:
    - HW_Fault on climbout
    - Lost GPS on climbout
    - Lost Mags during flying mode
    - Lost Static Pressure during hover
    - Lost GPS during flying mode
  - Results documented in "Release Candidate 3.3 Testing" tracking spreadsheet
- Spencer Hoehl thanked external visitor for flight test participation
- **Maciej provided S1-22 loss of IAS controller page parameters:** NO_IAS_A = -1.1932, NO_IAS_B = 1.5509
- **Maciej directed deployment of Flamewheel(s) for additional lost GPS testing with in-person observation**
- **Spencer Hoehl committed to updating S10022 parameters first thing in the morning**

**Status:** RC 3.3 testing progressing through Phase 3 (failure mode validation); all tested flights showing nominal or documented error responses; pitot calibration and QC flights on schedule; Flamewheel lost GPS testing to expand scope with enhanced observation.