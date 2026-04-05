# Expendable Sonobuoy-Launched Unmanned Aerial Vehicle for ASW Cued Search, Detection, Tracking and Classification

## Document Metadata
- **Type:** SBIR Phase II Proposal
- **Client/Agency:** U.S. Navy (Naval Air Warfare Center Aircraft Division – NAVAIR)
- **Program/Solicitation:** Navy SBIR Topic N251-016; Phase I Contract N6833525C0492
- **Date:** January 4, 2025 (proposal prepared); January 12, 2026 (document modified)
- **BST Products/Systems Referenced:** S0 (air-deployed UAS platform); S0-MAD (magnetic anomaly detection variant); S0-Acoustic (acoustic sensing variant); E2 (multirotor for deployment testing)
- **Key Personnel:** Dr. Jack Elston (PI/CEO, BST); Tim Rorick (Chief Technologist, Ultra Maritime); Paul DeMond (Program Manager, Ultra Maritime); Jeff Orton (Lead Engineer, QuSpin); Ed Kase (TABA Consultant)

## Executive Summary
Black Swift Technologies proposes a Phase II effort to fabricate, integrate, and validate a production-ready Sonobuoy-Launched Unmanned Aerial System (SL UAS) capable of performing magnetic anomaly detection (MAD) and deploying in-water passive acoustic sensors for anti-submarine warfare (ASW) operations. Building on Phase I success demonstrating magnetic noise performance below 20 pT/√Hz and mechanical compatibility with the LAU-126A sonobuoy launch container, Phase II will mature two specialized S0 variants—one optimized for magnetometer operations and one for acoustic sensor deployment—with integrated sensor-responsive autonomy and multi-vehicle coordination capabilities.

## Technical Approach

### Overall System Architecture
The Phase II effort will develop two complementary aircraft variants based on the BST S0 platform:
- **S0-MAD:** Optimized for low-noise magnetic anomaly detection with integrated magnetometer
- **S0-Acoustic:** Configured for water landing and deployment of in-water passive acoustic sensor array

This two-aircraft approach maximizes mission flexibility, keeps individual aircraft size and cost low, and enables advanced sensor fusion and swarming operations. The system is designed to operate autonomously in maritime environments within stringent magnetic, acoustic, and SWaP (Size, Weight, and Power) constraints while remaining compatible with the Navy's existing LAU-126A sonobuoy launch infrastructure.

### Magnetic Sensing Technical Approach
- **Sensor:** QuSpin Gen-2 QTFM (Optically Pumped Magnetometer) with <1 pT/√Hz noise spectral density
- **Platform Integration:** Modified S0 fuselage with integrated magnetometer; sensor placement via short structural booms to maximize standoff from propulsion components
- **Noise Control Strategies:** 
  - Passive magnetic shielding of propulsion components (design available if needed)
  - Optimized sensor placement and structural isolation
  - Calibration-informed compensation techniques
  - Active and passive noise control measures
- **Performance Target:** Maintain <20 pT/√Hz magnetic noise floor in 0.01–100 Hz band during dynamic flight operations
- **Validation Method:** Local flight tests with multiple heading and bank angle passes at 400+ feet altitude in low-infrastructure areas to verify noise specifications in flight

### Acoustic Sensing Technical Approach
Integrated deployable subsystem combining:
- **Hydrophone:** 5 Hz to 40 kHz bandwidth (omnidirectional response)
- **E-field Sensors:** Split into ELFE (Extremely Low Frequency Electromagnetic, 0.01–5 Hz) and ULF (Ultra Low Frequency) components to overcome physical limitations of traditional acoustic sensing at ultra-low frequencies
- **Deployment Method:** Lightweight fiber-optic tether (200 feet) to decouple sensing elements from aircraft-induced electrical and mechanical noise
- **Payload Container:** Right-cylinder configuration integrated into modified S0 fuselage with automated deployment mechanism
- **Noise Isolation:** Acceleration-canceling hydrophone design and tuned suspension system with 11-inch vertical damper disc and 2-lb terminal weight
- **Operational Requirements:** 
  - Deployment depth: up to 200 feet
  - Minimum operating duration: 60–70 minutes
  - Calibrated acoustic sensitivity: ±2 dB across spectrum
  - Data transmission: 20 nm line-of-sight RF link with whitened digital data

