# Intelli-Copter Micro-Unmanned Aerial System White Paper

## Document Metadata
- Type: White Paper / Technical Proposal
- Client/Agency: Not explicitly named (appears to be law enforcement or government agency based on use case language)
- Program/Solicitation: Not specified
- Date: July 24, 2013
- BST Products/Systems Referenced: Custom tablet-based operator control unit (OCU); Android-based gesture control interface; autonomous navigation and mapping software
- Key Personnel: Not named individually
- Partner Organizations: Intuitive Research & Technology Corporation, Leptron, Chiaro Technologies

## Executive Summary

Black Swift Technologies, in partnership with Intuitive Research & Technology Corporation, Leptron, and Chiaro Technologies, proposed development of the Intelli-Copter—a man-portable micro unmanned aerial system (MUAS) with vertical takeoff and landing (VTOL) capability designed to autonomously search, map, and visualize the interior of confined structures (buildings, caves) in real-time using advanced 3D imaging and autonomous navigation. The system would provide operators with unprecedented situational awareness of multi-level indoor environments from a safe standoff distance via a tablet-based interface.

## Technical Approach

**Two-Phase Development Program:**
- **Phase I (10 months):** Design, build, and V&V testing to achieve TRL-6 prototypes. Vehicle and imaging/autonomy systems developed in parallel using a COTS VTOL aircraft for sensor/algorithm development to isolate cost and schedule risks.
- **Phase II (8 months):** Full integration and optimization to deliver TRL-8 system with sensor package optimized for the custom MUAS vehicle.

**Development Process:** Requirements → Design → Development → Testing (unit, system, field) → Final Acceptance, with customer buyoff at each stage.

