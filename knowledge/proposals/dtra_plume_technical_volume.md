# DTRA Plume Technical Volume

## Document Metadata
- Type: SBIR Phase I Technical Volume / Proposal
- Client/Agency: Defense Threat Reduction Agency (DTRA)
- Program/Solicitation: DTRA SBIR Topic "PLUMES" (2025)
- Date: Submitted May 2025 (document modified through May 21, 2025)
- BST Products/Systems Referenced: S2 UAS, SwiftCore Flight Management System, SwiftTab, SwiftStation
- Key Personnel: Dr. Jack Elston (CEO, Principal Investigator), Dr. Maciej Stachura (CTO, Project PI), Beck Cotter (last editor)
- Subcontractors/Partners: Brookhaven National Laboratory (BNL), EKase Consulting (Technical and Business Assistance)

## Executive Summary

Black Swift Technologies proposes to develop an AI-driven, autonomous Unmanned Aircraft System (UAS) capable of real-time detection, tracking, and three-dimensional reconstruction of airborne plumes generated during explosive tests. The system combines BST's proven fixed-wing UAS platforms (S2) with advanced neural volumetric reconstruction algorithms (Neural Radiance Fields and related techniques) developed by Brookhaven National Laboratory to enable autonomous plume characterization without manual pilot intervention. Phase I focuses on demonstrating technical feasibility through laboratory and field validation, while establishing performance requirements for government UAS platforms that meet NDAA and Blue UAS compliance standards.

## Technical Approach

### Core Innovation
The proposal leverages Neural Radiance Fields (NeRFs) and time-dynamic neural scene representation techniques to reconstruct multidimensional plume volumes from sparse, non-overlapping imagery acquired by UAS-mounted cameras. Unlike traditional photogrammetry (which requires dense, precisely overlapping images), NeRFs enable 3D reconstruction from limited viewpoints and can model semi-transparent or evolving volumes typical of explosive plumes.

### Key Technical Components:
1. **Neural Volumetric Reconstruction**: Application of NeRF variants including:
   - K-Planes and HexPlane for time-dependent scene reconstruction
   - Dex-NeRF for handling semi-transparent media
   - NeRFPlayer and Gaussian Splatting for near-real-time processing

2. **Multi-Sensor Data Fusion**: Open-source Python-based platform to:
   - Synchronize imagery from multiple UAS-mounted EO/IR cameras
   - Integrate GPS/IMU telemetry with precise time-tagging
   - Support real-time and post-flight processing pipelines
   - Interface directly with BST's SwiftCore Flight Management System for closed-loop autonomous control

3. **Sensor Integration Architecture**:
   - Modular, sensor-agnostic framework supporting varied camera models and data formats
   - Integration with range-based sensor systems (LiDAR, radar) where available
   - Support for adaptive frame-rate controls and onboard quality-check routines

### Technical Risk Mitigation:
- **Reconstruction Fidelity Risk**: Establish confidence bounds through controlled lab experiments; use BST's high-endurance fixed-wing platforms to increase data coverage density; leverage gimbal systems with 0.5° pointing accuracy and dual RTK-GPS providing 3-5 cm positioning and <0.2° heading accuracy
- **Real-Time Processing Risk**: Benchmark NeRF latency early; implement hybrid on-board/off-board processing with low-latency preview models driving navigation while full reconstructions occur asynchronously or ground-based
- **Sensor Integration Risk**: Build modular architecture from outset; leverage BST's proven experience integrating tightly coupled avionics and payload systems; test early on BST S2 platform in known configuration

## Products & Capabilities Described

### Black Swift Technologies S2 UAS
- **Description**: 20-pound fixed-wing UAS developed for NASA, NOAA, and USGS missions in extreme environments
- **Proposed Use**: Primary platform for field testing and validation; equipped with synchronized EO/IR cameras and attitude-stabilized mounts for plume reconstruction
- **Specifications**: 
  - High-endurance fixed-wing design
  - Proven operational history in volcanic calderas, active wildfires, Category 5 hurricanes
  - NDAA-compliant and Blue UAS-approved
  - Dual RTK-GPS with 3-5 cm positioning accuracy and <0.2° heading accuracy
  - Capable of mounting Trillium gimbals (0.5° pointing accuracy)
  - Integrates with SwiftCore Flight Management System

