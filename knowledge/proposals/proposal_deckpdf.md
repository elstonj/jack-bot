# Common Hardware Architecture for UAS - Distributed Avionics Proposal

## Document Metadata
- **Type:** SBIR Proposal (Phase I)
- **Client/Agency:** United States Air Force (Department of the Air Force)
- **Program/Solicitation:** AFWERX focus areas (specific SBIR topic/solicitation number not explicitly stated)
- **Date:** June 17, 2021
- **BST Products/Systems Referenced:** SwiftCore FMS, S2 (fixed-wing UAS), E2 (multi-rotor UAS)
- **Key Personnel:** 
  - Jack S. Elston, PhD (Principal Investigator, CEO)
  - Maciej Stachura, PhD (CTO, UAS Control System Expert)
  - Bill Nickerson
  - Cory Dixon
  - Brian Argrow
  - Eric Frew

## Executive Summary
Black Swift Technologies proposes to develop a service-oriented, distributed avionics architecture for DoD UAS that enables plug-and-play component replacement and interoperability across multiple platforms. Building on the proven SwiftCore FMS foundation, Phase I will focus on customer discovery with USAF operators (AFRL and Travis AFB) to define technical requirements and develop a transition plan for Phase II implementation and flight testing.

## Technical Approach

**Core Innovation:** Transform BST's existing modular flight management solution into a distributed, service-oriented architecture that enables:
- **Service Discovery** – modules automatically added/removed with system awareness of current capabilities
- **Component Testing** – reliability/performance requirements tested and verified at component level
- **Safety** – true redundancy through service discovery and type-based bus messaging
- **Interoperability** – open standards allow components from different manufacturers to work together

**Technology Foundation:**
- Base technology: SwiftCore FMS (already deployed in UAS globally)
- Updated bus protocol designed specifically for service-oriented architecture
- Additional hardware components based on proven BST node design for distributed sensors and control
- New algorithms for distributed architectures (e.g., intelligent redundant subsystem enablement)

**Phase I Work Plan (90 days):**
1. **Preliminary Report** (Days 0-5) – 15-slide research plan
2. **Customer Discovery** (Days 0-60) – Discussions with USAF operators (AFRL, Travis AFB) to identify specific modular system needs
3. **Technical Adaptation Study** (Days 40-80) – Design technology to fit USAF needs while maintaining commercial viability
4. **Definition of Phase II Trial** (Days 50-90) – Work with identified end-users to define specific technology demonstration
5. **Final Report** (Days 60-90) – 15-page report + 15-slide presentation

## Products & Capabilities Described

### SwiftCore FMS
- **What it is:** Flight Management System that serves as the kernel for the proposed distributed avionics architecture
- **Current use:** Already employed in S2 and E2 UAS platforms; deployed for UAS applications globally
- **Proposed enhancement:** Expansion to support service-oriented architecture with open protocols

### S2 (Fixed-Wing UAS)
- **Current use:** Avionics platform running SwiftCore FMS
- **Commercial success:** Selected for NASA Goddard Space Flight Center MALIBU project; chosen by NASA JPL for Costa Rica trace gas sensing operations
- **Proposed role:** Platform for Phase II demonstrations of modular avionics capabilities

### E2 (Multi-Rotor UAS)
- **What it is:** Multi-rotor platform with SwiftCore FMS
- **Commercial use:** Operated by commercial partner Alerion Technologies for wind turbine inspections
- **Proposed role:** Demonstration platform for plug-and-play capabilities

### Hardware Modules (Proposed/Existing)
- Electronic Speed Controllers (ESCs) – intelligent, service-oriented versions
- GNSS modules
- Servo controllers
- Battery monitoring modules
- Payload sensor interface boards
- Motor controllers

## Use Cases & Applications

**Primary Defense Application:**
- USAF UAS fleet modernization with modular plug-and-play components for easier maintenance and upgrades
- Enabling advanced sensor integration (SAR, LWIR hyperspectral cameras) and onboard HPEC for edge AI
- Addressing pain points: component replacement, fleet standardization, supply chain resilience

**Identified USAF Stakeholders:**
- David Grymin (AFRL)
- Kenny Perkins (Travis AFB, 60th SFS)
- 412th Test Wing (Edwards AFB)

