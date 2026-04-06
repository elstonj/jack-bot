# Navy SBIR Phase I Proposal: Sonobuoy-Launched UAS for Anti-Submarine Warfare

## Document Metadata
- **Type:** Navy SBIR Phase I Proposal – Technical Narrative
- **Proposal Number:** N251-016-0021
- **Topic Number:** N251-016
- **Client/Agency:** U.S. Navy
- **Program/Solicitation:** Navy SBIR (Small Business Innovation Research)
- **Date:** Submitted 2025 (document edited through May 2025)
- **BST Products/Systems Referenced:** S0 UAS (primary platform)
- **Key Personnel:** 
  - Dr. Jack Elston (Principal Investigator, BST)
  - Dr. Maciej Stachura (Lead Engineer, BST)
  - Adam Sniff (Consultant – Hydrophone Design, Cetacean Research Technology)
  - Jeffrey Orton (Senior Engineer, QuSpin Inc.)

---

## Executive Summary

Black Swift Technologies proposes developing a Sonobuoy-Launched Unmanned Aerial Vehicle (SL UAS) capable of magnetic anomaly detection (MAD) and passive acoustic sensing for Anti-Submarine Warfare (ASW), integrating seamlessly with the Navy's P-8A Poseidon platform. The effort leverages BST's proven S0 UAS platform (operationally deployed by NOAA in hurricanes and polar regions) modified with a QuSpin QTFM Gen-2 magnetometer and a lightweight hydrophone from Cetacean Research Technology, targeting a cost objective of <$10,000 per unit in quantities of 100.

---

## Technical Approach

### 1. Magnetic Anomaly Detection (MAD) System
- **Sensor:** QuSpin QTFM Gen-2 optically pumped atomic scalar magnetometer
- **Specifications:**
  - Sub-picotesla sensitivity (<2 pT/√Hz, Navy threshold: 20 pT/√Hz in 0.01–100 Hz range)
  - Noise spectral density: <1 pT/√Hz
  - Dynamic range: ±100 µT (expandable to ±150 µT per letter of support)
  - Bandwidth: 0–500 Hz
  - Built-in 3-axis vector capabilities and IMU
- **Integration approach:** BST's proprietary avionics (previously modified for EMI-sensitive equipment in NASA soil moisture L-band radiometer project) will minimize platform-induced magnetic noise through advanced shielding and noise compensation algorithms
- **De-risking activity:** BST successfully conducted a test flight with QuSpin magnetometer over an oil and gas pumping station, demonstrating clear magnetic signature detection with flight track correlation

### 2. Acoustic Sensor Integration
- **Partner:** Cetacean Research Technology (CRT)
- **Specifications:**
  - Ultra-low self-noise design with hydrophone self-noise levels below sea-state zero
  - Calibration accuracy: ±2 dB threshold, ±1 dB objective
  - Automatic scuttling functionality for operational security
  - Laboratory testing to validate directivity index (DI), noise equivalent levels, and calibration accuracy
- **Data processing:** Algorithms will whiten signals relative to environmental noise, reducing uplink bandwidth requirements while maintaining data fidelity

