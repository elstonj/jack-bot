# A121-036-0211 Technical Proposal: Multi-Vehicle Operational Control Unit (OCU)

## Document Metadata
- **Type:** SBIR Phase I Technical Proposal
- **Client/Agency:** U.S. Army
- **Program/Solicitation:** Topic Number A121-036
- **Date:** Submitted December 29, 2011 (modified through June 10, 2013)
- **BST Products/Systems Referenced:** NetUAS software suite, custom low-cost autopilot system, small electric aircraft platform (Tempest)
- **Key Personnel:** 
  - Jack S. Elston (Principal Investigator, CTO and co-founder)
  - Cory R. Dixon (Software Engineer)
  - Maciej Stachura (Engineer, F-1 Ph.D. student from Canada)

## Executive Summary
Black Swift proposes to develop an innovative Operational Control Unit (OCU) architecture that enables a single operator to effectively monitor and command multiple semi-autonomous to fully autonomous unmanned vehicles at scales from small team to battalion level. The system will employ automated data filtering, context-aware display algorithms, and modern tablet/surface-based user interfaces to present vehicle status, sensor data, and uncertainty information without overwhelming the operator. Phase I deliverables include a detailed design specification, visualization mock-ups, algorithms, evaluation criteria, and an implementation plan for Phase II prototype development.

## Technical Approach

### Core Design Philosophy
The OCU is designed using a **spiral development methodology** with iterative assessment to ensure continuous alignment with customer specifications and state-of-the-art in tablet and surface computing interfaces.

### Key Technical Components

**1. Automated Data Display and Filtering**
- Context-sensitive state machine to recognize operational situations and automatically adjust displayed data
- Data hierarchy development tied to specific situations and operator needs
- Intelligent filtering mechanisms to reduce information overload while ensuring critical data is never missed
- Separate algorithms for vehicle/small unit level (tablet-based) and battalion level (surface-based) displays

**2. Uncertainty Representation**
- Multi-source uncertainty display including:
  - Vehicle state uncertainty
  - Environmental state uncertainty from noisy sensors
  - Task completion uncertainty
- Methods to present uncertainty visually without overwhelming operators
- Algorithms to determine when uncertainty information should be prominently displayed vs. available on demand

**3. Situational Awareness (SA) Reconciliation**
- Two-way SA mechanisms allowing operators to correct or reconcile vehicle team awareness
- Communication protocols for quick and effective consensus on SA issues
- Design ensures multi-user distributed control with shared situational picture

**4. User Interaction Methods**
- **Tablet-based interfaces** for small unit/vehicle-level control with touch interaction optimized for field conditions
- **Surface-based computing** for battalion-level command and control with multi-user interaction
- Universal interaction methods prioritized; device-specific advanced features identified as secondary
- Integration pathway with existing OCU systems (Cloudcap Technologies interfaces)

**5. System Integration Standards**
- Compliance with Joint Architecture for Unmanned Systems (JAUS) standards
- Interface definition for TIGR system (proprietary Army intelligence database)
- Backward compatibility with existing ground-based systems and UAS communications methods

## Products & Capabilities Described

### NetUAS Software Suite
- **What it is:** Service discovery and publish/subscribe architecture for unmanned systems enabling multi-vehicle operations without scripting
- **Previous deployment:** Successfully demonstrated on VORTEX2 supercell thunderstorm sampling campaign with 4 networked vehicles (Tempest aircraft, mobile ground control station, tracker vehicle, Mobile Mesonet scout vehicle)
- **Key advantage:** Designed from ground-up for multi-vehicle control; allows dynamic service discovery; supports graphical and text-based data display formats
- **Differentiator vs. competitors:** Cloudcap operator interface only displays vehicle telemetry (no payload data), treats all vehicles identically, typically controls one vehicle at a time; NetUAS designed for multiple heterogeneous systems with user-selectable data streams

### Black Swift Small UAS Platform (Tempest)
- **What it is:** Low-cost, small electric aircraft with custom-built autopilot designed in collaboration with RECUV (University of Colorado)
- **Modifiable payload options:** Still camera, infrared (IR), or video camera
- **Use in proposal:** Prototype vehicle for OCU testing and demonstration; integrated with networking and cooperative control capabilities
- **Additional capabilities:** Collision avoidance, meshed networking, distributed optimization for cooperative control

### Proposed OCU Architecture
- **Platform flexibility:** Works across COTS tablet devices, multi-user surface computing platforms, and existing ground stations
- **Scalability:** Designed for small team operations up to battalion-level (40+ vehicles implied)
- **Data handling:** Dynamic, modular approach allows inclusion of new vehicle types and sensor subsystems without redesign

## Use Cases & Applications

### Military Operations
- **Multi-vehicle team command and control** at small unit through battalion levels
- **Distributed operator control** with remote observers and multiple command centers
- **Complex heterogeneous team operations** combining aerial and ground-based vehicles
- **Real-time data aggregation** from multiple vehicle subsystems and sensor payloads

