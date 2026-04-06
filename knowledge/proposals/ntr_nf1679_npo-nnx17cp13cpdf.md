# Multi-hole Probe (MHP)

## Document Metadata
- Type: NASA Form 1679 - Disclosure of Invention and New Technology
- Client/Agency: NASA
- Program/Solicitation: SBIR Phase II (NASA CASE NO. NPO-NNX17CP13C)
- Date: 2018-08-06 (filed); developed 2014-2018
- BST Products/Systems Referenced: Multi-hole Probe (MHP)
- Key Personnel: Jack Elston (CEO, innovator), Maciej Stachura (CTO, innovator)

## Executive Summary
This disclosure presents an improved design of a multi-hole probe for measuring 3D winds and static pressure from small unmanned aircraft systems (sUAS). The compact, lightweight, 3D-printed sensor suite represents a significant advancement over commercial alternatives, enabling deployment on high-risk missions with minimal replacement cost while maintaining accuracy and robustness.

## Technical Approach

**Design Philosophy:**
- Compact, lightweight design specifically engineered for sUAS integration
- Leverages 3D printing technology for rapid, low-cost manufacturing with high accuracy
- Emphasis on simplicity to reduce cost and enable use in high-risk missions

**Sensor Configuration:**
- Half-dome design with 5 pressure ports
- Center port measures total pressure (airspeed)
- 4 offset ports (45° spacing around hemisphere) measure angle of attack and sideslip angle
- Static pressure measured by comparing center hole total pressure with static pressure reference

**Key Components:**
- 20 cm H₂O version of SM9541 differential pressure sensor (airspeed measurement)
- Multiple 10 cm H₂O versions of SM9541 sensors (increased resolution for angle of attack/sideslip)
- MS5607 sensor (static pressure, temperature, humidity with high resolution)
- Custom-designed sensor board with 5 dynamic pressure sensors
- Custom electronics with CAN bus interface for autopilot/data logger integration
- 3D-printed mechanical assembly

## Products & Capabilities Described

**Multi-hole Probe (MHP)**

*Specifications:*
- Physical dimensions: 2 × 4 inches
- Weight: 62 grams
- Measures: 3D wind components (airspeed, angle of attack, sideslip), static pressure, temperature, humidity
- Interface: CAN bus output
- Design approach: Fully 3D-printed body; blunt, non-protruding design

*Key Advantages:*
- Extremely lightweight (62g) enables integration into most sUAS platforms
- Compact profile minimizes aerodynamic disruption and ground-handling damage risk
- 3D printing enables rapid design iteration and customization for different installation requirements
- Robust design reduces risk of sensor damage during field operations
- Low manufacturing cost allows deployment on expendable sUAS assets
- Combines all sensor measurements in a single integrated package

*Performance Claims:*
- Wind tunnel tested and validated against commercial systems (December 2016)
- High-resolution measurements suitable for atmospheric model validation

## Use Cases & Applications

**Primary Applications:**
- Atmospheric science research and weather modeling (local and global scale)
- Validation of dynamic small-scale atmospheric phenomena models
- Volcanic plume sampling and remote characterization
- Severe weather prediction improvement (6-24 hour forecasts for convection-driven systems)
- Federal agency operations (NASA, NOAA, NSF)

**Research Initiatives:**
- Mesoscale Predictability Experiment (MPEX) - improving numerical weather prediction
- High-altitude atmospheric sampling missions
- ISARRA mission demonstration (July 2018)

**Current/Potential Customers:**
- NOAA (1 unit in use; 3 additional units planned for purchase)
- University of Colorado (1 unit sold)
- UCAR/NCAR
- University research institutions

## Development Timeline

- **01/2014:** Initial discussion and conceptual design
- **10/2014:** Circuit board design; first written description
- **11/2014:** Detailed 3D CAD design of scaffolding; initial prototype construction and testing
- **12/2014:** Circuit board prototype completed; complete sensor module CAD design finalized
- **09/2016:** New 3D CAD design for 3D printing completed
- **10/2016:** Laser-cut parts ordered, assembled, and first model completed
- **10/2020:** Firmware and data collection code written
- **12/2016:** Wind tunnel testing completed; first successful operational test; disclosure to University of Colorado
- **07/2018:** ISARRA mission demonstration

## Notable Details

**Innovation Classification:**
- Modification to existing technology (not a substantial advancement or major breakthrough)
- State of development: Modification/Production Model

**Prior Art Context:**
Commercial multi-hole probes exist but typically suffer from:
- Excessive weight
- Protruding design reducing robustness
- Limited compactness for sUAS integration
- Higher cost

The BST design is described as the first commercial system combining all sensor measurements in as light and compact a package while leveraging 3D printing technology.

**Intellectual Property:**
- Patent status not indicated in this disclosure
- No software patent questions applicable (hardware innovation)

**Commercialization Status:**
- Demonstrated commercial traction with early sales (University of Colorado, NOAA)
- NOAA contract for additional units represents sustained government interest
- Product ready for deployment in operational research missions

**Key Innovator Contributions:**
- Jack Elston: Initial design, PCB assembly, firmware
- Maciej Stachura: Mechanical design