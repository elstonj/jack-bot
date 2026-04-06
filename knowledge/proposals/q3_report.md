# Improved UAS Robustness through Augmented Onboard Intelligence - Q3 Report

## Document Metadata
- Type: SBIR Phase II Quarterly Report #3
- Client/Agency: NASA
- Program/Solicitation: NASA SBIR 2017 Phase II; Contract No. 80NSSC18C0042
- Date: January 2019
- BST Products/Systems Referenced: S2 aircraft, SwiftCore, SwiftTab
- Key Personnel: Dr. Jack S. Elston (PI), Dr. Maciej Stachura (Machine Learning/Regulatory Expert), Dr. Dan Connors (Computer Vision Expert)

## Executive Summary
This Phase II effort aims to develop a highly capable onboard intelligence system with machine learning algorithms to detect early warnings and provide diagnostics of potential failures in critical UAS subsystems. The system comprises networked monitoring nodes (actuator, battery, vision, and flight management) designed to be small, lightweight, and low-power while providing the reliability necessary for safe NAS operations including beyond-line-of-sight and autonomous flights. Q3 work focused on customer portal development with new plotting and data conversion tools.

## Technical Approach

**Core System Architecture:**
- Decentralized networked monitoring nodes that cooperate with a centralized flight management node
- Uses CAN bus architecture and open-source UAVCAN protocol for inter-node communication
- Four types of specialized monitoring nodes: actuator, battery, vision, and flight management
- All nodes share common core architecture (SwiftCore-based firmware) with specialized IO and sensors
- Machine learning algorithms trained on historical flight data to detect off-nominal conditions

**Key Technical Components:**
1. **Actuator Monitoring Node** - Tracks servo/motor performance, detects failures before they occur
2. **Battery Monitoring Node** - Monitors charge state, balance, degradation; recommends maintenance
3. **Vision Node** - NVIDIA Jetson-based system for landing site selection and hazard detection
4. **Flight Management Node** - Centralized processing and decision-making hub

**Algorithms & Capabilities:**
- Wireless communication subsystem monitoring (antenna selection, ground station deployment)
- Propulsion system performance tracking (efficiency monitoring, payload weight detection)
- Environmental hazard detection (aircraft icing)
- Safe landing area detection from vision sensors
- Actuator health monitoring with predictive maintenance recommendations
- Integration with autopilot and operator interface for alerts and mitigation actions

**User Interface:**
- ECAM (Elektronically Centralized Aircraft Monitoring) system-based approach for pilot interface
- Simple framework for displaying maintenance instructions and fault resolution checklists
- Intuitive alert system designed to avoid overwhelming operators with information
- SwiftTab application integration for ground station display

**Customer Portal:**
- Online tool for post-flight analysis using same ML algorithms as onboard system
- Flight log upload capability for automated assessment
- Published data format to support third-party UAS systems
- Cloud-based architecture with multi-threaded implementation for scalability

## Products & Capabilities Described

### S2 Aircraft
- Past NASA SBIR-developed platform used for Phase II flight testing
- Proven platform for scientific campaigns in difficult/dangerous areas
- Used extensively for algorithm validation and reliability demonstrations

### SwiftCore
- Firmware codebase serving as foundation for all monitoring node firmware
- Handles sensor interfacing, non-volatile memory management, CAN bus communication
- Modular design enabling quick incorporation of new sensing capabilities

### SwiftTab
- Ground station application receiving updates to support new UI features
- Displays monitoring system alerts and maintenance recommendations
- Integrates with new communications protocol for subsystem status information

### Monitoring Nodes (Hardware Under Development)
- **Actuator Monitoring Node**: Interfaces with servo actuators, tracks control surface performance
- **Battery Monitoring Node**: Voltage, current, temperature monitoring; cycle tracking
- **Vision Node**: Camera interface, deep learning computation (Jetson platform), CAN integration
- **Flight Management Node**: Linux-based central processing, runs primary ML algorithms

## Use Cases & Applications

**NASA Applications:**
- Arctic operations (Sierra UAS heritage)
- Volcanic plume characterization (DragonEye heritage)
- Icing detection and mitigation in challenging environments
- Soil moisture mapping campaigns
- Enable operations in areas historically considered too risky
- Reduce training requirements for scientists to operate UAS directly

