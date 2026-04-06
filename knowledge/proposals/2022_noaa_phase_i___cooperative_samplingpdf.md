# Cooperative Airborne In-Situ Sampling of Severe Convective Storms

## Document Metadata
- Type: NOAA SBIR Phase I Proposal
- Client/Agency: NOAA Office of Oceanic and Atmospheric Research (OAR)
- Program/Solicitation: NOAA-OAR-TPO-2022-2007117, PKG00270208
- Date: 2022
- BST Products/Systems Referenced: S0 (VTOL), S1, S2, SwiftCore Flight Management System, SwiftFlow Multi-hole Probe (MHP), SwiftPilot autopilot, SwiftTab UI
- Key Personnel: Dr. Maciej Stachura (PI, CTO), Dr. Jack S. Elston (Lead Engineer, CEO/co-founder)

## Executive Summary
Black Swift Technologies proposes the design, development, and validation of the Coordinated Atmospheric Thermodynamics Sampling System (CATSS)—a networked team of up to 10 cost-effective small VTOL uncrewed aircraft with integrated sensor suites capable of cooperative atmospheric sampling in severe convective storms. The system will enable transformative capabilities such as simultaneous volumetric, vertical, and horizontal atmospheric measurements while maintaining turn-key, commercial-off-the-shelf (COTS) operational simplicity managed by a single operator or small team.

## Technical Approach

### Core Architecture
- **Foundation Platform**: BST VTOL S0—a low-cost, air-deployable VTOL UAS originally developed under NOAA SBIR for P3-based hurricane monitoring, extended with land-based reusable capabilities
- **Network Coordination**: Up to 10 aircraft intelligently networked with on-board control algorithms enabling cooperative sampling strategies
- **Hardware Enhancement**: Addition of computational nodes (small Linux single board computers or dual-core chips) separate from core avionics to run coordination algorithms while maintaining reliable basic control
- **Communication**: Inter-aircraft mesh network with 10 km range and sufficient bandwidth for up to 10 nodes; routing protocol handles dynamic node addition/removal
- **Software Framework**: Enhanced BST SDK with open API to SwiftPilot autopilot; modified to support third-party coordination algorithm specification and execution

### Phase I Focus
- System architecture design and finalization
- Hardware/software for safe multi-aircraft operations
- Inter-aircraft mesh network development and testing
- User interface modifications for multi-aircraft control
- Coordination algorithm development and simulation
- Next-generation on-board failure detection and mitigation

## Products & Capabilities Described

### S0 VTOL UAS
**Specifications:**
- Weight: 1.8 kg
- Wingspan: 1.5 m
- Cruise time: 60 minutes
- Launch type: Fully autonomous VTOL
- Propulsion: Electric
- Communication range: 10 km
- Thrust-to-weight ratio: ~2:1 (allows VTOL and dash speeds to 45 m/s / 100 mph)
- Wing structure tested with maneuvers exceeding 100 m/s (225 mph)

**Sensor Suite (Integrated):**
- 3D inertial winds
- Pressure, temperature, humidity measurements
- 100 Hz sensor rate
- Flush-air system in nose cone
- Advanced mechanical designs to mitigate pressure port water-droplet bridging in heavy precipitation

**Capability**: Proven ability to operate in extreme conditions including supercell thunderstorms, derechos, heavy precipitation, high winds, and large-scale turbulence. Successfully operated by NOAA and US Air Force.

### SwiftFlow Multi-hole Probe (MHP)
**Specifications:**
- Weight: 50 g
- Wind velocity resolution: 0.03 m/s
- Wind velocity accuracy: 0.29 m/s
- Temperature range: -40°C to 85°C
- Temperature accuracy: ±0.3°C
- Pressure resolution: 0.012 mbar
- Pressure accuracy: 1.5 mbar
- Relative humidity range: 0-100% RH
- Humidity accuracy: ±1.3% RH

**Origin**: Originally designed under NASA SBIR; represents 10x cost reduction compared to comparable instruments.

**Wind Tunnel Validation (NOAA ATDD)**:
- α error: 0.10°
- β error: 0.25°
- True airspeed error: 0.06 m/s

**Market Impact**: Already sold/delivered to NOAA, NASA, NCAR, University of Colorado Boulder, and others.

### SwiftCore Flight Management System
- Purpose-built avionics with tightly coupled sensors
- CAN bus interface for rapid payload integration
- Electronic Centralized Aircraft Monitor System (ECAMS) with Level 2 (Master Caution/Yellow) and Level 3 (Master Warning/Red) failure detection and mitigation
- Automated response to subsystem failures

### SwiftTab User Interface
Being modified to support multi-aircraft operations with:
- Automated pre-flight checks for all powered aircraft
- Multi-aircraft selection and team-level commands (begin mission, pause/orbit, land)
- Up to 10 aircraft status display with intuitive detailed status access
- Further ECAMS automation for failure resolution without operator intervention
- Support for multiple operators with subsets of coordinated vehicle team (FAA compliance)

### Proposed CATSS-Specific Capabilities
- **Mesh Network**: 10 km inter-aircraft range with true meshing topology (no single point of failure)
- **Service Discovery**: Identification of connected vehicles and their capabilities (payload sensors, flight envelope)
- **Subscription-Based Data Dissemination**: Participants can subscribe to aircraft telemetry, scientific measurements, and other network data
- **Cost**: Replacement cost below $7,500 per aircraft
- **Deployment Speed**: Single operator can launch 10 aircraft within 5 minutes of each other

## Use Cases & Applications

### Primary Focus: Severe Convective Storms
- Supercell thunderstorms
- Derechos
- Tornadic systems
- Fire weather conditions

