# Current and Pending Support Information - Maciej Stachura

## Document Metadata
- Type: NSF/OMB Current and Pending (Other) Support form (Biographical Sketch component)
- Client/Agency: National Science Foundation (OMB Form 3145-0279)
- Key Personnel: Maciej Stachura, Co-Founder and Chief Technology Officer, Black Swift Technologies LLC, Boulder, Colorado
- Date: Certified 2026-03-31
- Last Editor: Beck Cotter

## Executive Summary
This is a compliance form documenting Maciej Stachura's current and pending research support across five active and pending projects funded by NASA and the Department of the Navy. The projects span autonomous aircraft control architectures, sonobuoy-launched UAS with magnetic anomaly detection and acoustic sensing, and expendable atmospheric profiling systems for hazardous weather operations.

## Current Active Projects (as of 2026-03-31)

### 1. Adaptive and Secure Autonomy for UAS
- **Award Number:** A2.02-1017
- **Source:** NASA
- **Duration:** 09/2025 – 03/2026
- **Budget:** $149,711
- **Stachura Effort:** 0.5 person-months (2025), 0.1 person-months (2026)
- **Objectives:** Define and document a modular, multi-layer sensing and control architecture spanning multi-vehicle coordination, ML-based sensing/control, standard navigation (waypoint tracking, altitude/speed commands, velocity vectors), control loop modifications (dynamic PID tuning via TECS-like algorithms), and low-level sensor/actuator control. System employs standardized pub/sub messaging and service discovery.

### 2. Development of SL UAS with Advanced MAD and Acoustic Sensing (Phase I)
- **Award Number:** N251-016-0021
- **Source:** Department of the Navy
- **Duration:** 07/2025 – 06/2026
- **Budget:** $236,399
- **Stachura Effort:** 0.61 person-months (2025), 0.43 person-months (2026)
- **Objectives:** Establish technical feasibility of integrating magnetic anomaly detection (MAD) and passive acoustic sensing into a Sonobuoy-Launched UAS (SL UAS) platform.

### 3. Expendable Air-Sea Profiling Observations in Hazardous Weather (Phase I)
- **Award Number:** N25A-T025-0009
- **Source:** Department of the Navy
- **Duration:** 07/2025 – 06/2026
- **Budget:** $237,494
- **Stachura Effort:** 0.37 person-months (2025), 0.27 person-months (2026)
- **Objectives:** Quantify capabilities of S0 UAS to provide higher-resolution, more accurate, and more cost-effective atmospheric data compared to existing platforms (radiosondes) in challenging air-sea interaction regions.

## Pending Projects

### 4. Development of SL UAS with Advanced MAD and Acoustic Sensing (Phase II)
- **Award Number:** To be assigned
- **Source:** Department of the Navy
- **Duration:** 01/2027 – 06/2030
- **Budget:** $1,397,610
- **Stachura Effort:** 0.15 person-months (2027-2028), 0.17 person-months (2029-2030)
- **Objectives:** 
  - Transition Phase I technical feasibility into production-ready, mission-validated Sonobuoy-Launched UAS
  - Solve Navy's ASW problem: provide persistent, multi-modal anti-submarine warfare search/detection within extreme volumetric and magnetic constraints of LAU-126A launch container
  - Validate magnetic noise floor performance below 20 pT/√Hz threshold under dynamic flight maneuvers and propulsion-driven environments (Phase I achieved this in lab/static conditions)
  - Transition from component selection to hardened, production-representative airframe capable of launch shocks and autonomous water-landing-to-sensing transitions
  - Mature coordination between S0-MAD and S0-Acoustic variants
  - Provide Navy with expendable, distributed sensing capability reducing detection latency and operator workload vs. traditional episodic sonobuoy sampling

### 5. Expendable Air-Sea Profiling Observations in Hazardous Weather (Phase II)
- **Award Number:** To be assigned
- **Source:** Department of the Navy
- **Duration:** 01/2027 – 12/2030
- **Budget:** $2,000,000
- **Stachura Effort:** 0.17 person-months (2027), 0.15 person-months (2028), 0.13 person-months (2029-2030)
- **Objectives:** Transition S0 from proven NOAA research platform to fully integrated, turnkey Department of the Navy operational capability through seven key initiatives:
  1. **Calibration and Validation:** Extensive over-ocean flight campaigns validating sensing accuracy against buoy and tower data
  2. **Turnkey DOW Operation:** Web-based, low-cognitive-load UI and automated data quality control
  3. **Real-Time Onboard Processing:** Upgrade S0 compute architecture with heterogeneous dual-core System-on-Chip (STM32MP1) to run turbulence and wave-state algorithms natively, enabling real-time data transmission
  4. **Forecast Improvements:** Use S0 data to improve turbulent mixing parameterizations, enhance track/intensity forecasts, evaluate boundary-layer structure improvements through data assimilation
  5. **Extreme Environment Hardening:** Mitigate extreme cold (-65°F) and icing via heaters on pressure ports and advanced chemical coatings
  6. **Autonomous Adaptive Sampling:** Implement closed-loop AI using Temporal Multimodal Multivariate Learner and IT-RRT planner for real-time flight path optimization maximizing information gain in high-uncertainty storm regions
  7. **DOW Integration:** Adapt S0 for compatibility with Navy Common Launch Tubes (CLT) and A-size sonobuoy canisters for deployment from P-8 and MH-60 platforms

