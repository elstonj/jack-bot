# AFX22.4 Phase II Technical Volume

## Document Metadata
- Type: SBIR Phase II Proposal – Technical Volume
- Client/Agency: U.S. Air Force (AFWERX)
- Program/Solicitation: AFX224-OCSO1 Phase II; Topic: Open Call for Innovative Defense-Related Dual-Purpose Technologies/Solutions
- Date: Submitted 2023 (created Oct 23, 2023; modified Apr 2, 2024)
- Proposal Number: F2-16588
- CAGE Code: 6PGF9
- BST Products/Systems Referenced: S2 (fixed-wing UAS), E2 (multirotor UAS), L-band radiometer (LDCR), SwiftCore flight management system
- Key Personnel: Dr. Jack Elston (Founder/CEO, PI), Dr. Maciej Stachura (Founder/CTO, Lead Engineer), Michael A. Hurowitz (CEO/CTO Orbital Micro Systems, LDCR Sensor Lead), Dr. Eryan Dai (Remote Sensing Scientist)

## Executive Summary
Black Swift Technologies proposes to adapt its existing commercial soil moisture mapping UAS into a dual-use system for mapping soil integrity (measured as cone index) to support C-130 cargo operations on unimproved landing zones worldwide. Working with Orbital Micro Systems (OMS) and the Center for Environmental Technology (CET), BST will modify an L-band radiometer, add thermal and NDVI sensors to a UAS platform, develop soil integrity algorithms, and conduct validation testing at Tyndall AFB. The resulting system will provide rapid, comprehensive mapping replacing current labor-intensive ground-based dynamic cone penetrometer measurements.

## Technical Approach

### Core Technology Foundation
- **Existing Commercial Base**: L-band Lobe Differencing Correlation Radiometer (LDCR) developed under NASA SBIR, previously validated for soil moisture mapping
- **Operational History**: 15+ years sensor development evolution; 8 years flight testing; TRL 8 for radiometer and UAS, TRL 4 for soil integrity outputs (expected TRL 7 by Phase II conclusion)

### Proposed Modifications

**1. L-Band Radiometer (LDCR) Upgrades:**
- Modify PCB design with integrated electromagnetic shielding and isolation hardware to reduce RF interference (RFI)
- Improve radiometric measurement accuracy and calibration source stability
- Implement rapid processing software for near-real-time soil moisture visualization on UAS or ground station
- Lab validation of sensor sensitivity, internal calibration stability, and overall performance

**2. UAS Platform Modifications (E2 multirotor base):**
- Mechanical housing redesign to accommodate updated radiometer
- Integration of surface temperature sensor and NDVI (Normalized Difference Vegetation Index) sensor
- Data logging/processing unit for real-time calculation capability
- All sensors must collect data simultaneously for soil integrity assessment

**3. Soil Integrity Algorithm Development:**
- Algorithm to compute cone index from L-band soil moisture measurements plus soil type
- Rapid post-flight processing code executable on-site for near-real-time results
- Accuracy and resolution optimization methods

### Technical Risk Mitigation
- **RF Interference Risk**: Addresses susceptibility via proprietary digital radiometer detection technique under development with CET; future capability to operate at lower frequencies for improved soil penetration
- **Soil Penetration Depth Risk**: L-band operating depth (~10 cm) may not fully capture cone test behavior at all C-130 weights; digital detection permits lower-frequency operation if needed

### Operational Specifications
- **Measurement Band**: 1400-1427 MHz (Earth Exploration Satellite Service protected band)
- **Radiometer Architecture**: LDCR with dual reference signals, dual antennas (zenith/nadir looking)
- **Calibration Accuracy**: 1.2 K (Kelvin) NEDT sufficient to discern ~1% volumetric soil moisture (VSM) differences
- **Soil Penetration**: ~10 cm depth
- **Pixel Resolution**: Approximately equal to aircraft flight altitude; enhanced post-processing possible
- **Coverage Capacity**: 3000' × 60' runway area mapable in ~10 minutes
- **Flight Altitude**: Variable (affects resolution)

