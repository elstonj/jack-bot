# Fire-Tech Proposal and Planning Document

## Document Metadata
- Type: Step 1 Proposal (Planning & Preparation Document)
- Client/Agency: NASA (Earth Science Directorate)
- Program/Solicitation: NASA NSPIRES 2022 - Wildland FireSense Project / FireTech solicitation (A.53)
- Date: Created July 7, 2022; Modified August 1, 2022; Step 1 Due August 2, 2022
- BST Products/Systems Referenced: S2 UAS, Soil Moisture Mapping (SMM) system, SwiftFlow probe
- Key Personnel: Jack Elston (last editor), Florian (manager at time of planning)

## Executive Summary
Black Swift Technologies proposes to deploy UAS-based technologies for operational wildfire management across pre-fire, active-fire, and post-fire phases. The proposal leverages NASA SBIR-matured systems (S2 UAS, SMM sensor, SwiftFlow probe) integrated with partner payloads for soil moisture mapping, atmospheric sensing, thermal imaging, and air quality monitoring, with coordinated field deployment in Colorado and California to provide near-real-time data products for fire management and modeling.

## Technical Approach

### Primary Systems & Technologies
1. **S2 UAS (Ruggedized Platform)**
   - Developed under NASA SBIR (NNX17CP13C)
   - Matured through Phase III and commercial deployments
   - Enables BVLOS operations with ADS-B out capability (coordinated with NASA Ames for airspace integration)
   - To be equipped with multiple payloads for fire applications

2. **Soil Moisture Mapping (SMM) System**
   - Developed under NASA SBIR (80NSSC18C0002)
   - UAS-based sensor system
   - Matured through Phase III
   - Orbital Micro Systems partner developing rapid extraction algorithms for near-real-time maps

3. **SwiftFlow Probe**
   - Developed under NASA SBIR (NNX17CP13C)
   - Wind and atmospheric sensing capability
   - Matured through testing over fire activity and analogous environments

### Fire-Specific Payloads (Partner-Developed)
- **NOAA Fire Line Thermal Sensor**: For active fire characterization and fire edge detection
- **NOAA Air Quality Sensors**: Modified versions of volcano-monitoring packages for downwind air quality assessment
- **High-Resolution 3D Wind Measurement System**: For combined remote and in situ fire parameter measurements

### Data Analysis & Integration Methodology
1. **Soil Moisture Applications**:
   - Pre-fire: Input to hydrology models for risk assessment
   - Post-fire: Soil integrity assessment for landslide threat modeling
   - Post-fire: Supplemental variable for flooding/runoff prediction (combined with saturation + storm data)

2. **Wind & Atmospheric Data**:
   - Integration into fire weather models in near-real-time
   - Boundary layer characterization (height, wind vectors, humidity)
   - Both pre-fire risk assessment and active-fire scenarios

3. **Fire Line Monitoring**:
   - Thermal sensor data combined with 3D wind measurements
   - Downwind air quality estimates
   - Support for fire suppression operations

4. **Near-Real-Time Data Distribution**:
   - Emphasis on rapid quicklook products via satellite, direct ground links, or relay through aerial assets (ER-2, Solar UAS)
   - Integration with fire weather models and digital twin projects

## Products & Capabilities Described

### S2 UAS
- **What it is**: Ruggedized, small unmanned aircraft system developed/manufactured by BST
- **NASA SBIR Heritage**: NNX17CP13C
- **Proposed use**: Multi-payload platform for sustained, coordinated wildfire monitoring across lifecycle phases
- **Enabling capability**: ADS-B out for BVLOS operations (coordinated with NASA Ames)
- **Operational history**: Has flown NOAA wildfire-specific payloads over controlled burns in Colorado (Boulder Parks and Open Space Forestry/Fire division)

### Soil Moisture Mapping (SMM) System
- **What it is**: UAS-mounted remote sensing system for soil moisture retrieval
- **NASA SBIR Heritage**: 80NSSC18C0002
- **Proposed uses**: 
  - Pre-fire: Hydrology modeling and risk assessment
  - Post-fire: Landslide threat assessment, flooding/runoff prediction
- **Enhancement**: Orbital Micro Systems partnership for rapid algorithm development enabling near-real-time products

### SwiftFlow Probe
- **What it is**: Wind and atmospheric sensing instrument
- **NASA SBIR Heritage**: NNX17CP13C
- **Characteristics**: Low-cost design, proven on multiple platform types (UAS, manned aircraft, aerostats, balloons)
- **Proposed use**: Pre-fire and active-fire atmospheric characterization for fire weather models

### NOAA Fire Line Thermal Sensor
- **What it is**: Thermal imaging payload developed by NOAA (Troy Thornberry team)
- **Proposed use**: 
  - Active fire characterization
  - Fire edge detection in smoke
  - Fire suppression support
