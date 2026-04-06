# NASA FY25 Phase I SBIR Subtopics

## Document Metadata
- Type: Solicitation guidance document
- Client/Agency: National Aeronautics and Space Administration (NASA)
- Program/Solicitation: Small Business Innovation Research (SBIR) Phase I, Fiscal Year 2025
- Date: 2025 (FY25)
- BST Products/Systems Referenced: None mentioned
- Key Personnel: None named

## Executive Summary
This is NASA's comprehensive FY25 SBIR Phase I solicitation document listing 60+ research subtopics across four mission directorates: Aeronautics Research (ARMD), Exploration Systems Development/Space Operations (ESDMD/SOMD), Science (SMD), and Space Technology (STMD). The document provides guidance, scope descriptions, technical requirements, and expected deliverables for small business innovation proposals across diverse aerospace and space technology areas.

## Document Structure
The document is organized by NASA Mission Directorate with subtopics identified by coded prefixes:
- **A** = Aeronautics Research Mission Directorate (ARMD)
- **H** = Exploration Systems Development Mission Directorate (ESDMD) and Space Operations Mission Directorate (SOMD)
- **S** = Science Mission Directorate (SMD)
- **Z** = Space Technology Mission Directorate (STMD)

## Key ARMD Subtopics Detailed (A-series)

### A1.02: Quiet Performance - Airframe Noise (SBIR)
- **Lead Center:** LaRC (Langley Research Center)
- **Participating Centers:** GRC (Glenn Research Center)
- **Scope Areas:**
  - Airframe Noise Analysis and Characterization
  - Airframe Noise-Prediction Technologies
  - Airframe Noise Reduction
- **Technical Focus:** Computational fluid dynamics techniques for aeroacoustic analysis, source identification methods for noise from landing gear and high-lift systems, novel instrumentation for noise measurement
- **Expected TRL at Completion:** 2 to 5
- **Primary Technology:** TX 15 Flight Vehicle Systems / TX 15.1 Aerosciences
- **Deliverables:** Research, Analysis, Prototype, Hardware, Software
- **Target Applications:** Advanced Air Vehicles Program (AAVP), Integrated Aviation Systems Program (IASP), Transformative Aeronautics Concepts Program (TACP), Truss-Braced Wing, small-core turbofan engines, ultra-high-bypass ratio engines
- **Critical Gaps:** Efficient computational tools for rapid evaluation of noise impact at design stage; improved numerical methods for complex engine/airframe configurations; better acoustic consideration in early design phases

### A1.03: Propulsion Efficiency - Propulsion Materials and Structures (SBIR)
- **Lead Center:** GRC
- **Scope:** Advanced materials and structures technologies for new highly efficient propulsion systems for subsonic transport vehicles
- **Expected TRL:** 1 to 4
- **Primary Technology:** TX 12 Materials, Structures, Mechanical Systems, and Manufacturing / TX 12.1 Materials
- **Key Technology Areas of Interest:**
  - **Modeling:** Rapid characterization of physics-based and data-driven constitutive models; computational materials and multiscale modeling tools; robust methods for designing advanced propulsion materials at all length scales; multiscale design tools
  - **High-Temperature Materials:** CMC (ceramic matrix composite) and EBC (environmental barrier coating) technology for components operating at 1,482°C (2,700°F) or higher; additive manufacturing approaches
  - **Digital Twin and Digital Thread:** Integration toolsets for ICME (Integrated Computational Materials Engineering) workflow automation; AI/ML models for digital twin/thread for propulsion materials and structures
- **Critical Gaps Identified:** Under-development of physics-based models linking length and time scales; inability to conduct real-time characterization at appropriate scales; lack of optimization methods bridging scales; lack of sensitivity and uncertainty models; insufficient verification and validation methods
- **Phase I Expectations:** Establish scientific, technical, and commercial feasibility; demonstrate advancement through analytical and experimental studies
- **Phase II Outcomes:** Models with experimental data, software tools, demonstrated material systems with enhanced properties, modeling tools for incorporation into NASA projects
- **Commercial Path:** Phase I recipients must consider commercialization and identify organizations to use technology post-Phase II