### 3. System Integration and Validation
- **Platform base:** Modified S0 UAS with modular design for seamless sensor integration
- **Key modification:** Adaptation from current freefall chute deployment (P-3) to Sonobuoy Launch Container (SLC) initialization and launch dynamics
- **Testing approach:**
  - Bench testing to characterize magnetic noise at sensor location
  - Simulations to validate cued search and target detection using data fusion algorithms
  - Structural analysis and CAD-based design iterations
  - Environmental chamber testing at extreme temperatures (BST's avionics have operated at -20°C in Greenland)

---

## Products & Capabilities Described

### S0 UAS Platform
- **Status:** TRL 9, operationally proven
- **Current users:** NOAA (air-deployed for hurricane monitoring)
- **Deployment method:** Currently freefall from P-3; to be modified for SLC/tube launch
- **Proven capabilities:**
  - Operations in extreme environments: hurricanes, polar regions (Greenland at -20°C)
  - Communication range: Successfully demonstrated 163 nm during hurricane sampling (objective; minimum requirement 50 nm)
  - Autonomous waypoint navigation and target tracking
  - >100 successful flights in Greenland
  - Most cost-effective air-deployed UAS in the world (per proposal)
- **Proposed modifications:** Structural changes to accommodate SLC payload volume and launch constraints; CAD (Cartridge Actuated Device) launch adaptation (preliminary work already conducted for NOAA/Air Force)

### QuSpin QTFM Gen-2 Magnetometer
- **Type:** Optically pumped atomic scalar magnetometer
- **Key advantage over airborne MAD systems:** Minimized platform-induced interference through advanced integration techniques
- **Integration history:** Used in NASA projects; successfully tested in BST test flight

### Cetacean Research Technology Hydrophone
- **Specifications:** Ultra-low self-noise, broad frequency coverage, rapid deployment capability
- **Integration cost:** Not exceeding $20,000

---

## Use Cases & Applications

### Primary Mission: Anti-Submarine Warfare (ASW)
- Magnetic anomaly detection for submarine localization
- Passive acoustic sensing for target classification and tracking
- Deployment from Navy P-8A Poseidon via sonobuoy launch systems
- Cued search operations with autonomous target tracking
- Data fusion of MAD and acoustic signals for improved detection accuracy

### Secondary/Commercial Markets (per proposal)
- **NOAA:** Environmental monitoring, hurricane tracking, marine ecosystem studies
- **Department of Homeland Security:** Border security, maritime surveillance
- **Offshore energy:** Pipeline and subsea infrastructure monitoring
- **Environmental monitoring:** Detection of illegal fishing, underwater ecosystem surveillance
- **Maritime logistics:** Rapid UAS deployment for shipping lane, port, and vessel inspection

---

## Phase I Objectives & Deliverables

### Primary Objective
Establish technical feasibility of integrating MAD and passive acoustic sensing into a SL UAS platform compatible with operational requirements.

### Five Specific Phase I Objectives

**Objective 1 – Sensor Integration Feasibility:**
- Assess QuSpin QTFM Gen-2 and lightweight hydrophone integration
- Evaluate noise mitigation strategies for platform-induced interference
- Ensure hydrophone meets Navy sensitivity, frequency range, and depth requirements

**Objective 2 – Platform Compatibility with SLC:**
- Modify S0 UAS to accommodate Sonobuoy Launch Container payload volume and weight
- Validate aerodynamic and structural modifications for successful launch and post-deployment operation in varying environmental conditions

**Objective 3 – Sensor Performance Validation:**
- Laboratory simulations and bench testing for magnetometer noise characterization and hydrophone acoustic sensitivity
- Compliance validation: magnetometer (20 pT/√Hz in 0.01–100 Hz), hydrophone (±2 dB threshold, ±1 dB objective calibration accuracy)
- Identify design modifications needed before flight testing

**Objective 4 – Data Fusion Algorithm Development:**
- Design, implement, and test algorithms combining MAD and acoustic outputs
- Evaluate real-time signal processing methods
- Explore machine learning techniques for optimized detection using simulated datasets

**Objective 5 – Autonomous Operation and Communication:**
- Test autonomous target tracking based on MAD and acoustic cues
- Validate communication/control systems for 50 nm minimum range (163 nm objective)
- Evaluate operational constraints related to data transmission and onboard processing

### Phase I Deliverables

**Base Tasks (Months 1–6):**
1. **B.1 – Requirements Analysis and Preliminary Design**
   - Detailed operational requirements analysis
   - Integration design for QuSpin QTFM Gen-2 and lightweight hydrophone
   - System concept of operations documentation

2. **B.2 – Platform Modifications**
   - Compatibility evaluation of S0 UAS with SLC
   - Airframe modifications for SLC initialization and launch dynamics
   - CAD simulations and physical prototype testing

3. **B.3 – Sensor Integration and Testing**
   - Laboratory integration of magnetometer and hydrophone
   - Performance validation (noise spectral density, frequency response)
   - Data fusion algorithm development and simulated scenario testing
   - Advanced filtering and sensor shielding for interference mitigation

4. **B.4 – Prototype Fabrication and Validation**
   - Functional SL UAS prototype fabrication
   - Simulated deployment tests validating SLC launch compatibility
   - Autonomy, communication range, and power efficiency evaluations

**Option Tasks (Months 7–12):**
1. **O.1 – Local Flight Testing of Phase I Prototype**
   - Multiple test iterations at BST's Longmont, Colorado test site
   - Risk reduction through rapid development, testing, and iteration

2. **O.2 – Certification for Phase II Flight Testing**
   - FAA and Navy operational compliance documentation
   - Risk assessments and regulatory coordination
   - Initiation of CAD launch certifications for Phase II Navy flight testing

3. **O.3 – Design for CAD Launch**
   - Structural analysis for Cartridge Actuated Device compatibility
   - Deployment simulations and preliminary integration plans
   - Leveraging BST's preliminary CAD launch work for S0 (NOAA/Air Force)

### Final Deliverables
- Preliminary Design Report with MAD/acoustic sensor specifications and simulation results
- Functional prototype capable of laboratory testing
- Structural analysis confirming payload integration and compliance
- Laboratory Validation Report with sensor testing results and Phase II recommendations
- Briefing decks outlining results for TPOC presentation (Base at 6 months, Option at 12 months)
- Final comprehensive report at conclusion of Phase I

---

## Technical Context: Competitive Landscape & State of the Art

### Tube-Launched UAS Development
- **AeroVironment Switchblade:** Leverages innovative folding mechanisms and robust avionics
- **Raytheon Coyote:** High-speed deployment from sonobuoy launch container
- **Anduril Altius-600:** Compact storage and deployment capabilities
- **BST's competitive advantage:** Won NOAA air-deployed UAS contract over Anduril, demonstrating superior capability in extreme operational environments

### Magnetometer Technology
- **State of the art:** QuSpin Gen-2 QTFM offers sub-picotesla sensitivity and wide dynamic range
- **Integration challenges addressed by industry:** Lockheed Martin and General Atomics platforms employ sensor isolation and active noise reduction techniques
- **BST's approach:** Leverage proprietary noise compensation algorithms validated during NOAA hurricane missions

### Acoustic Sensor Technologies
- **Industry leaders:** Sonardyne (Sentinel system), Teledyne (Slocum Glider with acoustic sensing)
- **CRT's expertise:** Customized hydrophone designs optimized for high sensitivity and broad frequency coverage
- **Data processing:** Advanced whitening and environmental noise compensation techniques

---

## Key Results & De-risking Activities

### Early Demonstration (Test Flight)
- **Objective:** De-risk sensor integration approach and provide preliminary validation
- **Test scenario:** Flight over oil and gas pumping station
- **Findings:** Clear magnetic signature detection; flight tracks correlated with magnetic data
- **Significance:** Demonstrates BST avionics' ability to integrate QuSpin magnetometer with minimal modification (simplified interface adapting in hours)

---

## Commercialization & Market Potential

### Primary Market: U.S. Navy
- Transition strategy focuses on integration with P-8A Poseidon acquisition program
- Phase II will conduct operationally relevant scenario testing
- Phase III involves manufacturing scale-up to meet cost objective (<$10,000 per unit, quantities of 100)
- Navy participation in exercises to showcase ASW capabilities

### Secondary Federal Markets
- **NOAA:** Environmental monitoring and hurricane research
- **DHS:** Maritime surveillance and border security

### Private Sector Markets
- **Offshore energy:** Pipeline and subsea infrastructure monitoring
- **Environmental monitoring:** Illegal fishing detection, ecosystem surveillance
- **Maritime logistics:** Shipping lane and port inspection

### Market Size
- UAS-based ASW systems: Projected to reach $2.1 billion by 2030
- Environmental monitoring market: Valued at >$17 billion in 2023

---

## Facilities & Equipment

### BST Facilities (Longmont, Colorado)
- **Prototyping and Fabrication Lab:** 3D printers, CNC machines, composite material workstations
- **