**Commercial/Civilian Federal Applications:**
- NASA missions (soil moisture mapping, atmospheric profiling)
- NOAA operations
- USGS projects
- Commercial drone operations (wind turbine inspection, surveying)

**AFWERX Focus Areas Addressed:**
- Dynamic Data-Driven Prognostics and Condition Monitoring System for Aircraft Systems
- Intelligent Flight Control Architectures with Emphasis on Flight Safety
- Service-Oriented Modular Flight/Propulsion Control Systems with Plug-and-Play Functionality

**Related Ongoing Work to Benefit:**
- NOAA-funded GPS-denied sensor suite
- USAF-funded atmospheric profiling aircraft
- AFWERX-funded preventative maintenance solution

## Key Results
*Phase I is a proposal; no results yet.* Success metrics defined for Phase I customer discovery:
- Meeting notes with identified USAF stakeholders (Award + 1 week)
- Engagement plan with David Grymin and Kenny Perkins (Award + 1 month)
- Feasibility plan for modular hardware integration into legacy systems like Piccolo and Dronecode (Award + 2 months)
- Identified quantitative metrics (platform downtime, repair time, total cost of ownership) (Award + 2.5 months)
- Accepted final report with findings (Award + 3 months)

## Notable Details

**BST Track Record:**
- Founded 2011; entirely self-funded through commercial sales, consulting, and non-dilutive grants
- Soil moisture mapping UAS project in NASA SBIR commercialization phase; earned $417,157 in non-NASA investment
- S2 platform rapidly becoming preferred choice for NASA, NOAA, USGS scientific campaigns
- Successfully transitioned multiple SBIR technologies to commercial products

**Team Expertise:**
- Jack Elston: PhD in complex networked UAS, experience in extreme environments (arctic, volcanoes, hurricanes, severe storms); published author
- Maciej Stachura: PhD Aerospace Engineering; involved in 300+ flight experiments including VORTEX2 tornado intercept; PI on NASA UAS projects (soil moisture radiometer, terrain-aware navigation, AI fault detection)
- Canadian citizen (Stachura) working under TN visa

**Transition Strategy:**
- Two identified customers ready for Phase II: AFRL (extensive UAS fleet for evaluation) and Travis AFB (commercial UAS replacement for high-wind security operations)
- Existing relationships at AFRL/RQ, Travis AFB (60th SFS), Edwards AFB (412th Test Wing)
- Commercial partnerships: discussions with Alerion Technologies (E2 operator)
- Post-Phase II plan: significant improvement to USAF UAS reliability, expanded vendor network for components, lower maintenance overhead

**Commercialization Strategy:**
- DoD market: $11.4B UAS spending projected for 2022; growing to $45.8B by 2025
- Commercial market: UAS market USD 19.3B (2019) → USD 45.8B (2025) at 15.5% CAGR
- 35% of commercial UAS moving toward open architecture (potential customers)
- Initial focus: mission-critical components with reliability issues (ESCs)
- Revenue model: 
  - Sale of plug-and-play modules (GNSS, servo controllers, battery monitoring, new intelligent ESCs)
  - Payload sensor interface boards
  - **Key differentiator:** All electronics manufactured in USA (not China)
- Planned equity capital raise to support commercialization
- Target markets: DoD, federal agencies (NASA, NOAA, DOE), commercial operators

**Competitive Advantages:**
- Only current solution with truly distributed, service-oriented avionics architecture
- Existing alternatives (Piccolo: dated, monolithic; Dronecode: open-source hobby-grade, limited flexibility)
- UAVCAN protocol exists but lacks hardware support and decentralized approach
- BST's distributed approach enables redundancy, future expansion, and automated service discovery

**Facilities:**
- 3,000 sq ft facility in Boulder, Colorado (2840 Wilderness Place Suite D)
- US-based manufacturing partners for electronic and mechanical components
- Required hardware, software, and computing resources for Phase II development

**Regulatory/Administrative:**
- DUNS: 078359543
- CAGE Code: 6PGF9
- SBA SBC ID: SBC_000404583
- Foreign national disclosure: Maciej Stachura (Canada, TN visa) involved in Task 03

**Dual-Use Potential:**
- Open protocol to be published with example code and SDK
- Encourages third-party hardware component development
- Specialized payloads: GPS-denied navigation, machine learning-based preventative maintenance, soil moisture measurement, trace gas detection
- Vision: UAS component marketplace