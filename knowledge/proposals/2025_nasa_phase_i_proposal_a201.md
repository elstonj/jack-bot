# 2025 NASA Phase I Proposal A2.01: GPS-Denied Navigation for UAS in Challenging Environments

## Document Metadata
- **Type:** NASA SBIR Phase I Proposal
- **Client/Agency:** NASA
- **Program/Solicitation:** NASA SBIR (specific topic not explicitly stated, but aligned with Small UAV Compatible Sensor Development and Payload Integration for Aeronautics Applications)
- **Date:** Submitted February 12, 2025 (created); modified through July 30, 2025
- **BST Products/Systems Referenced:** S2 (fixed-wing UAS platform), S0 (small UAS for extreme weather), SwiftCore Flight Management System
- **Key Personnel:** 
  - Dr. Maciej Stachura (PI, CTO)
  - Dr. Jack S. Elston (Hardware Lead, CEO/Co-founder)
  - Daniel Prendergast (Software Lead)
  - Dr. Christoffer Heckman (Algorithm Lead, University of Colorado, subcontractor)

---

## Executive Summary

Black Swift Technologies proposes developing a next-generation UAS perception system combining low SWaP-C sensors (cameras, radar, range sensors) with advanced terrain relative navigation (TRN) algorithms to enable fixed-wing UAS to operate autonomously in GPS-denied environments and challenging weather/terrain. The system will be validated through two ambitious Phase II flight demonstrations: (1) autonomous low-altitude terrain following at 10m above mountainous terrain, and (2) autonomous return-to-base navigation from 10+ km distances without GPS. Phase I focuses on algorithm selection, hardware trade studies, planning software adaptation, and sensor fusion development using archived flight data.

---

## Technical Approach

### Core Innovation: Integrated Multi-Modal Perception System

The proposed system combines three algorithmic pillars with a modular hardware architecture:

#### **Algorithmic Components (Task 3):**

1. **Optical Flow Algorithms** – Real-time terrain tracking by analyzing motion patterns in camera frames to detect terrain displacement relative to the aircraft. Used to maintain safe distance from terrain and validate against pre-loaded digital surface models (DSMs).

2. **Object Detection & Tracking (YOLO-based)** – Machine vision feature tracking for discrete hazards (towers, power lines, obstacles). Operates at ~30 fps on embedded hardware; enables both collision avoidance and GPS-denied navigation via landmark identification.

3. **Semantic Segmentation** – Deep learning-based scene classification to identify roads, lakes, rivers, mountains, and geographic features. More robust than traditional feature-matching approaches (e.g., SLAM) to seasonal changes, snow cover, and environmental variations.

#### **Sensor Fusion Strategy (Task 5):**

All-weather capability via multi-modal fusion:
- **Primary (good visibility):** Vision-based optical flow + YOLO feature tracking + semantic segmentation
- **Degraded (fog/precipitation):** Lightweight radar altimeters + pre-computed digital elevation models + inertial/airspeed data
- **Fallback:** Visual-Inertial Odometry (VIO) + inertial measurement units (IMU) + airspeed sensors for position tracking parallel to vision-based techniques

#### **Terrain Relative Navigation (TRN) Core:**

- Merges real-time sensor data with high-resolution a priori terrain information (digital surface models, satellite data)
- Dynamically adjusts flight paths based on hazard detection and sensor feedback
- Enables autonomous path refinement in real-time (online planning) rather than reliance on pre-planned waypoints

#### **Mission Planning Software:**

Adaptation of existing low-TRL planner (developed for Makushin Volcano mission with NASA/USGS) to:
- Generalize across multiple UAS platforms via performance capability models
- Integrate high-resolution obstacle data (Maxar satellite imagery)
- Automate vertical routing with dynamic altitude constraints based on terrain and aircraft climb/descent limits
- Provide web-based interface (AWS-hosted) for NASA mission groups

### Hardware Architecture (Task 4):

