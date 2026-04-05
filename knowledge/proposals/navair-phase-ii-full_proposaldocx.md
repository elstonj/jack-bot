# NAVAIR SBIR Phase II Full Proposal: Sonobuoy-Launched UAS for ASW

## Document Metadata
- **Type:** SBIR Phase II Full Proposal
- **Client/Agency:** U.S. Navy (NAVAIR)
- **Program/Solicitation:** Topic N251-016 – "Expendable Sonobuoy-Launched Unmanned Aerial Vehicle for ASW Cued Search, Detection, Tracking, and Classification"
- **Date:** March 16, 2026 (prepared date)
- **BST Products/Systems Referenced:** S0 (unmanned aerial system/airframe), S0-MAD (magnetic anomaly detection variant), S0-Acoustic (acoustic sensing variant), SwiftCore (onboard processing via Jetson AGX Orin)
- **Key Personnel:** Jack Elston (Principal Investigator), Beck Cotter (Proposal Specialist), Maciej Stachura (last editor)
- **Phase I TPOC:** Angel Reyes-Ruiz (NAVAIR)

## Executive Summary

Black Swift Technologies proposes a Phase II effort to develop, integrate, and validate a production-ready Sonobuoy-Launched Unmanned Aerial System (SL UAS) capable of performing magnetic anomaly detection (MAD) and deploying in-water passive acoustic sensors for Anti-Submarine Warfare (ASW) cued search, detection, tracking, and classification. The system comprises two aircraft variants based on the BST S0 platform—an S0-MAD for magnetometer operations and an S0-Acoustic for acoustic sensing—both deployable from the LAU-126A sonobuoy launch container with a target unit cost below $10,000 in quantity production. Phase II will harden the SL UAS architecture for dynamic launch and flight environments, validate magnetic performance in full-flight conditions, demonstrate acoustic sensor deployment and operation, and establish a clear transition path to Phase III and low-rate initial production.

## Technical Approach

### System Architecture

**Two-Aircraft Configuration:**
- **S0-MAD variant:** Optimized for magnetic anomaly detection with integrated magnetometer, minimized magnetic noise through active and passive shielding, and sensor placement via structural booms
- **S0-Acoustic variant:** Modified for water landing and deployment of tethered acoustic/E-field sensor suite; includes automated deployment mechanism for 200-foot sensor string

**Rationale for Split Architecture:**
- Maximizes mission flexibility
- Keeps individual aircraft size and cost low
- Enables advanced sensor fusion and autonomous swarm operations
- Allows independent optimization for each sensing modality

### Magnetic Sensing Implementation

**Platform Noise Control:**
- Phase I testing confirmed the S0 airframe achieves extremely low magnetic noise levels at sensor location
- Phase II will implement:
  - Magnetic shielding of propulsion components
  - Optimized sensor placement via short structural booms
  - Calibration-informed compensation techniques
  - Hardened avionics and power systems for LAU-126A compatibility

**Performance Target:** Threshold requirements for in-flight magnetic performance validation (specific numerical thresholds not detailed in proposal text)

### Acoustic Sensing Implementation

**Integrated Multi-Modal Approach:**
- **Hydrophone:** 5 Hz – 40 kHz bandwidth (traditional sonobuoy capability)
- **E-field sensors:** Two variants to cover ultra-low frequency range
  - ELFE (Extremely Low Frequency Electromagnetic): unspecified range
  - ULF (Ultra Low Frequency): 0.01 Hz – 5 Hz
- **Deployment method:** Lightweight fiber-optic tether (200 feet) to decouple sensors from aircraft-induced electrical and mechanical noise
- **Sensor payload configuration:** 11-inch vertical damper disc, 2-lb terminal weight
- **Operating life:** 60–70 minutes while delivering whitened digital data over 20 nm line-of-sight RF link

**Noise Isolation Strategy:**
- Acceleration-canceling hydrophone design
- Tuned suspension system to mitigate mechanically induced noise below 100 Hz
- Calibration accuracy target: ±2 dB across spectrum

### Onboard Processing

