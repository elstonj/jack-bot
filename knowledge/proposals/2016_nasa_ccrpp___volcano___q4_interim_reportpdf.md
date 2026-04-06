# 2016_NASA_CCRPP___Volcano___Q4_Interim_Report.pdf

## Document Metadata
- Type: Quarterly Demonstration Report (Q4 Interim Report)
- Client/Agency: NASA (via NSSC contract)
- Program/Solicitation: SBIR CCRPP (Commercial Crew and Cargo Program Related) / Contract 80NSSC22CA192 / Topic 2022-1-1118
- Date: August 2023
- BST Products/Systems Referenced: S2, S0, S2-VTOL, SwiftCore, SwiftTab, SwiftPilot, E2, Altius turbulence probe, multi-hole probes (MHP)
- Key Personnel: Jack Elston (PI), Maciej Stachura (Lead Engineer)

## Executive Summary
This Q4 interim report documents Black Swift Technologies' progress on developing ruggedized UAS for scientific data gathering in harsh environments. Building on Phase II-e work with the S2 aircraft in volcanic environments, the project focuses on four key technical objectives: intelligent flight in strong winds, user interface improvements for scientific data management, advanced mission planning for terrain and communications, and improved manufacturability of the S2-VTOL variant. The work is funded by NASA and NOAA partners requiring capabilities for extreme atmospheric environments.

## Technical Approach

### Core Strategy
BST is enhancing its S2 and S0 aircraft platforms through automation and software improvements to enable routine operations in previously challenging conditions. Key approach elements:

1. **Wind-Aware Flight Planning**: Integration of real-time environmental assessment with predictive models to minimize energy usage through dynamic flight path adjustments implemented in SwiftCore firmware.

2. **Advanced Mission Planning**: Development of automated mission planner that handles terrain avoidance, restricted airspace conformance, line-of-sight (LoS) communications optimization, and battery usage estimation.

3. **Sensor Payload Protection**: Testing of sintered PTFE membrane protection for multi-hole pressure (MHP) tips to enable operations in precipitation.

4. **Hardware Refinements**: Updates to deployment tube controllers, autopilot boards, GPS antennas, and radio systems for improved reliability and range.

### Technical Implementation Details

**Altitude Turbulence Probe Development**:
- Modified 9-port nose cone design for Altius payload
- Countersunk adhesive channel design to reduce diaphragm effects from water droplets
- Tested membrane protection using sintered PTFE industrial IP-rated protection vents
- Developed capability to compensate for port clogs using redundant pressure measurements

**S0 Aircraft Improvements**:
- Propeller upgrade from 6x3 to 7x4 with motor Kv reduction (2550 to 1950) yielding ~10% static thrust efficiency improvement
- Enhanced safety mechanisms: spring-loaded arming flap latch, single "press and hold" power sequence
- Improved electronics: deployment tube battery monitoring, charging current indication, soft power button with 10-second hard power-off
- GPS: tuned antenna directly on PCB for improved signal-to-noise ratio, better ocean-surface performance
- Radio: redesigned boards for 2W higher power operations, additional UART for RSSI monitoring, modified communication protocol for lower baud rates
- On-track for delivery of 8 full systems by end of August 2023

**Precipitation Testing**:
- Membrane frequency response testing showed acceptable performance despite some high-frequency attenuation
- Water impact testing confirmed membrane integrity under high-speed water jet impacts
- No water penetration observed in precipitation tests; large droplet impacts acceptable with selective data exclusion

## Products & Capabilities Described

### S2 (Fixed-Wing UAS)
- **Description**: Primary long-endurance aircraft for scientific missions in extreme environments
- **Use in Project**: Volcano observation, wind research, trace gas sampling (SO₂), remote sensing payloads
- **Specifications**: ~20 m/s cruise speed, capable of sustained operations in strong winds and complex terrain
- **Demonstrated Capability**: 4 missions to Makushin Volcano summit in Alaska; encounters with winds and downdrafts exceeding manned aircraft capabilities
- **Performance Issues Addressed**: Limited propulsion efficiency on long ingress (20 miles), vulnerability to lateral and vertical wind gusts