### Scientific/Research Operations
- **Severe weather monitoring:** VORTEX2 campaign demonstrated complex multi-vehicle coordination for tornado/supercell research
- **Autonomous cooperative tasks:** Demonstrated through physical Pac-Man game implementation using 5 ground robots, showing rapid reconfiguration capability

### Commercial Market (Post-SBIR)
- **Ranching applications:** Cattle counting and herd management
- **Land management:** Wetland land cover mapping, general ranch management
- **Aerial imaging and survey:** Turn-key remote sensing service provision
- **Utility management:** Implied infrastructure inspection and monitoring

## Phase I Technical Objectives (Deliverables)

1. **Vehicle/Team Participant List:** Identification of multi-vehicle team types and expected vehicle interfaces
2. **Data Hierarchy:** Mission-relevant data organized by situation and operator level
3. **Situation Recognition Algorithms:** Context-switching mechanisms with clear algorithmic explanations
4. **SA Reconciliation Methods:** Mechanisms for maintaining operator-vehicle team situational agreement
5. **Uncertainty Typology:** Comprehensive list of uncertainty types with display methodology
6. **Evaluation Plan:** Metrics including intuitiveness, information location time, command issuance time, uncertainty identification capability, SA reconciliation time
7. **Hardware Platform Plan:** Current OCU platforms catalogued; desired technologies (surface computing, touch interfaces) identified; implementation approach defined
8. **Visualization Mock-up:** Complete interface demonstration for all situations and both tablet/surface platforms
9. **Final Report:** Comprehensive system documentation with Phase II implementation plan and risk mitigation strategy

## Phase I Optional Work (If Selected)

- Design modifications based on feedback
- Hardware selection for prototype (specific tablet and surface computing platforms)
- Skeleton OCU implementation with limited functionality for interface/UX analysis
- TIGR system interface specification
- Simulation environment integration with vehicle and situation data
- Updated final report incorporating interim work

## Key Results

This is a proposal document without results. However, it references previous successful implementations:

**VORTEX2 Campaign (2009-2010):**
- Successfully demonstrated NetUAS in most complex operational configuration to date
- Coordinated 4 networked vehicles with multiple subsystems each
- Enabled real-time data distribution and command across heterogeneous team
- Demonstrated capability to handle large numbers of vehicles and complex interfaces

**Pac-Man Autonomous Demonstration:**
- Small team (3 engineers) rapidly reconfigured NetUAS from aerial to ground robot control
- Included autonomous agents, indoor sensors, live video in 3-week timeframe
- Demonstrated system modularity and flexibility despite unfunded/skunkworks nature

**Previous Commercial Pilots (Planned, not yet executed):**
- Identified 5 early adopter ranching sites in Colorado/Wyoming with $750K-$3M annual revenues
- Planned June-August 2012 pilots expected to generate $60K-$80K revenue
- Land areas to be mapped: 1-3 square miles (within prototype system capability)
- System cost: ~$2,000-3,000 per platform (excluding payload)

## Notable Details

### Partnerships & Institutional Support
- **University of Colorado Boulder:** Facilities partnership, access to 3 airframes operating under 62 Certificates of Authorization spanning 24,000 square miles
- **RECUV (Research and Engineering Center for Unmanned Vehicles):** Co-design partner on autopilot and aircraft platform; over 300 flight experiments conducted
- **NSF Major Research Instrumentation (MRI) Grant:** Concurrent next-generation UAS development with meshed networking, collision avoidance, environmental energy extraction, and cooperative control — designed to integrate with OCU results for real-world testing
- **Potential University of Colorado Consultant Pool:** Computer Science department available for Phase II if needed

### Competitive Advantages Claimed
- 8+ years of multi-vehicle UAS OCU design and operational experience (vs. competitors with single-vehicle focus)
- NetUAS architecture supports heterogeneous systems with dynamic service discovery (vs. static, vehicle-type-specific competitors)
- Demonstrated field deployment and real-world validation through VORTEX2
- Co-located team expertise in autopilots, networking, cooperative control, and UI/UX
- Access to test vehicles and airspace (24,000 sq mi of authorized flight area)

### Commercialization Model
- **Revenue Strategy:** Position as "data service provider" rather than UAS vendor — eliminating need for end-user training/support
- **Pricing Model:** Value-based pricing tied to application, area mapped, vehicle count, and imaging modality
- **Target Markets:** Ranching/land management (pilot), with planned expansion to farming, utility management, and broader remote sensing ($8B market projected by 2015)
- **Phase I Funding Expected Outcome:** Prototype validation to attract investor capital for commercialization

### Timeline and Funding Context
- Document created December 29, 2011; reflects late-2011 market conditions
- References FAA commercial UAS approval expected "by end of 2012" (actually took much longer)
- Mentions pending RECUV autopilot licensing ($4K-7K recovery expected by February 2012)
- Positioned to capitalize on anticipated 2015 commercial UAS market explosion

### Risk Awareness
- Identifies integration with existing Army systems (TIGR, JAUS standards) as primary Phase II concern
- Acknowledges need for TIGR system clearance/approval before Phase II deployment
- Hardware selection deferred to Phase I Option to enable rapid Phase II transition