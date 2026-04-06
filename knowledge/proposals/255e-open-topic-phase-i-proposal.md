# 25.5E-Open-Topic-Phase-I-Proposal

## Document Metadata
- **Type:** SBIR Phase I Proposal
- **Client/Agency:** Department of the Air Force (DAF)
- **Program/Solicitation:** AF Open Topic 25.5E (DoD 25.5 Release 10 Commercial Solutions Opening); Proposal Number FX255-PCSO1-1104
- **Date:** Submitted August 5, 2025 (proposal deadline)
- **BST Products/Systems Referenced:** S3 UAS (primary focus), S2 UAS, E2 multirotor, S0 UAS, SwiftCore Flight Management System
- **Key Personnel:** Dr. Jack Elston (Technical Lead, Lead Engineer for Electronic Design & Firmware), Dr. Maciej Stachura (Co-founder, FAA COA & Regulatory Lead)

## Executive Summary

Black Swift Technologies proposes the S3 UAS, a next-generation vertical takeoff and landing (VTOL) uncrewed aircraft system designed for persistent, autonomous, all-weather operations in GPS-denied and contested environments. Building on proven heritage platforms (S2, E2) deployed by NASA and NOAA in extreme conditions (volcanic plumes, hurricanes, wildfires), the S3 introduces solar-powered autonomous recharging, vision-based terrain-relative navigation, and field autonomy enabling sustained unattended operations spanning days to months. The Phase I effort focuses on validating and adapting the S3 platform to meet critical Air Force operational requirements, particularly for base perimeter security, forward area ISR, and autonomous landing zone assessment in austere environments.

## Technical Approach

### Core Technical Innovations

**All-Weather, Field-Hardened VTOL Airframe**
- Swept-wing configuration and vertical stabilizer designed for turbulent, low-altitude flight in gusts exceeding 50 knots
- Comprehensive precipitation resistance and de-icing enhancements
- Conformal electronics bay with ingress protection sealing for rain, snow, dust, corrosive environments
- Redundant avionics, fault-tolerant power distribution, reinforced landing gear for semi-prepared/remote surfaces

**GNSS-Denied Autonomy & Vision-Based Navigation**
- Stereo camera system with onboard embedded processing for terrain-relative navigation and obstacle avoidance
- Real-time semantic classification of safe landing zones
- Hierarchical control architecture supporting safe failover, route replanning, and autonomous decision-making
- Capability for full autonomous launch, patrol, and landing without operator intervention
- Vision-based navigation stack enables precision autonomous landings at unprepared sites and adaptive route replanning
- Partnership with Maxar on novel satellite-imagery-based vision navigation techniques showing promise

**Long-Endurance, Unattended Operation**
- Wing-mounted solar arrays with smart battery management and advanced thermal regulation
- Multiple sorties per day for weeks at a time without returning to base
- In-flight wind estimation and dynamic cruise optimization for energy efficiency in adverse weather
- Ground-effect-aware landing procedures, automated health checks, post-flight diagnostics
- Solar recharge capability enables distributed deployment and unattended multi-sortie autonomy

**TAK-Native Integration & Situational Awareness**
- Full integration with Tactical Assault Kit (TAK) system for seamless interoperability with Air Force command and control workflows
- S3 telemetry, video feeds, mission plans, and alerts streamed to ATAK/CivTAK environments
- Mission planning through TAK plugins; live alerts from onboard analytics (motion detection, anomaly tracking) trigger operator notifications
- Minimal specialized ground control infrastructure required

**Modular Payload Support & Smart Response**
- Swappable EO/IR, multispectral, RF payloads for mission-specific tasks
- Onboard autonomy allows mission behavior modification in response to live alerts or external sensor cues
- Multi-aircraft cooperative capability with swarm-like coverage scalability
- Collaborative work with Ukrainian partners on lightweight drone detection integration

### Development Foundation

- Builds on over a decade of operational UAS experience and proven field deployments
- Leverages flight-tested components and autonomy stacks from NASA, NOAA, DoD campaigns
- Environmental testing completed: EMI, temperature extremes, vibration, ingress protection
- Modular, containerized software for autonomy, navigation, failsafe control portable to higher-assurance environments
- Extensible architecture accommodates future autonomy frameworks and sensor upgrades

