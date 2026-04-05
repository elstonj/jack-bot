# CPS_Elston.pdf - Current and Pending Support Information

## Document Metadata
- Type: NSF Current and Pending (Other) Support form (OMB-3145-0279)
- Key Personnel: Jack S. Elston (CEO & Founder, Black Swift Technologies)
- Organization: Black Swift Technologies LLC, Boulder, Colorado
- Date: 2026-03-31 (certified)
- Form Version: SCV C&P(O)S v.2024-1

## Executive Summary
This is Jack Elston's disclosure of current and pending research support for Black Swift Technologies, covering five active and proposed projects spanning NASA and Department of Navy funding. Projects focus on autonomous UAS flight control, sonobuoy-launched systems with magnetic anomaly detection (MAD) and acoustic sensing, and expendable air-sea profiling platforms for naval and atmospheric applications. Total active funding: ~$623,604; total pending funding: ~$3,800,000.

## Current Projects (Active as of 2026)

### 1. Adaptive and Secure Autonomy for UAS
- **Status**: Current
- **Funder**: NASA
- **Award Number**: (not listed)
- **Duration**: 08/2025 - 01/2026
- **Funding**: $149,711
- **Elston Effort**: 0.5 months (2025), 0.1 months (2026)
- **Objective**: Develop and validate a modular, layered architecture for the SwiftCore avionics system to enable aircraft autonomy per NASA requirements.

### 2. Development of a SL UAS with Advanced MAD and Acoustic Sensing Capability (Phase I)
- **Status**: Current
- **Funder**: Department of the Navy
- **Award Number**: N251-016-0021
- **Duration**: 07/2025 - 06/2026
- **Funding**: $236,399
- **Elston Effort**: 0.5 months (2025), 0.43 months (2026)
- **Objective**: Establish technical feasibility of integrating Magnetic Anomaly Detection (MAD) and passive acoustic sensing into a Sonobuoy-Launched Unmanned Aircraft System (SL UAS) platform.

### 3. Expendable Air-Sea Profiling Observations in Hazardous Weather via Small UAS (Phase I)
- **Status**: Current
- **Funder**: Department of the Navy
- **Award Number**: N25A-T025-0009
- **Duration**: 07/2025 - 06/2026
- **Funding**: $237,494
- **Elston Effort**: 0.36 months (2025), 0.27 months (2026)
- **Objective**: Quantify capabilities of S0 UAS to provide higher-resolution, more accurate, more cost-effective atmospheric data vs. radiosondes, particularly in challenging air-sea interaction regions.

## Pending Projects (Proposed)

### 4. Development of a SL UAS with Advanced MAD and Acoustic Sensing Capability (Phase II)
- **Status**: Pending
- **Funder**: Department of the Navy
- **Duration**: 01/2027 - 06/2030
- **Funding**: $1,400,000
- **Elston Effort**: 0.11 months (2027-2028), 0.14 months (2029-2030)
- **Objectives**:
  - Transition Phase I technical feasibility to production-ready, mission-validated SL UAS
  - Demonstrate magnetic noise floor below 20 pT/√Hz threshold under dynamic flight maneuvers and propulsion-driven environments
  - Develop hardened, production-representative airframe capable of launch shocks and autonomous water-landing-to-sensing transitions
  - Mature coordination between S0-MAD and S0-Acoustic variants
  - Provide Navy with expendable, distributed sensing capability to reduce detection latency and operator workload vs. traditional sonobuoy sampling
  - Focus on Anti-Submarine Warfare (ASW) search and detection within LAU-126A launch container constraints

