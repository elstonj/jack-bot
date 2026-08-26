# EMASS-BST Slack Channel

## Document Metadata
- Type: Slack channel conversation / technical collaboration thread
- Client/Agency: Black Swift Technologies (BST) internal collaboration with Nanoveu
- Program/Solicitation: EMASS (Energy Management and Autonomous Systems)
- Date: February 2026 - April 2026
- BST Products/Systems Referenced: E2 (multirotor platform), SwiftPilot autopilot, SWIL (Software-In-Loop simulation), ECS-DoT (Energy Control System - Device on Target)
- Key Personnel: Jack (Jack Elston, GitHub: elstonj-bst), Daniel Prendergast (DTPrendergast), Nikhila (Nanoveu), Moe (Nanoveu AI/ML lead), Maciej, Sergio Ruocco (Autoboot specialist), Shantanu

## Executive Summary
This Slack channel documents the collaborative development between Black Swift Technologies and Nanoveu to integrate an AI-based energy optimization system (ECS-DoT chip) onto BST's E2 multirotor platform. The project involved training a deep reinforcement learning (PPO) model to optimize motor control for energy efficiency, testing in Gazebo simulation, and preparing for hardware-in-loop (HWIL) and live flight testing.

## Technical Approach

### System Architecture
The integration involved:
1. **ECS-DoT Hardware**: A custom chip running C/C++ firmware with embedded AI inference (PPO model)
2. **BST Autopilot Integration**: ECS-DoT connects via UART to the SwiftPilot autopilot at 115200 baud
3. **Payload State Machine**: ECS-DoT implements BST's payload protocol:
   - System initialization handshake
   - Heartbeat telemetry at 0.2s intervals (critical for connection stability)
   - Payload state transitions: DISCONNECTED → CONNECTED → READY → ACTIVE
   - Actuator command output at 70Hz via ACTUATOR_VALUES packets with 16-channel PWM array

### AI Model Development
- **Training Data**: Flight logs from E2 aircraft (E20006 and E20009 identical units)
- **Simulation Environment**: Gazebo with SwiftPilot SWIL using examples/gazebo folder
- **Flight Conditions Tested**:
  - Benign straight-and-level flight
  - Dynamic flight maneuvers
  - Multiple altitude variations (1636-1647m in test waypoints)
  - Up to 16 waypoints with varying altitudes to improve model variance
- **Model Type**: PPO (Proximal Policy Optimization) reinforcement learning
- **Challenges**: Initial sim-only models showed high error when applied to real flight data; required integration of real flight logs for improved accuracy

### Telemetry Integration
ECS-DoT receives from autopilot at specified rates:
- TELEMETRY_POSITION: 10Hz
- TELEMETRY_ORIENTATION: 20Hz
- TELEMETRY_SYSTEM: 1Hz
- TELEMETRY_HEARTBEAT: 4Hz (required for connection maintenance)

## Products & Capabilities Described

### E2 Multirotor Platform
- **Configuration**: 4-rotor electric multirotor
- **Specifications**:
  - Mass: 11.45 kg
  - Battery: 6-cell Li-Ion, 42000 mWh (907.2 Wh) capacity, 18V nominal
  - Motor control: 16-channel PWM output
  - Cruise speed (safety limit): 3.0 m/s
  - Vehicle limits:
    - Roll/Pitch: ±20° 
    - Roll/Pitch rate: 6.98 rad/s
    - Yaw rate: 0.52 rad/s
    - Side speed: 4.0 m/s
    - Vertical speed: -1.50 to 3.00 m/s
    - Max lost GPS: 5s
    - Max PDOP: 3.0

### SwiftPilot Autopilot
- Runs two instances: 
  - SWIL (Software-In-Loop) version for simulation (examples/gazebo)
  - Real-time version for flight (bin/pro_core_swil_MULTIROTOR)
- Key daemons:
  - gcsDaemon: Ground station interface (port 55554)
  - pro_core_swil_MULTIROTOR: Flight control core
- Protocol support:
  - TCP GCS interface on port 55555
  - UART payload interface on configurable serial port
  - Telemetry packet structure with system init, heartbeat, position, orientation, system state
  - Payload control mode: Only one payload allowed at a time on port 55551
- Safety features:
  - Vertical rate limiting (error if >3.03 m/s)
  - Vehicle limit enforcement
  - Payload error state detection with automatic reset

### ECS-DoT Development Environment
- **SDK**: Docker-based baremetal development kit (ghcr.io/emassai/ecsdot-baremetal-sdk-blackswift)
- **Eval Board**: FTDI Dual RS232-HS interface, dual UART ports (ttyUSB0, ttyUSB1)
- **Development Board**: Single RS232-HS variant with JTAG support
- **Build System**: Docker container with compilation tools, includes:
  - bst-ecsdot-comms: Communication interface library
  - emass_hwil: Hardware-in-loop application directory
  - Packet creation functions (Packet_create()) for UART transmission
- **Flashing/Deployment**:
  - Method 1: Direct compilation and debugging via JTAG in Docker SDK
  - Method 2: Pico 2 autoboot firmware (via Raspberry Pi Pico 2 with headers)
