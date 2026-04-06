# Sensor Fusion and Algorithms for Mapping at Low Altitude Above Rugged Terrain

## Document Metadata
- Type: NASA SBIR Phase I Proposal
- Client/Agency: NASA
- Program/Solicitation: SBIR 2018-I, Topic A2.02-9342
- Date: 2018
- BST Products/Systems Referenced: S2 UAS, SwiftCore Flight Management System, BST SDK
- Key Personnel: Dr. Maciej Stachura (Principal Investigator, CTO), Dr. Jack S. Elston (Lead Engineer, CEO/co-founder), Joshua Fromm (Aircraft Design and Integration)

## Executive Summary
Black Swift Technologies proposes to develop a sensor fusion and autonomous guidance subsystem enabling fixed-wing UAS to safely conduct low-altitude flights over rugged terrain and obstacles. The system will integrate multiple sensing modalities (cameras, lidar, radar) with advanced algorithms for real-time obstacle/terrain avoidance and path planning, initially demonstrated on the mission-proven S2 UAS. This capability addresses a critical gap in UAS operations, enabling new scientific and commercial applications requiring low-altitude sampling in complex environments.

## Technical Approach

### Phase I Objectives
Phase I focuses on comprehensive design and engineering groundwork to enable Phase II flight testing:
1. **Sensor Testing and Selection** - Identify and evaluate candidate sensors; establish sensing requirements based on mission needs and algorithm requirements
2. **Algorithm Testing and Selection** - Research and select machine vision, sensor fusion, and obstacle avoidance algorithms suitable for fixed-wing aircraft dynamics and onboard computational constraints
3. **Subsystem Design** - Integrate selected hardware into subsystems compatible with S2 UAS mounting, power, and data interfaces using BST SDK
4. **Flight Test Preparation** - Develop safety case, contingency plans, and NASA Flight Safety Review Board materials for Phase II testing

### Sensor Suite Candidates
BST evaluated sensors across multiple modalities:
- **Machine Vision**: OpenMV Cam M7 (self-contained embedded vision processor); NVIDIA Jetson TX2 (GPU-accelerated real-time video processing with CUDA cores and machine learning libraries)
- **Lidar**: Velodyne Ultra Puck (32 channels, 200m range, ±15° to -25° vertical FOV, 360° horizontal FOV)
- **Solid-State Lidar**: Lightware SF00 (250m range, 0.01m resolution, >200Hz update rate)
- **Radar**: TEF810X transceiver (76-81 GHz, 250m range capability for automotive/UAS applications)

Key requirement: sensors must have sufficient range for decision-making (250m minimum) and be lightweight/compact for small UAS integration.

### Algorithm Development
- Leverage recent advances in GPU-accelerated processing and machine learning libraries (NVIDIA Jetson-focused)
- Research vision-based approaches: monocular/stereo vision for obstacle detection and identification
- Develop sensor fusion algorithms to combine multi-modal data (cameras, lidar, radar)
- Implement path planning for obstacle avoidance suitable to fixed-wing dynamics (avoiding high-G maneuvers)
- Reference state-of-the-art: stereo vision methods, optical flow techniques, vision-based navigation in GPS-denied environments

