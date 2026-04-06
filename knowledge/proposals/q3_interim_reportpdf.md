# A Ruggedized UAS for Scientific Data Gathering in Harsh Environments - Phase II-E Interim Report

## Document Metadata
- Type: Interim Report (Q3)
- Client/Agency: NASA
- Program/Solicitation: NASA SBIR Phase II-E, Contract NNX17CP13C
- Date: June 2020
- BST Products/Systems Referenced: S2 XT (fixed-wing), VTOL S2 XT (vertical takeoff/landing variant), SwiftCore Flight Management System, SwiftTab user interface, SwiftPilot autopilot
- Key Personnel: Jack Elston (PI), Maciej Stachura (Lead Engineer)

## Executive Summary
Black Swift Technologies is developing a VTOL (vertical takeoff and landing) variant of the S2 XT unmanned aircraft system for volcanic ash sampling and atmospheric monitoring in harsh environments. The Phase II-E effort adds VTOL capability with high-wind landing algorithms, real-time data visualization, and culminates in a scientific field campaign to Makushin Volcano in Alaska. This extends the S2 XT's existing fixed-wing volcanic sampling capability to operate in areas without suitable runways while maintaining the ability to operate in difficult volcanic plume environments.

## Technical Approach

### Core Innovation
- Convert the existing S2 XT fixed-wing aircraft to VTOL configuration by adding four rotors
- Develop a hybrid control algorithm that uses both rotors and fixed-wing aerodynamic surfaces for landing in high winds (20-30+ mph)
- Implement real-time sensor data visualization and downlink capabilities
- Demonstrate system at Makushin Volcano, Alaska (backup: Hawaii)

### Key Technical Components
1. **VTOL Airframe Design**: Added 4 rotors to existing S2 XT platform with motor mounts tilted 5° for improved yaw authority; motors can be positioned outboard if needed for enhanced control in high winds
2. **Control Algorithms**: Hybrid landing system using multi-hole probe sensor to keep aircraft pointed into wind, maintaining sufficient airflow over control surfaces during descent
3. **Battery System**: 6S9P pack using high-discharge cells (Sony Murata VTC6 or LG 18650HG2) rated for 139A continuous discharge at 3.0V/cell, 50% larger than baseline S2 battery; estimated 2.532 kg mass (152g heavier than baseline)
4. **Wing Modifications**: Increased wingspan by 32" total (16" per wing); redesigned center section with mold shift to move wing joint outboard, allowing 40" inboard section instead of 16", reducing weight and improving stiffness
5. **Autopilot**: SwiftCore Flight Management System with updated desaturation algorithms for managing control saturation across all four axes
6. **Communications**: Integration of Iridium modem as backup for BVLOS operations; ADS-B receiver for traffic awareness; 900 MHz radio for primary command/control

## Products & Capabilities Described

### S2 XT (VTOL Variant)
- **What it is**: Fixed-wing UAS adapted with VTOL rotors for volcanic sampling; complements rather than replaces original S2 XT
- **Configuration**: Small UAS with pneumatic launcher capability removed, VTOL rotors added
- **Performance targets**: 
  - 1 hour flight time (cruise)
  - 120 seconds VTOL hover endurance (40s takeoff, 40s landing, 40s landing reserve)
  - 15% battery capacity remaining prior to VTOL landing phase
  - Capable of operations in winds 20-30+ mph
- **Specifications**:
  - Aircraft mass: 12.7 kg
  - Baseline cruise power: 398W
  - VTOL hover power: 2,500W
  - Payload capacity: volcanic sampling package
  - Operating area: 20' x 20' minimum landing zone

### SwiftCore Flight Management System
- Updated autopilot firmware with new control algorithms for VTOL operations
- Hybrid landing control using rotors + aerodynamic surfaces
- Generic desaturation code for managing thrust and torque saturation across four control axes
- CAN protocol integration for rotor control and sensor interfacing
- Iridium backup communication capability
- ADS-B traffic awareness integration

