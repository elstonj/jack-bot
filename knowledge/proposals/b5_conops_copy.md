# B5: S0 Weather Collection Concept of Operations

## Document Metadata
- Type: Concept of Operations (CONOPS)
- Client/Agency: United States Navy
- Program/Solicitation: B5 program (appears related to NOAA/Navy collaboration on weather collection)
- Date: 2026-11-03
- BST Products/Systems Referenced: S0 (S0-AD Air-Deployed variant), SwiftTab control tablet, SwiftCore (implied in mission planning/data systems)
- Key Personnel: Jack Elston (last editor)

## Executive Summary
This CONOPS describes the operational employment of Black Swift Technologies' S0 Air-Deployed (S0-AD) weather collection platform by the U.S. Navy to collect high-resolution atmospheric and ocean-surface data from extreme environments. The system addresses a capability gap in collecting multi-altitude weather data at standoff distances from naval task forces, and will be deployed from manned aircraft (P-8, C-130, MH-60) to support weather forecasting, mission planning, and operational safety across maritime operating areas including the Arctic.

## Technical Approach

### System Architecture
The S0-AD is a compact Group 1 UAS (~3 pounds, <2-foot wingspan) designed for air deployment and autonomous operation:

**Core Components:**
- **S0-AD Aircraft**: Fully autonomous data collection platform with atmospheric and sea-surface sensors; deployable via tube-launch or hand-launch from multiple aircraft types
- **Deployment Sleeve**: Adapts folded S0-AD to launch tube systems; houses drag parachute for initial stabilization and orientation
- **Mission Planning and Data Download Computer**: Laptop-based system for pre-flight mission planning (autonomous flight profile from drop to ditch) and post-mission data downloading/formatting for Navy METOC integration
- **SwiftTab Control Tablet**: Real-time control interface (if employed) providing full aircraft control, position tracking, and system health/status on map-based interface
- **Datalink/Data Recorder**: Connects S0 aircraft to control tablet via host aircraft VHF antenna; records all transmitted weather data

### Operational Autonomy Model
- **Fully autonomous flight** after deployment; no in-flight pilot intervention required
- Pre-loaded mission plans define altitude profiles, flight paths, and collection objectives
- Only in-flight command available: system ditch capability
- **No sense-and-avoid capability**; relies on pre-planned spatial deconfliction and ATC procedural deconfliction

### Data Collection Methodology
- **10 Hz data rate** collected onboard
- **200 nautical mile range** for data transmission to host aircraft via VHF
- ML-based adaptive sampling algorithms dynamically update flight paths in real-time to maximize information gain by targeting regions of highest forecast sensitivity
- Post-mission data transferred via air-gapped removable media to Navy METOC systems

### Launch/Recovery Concept
- **Deployment modes**: Common Launch Tubes (CLT), A-size sonobuoy tubes (P-8, C-130), hand-launch from cabin door/ramp (C-130, MH-60)
- **Parachute stabilization**: Deployed immediately after release for initial orientation
- **Recovery**: Aircraft ditches in water; data recorder remains aboard host aircraft
- **Communication range**: Host aircraft must remain within ~200 nautical miles during mission

## Products & Capabilities Described

### S0-AD (S0 Air-Deployed Weather Collection Platform)
**What it is:** Compact, air-deployable UAS designed for operations in extreme atmospheric environments, including hurricanes, severe convection, and marine boundary layer studies.

**Technical Specifications:**
- Weight: ~3 pounds
- Wingspan: Just under 2 feet
- Operating altitude envelope: Surface to 8,000 feet AGL
- Flight endurance: Up to 2 hours
- Flight range: ~150 nautical miles independent of host platform
- Temperature range: −65 °F (Arctic) to equatorial heat
- All-weather capability: Category 5 hurricane winds, heavy precipitation, Arctic icing

**Data Collection Parameters:**
- 3D wind vectors
- Atmospheric pressure, temperature, humidity
- Sea surface temperature
- Wave height and wave slope
- Turbulence metrics
- 10 Hz sampling rate
- ~200 nautical mile data transmission range

**Proposed Navy Use Cases:**
- High-resolution environmental awareness for fleet operations
- Hurricane and severe storm tracking
- Electromagnetic spectrum propagation assessment
- Maritime maneuverability evaluation (sea state, ice conditions)
- Aviation operations support
- ISR sensor performance evaluation
- Multi-altitude data collection at standoff distances from task force

