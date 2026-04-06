# B.1: Requirements Analysis and Preliminary Design

## Document Metadata
- **Type:** Requirements Analysis & Preliminary Design (Phase 1 Deliverable)
- **Client/Agency:** U.S. Navy
- **Program/Solicitation:** Navy SBIR - Magnetometer (Sonobuoy Launched UAS for ASW Re-Acquire, Tracking, and Classification)
- **Date:** Created 2025-09-16; Modified 2025-10-13
- **BST Products/Systems Referenced:** S0 UAS platform, S0-AD (modified variant), BST avionics systems
- **Key Personnel:** Maciej Stachura (last editor)
- **Partner Organizations:** CRT (acoustic sensor collaboration), QuSpin (magnetometer supplier)

## Executive Summary
This Phase 1 deliverable outlines the requirements analysis and preliminary design for integrating a QuSpin QTFM Gen-2 magnetometer and lightweight hydrophone onto the Navy's Sonobuoy Launcher (SL) UAS platform, based on BST's S0 UAS experience. The document details Navy operational requirements, identifies critical design challenges (particularly platform magnetic noise and sensor integration), and establishes a task list for interim reporting focused on hardware BOM, mass estimates, sensor proximity decisions, and requirement verification.

## Technical Approach

### Overall System Integration Strategy
- Leverage BST's existing S0 UAS platform as the baseline for the SL UAV derivative
- Integrate QuSpin QTFM Gen-2 magnetometer for Magnetic Anomaly Detection (MAD) capability
- Integrate CRT hydrophone for in-water passive acoustic sensing
- Utilize BST avionics systems and existing compute/control infrastructure
- Employ Jetson Orin SBC for on-board processing (Navy-specified requirement, though noted as oversized for current needs)

### Critical Technical Challenges Identified

**Magnetometer Integration:**
- Platform magnetic noise is 10-30x above requirements (250-600 pT/√Hz vs. 20 pT/√Hz threshold)
- Electric motor generating ~100 nT of noise—primary culprit requiring magnetic shielding
- Motor aliasing identified as the biggest problem since filters cannot mitigate aliased noise
- Magnetic field calibration essential but must be done in-air through calibration flight:
  - Multiple orientations matching in-flight conditions
  - Pass through same point with level wings at different headings
  - Conduct at high altitude (120-150m FAA limit or PNG limit)
  - Follow with survey of calibration area
- Heading error currently 120-150 nT from platform magnetics (calibratable but critical to address)
- Solutions: magnetic shielding of motor (can compensate heading error offset), relocating motor away from propeller via torque tube (improves shielding effectiveness by ~10x)

**Acoustic Sensor Integration:**
- CRT hydrophone is analog output; requires ADC/recording system (external MCU responsibility, not CRT scope)
- Tether length and cable reel space required for depth operation (200-400 ft objective)
- Deployment time constraint (60-120s) drives mechanical design

## Products & Capabilities Described

### S0 UAS Platform
- **What it is:** BST's proven small UAS baseline platform
- **Proposed Use:** Foundation for SL UAV derivative with magnetometer and hydrophone payloads
- **S0-AD variant:** Modified version being evaluated; requires assessment of modifications needed to accommodate payload weight increase
- **Performance baseline:** 60 m/s cruise speed; adding payload requires motor/prop efficiency update
- **Existing capabilities leveraged:** Avionics systems, autonomous waypoint/orbit capability, control systems

### QuSpin QTFM Gen-2 Magnetometer
- **What it is:** Quantum scalar magnetometer from QuSpin (third-party sensor)
- **Proposed Use:** Primary sensor for MAD system
- **Specifications/Requirements to be met:**
  - Platform magnetic field noise: <1 pT/√Hz (DC to 100 Hz)
  - Dynamic range: ±100 μT per axis, no dead zones
  - Accuracy: 1 nT across -0°C to +50°C
  - In-air noise threshold: 20 pT/√Hz (0.01-100 Hz band)
  - Must support real-world operational conditions

### CRT Hydrophone
- **What it is:** Lightweight hydrophone for passive acoustic detection (supplied by partner CRT)
- **Proposed Use:** In-water acoustic sensor for ASW applications, deployed via tether
- **Specifications/Capabilities:**
  - Frequency coverage: ~1 Hz to 25 kHz (threshold 0.01-2.5 kHz; objective 0.001-25 kHz)
  - Operating depth: 200 ft threshold / 400 ft objective
  - Operating life: 60 min threshold / 70 min objective
  - Directivity: Omnidirectional (threshold); higher gain or direction-finding (objective—not feasible per CRT)
  - Noise performance: Low-noise design below sea-state-zero or near it across bandwidth
  - Calibration: ±3 dB easily achievable; ±2 dB likely; ±1 dB possible pending testing
  - Deployment time: 60-120 seconds