### 5. Expendable Air-Sea Profiling Observations in Hazardous Weather via Small UAS (Phase II)
- **Status**: Pending
- **Funder**: Department of the Navy
- **Duration**: 01/2027 - 12/2030
- **Funding**: $2,400,000
- **Elston Effort**: 0.14 months (2027-2028), 0.12 months (2029-2030)
- **Objectives**: Transition S0 from NOAA research platform to fully integrated, turnkey DoW (Department of the Navy) operational capability:
  1. **Calibration and Validation**: Over-ocean flight campaigns to validate sensing accuracy and responsiveness against buoy/tower data
  2. **Turnkey DOW Operation**: Web-based, low-cognitive-load user interface and automated data quality control
  3. **Real-Time Onboard Processing**: Upgrade compute architecture with heterogeneous dual-core System-on-Chip (STM32MP1) for native turbulence/wave-state algorithms and real-time data transmission
  4. **Forecast Improvements**: Use S0 data to improve turbulent mixing parameterizations, enhance track/intensity forecasts, and assimilate into boundary-layer models
  5. **Extreme Environment Hardening**: Mitigate extreme cold (-65°F) and icing via heater-equipped pressure ports and advanced coatings
  6. **Autonomous Adaptive Sampling**: Implement closed-loop AI (Temporal Multimodal Multivariate Learner and IT-RRT planner) for real-time flight path optimization in high-uncertainty storm regions
  7. **DOW Integration**: Adapt S0 for compatibility with Navy Common Launch Tubes (CLT) and A-size sonobuoy canisters for deployment from P-8 and MH-60 platforms

## Products & Systems Referenced

### SwiftCore
- Modular, layered avionics architecture for autonomous flight control
- Target: NASA autonomy requirements

### S0 (S-Zero)
- Expendable atmospheric/air-sea profiling UAS
- Currently a proven NOAA research platform
- Planned for Navy operational use
- Proposed enhancements: heterogeneous dual-core compute (STM32MP1), advanced sensing, extreme hardening, autonomous adaptive sampling
- Deployment method: Navy Common Launch Tubes (CLT) and A-size sonobuoy canisters

### S0-MAD
- S0 variant with Magnetic Anomaly Detection sensor package
- Target performance: <20 pT/√Hz magnetic noise floor
- Use case: Anti-Submarine Warfare detection
- Constraint: Must fit within LAU-126A launch container

### S0-Acoustic
- S0 variant with passive acoustic sensing
- Use case: Anti-Submarine Warfare detection in coordination with S0-MAD

## Applications & Use Cases

1. **Anti-Submarine Warfare (ASW)**: Persistent, multi-modal search and detection with sonobuoy-launched platforms; distributed sensing to reduce detection latency and operator workload
2. **Atmospheric/Oceanographic Research**: Air-sea profiling, boundary-layer characterization, turbulent mixing measurement
3. **Hurricane/Severe Weather Operations**: Hazardous weather profiling; forecast model improvement via data assimilation; autonomous adaptive sampling in high-uncertainty storm regions
4. **Autonomous Navigation & Control**: Modular autonomy architecture for multi-vehicle coordination

## Key Technical Details

- **MAD Performance Target**: Magnetic noise floor <20 pT/√Hz under dynamic flight (improvement from Phase I lab/static performance)
- **Compute Architecture**: Heterogeneous dual-core STM32MP1 System-on-Chip for onboard real-time processing
- **AI/ML Methods**: Temporal Multimodal Multivariate Learner; IT-RRT (Information-Theoretic Rapidly-Exploring Random Trees) planner
- **Environmental Hardening**: Extreme cold (-65°F), icing mitigation, advanced chemical coatings
- **Launch Integration**: LAU-126A container, Navy Common Launch Tubes, A-size sonobuoy canisters, P-8 and MH-60 deployment platforms

## Notable Details

- **Research Transition Strategy**: Clear progression from Phase I feasibility to Phase II production-readiness and operational integration (2025-2030 timeline)
- **Multi-Agency Support**: NASA (autonomy), Navy (ASW and atmospheric profiling), NOAA collaboration (weather platform maturation)
- **User Interface Design**: Emphasis on low-cognitive-load web-based control to minimize operator burden
- **Expendable Platform Focus**: Both SL UAS and S0 designed as cost-effective, one-time-use or short-life assets
- **Distributed Sensing**: Phase II projects emphasize multi-modal, coordinated sensor packages (MAD + Acoustic; turbulence + wave state) for operational advantage
- **No Overlaps Declared**: All five projects certified as non-overlapping

---

**Note**: This is a compliance disclosure document listing active and proposed projects. It provides high-level objectives and funding amounts but not detailed technical specifications or results. Substantive technical and performance details would be found in the underlying proposal and project reports.