### A1.04: Novel Aircraft Configurations for Electrified Aircraft Propulsion (SBIR)
- **Lead Center:** GRC
- **Scope:** Zero-emission electric aircraft for 1,500 to 5,000 lbs. drones and piloted aircraft enabled by electric propulsion
- **Expected TRL:** 1 to 3
- **Primary Technology:** TX 01 Propulsion Systems / TX 01.3 Aero Propulsion
- **Key Performance Metrics:** Payload, range, speed, energy use per mile, in-flight emissions per mile
- **Phase I Deliverables:**
  1. Design study demonstrating novel configuration uses less total energy than current aircraft
  2. Engine producing both thrust and electric power with outputs aligned to application
  3. Clear path to FAA certification date of 2030 or earlier
  4. Identified launch customers with letters of commitment
  5. Payload, range, speed, and energy metrics matched to launch customer
  6. Understanding of relevant FAA/military standards for engines and aviation electrical systems
  7. Operational concept describing flight segments, conditions, and recharge concept
  8. Facilities to support Phase I and II development/testing
- **Phase II Deliverable:** Small, flying prototype zero-emission electric aircraft scalable to 1,500-5,000 lbs.
- **Strong Proposal Characteristics:**
  - One or more identified launch customers with letters of commitment
  - Clear FAA certification path for 2030 or earlier
  - Performance metrics matched to launch customer requirements
  - Solutions applicable to UAV, aircraft, and eVTOL systems in 1,500+ lbs. class
  - Understanding of FAA/military standards
  - Clear operational concept
  - Adequate facilities for development/testing
- **Market Context:** Applicable to emerging electric and electric aircraft markets
- **Note:** Focuses on aircraft designs, not hybrid-electric engines (see A1.09 for engine proposals)

### A1.06: Vertical Takeoff and Landing (VTOL) Vehicle Technologies (SBIR)

#### Scope 1: Technologies to Improve VTOL Vehicle Design Tools
- **Focus:** Rotorcraft Design Tool Airfoil Table Generator
- **Technical Description:**
  - Automated tool for preparing C81-formatted airfoil tables
  - C81 tables contain lift, drag, moment coefficients over ±180° angle of attack
  - Multiple Mach numbers covering rotor operating range
  - Combines experimental and predicted values
- **Capabilities Required:**
  - Ability to generate C81 tables using predicted coefficients
  - Support for various airfoil types (sharp/blunt leading/trailing edges, multi-element designs)
  - Reynolds number range: tens of thousands to tens of millions in chord Reynolds
  - Mach number range: near zero to >Mach 1
  - Capture stall, post-stall, and reversed flow conditions
  - Support multiple aerodynamic solvers (xfoil, MSES, Overflow, etc.)
  - Interface with various airfoil coordinate input formats
  - Computational grid generation capability
  - Graphical user interface, command-line interface, and Python API modes
  - Ability to merge predicted coefficients with other sources (e.g., NACA 0012 standard tables)
- **Expected TRL:** 3 to 5
- **Primary Technology:** TX 11 Software, Modeling, Simulation, and Information Processing / TX 11.2 Modeling
- **Deliverables:** Analysis, Research, Prototype
- **Phase I Expectations:** Design concepts supported by analytical studies, establish Phase II goals, quantify technology performance projections
- **Phase II Expectations:** Further develop designs, validate achievement of goals through analysis, modeling, simulation, and product demonstration
- **Relevance:** Revolutionary Vertical Lift Technology (RVLT) Project, Advanced Air Vehicle Program; addresses Advanced Air Mobility mission objectives and Strategic Thrust 4: Safe, Quiet, and Affordable Vertical Lift Air Vehicles