**Key Technical Innovation:** Integration of custom IR structured light 3D imaging (Chiaro's "StereoActive" technology) with 6-DOF SLAM (Simultaneous Localization and Mapping) using IMU fusion for GPS-denied indoor navigation and multi-level environment mapping.

## Products & Capabilities Described

### Vehicle System
- **Custom folding micro helicopter** with counter-rotating rotors to minimize diameter
- **Specifications:**
  - Man-portable in rugged carrying tube
  - Setup time: <3 minutes
  - Flight endurance: minimum 30 minutes
  - Folding rotor design for compact storage
  - Integrated power and payload systems
  - Backpack or hard-shell tube carrying case

### Autopilot System
- **Low-level Flight Controls:** Stabilizes aircraft in roll, pitch, yaw, height, and airspeed using IMU, pressure altimeter, and sonar rangefinders
- **Navigation and Mapping:** 6-DOF SLAM algorithm fusing:
  - EO/IR camera feature detection
  - 3D structured light measurements
  - IMU data via Kalman-type fusion filter
  - GPS integration when available for global coordinate registration
- **Flight Modes:**
  - Fully autonomous: explores environment, performs obstacle detection and collision avoidance
  - Augmented: operator provides high-level commands (fly forward, climb, yaw) via tablet; defaults to hover if no input

### Imaging Payload

**EO/IR Camera Array:**
- Multiple cameras stitched into panoramic imagery for virtual pan-tilt-zoom (PTZ)
- Omni-directional viewing for situational awareness
- Hardware-based H.264 video compression for low-latency wireless streaming
- Virtual PTZ allows operator to select regions of interest from panorama without physical camera movement
- Operates in all lighting conditions, including complete darkness

**Structured Light 3D Imaging System (Chiaro "StereoActive" Solution):**
- Custom IR projector with synchronized micro cameras and integrated image processor
- One or more systems mounted on MUAS for 360-degree point cloud generation
- **Baseline Performance:** Centimeter-level accuracy
- Active optical technique enabling operation in total darkness
- Designed to overcome degraded performance in bright/direct sunlight through high-power, low-duty-cycle illumination
- Full-frame 3D capture without scanning

**3D Imaging Technology Comparison:** White paper notes that available COTS solutions (laser scanning, stereo vision, time-of-flight) have limitations in SWaP, accuracy, or range unsuitable for MUAS employment; Chiaro's custom solution addresses these constraints.

### Communication System
- **Multi-hop mesh network** architecture enabling:
  - Real-time data sharing with geographically dispersed users
  - Multi-vehicle control from single operator
  - Cooperative and distributed vehicle control
  - Range extension through relay chains
  - Seamless user access and real-time data updates

**Bandwidth Requirements (Single Vehicle):** Detailed breakdown provided in requirements table (specific values not extracted in provided text excerpt).

**Unique Capability:** Communication-aware planning—automatic detection and tasking of available MUAS as communication relays with continuous position updates, optimizing relay chains without operator intervention. Critical for cave/constrained environments with limited range.

### Operator Interface
- **Tablet-based OCU** with touch and gesture controls
- Adapted from Black Swift's existing Android-based UAV control system
- Features:
  - Intuitive gesture-based multi-touch controls
  - Real-time 3D map navigation and manipulation
  - Video display/playback capability
  - Multi-operator, multi-vehicle support
  - Omni-directional view for situational awareness with rapid PTZ switching to high-resolution regions of interest
  - Does not require continuous user attention due to autonomous flight capabilities

## Use Cases & Applications

**Primary Missions:**
- Interior mapping of residential/commercial properties (doorway/window navigation)
- Cave and confined structure exploration and mapping
- Multi-level structure mapping (unique 6-DOF SLAM advantage)
- Real-time detection of hidden rooms or passageways
- Time-critical intelligence gathering (location of people, structure assessment)
- Mission scenarios where operator needs safe standoff distance from potentially hazardous environments

**Operational Scenarios:** Law enforcement, military, civilian search and rescue, structural inspection, underground environment reconnaissance.

## Key Technical Specifications

**Vehicle Size, Weight & Power:**
- Platform designed to be man-portable with minimal SWaP for payload
- Baseline specifications provided in Table 2 (specific numbers not extracted)
- Minimum 30-minute flight time requirement
- Operating temperature range: -10°F to 120°F (nominal)

**System-Level Requirements** (from Table 1 - specific thresholds not detailed in provided excerpt):
- Autonomous navigation in GPS-denied environments
- Real-time video and 3D point cloud streaming
- Autonomous obstacle detection and collision avoidance
- Support for multiple flight modes
- Secure wireless communication
- Man-portable deployment capability

**Structured Light Performance:**
- Centimeter-level ranging accuracy
- 360-degree point cloud capability
- Daylight-capable through custom projector design
- Full-frame 3D capture per frame

## Risk Analysis

**Identified Technical Risks (12 total):**

1. **3D Ranging System SWaP exceeds MUAS capability** (Medium Risk)
   - Mitigation: Early sensor-vehicle coordination on SWaP envelope

2. **3D Ranging accuracy/resolution insufficient** (Low Risk)
   - Chiaro's extensive experience de-risks; contingency: slower vehicle operation to increase measurement count

3. **3D Ranging detection range insufficient (especially in direct sunlight)** (Medium-High Risk)
   - Mitigation: Detailed projection power analysis early; contingency: vehicle wall-following increases mapping time

4. **Communication range/power inadequate for indoor operation** (Low Risk)
   - Mitigation: Early RF power budget analysis and testing of multiple COTS radio solutions

5. **Communication bandwidth insufficient for video/3D point-cloud streaming** (Low Risk)
   - Contingency options: reduce video resolution, point cloud resolution, frame rate, or compression quality

6. **Vehicle rotor diameter too large for doorway/window navigation** (High Risk)
   - Mitigation: Detailed customer requirements definition to establish maximum rotor diameter; reduce payload SWaP if necessary

7. **Vehicle too large for single-operator portability** (Low Risk)
   - Leptron's folding rotor blade experience de-risks this

8. **Insufficient flight time with imaging payload** (High Risk)
   - Primary concern: 3D imaging power consumption in direct sunlight unknown; Mitigation: detailed projection power analysis; adaptive performance (higher power in sunlight, reduced indoors); contingency: reduce payload performance to reduce weight/power

9. **Payload scope creep** (Very High Risk—High Consequence)
   - Mitigation: Detailed customer discussions during requirements phase to lock payload scope early

10. **Temperature requirement changes** (High Consequence, Low Probability)
    - Battery composition changes would affect weight/flight time; contingency: detailed customer discussions to confirm temperature range covers operational spectrum

**Risk Monitoring:** Continuous tracking through program reviews; mitigation actions tracked for effectiveness; strategies refined as needed.

## Notable Details

**Partnership Structure:**
- **Leptron:** Leader in industrial remotely piloted helicopters; expertise in VTOL platforms, folding rotor designs, harsh environment operation
- **Chiaro Technologies:** Specialist in structured light triangulation-based 3D imaging; OEM components; patented algorithms and optical technology
- **Black Swift Technologies:** sUAS/MUAS design, integration, deployment expertise; hundreds of field deployments across U.S.; FAA regulatory navigation expertise; existing Android tablet control interface (adaptable to this system)

**Competitive Advantages:**
- No existing fieldable UAS available with stated capabilities
- Custom design optimized for mission (vs. COTS limitations)
- 6-DOF SLAM enabling multi-level structure mapping (vs. traditional planar SLAM)
- Fused IMU-feature SLAM for robustness and accuracy
- Global coordinate registration via GPS when available
- Real-time 3D map visualization at operator during autonomous exploration
- Communication-aware relay planning (unique capability)
- Virtual PTZ from camera array (avoids heavy physical gimbal)
- Structured light enabling operation in total darkness

**Mission-Critical Capabilities:**
- Autonomous exploration with operator ability to take over for detailed inspection of features of interest
- Multi-hop mesh networking extending range and enabling multi-user access
- Real-time map building and visualization during flight
- 360-degree 3D point clouds enabling hidden room/passageway detection

**Program Risk Management Philosophy:** Two-phase approach isolates vehicle and sensor development risks; significant V&V testing and redesign cycles built into schedule to reduce likelihood of late-stage deficiencies.