### Multi-Modal Sensor Fusion Concept
The integrated system enables two operational scenarios:
1. **Acoustic-cued magnetic search:** Acoustic detections from SL UAS trigger search pattern execution by magnetometer-equipped SL UAS
2. **Magnetic-cued acoustic deployment:** Magnetometer detection directs deployment of multiple acoustic SL UAS for precise target localization and classification

Higher-level data fusion and target classification algorithms remain the responsibility of Navy-provided systems and CONOPS, preserving flexibility for integration with existing Navy mission systems.

### Autonomy and Coordination (Phase II Option Tasks)
- **Sensor-Responsive Flight Behaviors:** Avionics-level hooks and control abstractions enabling magnetic or acoustic detections to drive adaptive flight behaviors
- **Inter-Vehicle Coordination:** Communication protocols designed to maintain coordination on disadvantaged networks using transient and small packet protocols
- **Information Sharing:** Distributed decision-making while preserving higher-level data fusion capabilities at Navy systems level
- **Hardware Integration:** Jetson AGX Orin onboard processing for target detection/classification (mechanical design, logical, and electrical interfaces for sensor-to-algorithm data flows)

## Products & Capabilities Described

### S0 Platform (Air-Deployed UAS)
- **What it is:** BST's proprietary small fixed-wing unmanned aircraft system designed for deployment from multiple launch methods (air-dropped from quadrotor, launched from surrogate aircraft platforms)
- **Form Factor:** Tube-launchable from LAU-126A sonobuoy launch container; expendable architecture
- **Propulsion:** Electric with brushless motors
- **Autonomy:** Established autonomous guidance and networked communication capabilities; compatible with semi-autonomous control strategies
- **Current Use Cases:** NOAA/OMAO air-deployed operations, environmental monitoring, marine research support
- **Production Status:** Aircraft in production; demonstrated deployments from NOAA P-3 and quadrotor

### S0-MAD (Magnetic Anomaly Detection Variant)
- **Integration:** Rugged sonobuoy launch container integration with mechanical folding, stowage, and deployment mechanisms
- **Magnetometer Sensor:** QuSpin Gen-2 QTFM with sub-picotesla sensitivity
- **Noise Performance (Phase I Demonstrated):** Magnetic noise floor below 20 pT/√Hz in 0.01–100 Hz band during static and ground-based testing
- **Phase II Objective:** Maintain this performance during dynamic flight operations and further improve via shielding/compensation if needed
- **Design Features:** 
  - Active and passive magnetic noise control
  - Optimized fuselage geometry for sensor standoff
  - Heading error specification: <3 nT

### S0-Acoustic (Acoustic Sensing Variant)
- **Configuration:** Modified S0 fuselage optimized for water landing
- **Payload Integration:** 
  - Hydrophone (5 Hz–40 kHz)
  - ELFE probe (0.01–5 Hz)
  - ULF probe
  - 200-foot fiber-optic tethered sensor string
- **Deployment Mechanism:** Automated release of tethered sensor array with damping and weighting system
- **Operating Life:** 60–70 minutes minimum (Navy threshold)
- **Data Link:** 20 nm line-of-sight RF connectivity
- **Depth Rating:** 200 feet

### Onboard Processing Hardware
- **Jetson AGX Orin:** GPU-based computing platform for real-time target detection and classification
- **Integration:** Mechanical and electrical interfaces designed into both MAD and Acoustic variants
- **Role:** Supports onboard detection algorithms while preserving interface hooks for Navy-provided classification systems

## Use Cases & Applications

### Primary Mission: Anti-Submarine Warfare (ASW)
- **Operational Concept:** Expendable sonobuoy-replacement system deployable from P-8A Poseidon at altitude
- **Detection Modes:**
  - Magnetic anomaly detection of submarine magnetic signatures at close range
  - Passive acoustic detection via hydrophone and E-field sensors for localization
  - Multi-modal fusion: acoustic detections cue MAD search; MAD detections cue acoustic deployment for classification
