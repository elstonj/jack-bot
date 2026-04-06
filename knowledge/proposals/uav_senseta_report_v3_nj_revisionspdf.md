# UAV Senseta Report V3 NJ Revisions

## Document Metadata
- Type: Research Report
- Client/Agency: Senseta (Colombian aerial surveying/mapping company)
- Program/Solicitation: Internal equipment evaluation
- Date: 2014-03-27 (Version 3)
- BST Products/Systems Referenced: Black Swift Company mentioned as potential developer of custom sUAS
- Key Personnel: Juan Nicolás Vargas Alejo (Electronic Engineer - elaboration), Jairo Alexander Lozano Ramírez (Civil Engineer - review), Rosario Ballesteros Casas (CEO Senseta - approval)

## Executive Summary
This is an internal research report by Senseta, a Colombian UAV services company, evaluating available UAV systems and defining ideal specifications for their operational needs. The report synthesizes 3.5 years of operational experience (2,000+ flight hours) to establish requirements for improved aerial surveying and mapping capabilities. The document evaluates existing platforms and concludes that commercial options are limited, recommending Black Swift as a potential custom developer.

## Technical Approach
Senseta conducted a systematic evaluation framework analyzing available UAV platforms against defined operational requirements. The methodology involved:
- Comparative analysis of sensor performance (camera GSD at 5cm resolution)
- Mission simulation on a 4,327-hectare polygon test area
- Performance modeling of different endurance/payload configurations
- Evaluation of subsystem architectures (flight platform, control system, launch/recovery, communications, GIS)

## Products & Capabilities Described

### Senseta's Existing Fleet:
**Fixed Wing UAV**
- Autonomous flight capability
- Cruise speed: 25 mph (40 kph)
- Material: EPO Foam
- Endurance: 20 minutes
- Max crosswind for autonomous operation: 20 km/h (12 mph)
- Range: up to 10 miles (16 km)

**Multirotor (3DR X8 Octacopter)**
- Autonomous flight
- Cruise speed: 5 m/s
- Materials: Aluminum and carbon fiber
- Endurance: 6 minutes
- Payload capacity: 600g
- Autopilot: Arduino-based processor

**Aerostatic Sensor**
- Small helium balloon platform
- Picavet camera suspension system
- Video surveillance and image capture

**Cessna Aircraft**
- Integrated Nikon D800 camera
- GPS geotagging
- Used for large area coverage

### Black Swift Company
Referenced as a potential partner capable of developing custom small Unmanned Aircraft Systems (sUAS) tailored to specific user needs.

## Use Cases & Applications

**Primary Mission**: Aerial surveying and photogrammetric mapping in Colombia
- Cadastral mapping
- Large-area coverage (polygon survey: 4,327 hectares)
- High-resolution orthophoto generation
- Areas with difficult terrain access

**Environmental Factors Addressed**:
- High-wind operation (wind speeds up to 70 km/h required due to Colombian geography)
- Variable terrain and remote locations

## Key Results

**Ideal UAV Specifications Defined**:
| Parameter | Specification |
|-----------|---------------|
| Endurance | 3 hours minimum |
| Payload | 6 kg standard; 15 kg for multispectral cameras |
| Control Range | 30 km |
| Wind Speed Tolerance | 70 km/h |
| GPS-RTK | Required (sub-meter accuracy without ground control points) |
| Weight | ~20 kg |
| Materials | Metal alloys, carbon fiber, or glass fiber composites |

**Sensor Performance Analysis**:
For a 4,327-hectare mission with 5cm GSD:
- Samsung NX1000 (20MP, 380g): 52 flights, 20 mission days, 8,767 photos
- Nikon D800 (36MP, 1,200g): 38 flights, 14 mission days, 7,363 photos
- Trimble Camera (60MP, 2,500g): 28 flights, 9 mission days, 4,465 photos

**Endurance Impact Analysis**:
- Current UAV (0.33 hrs endurance): 52 flights, 20 mission days
- Sirius Pro (3 hrs endurance): 8 flights, 5 mission days
- Discoverer (20 hrs endurance): 1 flight, 2 mission days

**Recommendations for Ideal Platform**:
- Must support RGB, IR, multispectral cameras, or compact LiDAR (2-20 kg range)
- Requires Inertial Measurement Unit (IMU) for attitude data
- Autopilot must synchronize camera shutter timing with GPS/IMU for accurate geotagging
- GPS-RTK capability eliminates need for ground control points
- Robust landing gear and emergency parachute required
- Ground station must support mission planning and real-time flight visualization
- Two-channel communications: manual control + telemetry (position, horizon, battery status)

## Notable Details

**Market Assessment**: Report concludes that only four commercial UAVs fully meet requirements:
1. Penguin B
2. Discoverer Small (identified as best commercial option with integrated avionics)
3. Atro-x (250 kg - too heavy for field portability)
4. NEO S-350 (150 kg - too heavy for field portability)

**Strategic Recommendation**: Due to limitations in commercial offerings, Senseta explicitly recommends considering **Black Swift Company** as a custom developer capable of building a sUAS specifically tailored to their operational needs and constraints.

**Key Operational Insights from 3.5 Years Experience**:
- Multirotor systems (6-minute endurance) insufficient for large-area missions
- Fixed-wing platforms optimal for surveying applications
- Sensor weight directly affects mission efficiency (larger sensors = fewer flights)
- RTK-GPS integration provides cost savings by eliminating ground control point surveys
- Portability critical for Colombian terrain access

**Technical Integration Priorities**:
- Camera-autopilot-GPS-IMU integration for precise geo-referencing
- Automated shutter control to minimize image redundancy
- Sub-meter GPS accuracy capability
- Extended range communications for remote operations