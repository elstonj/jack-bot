# Wind-powered Autonomous Albatross-like Navigation Developed for Endurance and Range (WAANDER)

## Document Metadata
- Type: Oral presentation proposal (draft)
- Client/Agency: DARPA
- Program/Solicitation: DARPA-PS-24-13 (Albatross program)
- Date: Drafted 2024-11-27; modified 2024-12-18
- BST Products/Systems Referenced: S0 UAS, SwiftCore™ FMS, SwiftTab™ UI, SwiftFlow MHP, SWIL simulation environment
- Key Personnel: Dr. Jack Elston (CEO, BST), Dr. Maciej Stachura (CTO, BST), Frank Stolle, Peter Weichman, Dan Z, Kevin Rose
- Partner Organizations: BAE Systems (prime contractor), NCAR (FFRDC partner), University of California Santa Barbara (Prof. Joao Hespanha - consultant), Woods Hole Oceanographic Institution (Dr. Francesco Ventura - consultant)

## Executive Summary
WAANDER is a DARPA Albatross program proposal to develop autonomous soaring capabilities for small unmanned aircraft systems (s-UAS) that mimic albatross flight patterns to extend mission endurance and range through wind energy harvesting. The program integrates Black Swift Technologies' proven S0 platform and avionics with BAE Systems' planning tools, NCAR's high-resolution weather forecasting, and novel extrema-seeking control algorithms for both land and ocean dynamic soaring.

## Technical Approach

### Overall System Architecture
- **Preflight Planning Perk (PF2P)**: Weather and energy forecasting module using NCAR's FastEddy™ microscale wind model (~10-15 m resolution) to identify soaring opportunities and generate optimal routes
- **Sensor and Harnessing Control System (SHCS)**: Onboard sensing and control integration for real-time exploitation of soaring conditions
- **Integration**: Operator interface (SwiftTab™ UI) presents route alternatives with mission tradeoffs; in-flight replanning adapts to sensed conditions

### Planning (PF2P - Preflight Planning Perk)
- Uses stochastic optimization (MOLRTDP algorithm) to solve multi-objective shortest path problems
- Input: BST platform model, terrain data, sea state, wind forecasts, and NCAR-computed soaring opportunities
- Builds graph from soaring opportunity nodes and traversals, estimating energy change and uncertainty
- Metrics optimized: Likelihood of Mission Success, Time to Objective, Risk (terrain/weather proximity)
- Iterative refinement using corridor algorithms and final evaluation with NCAR microscale weather model
- Separate use of lower-resolution wind for planning efficiency and high-resolution FastEddy data for detailed metrics

### Sensing (SHCS - Sensor Integration)
- **Baseline avionics**: S0 Avionics Suite (proven in hurricanes, TRL-9)
- **Sensor suite**: SwiftFlow MHP for fine-scale turbulence and 3D wind vectors
  - 5-hole probe (only one proven to work in heavy precipitation)
  - Pressure, temperature, humidity sensors
  - Wave height and surface temperature measurement
  - Long-range communications (>180 miles)
  - Flush-air sensing nose cone
- **Sampling rate**: ~100 Hz for altimetry and environmental sensing
- **Target latency**: <50 ms for EO/IR stereo vision mapping (local ~50 m range)
- Integration proven against NIST-calibrated weather tower

### Control (SHCS - Control Algorithms)

**Land Soaring:**
- Extrema-seeking control algorithms that dynamically adjust pitch, roll, and lift to exploit thermals and ridge lift
- Based on past dynamic soaring work on S0 in hurricanes (eyewall seeking)
- Uses SWIL simulation environment adapted from NCAR detailed model outputs
- Targets constant climb paths exploiting flow over terrain features

**Ocean Soaring:**
- Model-free control algorithm reproducing albatross flight patterns
- Based on maximizing instantaneous rate of (kinetic + potential) energy harvesting
- Physics-driven CNN model for real-time 3D sea wave reconstruction
- Newton-based extremum seeking controller with sinusoidal perturbation of roll angle (φ)
- Extension from simplified vertical wind shear over flat surface to 3D dynamic sea surface data
- "Wave crest-informed" corrections to planned route using local altimetry data
- Challenges: Parameter perturbation frequency optimization to avoid resonance with near-shore sea surface features

## Products & Capabilities Described

### Black Swift Technologies (BST) Products

**S0 UAS Platform**
- Small unmanned aircraft system with proven endurance >2 hours under aerial deployment constraints
- Already demonstrates required baseline endurance
- Successfully operated in extreme conditions (hurricanes, volcanic environments)
- Commercial airframe (NAN Compass) adapted with BST avionics
- 10 airframes planned for field testing

**SwiftCore™ Flight Management System (FMS)**
- Advanced end-to-end avionics solution for autonomous flight control and command
- Enables fully autonomous operations
- All electronics, firmware, and software developed in-house by BST
- Proven TRL-9 with deployment in hurricanes and extreme weather
- Enables rapid iteration without external vendor reliance

**SwiftFlow MHP**
- Advanced sensor suite measuring fine-scale turbulence and 3D wind vectors
- Proven in heavy precipitation and severe turbulence conditions
- Includes unique 5-hole probe for precipitation environments
- 100 Hz sampling rate

