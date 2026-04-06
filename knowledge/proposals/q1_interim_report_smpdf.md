# Q1 Interim Report: A Ruggedized UAS for Scientific Data Gathering in Harsh Environments

## Document Metadata
- Type: Interim Report (Phase II-E SBIR)
- Client/Agency: NASA (JPL)
- Program/Solicitation: NASA SBIR Phase II-E; Contract Number NNX17CP13C
- Date: December 2019
- BST Products/Systems Referenced: S2 XT, S2 VTOL, SwiftCore Flight Management System, SwiftTab (user interface), SwiftPilot (autopilot), multi-hole probe sensor
- Key Personnel: Jack Elston (PI, BST), Maciej Stachura (Lead Engineer, BST)

## Executive Summary

Black Swift Technologies is developing a vertical takeoff and landing (VTOL) variant of its S2 XT ruggedized unmanned aircraft system for volcanic sampling and scientific data collection in harsh environments. The Phase II-E work extends the company's proven S2 XT fixed-wing platform by adding VTOL capability while maintaining endurance and payload capacity, enabling operations in areas where conventional aircraft cannot land and supporting real-time adaptive flight missions directed by scientists in the field.

## Technical Approach

**VTOL S2 XT Development:**
- Adding four rotors to the existing S2 XT airframe to enable vertical takeoff and landing
- Aerodynamic redesign: increased wingspan by 32" at root, extended tailboom by 10", changed V-tail angle from 35° to 40°
- Prototype constructed with wing inserts (2 x 18" inner sections), 3D-printed rotor arm mounts, and carbon fiber booms
- Battery size increased 50% to support rotor operations while maintaining approximately 1-hour endurance with 5 lb payload
- Design maintains wing loading and stability characteristics similar to standard S2 XT

**High-Wind Landing Algorithm:**
- Novel hybrid VTOL/fixed-wing control system designed to operate in winds >30 mph (commercial VTOL competitors typically limited to <15 mph)
- Algorithm keeps vertical descent rate high enough for aileron/elevator control surfaces to remain effective
- Uses low-cost multi-hole probe sensor to maintain nose-into-wind orientation, reducing adverse roll from wind hitting wings
- Leverages both rotor thrust and aerodynamic control surfaces for landing stability

**Supporting Technology:**
- Integration with SwiftCore Flight Management System avionics
- Updates to SwiftTab tablet-based user interface for VTOL-specific command and control
- Development of real-time in-flight data visualization system allowing scientists to monitor sensor data and adaptively direct aircraft
- Simulation testing using Gazebo environment with wind models; higher-fidelity JSBSim-based simulator under development on separate NASA project

## Products & Capabilities Described

**S2 XT (Fixed-Wing Base Platform)**
- Small, composite fixed-wing UAS designed for scientific missions in harsh environments
- Specs: ~9.3 kg baseline weight, 121" wingspan, electric propulsion, pneumatic catapult launch, belly landing
- Flight envelope: max 48 kts, cruise 39 kts, 1.5 hour endurance, 58.5 nm range, up to 5 lb payload
- Proven in field at Turrialba Volcano (Costa Rica) as part of JPL-funded ELEVATE campaign
- Can operate in high altitude, high winds, damaging particulates (volcanic ash, precipitation)

**S2 XT VTOL Variant (under development)**
- Same airframe with added four-rotor system (rotors mounted on extended wings)
- Removes catapult-launch and belly-landing reinforcements; adds VTOL-specific components
- Target specifications: ~12.1 kg gross takeoff weight, similar wing loading to standard S2 XT, ~90 minute endurance with 5 lb payload
- Key advantage: can operate in winds up to 30 mph during VTOL operations (takeoff/landing)
- Design trades 5% endurance/payload for VTOL capability

**SwiftCore Flight Management System (FMS)**
- Autopilot and avionics suite developed in-house by BST
- CAN bus protocol for motor/rotor control integration
- Supports modular sensor integration with well-documented power and data interfaces
- Being updated with VTOL control algorithms and firmware

**SwiftTab User Interface**
- Tablet-based ground control station software
- Tablet-specific command/control capabilities for VTOL aircraft operation
- Real-time data visualization of on-board sensors

**Multi-Hole Probe Sensor**
- Developed in Phase I/II; measures 3D winds, pressure, temperature, relative humidity
- Low cost and power consumption (0.5 W average)
- Used for wind-vane function in high-wind landing algorithm
- Has standalone commercial applications for atmospheric campaigns

## Use Cases & Applications

**Primary Mission: Volcanic Sampling and Monitoring**
- Proximal and distal sampling inside volcanic plumes
- Measurement of volcanic gases (SO2, CO2, H2S, H2O) and ash characteristics
- In-situ validation of Volcanic Ash Transport and Dispersion (VATD) models used by nine Volcanic Ash Advisory Centers (VAAC)
- Support for aviation safety: with ~33,000 new aircraft expected over next 20 years and 4.5% annual air traffic growth, volcanic ash encounters are increasing risk

**Specific Campaigns Mentioned:**
- **Makushin Volcano, Alaska**: USGS-funded mission to measure SO2 emission rates and summit photogrammetry; plans include BVLOS operations from base site near Dutch Harbor airport, 25 km from volcano summit; volcano characterized by complex topography, winds >15 knots common, multiple degassing features
- **Turrialba Volcano, Costa Rica**: Completed as part of ELEVATE campaign
- **Hawaii**: Backup location for Phase II-E flight campaign (existing flight permissions)

**NASA Applications:**
- Tropospheric Chemistry Program (TCP)
- Applied Sciences Air Quality Program
- CALIPSO (Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations)
- Aura mission
- CATS (Cloud-Aerosol Transport System)
- OCO-2/3 (Orbital Carbon Observatory)
- Earth Ventures airborne field campaigns
- JPL small programs focused on volcanic observations

**Non-NASA Commercial Applications:**
- USGS volcanic monitoring and volcano research
- NOAA atmospheric science
- DOE/National Weather Service
- Wildfire monitoring and support (operation in particulate-laden, turbulent environments)
- MALIBU project (NASA GSFC) for Landsat calibration at difficult mountain sites
- SoOp (NASA JPL) snow water equivalent measurements in mountains

## Key Results (Interim Report)

**Completed Activities:**

1. **Aerodynamic Analysis & Design**
   - XFLR5 analysis confirmed design maintains stability/controllability comparable to standard S2 XT
   - Stability margin: 0.22 (vs. 0.18 for standard S2)
   - Horizontal tail volume coefficient: 0.66 (identical to standard)
   - Vertical tail volume coefficient: 0.024 (vs. 0.025 standard)
   - Wing loading: 43.3 oz/ft² (vs. 42.9 standard) despite ~3 kg weight increase

2. **VTOL Prototype Flight Testing**
   - Prototype built and flown under Part 107 regulations
   - Flight data validated motor/ESC/propeller combination
   - Manual hover/multirotor control demonstrated adequate control authority
   - Forward flight to ~1000 ft AGL with loops executed successfully
   - Forward flight at cruise speed (19 m/s) showed power consumption of 299 W
   - Extrapolated cruise endurance: ~100 minutes at 19 m/s (exceeding 90-minute target) with 5 lb payload at 600 Wh battery
   - Pilot comments: "aircraft flew very well and very similar to a regular S2; no destabilizing issues with rotor mounts"

3. **High-Wind Landing Algorithm**
   - Simulation framework established (Gazebo)
   - Control gains refined through flight testing
   - System validated as controllable via manual handset

4. **Alaska Flight Campaign Planning**
   - CONOPS and flight permissions strategy documented
   - Scientific overview completed for BVLOS operations
   - Safety plan developed coordinating with Dutch Harbor airport traffic (multiple operators: Grant Aviation, PenAir, ACE Air, LifeMed, Maritime Helicopters, USCG)
   - Radio coordination procedures established (CTAF 122.6, weather 129.5)
   - Real-time telemetry capabilities defined (forward video camera, gas sensor data)
   - Target operation area: 20' x 20' landing zone in winds up to 30 mph

5. **Real-Time Data Visualization Development**
   - Prototype capability demonstrated
   - Modular architecture designed for future sensor additions
   - Will display time-series data from on-board sensors

**Outstanding Tasks:**
- FAA approval for BVLOS operations
- Mechanical design optimization (reduce ESC/wiring weight, internal routing, improved rotor/boom aerodynamics)
- Single-piece wing development for production models
- Custom carrying case design for VTOL components
- Manufacturing process and QC documentation
- Flight testing in high winds (target: 5 takeoffs/landings in 25-30 mph winds at BST test site)
- Alaska deployment and scientific flight campaign

## Notable Details

**Technical Innovations:**
- Unique hybrid VTOL algorithm combining rotor thrust with aerodynamic control surfaces—addresses gap where commercial VTOL fixed-wing aircraft struggle above 15 mph winds
- Low-cost multi-hole probe as wind-vane sensor elegantly solves high-wind landing control problem
- Modular, quick-swap payload section with defined mechanical/electrical interfaces enables rapid sensor integration

**Commercialization Strategy:**
- VTOL variant complements rather than replaces fixed-wing S2 XT; targets different mission sets
- Conversion kit from rail-launch to VTOL not currently planned (weight/cost trade-off)
- Initial production will use 2-piece wings (lower tooling cost); future versions single-piece for weight optimization
- Existing flight permissions from Phase II in Hawaii provide backup mission location
- Multiple existing potential customers identified (MALIBU, SoOp, NOAA ATD) who could benefit from VTOL capability

**Matching Funds & Partnerships:**
- **Creare**: Providing matching funds for VTOL SwiftCore avionics development (their own aircraft design for NOAA; same control algorithms benefit both platforms)
- **USGS**: Providing matching funds for Makushin Volcano flight campaign (travel, payload sensor modifications); specific interest in real-time data telemetry for adaptive mission planning
- Partnership enables shared algorithm development with mutual benefits

**Operational Context:**
- S2 platform has proven heritage: successfully deployed in Costa Rica, tolerates repeated landings on rocky roads and hillside pastures
- SwiftCore FMS and well-documented interfaces established as user-friendly for field scientists directing flight operations
- Commercial success of S2 base platform and multi-hole probe sensor demonstrates market validation

**Volcano Monitoring Justification:**
- Current VATD models lack in-situ validation; satellite data (ASTER, MODIS, AIRS, OMI) suffer cloud masking, infrequent coverage, resolution limits
- Dave Pieri (JPL volcanologist) noted ash "thickness and density are largely unvalidated and not quantitative enough"
- Limited existing in-situ volcanic plume data due to hazard to manned aircraft; UAS uniquely positioned to fill gap
- Enhanced capability supports both aviation safety and volcano research (magmatic system dynamics, eruption forecasting)

**Payload Specifications (Makushin Campaign):**
- BST 5-hole probe: 100g, 0.5 W average
- Licor 850 CO₂/H₂O analyzer: 1300g, max 14 W, 12-30V input, 4.6 W average
- Additional sensors potentially included in modified payload tray

**Performance Data Points:**
- Rate of climb: 950 ft/min
- Rate of descent: 810 ft/min
- Maximum glide slope: 15 degrees
- Structural limit loads: -1.5G to +3.8G; gust loads -4.2G to +6.2G (1.5 factor of safety); no in-flight structural failures to date
- Wind conditions at Makushin: predominant from west, typically <15 m/s in early/late summer;