## Products & Capabilities Described

### S3 UAS (Primary System)

**What it is:**
- Next-generation Group 2 VTOL fixed-wing hybrid UAS
- Derived from proven S2 platform but with radical design modifications and transformational advances
- Small UAS combining VTOL deployment, GPS-denied autonomy, and solar-based endurance at fraction of logistical burden/cost
- EAR-classified (Export Administration Regulations) rather than ITAR, facilitating commercial sales and international collaboration

**Proposed Use in Defense Context:**
- Base perimeter security and autonomous patrol with unattended operation
- Forward airfield assessment and C-130 landing zone scouting
- Autonomous drone detection and counter-UAS awareness
- Battlefield damage assessment and ISR in contested environments
- CBRN and environmental monitoring with specialized payloads
- Convoy overwatch and mobile threat response

**Specifications & Performance Claims:**
- VTOL capability eliminates need for launch infrastructure
- Operates in precipitation, icing, wind gusts >50 knots
- Days-to-months autonomous unattended operation without returning to base
- Multiple sorties per day capability via solar recharge
- Vision-based autonomous landing at unprepared sites
- GPS-denied navigation and autonomous obstacle avoidance
- Modular payload bay for EO/IR, multispectral, RF, drone detection sensors
- TAK-native situational awareness integration

### S2 UAS (Legacy/Heritage System)

**What it is:**
- Proven fixed-wing small UAS platform with decade of operational experience
- Operates in extreme weather: volcanic plumes, hurricanes, wildfire smoke

**Historical Use & Achievements:**
- NOAA wildfire monitoring (NightFOX project) providing real-time atmospheric data
- NASA volcanic plume sampling in Costa Rica (25-mile range, 7,000 ft altitude gain)
- CO₂ mapping missions over jungle canopy at ~20 m above ground
- NEON site satellite calibration/validation campaigns
- Onboard semantic segmentation for pixel-level video classification
- Methane emissions detection and localization
- Successfully navigated severe turbulence, icing, precipitation

### E2 Multirotor

**What it is:**
- Commercial multirotor platform in BST product line
- Used for GIS, precision agriculture, critical infrastructure inspection

### S0 UAS

**What it is:**
- Ultra-light swarming variant currently under development
- Demonstrates coordinated surveillance and reconnaissance capabilities

## Use Cases & Applications

### Defense/Air Force Use Cases

1. **Base Security & Perimeter Surveillance**
   - Autonomous patrol of installation perimeters
   - Persistent overwatch without requiring full-time operator presence
   - Initial anchor customer: 673rd Security Forces Squadron at Joint Base Elmendorf-Richardson (JBER) for autonomous perimeter patrol and remote facility monitoring in Arctic/sub-Arctic conditions
   - Also engaging Grand Forks Air Force Base

2. **Forward Air Controller Support**
   - Autonomous scouting and validation of C-130 landing strips
   - Temporary airstrip evaluation in austere environments
   - Cargo drop zone reconnaissance

3. **Battlefield Damage Assessment**
   - Repeatable flyovers detecting structural changes
   - Post-kinetic engagement threat assessment

4. **CBRN and Environmental Monitoring**
   - Integration of specialized sensors for airborne hazard detection
   - Gas leak detection
   - Radiological signature detection at remote sites

5. **Convoy Overwatch**
   - Pre-positioned S3 systems loitering over known routes
   - Autonomous response to movement/sensor triggers

6. **Drone Detection & Counter-UAS**
   - Mobile drone detection node for identifying hostile UAS
   - Asset protection for aircraft on ground and munitions storage
   - Currently collaborating with Ukrainian partners on lightweight detection capabilities

7. **Discrete Island-Hopping Operations**
   - Particularly suited to geopolitically sensitive regions (South China Sea)
   - Small size, low acoustic signature, extended endurance
   - GNSS-denied navigation enables autonomous operation without alerting hostile forces
   - Ideal for intelligence collection in electromagnetically contested environments

