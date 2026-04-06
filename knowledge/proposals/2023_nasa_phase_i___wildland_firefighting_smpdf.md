# UAS Data Assimilation for Improved Wildland Fire Fighting Decision Support

## Document Metadata
- Type: NASA SBIR Phase I Proposal
- Client/Agency: NASA (Earth Science Division)
- Program/Solicitation: NASA SBIR 2023-I, Topic A3.02-1718
- Date: March 13, 2023 (created); September 22, 2023 (modified)
- BST Products/Systems Referenced: S0 VTOL UAS, SwiftTab User Interface, SwiftFlow multi-hole probe
- Key Personnel: Dr. Jack S. Elston (PI, CEO/Co-founder), Dr. Maciej Stachura (Lead Engineer, CTO), Dr. James Pinto (NCAR Lead)

## Executive Summary
Black Swift Technologies proposes a pilot study to improve wildland firefighting safety by collecting targeted UAS observations near active fires and assimilating them into advanced meteorological models using data assimilation techniques. The goal is to generate high-resolution, accurate low-level wind and turbulence guidance products that support safe aerial firefighting operations (including nighttime flights) and enable integration of crewed and uncrewed aircraft in complex terrain.

## Technical Approach

**Core Innovation:** Deploy strategically-positioned weather-sensing UAS (S0 platform) to collect atmospheric observations (3D winds, pressure, temperature, humidity) near wildland fires. These observations will be assimilated using NCAR's Ensemble Kalman Filter (EnKF) approach to generate 4D gridded analyses of low-level winds and turbulence. Results will be integrated into existing wildfire management tools (primarily ATAK—Android Team Awareness Kit).

**Key Technical Elements:**
1. **Ensemble Sensitivity Analysis** - Use high-resolution ensemble simulations of past fires (Calwood Fire, Four Mile Canyon Fire) to identify areas of greatest forecast uncertainty and optimal UAS sampling locations
2. **Data Assimilation** - NCAR will perform Observing System Experiments (OSEs) using EnKF tailored for UAS observations to quantify impact on wind/turbulence predictions
3. **Real-Time Integration** - Develop standardized interfaces to feed meteorological products into ATAK and other wildfire management systems
4. **Multi-UAS Coordination** - Establish operational protocols for simultaneous operation of multiple S0 platforms in complex terrain and near active fire zones

**Mitigation of Operational Constraints:**
- Early flights will occur outside Temporary Flight Restriction (TFR) boundaries or at night when crewed aircraft not operating
- Leverage existing FAA Certificates of Authorization and NASA flight safety approvals
- Partnership with Colorado's Center of Excellence for Advanced Technology Aerial Firefighting to coordinate permissions

## Products & Capabilities Described

### S0 VTOL UAS
- **Description:** Small, rugged, purpose-built atmospheric research platform developed in partnership with NOAA and Air Force
- **Specifications:**
  - Weight: 1.8 kg
  - Wingspan: 1.5 m
  - Cruise time: 60 minutes
  - Propulsion: Electric
  - Launch type: Vertical Takeoff and Landing (VTOL)
  - Communication range: 10 km
  - Operational ceiling: 4,500 m (15,000 ft) AGL
  - Payload: 3D inertial winds, pressure, temperature, humidity
  - Sensor rate: 100 Hz
- **Proposed Use:** Primary platform for gathering targeted meteorological observations in vicinity of wildland fires; capability to operate in harsh environmental conditions (hurricanes, convective storms, wildfire zones)
- **Key Advantage:** VTOL capability enables launch/recovery in rugged, complex terrain typical of wildfire regions in intermountain west; can operate at night when crewed aircraft grounded

### SwiftFlow Multi-Hole Probe (Sensor)
- **Description:** Custom-designed 3D wind measurement instrument; 50g weight
- **Specifications:**
  - Wind velocity resolution: 0.03 m/s
  - Wind velocity accuracy: 0.29 m/s
  - Temperature range: -40°C to 85°C
  - Temperature accuracy: ±0.3°C
  - Pressure resolution: 0.012 mbar
  - Pressure accuracy: 1.5 mbar
  - Relative humidity range: 0-100% RH
  - Humidity accuracy: ±1.3% RH
