# Nighttime Fire Observations eXperiment (NightFOX) - UAS wildfire measurements in support of FIREX and fire weather forecasting

## Document Metadata
- Type: NOAA research proposal
- Client/Agency: NOAA Earth System Research Laboratory (ESRL), Chemical Sciences Division (CSD)
- Program/Solicitation: NOAA UAS Program RFP (FIREX-related)
- Date: March 2017 (submitted); performance period FY17-FY19 (June 1, 2017 – September 30, 2019)
- BST Products/Systems Referenced: SuperSwift UAS
- Key Personnel: 
  - Ru-Shan Gao (PI, NOAA/ESRL/CSD) 
  - Karen Rosenlof, Troy Thornberry (NOAA/ESRL/CSD)
  - Brian Argrow (University of Colorado)
  - Sher Schranz (NOAA/ESRL/GSD)

## Executive Summary
NightFOX proposes to design, build, and deploy an integrated UAS Observation System (UASOS) based on the SuperSwift platform to conduct nighttime measurements of wildfire emissions and properties. The system addresses a critical data gap in fire research by combining in situ (CO2, CO, aerosol, meteorology) and remote sensing (fire radiative power, fire perimeter) instrument packages to support NOAA's FIREX field mission (July-September 2019) and improve fire weather forecasting models. Nighttime measurements are impossible with manned aircraft due to safety concerns but essential for understanding the full diurnal fire emission cycle and localized air quality impacts.

## Technical Approach

### UAS Platform Selection
- **SuperSwift UAS** (Black Swift Technologies, Boulder, CO)
  - Selected over alternatives (Tempest, Penguin BE, Puma AE) for three key attributes:
    1. Sufficient 5 lb payload capacity for planned instruments
    2. Operational radius 30-60 km adequate for fire observations
    3. Forward-located, spacious, interchangeable nose-cone payload bay ideal for atmospheric sampling and instrument swapping
  - Specifications: MTOW 16 lbs, 10 ft wingspan, 2+ hr endurance, 18 m/s cruise speed, 20 kft ceiling, hand launch, belly-skid landing
  - Key advantage for fire work: electric propulsion avoids air-breathing engine vulnerability to dense fire plume encounters

### In Situ Payload Development
- **Sensors planned**: CO2, CO, aerosol (fine and coarse modes), ambient RH, temperature, pressure, wind
- **Design goals**:
  - Research-grade sensitivity for fire plume measurements
  - 1-second response time (critical for spatial resolution at 20 m/s aircraft speed; 25-s response = 0.5 km blur)
  - Cost target: $10-15K per package (~10× cheaper than manned aircraft equivalents)
  - Total weight: <5 lbs
  
- **Specific instruments**:
  - **CO2/CO**: Commercial sensors with modifications for improved response time; custom sensors if needed
  - **Fine-mode aerosol (140-3000 nm)**: Custom sensor previously developed (Gao et al., 2016)
  - **Coarse-mode aerosol (1-10 µm)**: Commercial sensors to be identified and tested
  - **RH/T/p**: InterMet iMet-XQ sensors
  - **Wind**: 5-hole probe developed by BST

### Remote Sensing Payload Development
- **Measurement objectives**: Fire radiative power (FRP), fire perimeter, ambient RH/T/p
- **Technical challenge**: FRP measurement requires spectral detectors without saturation in fire radiances
  - Mid-infrared (MIR, ~4 µm) single-element sensors selected for small size and low cost
  - LWIR (7-14 µm) thermal imager for context (becomes saturated but provides spatial coverage)
  - Visible wavelength camera for higher-resolution context
  - Cross-track MIR scanning to improve spatial resolution
- **Design goal**: $15-20K per remote-sensing package
- **Data handling**: Onboard computer stores complete dataset; real-time monitoring subset sent to ground

### System Integration & Testing
- Year 1: Sensor selection and acquisition; establish FAA/DoI/USFS relationships; planning observation strategies
- Year 2: Prototype payload development; integration onto SuperSwift; test flights (nighttime and Beyond Line of Sight); opportunistic prescribed burn sampling
- Year 3: Payload finalization; build two spare packages; participate in FIREX mission (August 2019); two pilots on duty; 2-4 sorties per night planned; 60-120 flight hours target (15 flying nights minimum 30 hours)

## Products & Capabilities Described

### SuperSwift UAS
- **Role**: Primary airborne platform; must be procured independently by University of Colorado during FY2017
- **Capability for NightFOX**: Enables nighttime fire observations safely without pilot risk; electric propulsion avoids fire plume engine damage; rapid payload exchange for multi-mission flexibility
- **Payload bay specifications**: >6" × 6" × 20" volume; 5 lb capacity
- **Operational context**: Hand-launched, lands on any paved road; fits mobile deployment model for unpredictable wildfire locations
- **Readiness level**: Currently RL4 (test flown); expected to reach RL8 (sufficient performance for fire observations) by project end

### In Situ Instrument Package
- **Current readiness**: RL3 (feasible, ~30% of sensors identified)
- **Expected final capability**: RL8 (production of research-grade data)
- **Key performance metrics**:
  - CO2 & CO detection in fire plumes
  - Aerosol size distributions and concentrations
  - Modified Combustion Efficiency (MCE = ΔCO2/(ΔCO2 + ΔCO)) derivation for fire characterization
  - Simultaneous meteorological context
- **Cost efficiency**: Target $10-15K/package vs. $100K+ for manned aircraft equivalent

### Remote Sensing Instrument Package
- **Current readiness**: RL3 (feasible)
- **Expected final capability**: RL8
- **Key performance metrics**:
  - Spatially-resolved fire radiative power (FRP) determination
  - Fire perimeter/extent mapping
  - Ambient meteorology (RH/T/p)
