# UAS Specifications for Volcanic Gas Observation Missions

## Document Metadata
- Type: Technical Volume / Proposal
- Client/Agency: INFICON (inferred from file path)
- Program/Solicitation: Not explicitly stated (appears to be phase-based work: Phase II mentioned)
- Date: 2023-09-13 to 2023-09-19 (creation/modification dates)
- BST Products/Systems Referenced: E2 UAS, S2 fixed-wing UAS, multi-rotor UAS (in development)
- Key Personnel: Geoff Bland (NASA GSFC contact)

## Executive Summary
Black Swift Technologies proposes developing a multi-rotor UAS to carry spectrometer payloads for volcanic gas observation missions, building on proven experience from E2 and S2 platforms flown in extreme volcanic environments. The effort includes NASA and FAA approval processes for safe operations over active volcanoes including Kilauea and Makushin.

## Technical Approach

**Baseline Platform (E2 UAS):**
- Multirotor design originally developed for wind turbine inspections
- Adapted for precipitation-resistant operations in volcanic environments
- Limited to 2kg payload capacity
- Proven in NASA scientific campaigns

**Proposed New Platform:**
- Multi-rotor UAS to carry larger spectrometer payloads (exceeding E2's 2kg limit)
- Will utilize BST's publicly available software development toolkit and API
- Same software/electronics as other certified BST aircraft
- Designed for 1-2 person crew operation
- Portable system for rapid deployment at multiple sites

**Software/Control Integration:**
- Payload control through radio links
- Real-time telemetry display for instrument status monitoring
- Capability to modify flight patterns in real-time based on measurements
- Data interface via BST's public SDK and API

## Products & Capabilities Described

### E2 UAS
- **What it is:** Multi-rotor platform originally for wind turbine inspections
- **Volcanic experience:** Flown in Costa Rica (Turrealba volcano, Rincon Viejo) with Cal Tech and JPL for trace gas observations
- **Adaptations:** Precipitation-resistant design for harsh volcanic environments
- **Performance specs:**
  - Endurance: ~30 minutes
  - Velocity: ~5 m/s
  - Payload capacity: 2kg (limiting factor for this application)

### S2 Fixed-Wing UAS
- **What it is:** 3-meter wingspan fixed-wing platform
- **Volcanic experience:** Recent operation (August 7, 2023) at Makushin Volcano, Alaska for USGS Volcano Science Center
- **Performance specs:**
  - Range: 15+ miles (traveled 5 miles to volcano, then 10 miles to edifice)
  - Altitude capability: Can climb 6,000+ feet (demonstrated 7,000 ft climb capability)
  - Endurance: Extended (sufficient for multi-leg missions)
  - BVLOS certified: Operated 25+ miles beyond visual line-of-sight
  - Wind rating: Capable of 50kt winds
- **Operations:** Pneumatic launcher capable, includes onboard imaging camera

### Proposed Multi-Rotor Platform
- **What it is:** New development to carry spectrometer and larger payloads
- **Payload capacity:** >2kg (specific capacity not stated)
- **Software base:** Reuses certified BST electronics and software from S2/E2
- **Operational design:** 1-2 person crew operation, portable, easy transport and setup

## Use Cases & Applications

### Kilauea, Hawaii
- **Mission scope:** 1km x 1km survey area centered on Kilauea
- **Altitude profiles:** 50m, 100m, and 150m AGL surveys
- **Flight parameters:**
  - Endurance requirement: ~30 minutes
  - Total path length: ~9km
  - Path spacing: ~150m minimum (due to endurance constraints)
- **Flight path challenges:**
  - 50m AGL: Terrain constraints from raised rim; requires ~113° FOV
  - 100m AGL: Feasible; requires ~74° FOV
  - 150m AGL: Feasible; requires ~53° FOV
  - Three altitudes require separate missions due to endurance/path length constraints

### Makushin Volcano, Alaska
- **Mission profile (recent actual flight):**
  - Takeoff from pneumatic launcher at Dutch Harbor
  - 5-mile transit at <400 ft AGL
  - Entry into Temporary Flight Restriction (TFR) airspace
  - 6,000 ft climb to volcanic edifice altitude
  - 10-mile transit to volcano summit
  - BVLOS operations approved
  - Demonstrated capability in up to 50kt winds
- **Measurements:** Volcanic gas observations
- **Client:** USGS Volcano Science Center
- **Success:** Two complete missions flown (August 7, 2023)

### General Volcanic Applications
- Trace gas observations in volcanic plumes
- High-altitude operations in extreme environments
- In situ atmospheric chemical measurements
- Areas too hazardous for manned aircraft

## Regulatory & Approval Experience

**NASA Approvals:**
- 6 completed Airworthiness Flight Safety Review Boards (AFSRB)
- Multiple Flight Readiness Review Boards (FRRB)
- Latest approval: Makushin volcano operations with BVLOS flight restrictions and challenging wind/terrain conditions
- Established as "leading NASA partner for UAS development and flight testing"

**FAA Approvals:**
- BVLOS operations approval demonstrated
- Temporary Flight Restriction (TFR) operations experience
- Pneumatic launcher operations approved

**Planned Approvals:**
- NASA AFSRB and FRRB for this specific effort
- FAA documentation for proposed operations

## Facilities & Resources

**Boulder, CO Headquarters:**
- 1,600 sq ft facility
- Electronics benches and prototyping shop
- Full atmospheric and aircraft simulation suite
- Multiple complete autopilot systems (FMS, ground station, user interface, communications)
- QC and integration capabilities
- Meeting space for stakeholder coordination

**Manufacturing:**
- In-house: Prototyping, assembly, sensor/avionics integration, QA
- Outsourced: Composite airframe work to Northwind Composites

**Testing Sites:**
- Local: Fenced field 10 minutes from office
- Regional: 20 x 20 mile test area in Pawnee National Grasslands (planned primary Phase II test site)
- High altitude: San Luis Valley with peaks to 15,000 ft MSL (regulatory limit for current operations)
- NASA authorization: Permission secured to operate multiple UAS at Pawnee site

## Notable Details

- **Payload Integration:** Public API allows third-party sensor developers to integrate and control instruments without extensive BST involvement
- **Cost efficiency:** Emphasis on repair/replacement economics vs. manned or larger UAS in high-risk applications
- **Rapid deployment:** Portable system design enables quick setup at multiple volcano sites
- **Risk mitigation:** Multi-aircraft deployment feasible with relatively low-cost platforms
- **Competitive positioning:** BST characterized as having unique experience in demanding atmospheric research, specifically extreme conditions (high-altitude, arctic, desert, particulates, turbulence)
- **Real-time adaptation:** Measurement-responsive flight planning enables efficient data collection
- **Recent success:** August 2023 Makushin operation demonstrates current operational maturity

## Unspecified Technical Details
- Exact payload capacity of proposed multi-rotor platform
- Timeline for Phase II development
- Specific spectrometer specifications or interface requirements
- Detailed cost estimates
- Comparative analysis with alternative approaches