## Products & Capabilities Described

### S0 UAS
- Multi-role small unmanned aircraft system
- Current use: NOAA research platform for atmospheric profiling
- Phase II objective: Operational Department of the Navy system
- Planned capabilities: Heterogeneous dual-core compute (STM32MP1), real-time onboard processing, autonomous adaptive sampling with AI, extreme weather hardening

### S0-MAD Variant
- S0 configuration with magnetic anomaly detection for anti-submarine warfare
- Target performance: Magnetic noise floor below 20 pT/√Hz
- Phase II validation: Under dynamic flight maneuvers and propulsion-driven environments

### S0-Acoustic Variant
- S0 configuration with passive acoustic sensing for ASW
- Phase II goal: Coordinated multi-modal sensing with MAD variant

### Sonobuoy-Launched UAS (SL UAS)
- Expendable UAS deployable from LAU-126A launch container
- Constraints: Extreme volumetric and magnetic limitations
- Capability: Autonomous water-landing-to-sensing transitions

## Use Cases & Applications

### Navy Anti-Submarine Warfare (ASW)
- Persistent, multi-modal detection within sonobuoy container constraints
- Expendable, distributed sensing reducing detection latency and operator workload
- Deployment from P-8 and MH-60 platforms via Navy Common Launch Tubes

### NOAA/Navy Meteorological Operations
- Atmospheric profiling in hazardous/extreme weather conditions
- Air-sea interaction region monitoring
- Hurricane/tropical cyclone sampling
- Real-time onboard data transmission for operational forecasting
- Replacement for traditional radiosonde platforms

## Technical Details & Specifications

**Magnetic Anomaly Detection Performance:**
- Target threshold: <20 pT/√Hz magnetic noise floor
- Phase I achievement: Laboratory and static ground environments
- Phase II challenge: Validation under dynamic flight and propulsion

**Compute Architecture (Phase II S0):**
- Upgrade to STM32MP1 heterogeneous dual-core System-on-Chip
- Natively execute turbulence and wave-state algorithms
- Enable real-time data transmission

**Extreme Environment Specifications:**
- Cold tolerance: -65°F (-54°C)
- Icing mitigation: Pressure port heaters and advanced chemical coatings

**AI/Autonomy (Phase II S0):**
- Temporal Multimodal Multivariate Learner
- IT-RRT (Informed Temporal Rapidly-Exploring Random Trees) planner
- Real-time flight path optimization for maximum information gain in high-uncertainty regions

**Navigation & Control (NASA Project):**
- Pub/sub messaging architecture with service discovery
- Multi-layer architecture: multi-vehicle coordination → ML-based sensing/control → standard navigation → control loop modifications → sensor/actuator control
- Standard capabilities: waypoint tracking, altitude/speed command, velocity vectors
- Dynamic PID tuning via TECS-like algorithms

## Notable Details

1. **No Project Overlaps:** All projects explicitly certified as having no actual or potential overlaps with other support.

2. **Multi-Agency Portfolio:** Projects span NASA (flight control/autonomy) and Department of the Navy (ASW, meteorological operations), suggesting BST is a strategic vendor for autonomous systems across federal agencies.

3. **Phase Progression:** Multiple Phase I projects (SL UAS MAD, S0 air-sea profiling) with matching Phase II proposals pending, indicating successful Phase I validation and continuity planning.

4. **Budget Escalation:** Phase II budgets significantly larger ($1.4M–$2M over 3-4 years) than Phase I ($236K–$237K over 1 year), consistent with transition to production/operational capability.

5. **Personnel Commitment:** Stachura's effort is modest (0.1–0.61 person-months per year), suggesting mature project execution delegated to larger teams while he retains CTO oversight.

6. **Operational Transition Strategy:** S0 explicitly framed as transitioning from research (NOAA) to operational (Department of the Navy) platform, indicating commercialization/military adoption pathway.

7. **Advanced Sensing Integration:** Projects combine traditionally separate domains—ASW (MAD + acoustics), meteorology (profiling), autonomous systems (AI-based flight planning)—suggesting BST capability in multi-modal sensor fusion.