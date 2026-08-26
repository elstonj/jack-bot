# Extending Lower-Atmosphere Observations with Air-Deployed and Reusable UAS

## Document Metadata
- **Type:** White paper / capability proposal
- **Client/Agency:** NOAA Office of Marine and Aviation Operations (OMAO) / Uncrewed Systems Operations Center
- **Program/Solicitation:** NOAA standing Broad Agency Announcement (open through 30 Sept 2026); potential SBIR Phase III sole-source under 15 U.S.C. § 638(r); NOAA IDIQ vehicle 1305M226D0012
- **Date:** August 17, 2026
- **BST Products/Systems Referenced:** S0 (air-deployed), S0-VTOL, SwiftCore (flight management), SwiftPilot, SwiftTab, S2 (NightFOX program)
- **Key Personnel:** Cory Dixon (last editor)

## Executive Summary
BST proposes an 18-month pilot program integrating one autonomous ground station with two S0-VTOL aircraft to provide frequent, lower-atmosphere atmospheric profiles to supplement NOAA's radiosondes. The system would operate at an approved range under VLOS controls with centralized fleet-management architecture designed to scale toward supervising multiple geographically distributed stations. The effort aims to demonstrate that reusable, recoverable UAS can increase observation frequency and geographic density while reducing operational labor and consumable logistics compared to balloon-based radiosondes.

## Technical Approach

### System Architecture
- **Station:** One autonomous, self-contained enclosure providing environmental protection, aircraft storage, battery charging, launch/recovery support, health monitoring, data transfer, and communications
- **Aircraft:** Two modified S0-VTOL aircraft capable of vertical launch/recovery (pivoting motors) with fixed-wing cruise efficiency
- **Flight Management:** SwiftCore autonomous flight-management system controls climbs, descents, altitude holds, profile segments, and precision recovery
- **Ground Control:** Centralized fleet-operations software aggregating station status, weather gates, aircraft health, mission schedules, data transfer, and maintenance actions
- **Communications:** Long-range RF capability; communications-availability monitoring and mission suspension when integrity is insufficient

### Station Functions (Autonomous Enclosure)
- Pre-flight monitoring: internal temperature, precipitation, wind, aircraft state, battery condition, communications, navigation availability, landing-zone status
- Automated health checks and readiness assessment
- Launch authorization and aircraft release
- Precision landing support via landing camera and companion computer with vision-assisted terminal guidance
- Aircraft securing and post-flight verification
- Controlled battery recharge with faults placing system in safe state
- Data and system-log transfer to central operations
- Alert generation and exception prioritization

### Flight Profiles
- Pressure, temperature, relative humidity, and three-dimensional wind measurements
- Autonomous execution of approved altitude profiles within defined envelope
- Ability to ascend/descend at controlled rates, hold at selected altitudes, repeat segments
- Maximum altitude: 15,000 feet AGL (subject to site elevation, airspace, weather, energy reserve, approval)
- Maximum endurance: 60 minutes
- On-board data recording with timestamps, position, aircraft state, calibration, and quality indicators
- Real-time or delayed data transmission through ground system

### Environmental Hardening & Cold/Icing Mitigation
- Bounded operational envelope rather than unrestricted icing claim
- Assessment of effects on atmospheric probe, propulsion, control surfaces, batteries, camera, enclosure, communications
- Candidate mitigations: coatings, localized heating, component changes, icing awareness, enclosure thermal management, procedural weather gates
- Environmental and flight evidence will establish allowable operational conditions

### Safety & Contingency
- Confidence gates for terminal guidance: unacceptable position integrity, visual confidence, landing-zone status, wind, or aircraft health command hold, go-around, alternate landing, or operator intervention
- Battery-management interfaces prevent charging outside approved limits; faults place system in safe state
- Automated exception management and alert prioritization
- Contingency procedures, operational-risk analysis, cybersecurity boundaries, role-based operator controls
- FAA safety roles (remote pilot in command, visual observers) assigned per approved test construct during pilot phase

