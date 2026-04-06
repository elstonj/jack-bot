# 2022-1-1118 - A Ruggedized UAS for Scientific Data Gathering in Harsh Environments: Q2 Interim Report

## Document Metadata
- **Type:** Quarterly Demonstration Report (Phase III CCRPP)
- **Client/Agency:** NASA (primary contract); NOAA (matching funds partners)
- **Program/Solicitation:** 2022-1-1118 SBIR CCRPP (Commercial Cargo, Resupply and Personnel Project)
- **Contract Number:** 80NSSC22CA192
- **Date:** February 2023 (Q2 interim report covering work through early 2023)
- **BST Products/Systems Referenced:** S0, S2, S2-VTOL, E2 quadcopter, SwiftCore (firmware), SwiftPilot (flight planning software), SwiftTab (UI app)
- **Key Personnel:** Jack Elston (PI, Principal Investigator), Maciej Stachura (Lead Engineer)

## Executive Summary
This Phase III CCRPP report documents BST's advancement of small UAS platforms for extreme environment operations. Building on Phase II-e volcano mission success, the work focuses on automation for harsh conditions through intelligent wind-aware flight planning, improved manufacturability of the S2-VTOL variant, enhanced scientific data management UI, and terrain/communication-aware mission planning. The project is funded by matching investments from NASA Ames, NOAA Weather and Post-Observation (WPO) groups for hurricane sampling and soil moisture mapping applications.

## Technical Approach

### Core Development Objectives
1. **Intelligent Flight in Strong Winds:** Real-time wind assessment combined with predictive models to automatically adjust flight paths and minimize energy usage. Implementation in SwiftCore firmware with planned flight testing.

2. **UI Improvements for Scientific Data Management:** Updates to SwiftTab app for flexible payload integration, common operating picture display, telemetry visualization, and payload control across interchangeable sensor packages.

3. **Advanced Mission Planning:** Automated processes for terrain navigation and communication system constraints, building on wind-aware planning capabilities.

4. **S2-VTOL Manufacturability:** Design simplification and cost reduction for the vertical takeoff/landing variant that enables launch/landing in strong winds and obstacle-dense areas.

### Technical Implementation Details

**S0 Aircraft Enhancements (Hurricane Mission):**
- New waterproof thermal heat sink design for speed controller (tested at 60W cruise: 34°C steady state; 125W high power: 40°C, well below 100°C limit)
- Redesigned deployment tube with active autopilot control, status feedback, and mechanical reliability improvements
- New 6-pin edge connectors with 2-way communications between aircraft and deployment control board
- Updated wireless communication system at 430MHz with improved VSWR (1.5-2.5) tuned for center band
- Antenna pattern testing in anechoic chamber showing degradation only at front (battery/wing occlusion)
- Out-of-band noise reduction: 10dB reduction in dropsonde band interference by shifting to 430MHz
- Link margin assessment: 12.17 dB at 1000 ft altitude / 150nm range; -16.66 dB at 200 ft (work ongoing)
- Real-time operating system (RTOS) migration on autopilot for improved timing with custom sensors
- Integration of RSS421 temperature/humidity sensor with pre-flight reconditioning capability
- Waterproof 5-hole wind probe with polyester DWR-coated membrane for hurricane-level precipitation measurement
- Wind tunnel testing planned at Embry-Riddle with custom pitch/yaw mount to characterize angle-of-attack, angle-of-sideslip, and true airspeed across range validated from past flights

**Wind-Aware Navigation Algorithm:**
Two complementary approaches under development:
- **Method 1 (Real-time):** Wind frame-based path planning using onboard wind data; replaces inertial path planning to achieve constant bank turns instead of excessive 40°+ banks in crosswind scenarios
- **Method 2 (Optimal Planning):** Energy-minimizing paths through 3D wind fields using weather forecasts or other wind data sources

