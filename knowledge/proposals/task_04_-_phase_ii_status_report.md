# Task 04 - Phase II Status Report: Atmospheric Sounding UAS

## Document Metadata
- Type: Phase II Status Report
- Client/Agency: U.S. Air Force (AFRL)
- Program/Solicitation: SBIR - Atmospheric Sounding UAS
- Contract Number: FA8730-20-C-0021
- Date: 16 March 2021
- BST Products/Systems Referenced: S0 (new design), S1, SwiftPilot (avionics stack)
- Key Personnel: Dr. Jack Elston (PI), Jack Elston (last editor)

## Executive Summary
This Phase II status report documents the development of the Atmospheric Sounding UAS, a vertical takeoff and landing (VTOL) aircraft designed for atmospheric data collection. The report covers completion of the S0 vehicle design and prototype construction, avionics integration using SwiftPilot, wind sensing validation through flight tests, and preparation for an upcoming test campaign at the DOE Southern Great Plains site in March-April 2021.

## Technical Approach

### Vehicle Design
- **Architecture**: VTOL aircraft with pivoting motors for pitch and roll control during hover and transition to/from horizontal flight
- **Wings**: Two-piece wing design (switched from originally planned one-piece due to supplier delays); selected from popular RC glider class with similar aerodynamic profile; requires larger tail than initially designed to accommodate aerodynamic differences
- **Control Validation**: Ground testing validated pitch acceleration control using pivoting motor system; commanded vs. measured pitch acceleration and torque scaling confirmed system capability for full flight regime
- **Construction**: Two first articles completed; aircraft packs into tight configuration for transport

### Avionics Integration
- **Stack**: Black Swift SwiftPilot avionics stack integrated with S0 sensors
- **Sensor Integration**: Drivers written for various sensors and battery management; bench-top testing conducted
- **Design Updates**:
  - Additional PWM lines for pivoting motor control
  - Improved circuit design for user panel switch (enhanced safety)
  - Enhanced power handling when connected to USB
  - Radio on/off control capability added to avionics
  - Component repositioning for fuselage fit
  - Changed power sense resistor for higher current limits
  - Replaced battery management chip due to charging issues
- **Thrust Testing**: New thrust stand acquired for motor/propeller combination testing; critical data generated for VTOL modes, wire gauge validation, and battery cell selection

### Wind Sensing
- **5-Hole Probe**: Nose cone design with 5 dynamic pressure sensors to measure angle-of-attack (α) and angle-of-sideslip (β)
- **Wind Estimation Algorithm**: Onboard wind estimator integrated; validates stable wind field estimation
- **Sensor Performance**: Demonstrated accurate alpha/beta measurements from 5-hole probe

## Products & Capabilities Described

### S0 Aircraft
- New VTOL atmospheric sounding platform
- Features: pivoting motors, two-piece wing, 5-hole probe nose cone, integrated SwiftPilot avionics
- Designed for autonomous operations including autonomous takeoff, altitude hold, airspeed hold, roll and pitch control loops
- Compact, transportable design

### S1 Aircraft
- Existing BST platform used for rapid integration testing and avionics validation
- Used as test bed for S0 avionics before commitment to S0 prototype
- Successfully demonstrated autonomous flight with S0 avionics including control loop performance
- Equipped with pitot tube and standard avionics

### SwiftPilot Avionics Stack
- Modular avionics platform
- Supports sensor integration, autonomous flight control
- Includes wind estimation firmware
- Radio control integration

## Use Cases & Applications

**Atmospheric Sounding/Data Collection**
- Autonomous atmospheric measurements in various flight regimes
- Wind field mapping and estimation
- Integration with balloon soundings for intercomparison
- Operations at DOE Southern Great Plains research site

**Research Collaboration**
- Coordinated operations with University of Nebraska multi-rotor assets
- Cross-validation with traditional balloon sounding data

## Test Campaign
- **Dates**: March 30 - April 3, 2021
- **Location**: DOE Southern Great Plains site
- **Flight Permissions**: Updated for BST S0 operations plus University of Nebraska multi-rotor assets
- **Validation Activities**: 
  - Rigorous launch schedule
  - Additional balloon soundings for intercomparison throughout the day
  - Comprehensive flight testing to validate sensor performance and wind estimation algorithms

## Key Results/Status
- Vehicle design completed and validated through ground testing
- Two S0 first articles constructed
- Avionics integration completed with full sensor driver suite
- Control system performance validated via S1 flight tests (autonomous takeoff, altitude hold, airspeed hold, control loop tracking demonstrated)
- Wind estimation algorithm validated in flight with reduced (pitot) and full (5-hole probe) sensor configurations
- Ready for Phase II test campaign

## Notable Details
- **Pandemic Impact**: Supply chain disruptions required wing supplier/design change mid-Phase II; mitigation achieved through selection of equivalent RC glider wing
- **Design Advantages**: Two-piece wing makes aircraft more portable while maintaining aerodynamic performance
- **Avionics Development**: Significant maturation of power management and safety systems during integration
- **Validation Approach**: Used existing S1 platform to de-risk S0 avionics before committing to prototype; conservative, methodical testing strategy
- **Sensor Innovation**: 5-hole probe integration for simultaneous measurement of wind vector components (velocity, alpha, beta)