### Operational Concept—Production Target
- **Pilot Phase:** One operator, one station, VLOS controls with on-site visual observers (regulatory requirement during testing, not production design)
- **Production Objective:** Centrally supervised BVLOS (Beyond Visual Line of Sight) operation without on-site observers; target of up to 30 concurrent station operations per fleet operator (subject to validation and FAA authorization)
- **Operator Role:** Fleet operators supervise autonomous missions, manage exceptions, escalate safety-critical events rather than manually pilot aircraft
- **Workload Model:** Under nominal conditions, stations execute approved profiles autonomously requiring operator acknowledgement; system prioritizes only conditions requiring human judgment; suspends new launches when workload, communications, weather, or unresolved alerts exceed thresholds
- **Maintenance Concept:** Physical maintenance, cleaning, calibration, battery replacement, exception response remain operator responsibility; "unattended" does not mean maintenance-free

## Products & Capabilities Described

### S0 (Air-Deployed UAS)
- **What it is:** Long-endurance, gravity-deployed atmospheric observation aircraft developed for severe weather environments
- **Deployment history:** Operated from NOAA WP-3D aircraft in tropical cyclones under established launch procedures and NOAA data workflows
- **Capabilities:** Extreme-wind/precipitation tolerance; delivers pressure, temperature, humidity, three-dimensional wind observations from locations inaccessible to crewed aircraft
- **Sensing:** Pressure, temperature, humidity, three-dimensional wind
- **Heritage:** Air-deployed S0 measurements validated against instrumented towers (DOE ARM Southern Great Plains site), radiosondes, dropsondes, streamsondes, tail Doppler radar, high-resolution atmospheric models
- **Known characterization needs:** Sensor response during rapid vertical motion, aircraft-induced temperature/humidity bias, wind-estimation behavior in tight turns

### S0-VTOL
- **What it is:** Reusable variant of S0 designed for autonomous atmospheric profiling from austere locations
- **Propulsion:** Pivoting motors enable vertical launch/recovery without launcher or runway; fixed-wing cruise supports efficient profiling
- **Sensing:** Same core atmospheric sensors as S0 (pressure, temperature, humidity, three-dimensional wind); includes landing camera and companion computer for terminal guidance
- **Altitude capability:** Up to 15,000 feet AGL (subject to conditions)
- **Endurance:** Maximum 60 minutes
- **Design features:** Battery-management interfaces, health status outputs, data-transfer capability, mechanical/electrical integration for autonomous enclosure operation
- **Integration:** Modified for enclosure operation with charging interfaces, vision-assisted terminal guidance, companion computing
- **Availability:** Two aircraft in base effort—one primary operational, one spare/test article

### SwiftCore
- **What it is:** BST's autonomous flight-management architecture and avionics foundation
- **Functions:** Controls climb, descent, altitude hold, profile execution, return to site, terminal guidance
- **Commonality:** Used across S0, S0-VTOL, and other BST platforms
- **Autonomy level:** Enables unattended profile execution within approved envelopes

### Centralized Fleet-Operations Software
- **What it is:** Ground control and fleet-management system designed for distributed station supervision
- **Aggregation functions:** Station status, weather gates, aircraft health, communications quality, mission schedules, data-transfer state, maintenance actions
- **Operator interface:** SwiftPilot and SwiftTab software (BST proprietary)
- **Capabilities:** Concurrent mission scheduling, station-state aggregation, health monitoring, role-based operator controls, alert prioritization, exception queues, workload limiting, communications-state management, maintenance escalation, audit logging
- **Deterministic fault injection:** Planned for testing (nominal/faulted conditions, simultaneous weather holds, communications loss, failed preflight checks, charging faults, recovery exceptions, overdue maintenance, multiple concurrent alerts)
- **Production scaling target:** Support 30 concurrent station operations per fleet operator (to be validated)

### S2 (Referenced)
- **What it is:** Atmospheric observation aircraft
- **Past use:** NightFOX program—lightweight multisensor payload for wildfire mapping and fire-radiative-power measurements
- **Relevance:** Demonstrates BST's NOAA scientific-payload experience

## Use Cases & Applications

