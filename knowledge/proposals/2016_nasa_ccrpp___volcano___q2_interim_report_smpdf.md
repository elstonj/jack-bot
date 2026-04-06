# 2016 NASA CCRPP Volcano Q2 Interim Report

## Document Metadata
- Type: Quarterly Demonstration Report (Q2)
- Client/Agency: NASA (Contract 80NSSC22CA192)
- Program/Solicitation: CCRPP (Commercial Crew and Cargo Program) - SBIR Phase III; Project 2022-1-1118
- Date: February 2023 (report period covers work through Q2 2023)
- BST Products/Systems Referenced: S0, S2, S2-VTOL, E2 quadcopter, SwiftCore (firmware), SwiftPilot (mission planning), SwiftTab (UI/app)
- Key Personnel: Jack Elston (PI), Maciej Stachura (Lead Engineer)

## Executive Summary
Black Swift Technologies reports progress on a NASA-funded effort to develop ruggedized UAS capabilities for scientific data gathering in harsh environments. The Phase III CCRPP project builds on Phase II-e work with the S2 aircraft, focusing on automation for extreme weather operations, improved mission planning for terrain and communications constraints, and development of a VTOL variant. Work includes concurrent missions for NOAA (hurricane sampling and soil moisture mapping) using the S0 and S2 platforms.

## Technical Approach

### Core Objectives
1. **Intelligent flight in strong winds** - Implementing wind-aware real-time flight path adjustment to minimize energy usage, combining environmental assessment with predictive models in SwiftCore firmware
2. **User interface improvements** - Enhanced SwiftTab app for flexible payload telemetry display and control; XML-based data struct framework for easy integration of new payloads
3. **Advanced mission planning** - Automated terrain and communications-aware flight planning for successful operations in rugged environments
4. **Improved S2-VTOL manufacturability** - Simplifying VTOL variant construction and reducing cost for near-vertical launch/landing in strong winds

### S0 Aircraft Modifications (Hurricane Sampling)
- **Thermal design**: New waterproof heat sink for speed controller, tested to 40°C at 125W (well below 100°C limit)
- **Deployment tube**: Redesigned quick-release mechanism with 6-pin edge connectors, active autopilot control, feedback systems, and mechanical redundancy
- **Communications**: Antenna redesigned from 403MHz baseline to 430MHz center band with improved VSWR (2.5-1.5 ratio); 10dB noise reduction in dropsonde band
- **Wind probe**: Innovative passive polyester membrane design with DWR coating to enable 3D wind measurement in hurricane-level precipitation
- **Autopilot**: Migration to RTOS for better sensor/interface timing management; new hardware for radio/sensor integration

### S2 Wind-Aware Navigation
- Two complementary approaches: (1) real-time wind navigation using onboard data only; (2) optimal path planning through varying wind fields using 3D wind forecasts
- Data from Makushin Volcano mission (10.1 m/s winds) showed aggressive 40° bank angles with current planner; new wind-frame approach targets constant-bank turns
- Implementation ongoing in SwiftPilot with flight testing planned

## Products & Capabilities Described

### S0 (Small tactical aircraft)
- **Use**: Tube-deployed from NOAA P3 for hurricane sampling; designed for extreme precipitation and turbulence
- **Specifications**: 
  - Cruise power 60W, capable of sustained operation in heavy rain
  - Communication range ~150nm at 1000ft AGL (12.17dB link margin)
  - Equipped with multi-hole wind probe for 3D wind measurement
  - Waterproof 5-hole probe tested in rain tunnel conditions

### S2 (Medium tactical aircraft)
- **Use**: Terrain-aware operations for volcano observation, soil moisture missions
- **Specifications**: 
  - Capable of 20-mile ingress operations but power-limited in some conditions
  - Wind-aware flight planning under development
  - Demonstrated in Makushin Volcano operations with USGS/NASA

### S2-VTOL
- **Use**: VTOL capability addresses launch/landing constraints in strong winds and obstacle-dense areas
- **Status**: Prototype tested in Phase II-e; redesign underway to improve manufacturability and reduce cost

### E2 Quadcopter
- **Use**: Soil moisture mapping missions (carrying Altum camera for NDVI/thermal data collection)
- **Specifications**: Operates at 400ft AGL for camera work, 180ft for radiometer work at 7.8 mph (3.5 m/s)

### SwiftCore Firmware
- Real-time autopilot system with wind-aware navigation algorithms
- Integration with terrain and communications planning
- RTOS migration for timing management with custom sensors

### SwiftPilot (Mission Planning Software)
- Path planning with wind-frame navigation capability
- Terrain and communications constraint modeling
- Integration with RSS421 temperature/humidity sensor

### SwiftTab (Ground Control Software/App)
- Payload telemetry display
- Flexible UI architecture for multi-payload operations
- XML-based data structure framework