- **Proposed Use:** Primary sensor for collecting 3-component wind measurements, PTH (pressure-temperature-humidity) data during S0 flights

### SwiftTab User Interface
- **Description:** Android-based ground control system developed by BST; designed for safety-critical UAS operations with minimal operator overhead
- **Features:** Simplifies data display to essential information; designed for multi-UAS operations; minimizes operator workload during emergencies
- **Proposed Use in Phase I:** Will be extended for compatibility with ATAK data exchange; will demonstrate real-time weather/wind display, scalar value plotting, geo-located shape display (fire perimeter)
- **Phase II Goal:** Provide enhanced capabilities to ATAK application

### Related Systems Referenced
- **S2 UAS:** Mentioned in context of ongoing NightFOX project with NOAA over prescribed burns and active fires
- **ATAK (Android Team Awareness Kit):** Open-source software developed by Air Force Research Laboratory; provides geospatial data, communications, and situational awareness; being actively developed with input from Center of Excellence for Advanced Technology Aerial Firefighting; BST will extend to display wind/turbulence information

## Use Cases & Applications

### Primary Use Case: Wildland Firefighting Decision Support
- **Problem Addressed:** Fatal 2021 air tanker crash (NTSB CEN22FA035) attributed to undetected low-level turbulence; current weather services fail to capture fine-scale wind structures and turbulence associated with fire effects
- **Operational Context:** Support safe operations of slurry bombers, spotter aircraft, and reconnaissance platforms both day and night; enable safe crewed-uncrewed aircraft coordination; provide path-finding for nighttime operations
- **Specific Application:** Generate real-time maps of where aircraft can safely operate based on their capabilities; warn of current turbulence; serve as ground truth for model validation
- **Geographic Focus:** Front Range of Colorado foothills (Boulder County); complex terrain typical of intermountain west

### Secondary Applications Identified:
1. **Fire Weather Forecasting & Fire Spread Prediction** - Wind/turbulence data inputs for improved fire behavior models
2. **Advanced Air Mobility (AAM)** - Low-altitude flight support in mountainous/urban environments
3. **Package Delivery with UAS** - Wind hazard awareness for commercial operations
4. **General Aviation Safety** - Expanding beyond wildfire to broader national airspace users
5. **Volcano Monitoring** - Leveraging S0 capability to operate in hazardous particulate environments

## Work Plan & Objectives

### Four Primary Objectives:

**Objective 1: Develop Automated UAS Sampling Strategies**
- Use offline high-resolution ensemble simulations of past fires (Calwood Fire, Four Mile Canyon Fire)
- Employ ensemble sensitivity analysis to identify areas of greatest forecast uncertainty
- Determine optimal profiling locations, cadence, spacing for weather-sensing UAS
- Develop standardized interface for tasking UAS with missions

**Objective 2: Assimilate UAS Observations & Assess Impact**
- Conduct actual UAS flights (1-2 high-risk fire days) in Boulder County foothills
- Use NCAR's EnKF framework for data assimilation
- Perform Observing System Experiments (OSEs) to quantify added value of UAS measurements
- Develop plan to transition to real-time data assimilation capability

**Objective 3: Develop Integration Interfaces**
- Create interfaces for safe operation of weather-sensing UAS near active fires
- Develop data exchange interfaces between UAS systems and Team Awareness Kit (TAK)
- Integrate wind/turbulence hazard information into ATAK
- Define all necessary data formats and protocols

**Objective 4 (Implicit): Commercial Viability Assessment**
- Conduct preliminary market research
- Identify Phase II/III funding sources and matching funds
- Engage stakeholders (UTM developers, commercial UAS companies, state/local governments, weather providers)

### Seven Task Breakdown:

**Task 1. UAS Sampling Strategies** - Ensemble sensitivity analysis on past fires to identify optimal observation locations; focus on areas of greatest forecast uncertainty

