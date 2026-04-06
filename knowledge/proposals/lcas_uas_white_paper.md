# LCAS UAS White Paper

## Document Metadata
- **Type:** White Paper / SBIR Project Proposal
- **Client/Agency:** Air Force Research Office (ARO) - mentioned as Phase II delivery recipient
- **Program/Solicitation:** SBIR (Small Business Innovation Research) implied
- **Date:** Created December 7, 2012; Modified February 16, 2013
- **BST Products/Systems Referenced:** SwiftPilot avionics, Black Swift Technologies sUAS platform
- **Key Personnel:** 
  - Dale Lawrence (BST, founding member of RECUV, DataHawk principal developer)
  - Ben Balsley (University of Colorado, Cooperative Institute for Environmental Sciences, DataHawk science director)
  - Partnership with Rocketship Systems for airframe manufacturing

## Executive Summary
Black Swift Technologies proposes to develop a commercial Low Cost Atmospheric Sampling System (LCAS) based on the successful DataHawk prototype, designed to revolutionize in-situ atmospheric boundary layer measurement through a small unmanned aircraft system (sUAS) that combines low cost, ease of operation, and high-resolution sensing capabilities. The system aims to provide cost-competitive alternatives to radiosondes while enabling single-operator deployment of multi-vehicle flocks for unprecedented atmospheric sampling resolution and coverage.

## Technical Approach

### Core Design Philosophy
- **Cost as driving requirement** throughout integrated design process (ground station, vehicle, sensors, operations, training)
- **Modular design approach** with standardized common elements and application-specific interchangeable components
- Optimization for **low-thrust, long-duration flight** at low airspeeds (vs. high-thrust hobby aircraft designs)
- **Simplified field operations** prioritizing minimal ground support equipment and single-operator deployment

### Key Technical Innovations Required

**Simplified Field Operations:**
- Highly portable with minimal ground support equipment
- Rugged, easily deployable/recoverable vehicles (launch and land virtually anywhere)
- Single science operator capable of launch/flight control/landing with minimal UAS training
- Gust-insensitive vehicles for adverse weather operations
- Small, inexpensive, "attritable" vehicles reducing operations planning burden

**High-Resolution Sensors:**
- Sub-meter-scale spatial resolution from moving vehicle requiring high temporal resolution
- Sensors must withstand rough field launch/landing, vibration, and large temperature excursions over ABL altitude range
- Extremely low-noise sensors with wide dynamic range to detect small-scale variations in presence of airspeed/temperature changes
- Small, lightweight, low-power, low-cost custom-developed sensors (off-the-shelf unsuitable)

**Increased Vertical Range:**
- Sustained ascent rates ~1 m/s for >60 minutes enabling high-resolution vertical profiling
- Ground launch ceiling: 3 km AGL minimum
- Balloon-drop capability to 9 km+ (DataHawk demonstrated to 9 km)
- Shift from high-thrust/low-duration to low-thrust/long-duration propulsion designs

**Multi-Vehicle Operation:**
- Enable "flocks" of multiple vehicles for simultaneous spatially-distributed or sequential sampling
- Single science operator management of multi-vehicle system
- Coordination methods enabling commercial product viability

### System Architecture Components

**Avionics:**
- SwiftPilot autopilot system (modified for atmospheric sampling missions)
- High-volume manufacturing selection to avoid obsolescence
- Electrical interfaces between autopilot and sensors

**Electrical Power System:**
- Common power regulation and distribution for propulsion and avionics
- Electric propulsion preferred over chemical combustion
- 12V DC operation capability for remote locations

**Ground Station:**
- Low-cost tablet computers (widely-available commercial) for cost control and obsolescence avoidance
- Standard USB interface supporting various antenna options
- Modular software with flexibility for operating, guidance, control, and sensing functions
- Multi-aircraft monitoring and command capability

**Airframe:**
- Expanded polypropylene (EPP) foam construction preferred (safety, durability, sensor mounting flexibility)
- Gust-insensitive designs prioritized
- Compact breakdown capability for transport/storage
- Standardized design principles enabling common materials, construction techniques, components, tools
- Modular electrical propulsion system with standard rear mounting, propeller adaptor