Real-world example: Makushin Volcano flight with 10.1 m/s winds showed S2 requiring 40°+ bank angles in standard inertial planning; wind frame correction reduces to ~15-25° for equivalent maneuvers.

## Products & Capabilities Described

### S0 (Tube-Launched Small UAS)
- **Purpose:** Hurricane sampling via deployment from NOAA P3 aircraft
- **Key Specs:** 60W typical cruise power, operational in heavy precipitation
- **Capabilities:** 3D wind measurement, extended range communications (working at 1000 ft AGL / 150nm), tube deployment with active aircraft control
- **Status:** Major design iterations completed for Phase III; scheduled for March 2023 flight tests ahead of hurricane season deployment
- **Payloads:** Wind probe, video systems, radiometric sensors

### S2 (Fixed-Wing Platform)
- **Purpose:** Long-range observation missions in challenging terrain (volcanoes, wildfire smoke, etc.)
- **Capabilities:** BVLOS operations, complex terrain navigation, strong wind tolerance (though improvements underway)
- **Status:** Proven in Makushin Volcano deployment (4 successful missions without incidents); some missions required turnaround due to power limits on 20-mile ingress or wind exceedance
- **Upgrades in Progress:** S2-VTOL variant for vertical launch/landing in strong winds; terrain-aware and communication-aware flight planning

### S2-VTOL Variant
- **Purpose:** Enable launch/landing from small or obstacle-dense areas in strong wind conditions
- **Status:** Prototype tested in Phase II-e; design refinement for manufacturability and cost reduction underway as part of Phase III

### E2 Quadcopter
- **Purpose:** Soil moisture mapping with radiometric and optical sensors
- **Capabilities:** Carries Altum camera (NDVI, thermal, digital surface model) and L-band radiometer
- **Operations:** Cruise speed 7.8 mph (3.5 m/s) for optimal sensor integration time

### SwiftCore (Firmware Platform)
- **Function:** Flight control and automation system
- **Enhancements:** Wind-aware flight planning algorithms, RTOS implementation, sensor interface management
- **Future:** Deployment control and advanced mission automation

### SwiftPilot (Flight Planning & Control Software)
- **Function:** Mission planning, waypoint management, real-time flight path adjustment
- **Enhancements:** Wind frame path planning, terrain-aware routing, communication constraint modeling
- **Status:** Wind navigation approach currently being added with flight testing planned

### SwiftTab (Mobile UI)
- **Function:** Ground station telemetry display and payload control
- **Enhancements:** Data type flexibility via XML struct framework, wind field mapping, scalar value visualization, payload-agnostic design for easy integration of new sensors

## Use Cases & Applications

### 1. Volcano Monitoring
- **Past Mission:** Makushin Volcano, Alaska (October 2022) with USGS and NASA
- **Achievements:** Only visual observations of volcano target in calendar year; produced 3D maps and thermal imagery
- **Challenges Encountered:** Strong winds and downdrafts exceeded S2 capabilities; power consumption on 20-mile ingress; extensive flight planning (months of prep)
- **Future Application:** Routine global volcano monitoring with automated wind-aware flight planning to reduce mission planning burden and expand operational envelope

### 2. Hurricane Sampling
- **Customer:** NOAA Weather and Post-Observation (WPO) group
- **Platform:** S0 tube-launched from NOAA P3 aircraft
- **Mission:** In-situ atmospheric data collection inside/near hurricane cores
- **Status:** Design validation flights scheduled March 2023; operational deployment during hurricane season with 6-8 aircraft
- **Requirements Addressed:** Extreme precipitation tolerance, extended range communications, automated deployment control

### 3. Soil Moisture Mapping
- **Program:** NOAA WPO SPLASH campaign (Spring Long-term Soil Moisture Mapping for Hydrology)
- **Platform:** BST E2 quadcopter with L-band radiometer
- **Operations:** 12 total flights conducted Oct 18-19, 2022; mapping 6 study areas
- **Data Collection:** 
  - Altum optical data at 400 ft AGL (120m) for NDVI and thermal
  - Radiometric L-band brightness temperature at 180 ft AGL (55m)
  - Footprint resolution: 180 ft (55m) diameter
