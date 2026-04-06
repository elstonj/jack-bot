# Coordinated UAS-Based Plume Tracking Technical Volume

## Document Metadata
- Type: SBIR Phase I Proposal (Technical Volume)
- Client/Agency: Defense Threat Reduction Agency (DTRA)
- Program/Solicitation: DTRA252-001 PLUMES; Proposal Number T252-001-0052
- Date: 2025 (submitted May 21, 2025)
- BST Products/Systems Referenced: S2 UAS, SwiftCore™ Flight Management System, SwiftTab, SwiftStation
- Key Personnel: Beck Cotter (last editor)

## Executive Summary

Black Swift Technologies (BST) proposes an AI-integrated, autonomous UAS system to enable real-time detection, tracking, and 3D volumetric reconstruction of airborne plumes produced during explosive tests. The system combines Neural Radiance Fields (NeRFs) and dynamic scene reconstruction algorithms with BST's proven fixed-wing UAS platforms and vertically-integrated avionics to address DTRA's critical need for autonomous plume characterization in operationally relevant conditions. Phase I will establish technical feasibility through controlled laboratory experiments and field demonstrations, culminating in performance requirements and software infrastructure for Phase II prototyping.

## Technical Approach

**Core Innovation**: Application of Neural Radiance Fields (NeRFs) and related neural volumetric reconstruction techniques to reconstruct dynamic, semi-transparent volumes (plumes) from sparse, multi-view imagery collected by airborne platforms.

**Key Technical Elements**:
- Neural volumetric reconstruction using NeRF-based algorithms and extensions (K-Planes, HexPlane, Dex-NeRF) for time-varying, semi-transparent scenes
- Multi-sensor data fusion platform integrating EO/IR cameras, GPS/IMU telemetry, and environmental sensors
- Integration with BST's SwiftCore™ avionics to enable closed-loop autonomous flight control based on plume reconstruction
- Physics-informed neural networks (PINNs) for enhanced accuracy
- Gaussian Splatting and NeRFPlayer techniques for near-real-time reconstruction
- Modular, open-source Python-based software infrastructure for sensor-agnostic deployment

**Approach Rationale**: Unlike traditional photogrammetry requiring dense, overlapping images and tightly controlled geometry, NeRFs can reconstruct complex multidimensional features from sparse, non-overlapping viewpoints—ideal for dynamically navigating UAS in outdoor environments.

## Products & Capabilities Described

### S2 UAS
- **What it is**: 20 lbs fixed-wing high-endurance aircraft designed by BST for atmospheric science missions
- **Use case**: Primary platform for Phase I field testing and operational deployment
- **Specifications**: Proven in extreme environments (volcanic calderas, active wildfires, Category 5 hurricanes) with NASA, NOAA, and USGS; equipped with dual RTK-GPS (3-5 cm positioning accuracy, <0.2° heading accuracy), compatible with attitude-stabilized gimbals (Trillium and others, ~0.5° pointing accuracy), capable of multi-hour endurance
- **Advantages**: Stable flight platform engineered for challenging conditions; proven onboard data collection of 3D wind data, aerosol concentrations, and thermal gradients

### SwiftCore™ Flight Management System
- **What it is**: BST's custom avionics suite
- **Use case**: Integration point for closed-loop flight control driven by plume reconstruction outputs; enables autonomous adaptive sampling based on uncertainty estimation
- **Capability**: Tight coupling between sensing and control for responsive plume tracking

### SwiftTab/SwiftStation
- **What it is**: Ground-based data visualization and management tools
- **Use case**: Integration with processing pipeline for visualization of reconstructions and real-time operational feedback

### Software Platform (to be developed)
- **What it is**: Modular, open-source Python-based infrastructure for multi-sensor data acquisition and processing
- **Capabilities**:
  - Synchronized/time-referenced image acquisition from multiple sensors
  - Automatic preprocessing, image indexing, time synchronization
  - NeRF-based volumetric rendering pipeline integration
  - Modules for plume classification, confidence estimation, data thinning
  - Onboard and real-time processing support
  - Interface with SwiftCore for flight path updates
  - Support for EO/IR cameras, GPS/IMU, wind sensors, LiDAR, and other modalities

## Use Cases & Applications

### Primary (DTRA - Defense/Test Support)
- **Explosive test plume characterization**: Real-time autonomous detection, tracking, and 3D reconstruction of plumes from explosive tests
- **Agent dispersion modeling**: Support for chemical/biological/radiological dispersal analysis
- **Post-test analysis**: High-resolution data collection in operationally relevant conditions to improve simulation validation
- **Nuclear incident response**: Safe, rapid characterization of plumes following nuclear events
- **Treaty verification**: Site characterization and sampling support

### Secondary (Federal Agencies & Commercial)
- **EPA environmental monitoring**: Emissions monitoring, fugitive emission detection, industrial facility compliance assessment, air quality metrics (methane, ozone, particulates)
- **FEMA emergency response**: Chemical and radiological disaster assessment, hazmat response, airborne threat characterization
- **Oil and gas industry**: Methane leak detection and localization (existing BST capability demonstrated with Chevron facilities)
- **Wildfire monitoring**: Smoke plume tracking and particulate characterization (demonstrated with NOAA)
- **Volcanic monitoring**: SO₂ and aerosol measurement (demonstrated at Makushin, Turrialba)

## Key Results (Anticipated)

