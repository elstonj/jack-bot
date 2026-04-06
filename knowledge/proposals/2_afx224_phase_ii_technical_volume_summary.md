# AFX22.4 Phase II Technical Volume Summary: Runway Integrity Validation through Soil Moisture Measurements from a Small UAS

## Document Metadata
- Type: SBIR Phase II Proposal Technical Volume Summary
- Client/Agency: U.S. Air Force / AFWERX
- Program/Solicitation: AFX224-OCSO1 Phase II; Open Call for Innovative Defense-Related Dual-Purpose Technologies/Solutions
- Proposal Number: F2-16588
- Date: 2023 (created/modified October 23, 2023)
- BST Products/Systems Referenced: Small UAS (Group 1 and Group 2), L-band radiometer (Lobe Differencing Correlation Radiometer/LDCR), flight management system
- Key Personnel: Jack Elston (last editor)
- Partner Organizations: Orbital Micro Systems (OMS), Center for Environmental Technology (CET) at University of Colorado

## Executive Summary
Black Swift Technologies proposes to adapt its existing commercial L-band radiometer soil moisture mapping system for the U.S. Air Force to rapidly assess soil integrity at unimproved landing zones for C-130 operations. The system measures volumetric soil moisture and will be modified with new algorithms to output cone index measurements, providing forward air controllers with critical data for landing decisions. This dual-use technology addresses a critical DoD need to replace slow, risky manual soil penetrometer evaluations with fast, non-contact remote sensing from small UAS.

## Technical Approach

### Core Technology
- **L-band Radiometer (LDCR)**: Proprietary Lobe Differencing Correlation Radiometer operating in 1400-1427 MHz Earth Exploration Satellite Service protected band
  - Uses dual reference signals and two antennas (one up-looking, one down-looking) for calibration stability
  - Measures brightness temperature with 1.2 K accuracy
  - Penetrates ~10 cm into soil surface
  - Pixel resolution approximately equal to aircraft flight altitude; can be enhanced through post-processing
  - Low power consumption, highly stable, refined calibration

### System Configuration
- Operates on Group 1 and Group 2 small UAS (fixed-wing and multirotor platforms)
- Both UAS and sensor manufactured in USA
- FAA, NASA, and NOAA approved for non-defense commercial operations
- State-of-the-art flight management system minimizes operator workload

### Soil Integrity Measurement Algorithm
- Combines measured brightness temperature with runway surface temperature and soil type data
- Converts soil moisture measurements to cone index output
- Current TRL for radiometer/UAS: 8; soil integrity algorithms: TRL 4 (expected TRL 7 by Phase II completion)

### Development History
- 15+ years of sensor design and evolution
- 8 years of flight testing
- Original development: NASA SBIR partnership with CET at University of Colorado

## Products & Capabilities Described

### L-Band Radiometer System
- **What it is**: Miniaturized, integrated radiometer for small UAS measuring volumetric soil moisture via brightness temperature
- **Proposed use**: Modified to measure and output soil integrity (cone index) for runway assessment
- **Specifications**:
  - Operating frequency: 1400-1427 MHz
  - Brightness temperature accuracy: 1.2 K (corresponds to ~1% volumetric soil moisture)
  - Soil penetration depth: ~10 cm
  - Pixel resolution: variable with flight altitude
  - Power consumption: low
  - Measurement update rate: continuous

### Small UAS Platform
- **What it is**: Purpose-built unmanned aircraft systems designed for extreme-condition operations
- **Proposed use**: Deliver L-band radiometer over unimproved landing zones for rapid soil mapping
- **Capabilities**: 11 years of development; proven in wildfire, volcano, tornado, and hurricane missions; customizable for specific mission demands
- **Platforms**: Both fixed-wing and multirotor variants available

## Use Cases & Applications

