# Dynamic Soaring for Persistent Venus Upper Atmosphere Observations

## Document Metadata
- **Type:** NASA SBIR Phase I Proposal
- **Client/Agency:** NASA
- **Program/Solicitation:** SBIR 2018-I, Topic S3.05-2693
- **Date:** Submitted February 9, 2018
- **BST Products/Systems Referenced:** SwiftCore Flight Management System, SwiftPilot autopilot, SwiftStation ground station, SwiftTab tablet interface, S2 UAS
- **Key Personnel:** 
  - Dr. Jack S. Elston (Principal Investigator, CEO/co-founder)
  - Dr. Maciej Stachura (Lead Engineer, CTO)
  - Joshua Fromm (Aircraft Design and Integration)
  - Dana Turse (Roccor subcontractor, Director of HSC R&D Programs)

## Executive Summary

Black Swift Technologies proposes a deployable unmanned aircraft system (UAS) based on dynamic soaring principles to enable persistent observation of Venus's upper atmosphere (50-60 km altitude). The design leverages proven dynamic soaring techniques—used by seabirds and high-speed aircraft—to extract energy from atmospheric wind shear, eliminating the need for large propulsion systems. Up to eight 4.3-meter wingspan gliders (<10 kg each) can be packaged within a standard Venus aeroshell, enabling long-duration missions even on the planet's dark side while continuously sampling atmospheric composition.

## Technical Approach

**Core Concept:** The proposal employs dynamic soaring—extracting energy from wind shear gradients—rather than conventional propulsion or solar power systems. Key advantages:

1. **Energy Harvesting:** Instead of battling Venus's ~100 m/s stratospheric winds, the aircraft leverage atmospheric shear layers (particularly at cloud interfaces and above topography) to maintain altitude indefinitely while performing targeted sampling
2. **Dark Side Operation:** Unlike solar-powered competitors, dynamic soaring provides energy independent of sunlight, allowing continuous operation around Venus's 4-day rotation
3. **Compact Deployment:** Deployable high-strain composite (HSC) wings fold into extremely compact packages within aeroshell constraints

**Technical Execution Strategy:**

- **Atmospheric Modeling (Task 2.0):** Integrate Venus atmospheric data from Venera probes (vertical/horizontal wind profiles, temperature, pressure) into BST's Gazebo-based simulation environment to model conditions at 50-60 km altitude
- **Flight Simulation (Task 3.0):** Implement autonomous dynamic soaring algorithms in simulation; test robustness across expected atmospheric variation ranges; demonstrate sustained flight and directional navigation capability toward targeted sampling locations
- **Deployable Aircraft Design (Task 4.0):** Roccor develops z-folded wing architecture using "dog-bone" tape-spring hinges (high-strain composite technology); prototype fabrication and bench-top structural testing
- **Material Selection (Task 4.3):** Trade study of composite matrices resistant to Venus's corrosive atmosphere (SO₂, H₂SO₄); candidates include Cyanate Ester, Polyimide, and Viton barrier coatings

## Products & Capabilities Described

### SwiftCore Flight Management System
- **What it is:** BST's integrated avionics architecture including SwiftPilot autopilot, SwiftStation ground station, SwiftTab tablet interface
- **Proposed Use:** Baseline autopilot for Phase II field testing; will execute dynamic soaring control algorithms; noted as COTS solution for testing (Venus-rated version not scope of this SBIR)
- **Capabilities:** Supports autonomous soaring missions, tested in extreme environments (hurricanes, severe storms, volcanic plumes)

### Proposed Venus UAS ("Venus Flytrap")
- **What it is:** Deployable fixed-wing glider, 4.3 m wingspan when deployed, <10 kg total mass including instruments and communications
- **Deployment Architecture:** 
  - Folds via z-fold hinges at two points per wing
  - Uses high-strain composite tape-spring hinges (Roccor technology)
  - Multiple aircraft nest in Pioneer aeroshell perimeter (8 units fit with volume remaining for avionics/instruments)