**Commercial Applications:**
- Survey and GIS operations with expensive sensors (GPS RTK, scanning LIDAR)
- Beyond-visual-line-of-sight (BVLOS) operations
- Fully autonomous operations without direct human oversight
- Maintenance schedule optimization for commercial operators
- Enable wider adoption by reducing failure rates and training requirements
- Support for future fully autonomous flights

**Specific Mission Scenarios:**
- Environmental hazard detection (icing, wind shear)
- Safe landing area identification for emergency situations
- Autonomous maintenance scheduling based on real-time health data
- Operations over populated areas with improved safety assurance

## Key Results (Q3 Focus)

**Customer Portal Development - Completed:**
1. **Plotting Tools**: Developed automated visualization tools extracting metrics from flight logs
   - Generates Google Maps overlays showing GPS track, payload triggers, waypoints
   - Drop-down menu for selecting data plots (air data, performance metrics, etc.)
   - Metrics extracted: POSIX timestamp, protocol revision, flight duration, hardware/software versions
   - User-interactive browser-based plot manipulation
   - Download capability for generating quick flight reports

2. **NetCDF Tools**: Developed software for data format conversion
   - Converts log parsing outputs to NetCDF format
   - Integration with Matlab for post-processing using validated historical tools
   - Enables use of BST's existing flight evaluation tools with current logs

3. **Database Development**: Design of customer database structure for storage of:
   - Customer details and metadata
   - Flight log files and hyperparameters
   - Integration of 6 years of historical BST flight data (Phase I database)

**Contract Status:**
- Total cumulative costs incurred (as of 1/12/19): $237,835
- Estimated physical completion: 37.5%
- Quarterly costs: Q1 $71,763.45, Q2 $84,555.13, Q3 $81,516.60

**Regulatory Progress:**
- Flight testing permission application status updated
- NASA AFSRB and FRR no longer required for gathering flight data per revised plan
- Streamlined approach to obtaining flight authorization

## Notable Details

**Phase I Accomplishments (Enabling Phase II):**
- Identified critical UAS failure modes and root causes through historical analysis
- Developed and validated machine learning algorithms for:
  - Wireless communication range tracking
  - Battery health classification and remaining flight time prediction
  - Motor failure detection and propulsion system health assessment
  - Actuator performance tracking
  - Launch system performance monitoring
- Successfully trained algorithms on 6+ years of historical flight data (since 2011)
- Early validation via alpha online portal showing practical algorithm value

**Key Innovation Points:**
1. **Failure Detection Examples from Phase I Data**: Algorithms automatically identified:
   - Antenna selection issues and ground station deployment problems affecting comm performance
   - Propulsion efficiency anomalies corresponding to payload weight changes
   - Performance consistency patterns enabling outlier detection without explicit fault definition

2. **Network Architecture Advantages:**
- Decentralized design allows iterative development and testing of subsystems
- Enables integration with third-party UAS not using BST avionics
- Facilitates both onboard real-time monitoring and post-flight analysis

3. **Commercialization Strategy:**
- Free online portal with published data format to support ecosystem adoption
- Incentivizes customers to upload flight data while growing training database
- Modular portal design allows easy addition of new algorithms and visualizations

**Regulatory & Safety Track Record:**
- BST has completed 7 AFSRB/FRRB reviews in past 3 years
- Established FAA flight permissions precedent for multiple complex UAS programs
- Expertise in safety case development for autonomous systems

**Team Expertise:**
- Dr. Elston: Principal Investigator, UAS systems expertise
- Dr. Stachura: Machine learning algorithms, regulatory compliance
- Dr. Connors: Computer vision, deep learning (contracted consultant)
- Support technicians for hardware validation and testing

**Work Schedule Status (Q3):**
- Scheduled for Q3: Actuator/battery monitoring algorithms, power system monitoring, landing site selection algorithm threading, web app implementation
- Completed ahead of schedule: Vision node design exploration, landing site algorithm exploration, customer database design
- Postponed to Q4: Bench testing of hardware failure modes (servos, batteries, ESC, motors, propellers)
- Next quarter focus: Algorithm training with new hardware, hardware-in-the-loop testing, bench testing, customer portal alpha testing with external users