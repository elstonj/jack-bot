# 2016_NASA_CCRPP___Volcano___Q5_Interim_Report_sm.pdf

## Document Metadata
- Type: Quarterly Demonstration Report (Q5)
- Client/Agency: NASA (CCRPP - Commercial Cargo and Crew Program Runner)
- Program/Solicitation: NASA SBIR Phase III-e; Contract Number 80NSSC22CA192; Topic 2022-1-1118
- Date: August 2023
- BST Products/Systems Referenced: S0, S2, S2-VTOL (S3), SwiftCore, SwiftTab, E2, 9-hole multi-hole turbulence probes (MHTP), Multi-hole Probe (MHP)
- Key Personnel: Jack Elston (PI/Principal Investigator), Maciej Stachura (Lead Engineer), Elston J.

## Executive Summary
This quarterly report documents Black Swift Technologies' Phase III continuation progress on developing ruggedized UAS for scientific data gathering in harsh environments. Building on successful Phase II-e volcano missions, BST has advanced intelligent flight algorithms, user interfaces, and manufacturing processes for the S2 and new S3 VTOL variants while conducting operational missions in hurricanes, volcano observations, and soil moisture mapping with NASA and NOAA partners.

## Technical Approach

### Core Innovation
The project addresses automation for extreme-environment operations. Key challenge: Phase II-e Makushin volcano mission revealed that while the S2 flew 4 successful missions, several had to turn back due to excessive propulsion power consumption on 20-mile ingress or wind exceeding aircraft capabilities. Flight planning was extremely time-consuming.

**Solution strategy:**
1. **Intelligent flight in strong winds** - Real-time wind assessment combined with predictive modeling to minimize energy usage; implemented in SwiftCore firmware
2. **User interface improvements** - Flexible payload telemetry display and control via SwiftTab app to accommodate interchangeable payloads
3. **Advanced mission planning** - Automated processes for terrain and communications management
4. **Improved manufacturability** - Simplify S2-VTOL (S3) construction to reduce cost and expand operational envelope with VTOL capability in strong winds

### Technical Systems
- **SwiftCore firmware** - Aircraft autopilot system with integrated eyewall-tracking controller and wind-aware navigation
- **SwiftTab app** - Ground control station interface with flexible payload integration
- **Multi-hole probe (MHP)** - 5-port sensor on aircraft nose measuring pressures at 100 Hz to estimate wind speed/direction
- **9-hole turbulence probes** - Advanced atmospheric measurement sensors for integration with external platforms (Altius UAS, P3 aircraft)

## Products & Capabilities Described

### S0 (Tube-Launched Reconnaissance Aircraft)
- **What it is:** Small tube-launched fixed-wing UAS optimized for deployment from P3 aircraft or ground-based systems
- **Specifications:**
  - Design flight duration: 1 hour minimum
  - Operational range achieved: 70+ nautical miles (goal: 150 NM)
  - Communications: Originally 115200 baud at 30 NM range; upgraded to 19200 baud achieving 70+ NM; transmit power increased from 1W to 2W maximum
  - Payloads: Multi-hole turbulence probes, thermal cameras, sea surface temperature sensors, laser altimeters
- **2023 Hurricane Deployment:** 8 systems delivered to NOAA; 4 systems deployed (2 in Hurricane Nigel, 2 in Tropical Storm Tammy)
  - Tammy Flight 1: 67 minutes duration, 72 NM communications range, successful data collection in extreme conditions including low-altitude (<30m) eyewall observations
  - Tammy Flight 2: 19 minutes (partial mission, sensor obstruction)
- **Notable Achievement:** Despite aggressive control commands during eyewall tracking test, demonstrated structural robustness flying 70+ minutes with continuous wing-wagging in tropical storm

