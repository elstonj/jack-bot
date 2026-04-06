# Improved UAS Robustness through Augmented Onboard Intelligence

## Document Metadata
- **Type:** Phase II SBIR Proposal
- **Client/Agency:** NASA
- **Program/Solicitation:** NASA SBIR 2017, Subtopic A1.09 "Vehicle Safety - Internal Situational Awareness and Response"
- **Date:** 2017 (Phase II proposal following Phase I completion)
- **Proposal Number:** A1.09-8639
- **BST Products/Systems Referenced:** S2 aircraft, S1 aircraft, SwiftCore Flight Management System (FMS)
- **Key Personnel:** Not explicitly named in provided text; mentions collaboration with NASA technical monitor Ricardo Arteaga

## Executive Summary

Black Swift Technologies proposes a Phase II effort to develop an onboard intelligence system for small unmanned aircraft systems (UAS) using networked monitoring nodes and machine learning algorithms to detect subsystem failures, provide early fault warnings, and enable automated diagnostics. The system will monitor critical UAS subsystems (communications, propulsion, actuators, battery, landing detection) and integrate with both BST and third-party UAS via a CAN/UAVCAN network architecture. Phase I successfully validated the approach through algorithm development and testing on BST's flight database spanning 2011-present, demonstrating feasibility for commercial implementation.

## Technical Approach

### Core Architecture
- **Decentralized monitoring nodes** with a **centralized flight management node** communicating via CAN bus using the open-source UAVCAN protocol
- Four distinct node types: actuator node, battery node, vision node, and flight management node
- Each node shares a common core architecture (ARM microcontroller, persistent storage, CAN interface) with specialized I/O and sensors
- Total onboard data requirement: ~13 kB/s for full S2 installation with 6 actuator nodes, 1 battery node, 1 vision node, and central management node

### Hardware Implementation
- **Actuator Node** (completed Phase I): Tracks servo performance via A/D converters measuring voltage, current, temperature; includes serial interface for smart servo telemetry
- **Battery Node** (completed Phase I): Monitors battery regression, tracks propulsion performance data; employs redundant power supply for mission-critical systems
- **Vision Node** (Phase II design): NVIDIA Tegra-based single-board computer for machine vision and onboard vision-based fault detection
- **Flight Management Node** (Phase II design): NVIDIA Tegra ecosystem for GPU-accelerated machine learning on system-level monitoring algorithms
- Nodes use CAN bus backbone with UAVCAN protocol for inter-node and autopilot communication

