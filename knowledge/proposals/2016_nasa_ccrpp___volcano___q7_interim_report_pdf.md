# 2022-1-1118 - A Ruggedized UAS for Scientific Data Gathering in Harsh Environments

## Document Metadata
- Type: Quarterly Demonstration Report (Q7/Interim Report)
- Client/Agency: NASA (SBIR contract)
- Program/Solicitation: NASA SBIR Phase III, CCRPP (Commercialization, Competition, and Rapid Prototyping) Program; Contract Number 80NSSC22CA192
- Date: May 2023 (reporting on work through Q2 2024)
- BST Products/Systems Referenced: S0, S2, S2-VTOL (S3), SwiftCore, SwiftTab, E2
- Key Personnel: Jack Elston (PI), Maciej Stachura (Lead Engineer), Daniel Prendergast (last editor)

## Executive Summary
This interim progress report documents BST's continued development of ruggedized UAS systems for scientific operations in extreme environments. Building on Phase II-e work that achieved volcano observations in Alaska, the Phase III CCRPP effort focuses on automating flight operations in harsh conditions through intelligent flight controllers, improved user interfaces, enhanced manufacturability of VTOL variants, and integration with multiple customer missions (NOAA hurricane sampling, NOAA soil moisture mapping, USGS volcano observation).

## Technical Approach

### Core Innovation Strategy
BST is automating mission execution in extreme environments through:
1. **Intelligent flight control algorithms** that assess real-time environmental conditions and adapt flight paths to minimize energy usage
2. **Automated mission planning** accounting for terrain, communication limitations, and weather
3. **Improved manufacturability** of VTOL platforms to reduce cost and enable wider deployment
4. **Flexible payload integration** with real-time telemetry visualization for scientific data management

### Key Technical Objectives (Current Phase)
- Intelligent flight in strong winds for increased mission success (wind-aware flight planning)
- User interface improvements for scientific data management (SwiftTab app enhancements)
- Advanced mission planning for terrain and communication limitations
- Improved manufacturability of S2-VTOL (renamed S3)
- Updated S0 VTOL design for rugged environment deployment

## Products & Capabilities Described

### S0 (Small UAS)
- **What it is**: Smallest variant in BST's aircraft family; fixed-wing configuration
- **Specifications**: 
  - Endurance: 103 minutes demonstrated
  - Range: 120+ nautical miles (tested), 150 nmi projected achievable
  - Operational altitude: 500-5000 ft MSL during hurricane operations
  - Payload capacity for meteorological sensors (multi-hole turbulence probes, dropsondes)
- **Current use**: NOAA WPO hurricane sampling (18 systems being deployed for 2024 season); NOAA calibration missions
- **Recent updates**: 
  - Servo replacement (old servos experienced unacceptable noise causing 50% random control surface deflections; replaced with KST servos)
  - Communications overhaul for extended range (reduced baud rate from ~48,000 to 4,800; switched from frequency-hopping spread spectrum to narrowband TDMA)
  - Temperature sensor improvements (identified solar heating bias; aircraft reads warmer than dropsondes)
  - Humidity measurement validation (good agreement with dropsondes)
  - Wind measurement capability (turbulence probes showing good agreement with reference sondes)

### S2 (Medium UAS)
- **What it is**: Medium-sized fixed-wing aircraft designed for scientific payload integration
- **Specifications**: 
  - 20-mile ingress range capability (with power management concerns noted)
  - Wind capability limits exceeded during Alaska missions
- **Use cases**: 
  - Volcano observations (Makushin, Alaska - 4 successful missions in 2023)
  - Soil moisture mapping (NOAA WPO)
  - Methane detection and mapping (oil & gas facility demo completed)
  - Remote sensing with specialized payloads (thermal, photogrammetry)
- **Notable achievements**: 
  - Only visual observations of target volcano during calendar year 2023
  - Generated 3D maps and orthomosaics with thermal data of Makushin Volcano
  - Demonstrated capability for sub-facility level methane emissions resolution

