# Distributed Extreme Weather Reconnaissance and Sensing

## Document Metadata
- Type: White paper / capability proposal
- Client/Agency: NOAA Office of Marine and Aviation Operations / Uncrewed Systems Operations Center
- Program/Solicitation: NOAA IDIQ (1305M226D0012); SBIR Phase III pathway noted (NAVAIR N251-016, STTR N6833525C0270, Air Force AF192-005); NOAA BAA (open through 30 Sept 2026)
- Date: August 17, 2026
- BST Products/Systems Referenced: S0-VTOL, SwiftCore, SwiftPilot, SwiftTab, SwiftStation, S1, S2
- Key Personnel: Cory Dixon (last editor)

## Executive Summary
Black Swift proposes a deployable fleet of S0-VTOL aircraft to provide rapid distributed reconnaissance and sensing during extreme weather events and incidents. The system combines multi-aircraft electro-optical/infrared (EO/IR) imagery collection with autonomous area-search and centralized mission management, offering NOAA a reusable local aerial capability to complement crewed aircraft, reduce response timelines, expand coverage, and expand to fire-weather profiling missions. Base effort delivers five operational EO/IR-capable aircraft with demonstration and transition; options add ten fire-weather profiling systems and cooperative autonomy enhancements.

## Technical Approach

### Core Architecture
- **Air Vehicle**: S0-VTOL platform — 2.6 kg fixed-wing VTOL with 60-minute endurance and 15,000 ft AGL design ceiling
- **Flight Management**: SwiftCore flight-management system with SwiftPilot autonomous flight control and SwiftTab operator interface
- **Payload Integration**: Lightweight EO/IR package (to be downselected) with synchronized position, time, attitude, and aircraft-state metadata; high-resolution onboard storage; selective preview downlink

### Multi-Aircraft Autonomy & Mission Management
- **Centralized Dynamic Area-Search**: One operator defines approved survey area; software divides work into collection sectors based on aircraft availability, image-overlap requirements, route geometry, energy reserves, and recovery constraints
- **Adaptive Tasking**: Software monitors progress and reallocates unfinished sectors if aircraft become unavailable
- **Point-of-Interest Operations**: Operator can designate secondary targets for additional collection based on preview imagery or pre-identified locations
- **Safety Constraints**: Flight execution bounded by approved geofences, energy reserves, weather limits, lost-link behavior, and operator authority

### Communications & Data Workflow
- **Downlink**: Selected preview imagery and thumbnails downlinked when link conditions and C2 priorities permit; full-resolution imagery retained onboard for post-flight offload
- **Telemetry**: Aircraft health, navigation, communications, energy, collection progress monitored through ground system
- **Failover**: Primary and spare ground-control/mission-management capability; hot-spare or failover arrangements for central ground-system failure modes

### Contingency & Safety
- **Loss of Link**: Hold, return, alternate-recovery, or safe-termination responses triggered by navigation degradation, command-link loss, insufficient energy, weather changes, landing-zone loss, or airspace conflicts
- **Payload Redundancy**: Loss of imagery payload does not remove C2; C2 traffic retains priority over imagery download
- **Operator Authority**: Operator retains launch authority, mission supervision, approval of material changes, and hold/return/intervention functions

## Products & Capabilities Described

### S0-VTOL
- **What it is**: 2.6 kg fixed-wing VTOL aircraft designed for extreme-weather reconnaissance
- **Endurance**: Up to 60 minutes
- **Ceiling**: Up to 15,000 ft AGL (subject to configuration, site, airspace, weather, reserve requirements)
- **Atmospheric Sensors** (meteorological configuration): Pressure, temperature, humidity, 3D winds (0.38 m/s resolution, ±0.48 m/s accuracy nominal)
- **Launch/Recovery**: Vertical takeoff and landing from austere locations (no runway required)
- **Proposed EO/IR Configuration**: Integration of lightweight electro-optical/infrared payload with synchronized geotagging, high-resolution onboard recording, and selective preview downlink

### SwiftCore Flight-Management System
- **Components**: SwiftPilot (autonomous flight, health monitoring, payload interfaces, fault responses), SwiftTab (map-based planning, georeferenced data, in-flight tasking, operator annunciation), SwiftStation (portable command, control, telemetry)
- **Capabilities**: Autonomous flight from launch through recovery, in-flight mission changes, centralized fleet supervision
- **Heritage**: Integrated onboard machine vision (NASA Swift Safe-to-Land program) demonstrates capability for onboard imaging, computing, flight-control integration, and safety behavior

### EO/IR Payload
- **Configuration**: Lightweight package to be downselected; must support mechanical fit, power, thermal management, mass properties, vibration, electromagnetic compatibility
- **Data Handling**: Image timing and georeferencing synchronized with aircraft state; high-resolution storage onboard; preview-image downlink capability; post-flight data export
- **Endurance Impact**: Integration must not significantly compromise S0-VTOL endurance or handling

## Use Cases & Applications

### Base Mission: Distributed EO/IR Reconnaissance During Extreme Weather
- **Wildfires**: Rapid local deployment for damage assessment, fire-behavior monitoring, and repeated revisits to dispersed or hazardous locations
- **Hurricanes**: Tactical area coverage complementing NOAA's Emergency Response Imagery workflow with crewed aircraft
- **Severe Storms**: Incident-area surveillance where mobilizing crewed aircraft is not responsive
- **Advantages over Current Methods**:
  - Vertical-takeoff capability enables deployment from austere incident-staging sites (no runway needed)
  - Multi-aircraft fleet enables faster revisit cycles and distributed area coverage compared to single-aircraft or surface stations
  - Complements crewed aircraft (wide-area) and surface networks (fixed-point observations)

