# Intelli-Copter Micro-Unmanned Aerial System White Paper

## Document Metadata
- Type: White Paper / Technical Proposal
- Client/Agency: Not explicitly named (appears to be for law enforcement/military/civilian applications)
- Program/Solicitation: Not specified
- Date: July 24, 2013
- BST Products/Systems Referenced: Custom VTOL MUAS (Intelli-copter)
- Key Personnel: Jack Elston (last editor)
- Partner Organizations: Intuitive Research & Technology Corporation, Leptron, Chiaro Technologies

## Executive Summary
Black Swift Technologies, in cooperation with Intuitive Research & Technology Corporation, Leptron, and Chiaro Technologies, proposed development of a fieldable micro unmanned aircraft system (MUAS) capable of autonomously searching and mapping the interior of confined structures (buildings, caves) by integrating a custom VTOL vehicle with advanced 3D imaging and autonomous navigation technologies. The "Intelli-copter" would provide operators with a rapidly deployable, man-portable system to accurately map and visualize 3D models of multi-level confined structures from safe stand-off distances in real-time.

## Technical Approach

### Core Concept
Integration of a custom vertical-flight MUAS with five major subsystems:
1. **Vehicle System** - Custom-designed folding micro helicopter with 30-minute minimum flight time
2. **Autopilot System** - Provides augmented or fully autonomous operation in GPS-denied environments
3. **Communication System** - Ad-hoc wireless mesh network with communication-reactive control
4. **Imaging Payload** - EO/IR camera array and 3D structured light ranging system
5. **Operator Interface** - Tablet-based control unit with touch/gesture controls

### Key Technical Innovations
- **6DoF SLAM Algorithm** - Simultaneous localization and mapping using 3D range measurements for multi-level structure mapping
- **Structured Light 3D Imaging** - Custom IR structured light projector and image processing for operation from complete darkness to bright sunlight
- **Indoor Navigation** - Real-time autonomous obstacle detection and collision avoidance using 3D measurements
- **Communication-Aware Planning** - Automatic configuration of relay assets for optimal communication chains without operator intervention
- **Virtual PTZ Capability** - Camera array stitched into panoramic image providing omni-directional viewing with virtual pan-tilt-zoom

## Products & Capabilities Described

### Intelli-Copter MUAS
**What It Is:** A custom-designed, man-portable, folding micro helicopter system capable of autonomous indoor/confined environment mapping and exploration.

**Key Specifications:**
- **Vehicle Size:** 25 inches tip-to-tip (objective: 16 inches)
- **Vehicle Weight:** 2 lbs (objective: 2.5 lbs)
- **Endurance:** 30 minutes minimum (objective: 1 hour)
- **Flight Ceiling:** Sustained 10/20 mph wind, gusts 20/30 mph (objective)
- **Temperature Range:** -10°F to 120°F (objective: 0°F to 120°F)
- **Audio Signature:** 80 dB target, lower preferred
- **Deployment Time:** 5 minutes (objective: 1 minute)
- **Storage:** Folding rotor design enabling storage in carrying tube (8 inches collapsed, objective: 4.25 inches)

**Payload:**
- Power available: 0.5 Ahr threshold, 1-2 Ahrs objective
- Battery: 14V @ 10,000 mAh

**Proposed Use:** Autonomous exploration and 3D mapping of:
- Residential/commercial building interiors
- Multi-level structures
- Cave-like confined environments
- Interior perimeter mapping for building exterior

### EO/IR Camera Array
**What It Is:** Multiple electro-optical/infrared cameras providing omni-directional situational awareness and feature detection for navigation.

**Specifications:**
- **Threshold:** 1 camera (60° FOV), 320x240 resolution, 0.5 lux sensitivity, 5 Hz video stream
- **Objective:** 6 cameras (360° FOV), 1024x768 resolution, 0.0 lux sensitivity, 10 Hz color video stream
- **Capability:** Virtual pan-tilt-zoom through panoramic stitching; H.264 hardware-based compression for bandwidth management

**Use Case:** Real-time operator situational awareness; feature detection for SLAM; navigation and collision avoidance; operation in complete darkness

### Structured Light 3D Ranging System ("StereoActive")
**What It Is:** Chiaro Technologies' triangulation-based 3D imaging system using custom IR structured light projector, dual micro cameras, and integrated image processor.

**Baseline Performance:**
- **Speed:** >5 fps
- **Resolution:** >60x40 pixels (objective: 320x240 @ 10 Hz)
- **Accuracy @ 15 ft:** 10 inches threshold, 2 inches objective
- **Max Range (Low Light):** 10 ft threshold, 30 ft objective
- **Max Range (Sunlight):** 5 ft threshold, 20 ft objective
- **Detectable Feature Size:** 0.5 ft threshold, 0.1 ft objective
- **Size/Weight:** <20 cm³, <200g
- **Operating Conditions:** Blackout to daylight capable

**Advantages Over Competing Technologies:**
- Full-frame 3D point cloud capture without scanning (faster than laser scanning)
- Active optical technique operating in total darkness (advantage over passive stereo)
- Compact form factor optimized for UAVs (vs. PrimeSense/Kinect)
- Superior daylight performance through custom high-power, low duty-cycle IR illumination

**Use Case:** Real-time 3D environmental mapping; autonomous navigation; obstacle detection; generation of point cloud data streamed to operator

### Autopilot System

**Flight Control Capabilities:**
- 6-DOF IMU (accelerometers and angular rate gyros)
- GPS receiver with integration for GPS-denied environments
- Pressure altimeter
- Sonic range finders (zenith and nadir orientations)
- Autonomous landing via nadir ground detection