- **Validation:** Comparison with ground probe measurements (7cm depth) shows good agreement; radiometer captures broader spatial averaging while in-situ probes resolve fine features (rivers/streams)
- **Remaining Deployments:** 3 of 7 total scheduled for April, June, September 2023
- **Improvements Made:** Real-time radiometer display/processing (replaced 11 voltage regulators due to noise), removed thermal drift source, achieved ~5x noise reduction overall

### 4. Air Quality & Atmospheric Science
- **Potential NASA Customers:** Tropospheric Chemistry Program (TCP), Applied Sciences Air Quality Program, CALIPSO, Aura, CATS, OCO-2/3, Earth Ventures programs
- **Applications:** Model validation, improved accuracy for dispersion models, volcanic ash hazard assessment, pollution alerts, toxic release warnings, wildfire smoke monitoring
- **Advantage Over Current Methods:** UAS operate in airspace hazardous for crewed aircraft; provide in-situ data where satellites have limitations (infrequent coverage, cloud masking, coarse resolution)

### 5. Wildfire Monitoring & Support
- **Potential Customers:** USGS, DOE, National Weather Service
- **Capability:** Operations in particulates and severe turbulence of wildfire environments
- **Platform Flexibility:** S0, S2 variants applicable

### 6. Calibration & Validation Missions
- **Application:** Satellite sensor calibration (ASTER, MODIS, AIRS, OMI)
- **Hardware:** Video-equipped S0 aircraft for imaging validation
- **Milestones:** 2x S0 calibration missions Q2 2022; 6x video S0 aircraft Q3 2023

## Key Results (Technical Accomplishments)

### Completed in This Phase:
1. ✓ All NASA Phase III deliverables completed
2. ✓ NOAA WPO Y1 soil moisture mapping deliverables completed
3. ✓ NOAA WPO Y1 hurricane sampling deliverables completed
4. ✓ S0 mechanical design iterations: new waterproof heat sink, deployment tube, release actuator with 2-way comms
5. ✓ Antenna redesign and anechoic chamber testing (10dB out-of-band noise reduction achieved)
6. ✓ Waterproof wind probe design completed with clear-air and rain-tunnel validation (ports remain unclogged vs. clogging in baseline)
7. ✓ Radiometer improvements (5x noise reduction, voltage regulator replacement, thermal drift elimination)
8. ✓ Soil moisture data validation against ground truth (October 2022 flights, 6 study areas)
9. ✓ Wind-aware path planning algorithm development underway (inertial vs. wind frame comparison validated)

### Quantified Performance Gains:
- **Heat Sink Thermal Performance:** 34°C @ 60W cruise, 40°C @ 125W high-power (target: <100°C)
- **Antenna VSWR Improvement:** 1.5-2.5 range, improved efficiency over baseline
- **Dropsonde Interference Reduction:** 10dB reduction by frequency optimization
- **Wind-Aware Navigation:** Reduction from 40°+ bank angles to 15-25° in strong wind scenarios
- **Radiometer Noise Reduction:** ~5x improvement post-calibration and hardware fixes
- **Soil Moisture Measurement Correlation:** Good agreement with in-situ probes in accessible areas (footprint limitations expected and acceptable)

### Ongoing/Planned:
- S0 wind tunnel testing (Embry-Riddle, Feb 20th week, 1-2 days)
- March 2023 S0 validation flights before NOAA P3 hurricane season deployment
- Wind frame path planner flight testing (months ahead)
- UI data visualization and XML struct framework implementation
- Link margin improvements for 200 ft altitude operations at 150nm range

## Notable Details

### Partnership & Customer Commitment:
- **Investor Parties:** NASA Ames, NOAA WPO (