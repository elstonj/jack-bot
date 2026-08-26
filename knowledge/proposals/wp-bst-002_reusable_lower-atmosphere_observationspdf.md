# Extending Lower-Atmosphere Observations with Air-Deployed and Reusable UAS

## Document Metadata
- **Type:** White paper / capability proposal
- **Client/Agency:** NOAA Office of Marine and Aviation Operations (OMAO) / Uncrewed Systems Operations Center
- **Program/Solicitation:** Not tied to a specific solicitation; presented as standalone proposal with SBIR Phase III pathway (references NAVAIR N251-016, STTR N6833525C0270, Air Force AF192-005); also compatible with NOAA standing Broad Agency Announcement (deadline 30 September 2026)
- **Date:** 17 August 2026
- **BST Products/Systems Referenced:** S0 (air-deployed), S0-VTOL, SwiftCore (autonomous flight management), SwiftPilot, SwiftTab, S2 (mentioned in context of NightFOX wildfire payload experience)
- **Key Personnel:** Cory Dixon (last editor)

## Executive Summary
Black Swift Technologies proposes an 18-month pilot program to NOAA combining one autonomous ground station and two reusable S0-VTOL aircraft to increase the frequency and geographic density of lower-atmosphere observations while reducing staffing and consumable logistics compared to traditional radiosondes. The pilot will validate unattended station operations under visual-line-of-sight controls and define the technical evidence and authorization pathway for later beyond-visual-line-of-sight (BVLOS) operation, with a production objective of one centralized fleet operator supervising up to 30 geographically distributed autonomous stations.

## Technical Approach

### Core System Architecture
- **Autonomous Enclosure:** Prototype ground station providing environmental protection, aircraft storage, battery charging (with temperature/voltage/current/health limits), internal/external condition monitoring, communications, launch preparation, landing-zone support, data transfer, and event logging
- **Aircraft Integration:** Two modified S0-VTOL aircraft equipped with:
  - Battery-management and charging interfaces
  - Health and status outputs
  - Landing camera and companion computer
  - Vision-assisted terminal guidance
  - Data-transfer interfaces
  - Mechanical and electrical interfaces for autonomous operation
- **Flight Management:** SwiftCore autonomous flight control enables:
  - Vertical takeoff and landing (VTOL)
  - Controlled climb/descent rates
  - Hold at selected altitudes
  - Segment repetition for capturing lower-atmosphere evolution
  - GNSS-supported outer approach with terminal landing guidance using confidence gates
  - Automated mission abort on integrity, visual confidence, landing-zone status, wind, or aircraft health issues

### Mission Profile Operations
- Enclosure monitors readiness: internal temperature, precipitation, wind, aircraft state, battery condition, communications, navigation availability, landing-area status
- Automated preflight health checks with readiness/exception status reporting to central fleet operator
- Ascent to approved altitude with controlled rates
- Profile execution (pressure, temperature, humidity, 3D winds) with onboard recording and ground transmission
- Data includes timestamps, position, aircraft state, calibration information, quality indicators
- Return-to-site triggered by mission completion or energy/weather/communications/navigation/airspace thresholds
- Post-landing: aircraft securing, battery/aircraft condition verification, data/logs transfer, controlled recharge
- Battery charging prevented outside approved parameters; faults place system in safe state with operator alert

### Environmental Hardening
- Cold and icing management through bounded operational envelope (not unrestricted icing claim)
- Candidate measures: coatings, localized heating, component changes, monitoring, procedural weather gates
- Evaluation of effects on atmospheric probe, propulsion, control surfaces, batteries, camera, enclosure mechanisms, communications
- Environmental and flight evidence will establish allowable operational conditions

### Centralized Fleet Operations Concept
- Aggregates station status, weather gates, aircraft health, communications quality, mission schedules, data-transfer state, maintenance actions
- Autonomous mission execution under nominal conditions with operator acknowledgement rather than continuous control
- System prioritizes only conditions requiring human judgment
- Suspends/limits new launches when operator workload, communications, weather, or unresolved alerts exceed thresholds
- Production objective: up to 30 concurrent station operations per fleet operator (subject to validation and FAA authorization)
- Note: One-to-many precedent exists (FAA waiver for 30 aircraft under specific operators), but does not transfer to BST/NOAA without separate validation and authorization

