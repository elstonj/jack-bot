# GPS Denied Navigation Phase I Proposal

## Document Metadata
- Type: NASA Phase I SBIR proposal
- Client/Agency: NASA
- Program/Solicitation: 2025 Phase I (topic A2.01 GPS Denied Navigation)
- Date: Submitted between 2024-12-11 and 2025-02-25
- BST Products/Systems Referenced: Multi-modal sensor suite, terrain relative navigation (TRN) algorithms, machine vision systems, sensor fusion engine
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
Black Swift Technologies proposes a Phase I effort to advance GPS-denied autonomous navigation capabilities for UAS by integrating a refined multi-modal sensor suite with enhanced terrain relative navigation algorithms, adaptive weather sensing, and autonomous mission planning. The work builds on prior NOAA and internal R&D projects to deliver a low SWaP-C system capable of operating in GPS-denied environments with real-time hazard detection and mitigation.

## Technical Approach

### Core Navigation Strategy
- **Computer Vision + ICP-Based Localization**: Uses YOLO object detection to identify semantic features (radio towers, buildings, etc.) from optical imagery, projects detections to WGS84 coordinates, then applies a modified Iterative Closest Point (ICP) algorithm to match detected features to a georeferenced database of known navigation features. The key innovation is constraining ICP to match "like objects to like objects" rather than allowing arbitrary point cloud matching.
- **Sensor Fusion Architecture**: Integrates altimeters, optical flow sensors, and range sensors with real-time inertial and environmental sensor data through an advanced fusion engine.
- **Terrain-Relative Navigation (TRN)**: Fuses real-time sensor inputs with high-resolution a priori terrain data for altitude control, terrain following, and obstacle avoidance.

### Five Technical Work Areas

1. **Refine and Integrate Multi-Modal Sensor Suite**
   - Optimize hardware integration of altimeters, optical flow sensors, and range sensors
   - Achieve low SWaP-C (Size, Weight, Power, Cost)
   - Refine calibrations and establish robust real-time data interfaces for challenging environments

2. **Enhance Terrain Relative Navigation Algorithms**
   - Build on prior work from NOAA and internal R&D (IRAD) projects
   - Optimize for precise altitude control, terrain following, and obstacle avoidance in GPS-denied conditions

3. **Develop Adaptive Weather and Hazard Sensing & Fusion Capabilities**
   - Refine machine vision and deep learning for semantic segmentation and obstacle detection
   - Integrate with inertial/environmental sensor data
   - Auto-detect and mitigate hazardous conditions (high winds, icing, precipitation)

4. **Advance Autonomous Mission Planning and Execution**
   - Refine flight planning algorithms for dynamic, safe mission profile generation
   - Integrate environmental forecasts and real-time sensor inputs
   - Optimize flight path and energy management during critical mission phases
   - Leverage operational data and historical flight testing experience

5. **Gather Customer and Operational Feedback**
   - Conduct ground tests and limited flight experiments with selected subsystems
   - Engage with end users and stakeholders
   - Refine technical parameters based on real-world performance data

## Products & Capabilities Described

### Machine Vision & Deep Learning
- YOLO-based object detection for identifying semantic features
- Semantic segmentation and obstacle detection
- Automated feature classification and georegistration

### Sensor Suite Components
- Altimeters
- Optical flow sensors
- Range sensors
- Inertial sensors
- Environmental sensors

### Sensor Fusion Engine
- Advanced multi-modal data fusion
- Real-time hazard detection and mitigation
- Automatic environmental condition assessment

### Navigation Algorithms
- Modified ICP (Iterative Closest Point) for semantic object matching
- Terrain-relative navigation algorithms
- Autonomous flight planning and mission execution
- Energy management optimization

## Use Cases & Applications
- GPS-denied autonomous operations
- Terrain-following flight
- Obstacle avoidance in complex environments
- Operations in challenging weather conditions (high winds, icing, precipitation)
- Missions requiring dynamic path replanning based on environmental forecasts and real-time sensor inputs

## Key Innovation
**Semantic Object-Based Navigation**: The primary R&D innovation is using semantically-named objects detected via computer vision (e.g., "radio tower" identified by YOLO) to localize against a database of named, georegistered features. This constrains the ICP matching problem to logical pairs (radio tower to radio tower) rather than allowing unconstrained point cloud matching, improving robustness and reducing computational complexity.

## Notable Details
- Builds on prior NOAA and internal R&D (IRAD) projects, indicating previous government validation
- Emphasizes low SWaP-C integration suitable for UAS platforms
- Ground testing and limited flight experiments planned for Phase I to validate subsystems
- Customer engagement and operational feedback incorporated into refinement cycle
- Autonomous system design accounts for dynamic mission adjustment in real-time