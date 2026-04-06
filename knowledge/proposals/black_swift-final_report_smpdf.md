# A Ruggedized UAS for Scientific Data Gathering in Harsh Environments

## Document Metadata
- Type: Final Report
- Client/Agency: NASA (Ames Research Center)
- Program/Solicitation: CCRPP FY 22-I, Subtopic S3.04 Unmanned Aircraft and Sounding Rocket Technologies
- Contract Number: 80NSSC22CA192
- Date: August 2024
- BST Products/Systems Referenced: S0, S2, S2-VTOL, S3, S0-VTOL, SwiftCore, SwiftTab, SwiftStation
- Key Personnel: Jack Elston (PI), Maciej Stachura (Lead Engineer)

## Executive Summary
This final report documents Black Swift Technologies' completion of a NASA CCRPP Phase II-e follow-on project developing ruggedized UAS platforms for scientific data collection in harsh environments including volcanic plumes, hurricanes, wildfires, and severe storms. The project successfully demonstrated the S2 UAS in operational missions at Makushin Volcano in Alaska while advancing automation capabilities for wind-aware flight planning, improved mission planning for terrain and communications constraints, and enhanced manufacturability of VTOL variants. Key deliverables include algorithms for high-wind operations, terrain- and communications-aware mission planning tools, successful deployment to Makushin Volcano with gas and imagery data collection, and prototype VTOL designs (S0 and S3).

## Technical Approach
BST's approach centered on expanding the operational envelope of small UAS through:

1. **Wind-Aware Flight Planning & Energy Management**: Development of machine learning-based power prediction models (decision tree regression using 6 variables: airspeed, climb/descent rate, roll angle, altitude, mass, and center of gravity) trained on 300+ S2 flights. Real-time assessment of environmental conditions combined with predictive models to minimize energy usage and inform dynamic flight path adjustments. Future iterations planned to incorporate vertical airspeed relative to air mass and angle-of-attack measurements.

2. **Intelligent Flight in High Wind Environments**: Algorithms for autonomous operations in strong winds, including:
   - Max wind mission profiles
   - Center fix operations
   - Inflow mission planning
   - Validated through simulation and flight testing

3. **Mission Planning Automation**: 
   - Terrain-aware mission planning to avoid obstacles and optimize flight paths
   - Communications-aware planning accounting for RF range and ground station positioning
   - Web-based mission planning system architecture developed

4. **Systems Integration**: Integration of communications, navigation, scientific payloads, and avionics into platforms optimized for specific mission types (tube-deployed S0, fixed-wing S2, vertical takeoff variants)

## Products & Capabilities Described

### S0 (Sounding Observation Aircraft)
- **Purpose**: Single-use, tube-deployed platform for hurricane sampling from NOAA P3 aircraft
- **Configuration**: Fits in ~5" OD x 37" long tube; spring-loaded wings deploy post-launch
- **Sensor Suite**: Pressure, temperature, relative humidity (RSS421), sea surface temperature, custom 5-hole pitot probe for 3D winds
- **Communications**: 400MHz link, tested for 150nm range from P3
- **Notable Features**: 
  - Waterproof 5-hole probe design using polyester membrane with DWR coating (passive, breathable design)
  - Heat sink design for ESC cooling (34°C at 60W cruise, 40°C at 125W high power)
  - Quick-release deployment mechanism with 2-way communications
  - Antenna redesigned for 430-445MHz band to reduce interference with dropsondes
  - Updated autopilot hardware and RTOS firmware
- **Status**: 18 aircraft delivered to NOAA; additional wind tunnel testing planned; scheduled for 2024 hurricane season deployment

### S2 (Fixed-Wing UAS)
- **Purpose**: High-endurance platform for scientific missions in harsh environments (volcanic, high-altitude, strong wind)
- **Capabilities**: 
  - 20-mile range ingress operations
  - Multi-payload compatibility (trace gas sensors, photogrammetry, radiometers, atmospheric sensors)
  - ADS-B receiver integration for manned aircraft awareness
  - Heated pitot tube for temperature variation handling (upgraded from Phase II-e prototype to production model with PCB-integrated heater, thermistor temperature feedback)
  - Backup satellite communications (Iridium) with automatic failover for lost-link scenarios
  - Long-range command/control with directional antenna capabilities
