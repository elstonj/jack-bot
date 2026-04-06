# Supplemental Budget and Other Information

## Document Metadata
- Type: Budget and procurement documentation for SBIR Phase I project
- Client/Agency: NOAA
- Program/Solicitation: 2018 SBIR Phase I
- Date: February 19, 2019 (document compilation date); August 2018 - February 2019 (components)
- BST Products/Systems Referenced: S0 (aircraft platform)
- Key Personnel: Jack Elston (lead), Maciej, Josh (team members on budget tasks)

## Executive Summary
This is a supplemental budget and procurement file for a NOAA SBIR Phase I project focused on developing and testing the S0 aircraft system. The document contains detailed task labor allocations, travel expenses, equipment/component purchases, and vendor quotes for avionics, sensors, motors, servos, batteries, and structural materials needed for the S0 design refinement, testing, and deployment phases.

## Technical Approach
The project involved six major work streams:

**1. Preliminary Tasks (Task IDs 1517, 1136, 1281)**
- Kickoff meetings, requirements review, test site review, risk assessment, and project management
- Labor: 40-312 hours allocated across team members

**2. Refinement of S0 Design**
- Aerodynamic design refinement (160-100 hours)
- Wing swivel, antenna integration, tail design, user interface, avionics design, firmware updates
- Aircraft internals, wiring, electronics integration, and sensor testing
- Wind sensor testing and build procedures/QC process development

**3. Automated Guidance Algorithm**
- Validation of simulation data with observations
- Collaboration with NCAR on hurricane simulations
- Development of robust automated guidance and Monte Carlo simulations
- Work on unique parameters for identifying relative location

**4. Preflight and Deployment Design**
- CONOPS document development
- Coordination with AOC (Aircraft Operations Center) on operational requirements
- Tablet-based preflight UI implementation
- Tube and parachute system design
- Aircraft deployment mechanism and electronics
- Protocol work with NCAR for AVAPS (Airborne Vertical Atmosphere Profiling System) integration

**5. Flight Testing**
- Iterative testing of aerodynamic improvements (40-120 hours)
- Severe weather testing in Colorado
- Deployment from launch tube flight tests
- Full tube-based system flights
- P3 aircraft integration flight tests (60 hours)

**6. System Specification**
- Data analysis, documentation, and final reporting

## Products & Capabilities Described

### S0 Aircraft System
- Small unmanned research aircraft platform
- Design features: swiveling wing design, integrated antennas, refined aerodynamics
- Deployment via launch tube system with parachute recovery
- Integration with AVAPS ground station for data collection
- On-board avionics and automated guidance systems
- Tablet-based preflight control interface

### Key Components & Specifications

**Avionics/Electronics:**
- Autopilot-v24 PCB assembly (20 units): $4,489.60 total
  - RoHS-compliant, 4-layer FR4, ENIG finish
  - Board fabrication, components, assembly labor included
  - 20 business day turnaround

**Motors & Speed Controllers:**
- KDE1806XF-2350 Brushless Motors (10 units @ $25.95 each): $259.50
  - 2350 KV rating, 770g+ thrust with 5" propeller at 4S
  - High-temperature windings (240°C continuous, 340°C max)
  - Silicone-wire leads with bullet connectors
- KDE KDEXF-UAS20LV 20A+ ESC (10 units @ $40.95 each): $409.50
  - Compatible with 2S LiPo to 6S LiHV (26.5V max)
  - Auto-recognition of control signals
  - Regenerative braking, temperature-controlled synchronous rectification

**Servos:**
- Hitec HS-5065MG Sub-Micro Servos (20 units @ $33.99 each): $679.80
  - 30.55 oz/in stall torque at 6.0V
  - 0.11 sec/60° transit time
  - Metal gears, digital programmable

**Structural Materials:**
- Kevlar Tube 2.000" x 2.030" x 72" (10 units @ $213.79 each): $2,137.90
- Wing molds (composite construction): $15,260.00 (1 unit)
- Composite wings (10 units @ $500 each): $5,000.00
- Wing assembly jigs: $4,000.00
- 3D-printed components (tail, nosecone, avionics tray via Shapeways): $135.60-$966.00

