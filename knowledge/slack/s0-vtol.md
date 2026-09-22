# #s0-vtol

## Overview
This channel is primarily used for development and testing of BST's S0 VTOL aircraft - a vertical takeoff and landing aircraft capable of transitioning to forward flight. The channel covers technical discussions, flight testing, hardware debugging, and customer delivery preparation.

Key participants: Jack Elston, Maciej, Sam Hild, Alex Lomis, Joshua Fromm, Ethan Domagala, Dan, Ben Busby, Kareem, Spencer Hoehl, Cory Dixon, Dan Prendergast, Meredith Needham, Kevin

Activity: High activity with 1500+ messages covering approximately 2+ years of development
Time range: Early development through August 28, 2026 (ongoing project)

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

**Power Switch System Issues (August 27-28, 2026):**
- Theory: RC circuit on AP power switch has wrong components or ones outside tolerance range (Maciej, requires verification by Sam Hild)
- Known boot issue: Power switch gets stuck on power-down and keeps triggering watchdog, causing continuous resets on bench (persistent firmware issue identified by Sam Hild)
- Timing check: Button timing appears acceptable (~1/2 second shorter than expected)
- Separate issue: One aircraft's AP power switch doesn't respond to button interrupt despite switch acting as expected (also identified by Sam Hild)
- EEPROM replacement considered but Sam reports low historical success rate
- Unclear why behavior varies: some resets continuous, others shut down too early

**Battery Configuration (August 27-28, 2026):**
- **Current Configuration: 4s3p** (quad 3-cell configuration) maintained for motor/ESC compatibility (confirmed by Jack Elston and Alex Lomis)
- **Testing Results: 4s2p** on Reliance RS50 cells behaves nicely (Alex Lomis)
- Future consideration: potential move to 5-6s system with larger motors and 1.5m→2m wing expansion for increased payload versatility (requires customer requirements determination - Alex Lomis flagged as important for future product sizing)

**Flight Operations:**
- Battery threshold for VTOL landing: 3V/cell based on performance data
- Hover capability limited to 8 minutes (1 minute with thermal constraints)
- COA altitude reduced from 2000' to 700' at RC Field, maintained 2000' at Heil Ranch
- **Ground Testing Before Flight (August 20, 2026):** Manual hover tests required out back before field flights to validate surface trim and GPS lock

**Customer Deliveries:**
- S0 systems will not include handsets, only tablet joysticks for manual mode
- Decision to leave aircraft in Barbados rather than shipping back ($1600 vs $360 cost)
- **ISARRA Delivery Priority (July 29, 2026):** S0-VTOL at ISARRA now top priority for ocean calibration data; two aircraft required for ERAU/ISARRA delivery (absolutely required), plus one for BST testing
- **ISARRA Flight Week: August 30 - September 3, 2026** with target shipping by early week
- **Delivery Timing - August 26, 2026:** Two S0 aircraft to ship for Friday (next day air) or Saturday (2nd day air) delivery to ERAU. Hotel shipping arranged for Saturday delivery. S0s require test flight before shipment.
- **Backup Shipping Plan:** BST's own S0 can ship if needed for ISARRA calibration day, with ERAU deliverables following Monday
- **Test Plan for ISARRA (August 17, 2026):**
  - 50 flights total (aggressive target given single aircraft and time constraints)
  - 5 flights >45 minutes collecting wind data
  - Validate min and max speeds
  - Late aborted transition (>12 m/s IAS)
  - Aborted landing during transition
  - Flight to min safe battery with hover testing below cutoff
  - Test in >20 mph winds

**Production Scaling:** Building multiple S0-VTOL aircraft in parallel; target 3 aircraft ready (S01005, S10020, and additional airframe) by late August 2026

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

### S0-VTOL Flight Testing Campaign & Delivery (August-September 2026)
**Current Status:** Active flight testing with S01005 as primary test aircraft; production scaling complete with 3 aircraft; critical focus on resolving autopilot power switch issues before ISARRA deployment (August 30 - September 3, 2026)

**Critical Issues Blocking ISARRA Deployment (August 27-28, 2026):**
- **Power Switch Boot Loop Issue (Primary - under investigation):**
  - Affects at least one autopilot stack
  - Power switch stuck on power-down, continuously triggering