### S3 (formerly S2-VTOL)
- **What it is**: VTOL variant with vertical takeoff/landing capability; addresses wind-limited launch/landing constraints
- **Status**: Functional prototype completed; first test flight in April 2024
- **Purpose**: 
  - Enable operations from very small or obstacle-dense areas
  - Launch/land even in strong winds
  - Greatly expand operational envelope vs. fixed-wing variants
- **Development focus**: Improving manufacturability and reducing cost for commercial viability
  - Electronics design refinement
  - Wing & tail composite improvements
  - Hover test validation completed
  - First production model design in progress
- **Future deployment**: Planned integration with volcano missions (Chile deployment postponed to early 2025; considering Popocatépetl in Mexico or Indonesian targets)

### S0 VTOL
- **What it is**: VTOL variant of the S0 aircraft
- **Status**: Updated design for rugged environment deployment; two units planned for ground-based observations
- **Purpose**: Ground-based remote sensing with vertical launch/land capability

### SwiftCore (Flight Control System)
- **What it is**: BST's firmware and flight control architecture
- **Capabilities**: 
  - Real-time wind assessment and predictive modeling integration
  - Automated flight path adjustment for energy optimization
  - Three hurricane-specific flight controllers: Eyewall Tracking, Inflow Measurement, Center Fix
  - Terrain-aware and communications-aware flight planning
- **Key features**:
  - Physics-based simulation integration (X-Plane extensions developed for validation)
  - Kinematic trajectory simulation for rapid controller evaluation
  - Multi-mode operation (heading hold, waypoint navigation, wind-relative control)

### SwiftTab (Ground Station Interface)
- **What it is**: Tablet-based ground station control and telemetry system
- **Recent improvements**:
  - Real-time payload telemetry visualization
  - Flexible display architecture accommodating interchangeable payloads
  - Hurricane control application UI with tabs for different flight controller access
  - AirOps integration showing aircraft and mission data to air crew and science team
  - Static IP ground station configuration
  - Automatic HDOBS (High-Density Observation data) retrieval
- **Benefits**: Reduced UAS operator workload; enables potential removal of UAS operator from required team in operational capacity
- **Operator controls**: Pre-flight and in-flight parameter adjustment; real-time controller status monitoring; override capability for emergency modes

### Payloads & Sensors

**Soil Moisture Mapping (NOAA WPO - Rev. D improvements)**:
- L-band Dual Coincident Ratio (LDCR) radiometer with digital correlator
  - Real-time in-flight calibration with interior references and adjustable wide temperature range
  - Better RFI (Radio Frequency Interference) mitigation
  - Better immunity to gain fluctuation and thermal drift
- New L-band antenna design:
  - 40° beamwidth (vs. 45° previous); higher resolution soil moisture
  - No tuning strips required; smaller UAS footprint; rapid manufacturing for scaling
- NDVI (Normalized Difference Vegetation Index) sensor:
  - Two-band (650nm, 810nm) reflectance measurement
  - Range: 2x Full Sunlight
  - Calibration uncertainty: ±5%
  - Temperature response: <0.1%/°C
  - Repeated measurement variance: <1%
- Thermal sensor (ambient-compensated infrared):
  - Range: -70°C to 380°C
  - Resolution: 0.02°C
  - FOV: 35°
  - Accuracy: ±0.3°C (22-40°C), ±0.5°C (0-60°C)
- Test results: NDVI shows very good correlation with reference Altum camera; thermal data shows larger bias (±5°C, within stated accuracy)

**Hurricane Sampling (NOAA WPO)**:
- Multi-hole turbulence probes (8 units for Altius integration; 2 units for Phase III)
- Video capability (6 equipped S0 aircraft for calibration)
- AVAPS antenna integration with noise filters

**Volcano Observation**:
- Thermal imaging payload
- Photogrammetry payload (camera for 3D reconstruction)
- Trace gas detection capability (methane mapping demonstrated)

