# Low-Cost Air Deployed sUAS Enabling Advanced Cooperative Control

## Document Metadata
- **Type:** SBIR Phase II Direct-to-Phase II Proposal (Volume II – Technical Volume)
- **Client/Agency:** U.S. Air Force Research Laboratory (AFRL); Defense/Air Force stakeholders
- **Program/Solicitation:** Topic Number AFX234-DCSO2 (Direct-to-Phase II Call for Innovative Defense-Related Dual-Purpose Technologies/Solutions with Clear Air Force Stakeholder Need)
- **Proposal Number:** F2D-7891
- **Date:** Submitted November 18, 2022
- **CAGE Code:** 6PGF9
- **BST Products/Systems Referenced:** S0 (air-deployed sUAS), S0-AD (air-deployed variant), S0 VTOL (ground-launch variant), S0 Mk2 (proposed USAF variant), SwiftCore (avionics system), E2 UAS, S2 UAS
- **Key Personnel Named:** 
  - Dr. Jack Elston (Founder, CEO, Principal Investigator)
  - Dr. Maciej Stachura (Founder, CTO, Lead Engineer)
  - Ed Kase (EKase Consulting LLC – Business Development, 20+ years experience, 12+ years SBIR commercialization)

## Executive Summary
Black Swift Technologies proposes to develop an enhanced air-deployed small unmanned aircraft system (S0 Mk2) specifically tailored for U.S. Air Force Research Laboratory (AFRL) requirements, enabling advanced cooperative control and swarming operations. Building on the commercially successful S0 platform developed for NOAA hurricane monitoring, the Phase II effort will introduce video payload capabilities, open modular interfaces, and cooperative control algorithms while maintaining the cost advantage (5x-10x cheaper than competitors like Raytheon Coyote and Area-I Altius) and enabling deployment of large UAS teams from C-130 aircraft. The system directly addresses Air Force strategic needs for low-cost, autonomous swarming platforms and supply chain resilience while leveraging BST's 11 years of proven expertise in scientific UAS operations in extreme environments.

## Technical Approach

### Core Development Strategy
BST proposes a four-pronged technical approach centered on adapting the proven commercial S0 platform:

1. **Airframe Modification for USAF Air Deployment**
   - Increase size/weight to extend mission endurance beyond 90 minutes
   - Optimize design for C-130 air-launch operations
   - Potentially incorporate folding wing mechanism for deployment efficiency
   - Target cost: Under $5,000 per aircraft; 90-120 minute mission time (with options for 4-hour variants)

2. **Integrated Sensor/Payload Suite**
   - Add electro-optical (EO) and infrared (IR) video transmission capabilities with real-time relay to deploying aircraft
   - Maintain highly accurate meteorological data collection (pressure, humidity, 3D winds, temperature)
   - Enable multi-mission functionality (ISR + atmospheric science)

3. **SwiftCore Avionics Architecture Adaptation**
   - Implement open modular interface enabling third-party algorithm integration
   - Distribute computing tasks across intelligent nodes via high-level message-based bus (vs. centralized autopilot approach)
   - Simplify integration for hardware/software-in-the-loop simulation and cooperative control algorithm development
   - Maintain subsystem lifecycle tracking, preventative maintenance, and redundancy capabilities

4. **Cooperative Control Software Interfaces**
   - Develop API/SDK interfaces compatible with AFRL's existing Skyborg and Golden Horde programs
   - Create mapping layer between current BST communications protocol and DoD systems
   - Support hierarchical control reducing operator overhead for multi-UAS operations
   - Implement software-in-the-loop (SITL) simulation capability for AFRL researchers

### Manufacturing & Supply Chain Approach
- All major components (avionics, software, radios, ground systems) designed and manufactured in the U.S.
- Design optimized for scalable domestic production from 10s to 100s per month
- Emphasis on resilient, non-Chinese supply chains to address DoD FY20 Industrial Capabilities concerns
- Maintained compatibility with commercial variants to sustain production economics