### SwiftCore Flight Management System
- **Description**: BST's custom-developed autopilot and flight management system
- **Use in Context**: Receives closed-loop plume reconstruction outputs to enable autonomous flight path adjustments; directly interfaces with multi-sensor processing pipeline
- **Capabilities**: Supports AI-driven flight control based on plume structure and uncertainty estimation

### Multi-Sensor Data Processing Platform (Phase I Deliverable)
- **Description**: Open-source Python-based software infrastructure for data acquisition, synchronization, and processing
- **Modules**: 
  - Multi-camera image ingestion and time-synchronization
  - GPS/IMU telemetry integration
  - NeRF-based volumetric reconstruction
  - Classification (plume vs. background discrimination)
  - Confidence estimation and data thinning for onboard processing
  - Visualization interfaces compatible with SwiftTab and SwiftStation
- **Interoperability**: Designed for compatibility with government-approved UAS platforms meeting NDAA and Blue UAS criteria

### Related BST Capabilities Referenced
- **SwiftTab/SwiftStation**: Ground station tools for visualization and mission planning
- **Methane Detection Payload**: Prior experience with direct measurement plume tracing using eddy covariance methods and 3D wind sensing

## Use Cases & Applications

### Primary: DTRA Explosive Test Support
- Real-time detection, tracking, and characterization of plumes from explosive tests
- Autonomous navigation through plume environments to optimize sensor data collection
- Reduction of manual UAS operation and associated operational risk in hazardous environments
- Support for post-test analysis, simulation validation, and agent dispersion modeling

### Secondary Federal Applications:
1. **EPA**: Airborne emissions monitoring for industrial compliance, fugitive emissions detection, dispersion modeling
2. **FEMA**: Rapid plume characterization following chemical/radiological accidents, support for disaster response teams
3. **NOAA**: Wildfire smoke tracking, atmospheric profiling, Earth system modeling
4. **NASA**: Aerosol distribution measurement, Earth science campaigns
5. **DOE**: Emissions monitoring from nuclear/fossil energy sites, hazardous release prediction validation
6. **DoD Broader**: Chemical/biological detection during operations, environmental hazard monitoring during training, nuclear incident response, treaty verification support

### Private Sector / Commercial:
- Oil and gas methane leak detection and localization (projected $150M+ market by 2027)
- Chemical manufacturing and refinery emissions monitoring
- Mining and waste management site characterization
- Utilities and infrastructure hazard detection
- Industrial safety and regulatory compliance monitoring
- Flare stack and venting system anomaly detection

## Key Technical Objectives (Phase I)

### Objective 1: Foundational Demonstration of Neural Volume Reconstruction
Reconstruct static volumes (opaque targets: cube, balloon, cotton balls) in laboratory using multi-angle single-camera imagery; establish performance baselines including reconstruction accuracy, confidence intervals, and required image density.

### Objective 2: Multi-Sensor Data Acquisition and Processing Platform Development
Create open-source Python infrastructure supporting synchronized multi-camera acquisition, metadata tagging, automated preprocessing, NeRF-based rendering, and integration with SwiftCore Flight Management System.

### Objective 3: Dynamic Volume Reconstruction in Lab
Test NeRF variants (K-Planes, Dex-NeRF) on moving/morphing targets (balloons, robotic platforms, fog surrogates) to characterize performance scaling with scene complexity, transparency, translation rate, and volumetric evolution.

### Objective 4: Field Demonstration Using UAS-Mounted Systems
Validate integrated system in outdoor environment using BST S2 with synchronized EO/IR cameras; reconstruct both static and dynamic test volumes; compare against structure-from-motion photogrammetry and in-situ measurements.

### Objective 5: UAS Sensing and Control Requirements
Define threshold accuracy requirements for:
- Intrinsic camera parameters (focal length, principal point, resolution)
- Extrinsic parameters (camera pose: sub-degree rotation, centimeter-level translation)
- Position accuracy (leveraging RTK-GPS capabilities)
- Develop preliminary flight planning framework for automated plume mapping

