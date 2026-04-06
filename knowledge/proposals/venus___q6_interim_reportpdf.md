# Dynamic Soaring for Persistent Venus Upper Atmosphere Observations

## Document Metadata
- **Type:** NASA SBIR Phase II Interim Report
- **Client/Agency:** NASA (NSSC - NASA Glenn Research Center)
- **Program/Solicitation:** NASA SBIR 2018, Topic NNH18C.1
- **Date:** February 28, 2020
- **Contract Number:** 80NSSC19C0181
- **BST Products/Systems Referenced:** Graecalis (Earth analog aircraft), S2 (mentioned in context of previous BST experience)
- **Key Personnel:** 
  - Jack Elston (PI, Black Swift Technologies)
  - Maciej Stachura (Lead Engineer, BST)
  - Ben Busby (Simulation Development, BST)
  - Mark Bullock (Venus Atmospheric Science, Science and Technology Corp.)
  - Nick Jenkins (Aircraft Modeling and Simulation)

## Executive Summary
This Phase II interim report describes BST's development of a dynamic soaring-based unmanned aircraft system (UAS) for persistent observations in Venus's upper atmosphere. The system uses proven energy-harvesting flight techniques to operate in the harsh Venusian environment without traditional propulsion, with up to eight aircraft deployable from a Pioneer aeroshell. Phase II focuses on high-fidelity simulation, autonomous soaring demonstration on Earth, deployable wing development, and design of a Venus-suitable aircraft capable of sampling atmospheric chemistry while extracting energy from wind shear.

## Technical Approach

### Core Innovation
Dynamic soaring—extracting energy from atmospheric wind shear—provides the primary propulsive mechanism. This approach has been validated by nature (albatrosses, petrels) and human achievements (fastest radio-controlled aircraft). For Venus, it eliminates the need for sealed propulsion systems vulnerable to corrosive sulfuric acid clouds.

### Key Technical Objectives
1. **High-fidelity simulation:** Integrate Venus atmospheric models (from General Circulation Models and mesoscale models) into Gazebo simulation with 6DOF aircraft dynamics backed by CFD
2. **Dynamic soaring controller development:** Mature Phase I algorithms for autonomous energy harvesting without a priori knowledge of wind-relative position/orientation
3. **Earth demonstration:** Autonomous dynamic soaring flight tests using the Graecalis prototype with validated algorithms
4. **Deployable UAS for Earth testing:** Build and flight-test a prototype with foldable wings suitable for aeroshell deployment
5. **Venus-environment design:** Develop materials and mechanisms for corrosive atmosphere survival, power generation, and deployment

### Simulation Environment
- **Modular ecosystem** allowing switching between multiple Venus atmospheric models
- **Integration points:**
  - Sebastien Lebonnois IPSL General Circulation Model (GCM)
  - UCLA GCM (H. Parrish)
  - AFES Venus GCM (H. Ando, Kyoto Sangyo)
  - WRF-LES models (M. Lefevre and M. Yamamoto)
  - VeGa-PDS balloon traverse data (1986)
- **Gazebo-based 3D flight simulation** with Earth and Venus wind models integrated as plugins
- **CFD analysis** (Euler/panel methods) for 6DOF aerodynamic database at varying attitudes, control deflections, airspeeds
- **Venus-GRAM RESTful API** deployed at https://atmosphere.bst.aero for atmospheric queries by latitude/longitude/altitude

### Materials & Corrosion Mitigation
Phase I discovered that carbon composite materials cured with chemically-resistant barrier films survive sulfuric acid exposure at BST's Roccor subcontractor facility. Phase II continues testing to:
- Monitor mass loss rates of exposed samples
- Assess post-exposure stiffness
- Apply barrier film technique to complex wing structures

### Structural Scaling & Aeroelastic Testing
Dimensional analysis demonstrates Earth flight tests can validate Venus structural integrity using **density-paired altitudes**:
- Match dynamic pressure by flying at consistent velocities at density-equivalent altitudes
- Inertia ratio (aircraft mass vs. fluid mass) identical at density-paired conditions
- Reduced frequency of elastic modes identical at consistent velocities
- Mach and Reynolds numbers remain similar order-of-magnitude (compressibility/viscosity effects expected negligible)
- Small Froude number differences (6%) not critical for aeroelastic modes