### Sampling Strategies (Proposed for Phase I/II)
1. **Vertical Gradient Sampling**: Aircraft in vertical stack to measure temperature/wind variations with altitude
2. **Horizontal Gradient Sampling**: Distributed aircraft measuring lateral atmospheric variations
3. **Volumetric Boundary Layer Snapshot**: Simultaneous profiling of atmospheric boundary layer
4. **Simultaneous Coordinated Profiling**: Multiple aircraft at different locations collecting synchronized data

### Broader Applications
- Fire weather monitoring and wildfire observations
- Atmospheric chemistry and plume detection
- Numerical weather prediction model improvement
- Augmentation of satellite-based measurements and satellite validation
- Complement to ground-based remote sensing
- Higher temporal frequency sampling of lower 5 km atmosphere to supplement balloon soundings
- Arctic operations (ERASMUS program experience)
- Volcanic plume observation
- Soil moisture measurement
- Upper atmospheric exploration research

## Key Results & Status
This is a Phase I proposal; no results are reported. The document outlines planned Phase I work to demonstrate feasibility, including:

**Proposed Milestones:**
1. Creation of system architecture design document
2. Documentation and validation of radio system performance for 10 aircraft
3. Prototype UI implementation on Android tablet
4. Demonstration through simulation of selected coordination algorithms

**6-Month Phase I Schedule** with tasks spanning:
- Cooperative system architecture design
- Coordination algorithm development and simulation
- Communication system integration and testing
- Preliminary UI development and testing
- Commercial viability exploration
- Report preparation

## Notable Details

### Competitive Advantages
- **Commercial Gap**: Existing UAS solutions are primarily one-off university/research platforms; few commercial solutions exist. Meteomatics produces multi-rotor systems (Meteodrones) but with limited severe weather capability.
- **Autonomy**: Proposes only example of autonomous formation flying for atmospheric sampling in recent history (previous example from ~2008, 14 years prior)
- **Unique Technology**: Advanced pressure port designs to prevent water-droplet bridging in heavy precipitation—common problem with multi-hole and pitot sensors
- **Extensible Architecture**: Designed with documented network interface to include other UAS (e.g., legacy NOAA UAS) in coordination framework

### Team Expertise
- **Dr. Maciej Stachura (CTO/PI)**: 
  - 300+ flight experiments including multi-aircraft cooperation
  - VORTEX2 campaign—first-ever tornadic supercell intercept by UAS
  - 140+ FAA Certificates of Authorization (COAs) for multi-state operations
  - Led NASA AFSRB/FRB processes for NAS operations
  - Prior Phase I/II NASA SBIR PI (soil moisture UAS)
  - Doctoral work: cooperative control algorithms for multi-UAS with unified sensing/communication framework

- **Dr. Jack S. Elston (CEO/Lead Engineer)**:
  - Ph.D. focused on meshed network UAS and control algorithms for tornadic supercell sampling
  - Designed Tempest UAS (VORTEX2 first intercept)
  - NSF Atmospheric Sciences Postdoctoral Fellow
  - Led multiple successful SBIR efforts with commercial Phase II/CCRP outcomes
  - Expertise: volcanic plume observation, wildfire monitoring, satellite validation, soil moisture, Venus upper atmosphere exploration

### Relevant Prior Experience
- **VORTEX2 (NSF/NOAA)**: First unmanned aircraft intercept of tornadic supercell; multi-aircraft coordination with real-time dissemination to 100+ participating vehicles
- **NOAA NightFOX**: S2 UAS fire weather sampling including night operations and BVLOS clearances
- **NOAA FIREX Project**: Dual-payload swappable thermal/IR and trace gas/particulate in-situ measurements
- **MIZOPEX (NASA)**: Multi-class UAS integration (NASA SIERRA, ScanEagles, micro UAS) in NAS
- **LAPSE-RATE (ISARRA)**: Multi-platform atmospheric science campaign (50 platforms, 1300+ flight hours, 96 field personnel)
- **ARM/ERASMUS**: Arctic atmospheric measurements demonstrating harsh environment operations
- **MET MAP**: Four simultaneous UAS deployment for gust front and boundary layer measurements
- **RAAVEN UAS (Univ. Colorado)**: Cooperative atmospheric sampling using BST SwiftFlow probe
- **CLOUD MAP**: University-led multi-UAS heterogeneous research platform

### Commercial Products from Prior SBIR
- **S2 UAS**: Scientific research platform currently in NOAA use
- **SwiftFlow Multi-hole Probe**: 10x cost reduction over comparable wind sensors; established customer base

### Regulatory & Operational Considerations
- Team has extensive FAA COA experience (140+ COAs mentioned)
- Proposes COA coordination with NOAA/FAA during Phase II for multi-aircraft flight testing
- Current proposal accommodates FAA restriction requiring one operator per aircraft via multi-ground-station architecture while targeting single-operator capability
- ECAMS failure detection designed to reduce operator workload from "pilot per aircraft" to "fleet manager" role

### Risk Mitigation Strategies
1. **Communication Delays/Dropouts**: Distributed algorithms handling periodic data loss; Phase I will test operational limits
2. **Radio Link Validation**: COTS radios surveyed; bench and long-range testing planned; modular avionics allow rapid radio swaps
3. **Operator Overload**: Simulation environment with up to 10 aircraft and injected failures; iterative UI refinement; prioritization of multi-aircraft failure responses

### Partnership Potential
- BST in contact with Meteomatics regarding cooperative solution integration using CATSS framework

---

**Note**: Document is comprehensive Phase I proposal with detailed technical specifications, team credentials, and implementation roadmap. No results data present as this is prospective work. Document thoroughly establishes technical feasibility path and BST's qualifications for execution.