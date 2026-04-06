# NTR Working Notes - S3 UAS Design Updates

## Document Metadata
- Type: Working notes / design documentation
- Client/Agency: NASA
- Program/Solicitation: 2016 SBIR (Volcano/CCRPP)
- Date: Working notes compiled by 2024; references milestones through May 2024
- BST Products/Systems Referenced: S2, S3 UAS
- Key Personnel: Daniel Prendergast (last editor)

## Executive Summary
These working notes document two major design updates to the S3 UAS airframe that reduce component complexity, improve controllability in extreme weather, and increase payload modularity. The redesign transitions from a 5-motor to a 3-motor system with thrust-vectoring front rotors, and separates avionics from the payload compartment to enable enhanced mission flexibility and extended endurance.

## Technical Approach

### Motor System Redesign (5 to 3 Motors)
- **Previous configuration**: Single pusher motor with 5-motor system
- **New configuration**: 3-motor system with two articulated (pivoting) front motors sized for vertical takeoff and one rear pusher motor
- **Key benefits**:
  - Lower component count reduces weight and complexity
  - Pivoting front rotors accommodate larger propeller for sufficient thrust on larger airframe
  - Enhanced yaw control via thrust vectoring (improvement over torque-based control in quad-lift frame)
  - Reduced high-power wiring by co-locating primary propulsion motors at battery packs
  - Motor pylons serve as heatsinks for high-power ESCs

### Power System Architecture
- **Transition to dual-battery configuration** (departure from BST's traditional lower-voltage, single-battery approach)
- **Design goal**: Space efficiency and redundancy
- **Emergency capability**: Aircraft can operate on single battery if one fails in flight
- **Battery balancing**: Automatic draw management to prevent unequal depletion
- **Custom PCB design** with two boards:
  1. "Supply board": Takes input from battery or centralized bus, outputs to ESC, can output power to central bus
  2. "Distribution board": Manages connections to supply boards, provides redundant power to avionics, secondary avionics, and payload

### Airframe and Payload Separation
- **Original design**: All components (battery, payload, motor, avionics) integrated into single fuselage structure
- **New design**: Elimination of traditional fuselage; replacement with **modular payload mounting pylon**
- **Avionics relocation**: Moved from payload compartment to wing pockets
- **Payload flexibility**: Allows standard S2-style payloads and smaller-diameter/shorter payloads for reduced mass and drag
- **Result**: Extended mission endurance and range

## Products & Capabilities Described

### S3 UAS (Small Uncrewed Aircraft System)
- **What it is**: Long-duration uncrewed aerial platform designed for operation in extreme environments
- **Design features**:
  - Aerodynamic and structural elements for high winds, precipitation, and icing
  - All-weather operational capability (strong winds, rain, snow, icing, smoke, volcanic plumes, particulates)
  - Modular payload mounting system with standardized interface
  - Dual-battery redundancy architecture
  - Thrust-vectoring propulsion for enhanced control in high moment-of-inertia yaw conditions
- **Design evolution documented**: May 2023 (initial concept) → Dec 2023 (CAD airframe) → Feb 2024 (avionics separation CAD) → May 2024 (initial hover test)
- **Payload capacity**: Maintains compatibility with S2-style payloads; can accommodate smaller specialized payloads

### S2 UAS
- Referenced as legacy system with compatible payload form factors
- S3 maintains backward compatibility with S2-style payloads

## Use Cases & Applications

### Current Primary Applications
- **Volcano monitoring**: Primary NASA/earth science application
- **Satellite calibration**: In-situ validation of satellite data

### Current Secondary Applications
- **Methane leak detection**: Pipeline monitoring for oil and gas infrastructure; BST already partnered with sensor company for this service

### Potential Future Applications
- Atmospheric data collection at high latitudes
- DoD intelligence, surveillance, and reconnaissance (ISR)
- Oil and gas industry gas sensing operations

### Environmental Conditions Addressed
- Volcanic plume sampling (ash, sulfur dioxide, particulates)
- Wildfire operations (smoke-laden atmospheres)
- Severe storm environments
- High-latitude atmospheric research

## Key Design Innovations

1. **Thrust Vectoring for Yaw Control**: Pivoting front motors provide superior yaw control compared to torque-based quad-lift frame, particularly important for fixed-wing aircraft with high yaw moment of inertia

2. **Modular Payload Pylon**: Replaces traditional fuselage; accommodates variable payload sizes/shapes/mounting styles while reducing overall mass and drag

3. **Distributed Power Architecture**: Multiple battery packs with redundancy instead of single large battery; improved transportation and operational safety

4. **Avionics-Payload Separation**: Eliminates design conflicts; enables independent optimization of payload compartment and flight systems

5. **Component Count Reduction**: Fewer motors and simplified electrical architecture reduce weight and improve reliability

## Deliverables
1. Four quarterly reports detailing updated S3 UAS design
2. New Technology Report (NTR) describing updated design and benefits

## Key Strategic Partners & Future Opportunities
- **Federal agencies**: NASA, NOAA, USGS (earth, atmospheric, environmental research)
- **Commercial**: Oil and gas industry (existing sensor partnerships for methane detection)
- **Current sensor partner**: BST already leveraging third-party sensor integration for methane applications

## Notable Details
- Document references figures (Figures 2-5, 36, 42) not included in this text
- Design focused on expanding operational envelope for "some of the most difficult environments on Earth"
- Emphasis on in-situ data collection to validate atmospheric models critical for human safety
- Positioning as alternative/complement to satellites (which suffer from infrequent coverage, cloud masking, resolution limits), ground systems, crewed aircraft, and balloons