- **Autoboot System**: Pico 2 stores and loads binaries to ECSDOT eval board on startup; requires:
  - Pico 2 UF2 firmware image flashing
  - Python deployment script for image upload
  - JTAG header connections (replaces USB JTAG mode)
  - Separate /dev/ttyACM0 output for autoboot debug
  - 5V power jack for eval board (or USB from Pico)

## Use Cases & Applications

### Primary Use Case: Energy Optimization in Flight
The ECS-DoT system is designed to:
1. Monitor real-time aircraft state (position, orientation, battery, motor currents)
2. Run AI inference (PPO model) to compute optimal motor commands
3. Output optimized PWM signals to motors for energy efficiency

### Specific Testing Configurations

**Simulation Testing (HWIL in Gazebo)**:
- Evaluated AI model performance in controlled environment
- Trained models on varying flight conditions
- Tested with 16-waypoint mission at altitudes 1636-1647m
- Energy savings calculated via flight time comparison (one flight with ECS-DoT, one without)

**Hardware Testing**:
- Bench test: PWM output validation with drone strapped/stationary
  - Test sequence: 10s at PWM 1300, 10s at PWM 1400, repeat 2 cycles, then stop
  - Validates motor control logic without flight risk
- Live flight testing: Full autonomous mission execution with ECS-DoT active payload control

## Key Results (Technical Progress Noted)

### Model Development Progress
- Initial sim-only model showed high error (~100+ A discrepancy in current prediction)
- Added real flight data from E2 aircraft; collected 6 minutes of flight logs
- Improved model accuracy by training on varied mission data
- Final model integrated into firmware with full telemetry → AI → PWM pipeline verified via GDB debugging

### System Integration Achievements
- **UART Communication**: Successfully established packet-based communication between ECS-DoT and autopilot
- **Payload State Machine**: Implemented full protocol including system init handshake, heartbeat at 0.2s intervals, and payload state transitions
- **Telemetry Processing**: Validated reception of position, orientation, and system telemetry at correct rates
- **Motor Control**: Confirmed 70Hz actuator output rate with 16-channel PWM mapping
- **AI Pipeline**: Complete end-to-end validation: telemetry input → AI model inference → PWM command output

### Known Issues Encountered and Resolved
1. **Heartbeat timeout**: Initial heartbeat rate too slow; corrected to 0.2s (250ms)
2. **Connection cycling**: Payload repeatedly cycling through DISCONNECTED→CONNECTED states due to heartbeat timeout; resolved by heartbeat adjustment
3. **Eval board visibility**: JTAG/UART ports not appearing due to jumper configuration and USB hub issues; resolved by proper cable management and group permissions
4. **Autoboot LED behavior**: Red light blinking correlated with autopilot communication, not independent firmware execution
5. **Linux permissions**: User account required dialout group membership for /dev/ttyUSBx access
6. **Vehicle limits enforcement**: Discovered vertical rate limit (3.03 m/s) required integration into AI model constraint set

## Notable Details

### Development Artifacts
- Flight log files provided: log_E20009.nc (6 minutes of E2 in-flight data with ECS-DoT hardware mounted)
- Test application: emass_test.zip and emass_test.tbz with Gazebo simulation interface
- Multiple binary versions prepared:
  - droneapp: Standard flight application
  - droneapp-20260402_2007: Latest production version for live flight
  - droneapp-stripped: Early test version
  - test: Bench test executable
  - HWIL-sim variants: For Gazebo simulation testing

### Integration Challenges
- Energy savings measurement: Difficult to isolate due to weather, battery aging, and flight-to-flight variability; addressed through instantaneous current integration per flight phase
- Model variance: Initial sim-only data insufficient; required additional waypoints with altitude variations
- Wind/disturbance modeling: No standard Gazebo disturbance models available; noted as future improvement area

### Hardware Details
- **ECS-DoT Eval Board**: Large blue FTDI Dual RS232-HS board with UART and JTAG ports
- **Pico 2 Autoboot**: Requires white button hold-down during USB connection for bootloader mode; stores boot images in flash
- **Power Options**: Either Pico 2 USB OR dedicated 5V barrel jack power (not both simultaneously to avoid electrical faults)
- **Serial Port Identification**: 
  - UART (if00-port0): Main ECSDOT communication
  - JTAG (if01-port0): SDK debugging/flashing
  - Autoboot (ttyACM0): Pico 2 output

### Team Structure
- **BST Side**: Jack (autopilot/core systems), Daniel Prendergast (flight operations), Maciej (parameters/vehicle config), Sergio Ruocco (autoboot/firmware deployment)
- **Nanoveu Side**: Nikhila (firmware integration), Moe (AI/ML model training), Shantanu (hardware/autoboot support)

### GitHub Collaboration
- Repository: emassAI/ecsdot-baremetal-sdk-blackswift
- Access managed via GitHub personal access tokens (fine-grained and classic tokens both used)
- Docker image distribution via GitHub Container Registry (ghcr.io)

This Slack channel represents active development and troubleshooting of a complex embedded AI integration, with strong emphasis on iterative testing, precise technical communication, and collaborative problem-solving across two organizations.