- **Deployed Systems**: 
  - Trace gas payload for volcanic gas measurements
  - Photogrammetry payload (cameras with geo-referencing)
  - L-band microwave radiometer for soil moisture (passive, 10-20m resolution)
  - Atmospheric sensor suite (temperature, pressure, humidity, winds)
- **Key Mission**: August 2023 deployment to Makushin Volcano, Alaska; successfully collected imagery and volcanic gas data at previously unreachable locations; 4 missions flown without incidents
- **Status**: Serial #S20015 built for NASA Phase III; continued development of manufacturability and VTOL variants

### S2-VTOL
- **Purpose**: Vertical takeoff/landing variant enabling launch/landing in small areas or extreme wind conditions
- **Development Status**: Prototype tested; design updates focusing on improved manufacturability and cost reduction
- **Functional Prototype**: Successful hover test completed May 2024
- **Planned Variants**: S0-VTOL and S3-VTOL designs in development

### S3 (Ruggedized UAS for Extreme Environments)
- **Purpose**: Expanded operational envelope for most difficult environments (volcanic plumes, wildfires, severe storms)
- **Development Status**: Updated CAD design completed December 2023; in development phase (TRL 6 beginning and end)
- **Planned Capabilities**: Enhanced performance in volcanic plumes, wildfire/smoke environments, and hurricane conditions
- **Future Partners**: Consideration of oil/gas industry for gas leak detection applications

### S0-VTOL
- **Status**: Design concept completed February 2024; functional hover test April 2024
- **Purpose**: VTOL variant for ground-based observations in rugged environments

### Ground Control Station Systems
- **SwiftTab**: Android/tablet-based application for telemetry display and payload control; updated UI for flexible multi-payload data visualization
- **SwiftStation**: Ground control station with modular antenna setup supporting multiple antenna types and directional options
- **SwiftCore**: Autopilot firmware with integrated wind-aware algorithms, RTOS features, and advanced control logic

### Scientific Payloads
- **Trace Gas Payload**: Updated design with improved cable routing, simplified assembly (40-hour assembly time), real-time telemetry monitoring via Python GUI; included inlet tubing optimization for better response times
- **Photogrammetry Payload**: Dual-camera system with extended-duration battery; geo-referencing capability; updated from Phase II-e design
- **L-Band Radiometer**: Passive microwave sensor for volumetric soil moisture (5-20cm depth) with 10-20m spatial resolution

## Use Cases & Applications

### NASA Applications
- Volcano monitoring and modeling validation (Makushin Volcano, Alaska - primary demonstration)
- Satellite calibration missions
- Atmospheric data collection at high latitudes
- Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) mission support
- Aura mission support
- Cloud-Aerosol Transport System (CATS) support
- Orbital Carbon Observatory (OCO-2/3) satellite validation
- Tropospheric Chemistry Program (TCP) missions
- Air quality monitoring
- Earth Ventures program support

### NOAA Applications
- **Hurricane Boundary Layer Research (NOAA WPO)**: Deploy S0 from P3 "Hurricane Hunter" aircraft to measure temperature, pressure, humidity, winds, and sea surface temperature in tropical storm boundary layers; real-time data transmission to National Hurricane Center, Environmental Modeling Center, and Hurricane Research Division
- **Soil Moisture Mapping (NOAA SPLASH Program)**: Use S2 and E2 multirotor with radiometer to map surface-atmosphere exchange processes, support National Water Model evaluation, and provide data for National Weather Service forecasting (Unified Forecast System, Rapid Refresh Forecast System)

### Commercial Applications
- **Pipeline Methane Leak Detection**: Oil and gas infrastructure monitoring; BST partnered with sensor company for operational service; demonstrated sub-facility level emission resolution
- **Wildfire Monitoring & Support**: Operations in smoke/particulate-laden environments with severe turbulence
- **Multi-hole Probe Sensor Commercialization**: Standalone sensor market identified