### Payload Suite (Volcanic Sampling)
- **Sensors integrated**:
  - Multi-hole probe (MHP) - developed in Phase I/II, measures atmospheric wind/pressure
  - Spectrometer (MicroDOAS) - SO2 detection in volcanic plumes
  - Electrochemical trace gas sensors - on CAN bus interface
  - LICOR CO2/H2O analyzer (USB interface, newly updated)
  - MAPIR camera - GPS-tagged imagery with CAN-bus triggering
  - Iridium modem (1600 MHz) - backup communications
  - ADS-B receiver - traffic detection
  - Video system - with GPS interference filters

### Real-Time Data Visualization
- Ground-based visualization software for displaying sensor time-series data in real-time
- Modular design for easy sensor addition/replacement
- Operates via long-range radio link to enable scientist-directed flight path modifications during missions
- Interleaved data transmission from multiple sensors over limited bandwidth

## Use Cases & Applications

### Primary Mission
- **Volcanic Ash Cloud Sampling**: Makushin Volcano, Alaska - demonstrates high-wind VTOL operations in harsh environment with difficult terrain access
- **Scientific Measurements**: In-situ atmospheric chemistry, wind profiles, SO2 concentrations in volcanic plumes

### Potential NASA Applications
- Tropospheric Chemistry Program (TCP)
- Applied Sciences Air Quality Program
- CALIPSO (Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations) mission validation
- Aura mission support
- CATS (Cloud-Aerosol Transport System) mission
- OCO-2/3 (Orbital Carbon Observatory) missions
- Earth Ventures airborne field campaigns
- JPL volcanic observation programs

### Potential Non-NASA Applications
- USGS volcanic monitoring and hazard assessment
- NOAA atmospheric science
- DOE emissions monitoring
- National Weather Service support
- Wildfire monitoring (smoke/particulate characterization)
- Dust storm tracking
- Toxic release response
- Commercial atmospheric sensing markets

### Previous Deployments (Phase II Success)
- Costa Rica: ELEVATE campaign (JPL-funded) at Turrialba Volcano
- Colorado mountain testing
- Multi-hole probe used in numerous atmospheric campaigns

## Key Results (Q3 Status - 75% Complete, $153,410 Expended)

### Technical Accomplishments Completed
1. **VTOL Prototype Testing**: 33 hover flight tests conducted
   - Yaw authority verified with 5° rotor tilt; sufficient for VTOL operations (can increase to 10° if needed)
   - Rotor-only requires ~20% control authority to achieve 10°/s yaw rate
   - Wing weight optimization: switched to lighter current-generation wings, reducing control oscillations by 35% in roll and 39% in pitch

2. **Control Algorithm Development**:
   - Framework for autonomous transition control completed
   - Generic desaturation algorithms implemented for robust multi-axis control management
   - Hybrid landing algorithm design complete, integrating multi-hole probe feedback

3. **Battery System Qualification**:
   - Cell selection narrowed to Sony Murata VTC6 or LG 18650HG2 (both capable of 139A continuous @ 3.0V/cell)
   - 6S9P pack design finalized at 572 Wh capacity (3kWh baseline analysis basis)
   - Estimated to weigh 2.532 kg (tested cells await validation)

4. **Airframe & Structural Design**:
   - Wing mold redesign completed in collaboration with North Wind Composites
   - Allows 40" center section (vs. 16" prototype), enabling lighter wing joiner tube
   - Improved composite layup flexibility for weight optimization
   - Rotor mount locations designed on inboard wing sections; designed as removable for transport

5. **Payload Construction**:
   - All mechanical assembly completed
   - MicroDOAS spectrometer firmware ported and updated (cleaned from 2016 baseline code)
   - Trace gas sensor firmware reused from Phase II Hawaii deployment
   - LICOR USB interface driver updated
   - MAPIR camera GPS-tagging and CAN-bus triggering configured
   - Payload power control via autopilot-switchable power rail

