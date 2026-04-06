# DOD Distributed Avionics Architecture SBIR Phase I Proposal

## Document Metadata
- Type: SBIR Phase I Proposal (Presentation Deck)
- Client/Agency: U.S. Air Force / Department of Defense
- Program/Solicitation: SBIR (specific topic not explicitly stated, but focused on modular UAS avionics)
- Date: June 2021 (created 2021-06-13, modified 2021-06-18)
- BST Products/Systems Referenced: SwiftCore FMS, S2 (fixed-wing UAS), E2 (multi-rotor UAS)
- Key Personnel: Jack S. Elston (PhD, PI, CEO), Maciej Stachura (PhD, CTO, UAS Control System Expert), Bill Nickerson, Cory Dixon, Brian Argrow, Eric Frew

## Executive Summary
Black Swift Technologies proposes to develop a service-oriented, distributed avionics architecture for DoD UAS that enables plug-and-play (PnP) modularity, allowing components from multiple vendors to be swapped, upgraded, and tested independently. Phase I will involve customer discovery with Air Force stakeholders (AFRL, Travis AFB) to validate technical approach and refine requirements for redundancy-enabled, open-protocol hardware that serves as an alternative to legacy centralized systems like Piccolo and Dronecode-based solutions.

## Technical Approach

**Core Architecture Concept:**
- Service-oriented architecture (SOA) applied to UAS avionics with automatic service discovery
- Distributed hardware and software replacing traditional centralized flight control systems
- Built upon proven BST SwiftCore FMS platform to reduce programmatic risk
- Open protocol and hardware standards enabling third-party component development

**Key Capabilities Enabled:**
- **Service Discovery**: New modules added/removed dynamically; system auto-detects current capability set
- **Component Testing**: Per-component reliability and performance requirements with easy verification
- **Safety/Redundancy**: True redundancy through service discovery and type-based bus messaging
- **Interoperability**: Open standards allow components from different manufacturers to work together

**Technical Modifications Planned:**
1. Updated bus protocol designed specifically for service-oriented architecture
2. Additional hardware components based on proven BST node design for distributed sensors and control
3. Algorithms specific to distributed architectures (e.g., intelligent redundant subsystem enablement)

**Hardware/Software Elements:**
- S2 fixed-wing UAS avionics configuration using SwiftCore FMS
- E2 multi-rotor UAS avionics configuration using SwiftCore FMS
- UAVCAN-compatible protocols (or similar open standard)
- Support for integration with third-party systems (Piccolo, Dronecode)

## Products & Capabilities Described

### SwiftCore FMS (Flight Management System)
- **What it is**: BST's modular flight management solution currently employed on UAS worldwide
- **Current use**: Core avionics platform for S2 and E2 aircraft
- **Proposed enhancement**: Expansion to support service-oriented architecture with open protocols and distributed node capabilities
- **Advantage**: Reduces technology risk by building on proven foundation

### S2 Aircraft
- **What it is**: Fixed-wing UAS platform developed through NASA SBIR soil moisture mapping project
- **Current achievements**: Selected for NASA Goddard MALIBU project; chosen by NASA JPL for Costa Rica trace gas sensing operations
- **Status**: Commercially successful with non-NASA investment of $417,157; growing user base at NASA, NOAA, USGS

### E2 Aircraft
- **What it is**: Multi-rotor UAS platform
- **Commercial use**: Deployed by Alerion Technologies for wind turbine inspections
- **Proposed benefit**: Will receive modular avionics improvements

### Proposed Modular Components (PnP Modules)
- **Electronic Speed Controllers (ESCs)**: Service-oriented intelligent ESCs with advanced diagnostics (identified as high-value scalable product; currently no reliable, affordable U.S.-made alternatives)
- **GPS/GNSS modules**: Modified with modular capability
- **Servo controllers**: Plug-and-play versions
- **Battery monitoring modules**: Enhanced modular versions
- **Sensor interface boards**: For payload sensors (SAR, LWIR hyperspectral cameras, etc.)
- **GPS-denied navigation nodes**: Specialized capability module
- **Machine learning-based preventative maintenance nodes**: AI fault detection capability

