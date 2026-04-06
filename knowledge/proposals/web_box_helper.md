# Web Box Helper

## Document Metadata
- Type: Interim Report (summary)
- Client/Agency: NOAA
- Program/Solicitation: SBIR Phase I (2019)
- Date: April 30, 2020
- BST Products/Systems Referenced: S1 aircraft, S2 aircraft, BST avionics
- Key Personnel: Not named in this document

## Executive Summary
BST completed Phase I work on a vision-based navigation system (Web Box Helper) for small unmanned aircraft, developing optical flow and sensor fusion algorithms to provide aircraft ground speed, odometry, and position estimates. The system was integrated into BST S1 and S2 platforms, with flight testing conducted to validate performance.

## Technical Approach
The project centered on computer vision-based autonomous navigation:
- **Optical flow algorithm**: Estimates aircraft ground speed and odometry using downward-facing camera imagery, providing stable position solutions over 30-second windows at 26 FPS on embedded hardware
- **Sensor fusion**: Integrates optical flow estimates with BST avionics (inertial and air data), magnetometer heading calibration, and wind-corrected inertial navigation via Kalman filtering
- **Machine vision hardware**: Downward-facing camera with single board computer for onboard processing
- **Key frame following**: Algorithm design to provide position updates with minimal processor overhead
- **SLAM exploration**: Literature review and candidate identification for Simultaneous Localization and Mapping capability

## Products & Capabilities Described

**BST S1 and S2 Aircraft**
- Platforms used for mechanical integration and flight testing of vision system
- Compatible with added machine vision payload

**BST Avionics**
- Used as stand-in for dedicated inertial and air data boards in Phase I
- Provides magnetometer, inertial, and air data inputs to sensor fusion algorithm

## Use Cases & Applications
- Small unmanned aircraft autonomous navigation without GPS or external positioning
- Ground speed and odometry estimation for position/navigation awareness

## Key Results

| Milestone | Completion | Due Date | Status |
|-----------|------------|----------|--------|
| Optical Flow Algorithm Design | 100% | 04/24/20 | Complete; flight tested |
| Sensor Fusion Algorithm Design | 100% | 04/30/20 | Complete; Kalman filter deployed |
| Hardware Selection & Board Design | 100% | 03/06/20 | Complete |
| Mechanical Integration | 100% | 03/20/20 | Integrated into S1 and S2 |
| Flight Test & Evaluation | 100% | 04/24/20 | Two relevant flights; supplemented with high-fidelity simulation |
| Key Frame Following Algorithm | 80% | 05/08/20 | Prototyped; full demo in development |
| SLAM Algorithm Development | 50% | 05/15/20 | Literature review complete; two candidates selected |

**Performance Achievements:**
- Optical flow algorithm runs at 26 FPS on embedded target (sufficient for application)
- Position solution stable over 30-second window
- Hardware selected with room for expansion in weight and cost
- High-fidelity simulation developed to supplement limited flight data

## Notable Details
- Document references "full associated interim report" for complete details
- Work was conducted as Phase I of a multi-phase SBIR effort
- Limited actual flight test data supplemented by high-fidelity simulation for algorithm development and verification
- Focus on embedded processor constraints and real-time performance
- Technology applicable to GPS-denied or GPS-challenged autonomous flight operations