# Sensor Fusion and Algorithms for Mapping at Low Altitude Above Rugged Terrain

## Document Metadata
- Type: NASA SBIR Phase I Proposal
- Client/Agency: NASA
- Program/Solicitation: SBIR 2018-I, Topic A2.02-9342
- Date: February 9, 2018 (created); submitted 2018
- BST Products/Systems Referenced: S2 UAS, SwiftCore Flight Management System, SwiftPilot autopilot, SwiftStation ground station, SwiftTab tablet interface, SuperSwift UAS, SuperSwift XT UAS
- Key Personnel: Dr. Maciej Stachura (PI, CTO), Dr. Jack S. Elston (Lead Engineer, CEO/co-founder), Joshua Fromm (Aircraft Design and Integration)

## Executive Summary
This Phase I proposal seeks to develop a sensor fusion and machine vision system enabling fixed-wing UAS to safely navigate and collect data at low altitudes over rugged, forested terrain with obstacles. The system will combine multiple sensing modalities (machine vision, lidar, radar) with advanced algorithms for real-time terrain contouring and obstacle avoidance, integrated onto the proven S2 platform with the SwiftCore flight management system. Success will enable new scientific and commercial applications requiring low-altitude operations beyond visual line-of-sight.

## Technical Approach

### System Architecture
BST proposes to develop an integrated subsystem combining:
1. **Multi-sensor suite** for comprehensive environmental awareness
2. **Advanced onboard processing** for real-time decision-making
3. **Modular integration** with the SwiftCore flight management system via the BST SDK
4. **Iterative design and testing** approach starting in Phase I

### Sensor Candidates Evaluated
- **Machine Vision**: OpenMV Cam M7 (embedded machine vision with self-contained processing)
- **Processing Platforms**: NVIDIA Jetson TX2 (256 CUDA cores, real-time video processing, graphics processing for motion planning)
- **Lidar**: Velodyne Ultra Puck (32 channels, 200m range, +15° to -25° vertical FOV, 360° FOV)
- **Laser Ranging**: Lightware SF00 (250m range, 0.01m resolution, >200 Hz update rate)
- **Radar**: TEF810X transceiver (76-81 GHz, 250m range capability)

### Algorithm Development
Phase I will identify and select from:
- **Machine Vision Algorithms**: Obstacle detection, identification, and ranging using monocular or stereo vision
- **Sensor Fusion Algorithms**: Integration of multiple sensor streams (vision, lidar, radar, a priori terrain data) with different accuracy/latency characteristics
- **Path Planning**: Fixed-wing specific obstacle avoidance algorithms suitable for onboard computation constraints
- **Reference implementations**: Building upon existing research (Barry & Tedrake stereo vision work, optical flow techniques, GPS-denied indoor flight demonstrations)

### Integration Methodology
- CAD modeling of sensors for mechanical integration
- Mechanical and electrical interface design for S2 platform
- Power budget and data interface integration with SwiftCore
- Simulator module development using Gazebo environment (already used for SwiftCore flight management system testing)
- Flight safety case preparation for NASA Airworthiness Flight Safety Review Board (AFSRB)

## Products & Capabilities Described

### S2 UAS
- **Description**: Small fixed-wing unmanned aircraft system with proven NASA flight heritage
- **Use in proposal**: Designated as primary demonstration platform for Phase II
- **Rationale**: Previously successful SBIR product with established reliability in scientific missions

### SwiftCore Flight Management System
- **Components**: SwiftPilot autopilot, SwiftStation ground station, SwiftTab tablet user interface
- **Capability**: Integrates payload, actuator, and sensor interfaces via onboard bus or ground station connection
- **Use**: Primary integration point for terrain-contouring and obstacle-avoidance subsystem
- **BST SDK**: Documented software development kit for modular integration with external systems

