# Development of a Low-Cost, High-Speed Unmanned Vehicle Flight Test Research Platform

## Document Metadata
- **Type:** NASA Research Announcement (NRA) Proposal
- **Client/Agency:** NASA (Innovative Concepts for Aviation - Leading Edge Aeronautics Research for NASA, LEARN)
- **Program/Solicitation:** LEARN1 NRA NNH13ZEA001N
- **Date:** August 1, 2013
- **BST Products/Systems Referenced:** SwiftPilot autopilot system
- **Key Personnel:** 
  - PI: Dr. Ryan P. Starkey (University of Colorado Boulder)
  - Co-I: Dr. Eric W. Frew (CU Boulder)
  - Co-I: Dr. Brian Argrow (CU Boulder)
  - Dr. Jack Elston (Black Swift Technologies, President)
  - James Mack (CU RECUV, Systems Engineer & Pilot)

## Executive Summary
This proposal seeks NASA funding to develop a low-cost, high-speed (Mach 1.4) unmanned aerial system (UAS) as a reusable flight test research platform. Building on four years of development at University of Colorado Boulder (the "GoJett" project), the team proposes a two-year effort to construct two identical supersonic UAS vehicles, increase technology readiness levels (TRLs) for supersonic unmanned systems, and develop flight test planning and procedures that reduce testing costs by an order of magnitude compared to current manned aircraft practices.

## Technical Approach

### Overall Strategy
- **Year 1:** System design refinement, component selection, safety/risk analysis, subsonic flight testing (up to Mach 0.6-0.8)
- **Year 2:** High-subsonic and low-supersonic flight testing at NASA Dryden Flight Research Center

### Vehicle Specifications (GoJett Configuration)
- **Target Speed:** Mach 1.4+
- **Empty Mass:** 30 kg
- **Fueled Mass:** 50 kg
- **Dimensions:** 2.4 m long, 1.3 m span
- **Hardware Cost:** ~$120,000 (substantially less expensive than comparable aerial targets while fully reusable)
- **Construction:** Carbon fiber composite fuselage and wings with internal spar structure
- **Propulsion:** AMT Nike miniature turbojet engine (baseline thrust 780 N) with planned afterburner addition for Phase II
- **Inlet:** Pitot inlet designed for maximum pressure recovery up to Mach 1.5
- **Control:** Fully automatic with certified RC pilot backup; uses vertical stabilizer/rudder (thrust vectoring nozzle deferred to Phase II as risk reduction)

### Control System Architecture
- **Flight Computer:** BST SwiftPilot autopilot system
- **Control Strategy:** Successive loop closure, dynamic inversion control, and gain scheduling
- **Development Validation:** 
  1. Test SwiftPilot on commercial off-the-shelf (COTS) jet trainer aircraft first
  2. Design control system for subsonic/transonic GoJett flight (up to Mach 0.8)
  3. Integrate ground proximity sensor and aeroprobe wind angle sensor
  4. Demonstrate auto-landing capability at 60+ knots
  5. Obtain FAA Certificates of Authorization (COAs)

### Aerodynamic Design
- CFD analysis using ZEUS and ANSYS software
- Wind tunnel validation at US Air Force Academy tri-sonic facility (Schlieren imaging for shock pattern verification)
- Performance envelope analysis showing vehicle can reach Mach 1.4 at 0-3 km altitude
- Specific excess power (P_s) diagrams developed for flight envelope definition
- Emphasis on minimizing inlet distortion and assessing air-data probe aerodynamic losses

### Propulsion System
- AMT Nike turbojet (COTS baseline engine for Phase I)
- Static test stand evaluation and ground testing
- Propulsion-airframe integration design and testing
- Afterburner design development for Phase II (long-lead item)
- Engine modifications and controller integration experience with both AMT and Jetcat engines

### Flight Operations & Airspace Access
Two-step airspace strategy:
1. **Low-speed testing (Mach 0.5-0.6):** FAA airspace via Certificate of Authorization (COA), leveraging CU's RECUV expertise (holds more active COAs than any other entity)
   - Potential sites: Table Mountain (Boulder, CO), New Mexico State University UAS Flight Test Center, or planned FAA UAS test sites
