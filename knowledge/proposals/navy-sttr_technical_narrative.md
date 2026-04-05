# Navy STTR Phase I Proposal: Expendable Air-Sea Profiling Observations in Hazardous Weather

## Document Metadata
- **Type:** STTR Phase I Proposal / Technical Narrative
- **Client/Agency:** U.S. Navy / Office of Naval Research (ONR)
- **Program/Solicitation:** Navy STTR N25A-T025-0009 (Topic: Expendable Air-sea Profiling Observations in Hazardous Weather Conditions)
- **Date:** Submitted January 2025 (document modified through December 2024)
- **BST Products/Systems Referenced:** S0 UAS (unmanned aircraft system), onboard sensors and flight management systems
- **Key Personnel:** 
  - Jack Elston (PI, CEO/Co-founder, BST)
  - Maciej Stachura (CTO, BST)
  - Joshua Wadler (Embry-Riddle Aeronautical University)
  - Jun Zhang (University of Miami)
  - John Park (Old Dominion University)

## Executive Summary
Black Swift Technologies proposes to adapt its proven S0 unmanned aircraft system for Navy-specific atmospheric profiling missions in severe weather environments, particularly tropical cyclones and polar lows. The S0 offers superior cost-effectiveness, higher temporal/spatial resolution, and extended flight duration compared to existing radiosondes and NCAR dropsondes, while eliminating personnel risk. The Phase I effort will validate the S0's capabilities, address technical limitations, and develop integration pathways for Navy operational deployment through partnerships with Embry-Riddle Aeronautical University, University of Miami, and Old Dominion University.

## Technical Approach

### Core Concept
Leverage BST's S0 UAS—a small, purpose-built platform already validated in extreme hurricane conditions—as a cost-effective, expendable atmospheric profiler to supplement and enhance Navy weather observation capabilities. The S0 combines:
- **Disposable air-deployed version** (launched from aircraft like P-3)
- **Reusable VTOL version** (launched from ships or land platforms)

### Proven Platform Performance (2024 Hurricane Season)
- 19 S0 UAS deployed by NOAA into four tropical cyclones (Ernesto, Francine, Helene, Milton)
- Operated in extreme conditions: vertical velocities to 30 m/s, horizontal winds to 209 knots simultaneously (Hurricane Milton)
- Battery endurance: >90 minutes demonstrated, extendable to 120 minutes
- Data collection: 3D winds, pressure, temperature, humidity, sea surface temperature, wave height
- Validation: Wind measurements validated against ARM Southern Great Plains 60 m tower (mean differences <0.50 m/s for all three wind components)

### Cost-Effectiveness Advantage
- **S0 cost:** $15K for ~120 minutes of low-altitude data
- **NCAR dropsonde cost:** ~$1000 for <5 minutes of data (from P-3)
- **Ratio:** S0 provides 24x more data per unit cost; reusable S0 versions offer 50-100x improvement over dropsondes

### Key Technical Capabilities
1. **Advanced sensors:**
   - Multi-hole probe for 3D wind measurement (100 Hz sampling rate)
   - Temperature/humidity sensors with improved shrouds to reduce solar bias
   - Laser altimeter for sea surface detection (with radar alternative being evaluated)

2. **Flight management:**
   - Autonomous programming with operator override capability
   - Stepped descent patterns (e.g., ~10 min holds at specific altitudes to measure boundary layer turbulence)
   - Spiral flight patterns for atmospheric profiling
   - Typical ascent rate: 4 m/s; descent rate: 6 m/s

3. **Onboard processing:**
   - Sufficient computing capability to support new automated sampling algorithms
   - Software API for development of new sampling strategies

## Products & Capabilities Described

### S0 UAS Platform

**What it is:**
- Small, lightweight unmanned aircraft (2.6 pounds documented in 2023 deployment)
- Designed specifically for atmospheric profiling in extreme turbulent environments
- Two operational variants: expendable air-deployed and reusable VTOL