**Communication Subsystem:**
- Variable per application, operating modes, data rates, radio range requirements
- Support for various commercial radio and custom/commercial antenna options
- Radio selection to be determined during design phase

**Sensor Suite:**
- Several standard interface types supported with appropriate data acquisition rates
- Options for on-board storage and/or real-time telemetry
- Custom development of sensors tailored to sUAS atmospheric measurement requirements

## Products & Capabilities Described

### LCAS sUAS System (Proposed Commercial Product)
**What it is:** A low-cost, highly portable small unmanned aircraft system designed for atmospheric boundary layer sampling, based on DataHawk prototype with upgraded ground station, avionics, and reduced manufacturing costs.

**Proposed use context:** 
- In-situ atmospheric sensing across ABL and lower troposphere
- Cost-competitive alternative to radiosondes for atmospheric sounding
- Fine-scale turbulence measurement campaigns
- Multi-vehicle coordinated atmospheric sensing

**Performance Specifications:**
- Flight speed: 10–15 m/s
- Mass: <1 kg
- Flight duration: 60–100 minutes
- Flight ceiling: 10 km MSL (balloon drop); 3 km AGL (ground launch)
- Ascent/descent rate: ±3 m/s
- Multi-vehicle capability: up to 5 aircraft from single ground station/operator
- Crew requirement: 1–2 people for setup and operation
- Ground station power: 12V DC operation for remote locations

### SwiftPilot Avionics System
**What it is:** BST's autopilot/avionics system for UAS applications.

**Capabilities:** Single and multiple vehicle control, user interface and networking protocols for multi-UAS operations.

**Application in LCAS:** To be modified for atmospheric sampling missions including sensor electrical interfaces and multi-aircraft monitoring/command interface.

### DataHawk (University of Colorado Prototype - Reference System)
**What it is:** Highly successful prototype sUAS developed at University of Colorado by Drs. Lawrence and Balsley.

**Demonstrated capabilities:** 9 km altitude (balloon-drop), atmospheric boundary layer sampling.

**Relationship to LCAS:** LCAS baseline design derived from DataHawk concept with commercialization enhancements.

## Use Cases & Applications

### Primary Applications
1. **Operational atmospheric sounding:** Twice-daily global atmospheric measurement around the world
2. **Scientific fine-scale measurement campaigns:** High-resolution boundary layer turbulence studies
3. **Convective/stable boundary layer research:** Mid-latitude and arctic stable boundary layers, convective processes
4. **Wind energy assessment:** Wind resource characterization and generation modeling
5. **Severe weather research:** Tornadic supercells and severe storm sampling (referenced Tempest system)
6. **Orographic effects studies:** Mountain/terrain-induced atmospheric phenomena
7. **Multi-scale atmospheric process characterization:** Kelvin-Helmholtz instabilities, convection, turbulent energy cascading

### Target Measurement Scales
- Horizontal: Few meters to several kilometers
- Vertical: Ground level to 3+ km (ground launch); up to 9+ km (balloon drop)

### Target Market (Phase III)
- **Initial market:** Government agencies and public entities (regulatory constraints)
  - Agencies seeking low-cost reusable alternatives to radiosondes
  - Air Force Research Office (ARO) - Phase II recipient
- **Future market:** Civilian and commercial sectors (pending FAA regulatory changes)

## Technical Requirements Addressed

### Critical Atmospheric Variables Measured
- Temperature
- Pressure
- Humidity
- Wind (magnitude and horizontal/vertical direction)
- Epsilon (turbulent energy dissipation rate)
- CT² (temperature turbulence structure constant)

**Measurement resolution requirement:** Horizontal resolution of "a very few meters at most" with even higher resolution for wind speed and temperature fluctuations to estimate turbulence parameters.

### Key Operational Requirements Addressed
- **Portability:** Minimal ground support equipment needed
- **Deployability:** Rugged vehicles capable of launch/recovery virtually anywhere
- **Operability:** Single science operator with minimal UAS training can conduct full mission
- **Durability:** Sensors withstand rough field operations, vibrations, temperature extremes
- **Weather capability:** Gust-insensitive designs enabling adverse weather operations
- **Cost control:** Design throughout production chain prioritizing affordability
- **Obsolescence avoidance:** High-volume component selection, tablet-based ground station

