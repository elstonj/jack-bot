# Cooperative Wind Sensing SBIR Phase II Proposal

## Document Metadata
- Type: SBIR Phase II Proposal
- Client/Agency: NASA
- Program/Solicitation: NASA SBIR S3.04 Subtopic - "Advanced Technologies for Coordinated In-Situ Atmospheric Sensing"
- Date: Submitted 2014-12-19 (proposal period covers 22 months of Phase II work)
- BST Products/Systems Referenced: Apollo aircraft, SwiftPilot autopilot, Black Swift Flight Management System (FMS), SwiftTab user interface, CAPS Multi-hole Probe (MHP), iMet PTH sensors
- Key Personnel: Dr. Jack S. Elston (PI), Prof. Brian Argrow, Prof. Dale Lawrence, Coby Leuschke (Rocketship Systems Inc.), Dr. Cory Dixon, Dr. Maciej Stachura

## Executive Summary
Black Swift Technologies proposes to develop the Coordinated Atmospheric Profiling System (CAPS), a commercial, turn-key multi-aircraft unmanned system for synchronized atmospheric data collection. Building on Phase I prototype work, Phase II will integrate the Apollo aircraft, custom wind/temperature/humidity sensors, autonomous coordination algorithms, and mesh networking into a fieldable system capable of performing volumetric atmospheric measurements—enabling new measurement strategies impossible with single aircraft or ground-based instruments.

## Technical Approach

### Core System Architecture
CAPS consists of:
- **Platform**: Modified Apollo aircraft (two wing variants: 54-inch span for baseline operations, 102-inch span for high-altitude/volcanic operations)
- **Flight Management**: Black Swift Flight Management System (FMS) featuring SwiftPilot autopilot with CAN bus modularity and Linux-based payload computer for autonomous operations
- **Sensors**: Custom CAPS Multi-hole Probe (MHP) for 3D wind measurement; iMet PTH sensor for pressure, temperature, humidity
- **Communications**: Microhard P900 mesh radios (10 km range, up to 10 nodes) integrated into FMS
- **Control Interface**: SwiftTab (Android-based tablet) user interface for multi-vehicle command and control

### Key Technical Capabilities from Phase I
- CFD-verified aerodynamic performance for both Apollo variants
- Prototype modular payload bay with standardized mechanical/electrical/data interfaces
- Custom CAPS Multi-hole Probe design (commercial COTS solutions deemed inadequate for robustness, size, cost)
- Virtual structure-based formation flight controller validated in simulation (with identified wind-field performance issues to be addressed in Phase II)
- Radio interface boards designed and ground-tested for P900 mesh network
- Multi-vehicle simulation capability for user interface evaluation

### Phase II Development Approach
Work organized into six technical objectives with iterative flight testing milestones:

1. **Vehicle and System Integration and Testing**: Baseline CAPS integrated on modified Apollo; ground testing in simulated adverse weather (rain, cold); integration of two prototype aircraft for sensor payload and wind tunnel testing

2. **Atmospheric Sensing Verification, Test, and Evaluation**: 
   - Wind tunnel testing at NCAR to validate MHP and PTH sensor accuracy and mechanical integration
   - Flight validation at Boulder Atmospheric Observatory (BAO) tower comparing CAPS measurements to tower-mounted instruments at 0, 50, 100, 150, 200, 250, 350m altitudes and additional sodar/lidar data
   - Results inform construction of five-aircraft baseline system

3. **Coordination Algorithm Development and Testing**:
   - Modification of formation flight controller to account for wind disturbances and vehicle dynamic constraints (critical gap identified in Phase I)
   - Implementation on SwiftPilot payload computer SDK
   - Software interface and inter-nodal messaging definition
   - UI development for intuitive multi-aircraft tasking with safety checks
   - Support for three sampling methodologies: horizontal gradient, vertical gradient, volumetric (helical)

4. **Coordinated Flight Test and Evaluation**: Three aircraft simultaneously flown at Pawnee National Grasslands with two in reserve; validation of coordination algorithms, mesh network, sensor payload modularity, and system operational ease

5. **High Altitude Performance Test and Evaluation**: Five 102-inch Apollo aircraft flown in coordinated formation near Alamosa, Colorado (mountain terrain up to 14,000 ft+) to validate volcanic plume observation capability; includes mass models of volcanic payload instruments