## Use Cases & Applications

### NASA Applications
- **Volcano monitoring**: Makushin Volcano (Alaska) operations demonstrated visual observations in conditions where no other data available that year
- **Satellite validation**: Providing in-situ data for ASTER, MODIS, AIRS, OMI satellite validation
- **Atmospheric science**: Support for Tropospheric Chemistry Program (TCP), CALIPSO, Aura, CATS, OCO-2/3 missions
- **Wildfire/volcanic monitoring**: Continued work with JPL and NASA Ames

### NOAA WPO Applications
1. **Hurricane Sampling**: S0 aircraft tube-deployed from NOAA P3; measures 3D winds in extreme precipitation; six additional vehicles planned for Q3 2022; next flights March 2023
2. **Soil Moisture Mapping (SPLASH Campaign)**: S2 and E2 operations measuring L-band brightness temperature and NDVI; four of seven deployments completed; final three scheduled April-September 2023

### Other Government/Commercial
- USGS monitoring (Christoph Kern, Angie Diefenbach, Jonathan Stock as advisors)
- DOE, National Weather Service applications
- Wildfire monitoring and support
- Commercial market for multi-hole turbulence probe sensor

## Key Results

### Hurricane Sampling Progress (Q2 2023 focus)
- Successfully completed mechanical redesigns for rain-resistant operation
- Antenna tuning achieved 10dB noise reduction in dropsonde band
- Waterproof wind probe design prevents clogging in maximum flow rain tunnel tests
- Cleared air tests showed fabric does not affect pressure measurements
- Link margin analysis: 12.17dB at 1000ft, insufficient at 150nm/200ft AGL
- Planned March 2023 flight tests to validate S0 improvements before hurricane season deployment

### Soil Moisture Mapping Results (October 2022 flights)
- 12 total flights conducted mapping 6 areas on Oct. 18-19, 2022
- Radiometer improvements reduced noise by ~5x through:
  - Replaced 11 voltage regulators with high noise
  - Removed temperature-dependent thermal source
  - Real-time processing display added
- Good agreement between UAS radiometer and in-situ ground probe data
- UAS averaged across larger footprint (~180ft diameter) vs. point measurements, explaining differences in high-moisture riparian areas
- October flight comparison showed high correlation with ground truth

### Wind-Aware Navigation Development
- Analyzed Makushin Volcano S2 flight data (10.1 m/s winds)
- Identified excessive bank angles (40°) on turns with tailwind vs. 15° headwind turns
- Developed wind-frame path planner to normalize turn radius
- Implementation in SwiftPilot; flight testing planned

### Phase III Milestone Delivery
- All NASA Phase III deliverables completed
- Year 1 NOAA WPO deliverables (both soil moisture and hurricane sampling) completed
- Milestones established through Q2 2023 (see Table 1 for detailed deliverable schedule)

## Notable Details

### Mission History
- Prior Phase II-e work validated S2 capability with successful Alaska deployment
- Four missions flown at Makushin with no incidents, but several forced turnarounds due to wind/power limitations
- Flight planning historically required months of preparation and constant real-time monitoring
- Automation objective driven by customer need to conduct routine global missions

### Multi-Customer Investment Structure
- Three separate entities investing in CCRPP: NASA Ames + two NOAA groups (WPO)
- All projects require operations in rugged terrain, precipitation, and/or strong winds
- Work leveraging customer/investor matching funds for concurrent development

### Technical Innovations
- **Waterproof wind probe**: Passive polyester membrane with DWR coating; novel approach allowing 3D measurements in hurricane-level precipitation
- **Wireless communication**: 445MHz antenna design with improved efficiency and out-of-band noise mitigation
- **Deployment tube**: Active autopilot control of tube release with bi-directional communication feedback
- **Wind navigation**: Wind-frame path planning to maintain constant bank angles independent of wind direction

### Manufacturing/Reliability Focus
- S0 redesigns emphasize manufacturability and cost reduction for fleet expansion (6-8 aircraft for hurricane season)
- Simplified mechanical designs (laser-cut antenna elements, 3D-printed aluminum heat sink)
- Testing infrastructure: rain tunnel for waterproofing validation, wind tunnel at Embry-Riddle for aerodynamic characterization

### Software Architecture Improvements
- XML-based data structure framework for payload agnosticity
- Real-time radiometer display for in-flight issue detection
- RTOS migration on autopilot for timing management with multiple custom sensors

### Upcoming Milestones (as of Feb 2023)
- March 2023: S0 flight tests prior to hurricane season
- Spring-late summer 2023: Three additional soil moisture flights (April, June, September)
- June 2023+: Hurricane season deployments with improved S0 fleet
- Q1-Q2 2023: Delivery of turbulence probe sensors for Altius integration
- Flight testing of wind-frame navigation algorithm