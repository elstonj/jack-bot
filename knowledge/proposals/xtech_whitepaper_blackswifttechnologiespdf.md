# Real-Time Autonomous UAS Swarms for Volumetric Sensing in Hazardous Environments

## Document Metadata
- **Type:** Concept White Paper (xTech Innovation submission)
- **Client/Agency:** U.S. Army
- **Program/Solicitation:** xTech Overwatch (Army innovation program)
- **Date:** 2025 (submission year; document created/modified May 21, 2025)
- **BST Products/Systems Referenced:** S2 UAS, S0 UAS, S0-VTOL (VTOL fixed-wing variant)
- **Key Personnel:** 
  - Dr. Maciej Stachura (CTO, Black Swift Technologies)
  - Dr. Jack Elston (CEO, Black Swift Technologies)
  - Dr. Gijs de Boer (Chair, Environmental Science & Technologies Dept., Brookhaven National Lab)
  - Dr. Arthur Sedlacek (Atmospheric Chemist, BNL)
  - Andrew McMahon (Electrical Engineer, BNL)

## Executive Summary
This innovation proposes an autonomous, distributed UAS swarm system that leverages Neural Radiance Fields (NeRFs) to achieve real-time 3D volumetric reconstruction of dynamic scenes, specifically for detecting, classifying, and tracking airborne plumes from explosions, chemical, or biological events. The system enables safe, rapid characterization of hazardous plumes using sparse, non-overlapping imagery from multiple small, fast-moving VTOL fixed-wing UAS operating autonomously as a coordinated team, with scalability to broader battlefield assessment applications.

## Technical Approach

### Core Technology
- **Neural Radiance Fields (NeRFs):** High-fidelity 3D volumetric reconstruction of dynamic, semi-transparent scenes from sparse, non-overlapping imagery—unlike traditional photogrammetry
- **NeRF Extensions:** K-Planes and Dex-NeRF specifically designed to handle time-varying scenes and transparency characteristics of plumes
- **Platform Base:** Black Swift Technologies' hardened, fixed-wing VTOL UAS (S0-VTOL) engineered for stable, long-endurance flight in extreme conditions
- **Multi-UAS Coordination:** Autonomous mission execution with minimal human input, enabling one-to-many control and swarm operations

### Positioning and Sensing Requirements
- **GPS Accuracy:** Centimeter-level precision achievable via RTK GPS (already used on proposed UAS and commercial platforms)
- **Heading Accuracy:** S0 UAS uses dual GPS providing 0.2-degree heading accuracy
- **Gimbal Pointing Accuracy:** Commercial gimbals achieve 0.5-degree pointing accuracy
- **Goal:** Relax traditional NeRF requirements (sub-degree rotation, centimeter-level translation) to levels achievable by current government UAS systems

### Integration Approach
- Vertically integrated engineering: custom avionics, sensor development, and AI-driven flight control
- Modular, open-source software framework for adaptability and platform compatibility
- Machine-readable reconstructed scene data immediately shareable with other robotic systems for real-time navigation and hazard avoidance
- Hybrid and optimized processing strategies to handle computational intensity

### Partnership
- **Brookhaven National Laboratory (BNL):** Advanced machine vision development expertise; atmospheric science expertise (aerosol processes, particulate physics, emission plume evolution); AI/ML techniques for atmospheric measurement

### Technical Risks & Mitigation
**Risks:**
- NeRF fidelity issues in sparse or dynamic scenes
- Platform pointing accuracy and lighting condition challenges
- Real-time processing latency (NeRF methods computationally intensive, may hinder timely autonomous responses)
- Multi-sensor synchronization and calibration (EO/IR, GPS/IMU integration)

**Mitigation:**
- Controlled testing to define performance limits
- Leveraging BST's proven integration expertise
- Hybrid and optimized processing strategies
- Modular, open-source framework for adaptability

### TRL Level
TRL 1-2 (Basic Research)

## Products & Capabilities Described

### S2 UAS
- **Description:** Medium-endurance fixed-wing UAS originally developed with NASA through SBIR program
- **Use Case:** Currently used by NASA, NOAA, USGS, and commercial entities for scientific remote sensing and Earth science missions
- **Status:** Transitioned from R&D prototype to production system; now commercial offering

