# Revolutionizing UAS Navigation: A Low SWaP-C Sensor Suite for Terrain Relative Autonomy

## Document Metadata
- **Type:** NASA SBIR Phase I Technical Proposal
- **Client/Agency:** NASA
- **Program/Solicitation:** NASA SBIR; ProSAMS Proposal Number A2.01-1010; Subtopic: Small UAV Compatible Sensor Development and Payload Integration for Aeronautics Applications
- **Date:** 2025-03-10 (submitted)
- **BST Products/Systems Referenced:** S2 UAS, S0 UAS, SwiftCore Flight Management System
- **Key Personnel:** 
  - Dr. Maciej Stachura (PI, CTO)
  - Dr. Jack S. Elston (Hardware Lead, CEO/Co-founder)
  - Daniel Prendergast (Software Lead)
  - Dr. Christoffer Heckman (Algorithm Lead, University of Colorado, subcontractor)

---

## Executive Summary

Black Swift Technologies proposes developing a next-generation UAS perception system combining low-SWaP-C altimeters, range sensors, and vision-based terrain sensing with advanced terrain relative navigation algorithms to enable safe fixed-wing UAS operations in GPS-denied environments, challenging terrain, and adverse weather. The system integrates deep learning-based semantic segmentation, optical flow processing, and sensor fusion to support two Phase II flight demonstrations: low-altitude terrain following (10m above obstacles in mountainous terrain) and long-distance GPS-denied return-to-home (10+ km) using feature tracking and landmark identification.

---

## Technical Approach

### Core System Architecture
- **Terrain Relative Navigation (TRN)** module merging real-time sensor data with high-resolution a priori digital terrain models (DTMs) for precise altitude control and dynamic terrain following
- **Multi-modal sensor fusion** combining vision, inertial measurement units (IMU), airspeed sensors, and all-weather radar
- **Deep learning vision processing** for:
  - Optical flow-based terrain tracking and obstacle avoidance
  - YOLO object detection for discrete hazards (towers, power lines)
  - Semantic segmentation for geographic feature identification (lakes, roads, mountains)
- **Feature-based GPS-denied localization** using landmark identification and database matching with Visual-Inertial Odometry (VIO) fusion
- **All-weather fallback capability** using lightweight radar sensors and digital surface models when vision is degraded/unavailable

### Phase I Focus
- Algorithm selection and development (optical flow, YOLO object tracking, semantic segmentation)
- Hardware selection trade studies (camera sensors, embedded compute, radar range finders)
- CONOPS and system architecture documentation
- Mission planning software enhancement
- Sensor fusion algorithm development and validation using archived flight data

### Phase II Objectives
- Two flight demonstrations validating the integrated system

---

## Products & Capabilities Described

### S2 UAS
- Fixed-wing platform for remote science missions
- Primary platform for technology integration and commercialization
- Planned recipient of terrain-relative autonomy capabilities

### S0 UAS
- Small UAS designed for severe weather operations
- Referenced for hurricane deployment experience (19 flights in 2024, including Category 5 storms)
- Demonstrated in extreme conditions (highest turbulence ever measured on Earth recorded)

### SwiftCore Flight Management System
- Autopilot system anchoring BST's avionics architecture
- Enables integration of advanced payloads and scientific sensors
- Foundation for terrain-relative navigation control algorithms

### Planning Software
- Existing low-TRL mission planning tool originally developed for Makushin volcano sampling mission (NASA/USGS collaboration)
- Phase I enhancement to:
  - Generalize for multiple UAS platforms
  - Integrate high-resolution digital surface models (Maxar Precision3D DSM)
  - Implement automated vertical route planning
  - Support dynamic flight plan updates based on sensor feedback

### Vision/Perception Hardware Suite (to be selected Phase I)
- Machine vision cameras (candidates: various NDAA-compliant options)
- Embedded computing platforms (candidates: NVIDIA Jetson, Luxonis OAK-D)
- Lightweight all-weather radar range finders
- Lightweight altimeters
- All designed for minimal SWaP-C integration on small UAS