**Hardware Integration:**
- Jetson AGX Orin for real-time target detection/classification processing
- Mechanical redesign to accommodate form/fit of processing hardware
- Logical and electrical interfaces for proper data flows from sensors to algorithms

### Sensor Fusion & Autonomous Operation

**Phase II Base Period:**
- Avionics-level hooks and control abstractions enabling magnetic or acoustic detections to drive adaptive flight behaviors
- Architecture supporting coordinated deployment of complementary sensors

**Phase II Option Period (Tasks O.1 and O.2):**
- **Task O.1 (Classified Algorithm Integration):** Integration of government-provided machine learning model for target detection/classification; design to maintain unclassified aircraft and payload status before operation, with classified data wiped before shutdown
- **Task O.2 (Swarm Operations):** Multi-SL UAS collaboration for ASW operations; information sharing via transient/small-packet protocols designed for disadvantaged network conditions

**Operational Concepts:**
- Acoustic SL UAS provides approximate location cue → triggers search pattern with magnetometer-equipped SL UAS
- Magnetometer detection → directs deployment of multiple acoustic SL UAS for precise localization
- Aligns with established ASW doctrine (MAD for area localization, acoustic assets for classification/tracking)

## Products & Capabilities Described

### S0 Platform

**What it is:** Expendable, tube-launched unmanned aerial vehicle developed by BST, originally demonstrated in non-ASW applications (NOAA P-3 deployments, quadrotor drops)

**Heritage:** Phase I testing confirmed compatibility with LAU-126A launch container and demonstrated magnetic noise performance exceeding Navy thresholds

**Performance Characteristics:**
- Cruise speed: ~70 knots
- Launch method: Pneumatic ejection from LAU-126A sonobuoy launch container
- Airframe: Designed for water landing and survival of 10G/100ms shock loads
- Operating temperature range: –20°C to +50°C
- Environmental resistance: Light rain, salt-water durability (validated in ocean testing)
- Target unit cost: <$10,000 in quantities of 100

**Phase II Variants:**
1. **S0-MAD:**
   - Integrated optical-pumped atomic magnetometer
   - Magnetic noise performance validated in ground tests (specific dB figures not provided in text, but magnetic signature graphs shown)
   - Phase I CAD design to be built out in Phase II with full flight validation

2. **S0-Acoustic:**
   - Water-landing capable airframe modifications
   - Integrated Ultra Maritime hydrophone and E-field sensor suite
   - Automated deployment mechanism for 200-foot tethered sensor package

### Ultra Maritime Sensor Suite

**Hydrophone & E-Field Sensors:**
- Manufacturer: Ultra Maritime
- Hydrophone bandwidth: 5 Hz – 40 kHz (standard maritime patrol aircraft capability)
- E-field sensors: ELFE and ULF variants for sub-1 Hz detection
- Simulated performance data provided (E-field sensor plots in proposal)
- Lightweight design suitable for aerial deployment via fiber-optic tether

### SwiftCore (Jetson AGX Orin Integration)

**Processing Capability:**
- Real-time target detection/classification
- Avionics interface for sensor-responsive autonomy
- Support for government-provided ML algorithms (Phase II Option)
- Configurable for classified/unclassified operation modes

## Use Cases & Applications

### Primary: Anti-Submarine Warfare (ASW)

**Mission Profile:**
- Cued search: Acoustic detections trigger magnetometer search patterns or vice versa
- Detection: Both MAD and passive acoustic sensing of submerged targets
- Tracking: Multi-vehicle coordination to maintain custody of submarine tracks
- Classification: Complementary sensor fusion to reduce false alarms and improve target ID

**Operational Scenario (from Navy ASW Doctrine):**
1. Acoustic SL UAS deployed, hydrophone/E-field sensors monitor for submarine noise
2. Detection cues deployment of MAD-equipped SL UAS to localize area of interest
3. Magnetic anomaly pinpoints target location
4. Additional acoustic SL UAS assets deployed for precise geolocation and classification
5. Data fused and passed to Navy mission systems for higher-level classification and tracking

