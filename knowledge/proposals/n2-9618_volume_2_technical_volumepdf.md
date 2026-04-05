# Expendable Sonobuoy-Launched Unmanned Aerial Vehicle for ASW Cued Search, Detection, Tracking, and Classification

## Document Metadata
- Type: SBIR Phase II Technical Volume (Proposal)
- Client/Agency: U.S. Navy (NAVAIR / PMA-264)
- Program/Solicitation: Navy SBIR Topic N251-016; Phase I Contract No. N6833525C0492
- Date: March 25, 2026
- BST Products/Systems Referenced: SØ (SØ-MAD, SØ-Acoustic variants)
- Key Personnel: Jack Elston (Principal Investigator), Beck Cotter (Corporate Official); Subcontractor: Ultra Maritime (Paul DeMond)

## Executive Summary
Black Swift Technologies proposes to develop a production-ready Sonobuoy-Launched Unmanned Aerial System (SL UAS) for Anti-Submarine Warfare (ASW) operations, consisting of two specialized variants: the SØ-MAD (Magnetic Anomaly Detection) equipped with a high-sensitivity magnetometer, and the SØ-Acoustic configured to deploy in-water passive acoustic sensors. Phase II will mature technical feasibility demonstrated in Phase I—specifically, validating magnetic noise floors below 20 pT/√Hz in dynamic flight conditions—into mission-validated prototypes compatible with Navy's LAU-126A sonobuoy launch infrastructure, while maintaining an expendable unit cost target below $10,000 at quantity 100.

## Technical Approach

### Overall Strategy
The phase II effort follows a 30-month Base Period plus 12-month Option Period (42 months total), structured as iterative "Design-Build-Test" cycles. The approach splits sensing into two airframe variants to optimize for their specific operational roles:

- **SØ-MAD**: Minimizes electromagnetic interference (EMI) through extensive fuselage redesign, battery system conversion to non-ferrous pouch cells, extended nose boom for sensor separation, and active/passive magnetic noise control measures
- **SØ-Acoustic**: Supports water landing and tethered sensor deployment via buoyant avionics bay, gravity-triggered release mechanism, and specialized internal architecture for sensor stowage and cable management

### Key Technical Elements

**Magnetic Sensing Architecture:**
- QuSpin magnetometer integrated on extendable boom (maximizes separation from propulsion/electrical systems)
- Battery redesigned from steel-cased cylindrical cells to pouch cells to eliminate ferrous magnetic signatures
- Fuselage widened to accommodate Single Board Computer (SBC) and provide better component separation
- Achieves required magnetic noise floor <20 pT/√Hz (0.01–100 Hz band) under powered conditions; Phase II validates performance in dynamic flight maneuvers
- Heading error target: <3 nT
- Calibration maneuvers include multi-heading crossings and attitude variation tests at ≥400 ft AGL

**Acoustic Sensing Architecture:**
- Hybrid sensor suite spanning 0.01 Hz–25 kHz via three sensor types:
  - **Hydrophone** (5 Hz–40 kHz): Omnidirectional sensor with acceleration-canceling design and tuned suspension to mitigate wave-motion noise
  - **ELFE probes** (0.5 Hz–10 Hz): Extremely Low Frequency Electromagnetic sensors
  - **ULF probes** (0.05–20 mHz): Ultra Low Frequency probes
- Sensors deployed via 200-foot fiber-optic tether to decouple sensing from aircraft-induced electrical/mechanical noise
- Passive deployment mechanism triggered by water contact; gravity-assisted descent to 200 ft mission depth
- Operating duration: ≥60 minutes minimum; objective 70 minutes

**Onboard Processing & Compute:**
- NVIDIA Jetson AGX Orin 64GB module (or equivalent, 275 TOPS AI compute capability) integrated on both variants
- High-bandwidth sensor-to-GPU data interfaces for real-time processing
- Onboard data reduction protocols to transmit compressed detections rather than raw streams
- Automated sanitization protocol for classified mission data before shutdown/scuttling; ensures unclassified-at-rest operation
- Modular software framework designed to host government-furnished detection models

