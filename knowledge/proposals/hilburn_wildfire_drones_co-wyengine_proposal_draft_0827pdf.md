# Wildfire Sensing and Prediction for Community Resilience

## Document Metadata
- **Type:** NSF Grant Proposal (draft)
- **Client/Agency:** NSF CO-WY Climate Engine Use-Inspired Research and Development Grant Program
- **Program/Solicitation:** NSF CO-WY Engines Use-Inspired R&D
- **Date:** August 27, 2024 (draft)
- **BST Products/Systems Referenced:** S2 drone, E2 drone, NightFOX sensor (NOAA), Soil Moisture sensor
- **Key Personnel:** 
  - Kyle Hilburn (Lead PI, CSU/CIRA)
  - Chris Robertson (Co-Investigator, CSU Drone Center Director)
  - Maciej Stachura (Co-Investigator, BST Chief Technology Officer)

## Executive Summary
This proposal seeks to demonstrate that drone-based remote sensing can provide high-resolution data (30 m) required for wildfire prediction and community resilience. While satellite fire detections provide early warnings at 375-2000 m resolution, wildfire modeling requires 30 m resolution data. The project will establish a concept of operations for three use cases (pre-season fuel assessment, lightning-started fire detection, and satellite hot-spot refinement), quantify workforce needs, and address regulatory challenges using drones operating from Christman Airfield in Fort Collins, Colorado.

## Technical Approach

**Primary Solution:** End-to-end modeling system integrating satellite-based and drone-based remote sensing for 30 m resolution forecasting of weather, fuels, fire, and smoke.

**Key Components:**
1. **Satellite data** provide early warnings over large coverage areas (GOES geostationary satellites)
2. **Drone-based sensors** provide spatial resolution to pinpoint locations and estimate fire behavior
3. **WRF-SFIRE modeling system** for data assimilation and wildfire prediction
4. **Data pipeline** for ingesting observations and producing forecasts
5. **Web-based visualization platform** for product delivery

