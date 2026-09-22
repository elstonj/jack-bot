# Expendable Sonobuoy-Launched Unmanned Aerial Vehicle for ASW Cued Search, Detection, Tracking, and Classification

## Document Metadata
- **Type:** Navy SBIR Phase I Final Report (Draft)
- **Client/Agency:** Department of the Navy / NAVAIR
- **Program/Solicitation:** SBIR Topic N251-016
- **Contract Number:** N6833525C0492
- **Contract Period:** March 23, 2026 – September 28, 2026
- **Date:** September 8-10, 2026 (created/modified)
- **TPOC:** Angel Ruiz-Reyes
- **BST Products/Systems Referenced:** S0 UAS platform
- **Key Personnel:** 
  - Dr. Jack Elston (Principal Investigator)
  - Dr. Maciej Stachura (Prepared By)
  - Meredith Needham (Corporate Official)
  - Beck Cotter (Last Editor)

## Executive Summary
Black Swift Technologies successfully established the technical feasibility of deploying an expendable, sonobuoy-launched unmanned aerial system (UAS) for anti-submarine warfare (ASW). The Phase I effort demonstrated that the S0 UAS platform can be modified to integrate a high-sensitivity magnetometer and passive acoustic sensor suite within the strict size, weight, and power (SWaP) constraints of a standard LAU-126A Sonobuoy Launch Container while mitigating platform-generated electromagnetic and mechanical noise. The program is recommended to proceed to Phase II for full-scale prototype fabrication and validation.

## Technical Approach

### Platform Integration
- **Baseline System:** Black Swift S0 UAS platform modified for sonobuoy deployment
- **Packaging Constraint:** LAU-126A Sonobuoy Launch Container (SLC) with maximum weight threshold of 39 pounds
- **Physical Validation:** Computational analysis and structural modeling confirmed the folded S0 airframe and deployment tube fit standard SLC dimensions

### Magnetic Sensing Integration
- **Sensor:** QuSpin QTFM Gen-2 optically pumped atomic scalar magnetometer
- **Noise Mitigation Strategy:** 
  - Five-foot extended nose boom
  - MuMetal (magnetic shielding alloy) motor enclosure
  - Ground and surrogate flight tests mapping noise spectral density across motor throttle levels and distances
