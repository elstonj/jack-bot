# VTOL Autopilot Project - Month 8 Update

## Document Metadata
- Type: Project status update (presentation)
- Client/Agency: Creare
- Program/Solicitation: 2019 VTOL Autopilot
- Date: January 20, 2020
- BST Products/Systems Referenced: Autopilot (AP) code, small prototype aircraft, Double Eagle
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
Black Swift Technologies completed controller and estimator implementation for a VTOL autopilot system, conducted simulator validation, and successfully achieved fully autonomous flight of a small prototype including navigation capabilities. The month focused on embedded system development, UI updates, prototype hardware upgrades, and initial flight testing with identified areas for improvement.

## Technical Approach
- Implemented full state machine for autopilot control
- Developed navigation system using "zero-roll yawing" technique
- Validation performed through Gazebo simulator with small prototype model
- Integrated safety parachute system to enable more aggressive testing schedule
- Added camera and video telemetry to prototype for monitoring

## Products & Capabilities Described

**Autopilot (AP) Code**
- Full controller and estimator implementation completed
- State machine-based architecture
- Integration with navigation system
- UI for VTOL control and monitoring

**Small Prototype Aircraft**
- Successfully achieved fully autonomous flight with navigation
- Equipped with pitot tube for airspeed measurement
- Laser system (purpose not detailed)
- Safety parachute system (deployed once during testing)
- Camera with live video transmission (low resolution) and 720p recording capability
- Demonstrated takeoff, transition, and forward flight phases

**Double Eagle (Larger Platform)**
- Mentioned for upcoming hover testing phase
- Autopilot integration planned

## Use Cases & Applications
- VTOL aircraft autonomous flight testing
- Development of coordinated turn capabilities
- Vertical takeoff and land (VTOL) operations with wing configuration

## Key Results
- Controller and estimator fully implemented and integrated into AP code
- Simulator validation completed
- Small prototype achieved fully autonomous flight including navigation
- Successfully demonstrated launch, takeoff, transition, and forward flight phases
- Safety parachute system validated (single deployment test)
- Camera/video system operational

## Problems Identified
- Navigation tracking performance needs improvement
- Indicated airspeed (IAS) dips during skidding turns
- Camera system issues (power-related malfunction)

## Next Steps
- Implement coordinated turns and compare power consumption
- Improve navigation tracking accuracy
- Hover testing of Double Eagle platform
- Complete autopilot integration on Double Eagle
- Gain tuning optimization
- Achieve vertical takeoff and land with wings on

## Notable Details
- Parachute system enabled more aggressive testing schedule and provided safety margin for prototype operations
- Navigation approach used "zero-roll yawing" technique rather than traditional coordinated turn methods
- Project in active development phase with defined milestones progressing toward larger platform (Double Eagle) deployment
- Simulator-based validation using Gazebo enabled safe iteration before flight testing