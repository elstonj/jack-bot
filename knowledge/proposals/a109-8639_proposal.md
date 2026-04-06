# Improved UAS Robustness through Augmented Onboard Intelligence

## Document Metadata
- **Type:** SBIR Phase II Proposal
- **Client/Agency:** NASA
- **Program/Solicitation:** NASA SBIR 2017, Topic A1.09 (Vehicle Safety - Internal Situational Awareness and Response)
- **Date:** December 4, 2017 (created); submitted for 2017 SBIR cycle
- **Proposal Number:** A1.09-8639
- **BST Products/Systems Referenced:** S1, S2, SwiftCore Flight Management System (FMS), UAVCAN protocol
- **Key Personnel:** Ricardo Arteaga (NASA Technical Monitor referenced)

## Executive Summary
Black Swift Technologies proposes developing an onboard intelligence system for small UAS that uses networked monitoring nodes and machine learning algorithms to detect early failures, provide diagnostics, and enable safe autonomous operations in the National Airspace System. The system addresses critical reliability gaps that prevent widespread UAS integration by monitoring wireless communications, propulsion systems, actuators, batteries, and identifying safe landing areas through machine vision.

## Technical Approach

### Core System Architecture
- **Distributed Network of Monitoring Nodes:** Decentralized nodes that cooperate with a centralized flight management node
- **Communication Protocol:** CAN bus with open-source UAVCAN protocol for extensibility to third-party UAS
- **Computing Platforms:** 
  - ARM microcontroller-based monitoring nodes (compact, low-power)
  - NVIDIA Tegra-based boards (Jetson X2) for computationally intensive system-wide algorithms and machine learning
- **Machine Learning Approach:** Combination of regression and classification algorithms trained on historical BST flight data (since 2011) and FAA UAS incident databases

### Network Architecture
- Full S2 system example: 6 actuator nodes + 1 battery node + 1 vision node + 1 central management node = 9 total nodes
- Required data bandwidth: 13 kB/s for system-wide communication and fault messages (including packet overhead)
- Redundant bus support for critical systems
- Remote firmware update capability

### Four Types of Monitoring Nodes
1. **Actuator Node:** Tracks servo performance (voltage, current, temperature), detects degradation
2. **Battery Node:** Monitors battery health, remaining capacity, predicts flight time; ensures redundant power supply to mission-critical systems
3. **Vision Node:** Runs deep learning algorithms for safe landing site detection
4. **Flight Management Node:** Central repository for data/hyperparameters; runs system-level management algorithms on Tegra GPU

## Products & Capabilities Described

### S2 Aircraft
- Mid-size UAS platform developed under prior NASA SBIR (soil moisture mapping project)
- Primary test platform for Phase II validation
- Proven in extended flight campaigns (MALIBU project completed 3 campaigns with 2018 campaigns planned; ELEVATE project in Costa Rica)

### S1 Surveying UAS
- Commercial product for 3D photogrammetry and orthomosaics
- Independently verified as best-performing platform for accuracy in its class
- Tight sensor-autopilot integration enables superior tracking and timing accuracy

### SwiftCore Flight Management System (FMS)
- Commercial autopilot system based on modular, networked architecture
- Uses CAN bus for robust communications
- Allows addition/subtraction of sensors, actuators, payloads without redesign
- Upgradeable component architecture for rapid technology adoption

### Machine Learning Algorithms

#### Already Designed and Tested (Phase I):
1. **Communication Performance:** Unscented Kalman Filter + classification to detect lost comm or degraded signal strength based on RSSI and range; detected operator error (incorrect antenna deployment) automatically in historical data
2. **Battery Tracking:** Regression algorithm (UKF-based) to estimate remaining capacity adjusted for temperature; tracks battery aging
3. **Loss of Propulsion Power:** AdaBoost with binary decision trees; 97.3% accuracy detecting engine failure with 1 second of data, 100% with 3 seconds (features: throttle, airspeed, altitude rate, acceleration)
4. **Propulsion System Degradation Tracking:** Regression algorithm comparing electrical input power to aerodynamic output power; corrects for atmospheric effects (temperature, pressure, density altitude) and aircraft mass to identify efficiency losses

