# A Ruggedized Unmanned Aircraft and Sensor Package for Measurement of Hazardous Airborne Emissions from Wildfires

## Document Metadata
- Type: SBIR Phase I Proposal Narrative
- Client/Agency: USDA NIFA (National Institute of Food and Agriculture)
- Program/Solicitation: USDA NIFA SBIR Program
- Date: September 27, 2017 (created); submitted before March 2017 deadline (proposal indicates 2017 submission)
- BST Products/Systems Referenced: S2 UAS, SwiftCore Flight Management System, SwiftTab user interface
- Key Personnel: Dr. Lois Wardell (atmospheric plume research, sensor/UAS development background)

## Executive Summary
Black Swift Technologies proposes to develop a miniaturized sensor payload integrated onto the proven S2 fixed-wing UAS to measure hazardous airborne emissions from wildfires. Operating at standoff distances downwind of fires (avoiding airspace conflicts with active firefighting), the system will characterize fine particulates, trace gases (CO, CO2, mercury, VOCs), and collect in situ samples for validation. Phase I will evaluate sensor integration, validate performance in aircraft operations, and develop operational concepts for safe deployment.

## Technical Approach

**Primary Strategy:**
- Integrate existing, field-proven handheld and commercial off-the-shelf (COTS) sensors onto the S2 platform rather than developing entirely new miniaturized sensors
- Design a modular payload tray allowing future sensor swaps as technology advances
- Operate downwind of active fires to measure plume composition at various plume ages, supporting atmospheric transport modeling
- Develop in situ sampling capability to validate sensor accuracy during flight
- Create concept of operations (CONOPS) ensuring safe operations without interference to firefighting efforts

**Key Technical Challenges Addressed:**
1. Integration of handheld sensors not originally designed for aircraft use
2. Managing multiple airflow and data interface requirements
3. Validating sensor accuracy in moving aircraft environment
4. Developing regulatory and operational clearances for wildfire environment deployment

## Products & Capabilities Described

### S2 UAS Platform
- Fixed-wing, long-endurance aircraft
- 2-hour flight endurance
- 20,000 feet maximum altitude capability
- Proven heritage in remote and in-Earth sensing campaigns
- Selected for NOAA FIREX campaign (night-time wildfire observations)
- Car launcher capable
- Designed for operation in difficult environments (severe storms, Arctic)
- Fully integrated avionics designed in-house by BST

### SwiftCore Flight Management System
- Full suite avionics package including autopilot, ground station, user interface
- Commercialized product
- Enables data tagging with aircraft telemetry
- Allows integration of multiple sensor data streams

### SwiftTab User Interface
- Ground station interface allowing mission operators to control sampling events
- Ability to remotely trigger in situ samplers during flight
- Designed for integration with payload systems

### Proposed Sensor Payload Suite

| Sensor Type | Range | Product Name | Purpose |
|---|---|---|---|
| Mercury Vapor | 0-10,000 μg/m³ | EMP 2 | Heavy metal emissions |
| PID (Photoionization Detector) | ppb-ppm | Alphasense AH2 | VOC detection (200+ species) |
| Particulate Counter | PM1, PM2.5, PM10 | Alphasense OPC-N2 | Fine particulate measurement |
| CO2 | 0-5000 ppm | Senseair K30FR | Combustion efficiency, greenhouse gas |
| SO2 and H2S | 20 and 100 ppm | Alphasense SOH A2 | Trace gases |
| CO | 0-500 ppm | Alphasense CO-A4 | Combustion indicator |
| Humidity | 0-100% | iMet-XF | Environmental condition |
| Temperature | -40 to +85°C | iMet-XF | Environmental condition |
| Pressure | 10-1200 mBar | iMet-XF | Environmental condition |
| 3D Winds | 0-60 m/s | Black Swift Technologies | Atmospheric dynamics |

**Novelty:** Integration of mercury vapor sensor, PID, and particulate counter onto UAS is described as "unique to this effort and represents a significant improvement over current state-of-the-art."

### In Situ Sampling System
- Baseline design: 2 samples per flight (minimum viable)
- Stretch goal: 8 samples per flight using Valco valve system with serial interface
- Pump and tank system based on existing BST CO2 analyzer design
- Multi-stage cassette filter for particulate analysis
- Ground control via SwiftTab interface for remote sample trigger
- Samples for post-flight lab validation of airborne sensor data

## Use Cases & Applications

### Primary: Wildfire Emission Monitoring
- **Near Real-Time Reporting:** Enable fire managers, health services, and researchers to characterize fire emissions and impacts
- **Downwind Operations:** Measure emissions at standoff distance, avoiding airspace conflicts with active firefighting
- **Plume Characterization:** Identify biomarkers in PM2.5 to determine vegetation species burned, combustion efficiency, burn characteristics
- **Multi-Scale Assessment:** 2-hour endurance enables regional missions; capable of measuring plumes hundreds of miles downwind
- **Pre-Fire Planning:** Assess fuel load conditions, vegetation species composition, and dryness for control burn planning