### Future Mission Infusion
- DoD intelligence, surveillance, and reconnaissance (ISR) applications
- Gas leak detection for oil and gas infrastructure (primary commercial focus)
- Atmospheric data collection at high latitudes

## Key Results

### Makushin Volcano Deployment (August 2023)
- Successfully completed 4 missions to volcano summit without incidents
- Achieved photogrammetry and volcanic gas measurements at previously unreachable locations
- Generated 3D mapping and orthomosaic imagery with thermal data
- Validated aircraft performance in extreme wind conditions (downdrafts and lateral winds exceeding some manned aircraft capabilities)
- Demonstrated beyond visual line of sight (BVLOS) operations in complex terrain
- Identified operational limitations: wind resource constraints requiring more aggressive power management and longer ingress planning

### Hurricane Sampling Development
- Two successful S0 prototype deployments from NOAA P3 in May 2022
- Validated mechanical deployment, communications range, and sensor functionality
- Established baseline for full-duration flight testing scheduled Spring 2023
- Antenna design improvements achieved 10dB reduction in dropsonde band interference
- Link margin analysis: 12.17dB at 1000ft / 150nm, -16.66dB at 200ft / 150nm (communication challenges at low altitude identified)
- Waterproof 5-hole probe design successfully tested in rain tunnel; measurements unchanged with precipitation (vs. clogging without waterproofing)

### Soil Moisture Mapping
- Four deployments completed (May-October 2022) across multiple seasonal conditions
- Generated high-resolution (10-20m) volumetric soil moisture maps
- Data collection supporting National Water Model evaluation
- Demonstrated aircraft/radiometer system capability for operational environmental monitoring

### Wind-Aware Flight Planning
- Machine learning power prediction model trained on 300+ S2 flights
- Decision tree regression successfully predicted energy usage in most conditions
- Model validation identified downdraft scenarios requiring additional variables (vertical airspeed relative to air mass, angle-of-attack)
- Established methodology for real-time energy assessment and flight path optimization

### Hardware & Firmware Advances
- ADS-B receiver integration for manned aircraft awareness (long-range capability: detected aircraft from many miles away)
- Heated pitot tube upgraded to production model with improved sensor, PCB-integrated heater, and thermistor feedback
- Satellite communications (Iridium) failover system operational with automatic configuration
- S0 ESC heat sink design: thermal testing showed 34°C at typical cruise (60W), 40°C at high power (125W)
- RTOS migration in progress for autopilot to improve sensor/interface timing management

### Manufacturing & Design
- S2-VTOL prototype design updates completed for manufacturability and cost reduction
- S0-VTOL design concept (February 2024) with functional hover test (April 2024)
- S3 design updated (December 2023) with improved specifications
- Simplified assembly processes for payloads documented

## Notable Details

### Partnerships & Customers
- **NASA Ames**: Primary government customer; working on S2 updates for internal campaigns
- **NOAA Weather Program Office**: Two separate matching-fund partnerships (hurricane sampling and soil moisture)
- **USGS**: Ongoing volcano observation partnership; technical advisors (Christoph Kern, Angie Diefenbach, Jonathan Stock)
- **Oil & Gas Industry**: Commercial interest in methane detection capabilities; partnership with sensor company established
- **Embry-Riddle**: Wind tunnel testing facility for S0 characterization

### Technical Innovations
1. **Waterproof Wind Probe**: Passive polyester membrane with DWR coating enabling measurement in hurricane-level precipitation without clogging
2. **Satellite Communications Failover**: Custom architecture allowing Iridium backup with automatic bandwidth optimization for slow link
3. **Modular Ground Station**: Quick-connect antenna system with improved RF conditions and field portability
4. **Production-Grade Heated Pitot Tube**: PCB-integrated design with thermistor feedback for efficient heating control
5. **Power Prediction Machine Learning**: Decision tree regression approach robust to out-of-dataset conditions

### Competitive Advantages