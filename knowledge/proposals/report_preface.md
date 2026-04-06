# Dynamic Soaring for Persistent Venus Upper Atmosphere Observations

## Document Metadata
- **Type:** NASA SBIR Phase I Interim Report
- **Client/Agency:** NASA
- **Program/Solicitation:** NASA SBIR 2018, Topic: Venus Upper Atmosphere Observations
- **Contract Number:** 80NSSC18P2078
- **Date:** October 2018
- **BST Products/Systems Referenced:** SwiftPilot (avionics), BST simulation environment (based on Gazebo), BST avionics
- **Key Personnel:**
  - Dr. Jack Elston (Principal Investigator)
  - Dr. Maciej Stachura (Lead Engineer)
  - Josh Fromm (Aircraft Design and Integration)
  - Dana Turse (Roccor PI/PM, Director of HSC R&D Programs)
  - Dr. Davis (Roccor)
  - Ms. Craven (Roccor)

## Executive Summary
BST proposes using dynamic soaring—a proven energy-harvesting flight technique—to enable persistent unmanned aircraft operations in Venus's harsh upper atmosphere (50-60 km altitude). The approach deploys multiple compact, high-aspect-ratio gliders from a standard aeroshell, enabling sustained atmospheric sampling without relying on batteries, solar panels, or traditional propulsion. Phase I focuses on simulating dynamic soaring feasibility on Venus, designing deployable wing structures, and identifying materials that survive the corrosive sulfuric acid/SO₂ environment.

## Technical Approach

### Core Concept
- **Flight Method:** Dynamic soaring to extract energy from atmospheric wind shear and vertical wind structures, allowing continuous operation even on Venus's dark side
- **Vehicle Configuration:** 4.3 m wingspan high-aspect-ratio deployable glider, ~10 kg total mass (including instruments and communications)
- **Deployment Scalability:** Up to 8 aircraft fit within a single Pioneer aeroshell ("Venus Flytrap"), with potential for secondary payload integration on larger missions
- **Energy Harvesting:** Uses wind-relative velocity from strong shear above cloud layer to maintain altitude and navigate, eliminating need for onboard propulsion or large battery capacity

### Technical Work Streams

**1. Venus Atmospheric Modeling (Tasks 2.1–2.2)**
- Extract atmospheric data from Pioneer and Venera probe measurements (pressure, temperature, 3D winds)
- Build physics-based model incorporating:
  - Lower gravity (vs. Earth)
  - CO₂/N₂ composition effects on viscosity and Reynolds number
  - Measured wind profiles and turbulence characteristics
- Integrate into BST's Gazebo-based simulation environment
- Model ranges of conditions to validate robustness of algorithms

**2. Simulation & Algorithm Development (Tasks 3.1–3.3)**
- Adapt baseline glider aerodynamic model for Venusian conditions (Reynolds numbers, pressures)
- Implement autonomous dynamic soaring algorithms for:
  - Persistent flight through wind shear above cloud tops
  - Targeted geographic navigation to perform sampling missions
  - Algorithm draws on published research in autonomous soaring for UAS
- Run extensive simulation suite to demonstrate sustained, persistent operations under varied atmospheric scenarios
- Test path-following algorithms to enable coordinated multi-aircraft operations

**3. Deployable Aircraft Design (Tasks 4.1–4.2)**
- **Partner:** Roccor (subcontractor specializing in High Strain Composite deployables)
- **Deployment Mechanism:** Z-fold wings at two hinge points per side using "dog-bone" tape-spring hinges cut into hollow composite tubes
- **Key Features:**
  - Strain up to 5% during fold/deployment cycle
  - Single-part solid-state hinges with no moving mechanisms
  - Low part count reduces complexity and corrosion risk
  - Allows rigid sections for control surfaces and sensor mounting
- **Tail Deployment Options:** Metallic springs or telescoping boom with strain-energy deployment
- **Result:** Compact stowage within aeroshell; rapid deployment in seconds

**4. Materials & Environmental Survivability (Task 4.3)**
- Survey alternative composite matrix materials for resistance to sulfuric acid and SO₂:
  - **Candidates:** Cyanate Ester, Polyimide, Silicone, Viton
  - Epoxy (baseline) inadequate for Venusian environment
  - Cyanate Ester and Polyimide: aromatic structures improve corrosion resistance; HSC-compatible
  - Viton: excellent SO₂/H₂SO₄ resistance but elastomeric; proposed as barrier film/layer over thermoset composite
- Phase I: Literature review and preliminary exposure testing
- Phase II: Detailed material testing under simulated Venusian chemistry

## Products & Capabilities Described