**Deployment Methods:**
- Tube-launch from P-8A Poseidon via existing A-size launch tubes
- Tube-launch from C-130 via Common Launch Tubes
- Hand-launch from MH-60 Seahawk cabin door
- Hand-launch from C-130 cabin door/ramp

**Performance Claims/Validation:**
- Proven in operational deployment during 2024-2025 NOAA hurricane seasons from WP-3D aircraft
- Validated in Category 5 hurricane conditions with extreme wind, turbulence, and precipitation
- Successfully demonstrated airframe, sensor suite, and data collection in severe environmental conditions

### SwiftTab Control Tablet
Real-time mission control interface providing full aircraft control, position tracking, and system health/status visualization on map-based display. Optional during autonomous operations; used during NOAA contractor-operated missions for real-time command of hurricane-specific operations (eyewall tracking, storm center fixing, targeted sampling).

### Mission Planning Software
Standalone laptop application supporting:
- Complete pre-flight mission planning (altitude profiles, flight paths, collection objectives)
- Autonomous mission profile loading onto S0 aircraft while in deployment sleeve
- Post-mission data download and format conversion for Navy METOC system compatibility
- Air-gapped data transfer to Navy systems via removable media

## Use Cases & Applications

### Primary Mission: Navy Weather Intelligence Support
- Support course-of-action development during task force operational planning
- Provide high-resolution environmental data when existing satellite, buoy, and shipboard sensor data insufficient
- Improve weather forecasting accuracy for fleet operations
- Support rapid environmental assessment and operational decision-making

### Specific Operational Scenarios
1. **Hurricane/Severe Storm Tracking**: Deployment into tropical storms through Category 5 hurricanes for high-resolution structure sampling
2. **Arctic Operations**: Extreme cold-weather and persistent icing environment data collection (−65 °F capability)
3. **Pre-Mission Environmental Assessment**: Multi-altitude profiling prior to naval operations in area of interest
4. **Concurrent Multi-Mission Operations**: Integration of weather data collection into P-8, C-130, and MH-60 primary missions (anti-submarine warfare patrols, maritime reconnaissance, training sorties)
5. **Sea State and Ice Condition Assessment**: Maritime maneuverability support in high-latitude regions
6. **Atmospheric Boundary Layer Studies**: Low-altitude vertical profiling in marine boundary layer

### Environmental Operating Domains
- Open oceans
- Enclosed seas
- Littoral regions
- Arctic (down to −65 °F with icing)
- Tropical/equatorial zones
- Extreme weather (Category 5 hurricanes)

## Key Results / Operational Validation

### Proven Capabilities (2024-2025 NOAA Deployments)
- Successful deployment from NOAA WP-3D "Hurricane Hunter" aircraft during 2024 and 2025 hurricane seasons
- Validated operation across range of severe environmental conditions: developing tropical storms through fully developed Category 5 hurricanes
- Confirmed airframe structural integrity and sensor performance in extreme wind, turbulence, and precipitation
- Demonstrated data collection and transmission reliability

### Current vs. Target Operational Model
**Current (Contractor-Operated)**:
- Operator onboard host aircraft
- Real-time tablet-based command interface
- Dynamic mission adjustment based on hurricane scientist input
- Contractor personnel provide expertise and operational control

**Target (Navy Autonomous)**:
- Fully autonomous post-deployment operation
- Pre-loaded mission plans executed without intervention
- No requirement for S0 operator aboard host aircraft
- Navy METOC personnel plan missions; aircrew handle deployment only

## Notable Details

### Capability Gap Being Addressed
Current Navy weather data sources (satellites, buoys, shipboard sensors, autonomous vehicles) have limitations:
- **Satellites**: Low spatial/temporal resolution, limited vertical profiling
- **Shipboard sensors**: Data only near vessel
- **Buoys/USVs**: Slow repositioning, cannot collect atmospheric data at multiple altitudes

S0-AD provides: **High-resolution multi-altitude data at significant standoff distances in extreme environments**

### Critical Policy and Safety Considerations
1. **Autonomous Flight Risk**: S0-AD conducts entire flight autonomously without user intervention; lacks sense-and-avoid capability. Requires Navy acceptance of autonomous UAS flight in proximity to manned aircraft and pre-planned deconfliction procedures.

2. **Operational Responsibility**: Must determine whether METOC personnel (flight plan developers) or host-platform aircrew (launch operators) bear responsibility for S0-AD operations. System kill/ditch capability assessment required as risk mitigation.