#### To Be Developed/Validated in Phase II:
5. **Classification of Propulsion Degradation:** Distinguish between nominal, damaged motor, damaged propeller, aircraft icing, and unknown failures; uses vibration signatures and atmospheric data
6. **Launcher Performance:** Track pneumatic launcher degradation over time
7. **Actuator Degradation/Failure:** Preventative maintenance tracking; monitors servo deflection, current, voltage, temperature, cycle count
8. **Flying/Not Flying Classification:** Safe power recovery algorithm; detects if aircraft is in flight upon boot-up to prevent throttle-up on ground
9. **Safe Landing Area Detection:** Deep learning on NVIDIA Tegra to identify trees, bushes, buildings, power lines, rough terrain, roads; generates safe landing zones based on aircraft landing distance requirements

### Customer Portal (Post-Processing Tool)
- Web-based platform where BST customers upload flight logs
- Algorithms assess communication system, propulsion system, and identify other faults
- Provides automated maintenance recommendations
- Data format published for use with non-BST UAS systems
- Creates growing database to improve algorithm training over time

## Use Cases & Applications

### Primary Missions Addressed
1. **Beyond-line-of-sight (BLOS) Operations:** Monitoring subsystems without direct pilot oversight
2. **Operations Over Populated Areas:** Safe failure detection and mitigation
3. **Fully Autonomous Operations:** High reliability without human intervention
4. **Scientific Missions:** Soil moisture mapping, multi-angle imaging, trace gas sampling (MALIBU, ELEVATE projects)
5. **Harsh Environments:** Arctic operations, volcano monitoring, hurricane sampling (implied from context); icing detection/mitigation for mountain operations

### Specific Failure Mitigation Examples
- **Lost Communication:** Real-time range tracking; checklist generation for operator corrective action
- **GPS Outage:** Safe landing area detection as fallback
- **Propulsion Failure (engine out):** Immediate detection to inform operator or autopilot for emergency procedures
- **Aircraft Icing:** Efficiency tracking detects ice accumulation; alerts operator to climb above cloud layer or return to base
- **Launcher Malfunction:** Tracks degradation over time to schedule maintenance before failure
- **Servo/Actuator Degradation:** Preventative maintenance warnings; preflight checks

## Key Results (Phase I)

### Failure Analysis
From BST flight database (since 2011) and FAA database:
- **Overall Success Rate:** 80.4%
- **Partial Failures:** 15.2% (mission redo required or next mission prevented)
- **Catastrophic Failures:** 3.8% (crash or complete loss)

**Failure Breakdown (by frequency):**
| Failure Type | Percentage |
|---|---|
| Lost Communication | 4.4% |
| Payload Failure | 3.2% |
| Landing Failure | 2.2% |
| GPS Outage | 1.9% |
| Loss of Propulsion Power | 1.9% |
| Inflight Airframe Failure | 1.3% |
| Launch Failure | 1.3% |
| Inclement Weather | 0.6% |
| User Error | 0.6% |
| Loss of Onboard Power | 0.6% |

BST data tracked well with FAA database proportions (Equipment Failure ~79-69%, Pilot Error ~20-31%).

### Algorithm Validation Results

**Communication System (Flight 2016-05-13):**
- Detected missed ground station antenna deployment in flight
- Regression (UKF) + classification algorithm correctly identified communication range reduction from 600m to 3km after correction
- Algorithm operates on encrypted and unencrypted links

**Propulsion System - Engine Failure Detection:**
- Classification accuracy: 97.3% with 1 second data; 100% with 3 seconds
- Decision boundary partitioning shows clean separation between engine-out (full throttle, negative energy change) and nominal states

**Propulsion Efficiency Tracking:**
- Demonstrated constant efficiency when corrected for aerodynamic effects
- Successfully identified anomalies: detected outlier flight with heavier payload (5.5→6.5 lbs) automatically
- After mass correction, fit normalized across multiple flight days
- Algorithm ready to detect efficiency degradation from motor damage, propeller damage, or icing

