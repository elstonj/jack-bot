# #s0-vtol

## Overview
This channel is primarily used for development and testing of BST's S0 VTOL aircraft - a vertical takeoff and landing aircraft capable of transitioning to forward flight. The channel covers technical discussions, flight testing, hardware debugging, and customer delivery preparation.

Key participants: Jack Elston, Maciej, Sam Hild, Alex Lomis, Joshua Fromm, Ethan, Dan
Activity: High activity with 1412 messages covering approximately 2+ years of development
Time range: Early development through recent upgrade discussions (2m wingspan proposal)

## Key Decisions

**Technical Architecture:**
- New S0 autopilots will not have external LED status output channel (early development)
- Motor pivot range: 5 degrees past vertical to 10 degrees below horizontal
- Operating environment: -10C to 40C, up to 20kt gusts
- Ruddervator deflection reduced to +/- 15 degrees based on flight data
- Hub board servo rates: 50Hz for servos, 300Hz for ESCs

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

## Projects & Initiatives

**S0-VTOL Development:**
- Status: 20/50 required test flights completed for certification
- Major milestone: First successful transition flight (Dec 23)
- Current focus: Reliability improvements after 2 crashes during transitions
- Aggressive testing schedule: 10 clean flights by end of August

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

**Sam Hild:**
- Configure Remote ID on aircraft before shipment
- Continue thermal testing on crashed S0-VTOL hub board
- Build 3 new aircraft with updated boards for delivery

**Alex Lomis:**
- Add QC checklist items for future deliveries
- Create new heat sink revision for ESC thermal management
- Evaluate 2m wingspan upgrade option from TJIRC

**Maciej:**
- Complete GPS hover testing before transition flights
- Continue debugging parameter corruption issues
- Develop storage charge calculation spreadsheet

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

## Recurring Topics & Themes

**Thermal Management Issues:**
- ESC overheating requiring FET upgrades and heat sink improvements
- Hub board lockup at 120°F (49°C) - fixed with clock source change
- GPS heat sensitivity causing drift - fixed with antenna circuit rework

**Flight Testing Challenges:**
- Two S0-VTOL crashes after transition with power/control loss
- Voltage initialization bugs affecting battery state estimation
- Static pressure sensor failures causing landing issues
- Motor thrust offset problems with BLHeli_S ESCs

**Hardware Reliability:**
- Parameter storage corruption issues requiring interrupt suspension fixes
- GPS hardware failures (modules physically falling apart)
- Current sensor lag affecting magnetometer calibration
- Servo signal compatibility issues with newer Bluebird servos

## Important Resources

**Technical Specifications:**
- Max payload: 1 lb target
- Sprint speed: 85 knots
- Max altitude: 18,000 ft operational, 12,000 ft launch/land
- Max wind: 15 m/s for takeoff/landing
- Endurance: ~55-60 minutes estimated, potentially 90 minutes with wing upgrade

**Component Part Numbers:**
- Power connector: 21004515-06 with waterproof cap 806-00028-00
- Button: 1241.1102.7098 (IP65 rated)
- Light pipe: 51513010250F
- LED: 732-5662-1-ND

**Performance Data:**
- Hover power: 56A current draw (781W power consumption)
- Forward flight efficiency: 127W at 18 m/s (actual ~20.5 m/s)
- Aircraft weight: 2550g AUW (170g reduction from previous version)

## Recent Activity

**Wing Upgrade Discussion:**
- Alex Lomis presented 2m wingspan upgrade from TJIRC
- 33% more wing area, higher aspect ratio (14 vs 10)
- Potential 90-minute flight time for meteorology payloads
- Portability concerns with 2m wingspan vs backpack transport

**Test Program Status:**
- 20 of 50 required test flights completed
- Missing critical tests: 45+ minute flights with wind data, speed validation, battery limit testing
- High wind testing (>20 mph) not yet completed

**Equipment Integration:**
- Vantage gimbal integration discussion (EO, IR, ultra low light + 3-axis gimbal)
- Manual flight capability consideration for future versions
- Naming convention discussion for upgraded version