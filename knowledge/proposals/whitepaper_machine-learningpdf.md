# Advanced Applications of Machine Learning for UAS

## Document Metadata
- Type: White Paper
- Client/Agency: NASA (SBIR program)
- Program/Solicitation: NASA Small Business Innovation Research (SBIR) Phase 2, Topic S3.04-8077
- Date: Published 2019 (created/modified dates in metadata: 2022-12-20 / 2020-10-25)
- BST Products/Systems Referenced: SwiftCore Avionics, SwiftPilot, SwiftTab, SwiftStation, S1, S2
- Key Personnel: Jack Elston (CEO), Maciej Stachura (CTO)

## Executive Summary
Black Swift Technologies proposes using machine learning algorithms to dramatically improve small UAS reliability by predicting critical maintenance needs and detecting hazardous faults in real-time. The system monitors subsystems (communications, propulsion, actuators, icing conditions) and provides autonomous diagnostics, addressing the fact that UAS failure rates are hundreds of times higher than manned aircraft, primarily due to lack of onboard monitoring and systematic maintenance protocols.

## Technical Approach

**Core Problem Addressed:**
- UAS failure rates occur at ~100-1000x the rate of general aviation aircraft
- Root causes: lack of onboard monitoring, no systematic maintenance protocols, absence of skilled pilot oversight
- Over 2/3 of failures are equipment-related rather than pilot error

**Machine Learning Solution:**
- Develop onboard algorithms to continuously monitor subsystem performance for faults and degradation
- Create predictive maintenance algorithms to identify component failures before they occur
- Implement distributed, modular avionics architecture with networked monitoring nodes
- Use SwiftCore avionics (designed entirely by BST) as the platform for machine learning deployment

**Specific Fault Detection Targets:**
1. Wireless communication subsystem failures (antenna selection, deployment errors)
2. Actuator and motor performance degradation (track efficiency over component lifetime)
3. Environmental hazards (icing detection via power requirements and vibration analysis)
4. Off-nominal performance indicators (general outlier detection)

**Data Sources & Validation:**
- Historic flight database from BST operations since 2011 (both internal and customer flights)
- Controlled laboratory tests on hardware (servos, motors, propellers)
- Simulation of failure modes (propeller damage, motor winding damage, ESC failures)

## Products & Capabilities Described

### SwiftCore Avionics System
**What it is:** End-to-end flight management system designed entirely by BST, including autopilot, ground station, user interface, and support electronics.

**Components:**
- **SwiftPilot Autopilot:** Advanced high-performance autopilot with dual 168 MHz Cortex-M4 CPUs (core processors) and optional 1 GHz Cortex-A8 payload processor; modularized CAN-bus architecture supporting UART, I2C, SPI, CAN, Ethernet, USB, GPIO
- **SwiftTab:** Android-based ground station tablet with intuitive flight planning interface, mid-flight plan modification capability, gesture-based controls
- **SwiftStation:** Tripod-mounted ground station with 900 MHz and GPS antennas, custom module expansion capability, multiple radio options

**Use in ML Context:** Modular, distributed avionics allows pairing of electronics with individual subsystems (servos, motors) for unique lifetime identification and tracking; robust CAN-bus network enables data exchange between monitoring nodes for vehicle-wide situational awareness.

### Machine Learning Algorithms (Developed/In Development)
- Real-time fault detection algorithms for icing, propeller damage, communications failures
- Preventative maintenance algorithms using clustering and support vector machines
- Efficiency curve modeling for propulsion system performance tracking
- Vibration analysis algorithms for propeller damage detection

## Use Cases & Applications

**Immediate Applications:**
1. **Beyond-line-of-sight (BLOS) operations** - Reliable autonomous operations without constant human oversight
2. **Flights over populated areas** - Ensuring safety through equipment redundancy and fault tolerance
3. **Fully autonomous operations** - Unmanned aircraft requiring self-diagnostics and maintenance prediction
4. **Commercial and scientific applications** - Enabling cost-effective UAS deployment

**Specific Problem Scenarios Addressed:**
- Communication losses due to antenna deployment errors
- Propeller damage from hard landings or debris strikes
- Wing icing in winter/high-altitude operations
- Servo and motor degradation over operational lifetime
- Battery health monitoring

## Key Results (Proof of Concept)

**Wireless Communication Subsystem:**
- Successfully identified historical instances of reduced comm performance (range <600m vs. 3km)
- Algorithms traced failures to correctable causes (antenna selection, ground station setup)

**Propulsion System Performance:**
- Detected aircraft icing through analysis of power requirements and efficiency curves
- Characterized normal vs. icing conditions on BST S1 and S2 aircraft

**Propeller Damage Testing:**
- Controlled propeller chipping tests showed:
  - 108% increase in vibration between undamaged and most-damaged propeller states
  - 5.9% reduction in propulsion efficiency with progressive damage
- Vibration metrics identified as strong automated detection indicators

**Servo Motor Bench Testing:**
- Over 3,000 combined hours of servo testing under representative loading
- Identified large variation between servos of same make/model (100% variation in current draw under similar loading)
- Demonstrated one servo steadily increasing current draw over 500+ hours (degradation tracking)

**Motor/ESC Testing:**
- Successfully differentiated motor efficiency curves for reversed propeller vs. normal operation
- Support vector machines identified as viable tool for in-family vs. out-of-family performance separation

**Online Portal Deployment:**
- Functional web interface for customers to upload flight logs
- Automated AI analysis running on all uploaded flights
- Geospatial analysis of communications performance (RSSI vs. GPS trajectory)
- Real-time flagging of off-nominal subsystem performance

## Notable Details

**Funding & Partnership:**
- NASA SBIR Phase 2 grant approved for total of $875K
- 1:1 matching opportunity for additional external funding
- Partnership with NASA and FAA critical for NAS integration efforts
- Delivery timeline: system to be provided to NASA within one year

**Commercialization Strategy:**
- Early validation through online portal (already operational)
- Gradual integration of onboard tracking components to BST aircraft and select customers
- Scalability to third-party aircraft/manufacturers via standardized interfaces and data formats
- Plans to publish standard data formats to enable third-party compatibility
- Modular avionics allow component sales to augment third-party UAS systems
- Revenue model: maintenance recommendation alerts with direct parts purchasing from integrated interface

**Competitive Advantages:**
- BST designs all critical flight management components in-house (unlike competitors using open-source avionics)
- Guarantees quality, robustness, and supply chain control
- Distributed modular avionics architecture enables fault isolation and scalability
- Couples avionics expertise with consulting services
- Access to proprietary flight database (2011-present) for algorithm training

**Technology Scope:**
- Addresses critical gap in NAS integration (reliability without skilled pilot)
- Positions BST to leverage broader industry opportunities (third-party UAS monitoring services)
- Enables low-cost, lightweight solutions aligned with economic viability goals
- Integration with COTS components allows rapid technology adaptation

**Key Personnel Background:**
- **Jack Elston (CEO):** Ph.D. from CU Boulder on complex meshed networks and control algorithms for in situ tornado sampling; technical lead on all BST avionics including SwiftCore autopilot system
- **Maciej Stachura (CTO):** M.S. and Ph.D. in aerospace engineering (CU Boulder); involved in 300+ flight experiments including VORTEX2 tornadic supercell intercept