### Commercial/Non-Defense Use Cases

1. **Methane Leak Detection**
   - Long-range autonomous inspection of energy infrastructure
   - 40,000+ oil and gas wells in Permian Basin alone represent substantial addressable market
   - No need for human operators or local infrastructure

2. **Wildfire Monitoring & Atmospheric Sensing**
   - Operation in harsh environments with smoke, turbulence, low visibility
   - Provides asset to scan area for drones before water bombers begin missions (safety improvement)
   - Currently working with NASA and USFS on drone detection integration

3. **Disaster Response & Search and Rescue**
   - Persistent overwatch and communications relay in post-disaster areas
   - Rapid assessment capability
   - Connections with NOAA and FEMA for hurricane monitoring and post-recovery

4. **Runway Foreign Object Detection (FOD)**
   - Future capability development for expeditionary airfield operations

5. **Scientific Research**
   - Volcano monitoring (CO₂ mapping, multiparametric data collection)
   - Soil moisture analysis
   - Environmental research and satellite validation/calibration

## Technical Risks & Mitigation

1. **Navigation and Perception in GPS-Denied & Low-Light Environments**
   - Risk: Vision-based autonomy may have reduced reliability in challenging lighting or environmental conditions (snow, smoke)
   - Mitigation: Multi-modal sensing redundancy from IMU and airspeed systems; partnership with Maxar on satellite-imagery-based vision navigation showing promising results

2. **Adverse Weather Performance**
   - Risk: Stable flight and accurate data collection during icing, precipitation, high winds (gusts >50 knots) requires robust controls
   - Mitigation: Flight controls and weatherproofing under development based on BST heritage platforms' proven Arctic/extreme weather performance

3. **Regulatory Risk (Non-DoD)**
   - Risk: Beyond-Visual-Line-of-Sight (BVLOS) operations remain constrained in U.S., limiting commercial methane leak detection market entry
   - Mitigation: Active collaboration with NASA and FAA to build safety case and conduct test campaigns supporting regulatory pathways; not a constraint for Air Force use case

## Phase I Objectives & Work Plan

### Scope
Validate and adapt the S3 autonomous persistent UAS platform to meet critical DAF operational needs with initial emphasis on autonomous base security, forward airfield support, and integrated drone detection capabilities.

### Key Phase I Objectives

1. **DAF End-User Discovery & Engagement (Days 5-60)**
   - Direct outreach to 10-20 DAF stakeholders across base security, combat communications, expeditionary air base operations
   - Identify specific mission contexts (base surveillance, drone detection, landing zone scouting, distributed ISR)
   - Build on existing engagement with JBER; expand to AFWERX and Air Force Security Forces ecosystem
   - Success marker: Positive replies for follow-ups from at least 5 end-users

2. **Problem Refinement & Gap Analysis (Days 15-60)**
   - Conduct interviews with Air Force leaders and promising end-users
   - Deeply understand operational challenges, mission limitations, capability gaps
   - Produce detailed write-up of end-users, pain points, current capability gaps
   - Identify needs: GPS-denied navigation, weather resilience, unattended operation, TAK interoperability

3. **Technical Adaptation & Specification Definition (Days 40-80)**
   - Structured engineering study defining necessary modifications to S3 platform for selected DAF use cases
   - Address hardware requirements (payload integration, cold-weather operation, icing resistance)
   - Software requirements (autonomy behaviors, TAK data flow standards)
   - Procedural considerations
   - Deliver detailed list of capabilities needed for DAF users, especially novel requirements

4. **Definition of Phase II Trial & Demonstration Roadmap (Days 40-90)**
   - Collaborate with early end-user stakeholders on demonstration objectives
   - Define transition pathway into operational environments
   - Identify trial location (JBER or other Air Force installation)
   - Establish success criteria and evaluation framework
   - Develop roadmap for Phase II integration and sustainment

5. **Final Report & Phase II Plan (Days 60-90)**
   - Synthesize findings from customer discovery, technical adaptation, mission alignment