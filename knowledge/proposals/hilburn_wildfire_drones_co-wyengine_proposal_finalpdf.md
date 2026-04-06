# Wildfire Sensing and Prediction for Community Resilience

## Document Metadata
- **Type:** NSF proposal / grant application
- **Client/Agency:** National Science Foundation (NSF) CO-WY Climate Resilience Engine Use-Inspired Research and Development Grant Program
- **Program/Solicitation:** NSF CO-WY Engines Use-Inspired Research and Development
- **Date:** Submitted August 30, 2024
- **BST Products/Systems Referenced:** S2 UAS, E2 UAS, NightFOX sensor (NOAA), Soil Moisture sensor
- **Key Personnel:** 
  - Kyle Hilburn (Lead PI, CIRA/CSU) - Research Scientist/Scholar III
  - Chris Robertson (Co-Investigator, CSU Drone Center) - Drone Center Director
  - Maciej Stachura (Co-Investigator, Black Swift Technologies) - Chief Technology Officer

## Executive Summary
This proposal seeks to demonstrate the feasibility and value of drone-based remote sensing to improve wildfire detection, prediction, and community resilience in Colorado and Wyoming. The project will integrate drone observations (using Black Swift Technologies' S2 and E2 platforms carrying the NOAA NightFOX sensor and soil moisture sensors) with CIRA's advanced WRF-SFIRE coupled fire-atmosphere-smoke modeling system to provide high-resolution (30 m) data for wildfire monitoring and prediction, addressing critical gaps in satellite-based detection (375-2000 m resolution).

## Technical Approach

### Problem Being Solved
Current satellite fire detection has insufficient spatial resolution (375-2000 m) for wildfire modeling which requires 30 m resolution input data. Even next-generation geostationary satellites (2030s) will only provide 1000 m thermal imagery. Drones are the only foreseeable technology to provide the required spatial resolution.

### Proposed Solution
An end-to-end modeling system combining satellite-based (broad coverage, early warning) and drone-based (high spatial resolution) remote sensing to forecast weather, fuels, fire, and smoke at 30 m resolution. The approach targets three use cases:
1. **Pre-season fuel assessment** - Collecting high-resolution data on fuel loading
2. **Lightning-started fire detection** - Surveying areas with recent lightning outbreaks using satellite lightning detections for targeting
3. **Satellite hot-spot refinement** - Pinpointing and characterizing fires detected by satellites

### Key Technical Components
- **Data pipeline:** Established workflow to ingest drone data into forecasting system
- **Modeling system:** WRF-SFIRE (Weather Research and Forecasting Fire Spread) with WRFXPY workflow manager for automated forecast generation
- **Data assimilation:** Integration of drone observations into coupled fire-atmosphere-smoke modeling
- **Workforce quantification:** Assessment of personnel needs at rural airstrips
- **Regulatory documentation:** Identification and mitigation of challenges in drone deployment timelines

### Performance Advantages Over Satellite Data
Figure 2 comparison (Granite Gulch Fire 2019) demonstrates:
- VIIRS satellite fire pixels (375 m) showed mean apparent temperature of 48°C
- NightFOX airborne sensor (28 m pixels) showed mean apparent temperature of 375°C with maximum of 600°C
- Result: Airborne data provides more accurate location specificity and better characterization of actively burning areas

## Products & Capabilities Described

### Black Swift Technologies Systems

**S2 UAS**
- Purpose: Carries NOAA NightFOX sensor for fire detection missions
- Configuration: Equipped to operate from rural airstrips
- Value commitment: $44,000
- Role: Primary platform for hot-spot characterization and lightning-started fire assessment

**E2 UAS**
- Purpose: Carries Soil Moisture sensor for fuel characterization
- Configuration: Dedicated platform for pre-season fuel assessment
- Value commitment: $28,000
- Role: Pre-fire season fuel loading data collection

### NOAA NightFOX Sensor (carried by S2)
- **Specification:** Multi-spectral payload including middle wavelength infrared (MWIR), short wavelength infrared (SWIR), and visible camera
- **Capabilities:** Detects and measures fire radiative power; characterizes actively burning areas with temperature measurements reaching 600°C
- **Spatial resolution:** 28 m pixel size vs. 375 m for satellite (VIIRS)
- **Value commitment:** $25,000
- **Advantage:** Can detect hotter temperatures due to smaller pixel size; provides more accurate fire location and behavior characterization

### BST Soil Moisture Sensor (carried by E2)
- **Purpose:** Pre-season assessment of fuel moisture conditions
- **Role in workflow:** Input to WRF-SFIRE modeling for fuel characterization
- **Value commitment:** $50,000

### WRF-SFIRE Modeling System (CIRA/CSU)
- **Current status:** Advanced from ARL 4 (prototype, 2019) to ARL 7 (functionality demonstrated, 2023)
- **Capabilities:** Coupled physical modeling of fire-atmosphere-smoke processes
- **Operational history:** >3,000 real-time forecasts produced since 2023
- **Integration:** WRFXPY workflow manager enables automated data ingestion, forecast generation, and web-based product delivery
- **Data assimilation:** Machine learning and Kalman filter techniques for fuel moisture modeling
- **Open-source:** Disseminated via GitHub (https://github.com/openwfm)

### CSU Drone Center Resources
- **DJI M350 UAS:** Equipped with thermal, LiDAR, and photogrammetry sensors ($46,000 value)
- **Christman Airfield:** 4,000-foot runway with FAA recognition including:
  - Beyond Visual Line of Sight (BVLOS) operations waivers
  - High-altitude flight permissions (up to 699 feet AGL)
  - Recognized Identification Area (RIA) status (no remote ID requirement)
  - Specialized research and UAS development permissions

## Use Cases & Applications

### 1. Pre-Season Fuel Assessment
- Compare drone-based fuel observations with LANDFIRE database and high-resolution satellite data (VIIRS, Maxar WorldView)
- Manual editing of fuel maps in Year 1, ramping to machine learning-based data fusion in Year 2
- **Benefit:** Updated, high-resolution fuel maps for improved modeling accuracy

### 2. Lightning-Initiated Fire Detection
- Deploy drones to survey areas with recent lightning outbreaks detected by satellite lightning mappers
- Addresses gap: Satellites cannot detect smoldering fires' heat; ground-based lightning detections provide targeting
- **Advantage:** Tolerates longer time lag between initial observation and drone deployment
- **Benefit:** Early detection before visible fire development

### 3. Satellite Hot-Spot Refinement
- Rapid response to satellite-detected fire locations
- **Challenge:** Time-sensitive; regulatory coordination required for rapid deployment
- **Benefit:** Higher-resolution characterization of fire extent and behavior for accurate prediction

### Geographic Context
- **Initial demonstration site:** Christman Airfield, Fort Collins, Colorado
- **Expansion plan:** Scale to rural airfields across Colorado and Wyoming
- **Economic impact:** Job creation and re-skilling in rural areas for drone operations and maintenance

## Key Results (Proposed/Anticipated)

This is a proposed Year 1 project; no actual results are reported. Expected deliverables by end of Year 1:

### Q1 (Jan-Mar 2025)
- Operational plan for flight demonstrations
- Drone and sensor hardware integration
- Communications system specification
- Forecasting system drone data ingest capability

### Q2 (Apr-Jun 2025)
- Completion of three demonstration flight scenarios (fuel, lightning, hot-spot)
- Revised operational plan based on lessons learned
- Semi-annual report

### Q3 (Jul-Sep 2025)
- Continued demonstration flights
- Initial evaluation of data and forecasts

### Q4 (Oct-Dec 2025)
- Comprehensive documentation of:
  - Concept(s) of operations
  - Timeliness of data quantification
  - Workforce needs assessment
  - Regulatory challenges and solutions
  - Final evaluation of data and forecasts

## Notable Details

### Competitive Landscape
- **Wildfire modeling competitors:** Technosylva's Wildfire Analyst (models only, not sensors)
- **Fire monitoring competitors:** Robotics Cats LookOut cameras, Optect flame detectors (fixed locations only); DeltaQuad (drones without fire focus)
- **AI-based systems:** Lockheed Martin/NVIDIA (prone to false positives and hallucinations)
- **BST advantages:**
  - American-made drones
  - NightFOX sensor developed in Colorado
  - Physics-based modeling avoids AI hallucination issues
  - Centralized equipment maintenance vs. distributed camera networks

### Stakeholders
- National Weather Service (beginning integrated warning team approach)
- U.S. Forest Service
- Bureau of Land Management
- National Park Service
- Colorado Division of Fire Prevention and Control

### Intellectual Property & Commercialization
- **Commercial opportunity:** Drone and sensor hardware for wildfire monitoring
- **Open-source components:** WRF-SFIRE modeling system, WRFXPY workflow manager (GitHub dissemination following open-source principles)
- **Follow-on funding paths:** NASA FireSense Program, USDA SBIR

### Project Budget
- **Total NSF request:** $296,224
- **Leveraged resources:** ~$297,000 (approximately 1:1 match)
  - CIRA/CSU: $101,000 (HPC cluster, NAS storage)
  - Black Swift Technologies: $147,000 (NightFOX sensor, S2, E2, soil moisture sensor)
  - CSU Drone Center: $49,000 (DJI M350, airfield access)
- **Subaward to Black Swift Technologies:** $100,000 (data collection and provision)

### Team Structure
- **Kyle Hilburn (CIRA/CSU Lead PI):** Project management, WRF-SFIRE data assimilation leadership, team coordination
- **Chris Robertson (CSU Drone Center):** Drone operations, airfield logistics, regulatory compliance
- **Maciej Stachura (Black Swift Technologies CTO):** Drone equipment, sensor technology, technical issues

Weekly virtual meetings and monthly in-person/site visit coordination planned. CIRA sub-team coordination via weekly in-person meetings.

### Social/Behavioral/Economic (SBE) Component
- Year 1: Collaboration with NOAA Social/Behavioral/Economic Scientist for:
  - Quantitative financial impact assessment
  - Rural/tribal/community engagement strategy
- Year 2+: Planned expansion of social science component
- DEI focus: Assessment using Gartner Inclusion Index (seven dimensions: fair treatment, integrating differences, decision-making, psychological safety, trust, belonging, diversity)

### Scientific Foundation
- Builds on existing funding: NASA grants (80NSSC19K1091, 80NSSC22K1717, 80NSSC23K1344) and NOAA grant (NA22OAR4050672I)
- Responds to identified stakeholder needs from NASA ARMD and NASA SMD Wildfire Stakeholder Engagement Workshops (2021-2022)
- Supports NASA Earth Science to Action Strategy and NOAA's Next Generation Fire System integration

### Risk Mitigation
- **Primary challenge:** Regulatory time lag between identification and deployment
- **Mitigation strategy:** Three use cases with varying time sensitivities (vegetation assessment: low; lightning: medium; hot-spot: high) to identify bottlenecks and solutions