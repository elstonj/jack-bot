# A Ruggedized UAS for Scientific Data Gathering in Harsh Environments

## Document Metadata
- Type: Phase I SBIR Proposal
- Client/Agency: NASA
- Program/Solicitation: NASA SBIR (Topic S3.04-8077)
- Date: 2016 (SBIR solicitation year)
- BST Products/Systems Referenced: SuperSwift airframe, SuperSwift XT (proposed), SwiftCore FMS, SwiftPilot autopilot, SwiftStation ground station, SwiftTab user interface
- Key Personnel: Dr. Jack S. Elston (PI/CEO), Prof. Brian Argrow (University of Colorado Boulder), Dr. Lois J. Wardell (Arapahoe SciTech), Dr. Cory Dixon, Dr. Maciej Stachura

## Executive Summary
Black Swift Technologies proposes the SuperSwift XT, a ruggedized small unmanned aircraft system (sUAS) purpose-built for collecting in situ scientific data from volcanic ash plumes and other harsh atmospheric environments. Based on the proven SuperSwift airframe and SwiftCore FMS, the XT variant will integrate trace gas, particulate, pressure, temperature, humidity, and wind sensors to support volcanic ash transport and dispersion (VATD) modeling and aviation safety.

## Technical Approach

### Phase I Objectives (6-month effort):
1. **Development of requirements** - Create concept of operations (CONOPS) for volcanic plume sampling based on mission parameters, sensor needs, and field heritage
2. **Ruggedization of SuperSwift airframe** - Modify design for sustained flight at up to 20,000 ft MSL with improved propulsion, wing aerodynamics, and ash/particulate protection
3. **Sensor suite integration** - Design and specify integration of:
   - Trace gas sensors (SO₂, CO₂, expandable to H₂S and CH₄)
   - Particulate sensors (particle size-frequency distribution, vertical ash concentration)
   - PTH sensors (pressure, temperature, humidity)
   - 3D wind measurement system
4. **Flight planning and certification** - Prepare FAA COA documentation and NASA Flight Safety/Flight Readiness Review materials for Phase II testing
5. **System specification** - Document final design, risks, and Phase II implementation plan

### Key Technical Modifications:

**Airframe improvements:**
- Battery, motor, and propeller optimization for sustained high-altitude flight
- Wing aerodynamic redesign for efficient 20 kft operations and improved turbulence handling
- Custom motor cowling and protective coverings to shield electronics from ash/particulates
- Enhanced seals on nose cone and interface points

**Sensor integration:**
- Field-swappable payload system with common power, data, and mechanical interfaces
- Modified nose cone with scoop design for proper airflow to sensors
- Custom internal scaffold for mass spectrometer, vacuum pump, and gas sensor mounting
- CFD and wind tunnel validation of scoop and airflow designs

**Avionics:**
- SwiftCore FMS expanded to support new sensor suite
- Near real-time data telemetry and sensor control via existing common data interface
- Aircraft state estimate for georeferencing sensor data

## Products & Capabilities Described

### SuperSwift (baseline platform)
- **Type:** Hand-launchable, fixed-wing sUAS for scientific missions
- **Characteristics:** Originally developed for NASA soil moisture mapping radiometer
- **Features:** 
  - Modular payload system with field-swappable nose cone
  - Proven endurance and operational range superior to multi-rotor systems
  - Standardized power, data, and mechanical interfaces
  - Larger payload capacity than Dragon Eye; longer endurance, higher ceiling, and longer range than Vector Wing
- **Proposed use in this context:** Base platform for XT variant

### SuperSwift XT (proposed innovation)
- **Type:** Purpose-built sUAS for harsh environment scientific sampling
- **Design drivers:** High altitude capability, strong winds/turbulence, ash/particulate protection
- **Unique capabilities:**
  - Terrain-following operations at high altitudes (up to 20 kft)
  - Designed for repeated safe flights through corrosive particulate environments
  - Hand-launchable convenience with extended payload capacity
  - Multi-mission flexibility through interchangeable payload modules
