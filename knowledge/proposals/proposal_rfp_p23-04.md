# Proposal RFP #P23-04: Graph Neural Networks (GNN) for UxS Collaborative Agent Control

## Document Metadata
- **Type:** Army Phase I SBIR Proposal
- **Client/Agency:** U.S. Army (via Barron-Associates as prime contractor)
- **Program/Solicitation:** Army Phase I SBIR Topic A214-044
- **Date:** January 13, 2023
- **BST Products/Systems Referenced:** E2 Multirotor UAS, S2 UAS, S0 UAS, SwiftCore Flight Management System
- **Key Personnel:** Dr. Jack S. Elston (CEO, co-founder, PI)

## Executive Summary
Black Swift Technologies proposes to adapt its E2 multirotor UAS platform for Army swarming and collaborative multi-agent operations by integrating Barron-Associates' software suite and expanding open interfaces to support advanced autonomy and teaming capabilities. The effort aims to enable Army personnel to deploy larger teams of UAS for similar operational cost and effort as single aircraft today, achieving 5-10x improvements in coverage without increased operator workload.

## Technical Approach
- **Platform Adaptation:** Modify the existing E2 multirotor UAS for Barron-Associates/Army integration
- **Software Integration:** Integrate Barron software suite into E2 avionics
- **Interface Expansion:** Update open interfaces in SwiftCore FMS to support higher-level collaborative capabilities
- **Architecture:** Leverage BST's distributed computing architecture with intelligent nodes and message-based bus (rather than centralized autopilot approach used by competitors)
- **Communication & Data Management:** Develop in-house communication and data management system ensuring continuous data collection while maintaining sUAS command and control via open interfaces
- **Key Design Principle:** Create seamless, automatic teaming capability reducing operator workload while enabling multi-vehicle autonomy

## Products & Capabilities Described

### Black Swift E2 Multirotor UAS
- **Type:** Rugged multirotor developed for autonomous infrastructure inspection; adapted here for Army swarm operations
- **Specifications:**
  - Flight ceiling: 14,000 ft
  - Max endurance: 35 minutes nominal
  - Max takeoff weight: 25 lbs
  - Max payload: 6.5 lbs
  - 4× 360Kv motors
  - Max winds endured: 30 mph
  - Custom Li-ion battery: 42,000mAh (6 cells)
  - Telemetry: 900 MHz ISM
- **Features:**
  - Field-swappable payload capability
  - Forward-mounted payload for full field-of-view
  - Folds into custom carrying case
  - Designed for minimal training requirements
  - Software flight simulator available
- **Proposed Use:** Foundation platform for Army collaborative multi-agent swarm operations

### SwiftCore Flight Management System (FMS)
- **Components:** Integrated autopilot, tablet-based ground control station, intuitive GUI
- **Design Philosophy:** 
  - Fully in-house design and code (not open source)
  - Sandboxed mission-critical core with secure code/algorithms
  - Open interfaces for third-party integration
  - Distributed computing architecture (intelligent nodes vs. centralized autopilot)
  - High-level message-based bus for computing task distribution
- **Capabilities:**
  - "Smart" sensor-based control minimizing operator workload
  - Autonomously modifies flight path based on sensor inputs
  - Subsystem lifecycle tracking
  - Preventative maintenance integration
  - Safety through redundancy
- **Proposed Expansion:** Update interfaces to support advanced autonomy and swarming

### Black Swift S2 UAS
- **Type:** Fixed-wing workhorse platform
- **Specifications:**
  - Payload capacity: 5 pounds
  - Endurance: 110 minutes
  - Ceiling: 6,000 meters (20,000 feet AGL)
  - Range: 110 km
  - Modular, field-swappable payload nose cone
- **Use:** Referenced as proven atmospheric sampling platform; potential future transition platform

### Black Swift S0 UAS
- **Type:** Small, ruggedized VTOL or tube-launched fixed-wing UAS
- **Use:** Low-cost swarm solutions; originally developed for NOAA hurricane sampling via P-3 air deployment
- **Reference:** Mentioned as part of BST's portfolio and potential application for swarming

## Use Cases & Applications

### Current BST Operational Uses (Portfolio Examples)
- **Arctic Operations:** High-altitude, high-latitude atmospheric research in Greenland (temperatures -20°C, altitudes to 14,000 ft), water vapor analysis
- **Coastal Monitoring:** Coastline observation with thermal and hyperspectral payloads; Landsat-8 and VIIRS instrument calibration
- **Trace Gas Detection:** Airborne measurements of CO2, SO2, CH4, H2S; orthomosaic, thermal, and 3D data products
- **Wildfire Support:** Nighttime in situ measurements of wildfire plumes; remote measurement of fire properties using CO2, CO, aerosol, RH/pressure/temperature sensors
- **Volcano Monitoring:** Plume monitoring with gas-specific sensors and nephelometer for particle size/distribution analysis
- **Soil Moisture Mapping:** L-band radiometer measurements up to 10 cm depth; coverage up to 600 acres per flight