2. **High-speed testing (subsonic to supersonic):** NASA Dryden Flight Research Center or Edwards AFB restricted airspace

## Products & Capabilities Described

### BST SwiftPilot Autopilot System
- **What it is:** Low-cost, highly capable miniature aircraft autopilot developed by Black Swift Technologies
- **Specifications:** Designed for small UAS with limited computational resources; integrates flight computer, sensor interfaces, and telemetry
- **Proposed Use:** Primary flight control system for GoJett platform, with control algorithms developed collaboratively by CU and BST
- **Risk Reduction:** Initial testing planned on COTS jet trainer before integration into supersonic platform
- **Key Capability:** Sufficient bandwidth and computational performance for high-speed control (up to and exceeding Mach 1.4)
- **Features:** Backup RC pilot interface with video streaming, automated fail-safe systems, sensor blending (air-data probes, ground proximity sensors)

### GoJett Unmanned Aerial System
- **Configuration:** Tailless supersonic design with vertical stabilizer (for Phase I) or thrust-vectoring nozzle (Phase II)
- **Materials & Construction:** Carbon fiber composite shell and bulkheads manufactured via patent-pending rapid prototyping mold at EBS Carbon
- **Deliverables for Phase I:** Two identical, flight-ready aircraft with production-level construction procedures and materials suitable for Mach 1.4+ sustained flight

## Use Cases & Applications

The proposal identifies extensive potential applications (Table 1) organized by technical discipline:

### Aerodynamics
- Sonic boom/acoustics research
- Blended wing body concepts
- Flow control techniques
- Stealth configurations
- Inlet designs
- Variable sweep wing technology

### Control & Operations
- Vertical takeoff systems
- Damaged aircraft control
- Flow control
- Pilot interface design
- Proximity/UAS integration in National Airspace System (NAS)
- Autonomy and sense-and-avoid algorithms
- Cooperative control systems

### Structures & Materials
- Additive manufacturing
- Advanced composites
- Integral antennas
- Coatings and protective systems
- Damage detection
- Landing gear integration

### Propulsion
- Altitude-compensating nozzles
- Combined-cycle engines
- Thrust vectoring
- Mode transition (subsonic-to-supersonic)
- In-flight refueling
- Rockets and staging concepts
- Variable geometry components
- Energy harvesting systems

### Science & Sensing
- Novel sensor integration
- Sensor blending algorithms
- Environmental monitoring
- Hurricane penetration research
- Tornado approach research
- Emergency response operations
- Flights of opportunity for atmospheric sampling

### Specific NASA Alignment
The proposal explicitly addresses four objectives from the LEARN NRA:
1. Assessment of environmental impact of increased routine UAS operations in NAS
2. Novel multidisciplinary design strategies for complex aeronautics systems
3. Exploitation of aeroelastic/aeroservoelastic behavior for improved aircraft
4. Hybrid-electric distributed propulsion with integrated autonomous control

## Key Results (Previous Work)

### GoJett Development History
- **Development Period:** Four years (prior to proposal submission in 2013)
- **Design Status:** Preliminary Design Review and transonic wind tunnel testing completed; currently on Major Design Revision 8
- **Engineering Test Unit (ETU):** Under construction at time of proposal; discovered actual shell/bulkhead mass was 5-8 kg less than estimated, enabling design elongation for drag reduction
- **Wind Tunnel Results:** 
  - USAF Academy tri-sonic testing completed
  - Schlieren imaging of shock patterns at Mach 1.32
  - CFD validation via ANSYS matching experimental Schlieren patterns closely
  - Model incorporated surface roughness and assembly gaps for accuracy