**SwiftTab™ UI**
- Cloud-based planning and post-processing interface
- Tablet-based operational UI with seamless transition between planning and operations
- Augmented for WAANDER to display: multiple path options with metrics (probability of success), soaring potential layers, terrain, forecast weather, sea state

**SWIL Simulation Environment**
- Developed by BST to integrate NCAR detailed model outputs for automated navigation
- Based on open-source tools
- Adaptable for land and ocean soaring simulations

### NCAR Contributions

**FastEddy® LES Model**
- Numerical modeling of complex microscale flows using advanced computing architectures
- Provides high-resolution (~10-15 m) 3D phenomenological models of lower atmosphere
- Identifies soaring potential
- Two-tier output: lower-resolution for path planning efficiency, high-resolution for detailed metrics

## Use Cases & Applications

### Immediate Test Objectives
- **Land Soaring**: Ridge and thermal soaring in Colorado and California test sites
  - Motivation cited: USGS/NASA volcanic sampling missions in Aleutian Islands could extend range >20 miles with soaring capability
  - Test site: BST main test site where U.S. regional soaring contests held annually; Ridge site in California (through Spencer/DSKinetic)
  - FAA permission up to 5000' at Colorado sites

- **Ocean Soaring**: Dynamic soaring over ocean wave fields
  - Validates albatross-like flight patterns
  - Tests wave-state awareness and extrema-seeking control

### Transition Applications (Future Commercialization)
- Compass call with s-UAS CONOPS (ES/CEMA)
- Persistent ES/EA using SFF payloads (ES/ECS)
- Planners and SIGINT payloads (ES/C4ISR)
- Small UAS avionics payloads alignment (ES/CAS)
- PHASA-35 HALE integration (I&S)
- Micro-LIDAR wind sensing research (ES/FL/ST)
- Microscale weather forecasting for ocean bird science (WHOI research)
- Infrasound passive sensing for denied environment weather measurements (ES/FL/ST)

## Key Technical Challenges & Innovation Requirements

1. **Soaring Potential Prediction**: Integrate weather, geography, operational boundaries, aircraft performance, and mission objectives into high-res 3D phenomenological models with probabilistic energy prediction and ML adaptation

2. **Operator Decision Support**: Present multiple path alternatives with terrain, weather, and mission information in unified visual space; enable single-click replanning

3. **Real-Time Dynamic Sensing**: Integrate rapid altimetry, 3D wind sensing, pressure with low-latency EO/IR stereo vision for local wind field, sea surface, and terrain mapping (<50 m range; <50 ms latency)

4. **Platform Control for Energy Harvesting**: Extrema-seeking, high-rate control for micro-effects and wave winds; tight coupling to replanner for safety and collision avoidance

5. **Frequent Validation Testing**: Over 100 days of flight testing to prove innovations for transition systems

## Field Testing Approach

- **Test Aircraft**: 10 s-UAS based on NAN Compass airframe with BST SwiftCore avionics
- **Test Duration**: >100 days allocated
- **Team**: 2 competition pilots integrated to accelerate transition from manual data gathering to automated soaring
- **Locations**: 
  - BST main test site (Colorado)
  - Ridge soaring site in California
- **Altitude Authority**: FAA approval up to 5,000' at most Colorado sites

## Notable Details

### Competitive Advantages & Past Performance
- Dr. Jack Elston (CEO) led successful NOAA hurricane-sampling missions and NASA dynamic soaring project on Venus
- Dr. Maciej Stachura developed autonomous flight control for USGS volcanic monitoring, demonstrating extreme wind condition capability
- Only 5-hole probe in existence proven to work in heavy precipitation (SwiftFlow MHP capability)
- Existing S0 platform already exceeds baseline endurance requirement (>2 hours)

### Consultant Expertise
- **Prof. Joao Hespanha** (UCSB): Multi-agent control systems, hybrid switched systems, distributed control; IEEE/IFAC Fellow
- **Dr. Francesco Ventura** (WHOI): Marine megafauna movement, seabird flight behavior, wandering albatross (Diomedea exulans) and black-browed albatross (Thalassarche melanophris) focus

### Historical Mission Relevance
- Past dynamic soaring work demonstrated with S0 across 4 different hurricanes (eyewall seeking capability)
- USGS/NASA volcanic missions in Aleutian Islands identified as key motivation (20+ miles range extension potential)

### Integration with BAE Systems
- WAANDER team includes BAE mission planning, controls, and payload experts as advisors
- Transition targets BAE products: MAFPS, sensor integration, and control systems
- Leverages BAE planning workflow (cloud-based with tablet UI transition for operations)

## Presentation Status & Next Steps
This is a **draft oral proposal presentation** dated 2024-12-12, prepared for DARPA Albatross program submission. Document includes formatting guidance, template styling, and presentation structure but represents work-in-progress slides (pages 13-27 contain actual proposal content; pages 28+ are backup/template examples). Last editor noted as Maciej Stachura (BST CTO). Presentation will be submitted to DARPA-PS-24-13@darpa.mil with 60-minute presentation and 30-minute Q&A expected.