**Launch & Flight Performance:**
- Airframe: Folding-wing design compatible with LAU-126A sonobuoy launch container
- Airspeed: ≥70 knots sustained
- Endurance: ≥70 minutes
- Range/Communications: ≥20 nm line-of-sight with existing BST long-range communications architecture
- Launch survivability: 10G/100ms shock pulse qualification without structural failure or calibration loss

**Sensor Fusion & Multi-Modal Operations:**
- Coordinated SØ-MAD and SØ-Acoustic operations enable two tactical modes:
  - *Acoustic-to-Magnetic (Cued Intercept)*: Acoustic detection triggers magnetometer search pattern
  - *Magnetic-to-Acoustic (Blind-Search Handoff)*: Magnetic anomaly triggers acoustic sensor deployment
- Multi-vehicle swarm logic allows synchronized MAD flight patterns with inter-vehicle communication for dipole model refinement and bearing improvements

## Products & Capabilities Described

### SØ-MAD (Magnetic Anomaly Detection Variant)
- **What it is**: Modified SØ airframe optimized for ultra-low-noise magnetic sensing
- **Proposed use**: Cued magnetic search and anomaly detection for subsurface target localization
- **Key modifications**: Extended nose boom, pouch-cell battery, widened fuselage, EMI-hardened internal layout
- **Specifications/Performance**:
  - Magnetic noise floor: <20 pT/√Hz (0.01–100 Hz)
  - Heading error: <3 nT
  - Airspeed: ≥70 knots
  - Endurance: ≥70 min
  - Launch compatibility: LAU-126A
  - Unit cost target: <$10,000 at qty 100

### SØ-Acoustic (In-Water Acoustic Deployment Variant)
- **What it is**: Modified SØ airframe configured for autonomous water landing and multi-sensor acoustic payload deployment
- **Proposed use**: Persistent passive acoustic detection and classification of maritime contacts post-deployment
- **Key features**: Water-sealed avionics bay with buoyancy foam, deployable tethered sensor array, gravity-triggered release mechanism
- **Specifications/Performance**:
  - Operating depth: ≥200 feet
  - Operating duration: ≥60 minutes (objective 70 min)
  - Frequency coverage: 0.01 Hz–25 kHz (via hydrophone + E-field hybrid)
  - Deployment time: ≤120 sec (objective 60 sec)
  - Unit cost target: <$10,000 at qty 100

### Ultra Maritime Acoustic/E-Field Sensor Suite
- **What it is**: Integrated hydrophone and electric-field probe package for broadband underwater acoustic/electromagnetic detection
- **Integration**: Deployed via fiber-optic tether from SØ-Acoustic UAS
- **Performance**:
  - Hydrophone: 5 Hz–40 kHz (CO—Calibrated Omnidirectional type with 8 dB improvement via textured ceramics)
  - ELFE sensors: 0.5 Hz–10 Hz band
  - ULF sensors: 0.05–20 mHz band
  - Target SNR improvements: 6–8 dB over baseline Q53H CO specifications

### Onboard Processing Module (NVIDIA Jetson AGX Orin)
- **Capability**: 275 TOPS AI compute for real-time detection/classification algorithm execution
- **Function**: Executes compressed sensor processing, contact reporting, and classified model hosting
- **Security**: Implements zeroization protocol for mission-critical data before asset loss/scuttling

## Use Cases & Applications

### Primary ASW Mission Scenarios

1. **Acoustic-Cued Magnetic Intercept**
   - SØ-Acoustic deployed as persistent "tripwire" in likely transit area
   - Detects contact via passive acoustic monitoring
   - Autonomously relays Area of Interest (AOI) to overhead SØ-MAD swarm
   - SØ-MAD assets transition to cooperative low-altitude magnetic search grid for precision localization and classification