- **Performance Achieved:** 1.5 pT/√Hz noise floor (significantly below Navy's 20 pT/√Hz threshold)

### Acoustic Sensing Architecture
- **Challenge:** Traditional piezo-based transducers physically limited below 1 Hz
- **Solution - Dual-Modality Approach:**
  - Acceleration-canceling omnidirectional hydrophone (5 Hz – 40 kHz range)
  - Extremely Low Frequency Electromagnetic (ELFE) and Ultra Low Frequency (ULF) E-field probes (0.001 Hz – 1 Hz range)

### Computational Infrastructure
- **Edge AI Processing:** NVIDIA Jetson AGX Orin compute module for onboard artificial intelligence processing

### Two-Aircraft Operational Architecture
Transitioned to dual-variant framework:
1. **S0-MAD Variant:** Carries magnetometer and Jetson AGX Orin compute module for edge AI processing
2. **S0-Acoustic Variant:** Designed for water landing and acoustic deployment via 200-foot fiber-optic tether

### Data Security & Classification Management
- System remains completely unclassified while at rest
- Classified machine learning models loaded immediately prior to launch
- Automated sanitization process purges classified data upon mission completion

## Products & Capabilities Described

### Black Swift S0 UAS Platform
- **Description:** Expendable unmanned aerial system designed for deployment from sonobuoy launch containers
- **Use Case:** ASW cued search, detection, tracking, and classification
- **Key Capability:** Modifiable airframe that fits within LAU-126A SLC volumetric constraints
- **Weight Constraint:** Total system maintained well under 39-pound Navy threshold

### Magnetometer Integration (S0-MAD Variant)
- **Sensor:** QuSpin QTFM Gen-2 optically pumped atomic scalar magnetometer
- **Purpose:** High-sensitivity magnetic anomaly detection for submarine detection
- **Noise Performance:** 1.5 pT/√Hz noise floor
- **Requirement Met:** Navy's 20 pT/√Hz maximum threshold exceeded by ~13× margin
- **Associated Computing:** NVIDIA Jetson AGX Orin for edge AI processing

### Acoustic Sensing Suite (S0-Acoustic Variant)
- **Hydrophone Component:** Acceleration-canceling omnidirectional hydrophone (5 Hz – 40 kHz)
- **E-field Sensing:** ELFE and ULF probes (0.001 Hz – 1 Hz)
- **Deployment:** Water landing capability with 200-foot fiber-optic tether for submerged operations

## Use Cases & Applications

### Primary Mission: Anti-Submarine Warfare (ASW)
- **Threat Context:** Adversary submarines pose severe threat to US Navy surface forces
- **Operational Requirement:** Find, track, and classify submerged contacts
- **Deployment Platform:** P-8A Poseidon aircraft via standard LAU-126A Sonobuoy Launch Containers
- **Operational Profile:** Expendable, sonobuoy-launched system for cued search, detection, tracking, and classification

### Sensor-Specific Applications
- **Magnetometer (S0-MAD):** Magnetic anomaly detection for submarine localization
- **Hydrophone/E-field (S0-Acoustic):** Passive acoustic signature detection and ultra-low frequency electromagnetic field sensing for vessel identification

## Key Results

### Platform Compatibility
- Physical dimensional checks confirmed folded S0 airframe and deployment tube fit standard LAU-126A SLC dimensions
- System weight maintained well under 39-pound Navy threshold

### Magnetic Noise Mitigation
- Motor-generated electromagnetic interference dissipates to background levels at 5-foot separation
- Achieved noise floor of 1.5 pT/√Hz, significantly outperforming Navy's 20 pT/√Hz maximum threshold

### Sensing Architecture Evolution
- Transitioned from single piezo-based acoustic approach (physically limited below 1 Hz) to dual-modality architecture combining:
  - Omnidirectional hydrophone covering 5 Hz – 40 kHz
  - ELFE/ULF E-field probes covering 0.001 Hz – 1 Hz
- Addressed low-frequency detection gap with complementary sensing modalities

### Two-Variant Operational Framework
Successfully developed two specialized variants optimizing different mission requirements:
- **S0-MAD:** Magnetometer + edge AI processing
- **S0-Acoustic:** Water landing + tethered acoustic deployment

### Classification Security Management
- Demonstrated unclassified system at rest with classified ML model loading pre-launch
- Established automated sanitization purging classified data post-mission

## Notable Details

### Partnerships & External Collaboration
- **Cetacean Research Technology (CRT):** Collaborated on hydrodynamic drag analysis, deployment mechanisms, and low-frequency E-field sensing alternatives

### Competitive Advantages Demonstrated
1. **Compact SWaP Integration:** Successfully integrated dual magnetometer + acoustic sensors within sonobuoy container constraints
2. **Magnetic Noise Performance:** Achieved 1.5 pT/√Hz—substantially exceeding Navy's 20 pT/√Hz requirement
3. **Multi-Modal Sensing:** Addressed frequency gap from 0.001 Hz to 40 kHz with complementary sensing approaches
4. **Edge AI Capability:** Integrated NVIDIA Jetson AGX Orin for onboard processing and classification
5. **Security Model:** Innovative approach to maintaining unclassified system state with dynamic classified ML loading

### Navy Requirements Addressed
- Operational deployment from P-8A Poseidon via standard LAU-126A SLC
- Strict SWaP constraints (39-pound maximum)
- Platform-generated noise mitigation for sensitive magnetometer operation
- Low-frequency acoustic detection capabilities
- Expendable/disposable operational model

### Recommended Next Phase
Proceed to Phase II for full-scale prototype fabrication and validation, building on successfully validated sensor feasibility and platform compatibility.

### Contract Data Rights
- SBIR/STTR data protection period: March 23, 2026 – March 23, 2046 (20 years)
- Government purpose rights: Perpetual after protection period expiration
- Export control restrictions apply (AECA/EAA)