6. **System Refinement and Completion**: Post-flight design modifications, manufacturability improvements, hardware/software optimization, packaging design, and documentation for TRL-8 commercialization

## Products & Capabilities Described

### Apollo Aircraft
- **54-inch wingspan variant**: Baseline system; waterproofed for rain operations; capable of 15m AGL with terrain-following; operates in up to 22 mph winds
- **102-inch wingspan variant**: High-altitude performance for mountain terrain and volcanic operations; enhanced payload bay (0.5 kg capacity) with removable modular nose cone
- **Performance**: Fully autonomous launch, flight, and landing from unimproved surfaces; field-assemblable without tooling
- **Proposed cost**: <$7,500 per aircraft (not including payload)

### CAPS Multi-Hole Probe (MHP)
- Custom-designed system for 3D wind measurement from sUAS (COTS solutions found inadequate)
- Features: 5 dynamic pressure sensors integrated with airframe-mounted autopilot sensors
- Prototype hardware and electronics completed in Phase I; requires wind tunnel calibration
- Proposed as standalone product for other sUAS projects
- Phase II includes algorithm refinement for inertial wind component estimation

### PTH Sensor (Pressure, Temperature, Humidity)
- iMet sensor core for temperature and humidity measurement
- Enhanced design in development during Phase I
- Protective scoop design required for flight operations
- Integrated with MHP in modular nose cone

### Black Swift Flight Management System (SwiftPilot Autopilot)
- Advanced GPS receiver with raw GLONASS constellation logging for post-processing accuracy
- Real-time positioning: ~50cm uncertainty; post-processed: <10cm in all three axes
- CAN bus interface for modularity and payload computer integration
- Linux-based payload computer enables autonomous mission scripting beyond waypoint following
- Advanced GPS/terrain-following algorithms enable 15m AGL operations
- Robust flight control for turbulent atmospheric conditions

### SwiftTab User Interface
- Android tablet-based command and control
- Multi-vehicle focus: displays vehicle health/status, map contextual information (operator-configurable to reduce clutter)
- Simulations during Phase I validated single-operator capability for multi-aircraft management
- Phase II modifications to support intuitive tasking of coordinated algorithms, gesture-based aircraft selection, and safety interlocks

### Mesh Network (Microhard P900)
- Range: 10 km aircraft-to-aircraft
- Capacity: 10 total nodes (aircraft and ground stations)
- Throughput: 115 kbps
- Expandable interface for integration into other platforms
- Custom radio interface boards designed and tested in Phase I

## Use Cases & Applications

### Primary Mission: Volcanic Emissions Monitoring
- Coordination with NASA ASTER satellite for SO₂ concentration comparison
- Vertical stacking of aircraft for plume height, ash concentration, temperature gradient characterization
- Extended payload bay for aerosol and additional gas sensors
- High-altitude mountainous operations demonstrated

### Atmospheric Science Applications
- **Boundary Layer Studies**: Measurement of atmospheric thermodynamics, turbulence characterization
- **Air Quality**: Identification and characterization of gas leaks, pollution transport
- **Climate/Ecology**: Non-anthropogenic gas monitoring (e.g., tundra thaw emissions)
- **Flux Measurements**: Distributed measurement enabling real-time spatial gradient determination (horizontal, vertical, volumetric)
- **Weather Prediction**: High-fidelity targeted data to improve model parameterizations

### Prior Research Context
- Team experience with previous sUAS platforms: DataHawk, SUMO, Tempest, NexSTAR
- Demonstrated capability in: mid-latitude/arctic boundary layers, convective boundary layers, orographic effects, wind energy, severe storm sampling
- Access to full ABL vertical extent with fine-scale measurement resolution

## Key Results (Phase I Accomplishments)

### Aircraft Development
- CFD-verified aerodynamic performance for 54" and 102" Apollo variants
- Design specifications met for high-wind (22 mph) and inclement weather operation
- Waterproofing completed for rain operations
- Modular payload bay prototype designed and static-tested; NASA NTR filed