3. **Weather Environment Constraint**: Safety considerations simplified if deployments limited to severe weather systems (normally avoided by manned aircraft). Clear-air deployment requires more comprehensive safety case.

4. **Mission Integration Impact**: Incorporating S0-AD collection into P-8, C-130, and MH-60 primary missions will affect those operations. Feasibility depends on ability to conduct concurrent data collection or requirement for dedicated sorties.

5. **Airspace Deconfliction**: Relies entirely on pre-planned spatial deconfliction and ATC procedural coordination; no onboard collision avoidance.

### Stakeholders and Training Requirements
**Task Force Command/Staff**: Familiarization training on S0-AD capabilities and operational impacts

**Task Force METOC Department** (Primary Operators):
- Classroom and practical training on system description, mission planning, operation, data analysis
- Integration of S0-AD data into Navy forecast models
- Coordination with ATC organizations

**Launch Platform Aircrew**:
- Handling, loading, startup, deployment procedures
- Preflight checks and data recorder management
- Integration into platform-specific training events

**Air Traffic Control Organizations**: Familiarization on S0-AD capabilities, collection profiles, operational behaviors

**CNATTU** (Center for Naval Aviation Technical Training Unit): Potential stakeholder for formalizing S0-AD training in Navy METOC training pipeline

### Remaining Development to Full Operational Capability (FOC)

**High-Priority Efforts:**
- **Turbulence and Wave Sensing Development** (High LOE): Real-time algorithm execution for Significant Wave Height, Mean Squared Slope, drag coefficient, momentum flux, turbulent kinetic energy; Kalman filter optimization for heavy precipitation/cloud cover
- **Cold and Icing Environment Hardening** (High LOE): Internal PTC heaters for pressure port protection, Ice-X wing/propeller coatings, validation at NASA Glenn Icing Research Tunnel
- **Tube Launch Integration** (Medium-High LOE): Identify specific Navy launch systems (P-8, C-130, MH-60), design interfaces, ground/flight testing for each platform permutation

**Medium-Priority Efforts:**
- **Atmospheric Sensing Validation**: Flight-relevant characterization of pressure, temperature, humidity, wind sensor response time, lag, cross-sensitivities
- **ML-Based Adaptive Sampling**: Advance from rule-based to closed-loop AI guidance; onboard algorithms target regions of highest forecast sensitivity
- **P-8/C-130/MH-60 Antenna Integration**: Research existing antenna compatibility; design and prototype custom antennas/interfaces if required
- **Mission Planning Laptop Development**: Standalone planning application for pre-flight mission loading; post-mission data download and Navy METOC format conversion

**Lower-Priority Efforts:**
- **Forecast Improvement Demonstration**: Real-time data assimilation in Navy models; track/intensity error reduction; near-surface structure representation
- **Fully Autonomous Operation**: Adaptation of preflight checks, aircraft-datalink connection establishment, and pre-loaded mission execution without tablet interface
- **Documentation and Training**: Operations manual, maintenance procedures, training guides, simulation systems
- **Cybersecurity and Airworthiness Certification**: Scope/impact depends on final employment concept, system interfaces, and policy decisions

### Hand-Launch Capability Development
Current deployment through NOAA P-3 AXBT-style freefall chute. Development required for:
- Hand-launch from C-130 cabin door/ramp
- Hand-launch from MH-60 cabin door
- Design adaptation and deployment method validation on target platforms

### Data Assimilation and Forecast Impact
- Successful offline assimilation into NOAA forecast models (demonstrated in Phase I)
- Phase II effort extends assimilation to Navy forecast models
- Focus on leveraging S0's high-density thermodynamic observations in lowest 2 km of atmosphere to reduce track/intensity errors and improve near-surface structure

### Arctic Operations as Key Priority
Document emphasizes Arctic environment as "particular operational interest" due to:
- Traditional weather platforms face significant performance/survivability limitations in extreme cold and icing
- S0-AD required for reliable operation at −65 °F with persistent atmospheric icing
- Critical for supporting U.S. Navy operations in high-latitude regions

### Current System State
- **Technology Readiness**: TRL-9 airframe proven in Category 5 winds
- **Operational Status**: Currently contractor-operated from NOAA aircraft; requires transition to Navy autonomous operations
- **Sensor Suite**: Validated in extreme conditions; algorithm refinement needed for real-time onboard execution