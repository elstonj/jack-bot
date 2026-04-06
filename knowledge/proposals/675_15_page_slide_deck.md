# S0 UAS Phase II SBIR Proposal – Air Force Atmospheric Sounding

## Document Metadata
- Type: Proposal support slide deck (15 slides)
- Client/Agency: U.S. Air Force
- Program/Solicitation: SBIR Phase II (Atmospheric Sounding)
- Date: Submitted 2019 (created 2019-10-29, modified 2019-12-30)
- BST Products/Systems Referenced: S0 UAS, S0-AD, Multi-hole Probe (MHP), S2 UAS
- Key Personnel: Jack Elston (PI, Ph.D. Aerospace Engineering, expertise in UAS for tornadic thunderstorm research and wind measurement)

## Executive Summary
Black Swift Technologies proposed to adapt its commercially-developed S0 UAS (hand-launched atmospheric sounding platform) for U.S. Air Force use, enabling automated vertical atmospheric profiling up to 15,000 feet to support weather forecasting and operational modeling. The Phase II effort would modify the existing commercial system for Air Force data interfaces and operational requirements, culminating in delivery of a production-ready S0 system with training to Air Force Weather operators at Hanscom AFB. An MOU with the Air Force Life Cycle Management Center supported the effort.

## Technical Approach

### Core System Modification
- **Foundation**: Commercial S0-AD platform (originally developed with NOAA for hurricane sampling, priced at $5,000 per unit)
- **Key Adaptations**:
  - New wing/tail design for hand-launch capability, extended endurance, and optimized fast climb to 15,000 ft
  - Unique tail design enabling deep-stall landing with near-vertical descent and ±10 ft landing accuracy
  - Integration of onboard Multi-hole Probe (MHP) sensor to control trajectory and improve measurement accuracy during profiling
  - Data formatting and transmission compatible with existing Air Force systems
  - Mission prep UI with scripting capabilities for custom sampling plans (goal: <5 min mission prep)

### Operational Profile
- Hand-launched by Air Force Weather operators (supporting SOF and Army operations)
- Fully autonomous operation ("launch-and-forget") with minimal training required
- Fast climb optimized for rapid data collection
- Real-time telemetry of science data during ascent; data file generation within 5 minutes of landing for upload to AF systems

## Products & Capabilities Described

### S0 UAS (Atmospheric Sounding Platform)
- **What it is**: Hand-launched, fully autonomous UAS purpose-built for atmospheric sensing; entirely U.S.-made
- **Proposed AF use**: Automated vertical atmospheric profile collection to 15,000 ft for integration into Air Force weather models and forecasting
- **Key specifications**:
  - Altitude capability: 15,000 ft in under 20 minutes (endurance goal)
  - Precision autoland: ±10 ft accuracy (target 10 consecutive autolands)
  - Wind tolerance: Capable in winds exceeding 30 mph
  - Launch method: Hand-launch
  - Recovery: Automated with ~10 ft accuracy
  - Flight hours: 2,500+ logged; 150+ FAA-approved flight operations; 8 NASA Flight Safety Reviews

### Multi-hole Probe (MHP) Sensor
- **What it is**: 3D wind and thermodynamic measurement sensor
- **Pricing**:
  - Version 1 (5-hole probe, pressure, temperature, humidity): $1,000; 9 sold to customers
  - Version 2 (Version 1 specs + IMU, magnetometer, GPS RTK): $2,000; on sale Q4 2019
- **AF application**: Onboard sensor controlling S0 trajectory to improve wind measurement accuracy during ascent
- **Performance specifications**:
  - Lateral wind accuracy: ±2° in heading, ±0.3 m/s in speed
  - Vertical wind accuracy: ±0.4 m/s
  - Temperature accuracy: ±0.3°C RMS
  - Pressure accuracy: ±1.5 hPa RMS
  - Humidity accuracy: ±1.3% RMS

### S0-AD (Commercial Precursor)
- **What it is**: Air-deployed UAS for atmospheric sampling (originally developed with NOAA)
- **Commercial status**: Under NOAA contract for 5 units with potential follow-on orders
- **Cost**: $5,000 per unit
- **Role in SBIR**: Foundation design adapted for AF hand-launch requirements

### S2 UAS
- **What it is**: Commercial UAS developed and improved under 2 NASA SBIRs
- **Context**: Referenced as example of BST's prior commercial UAS platform

## Use Cases & Applications

### Air Force Operational
- **Personnel**: Air Force Weather forecasters supporting ACC (Air Combat Command), Army, and Special Operations Forces (SOF)
- **Missions**: 
  - Support 557th Weather Wing forecasting and modeling efforts
  - Provide 3D wind profiles for accurate cargo drops
  - Generate localized weather refinements for tactical operations
  - Rapid deployment in forward/deployed locations
- **Operational Requirements**:
  - Wind speed/direction data (primary for Army and SOF support)
  - Temperature and dewpoint
  - Pressure measurements
  - Data delivery within 15 minutes of landing for assimilation into AF models

### Non-Defense Applications
- **NOAA**: Potential replacement for balloon-borne radiosondes (currently 800+ weather stations worldwide use radiosondes twice daily)
- **National Weather Service (NWS)**: Replacement platform for upper-air balloon soundings
- **Atmospheric research**: Platform for universities and research centers

## Key Metrics & Objectives (Trial Success Criteria)

### Performance Validation
1. **Flight Performance**:
   - Reach 15,000 ft in under 20 minutes
   - Execute 10 consecutive autolands with error never exceeding ±10 ft
   - Sample in winds exceeding 30 mph