### Sensor Development
- COTS multi-hole probe evaluation; determined inadequate for CAPS requirements
- Custom CAPS MHP designed and hardware/electronics prototyped
- Comprehensive COTS sensor evaluation for wind, pressure, temperature, humidity measurement
- PTH sensor core (iMet) selected; enhanced design underway

### Coordination Algorithms
- Formation flight controller implemented and validated in simulation for vertical and horizontal formations
- **Key finding**: Identified critical gap—most published cooperative control algorithms fail to account for wind disturbances; formation controller does not explicitly account for vehicle dynamic constraints
- Simulation infrastructure established for continued algorithm development

### Communications
- Five radio systems evaluated against requirements
- Microhard P900 selected as optimal solution
- Custom radio interface boards designed and ground-tested
- Simulations confirmed range requirements

### User Interface
- SwiftTab multi-vehicle simulation identified key UI improvements needed
- Single-vehicle-centric design paradigm replaced with multi-vehicle capability visualization
- Demonstrated feasibility of single-operator multi-aircraft management in simulation

## Notable Details

### Competitive Differentiation
- **No commercial turn-key system exists** for integrated multi-aircraft coordination with autopilot, networking, and payload integration
- Research systems have demonstrated multi-aircraft flight, but none commercialized with operational simplicity focus
- Team possesses **unique FAA/NAS multi-aircraft operations experience**
- Prior commercialization track record: BST self-funded for 2 years on avionics/GCS sales; ongoing commercialization of Black Swift FMS

### Organizational Experience
- **CU Boulder collaboration**: Prof. Brian Argrow (aerodynamics), Prof. Dale Lawrence (coordination algorithms), Dr. Maciej Stachura (atmospheric science flight operations)
- **Rocketship Systems Inc. (RSI) subcontract**: Coby Leuschke (Apollo airframe design, manufacturing, integration)
- **NCAR partnership**: Wind tunnel facilities and atmospheric sensor expertise; NCAR soil moisture mapping sUAS currently in development with NASA

### Modular Approach
- Standardized mechanical, electrical, and data interfaces enable payload reconfiguration
- FMS/autopilot hardware installable on pre-existing platforms
- Multiple coordination schemes implementable (formation flight and others)
- Modular nose cone field-swappable without tooling

### Market Positioning
- **Cost focus**: Designed to minimize total system cost (capital, maintenance, training, operational robustness)
- **Target users**: Budget-constrained researchers, commercial entities, federal agencies (beyond NASA)
- **Commercialization strategy**: Phase II completion targets TRL-8 for sale to early adopters; plans to commercialize MHP as standalone product

### Technical Risks Identified and Addressed
- **Wind algorithm performance**: Phase I simulations revealed coordination algorithms degrade in strong winds; Phase II addresses this with explicit wind accounting and dynamic constraint inclusion
- **Sensor accuracy**: Prototype MHP to undergo NCAR wind tunnel validation and BAO tower comparison flights
- **Multi-aircraft operational safety**: SwiftTab UI design includes safety interlocks and checks to prevent unsafe commanding

### Testing Plan
- **BAO Tower (Colorado)**: Sensor validation and comparison with tower instruments (0-350m altitude range)
- **Pawnee National Grasslands (Colorado)**: Multi-aircraft coordination algorithm validation; three aircraft + two reserves
- **Alamosa, Colorado (mountain terrain)**: High-altitude operations validation with 102" Apollo variant
- Each test site requires separate FAA Certificate of Airworthiness and NASA flight approval

### Deliverables
- Fully integrated CAPS system (5x 54" Apollo or 5x 102" Apollo)
- Complete system documentation and user manuals
- Flight operation procedures and safety protocols
- Algorithm source code and software interfaces
- Hardware designs (Apollo, MHP, nose cone) suitable for manufacturing
- Technical reports from each flight test campaign

## Financial/Business Context
- Phase II proposal (no specific budget stated in extracted content)
- 22-month period of performance
- Key personnel allocation: PI ~450 hours project management/oversight; Prof. Argrow, Prof. Lawrence, Dr. Dixon, Dr. Stachura allocated for specific technical tasks
- Subcontractor support from RSI (Coby Leuschke ~400+ hours) and CU graduate/undergraduate research assistants

---

**Document Status**: Proposal appears complete; document extraction cuts off during description of Task 5.