- **Operational history**: Flown by BST on S2 over controlled burns in Colorado

### NOAA Air Quality Sensors
- **What it is**: Air quality monitoring payloads (adapted from volcano monitoring work)
- **Proposed use**: Downwind air quality sensing across all fire lifecycle phases

### SwiftCore (Implied)
- **Reference**: "SwiftCore" mentioned in metadata context; technical details not elaborated in this document

## Use Cases & Applications

### Pre-Fire Phase
- Risk assessment through boundary layer characterization and fuel moisture mapping
- Prescribed burn planning with high-resolution atmospheric and soil data
- Coordinated multi-platform observations for improved fire spread model initialization

### Active Fire Phase
- Real-time fire edge detection and characterization
- 3D wind field measurements for fire behavior modeling
- Downwind air quality and emissions monitoring
- Fire suppression support operations
- Digital twin development/refinement

### Post-Fire Phase
- Landslide hazard assessment via soil moisture and vegetation state mapping
- Flooding/runoff prediction from burn scar watersheds
- Ecosystem impacts and restoration planning
- Air and water quality monitoring

### Geographic Focus
- **Phase 1**: Colorado-based testing with local groups
- **Phase 2**: California expansion
- **Specific test sites identified**: 
  - SJSU Wildfire Interdisciplinary Research Center (Craig B. Clements) with Canyon Fire Test site (multiple 100-ft met towers)
  - Boulder Parks and Open Space (prior testing location)

## Notable Details

### Partnership Ecosystem
- **NASA Ames** (Alok Shrestha): Wildfire applications, flight permissions, real-time data integration, BVLOS airspace coordination
- **NASA GSFC** (Geoff Bland): Boundary layer observation, airspace integration
- **NOAA** (Troy Thornberry): Fire line thermal sensor development, air quality sensors, fire weather/fireline modeling expertise
- **Colorado Center of Excellence** (Ben Miller): Firefighting innovation and public safety community engagement
- **Orbital Micro Systems**: Soil moisture algorithm development for near-real-time capability
- **SJSU Wildfire Interdisciplinary Research Center**: Field testing and fire behavior/meteorology expertise

### Operational Considerations
- Emphasis on "field-ready product" through iterative end-user feedback
- Safety-focused coordination techniques to avoid interference with standard operations
- Transition from current NASA reliance on manned platforms (ER-2) toward fully autonomous UAS solutions
- Real-time data distribution critical for operational utility (mentioned as "very important" by management)

### Competitive Advantages / Unique Capabilities
- Ruggedized S2 platform with proven wildfire operation history
- Integrated suite of sensors (moisture, wind, thermal, air quality) addressing multiple fire lifecycle phases
- NASA SBIR Phase III maturation + commercial deployment validation
- Low-cost atmospheric sensing technology proven on multiple platform types
- NOAA partnership for specialized fire-specific instrumentation

### Proposed Innovations Addressing Solicitation
- Model-directed, coordinated autonomous observations from multiple vantage points
- Real-time data fusion and computational processing
- Machine learning/AI for new data product generation
- Seamless integration of spaceborne, airborne, and in situ assets
- Enhanced instruments for small spacecraft/aerial platforms with reduced mass/power

### Requirements Addressed
The proposal explicitly addresses NASA's stated needs for:
- High-resolution, sustained "staring" observations at critical targets
- Novel suborbital platform capabilities
- Next-generation unmanned platforms for wildfire management
- Real-time capability improvements
- Digital twin integration

## Step 1 Proposal Strategy Notes

### Key Elements for 4000-Character Submission
- Lifecycle stages: Pre-fire (risk assessment), active-fire (real-time management), post-fire (hazards & restoration)
- Team expertise: BST (UAS platform, SMM, SwiftFlow), NASA Ames/GSFC (integration, airspace), NOAA (fire instruments & modeling), Colorado CoE (end-user engagement), Orbital Micro Systems (algorithms)
- Targeted stakeholders: Fire managers, wildfire agencies, forestry services, research centers
- Data methodologies: Soil moisture for hydrology/landslide/flood modeling; wind/atmospheric integration into fire models; thermal fire characterization; air quality sensing
- Mission relevance: Directly supports Wildland FireSense Project goals for novel suborbital platforms enabling improved wildfire management

### Preparation Notes
- Emphasized need to include wildfire expert on team
- Reviewer recommendations to be submitted separately
- Florian (100% manager) role clarified; Alok to be listed as collaborator
- LIDAR and hyperspectral camera mentioned as possible future S2 payloads (noted but not primary focus)
- Document serves as planning reference; actual Step 1 submission compressed to 4000 characters

---

**Document Status**: Planning document for Step 1 proposal preparation. Step 1 due date was August 2, 2022. This document was last modified August 1, 2022, indicating final pre-submission review.