# WWF Proposal

## Document Metadata
- Type: Proposal/Application
- Client/Agency: World Wildlife Fund (WWF)
- Program/Solicitation: WWF Wildlife Crime Technology Project
- Date: Submitted June 2, 2013 (created); last modified January 10, 2017
- BST Products/Systems Referenced: SwiftSentinel, SwiftPilot (autopilot), SwiftStation (ground control station), SwiftTab (user interface tablet)
- Key Personnel: Jack Elston (President/Co-founder, Support Engineer), Oier Penagaricano-Munoa (Project Manager), Raymond Oung (Lead Engineer), Maciej Stachura (Support Engineer/CTO), Coby Leuschke (Training Lead, Rocketship Systems President), Moses Gichanga (Maintenance Lead, ASR CEO), Lian Pin Koh (Advisor/Training Coordinator, Conservation Drones), Serge Wich (Advisor/Training Coordinator, Conservation Drones)

## Executive Summary
Black Swift Technologies proposes the SwiftSentinel small unmanned aerial system (sUAS) as a solution for the WWF Wildlife Crime Technology Project. The company offers either a complete system for purchase or operating the platform as a service, leveraging established partnerships with Autonomous Systems Research in Africa and Conservation Drones in Asia to provide training, maintenance, and operational support for wildlife surveillance and monitoring missions.

## Technical Approach

**Core System Architecture:**
The SwiftSentinel is a fixed-wing sUAS comprising five major components:

1. **Airframe (Nurf)**: 2-meter wingspan fixed-wing aircraft constructed from expanded polypropylene foam (EPP)
   - Designed for durability and rapid setup/teardown (5-10 minutes with two-person crew)
   - 60-minute flight endurance at ~10 km/h wind speeds
   - 72 km maximum range per mission
   - 60-minute battery charging (via car battery or solar panels)
   - Capable of light precipitation and sand operation; designed for potential modification to heavy precipitation, water landings, parachute deployment
   - Operating ceiling: 3,000 meters (10,000 ft) above sea level

2. **Autopilot (SwiftPilot)**: Patent-pending proprietary autopilot system
   - Fully autonomous capability (autonomous take-off, flight, landing)
   - Proven in extreme weather conditions (tornadoes, arctic, storms)
   - Stall recovery capability
   - Optional radio-controlled mode via multiplexer add-on for aggressive maneuvers
   - Integrated removable microSD card for onboard telemetry logging
   - Interchangeable wireless transceiver modules supporting multiple frequency bands and ranges

3. **Payload Options**:
   - Electro-optical (EO) HD wireless imaging/video camera with optional two-axis gimbal
   - Forward-Looking Infrared (FLIR) thermal camera with optional two-axis gimbal for heat signature detection (night/rain/fog/canopy conditions)
   - Optional single-board computer for computationally intensive operations (RF triangulation, target tracking, route optimization)

4. **Ground Control Station (SwiftStation)**:
   - All communication electronics in hard-shell, waterproof case
   - Ruggedized Panasonic Toughpad with Android OS interface (SwiftTab)
   - Car battery or wall outlet powered
   - Mission planning with hardware-in-the-loop simulation capability (X-Plane compatible)
   - Support for 100+ waypoints and multiple flight parameters
   - Real-time flight plan adjustment
   - Multi-format map and geo-referenced data import

**Wireless Transceiver Options:**
| Transceiver Type | Frequency | Max Range |
|---|---|---|
| Digi XBee Pro Series | 868/900 MHz | 40 km |
| Digi XTend | 900 MHz | 64 km |
| Microhard Products | 900 MHz/2.4 GHz/3.4 GHz | 100 km |

## Products & Capabilities Described

### SwiftSentinel sUAS
- **What it is**: A complete small unmanned aerial system specifically developed for wildlife monitoring and surveillance, joint project between BST, Rocketship Systems Inc., and Autonomous Systems Research, partially IEEE-funded
- **Design philosophy**: End-user focused, affordable, easy-to-use for novice operators, physically robust, low maintenance
- **Modular architecture**: Customizable to specific end-user requirements
- **Key capabilities**: 
  - Intuitive Android tablet interface with autonomous flight
  - 5-10 minute operational setup
  - Thermal and electro-optical imaging payloads
  - Mission planning with simulation capability
  - Multiple simultaneous sUAS operation capability
  - Robust autopilot proven in extreme weather

### SwiftPilot Autopilot
- **Suppliers**: InvenSense (IMU), Measurement Specialties (pressure sensor)
- **Specifications**: Patent-pending design; proven in tornadoes, arctic conditions, storms; stall recovery capability
- **Flexibility**: Rapidly integrates various payloads; supports multiple wireless transceiver modules