- **Performance Specifications:**
  - Operates at 50-60 km altitude on Venus
  - Designed to fly faster than local wind speeds (~100 m/s) while harvesting energy via dynamic soaring
  - Profiles above/through cloud tops during flight path maneuvers
  - Can coordinate with other deployed aircraft to locate optimal updraft regions
- **Key Innovation:** Rigid deployable structure (vs. inflatables) enables rapid deployment (<seconds) via simple mechanisms proven on Earth tube-launched UAS over hurricanes

### High-Strain Composite (HSC) Deployable Technology
- **What it is:** Roccor's proprietary tape-spring hinge technology using "dog-bone" cut patterns in hollow composite tubes
- **Specifications:**
  - Allows 180° bends with flattening and rolling into coils for extreme packaging efficiency
  - Naturally compliant to misalignments when folded; single-part "solid state" design
  - Can withstand up to 5% strain during deployment
  - Roccor currently delivering >2,000 units for satellite solar array deployment
- **Proposed Use:** Wing and tail deployment mechanisms for Venus UAS

## Use Cases & Applications

### Primary Mission: Venus Upper Atmosphere Observation
- **Target Altitude:** 50-60 km (above cloud tops)
- **Sampling Type:** Targeted profiling through atmospheric layers while continuously soaring
- **Mission Duration:** Persistent (potentially many planetary rotations) due to energy harvesting
- **Science Objectives:** Exploit dynamic soaring flight paths to combine energy extraction with routine sampling missions
- **Scalability:** 
  - Single Pioneer aeroshell: up to 8 aircraft (technology demonstration scale)
  - Pathfinder/Flagship missions: can include 1-2 aircraft as secondary payloads on dirigible/balloon-primary missions

### Secondary Commercialization Applications (Earth-based)
1. **Hurricane Sampling:** Replace short-duration GPS dropsondes and Coyote air-deployed UAS with longer-endurance deployable aircraft; larger payload capacity
2. **Severe Storm Penetration:** BST has extensive VORTEX2 and supercell experience; soaring algorithms extend flight duration for day/night storm profiling
3. **Volcanic Plume Monitoring:** Corrosion-resistant design enables extended SO₂/toxic gas sampling near active volcanoes (BST conducted field campaign in 2018)

## Key Technical Challenges Addressed

### Challenge 1: Energy Supply on Dark Side
- **Problem:** Venus rotates every 243 days (every 4 Venus days = 360 hours); planet circles every ~90 hours at cloud-top wind speeds
- **Solution:** Dynamic soaring provides propulsive power; solar energy on light side charges batteries for control surface actuation on dark side; eliminates need for sealed electric propulsion (difficult to protect from corrosive atmosphere)

### Challenge 2: Packaging High-Aspect-Ratio Glider in Aeroshell
- **Problem:** Efficient dynamic soaring requires large wing area; standard aeroshells are highly volume-constrained
- **Solution:** HSC tape-spring hinges enable z-fold deployment; rigid structure maintains aerodynamic performance post-deployment (unlike inflatable dirigibles)

### Challenge 3: Atmospheric Corrosion (SO₂, H₂SO₄)
- **Problem:** Epoxy composite matrices degrade in sulfuric acid; electronics and motors difficult to seal
- **Solution:** 
  - Trade study of alternative matrix materials (Cyanate Ester, Polyimide)
  - Viton barrier films/coatings
  - Propulsion-less design simplifies sealing vs. motor-driven competitors

### Challenge 4: Navigation and Sampling in High Winds
- **Problem:** Sustained 100 m/s winds make conventional sampling difficult
- **Solution:** Flight path algorithms combine dynamic soaring cycles to incrementally change position; intelligent path following toward targeted surface locations; profiling achieved during energy-harvesting maneuvers

## Phase I Work Plan (6 Months)

**Task 1 - Preliminary Work:**
- Kickoff meeting (4 hours prep + meeting)
- Requirements document from literature review (90 person-hours across team)
- Project management (104 hours, Dr. Elston)