**Navigation Modes:**
1. **Fully Autonomous Mode** - Explores and maps environment; performs obstacle detection and collision avoidance using imaging sensors
2. **Augmented Mode** - Operator directs via high-level commands (fly forward, climb, yaw); auto-hover if no input

**SLAM Implementation:**
- 6DoF SLAM algorithm fused with IMU data via fusion filter
- Multi-level structure mapping capability (vs. traditional planar SLAM)
- Global coordinate reconciliation when GPS available (near windows or outdoors)
- Real-time map construction and visualization to operator

### Communication System

**Architecture:** Ad-hoc mesh network with multi-hop capability and communication-reactive control

**Performance Requirements:**
- **Range:** 1000 ft indoors (threshold), 2 miles restricted line-of-sight (objective)
- **Multi-hop:** 2 vehicles with full data (threshold), 5 vehicles with full data (objective)
- **Bandwidth:** 500 kbps (threshold), 11 mbps (objective)
- **Encryption:** None (threshold), 128-bit AES (objective)

**Bandwidth Allocation (Single Vehicle):**
- 3D Point Cloud: 35 kbps
- Video (320x240 8-bit color, 10 fps): 350 kbps
- Flight Controls: 3 kbps
- Health & Status: 2 kbps
- Additional Payloads/Sensors: 10 kbps
- **Total: 400 kbps**

**Unique Capability - Communication-Aware Planning:** Automatically detects available MUAS assets, tasks them as relays, and continuously updates their positioning to optimize communication chains without operator interaction. Critical for cave environments with severely limited range.

### Operator Interface
**What It Is:** Tablet-based operator control unit (OCU) with touch/gesture-based controls (Android platform).

**Capabilities:**
- High-level flight command interface (joystick-like)
- 3D map visualization and manipulation
- Feature measurement capabilities
- Real-time video display and playback
- Multi-operator access to synchronized data
- Omni-directional panoramic viewing
- Virtual PTZ control for zooming/panning within panoramic image

**Design Philosophy:** Intuitive interface requiring minimal operator attention, allowing focus on information and mission objectives.

## Use Cases & Applications

### Primary Mission Scenarios
1. **Interior Building Search and Mapping**
   - Mapping rate: 100 sq ft/min (threshold), 750 sq ft/min (objective)
   - Mapping accuracy: 5 ft (threshold), 1 ft (objective)
   - Applications: Search and rescue, tactical operations, building assessment

2. **Multi-level Structure Mapping**
   - Objective: 200,000 sq ft industrial complex in 15 minutes (vs. 30 minutes threshold)
   - Capability to detect hidden rooms and passageways

3. **Building Exterior Perimeter Mapping**
   - Rate: 50 linear ft/story/min (threshold), 100 linear ft/story/min (objective)

4. **Cave and Confined Environment Exploration**
   - Operation in complete darkness
   - Navigation through narrow passages and vertical shafts
   - Multi-hop communication relay capability for extended range

### Operational Requirements Addressed
- **Time-critical information** on structure interior (location of people, hidden spaces)
- **Safe stand-off distance** operation for operator safety
- **Minimal training** requirements for operator
- **Rapid deployment** from field-portable configuration
- **Real-time situational awareness** through simultaneous video and 3D mapping
- **Global Position Accuracy:** 5 ft threshold, 1 ft objective (outdoors); 5 ft local position accuracy indoors (threshold and objective)

## Program Development Plan

### Two-Phase Approach (Risk and Cost Reduction)

**Phase I: Technology Demonstration (8-12 months)**
- Objective: First working prototypes at TRL-6
- Approach: Design and test vehicle, imaging system, and autonomous behaviors in parallel (not independently)
- Use of commercial COTS VTOL platform for sensor/autonomy development to isolate risks
- Prototype-level sensor system (not optimized for SWaP)
- Significant unit and field testing with design iteration
- Deliverable: Functional prototypes demonstrating feasibility of each major subsystem

**Phase II: System Integration (6-8 months)**
- Objective: Complete TRL-8 fieldable system
- Integration of custom vehicle with optimized imaging/communication payload
- Final SWaP optimization
- Extensive field testing and ruggedization
- Deliverable: Fully integrated, ruggedized, man-portable operational system

### Development Methodology
- **Requirements Phase** - Functional requirements definition with customer and team
- **Design Phase** - Detailed design outlines and technical specifications
- **Development Phase** - Hardware, software, and mechanical development
- **Testing Phase** - Unit testing, system integration testing, field testing
- **Final Acceptance** - Presentation against requirements and design specifications

### Schedule Key Features
- Parallel vehicle and sensor development in Phase I to isolate risks
- Integrated unit and system testing followed by issue resolution periods
- Emphasis on robustness, ruggedization, and field-readiness throughout

## Risk Analysis and Mitigation

### High-Risk Items Identified

1. **3D Ranging System SWaP Exceeds MUAS Capability** (HIGH)
   - Mitigation: Early SWaP scoping between sensor and vehicle teams; detailed projector power analysis
   - Contingency: Reduce payload performance to reduce required vehicle size

2. **Vehicle Flight Time Insufficient with Imaging Payload** (HIGH)
   - Root Cause: Structured light projector power requirements uncertain for daylight operation
   - Mitigation: Extensive projection power analysis early in program; adaptive power management (higher power in sunlight, reduced indoors)
   - Contingency: Reduce payload performance/weight if necessary

3. **3D Ranging System Detection Range Inadequate** (MEDIUM)
   - Mitigation: Detailed projector power analysis; extensive testing
   - Contingency: Vehicle may require wall-following flight pattern, increasing mapping time

4. **Vehicle Too Large for Confined Environments** (MEDIUM-HIGH)
   - Mitigation: Proper rotor diameter scoping with customer during requirements definition; define maximum diameter early
   - Contingency: Reduce payload performance to reduce vehicle size

5. **Communication Range/Power