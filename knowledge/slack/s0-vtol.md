# #s0-vtol

## Overview
This channel is primarily used for development and testing of BST's S0 VTOL aircraft - a vertical takeoff and landing aircraft capable of transitioning to forward flight. The channel covers technical discussions, flight testing, hardware debugging, and customer delivery preparation.

Key participants: Jack Elston, Maciej, Sam Hild, Alex Lomis, Joshua Fromm, Ethan, Dan
Activity: High activity with 1412+ messages covering approximately 2+ years of development
Time range: Early development through April 2026 (ongoing project)

## Key Decisions

**Technical Architecture:**
- New S0 autopilots will not have external LED status output channel (early development)
- Motor pivot range: 5 degrees past vertical to 10 degrees below horizontal
- Operating environment: -10C to 40C, up to 20kt gusts
- Ruddervator deflection reduced to +/- 15 degrees based on flight data
- Hub board servo rates: 50Hz for servos, 300Hz for ESCs
- Moving away from current ESC hardware (April 2026)

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

## Projects & Initiatives

**S0-VTOL Development (Spin-Up Phase - April 2026):**
- Status: 20/50 required test flights completed for certification
- Current phase: Re-spinning work with focus on ground testing improvements before resuming flight tests
- Major concern: Recent consecutive transition flight failures cannot be replicated on ground
- Ground testing strategy: Moving toward test methodologies similar to S3 program with independent sensor logging
- S0 VTOL Test Plan created with primary steps and substasks for systematic testing approach (April 17, 2026)
- Motor RPM tracking: Evaluating optimal measurement approach considering feed-forward control implementation for one-motor-out scenarios (April 19, 2026)

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
- Conduct customer training (completed Barbados training)
- Update charge connector and button on interface board
- Coordinate integrated testing setup: work with team to connect independent sensor logging system to autopilot for laptop-based ground testing (April 17, 2026)

**Sam Hild:**
- Configure Remote ID on aircraft before shipment
- Continue thermal testing on crashed S0-VTOL hub board
- Build 3 new aircraft with updated boards for delivery
- Set up independent RPM logging capability using Teensy (April 17, 2026)

**Alex Lomis:**
- Add QC checklist items for future deliveries
- Create new heat sink revision for ESC thermal management
- Evaluate 2m wingspan upgrade option from TJIRC
- Lead ground testing discussion to address replicability gap with flight failures
- Design independent sensor logging system: RPM sensors and potentiometers to log motor outputs separately from autopilot commands (April 17, 2026)
- Create and maintain S0 VTOL Test Plan with primary steps and substasks (April 17, 2026) - plan approved by Maciej
- Consider long-term implications: Evaluate RPM measurement approaches in context of future feed-forward control implementation for one-motor-out scenarios (April 19, 2026)

**Maciej:**
- Complete GPS hover testing before transition flights
- Continue debugging parameter corruption issues
- Develop storage charge calculation spreadsheet
- Coordinate S0-VTOL ground testing plan in conjunction with spin-up (April 17, 2026)
- Ensure parameter backup and prop-off testing before controlled flight testing (April 17, 2026)
- Advise on motor RPM measurement strategy to support eventual feed-forward control on motor RPM difference with appropriate feedback gains (April 19, 2026)
- Work with team to determine optimal failure mitigation approach: either achieve high-confidence ground testing, develop trusted parachute system, or implement pre-flight failure detection (April 19, 2026)

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
- TJIRC - 2m wingspan upgrade option discussion
- Jawstec - parts ordering for assembly
- Harting - power connector specifications
- Digikey - sourcing RPM sensors and potentiometers for ground testing (April 2026)

## Recurring Topics & Themes

**Thermal Management Issues:**
- ESC overheating requiring FET upgrades and heat sink improvements
- Hub board lockup at 120°F (49°C) - fixed with clock source change
- GPS heat sensitivity causing drift - fixed with antenna circuit rework

**Flight Testing Challenges:**
- Two S0-VTOL crashes after transition with power/control loss
- Recent consecutive transition flights showing similar failure patterns that cannot be replicated on ground
- Gap between ground test behavior and in-flight behavior
- Voltage initialization bugs affecting battery state estimation
- Static pressure sensor failures causing landing issues
- Motor thrust offset problems with BLHeli_S ESCs
- Uncertainty over viability of high integral gain motor control in one-motor-out scenarios (April 19, 2026)

**Hardware Reliability:**
- Parameter storage corruption issues requiring interrupt suspension fixes
- GPS hardware failures (modules physically falling apart)
- Current sensor lag affecting magnetometer calibration
- Servo signal compatibility issues with newer Bluebird servos
- ESC firmware/output compatibility concerns leading to hardware transition decision

**Ground Testing Methodology:**
- Need for sinusoidal motor command tests with independent RPM verification
- Desire to log ESC outputs independently of autopilot commands over extended test periods
- Integration of multiple sensor inputs for comprehensive ground validation
- Structured test plan approach to systematically validate S0 VTOL before flight testing resumption
- Motor RPM measurement as foundational design choice affecting long-term control architecture (April 19, 2026)

**Risk Management & Flight Safety (April 2026):**
- Recognition that ground testing alone may be insufficient to prevent in-flight failures
- Need for systematic approach to failure mitigation: high-confidence ground testing, parachute recovery, or failure detection before flight
- Importance of not resuming flights without confidence in failure prevention or mitigation strategy

## Important Resources

**Technical Specifications:**
- Max payload: 1 lb target
- Sprint speed: 85 knots
- Max altitude: 18,000 ft operational, 12,000 ft launch/land
- Max wind: 15 m/s for takeoff/landing
-