**Sensors & Instruments:**
- LW20 Laser Rangefinder (10 units @ $329.00 each): $3,290.00
  - 100m range, IP67 enclosure, I2C/serial interface
  - 678 readings per second
- RD-41 Sensor Module from Vaisala (10 units @ $227.69 each): $2,276.90
  - PTU (Pressure, Temperature, Humidity) sensor
  - Model: RSS421 1E A

**Power Systems:**
- Custom 6S 14,000mAh Battery Packs (2 units @ $238.00): $476.00
  - 6S4P 21.6V configuration with custom 10AWG leads
- Custom 3S 14,000mAh Battery Pack (1 unit @ $154.00): $154.00
  - 3S4P 10.8V configuration with Sermos/Powerpoles connector
- Total battery order: $630.00

**Recovery Systems:**
- 24" Compact Elliptical Parachute (5 units @ $72.02 each): $360.10
  - 2.1lb @ 20fps descent rate
  - Suitable for mid-power applications

**Launch System Components:**
- Launcher Tube (5 units @ $25.99 each): $129.95

**Total Component/Material Budget:** $42,138.55

## Use Cases & Applications

### Hurricane Research & Atmospheric Sampling
- Integration with NCAR hurricane simulation models
- Deployment from P3 aircraft for storm sampling
- AVAPS ground station compatibility for data relay
- Automated guidance algorithms for storm navigation
- Severe weather testing in Colorado environment

### Operational Deployment
- Launch tube deployment system allowing aircraft to be carried/deployed from larger research aircraft
- Automated recovery via parachute system
- Real-time telemetry via tablet-based UI
- Multi-aircraft coordination capability (based on encoded laser sensors allowing multiple UAVs)

## Travel & Meeting Expenses

**Washington DC Area (Silver Spring, MD) Trip:**
- Flights: $379.60
- Public transportation: $9.60
- Hotel (DoubleTree Hilton Silver Spring): $338.30 (2 nights @ $169.15)
- Per diem (Silver Spring): $138.00 (2 days @ $69.00)
- **Subtotal: $865.50**

**Orlando/Lakeland, Florida Trip:**
- Flights: $745.20 (2 roundtrips @ $372.60)
- Car rental: $229.28
- Per diem: $550.00 (10 days @ $55.00 general Florida rate)
- Hotel (Lakeland area): $940.00 (10 nights @ $94.00)
- **Subtotal: $2,464.48**

**Total Travel Budget: $3,329.98**

## Notable Details

### Partnerships & Coordination
- **NCAR (National Center for Atmospheric Research):** Collaboration on hurricane simulation data and AVAPS protocol integration
- **AOC (Aircraft Operations Center):** Coordination on operational requirements for tube-based deployment and on-board operations
- **P3 Aircraft Integration:** Plans for flight testing aboard P3 research aircraft

### Manufacturing & Vendors
- **SlingShot Assembly:** PCB manufacturing and assembly (quote #15761, 20 boards in 20 business days)
- **Vaisala Inc.:** PTU sensor modules (RSS421 models)
- **KDE Direct:** Brushless motors and ESCs optimized for UAS applications
- **LightWare Optoelectronics:** Laser rangefinders
- **Shapeways:** 3D-printed plastic components
- **MaxAmps:** Custom battery pack builds with specific connector and lead configurations
- **Fruity Chutes:** Recovery parachutes
- **Rockwest Composites:** Kevlar tubing

### Project Focus Areas
- **Aerodynamic optimization:** Extensive refinement of wing and tail designs with multiple iterations
- **Tube-based launch system:** Novel deployment mechanism requiring custom electronics and mechanical design
- **Automated guidance:** Algorithm development for storm navigation in severe weather conditions
- **Sensor integration:** Multiple instruments (PTU sensors, laser rangefinders, wind sensors) with data telemetry
- **Production readiness:** Development of build procedures, QC processes, and documentation

### Flight Test Strategy
- Iterative Colorado testing for aerodynamic validation
- Severe weather testing capability
- Progressive testing: tube deployment → full tube system → P3 integration
- Data analysis and feedback loops driving design refinement

This budget document represents Phase I preliminary design and testing for what appears to be an atmospheric research platform designed for deployment from larger research aircraft into severe weather environments, particularly hurricanes.