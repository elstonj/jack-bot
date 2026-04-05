# Navy SBIR Phase I Technical Narrative: Sonobuoy-Launched UAV for Anti-Submarine Warfare

## Document Metadata
- **Type**: Navy SBIR Phase I Proposal (Technical Narrative, Volume 2)
- **Client/Agency**: U.S. Navy (NAVAIR)
- **Program/Solicitation**: Navy SBIR Topic No. N251-016
- **Proposal Number**: N251-016-0021
- **Date**: Submitted 2025 (document last modified January 2026)
- **BST Products/Systems Referenced**: S0 UAS, S0 (air-deployed variant), proprietary avionics systems
- **Key Personnel**: 
  - Dr. Jack Elston (Principal Investigator)
  - Dr. Maciej Stachura (Lead Engineer)
  - Adam Sniff (Consultant - Hydrophone Design, Cetacean Research Technology)
  - Jeffrey Orton (Senior Engineer, QuSpin Inc.)

---

## Executive Summary

Black Swift Technologies proposes to develop a Sonobuoy-Launched Unmanned Aerial Vehicle (SL UAS) capable of performing magnetic anomaly detection (MAD) and passive acoustic sensing for Anti-Submarine Warfare (ASW). The solution leverages the proven S0 UAS platform—already operationally deployed by NOAA for hurricane monitoring and demonstrated in extreme environments—and integrates a QuSpin QTFM Gen-2 magnetometer and lightweight hydrophone from Cetacean Research Technology. Phase I will establish technical feasibility through sensor integration, platform modification to accommodate sonobuoy launch container constraints, laboratory validation, and development of data fusion algorithms.

---

## Technical Approach

### 1. **Magnetic Anomaly Detection (MAD) System**
- **Sensor**: QuSpin QTFM Gen-2 optically pumped atomic scalar magnetometer
- **Specifications**:
  - Sub-picotesla sensitivity (<2 pT/√Hz nominal)
  - Noise spectral density: <1 pT/√Hz
  - Dynamic range: ±100 µT (±1–150 µT per QuSpin letter)
  - Bandwidth: 0–500 Hz
  - Built-in 3-axis vector capabilities and IMU
- **Performance requirement**: 20 pT/√Hz in 0.01–100 Hz band (Navy threshold)
- **Integration approach**: Modified proprietary BST avionics with EMI shielding; technology previously validated on NASA L-band radiometer soil moisture mission
- **Platform noise mitigation**: Advanced avionics, shielding techniques, and proprietary noise compensation algorithms

### 2. **Acoustic Sensor Integration**
- **Partner**: Cetacean Research Technology (CRT)
- **Design approach**: Lightweight, ultra-low self-noise hydrophone with automatic scuttling functionality
- **Performance targets**:
  - Self-noise below sea-state zero
  - Directivity index (DI) and noise equivalent levels validated via lab testing
  - Calibration accuracy: ±2 dB threshold, ±1 dB objective
  - Frequency range and depth requirements per Navy specs (not explicitly stated)
- **Data processing**: Whitening algorithms to reduce uplink bandwidth without compromising signal fidelity

### 3. **System Integration and Validation**
- **Platform**: Modified S0 UAS with modular payload design
- **Key modifications**: Structural and aerodynamic changes to accommodate Sonobuoy Launch Container (SLC) initialization and launch dynamics (distinct from current P-3 freefall chute deployment)
- **Bench testing**: Magnetic noise characterization at sensor location against Navy thresholds
- **Simulations**: System-level validation for cued search and target detection using data fusion
- **Existing S0 airframes** will be used for sensor testing and validation during Phase I

### 4. **Data Fusion and Autonomous Operation**
- Machine learning algorithms for autonomous target tracking based on MAD and acoustic cues
- Real-time signal processing for combined magnetic and acoustic data streams
- Communication range: 50 nm minimum requirement; 163 nm objective (demonstrated in NOAA hurricane missions)

---

## Products & Capabilities Described

