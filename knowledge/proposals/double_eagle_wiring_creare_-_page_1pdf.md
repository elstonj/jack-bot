# Double Eagle Wiring (Creare)

## Document Metadata
- Type: Technical schematic/wiring diagram
- Client/Agency: Creare
- Program/Solicitation: 2019 VTOL Autopilot
- Date: Created 2020-08-07
- BST Products/Systems Referenced: None directly (this is a wiring diagram for a client system)
- Key Personnel: Not identified

## Executive Summary
This is a wiring diagram for the Double Eagle VTOL (vertical takeoff and landing) system developed for Creare, showing the electrical interconnections between autopilot, batteries, sensors, actuators, and motor control systems.

## Technical Approach
The system uses a distributed architecture with:
- **Power**: Dual 6S 14Ah Lithium-Ion batteries with specific plug/unplug sequencing (one plugged first/unplugged last; one plugged last/unplugged first)
- **Control**: Autopilot with IMU requiring vibration isolation via damping material or dampened mounting board
- **Communication**: Futaba R70008sb radio receiver
- **Sensing**: LightWare LW20/c laser range finder, GPS/Magnetometer
- **Actuation**: Four motor actuators (0-3) with corresponding motors, controlled through actuator modules
- **Distribution**: McMaster 7626K42 power distribution block
- **Safety**: Terminating resistors on supply board and pressure board (pressure board terminating resistor marked as ON)

## Products & Capabilities Described
**Autopilot System**
- Role: Primary flight control computer
- Requirement: Mounted on vibration-dampening material to reduce IMU noise
- Interfaces with all sensors and motor actuators

**Sensors**
- LightWare LW20/c: Laser altimeter/range finder
- GPS/Magnetometer module: Navigation and heading reference

**Motor System**
- Four independent motors (0, 1, 2, 3) with corresponding ESC actuators
- Provides VTOL lift/thrust capability

## Use Cases & Applications
- VTOL platform development for Creare
- Autonomous or semi-autonomous aerial vehicle operations

## Notable Details
- Clear operational procedure documented: specific battery connection sequence to ensure safe power sequencing
- Vibration isolation requirements emphasized for IMU accuracy in flight control
- Dual battery redundancy or load-sharing configuration
- Terminating resistor configuration suggests CAN bus or similar communication protocol