### Jetson Orin SBC
- **What it is:** NVIDIA Jetson Orin single-board computer
- **Proposed Use:** On-board processing platform (Navy-mandated)
- **Specifications (Navy requirement):**
  - AI performance: ≥275 TOPS (INT8)
  - GPU: ≥1.3 GHz clock, ≥2048 CUDA cores, ≥64 Tensor cores
  - CPU: ≥12 cores @ 2.2 GHz
  - Memory: ≥64 GB RAM
- **BST Assessment:** Noted as oversized/overkill for computational needs and large for airframe scale; Navy unlikely to accept substitution despite size/weight concerns

## Use Cases & Applications

### Primary Mission: Anti-Submarine Warfare (ASW)
- **Application:** Re-acquisition, tracking, and classification of submarine targets
- **Operational Concept:** Sonobuoy-launched autonomous UAS conducting pre-programmed surveys and autonomous target tracking (Phase III objective)
- **Detection Method:** Dual-sensor approach combining MAD (magnetometer) and passive acoustic (hydrophone) for complementary detection/classification

### Operational Deployment Context
- **Packaging:** Must fit LAU-126A Sonobuoy Launch Container (SLC) or equivalent
- **Launch envelope:** Full Navy sonobuoy production specifications (rocket-boosted deployment)
- **Range:** 20 nm LOS (threshold); 50 nm (objective)
- **Endurance requirement:** 70 minutes minimum

## Key Design Requirements (Derived from RFP)

### Platform Specifications
- **Weight:** Max 39 lb (17.7 kg) bare (excluding SLC)
- **Stowed dimensions:** 4.875" dia × 36" length (12.38 cm × 91.44 cm)
- **Shelf life:** 9 years
- **Cruise speed:** 70 knots threshold (note: 10 m/s faster than S0)
- **Altitude:** 500-2,000 ft operational
- **Payload volume:** >94.4 in³ (1,546.94 cm³)
- **Temperature range:** -20°C to +50°C operation; light rain capable (>1 nm visibility)
- **Cost target (Phase III):** <$10,000 in quantities of 100

### Autonomy Requirements
- **Threshold:** Autonomous waypoint/orbit flight (currently available)
- **Objective:** Autonomous target tracking cued by MAD system (to be developed in Phase II)

### Command & Control
- Phase I-II: Any C2 architecture acceptable
- Phase III: Must conform to UAS Control Segment (UCS) Architecture standard

## Phase 1 Task List (Interim Report Requirements)

1. **Hardware BOM:** Complete list of magnetic sensor, hydrophone, and compute node hardware to be added
2. **Mass budget:** Estimate weight increase to determine S0-AD modification requirements
3. **Magnetometer proximity:** Determine required distance/location; plan ground testing on S0-AD (noted as critical despite being Phase B.3 task)
4. **Sonobuoy launcher specs:** Obtain Navy Sonobuoy Launcher (LAU-126A) detailed specifications
5. **Acoustic tether sizing:** Determine tether length required for acoustic sensor deployment
6. **Requirement traceability:** Enumerate all RFP requirements and ensure measurable requirements have defined verification methods

## Notable Details

### Risk Mitigation Strategy
- Existing BST avionics and CRT hydrophone designs reduce integration risk
- Pre-Phase 1 flight data already collected on S0 with magnetometer (heading error issues documented)
- Ground testing on S0-AD planned to "solidify design" before formal Phase B.3 sensor testing

### Key Technical Insights
- **Motor noise is dominant problem:** ~100 nT baseline requires 10-30x noise reduction
- **Calibration is essential:** Heading error (120-150 nT) is within signal detection band; must be calibrated out via in-air calibration flights
- **Aliasing concerns:** Magnetic noise aliasing is unfilterable and mimics signatures; magnetic shielding is required solution
- **Motor placement optimization:** Moving motor away from propeller via torque tube can improve shielding effectiveness by ~10x

### CRT Partnership Notes
- CRT responsible for specifying ADC/recording system (external to hydrophone scope)
- CRT responsible for scuttle logic, data whitening, and signal processing (built into MCU/software)
- CRT acknowledged unable to provide direction-finding capability (threshold is omnidirectional only)
- CRT able to achieve most acoustic requirements with low-noise design

### Performance Capability Gaps Identified
- Magnetometer heading error (currently 120-150 nT vs. 1 nT target)—mitigation via calibration + shielding
- Acoustic frequency coverage below 1 Hz not feasible (threshold 0.01 Hz)
- Direction-finding not achievable (objective only)
- Jetson Orin size/weight vs. actual computational need (Navy mandate overrides optimization)

### Next Design Phases
- B.2: Detailed design of magnetic shielding for motor
- B.3: Sensor integration and testing
- Phase II: Autonomous MAD-cued target tracking development