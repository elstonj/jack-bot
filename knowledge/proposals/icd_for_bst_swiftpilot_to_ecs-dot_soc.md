# Interface Control Document: BST SwiftPilot – ECS-DoT SoC

## Document Metadata
- Type: Interface Control Document (ICD)
- Client/Agency: ECS-DoT (Emergency Communications System - Department of Transportation)
- Program/Solicitation: Not explicitly stated
- Date: Created 2026-08-20, Modified 2026-08-21
- BST Products/Systems Referenced: SwiftPilot, E2 Payload Port, BST Software Development Kit (SDK)
- Key Personnel: Daniel Prendergast (last editor)

## Executive Summary
This ICD defines the hardware and software interfaces between the BST SwiftPilot autopilot system and an ECS-DoT System-on-Chip (SoC) board for integrated flight control. The document specifies electrical connections, data formats, message rates, and communication protocols required for the ECS-DoT board to receive aircraft sensor data and transmit flight control commands.

## Technical Approach

### Hardware Interface
- **Connection Type**: 4-wire cable between E2 Payload port and ECS-DoT board
- **Cable Feature**: Inline voltage regulator to step down power to X.X VDC (value redacted in document)
- **Primary Connector**: 9-pin D-Sub female connector on BST E2 Payload Port
- **Pins Used for Main Interface**:
  - Pin 1: V+ (Raw Battery, 19.2V - 25.2V, 3A max)
  - Pin 2: GND (3A max)
  - Pin 3: UART Tx (from aircraft)
  - Pin 4: UART Rx (to aircraft)
  - Pins 5-9: CAN bus and additional UART GND (alternative/optional connections)

### Software Interface
- **Architecture**: ECS-DoT SoC sits on E2 stability and actuator control loop
- **Operation Model**: Synchronous per-cycle operation:
  - Receives sensor and aircraft state measurements from SwiftPilot at start of each control cycle
  - Processes data and calculates control command
  - Transmits control signal back to autopilot
- **Communication Protocol**: UART via payload connector
- **Data Access**: Best achieved using BST Software Development Kit (SDK)

## Products & Capabilities Described

### SwiftPilot
- BST's autopilot system that serves as the primary flight control interface
- Manages aircraft sensors and stability/actuator control loops
- Exposes E2 Payload Port (9-pin D-Sub connector) for external system integration
- Provides real-time aircraft state and sensor data at configurable rates

### E2 Payload Port
- 9-pin D-Sub female connector on aircraft
- Supports multiple communication standards (UART, CAN bus)
- Supplies raw battery power (19.2V - 25.2V)
- UART interface operates at aircraft voltage levels

### ECS-DoT SoC Board
- Small development board (~7cm x 6cm)
- Powered and programmed via JTAG microUSB (5V input)
- UART pins accessible via J20 header connectors
- Default configuration: UART signals bridged to FTDI USB via jumpers
- UART signals operate at 3.3V logic level
- Calculates flight control commands in real-time

## Data Interface Specifications

### SwiftPilot → ECS-DoT (Sensor/Autopilot Data)

| Data Element | Units | Rate (Hz) | Max Rate (Hz) | Notes |
|---|---|---|---|---|
| PWM (each rotor) | μs | 20 | 300 | |
| Speed Over Ground | m/s | 10 | 10 | |
| Throttle | N/A | N/A | N/A | Calculated on ECS-DoT board |
| Climb/Descent Rate | m/s | 10 | 10 | |
| Battery Current | A | 1 | 10 | |
| Battery Voltage | VDC | 1 | 10 | |
| Power | W | N/A | N/A | Calculated on ECS-DoT board |
| Orientation (Roll, Pitch, Yaw) | degrees | 20 | 1000 | |
| Altitude | meters MSL | 10 | 10 | |
| Barometric Pressure | hPa | 2 | 50 | |

### ECS-DoT → SwiftPilot (Flight Control Commands)

| Data Element | Units | Rate (Hz) |
|---|---|---|
| PWM (for each motor) | μs | 70 |

(Document incomplete - command data table cut off)

## Use Cases & Applications
- Integration of external flight control algorithms (ECS-DoT SoC) with BST SwiftPilot autopilot
- Real-time closed-loop flight control with stability augmentation
- Emergency Communications System operations requiring customized control logic

## Key Technical Details & Specifications
- **Voltage Regulation**: Inline regulator in cable (specific output voltage redacted)
- **UART Electrical Standard**: 3.3V logic levels on ECS-DoT side
- **Power Budget**: 3A max from battery pins; 500mA max from CAN power pins
- **Cycle Rate**: Synchronous with autopilot control loop (primary rate appears to be ~20 Hz based on orientation sensor)
- **Maximum Sensor Rate**: 1000 Hz for orientation data, allowing for high-bandwidth control
- **Microcontroller Programming**: JTAG microUSB interface

## Notable Details
- Document references BST SDK as standard tool for accessing UART data
- The ECS-DoT board has flexible UART routing via jumper configuration (can route to FTDI USB bridge or direct access)
- Throttle and Power calculations are offloaded to ECS-DoT board rather than transmitted from SwiftPilot
- CAN bus interface available on E2 Payload Port (pins 5-8) but not used in primary SwiftPilot-ECS-DoT interface
- Motor PWM command rate (70 Hz) matches typical multirotor/fixed-wing servo control requirements
- Document appears to be work-in-progress (table incomplete, voltage values redacted with "X.X")