### Secondary Applications (Post-Phase II):
- **Industrial Emissions Monitoring:** Smokestack plume characterization for EPA compliance verification
- **Chemical Fire Assessment:** Characterize composition and danger of chemical fires at refineries
- **Volcanic Emissions:** Payload design builds on existing volcanic sampling experience
- **Multispectral Remote Sensing:** EO/IR video and imagery support for wildfire operations
- **Satellite Truthing:** Validate satellite-derived fire parameters with airborne measurements

## Key Results (Reports / Findings)

This is a Phase I proposal narrative, not a report with results. However, the document references significant published research demonstrating the problem and approach feasibility:

**Problem Scope:**
- Wildfires release 3x more fine particulate matter than accounted for in U.S. National Emissions Inventory
- 200+ gaseous compounds identified from biomass burning
- Global estimate: 339,000 premature deaths from wildfire emissions annually
- U.S. mercury emissions from wildfires: 44,000 kg/year
- Global lead emissions: 1,900,000 kg/year average
- 2011 Wallow Fire smoke plume extended 1,000 miles

**Technical Feasibility Evidence:**
- Handheld dust monitors successfully flown in aircraft (Weber et al., 2012)
- Alphasense OPC-N2 optical counter validated with good PM1.0, PM2.5, PM10 correlation (Crilley et al., 2017)
- Combustion efficiency calculated from airborne CO/CO2 measurements in Siberian fires (Paris et al., 2009)
- Organic biomarkers identified in downwind smoke (Ward et al., 2006)
- Smoldering vs. flaming combustion detectable through enhanced particulate/organic carbon (Alves et al., 2011)

## Notable Details

### BST Company Profile (as of 2017)
- Founded: 2011
- Staff: 4 engineers + 2 sales/marketing
- Commercialized products: SwiftCore FMS and S1 survey UAS
- Track record: Multiple SBIR successes leading to commercialization

### Flight Operations & Regulatory Experience
- Secured/maintained 140+ FAA Certificates of Authorization
- Operations in Colorado, Kansas, Nebraska
- Special permissions: high-altitude ops, 20-mile beyond line-of-sight, multi-aircraft coordination
- Successfully completed 5 NASA flight safety and readiness reviews
- Unique missions: supercell/tornado penetration, Arctic operations, multi-aircraft formation over Indian Ocean, high-altitude mountainous mapping

### Technical Heritage & Partnerships
- **NOAA FIREX Participation:** Selected for NightFOX component measuring fire plume emissions and remote fire observation over prescribed burns in coordination with University of Colorado
- **Thermodynamic Sensors:** Pressure, temperature, humidity, wind velocity sensors developed by BST under NASA SBIR with commercial success
- **Payload Integration Experience:** Previously integrated L-band radiometer (soil moisture), 12-camera multispectral array, LI-COR CO2/H2O analyzer, volcanic plume sampling package
- **Scientific Advisor:** Dr. Lois Wardell—background in volcanic emissions airborne/remote sensing, managed Scripps MAC campaign measuring black carbon radiative forcing with 10 instruments per aircraft over Indian Ocean

### Operational & Regulatory Strategy
- Partnering with David Grimm (Tall Timbers Research Station, Florida)—retired wildland firefighter with incident commander experience
- Emphasis on working with both researchers and fire incident managers to secure operational clearances
- Current collaboration with NOAA/University of Colorado on FIREX NightFOX (separate from this proposal but demonstrating close-in fire plume access)
- Phase I focus on CONOPS development for Phase II deployment in operational environment

### Competitive Landscape
- **Comparison to Scentroid DR300:** Quadrotor-based smokestack sampling system
  - DR300: 1 in situ sample, 2 trace gas sensors, DJI Phantom frame, ~15 min flight time, 500m ceiling
  - Proposed S2 system advantages: thermodynamic measurements, 2-hour endurance, larger area coverage, 4+ gas species, particulate counter, PID, multiple in situ samples (up to 8)

### USDA NIFA Strategic Goal Alignment
Proposal explicitly addresses multiple NIFA Sub-Goals:
- **1.1 (Food Security):** Wildfire impacts on agricultural lands, soil erosion, watershed degradation
- **1.2 (Climate Adaptation):** CO2 and brown carbon characterization for climate modeling
- **1.3 (Natural Resources):** Improved wildfire management and emissions characterization
- **1.4 (Bioenergy):** Sustainable forest biomass production through better fire management
- **1.6 (Food Safety):** Mercury, lead, and heavy metal contamination tracking in food systems
- **1.7 (Firefighter/Public Safety):** Characterization of hazardous emissions for first responder and public health protection

### Phase I Work Plan (8 months, performed at BST Boulder, CO facility)
1. **Sensor Suite Selection:** Evaluate candidate sensors, determine simultaneous integration limits, confirm OEM specifications for aircraft use
2. **Payload System Design:** Power, data interfaces, mechanical mounting, airflow management for 9+ sensors; avionics modification for telemetry tagging; SwiftTab interface integration
3. **In Situ Sampler Design:** Pump/tank system, filter cassette integration, ground control interface; feasibility study for 8-sample configuration
4. **Validation Plan:** Ground calibration with standard gases and reference dust counters; airborne testing protocol for Phase II
5. **CONOPS Development:** Flight plans, site selection, FAA/incident command coordination for Phase II operational deployment