2. **Sensor Accuracy** (meteorological suite):
   - Wind estimation (lateral): ±2° heading, ±0.3 m/s speed
   - Wind estimation (vertical): ±0.4 m/s
   - Temperature: ±0.3°C RMS
   - Pressure: ±1.5 hPa RMS
   - Humidity: ±1.3% RMS

3. **Ground Systems & Data Handling**:
   - Mission prep: <5 minutes per mission
   - Real-time telemetry of science data over entire 0–15,000 ft profile
   - Data file generation for AF system upload: within 5 minutes of landing

## Milestone Schedule & Deliverables

| Task | Delivery | Deliverable | Acceptance Criteria | Payment |
|------|----------|-------------|-------------------|---------|
| 01 | +1 mo | Commercial/AF requirements specifications | AF End-Users agree specs meet needs | $50,000 |
| 02 | +4 mo | 15-slide status report | AF technical monitor acceptance | $100,000 |
| 03 | +8 mo | 15-slide status report | AF technical monitor acceptance | $150,000 |
| 04 | +12 mo | 700-word summary report | AF technical monitor acceptance | $150,000 |
| 05 | +13 mo | Project summary & technical report | AF technical monitor acceptance | $100,000 |
| 06 | +13 mo | Deliver S0 UAS system with AF customizations | AF End-User physical acceptance | $50,000 |
| 07 | +13 mo | Training for AF end-user(s) on S0 operation | AF End-User(s) verify training sufficiency | $50,000 |
| 08 | +14 mo | Test support & performance report | AF End-User(s) endorse test results | $50,000 |
| 09 | +15 mo | Additional reporting as required | AF acceptance of all required documents | $49,380 |

**Total Phase II Proposed Value**: $699,380

## Phase I Results & End-User Discovery

### S0 Prototype Testing
- Flew atmospheric sensing suite prototype in Phase I
- Validated core operational concepts with Air Force end-user

### AF End-User Requirements (from Phase I discussions)
- **Altitude**: 10,000 ft minimum (goal supports most tactical missions)
- **Flight Duration**: Shorter is better for rapid data delivery (40 minutes acceptable); prioritizes data fidelity over speed
- **Recovery Area**: ±10 ft accuracy; must consider safety/ease of use and environmental factors (fields, desert, forest, hills)
- **Data Downlink**: Post-landing collection acceptable if recovery/processing time <15 minutes
- **Deployment**: Hand-launch by AF Weather operator (SOF or Army support)
- **Parameters Needed**: Standard upper-air measurement—wind speed/direction (critical for Army/SOF), temperature, dewpoint, pressure

## Air Force End-User & Stakeholder Engagement

### MOU Status
- **MOU obtained from**: Bruce A. Lambert, NH-04, DAF Chief Engineer, Weather Systems Branch, Air Force Life Cycle Management Center, Hanscom AFB, Massachusetts
- **MOU statement**: "The Upper Air UAS solution proposed by Black Swift is of interest to AFLCMC/HBAW, and can assist Air Force Weather in developing a tactical upper air measurement tool to support Air Force, Army, and SOF operations, which is a current unfunded requirement for ACC/A5W. Should Black Swift be selected for a Phase II award under the SBIR program, it would provide a great opportunity to conduct feasibility and/or prototyping to better test their technology with Air Force Weather needs."

### Key Stakeholder Engagement Requirements
- **Range Access & Safety**: BST has access to primary test site (600-acre sod farm 15 miles from BST office); required FAA certifications, range permissions, and insurance
- **Interfacing Needs**: Test range officials, Information Assurance (IA) officials, FAA coordination, technical monitor support
- **Track Record**: BST demonstrated strong history obtaining approvals from NASA, NOAA, and DOE

## Commercialization & Financial Sustainability

### Prior SBIR Commercialization Successes
- Soil Moisture Mapping UAS (NASA SBIR-derived)
- S2 UAS (developed under 2 NASA SBIRs)
- Multi-hole Probe (NASA SBIR-derived; 9 units sold to date, expanding market)
- Machine Vision technology for UAS (NASA SBIR; transferred to underwater technology sector with commercial customer)
- Predictive maintenance technology for UAS (NASA SBIR)

### Market Size & Opportunity
- Weather forecasting market: Projected $4.63 billion by 2025
- Potential customers: NOAA, NSSL (National Severe Storms Laboratory), NCAR (National Center for Atmospheric Research)
- Addressable market: 800+ weather stations worldwide using balloon radiosondes twice daily
- Expected S0 margin: ~50%

### BST Financial Performance (as of proposal)
**Profit & Loss Comparison** (Jan 1 – Nov 1, 2019 vs. 2018):

| Metric | 2019 (Jan-Nov) | 2018 (Jan-Nov) |
|--------|----------------|----------------|
| Total Income | $941,197.50 | $799,107.04 |
| COGS | $160,306.86 | $180,241.34 |
| Gross Profit | $780,890.64 | $618,865.70 |
| Total Expenses | $579,067.70 | $512,345.10 |
| Net Operating Income | $201,822.94 | $106,520.60 |
| Net Income | $203,970.93 | $81,792.47 |

- **Year-over-year growth**: 17.8% increase in total income (Jan-Nov 2019 vs. 2018)
- **Profitability**: BST demonstrated end-of-year profit for 5 consecutive years
- **2019 Status**: Nearly 15% ahead of revenue pace from prior year

### Pricing Strategy
- **MHP Version 1**: $1,000 (5-hole probe, pressure, temp, humidity)
- **MHP Version 2**: $2,000 (Version 1 + IMU, magnetometer, GPS RTK)
- **S0-AD**: $5,000 per unit

## Notable Details & Competitive Advantages

### Unique Technical Capabilities
- **