### S2-VTOL (Vertical Takeoff/Landing Variant)
- **Description**: Enhanced S2 variant with VTOL capability for extreme environments
- **Use Case**: Launch and landing from small or obstacle-dense areas; strong wind operations
- **Status**: Prototype tested during Phase II-e; undergoing manufacturability improvements for commercial version
- **Key Advantage**: Eliminates need for runway or landing area

### S0 (Small Deployable UAS)
- **Description**: Compact, tube-launched aircraft for rapid deployment from crewed platforms (e.g., P3 aircraft)
- **Current Work**: Construction of 8 units with latest improvements
- **Payloads**: Multi-hole pressure probe, video systems, specialized sensors
- **Deployment**: Launches from P3 aircraft via parachute deployment tube
- **Communication Range**: Previous limitation ~30 nmi; targeting 150 nmi through radio and protocol improvements
- **Battery Monitoring**: Enhanced diagnostics with onboard battery voltage monitoring

### E2 (Soil Moisture Mapping UAS)
- **Description**: Platform for L-band radiometry and vegetation/thermal mapping
- **Use**: NOAA WPO soil moisture mapping campaign
- **Specifications**: Updated radiometer design with improved cold source; NDVI sensors; thermal camera
- **Recent Missions**: 10 flights mapping 5 areas at Rocky Mountain Biological Laboratory (June 2023)
- **Data Processing**: Raspberry Pi Zero W with USB storage for radiometer and telemetry data

### SwiftCore (Autopilot Firmware)
- **Description**: Core flight control and navigation firmware
- **Enhancements**: Implementation of wind-aware flight planning, terrain-aware navigation, terrain avoidance algorithms
- **Development**: Python-based algorithms being transferred to tablet for simplified operations

### SwiftTab/SwiftPilot (Ground Control Software)
- **Description**: Tablet-based mission planning and monitoring application
- **Improvements**: 
  - XML-based payload data parsing and variable definition
  - Real-time geo-referenced plotting of sensor data (e.g., SO₂ concentrations overlaid on map)
  - Time-series telemetry visualization
  - Advanced mission planning GUI with cost function weighting
  - 3D route visualization
- **Hardware**: Operates on tablet for field operations; planning algorithms can execute offline

### Advanced Mission Planner
- **Description**: Automated route generation and validation tool
- **Capabilities**:
  - Terrain avoidance with configurable minimum enroute altitude
  - Airspace conformance (keep-out zones, restricted airspace)
  - Line-of-sight (LoS) communications analysis and optimization
  - Battery usage estimation with wind compensation
  - Estimated time enroute (ETE) calculation
  - 3D visualization of top 5 route options
- **Algorithm**: Waypoint grid generation with Dijkstra's shortest path algorithm via NetworkX library
- **Cost Function**: Balances lost LoS time, battery usage, and low altitude with user-configurable weights
- **Application Example**: Makushin Volcano ingress route (7,000 ft climb over 14 miles with terrain and airspace constraints)
- **Status**: Offline pre-mission tool; future integration planned for real-time mission execution updates

### Altius Turbulence Probe
- **Description**: 9-hole multi-hole pressure (MHTP) tip for measuring wind components in severe weather
- **Integration**: Partnership with Altius team; tested on S2 airframe with dual MHP sensors for validation
- **Specifications**: Comparable to S0 MHP; improved membrane design; redundant port capability for clog compensation
- **Application**: NOAA WPO hurricane sampling missions

## Use Cases & Applications

### Operational Missions Completed/Ongoing

**Makushin Volcano Observations (Alaska)**
- Partner: USGS, NASA, NOAA
- Platform: S2
- Payloads: Thermal camera, SO₂ trace gas sensor, multispectral imaging
- Achievements: 5 flights to summit with 2 different payloads; produced 3D maps and orthomosaics with thermal data overlay
- Environmental Challenges: Extreme winds, downdrafts, complex mountain terrain, beyond-visual-line-of-sight (BVLOS) operations
- Data Products: Visual observations (only achieved during this calendar year), 3D photogrammetry, thermal imagery, SO₂ plume tracking