#### Scope 2: High Voltage eVTOL Powertrain Test Equipment
- **Objective:** Develop EMI (electromagnetic interference) and PQ (power quality) test equipment for eVTOL powertrain systems
- **Operating Requirements:**
  - Operating voltages: minimum 650 Vdc (1 kV preferred)
  - Current: 150 A minimum (300 A preferred)
  - Bandwidth: DC to 250 kHz minimum (may vary by application)
  - Operating altitude: up to 15,000 ft
  - 250 kHz bandwidth for EMI noise investigation
- **Equipment Types Needed:**
  - EMI equipment: power amplifiers, isolation transformers, ripple/surge injection units
  - Power equipment: power amplifiers, isolation transformers, fault injection units, dynamic load banks, wide bandwidth emulators/power supplies
- **Expected TRL:** 4 to 6
- **Primary Technology:** TX 13 Ground, Test, and Surface Systems / TX 13.2 Test and Qualification
- **Deliverables:** Hardware, Analysis
- **Phase I Expectations:** Detailed design and analysis of proposed equipment; breadboard units to validate approach (desired)
- **Phase II Expectations:** Prototype hardware validated through testing
- **Critical Gap:** EMI and PQ test equipment for high voltage/high power applications does not currently exist
- **Context:** Supports EAPT (Electrified Aircraft Propulsion Technologies) and RVLT projects; provides data for FAA certification standards development

### A1.08: Aeronautics Ground Test and Measurement Technologies: Diagnostic Systems for High-Speed Flows and Icing (SBIR)
- **Lead Center:** LaRC
- **Scope:** Two primary areas - diagnostic systems for high-speed flows and icing research diagnostics
- **Expected TRL:** 3 to 6
- **Primary Technology:** TX 13 Ground, Test, and Surface Systems / TX 13.2 Test and Qualification

### A1.09: Zero-Emissions Technologies for Aircraft (SBIR)
- **Lead Center:** GRC
- **Focus:** Technologies for reducing or eliminating aircraft emissions
- **Distinction from A1.04:** A1.09 focuses on engine technologies while A1.04 addresses aircraft configurations

### A1.11: Health Management and Sensing Technologies for Sustainable Aviation Vehicles (SBIR)
- **Lead Center:** GRC
- **Scope:** Sensing and health management systems for sustainable aviation vehicles

### A2.01: Flight Test and Measurement Technologies (SBIR)
- **Lead Center:** LaRC
- **Focus:** Technologies for aircraft flight testing and measurement systems

### A2.02: Enabling Aircraft Autonomy (SBIR)
- **Lead Center:** LaRC
- **Scope:** Technologies for autonomous aircraft operations

### A2.04: Aviation Cybersecurity (SBIR)
- **Lead Center:** LaRC
- **Focus:** Cybersecurity solutions for aviation systems

### A3.02: Advanced Air Traffic Management for Nontraditional Airspace Missions (SBIR)
- **Lead Center:** LaRC
- **Scope:** Air traffic management for new airspace use

### A3.03: Future Aviation Systems Safety (SBIR)
- **Lead Center:** LaRC
- **Focus:** Safety technologies for aviation systems

### A3.05: Advanced Air Mobility (AAM) Integration (SBIR)
- **Scope:** Integration of advanced air mobility systems

## ESDMD/SOMD Subtopics (H-series)
The document lists 13 subtopics under the Exploration Systems Development Mission Directorate and Space Operations Mission Directorate (H3-H15 series), covering:
- Oxygen-compatible habitation solutions
- Hydrogen peroxide production in space
- Long-duration portable life support systems
- Advanced materials for spacesuits
- Lunar solar array structures
- Trusted autonomy in space systems
- In-space production applications
- Flight dynamics and navigation
- Lunar communication technologies
- Commodity purity analysis
- Venous gas emboli detection
- Lunar surface mobility systems (autonomous capabilities and regolith simulation)

## SMD Subtopics (S-series)
The document lists 23 subtopics under the Science Mission Directorate (S11-S17 series), covering:
- Remote sensing technologies (Lidar, active/passive microwave, sensors)
- Exoplanet detection and characterization
- Optical systems and fabrication/testing
- X