### Proposed Terrain Contouring and Obstacle Avoidance Subsystem
- **Architecture**: Modular, hardware-agnostic subsystem (initial deployment on S2)
- **Intended outputs**: Real-time navigation decisions and avoidance maneuvers
- **Key capability**: Enables automated low-altitude flight in terrain-constrained environments without high-G maneuvers
- **Extensibility**: Designed for future deployment on multi-rotor platforms as well

## Use Cases & Applications

### Scientific Applications
- **Volcanic plume sampling**: Low-altitude flights around volcanic vents in Costa Rica (mission that identified the need)
- **Trace gas measurements**: Methane detection from pipelines and point sources (requires low altitude flight due to gas dispersion)
- **Atmospheric sampling**: CO₂ emissions sampling, atmospheric boundary layer profiling
- **Forest/biomass assessment**: Forest biofuel calculation, invasive species identification
- **Terrain monitoring**: Rock and mudslide mitigation, snowpack analysis
- **High-resolution photogrammetry**: 3D mapping and point cloud generation over 600+ acre areas
- **Infrastructure inspection**: Pipeline and powerline monitoring over long distances

### Operational Regimes Enabled
- Beyond visual line-of-sight (BVLOS) operations
- Night operations over time-restricted features (wildfires, volcanoes)
- Low-altitude canyon/gorge navigation
- GPS-denied environment operations
- Terrain-constrained area access requiring minimal landing space

## Key Results
This is a Phase I proposal; no experimental results are provided. The document outlines the planned approach and deliverables for Phase I work.

## Phase I Deliverables & Milestones

1. **Requirements, specification, and design document**
2. **Sensor overview document**: Intended sensors, mounting locations, required interfaces
3. **Algorithm overview document**: Machine vision algorithms (monocular/stereo), sensor fusion approach
4. **UAS subsystems**: Sensor-specific subsystems with processing and interface components
5. **Flight Safety Review materials**: Documentation for NASA AFSRB approval
6. **Final report**: Implementation details and Phase II transition plan

## Work Plan Summary (6-month Phase I, ~800 estimated hours across team)

- **Task 1.0** Preliminary Work: Kickoff, mission requirements documentation, project management (164 hrs)
- **Task 2.0** Sensor Selection: State-of-art survey, requirements identification, sensor selection, interface definition (90 hrs)
- **Task 3.0** Algorithm Selection: Machine vision algorithms, COTS implementations, sensor fusion requirements and algorithms, obstacle avoidance algorithms (220 hrs)
- **Task 4.0** Subsystem Integration: Sensor CAD models, mechanical integration, power/data interfaces, simulator modules (180 hrs)
- **Task 5.0** Flight Testing Preparation: CONOPS development, risk assessment/mitigation, Flight Test Plan and Flight Readiness Review materials (100 hrs)
- **Task 6.0** Solution Specification: Phase II implementation plan, final report (170 hrs)

## Notable Details

### Competitive Positioning vs. State of the Art
- **Multi-rotor advances**: Commercial multi-rotor platforms now have standard obstacle avoidance; proposal brings this capability to fixed-wing aircraft
- **Fixed-wing gap**: Very limited work on real-time obstacle avoidance for fixed-wing UAS compared to multi-rotor
- **Recent enabling technologies**: Sensor miniaturization (OpenMV, automotive lidar/radar), onboard GPU processing (Jetson TX2), and algorithm development (vision-based SLAM, optical flow) have created opportunity window
- **Unique approach**: Combines longer-range sensing (250m lidar/radar) with machine vision to eliminate need for high-G evasive maneuvers

### Key Partnerships & Prior Success
- **CU Boulder relationship**: PI and team have extensive University of Colorado affiliation for flight testing and airspace approvals
- **Previous NASA SBIR success**: 
  - Soil Moisture Mapping sUAS (NNX14CG09C): Generated $719,314 additional investment post-Phase II
  - Ruggedized UAS for Harsh Environments (NNX16CP42P, ongoing Phase II): Already achieved commercialization with two new payloads integrated into NASA missions
- **Flight heritage**: S2 and related platforms already flown in multiple NASA scientific campaigns
- **Regulatory experience**: Team has secured and maintained >140 FAA Certificates of Authorization; successfully completed six NASA AFSRB/FRRB processes