### S2 (Terrain-Aware Aircraft)
- **What it is:** Small fixed-wing UAS designed for extended range operations in complex terrain and difficult weather
- **Use cases:** Volcano monitoring, soil moisture mapping, beyond-visual-line-of-sight (BVLOS) operations
- **Achievements:**
  - Makushin Volcano (Alaska, Phase II-e): 4 successful missions, achieved only visual observations of target volcano that calendar year
  - Generated 3D maps and orthomosaics with thermal data overlay
  - Demonstrated: terrain navigation, communication through complex topography, high-altitude operations
- **Challenges:** 20-mile ingress consumed excessive power; encountered winds exceeding aircraft capabilities; required months of flight planning preparation

### S2-VTOL / S3 (Vertical Takeoff and Landing Variant)
- **What it is:** VTOL variant enabling launch/landing in strong winds and obstacle-dense areas
- **Advantages:** Eliminates runway requirements; enables operations from small or complex terrain areas
- **Status:** Prototype tested in Phase II-e; current effort focuses on simplifying construction and reducing price
- **Planned deployments:** Chile volcano observation mission Q1 2024

### E2 (Soil Moisture Mapping System)
- **What it is:** Small fixed-wing UAS configured with radiometer and multispectral/thermal camera payload
- **Specifications:**
  - Payload: Altum multispectral/thermal camera + L-band radiometer
  - Mission profile: Two coordinated flights per area—one with multispectral/thermal, one with radiometer
  - Data products: NDVI maps, ground temperature maps, digital elevation models (DEM), L-band brightness temperature maps, soil moisture percentage maps
- **2023 Deployment:** NOAA WPO SPLASH project, September-October campaigns
  - Location: Rocky Mountain Biological Laboratory (RMBL), Crested Butte, Colorado
  - Mission success: 24 total flights across 6 areas, mapped twice each (September and October)
  - Data demonstrates seasonal pond drying and soil moisture variability
  - New radiometer revision (Rev. D) under development to eliminate pre-flight calibration step

### Multi-Hole Turbulence Probes (MHTP) / 9-Hole Probes (MHP)
- **What it is:** Advanced atmospheric measurement sensors with 5 or 9 pressure ports
- **Capabilities:** Measure wind speed and direction at high frequency (100 Hz); integrated atmospheric physics provide true airspeed, angle of attack/yaw
- **2023 Deployment (Altius UAS):**
  - 4 probes delivered to NOAA for Altius integration
  - 2 Tropical Storm Tammy flights: 58 minutes and 37 minutes respectively
  - Performance: Successfully operated in significant rain and storm conditions
  - Data undergoing quality control; preliminary analysis shows capability despite interface unit mismatch issues

## Use Cases & Applications

### 1. Hurricane Sampling (NOAA Weather and Pressures Operations)
- **Mission:** Eyewall tracking and meteorological data collection in tropical cyclones
- **Platforms:** S0 deployed from NOAA P3 aircraft; data integration with AVAPS dropsondes
- **2023 Operations:**
  - Hurricane Nigel (Category 2): 2 deployment attempts; both failed due to parachute latch QA issue (resolved)
  - Tropical Storm Tammy: 4 S0 deployments + 2 Altius probe flights; 2 successful S0 missions
- **Scientific payload:** Meteorological sensors (temperature, humidity, pressure, wind), sea surface temperature, laser altimeter for wave height, multi-hole probe turbulence data
- **Eyewall tracking algorithm:** Real-time wind measurement identifies eyewall ridge (highest windspeed peaks on either side of eye); controller performs left-right turns to maintain track along high-wind ridge
  - Simulation results: Mean Absolute Error 1571 meters, tracking bias 335 meters outside optimal trajectory at 500m MSL
  - Configurable controller parameters for different mission profiles (intercept eye, track maximum winds, follow rain bands)

### 2. Volcano Observations (USGS/NASA)
- **Location:** Makushin Volcano, Alaska (Phase II-e); planned Chile deployment Q1 2024
- **Mission:** In situ observations of volcanic activity, gas emissions, thermal features
- **S2 achievements:** 3 specialized payloads developed during Phase II-e
  - Generated 3D maps and orthomosaics with thermal overlays
  - Achieved only visual observations of target volcano during calendar year
  - Navigation through complex terrain and beyond-visual-line-of-sight communication