- **Performance specifications addressed:**
  - Sustained flight at 20,000 ft MSL
  - Aggressive flight envelope for strong turbulence
  - Particle size-frequency distribution measurement
  - Vertical ash concentration profiling
  - SO₂ and CO₂ flux measurement capability
  - Wind velocity measurement (3D)

### SwiftCore Flight Management System
- **Components:** SwiftPilot autopilot, SwiftStation ground station, SwiftTab user interface
- **Basis:** Derived from SwiftPilot Light (previously sold to research and commercial customers)
- **Scientific features:**
  - High-accuracy GPS
  - Advanced mission planning tools
  - Modular sensor payload architecture
  - Dedicated Linux single-board computer for sensor data processing and custom algorithms
  - On-board analysis capabilities
  - Near real-time data telemetry interface
  - Sensor control parameter transmission during flight
- **Expandability:** Already proven with hyperspectral cameras, infrared sensors, scanning lidar; proposed expansion to atmospheric chemistry sensors

## Use Cases & Applications

### Primary Application: Volcanic Plume Sampling
- **Scientific objectives:**
  1. Support new observational capabilities for chemical/physical properties of emissions to improve aviation ash hazard response
  2. Improve accuracy/precision of volcanic eruption predictions
  3. Calibrate and validate traditional volcanic plume sensing methods in dangerous circumstances

- **Measurement targets from fresh eruptions:**
  - Particle size-frequency distribution (vertical profile)
  - Ash cloud height and thickness
  - Spatial/temporal variability of ash concentration
  - SO₂ flux measurement
  - Trace gas composition (CO₂, H₂S, CH₄)
  - Temperature, pressure, humidity profiles
  - 3D wind field characterization

- **Operational concept:** Low-AGL terrain-following flight to directly sample plumes immediately after eruption (highest chemical/physical sample density), complementing HALE and medium-sized UAS that sample higher altitude dispersed plumes

### NASA Applications (mentioned):
- Support for Volcanic Ash Transport and Dispersion (VATD) model calibration/validation
- Enhancement of NASA's airborne science fleet performance
- Support for aviation safety (air traffic management systems informed by volcanic ash data)

### Non-NASA Applications (referenced as secondary focus):
- Wildfire smoke characterization
- Smog and gas cloud analysis
- General atmospheric chemical phenomena measurement in hazardous environments

## Key Design Rationale

**Why SuperSwift XT vs. existing platforms:**
- **vs. Multi-rotor sUAS:** Limited endurance and operational range for characterizing large-scale atmospheric structures
- **vs. modified general-purpose sUAS:** Existing platforms suffer from breakdowns and flight envelope limitations; not explicitly designed for harsh environmental survival
- **vs. Dragon Eye:** Larger payload capacity with proven science heritage
- **vs. Vector Wing:** Higher altitude ceiling, longer endurance, greater range
- **vs. medium/HALE UAS:** Lower cost, faster deployment, acceptable loss profile for high-risk missions, multi-aircraft swarm capability feasible

**Safety advantages:**
- Eliminates risk to researchers/scientists by enabling remote operation near dangerous phenomena
- Rapid deployment capability (minutes after eruption event)
- Multiple coordinated aircraft deployment for enhanced temporal/spatial sampling

## Technical Work Packages

### Work Package 1: Preliminary Tasks (Requirements Development)
- Kickoff meeting coordination (10 hours)
- CONOPS development for volcanic plume sampling (39 hours)
- Sensor measurement requirements identification (50 hours)
- Airframe requirements identification (56 hours total including CU team)
- Requirements document creation (42 hours + CU oversight)

### Work Package 2: Airframe Modifications and Development
- Performance evaluation vs. mission requirements (273 hours)
- Ruggedization design identification (75 hours plus subcontractor contributions)
- SuperSwift XT CAD design (115 hours)
- CFD tests (5 hours oversight + graduate RA support)
- Wind tunnel tests (5 hours oversight + RA + 20 hours analysis at BST)