### Proposed Army Application
- **Collaborative Swarm Operations:** Multi-vehicle autonomous teaming for enhanced coverage and reduced operator burden
- **Objective:** Enable Army to deploy larger UAS teams at similar cost/effort as single platforms today

## Key Findings & Capabilities Addressed

### Military Need
- Document references FY20 Industrial Capabilities report to Congress highlighting:
  - Current air-deployed DoD vehicles lack open interfaces, modular architecture, or rapid upgradability
  - Four randomly selected U.S. sUAS platforms designed for DoD relied heavily on Chinese suppliers (security/supply chain risk)
  - Critical DoD need: work with commercial sUAS industry to develop adaptable, low-cost platforms with low supply chain risk

### BST Competitive Advantages for This Requirement
1. **Vertically Integrated Design & Manufacturing:** All aircraft, avionics, FMS, ground stations, and support equipment designed and maintained by BST in-house; entire supply chain managed by USA-based company
2. **Only U.S. Group 1 UAS Manufacturer** with in-house flight management system AND aircraft design capability
3. **Modular, Distributed Avionics Architecture:** Unlike competitors relying on centralized autopilots with limited computing, SwiftCore uses intelligent nodes and message-based bus enabling:
   - Simplified third-party component integration
   - Advanced subsystem lifecycle tracking
   - Preventative maintenance capabilities
   - Safety redundancy
4. **Data-Centric Flight Control:** Payload-focused system with real-time telemetry and autonomous flight path adaptation
5. **Field-Swappable Modular Payload System:** Common power, data, mechanical interfaces; no specialized tools required
6. **Proven in Extreme Conditions:** Track record with USAF, NOAA, NASA, USGS, leading research institutions
7. **Supply Chain Resilience:** Successfully navigated recent electronic parts shortages through design flexibility and relationships with regional board houses

## Notable Details

### Company Profile
- **Founded:** 2011, Boulder, Colorado
- **Facility:** 3,000 sq. ft. in Boulder with prototyping, simulation, testing, manufacturing, and meeting space
- **Testing Infrastructure:**
  - Sod farm 20 minutes east (office)
  - Pawnee National Grasslands test area (20×20 miles with 1,000 ft waiver)
  - San Luis Valley high-altitude testing (up to ~15,000 ft MSL)
  - Established relationship with Alaska DOT for BVLOS missions via UAS Activity Areas

### Relevant Prior Work
**Completed Phase II SBIRs:**
- NASA: Machine vision automated safe landing system for distressed UAS
- NASA: AI-enabled predictive and preventive maintenance system for UAS (extended via AFWERX 20.3)
- NASA: Soil moisture management system with L-band radiometer

**Active/Current Projects:**
- AFWERX 20.3 Phase I: AI/ML algorithms for predictive maintenance
- NOAA Phase II: Small, low-cost air-deployed UAS for hurricane boundary layer observations (SwiftFlow 3D Wind Probe)
- NASA Phase II: Venus upper-atmosphere sampling vehicle with dynamic soaring capability
- NOAA Phase II: AI-enabled GPS-denied navigation for coastal BVLOS mapping
- Alerion (Spain): Wind turbine inspection multirotor with LiDAR/RGB cameras
- Commercial 5G signal mapping project

**Transition Success:**
- 18 successful SBIR projects transitioned to Phase III and commercial opportunities
- Recent Phase III NASA contract for volcano monitoring, soil moisture mapping, CO2 detection
- Two active NOAA contracts (tube-launched air-deployed UAS, mountainous soil moisture)
- USGS use of soil moisture payload for wildfire mitigation

### Technical Strengths Emphasized
- PI (Dr. Jack S. Elston) is CEO with Ph.D. focused on UAS control algorithms for extreme conditions; designed Tempest UAS for first-ever tornadic supercell intercept (VORTEX2 project)
- Led development of SwiftCore autopilot anchoring FMS
- Published 100+ COA applications; conducted hundreds of field experiments including Arctic deployments
- Co-authored numerous peer-reviewed publications and conference papers on UAS topics
- Demonstrated expertise integrating diverse payloads (multispectral/RGB cameras, LiDAR, EO/IR, trace gas sensors, nephelometer, temperature/pressure/humidity/wind sensors, L-band radiometer)

### Manufacturing & Supply Chain
- **In-House:** All electronics (autopilot, power boards, GNSS), software, firmware, mechanical design
- **Outsourced:** Composite airframe work (Northwind Composites), circuit board manufacturing (Denver-area board houses)
- **Supply Chain Resilience:** Maintained production through recent electronic parts shortages via design flexibility and local supply relationships