### S0 UAS
- **Description:** Unique air-deployed fixed-wing UAS capable of extreme-weather operations (Category 5 hurricanes, Arctic conditions, active volcano plumes)
- **Development:** Originally developed under NOAA SBIR
- **Use Case:** Primary supplier to NOAA for hurricane reconnaissance missions; transitioning to broader government and commercial operations
- **Production Growth:** 4 units two years ago → 19 units last year → 50 units ordered this year, with expectations exceeding 100 units next year (NOAA, Navy, Air Force orders)
- **Capabilities:** Achieves centimeter-level GPS accuracy with RTK, dual GPS for 0.2-degree heading accuracy

### S0-VTOL
- **Description:** VTOL (vertical takeoff and landing) variant of the S0, fixed-wing hybrid configuration
- **Proposed Use:** Platform of choice for this Army plume-tracking initiative
- **Advantages:** Combines VTOL flexibility with fixed-wing endurance and speed; achieves rapid or long-range assessment superior to quadrotor solutions

## Use Cases & Applications

### Primary Use Case
**Hazardous Plume Characterization:** Autonomous detection, classification, and 3D volumetric tracking of airborne plumes from:
- Explosive events
- Chemical releases
- Biological incidents
- Enables safe, rapid characterization where manual UAS operations are labor-intensive and risky

### Secondary/Scalable Applications
- **3D Battlefield Assessment:** Situational awareness, target recognition, damage estimation, mission planning
- **Emissions Monitoring:** EPA applications for regulatory compliance
- **Incident Response:** FEMA autonomous systems for hazardous incident response
- **Atmospheric Research:** NOAA/NASA enhancement of atmospheric particulate and plume physics studies
- **Industrial Monitoring:** 
  - Oil and gas leak detection and compliance (BST already working with Chevron)
  - Utilities, chemical manufacturing, waste management safety and operational efficiency
  - Asset protection

### Adjacent/Demonstrated Applications
- Hurricane reconnaissance (NOAA operations)
- Arctic operations
- Active volcano monitoring and sampling
- Severe storm research

## Key Results
This is a concept white paper proposing future work; no experimental results are presented. The document is forward-looking, outlining planned technical approach rather than completed research.

## Notable Details

### Competitive Advantages
1. **Hardware Hardening:** BST world leader in UAS designed to survive extreme environments where competitors won't operate
2. **Recent Guinness World Records:**
   - Highest winds flown in: 240 mph (UAS world record)
   - Consistent operations in Arctic, severe storms, active volcano plumes
3. **AI-Native Approach:** Machine-readable volumetric data immediately shareable with other autonomous systems for real-time decision support
4. **Modular Design:** Open-source software framework enables rapid adaptation and compatibility across platforms

### Operational Track Record
- **Government Customers:** NASA (Earth Science missions), NOAA (hurricane operations), USGS
- **Mission Operations:** Described as "very operation-heavy organization" with regular government customer flights
- **Army Engagement:** Recently increasing Army involvement; planned demonstrations at August UAS Summit with Army Capability Manager-Unmanned Aircraft Systems (ACM-UAS)

### Commercial Transition Record
- Multiple SBIR-funded technologies successfully transitioned to commercial products (S2, S0)
- Proven pathway from R&D prototype to production system to broad government/commercial adoption

### Company Information
- **Location:** Boulder, Colorado
- **Size:** 9 employees (at time of submission)
- **Website:** www.bst.aero
- **Previous DoD Business:** AFWERX, Navy, Air Force contracts
- **Capital Raised:** $0.00 (indicates bootstrap or self-funded operation as of submission date)
- **Primary Contact:** Maciej Stachura (stachura@blackswifttech.com)
- **Secondary Contact:** Jack Elston (elstonj@blackswifttech.com)

### Army Strategic Alignment
- Autonomy and collaborative multi-UAS coordination (Army modernization priority)
- Reduction of human operators in hazardous environments
- One-to-many control and machine-to-machine coordination
- Decentralized, real-time data collection for enhanced situational awareness
- AI-native alternative to legacy ISR systems