### Machine Learning Algorithms
Algorithms designed during Phase I (trained on BST's flight database with failures identified):
1. **Wireless Communication Subsystem:** Regression (Unscented Kalman Filter) + classification to detect reduced comm performance, antenna configuration errors
2. **Battery/Propulsion System:** Regression algorithm to track remaining flight time and classify battery health; classification to detect motor failures and propulsion degradation
3. **Propulsion System Efficiency Tracking:** Monitors efficiency ratio between electrical input power and aerodynamic output; identifies damage (propeller, motor) and aircraft icing; corrects for aerodynamic effects (temperature, pressure, density altitude, aircraft mass)
4. **Actuator Performance:** Tracking of control surface actuator degradation
5. **Vision-Based Safe Landing Detection:** Deep learning (Caffe framework trained on NVIDIA Tesla K40 GPU) to classify landing hazards (trees, bushes, obstacles); identifies clear landing areas of required length (~30m for S1 aircraft)

**Phase I Algorithm Performance Examples:**
- Engine failure detection: 97.3% accuracy on 1 second of data, 100% on 3 seconds (AdaBoost with binary decision tree classifiers)
- Propulsion efficiency tracking: Consistent efficiency profiles across similar configurations; identified outliers (heavier payloads, configuration changes)

### Network & Integration
- **CAN bus protocol**: Industry-proven in aerospace and automotive; basis for UAVCAN implementation
- **UAVCAN advantages**: Message definition scheme, larger message type support, redundant bus architecture, remote firmware updates, open-source for third-party system integration
- System designed to integrate with both BST-equipped and third-party UAS with minimal impact to aircraft performance

## Products & Capabilities Described

### S2 Aircraft
- **What it is:** A fixed-wing research UAS developed under previous NASA SBIR (Soil Moisture Mapping)
- **Use in this context:** Platform for extensive Phase II flight testing of the proposed monitoring and diagnostics system; has proven successful in scientific campaigns including MALIBU (GSFC) and ELEVATE (JPL) projects
- **Specifications:** Requires ~30m landing distance

### S1 Aircraft
- **What it is:** Commercial surveying UAS
- **Use in this context:** Independently verified as one of best-performing UAS for 3D photogrammetry; platform used for vision algorithm training with rural area flight data (2016 Oklahoma flight over 1km x 1km areas)
- **Performance:** Leverages advanced payload integration lessons from NASA/NOAA work

### SwiftCore Flight Management System (FMS)
- **What it is:** Commercial autopilot system from BST
- **Specifications:** Modular design with CAN bus backbone; allows addition/subtraction of sensors, actuators, payloads without full redesign
- **Integration:** Central node in monitoring system; receives fault messages and hyperparameters from monitoring nodes; communicates through CAN bus

## Use Cases & Applications

### Primary Mission Applications
1. **Beyond-line-of-sight operations:** Requires improved reliability and autonomous fault detection
2. **Flights over populated areas:** Demands higher safety standards through onboard diagnostics
3. **Fully autonomous operations without direct human oversight:** Necessitates system robustness approaching manned aircraft reliability

### Specific Failure Mitigation Scenarios
- **Lost Communication Events:** Real-time detection of reduced comm performance; operator checklists for diagnosis and correction
- **Propulsion System Degradation:** Early warning of motor damage, propeller damage, or aircraft icing before catastrophic failure
- **Aircraft Icing Detection:** Monitors performance degradation caused by ice accumulation; enables operator decision-making on emergency return vs. climb-above-clouds mitigation
- **Emergency Landing:** Machine vision system guides aircraft to safe landing area when primary landing site is unavailable
- **Actuator/Servo Failures:** Tracks performance degradation and recommends maintenance/replacement before failure
- **Payload Sensor Failures:** Detects non-functional payload sensors during mission

### Commercial & Scientific Applications
- Soil moisture mapping operations (ongoing CCRPP SBIR)
- Multi-angle imaging and spectral analysis (MALIBU/GSFC project - 3 completed flight campaigns, winter/spring 2018 confirmed)
- Trace gas detection operations (ELEVATE/JPL project in Costa Rica)
- Commercial surveying and 3D photogrammetry
- Non-NASA commercial operations by companies with limited UAS expertise

## Key Results (Phase I)

### Failure Rate Analysis
Compiled from BST flight database (2011-present) and validated against FAA incident/accident database:
- **Overall Success Rate:** 80.4%
- **Partial Failures:** 15.2% (re-fly required or prevents next mission but not catastrophic)
- **Catastrophic Failures:** 3.8% (crash, fly-away, total loss)

**Failure Breakdown:**
- Lost Communication: 4.4%
- Payload Failure: 3.2%
- Landing Failure: 2.2%
- GPS Outage: 1.9%
- Loss of Propulsion Power: 1.9%
- Inflight Airframe Failure: 1.3%
- Launch Failure: 1.3%
- Inclement Weather: 0.6%
- User Error: 0.6%
- Loss of Onboard Power: 0.6%

**FAA vs. BST Comparison:**
- BST Equipment Failures: 69.0% (FAA: 79.8%)
- BST Pilot Error: 31.0% (FAA: 19.5%)

### Algorithm Validation Results

**Communication System Algorithm:**
- Successfully identified root causes of reduced comm performance in past flights (incorrect antenna selection, ground station antenna deployment failures)
- Demonstrated both regression (path loss model prediction) and classification (good/bad comm thresholds) capabilities

**Propulsion System Engine Failure Detection:**
- AdaBoost classifier with decision tree components
- Feature vectors: throttle setting, airspeed, altitude rate, acceleration
- 97.3% accuracy on 1-second data windows; 100% on 3-second windows
- Decision boundary shows expected relationship: engine-out conditions produce full throttle with energy loss (descent)

**Propulsion Efficiency Tracking:**
- Consistent efficiency profiles across similar aircraft configurations when corrected for aerodynamic effects
- Successfully identified outlier flight caused by heavier payload/battery (5.5 lbs → 6.5 lbs); efficiency normalized after mass correction and induced drag accounting
- Demonstrated ability to detect performance degradation independent of exact vehicle models

**Machine Vision Safe Landing Detection:**
- Trained Caffe deep learning model on training data from BST flight photos
- Successfully classified trees and bushes as landing hazards
- Tested on 2 rural images (~176m × 117m footprints) from August 2016 Oklahoma flight
- Identified clear landing gaps meeting 30m requirement for S1 aircraft in both field and road-adjacent scenarios

### Hardware Development
- **Actuator Node:** Designed, built, and electrically tested in Phase I
- **Battery Node:** Designed, built, with multiple iterations required for wide input voltage ranges and ESC back-EMF handling; actively being tested for incorporation into current BST product lineup
- Both boards scheduled for flight testing between Phase I and Phase II

### Portal & Algorithm Tool
- BST built **alpha version online portal** where customers upload flight data
- Automatic assessment provided for: communication system performance, propulsion system performance, and fault detection
- Demonstrates commercial viability and customer adoption potential

## Notable Details

### Competitive Advantages & Innovation
- **First active part tracking system:** Team unaware of any prior attempt at active part tracking/monitoring for small UAS; proposed "smart battery" concept pairs monitoring nodes with components for usage history and failure statistics
- **Heritage capability:** BST currently uses machine learning in commercial systems for event classification (launch/landing detection); this extends approach to complex failure prediction
- **Vehicle and avionics-agnostic solution:** Can be deployed on most COTS UAS with minimal performance impact; generalizable beyond BST platforms

### BST Track Record & Commercialization Success
- **Company history:** Self-funded since 2011 by commercial sales, consulting, development contracts, and non-dilutive grants
- **Soil Moisture Mapping SBIR:** Currently in CCRPP phase; earned **$417,157 in non-NASA investment** for commercialization
- **S2 aircraft commercialization:** Developed under Soil Moisture Mapping SBIR; successfully used on MALIBU (GSFC) with 3 completed campaigns and additional winter/spring 2018 campaigns confirmed; longer-term JPL collaboration on MALIBU commercialization
- **S1 commercial success:** Independently verified as one of best-performing UAS for 3D photogrammetry; competitive advantage from tight sensor-autopilot integration enabling superior accuracy
- **SwiftCore FMS:** Commercial autopilot product with proven modular architecture and CAN bus heritage

### Regulatory & Safety Capability Demonstration
- **FAA flight permissions:** Secured for previous NASA Soil Moisture Mapping Phase II and Phase II-E SBIR efforts
- **AFSRB/FRRB experience:** Successfully completed NASA Airworthiness Flight Safety Review Boards and Flight Readiness Review Boards 7 times in previous 3 years
- **Status:** Leading NASA partner for UAS development and flight testing

### Phase II Technical Objectives
1. Finalize design of actuator, battery, vision, and flight management monitoring nodes
2. Iterative design and testing of ML algorithms for failure detection, maintenance diagnostics, and safe landing detection
3. Bench-top testing and hardware-in-the-loop simulation to gather training data
4. UI implementation for intuitive operator alerts (standards-based on manned aircraft concepts)
5. Customer-facing online portal deployment for algorithm testing/deployment and data from third-party platforms
6. Full system flight validation on S2 aircraft with reliability metrics analysis

### Network Protocol Selection Rationale
Selected UAVCAN over BST proprietary CAN protocol for Phase II because:
1. Message definition scheme simplifies custom message format creation
2. Better support for larger message types
3. Redundant bus architecture support (critical for reducing failures)