### **S0 UAS (TRL 9)**
- **What it is**: Air-deployed, ruggedized unmanned aerial system proven in extreme environments
- **Current use**: NOAA hurricane monitoring, deployed from P-3 Orion
- **Extreme environment credentials**: 
  - Operational in hurricane conditions
  - Proven in polar regions (Greenland with >100 flights at temperatures as low as -20°C)
  - Avionics validated for data fidelity under harsh conditions
- **Proposed use in this project**: 
  - Base platform for SL UAS development
  - Modified to integrate MAD and acoustic sensors
  - Adapted for sonobuoy launch container deployment
  - Cost-effective option: claimed as "most cost effective air-deployed UAS in the world"
- **Relevant specifications**:
  - Pre-programmed waypoint navigation capability
  - Autonomous target tracking demonstrated
  - Long-range data collection (163 nm communication range during hurricane ops)
  - Modular payload design facilitating sensor integration

### **BST Proprietary Avionics**
- **Capabilities**: 
  - EMI-sensitive equipment compatible (demonstrated on NASA radiometer project)
  - Simplified interface enabling rapid adaptation (hours-scale modification cited)
  - Over 100 successful flights in extreme conditions
  - Built-in noise compensation algorithms (derived from atmospheric sampling missions)
- **Proposed use**: Integration with QuSpin magnetometer; primary platform for MAD noise reduction

---

## Use Cases & Applications

### **Primary: Anti-Submarine Warfare (ASW)**
- Magnetic anomaly detection for submarine identification and tracking
- In-water passive acoustic sensing for submarine monitoring
- Expendable platform designed for P-8A Poseidon integration via sonobuoy launch systems
- Cued search operations using fused MAD and acoustic data

### **Secondary/Commercial Applications**
- **Federal Agencies**:
  - NOAA: Hurricane tracking, marine ecosystem monitoring
  - Department of Homeland Security: Border security, maritime surveillance
- **Private Sector**:
  - Offshore energy: Pipeline and subsea infrastructure monitoring
  - Environmental monitoring: Illegal fishing detection, underwater ecosystem studies
  - Maritime logistics: Rapid deployment for shipping lane and port inspections

---

## Key Results / Prior Validation

### **De-Risking Flight Demonstration**
- BST recently completed a successful test flight integrating QuSpin magnetometer with S0 avionics
- Location: Over oil and gas pumping station
- Flight tracks clearly displayed magnetic signature of target
- Purpose: Preliminary validation of sensor integration approach
- Significance: Early de-risking activity demonstrating feasibility before formal Phase I effort

---

## Phase I Objectives and Deliverables

### **Five Specific Technical Objectives**

**Objective 1: Demonstrate Sensor Integration Feasibility**
- Assess QuSpin QTFM Gen-2 and lightweight hydrophone integration within SL UAS
- Ensure performance maintained under operational conditions
- Evaluate noise mitigation strategies for platform-induced interference
- Validate hydrophone meets Navy sensitivity, frequency range, and depth requirements

**Objective 2: Develop Platform Compatible with Sonobuoy Launch Constraints**
- Modify S0 UAS for Sonobuoy Launch Container (SLC) payload and weight constraints
- Validate aerodynamic and structural modifications for successful launch
- Ensure post-deployment functionality under varying environmental conditions

**Objective 3: Validate Sensor Performance in Controlled Environments**
- Laboratory simulations and bench testing of magnetometer noise performance
- Hydrophone acoustic sensitivity characterization
- Compliance verification: 20 pT/√Hz magnetometer noise in 0.01–100 Hz band
- Calibration accuracy validation: ±2 dB threshold, ±1 dB objective
- Determine if design modifications needed before flight testing

**Objective 4: Develop and Evaluate Data Fusion Algorithms**
- Design and test algorithms combining MAD and acoustic sensor outputs
- Real-time signal processing feasibility evaluation
- Machine learning-based techniques for optimized detection on simulated datasets

**Objective 5: Demonstrate Autonomous Operation and Communication**
- Test autonomous target tracking based on MAD and acoustic cues
- Validate communication/control systems for ≥50 nm range (objective: 163 nm)
- Evaluate data transmission and onboard processing constraints

