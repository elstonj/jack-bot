# #s0-vtol

## Overview
This channel is primarily used for development and testing of BST's S0 VTOL aircraft - a vertical takeoff and landing aircraft capable of transitioning to forward flight. The channel covers technical discussions, flight testing, hardware debugging, and customer delivery preparation.

Key participants: Jack Elston, Maciej, Sam Hild, Alex Lomis, Joshua Fromm, Ethan Domagala, Dan, Ben Busby
Activity: High activity with 1420+ messages covering approximately 2+ years of development
Time range: Early development through July 20, 2026 (ongoing project)

## Key Decisions

**Technical Architecture:**
- New S0 autopilots will not have external LED status output channel (early development)
- Motor pivot range: 5 degrees past vertical to 10 degrees below horizontal
- Operating environment: -10C to 40C, up to 20kt gusts
- Ruddervator deflection reduced to +/- 15 degrees based on flight data
- Hub board servo rates: 50Hz for servos, 300Hz for ESCs
- Moving away from current ESC hardware (April 2026)
- DShot protocol running at 300 baud on test rig (May 1, 2026)

**Flight Operations:**
- Battery threshold for VTOL landing: 3V/cell based on performance data
- Hover capability limited to 8 minutes (1 minute with thermal constraints)
- COA altitude reduced from 2000' to 700' at RC Field, maintained 2000' at Heil Ranch

**Customer Deliveries:**
- S0 systems will not include handsets, only tablet joysticks for manual mode
- Decision to leave aircraft in Barbados rather than shipping back ($1600 vs $360 cost)

**Hardware Fixes:**
- Sam switched from MSI to HSI clock source to fix heat sensitivity lockup issues
- RTK heat sensitivity fixed with circuit updates (L: 27uH, R: 10 Ohm, C: 47pF)

**Flight Testing Strategy (April 2026):**
- Motor RPM measurement approach: Prioritize scheme supporting long-term feed-forward control on motor RPM difference with smaller feedback gains on yaw rate controller rather than simple independent sensor logging (April 19, 2026)
- Failure risk mitigation: Team must choose between high-confidence ground testing, trusted parachute system, or pre-flight failure detection capability before resuming flights (April 19, 2026)
- S0-VTOL ground testing to be aligned with S3 methodology (April 28, 2026)

**Ground Testing & Crash Analysis (April 29 - May 2, 2026):**
- Crash autopilot code version identified: 0xf9eb3e6c (April 29, 2026)
- Baseline established for comparing test rig behavior against crash conditions
- Sinusoidal loop testing will require custom firmware (small change at output stage)
- Instrumentation approach prioritized: PWM sensors to be deployed first, followed by remaining instrumentation components (Hall effect rotation sensors, couplers, optical RPM sensors)
- S3 ground testing methodology includes 15-minute run warm-up as QC-like test to verify hardware/mechanical integrity (Joshua Fromm recommendation, April 30, 2026)
- Visual observations alone insufficient for crash failure diagnosis; instrumentation logging required for meaningful data (April 30, 2026)

**DShot Telemetry (May 1, 2026):**
- PWM-to-UART board may no longer be required for instrumentation given DShot 300 implementation on test rig
- DShot telemetry decoding library available in Autopilot/shared/devices/actuators directory

**Crash Aircraft Failure Pattern (May 2, 2026):**
- Aircraft experienced back-to-back failures with different characteristics: first failure showed ~30% throttle command shift in PWM mode (manageable), second failure showed same issue but worse after switching to DShot protocol
- Potential ESC/PWM scaling issue identified that may cause command shifting
- DShot protocol attempted as mitigation for the underlying scaling issue but made failure worse
- Sam conducting oscilloscope testing to determine if cause is related to the identified issue (May 2, 2026)

**Test Rig Motor Failure & Investigation (May 5-6, 2026):**
- Brief motor command freeze (~1 second) followed by all three motor shutdown observed during overnight test run (May 5, 2026)
- Ailerons and tail surfaces continued operating during motor shutdown event
- Motor shutdown potentially caused by switched output to ESC from battery on autopilot (Jack Elston's initial hypothesis, May 5, 2026)
- Investigation findings (May 6, 2026):
  - Hub board was sending 0s on DShot protocol; logs showed three >3-second gaps from AP starting at 3.5 hours
  - Motors shut down at first gap in packets at approximately 3 hours 25 minutes
  - Hub board still receiving power and outputting previous PWM during all gaps
  - Autopilot gaps appear to be logging issues (coinciding with missing IMU data), not actual command transmission failures
  - Pivot command bug identified by Maciej and fixed with updated binary; pivots were receiving commands but at much slower rate than other surfaces
  - Pivot slow motion caused by gyro drift in attitude estimator after magnetometer failure at ~65 minutes into log; pivots attempting to hold heading
  - Channel 2 occasional values exceeding 2000µs limit (2001-2005µs) determined to be normal behavior for some surfaces on aircraft, not an error
  - Magnetometer issues resolved after replacing SD card with fresh card
  - ESC behavior verified stable: tested ESC with constant throttle (1200µs) and simulated errors over entire input range - no unexpected halts or failures observed

**Pivot Servo Issues (May 7, 2026):**
- Left front pivot stopped moving during test; one previous crash correlated with stuck pivoter
- Pivot PWM range for left front: min 2080µs, center 1985µs, max 1010µs
- Sam Hild identified PWM "shift" issue: signal appears corrupted/attenuated rather than changed in value
- Initial hypothesis: Voltage-related issue, possibly faulty level shift circuit

**Parachute/Ejection System (May 13, 2026):**
- Team considering Peregrine CO2 ejection device (8g/12g option) from Apogee Rockets as parachute deployment mechanism
- Joshua Fromm indicated team comfort with loading own pyro charges using small amounts of black powder

**Testing Approach Strategy (May 19, 2026):**
- Sam Hild pursuing dual strategy: both in-flight logging combined with parachute system deployment rather than choosing between them (May 19, 2026)
- Focus: Continue ground testing while also preparing logging hardware for flight testing

**Critical Hardware Issues Identified & Resolved (May 25-26, 2026):**
- Sam Hild identified and characterized multiple distinct hardware issues on test rig (May 25, 2026):

  **Issue 1 - Left Motor Failure (May 25, 2026):**
  - Left motor went out without recovery; ESC error chime heard; no autopilot errors except RID
  - All other surfaces/motors commanded correctly; BSTCAN packets reporting correctly
  - DShot commanding valid 0x0000 commands (passing CRC)
  - Neither motor disable/enable, hub board power cycle, CAN reconnect, nor surface replug resolved issue
  
  **Issue 2 - Rear Motor RPM Shift (May 25, 2026):**
  - Rear motor running ~800 RPM faster than other two motors despite identical autopilot commands and tablet ranges
  - Strange RPM ramp-up on motor start with sine wave shifting upward during startup
  - Observed in manual log review (not yet in DShot command logs due to logging difficulty)
  - Only seen on rear motor so far but may occur on others

**CAN Bus & Motor Control Issues - Root Causes & Resolutions (May 26, 2026):**
- Comprehensive issue analysis and fixes applied to test rig (Sam Hild, May 26, 2026):
  
  **CAN Bus Issues (RESOLVED):**
  - Missing termination fixed on test rig

**Flight Testing Expansion (July 20, 2