# Phase II+ Effort Proposal (NASA SBIR Battery Diagnostics)

## Document Metadata
- Type: Phase II+ proposal with integrated partner presentation
- Client/Agency: NASA
- Program/Solicitation: 2017 SBIR (Topic: Internal Intelligence)
- Date: October 23, 2018
- BST Products/Systems Referenced: ECAM (Environmental Condition Assessment Module) interface with failure classification logic
- Key Personnel: Maciej Stachura (last editor); Dynexus team: David Sorum (CEO), David Lung (Chief Product Officer), Jon Christophersen (Chief Scientist), John Voeller (Chief Knowledge Officer)
- Partner: Dynexus Technology Inc. (battery diagnostics provider)

## Executive Summary
BST proposed a Phase II+ effort integrating Dynexus Technology's battery health monitoring technology (iRIS™ - Inline Rapid Impedance Spectroscopy) into UAS platforms to reduce accident rates and enable wider NAS integration. The work combines battery state tracking, propulsion degradation detection, and motor health diagnostics through bench and flight testing, with application to the emerging eVTOL market.

## Technical Approach

### Battery Health Monitoring
- **Prediction capability**: Remaining battery within ±100 mAh; total capacity within ±200 mAh
- **Integration**: ECAM interface with three-tier failure classification:
  - **Level 1 (Advisory)**: Total capacity below 75%
  - **Level 2 (Master Caution)**: Total capacity below 60%; remaining capacity after landing below 20%
  - **Level 3 (Master Warning)**: Remaining capacity after landing below 10%

### Propulsion Degradation Monitoring
- **Approach**: Regression algorithm analyzing propulsion system efficiency
- **Classification capability**: Detects degraded state and classifies root cause:
  1. Damaged motor
  2. Damaged propeller
  3. Icing conditions
  4. Other catch-all category
- **ECAM failure thresholds**:
  - Level 2: 80% of nominal efficiency (damaged motor/propeller/other); icing conditions pre-flight
  - Level 3: 60% of nominal efficiency (damaged motor/propeller/other); 80% of nominal with icing
- **Data collection**: Motor RPM, voltage, current, throttle setting, static pressure, OAT, humidity, altitude, IAS, climb/sink rate, aircraft mass

### Flight Test Plan
- **Bench testing**: 3 hours with nominal, bent shaft, and damaged propeller configurations
- **Flight testing**: 1 hour with nominal, bent shaft, and damaged propeller configurations
- **Stretch goal**: 1 flight through known icing conditions

## Products & Capabilities Described

### ECAM (Environmental Condition Assessment Module)
- Real-time failure monitoring interface
- Multi-level alert system (Level 1-3)
- Integrates battery and propulsion diagnostics
- Displays actionable warnings to operator

### iRIS™ (Inline Rapid Impedance Spectroscopy) - Dynexus Technology
**What it is**: Non-destructive battery diagnostic tool using AC impedance measurement under load conditions

**Key specifications**:
- Frequency range: 0.1-2000 Hz
- Active 10-second wideband AC input pulse
- Measures at point of need under load (vs. traditional EIS requiring no-load, equilibrium conditions)
- 10 years of optimization and validation for lithium-ion batteries

**Technical capabilities**:
- **State of Charge (SOC)**: Battery "fuel gauge"
- **State of Health (SOH)**: Current battery condition and degradation
- **Remaining Useful Life (RUL)**: Predictive end-of-life estimation
- **State of Stability (SOS)**: Detection of instability and safety hazards

**Performance metrics**:
- Ohmic resistance measurement (where curve crosses real axis)
- Charge transfer resistance (semicircle width analysis)
- Warburg impedance (low frequency tail)
- Impedance increases correlate with age/use
- Validated correlation with INL power fade studies (R² = 0.984-0.993)

**Safety validation** (Sandia National Labs):
- Thermal ramp testing shows iRIS can detect onset of failure conditions
- Benign measurement: 10,000 under-load measurements showed negligible additional degradation
- Sensitive enough to detect faulty cells in multi-cell strings

## Use Cases & Applications

### Primary: UAS Safety Integration
- **Problem addressed**: Current UAS failure rate of 3,800 per 100,000 flight hours (BST goal: reduce to GA aircraft level of 11.8 per 100,000)
- **Battery-related failures**: 13.7% of current UAS failures
- **Solution**: Advanced battery monitoring for wider NAS integration

### Secondary: eVTOL Market
- **Market context**: Companies including Uber, Airbus, Bell, Boeing, Embraer developing electric vertical-takeoff-and-landing vehicles
- **Requirements addressed**: Autonomy, affordability, low noise reliability
- **UAS as proving ground**: Battery technology validation before eVTOL deployment

### Tertiary Applications (Dynexus)
- Cell qualification for manufacturing
- Just-in-time replacement vs. scheduled replacement (cost optimization)
- Battery second-use certification (e.g., stationary energy storage)
- Non-battery applications: metal quality, weld strength, metal coatings assessment

## Key Results

### Dynexus Technology Validation Studies

**Idaho National Laboratory (INL) - Aging Studies**:
- USABC pulse testing (16 hrs) vs. EIS (10 min) comparison
- Strong linear correlation between EIS impedance growth and power fade across temperature variants
- 25°C: R² = 0.984; 45°C variants: R² = 0.989-0.993
- Long-term validation: iRIS measurements under load (10,000 cycles) showed similar degradation profiles to no-load measurements, demonstrating benign measurement characteristics

**INL - String Aging**:
- iRIS sensitive enough to detect individual faulty cells within multi-cell strings
- Tested 2-cell, 3-cell, and 4-cell configurations with calendar-life aging

**Sandia National Labs (SNL) - Safety Studies**:
- iRIS applied to thermal ramp abuse testing (3S1P cell configuration)
- Demonstrated detection capability for onset of catastrophic battery events
- Quote: "The successful development of the rapid impedance spectrum sensor can help improve the overall safety and reliability of lithium-ion batteries...significantly leapfrogging existing approaches."

## Notable Details

### Strategic Context
- Dynexus CEO David Sorum is licensed private pilot (SEL), aligning with aviation focus
- Dynexus Chief Scientist Jon Christophersen is primary iRIS inventor with 15 years battery experience at INL and Group Lead of INL Battery Test Center
- John Voeller (Chief Knowledge Officer) brings government/enterprise technology policy experience (former CTO Black & Veatch, ASME Fellow)

### Competitive Advantages
- iRIS operates under load (operational conditions) vs. traditional EIS requiring no-load equilibrium
- Field-deployable vs. expensive/bulky lab equipment
- 10 years of validation specifically for lithium-ion batteries
- Breakthrough in battery safety diagnostics identified as gap in field

### Market Size Reference
- Batteries are trillion-dollar industry; diagnostics historically underfunded vs. design and longevity investments

### Technical Limitations Addressed
- Traditional AC impedance unsuitable for field conditions (requires expensive equipment, no-load operation, equilibrium states)
- iRIS solves this through active wideband measurement in operational context