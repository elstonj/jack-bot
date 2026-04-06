# Battery Monitoring Node

## Document Metadata
- Type: New Technology Report (NTR)
- Client/Agency: NASA Armstrong
- Program/Solicitation: NASA 2017 SBIR Phase I; Topic A1.09-8639 "Improved UAS Robustness through Augmented Onboard Intelligence"
- Contract Number: NNX17CD08P
- Date: Submitted December 2017 (created 2017-12-06, modified 2017-12-08)
- BST Products/Systems Referenced: Battery monitoring node (component of distributed onboard monitoring system for small UAS)
- Key Personnel: Jack Elston (lead innovator, initial design/PCB/firmware), Maciej Stachura (mechanical design); NASA COTR: Ricardo Arteaga

## Executive Summary
BST developed a standalone circuit board that monitors the health and status of batteries on small unmanned aircraft systems (UAS). The battery monitoring node interfaces with onboard power systems and is part of a larger distributed monitoring network that provides health diagnostics and off-nominal condition alerts to both the autopilot and operator, reducing mission failure risk.

## Technical Approach
The battery monitoring node is a circuit board with the following components and features:

**Hardware:**
- ARM microcontroller (highly capable)
- Persistent onboard storage
- Input voltage protection
- CAN bus interface
- Redundant 5V to 8.4V selectable power supply with automatic failover to backup regulator
- UART interface for smart battery system telemetry

**Software/Algorithms:**
- Onboard machine learning algorithm for battery tracking
- Monitors voltage, current, and temperature in real time
- Logs battery usage and overall capacity per flight
- Calculates remaining flight time
- Recommends battery replacement when total capacity drops below threshold

**Design Characteristics:**
- Compact size and low power consumption to minimize weight penalty on small UAS
- Part of a networked CAN bus-based distributed monitoring system
- Communicates health status to autopilot and operator

## Products & Capabilities Described

**Battery Monitoring Node**
- What it is: A standalone circuit board that interfaces with and monitors UAS battery systems
- How proposed to be used: As part of a distributed onboard monitoring network for small UAS to detect off-nominal conditions and provide maintenance recommendations
- Key specifications:
  - 5V to 8.4V selectable power output
  - ARM microcontroller-based
  - CAN bus compatible
  - Machine learning-based battery health algorithm
  - Automatic backup power regulator switching
  - Flight-by-flight battery capacity logging

## Use Cases & Applications
- Small UAS operational reliability and robustness
- Onboard health and diagnostic monitoring for unmanned aircraft
- Battery state-of-health tracking and predictive maintenance
- Risk mitigation for mission failure due to battery discharge or damage
- Reducing barriers to entry and increasing confidence in UAS technology for broader market adoption

## Development Timeline
- June 10, 2017: Initial discussion and conceptual design
- July 28, 2017: Circuit board design completed
- August 29, 2017: First board prototype received
- September 3, 2017: Testing and design iteration
- October 25, 2017: Final prototype design received

## Technology Readiness
- State of Development: Prototype (completed) and used in current work
- Degree of Technical Significance: Substantial Advancement in the Art
- Patent Status: No patents or patent applications listed

## Notable Details
- Redundant power supply with automatic failover is a key differentiator—ensures continued operation even if primary regulator fails
- Onboard logging enables accurate battery health tracking across multiple flight cycles
- System designed to lower barrier to entry for UAS operations by mitigating battery-related failure risks
- Part of broader "augmented onboard intelligence" approach to UAS robustness
- Small form factor and low power consumption critical for integration across distributed monitoring architecture without adding significant weight
- Supporting documentation includes battery.png and supplyRevA4.pdf (supply board schematic or design)