### Safety and Regulatory Approach
- **VLOS Pilot Phase:** On-site visual observers serve as pilot-phase safety and regulatory control (not production concept)
- **Unattended Operation Definition:** Station can operate without on-site personnel but remains maintenance-intensive; "unattended" does not mean maintenance-free
- **Production Objective:** Centrally supervised BVLOS operation without on-site observers
- **Phased Authorization Path:** Pilot will not claim 30-station ratio as validated; will collect evidence (station reliability, communications, alert rates, operator workload, contingency/recovery) to determine defensible ratio and support later authorization request
- Enclosure design includes safe maintenance access and controlled procedures
- Safety roles (remote pilot in command, visual observers) assigned per approved test construct during progressive testing and base demonstration

## Products & Capabilities Described

### S0 (Air-Deployed)
- **Description:** Atmospheric measurement aircraft developed for severe environments; deployable from NOAA WP-3D aircraft
- **Operating Heritage:** Has operated in tropical cyclones and extreme conditions (high winds, precipitation)
- **Capabilities:** Delivers pressure, temperature, humidity, 3D wind observations from locations inaccessible to crewed aircraft
- **Proposed Use:** Reference aircraft for comparison testing; proposed Option 2 (winter campaign) would produce and deploy 50 air-deployed S0 systems for OMAO campaigns

### S0-VTOL
- **Description:** Reusable variant of S0; combines air-deployed S0 core sensing, avionics, autonomous-flight foundation with VTOL configuration
- **Configuration:** Pivoting motors permit vertical launch/recovery without launcher or runway; fixed-wing cruise supports efficient profiling and loiter
- **Performance Specs:** 
  - Maximum altitude: 15,000 feet AGL (subject to site elevation, airspace, weather, energy reserve, approval)
  - Maximum endurance: 60 minutes
- **Sensor Suite:** Pressure, temperature, relative humidity, 3D winds
- **Proposed Use in Pilot:** Two units integrated with autonomous enclosure; one primary operational article, one spare/test article; production concept is one S0-VTOL per site

### SwiftCore
- **Description:** BST's autonomous flight-management architecture
- **Capabilities:** Handles autonomous profile execution, altitude hold, segment repetition, landing guidance
- **Application:** Used in both S0 and S0-VTOL; fundamental to unattended operation

### Centralized Fleet-Operations Software (Prototype)
- **Capabilities:** Station-state aggregation, mission scheduling, health monitoring, alert taxonomy/prioritization, communications management, maintenance escalation, operator-workload limiting
- **Proposed Use:** Option 3 would implement prototype using base physical station plus simulated endpoints representing ≥30 stations to evaluate concurrent scheduling, exception handling, workload

### Ground Control Station (GCS)
- Part of deliverables; supports remote monitoring and command
- Designed for fleet operators managing automated missions, handling exceptions, escalating safety events