### Primary Use Case: Lower-Atmosphere Observation Augmentation
- **Mission:** Increase frequency and geographic density of lower-atmosphere observations to supplement NOAA's 92 radiosondes
- **Target conditions:** Rapidly changing lower-atmosphere conditions where temperature, moisture, winds, stability, and turbulence evolve quickly
- **Advantage over balloons:** Recoverable platform can repeat profiles from same location, vary observation schedule, measure higher-rate three-dimensional winds from controlled flight
- **Complementary role:** Reusable UAS stations complement—not replace—radiosondes; balloon soundings remain essential for full-depth stratospheric observations

### Operational Scenarios
- **Event-driven profiling:** Support critical-weather releases with flexible scheduling
- **Remote site operations:** Reduce staffing and resupply burden at geographically isolated stations
- **Atmospheric River, winter-weather, or other airborne-science campaigns:** (Option 2) 50 air-deployed S0 systems for OMAO host-aircraft deployment

### Geographic Scope
- NOAA's existing 92 radiosonde locations across North America and Pacific Islands
- Remote sites where personnel logistics are particularly consequential
- Approved pilot site and range (to be designated by NOAA)

## Proposed Scope & Tasking

### Base Effort (18 months)
**Task 1 — System Design Concept**
- Define mission, pilot site, observation schedule, altitude/airspace envelope, variables, reference sources, data products, latency, weather limits, operator roles, cybersecurity, maintenance, success criteria, production concept
- Develop integrated architecture (power, thermal, charging, battery management, aircraft restraint, communications, launch/recovery, health monitoring, data transfer, degraded modes, emergency behavior, VLOS sequencing, BVLOS transition path)
- Define centralized fleet-operations concept (fleet-operator and regulatory roles, station-state aggregation, mission scheduling, alert taxonomy, exception prioritization, communications/cybersecurity dependencies, maintenance escalation, workload measures, evidence for 30-station ratio)
- Conduct system-design and preliminary safety reviews

**Task 2 — Aircraft Integration and Environmental Hardening**
- Modify two S0-VTOL for enclosure operation (battery-management interfaces, health/status outputs, landing camera, companion computing, vision-assisted terminal guidance, data transfer, mechanical/electrical integration)
- Evaluate cold and icing effects; implement coatings, heating, component changes, monitoring, procedures
- Define supported operating envelope

**Task 3 — Autonomous Enclosure Development and Integration**
- Design and fabricate one prototype enclosure (environmental protection, storage, controlled charging, internal/external monitoring, communications, launch preparation, landing-zone support, data transfer, event logging, maintenance access)
- Integrate enclosure, aircraft, ground-control station, remote interface, site equipment into single configuration

**Task 4 — Progressive Verification and Unattended VLOS Demonstration Readiness**
- Component, software-in-the-loop, hardware-in-the-loop, environmental, charging, stationary launch/recovery, precision-landing, profile, degraded-mode, and repeated-cycle testing
- Develop command-and-control, operational-risk, airspace, contingency, remote-intervention evidence for approved-range demonstration under VLOS
- Verify station exposes aircraft-health, mission, communications, charging, weather, maintenance, fault states required by future fleet-management service
- Define fault scenarios, operator-workload measures, test procedures for subsequent one-to-many evaluation
- Demonstrate unattended station sequencing under VLOS
- Document requirements for later BVLOS and multiple-aircraft authorization
- Close flight-critical discrepancies before site event

**Task 5 — Co-Located Demonstration**
- Install pilot at approved range beside upper-air or comparable reference capability
- Conduct paired or closely timed S0-VTOL and radiosonde/reference observations
- Execute repeated automated cycles under VLOS
- Deliver synchronized aircraft, enclosure, atmospheric, reference, video data
- Evaluate observation quality, data availability, launch/recovery performance, recharge, environmental limitations, staffing, operator interventions, maintenance, logistics

**Task 6 — Transition Package**
- Deliver validated configuration, interfaces, test evidence, operating/emergency procedures, training, maintenance assumptions, data documentation, production concept, cost-per-profile analysis
- Recommendations for candidate sites, spares, sustainment, follow-on deployment
- Preliminary centralized fleet-operations and unit-economics model addressing operator-to-station ratios, shift assumptions, alert demand, communications support