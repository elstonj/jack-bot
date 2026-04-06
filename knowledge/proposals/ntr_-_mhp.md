# Multi-hole Probe (MHP)

## Document Metadata
- Type: New Technology Report (NTR)
- Client/Agency: NASA Jet Propulsion Laboratory (JPL)
- Program/Solicitation: 2016 SBIR Phase I, Topic S3.04-8077
- Contract Number: NNX16CP42P
- Date: December 2-7, 2016
- BST Products/Systems Referenced: S3 (Small UAS for Scientific Data Gathering in Harsh Environments)
- Key Personnel: Jack Elston (lead innovator, initial design/PCB/firmware), Maciej Stachura (mechanical design), Dave Pieri (NASA COTR)

## Executive Summary
Black Swift Technologies developed an improved, compact multi-hole probe for measuring 3D winds and static pressure from small unmanned aircraft systems (sUAS). Designed for harsh field environments, the device combines 5 pressure ports, custom sensor electronics, and 3D-printed construction to create a lightweight (62g), robust sensor package that integrates onto most sUAS platforms.

## Technical Approach

**Core Design:**
- Half-dome aerodynamic probe with 5 pressure ports
- Center port measures total pressure; 4 offset ports (45° spacing around hemisphere) measure angle of attack and sideslip
- All mechanical components 3D-printed to high accuracy for weight and cost reduction
- Custom-designed sensor board integrates all measurements

**Sensor Suite:**
- **Airspeed measurement:** Center hole total pressure vs. static pressure using SM9541 sensor (20cm H₂O version)
- **Angle of attack & sideslip:** Total pressure from center port compared to 4 offset ports using SM9541 sensors (10cm H₂O versions for increased resolution)
- **Static pressure, temperature, humidity:** MS5607 sensor integrated on custom board
- **Data interface:** CAN bus output for autopilot/on-board data logger integration

**Manufacturing & Assembly:**
- 3D printing enables rapid construction, low cost, and design flexibility
- Custom PCB board design with integrated sensor electronics
- Firmware developed for automated data collection

## Products & Capabilities Described

**Multi-hole Probe (MHP)**
- **What it is:** Compact aerodynamic probe for atmospheric measurement from sUAS
- **Specifications:**
  - Dimensions: 2" × 4"
  - Weight: 62g
  - Measures: 3D wind components (airspeed, angle of attack, sideslip), static pressure, temperature, humidity
  - Output: CAN bus interface
  - Sensors: 5× SM9541 dynamic pressure sensors (mixed 20cm and 10cm H₂O), 1× MS5607 (pressure/temperature/humidity)
- **Design advantages:**
  - Blunt profile minimizes protrusion from airframe (increases robustness vs. traditional probes)
  - 3D-printed construction (rapid manufacture, low replacement cost suitable for high-risk missions)
  - Extremely lightweight enables integration into most sUAS platforms
  - Simple design reduces cost and enables high-risk mission deployment

## Use Cases & Applications

**Primary Applications:**
- Volcanic plume sampling (NASA and federal agencies: NOAA, NSF)
- Weather modeling validation through 3D in situ atmospheric measurements (local and global scales)
- Small-scale dynamic phenomenon research
- Severe weather prediction (6-24 hour forecasting for convection-driven systems)

**Target Organizations:**
- University Corporation for Atmospheric Research (UCAR)
- National Center for Atmospheric Research (NCAR)
- Mesoscale Predictability Experiment (MPEX)
- iMET (existing commercial partnership for instrument integration)

## Development Timeline
- **01/01/2014:** Initial discussion and conceptual design
- **10/04/2014:** Circuit board design
- **11/10/2014:** Detailed 3D CAD design of scaffolding
- **11/25/2014:** Initial prototype construction and testing
- **12/01/2014:** Circuit board prototype completed
- **12/04/2014:** Complete 3D CAD design of sensor module
- **09/15/2016:** New 3D CAD design for 3D printing
- **10/01/2016:** Laser-cut parts ordered and assembled
- **10/20/2016:** Firmware and data collection code completed
- **12/02/2016:** Wind tunnel testing completed; comparison with commercial system performed

## Notable Details

**Competitive Advantages:**
- First commercial system combining compact weight, robustness, and full 3D wind measurement capability
- 3D printing enables rapid iteration and field-replaceable design
- Drastically lighter than traditional commercial multi-hole probes
- Blunt design eliminates external protrusions vulnerable to ground damage
- Cost reduction makes viable for high-loss-probability missions

**Technology Readiness Level:**
- State: Prototype, Modification, Used in Current Work
- Degree of Significance: Substantial Advancement in the Art
- Wind tunnel testing completed and validated against commercial baseline

**Commercialization Path:**
- Existing commercial interest from iMET for instrument integration
- Potential use by NASA, NOAA, NSF, and research institutions

**Supporting Documentation:**
- MS5607 pressure/temperature/humidity sensor datasheet
- SM9541 differential pressure sensor datasheet
- Circuit board schematic (report_mhp_circuit.png)
- Final probe design image (report_mhp_final.png)
- Integrated system image (report_mhp_integrated.png)