## Products & Capabilities Described

### 1. **L-Band LDCR Radiometer**
- **What it is**: Miniaturized L-band passive radiometer using proprietary Lobe Differencing Correlation Radiometer architecture
- **Previous use context**: Soil moisture mapping for NASA SMAP satellite calibration (NASA SBIR), USGS wildfire mitigation (California), NOAA SPLASH hydrological project, Toro commercial irrigation optimization
- **Specifications**: 
  - Operates 1400-1427 MHz band
  - Measures brightness temperature with 1.2 K accuracy
  - Enables ~1% VSM discrimination within 10 cm soil depth
  - Low power consumption, stable design from 8+ years evolution
- **Proposed adaptation**: Hardened PCB design for reduced RFI; improved accuracy/precision; rapid processing software

### 2. **E2 UAS Platform (Multirotor)**
- **What it is**: COTS BST-developed multirotor UAS
- **Proposed modifications**: Housing redesign; integration of thermal sensor, NDVI sensor, data logger; capability for simultaneous multi-sensor data collection
- **Performance**: Can map 3000' × 60' runway in ~10 minutes
- **Manufacturing**: Fully USA-manufactured

### 3. **S2 UAS (Fixed-Wing)**
- **What it is**: COTS BST fixed-wing UAS alternative platform
- **Application**: Also capable of carrying LDCR payload; used when coverage/resolution balance differs from multirotor
- **Manufacturing**: Fully USA-manufactured

### 4. **Soil Integrity Algorithm/Software Suite**
- **What it is**: New software package (TRL 4 → 7)
- **Function**: Computes cone index from LDCR soil moisture output + soil type data
- **Capability**: Near-real-time on-site processing post-flight
- **Performance metric**: Accuracy and resolution to be determined through local and AFB testing

### 5. **SwiftCore Flight Management System**
- **Brief mention**: State-of-the-art autopilot; minimizes operator workload; improves data quality; customizable for mission demands
- **Not primary focus of this proposal but core BST capability referenced

## Use Cases & Applications

### Primary Use Case: C-130 Runway Operations
- **Mission**: Enable USAF to land C-130 cargo aircraft on unimproved/unconventional landing zones worldwide
- **Problem addressed**: Current manual cone penetrometer approach is:
  - Labor-intensive and time-consuming
  - Provides only limited point measurements
  - Operationally risky in contested areas
  - Unable to generate full landing zone map
  - Impractical in harsh geographic/weather conditions

- **Impact scope**: 
  - 160+ air operation (AO) facilities and airfields
  - 9,000+ worldwide AO personnel
  - 7.3 million annual aircraft operations

### Secondary/Potential Applications

**Defense:**
- Army ground mobility assessments (vehicle trafficking capability)
- Trafficability assessments for expeditionary operations
- Earthen dam stability/saturation monitoring
- Forward air controller decision support for landing suitability

**Non-Defense Commercial:**
- Construction (site assessment for structural load-bearing)
- Mining (soil saturation and integrity around excavation)
- Railways (UK Network Rail contacted; soil integrity around rail lines)
- Agriculture (precision irrigation optimization via Toro partnership model)
- Land management (wildfire-prone area monitoring continuation)

### Transition Path
- **Phase II customer**: AFRL/RQ (Aerospace Systems Directorate) with TPOC Paul Fleitz; Civil Engineering School at AFIT (Capt Kyle Egbert, 1st Lt Collin Gwaltney)
- **Phase III transition**: Air Force Civil Engineer Center's Airfield Pavement Evaluation team at Tyndall AFB, FL
- **Future operational integration**: Air Mobility Command (AMC) and Expeditionary Civil Engineer Group
- **Long-term vision**: Air-deployed UAS release from C-130 for pre-landing zone reconnaissance