### Fire-Weather Profiling (Option 1)
- **Mission**: Controlled vertical atmospheric profiles (climbs, descents, level holds, repeated segments) measuring pressure, temperature, humidity, 3D winds
- **Problem Addressed**: Surface weather stations cannot resolve vertical structure controlling inversions, moisture recovery, low-level winds, wind shear, and mixing; radiosondes drift and are expended
- **Workflow**: Aircraft completes approved profile; onboard recording of pressure, temperature, humidity, winds, aircraft state, and quality metadata; post-flight processing produces agreed exchange file for evaluation by NWS, OAR, or other model-data users
- **Deployment Scale**: Ten systems for reusable vertical profiling and agreed profile-to-file workflow

### Operational Growth Path (Option 2)
- **Cooperative Autonomy**: Decentralized coordination layer allowing aircraft to exchange status for cooperative task allocation and replanning
- **Reduced Ground Dependence**: Preserve useful collection when vehicle or link becomes unavailable
- **Resilience**: Fault-response and repeated-mission evidence supporting more robust incident operations

## Key Results
This is a proposal document with no final results. However, the document references prior BST achievements as risk-reduction evidence:

### S1 Aerial Mapping Heritage (CH2MHill Fly-Off)
- **Coverage**: 693 images over test area; 99.7% usable in processing
- **Geolocation Accuracy**: 7.1 cm mean reprojection error
- **Image Connectivity**: Average 190.11 image connections per pair (demonstrating data-centric flight planning principles)
- **Competitive Performance**: Superior to comparison platforms in image-overlap uniformity and network connectivity
- **Note**: Results apply to historic S1 configuration, not expected S0-VTOL performance; demonstrates principles informing proposed search patterns, overlap management, completeness checks, and georeferenced imagery workflow

### Operational Heritage
- **S0 Air-Deployed Operations**: S0 aircraft have operated from NOAA WP-3D aircraft in tropical cyclones with established launch, communications, ground-control, and data-handling procedures
- **Multi-Aircraft Coordination**: Concurrent operation of two air-deployed S0 aircraft exercised in both clear-air testing and operational missions
- **Wildfire Remote Sensing**: S2 carried multisensor payload (visible, thermal, infrared) for wildfire mapping and fire-radiative-power characterization under NOAA's Nighttime Fire Observations eXperiment
- **Payload Integration Experience**: Multispectral cameras, atmospheric sensors, trace-gas instruments, particulate sensors, radiometers in wildfire, volcanic, Arctic, and Earth-observation missions

## Notable Details

### U.S. Design & Manufacturing
- All airframes, SwiftCore, operator interfaces, payload interfaces, and ground systems designed and manufactured in the United States
- Risk reduction through existing NOAA S0 operating heritage and scientific-payload integration experience

### Demonstration & Transition Strategy
- **One-Operator Demonstration**: Planned centralized multi-aircraft event demonstrating coordinated reconnaissance under a Government-approved waiver or authorization
- **FAA Waiver/Authorization Path**: Task 1 includes development of safety case, concept of operations, operating procedures, and supporting evidence for FAA or Government waiver application
- **Measured Investment**: Establishes reusable, U.S.-manufactured capability while providing practical path from development to repeatable incident-response missions
- **Acceptance & Delivery**: Following Government-observed demonstration and closure of delivery-critical discrepancies, complete acceptance checkout and deliver five EO/IR-capable aircraft, integrated payloads, primary and spare ground equipment, trained operators, procedures, configuration records, and test evidence

### Out of Scope (Base Effort)
- Automated target recognition
- Unrestricted flight in active fire airspace
- Continuous full-resolution video downlink (instead, selected previews downlinked when link conditions permit; high-resolution retained onboard)
- Direct integration with operational common operating picture

### Intellectual Property & Award Pathway
- **IP**: Deliverables may incorporate BST pre-existing SwiftCore, SwiftPilot, SwiftTab, ground-station software, fleet-management software, autonomy functions, and manufacturing know-how; data rights assertions to be defined in agreement
- **SBIR Phase III Sole-Source Pathway**: BST holds SBIR data-rights lineage on S0 program enabling Phase III sole-source award per 15 U.S.C. § 638(r); references NAVAIR N251-016, STTR N6833525C0270, Air Force AF192-005
- **Alternative**: NOAA BAA (open through 30 Sept 2026); Award by mid-September permits FY26 ORF obligation before lapse

### Cost & Schedule
- **Base ROM**: $1.00M / 15 months (5 aircraft, EO/IR payloads, waiver effort, 1 demonstration)
- **Option 1 (Fire-Weather)**: $0.40M / 12 months (10 systems, reference comparisons, 1 demonstration)
- **Option 2 (Cooperative Autonomy)**: $0.70M / 12 months (cooperative functions, reliability/fault-response testing, 1 demonstration)
- **Total Maximum**: $2.10M

### Government-Furnished Resources
- Mission owner, reconnaissance and fire-weather evaluators, operating areas, imagery/profile requirements
- Test-site access, FAA/Government waiver participation, airspace approvals
- Incident surrogates, analyst participation, reference datasets, spectrum/cybersecurity decisions
- Receiving/property personnel, timely review of concept/readiness/demonstration gates