## Development Plan

### PHASE I (12 months)
**Objective:** Develop proof-of-concept prototype with airborne and ground station components, initial functionality and flight quality testing.

**Key Tasks:**
1. Design gust-insensitive airframe, initial flight testing, subsystem integration; verify rapid single-operator assembly/deployment
2. Atmospheric sensing subsystem design and verification:
   - Prototype sensor suite development
   - Data handling software design/simulation/testing for wind velocity, pressure, temperature, humidity, epsilon, CT²
3. SwiftPilot avionics modifications:
   - Communication subsystem radio selection
   - Electrical autopilot-sensor interfaces
   - User interface modification for multi-aircraft atmospheric sampling missions
4. Phase II test plan development with airspace permission strategy
5. Airframe, sensor, autopilot integration in prototype vehicle
6. Proof-of-concept flight testing
7. Final report: prototype system design, trade-offs, support documentation

**Deliverable:** Documented prototype system as basis for Phase II

### PHASE II (estimated 2 years)
**Objective:** Manufacture and flight test aircraft fleet; validate measurements against instrumented meteorological towers; validate multi-vehicle operational control; establish production costs suitable for Phase III commercialization.

**Key Tasks:**
1. Construction and flight testing of final aircraft design based on Phase I prototype
2. Airspace permission and operational documentation (frequencies, safety procedures enabling rapid user airspace approval in US national/restricted airspace)
3. Design refinements based on flight test results and user consultation
4. Manufacturing process refinement for low-cost assembly at 100+ vehicles/year scale
5. Sensor calibration and comparison testing with instrumented field tests
6. Documentation for operational flights, maintenance, ARO personnel training
7. Deliver 10 ready-to-operate aircraft to ARO with ground station and transport packaging
8. Phase II final report

**Deliverables:** 10-aircraft system to ARO; production-ready design and processes

### PHASE III
**Objective:** Products ready for commercialization through technology licensing to industry partners.

**Approach:**
- License technology to established manufacturers enabling volume/precision production without BST production scaling burden
- Industrial partner supply chain expertise informs support systems design (transport, operation, maintenance)
- BST provides software libraries and hardware interface definitions for value-added resellers/researchers to integrate third-party sensors (air particulate, etc.)
- Initial market focus: Public entities/government agencies (FAA regulatory environment constraint)
- Market expansion to civilian/commercial pending new FAA regulations

**Expected Outcome:** Commercial product availability through licensed manufacturers

## Key Results
No results reported (this is a proposal document, not a report). This white paper presents concept and development plan without experimental data or performance validation.

## Notable Details

### Team & Organization Structure
- **Black Swift Technologies:** Overall system integration, ground station, avionics, flight software; 30 combined years experience in sUAS atmospheric sampling beginning with University of Colorado RECUV (Research and Engineering Center for Unmanned Systems)
- **University of Colorado:** Vehicle design and sensor development leadership (Dr. Lawrence, Dr. Balsley)
- **Rocketship Systems:** Airframe manufacturing and integration expertise

### Competitive Positioning
- **Problem addressed:** Despite 15+ years of sUAS research prototypes (DataHawk, SUMO, M2AV, Tempest, NexSTAR), **no suitable commercial system exists** despite proven capabilities
- **Key gaps in existing systems:** 
  - High operational costs and training burden (typically 3+ person teams)
  - High vehicle/sensor fragility and cost
  - Limited vertical range/resolution trade-offs
  - Lack of multi-vehicle operational capabilities
  - Cost prohibitive for regular scientific/operational use
- **BST differentiation:** 
  - Cost-driven design methodology (rare in UAS industry)
  - Simplified operations (1-2 person teams vs. 3+)
  - Modular design enabling low-cost production scaling
  - Multi-vehicle coordination capability
  - High-resolution sensor suite development

### Technology Validation Basis
- Proposal builds on proven DataHawk prototype performance (9 km altitude, successful atmospheric measurement campaigns)
- References published results from multiple research sUAS platforms (Tempest