**Task 2. Multi-UAS Integration into Wildfire Space** - Determine interfaces, permissions, operational protocols for simultaneous operation of up to 3 S0 platforms; leverage existing FIREX-AQ/NightFOX permissions; create actionable plan for expanded daytime operations in Phase II

**Task 3. Gathering & Assimilation of UAS Measurements** - Conduct targeted atmospheric measurements with S0 during high-risk fire days; flights leveraged from other funded projects with data-sharing agreements in place

**Task 4. Assessment of Forecasting Improvements for 3D Wind & Turbulence** - NCAR performs data denial experiments (OSEs); compares UAS-assimilated forecasts against independent truth data (vertical wind profiles from separate UAS, surface station observations); measures improvement in wind prediction accuracy and turbulence representation

**Task 5. Integration of UAS Meteorological Observations into Wildfire Operations** - Develop interfaces for feeding wind/turbulence data into wildfire management tools; produce document outlining necessary interfaces, data formats, stakeholder requirements; demonstrate integration using ATAK; leverage BST SwiftTab experience to extend ATAK capabilities

**Task 6. Explore Commercial Potential & Product Viability** - Preliminary market research; identify funding sources; engage stakeholders early

**Task 7. Prepare & Submit Reports** - Interim and final technical reports per contract requirements

### Project Schedule & Milestones (6-month Phase I):

**Milestone 1:** Develop algorithms/methods for automatically generating UAS sampling patterns based on forecast models and observations

**Milestone 2:** Produce document detailing requirements, risks, and mitigation for operating S0 UAS in wildfire response

**Milestone 3:** Gather data for 1-2 high-risk fire days with S0 UAS from ensemble-identified optimal locations

**Milestone 4:** Produce report quantifying improvement in low-level wind predictions afforded by UAS data assimilation

## Partnership & Collaboration Structure

**Primary Partners:**
- **NCAR/RAL (National Center for Atmospheric Research / Research Applications Laboratory)**
  - Leads data assimilation experiments using EnKF approach
  - Conducts ensemble sensitivity analyses
  - Performs observing system experiments
  - Lead: Dr. James Pinto (30+ years atmospheric science experience; 6 years Science Deputy for Aviation Applications Program)

- **Colorado Center of Excellence for Advanced Technology Aerial Firefighting (CoE)**
  - Facilitates permissions for UAS operations near/in active fire zones
  - Provides operational guidance and wildfire management requirements
  - Advises on integration with existing incident command systems
  - Actively involved in ATAK development

**Secondary Partnerships/References:**
- **Autonodyne** - UTM/airspace management software developer; offered to provide integration support and serve as potential Phase II subcontractor for wildfire-centric platform development
- **ATAK Product Center / TAK Program** - Maintains open-source ATAK software; coordination with civilian CivTAK development

## Key Results (from Related Work)

**Existing NCAR Validation Data:**
- Previous NCAR DA experiments (Jensen et al. 2021, 2022) demonstrated significant improvement in wind predictions when UAS data assimilated
- Example: Saguache Canyon drainage wind case (July 19, 2018) - UAS DA correctly predicted flow reversal at 8:30 UTC that was missed in data-denial runs; captured wind evolution 08:00-11:30 MDT
- Turbulence proxy metrics (vertical velocity distributions) showed improved representation with UAS DA, particularly in capturing broadening of distribution during late morning hours indicating more intense updrafts/downdrafts

**BST Operational Track Record:**
- 140+ FAA Certificates of Authorization maintained across CO, KS, NE
- 5 successful NASA Airworthiness Flight Safety Review Board (AFSRB) and Flight Readiness Review (FRR) process completions
- Completed field operations including: supercell tornado intercepts (VORTEX2), Arctic operations, multi-aircraft coordination, beyond-line-of-sight, high-altitude mountainous mapping
- Ongoing NightFOX project with NOAA over prescribed burns and active wildfires with S2 platform

## Notable Details

### Competitive Advantages & Innovation:
- **