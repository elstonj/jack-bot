# UAS Data Assimilation for Improved Wildland Fire Fighting Decision Support

## Document Metadata
- **Type**: NASA SBIR Phase I Proposal
- **Client/Agency**: NASA (Subtopic A3.02: Advanced Air Traffic Management for Nontraditional Airspace Operations)
- **Program/Solicitation**: NASA SBIR 2023-I; Proposal Number 23-1-A3.02-1718
- **Date**: March 14, 2023 (submitted)
- **BST Products/Systems Referenced**: S0 VTOL UAS, SwiftTab User Interface, SwiftFlow Probe (meteorological sensor package)
- **Key Personnel**: Jack Elston (CEO/Co-founder, Principal Investigator, Authorized Contract Negotiator)

## Executive Summary
Black Swift Technologies proposes a pilot study to demonstrate how targeted UAS observations collected near wildland fires can be assimilated into meteorological models to improve low-level wind and turbulence forecasts essential for safe aerial firefighting operations. Partnering with NCAR/RAL and Colorado's Center of Excellence for Advanced Technology Aerial Firefighting, BST's S0 UAS will collect 3D wind, pressure, temperature, and humidity data that will be processed through an Ensemble Kalman Filter approach to generate enhanced wind/turbulence guidance products integrated into wildfire management systems (ATAK). The work directly addresses safety concerns highlighted by fatal air tanker crashes caused by undetected low-level turbulence.

## Technical Approach

**Core Innovation**: Integration of three existing technologies—BST's S0 UAS, NCAR's data assimilation system (Ensemble Kalman Filter), and existing wildfire airspace management tools (ATAK/CivTAK)—to create a near-real-time wind and turbulence guidance product.

**Methodology**:
1. **UAS Sampling Strategy**: Use ensemble sensitivity analysis on historical fires (e.g., Calwood Fire, Four Mile Canyon Fire) to identify areas of greatest uncertainty in wind forecasts and optimal UAS deployment locations
2. **Data Collection**: Deploy S0 VTOL platforms to collect in-situ atmospheric measurements (3-component winds, pressure, temperature, relative humidity at 100 Hz sensor rate)
3. **Data Assimilation**: NCAR applies EnKF methodology tailored for UAS observations to produce 4D gridded analyses of wind and turbulence
4. **Validation**: Compare assimilated forecasts against independent truth data from additional UAS flights and surface stations (e.g., CU Boulder observatory)
5. **Integration**: Develop interfaces to feed enhanced wind/turbulence products into ATAK for wildfire operations coordination and dissemination to incident commanders, crewed aircraft, and UTM systems

**Technical Objectives** (Phase I focus):
- Develop automated UAS sampling algorithms to generate flight patterns based on forecast models and current observations
- Create operational requirements document for safe S0 UAS deployment near wildfires
- Conduct 1-2 high-risk fire day data collection flights in Boulder County foothills
- Quantify forecasting improvements in low-level winds over 3-12 hour periods post-sampling
- Demonstrate sequential flights improving validation

**TRL Progression**: Begin TRL 4 → End TRL 7

## Products & Capabilities Described

### S0 VTOL UAS
- **What**: Electric, vertical takeoff and landing aircraft developed in partnership with NOAA and Air Force
- **Specifications**:
  - Weight: 1.8 kg
  - Wingspan: 1.5 m
  - Cruise endurance: 60 minutes
  - Communication range: 10 km
  - Launch type: VTOL (enables operations in complex terrain)
  - Sensing payload: 3D inertial winds, pressure, temperature, humidity
- **Proposed use**: Collect targeted atmospheric observations near wildfires; data integrated into data assimilation models
- **Ruggedness**: Designed for harsh environmental conditions including hurricanes, convective storms, wildfires
- **Users**: NOAA, Air Force

### SwiftFlow Probe (Meteorological Sensor Package)
- **Specifications**:
  - Weight: 50 g
  - Wind velocity resolution: 0.03 m/s; Accuracy: ±0.29 m/s
  - Temperature range: -40°C to 85°C; Accuracy: ±0.3°C
  - Pressure resolution: 0.012 mbar; Accuracy: ±1.5 mbar
  - Relative humidity range: 0-100% RH; Accuracy: ±1.3% RH
  - Sensor rate: 100 Hz
- **Proposed use**: Provide accurate in-situ atmospheric measurements for data assimilation

### SwiftTab User Interface
- **What**: BST's proprietary UAS management system designed with safety and minimal operator overhead in mind
- **Proposed use**: Extended to be compatible with Android Team Awareness Kit (ATAK) for disseminating wind/turbulence data in wildfire operations
- **Capability**: Manages multiple UAS from single interface; simplifies data presentation, especially during faults

### NCAR/RAL Data Assimilation System
- **Methodology**: Ensemble Kalman Filter (EnKF) approach tailored to assimilate UAS observations
- **Outputs**: 4D gridded analyses and predictions of winds and turbulence; vertical velocity distributions as proxies for turbulence
- **Capability**: Observing System Experiments (OSEs) to quantify impact of targeted UAS measurements

## Use Cases & Applications