**Proposed use in this context:**
- Replace or augment radiosondes and dropsondes for Navy atmospheric profiling in hazardous weather
- Integration with Navy launch platforms: sonobuoy launch systems, external pods on P-8A Poseidon, CH-53E helicopters
- Real-time data assimilation into Navy forecasting systems (COAMPS-TC mentioned as example)

**Specifications and performance claims:**
- Flight endurance: 90+ minutes (extendable to 120 min)
- Altitude range: Capable of low-altitude air-sea interface measurement to higher altitudes
- Wind measurement accuracy: Validated within 0.50 m/s across all components
- Operational ceiling: Proven in Category 5 hurricanes, heavy rain, extreme wind shear
- Data rate: 100 Hz for wind measurements onboard
- Deployment diversity: Air-deployable from P-3, ship-launchable, land-launchable (VTOL variant)

## Use Cases & Applications

### Primary Mission: Hazardous Weather Observation
1. **Tropical Cyclone Monitoring:**
   - Real-time data collection from eyewalls and boundary layers
   - Air-sea interface measurements critical for understanding storm intensification
   - Boundary layer thermodynamics and structure characterization

2. **Polar Operations:**
   - Polar low monitoring
   - Polar ice edge measurements
   - Extended-duration sampling enabled by autonomous control

3. **Naval Operational Support:**
   - Decision support for maritime operations in severe weather
   - Real-time data for forecasting model assimilation
   - Personnel safety (eliminates crewed aircraft risk in extreme conditions)

### Secondary Applications
- Coastal monitoring
- Environmental research partnerships (e.g., ONR MURI SASCWATCH on air-sea coupling)
- Disaster response
- Climate research

## Phase I Technical Objectives (Base and Option)

### Base Phase (6 months)

**Objective 1: Quantify Enhanced Observation Capabilities**
- Comparative analysis of S0 vs. radiosondes, AVAPS dropsondes, competing systems (Raytheon Coyote, Anduril Altius-600)
- Metrics: data resolution, accuracy, cost-effectiveness, spatial/temporal coverage
- Focus on air-sea interaction regions and boundary layer processes

**Objective 2: Assess and Improve S0 Capabilities**
- Identify error sources in wind, turbulence, and vertical velocity measurements
- Calibration/validation through wind tunnel tests and field deployments
- Error mitigation strategies
- Icing capability assessment and design updates

**Objective 3: Produce New and Unique Observations**
- Develop algorithms for vertical wind measurement (100 Hz data)
- Implement onboard turbulence calculations
- Wave spectra/energy characterization via onboard radar
- Expand beyond hurricane-specific missions to other environmental applications

**Objective 4: Automatic Targeting of Areas of Interest**
- Develop two autonomy levels:
  - **Open-loop:** Preprogrammed sampling based on TC forecast model utilities
  - **Closed-loop:** Machine learning surrogate models with real-time adaptive updates
- AI algorithms with dimensionality reduction for onboard computing constraints

### Option Phase (6 months)

**Option 1: Phase II Cal/Val Plan**
- Wind tunnel testing protocols
- Field validation against instrumented towers
- Comparative studies with NCAR dropsondes
- Refinement of algorithms for vertical velocity and turbulence

**Option 2: Wave Measurement Development**
- Evaluate radar alternatives to laser altimeter
- Characterize wave shape, frequency, height, and spectra
- Test in precipitation and cloud conditions
- Ensure rapid measurements at ground speeds >200 mph

**Option 3: S0 Operation in Icing**
- Identify icing impacts on multi-hole probe, wings, propellers
- Design heating elements or de-icing coatings
- Enable all-weather Navy operational capability

**Option 4: Stakeholder Engagement and Integration Planning**
- Interview DoD stakeholders on launch platforms, comms, data formats
- Develop detailed integration plan for large-scale deployment
- Address hardware, software, and logistical requirements

## Phase I Work Tasks by Organization