**Vision-Based Safe Landing Detection (Phase I preliminary):**
- Training: Caffe deep learning framework on NVIDIA Tesla K40; targeted for NVIDIA Jetson deployment
- Classified trees and bushes in rural flight data (1km × 1km areas)
- Successfully identified landing gaps in two test images (~176m × 117m each); S1 requires 30m landing distance
- Training data from 2016-08-15 flights near Enid, OK

### Hardware Development
- **Actuator Node:** Fully designed, PCB routed, BOM generated; firmware written and electrically tested; first boards delivered
- **Battery Node:** Designed with iterations to handle wide input voltage range and ESC back-EMF; firmware under development
- Both nodes integrated and tested with SwiftCore autopilot on CAN bus

## Notable Details

### BST Commercial Success & Track Record
- **Founded:** 2011; entirely self-funded by commercial sales, consulting, and non-dilutive grants
- **Prior NASA SBIR Success:** Soil Moisture Mapping UAS project in CCRPP phase; earned $417,157 in non-NASA investment for commercialization
- **S2 Commercialization:** Selected for GSFC MALIBU project (3 completed campaigns, 2018 campaigns confirmed); JPL ELEVATE project (Costa Rica trace gas sampling)
- **FAA/NASA Flight Heritage:** Successfully completed AFSRB and FRRB reviews 7 times in prior 3 years; secured FAA flight permits
- **S1 Market Position:** Independently verified as best-performing commercial UAS for 3D photogrammetry/orthomosaics

### Competitive Advantages
1. **Distributed Modular Architecture:** Allows iterative implementation; third-party UAS integration without BST avionics
2. **Open Standards:** UAVCAN protocol enables ecosystem beyond BST systems
3. **Mature Codebase:** Leveraging SwiftCore FMS distributed architecture and existing machine learning work (event detection already in commercial products)
4. **Proven ML Approach:** Phase I results show algorithms find failure patterns without explicit programming
5. **Comprehensive Failure Database:** 6+ years of BST internal data + FAA database for training
6. **Published Data Format:** Portal tools available to non-BST systems; expands market and improves algorithms

### Phase II Technical Objectives Summary
1. Finalize/validate actuator node, battery node, vision node, flight management node designs
2. Design, train, validate machine learning algorithms for all identified failure modes
3. Bench-top testing and hardware-in-the-loop simulation for training data, sensor validation, bandwidth verification
4. Implement intuitive operator alerts (informed by manned aircraft standards)
5. Deploy customer-facing online portal for iterative algorithm improvement
6. Flight test full system on S2 with designed failures to validate reliability metrics

### Risk Mitigation
- **Icing Detection Risk:** Getting NASA AFSRB approval for icing flight experiments is identified as major risk; backup plan uses simulation environment
- **Vision Algorithm Complexity:** Preliminary Phase I work completed to reduce Phase II integration risk
- **Hardware Schedules:** PCB designs completed in Phase I to manage lead times

### Intellectual Property & Commercialization Strategy
- System designed for both on-board real-time operation and post-processing
- Commercial model: integrate into S1/S2 product lines, sell as retrofit to existing COTS systems, monetize customer portal
- Target customers: NASA, NOAA, commercial UAS operators with limited expertise requiring safer operations

### Relevant Prior Work Referenced
- Elston et al. 2013: Publish-subscribe UAS network with auto-capability detection (distributed architecture predecessor)
- Safe2Dtich project: Complementary emergency landing research
- Multi-AngLe Imaging BRDF UAS (MALIBU): Real-world validation platform
- ELEVATE: JPL collaboration for trace gas sensing

---

**Note:** Document appears complete in provided text, though Part 5 (Testing, Simulation, Validation) section is cut off mid-sentence. The proposal comprehensively addresses Phase II work plan (Part 4, sections 1.0-7.0) and detailed technical