### Component Development
- **Propulsion System:** Multiple test iterations of gas turbine engine with afterburner and variable area nozzle
- **Structures:** Carbon fiber manufacturing process validated and refined; rapid prototyping mold approach proven
- **Control Systems:** Control architecture design and preliminary validation completed
- **Mass Budget:** Baseline vehicle at 50 kg with ~10 kg margin
- **Performance Envelope:** CFD analysis and constraint analysis show vehicle can reach Mach 1.4 at 3 km altitude with baseline 780 N thrust

### Manufacturing Lessons Learned
- Carbon fiber design/analysis tools (ANSYS FEA, Solidworks) require careful validation against physical hardware
- Rapid prototyping mold approach at EBS Carbon reduces cost while enabling accurate geometry

## Notable Details

### Cost & Affordability Focus
- Total airframe hardware cost: ~$120,000 (competing aircraft examples: HiMAT cost $17M, X-36 cost $21M, BQM-167A target $0.57M/unit)
- Completely reusable platform (unlike disposable targets)
- Expendable capability enables bolder flight test profiles with reduced risk-aversion drivers
- Repeatable, low-cost design process suitable for rapid adaptation to new configurations

### Partnership Structure
**Academic:** University of Colorado Boulder (PI institution with 4 years development history)

**Industrial Partners:**
- **Black Swift Technologies:** Flight computer (SwiftPilot) and flight control expertise (Dr. Jack Elston, President)
- **EBS Carbon:** Carbon fiber airframe manufacturing
- **Raytheon/Boeing Phantomworks:** Technical oversight and aerospace system expertise (pending formal commitment)

**Government/Military:**
- **NASA Dryden Flight Research Center:** Flight test planning, safety/risk analysis, facility access for high-speed testing (in-kind support, pending approval)
- **US Air Force Academy:** Wind tunnel facility access and transonic testing support (CRADA relationship)
- **AFRL Air Vehicles Directorate:** Technical advisory board support (no direct funding)

**University Resources:**
- **RECUV (Research & Engineering Center for Unmanned Vehicles):** FAA COA expertise, facilities, personnel
- **Computational:** JANUS supercomputer (184 teraflops, 16,416 cores), CHyMP private cluster (128 cores), workstations
- **Manufacturing:** Department machine shops (no labor cost from indirect budget), composite lab
- **Testing:** Table Mountain Radio Quiet Zone (1,800 acres near Boulder), Pawnee National Grasslands (32x32 km near Greeley)

### FAA & Regulatory Strategy
- RECUV holds more FAA Certificates of Authorization than any other entity in the country
- Recent COA approval turnaround: 3 months or less with multi-state coverage (Colorado, Nebraska, Oklahoma, Alaska)
- Proposal to streamline risk/safety assessment through integrated vehicle design and concept-of-operations
- Advisory board includes government and industry expertise in high-speed flight testing and risk management

### Technology Readiness & Risk Reduction Strategy
- **Heritage Components:** Most major subsystems (landing gear, control systems, structural concepts) already flight-tested
- **Risk Mitigation:** 
  - Phase I uses unmodified off-the-shelf engine (not custom custom engine) for 0.6-0.8 Mach testing
  - Vertical stabilizer/rudder baseline instead of thrust-vector nozzle for Phase I
  - Engineering Test Unit (ETU) used to validate integration before Critical Design Review
  - Comprehensive ground testing (component, subsystem, integrated) prior to flight
  - Hardware-in-the-loop and software-in-the-loop simulation validation
  - Test Readiness Review at Month 9 with expert advisory board participation

### Project Team Organization
- PI as Project Manager; Professional Research Assistant as Systems Engineer
- 3 faculty + 3 professional research assistants + 4 graduate research assistants
- 10-15 graduate/undergraduate students contributing 15-25 hours/week
- Weekly full-team meetings, twice-weekly sub-team meetings
- Monthly interactions with advisory board (government, industry, military)

### Deliverables
1. Aircraft hardware selection documentation (sensors, components enabling low-cost design)
2. Flight test planning and FAA integration procedures
3. Flight test planning for NASA Dryden (risk/safety analysis minimization approach)
4. Two flight-ready unmanned aircraft
5. Journal, conference, and progress