# Blue UAS Mission SBIR Phase I - Technical Overview

## Document Metadata
- **Type:** SBIR Phase I Proposal / Technical Presentation
- **Client/Agency:** U.S. Air Force (Department of Air Force)
- **Program/Solicitation:** Air Force SBIR Topic AFX235-CSO1 ("An All Weather and Multi-Mission UAS for Air Force Bases")
- **Proposal Number:** FX235-CSO1-1575
- **Date:** Submitted 2023 (created/modified October 23, 2023)
- **CAGE Code:** 6PGF9
- **BST Products/Systems Referenced:** S3 (primary), S2, S1, E2, SwiftCore/SwiftPilot FMS
- **Key Personnel:** 
  - Dr. Jack S. Elston (CEO, Principal Investigator)
  - Dr. Maciej Stachura (Chief Technology Officer, Aircraft Design & Systems Engineering)

---

## Executive Summary

Black Swift Technologies proposes to adapt its S3 vertical takeoff and land (VTOL) fixed-wing UAS to provide a modular, all-weather unmanned aircraft system for multi-mission capability at Department of Air Force (DAF) bases globally. The system addresses critical needs for 24/7 base security, emergency response, civil engineering support, and specialized sensing operations in extreme conditions (45+ mph winds, -40°F to +110°F temperatures, heavy precipitation) while reducing operator workload through autonomous operation and on-board diagnostics.

---

## Technical Approach

### Core Concept
Adapt BST's existing S3 VTOL fixed-wing UAS platform—designed for extreme atmospheric research—for military base operations requiring:
- All-weather capability (24/7/365 operation)
- Rapid deployment and modular payload integration
- Seamless integration with existing Air Force command and control systems
- Reduced operator cognitive load through advanced autonomy

### Key Technical Capabilities Proposed
1. **Intelligent Wind and Terrain-Aware Control**
   - Enable high-wind VTOL operations (45+ mph sustained winds)
   - Dynamic terrain and obstacle avoidance

2. **Specialized Aerodynamic Design**
   - Efficiency optimized for turbulent environments
   - Extended endurance: 90 minutes default at 45 mph cruise with full payload; 4+ hours with smaller payloads or integrated solar

3. **Advanced Autonomy**
   - Automatic adaptation to changing conditions and vehicle status
   - Automated pre-flight checks and mission planning
   - Machine learning-based fault prediction and detection
   - Vision-based GPS-denied navigation and automated emergency landing

4. **Distributed, Redundant Systems Architecture**
   - Service discovery-based subsystems enabling fault tolerance
   - On-board vision and radar-based obstacle/terrain avoidance
   - Machine learning system for predictive maintenance and automatic diagnostics

5. **Operational Features**
   - Tool-free setup/breakdown with glove-compatible assembly
   - IP-rated aircraft design for ingestion protection (volcanic ash, corrosive gases, precipitation)
   - Rapid deployment: ready to launch within minutes
   - Maximum dash speed: 100 mph
   - Temperature range: -40°F to +110°F

### Systems Integration
- Integrates with existing DAF Command & Control systems
- Modular payload architecture allowing flight-line reconfiguration
- Energy-aware warning system for rapidly evolving flight conditions
- Energy extraction through dynamic soaring to extend mission duration

---

## Products & Capabilities Described

### S3 (Primary Platform)
- **What it is:** VTOL fixed-wing UAS, Group 1-2 classification, evolved from BST's extreme-environment research heritage
- **Proposed use in this context:** Adapted as multi-mission platform for base-level DAF operations
- **Key specifications/performance:**
  - Operates in 45+ mph winds, -40°F to +110°F temperatures, heavy precipitation
  - 90-minute default endurance at 45 mph with max payload; extendable to 4+ hours
  - Maximum dash speed: 100 mph
  - 24/7/365 capable
  - Modular payload system for rapid mission reconfiguration

### SwiftCore/SwiftPilot Flight Management System (FMS)
- **What it is:** Proprietary, modular autopilot/flight control system with built-in redundancy
- **Use:** Core avionics for the adapted S3; provides autonomous flight capability
- **Notable feature:** Developed from ground-up by BST team; includes advanced control algorithms, firmware, and user interface

### Soil Moisture Measurement Payload
- **What it is:** Remote sensing payload for measuring soil moisture via UAS
- **Demonstrated use:** Currently deployed with USGS for wildfire mitigation; NASA Phase III contract for expanded capability
- **Relevance:** Example of BST's modular payload expertise applicable to CBRN and other sensing needs

### Vision-Based Safe-to-Land System
- **What it is:** Machine vision system for automated landing without pre-planned landing zones
- **Development:** NASA-funded effort; demonstrated in 2018
- **Relevance:** Supports autonomous operation claim and reduces operator workload

### Solar Panel Integration
- **What it is:** Solar cells integrated on aircraft wings
- **Capability:** Extended endurance (4-6 hours per flight) with ground-based recharging enabling month-long autonomous campaigns
- **Application relevance:** Supports 24/7/365 persistent monitoring potential

### Airdata Systems
- **Capability:** Mitigate ice and heavy precipitation ingestion
- **Feature:** Critical for all-weather operation mandate

---

## Use Cases & Applications

### Primary Proposed DAF Mission Sets
1. **Perimeter Surveillance for Security Forces**
   - 24/7 base security monitoring
   - Automated rapid response to perimeter events

2. **High-Resolution Orthoimagery for Civil Engineering**
   - Base infrastructure survey and mapping
   - Terrain characterization

3. **Emergency Response**
   - Rapid deployment with modular payloads
   - On-call incident response (fires, accidents, etc.)

4. **Chemical, Biological, Radiological, Nuclear (CBRN) Sensing**
   - Modular payload integration for specialized sensors
   - Hazardous environment operations without pilot risk

