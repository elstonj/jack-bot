# Improved UAS Robustness through Augmented Onboard Intelligence

## Document Metadata
- **Type:** Phase II-E Statement of Work (SBIR proposal)
- **Client/Agency:** NASA
- **Program/Solicitation:** NASA SBIR, Topic A1.09-8639
- **Date:** Not explicitly stated (Phase II-E follow-on to Phase I work)
- **BST Products/Systems Referenced:** S2 UAS, S1 UAS, SwiftCore Flight Management System, SwiftTab operator interface
- **Key Personnel:** Dr. Dan Connors (subcontractor - computer vision and machine learning expert)

## Executive Summary
BST proposes to develop an onboard intelligence system for small UAS that provides early fault detection and self-diagnostic capability through machine learning algorithms. Phase II work will integrate this monitoring system with the S2 UAS platform, train and validate detection algorithms for common failure modes, and deploy a commercial web-based portal for post-processing analysis and algorithm iteration.

## Technical Approach

### System Architecture
The monitoring system is built on a distributed, modular architecture with three main components:

1. **Monitoring Nodes**: Modular hardware based on a consistent core design that can be adapted for different subsystems
   - Firmware based on SwiftCore Flight Management System libraries
   - Support for multiple sensor types and CAN bus integration
   - UAVCAN protocol for hyperpameter dissemination, synchronized timing, and firmware updates

2. **Flight Management Node**: Central processing hub composed of:
   - Modified monitoring node for CAN bus communication
   - Nvidia Jetson X2 board (Tegra-based GPU) for computationally heavy machine learning and system management
   - Repository for flight data and hyperparameters

3. **Subsystem-Specific Nodes**:
   - Actuator monitoring node (servo performance tracking)
   - Battery monitoring node (capacity and health tracking)
   - Vision node (for safe landing area detection)

### Extensibility
- Components designed to integrate with non-BST UAS systems
- Web-based portal for post-processing analysis of user-supplied flight log files
- Support for multiple UAS platforms through standardized log file formats

## Products & Capabilities Described

### S2 UAS
- Primary platform for Phase II integration and validation
- Proven system for scientific campaigns in difficult/dangerous environments
- Will undergo flight testing with designed failure scenarios

### SwiftCore Flight Management System
- Distributed system with robust library infrastructure
- Already-proven architecture that will underpin the new monitoring firmware
- Provides baseline sensor interfacing and communication protocols

### SwiftTab Operator Interface
- Tablet-based ground control station supporting multiple simultaneous operators
- Will be enhanced with ECAM-style (Electronic Centralized Aircraft Monitoring) UI components
- Supports role specialization: pilot monitor, science payload lead, triage operator
- Designed to scale for multi-vehicle operations

### Web-Based Customer Portal
- Cloud-hosted application for log file upload and analysis
- Runs diagnostic algorithms on user-supplied flight data
- Will display fault detection results in similar format to SwiftTab UI
- User account management with secure HTTPS authentication
- Allows algorithm iteration and improvement using customer flight data
- Potential expansion to support third-party UAS platforms through standardized log formats

## Use Cases & Applications

### Failure Detection and Mitigation
The system targets early detection of common small UAS failures:

1. **Lost Communication**: Predict maximum communication range by fitting RSSI signal strength vs. range; alert operator when approaching limits
2. **Battery Failure**: Track remaining capacity adjusted for temperature; predict remaining flight time; identify degraded batteries requiring replacement
3. **Propulsion System Loss**: Classify complete motor failure vs. degradation using AdaBoost with binary decision trees
4. **Propulsion Degradation**: Detect performance loss from motor/propeller damage or icing through efficiency regression and vibration analysis
5. **Launcher Performance**: Monitor energy delivery degradation during launch phase (for pneumatic launcher)
6. **Actuator/Servo Degradation**: Track servo performance over lifetime; enable preventative maintenance alerts; ground-based pre-flight assessment
7. **Inflight Autopilot Reboot Recovery**: Detect whether aircraft is flying on system bootup to enable safe power recovery in flight
8. **Safe Landing Area Detection**: Computer vision algorithms to identify safe landing zones when propulsion lost, GPS fails, or user error occurs

### Environmental Operations
- Arctic operations (extended endurance)
- Icing encounters (clear, rime, and mixed icing classification)
- Rural and developed area operations
- Seasonal variations (snow-covered terrain scenarios)

### Reliability Goals
- Target: 1 catastrophic failure per 200 flights
- Target: 1 partial failure per 50 flights

## Key Technical Objectives (Phase II)

1. **Subsystem Design & Validation**: Finalize hardware for actuator monitoring, battery monitoring, vision node, and centralized flight management node

2. **Algorithm Development & Training**: Iterative design and flight validation of 8 machine learning algorithms plus vision-based landing detection

3. **Testing & Validation Strategy**:
   - **Bench-top Testing**: Servo degradation (3 servos to failure), battery cycling to <60% capacity, damaged motor/propeller testing
   - **Hardware-in-the-Loop Simulation**: Inflight reboot scenarios, propulsion degradation (icing simulation via drag increase)
   - **Flight Experiments**: Servo validation, battery testing (3 flights using >50% capacity), damaged propeller flights (3 tests), autopilot reboot recovery, icing flights (if approved), safe landing site selection tests

4. **Operator Interface**: ECAM-style UI components for SwiftTab; intuitive alerts about subsystem failures and maintenance needs; generic card interface for failure resolution procedures

5. **Customer Portal**: Upload flight logs, run algorithms on user data, display results, user account management, secure hosting with scalability

6. **Flight Validation**: Full system testing on S2 with measured reliability metrics

## Risk Identification and Mitigation

**Primary Risk: Flight Testing with Fault Injection**
- Mitigation: Use separate redundant avionics for aircraft control while injecting faults into test system; high-fidelity HWIL simulation as alternative for risky scenarios
- BST has track record of successful NASA-approved flights; materials already adopted by GSFC as template

**Vision System Scope Risk**
- Mitigation: Brought in computer vision expert (Dr. Dan Connors) familiar with Nvidia Tegra platform

**Algorithm Implementation Risk**
- Mitigation: Subcontractor also versed in machine learning for troubleshooting

**Flight Permission Risk** (for icing and reboot tests)
- Mitigation: X-Plane simulation models of S1 and S2 aircraft available as backup data sources

## Notable Details

- **Manned Aviation Standards**: UI design based on ECAM systems proven in commercial aviation, enabling rapid adoption by pilots familiar with manned aircraft
- **Multi-operator Architecture**: SwiftTab supports multiple simultaneous operators with role specialization, positioned for scaling to multi-vehicle control with single pilot-in-command
- **Data Collection Strategy**: Web portal designed to incentivize customer uploads for continuous algorithm improvement
- **Icing Classification**: Detailed temperature-based categorization (Clear: -2 to -10°C; Mixed: -10 to -15°C; Rime: -15 to -20°C)
- **Launcher Integration**: Concurrent NASA project developing pneumatic launcher; S2 launcher data will be available for algorithm training
- **Legacy Platform Support**: Phase I used S1 aircraft data for vision algorithm training; results shown in orthomosaic markup examples
- **Modular Design Philosophy**: All components kept general enough for integration with non-BST UAS systems and third-party platforms

---

**Document Classification:** Proprietary and Confidential - NASA SBIR Review Purposes Only