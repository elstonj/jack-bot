# #s0-vtol

## Overview
This channel is primarily used for development and testing of BST's S0 VTOL aircraft - a vertical takeoff and landing aircraft capable of transitioning to forward flight. The channel covers technical discussions, flight testing, hardware debugging, and customer delivery preparation.

Key participants: Jack Elston, Maciej, Sam Hild, Alex Lomis, Joshua Fromm, Ethan Domagala, Dan, Ben Busby, Kareem, Spencer Hoehl, Cory Dixon, Dan Prendergast
Activity: High activity with 1500+ messages covering approximately 2+ years of development
Time range: Early development through August 25, 2026 (ongoing project)

## Key Decisions

**Technical Architecture:**
- New S0 autopilots will not have external LED status output channel (early development)
- Motor pivot range: 5 degrees past vertical to 10 degrees below horizontal
- Operating environment: -10C to 40C, up to 20kt gusts
- Ruddervator deflection reduced to +/- 15 degrees based on flight data
- Hub board servo rates: 50Hz for servos, 300Hz for ESCs
- Moving away from current ESC hardware (April 2026)
- DShot protocol running at 300 baud on test rig (May 1, 2026)
- **ESC Strategy Shift (August 17, 2026):** After persistent issues with new ESC protocol causing motor startup jitter and unreliable startups on rear motor, team pivoted to reverting T-Motor ESC (proven on S1-VTOL with 120+ test flights) running in PWM mode for S0 testing and delivery
- **Autopilot Hardware Improvements (August 20-24, 2026):** 
  - Fixed multiple sensor initialization issues: IMU SPI data reads optimized (DIV2→DIV4), register access corruption fixed
  - Magnetometer chip gradually failing; added code allowing boot without mag (sets HW_FAULT/NO_MAGS error) rather than complete failure
  - Fixed EEPROM serial number handling to survive odd EEPROM behavior
  - GPS warm-start battery discharging issue persists but not critical
  - SD card corruption after very long duration runs likely hardware defect

**Flight Operations:**
- Battery threshold for VTOL landing: 3V/cell based on performance data
- Hover capability limited to 8 minutes (1 minute with thermal constraints)
- COA altitude reduced from 2000' to 700' at RC Field, maintained 2000' at Heil Ranch
- **Ground Testing Before Flight (August 20, 2026):** Manual hover tests required out back before field flights to validate surface trim and GPS lock

**Customer Deliveries:**
- S0 systems will not include handsets, only tablet joysticks for manual mode
- Decision to leave aircraft in Barbados rather than shipping back ($1600 vs $360 cost)
- **ISARRA Delivery Priority (July 29, 2026):** S0-VTOL at ISARRA now top priority for ocean calibration data; two aircraft required for ERAU/ISARRA delivery (absolutely required), plus one for BST testing
- **ISARRA Flight Week: August 30 - September 3, 2026** with target shipping by early week (August 24 decision to potentially split: S01005 earlier, ERAU S0s early next week)
- **Test Plan for ISARRA (August 17, 2026):**
  - 50 flights total (aggressive target given single aircraft and time constraints)
  - 5 flights >45 minutes collecting wind data
  - Validate min and max speeds
  - Late aborted transition (>12 m/s IAS)
  - Aborted landing during transition
  - Flight to min safe battery with hover testing below cutoff
  - Test in >20 mph winds
- **Production Scaling:** Building multiple S0-VTOL aircraft in parallel; target 3 aircraft ready (S01005, S10020, and additional airframe) by late August 2026

**Hardware Fixes & Resolutions:**
- Sam switched from MSI to HSI clock source to fix heat sensitivity lockup issues
- RTK heat sensitivity fixed with circuit updates (L: 27uH, R: 10 Ohm, C: 47pF)
- **Connector/Mechanical Issue (August 5, 2026):** S01005 boot loop caused by tape around nose causing tight fit that bent board/connectors; EEPROM write times still slow (hardware stress)
- **Test Setup vs. Hardware Issues (August 18, 2026):** Motor RPM shift and cutout issues on test stand resolved as test setup problem, not hardware defect
- **Pivot Servo Issue Resolution (August 5-6, 2026):** Left front pivot slow motion caused by gyro drift in attitude estimator after magnetometer failure; replaced SD card, fixed magnetometer issues
- **ESC Parameter Tuning (August 17, 2026):** Extensive SFOC parameter tuning attempted but no consistent improvement found for motor startup jitter; decided to revert to proven T-Motor ESC rather than continue troubleshooting new ESC

**Flight Testing Strategy (April 2026):**
- Motor RPM measurement approach: Prioritize scheme supporting long-term feed-forward control on motor RPM difference with smaller feedback gains on yaw rate controller rather than simple independent sensor logging (April 19, 2026)
- Failure risk mitigation: Team must choose between high-confidence ground testing, trusted parachute system, or pre-flight failure detection capability before resuming flights (April 19, 2026)
- S0-VTOL ground testing to be aligned with S3 methodology (April 28, 2026)

**Parachute/Ejection System (May 13, 2026):**
- Team considering Peregrine CO2 ejection device (8g/12g option) from Apogee Rockets as parachute deployment mechanism
- Joshua Fromm indicated team comfort with loading own pyro charges using small amounts of black powder
- Decided on dual strategy: in-flight logging combined with parachute system deployment (May 19, 2026)

## Projects & Initiatives

### S0-VTOL Flight Testing Campaign (August 2026)
**Current Status:** Active flight testing with S01005 as primary test aircraft
- **August 24-25, 2026:** S01005 successfully completed full transition with minor GPS issues and multiple smooth transitions documented
- **Flight Performance (August 25, 2026):** 7 flights flown from ~95% to 40% battery; landing still manageable at 40% but takeoff near saturation at just under 50% (flying older Samsung cells; new RS50 cells expected to perform significantly better at <40%)
- **Parallel Airframe Build-up:** Sam Hild bringing up 3 additional S0-VTOL autopilot stacks; at least 1-2 expected ready by August 25-26 for integration into new airframes
- **Ground Testing Protocol:** 30-second joystick hovers with rest between flights to prevent overheating; manual hover tests out back before field flights; target 20% battery minimum before landing
- **Avionics Swap (August 24, 2026):** Plan to swap S1-VTOL avionics into S01005 for continued testing
- **Next Phase:** Sod Farm testing campaign targeting 15-20 transition flights on S01005 by August 25-26

### S1-VTOL Testing
**Current Status:** Supporting S0 development with proven platform
- 120+ successful flights on T-Motor ESC in PWM mode
- Successfully tested lost GPS and lost mags recovery code (both result in auto land)
- Being used as avionics donor and to validate new firmware before S0 deployment

### Multiple S0-VTOL Airframe Production
**Current Status:** Building to 3 aircraft total by late August 2026
- S01005: Primary test aircraft, now flying transition tests
- S10020: Secondary aircraft being prepared (hub board updates needed, ESC reversion to T-Motor)
- Third aircraft: In assembly, needs avionics and final checkout
- **Challenge:** Finding 3 autopilot boards with working sensor combinations is major bottleneck

### New ESC Integration
**Status:** Attempted but abandoned; reverted to proven solution
- Initial plan: Replace T-Motor ESCs with new protocol ESCs for better reliability
- Issue encountered (August