2. **Magnetic-Cued Acoustic Verification**
   - SØ-MAD conducts wide-area magnetic sweep patrols
   - Upon magnetic anomaly detection, autonomously cues splash-down deployment of SØ-Acoustic asset at precise coordinates
   - Provides persistent multi-modal tracking and target verification for "silent" targets (e.g., AIP-powered submarines, stationary sea mines)

3. **Multi-Vehicle Swarming**
   - Two or more SØ-MAD aircraft maintain synchronized flight patterns for maximum sensor coverage
   - Inter-vehicle communication refines magnetic dipole model and bearing estimates
   - Significantly reduces Time-to-Target (TTT) vs. manual operator-cued transitions

### Operational Context
- Deployment from manned naval platforms equipped with LAU-126A launchers (P-3, maritime patrol aircraft, naval vessels)
- Operations in contested/denied maritime environments
- Distributed, attritable sensing architecture supporting operational concepts that emphasize sensor fusion over traditional episodic sonobuoy sampling

### Dual-Use Applications (Beyond ASW)
- Unexploded ordnance (UXO) detection
- Environmental monitoring and magnetic field mapping
- Maritime domain awareness

## Key Results (Phase I Foundation)

### Phase I Achievements
- **Magnetic noise floor validation**: Achieved <20 pT/√Hz in 0.01–100 Hz band under powered conditions (ground testing)
- **Mechanical compatibility**: Confirmed SØ airframe compatibility with LAU-126A launch envelope (size, mass, center-of-gravity, structural loading)
- **Design maturation**: Established CAD designs and preliminary component selections for both SØ-MAD and SØ-Acoustic variants
- **Acoustic sensor foundation**: Validated multi-modal sensor suite concept (hydrophone + E-field) across required frequency bands

### Phase I Success Criteria Met
Phase I established technical feasibility; Phase II builds toward production readiness and dynamic flight validation.

## Notable Details

### Partnerships & Subcontractors
- **Ultra Maritime**: Acoustic/E-field sensor payload developer; provided SBIR experience (N091-019, N192-060) with E-field sensing for ASW sonobuoys
- **QuSpin**: Subject matter expertise on magnetometer integration and flight-data analysis
- **Royal Navy**: Informal international test collaboration (external funding) to evaluate system in diverse maritime climates
- **DoN-SEC / Navy SBIR Experimentation Cell (TCE)**: Primary venue for operational validation at Camp Pendleton / Camp Lejeune; twice-yearly events

### Manufacturing & Transition Strategy
- **Design for Manufacturability (DFM)** emphasis to achieve <$10,000 unit cost at qty 100
- Production-representative first articles built during Phase II
- Complete technical data package (3D CAD, 2D drawings, BOM) delivered for Navy procurement/Phase III transition
- Interface Control Documents (ICDs) ensure compatibility with Navy UAS Control Segment (UCS) and LAU-126A infrastructure
- Phase III Transition Roadmap outlines path to full-rate production and fleet integration

### Security & Operational Flexibility
- **Unclassified-at-rest architecture**: Sensitive algorithms and mission models treated as volatile data; zeroization protocol ensures classified binaries erased before shutdown/scuttling
- **Modular algorithm framework**: Designed to host government-furnished models while enabling BST baseline detection logic for system validation
- **Distributed sensing philosophy**: Split-airframe approach (MAD + Acoustic) maximizes mission flexibility, keeps cost/size low, enables swarm and sensor fusion

### Competitive Advantages
1. **Proven SØ platform**: TRL 9 for hurricane survival and P-3 deployment compatibility
2. **Magnetic quieting expertise**: Demonstrated ability to achieve Navy thresholds via pouch-cell battery redesign and fuselage optimization
3. **Fiber-optic tether deployment**: Unique decoupling of in-water sensors from aircraft-induced noise
4. **Multi-modal fusion ready**: Coordinated MAD/Acoustic operations aligned with established ASW concepts
5. **Expendable cost model**: Target <$10k per unit at qty 100 supports attritable operational doctrine

### Risk Mitigation
- Magnetic shielding of propulsion components retained as risk-reduction option if early in-flight margin eros