**Sensor Suite (Low SWaP-C focus):**
- Machine vision cameras (candidate: Luxonis OAK-D; others under trade study)
- All-weather radar range finders
- Embedded computing platform (candidates: NVIDIA Jetson; comparison with Luxonis and others)
- Inertial measurement units (IMU)
- Airspeed sensors
- NDAA-compliant components prioritized

**Design Principle:** Modular, open interface for seamless integration across different small UAS platforms (S2, S3, etc.)

---

## Products & Capabilities Described

### **Black Swift Technologies S2 (Fixed-Wing UAS)**
- **What it is:** Primary platform for Phase II flight demonstrations; proven in NASA missions including volcano sampling
- **Use in this project:** Testbed for terrain relative navigation at low altitude (10m above obstacles); capable of long-range operations (20+ mile transit)
- **Specifications:** Fixed-wing design optimized for endurance and range; compatible with modular sensor payloads

### **Black Swift Technologies S0 (Small UAS)**
- **What it is:** Highly capable system for extreme weather operations
- **Use in this project:** Referenced for BST's proven severe weather operational experience (100+ Greenland missions, multiple volcano intercepts, 19 hurricane flights in 2024 including Cat 5)
- **Relevance:** Demonstrates BST's track record that informs sensor/hardware robustness requirements

### **SwiftCore Flight Management System**
- **What it is:** Proprietary autopilot system developed by Dr. Elston; integrates real-time control algorithms
- **Use in this project:** Foundation for implementing terrain relative navigation control algorithms and sensor fusion
- **Specifications:** Capable of high-frequency (real-time) adaptive flight control; supports onboard processing of vision-based perception

### **Perception System Hardware (Proposed - Task 4 Output)**
- **Cameras:** TBD via trade study; candidates include Luxonis OAK-D (depth + RGB), other NDAA-compliant options
- **Compute Platform:** TBD via trade study; candidates include NVIDIA Jetson Orin Nano/Jetson AGX Orin
- **Radar:** Lightweight all-weather range finder (specifics to be selected; existing BST NOAA collaborations provide reference designs for ocean surface detection at 10m altitude in extreme rain/sea spray)
- **Inertial/Airspeed:** Standard aviation-grade IMU and pitot tube

### **Planning Software (Adaptation of Existing Tool)**
- **Current TRL:** Low (~3-4); field-tested for Makushin Volcano mission
- **Enhancements in Phase I:**
  - Multi-platform generalization
  - Obstacle data integration (Maxar satellite DSMs)
  - Automated vertical routing
  - Web-based user interface
- **Target Users:** NASA mission planning groups (ACERO, Earth Sciences, flight research initiatives)

---

## Use Cases & Applications

### **Primary Phase II Flight Demonstrations:**

1. **Low-Altitude Terrain Following in Mountainous Terrain**
   - **Target:** Autonomous flight maintaining 10m above obstacles in Colorado mountains (vision-based)
   - **Degraded Capability:** 20m altitude without vision system (fog/rain/night), using radar + DSM
   - **Science Relevance:** Volcanic sampling missions requiring close proximity to terrain for gas measurements
   - **Technical Challenge:** Fixed-wing aircraft dynamics at low altitude; ensuring safe obstacle avoidance while maintaining energy efficiency

2. **Long-Distance GPS-Denied Return-to-Base**
   - **Target:** Autonomous navigation from 10+ km distance back to operator's visual line of sight without GPS
   - **Method:** YOLO-based landmark tracking + semantic segmentation (roads, lakes, geographic features) for feature database matching; sensor fusion with VIO and inertial data for position triangulation
   - **Seasonal Validation:** Testing across varying conditions (winter snow, summer vegetation) to prove robustness vs. SLAM-based approaches
   - **Technical Challenge:** Drift reduction in long-range inertial navigation; feature matching resilience to seasonal/environmental changes

### **Operational Mission Applications:**

1. **Volcanic Survey Missions**
   - Ongoing NASA Ames mission in Costa Rica (2025) for trace gas sampling
   - Planned USGS missions in Chile
   - Requirement: Long-range transit (20+ miles) + low-altitude sampling near vents with obstacle avoidance