## Use Cases & Applications

### Primary DoD Use Cases
- **Fleet management simplification**: Easy component replacement and updates across USAF UAS fleets without aircraft-level system replacement
- **Travis AFB security operations**: Drop-in replacement for commercial UAS solutions struggling with high-wind environments
- **Component standardization**: Support for fixed-wing, VTOL, multi-rotor, and helicopter UAS currently using diverse autopilot systems (Piccolo, Dronecode)

### Secondary Applications (NASA/NOAA/Federal Government)
- Advanced sensor integration (SAR, LWIR hyperspectral, trace gas detectors)
- GPS-denied environments and low-altitude flight navigation using machine vision
- Terrain-aware navigation
- Soil moisture mapping and radiometry
- Atmospheric profiling
- Scientific field campaigns (extreme weather, volcanoes, wildfires, arctic operations)

### Commercial Applications
- Wind turbine inspections (via Alerion Technologies)
- General UAS payload upgrades and expansion

## Phase I Objectives & Timeline

| Objective | Success Metric | Timeline |
|-----------|----------------|----------|
| Meet with USAF UAS operators on pain points for component replacement | Meeting notes with identified stakeholders (David Grymin-AFRL, Kenny Perkins-Travis AFB) | Award + 1 week |
| Communicate plan for advanced modular onboard system | Engagement confirmation with David Grymin and Kenny Perkins | Award + 1 month |
| Create plan for modifications to existing technology for legacy system integration | Agreement from USAF users on plan feasibility | Award + 2 months |
| Identify quantitative metrics for Phase II (downtime, repair time, TCO, etc.) | Full team buy-in on metrics, acceptable values, computation methods | Award + 2.5 months |
| Create necessary reports | Reports accepted by technical POC and identified customers | Award + 3 months |

## Work Plan / Statement of Work (Phase I)

**Duration**: 90 days

| Task | Duration | Description | Performer |
|------|----------|-------------|-----------|
| 01 - Preliminary Report (DELIVERABLE) | Days 0-5 | 15-slide research plan document | Jack Elston |
| 02 - USAF Customer Discovery & Problem Refinement | Days 0-60 | Discussions with active UAS users (AFRL, Travis AFB) to identify specific modular system needs and replaceable component requirements | Bill Nickerson, Jack Elston |
| 03 - Technical Adaptation & Modification Study | Days 40-80 | Design adaptation to fit USAF customer needs while maintaining commercial viability | Jack Elston, Maciej Stachura |
| 04 - Definition of Solution Trial with AF End-User | Days 50-90 | Define specific technology trial for Phase II testing by active small UAS operators | Jack Elston, Bill Nickerson |
| 05 - Final Report (DELIVERABLE) | Days 60-90 | 15-page report + 15-slide presentation incorporating all Phase I findings | Jack Elston, Bill Nickerson |

**Deliverables**: 
- Preliminary Report (15 slides)
- Final Report (15 pages + 15 slides)
- Assessment of proposed technologies and USAF capability enhancements
- Phase II flight trial definition

## Key Results & Strategic Value

### Technical Merit
- Addresses fundamental limitation of current DoD UAS avionics (legacy Piccolo systems lack expandability; Dronecode solutions are hobby-grade with limited flexibility)
- Aligns with AFWERX focus areas: Dynamic Data-Driven Prognostics, Intelligent Flight Control with Flight Safety Emphasis, Service-Oriented Modular Flight/Propulsion Control with PnP functionality
- Supports concurrent funded work: NOAA GPS-denied sensor suite, USAF atmospheric profiling aircraft, AFWERX preventative maintenance solution

