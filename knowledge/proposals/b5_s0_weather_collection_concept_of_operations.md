# B5: S0 Weather Collection Concept of Operations

## Document Metadata
- **Type:** Concept of Operations (CONOPS)
- **Client/Agency:** United States Navy
- **Program/Solicitation:** Navy STTR Phase I Deliverable; Hazardous Weather topic
- **Date:** Created 2025-12-16; Modified 2026-01-05
- **BST Products/Systems Referenced:** S0 Air-Deployed (S0-AD) Weather Collection Platform; SwiftTab control tablet; SwiftCore mission planning/data download system
- **Key Personnel:** Daniel Prendergast (last editor)

## Executive Summary
This CONOPS describes how Black Swift Technologies' S0 Air-Deployed (S0-AD) uncrewed aircraft system would be operated by U.S. Navy personnel to collect high-resolution atmospheric and ocean-surface weather data in extreme environments. The S0-AD would be deployed from manned naval aircraft (P-8, C-130, MH-60) to fill capability gaps in weather data collection at standoff distances, multiple altitudes, and in severe weather conditions that support fleet operational planning, hurricane tracking, and maritime safety.

## Technical Approach

### System Architecture
The S0-AD is a compact, fully autonomous Group 1 UAS weighing approximately 3 pounds with a wingspan under 2 feet. It operates entirely autonomously after deployment with no in-flight pilot intervention except for a ditch command capability. Key system components:

- **S0-AD Aircraft:** Compact, air-deployable platform with integrated atmospheric and sea-surface sensors; fully autonomous operation after release
- **Deployment Sleeve:** Adapts folded S0 to launch tube systems; houses drag parachute for initial stabilization
- **Mission Planning Computer:** Laptop-based system for pre-mission planning and post-mission data download (to be developed in Phase II)
- **SwiftTab Control Tablet:** Real-time control interface for mission profile adjustments during flight
- **Datalink/Data Recorder:** VHF-based connection to host aircraft; records all weather data transmitted from S0

### Deployment Modes
- Tube-launch from Common Launch Tubes (CLT) or A-size sonobuoy tubes on P-8 and C-130
- Hand-launch from cabin door or ramp of C-130 and MH-60 platforms
- Uses host aircraft's existing skin-mounted VHF antennas for data reception

### Data Collection & Transmission
- Collects sensor data at 10 Hz sampling rate
- Transmits to host aircraft via VHF at ranges up to approximately 200 nautical miles
- Data received by host aircraft datalink/data recorder for post-mission download

### Operational Workflow
1. METOC personnel develop autonomous mission plan using mission planning software; load profile onto S0 in deployment sleeve
2. Aircrew briefs on drop location, mission objectives, deployment procedures
3. Host aircraft navigates to designated drop location
4. Crew chief powers on S0 aircraft and data recorder; verifies connectivity
5. Aircrew deploys S0 at designated location; S0 deploys parachute, stabilizes, transitions to powered flight
6. Host aircraft maintains communication range (≈200 nm) throughout collection period
7. S0 executes entire mission autonomously
8. Upon mission completion and host aircraft recovery, data recorder delivered to METOC for analysis and integration into forecast models

## Products & Capabilities Described

### S0 Air-Deployed (S0-AD) Platform

**Physical Specifications:**
- Weight: Approximately 3 pounds
- Wingspan: Just under 2 feet
- Altitude envelope: Surface to 8,000 feet above ground level
- Endurance: Up to 2 hours flight time
- Independent range: Approximately 150 nautical miles (independent of host platform range)
- Temperature operating range: −65 °F to equatorial heat conditions

**Sensor Suite & Measurements:**
- Atmospheric pressure, temperature, humidity
- Three-dimensional wind vectors
- Sea surface temperature
- Wave height and wave slope
- Turbulence metrics (to be refined in Phase II)
- High-frequency wind and radar data (up to 100 Hz for wave/turbulence algorithms)