**Phase I Objectives & Deliverables**:

1. **Foundational Demonstration of Neural Volume Reconstruction**
   - Reconstruct static volumes in controlled lab (1-10 m³ capture domain) using NeRF-based algorithms
   - Establish performance baselines (reconstruction accuracy, confidence intervals, required image density)
   - Deliverable: Reconstruction representations and validation analysis

2. **Multi-Sensor Data Acquisition and Processing Platform**
   - Open-source software framework for synchronized multi-sensor data management
   - Python-based modular interfaces for various camera models and sensor buses
   - Full pipeline from image ingestion to neural reconstruction and visualization
   - Deliverable: Agnostic, open-source software platform

3. **Dynamic Volume Reconstruction (Laboratory)**
   - Test NeRF performance on moving/evolving targets (balloons on moving platforms, morphing targets, semi-transparent surrogates)
   - Evaluate scenarios: translation along defined paths, volumetric change, combined motion/evolution, semi-transparency
   - Output metrics: reconstruction latency, sensor density requirements, scene evolution vs. performance relationships
   - Deliverable: Dynamic reconstruction representations and validation analysis

4. **Field Demonstrations (Static and Dynamic)**
   - UAS-mounted EO/IR imaging of stationary and moving targets
   - Comparison against structure-from-motion photogrammetry and physical measurements
   - Robustness assessment to lighting variations, wind, motion blur
   - Deliverable: Field reconstruction representations and validation analysis

5. **UAS Sensing and Control Requirements**
   - Establish threshold requirements for camera intrinsic parameters (focal length, principal point, resolution) and extrinsic parameters (position/attitude accuracy)
   - Define geotagging accuracy needs (centimeter-level position with RTK GPS, sub-degree attitude possible with commercial gimbals)
   - Develop framework for automatic flight planning
   - Deliverable: List of threshold requirements and metrics relating plume state accuracy to sensor accuracy

6. **Security Framework**
   - Cybersecurity and data protection aligned with DFARS 252.204.7012
   - Address secure storage, transmission, processing of plume data
   - Propose Zero Trust architecture options and DoD enterprise system compatibility
   - Deliverable: Modular, implementation-ready security plan

## Notable Details

### Partnership & Collaboration
- **Brookhaven National Laboratory (BNL)**: Leadership in neural volumetric reconstruction, NeRF applications; collaborative Phase I effort
- **Regulatory/Compliance**: NDAA compliance, Blue UAS approval pathway; BST has completed NASA AFSRB/FRR processes and received AFWERX approvals

### BST Competitive Advantages
- **Vertically integrated**: Custom avionics (SwiftCore), sensors, AI-driven flight control, and ground visualization developed in-house
- **Operational history**: Decade of proven UAS operations in extreme environments; over 140 FAA Certificates of Authorization (COAs)
- **Proven platforms**: S2 already operational with NASA, NOAA, USGS; existing methane detection and volcanic plume sampling missions
- **Hardware maturity**: Platform already meets government requirements (RTK-GPS dual receivers, gimbal integration, NDAA compliance)

### Key Technical Risks & Mitigations
1. **Inadequate reconstruction fidelity in sparse/dynamic scenes**: Mitigated by controlled lab experiments, adaptive frame-rate controls, BST's high-endurance platform for increased data density, and proven gimbal/GPS accuracy
2. **Real-time processing latency**: Hybrid on-board/off-board processing, low-latency preview models (Gaussian Splatting) driving navigation with full reconstructions asynchronous
3. **Sensor integration/platform compatibility**: Modular open-source architecture, BST's proven integration expertise, early testing on known S2 configuration

### Commercial Pathway
- **Primary market**: DTRA Phase III demonstration, broader DoD WMD countermeasures (JPEO-CBRND, DARPA, AFRL)
- **Secondary markets**: EPA environmental monitoring, FEMA emergency response, commercial oil/gas leak detection, wildfire monitoring
- **Modularity**: System designed for deployment across fixed-wing or rotary-wing platforms, supporting rapid adoption via SBIR Phase III sole-source or OTA vehicles
- **Timeline**: Phase I establishes feasibility; Phase II prototyping with live demonstration; Phase III operational evaluation at DTRA test site

### Phase II Transition Plan
- Foundational capabilities from Phase I directly integrated with adaptive flight control algorithms
- Software evolution to support onboard/edge processing, multi-agent coordination, physical priors (wind vectors, dispersion models)
- Sensor fusion validation informs tighter navigation/data collection integration with real-time tasking based on uncertainty quantification
- Platform refinements and payload integration informed by Phase I hardware tolerance insights
- Modular architecture enables expansion to alternate airframes (Blue UAS, NDAA-compliant systems)

### Compliance & Security
- DFARS 252.204.7012 and NIST 800-171 (CUI) for Phase II
- ITAR/EAR export control measures as needed
- No foreign nationals proposed
- Early engagement with DTRA system integration teams for test range compatibility (radar tracking, communications, GPS-denied navigation)

---

**Note**: This proposal is a comprehensive SBIR Phase I technical submission demonstrating substantial domain expertise in atmospheric sensing UAS, clear alignment with DTRA's unmet needs, and a structured, risk-mitigated approach to technology maturation. The proposal leverages BST's operational heritage while introducing state-of-the-art AI/ML (NeRFs) in a dual-use context with clear commercialization pathways.