| Task | Primary Organizations | Scope |
|------|----------------------|-------|
| **B.1: Background Review** | ERAU, UM, BST | Literature review of AVAPS, radiosondes, competitors; cost/accuracy/coverage analysis |
| **B.2: S0 Data Analysis & Enhancements** | BST, ERAU, UM, ODU | Integration with Navy platforms; error analysis; icing mitigation strategies |
| **B.3: Turbulence & Wave Measurements** | BST, ERAU, UM | Onboard turbulence algorithms (100 Hz); radar-based wave height/spectra |
| **B.4: Automatic Sampling** | ODU, BST | Open-loop preprogrammed rules; closed-loop ML surrogate models with dimensionality reduction |
| **O.1: Cal/Val Plan** | ERAU, UM, BST, ODU | Wind tunnel tests, field comparisons, algorithm refinement |
| **O.2: Wave Measurement Dev.** | BST, ERAU, UM | Radar system evaluation, precipitation testing, high-speed measurement validation |
| **O.3: S0 Operation in Icing** | BST | Design updates for multi-hole probe, wings, propellers; heating/de-icing systems |
| **O.4: Stakeholder Engagement** | BST, ERAU, UM, ODU | DoD interviews, integration planning, deployment roadmap |

## Key Results & Validation Data

### Wind Measurement Validation (Existing)
- **Test:** 10 S0 flights vs. ARM Southern Great Plains 60 m tower (March-April 2021)
- **Result:** Mean wind speed differences <0.50 m/s across zonal (u), meridional (v), and vertical (w) components
- **Finding:** S0 captured similar histogram distributions and turbulence variance as calibrated tower
- **Status:** Recent sensor setup changes and new shrouds implemented; peer-review manuscript in preparation

### Performance in Extreme Conditions (2024 Hurricane Season)
- **Flights:** 19 S0 deployed into Hurricanes Ernesto, Francine, Helene, Milton
- **Extreme conditions encountered:** Vertical velocities 30 m/s, horizontal winds 209 knots simultaneously
- **Data collection:** Continuous 3D atmospheric and surface measurements from boundary layer to higher altitudes
- **Outcome:** Demonstrated operational feasibility in Category 5 hurricane eyewalls

### Comparative System Analysis
- **Competitors evaluated:**
  - NCAR AVAPS dropsondes: $1K per <5 min profile from specialized aircraft
  - Radiosondes: Limited temporal/spatial resolution, twice-daily fixed locations, single-use, logistically difficult at sea
  - Raytheon Coyote: Larger, more expensive
  - Anduril Altius-600: Larger, designed for different missions
  
- **S0 advantages:** Lower cost, higher endurance, operator-controlled targeting, reusable variants, air-sea interface access

## Notable Details

### Strategic Partnerships
1. **NOAA Collaboration:** 
   - Operational partnership demonstrated through 2023-2024 hurricane deployments
   - Co-developed S0 platform with NOAA
   - Access to NOAA facilities and datasets for validation

2. **University Research Team:**
   - **Embry-Riddle Aeronautical University:** Wind tunnel facilities for sensor calibration; boundary layer expertise (Joshua Wadler)
   - **University of Miami:** Air-sea interaction and turbulence expertise (Jun Zhang); boundary layer thermodynamics
   - **Old Dominion University:** AI/machine learning for adaptive sampling strategies (John Park)
   - All institutions have advanced computational resources for algorithm development

3. **ONR MURI Alignment:**
   - Proposed work coordinates with Dr. David Richter's ONR MURI "SASCWATCH" (Study on Air-Sea Coupling with Waves, Turbulence, and Clouds at High Winds)
   - Mutual benefit: SASCWATCH needs turbulence/wave measurements; S0 provides platform

### Competitive Advantages Highlighted
1. **Cost efficiency:** 2x to 50-100x cost advantage depending on comparison platform
2. **Proven platform:** Multiple successful hurricane deployments (19