### Venus Flytrap UAS
- **Wingspan:** 4.3 m (fully deployed)
- **Mass:** ~10 kg including onboard instruments and communications
- **Capability:** Multi-aircraft swarm deployment (up to 8 per aeroshell)
- **Deployment Mode:** Compact fold fitting standard Pioneer aeroshell; deploys in seconds
- **Operational Altitude:** 50–60 km on Venus
- **Endurance:** Unlimited (energy sustained via dynamic soaring; traditional battery limitations eliminated)
- **Navigation:** Autonomous algorithms enable global mobility and targeted area sampling despite 90-hour planetary circulation

### BST Simulation Environment
- Based on open-source Gazebo platform
- Modular atmospheric model (swappable Earth/Venus conditions)
- Integrated dynamic soaring algorithm development and testing
- Supports rapid prototyping and parameter variation
- Used for Phase I feasibility validation and Phase II flight planning

### SwiftPilot Avionics
- To be used for Phase II flight testing (COTS solution for prototype; not customized for Venus in Phase I)
- Provides control surface actuation, onboard system management, and basic autonomous flight logic

## Use Cases & Applications

### Primary Use Case: Venus Upper Atmosphere Sampling
- **Region:** 50–60 km altitude (cloud-top region with dynamic atmospheric structure)
- **Science Objectives:** Vertical profiling through and above clouds; targeted area sampling enabled by geographic navigation
- **Mission Duration:** Long-endurance (months/years theoretically possible) due to energy harvesting; no battery depletion on dark side
- **Sampling Strategy:** Dynamic soaring flight paths designed to integrate sensing with energy harvesting; multi-aircraft coordination to map optimal vertical updrafts

### Secondary/Parallel NASA Applications
- **Hurricane Sampling:** Similar dynamic soaring applied to tropical cyclones; harvesting energy from wind shear
- **Severe Storm Sampling:** Updrafts in convective systems
- **Volcanic Plume Observation:** SO₂ detection; leveraging BST's prior experience flying near volcanic vents

### Non-NASA Commercial/Agency Applications
- **NOAA:** Hurricane and fire-weather observations
- **USGS:** Volcanic emissions monitoring
- **NWS:** Data assimilation for ensemble weather forecasting

## Key Results

**Phase I Interim Report Status (as of 10/27/2018):**
- **Financial Progress:** $82,296 cumulative costs; ~50% physical completion
- **Simulation:** Venus atmospheric model development underway; Gazebo integration planned
- **Hardware:** Roccor hinge prototype (tape-spring dog-bone design) demonstrated; preliminary deployment concept drafted
- **Material Survey:** Literature review scope identified; candidate materials selected for Phase II testing

**Planned Phase I Deliverables (by end of Phase I):**
1. Validated Venus atmospheric model with full wind/turbulence profiles
2. Simulation demonstrations of persistent dynamic soaring flight across range of Venusian conditions
3. Prototype deployable wing with functional hinge; static load testing
4. Risk mitigation plan for corrosive environment (material candidates vetted)
5. Phase II implementation plan including Earth analog flight test sites and protocol

## Notable Details

### Competitive Advantages
- **Unique Energy Strategy:** Dynamic soaring eliminates propulsion/large batteries (major simplification vs. prior Venus concepts)
- **Harsh Environment Resilience:** No spinning propeller to seal; rigid composite structure simpler to protect than inflatable designs
- **Scalability:** Multi-aircraft deployment enables redundancy, distributed sensing, and coordinated atmospheric mapping
- **Existing Expertise:** BST's prior work flying near volcanic plumes (SO₂ tolerance); Roccor's spaceflight-proven deployable structures (>2000 units in production for satellite constellation)

### Risk Mitigation Strategy
- **Highest Risks Addressed in Phase II:**
  1. **Deployable Reliability:** Flight testing with both rigid and deployable airframes; iterative algorithm refinement before full system test
  2. **Autonomous Soaring Validation:** Ground tests at Earth analogs (identified during Phase I) to test dynamic soaring before Venus relevance
  3. **Survivability:** Environmental chamber testing (simulated Venusian atmosphere) of exposed components; encapsulation/sealing of vulnerable electronics

### Partnership Structure
- **BST:** Overall system architecture, atmospheric modeling, simulation, autonomous flight algorithms, airframe integration, flight testing
- **Roccor:** Deployable wing design, High Strain Composite hinge fabrication, structural analysis, material survey

### Technology Transition Path
- **Phase II (if funded):** Full-scale prototype build; rigorous Earth flight testing at identified analogs; material exposure chamber validation
- **Post-Phase II:** Technology applicable to secondary NASA payloads, other planetary missions (balloon/dirigible companion payloads), and commercial weather/environmental monitoring platforms

### Key Technical Assumptions/Validation Goals
- **Assumption:** Wind shear above Venus cloud layer (measured by Venera probes) provides sufficient energy density for dynamic soaring
- **Validation Goal:** Simulation-based proof that algorithms can sustain altitude and achieve targeted navigation across multiple soaring cycles

### Document Quality Note
This is a substantive Phase I interim report with detailed technical sections, labor breakdowns, and clear task descriptions. Provides strong foundation for Phase II proposal if funded.