## Products & Capabilities Described

### S0 / S0-AD (Air-Deployed sUAS) – Base Commercial Platform
**What it is:** 
- Lightweight (3 lbs), fixed-wing unmanned aircraft system originally developed for NOAA's P-3 Orion "Hurricane Hunter" aircraft
- Designed for autonomous flight in extreme atmospheric conditions (hurricane force winds, heavy precipitation)
- Proven operational capability since 2022 with NOAA deployments

**Specifications & Performance:**
- Cost: $5,000 per aircraft (target maintained in USAF variant)
- Endurance: 90+ minutes (extended versions capable of 4 hours)
- Payload capacity: Meteorological instruments (pressure, humidity, 3D wind, temperature sensors) + video systems
- Operational ceiling: Can operate as low as 100 feet AGL (demonstrated in hurricane eyewalls)
- Speed: Dash capability exceeding 100 mph with reduced audio signature vs. multirotor platforms
- Communications: Open modular interfaces; commercial radios with encryption capability; proposed DoD network certification

**How proposed for USAF use:**
- Modified design designated S0 Mk2 to support USAF-specific requirements for video ISR, cooperative control, and air deployment from C-130
- Enhanced communications system for DoD integration
- Integration with Skyborg, Golden Horde, ALOBO, and Vigilant Spirit Ground Control Station architectures

**Demonstrated Commercial Success:**
- Sold to NOAA (initial 2 VTOL units + contract for 14 additional S0-AD aircraft for hurricane research)
- NOAA contract value: ~$500K (hardware + support) for initial order; ongoing operations
- Embry Riddle University orders received
- Interest from TruWeather and other hyperlocal weather providers

### S0 VTOL – Ground-Launch Variant
**What it is:** 
Modified S0 variant with vertical takeoff/landing capability for ground operations

**Specifications:**
- Speed: >100 mph dash capability
- Reduced acoustic signature vs. multirotor alternatives
- Atmospheric profiling + ISR platform capability
- Designed for landfalling hurricane monitoring

**Commercial Status:**
- 2 units sold/under contract to NOAA (~$30K with support)
- Interest from Embry Riddle and other universities

### SwiftCore Avionics System
**What it is:** 
Proprietary distributed autopilot architecture developed exclusively by BST aerospace engineers

**Key Features:**
- Intelligent distributed nodes connected via high-level message-based bus (vs. centralized autopilot)
- Modular design enabling third-party component integration
- Well-defined open interfaces for ecosystem development
- Subsystem lifecycle tracking and preventative maintenance capabilities
- Built-in redundancy for safety-critical functions
- Proven across multiple aircraft platforms and atmospheric science missions

**Advantages Over Competitors:**
- Designed by and for UAS experts
- Compatible with open-source integration without exposing critical code to adversaries
- Foundation for advanced capabilities (subsystem health monitoring, autonomous adaptive control)

**USAF Application:**
- Will be enhanced with API/SDK for Skyborg, Golden Horde, and ALOBO algorithm integration
- Enable simplified development environment for cooperative control research

### S2 UAS
**What it is:** Larger BST platform used for extended-duration atmospheric research

**Applications mentioned:** High-altitude research (NASA Greenland studies at 14,000 ft), coastline monitoring, trace gas detection

## Use Cases & Applications

### Primary USAF/Defense Applications

**1. Swarm/Cooperative Operations (Skyborg, Golden Horde Programs)**
- Enable deployment of large numbers of S0 Mk2 from single C-130 sortie
- Support autonomous teaming architectures
- Reduce operator workload through hierarchical control algorithms
- Provide 5x-10x coverage improvement without increase in operator burden
- Enable "complexity, unpredictability, and mass" strategy per USAF S&T Strategy

**2. Air-Launched ISR Missions (ALOBO Architecture)**
- Real-time EO/IR video relay from deployed platforms to host aircraft
- Multi-hour persistent surveillance from sequential UAS deployments
- Low-cost, expendable platforms enabling liberal employment in contested environments