6. **Avionics Integration**:
   - **Iridium Board**: Custom integration board designed and prototyped; micro-controller sniffs 900 MHz heartbeat packets and routes to Iridium modem on lost-link condition; firmware development ~50% complete
   - **ADS-B Receiver**: Ping Rx receiver integrated; firmware reads traffic data (N-number, aircraft type, lat/lon/altitude); CAN-bus relay to autopilot in progress
   - **Video System**: Dual-filter setup designed to prevent GPS interference; remote on/off capability added; tested successfully at 1 NM range with RTK GPS maintained; 30 km range validation test in planning

7. **Safety Review & Compliance**:
   - AFSRB (Airworthiness and Flight Safety Review Board) presentation completed
   - Pre-AFSRB meeting completed; materials prepared for FRRB (Flight Readiness Review Board)
   - Virtual site visit approach approved (physical visit waived due to travel restrictions/timeline)
   - Key requests for additional documentation submitted by AFSRB (maintenance logs, emergency procedures, payload structure photos, battery specs, thermal endurance data, laser certification, FTS assessment, etc.)

8. **Alaska Deployment Coordination**:
   - Site selection completed: Makushin Volcano with backup location at 20'x20' landing zone
   - Local liaison established (Andy Dietrick); site visit photos and 3D photogrammetry obtained
   - Contact matrix created: aviation operators, infrastructure (internet/shipping), airspace management, land owners
   - Weather and FAA SWIM data access verified; telemetry uplink to NASA airborne tracking system planned

### Flight Test Data
- Yaw rate command tracking: measured yaw follows commanded 10°/s rate with ~20% rotor authority utilization
- Roll/pitch oscillation reduction: 35% roll rate improvement, 39% pitch rate improvement with lighter wings
- Video link budget: calculated capability to 30 km range with current antenna setup
- GPS: RTK solution maintained during video system operation

### Firmware/Software Status
- SwiftCore autopilot: hybrid VTOL/fixed-wing control, transition framework, saturation management complete
- SwiftTab (tablet UI): VTOL-specific command/control updates in progress
- SwiftPilot: hybrid algorithm implementation tested
- Gazebo simulation: high-wind landing algorithm simulation validation prepared

## Notable Details

### Matching Funds Leverage
- **Creare contribution**: VTOL SwiftCore avionics development for their own NOAA aircraft platform (deck operations in high winds)
- **USGS contribution**: Makushin Volcano mission execution (travel, payload sensor modifications)
- **External investment**: Additional funds augmenting BST internal R&D capability

### Commercial/Market Advantages
- **Unique high-wind VTOL capability**: Operating in 20-30+ mph winds significantly exceeds competitors (typical VTOL fixed-wing limited to <15 mph)
- **Reduced power consumption vs. oversize rotors**: Hybrid approach maintains fixed-wing efficiency while adding VTOL; complements rather than replaces baseline S2 XT
- **Expandable sensor architecture**: Modular payload with real-time downlink visualization enables scientist-directed adaptive sampling
- **Ruggedized for harsh environments**: Unlike consumer/light UAS, designed to operate in volcanic ash, precipitation, high winds

### Competitive Differentiation
- **Multi-hole probe sensor** (Phase I/II SBIR heritage): proprietary low-cost wind measurement sensor integrating with control algorithm
- **SwiftCore avionics maturity**: flight-proven in Costa Rica ELEVATE campaign, used by MALIBU (NASA GSFC), SoOp (NASA JPL), NOAA ATD
- **Operating area flexibility**: 20'x20' landing zone requirement vs. runway-dependent competitors
- **Deployment history**: Proven in volcanic ash, mountain sites, remote locations; repair/replacement costs favorable for high-risk missions

### Future Development (Planned through end of Phase II-E)
- Battery conditioning/maintenance procedures and capacity verification protocols
- Historical flight data/interpolated performance validation for 15-min reserve requirement
- Temperature impact characterization on endurance/range
- Laser certification