# A Ruggedized UAS for Scientific Data Gathering in Harsh Environments (Volcano Monitoring)

## Document Metadata
- Type: NASA SBIR CCRPP (Commercialization, Creativity, and Research Proliferation) Phase III Proposal
- Client/Agency: NASA Ames Research Center; NOAA (multiple groups); USGS
- Program/Solicitation: NASA SBIR 2022; CCRPP matching funds program; Proposal Number 2022-1-1118
- Date: 2016 submission (filed); Phase II-e completed September 2021 (Makushin volcano deployment); Phase III proposal for 2022-2024
- BST Products/Systems Referenced: S2 (fixed-wing UAS), S2-VTOL (vertical takeoff/landing variant), S0 (disposable hurricane sampler), SwiftCore Flight Management System (FMS), SwiftPilot autopilot, SwiftTab user interface, SwiftFlow probe
- Key Personnel: Dr. Jack S. Elston (Principal Investigator), Dr. Maciej Stachura (Lead Engineer), Josh Fromm (Mechanical Engineering Lead)

## Executive Summary
Black Swift Technologies proposes to mature UAS technologies developed under prior NASA SBIR funding by adding advanced autonomous flight planning for extreme wind environments, improved scientific data visualization interfaces, terrain and communication-aware mission planning, and manufacturing cost reductions (up to 30%) for the S2-VTOL platform. The effort combines customer investment from NASA Ames, NOAA, and USGS with CCRPP matching funds to enable routine operations in harsh environments including volcanic plume sampling, hurricane observation, and soil moisture mapping in mountainous terrain.

## Technical Approach

### Core Development Areas

1. **Intelligent Flight in Strong Winds**: Development of algorithms to calculate and navigate feasible flight paths in extreme wind conditions (lateral and vertical) using a priori mesoscale models and real-time in situ measurements. Includes online machine-learning-based flight time prediction with dynamic power reserve calculation to ensure safe BVLOS return-to-base capability. Critical for both S2-VTOL volcanic missions and S0 hurricane deployments where wind speeds frequently exceed the UAS maximum airspeed.

2. **Scientific Data Management UI**: Enhanced SwiftTab user interface to enable real-time monitoring and visualization of arbitrary sensor data in time-series or geographic/map formats. Allows operators and scientists to adjust flight paths in real-time based on live scientific data (e.g., trace gas concentrations on volcanoes). Addresses challenge of integrating ~20 different specialized payloads developed for various missions.

3. **Advanced Mission Planning (Terrain & Communications)**: Integration of digital elevation maps with aircraft performance models to automatically generate flight plans that safely avoid terrain while enabling close proximity operations to targets (volcanic vents). Coupling of radio line-of-sight models with terrain to prevent communication loss. Automated safe lost-comms waypoint recalculation to maintain signal during unscheduled deviations.

4. **S2-VTOL Manufacturing Optimization**: Design and process improvements to reduce build time and system cost by up to 30%, targeting a price point of $40,000 to expand market accessibility while maintaining performance in difficult environments.

### Technical Foundation
- SwiftCore FMS: Proprietary flight management system capable of logging up to 128 unique sensors; supports autonomous operations
- SwiftPilot autopilot: Handles autonomous takeoff/landing and wind-aware flight control
- Multi-hole turbulence probe (new IP): Cost-reduced 3D wind and atmospheric data measurement sensor

## Products & Capabilities Described

### S2 (Fixed-Wing UAS)
- **Description**: Small tactical UAS designed for harsh environments; gross takeoff weight <55 lbs with payload; endurance ≥1 hour; 15 km diameter operational radius
- **Use in Proposal**: Primary platform for volcanic gas monitoring (NASA Ames), soil moisture radiometer operations (NOAA SPLASH), and photogrammetry/thermal imaging campaigns
- **Specifications**: 
  - Payload capacity: up to 5 lbs
  - Demonstrated BVLOS operations to 15+ miles (20 miles tested at Makushin)
  - Operates in strong downdrafts (>2000 fpm tested), high-altitude turbulence, corrosive particulates
  - Operates to -40°C (Greenland deployment)
  - Approved Category 1 UAS (<55 lbs)