- **Cost**: $15-20K/package
- **Calibration approach**: Laboratory for remote sensing package; field intercomparison with ground measurements and established instruments

### UAS Observation System (UASOS)
- **Current readiness**: RL2 (concept formed)
- **Expected final readiness**: RL8 (data coverage sufficient to characterize medium-sized wildfire)
- **Deliverable**: Proven small UAS capable of nighttime and Beyond Line of Sight (BLOS) operation
- **Observation strategy** (RL3→RL8):
  - **In situ flights**: Vertical and horizontal sampling patterns through fire plumes
  - **Remote sensing flights**: Cross-track scanning patterns over fire perimeter
  - Both support nighttime fire plume characterization and fire weather model validation

## Use Cases & Applications

### Primary Mission: NOAA FIREX (FY2019)
- **Context**: Comprehensive NOAA research effort to understand wildfire impacts on atmosphere, climate, and air quality; July-September 2019 field campaign in western U.S.
- **NightFOX role**: Fill critical nighttime measurement gap; manned aircraft cannot operate safely at night
- **Specific scientific goals**:
  - Quantify nighttime fire emissions (CO2, CO, aerosol) overlooked by day-only manned missions
  - Characterize fire plume vertical and horizontal distributions at night
  - Determine modified combustion efficiency (MCE) and fire regime (flaming vs. smoldering) under nighttime conditions
  - Support WRF-Sfire fire weather model improvement

### Secondary Applications
- **Prescribed burn evaluation** (FY2018): Test deployments during controlled summer burns, potentially with Aerodyne mobile laboratory co-location
- **Oil and gas flare detection/validation**: Remote sensing package calibration and validation of satellite measurements for gas flaring
- **Satellite algorithm validation**: NESDIS collaboration for fire parameter retrieval algorithm refinement

### Operational Deployment Model
- CU mobile command center with UASOS drives to wildfire location (1-2 day mobilization)
- Operations next to Aerodyne mobile lab during FIREX for coordinated measurements
- Real-time coordination with incident management teams (IMTs) and FAA/DoI/USFS airspace control
- Hand-launched from any paved road; no runways required
- Nighttime operations over active fire areas (primary unique capability)

## Key Technical Decisions & Justifications

### Sensor Response Time Emphasis
- Recognized that standard industrial solid-state sensors (10-60 s response time) inadequate for UAS spatial resolution
- At 20 m/s cruise speed, 25-s delay = 0.5 km spatial blur
- Commitment to achieve <1 s response time through commercial modifications or custom instruments
- Addresses fundamental SWaP (size, weight, power) constraint while maintaining research quality

### Cost-Effectiveness Strategy
- Target $10-15K per in situ package vs. $100K+ for manned aircraft equivalents (10× reduction)
- Target $15-20K per remote package vs. equivalent standalone thermal/IR systems
- Achieved through miniaturization and commercial sensor integration with custom modifications
- Enables future operational deployments and network flying concepts

### Redundancy & Risk Mitigation
- Plan to build two complete instrument packages (in situ and remote) to survive UAS loss scenario
- Identified fallback UAS platforms (CU Tempest and Mistral) if SuperSwift purchase delayed or aircraft damaged
- Primary and secondary sensor candidates identified from project start; switching strategy if primary inadequate
- CSD internal funding identified for cost overrun contingency (typical overage risk flagged as moderate-high)

## Notable Details

### Institutional & Personnel Strengths
- **Team expertise**: Dr. Gao (proven instrument developer, three NOAA/NASA mission leads); Thornberry (instrument PI experience, NASA missions); Argrow (UAS expert, FAA regulatory relationships); Schranz (fire weather modeling)
- **Support infrastructure**: NOAA ESRL/CSD engineering staff (mechanical, electrical, software); University of Colorado IRISS Program for UAS operations
- **Coordination**: All key personnel located in Boulder, CO; monthly meetings + ad-hoc coordination

### FIREX Steering Committee Endorsement
- Strong written support from FIREX project members (Schwarz, Roberts, Warneke)
- Identified NightFOX as addressing "high-value goal" of FIREX; fills "critical need"
- Highlighted unique value: (1) geographic extent of nighttime emissions, (2) vertical dimension unavailable to mobile labs, (3) fire regime determination via MCE from CO2/CO, (4) near-source emission rates with high spatial resolution

### Regulatory & Airspace Strategy
- **FAA coordination**: Brian Argrow experienced in COA (Certificate of Waiver or Authorization) applications; early engagement planned
- **Multi-agency coordination**: DoI (Department of Interior), USFS (Forest Service), NOAA AOC (Aircraft Operations Center), incident management teams
- **BLOS operations**: UAS must secure Beyond Line of Sight waiver; CU currently has COAs for Pawnee Grasslands and Table Mountain (nighttime BLOS expansion in Year 2)
- **NEPA clearance**: Categorical Exclusion (CE) determination completed; no significant environmental impact identified

### Readiness Level Trajectory
| Component | Current | Target |
|-----------|---------|--------|
| UAS Platform | RL4 | RL8 |
| UAS Payload | RL3 | RL8 |
| UAS Observing System | RL2 | RL8 |
| UAS Observing Strategy | RL3 | RL8 |

Success criteria emphasize demonstration (favorable intercomparison with established instruments), operational performance (>2 hr flights, data recovery), and scientific utility (fire weather model improvement).

### Budget & Resource Plan
- **Total requested**: $488.9K (3 years)
- **In-kind contributions**: $559.8K (>100% match)
-