### Commercialization Strategy
**Target Markets**:
1. NASA and government agencies (continuation of existing relationships)
2. Commercial survey/GIS sector (3D photogrammetry for orthomosaic generation, point clouds)
3. Infrastructure monitoring (pipeline/powerline inspection with methane detection)
4. International markets (design kept below ITAR threshold for EAR classification, enabling export)

**Entry Strategy**:
- Early releases to trusted commercial customers for validation
- In-house deployment by BST operations team for internal missions
- Refinement before broader market release
- Direct integration into S2 platform first, then extension to other platforms

**Key Commercial Drivers**:
- Lower barrier to entry for small UAS operators (intuitive tablet-based control)
- Reduced risk of mission failure in low-altitude operations
- Extended flight range for infrastructure monitoring (S2 covers 80 miles in 2-hour flight)
- Enable BVLOS operations (major regulatory milestone)

### Facilities & Infrastructure
- **1,600 sq. ft. facility** in Boulder, CO with:
  - Prototyping and testing equipment
  - Full atmospheric and aircraft simulation tools suite
  - Multiple spare autopilot systems for testing
  - Manufacturing capability (composites outsourced to Northwind Composites)
- **Nearby test areas**:
  - 10-minute fenced field
  - 20×20 mile Pawnee National Grasslands area
  - San Luis Valley high-altitude site (peaks to 15,000 ft MSL) planned as Phase II primary test site
- **NASA partnerships**: Securing permission to operate at San Luis Valley under JPL coordination

### Team Expertise

**Dr. Maciej Stachura (PI, CTO)**
- Ph.D. and M.S. in Aerospace Engineering (CU Boulder)
- 300+ flight experiments including multi-aircraft cooperative control and VORTEX2 tornadic supercell intercept
- 140+ FAA Certificates of Authorization
- Led completion of NASA AFSRB/FRRB for UAS in National Airspace System
- Previous Phase I and II NASA SBIR PI (soil moisture mapping)
- Research focus: Cooperative control algorithms, communication-aware information gathering
- Full-time commitment

**Dr. Jack S. Elston (Lead Engineer, CEO/co-founder)**
- Ph.D. from CU Boulder (meshed network UAS for tornado sampling)
- NSF Atmospheric and Geospace Sciences Postdoctoral Fellow
- Designed Tempest UAS (first-ever unmanned intercept of tornadic supercell in VORTEX2)
- Technical lead for SwiftCore avionics development
- 100+ authored publications, 100+ COA applications, 100s of flight experiments
- Arctic deployment experience
- Full-time employment at BST
- Research focus: In-situ atmospheric measurements, wind estimation, energy harvesting for UAS

**Joshua Fromm (Aircraft Design and Integration)**
- B.S. and M.S. in Aerospace Engineering, Fluid Dynamics concentration (CU Boulder, 2009)
- Dream Chaser mass model drop test at DFRC
- Payload system design for ice thickness/surface characteristics measurement (EO optics, IR, lidar, hyperspectral radiometer)
- BST specialization: Science payload integration, minimizing impact of aircraft dynamics/control systems on sensing

### Safety & Regulatory Approach
- **Early planning**: Phase I includes development of safety case materials for AFSRB and Flight Readiness Review Board
- **Risk management**: Detailed contingency planning and failsafes for low-altitude terrain/obstacle flight operations
- **Coordination**: Engaging previous NASA contacts and technical monitor to ensure flight approval strategy
- **Safe2Ditch integration**: Proposed system could combine with automatic emergency landing technology for enhanced safety
- **FAA coordination**: Work planned through CU for higher-altitude flight certifications (S2 currently limited to 400' AGL under commercial exemption)

### Related Prior Research
Proposal extensively references state-of-art work by Barry & Tedrake (pushbroom stereo vision at high speed), Roy (motion planning under uncertainty), Bry (GPS-denied flight), and others. BST team has direct involvement in referenced work (Dr. Stach