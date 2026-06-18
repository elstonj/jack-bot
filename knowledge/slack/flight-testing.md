# #flight-testing

## Overview

The #flight-testing channel serves as Black Swift Technologies' primary hub for coordinating flight test operations, troubleshooting aircraft and payload issues, and tracking firmware/software development across their fleet of fixed-wing (S-series), multirotor (E2, Flamewheel), and VTOL (S0, S1-VTOL, S3) platforms.

**Key Participants:** Maciej (lead flight testing/analysis), Jack Elston (firmware development), Joshua Fromm (QA/component sourcing), Ben Busby (tablet/GCS software), Nate (videography/pilot), Alex Lomis (field operations/media/pilot), Sam Hild (Remote ID integration/test pilot), Dan Prendergast (autopilot/control systems/operations), Danny Troke (data management), Ethan Domagala (pilot), Beck Cotter (operations support), Paige Smith (media/video curation), Meredith Needham (logistics/administrative support), Sunny Slope Sod Farm (external airspace contact/CU training partner), Chris & Kevin (external clients/stakeholders), Christoph & Angie (internal stakeholders), Dan H. (external contact/AUVSI show), Ken Jochim (BAS airfield operator)

**Activity Level:** Extremely high — 5,600+ messages across June 2020 through June 2026. Daily operations with multiple aircraft flights, rapid issue turnaround, continuous firmware iterations, and intensive VTOL transition testing. Current activity (June 2026) shows ongoing flight test operations with multiple payload integration flights planned, Kansas (KS) demo preparation, and high operational tempo with logistics coordination.

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
- **April 25, 2026:** E-MASS project training data collection scheduled; confirmed two relatively charged E2 batteries available for mission; waypoint plan phases configured for sequential loading during flight to maximize training data capture across one or two flights
- **April 27, 2026:** S3-MASS approved for first full autonomous flight after successful hover tests; motor_out_yaw branch deferred from S3_mass_model (integral gain tuning concerns and motor failure mitigation strategy requires further development; rudder damping gains require aircraft-specific tuning vs. S0 baseline)
- **April 28, 2026:** S3-MASS successful first full autonomous flight completed; S1-22 landing profile optimization scheduled for concurrent testing to inform S3 future flights
- **April 29, 2026:** S3 prioritized for continued tuning flights with S10022 and S-MASS as lower priority backup options; S3 requires Jack Elston and Alex Lomis availability for mission success; E-MASS controller binary expected from external team around noon with afternoon E2 testing contingent on simulation validation passing
- **April 30, 2026:** S1-22 pitch fix flight testing approved; takeoff pitch trim adjusted to 5 and 10 degrees for evaluation; Remote ID (RID) update scheduled for S3-MASS testing pending firmware readiness
- **May 1, 2026:** S10022 flight completed successfully with identified vibration on hover and RID baud rate issue requiring investigation and correction
- **May 4, 2026:** S1-22 flight testing contingent on wind conditions; winds dropped below 10 mph, Alex Lomis confirmed available for operations; Remote ID warnings identified in both flight and ground modes during recent testing — Sam Hild deprioritized RID fix vs. S0-VTOL work but committed to investigating
- **May 7, 2026:** S3-MASS flight testing scheduled for May 8, 2026 with 9am departure; favorable weather forecasted (small rain chance at 3pm); Maciej leading with S3 to be transported in RAV; video documentation requested with Mavic drone
- **May 8, 2026:** E-MASS payload testing shifted from Sunny Slope Sod Farm to model airfield location; Jack Elston to lead when returning from current operations; E-MASS controller showing drift issues in simulation between waypoints (65-80% completion before failure) but with slower failure rate and good pre-failure warning indicators for manual intervention
- **May 11, 2026:** S3-MASS flight testing scheduled for May 12, 2026; Maciej planned 1 tuning flight (~35 minutes) + potential second flight for extra time-on-float (TOF) testing if tuning progresses well; 5-6 S1-22 flights possible with additional personnel; promotional video capture planned with new nose cone; E-MASS testing deferred to Thursday (May 14-15)
- **May 12, 2026:** 
  - S3-MASS flight testing plan confirmed: 2 flights after CU S2 training operations complete (9am start time approved)
  - 4 additional S3 flights scheduled for Friday Fly day (May 17)
  - S1-VTOL failure testing stretch goal approved for week: flight terminate, pitot cover left on, lost GPS transition, lost mags, etc.
  - Concurrent dual-aircraft operations approved: CU training with S2 at Sod Farm (Dan Prendergast and Nate leading) while Maciej runs S1-22 and S3 flights on separate channel
  - S1-22 pitch up maneuver code change (wait until off ground) and rotor dump forward timing adjustment approved for testing
  - S2 flight plan parameters: CU S2 `Limits` tab `Flight Path` maximum value verified/set to 9 degrees
  - Alex Lomis confirmed to provide video/AV equipment for Friday operations
  - Log collection from CU flights prioritized for battery performance analysis during takeoff climbouts
- **May 14, 2026:** S1-VTOL failure testing comprehensive test plan approved for May 15 flight operations; includes mag failure landing (gyro integration), loss of laser on landing, low battery flight terminate with transition, joystick transition, lost GPS, and loss of engine in flight. Loss of pitot and loss of pitot + GPS deferred due to simulation crashes; Jack Elston approved conducting tests at higher altitude to minimize takeover risk. S1-VTOL failure testing to be developed into customer training scenario after validation.
- **May 14, 2026:** Emergency procedures training expansion approved by Dan Prendergast and Jack Elston; proposal to include 4G negative dive and loss-of-system scenarios in standard customer training curriculum
- **May 15, 2026:** S1-22 flight testing extended beyond 1-hour baseline
- **June 17, 2026:** Flight operations cancelled due