**Key Capabilities:**
- Autonomous operation without in-flight pilot intervention
- Multiple deployment modes (tube-launch and hand-launch)
- High-rate data collection (10 Hz baseline)
- Reception via existing host aircraft antennas
- Pre-mission autonomous planning
- ML-based adaptive sampling (dynamic real-time flight path updates targeting regions of highest forecast sensitivity)
- All-weather operation including Category 5 hurricanes and extreme Arctic conditions (−65 °F, persistent icing)
- Data range: Up to ~200 nautical miles from host aircraft

### SwiftTab Control Tablet
- Tablet-based real-time control interface
- Provides full aircraft control and mission profile adjustments
- Real-time position, system health, and status display on map-based interface
- Optional real-time operation mode (departure from fully autonomous concept)

### Mission Planning & Data Download System (Phase II Deliverable)
- Standalone laptop-based mission planning application
- Allows complete autonomous mission profile development (drop to ditch)
- Pre-loaded mission execution without tablet or operator intervention
- Post-mission data download from datalink/data recorder
- Data formatting for Navy METOC system integration
- Air-gapped data transfer via removable media

## Use Cases & Applications

### Primary Mission: Naval Weather Intelligence Support
- **Mission Planning Support:** Provides high-resolution environmental data to support course-of-action development and analysis during Navy operational planning
- **Hurricane & Severe Storm Tracking:** Enables rapid access to developing tropical storms through Category 5 hurricanes
- **Multi-Altitude Data Collection:** Collects atmospheric profiles at multiple altitudes simultaneously across storm and non-storm environments
- **Standoff Distance Operations:** Operates at significant standoff distances from task force (up to 200 nm from host aircraft, independent 150 nm range)

### Operational Need Areas Addressed
- Mission planning and operational safety assessment
- Hurricane and severe storm tracking and intensity analysis
- Electromagnetic spectrum propagation effects assessment
- Maritime maneuverability considerations (sea state, ice conditions)
- Aviation operations planning
- Intelligence, Surveillance, and Reconnaissance (ISR) sensor performance prediction

### Environmental Conditions of Interest
- **Arctic Operations:** Extreme cold (−65 °F) and persistent atmospheric icing conditions; areas where traditional platforms face survivability limitations
- **Extreme Weather:** High winds and heavy precipitation of Category 5 hurricanes
- **Full Maritime Operating Areas:** Open oceans, enclosed seas, littoral regions
- **Benign to Extreme:** From minimal wind/precipitation to Category 5 hurricane conditions

### Current Operational Validation
The S0 system has been successfully deployed from NOAA WP-3D "Hurricane Hunter" aircraft during 2024 and 2025 hurricane seasons, demonstrating operation in:
- Developing tropical storms through Category 5 hurricanes
- Extreme wind, turbulence, and precipitation environments
- Hurricane-specific operations: eyewall tracking, storm center fixing, targeted sampling of high-interest storm features

## Key Results / Operational Validation

### Demonstrated Performance (2024-2025 NOAA Operations)
- Successful deployments from NOAA WP-3D aircraft in operational hurricane reconnaissance missions
- Validated S0 airframe, sensor suite, and data collection performance across severe environmental conditions
- Proven capability to operate in extreme wind, turbulence, and precipitation of developing tropical systems through Category 5 hurricanes

### Data Assimilation Success (NOAA Models)
- S0 data successfully assimilated into NOAA forecast models
- Demonstrated ability to provide high-density thermodynamic observations in lowest 2 km of atmosphere
- Potential for reducing track and intensity forecast errors and improving near-surface structure representation

### Current Operational Model (NOAA Configuration)
- Real-time operator control from host aircraft using tablet interface
- Contractor personnel onboard for specialized hurricane operations
- Enables hurricane-specific collection patterns (eyewall tracking, storm center fixes)
- Requires real-time command based on dynamic hurricane location and informed by hurricane scientist expertise

## Notable Details

### Current vs. Proposed Operational Models

**Current NOAA Configuration:**
- Contractor-operated, real-time control model
- Trained S0 operator onboard host aircraft
- Tablet-based real-time command interface
- Specialized hurricane-specific flight patterns requiring operator knowledge of hurricane dynamics