- **Deployment Profile:** Air launch from LAU-126A-equipped maritime patrol aircraft; autonomous flight to search area; acoustic variant water landing and in-water sensor deployment; data transmission to ship/aircraft for Navy-level fusion
- **Target Scenarios:** Surrogate submarine detection, tracking, and classification in maritime environments

### Secondary Applications (Cited in Proposal)
- **Unexploded Ordnance (UXO) Detection:** Leverage magnetometer capabilities for magnetic field mapping and subsurface hazard detection
- **Environmental Monitoring:** Support marine animal research organizations; real-time oceanographic and biological sensing
- **Magnetic Navigation and Surveys:** Army and Air Force ISR applications using geomagnetic field mapping
- **Infrastructure Inspection:** Coastal and maritime asset surveillance
- **Scientific Research:** Oceanographic and geophysical field campaigns

## Key Results (Phase I Demonstration)

### Phase I Success Criteria Met
- **Magnetic Noise Performance:** Validated noise floor below 20 pT/√Hz in 0.01–100 Hz band during static and ground-based testing with S0 platform and integrated magnetometer
- **Mechanical Compatibility:** Confirmed mechanical feasibility of integrating S0 within LAU-126A launch envelope, including:
  - Size, mass, center-of-gravity constraints satisfied
  - Structural loading compatible with sonobuoy deployment dynamics
  - Folding and stowage mechanisms validated
- **Sensor Integration Feasibility:** Established technical viability of integrating high-sensitivity magnetometer and deployable acoustic sensing within S0 architecture
- **Test Data:** Magnetic noise characterization plots showing performance at 0 feet and 5 feet sensor standoff from aircraft throttling at full power

### Phase II Milestone Structure (6 Milestones Identified)
1. **Flight Validation of Magnetic Performance (Task B.2):** Data proving magnetic capability meets <20 pT/√Hz and <3 nT heading error in-flight under representative maneuvers
2. **Water Landing and Acoustic Deployment (Task B.6):** Successful automated deployment of 200-foot tethered sensor string in ocean environment with sustained 60–70 minute operating life
3. **Environmental and Shock Qualification (Task B.7):** Successful LAU-126A shock testing (10G/100ms) and environmental validation (−20°C to +50°C, light rain); hardened airframes ready for P-8 deployment
4. **Flight Qualification of Platforms (Task B.8):** Complete operational scenario validation including air launch from LAU-126-equipped aircraft, water landing, acoustic deployment, payload performance verification, and surrogate target detection
5. **Phase II Option Milestone (Task O.1):** Classified algorithm integration with design ensuring unclassified operation and secure data wiping
6. **Final Validation and Phase III Transition (Task O.3):** Level 3 Technical Data Package and Integration Control Documents (ICDs) supporting Navy UCS integration; Navy operator demonstration

## Notable Details

### Partnership & Subcontractor Qualifications
- **Ultra Maritime (Subcontractor):**
  - 70-year history as world's leading sonobuoy manufacturer (>7 million units produced)
  - Extensive sensor engineering development capabilities
  - Prior SBIR and STTR program experience
  - Paul DeMond: 45+ years sonobuoy/sensor system development; INCOSE Certified Systems Engineering Professional; PM/PI for PMA-264, NUWC, DARPA programs (Q-77A, HLA, ADAR, DVLA, NUAMP, MSS, ACOMMS systems)
  - Tim Rorick: 30+ years underwater sonar ASW systems design; recognized SME in acoustic sensor design for sonobuoys
  - Commitment to manufacturing at scale post-Phase III using existing U.S. manufacturing facilities

- **QuSpin, Inc. (Consultant):**
  - 10+ years experience productizing optically pumped atomic magnetometers
  - Jeff Orton: Lead Engineer with geophysics and mobile-platform deployment expertise
  - Gen-2 QTFM sensor specifications: <1 pT/√Hz noise, compact form factor, proven field robustness