### Integration Strategy
- Develop CAD models for all sensors
- Design mechanical interfaces to S2 UAS with optimal field-of-view coverage
- Define power and data interfaces compatible with SwiftCore Flight Management System
- Implement simulator modules in Gazebo-based environment (BST's existing framework) for algorithm testing before hardware flight trials
- Utilize BST SDK for clean onboard bus and ground station integration

## Products & Capabilities Described

### S2 UAS
- **What it is**: Mission-proven fixed-wing UAS developed from previous NASA SBIR successes
- **Role in proposal**: Platform for Phase II flight demonstration and initial deployment of terrain-contouring/obstacle-avoidance subsystem
- **Flight heritage**: Demonstrated utility in scientific atmospheric sampling campaigns
- **Specifications implied**: Sufficient payload capacity for sensor suite; autopilot integration capability

### SwiftCore Flight Management System
- **What it is**: BST's proprietary flight management system with associated hardware modules for payload, actuator, and sensor interface
- **Role in proposal**: Primary integration point for new sense-and-avoid subsystem
- **Capability**: Supports modular payload integration via onboard bus and ground station interface

### BST SDK
- **What it is**: Software development kit for integration with SwiftCore
- **Role in proposal**: Critical for clean integration of new subsystems; will be improved/documented during Phase I
- **Purpose**: Enable integration of technology on multiple UAS platforms beyond S2 for wider commercialization

### Proposed Sense-and-Avoid Subsystem
- **What it is**: Integrated hardware/software system combining sensors, processing units, and algorithms
- **How it functions**: Multi-sensor fusion provides obstacle/terrain awareness; algorithms enable real-time autonomous path replanning to avoid detected hazards
- **Operational regime**: Low-altitude flights in rugged/forested terrain with obstacles up to 10m+ (trees, towers, irregular topography)
- **Decision-making**: Onboard processing enables autonomous decisions without relying on pilot visual input (supports BVLOS/night operations)

## Use Cases & Applications

### Scientific Missions
- **Volcanic plume sampling**: Low-altitude flights over vents to measure CO2 emissions (mentioned as the campaign where need was identified in Costa Rica)
- **Severe weather research**: Sampling of atmospheric properties in complex terrain
- **Forest biofuel assessment**: High-resolution data collection in vegetated areas
- **Snowpack analysis**: Measurements requiring low altitude over mountainous regions
- **Rock/mudslide mitigation**: Monitoring of hazardous terrain features
- **High-resolution photogrammetry**: 3D point cloud generation requiring close-range acquisition

### Infrastructure Inspection
- **Pipeline monitoring**: Low-altitude trace gas (methane) measurements over long distances (S2 can cover 80 miles in 2 hours)
- **Powerline inspection**: Extended BVLOS operations over obstacles
- **Wind turbine inspection**: Close approach to large structures without collision risk

### Atmospheric Science
- **Boundary layer profiling**: Multi-vehicle operations in stacked formations through wind features
- **Surface flux calculations**: Arctic tundra and other challenging environments

### Geographic Information Systems (GIS)
- **Commercial survey applications**: Photogrammetry-based 3D mapping and orthomosaic generation over areas up to 600 acres per flight
- **Low-barrier-to-entry operator tools**: Automated guidance reduces risk for operators without extensive UAS experience

### Regulatory/Capability Advancement
- **Beyond Visual Line of Sight (BVLOS) operations**: Safe low-altitude flight without pilot visual input
- **Night operations**: Enables temporary flight restriction missions (wildfires, volcanoes) without daylight constraints
- **Integration into National Airspace System**: Demonstrates milestone capability for routine UAS integration

## Work Plan & Milestones

### Phase I Deliverables (6-month effort)
1. **Requirements, specification, and design document** - Complete architectural design guidance
2. **Sensor overview document** - Intended sensors, mounting locations, required interfaces
3. **Algorithm overview document** - Machine vision and sensor fusion algorithms for obstacle detection
4. **UAS subsystem components** - Subsystems accommodating each sensor with processing and avionics interfaces
5. **Flight Safety Review materials** - Complete safety case and documentation for NASA approval
6. **Final report** - System implementation details and Phase II work plan

### Major Work Tasks
- **Sensor Selection (Task 2.0)**: Identification of state-of-the-art sensors; requirements definition based on mission and algorithms; selection of minimal viable sensor set; identification of interfaces/power/data requirements
- **Algorithm Selection (Task 3.0)**: Research machine vision approaches; evaluate COTS implementations; define sensor fusion requirements; develop/select fusion algorithms; identify and select obstacle avoidance algorithms for fixed-wing platforms
- **Subsystem Integration (Task 4.0)**: CAD modeling; mechanical integration design to S2; power/data interface definition; development of Gazebo simulator modules
- **Flight Test Preparation (Task 5.0)**: CONOPS development; risk identification and mitigation strategies; NASA AFSRB and FAA Certificate of Authorization preparation
- **Phase II Planning (Task 6.0)**: Implementation roadmap based on simulation results; final report

### Key Personnel & Effort Allocation
- **Dr. Maciej Stachura (PI/CTO)**: Overall project management (104 hrs), mission requirements, algorithm research, subsystem design
- **Dr. Jack S. Elston (Lead Engineer/CEO)**: Electronic design, firmware development, sensor integration, algorithm selection
- **Joshua Fromm (Aircraft Design/Integration)**: Mechanical design, sensor CAD modeling, integration to S2 airframe
- **Phase I total effort**: Distributed across 6-month period with iterative design approach

## Key Technical Details

### Sensing Architecture Considerations
- **Coverage approach**: Multiple cameras/sensors positioned around aircraft to provide comprehensive spatial awareness (referenced automotive example showing 360° coverage patterns)
- **Range/update rate requirements**: Detection range of 250m minimum; update rates sufficient for real-time reaction at aircraft speeds
- **Sensor fusion necessity**: Multiple sensing modalities required for robust operation in varied lighting, atmospheric, and terrain conditions
- **A priori data integration**: Digital elevation maps and terrain databases combined with active sensing for enhanced situational awareness (especially relevant for canyon operations with limited escape directions)

### Computational Strategy
- Leverage miniaturization of vision processors and availability of GPU-accelerated embedded platforms (NVIDIA Jetson TX2 specifically called out)
- Exploit advances in automotive industry for lidar and radar miniaturization
- Utilize existing Gazebo-based simulation infrastructure for algorithm development/testing before flight
- On-board processing essential to support BVLOS/night operations without pilot intervention

### Flight Safety Approach
- Early coordination with NASA technical monitor and Flight Safety Review Board
- Detailed contingency planning and failsafes for low-altitude/obstacle proximity flights
- Preparation of comprehensive safety case during Phase I (lessons learned from previous SBIR efforts)
- FAA Certificate of Authorization coordination (leveraging BST's experience with 140+ COAs for Colorado, Kansas, Nebraska)

## State-of-the-Art & Competitive Positioning

### Current Limitations Addressed
- **Multi-rotor dominance**: While quadcopters have proximity sensors and manual obstacle avoidance capability, little work addresses fixed-wing platforms
- **Fixed-wing constraints**: Unique dynamics (continuous forward motion, large turning radius, difficulty hovering) create different sensing/algorithm requirements than multi-rotor
- **VTOL limitations**: Alternative solutions (vertical-takeoff hybrid systems) are expensive and reduce flight endurance significantly
- **Terrain database limitations**: High-resolution DEM data insufficient for small UAS low-altitude operations in mountainous terrain

### Proposed Innovations
- **Longer-range sensing**: Multi-sensor fusion with 250m detection range enables safe decision-making without high-G evasive maneuvers
- **Practical fixed-wing focus**: Addresses gap in literature (most obstacle avoidance research focuses on multi-rotor or theoretical fixed-wing)
- **Rapid-prototyping approach**: Leverages recent GPU computing advances and COTS sensor miniaturization for practical implementation
- **Modular design**: SDK-based approach enables integration across multiple UAS platforms, not just S2
- **Safe2Ditch integration**: Potential future combination with emergency landing capability

## Notable Details

### Commercial Potential & Roadmap
- **Existing BST success**: Previously completed Phase I and Phase II SBIR for soil moisture mapping; currently executing Phase II for ruggedized systems. Both showed commercial uptake beyond SBIR funding.
- **Post-SBIR investment examples**: Soil moisture SBIR attracted additional $719,314 investment; ruggedized UAS SBIR integrated into NASA missions with commercial success
- **Target markets**:
  - NASA scientific missions (primary initial customer)
  - Commercial GIS/surveying sector (600-acre flight capability, intuitive Android tablet control)
  - Infrastructure inspection (80-mile range S2 platform for pipeline/powerline monitoring)
  - Low-barrier-to-entry UAS operations (reducing operator burden, improving safety)

### Integration with Existing BST Infrastructure
- **Flight heritage**: S2 and related platforms (SuperSwift, SuperSwift XT) already deployed in multiple NASA campaigns
- **Operations experience**: Team has conducted 300+ flight experiments; secured/maintained 140+ FAA COAs; participated in VORTEX2 tornadoes, Arctic deployments, multiple atmospheric science campaigns
- **Payload integration expertise**: Joshua Fromm specializes in minimizing airframe/avionics impacts on sensor operation
- **Previous SBIR leadership**: Dr. Stachura was PI for Phase I/II soil moisture