# BAE Systems WAANDER Albatross Oral Proposal

## Document Metadata
- Type: Oral proposal presentation (Google Slides)
- Client/Agency: DARPA
- Program/Solicitation: DARPA-PS-24-13 (Albatross program)
- Date: Created 2024-11-22; Modified 2024-11-26
- BST Products/Systems Referenced: S0 UAS, SwiftCore avionics, SwiftFlow MHP sensor suite, SwiftCore firmware, SWIL simulation environment
- Key Personnel: Dr. Jack Elston (CEO, BST), Dr. Maciej Stachura (CTO, BST), Spencer Lisenby (dynamic soaring expert consultant)
- Partner Organizations: NCAR (National Center for Atmospheric Research), WHOI (Woods Hole Oceanographic Institution), BAE Systems (prime contractor)

## Executive Summary
This is a 42-slide oral proposal presentation for DARPA's WAANDER (Wind-powered Autonomous Albatross-like Navigation Developed for Endurance and Range) program. Black Swift Technologies proposes to develop autonomous soaring capabilities for small UAS to achieve long-endurance missions through dynamic soaring and thermal soaring, leveraging their proven avionics, sensor suites, and flight control systems. The proposal emphasizes rapid iteration through frequent flight testing at multiple Colorado and California test sites.

## Technical Approach

**Overall Strategy:**
- Develop seamless autonomous soaring enabling long-endurance mission objectives
- Four core technical pillars: Plan, Sense, Control, and Flight Tests
- Iterative development with 1–3 flights per week throughout the program
- Progression from manual control for system identification (sys-id) to autonomous soaring algorithms

**Key Technical Workstreams:**

1. **Planning (P2FP - Weather and Energy Forecasting)**
   - Weather forecast-informed mission planning with energy savings prediction
   - Integration with NCAR detailed atmospheric models
   - Automated terrain and communications-aware planning tools
   - Adapted from existing SWIL simulation environment used for hurricane missions
   - Optimization for energy-aware planning and soaring path selection

2. **Sensing (Real-time High-Frequency Wind Condition Detection)**
   - SwiftFlow MHP sensor suite measures fine-scale turbulence and 3D wind vectors
   - 100 Hz sampling rate for atmospheric sensing
   - Measures: 3D wind, alpha/beta, true airspeed, pressure, temperature, humidity
   - Proven in heavy precipitation and severe turbulence environments
   - Calibrated against high-accuracy sources (NOAA systems, DOE ARM towers)

3. **Control (Harness Energy from Winds)**
   - Extrema-seeking control algorithms for thermal and ridge soaring
   - Pitch, roll, and lift adjustment for thermal and ridge exploitation
   - High-rate controllers for precision adjustments near terrain
   - Baseline system achieves 2+ hour endurance already (under more stringent aerial deployment constraints)

4. **Flight Tests (Safe, Continuous Testing)**
   - Land-based soaring: Colorado sites (Sod Farm for thermals, Pawnee National Grasslands for cross-country)
   - Ocean/ridge soaring: California dynamic soaring location
   - Pilots: BST thermal soaring pilot, former AF test pilot, Spencer Lisenby
   - Iterative approach: manual control → sys-id → autonomous algorithm development

## Products & Capabilities Described

### S0 UAS (Small Unmanned Aircraft System)
- **What it is:** BST's baseline small UAS platform with integrated avionics and sensor suite
- **Specifications:** Already achieves 2+ hour endurance under aerial deployment constraints; system-identification capable
- **Use in this proposal:** Baseline platform for soaring algorithm development and integration
- **Status:** TRL-9, field-tested in hurricanes

### SwiftCore Avionics Suite
- **What it is:** Fully in-house developed avionics electronics and firmware
- **Capabilities:** Stable operation in extreme conditions (hurricanes, Category 5), integration with commercial airframes
- **Advantages:** All electronics, firmware, and software developed in-house at BST, enabling rapid modification without external vendor dependency
- **Status:** TRL-9, hurricane-proven

### SwiftFlow MHP Sensor Suite
- **What it is:** Advanced atmospheric sensor package measuring fine-scale turbulence and 3D wind vectors
- **Specifications:** 100 Hz sampling rate; measures 3D wind, alpha/beta, TAS, pressure, temperature, humidity; minimum 15 m resolution
- **Calibration:** Validated against NOAA systems and DOE ARM towers
- **Use in this proposal:** Real-time detection of ridge and thermal soaring opportunities; energy calculation data collection
- **Status:** Proven in heavy precipitation and severe turbulence (hurricanes, volcanic plumes)

### SWIL Simulation Environment
- **What it is:** Integrated planning and simulation environment with NCAR atmospheric model outputs
- **Use:** Automated navigation, terrain and communications-aware planning
- **History:** Previously used for hurricane mission planning
- **Adaptation:** Being extended for energy-aware flight planning and soaring path optimization

## Use Cases & Applications

**Within WAANDER Program:**
- Land-based thermal soaring in Colorado mountain/plains environments
- Ridge soaring in California dynamic soaring locations
- Ocean soaring for long-endurance maritime missions

**Historical Applications (Demonstrating Capability):**
- Hurricane operations (NOAA)—Cat 5 demonstrations
- Volcanic plume sampling (USGS)
- Arctic operations
- Venus soaring simulations (NASA)

**Planned Commercialization:**
- ISR (Intelligence, Surveillance, Reconnaissance)
- Disaster response
- Scientific data collection

## Notable Details

**Team Structure:**
- Black Swift Technologies: Core technical team (avionics, sensor systems, control algorithms, flight operations)
- NCAR: Weather forecasting and atmospheric model integration
- BAE Systems: Prime contractor, oversight, guidance
- Consultants: Spencer Lisenby (dynamic soaring expert)

**Program Delivery Highlights:**
- **Rapid Development:** Full in-house development of all electronics, firmware, and software eliminates external vendor dependencies
- **Proven Track Record:** Successfully delivered high-complexity projects (NOAA, NASA, USGS)
- **Field-Ready Systems:** S0 and SwiftFlow already TRL-9; avionics tested in hurricanes
- **Test Infrastructure:** Multiple dedicated test sites within reasonable distance of BST headquarters
  - Colorado Sod Farm (15 minutes away, thermal soaring competition site)
  - Pawnee National Grasslands (20×20 miles, 5000' altitude permission)
  - California ridge soaring site with leading expert (Spencer Lisenby)
- **Test Frequency:** 1–3 flights per week enables rapid iteration
- **Expert Pilots:** Mix of BST internal thermal soaring pilot, former AF test pilot, and leading dynamic soaring expert

**Six-Month Checkout Requirement:** BST's mature, field-tested avionics and sensor systems are positioned for rapid integration and checkout.

**Data and IP:**
- Slides reference "Deliverables and Data Rights" (slide 26) and budget/schedule summaries but detailed content not provided in document excerpt

**Relationship to BAE:**
- This is a BAE Systems-led proposal with Black Swift Technologies as a subcontractor/key technical contributor
- Presentation follows BAE Systems style guidance and branding requirements
- Document includes BAE design templates, color palettes, and brand standards