### S2-VTOL (Vertical Takeoff/Landing Variant)
- **Description**: Modified S2 with VTOL capability added during Phase II-e; enables launch/landing from minimal or obstacle-dense areas
- **Use in Proposal**: 
  - Primary NASA Ames deliverable for volcano monitoring missions
  - Prototype tested during Phase II-e; first operational mission planned March 2022 (Costa Rica)
  - Expected to expand operational envelope significantly for missions requiring rapid deployment to remote areas
- **Performance Gains**: Simplifies launch/landing logistics; enables operations from confined sites unsuitable for runway-dependent aircraft
- **Procurement Target**: Six aircraft planned for acquisition/development

### S0 (Disposable Hurricane Sampler)
- **Description**: Small, expendable UAS designed for deployment from manned aircraft (NOAA WP-3D); launched into tropical cyclones and severe weather
- **Use in Proposal**: 
  - NOAA hurricane observation missions
  - Will benefit from wind-navigation algorithms developed in CCRPP
  - Intended for air deployment with continuous command/control and data telemetry
- **Performance Goals** (Phase III objective):
  - Multi-hour duration
  - Communication range: 150+ nautical miles (WP-3D to S0)
  - Operates in severely turbulent tropical cyclone environments
  - Capable of reaching sampling areas where direct flight not feasible due to wind speeds exceeding airspeed
- **Procurement Target**: 8-14 aircraft planned (calibration, hurricane missions, video-equipped variants)

### Payload Suites

**Volcano Flux Sensor Suite**:
- CO₂ sensor (LICOR)
- SO₂ sensor (CityTech electrochemical)
- H₂S sensor (CityTech electrochemical)
- UV DOAS spectrometer with collimating optics
- Pressure, temperature, humidity sensors
- Upward-looking optical configuration for plume sampling
- Field-swappable nose cone integration

**Photogrammetry/Thermal Payload**:
- 24 MP RGB camera (Sony a5100 tested)
- FLIR Vue Pro R thermal camera
- Extended battery pack for enhanced endurance
- Demonstrated 1 km² mapping capability with orthomosaic and thermal overlay

**Soil Moisture/Remote Sensing Payload**:
- Lobe Differencing Correlation L-band Radiometer (LDCR)
- Surface imaging sensors
- Optional SwiftFlow probe (wind and thermodynamic measurements)

**Communications**:
- Iridium satcom package as backup data link
- Primary point-to-point wireless (demonstrated 15-20 mile BVLOS range)
- Integrated ground station architecture

### SwiftCore FMS & SwiftPilot
- Modular avionics suite supporting up to 128 sensor inputs
- Autonomous mission execution with in-flight replanning capability
- Real-time data logging to onboard storage
- Automated wind-aware flight control and power management
- Field-proven in extreme conditions (strong winds, downdrafts, high altitude, low temperature)

## Use Cases & Applications

### Primary Funded Applications

**1. NASA Ames Volcanic Observation (Makushin, future volcanoes)**
- Continuous monitoring of volcanic gas emissions (CO₂, SO₂, H₂S)
- Plume characterization and flux measurement
- Photogrammetric 3D mapping of calderas with thermal anomaly detection
- Validation/calibration target for satellite instruments (ASTER, CALIPSO, OCO-2/3)
- BVLOS operations in extreme wind and terrain conditions
- Recent success: September 2021 deployment to Makushin Volcano, Alaska
  - 4 flights conducted (3 successful data collection)
  - Encountered winds >40 kts, downdrafts >2000 fpm
  - Generated 1 km² thermal orthomosaic of summit
  - Validated trace gas sensor payload and real-time data streaming
  - Only visual observations of target volcano that calendar year
  - Demonstrated safe autonomous return-to-base in dangerous conditions