### SwiftStation Ground Control Station
- Packaged with communication electronics and Panasonic Toughpad tablet
- SwiftTab interface for mission planning and real-time flight control
- Simulation capability and multi-format map support
- Total system weight with case: just over 20 kg

## Use Cases & Applications

- **Wildlife surveillance**: Primary application for IFAW and Kenya Wildlife Service
- **White rhinoceros monitoring**: Currently under evaluation by IFAW and Kenya Wildlife Service in East Africa; successfully completed initial flight tests in Kenya
- **Wildlife crime detection**: Monitoring of illegal human activities (logging, poaching, forest fires)
- **Large animal species surveying**: Mapping and census applications
- **Land use/cover mapping**: Near real-time geo-referenced mapping
- **Illegal forest activity monitoring**: Video and still photography documentation

## Key Results (Project Status)

- SwiftSentinel successfully completed initial field tests in Kenya
- System currently under evaluation for purchase by IFAW and Kenya Wildlife Service
- Meets expectations of both organizations according to proposal
- Established operational partnerships and training networks in Africa (via ASR in Kenya) and Asia (via Conservation Drones in Nepal, Cambodia, Indonesia)

## Notable Details

### Company Background & Expertise
- Black Swift Technologies founded 2011 as spinoff from University of Colorado Boulder's RECUV
- Leadership team: 5 Ph.D. graduates in Aerospace/Electrical Engineering, 1 Ph.D. candidate in business, 1 MBA graduate
- Combined team experience: 1000+ hours UAV flight time, 70+ peer-reviewed publications, 65 FAA Certificates of Authorization
- Extensive operational experience across diverse missions and challenging conditions

### Platform History & Track Record
BST team designed/developed the Tempest sUAS that performed the first-ever sUAS intercept of a tornadic supercell thunderstorm (VORTEX2, 2010); 21 missions in extreme weather

### Partnership Ecosystem
1. **Rocketship Systems Inc.** (USA): Airframe design/manufacturing (Nurf airframe), custom precision components, FlyingFoam division for CNC foam cores
2. **Autonomous Systems Research** (Kenya): African operations, maintenance, logistics hub, training; CEO Moses Gichanga
3. **Conservation Drones** (International): Asian operations, maintenance, logistics, training network; Co-founders Lian Pin Koh and Serge Wich; 10+ countries of operational experience; systems distributed to Jane Goodall Institute, WWF Nepal, Sumatran Orangutan Conservation Programme, WWF Netherlands, Google Inc., Flora and Fauna International, Greenpeace International, RSPB

### Maintenance & Logistics Model
Three-tier distributed model (Organizational/Intermediate/Depot levels) designed to reduce costs, minimize downtime, and build local capacity

**African Model**: Depot-level facility in Nairobi, Kenya (operated by ASR); I-level centers near operational areas; O-level at host organizations

**Asian Model**: Conservation Drones leverages existing network (Sabah/Malaysian Borneo, Sumatra) to establish integration, maintenance, training facilities

### Training Program
- 2-day course deemed sufficient for novice users
- Day 1: Classroom instruction and simulator flight
- Day 2: Practice flights with realistic mission scenarios
- Covers system manuals, documentation, O-level maintenance tasks
- Additional training available upon request
- Ongoing support provided by ASR (Africa) and Conservation Drones (Asia)

### Export Compliance
- Base-level SwiftSentinel not subject to known ITAR or export restrictions (uses COTS and open-source technology)
- Some payloads (thermal FLIR cameras) potentially subject to ITAR; BST will work with export regulation specialist to ensure compliance

### Delivery Options Proposed

**Option 1: Purchase**
- Complete system includes: 2 Nurf airframes with SwiftPilot, EO video camera, optional FLIR camera, 1 SwiftStation, battery chargers, secondary batteries
- Ruggedized hard-shell waterproof transport case
- Total system weight: just over 20 kg
- 3 years of software/firmware updates included
- On-site training and maintenance provided

**Option 2: Service Model**
- Operating platform as a service leveraging existing partnerships
- Cost varies based on user needs (available upon request)
- Access to established African and Asian operational networks

### Competitive Advantages
- Proven extreme weather capability (tornado intercept experience)
- Modular, customizable design
- Robust, low-maintenance construction (EPP foam)
- Intuitive user interface designed for novices
- Established operational and training partnerships in target regions
- Rapid deployment capability (5-10 minute setup)
- Extended mission capability with dual airframes and solar charging

### Component Suppliers
InvenSense (IMU), Measurement Specialties (pressure sensors), Airborne Innovations (wireless video/command links), Digi International (wireless transceivers), Microhard Corporation (wireless systems), Panasonic Toughpad (ruggedized tablet), Pelican (transport cases)