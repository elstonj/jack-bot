# Proposal F2-16588 - Non-Proprietary Work Plan (AFWERX SBIR Phase II - Soil Moisture Mapping)

## Document Metadata
- **Type:** SBIR Phase II Proposal / Non-Proprietary Work Plan
- **Client/Agency:** U.S. Department of Air Force (DAF) / Air Force Research Laboratory (AFRL)
- **Program/Solicitation:** AFWERX SBIR Phase II, Topic AFX224-0CS01
- **Proposal Number:** F2-16588
- **Date:** 11 October 2023
- **BST Products/Systems Referenced:** UAS (unmanned aircraft system), L-band radiometer
- **Key Personnel:** Jack Elston (last editor)
- **Partners:** OMS (Orbital Micro Systems), CET (partnering organization), NASA (prior collaboration)

## Executive Summary
Black Swift Technologies, in partnership with Orbital Micro Systems and CET, proposes to modify an existing NASA-validated UAS-based L-band radiometer system to measure soil integrity (cone index) for mapping unimproved landing zones used in C-130 operations. The 21-month Phase II effort will adapt the soil moisture measurement technology with NDVI and thermal sensors, develop soil integrity algorithms, and conduct field validation at local sites and Tyndall Air Force Base to provide forward air controllers with critical decision-support data.

## Technical Approach

### Core Technology
- **Existing Foundation:** L-band radiometer system previously developed and validated in conjunction with NASA for soil moisture mapping
- **Adaptation Strategy:** Modify L-band radiometer for DAF-specific requirements and C-130 landing zone assessment
- **Sensor Integration:** Add NDVI (Normalized Difference Vegetation Index) and thermal sensors for real-time soil moisture calculation
- **Signal Integrity:** Design new electromagnetic interference (EMI) protection for the sensing system
- **Data Architecture:** Develop/select data logger hardware for integrated sensor suite

### Development Tasks (Months 1-18)
1. **Requirements Analysis (Month 1):** Customer interviews and specification gathering for resolution, accuracy, and VAS (vertical antenna scanning)-based soil integrity measurements
2. **Sensing System Modifications (Months 2-6):**
   - Electromagnetic interference protection design
   - New circuit board design, ordering, and assembly
   - Lab testing and validation
   - Mechanical design for UAS mounting and protection

3. **UAS Platform Modifications (Months 4-8):**
   - NDVI and thermal sensor procurement
   - 3D CAD design and wiring integration
   - Build and validation of complete modified system

4. **Algorithm Development (Months 6-12):**
   - Code modification for volumetric soil moisture (VWC) computation with updated radiometer and new sensors in near real-time
   - Literature review and soil integrity algorithm refinement based on soil moisture and soil type relationships
   - Performance validation on historical datasets
   - Development of performance metrics and minimum viable performance thresholds

5. **Local Field Testing (Months 12-14):**
   - Minimum 4 test flights across volumetric water content (VWC) range: 5%-40%
   - In-situ cone penetrometer measurements for validation
   - Testing across 3 different soil types and 3 vegetation cover types

6. **Model Refinement (Months 14-17):**
   - Accuracy quantification of remote sensing technique vs. penetrometer measurements
   - Development of VWC vs. cone index model with soil type coefficients
   - Additional local flights to improve accuracy and minimize error

7. **Operational Testing (Months 17-18):**
   - Flight operations authorization and test plan for Tyndall Air Force Base
   - Data collection across variable soil conditions and moisture levels
   - Comparison of UAS-based data against ground observations
   - Quantitative system performance analysis

## Products & Capabilities Described

### L-Band Radiometer System
- **Purpose:** Measures volumetric water content (soil moisture) from which cone index is derived
- **Prior Development:** NASA-validated system
- **Proposed Enhancement:** Modified for EMI protection and integration with auxiliary sensors
- **Integration:** Will function with NDVI and thermal sensors for real-time soil moisture and soil integrity computation

### Modified UAS Platform
- **Capability:** Autonomous or remote-piloted system equipped with integrated sensor suite
- **Sensor Payload:** 
  - Modified L-band radiometer
  - NDVI sensor for vegetation assessment
  - Thermal sensor for surface temperature
  - Integrated data logger
- **Application:** Mapping soil integrity over unimproved landing zones

### Soil Integrity Algorithm
- **Output:** Cone index (measure of soil strength) computed in near real-time
- **Input Variables:** L-band derived volumetric soil moisture, vegetation type/density (NDVI), surface temperature
- **Sophistication:** Soil type-specific coefficients for accuracy across different soil classes
- **Validation Basis:** Comparison against field penetrometer measurements