---

## Use Cases & Applications

### Primary Mission Scenarios

**1. Volcanic Gas Sampling / Volcanic Survey**
- Multiple previous missions with NASA and USGS in Costa Rica, Hawaii, and Alaska
- Upcoming missions planned for Costa Rica (NASA Ames) and Chile (USGS)
- Requirements: low-altitude flight (as close to terrain as safely possible) for trace gas measurement over long ranges (e.g., 20-mile transit to Makushin Volcano) in complex terrain
- Challenges: terrain proximity requirement, fixed-wing platform constraints, long range/endurance, GPS-denied capability desired

**2. Low-Altitude Terrain Following in Mountainous Terrain**
- Target: maintain 10m altitude above obstacles in Colorado mountains
- Visibility scenario: 10m clearance validated with vision system in good conditions
- Degraded conditions: 20m minimum altitude without vision system (simulating fog, rain, nighttime) using radar + digital surface models
- Pre-planning with feasible path generation and wind consideration

**3. GPS-Denied Return-to-Home**
- Distance: 10+ km autonomous return from loss-of-GPS point to operator's visual line-of-sight
- Method: Feature tracking and landmark identification using YOLO + semantic segmentation + database matching
- Seasonal robustness: validation across varying seasonal conditions (addressing snow cover, seasonal vegetation changes)

**4. Wildfire Surveying**
- Terrain-aware operations in mountainous wildfire-prone areas
- Reduced visibility operations through smoke
- Alignment with NASA ACERO project objectives
- Drawing on BST's NOAA/USGS wildfire missions experience

**5. Severe Weather Operations**
- Hurricane observation and sampling (referenced: 19 Category 5 flights in 2024)
- Greenland operations (100s of missions documented)
- NOAA collaboration on ocean surface detection through extreme rain/sea spray at 10m altitude, 200+ knot ground speeds
- Radar-based sensors adapted as all-weather backup for terrain following

**6. Infrastructure Inspection**
- Low-altitude reliable flights for infrastructure inspection at various terrain/building heights
- Methane leak detection in oil/gas facilities (partnership with Chevron referenced)

**7. Lunar/Planetary Landing Simulators (Future)**
- Terrestrial testbed application for developing algorithms/hardware for lunar and planetary landers
- Terrain relative navigation, hazard detection, and hazard relative navigation capabilities transferable
- Open interfaces maintained for future NASA groups

---

## Key Technical Results & Specifications

### Performance Targets

**Terrain Following:**
- Vision-based clearance: 10m above obstacles
- Radar/DSM-based clearance (degraded visibility): 20m above terrain
- Obstacle types: terrain, trees (>10m height)
- Platform: fixed-wing UAS
- Terrain type: mountainous

**GPS-Denied Navigation:**
- Return distance: >10 km to operator's visual line-of-sight
- Methods: YOLO feature tracking, semantic segmentation, landmark identification from public map data
- Robustness: validation across seasonal variations (snow cover, vegetation changes)
- Sensor fusion: VIO + inertial + airspeed measurements

**Algorithm Development (Phase I Outputs)**
- Month 5 deliverable: Quantitative analysis data from three core algorithms:
  1. Optical flow (terrain tracking)
  2. Object tracking (collision avoidance + navigation)
  3. Semantic segmentation (scene simplification: roads, geographic features)
- Month 6 deliverable: Sensor fusion algorithm results using 3-5 archived flights with terrain sensors as validation surrogates; RMS error cross-validation metrics

### Historical Performance References

- **Hurricane Operations:** 19 Category 5 flights in 2024; highest turbulence ever measured on Earth recorded
- **Extreme Weather Deployment:** 100s of missions in Greenland
- **Volcanic Sampling:** Multiple successful missions in Costa Rica, Hawaii, Alaska
- **Previous SBIR Success:** Phase I and Phase II completion for soil moisture mapping UAS (commercialized)

---

## Notable Details

### Competitive Advantages & State-of-the-Art Differentiation