**NOAA WPO Hurricane Sampling**
- Platform: S0 aircraft (6 units), tube-launched from P3
- Payload: Altius turbulence probe (9-hole MHTP)
- Objective: In-situ wind measurements in hurricane conditions
- Status: Equipment delivery Q3 2023; hurricane season operations

**NOAA WPO Soil Moisture Mapping (SPLASH Campaign)**
- Platform: E2
- Location: Rocky Mountain Biological Laboratory and study sites
- Payloads: L-band radiometer, NDVI sensors (upward and downward-looking), thermal camera
- Methodology: Maps soil moisture via cosmic microwave background comparison; complements NDVI vegetation index and thermal data
- Recent Campaign: June 2023 with 10 flights covering 5 study areas
- Data Quality: Improved stability and accuracy with updated radiometer design

**Oil and Gas Methane Monitoring (Emerging Commercial Application)**
- Platform: S2
- Payload: Trace gas (CH₄) sensor
- Objective: Sub-facility-level methane emission mapping over entire facility in short timeframe
- Status: Demonstration completed; continued work for paid service offering

### Potential NASA Applications
- Tropospheric Chemistry Program (TCP)
- Applied Sciences Air Quality Program
- CALIPSO, Aura, CATS, OCO-2/3 missions
- Volcanic and wildfire observations (JPL, NASA Ames partnership)
- Airborne field campaigns through Earth Ventures program
- Model validation and atmospheric data collection for weather/dispersion models

### Potential Non-NASA Applications
- USGS: Volcano and geological monitoring
- DOE: Energy sector applications
- National Weather Service: Weather data collection
- Wildfire monitoring and support (hazardous particulates/turbulence environment)
- Commercial market for multi-hole pressure probe sensors

## Key Results (for this interim report period)

### Completed Deliverables
- All Phase III NASA deliverables completed
- Year 1 deliverables for NOAA WPO soil moisture mapping mission completed
- Year 1 deliverables for NOAA WPO hurricane sampling mission completed
- Work initiated on intelligent flight through winds

### Technical Accomplishments

**Altius Probe Development**:
- Modified nose cone design tested successfully on S2 airframe
- Dual MHP sensor comparison validated Altius measurements against S0 baseline
- Developed compensatory algorithms for port clog scenarios using 9-hole redundancy
- Confirmed membrane material (sintered PTFE) maintains integrity under precipitation

**S0 Aircraft Construction**:
- All 8 deployment tubes fully constructed and assembled
- Subsystems partially assembled; on-track for completion by August 2023
- Propeller efficiency improvements verified (~10% static thrust gain)

**Soil Moisture Mapping**:
- June 2023 campaign executed: 10 flights, 5 study areas
- Radiometer redesign yielded improved map stability and accuracy
- Standalone system developed: consolidated L-band radiometer + NDVI + thermal into single payload (previously required two flights)

**Mission Planning System**:
- Operational automated planner developed for transit segment route optimization
- Successfully applied to Makushin Volcano mission planning (14-mile, 7,000 ft climb)
- 3D visualization and route performance analysis demonstrated
- Supports terrain clearance, airspace conformance, LoS analysis, and battery optimization

**Wind Sensing Research**:
- Identified magnetometer calibration as critical for wind estimation accuracy (target: <1° heading error)
- Demonstrated 0-5° yaw errors in standard calibrated magnetometers due to non-orthogonal sensors
- Validated heading-correction algorithm using forward/back flight test data
- Work ongoing on advanced magnetic calibration methods

**UI Improvements**:
- XML-based payload data parsing system implemented
- Real-time geo-referenced sensor plotting capability demonstrated (SO₂ plume visualization)
- Time-series telemetry display functional for in-flight calibration verification

### Performance Data

**Precipitation Testing Results**:
- Membrane protected MHP tip maintained pressure readings throughout water impact tests
- Frequency