### Problem/Opportunity
- DoD installed base uses diverse autopilots lacking common modular architecture
- Future capability requirements (advanced SAR/LWIR sensors, onboard HPEC for AI) difficult to integrate into current systems
- No existing avionics solution (other than BST SwiftCore) employs true distributed architecture supporting service-oriented approach
- Current solutions enable only centralized, monolithic replacement rather than modular upgrades

### Competitive Advantage
- Only BST SwiftCore currently offers truly distributed architecture supporting automated service discovery
- 10 years of BST experience developing modular avionics hardware, software, firmware
- Proven commercialization track record (self-funded since 2011; successful NASA SBIR projects with subsequent private investment)
- U.S.-based manufacturing (all electronics produced in USA vs. Chinese alternatives)

## Key Personnel & Expertise

### Jack S. Elston, PhD (Principal Investigator, CEO)
- PhD research: Complex meshed networks, UAS, control algorithms for severe convective storm sampling
- Experience: Seven continents, Arctic operations, volcano-side flights, wildfire monitoring
- Expertise: Extreme environment UAS operations, tube-launched UAS (hurricane observations), machine vision, GPS-denied navigation, advanced UAS projects (Venus glider exploration)
- Publications: Handbook chapter on networked command/control (2013); Journal of Intelligent and Robotic Systems (2009)

### Maciej Stachura, PhD (CTO, UAS Control System Expert)
- Education: M.S. and Ph.D. in Aerospace Engineering, University of Colorado Boulder
- Research: 300+ flight experiments including multi-aircraft cooperative flight, VORTEX2 tornadic supercell intercept
- Experience: PI on NASA advanced UAS projects (soil moisture radiometer for sUAS, terrain-aware low-altitude machine vision navigation, AI-based onboard fault detection)
- Publications: Journal of Field Robotics (2017); IEEE IGARSS (2016) on L-band soil moisture mapping

### Support Team
- Bill Nickerson: Customer discovery and engagement
- Brian Argrow, Eric Frew, Cory Dixon: Referenced as contributors to foundational networked UAS work

## Commercialization Strategy

### Market Opportunity
- UAS spending projected at $11.4B (2022), growing to $45.8B (2025) per Teal Group
- Global UAS market estimated $19.3B (2019), projected $45.8B (2025) at 15.5% CAGR
- Commercial UAS market shows 35% moving toward open architecture (strong fit for this solution)
- Mission-critical components with poor quality (e.g., ESCs) represent high-demand replacement market

### Revenue Models
1. **Sale of PnP modules** for UAS operators:
   - BST-designed hardware (GNSS, servo controllers, battery monitoring—modified with modular capability)
   - New intelligent ESCs with service-oriented architecture and advanced diagnostics
   - Interface boards for growing sensor payload ecosystem

2. **SDK and Protocol Publishing**:
   - Open protocol and example code published to encourage third-party hardware development
   - Enables BST modules in third-party systems
   - Creates UAS component marketplace

3. **Aircraft Platform Sales**:
   - Existing S2/E2 aircraft line benefits directly from developments
   - Enables additional government and commercial sales

### Customer Base & Relationships
**DoD/Federal**:
- AFRL/RQ, Travis AFB (60th SFS), Edwards AFB (412th Test Wing) with associated Small Business Offices
- Existing relationships from prior SBIR successes

**Federal Civilian**:
- NASA, NOAA, USGS, DOE (existing user base for BST solutions)
- Benefit from fleet modernization without full platform replacement

**Commercial**:
- Alerion Technologies (E2 wind turbine inspection platform)
- Growing commercial demand for non-Chinese, reliable PnP components

### Transition Strategy
**Phase I** identifies two anchor customers:
1. **AFRL**: Facilitate introduction of BST modular system into current fleet; test compatibility with third-party systems
2. **Travis AFB**: Drop-in replacement solution for commercial UAS with high-wind performance issues; planned collaboration with existing commercial provider

### Funding & Capitalization
- BST entirely self-funded since 2011 (commercial sales, consulting, development contracts, non-dilutive grants)
- Prior commercialization success: $417,157 non-NASA investment secured for soil moisture mapping UAS