## Key Results (Phase II Objectives & Expected Deliverables)

### Technical Objectives & Key Results Framework

**Objective 1: Modified L-Band Radiometer (LDCR)**
- Completed PCB redesign with RFI shielding/isolation components
- Lab assessment report: sensor sensitivity, calibration stability, overall performance metrics
- Improved data processing software for rapid on-site soil moisture visualization
- Flight testing vs. previous design with performance metrics delivery

**Objective 2: UAS Platform Modifications**
- E2 UAS design documents, prototype, and test results
- Mechanical housing adaptation for updated sensor + thermal/NDVI sensors
- Real-time soil moisture calculation validation
- Prototype deliverable for local and on-base testing

**Objective 3: Soil Integrity Algorithm Development**
- Algorithm and code for cone index computation (inputs: L-band soil moisture + soil type)
- Rapid post-landing processing capability
- Accuracy/resolution assessment with improvement methods

**Objective 4: Local Field Testing & Refinement**
- Test flights at BST's Longmont, CO site across grass, crops, bare soil
- In situ cone index measurements via standard penetrometer for ground truth
- Algorithm validation and improvement data collection
- Coordination with DAF customer for accuracy/repeatability requirements

**Objective 5: Tyndall AFB Validation Campaign**
- Hardware/algorithm refinements based on local testing
- Flight campaign at Tyndall AFB in partnership with AFRL
- Quantitative reliability and accuracy assessment vs. ground truth sensors
- Results conveyed to customer

### 21-Month Deliverable Schedule

| Milestone | Timeline | Deliverable | Acceptance Criterion | Payment |
|-----------|----------|-------------|---------------------|---------|
| 1 | Award + 1 mo | Customer requirement specifications (resolution, accuracy, format) | DAF end-users confirm specs meet needs | $100,000 |
| 2 | Award + 6 mo | Modified L-band sensing instrument with refined radiometer & auxiliary sensors | DAF customer accepts via status report | $200,000 |
| 3 | Award + 8 mo | UAS modifications with temperature & NDVI sensors for real-time calculation | DAF customer accepts MVP testing results | $200,000 |
| 4 | Award + 12 mo | Soil integrity algorithms & code (cone index from soil moisture + soil type) | DAF customer accepts algorithm docs & past data results | $200,000 |
| 5 | Award + 14 mo | Local field test data (cone index in situ + UAS soil moisture) | Data compiled and made available to TM | $100,000 |
| 6 | Award + 17 mo | Cone index computation refinement (vs. ground penetrometer) | DAF end-user examines & accepts via status report | $200,000 |
| 7 | Award + 18 mo | Tyndall AFB flight campaign report | Test report endorsed by DAF end-user(s) | $150,000 |
| 8 | Award + 21 mo | Additional AF-required reporting/documentation | All reports endorsed by DAF end-users | $99,725 |

**Total Phase II Contract Value**: $1,249,725 (over 21 months)

### Final Report Requirements
- Single-page project summary (non-proprietary)
- Project objectives met and work completed
- Results obtained and technical feasibility estimates
- Quarterly status reports minimum
- Phase II summary report (≤700 words) with technology description and government/private sector applications

## Notable Details

### Company Background
- **Founded**: 2011, Boulder, CO
- **Business Model**: Bootstrapped; no external investors; all equity retained
- **Market Position**: 11+ years purpose-built UAS development; proven capability in extreme environments

### Technical Maturity & Prior Success
- **SBIR Portfolio**: 18 successful SBIR projects; 3 transitioned to Phase III
- **NASA/NOAA/USGS Partnership History**: 
  - NASA SBIR for L-band radiometer development (original soil moisture mapping)
  - NOAA Phase III contract for hurricane observation UAS and mountainous soil moisture mapping
  - USGS partnership for wildfire mitigation soil moisture measurements
- **Non-Defense Commercial Revenue (prior 12 months)**: ~$750,000
- **Predecessor Technology Sales**: