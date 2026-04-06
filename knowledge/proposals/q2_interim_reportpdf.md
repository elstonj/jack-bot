# A Ruggedized UAS for Scientific Data Gathering in Harsh Environments

## Document Metadata
- Type: Phase II-E SBIR Interim Report
- Client/Agency: NASA (Jet Propulsion Laboratory)
- Program/Solicitation: NASA SBIR Phase II-E, Contract NNX17CP13C
- Date: March 2020
- BST Products/Systems Referenced: S2 XT (fixed-wing), VTOL S2 XT (vertical takeoff/landing variant), SwiftCore Flight Management System, SwiftPilot, SwiftTab
- Key Personnel: Jack Elston (PI), Maciej Stachura (Lead Engineer)

## Executive Summary
Black Swift Technologies is developing a vertical takeoff and landing (VTOL) variant of the S2 XT small unmanned aircraft system for volcanic sampling and harsh environment scientific data gathering. This Phase II-E extension adds VTOL capability and high-wind operation algorithms to the existing fixed-wing platform, with planned deployment to Makushin Volcano in Alaska to validate the system and demonstrate real-time data visualization for scientists.

## Technical Approach

**Core Development:**
- Adapting the existing S2 XT fixed-wing airframe by adding four rotors for VTOL capability while maintaining ability to operate in volcanic ash and precipitation
- Designing hybrid landing algorithm that uses both rotors and fixed-wing aerodynamic surfaces (ailerons, elevator) for landing in high winds
- Developing real-time in-flight data visualization system for on-board sensors
- Conducting scientific flight campaign at Makushin Volcano, Alaska (with backup location in Hawaii)

**Key Technical Features:**
- VTOL system designed to preserve ~1 hour endurance
- Weight-optimized design removing catapult launch and belly-landing systems
- Multi-hole probe sensor for wind measurement to keep aircraft pointed into wind during landing
- Hybrid control during descent maintains vertical rate sufficient for wing surfaces to provide control authority
- Target capability: operation in winds above 20 mph (up to 30 mph)

**Technical Objectives Progress (as of Q2 report):**
1. **VTOL S2 XT Airframe**: Prototype constructed and test-flown; motor/propeller selection validated
2. **High Wind VTOL Algorithms**: Control algorithm framework completed; autonomous transition logic implemented
3. **In-Flight Data Visualization**: Sensors selected and modeled in CAD for real-time display capability
4. **Scientific Campaign**: Pre-AFSRB completed; materials prepared for safety review boards

## Products & Capabilities Described

### S2 XT (VTOL Variant)
**What it is:** Small fixed-wing unmanned aircraft adapted with four electric rotors for vertical takeoff and landing while retaining original performance characteristics for harsh environment operations.

**Specifications:**
- Wing Span: 120.6"
- Length: 73.4"
- Empty Weight: 15 lbs
- Max Gross Weight: 21 lbs
- Payload Capacity: 5 lbs
- Max Altitude: 10,000 ft
- Max Speed: 48 kts
- Cruise Speed: 37 kts
- Stall Speed: 23 kts
- Max Duration: 90 minutes (standard config)
- Max Range: 63 miles
- Construction: Fiberglass and carbon fiber
- Motor: KDE4215XF
- Battery: 6S 14Ah
- Glide Ratio: 14.3:1

**Proposed Use in Volcanic Sampling:** Enables vertical takeoff from constrained locations (20'x20' areas), operates in high winds and ash, carries payload without pneumatic launcher.

### SwiftCore Flight Management System
- Autopilot/avionics for S2 variants
- Uses CAN protocol for rotor control communications (minimizes wing wiring)
- Integrated with real-time telemetry system

### Multi-Hole Probe (MHP)
**Specifications and Performance:**
- 5-hole probe for measuring wind angle of attack (α), sideslip (β), and dynamic pressure (q)
- Wind tunnel calibrated with 900+ different probe orientations tested
- Measurement methodology: 9th order polynomial fit of non-dimensional pressure coefficients
- **Performance (from wind tunnel data):**
  - α RMS error: 0.4° (raw), 0.1° (filtered)
  - β RMS error: 0.53° (raw), 0.25° (filtered)
  - True airspeed RMS error: 0.24 m/s (raw), 0.06 m/s (filtered)
- Used for real-time wind measurement to keep aircraft pointed into wind during landing

### Volcanic Sampling Payload
**Components:**
- Licor LI-850 (CO₂ and H₂O measurement)
- City Tech electrochemical sensors (SO₂ and H₂S detection)
- Ocean Insight Flame-S spectrometer
- Mapir EO camera (RGB, downward-facing)
- FPV video camera (forward-facing)
- Payload GNSS/magnetometer
- Raspberry Pi Zero payload computer
- Air inlet/exhaust system with quick-connect fittings

**Total Payload Weight:** ~2 lbs of instruments

## Use Cases & Applications

### Primary Mission: Volcanic Ash & Gas Sampling
- Monitor volcanic plumes for ash composition and distribution
- Measure volcanic gas emissions (CO₂, SO₂, H₂S) for volcanic monitoring and eruption prediction
- Photogrammetry survey of volcano summits
- Validation of atmospheric dispersion models
- Demonstration of rapid response capability for volcanic eruption monitoring

### Specific Test Campaign
- **Location:** Makushin Volcano, Alaska (primary); Hawaii (backup)
- **Test Objectives:** 
  - Demonstrate vertical takeoff from 20'x20' area
  - Operate in winds above 20 mph (up to 30 mph maximum)
  - Autonomous volcanic sampling missions
  - Real-time data display for scientist-directed adaptive sampling

### Potential NASA Applications
- Tropospheric Chemistry Program (TCP)
- Applied Sciences Air Quality Program
- CALIPSO mission support
- Aura mission support
- Cloud-Aerosol Transport System (CATS)
- Orbital Carbon Observatory (OCO-2/3)
- Earth Ventures airborne field campaigns
- JPL volcanic observation programs
- MALIBU project (Landsat calibration at mountain sites)
- SoOp (Snow water equivalent measurements)
- NOAA ATD atmospheric science campaigns

### Non-NASA Applications
- USGS volcano monitoring
- NOAA atmospheric studies
- DOE energy research
- National Weather Service applications
- Wildfire monitoring and support
- Pollution monitoring and toxic release response
- Dust storm tracking

## Key Results (Q2 Interim Report Status - 50% Complete)

### Completed Work
- **VTOL Prototype Flight Testing:** Prototype constructed with refined motor/propeller selection
- **Motor/Propeller Performance:** 
  - Initial propeller: 18.5" diameter, provided 1.38:1 thrust-to-weight ratio (insufficient)
  - Updated propeller: 20" diameter, achieved 1.89:1 thrust-to-weight ratio (within desired 1.5:1 to 2:1 range)
  - ESC requirements updated from 50A to 75A due to increased current draw
- **Yaw Control Issue:** Lighter new propellers (4x lighter) reduced yaw control authority
  - Solution: Motor cant of ~6° in yaw axis (opposite motors in opposite directions) to improve yaw torque
  - Will slightly reduce thrust-to-weight but adequate margin remains
- **Multi-Hole Probe Wind Tunnel Validation:** 3 hours of wind tunnel testing completed by NOAA
  - 900+ probe orientation points tested
  - Over 1 million measurements collected
  - Excellent symmetry and performance validated
  - Non-linearity handled through 9th order polynomial fitting
  - RMS errors very low (see specifications above)
- **Payload Development:**
  - All sensors selected and ordered
  - Payload CAD design completed
  - Mechanical design for Makushin deployment completed and ordered
  - FPV camera integration: GPS interference issue identified and resolved with bandpass filter
  - Heated pitot system tested at -7°C, achieved 41°C tip temperature
  - Payload computer (Raspberry Pi Zero) integration completed
- **Flight Permissions:** Pre-AFSRB completed; materials prepared for AFSRB and FRRB

### Current Status
- **Project completion: 50%**
- **Amount expended: $102,273.00**

### Future Planned Work
- Motor cant implementation for improved yaw control
- Simulation testing of hybrid landing algorithm in Gazebo
- Extensive VTOL prototype flight testing in light to moderate winds (10 takeoffs/landings)
- High-wind testing (5 takeoffs/landings in 25-30 mph winds)
- Manufacturing and QC process documentation
- Makushin Volcano flight campaign (Alaska) or Hawaii backup
- Real-time data visualization software development

## Notable Details

### Matching Funds & Partnerships
- **Creare:** Providing matching funds for SwiftCore VTOL capability development (their own NOAA aircraft uses same avionics)
- **USGS:** Providing matching funds and scientific direction for Makushin Volcano campaign
- **JPL:** Technical monitoring (Lance Christensen, Robert Jones) and test site support

### Competitive Advantages
- **High-wind VTOL capability:** Most VTOL fixed-wing aircraft limited to <15 mph winds; S2 VTOL targets >30 mph through hybrid algorithm using fixed-wing surfaces + rotors
- **Harsh environment operation:** Unlike standard VTOL aircraft, can operate in volcanic ash and precipitation
- **Long endurance:** ~1 hour target, better than typical multirotor designs
- **Cost efficiency:** Small UAS cheaper than manned aircraft, larger UAS, or balloons for these missions
- **Modular payload system:** Designed for rapid sensor swapping and customization

### Technical Achievements Specific to Phase II-E
1. **Hybrid landing algorithm concept:** Using multi-hole probe to keep aircraft pointed into wind maintains control authority during descent
2. **Real-time visualization capability:** Responding to USGS need for scientist-directed adaptive sampling
3. **Integration of mature hardware/software:** Leveraging existing S2 platform and SwiftCore avionics for rapid development

### Safety and Compliance
- Aircraft designed to -1.5G to +3.8G limit loads with 1.5x safety factor
- Gust loads tested: -4.2G to +6.2G
- Never had structural failure in flight
- Pre-flight inspection and maintenance procedures documented
- Flight operations plans prepared for AFSRB/FRRB review
- FAA registration and pilot certification in place

### Commercialization Path
- Design intent is commercially-ready platform by end of Phase II-E
- Manufacturing process, wiring, QC, and documentation included in scope
- VTOL variant designed to complement (not replace) fixed-wing S2 XT
- Target customers already identified and engaged (MALIBU, SoOp, NOAA ATD, USGS)