**2. NOAA Hurricane/Tropical Cyclone Sampling (Atlantic, Eastern Pacific)**
- In situ boundary layer measurements during tropical cyclones
- Meteorological and oceanographic data collection in severe weather
- Air deployment from NOAA WP-3D research aircraft
- Path finding to reach sampling areas when direct flight blocked by wind
- Multi-hour duration missions with 150+ NM control range
- Expected to improve hurricane intensity forecasting

**3. NOAA SPLASH Campaign - Soil Moisture Mapping (East River Basin, Colorado)**
- L-band radiometer remote sensing for soil moisture mapping
- NDVI vegetation assessment
- Mountainous, complex terrain environment (10 km² study area)
- Low-altitude terrain-following flights for radiometer optimization
- Seven week-long campaign deployments (May-August) to track seasonal soil moisture evolution
- Validation of retrieval uncertainty against ground-deployed sensors
- Field test bed for terrain-aware planning algorithms

**4. Broader Applications (Identified for Future Market)**
- **Wildfire Monitoring**: Real-time plume characterization, particulate/gas sampling during active fires (1 NCAR mission completed)
- **Weather Observation & Model Validation**: 3D atmospheric profiling for local/global weather models; early warning for severe weather (supercells, tornadoes)
- **Remote Sensing in Difficult Areas**: Emergency response, wildlife monitoring, infrastructure inspection in hazardous environments
- **Oil/Gas Operations**: Emissions monitoring, leak detection in sensitive areas (tundra, etc.)

## Key Results (Phase II-e, September 2021 Makushin Deployment)

### Mission Execution
- **Flight 1 (Sept 10)**: Photogrammetry payload; successful ingress and summit reach; downdraft-induced higher-than-forecast power consumption; conservative return with 3.2x required battery reserve; validated 15-mile wireless comms and BVLOS operations; all three onboard sensors functional
- **Flight 2 (Sept 11)**: Photogrammetry payload; encountered >40 kts headwind and strong downdraft ~1.5 km from summit; autonomous detection of dangerous conditions and safe return; 25% lower average power than Flight 1
- **Flight 3 (Sept 12)**: Full mission success; elevated ingress path strategy reduced downdraft impact; completed primary 1 km² summit mapping goal; generated 3D terrain model and thermal overlay orthomosaic; imaged active hydrothermal area in Upper Makushin Valley
- **Flight 4 (Sept 12)**: First trace gas payload flight; encountered 2000 fpm dowdraft; successful autonomous return-to-base with 1000 ft AGL minimum; validated gas calibration procedures and real-time data telemetry; sensors confirmed within specifications

### Scientific/Technical Outcomes
- Demonstrated ability to conduct routine observations in extreme conditions with minimal weather windows
- Achieved only visual observations of target volcano during that calendar year
- Validated modular payload architecture and field-swappability
- Identified key operational bottlenecks: flight planning labor intensity, manual wind-based mission adjustments, conservative power reserves due to prediction uncertainty

### Lessons Learned
- Mission planning required months of preparation despite modern automation
- Real-time wind observations needed constant feedback integration by trained pilots
- Battery margin predictions overly conservative due to downdraft unpredictability
- Feasibility of BVLOS operations confirmed; safe return capability validated despite extreme conditions

## Notable Details

### Operational Heritage
- BST S2 actively in commercial use by multiple research groups
- ~20 different specialized payloads successfully integrated and deployed
- Prior Phase II SBIR work (NNX17CP13C with USGS) established volcanic sampling capability baseline
- Existing customer base and pre-orders reducing adoption risk

### Customer Commitment & Matching Funds
- **Three separate investors**: NASA Ames, two NOAA groups
- **Committed procurement/development targets**:
  - 2 S0 aircraft for calibration (Q2 2022)
  - 1 S2 for SPLASH soil moisture (Q2 2022)
  - 6 S0 aircraft for hurricane missions (Q3 2022)
  - 1 S2 with volcanic trace gas payload (Q3 