### **Phase I Deliverables**
1. **Preliminary Design Report**: Sensor integration specs, simulation results under realistic mission scenarios
2. **Prototype Development**: Functional laboratory-testable prototype; structural analysis of payload integration
3. **Laboratory Validation Report**: Magnetic and acoustic sensor test results, noise characterization, calibration accuracy, Phase II recommendations

### **Phase I Base and Option Tasks**

| Task | Duration | Description |
|------|----------|-------------|
| **B.1** | Months 1–6 | Requirements analysis and preliminary design; collaboration with CRT on hydrophone specs; system concept of operations documentation |
| **B.2** | Months 1–6 | SLC compatibility evaluation; airframe modifications; iterative CAD testing and physical prototyping |
| **B.3** | Months 2–9 | Laboratory sensor integration and testing; magnetometer compliance validation; hydrophone calibration; data fusion algorithm development using simulated scenarios |
| **B.4** | Months 6–12 | Prototype fabrication; simulated deployment testing for SLC compatibility; autonomy, communication range, and power efficiency evaluation |
| **O.1** | Months 7–12 | Local flight testing at BST Longmont, Colorado facility; iterative design improvements to reduce Phase II risks |
| **O.2** | Months 9–12 | Initiate FAA and Navy certification/approvals for Phase II flight testing; CAD launch compliance documentation; regulatory coordination |
| **O.3** | Months 7–12 | Cartridge Actuated Device (CAD) launch modifications; structural analysis and deployment simulations; BST preliminary work for NOAA/Air Force CAD launches leveraged |

---

## Notable Details

### **Technical Innovation Highlights**
- **Platform Noise Reduction**: Advanced avionics and shielding designed to mitigate airborne MAD interference (critical limitation in existing systems)
- **Enhanced Autonomy**: ML-based algorithms enabling dynamic mission adaptation and autonomous submarine tracking
- **Cost Effectiveness**: Leveraging proven S0 design to minimize development costs; target unit cost <$10,000 in quantities of 100

### **Partnerships and Subcontractors**
- **QuSpin Inc.**: Provides QTFM Gen-2 magnetometer and integration expertise; committed letter of support
- **Cetacean Research Technology**: Hydrophone design, fabrication, and calibration (not to exceed $20,000); Adam Sniff as consultant
- **Test Site**: Sunny Slope Sod Farm, Longmont, Colorado (private location for flight testing)

### **Facilities and Equipment**
- **BST Infrastructure**: Prototyping/fabrication lab (3D printers, CNC, composite workstations), electronics integration/testing lab (soldering, oscilloscopes, environmental chambers)
- **Equipment Purchases Justified**: High-sensitivity magnetometer testing rig ($11,500) for QuSpin QTFM Gen-2 evaluation in simulated flight conditions
- **Environmental Compliance**: All BST facilities certified for federal, state, local environmental regulations; flight testing in remote areas to minimize noise impact; certified recycling and waste management

### **Competitive Positioning**
- **Existing Competitors**: AeroVironment Switchblade, Raytheon Coyote, Anduril Altius-600 (all tube-launched UAS platforms)
- **BST Advantage**: Won NOAA air-deployed UAS contract over Anduril; proven superiority in extreme operational environments; existing operational history with P-3/NOAA integration
- **Market Opportunity**:
  - Global ASW UAS market projected at $2.1 billion by 2030
  - Environmental monitoring market valued at >$17 billion (2023)
  - Significant dual-use commercialization potential

### **Related BST Experience**
- S0 UAS operational with NOAA; preliminary MAD testing with QuSpin already completed
- Demonstrated autonomous waypoint navigation and target tracking
- 163 nm communication range achieved during hurricane sampling operations
- Avionics adapted in hours to accommodate new sensor requirements (simplified interface design)
- Successful integration of EMI-sensitive equipment on past projects (NASA radiometer)

### **Phase II Transition Strategy**
- Close coordination with NAV