1. **Integrated vs. Isolated Sensors:** Proposed system uses advanced sensor fusion vs. disparate standalone sensors typical in current UAS
2. **Deep Learning Vision:** Semantic segmentation + YOLO vs. traditional model-based approaches
3. **Semantic Matching:** Robust to failure modes in low-level feature matching (fails on repetitive objects like forests, low-density features like deserts, seasonal changes); uses sparse set of semantically-named objects for matching
4. **Real-Time TRN:** Merges real-time sensor data with a priori DTMs vs. fixed flight plans and static maps
5. **Adaptive Flight Planning:** Dynamic path refinement based on real-time data vs. static pre-planned routes
6. **Modular, Open Architecture:** Designed for seamless integration across multiple UAS platforms vs. platform-specific systems
7. **Low SWaP-C Design:** Addresses limitations of bulky, energy-intensive sensors (e.g., conventional LIDAR)

### Operational Experience & Flight Safety Credentials

- **FAA Authorizations:** >140 Certificates of Authorization (COAs) obtained/maintained by Dr. Stachura; >100 COAs authored/maintained by team
- **NASA Flight Safety Certification:** Completed 9 Airworthiness Flight Safety Review Boards (AFSRB) and Flight Readiness Review Boards (FRRB)
- **First UCAS Certification:** BST first company to successfully complete NASA's Unmanned Commercial Aviation Services (UCAS) review
- **Beyond Visual Line-of-Sight Pioneer:** Worked with NASA Ames and Alaska Department of Transportation to pioneer BVLOS operations in Alaska for public safety without ground observers or chase aircraft

### Market Opportunity & Commercialization Strategy

**Market Gaps:**
- No current commercial or government UAS has these capabilities in operational capacity
- Critical need identified during BST's own NASA volcano sampling missions in Costa Rica

**Go-To-Market:**
- **Primary Product:** Integration into BST's commercial S2 UAS platform
- **Secondary Applications:** 
  - Infrastructure inspection
  - Methane detection (ongoing Chevron partnership)
  - Integration into legacy NASA UAS (e.g., ACERO platform)
  - Future Urban Air Mobility aircraft (validation pathway before crewed applications)
- **Commercialization Phases:** Screening → preliminary assessment → detailed market study → Phase I/II product development → trial production → pre-commercialization analysis → production start-up
- **Product Roadmap:** 
  1. Stand-alone real-time 3D hazard mapping system for small UAS
  2. Control algorithm "applications" (terrain following, safe-to-land) layered on top

**Risk Mitigation:**
- BST operates both as deep-tech developer and operational services provider
- Service work validates technology in extreme environments; reduces risk of non-practical SBIR research
- Direct partnership with NASA missions (volcano sampling in Costa Rica) serves as testbed and proof-of-concept

### Partnerships & Collaborations

- **University of Colorado Boulder:** Autonomous Robotics and Perception Group (ARPG) under Dr. Christoffer Heckman
  - Expertise in computer vision, machine learning, sensor fusion, field robotics
  - Applying semantic segmentation methods to overcome SLAM limitations
- **NASA Ames, USGS, NOAA:** Ongoing mission collaborations and operational feedback
- **Embry-Riddle Aeronautical University:** Wind tunnel facility access for wind measurement system characterization
- **Chevron:** Partnership for methane leak detection UAS operations
- **Maxar Technologies:** High-resolution digital surface model (Precision3D DSM) data integration

### Phase I Deliverables & Schedule (6 months)

| Month | Milestone |
|-------|-----------|
| 2 | Mission CONOPS and System Architecture document (for NASA technical monitor) |
| 3 | Prototype updated planning software (web-based, available to NASA personnel) |
| 5 | Quantitative analysis: optical flow, object tracking, semantic segmentation algorithms |
| 6 | Sensor fusion algorithm results with RMS error cross-validation metrics |

### Resource Allocation

Total Phase I effort: 900 hours across team
- Dr. Maciej Stachura (PI): 300 hours
- Dr. Jack Elston (Hardware): 200 hours
- Daniel P