**Proposed Navy Configuration:**
- Fully autonomous operation without contractor personnel onboard
- Pre-planned missions with no in-flight control intervention (except ditch command)
- METOC personnel develop mission plans; aircrew executes deployment only
- No sense-and-avoid capability; relies on pre-planned spatial deconfliction and ATC procedural deconfliction

### Capability Gaps Addressed
The S0-AD is designed to address existing Navy weather data collection gaps:
- **Limitations of Current Systems:**
  - Satellites: Low spatial/temporal resolution, limited vertical profiling
  - Shipboard sensors: Data only in immediate vessel vicinity
  - Buoys/USVs: Slow repositioning, incapable of multi-altitude atmospheric collection
- **S0-AD Solution:** High-resolution data at multiple altitudes, significant standoff distances, rapid deployment capability

### Host Platform Integration
**Identified Target Platforms:**
- P-8 Poseidon (tube-launch via CLT or A-size sonobuoy tubes)
- C-130 Hercules (tube-launch and hand-launch from cabin door or ramp)
- MH-60 Seahawk (hand-launch from cabin door)

**Launch Tube Systems:**
- Common Launch Tubes (CLT)
- A-size sonobuoy launch tubes
- Pneumatic pressure-based launch systems (Navy standard)

### Operational Considerations & Safety Constraints

**Safety & Responsibility Issues Requiring Navy Policy Determination:**
1. **Autonomous Operations Near Manned Aircraft:** S0-AD conducts entire flight autonomously without sense-and-avoid capability; safe operations rely on pre-planned spatial deconfliction and ATC procedural deconfliction. Requires Navy risk assessment and approval.

2. **Operational Responsibility:** Must determine whether operational responsibility resides with:
   - METOC personnel developing collection flight plan, OR
   - Host-platform aircrew launching and initiating autonomous collection

3. **Control Capability Adequacy:** Must assess whether system kill/ditch capability provides sufficient risk mitigation during concurrent manned/unmanned aircraft operations

4. **Deployment Environment Constraints:** 
   - Simpler safety case if limited to severe weather (otherwise avoided by manned aircraft)
   - More comprehensive safety case required if deployment into clear-air environments

5. **Host Platform Mission Impact:** Integration of S0-AD into P-8, C-130, MH-60 mission sets will affect primary missions; feasibility depends on whether S0-AD collection can be conducted concurrently with other assigned missions (ASW patrols, maritime reconnaissance, training sorties) or requires dedicated sorties

### Remaining Development Work (Phase II & Beyond)

**Phase II Tasks (Included in Current STTR Proposal):**
1. **Atmospheric Sensing Validation** - Characterize thermodynamic and wind sensing suite response (Task B.4)
2. **Turbulence & Wave Algorithm Development** - Real-time onboard execution of algorithms for SWH, MSS, drag coefficient, momentum flux, turbulent kinetic energy (Tasks B.2, B.3, B.5; validation Task O.5)
3. **Forecast Improvement Demonstration** - Offline data assimilation into Navy models (Task B.1); real-time assimilation (Task O.1)
4. **Cold & Icing Environment Hardening** - PTC heaters for pressure ports, Ice-X wing/propeller coatings, NASA Glenn Icing Research Tunnel validation (Tasks O.2, O.3)
5. **ML-based Sampling Flight Patterns** - Simulation framework development (Task B.6); real-time demonstration in live storm conditions (Task O.6)
6. **P-8/C-130/MH-60 Antenna Integration** - Research antenna options, design interfaces, prototype integration with one platform (Task O.4)
7. **Fully Autonomous Operation Development** - Adapt for autonomous preflight checks, aircraft-datalink connection establishment, pre-loaded mission execution without SwiftTab (Task O.4)

**Post-Phase II Development (Not Included in Current Proposal):**
- Complete antenna integration configurations for all target platforms
- Tube launch system prototyping and operational validation for each launch method variant
- Mission planning and data download laptop development
- System documentation and training materials
- Cybersecurity and airworthiness certifications

### Training Requirements Identified
- **Task Force Command/Staff:** Famil