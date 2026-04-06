# Phase II+ Proposal - Battery Health and Propulsion Degradation Monitoring

## Document Metadata
- Type: SBIR Phase II+ Proposal Presentation
- Client/Agency: NASA
- Program/Solicitation: 2017 SBIR (Phase II-E)
- Date: 2018-10-23
- BST Products/Systems Referenced: ECAM (Electronic Centralized Aircraft Monitoring interface), UAS flight monitoring systems
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
BST proposed a Phase II+ effort to improve battery health monitoring and propulsion degradation detection for UAS operations, leveraging battery technology from Dynexus. The work aims to reduce UAS accident rates by addressing battery system failures (currently 13.7% of UAS failures) and propulsion degradation—critical gaps in current UAS safety monitoring for integration into the National Airspace System (NAS).

## Technical Approach

### Battery Health Monitoring
- Predict remaining battery capacity within 100mAh accuracy
- Predict total battery capacity to within 200mAh accuracy
- Implement three-tier failure warning system via ECAM interface:
  - **Level 1 (Caution):** Total capacity below 75%
  - **Level 2 (Master Caution):** Total capacity below 60% OR remaining capacity after landing below 20%
  - **Level 3 (Master Warning):** Remaining capacity after landing below 10%

### Propulsion Degradation Detection
- Develop regression algorithm to monitor propulsion system efficiency
- Classify reduced engine performance into four categories: damaged motor, damaged propeller, icing conditions, or other
- Three-tier failure warning system via ECAM:
  - **Level 2 (Master Caution):** 80% of nominal efficiency (motor/propeller/other damage) OR icing conditions detected in pre-flight
  - **Level 3 (Master Warning):** 60% of nominal efficiency (motor/propeller/other damage) OR 80% of nominal with icing

### Data Collection Plan
- **Bench testing (3 hours):** nominal motor system, bent motor shaft, damaged propeller
- **Flight testing (1 hour):** nominal system, bent motor shaft, damaged propeller
- **Stretch goal:** 1 flight through known icing conditions

### Sensor/Telemetry Data Gathered
Motor RPM, voltage, current, throttle setting, static pressure, OAT (outside air temperature), humidity, altitude, IAS (indicated airspeed), climb/sink rate, aircraft mass

## Products & Capabilities Described

### ECAM (Electronic Centralized Aircraft Monitoring)
- Cockpit interface for presenting battery and propulsion health alerts across three severity levels
- Provides standardized warnings (Level 1 Caution, Level 2 Master Caution, Level 3 Master Warning)

### Battery Tracking System
- Real-time capacity estimation with high precision
- Post-landing reserve capacity prediction

### Propulsion Health Monitoring
- Efficiency regression modeling
- Fault classification capability

## Use Cases & Applications

### Primary Mission
- UAS safety improvement for National Airspace System (NAS) integration
- Reduction of UAS accident rates from current 3,800 per 100,000 flight hours to General Aviation (GA) baseline of 11.8 per 100,000 flight hours

### Secondary Market Opportunity
- Electric vertical-takeoff-and-landing (eVTOL) market proving ground
- Target market includes Uber, Airbus, Bell, Boeing, and Embraer
- eVTOL market requirements: autonomy, affordability, low noise

## Rationale & Problem Statement

- **Current UAS safety gap:** UAS failure rate is ~320× higher than GA aircraft (3,800 vs. 11.8 per 100,000 flight hours)
- **Battery system criticality:** 13.7% of current UAS failures attributed to battery system issues
- **Technology gap:** Limited advanced battery monitoring technology available in current SBIR efforts
- **NAS integration requirement:** More robust monitoring needed for widespread UAS integration into National Airspace System

## Notable Details

- Proposal frames battery/propulsion health monitoring as foundational safety technology for broader UAS market expansion
- Technology has dual application to emerging eVTOL commercial market (urban air mobility)
- Approach uses proven ECAM alerting paradigm (from manned aviation) adapted for UAS
- Data-driven fault classification (damaged motor vs. propeller vs. icing vs. other) suggests machine learning or statistical modeling component
- Includes ambitious icing validation goal despite typical UAS operating restrictions