- **Challenges:** Multi-month flight planning required; frequent wind assessments during mission; communication system limitations; terrain navigation complexity
- **Future:** S3 VTOL variant planned for Chile mission to enable launch/landing at high-altitude, obstacle-dense summit areas

### 3. Soil Moisture Mapping (NOAA WPO SPLASH Campaign)
- **Location:** Rocky Mountain Biological Laboratory, Crested Butte, Colorado
- **Mission:** Map soil moisture spatial variability across mountain meadows and wetland areas using dual-flight approach
- **E2 payload configuration:**
  - Flight 1 per area: Altum multispectral/thermal camera → NDVI, thermal, DEM maps
  - Flight 2 per area: L-band radiometer → brightness temperature, corrected for terrain slope
  - Combined analysis: Soil moisture percentage maps integrating radiometer, NDVI, thermal, and soil type data
- **2023 Results:** Seasonal monitoring September-October
  - Avery sites: Clear dry-down trend between months; some October data affected by snow on eastern edge
  - Kettle Ponds: Seasonal ponds filled from spring snowmelt, drying through fall (distinct signature September, mostly dry October)
- **Science validation:** Demonstrates capability for routine, high-resolution soil moisture monitoring in complex mountain terrain

### 4. Methane Emissions Detection
- **Application:** Oil and gas facility monitoring
- **Capability:** S2 with trace gas payloads can measure facility-level and sub-facility-level emissions
- **Recent activity:** Demonstration flight completed; commercialization discussions ongoing
- **Market potential:** Commercial service offering for emissions monitoring and reporting

## Key Results (Q5 Report Period)

### Technical Accomplishments Completed
1. **NASA Phase III matching funds:** All deliverables completed
2. **NOAA WPO soil moisture mapping:** Year 1 deliverables completed; 24 flights mapping 6 areas twice (September-October 2023)
3. **NOAA WPO hurricane sampling:** Year 1 deliverables completed; 8 S0 aircraft and 4 turbulence probes delivered; 4 S0 deployments in hurricanes; 2 Altius probe flights
4. **Intelligent flight algorithms:** Initial simulation environment for wind-aware flight testing completed; simplified wind-following controller tested in Tropical Storm Tammy
5. **Eyewall tracking:** Advanced algorithm developed, tested in simulation (700+ configuration grid search); implemented in firmware with configurable parameters
6. **User interface improvements:** SwiftTab updated with wind barbs scaling with zoom level
7. **S2-VTOL design:** Work begun on latest revision (S3) with simplified construction for manufacturability improvement
8. **Makushin volcano observations:** 5 successful flights completed using automated flight planning tools developed in this effort

### Magnetometer Calibration Improvement
- **Problem:** Wind measurement errors in clear air testing attributed to magnetometer calibration errors
- **Solution:** New QA method developed using full-orbit assumption (180-degree wind symmetry)
- **Result:** Retroactively corrected previous flight datasets; Tropical Storm Tammy data significantly cleaner after application

### Range Enhancement (S0 Communications)
- **Original:** 30 NM (clear air test baseline)
- **Achieved Q5:** 70+ NM (TS Tammy operation)
- **Technical approach:** 
  - Reduced baud rate 115200 → 19200
  - Increased transmit power 1W → 2W
  - Implemented packet compression (e.g., humidity: float → uint16, 50% bandwidth reduction)
  - Separated telemetry/command queues with dynamic prioritization
- **Goal:** 100-150 NM; requires further optimization (4.8k baud target for 4x range improvement)
- **Future approach:** Phase-of-flight telemetry rate variation, field elimination, automated pre-flight procedures

### Hurricane Mission Performance
**TS Tammy Flight 1 (67 minutes):**
- Full mission success, battery-