# Navy STTR Phase I Proposal: Expendable Air-Sea Profiling Observations in Hazardous Weather

## Document Metadata
- **Type:** STTR Phase I Proposal - Technical Narrative
- **Client/Agency:** Office of Naval Research (ONR), Department of Defense
- **Program/Solicitation:** Navy STTR 25.A (N25A-T025-0009) - Hazardous Weather Topic
- **Date:** Submitted February 2025
- **BST Products/Systems Referenced:** S0 UAS (both air-deployed disposable and ship/land-launched VTOL reusable versions)
- **Key Personnel:** 
  - Jack Elston (BST, PI/CEO & Co-founder)
  - Maciej Stachura (BST, CTO)
  - Joshua Wadler (Embry-Riddle Aeronautical University, Co-I)
  - Jun Zhang (University of Miami, Co-I)
  - John Park (Old Dominion University, Co-I)

## Executive Summary

Black Swift Technologies proposes to adapt and enhance the S0 unmanned aircraft system (UAS) for Navy-specific atmospheric profiling in hazardous weather conditions, particularly tropical cyclones and polar lows. Building on proven capability demonstrated through 19 S0 deployments into four hurricanes in 2024 (Ernesto, Francine, Helene, Milton), BST aims to overcome limitations of traditional radiosondes and dropsondes through improved spatial/temporal resolution, extended flight duration (120 minutes vs. 5 minutes for dropsondes), and significantly lower cost per observation ($15K disposable vs. $1,000 per dropsonde).

## Technical Approach

### S0 UAS Platform Design
The S0 platform exists in two configurations:
- **Air-deployed disposable version:** Dropped from aircraft, cost-effective for single-use missions
- **VTOL reusable version:** Land or ship-launched, recoverable for multiple deployments

### Key Technical Specifications (Demonstrated 2024)
- **Flight endurance:** 90+ minutes baseline, extendable to 120 minutes by project start
- **Ascent rate:** 4 m/s
- **Descent rate:** 6 m/s
- **Extreme environment capability:** Demonstrated operation in:
  - Vertical velocities up to 30 m/s
  - Horizontal wind speeds up to 209 knots
  - Both experienced simultaneously in Hurricane Milton
  - Heavy precipitation and turbulent boundary layer conditions

### Sensor Suite
- **Primary wind measurement:** Multi-hole probe with 100 Hz onboard wind calculation capability
- **Atmospheric measurements:** 3D winds, pressure, temperature, humidity
- **Oceanographic measurements:** Sea surface temperature, wave height (laser altimeter currently; radar alternative under investigation)
- **Flight management:** Advanced onboard computing and software API for autonomous mission planning

### Cost Advantage Over Existing Systems
- Disposable S0: ~2x cost advantage over dropsondes
- Reusable S0: 50-100x cost advantage per observation
- S0 provides 120 minutes of data at low altitude for $15K vs. 5 minutes of dropsonde data for $1,000

## Products & Capabilities Described

### S0 UAS
**What it is:** Purpose-built small UAS designed for atmospheric profiling in extreme weather environments

**Current capabilities:**
- Collects 3D wind, pressure, temperature, humidity at high temporal/spatial resolution
- Autonomous or manually-controlled flight with operator override
- Can execute stepped descent patterns for boundary layer turbulence measurement (~10 minutes per altitude level)
- Can execute spiral flight patterns for vertical profiling
- Eliminates personnel safety risks compared to crewed aircraft in hazardous conditions
- Compatible with modern data assimilation systems (e.g., COAMPS-TC for tropical cyclone forecasting)

**Validation results:**
- Wind measurement validation against ARM Southern Great Plains (SGP) 60 m tower (March-April 2021):
  - Mean differences in average wind speed within 0.50 m/s for all three wind components (u, v, w)
  - Successfully captured similar turbulence characteristics as calibrated tower
  - Demonstrated ability to measure momentum and sensible heat fluxes
