# Task 03 - Phase II Status Report

## Document Metadata
- Type: Status Report (presentation format)
- Client/Agency: United States Air Force (AF)
- Program/Solicitation: SBIR Phase II, Contract FA8730-20-C-0021
- Date: 2020-08-17 (created/modified)
- BST Products/Systems Referenced: S0, S1 (atmospheric sounding UAS variants)
- Key Personnel: Dr. Jack Elston (PI)

## Executive Summary
This Phase II status report documents BST's progress on an atmospheric sounding UAS under Air Force contract. Task 02 (prototype construction and testing) was completed with a first article vehicle successfully built and flight-tested, validating design parameters and control authority. Task 03 (user interface development and meteorological data collection) was 50% complete at report time, with deployment planned for October 2020 at the Southern Great Plains (SGP) site following COVID-related delays from August.

## Technical Approach

**Airframe Development:**
- Constructed first article prototype with quick-disconnect wing and fully articulated tail section
- Incorporated ~2:1 thrust ratio for VTOL capability
- Updated design based on flight testing: moved wing to accommodate new battery, repositioned motor pods for desired center of thrust
- Modified components for center of gravity optimization after receiving parts

**Avionics & Control:**
- Developed and tested complete wiring harness with sensor integration (dynamic pressure, static pressure, GPS, magnetometer, temperature)
- Built simulation model (S0) to develop transition algorithms for VTOL operations
- Firmware development for vertical takeoff/landing and transition control
- Pitch control authority achieved ~200°/s² pitch acceleration with tail surface deflection ranges validated
- Control tuning targets: roll/pitch delay <0.4s with RMS error <3°, altitude RMS error <1m, position RMS error <1.5m

**Software & Operations:**
- Completed user interface with flight planning/execution software
- Developed data interface and quick QC analysis software
- Vertical profile creation/modification capability
- Created comprehensive test cards for both local (Sod Farm) and deployment (SGP) sites

## Products & Capabilities Described

**S0/S1 (Atmospheric Sounding UAS):**
- Vertical takeoff and landing capable vehicle
- Forward flight endurance validated through battery draw testing and extrapolation
- Demonstrated stability in ~20 knot winds
- Highly responsive control through manual handset
- Hand-launch capable
- Quick-disconnect wing for field operations
- Fully articulated tail section for VTOL control authority

## Use Cases & Applications

**Mission Types:**
- Atmospheric profiling at fixed locations (vertical profiles)
- Wind measurement via radiosonde-equivalent flights at multiple altitudes and airspeeds (1, 2, 4, 6 m/s target speeds)
- Tower comparison flights to validate against reference measurements
- Circular, racetrack, and star pattern flight profiles for spatial wind evaluation
- Deployment site: Southern Great Plains (SGP) ARM facility managed by DOE

**Sampling Parameters:**
- Target altitude: 400m (local testing), 60m (SGP tower comparison)
- Target airspeed: 18 m/s
- Sustained loiter capability: 8+ minutes at altitude during circular patterns
- Multiple diameter circles: 50m, 100m, 150m, 200m

## Key Results

**Task 02 Completion (100%):**
- First article successfully constructed with all components assembled and tested
- Flight testing validated: stability, hand launch, endurance matching requirements, control authority
- Wind sensing nose cone, GPS tray, avionics, fuselage, and wing all functional
- All sensors (pressure, GPS, magnetometer, temperature) tested and operational
- Radio and handset input verified working
- Tail surface deflection range sufficient for pitch/roll control in VTOL operations

**Task 03 Progress (50%):**
- User interface completed but only tested in simulation at report time
- Data interface and QC analysis software completed
- Flight permissions obtained for SGP site
- DOE scientific content and safety review approval granted
- Part 107 waiver for 1000' operations submitted
- Test cards created for 13 distinct test scenarios
- Firmware development completed

## Notable Details

**Deployment & Data Sharing:**
- Originally scheduled for August 2020, delayed to October 2020 due to COVID-19
- Using DOE's Southern Great Plains ARM facility as deployment site
- Meteorological data to be shared with DOE community, enabling broader scientific review
- Potential for dual-use applications identified
- Schedule confidence: October testing should allow time for data analysis and delivery of 5 aircraft by January deadline

**Technical Achievements:**
- Developed autonomous transition algorithms between vertical and forward flight
- Validated VTOL control authority independently of fixed-wing systems
- Created simulation capability (S0 model) for algorithm robustness testing
- Achieved responsive manual control while maintaining autonomous capability
- Designed for field deployment with quick-disconnect modular construction

**Air Force Requirements Met:**
- Prototype validated against Task 1 design parameters
- Meteorological data collection capability demonstrated
- Comprehensive user documentation and training interface prepared
- Multiple mission profile capability (profiling, loitering, wind comparison)