### S2
- **Mentioned Context:** NightFOX program; carried lightweight multisensor payload for wildfire mapping and fire-radiative-power measurements (demonstrates BST's scientific-payload integration experience)

## Use Cases & Applications

### Primary Use Case: NOAA Radiosonde Network Augmentation
- **Current Need:** National Weather Service operates 92 radiosonde stations across North America and Pacific Islands; personnel release balloons 2–4 times daily plus additional event-driven releases
- **Limitations Addressed:** 
  - Balloon observations drift from release location (not collocated)
  - Cannot be recovered or repeated
  - Cannot hold at selected altitude or repeat vertical segments
  - Labor and consumables increase proportionally with observation frequency
  - Remote sites face staffing and resupply challenges
- **Proposed Solution:** S0-VTOL stations return to same site, enable scheduled or event-driven profiles, reduce staffing needs, preserve radiosondes for full-depth observations they uniquely provide
- **Complement, Not Replacement:** Recognizes radiosondes are "indispensable to forecasting, research, aviation, and numerical weather prediction" and "essential" for full-depth soundings; S0-VTOL addresses lower-atmosphere observation frequency/density constraint

### Specific Operational Scenarios
- **Rapid Lower-Atmosphere Monitoring:** Repeated measurements during rapidly changing conditions (where temperature, moisture, winds, stability, turbulence change rapidly)
- **Remote Site Operations:** Austere locations where staffing and resupply are particularly consequential
- **Event-Driven Profiles:** Flexible scheduling triggered by meteorological conditions rather than fixed-time releases
- **Atmospheric River/Winter-Weather Campaigns:** Option 2 proposes 50 air-deployed S0 systems for OMAO campaigns (winter weather, atmospheric rivers, or other science campaigns)

## Key Results / Validation Evidence

### Existing Measurement Validation
BST has compared S0 observations against:
- Instrumented tower at Department of Energy Atmospheric Radiation Measurement Southern Great Plains site
- Radiosondes, dropsondes, streamsondes
- Tail Doppler radar
- High-resolution atmospheric models

### Effects Requiring Continued Characterization
- Sensor response during rapid vertical motion
- Aircraft-induced temperature or humidity bias
- Wind-estimation behavior in tight turns

### Proposed Pilot Validation Measurements
The pilot will measure/quantify:
- Installation effects
- Accuracy
- Repeatability
- Availability
- Workload (nominal and exception-handling)
- Environmental limits
- Cost per usable profile
- Launch and recovery performance
- Recharge effectiveness
- Maintenance demand
- Communications availability
- Operator interventions required
- Logistics demands
- Staffing requirements

### Production Path Evidence
The pilot will establish:
- Defendable operator-to-station ratio (targeting up to 30, but evidence-based determination)
- Station reliability metrics
- Communications link quality
- Alert demand rates
- Contingency and recovery procedures
- Transition path to BVLOS and multiple-aircraft authorization

## Notable Details

### Risk Reduction Strategy
- Builds on 15+ years of S0 operational heritage in NOAA severe-weather missions
- Uses proven core sensing, avionics, SwiftCore autonomous-flight foundation
- Prior measurement-validation work provides baseline; pilot will quantify system-level (not just component) performance
- Regulatory precedent exists for one operator supervising up to 30 aircraft (FAA waivers), though authorization does not transfer; pilot designed to collect evidence needed for BST/NOAA-specific authorization

### NOAA Foundation
- S0 air-deployed from WP-3D in tropical cyclones under established NOAA launch procedures and data workflows
- S0-VTOL applies same core technologies in reusable configuration
- NightFOX experience demonstrates BST's ability to integrate scientific payloads for NOAA missions

### Production Economics Emphasis
- Proposal emphasizes that economic case depends on **network-level labor/consumables/maintenance/communications/availability/cost**, not single-sortie cost
- Relevant comparison is cost per usable profile across operating network
- Centralized supervision of multiple stations from one operations center is essential to economic case
- Production concept: one enclosure + one aircraft per site, supervised through centralized fleet-management system

### Intellectual Property
Deliverables may incorporate BST's pre-existing proprietary assets:
- Airframes (S0, S0-VTOL)
- SwiftCore autonomous-flight management
- SwiftPilot, SwiftTab ground-station software
- Centralized fleet-management software
- Simulation assets, operator-interface software
- Alert-management logic, fleet-orchestration methods
- Atmospheric wind-estimation methods
- Autonomy functions, interfaces, models, manufacturing know-how
- Data rights assertions to be defined in agreement

### Acquisition Pathway
- Compatible with NOAA IDIQ 1305M226D0012
- BST holds SBIR data rights lineage on S0 program
- Eligible for Phase III sole-source award under 15 U.S.C. § 638(r)
- References prior awards: NAVAIR N251-016, STTR N6833525C0270, Air Force AF192-005
- Alternative: NOAA Broad Agency Announcement (open through 30 September 2026)
- Timing note: Award by mid-September permits FY26 ORF obligation before lapse; deliveries extend into FY27 as non-severable season-readiness capability

### Phased