**Task 2 - Venus Atmospheric Model Development:**
- Examine Venera probe data; generate parameter tables (60 hours, Dr. Elston)
- Build full atmospheric model in BST Gazebo environment (60 hours, Dr. Elston)

**Task 3 - Simulation Creation and Flight Algorithms:**
- Develop Venus-adapted UAS aerodynamic model (80 hours each, Dr. Stachura & Fromm)
- Implement dynamic soaring algorithms in simulation (80 hours, Dr. Elston)
- Conduct extensive persistent-flight simulations with algorithm iteration (100 hours, Dr. Elston)

**Task 4 - Deployable Aircraft Development:**
- Preliminary design concepts for deployable wings (36 person-hours across team)
- Structural analysis and prototype fabrication (56 person-hours across team including Roccor)
- Material/corrosion survey and risk mitigation (22 person-hours)

**Task 5 - Solution Specification:**
- Integrate hinges into BST-provided aircraft; static load testing (47 person-hours)
- Phase II implementation plan with Earth analog testing identification (50 hours)
- Final report compilation (100 person-hours)

**Total BST Effort:** ~1,450 person-hours across team
**Roccor Subcontract:** $29,978.02 (40 hours over 6 months)

## Key Results (Reports/Findings)

Not a results report—this is a forward-looking proposal. However, it documents:

1. **State-of-Art Comparison:** Only one prior heavier-than-air Venus aircraft proposed (Landis et al., 2001-2003); that design relied on solar propulsion and could not sustain dark-side flight. This proposal's dynamic soaring approach is novel for Venus planetary exploration.

2. **Earth Analog Validation:** BST's published research demonstrates autonomous soaring algorithms' feasibility:
   - Elston et al. (2014): Dynamic soaring for supercell storm observation
   - Multiple references to successful soaring algorithm deployment in heterogeneous wind fields
   - Team has 300+ flight experiments with UAS in extreme atmospheric conditions

3. **Technical Feasibility Evidence:**
   - Roccor's tape-spring hinges are flight-proven (satellite solar array deployments)
   - High-strain composites documented to 5% strain capability
   - Venus atmospheric data (Venera 7/8) available for model validation
   - Wind shear characteristics at 50-60 km altitude well-documented; analogs exist on Earth (mountain waves, cirrus cloud regions)

## Notable Details

### Commercialization Track Record
- BST completed Phase I+II soil moisture mapping SBIR (NNX14CG09C); generated $719,314 additional investment post-Phase II
- Ongoing Phase II SBIR (NNX16CP42P) for ruggedized harsh-environment UAS showing commercial success:
  - Two payloads already integrated into NASA missions
  - 3D-printed multi-hole wind probe sensor: 10x cost reduction vs. legacy instruments; informal pre-orders for 10 units
- Demonstrates pathway from SBIR to commercial deployment

### Facilities & Testing Infrastructure
- 1,600 sq ft Boulder, CO headquarters with full prototyping/electrical integration capability
- Access to multiple test sites:
  - Local fenced field (10 min from office)
  - Pawnee National Grasslands (20×20 mile area)
  - San Luis Valley (high-altitude testing up to 15,000 ft MSL, peaks >14,000 ft; planned primary Phase II site for dynamic soaring)
- 6 successful NASA Airworthiness Flight Safety Review Board (AFSRB) and Flight Readiness Review (FRRB) approvals; leading NASA UAS partner
- Full simulation environment: Gazebo-based atmospheric modeling with hooks for customization

### Partnership Structure
- **Roccor LLC** (subcontractor): Dana Turse as PI/PM for HSC deployable work
  - 15+ years composite design/material development experience
  - Patent-holder in deployable structures (slit-tube beams, antenna reflectors)
  - Currently contracted by satellite constellation for 2,000+ composite hinged booms

### Phase II Vision
**Highest-Risk Mitigation Areas:**
1. **Deployable Aircraft Reliability:**