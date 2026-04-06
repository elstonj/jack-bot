# Blue River SwiftCore FMS Project Overview

## Document Metadata
- Type: Project proposal / integration plan
- Client/Agency: Blue River Technology
- Program/Solicitation: Commercial sales/custom integration
- Date: April 6, 2016
- BST Products/Systems Referenced: SwiftCore FMS, SwiftTab, SwiftPilot, SwiftStation
- Key Personnel: Not named

## Executive Summary
Black Swift Technologies proposed integrating its SwiftCore Flight Management System into a DJI S1000 and custom Raven X8 multirotor for Blue River Technology, replacing their DJI A2 flight controller with an advanced autopilot system capable of accepting external navigation input from a Phoenix Aerial AL3 RTK/fiber-optic gyro system. The project aimed to deliver two fully integrated flight-ready systems with significantly improved position tracking, waypoint navigation, and mission performance.

## Technical Approach
- **Primary integration task**: Modify SwiftCore FMS to accept external navigation inputs from Novatel SPAN OEM615 navigation board (used with Phoenix Aerial AL3 system)
- **Navigation integration**: Accept 20 Hz attitude and position updates from external nav board; implement failsafe mode to revert to onboard GPS/IMU if external nav covariance exceeds 0.05
- **Vehicle characterization**: Mass, inertia, and rotor performance measurements
- **Custom design/manufacturing**: Electrical and mechanical integration including custom mounts and wiring harnesses
- **Flight testing**: Gain tuning and performance validation/verification
- **Scope characterization**: BST classified this as "nominal vehicle-specific integration" rather than R&D, as no new customer-specific capabilities were being developed

## Products & Capabilities Described

**SwiftCore FMS:**
- Advanced autopilot system replacing DJI A2
- Accepts external navigation solutions (specifically Novatel SPAN OEM615/AL3)
- Capable of executing pre-programmed or in-flight uploaded flight plans
- Smooth banked turn execution along predetermined flight paths
- Manual control capability for recovery in high wind conditions

**SwiftCore FMS Components Included:**
- SwiftTab user interface with tablet computer
- SwiftPilot autopilot system
- SwiftStation ground station

## Flight Performance Requirements
The system was required to achieve the following under specified conditions (wind ≤10 mph, gusting to 15 mph; nav covariance <0.05):
- **Altitude tracking**: ±1 m error tolerance
- **Horizontal path deviation**: ±1 m error tolerance
- **Manual recovery capability**: Ability to conduct forward flight and landing in 20 mph winds
- **Failsafe operation**: Automatic reversion to onboard sensors if external nav degraded

## Use Cases & Applications
- Multirotor sensor-based mapping missions (primary focus)
- High-precision waypoint navigation in wind conditions
- Missions requiring improved 3D position tracking accuracy under adverse weather

## Deliverables
- 2× complete SwiftCore FMS systems with tablets and ground stations
- Full mechanical/electrical integration into both aircraft
- Custom mounts and wiring harnesses (CAD files provided)
- 4-hour training course (2 hours classroom, 2 hours field training) at BST Boulder facility
- Flight test summary report with performance metrics and validation results

## Project Schedule & Effort
- **Duration**: 8 weeks from vehicle receipt
- **Week 1**: Vehicle inspection and characterization
- **Week 2**: Mechanical/electrical design and manufacturing initiation
- **Weeks 3-4**: FMS software modification for external nav inputs
- **Week 5**: Mechanical/electrical integration and validation
- **Weeks 6-7**: Flight testing, gain tuning, performance validation, report generation
- **Week 8**: System delivery

## Budget
- **Total Project Cost**: $29,438 (20% discount applied)
  - 2× SwiftCore FMS @ $8,399 each: $16,798
  - 2× Customer-specific airframe integration @ $10,000 each: $20,000
  - Subtotal: $36,798
  - Discount (20%): -$7,360

**Payment Schedule:**
- Project kickoff: S1000/Raven delivery
- Milestone 1 (electrical/mechanical design approval): $10,000
- Milestone 2 (flight demonstration with external nav): $5,000
- Milestone 3 (performance report submission): $5,000
- Milestone 4 (system delivery): $9,438

## Intellectual Property
- Blue River receives CAD drawings for custom wiring harnesses and vehicle mounts for exclusive use on future X8/S1000 systems using SwiftCore FMS
- All other work products and IP remain BST property

## Notable Details
- **Discount rationale**: 20% discount offered on first two systems (rather than rush fees) in exchange for performance feedback and understanding of future collaboration opportunity
- **Customer responsibility**: Blue River required to supply single S1000 and Raven X8 pre-integrated with AL3 system for BST use during integration period
- **Navigation advantage**: AL3's GPS RTK + fiber-optic gyro was expected to provide significantly more accurate position/attitude than SwiftCore's internal sensors (20 Hz update rate emphasized)
- **External oversight**: Payment schedule structured to provide Blue River input and approval checkpoints at design phase and performance demonstration phases
- **Editor notes**: Document contains internal comments noting scheduling tightness (Week 2 mechanical development timeline questioned) and some discussion about discount vs. rush fee framing