### Primary Use Case: Wildland Firefighting Safety
- **Problem addressed**: Fatal air tanker crashes caused by undetected low-level turbulence (referenced: NTSB Accident CEN22FA035, late 2021 nighttime air tanker crash)
- **Solution benefits**:
  - Enable safe nighttime wildfire operations by providing accurate turbulence forecasts
  - Create "map of safe operational envelopes" for crewed and uncrewed aircraft based on turbulence/wind hazard data
  - Replace high-risk pilot reports (which require aircraft to enter dangerous areas) with model-derived guidance
  - Accelerate UAS integration into aerial firefighting by demonstrating safety enhancement for skeptical crewed aircraft operators
  - Support incident commanders in strategic planning and asset allocation

### Secondary/Extensible Applications
- **Advanced Air Mobility (AAM)**: Low-altitude wind forecasts for mountainous areas and urban corridors
- **NASA 3D-Winds Mission**: Support for Earth Science programs (National Research Council Decadal Survey)
- **Fire prediction**: Improved short-term weather forecasts supporting fire spread modeling
- **UTM systems**: Integration of wind/turbulence data into weather-aware Traffic Management Systems
- **Package delivery UAS**: Provision of wind/turbulence information for low-altitude autonomous flights

### Operational Partners Identified
- California Department of Forestry and Fire Protection (CalFire)
- Colorado Center of Excellence for Advanced Technology Aerial Firefighting
- NOAA (existing relationship via FIREX project; NightFOX project for nighttime operations)

## Key Results
This is a Phase I proposal, so no results are reported. However, the proposal outlines specific deliverables and success metrics:

**Phase I Deliverables**:
1. Document detailing operational requirements, risks, and mitigation strategies for S0 deployment near wildfires
2. Ensemble sensitivity analysis identifying optimal UAS sampling locations for 2 historical fire cases
3. Data collected from 1-2 high-risk fire days in Boulder County
4. Quantified forecasting improvement metrics (wind/turbulence accuracy, spatial/temporal coverage)
5. Interface specifications and data formats for integrating wind/turbulence products into ATAK
6. Assessment of commercial viability and Phase II/III funding pathways

**Validation Approach**:
- Compare NCAR DA-generated wind fields against independent truth data (separate UAS vertical profiles, surface stations)
- Assess improved prediction of vertical velocities and turbulence distributions
- Measure forecast skill over 3-12 hour time horizons

## Notable Details

### Partnership Structure
- **Black Swift Technologies**: Lead; system integration, UAS operations, commercialization
- **NCAR/RAL**: Data assimilation expertise, EnKF methodology, real-time DA system development
- **Colorado CoE for Advanced Technology Aerial Firefighting**: Operational requirements definition, regulatory/TFR coordination
- **Autonodyne**: UTM/airspace integration software (participating in NIST PULSE accelerator with BST)
- **EKase Consulting**: Technical and Business Assistance services ($6,500 TABA funding)

### Budget Summary (6-month Phase I)
- **Total proposed**: $155,956.25
- **BST direct labor**: $84,471.56 (4 staff: PhD Aerospace Engineer PI at $82/hr, Lead Engineer at $67/hr, Mechanical Engineer at $53/hr, Software Engineer at $80/hr)
- **NCAR/RAL subcontract**: $33,580.11
- **G&A rate**: 18.32%
- **Profit margin**: 7%
- **Fringe rate**: 29.28% (based on NOAA negotiated agreement)

### Company Profile
- **Size**: 8 current employees; projected growth to 16 in 3 years
- **Location**: 2840 Wilderness Pl Ste D, Boulder, CO 80301
- **Business strategy**: Revenue growth through technology R&D and consulting (not I-Corps participation planned)
- **Existing customer base**: NOAA, Air Force, recognized for reliable platforms for atmospheric research in extreme conditions (high-altitude, arctic, desert, volcanoes, tornadoes, hurricanes)

### Competitive Advantages Highlighted
1. **Existing BST capabilities**: Purpose-built scientific platforms, system integration expertise, proven performance in extreme atmospheric environments
2. **Novel combination**: First application combining UAS meteorological observations + EnKF data assimilation + wildfire operations integration
3. **State-of-art gap**: Current wildfire operations rely on inadequate standard aviation weather services or high-risk pilot reports; proposed system offers fine-scale turbulence detection and forecasting
4. **Scalability**: Open interfaces and established data standards enable adding weather measurement capability to other aerial/ground-based wildfire assets
5. **Regulatory pathway**: Existing NOAA/FIREX relationship and NightFOX nighttime operations work provide foundation for TFR/regulatory coordination

### Known Relationships & Precedents
- **NOAA partnership**: Joint development of S0 VTOL platform; existing FIREX project collaboration; NightFOX project for nighttime wildfire operations
- **NCAR collaboration**: Multi-year partnership on UAS data assimilation; existing EnKF capabilities tailored to UAS observations
- **NIST PULSE accelerator**: Both BST and Autonodyne using program for customer discovery toward combined UTM/wildfire platform

### Unaddressed/Risk Areas
- Phase I focuses on research validation; actual TFR-integrated operations planned for Phase II
- Daytime operations near active fires limited by crewed aircraft conflicts; Phase II strategy includes nighttime operations and just-outside-TFR positioning
- Software integration with ATAK not yet developed; needs exploration of CivTAK compatibility
- Commercial path dependent on regulatory approval for UAS near-fire operations