**Launch Platform Compatibility:**
- P-8A Poseidon maritime patrol aircraft (primary)
- Deployment from LAU-126A sonobuoy launch container at altitude

### Secondary / Dual-Use Applications

1. **Unexploded Ordnance (UXO) Detection:** Magnetometer-based detection referenced in prior work (Seidel et al., 2023)
2. **Environmental Monitoring:** Coastal surveys, marine ecosystem monitoring
3. **Magnetic Field Mapping:** Geophysical surveys, geological research
4. **Infrastructure Inspection:** Cable/pipeline monitoring
5. **Scientific Research:** Marine animal research organizations expressed interest (per proposal); cited in well abandonment services market context ($1.45B in 2023, projected $2.48B by 2032, CAGR 6.1%)
6. **Maritime Surveillance:** Commercial and civilian ISR applications

## Key Results (Phase I Evidence)

### Magnetic Performance

**Flight-Test Evidence:**
- "Phase I testing confirmed that the S0 airframe can support extremely low magnetic noise levels at the sensor location"
- Magnetic signature graphs show noise performance across full spectrum with S0 throttling at 0 ft and 5 ft from magnetic sensor
- Performance validated in static and ground-based tests; Phase II will extend validation to fully dynamic flight conditions

### Mechanical Compatibility

- Successful integration with LAU-126A sonobuoy launch container
- Demonstrated survival of pneumatic launch shock loads
- Confirmed water-landing capability and saltwater durability

### System Heritage

- S0 aircraft in production (Phase I deliverables shown in proposal imagery)
- Successful deployment from NOAA P-3 maritime patrol aircraft
- Demonstrated air-drop capability from quadrotor platform (concept validation)

## Phase II Work Plan & Milestones

### Base Period (30 months, estimated): Tasks B.1 – B.8

| Task | Objective | Key Milestone |
|------|-----------|---------------|
| **B.1** | Design, manufacture, test S0-MAD airframe with integrated magnetometer; active/passive noise control; LAU-126A safety/compatibility | — |
| **B.2** | Flight validation of magnetic performance in dynamic flight conditions | **Milestone:** Magnetometer in-flight performance data |
| **B.3** | Integrate Jetson AGX Orin processing hardware; mechanical and electrical interface design | — |
| **B.4** | Ground characterization of Ultra Maritime acoustic/E-field sensor suite; sensitivity, self-noise, bandwidth validation | — |
| **B.5** | Design, fabricate, test S0-Acoustic airframe optimized for water landing; automated sensor deployment mechanism | — |
| **B.6** | Staged water-landing flight tests (freshwater → ocean); acoustic sensor deployment and operating life validation | **Milestone:** Acoustic UAV capability proof-of-concept |
| **B.7** | Environmental and shock qualification; LAU-126A compatibility testing; temperature range –20°C to +50°C validation; hardened airframe delivery | — |
| **B.8** | End-to-end operational test of both SL UAS variants in relevant maritime environment; air launch, water landing, sensor deployment, payload validation, data transmission | **Milestone:** Full system demonstration (launch, flight, deployment, target detection/tracking) |

### Option Period (12 months, estimated): Tasks O.1 – O.3

| Task | Objective | Key Milestone |
|------|-----------|---------------|
| **O.1** | Classified ML algorithm integration; design for unclassified airframe/payload status pre-operation; classified data wipe procedures | — |
| **O.2** | Swarm operations development; multi-vehicle coordination; information sharing over disadvantaged networks | — |
| **O.3** | Final validation with ML models loaded; Navy personnel operational demonstration; Level 3 Technical Data Package (TDP) delivery; Interface Control Documents (ICDs) for UCS integration | **Milestone:** Production-ready system for Phase III transition |

### Environmental Testing Program

**Progression:**
1. Laboratory and bench-level verification of subsystem performance
2. Environmental and shock qualification (LAU-126A loads, temperature, humidity, light rain)
3. Air-launch from surrogate platforms
4. Acoustic sensor deployment validation
5. Multi-modal detection against surrogate targets in operationally relevant maritime environments

## Government Participation Required

**Government