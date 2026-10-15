# #flight-testing

## Overview

The #flight-testing channel serves as Black Swift Technologies' primary hub for coordinating flight test operations, troubleshooting aircraft and payload issues, and tracking firmware/software development across their fleet of fixed-wing (S-series), multirotor (E2, Flamewheel), and VTOL (S0, S1-VTOL, S3) platforms.

**Key Participants:** Maciej (lead flight testing/analysis/firmware development), Jack Elston (firmware development/debugging support), Joshua Fromm (QA/component sourcing), Ben Busky (tablet/GCS software), Nate (videography/pilot), Alex Lomis (field operations/media/pilot), Sam Hild (Remote ID integration/test pilot/magnetometer troubleshooting), Dan Prendergast (autopilot/control systems/operations), Danny Troke (data management), Ethan Domagala (pilot/tablet operator), Beck Cotter (operations support), Paige Smith (media/video curation), Meredith Needham (logistics/administrative support), Scott (equipment/field operations), Stefan (payload data processing - CH4/CO2), Spencer Hoehl (QA/maintenance workflow coordination/process formalization lead/flight readiness review automation lead/test pilot), Sunny Slope Sod Farm (external airspace contact/CU training partner), Chris & Kevin (external clients/stakeholders), Christoph & Angie (internal stakeholders), Dan H. (external contact/AUVSI show), Ken Jochim (BAS airfield operator), Boulder Emergency Squad (external visitor/stakeholder), NRL/Naval Research Laboratory (external client/payload testing), Matt at NRL (external contact/gimbal payload lead/battery support), Brian (external stakeholder/SOCOM demo operator), ERAU (external partner - isarra project), NREL (external contact - equipment/batteries), Eryan (ERAU contact - E2 testing/SMM data evaluation)

**Activity Level:** Extremely high — 5,600+ messages across June 2020 through October 2026. Daily operations with multiple aircraft flights, rapid issue turnaround, continuous firmware iterations, and intensive VTOL transition testing. October 12-13, 2026 activity shows S1-VTOL transition testing, S-series aircraft QC operations, hover control refinement, and post-flight analysis with focus on IAS sensor diagnostics and control mode troubleshooting.

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

### Firmware & Software
- **October 12, 2026:** Internal AP repo pull-based approach approved for firmware distribution; packaging method for customer deployment deferred for later decision
- **October 13, 2026:** S10021 (Xtend) transition flight conducted on existing binary from previous week (no new binary required)

---

## Projects & Initiatives

### S1-VTOL Transition Testing & Flight Readiness
- **Status (October 13, 2026):** Active flight testing phase
- **Key aircraft:** S10005, S10021 (Xtend), S10022
- **Recent activities:**
  - S10021 transition flight (Oct 13): Takeoff → orbit → land + joystick hover, performed