- Independent validation by de Boer et al. (2024): S0 provided reasonable atmospheric state measurements; biases subsequently addressed through sensor setup changes and new solar-blocking shroud for temperature/humidity

### Proposed Enhancements (Phase I Focus)

**Data processing improvements:**
- Refined algorithms for vertical velocity and turbulence estimation
- Onboard high-rate turbulence computation (100 Hz wind data processing)
- New algorithms for wave spectra and energy characterization using onboard radar

**Hardware improvements:**
- Integration with Navy-specific launch platforms (sonobuoy launch systems, external pods on P-8A Poseidon or CH-53E helicopters)
- Alternative wave measurement sensors (radar to replace laser altimeter struggling in heavy precipitation)
- Icing mitigation strategies (heating elements, de-icing coatings)
- Extended endurance battery optimization

**Autonomous capabilities:**
- Open-loop automatic sampling: Preprogrammed flight rules derived from TC forecasting model utilities
- Closed-loop sampling: Machine learning surrogate models trained on hurricane forecasting data enabling adaptive real-time learning as new observations are acquired
- AI-based dimensionality reduction for onboard computation constraints

## Use Cases & Applications

### Primary Mission: Tropical Cyclone Observation
- Real-time data collection from hurricane eyewalls and boundary layers
- Measurement of air-sea interactions at the marine atmospheric boundary layer (MABL)
- Drag coefficient (C_D) characterization at high winds—critical for TC intensity prediction
- Data for improving COAMPS-TC and other Navy forecasting models

### Demonstrated 2024 Operations
- Four hurricanes: Ernesto, Francine, Helene, Milton
- 19 S0 aircraft deployed from NOAA WP-3D (P-3) aircraft
- Collected data in previously inaccessible regions (hurricane eyewalls)

### Extended Applications (Phase I/II Development)
- **Polar environments:** Polar low monitoring, ice edge research
- **Maritime operations:** Support for Navy operations in severe weather
- **Disaster response:** Environmental monitoring and risk assessment
- **Climate research:** Air-sea coupling studies, ocean-atmosphere interaction dynamics

## Phase I Objectives & Deliverables

### Objective 1: Quantify Enhanced Observation Capabilities
- Comparative analysis vs. radiosondes on data resolution, quality, and cost-effectiveness
- Assessment of S0 capacity for high-resolution, dense data in air-sea interaction regions
- Documentation of advantages over dropsondes and radiosondes

### Objective 2: Assess & Improve S0 Capabilities
- Error analysis identifying sources of uncertainty in wind, turbulence, and vertical velocity measurements
- Calibration and validation through:
  - Wind tunnel tests
  - Field deployments in controlled conditions
  - Comparative studies with instrumented towers and NCAR dropsondes
- Icing impact evaluation and mitigation strategy identification
- Algorithm refinements for maximum data quality

### Objective 3: Produce New & Unique Observations
- Vertical wind measurement implementation
- Turbulence measurements from 3D wind data (new vs. legacy systems)
- Wave property characterization using onboard radar
- Software/hardware updates for non-hurricane environments

### Objective 4: Automatic Target Areas of Interest
- Development of automated sampling strategies for air-sea/ice interface areas
- Leverage existing onboard computing capability and software API
- Preparation for operational Navy deployment

### Base Tasks (6-month + 6-month Option period)

**B.1: Background Review and Comparative Analysis (ERAU, UM, BST)**
- Detailed review of existing platforms (NCAR dropsondes, radiosondes, Raytheon Coyote, Anduril Altius-600)
- Comparative analysis: cost, data accuracy, spatial/temporal coverage, longevity
- Prior S0 mission results highlighting strengths and improvement areas

**B.2: S0 Data Analysis and Enhancements (BST, ERAU, UM, ODU)**
- Integration plan with Navy launch platforms (sonobuoy, P-8A external pod, CH-53E)
- Simulations and mechanical validation of platform compatibility
- Detailed error analysis of current S0 data
- Icing impact assessment and mitigation strategies