### Geographic Focus (Phase I Customer Discovery Targets)
- **Elmendorf Air Force Base, Anchorage, AK** (Point of Contact: Lt Col David Wilson)
  - Arctic operations; extreme cold/wind testing ground
- **Grand Forks Air Force Base, Grand Forks, ND** (Point of Contact: MSgt Jason Carey, North Spark Defense Lab)
  - Significant temperature and wind extremes; key test location cited in abstract
- **Thule Air Base, Greenland** (Point of Contact: CMSgt John Bentivegna)
  - Extreme Arctic environment
- **INDOPACOM-Pacific Theater bases** (Eielson AFB, Misawa AB, others)
  - Force readiness enhancement in contested Indo-Pacific region

### Historical BST Use Cases (Demonstrating Extreme-Environment Pedigree)
- Volcano monitoring (Makushin, Alaska USGS pathfinding mission 2012; NASA SBIR since 2012)
- Hurricane observations and storm sampling (initial NOAA SBIR 2017)
- Wildfire mitigation via soil moisture mapping
- Tornado intercept and in-situ atmospheric sampling (VORTEX2 participation)
- Greenland glacier research campaigns at 14,000+ ft in -20°C conditions (2015)
- Wind profiling in 40+ mph winds for USAF (2013)

---

## Key Technical Accomplishments & Product History

### Foundational Technology Development Timeline
- **2011:** BST founded; began developing modular UAS from ground-up
- **2012:** Initial NASA SBIR for volcano observation platform (~$2M funding leading to $2M+ additional investment)
- **2013:** USAF Phase I & II for wind profiling UAS (15,000 ft capability in 40+ mph winds)
- **2015:** Greenland campaign with 14,000+ ft operations in -20°C
- **2016:** 
  - Development and initial sales of S2 fixed-wing UAS ($1M in system/payload sales to date)
  - Development of E2 multi-rotor for infrastructure inspection
  - Profitable revenue growth begins
- **2018:**
  - NASA Phase I & II for machine learning predictive maintenance algorithms
  - Flight demonstration of machine vision safe-to-land system
  - Continued S2 sales traction
- **2019:**
  - Development of S1 photogrammetry platform (reportedly outperformed all competitors in fly-off)
  - NASA SBIR for soil moisture payload (~$2M funding)
- **2020:** 
  - SwiftCore FMS development and first sales
- **2021:**
  - NASA Phase III contract for soil moisture, volcano monitoring, and CO2 detection
  - Two NOAA contracts: tube-launched air-deployed UAS for hurricanes; soil moisture in mountainous terrain
- **2023:**
  - Projected $2M revenue
  - Commitments from University of Maryland Eastern Shore, NOAA, NASA for 2023+ deliveries

### Intellectual Property & Proprietary Systems
- End-to-end UAS IP: user interface, ground station, communications protocol, avionics, control algorithms, vehicle design
- SwiftCore/SwiftPilot FMS: proprietary modular flight management system with built-in redundancy
- Advanced sensing integration (vision-based, radar-based)
- Machine learning-based fault detection/prediction
- Dynamic soaring algorithms for energy extraction
- Vision-based GPS-denied navigation and emergency landing systems

### Technology Readiness Levels (TRL)
- Large portfolio of foundational UAS technology with **several items at TRL-9** (production/operational)
- S2 and S1 have demonstrated commercial viability
- SwiftCore FMS in operational use

---

## Commercialization & Market Positioning

### Financial Performance
- **Cumulative revenue since 2011:** $6.8M+
- **2023 projected revenue:** $2M
- **Profitable revenue growth:** Consistent since 2016
- **SBIR Awards:** 18 total Phase I awards; 7 Phase II awards accepted; $5.754M in total SBIR funding received
- **Revenue sources:**
  - Phase III NASA contract (soil moisture, volcano monitoring, CO2 detection)
  - Two NOAA contracts (hurricane observations, soil moisture mapping)
  - USGS soil moisture payload for wildfire mitigation
  - S2 product sales ($1M cumulative)
  - Bootstrapped company; discussing additional investor commitments for commercial offerings

### Market Analysis
- **Global military drone market:** 
  - 2020 valuation: USD 19.23 billion
  - 2028 projected: USD 63.05 billion
  - CAGR: 16.01% (2021-2028)
- **BST differentiation:** 
  - Price competitive with commercial market (2-5x lower cost than DoD-specific UAS with similar mission sets)
  - US-made systems
  - Modular design enabling rapid customization
  - Extreme-environment heritage and proven reliability

### Existing Customer Base
**Defense:**
- U.S. Air Force (three successful SBIR projects delivered; customers in AFLCMC and AMC)
- USGS
- U.S. Navy/Naval research

**Non-Defense:**
- NASA (Goddard Space Flight Center, Jet Propulsion Laboratory)
- NOAA
- The University of Miami
- University of Colorado
- University of Maryland Eastern Shore
- Alerion Technologies
- Turf Scout (commercial soil moisture)

### Strategic Recognition
- **Top 50 Colorado Companies to Watch** designation
- Four profitable product lines (S0, S1, S2, E2; plus SwiftCore FMS)

### Transition/Commercialization Strategy (Post-Phase I)
1. Continue engagement with Grand Forks AFB, Thule AB, and other DAF organizations
2. Develop Phase II proposal to adapt and field S3 with identified end-user
3. Follow Phase II with Technology for Advanced Command and Control/Sustainment (TACFI) or Sustainment and Training for Force Integration (STRATFI) effort
4. Utilize sole-source acquisition authority for rapid transition of S3 prototype into operational environment
5. First delivery system to Grand Forks AFB for field operations and validation
6. Parallel commercialization with non-defense partners (NOAA, NASA, US