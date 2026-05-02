# #s0-vtol

## Overview
This channel is primarily used for development and testing of BST's S0 VTOL aircraft - a vertical takeoff and landing aircraft capable of transitioning to forward flight. The channel covers technical discussions, flight testing, hardware debugging, and customer delivery preparation.

Key participants: Jack Elston, Maciej, Sam Hild, Alex Lomis, Joshua Fromm, Ethan, Dan
Activity: High activity with 1412+ messages covering approximately 2+ years of development
Time range: Early development through May 1, 2026 (ongoing project)

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

**Ground Testing & Crash Analysis (April 29 - May 1, 2026):**
- Crash autopilot code version identified: 0xf9eb3e6c (April 29, 2026)
- Baseline established for comparing test rig behavior against crash conditions
- Sinusoidal loop testing will require custom firmware (small change at output stage)
- Instrumentation approach prioritized: PWM sensors to be deployed first, followed by remaining instrumentation components (Hall effect rotation sensors, couplers, optical RPM sensors)
- S3 ground testing methodology includes 15-minute run warm-up as QC-like test to verify hardware/mechanical integrity (Joshua Fromm recommendation, April 30, 2026)
- Visual observations alone insufficient for crash failure diagnosis; instrumentation logging required for meaningful data (April 30, 2026)

**DShot Telemetry (May 1, 2026):**
- PWM-to-UART board may no longer be required for instrumentation given DShot 300 implementation on test rig
- DShot telemetry decoding library available in Autopilot/shared/devices/actuators directory

## Projects & Initiatives

**S0-VTOL Development (Spin-Up Phase - April-May 2026):**
- Status: 20/50 required test flights completed for certification
- Current phase: Intensive ground testing with instrumentation improvements before resuming flight tests
- Recent ground testing status: No obvious CAN issues detected in latest test results; maximum command delay was 19.5ms; no Fletcher errors occurred (April 30, 2026)
- Ground testing focus: Preparing sinusoidal loop test with appropriate instrumentation; evaluating DShot 300 telemetry for output signal logging (May 1, 2026)
- Next steps: Order instrumentation components (ESC telemetry loggers, eRPM sensors, PWM loggers, optical RPM sensors for motors; PWM loggers and Hall effect rotation sensors for servos) while continuing current test regime
- Major concern: Consecutive transition flight failures cannot be replicated on ground - instrumentation critical for identifying root cause
- Baseline comparison: Test rig behavior now being compared against crash conditions with matched autopilot code version (0xf9eb3e6c)
- **Pending Decision (May 1, 2026):** Whether to prioritize parachute system integration and resume flight testing if CAN termination issue (S01006) identified as likely crash cause, versus continuing extended ground testing phase

**S1-20 Aircraft Reference Data:**
- Reference aircraft completed 213 total flights with 10.5 hours combined flight time over past year
- 172 transition flights totaling 10.2 hours of forward flight (April 30, 2026)

**ADONIS Project:**
- Contract deliverable: Flight testing required by March 24
- Hardware: No S0 deliveries after flights, team retains aircraft
- Priority shifted to simulation interface setup with Gateworks board

**Customer Deliveries:**
- ERAU: Two S0-VTOLs scheduled
- Barbados: One S0-VTOL delivered, training conducted by Jack
- Multiple QC issues identified requiring process improvements

## Action Items & Commitments

**Jack Elston:**
- Complete 50 flight test program for S0-VTOL certification
- Provided DShot telemetry decoding library reference (May 1, 2026)
- Offered to develop output signal logger for AP if needed (May 1, 2026)
- Coordinate integrated testing setup with instrumentation logging priority

**Sam Hild:**
- Execute ground testing with current setup before deploying advanced instrumentation (April 30, 2026)
- Preserve crashed autopilot code version during ground testing iterations
- Deploy PWM sensors as minimum instrumentation requirement before proceeding with more complex tests (April 30, 2026)
- Investigating DShot version on test rig and implications for instrumentation strategy (May 1, 2026)
- Build 3 new aircraft with updated boards for delivery
- Set up independent RPM logging capability

**Maciej:**
- Generate sinusoidal firmware version for crashed S0 autopilot code if requested by Sam (offered April 30, 2026)
- Continue parameter corruption debugging
- Coordinate S0-VTOL ground testing plan in conjunction with spin-up
- Lead ground testing methodology alignment between S0 and S3 programs
- **Investigating S01006 CAN termination issue as potential cause of recent crash (May 1, 2026)**

**Alex Lomis:**
- Manage instrumentation documentation in Asana task (April 30, 2026)
- Instrumentation specification includes: ESC telemetry + eRPM + PWM logger + optical RPM for motors; PWM logger, Hall effect rotation sensors, couplers for servos; ESC telemetry for power data
- Coordinate ordering of instrumentation components with supply chain (April 30, 2026)
- Design and implement sensor logging system to enable data-driven failure analysis
- Confirmed DShot 300 running on test rig (May 1, 2026)

**Joshua Fromm:**
- Contribute S3 ground testing methodology insights to S0 program (April 30, 2026)
- Recommend 15-minute warm-up run as QC-like test for hardware/mechanical verification

## Client & External References

**Customers:**
- Embry Riddle Aeronautical University (ERAU) - receiving two aircraft
- Barbados deployment - one aircraft delivered, training completed
- Stanford team - provided aerodynamic model for research

**Partners/Competitors:**
- TruWeather - developing competing weather multi-rotor with AFWERX Phase II funding
- Teledyne FLIR - discussing ATR (Automatic Target Recognition) integration
- Airlogix GOR platform - competitive intelligence reference
- Vantage gimbal integration from Vesper quad rotor project

**Suppliers:**