**B.3: Turbulence and Wave Height Measurements (BST, ERAU, UM)**
- Onboard turbulence computation algorithms from 100 Hz wind data
- Wave height measurement development (radar sensor quantification)
- Measurement accuracy requirements specification

**B.4: Automatic Sampling (ODU, BST)**
- Open-loop autonomous sampling: preprogrammed rules from TC forecasting model utilities
- Closed-loop autonomous sampling: machine learning surrogate models with real-time adaptive learning
- AI dimensionality reduction for UAS computational constraints

### Option Tasks (Phase II Preparation)

**O.1: Phase II Cal/Val Plan (ERAU, UM, BST, ODU)**
- Wind tunnel tests
- Field deployments in controlled conditions
- Comparative studies with instrumented towers and NCAR dropsondes
- Algorithm refinement for vertical velocity and turbulence estimation

**O.2: Wave Measurement Development (BST, ERAU, UM)**
- Radar vs. laser-based systems evaluation
- Wave shape, frequency, height measurement accuracy
- High-speed measurement capability (200+ mph ground speed)

**O.3: S0 Operation in Icing (BST)**
- Multi-hole probe icing impact assessment
- Wing and propeller icing evaluation
- Design updates enabling icing condition operation

**O.4: Stakeholder Engagement and Integration Planning (BST, ERAU, UM, ODU)**
- DoD stakeholder interviews on preferred launch platforms, communication systems, data delivery formats
- Navy operator collaboration on operational requirements
- Detailed large-scale deployment integration plan

## Key Results & Validation Data

### 2024 Hurricane Deployments
- Successfully deployed S0 into four hurricanes with 19 aircraft
- Collected 3D winds, pressure, temperature, humidity, SST, and wave height data
- Operated in extreme conditions: vertical velocities to 30 m/s, horizontal winds to 209 kts simultaneously

### SGP Wind Tower Validation (2021)
- 10 S0 flights over 3 days compared against ARM SGP 60 m tower
- **Zonal wind (u):** Mean difference <0.50 m/s
- **Meridional wind (v):** Mean difference <0.50 m/s
- **Vertical wind (w):** Mean difference <0.50 m/s
- Successfully captured increasing turbulence variance on day 3, matching tower observations
- Wind speed histogram distributions similar between S0 and calibrated tower

### Independent Comparative Study (de Boer et al. 2024)
- S0 tested against commercial sUAS and three university-developed research systems
- Finding: S0 provided reasonable atmospheric state measurements
- Demonstrated ability to measure momentum and sensible heat fluxes
- All sUAS had errors vs. SGP tower; S0 biases subsequently corrected through:
  - Sensor setup changes
  - New solar-blocking shroud for temperature/humidity

### Boundary Layer Observations
- Stepped descent flight patterns successfully collected boundary layer turbulence features
- Each descent step ~10 minutes at specific altitudes as designed
- Data quality suitable for understanding air-sea interactions and TC intensification processes

## Notable Details

### Partnerships & Supporting Research
- **NOAA Collaboration:** Active ongoing partnership with NOAA using NOAA WP-3D (P-3) for deployment
- **University Team:** Embry-Riddle, University of Miami, Old Dominion University providing specialized expertise
  - ERAU: Wind tunnel facilities for sensor characterization
  - UM: Boundary layer physics and air-sea interaction expertise
  - ODU: AI/machine learning for autonomous sampling
- **ONR MURI SASCWATCH Connection:** Proposal team will collaborate with Dr. David Richter's (University of Notre Dame) ONR MURI on air-sea coupling with waves, turbulence, clouds at high winds

### Competitive Positioning vs. Legacy Systems

**vs. Dropsondes (NCAR AVAPS/Vaisala):**
- Cost: 2x lower for disposable S0 (requires specialized P-3/WC-130J aircraft)
- Endurance: 120 min vs. 5 min data collection
- Coverage: Multiple simultaneous deployments possible; episodic vs. continuous data
- Accessibility: Can target specific