## Use Cases & Applications

### Primary Use Case: C-130 Landing Zone Assessment
- **Mission:** Map soil integrity to support forward air controllers' decision-making for C-130 operations
- **Operational Need:** Assess unimproved landing zones for aircraft landing suitability
- **Decision Support:** Provide rapid, high-resolution soil integrity data for quick informed decisions
- **Operational Impact:** Improve mission effectiveness and safety for tactical airlift operations

### Test Locations
- **Local Testing:** Unspecified local sites with controlled soil and vegetation conditions
- **Operational Testing:** Tyndall Air Force Base (primary) or other customer-defined locations

### Soil Conditions Tested
- Volumetric water content range: 5%-40%
- Multiple soil types (minimum 3)
- Multiple vegetation cover types (minimum 3)

## Deliverables & Milestones

| Milestone | Timeline | Deliverable | Acceptance Criteria | Payment |
|-----------|----------|-------------|-------------------|---------|
| M1: Requirements Analysis | +1 month | Customer specifications and requirements list | DAF end-users confirm specifications meet needs; Requirement Plan accepted | $100,000 |
| M2: Sensing System Modifications | +6 months | Modified L-band radiometer with EMI protection and new circuit board | DAF Customer accepts testing results via status report | $200,000 |
| M3: UAS Platform Modifications | +8 months | Modified UAS with NDVI/thermal sensors and real-time calculation capability | DAF Customer accepts MVP testing results | $200,000 |
| M4: Algorithm Development | +12 months | Algorithms and code for cone index computation | DAF Customer accepts documentation and validation results | $200,000 |
| M5: Local Field Testing | +14 months | Test data compiled with in-situ cone index and soil moisture measurements | Gathered data available for technical monitor acceptance | $100,000 |
| M6: Model Refinement | +17 months | Refined cone index computation model with accuracy improvements | DAF End-User accepts results vs. ground-based measurements | $200,000 |
| M7: Tyndall AFB Testing | +18 months | Flight campaign test report and comparative analysis | Test report endorsed by DAF End-Users confirming results | $150,000 |
| M8: Final Reporting | +21 months | Final Report, Phase II Summary, and any required documentation | Reports endorsed by DAF End-Users | $99,725 |

**Total Contract Value:** $1,249,725

### Required Reports
- **Final Report:** Draft within 30 days of Phase II completion; includes single-page summary, objectives met, work completed, results, technical feasibility
- **Quarterly Status Reports:** Progress documentation aligned with DAF end-user needs
- **Phase II Summary Report:** ≤700 words; includes technology description and applications/benefits
- **Engineering Documentation:** Drawings, software documentation, user manuals, O&M documentation as required
- **Hazard Analysis:** Preliminary hazard analysis to be included in deliverables

## Notable Details

### Team Composition
- **BST Role:** Lead contractor with UAS and system integration responsibility
- **Orbital Micro Systems (OMS):** Technology partner (L-band radiometer expertise)
- **CET:** Supporting partner
- **AFRL Collaboration:** Long history with UAS remote sensing; will provide ongoing support and Tyndall AFB coordination

### Technical Validation Strategy
- **Dual Validation Approach:** UAS remote sensing data compared directly against ground truth (cone penetrometer measurements)
- **Real-World Testing:** Field campaigns designed to capture performance across natural variability in soil type, moisture, and vegetation
- **Iterative Refinement:** Local testing results inform model refinement before operational testing at Tyndall AFB

### Operational Integration Focus
- **End-User Emphasis:** Direct collaboration with DAF end-users and forward air controllers for requirements definition
- **Decision Support:** System designed to provide rapid, actionable intelligence rather than research data alone
- **Near Real-Time Processing:** Algorithm designed for on-board or rapid computation of soil integrity during flight operations

### Unique Capabilities Leveraged
- **Heritage Technology:** Builds on existing NASA-validated L-band radiometer reducing technical risk
- **Integrated Multi-Sensor Approach:** Combines radiometric soil moisture measurement with optical and thermal data for enhanced accuracy
- **Operational Validation:** Planned testing at active military installation (Tyndall AFB) rather than laboratory environments only

### Risk Mitigation Elements
- **Staged Development:** Concurrent UAS and sensing modifications (Tasks 2-3) allow parallel progress
- **Early Algorithm Validation:** Code tested on existing historical datasets before field collection
- **Controlled Local Testing:** 4+ flights across defined soil/moisture/vegetation matrix establish performance envelope
- **Performance Metrics:** Explicit acceptance criteria tied to accuracy and resolution requirements