This approach enables validation without aircraft modifications.

## Products & Capabilities Described

### Graecalis Aircraft (Earth Analog)
- **Type:** High-aspect-ratio glider designed for autonomous dynamic soaring
- **Configuration:** Fixed-wing UAS with deployable wing sections
- **Baseline design:** Similar aerodynamic design to be scaled for 10 kg Venus payload
- **Deployment:** Multi-hinged wing sections fold for stowage in Pioneer aeroshell
- **Instrumentation:** Autopilot with telemetry logging of attitude, airspeed, control inputs, sounding data
- **Phase I achievement:** Full-scale wing with fold-and-deploy capability demonstrated; composite barrier film viability proven

### Venus Aircraft (Conceptual Design)
- **Target payload:** 10 kg atmospheric sampling instruments
- **Configuration:** High-aspect-ratio glider optimized for dynamic soaring
- **Scaling:** Up to 8 aircraft fit in Pioneer aeroshell ("Venus Flytrap" deployment scheme)
- **Deployment mechanism:** Folding wing sets with breakaway hinges from aeroshell
- **Structural materials:** Carbon composites with sulfuric-acid-resistant barrier films
- **Power generation options under study:**
  - Solar panels for day-side charging/emergency propulsion
  - External wind turbine for night-side/cloudy-period electricity generation
  - Propulsion system trade-off analysis (mass penalty vs. mission flexibility)
- **Flight control:** Autonomous dynamic soaring algorithms with no ground-relative orientation requirement
- **Localization:** Position estimation methods based on interplanetary mission heritage for science data tagging

### Autopilot System
- **Capability:** BST-developed autopilot infrastructure for dynamic soaring algorithm implementation
- **Testing:** Hardware-in-the-loop (HWIL) validation in Gazebo before flight
- **Dynamic soaring modes:** 
  - Energy harvesting without a priori wind knowledge
  - Relative soaring techniques for Venus (no station-keeping possible)
  - Large altitude change sampling schemes (identified in Phase I as high-value for atmospheric profiling)
  - Latitudinal transit capabilities

## Use Cases & Applications

### Primary Mission: Venus Upper Atmosphere Observations
- **Altitude range:** Cloud-top region (~48-65 km), where Venus Flytrap can be deployed from entry vehicle
- **Mission duration:** Days of continuous sampling with altitude and latitudinal range capability
- **Science objectives:** In situ atmospheric sampling (chemistry, physics, aerosols)
- **Advantages over alternatives:**
  - **vs. Dirigibles/Balloons:** Dynamic soaring provides active control and persistent sampling without gas replenishment or buoyancy management in extreme winds
  - **vs. Solar-powered aircraft:** No sealed propulsion needed (eliminates corrosion vulnerability); energy extracted continuously from wind shear regardless of day/night/cloud cover

### Scaling Scenarios
- **Technology Demonstration:** Single Venus Flytrap (up to 8 aircraft)
- **Pathfinder Mission:** Venus Flytrap as primary payload
- **Flagship Mission:** Venus Flytrap with secondary deployment capability alongside primary dirigible/balloon payloads
- **Redundancy/Coordination:** Multiple aircraft enable different sensor suites, cross-platform data sharing to optimize soaring regions, fault tolerance

### Secondary NASA Applications (Earth)
- **Hurricane sampling:** Autonomous soaring in severe convective conditions
- **Severe storm observation:** Long-endurance sampling at altitude
- **Volcanic plume monitoring:** Persistent observations of emissions

### Non-NASA Applications
- **NOAA:** Hurricane and fire weather observations
- **USGS:** Volcanic emission characterization

## Key Results (Phase II Interim Status)

### Completed Technical Activities

#### 1. Venus Atmospheric Model Integration
- **GCM data acquisition:** Coordination with Sebastien Lebonnois (IPSL) for high-resolution circulation model wind fields
- **Mesoscale model evaluation:** WRF-LES variants assessed for turbulence representation
- **Historical data:** VeGa-1986 balloon traverse data (48 hours per balloon, pressure, temperature, humidity, winds, backscatter) integrated
- **API deployment:** Venus-GRAM RESTful service live at atmosphere.bst.aero; supports JSON queries with temperature, density, pressure, wind (u, v, w) responses

#### 2. Atmospheric Model Integration to JSBSim/Gazebo
- **Venus-GRAM API:** Modified FORTRAN code for network compatibility; outputs consolidated to single location; concurrent request handling via unique ID assignment
- **Plugin architecture:** Standardized interface for rapid wind model import (Earth ridge soaring, jet stream, hurricane analogs; Venus models)

#### 3. Structural/Aeroelastic Analysis
- **Key finding:** Earth flight tests at density-paired altitudes validate Venus structural integrity without modification
- **Verification approach:** Modal ground testing (baseline, post-sine, post-flight); hinge deployment validation; high-load-factor maneuvers; flutter margin demonstration
- **Physics scaling:** Dimensionless analysis confirms dynamic pressure, inertia ratio, reduced frequency, Mach/Reynolds all consistent between density-paired Earth/Venus altitudes
- **Material validation:** Initial sintering of composite barrier films in sulfuric acid vapor showed "extremely low mass loss" rates (Phase I baseline)

#### 4. Deployable Wing Development (Phase I Foundation)
- **Roccor subcontractor:** Full-scale wing section demonstrated fold-deploy-fold repeatability
- **Barrier film application:** Carbon composite samples cured with sulfuric-acid-resistant films; Phase II continuation with more complex geometries

### Planned Phase II Milestones

1. **High-fidelity simulation environment operational** with Venus GCM/mesoscale data, Earth wind analogs, 6DOF aircraft model
2. **Autonomous dynamic soaring flight test** on Earth (under FAA Part 107) demonstrating sustained, indefinite energy-harvesting flight
3. **Deployable wing prototype for Earth testing** constructed by Roccor, passing lab deployment/torque tests and flight validation
4. **Venus aircraft aerodynamic design finalized** using CFD/simulation optimization for 10 kg payload scaling
5. **Material catalog for Venus environment** with mass-loss/stiffness data; final barrier film application process defined
6. **System documentation** including schematics, wiring, UI features, supporting calculations

### Performance Expectations
- **Energy surplus:** Phase I simulations indicated atmosphere provides excess energy for flight, allowing turbine-based electrical generation rather than speed increase
- **Night-side operation:** Battery charging from day-side solar can sustain night-side traversal; turbine provides alternate power regardless of illumination/cloud density
- **Sampling capability:** Autonomous algorithms support large altitude changes (identified as high-value for atmospheric profiling) and latitudinal transit during mission

## Notable Details

### Partnership & Collaboration
- **Roccor (subcontractor):** Wing deployment mechanisms, composite fabrication, 3D scanning (Faro Arm), laboratory testing (deployment, torque, corrosion exposure)
- **Science & Technology Corp. (Mark Bullock):** Venus atmospheric science expertise, circulation model interpretation
- **Nick Jenkins:** CFD modeling, 6DOF flight mechanics validation
- **Sebastien Lebonnois (IPSL, external):** General circulation model data provision
- **NASA advisors:** Mike Pauken (JPL)
- **NASA contracting:** Helen Roberson (NSSC COR), Bruce Cogan (AFRC COR)

### Deployment Architecture
- **Pioneer aeroshell:** Standard vehicle; houses up to 8 folded aircraft plus parachute descent system
- **Nomenclature:** "Venus Flytrap" - colloquial name for multi-aircraft deployment concept
- **Deployment scheme:** Conceptual design phase; full aeroshell dynamics simulation planned as Phase II stretch goal

### Competitive Positioning
- **Unique advantages:**
  1. **No sealed propulsion:** Eliminates motor/propeller sealing complexity against sulfuric acid
  2. **Day/night operation:** Energy harvesting + battery/turbine alternatives
  3. **Scalability:** 1-8 aircraft fit in standard aeroshell; variable payload/redundancy
  4. **Earth validation path:** Dynamic soaring algorithms proven on Earth before Venus deployment
  5. **Leverages existing BST autopilot infrastructure**

### Risk Mitigation Strategies Identified
- **Aeroelastic validation:** Earth flight testing at density-paired altitudes eliminates need for Venus-scale prototyping before deployment