**Meteorological**:
- Wind speed/direction measurement (multi-hole probes)
- Humidity sensors
- Temperature sensors (with solar heating compensation)
- Pressure measurement

## Use Cases & Applications

### Current/Completed Missions

**Makushin Volcano, Alaska (2023)**
- 4 successful missions; 5 flights to summit with 2 different payloads
- Achieved only visual observations of target volcano during calendar year 2023
- Deployed 20-mile ingress in extreme wind and downdraft conditions
- Some missions forced to turn back due to excess propulsion power requirements or wind exceeding S2 capabilities
- Generated 3D maps and orthomosaics with thermal data overlay

**NOAA WPO Hurricane Sampling (Ongoing)**
- 18 S0 systems being deployed for 2024 hurricane season
- Second ground control station being delivered for NOAA P3 N42 aircraft
- Clear air testing completed March 2024:
  - Range achieved: 120 nmi (150 nmi projected)
  - Communications validated with P3 at 10/30 degree bank angles and various orientations
  - Data compared favorably with IR dropsondes
  - Humidity agreement good; temperature reads slightly warm (potential solar heating); wind measurements good
- Flight time endurance: 103 minutes demonstrated
- Planned: hurricane center finding (Figure-4 pattern variant), eyewall tracking, inflow measurement patterns

**NOAA WPO Soil Moisture Mapping (Completed Year 1)**
- Sensor Rev. D development completed
- Test flights over Sod Farm (varied terrain and vegetation)
- NDVI comparison with Altum reference camera shows good correlation
- Thermal data comparison shows larger bias; further testing needed
- Flight-ready E2 UAS equipped with new sensors

**Chile Volcano Deployment (USGS)**
- Originally planned Q2 2024; postponed to early 2025 due to flight permissions
- Alternative targets under consideration: Popocatépetl (Mexico), Indonesian volcanoes

**Oil & Gas Facility Demonstration**
- Completed demo showing methane measurements across entire facility
- Sub-facility level emissions resolution demonstrated
- Ongoing work to develop as paid commercial service

### Potential NASA Applications
- Earth Science program integration (Tropospheric Chemistry Program, Air Quality, CALIPSO, Aura, CATS, OCO-2/3)
- Airborne field campaign support
- Volcanic and wildfire observations (JPL, NASA Ames collaboration)

### Potential Non-NASA/Commercial Applications
- USGS volcano monitoring
- DOE environmental monitoring
- National Weather Service operations
- Wildfire monitoring and support (hazardous particulate/turbulence environments)
- Oil & gas methane emissions monitoring
- Commercial market for multi-hole probe sensors

## Key Results (Technical Accomplishments)

### Completed Phase III Deliverables
- All NASA Phase III deliverables completed
- Y1 deliverables for NOAA WPO soil moisture mapping completed
- Y1 deliverables for NOAA WPO hurricane sampling completed
- Matching funds secured from NASA Ames, NOAA (two groups), USGS

### Hurricane Flight Controller Development

**Eyewall Tracking Controller**
- Two algorithms finalized and validated:
  1. **Alignment Controller**: Periodic turn to align aircraft heading with wind direction; uses optional OFFSET parameter to counteract storm inflow/outflow
  2. **Left-Right Controller**: Crosses eyewall alternately when decreasing windspeed trend detected
- Verified in Python trajectory simulation and X-Plane physics-based simulation
- Local flight test validation completed (Eyewall Tracking)
- Operational configurable parameters: 14 settings for fine-tuning (planned reduction for final version)
- Example trajectory: mean error of 1203 meters using Left-Right algorithm

**Inflow Measurement Controller**
- Leverages Eyewall Tracking algorithms in intercepting phase
- Aircraft spirals inward following wind direction (INTERCEPT_OFFSET = 0 degrees)
- Purpose: collect wind data on hurricane air