**3. Special Operations and Tactical Applications**
- Support SOCOM PEO Fixed Wing requirements
- AFSOC/A5 ISR and Strike missions
- Medium Altitude, Long-Endurance Tactical (MALET) program coordination
- Reduced detectability vs. larger platforms (low acoustic signature)

**4. Research & Development Platform**
- Hardware-in-the-loop and software-in-the-loop simulation for AFRL algorithm development
- Testbed for advanced autonomy, swarming, and hierarchical control research
- Modular architecture enabling rapid capability upgrades

### Non-Defense Commercial Applications

**1. Hurricane Monitoring & Atmospheric Science (NOAA)**
- In-situ measurements of atmospheric boundary layer conditions during hurricane eyewall penetration
- Real-time video observations of hurricane internal structure (novel capability)
- Hyper-local meteorological gradient mapping through multi-platform deployment
- Current active contract: 14 S0-AD aircraft for next two hurricane seasons
- Potential for expanded orders (currently ~10 per year baseline, expected to increase with swarming capability)

**2. Hyperlocal Weather Prediction (Commercial)**
- Data provision to weather services (TruWeather, etc.)
- Precision agriculture applications requiring localized weather data
- Market: Global weather instruments valued at $322.86M (2018), projected $496.78M by 2025 (6.33% CAGR)

**3. Volcano Monitoring & Volcanic Plume Observation**
- Deployment of multiple S0 variants to measure gas concentrations, plume dynamics
- USGS partnership for volcano monitoring

**4. Wildfire Research & Monitoring**
- Nighttime measurements of wildfire plume properties
- Remote sensing of fire characteristics
- USGS wildfire mitigation support via soil moisture payloads

**5. Precision Agriculture & Environmental Monitoring**
- Soil moisture mapping via specialized payloads
- Coastal monitoring using thermal and hyperspectral sensors
- Satellite calibration support (Landsat-8, S-NPP VIIRS validation)

## Key Results (Phase I Feasibility Study & Commercial Validation)

### Phase I Activities Completed
**Stakeholder Engagement:**
- 63 total federal government contact attempts
- 30 successful email contacts, 6 successful phone contacts, 1 in-person meeting
- 8 unique federal government organizations reached (36 unique USAF organizations contacted)
- Identified empowered end-users: Dr. David Grymin (AFRL/RQQA), Dr. Paul Fleitz (AFRL/RQQC)

**Requirements & Use Cases Derived:**
- AFRL/RQQA air deployment requirements for swarming research
- Integration needs with existing Skyborg, Golden Horde, ALOBO architectures
- DoD communication and cybersecurity integration requirements
- Open interface specifications for cooperative control algorithm development

**Commercial Validation:**
- NOAA contract for 14 S0-AD aircraft (~$500K hardware + support)
- Interest from Embry Riddle, TruWeather, and other commercial partners
- Demonstrated market demand for atmospheric science platform exceeding current commercial offerings

### Phase II Deliverables (Planned)

**Milestone 1 (Month 1):** Requirements specification and interface definition document
- Customer acceptance criteria: DAF end-users confirm specifications meet needs

**Milestone 2 (Month 6):** Functional prototype with air launch components
- Acceptance: Flight data demonstrating requirements compliance

**Milestone 3 (Month 8):** Communications system meeting DoD criteria
- Acceptance: Validated range, bandwidth, reliability through ground testing

**Milestone 4 (Month 10):** DAF mission-specific API/SDK and UI
- Acceptance: Software-in-the-loop simulation demonstration

**Milestone 5 (Month 12):** Final technical report
- Acceptance: DAF technical monitor endorsement

**Milestone 6 (Month 13):** Delivery of 3 S0 Mk2 systems with AF customizations
- Acceptance: Physical delivery and DAF end-user acceptance

**Milestone 7 (Month 15):** Flight test support and validation
- Acceptance: Test report endorsed by DAF end-user