### Work Package 3: Sensor Suite Integration
- Mass spectrometer/pump/gas sensor trade study (55 hours)
- External interface design for trace gas/particulate sensors (110 hours)
- Nose cone scoop modification design with CFD (5 hours oversight + RA)
- Internal assembly/scaffold design (30 hours)

### Work Package 4: Flight Planning & Certification
- Test site review and selection (1 hour CU + 40 hours BST total) - Alamosa County, Colorado (7,500-14,000+ ft elevation)
- FAA COA preparation and submission (20 hours)
- NASA AFSRB and FRRB documentation planning

### Work Package 5: Solution Specification & Phase II Planning
- System specification documentation (25 hours)
- Risk identification and mitigation planning (30 hours)
- Phase II implementation plan (30 hours)
- Final report (50 hours)

## Notable Details

### Company Experience & Heritage
- **PI (Dr. Jack S. Elston):** CEO/co-founder of BST; Ph.D. work on Tempest sUAS for VORTEX2 project (first sUAS intercept of tornadic supercell, May 2010); 300+ flight experiments including Arctic deployments; 100+ COA applications authored
- **Team expertise:** Complex atmospheric sampling, severe weather operations, multi-aircraft coordination, FAA/NASA regulatory navigation
- **Related work:** Energy-Aware Aerial Systems (AFRL), AVIATE (2013, Aeroprobe multi-hole probe integration)

### Subcontractors & Partners
- **University of Colorado Boulder (RECUV):** Wind tunnel testing, CFD analysis, FAA approval coordination
- **Arapahoe SciTech:** Sensor mounting requirements, dropsonde design expertise for ash plume penetration
- **Dr. Lois J. Wardell:** Dropsondes and harsh environment sensor experience

### Test Site Selection
- **Alamosa County, Colorado** (already has BST FAA COA approval)
- Mountainous terrain elevation: 7,500 ft to 14,000+ ft
- Beneficial for validating high-altitude capabilities
- Reduces FAA approval timeline risk for Phase II

### Phase II Scope (mentioned)
- Manufacture, assemble, and integrate prototype SuperSwift XT
- Flight testing in hazardous conditions with integrated sensor suite
- Validation of PTH, wind, particulate, and trace gas measurement capabilities
- Demonstration of in situ measurement capability for VATD model calibration/validation
- Field deployment and mission validation

### Competitive Position
- **Cost advantage:** sUAS more economical than manned or large UAS; loss-acceptable for high-risk missions
- **Unique capability:** Purpose-designed platform vs. adapted general-purpose systems
- **Flexibility:** Modular payload system enables mission versatility beyond volcanic sampling
- **Maturity:** Built on proven SuperSwift and SwiftCore heritage with extensive field validation

### NASA Mission Alignment
- Addresses goal to "enhance performance and utility of NASA's airborne science fleet"
- Supports aviation safety through VATD model improvement
- Fills data gap in volcanic ash sampling (particle properties, ash concentration, altitude, temporal variability)
- Complements satellite remote sensing and ground-based monitoring
- Enables rapid response to volcanic eruption events

### Risk Mitigation Strategies Mentioned
- Early FAA COA paperwork in Phase I to reduce Phase II schedule risk
- CFD and wind tunnel validation before prototype construction
- Subcontractor expertise to guide design decisions (CU aerodynamics, Arapahoe SciTech sensor integration)
- Field-proven base platform (SuperSwift) reduces technical risk vs. new airframe design
- Phase II implementation plan developed during Phase I to ensure design-to-build transition

---

**Document Status:** This is a Phase I proposal; proposal was not marked as awarded or rejected in available metadata. Proposal S3.04-8077 appears to be from the 2016 NASA SBIR volcano monitoring solicitation.