2. **Wildfire Operations**
   - Alignment with NASA ACERO project goals (wildfire detection/characterization)
   - Challenges: Mountainous terrain + reduced visibility from smoke
   - Terrain-aware flight essential for safe operations in burn areas

3. **Severe Weather Operations**
   - Hurricane reconnaissance: BST's 2024 Cat 5 flights demonstrate operational feasibility
   - Ocean surface detection at 10m altitude through extreme rain/sea spray (radar-based capability being developed with NOAA)
   - Requires robust all-weather sensor fusion

4. **Methane Leak Detection**
   - Partnership with Chevron for oil/gas facility inspection
   - Low-altitude flights over rugged terrain for plume mapping
   - Terrain relative navigation improves coverage and safety

5. **Infrastructure Inspection**
   - Power line, tower, and facility surveys at low altitude
   - Reliable low-altitude flight over complex terrain

6. **Lunar/Planetary Landing Simulation**
   - Terrestrial testbed for developing terrain relative guidance algorithms
   - Machine vision tools (semantic segmentation, feature detection) applicable to hazard detection for lunar landers
   - Open system interfaces to enable future NASA exploration work

### **Future Commercial Applications (Section 6):**

- **Urban Air Mobility (UAM):** Altitude control and obstacle avoidance for autonomous passenger aircraft
- **Cargo Delivery:** Reliable BVLOS operations over urban/rural terrain
- **Defense/Security:** GPS-denied navigation resilience against jamming

---

## Key Technical Results & Performance Claims

### **Quantitative Assertions (from proposal):**

1. **Terrain Following Accuracy:**
   - Vision-based: 10m altitude maintenance over mountainous obstacles
   - Radar-based (degraded): 20m altitude with DSM fusion

2. **GPS-Denied Navigation Range:**
   - 10+ km autonomous return-to-base without GPS
   - Tested across seasonal conditions

3. **Sensor Fusion Performance:**
   - Phase I deliverable (Month 6): Cross-validation metrics using archived flight data
   - RMS error quantification when terrain sensors are available vs. unavailable portions of flight

4. **Hardware SWaP-C:**
   - Low power consumption enabling integration on small UAS
   - Specific values TBD in Task 4 trade study

5. **Algorithm Speed:**
   - YOLO object detection: ~30 fps on embedded hardware
   - Real-time processing requirement to match aircraft dynamics

### **Precedent & Historical Performance (BST Operations):**

- **100+ missions** in Greenland in extreme cold/wind
- **Multiple successful intercepts** of volcanic plumes (Costa Rica, Hawaii, Alaska)
- **19 hurricane flights** in 2024, including Category 5 with highest turbulence ever measured on Earth
- **First company** to complete NASA's new Unmanned Commercial Aviation Services (UCAS) review
- **9 NASA Airworthiness Flight Safety Review Boards (AFSRB)** and Flight Readiness Review Boards (FRRB) completed
- **100+ FAA Certificates of Authorization (COAs)** secured/maintained across multiple states

---

## Phase I Work Plan & Deliverables

### **Tasks & Timeline (6 months):**

| Task | Description | Key Deliverables | Lead |
|------|-------------|------------------|------|
| 1: Mission CONOPS & Architecture | Scenario compilation from NASA groups; quantitative metrics; system architecture documentation | Month 2: CONOPS & architecture document to NASA | Dr. Stachura, Dr. Elston |
| 2: Planning Software Adaptation | Multi-platform generalization; obstacle data integration; automated vertical routing; web UI | Month 3: Prototype planning software available to NASA | D. Prendergast |
| 3: Algorithm Selection & Development | Optical flow, YOLO feature tracking, semantic segmentation development using archived BST flight data | Month 5: Algorithm performance data (accuracy, speed) | D. Prendergast, Dr. Heckman (CU) |
| 4: Hardware Selection & Interface Design | Sensor & compute trade study (cameras, radar, Jetson/OAK-D); modular integration interface design | Month 6: Hardware recommendations; validation testing of ≥1 algorithm on selected board | Dr.