**Three Use Cases:**
- **Pre-season fuel assessment:** High-resolution fuel loading data collection before fire season; comparison with LANDFIRE database and satellite data (VIIRS, Maxar WorldView); future machine learning-based data fusion
- **Lightning-started fire detection:** Using satellite-based lightning detection to target drone surveillance of areas with recent lightning strikes (tolerant of longer deployment times since satellites can't detect smoldering heat)
- **Satellite hot-spot refinement:** Rapid deployment to characterize fires detected by geostationary satellites, providing higher-resolution characterization for improved prediction

**Technical Advantages Over Satellite Alone:**
- Smaller pixels (28 m vs. 375 m) enable detection of hotter temperatures (375-600°C vs. 48°C mean)
- Better spatial specificity of fire locations and active burning areas
- Ability to operate in areas with poor road access, complementing human surveys

## Products & Capabilities Described

### Black Swift Technologies Contributions

**S2 Drone**
- Carries NightFOX sensor for thermal fire detection
- In-kind contribution: $44,000

**E2 Drone**
- Carries Soil Moisture sensor
- In-kind contribution: $28,000

**Soil Moisture Sensor**
- For fuel moisture assessment and wildfire modeling inputs
- In-kind contribution: $50,000

**NightFOX Payload (NOAA)**
- Multi-spectral sensor package: middle wavelength infrared (MWIR), short wavelength infrared (SWIR), visible camera
- Carried by S2 drone
- In-kind contribution: $25,000
- **Performance demonstrated:** Compared to VIIRS satellite data on Granite Gulch Fire (2019)
  - Mean temperature: 375°C (max 600°C) vs. satellite 48°C
  - Superior spatial resolution (28 m vs. 375 m)
  - Better definition of active fire areas

### CSU Drone Center Contributions

**DJI M350 Drone**
- Equipped with thermal, Lidar, and photogrammetry sensors
- In-kind contribution: $46,000

**Christman Airfield (CSU Resource)**
- 4,000-foot runway
- FAA Recognized Identification Area (no remote ID required for UAS)
- Part 107 waivers for: Beyond Visual Line of Sight (BVLOS), high-altitude flights to 699 ft AGL, specialized research/UAS development operations
- In-kind contribution: $3,000

### CIRA Contributions

**Haguespeak HPC Cluster**
- For WRF-SFIRE model execution
- In-kind contribution: $86,000

**Firet NAS Storage**
- For data storage
- In-kind contribution: $15,000

**WRF-SFIRE Modeling System**
- Coupled fire-atmosphere-smoke modeling platform
- Integrated with NOAA's Next Generation Fire System (NGFS)
- Produces 3000+ real-time forecasts since 2023
- Application Readiness Level advanced from ARL 4 (2019) to ARL 7 (2023)
- Open-source distribution via GitHub (https://github.com/openwfm)

**WRFXPY Workflow Manager**
- Automated data ingest, forecast execution, and product delivery to web
- Enables "push-button" operational forecasting

## Use Cases & Applications

### Primary Mission: Wildfire Prediction and Community Resilience

1. **Pre-Season Fuel Assessment (Time-Insensitive)**
   - High-resolution fuel loading characterization
   - Validation against LANDFIRE database
   - Comparison with high-resolution satellite data
   - Supports community risk assessment and mitigation planning

2. **Lightning-Started Fire Detection (Moderately Time-Sensitive)**
   - Targets areas with recent lightning strikes detected by geostationary satellites
   - Surveys for smoldering fires not yet detectable by satellites
   - Longer tolerance for deployment time lag
   - High value for early detection in remote areas

3. **Satellite Hot-Spot Refinement (Time-Sensitive)**
   - Rapid deployment to satellite-detected active fires
   - High-resolution characterization for accurate fire behavior prediction
   - Provides input data at 30 m resolution required for WRF-SFIRE modeling
   - Challenges: regulatory constraints on rapid deployment

### Secondary Applications
- Forest management
- Prescribed burn planning
- Incident response
- Smoke prediction and air quality forecasting

### Geographic Focus
- Year 1: Fort Collins, Colorado (Christman Airfield)
- Scalable to other rural airfields across Colorado and Wyoming
- Potential for national expansion

## Key Results (Proposal Basis, Not Yet Executed)

The proposal is a draft submitted in August 2024 for a one-year project planned to run Jan-Dec 2025. No results are yet available, but the proposal cites:

**Historical Performance (WRF-SFIRE System):**
- Advanced ARL from 4 to 7 between 2019-2023
- Producing 3,000+ real-time forecasts since May 2023
- Integrated with NOAA's Next Generation Fire System
- Running on CSU HPC resources via automated workflow

**Comparison to Existing Capabilities:**
- NightFOX airborne data vs. VIIRS satellite (Granite Gulch Fire, Aug 2019):
  - Thermal resolution: 28 m airborne vs. 375 m satellite
  - Temperature detection: 375°C mean airborne vs. 48°C mean satellite
  - Maximum temperature: 600°C airborne
  - Superior spatial specificity of active burning areas

## Notable Details

### Problem Statement
- Wildfire crisis: increasing frequency, size, intensity in U.S.
- Current satellite resolution (375-2000 m) insufficient for operational wildfire modeling (requires 30 m)
- Next-generation geostationary satellites (2030s) will only provide 1000 m thermal imagery
- Drones are "the only technology to provide required spatial resolution in the foreseeable future"
- National Weather Service seeking integrated warning team approach; currently contracts with private companies (Technosylva) for fire spread forecasting

### Stakeholders Identified
- National Weather Service (NWS)
- U.S. Forest Service (USFS)
- NOAA
- Bureau of Land Management
- National Park Service
- Colorado Division of Fire Prevention and Control
- Rural communities in CO/WY

### Competitive Landscape
- **Modeling:** Technosylva Wildfire Analyst (proprietary, non-operating sensors)
- **Fixed monitoring:** Robotics Cats LookOut cameras, Optect flame detection (stationary only)
- **UAVs for fire:** DeltaQuad (general-purpose, not fire-specific)
- **AI-based systems:** Lockheed Martin, NVIDIA (risk of false positives/hallucinations)
- **Platform:** Geospiza (local, decision-support focused)
- **Consulting:** Wildfire Defense Systems

**BST Competitive Advantages:**
- Physical modeling eliminates AI hallucinations
- American-made drones (BST)
- NightFOX sensor developed in Colorado
- Integrated end-to-end system (hardware + modeling + operations)

### Regulatory Challenges
- Time lag from fire detection to drone deployment identified as major challenge
- Three use cases specifically selected to accommodate varying regulatory/deployment time constraints
- Project will document regulatory bottlenecks and explore mitigation strategies
- Christman Airfield's existing FAA waivers (BVLOS, high altitude) reduce some constraints

### Economic Development Vision
- Job creation in rural Colorado/Wyoming for drone operations and maintenance
- Re-skilling workforce in rural areas
- 117 airports/airfields in CO/WY identified as potential "engines for economic growth"
- BST pursuing follow-on USDA SBIR funding
- Potential NASA FireSense Program follow-on support

### Intellectual Property & Commercialization
- **Proprietary:** Drone hardware (BST), specialized sensors, operational procedures
- **Open-source:** WRF-SFIRE modeling system and WRFXPY workflow manager distributed via GitHub
- Project explicitly seeks to "commercialize the drone and sensor hardware solutions"
- Drone-based products expected to have value beyond wildfire (forest management, prescribed burn planning, incident response)

### Partnership Structure
- **CIRA:** Modeling, data assimilation, web platform, NOAA coordination
- **CSU Drone Center:** Operations, airfield access, regulatory compliance
- **Black Swift Technologies:** Drone/sensor hardware, technical integration
- All three entities contributing significant in-kind resources ($297K leveraged against $296K requested budget)

### Project Timeline (Proposed)
- **Q1 (Jan-Mar 2025):** Hardware integration, system specification, flight prep
- **Q2 (Apr-Jun 2025):** Initial flight demonstrations, three use case testing
- **Q3 (Jul-Sep 2025):** Continued demonstrations, initial data evaluation
- **Q4 (Oct-Dec 2025):** Documentation, final report, concept of operations

### NOAA/Government Relationship
- Kyle Hilburn has advanced Application Readiness Level of WRF-SFIRE from ARL 4 to ARL 7 through NASA and NOAA funding
- CIRA has offices at 6 NOAA locations with 8+ years of relationship-building
- Integration with NOAA's Fire Weather Testbed (FWT)
- Real-time operational forecasting now running on CSU HPC resources

### Social Science Component
- Year 1: Collaboration with NOAA Social/Behavioral/Economic Scientist (SBES) on financial impact assessment and community engagement
- Year 2+: Planned expansion of social science component
- Inclusive engagement strategy aligned with NASA DEIA principles

---

**Budget Requested:** $296,224  
**Total Leveraged Resources:** $297,000 (roughly 1:1 match)