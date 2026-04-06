# CU Final Report: A Ruggedized UAS for Scientific Data Gathering in Harsh Environments

## Document Metadata
- Type: Phase I SBIR Final Report
- Client/Agency: NASA
- Program/Solicitation: 2016 SBIR (Volcano topic)
- Date: November 30 – December 9, 2016
- BST Products/Systems Referenced: BST Multi-Hole Probe (MHP), SuperSwift (airframe)
- Key Personnel: Roger Laurence (Research and Engineering Center for Unmanned Vehicles, University of Colorado Boulder); Maciej Stachura (last editor)

## Executive Summary
This Phase I final report documents wind tunnel calibration and validation of Black Swift Technologies' multi-hole probe (MHP) for measuring angle of attack (α), sideslip (β), and true airspeed (V) on small UAS operating in harsh environments. The work compared BST MHP performance against a commercial Aeroprobe reference instrument and conducted CFD analysis to assess airframe interference effects. Results demonstrate α and β estimation within ±1° and airspeed estimation within ~0.6 m/s, meeting or approaching project goals.

## Technical Approach

### Wind Tunnel Testing
- **Facility**: Low-speed wind tunnel (0.84 m diameter test section) at National Center for Atmospheric Research Foothills Lab, Boulder, Colorado
- **Reference Instrument**: 5-hole multi-hole probe from Aeroprobe Corporation mounted alongside BST MHP for direct comparison
- **Mounting System**: 80/20 aluminum structure with custom adapter designed to minimize support arm interference on BST MHP
- **Calibration Phase**: 75 calibration runs at known α, β, and airspeed (V) to develop pressure-to-flight-parameter relationships
- **Validation Phase**: Separate orientations within calibration bounds to assess accuracy

### Measurement Methodology
- **Angle Measurement**: AccuMASTER 7434 digital inclinometer (±0.2° accuracy, ±0.05° resolution) for true α and β
- **Test Ranges**: 
  - α range: -8.55° to 8.10°
  - β range: -8.65° to 7.35°
- **Angular Offsets Corrected**:
  - BST MHP: α offset -0.35°, β offset -0.65° relative to support arm
  - Wind tunnel floor slope correction: -0.15° subtracted from all α values
  - Aeroprobe: α offset +0.30°, β offset -0.55° relative to support arm
  - Instrument separation: BST MHP ~0.85° greater α, Aeroprobe ~0.10° greater β

### Neural Network Calibration
- **Algorithm**: Scaled Conjugate Gradient (SCG) training via MATLAB Neural Network Toolbox
- **Network Architecture**: 
  - Inputs: 6 pressure readings (static pressure + 5 differential pressures from probe ports)
  - Hidden Layer: 10 neurons with hyperbolic tangent sigmoid transfer function (tansig)
  - Output Layer: Linear transfer function (purelin) producing α, β, V estimates
- **Training Data Split**: 70% training, 15% validation, 15% test
- **Rationale**: Neural networks proven effective for relative wind sensing on small UAS (references: Laurence 2016, Quindlen 2013)

### CFD Analysis
- **Software/Modeling**: k-ε turbulence model with ideal gas assumption
- **Flight Conditions**: 20 m/s airspeed, 830 hPa pressure, 300 K temperature
- **Scope**: SuperSwift nosecone geometry at α varying -5° to +9° in 2° increments, β held at 0°
- **Output**: Gauge pressure distribution across airframe surface to identify MHP interference

## Products & Capabilities Described

### BST Multi-Hole Probe (MHP)
**What it is**: Compact 5-port air data probe measuring dynamic and static pressures for flight parameter estimation on small UAS

**Proposed use in this context**: Primary sensor for measuring angle of attack, sideslip, and true airspeed on SuperSwift during scientific missions in harsh environments (e.g., volcano monitoring)

**Performance specifications achieved**:
- **Angle of Attack (α) Accuracy**: ±1° across tested range (-8.55° to +8.10°)
  - At 13 m/s tunnel speed: error independent of true orientation
  - At 18 m/s tunnel speed: error increases with positive α but remains within ±1°
- **Sideslip (β) Accuracy**: ±1° across tested range (-8.65° to +7.35°)
  - Significantly less dependent on true orientation than α