### Primary Use Case: Military
- **C-130 Runway Integrity Assessment**: Rapidly evaluate unimproved landing zones worldwide for C-130 cargo operations
  - Impact scope: 160+ air operation facilities, 9,000+ worldwide AO personnel, 7.3 million annual aircraft operations
  - Eliminates need for ground personnel to physically access potentially contested areas
  - Enables "air-deployed" operation from C-130 in future capability
  - Transition path: Air Force Civil Engineer Center's Airfield Pavement Evaluation team at Tyndall AFB, FL (evaluates 200+ airfields globally)

### Secondary Defense Applications
- Domestic flying training events
- Overseas contingency missions
- Trafficability assessments
- Monitoring stability/saturation of earthen dams

### Commercial/Non-Defense Applications
- **Construction & Mining**: Soil strength assessment for site preparation
- **Agriculture**: Soil moisture mapping for farm management
- **Land Management**: Wildfire-prone area assessment (existing USGS partnership)
- **Railway Industry**: Roadbed integrity assessment
- **Golf Courses**: Smart irrigation optimization (existing partnership with Toro)
- **Hydrological Monitoring**: Mountain valley snowmelt modeling

## Key Results (Development & Validation History)

### Existing Commercial Deployments
- **NASA Partnership**: Original development and validation with NASA's Soil Moisture Active Passive (SMAP) satellite calibration
- **USGS (California)**: Soil moisture mapping over wildfire-prone areas
- **NOAA (SPLASH Project)**: Study of Precipitation, Lower Atmosphere and Surface for Hydrometeorology
- **Toro Corporation**: Golf course soil moisture mapping for smart irrigation
- **Universities**: Systems sold to University of Virginia and Cooperative Institute for Research in Environmental Sciences (CIRES) at University of Colorado Boulder
- **Data Services**: Ongoing revenue from USGS wildfire mitigation research, Western State University satellite calibration/validation, NOAA hydrological modeling

### Revenue Traction
- Previous L-band radiometer sales and services: **$0.7M combined revenue**
- Soil integrity capability: Not yet commercialized but shows strong market interest

### Technical Validation
- 15+ years of sensor evolution
- 8 years of active flight testing
- Demonstrated soil moisture accuracy over numerous field sites
- Stable, low-power, reliable hardware with refined calibration and software

## Notable Details

### Competitive Advantage vs. Current Methods
- **Current Method**: Manual dynamic cone penetrometer measurements by ground personnel
  - Labor-intensive, time-consuming
  - Provides only point measurements, not full runway characterization
  - Risky in contested/unstable areas
  - Slow process
- **BST Proposed Solution**: Non-contact, "on-the-move" remote sensing
  - Rapidly maps entire landing zone
  - Can be air-deployed, eliminating ground personnel risk
  - Faster assessment enabling quicker decision-making
  - Augments or potentially replaces existing techniques

### Technical Risks & Mitigation
1. **Radio Frequency Interference Risk**: Radiometers operating in predefined bands more vulnerable to inadvertent or jamming interference
   - **Mitigation**: Ongoing technology development with CET for proprietary digital radiometer detection technique providing enhanced interference detection/mitigation

2. **Soil Penetration Depth Risk**: L-band penetration (~10 cm) might be insufficient to correlate with C-130 cone test measurements at all landing weights
   - **Mitigation**: Digital detection technique allows operation at lower frequency bands with improved soil penetration depth

### Dual-Use Technology Value
- Commercial and defense applications clearly identified
- Already demonstrated market viability with existing customers and partners
- Team plans to incorporate soil integrity capability into current commercial offerings post-Phase II
- Addresses Air Force Science & Technology Strategy 2030 goals for persistent awareness and decision-making
- Addresses Space Force's Category A soil moisture observation gaps (outlined in 2014 JROC-M study)

### Manufacturing & Regulatory Status
- All components manufactured in USA
- Approved for non-defense operations by FAA, NASA, and NOAA
- 11 years of proven UAS platform development
- Proprietary LDCR architecture with established intellectual property