### Objective 6: Security Framework
Define cybersecurity and data protection protocols aligned with DFARS 252.204.7012 and NIST 800-171 for Controlled Unclassified Information.

## Phase I Statement of Work (8 Tasks, 7-Month Performance Period)

**Task 1: Kickoff and Requirements** - Define accuracy needs for dynamic plumes; conduct trade study of government UAS (Blue List options) and camera/gimbal capabilities; produce requirements document

**Task 2: Data Acquisition and Processing Software** - Develop modular, open-source Python platform for multi-sensor synchronization, image preprocessing, NeRF pipeline management, and SwiftCore integration; include unit tests and simulated sensor validation

**Task 3: UAS Payload Setup** - Procure and integrate camera payload on BST UAS maintaining NDAA compliance; coordinate with BNL on data formats and telemetry requirements

**Task 4: Dynamic Volume Reconstruction (Lab)** - Test NeRF methods on moving/morphing targets; validate against known motion parameters; assess performance under varying complexity, transparency, and sensor density

**Task 5: Static and Dynamic Reconstructions (Field)** - Conduct UAS flight tests using S2; collect imagery of stationary and moving targets; compare to photogrammetry baselines and direct measurements; assess robustness to environmental factors

**Task 6: UAS Sensing and Control** - Analyze impact of sensor resolution, geotagging accuracy, frame rate, and camera pointing on reconstruction; map requirements against BST platforms and NDAA/Blue UAS compliance; develop preliminary flight planning framework

**Task 7: Security Framework** - Define cybersecurity protocols for data protection, transmission, and access control; develop implementation-ready plan for Phase II; address DFARS, NIST 800-171, and DoD enterprise system compatibility

**Task 8: Final Report** - Comprehensive report documenting all experimental results, software architecture, performance metrics, lessons learned, and Phase II recommendations

## Key Results / Anticipated Deliverables

### Technical Deliverables:
1. Demonstrations of static and dynamic volumetric reconstruction in controlled and field settings
2. Open-source multi-sensor data acquisition and processing software platform
3. Quantified reconstruction accuracy and performance metrics (accuracy, latency, required sensor density)
4. Design guidelines for UAS payload and avionics requirements (camera resolution, frame rate, timing precision, pointing accuracy)
5. Performance envelope curves defining minimum conditions for real-time operation
6. UAS sensing and control requirements document with threshold metrics
7. Security framework and cybersecurity implementation plan
8. Comprehensive final technical report with experimental analysis and Phase II roadmap

### Performance Expectations:
- Achieve reconstruction accuracy sufficient for real-time plume tracking in explosive test scenarios
- Maintain latency tolerances compatible with autonomous flight control feedback loops
- Validate feasibility on government UAS platforms meeting NDAA and Blue UAS compliance
- Establish clear compatibility with current FAA-authorized commercial UAS systems

## Phase II Vision and Transition

Phase I is explicitly structured as a foundation for Phase II full system development:
- Integrate validated reconstruction algorithms with adaptive flight control for autonomous plume tracking
- Extend software platform to support onboard edge processing and multi-agent UAS coordination
- Incorporate physical priors (wind vector fields, dispersion models) into reconstruction algorithms
- Implement real-time uncertainty-based task planning enabling autonomous data gap filling
- Conduct prototype integration on BST S2 with pathway to alternate platforms (Blue UAS, rotary-wing)
- Achieve operational readiness for live DTRA explosive test demonstrations

## Regulatory and Security Clearances (Phase II Preparation)

- BST has completed 140+ FAA Certificates of Authorization (COAs) for NAS operations
- Team experienced with NASA Airworthiness Flight Safety Review Board (AFSRB) and Flight Readiness Review (FRR) processes
- Platforms approved by AFWERX (S0 for swarming, E2 for advanced sensor testing)
- Phase II will implement DFARS 252.204.7012 and NIST 800-171 compliance for CUI
- Will coordinate with Defense Technology Security Administration (DTSA) for export control compliance if applicable
- Personnel screening and facility access controls to be implemented as needed