- **True Airspeed (V) Accuracy**: ~0.6 m/s mean error (goal was 0.5 m/s)
  - Nearly constant error at fixed tunnel speed regardless of orientation
  - Maximum error: 0.6 m/s at 18 m/s tunnel speed

### SuperSwift (BST Airframe)
**What it is**: Small UAS platform for scientific operations

**Use in context**: Intended platform for deploying the MHP; CFD analysis focused on nosecone aerodynamics to understand mounting interference

**Airframe Effect Finding**: Preliminary CFD results indicate the nosecone creates ~4 m/s airspeed differential between top and bottom surfaces at 0° α, affecting static pressure measurement

## Use Cases & Applications

- **Volcano Monitoring**: Primary application of Phase I work (SBIR topic area)
- **Scientific Data Gathering in Harsh Environments**: General capability for extreme-environment operations
- **Atmospheric Measurement**: Wind and flight parameter sensing for meteorological research

## Key Results

### Wind Tunnel Comparison Results (BST MHP vs. Aeroprobe)

**Airspeed Discrepancies**:
- Aeroprobe consistently reports higher true airspeed than wind tunnel pitot-static reference
- Aeroprobe errors approximately 50% greater than manufacturer specifications
- Root cause: dynamic pressure measurement bias/sensor miscalibration (Aeroprobe reports lower dynamic pressure than wind tunnel)
- Aeroprobe α errors: within ±1° (per manual specification)
- Aeroprobe β errors: exceed ±1° specification at lower true α values; clear correlation between β error and true α (β error independent of true β)

**BST MHP Performance vs. Neural Network Regression**:
- Training regression achieved excellent fit (slope ~1, intercept ~0)
- α estimation: mean errors within ±1° goal across all speeds and orientations
- β estimation: mean errors within ±1° goal, less orientation-dependent than α
- V estimation: mean errors ~0.6 m/s, approaching 0.5 m/s goal

### CFD Findings
- Airframe interference on MHP confirmed: velocity magnitude variations of ~4 m/s between top/bottom surfaces at 0° α
- Nosecone alone analyzed; full airframe simulation recommended
- Mounting influences potentially calibratable (reference: Houston et al. 2016 intercomparison study)

### Data Quality Notes
- 75 calibration orientations produced 75 pressure measurement sets
- Validation orientations intentionally selected far from calibration points to test extrapolation behavior
- All measurements corrected for instrumental offsets and environmental factors (floor slope, inclinometer accuracy limits)

## Notable Details

### Calibration Approach Innovations
- Custom aerodynamic adapter designed to minimize 80/20 support arm interference on BST MHP
- Systematic correction methodology for mounting-induced angular offsets
- Dual-instrument simultaneous testing against Aeroprobe reference (though angular separation noted as limitation)

### Identified Limitations & Future Work
1. **Wind Tunnel Mount Refinement**: Current setup has undesirable angular offset between BST MHP and Aeroprobe; Phase II should mount both instruments on single carrier with aerodynamically shaped supports (airfoil vertical support, thin rods)
2. **CFD Scope Expansion**: Phase I limited to nosecone; Phase II should model:
   - Complete SuperSwift airframe
   - Multiple α and β combinations
   - Varying airspeed, environmental pressure, density regimes
   - Comparative analysis: MHP on SuperSwift vs. in wind tunnel vs. isolated
3. **Regression Algorithm Comparison**: SCG chosen for speed but noted as potentially less accurate than Levenberg-Marquardt or Bayesian Regularization; Phase II should evaluate alternatives
4. **Neural Network Optimization**: 10 hidden neurons selected empirically; Phase II should determine optimal count
5. **Aeroprobe Discrepancies**: Errors 50% higher than manual specs warrant investigation of sensor calibration status or wind tunnel test procedure errors

### Partnership Context
- University of Colorado Boulder's Research and Engineering Center for Unmanned Vehicles conducted testing
- NCAR Foothills Lab wind tunnel facility used
- Work informed by prior UAS air data sensing research (Laurence, Argrow, Frew 2016; Quindlen, Langelaan 2013; Houston et al. 2016 intercomparison)

### Technical Maturity
Phase I established proof-of-concept for BST MHP viability. Calibration/validation complete for wind tunnel environment. Transition to flight testing and airframe-integrated performance validation planned for Phase II (2 additional years).