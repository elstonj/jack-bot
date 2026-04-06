# Black Swift Quad-rotor System Design Concept

## Document Metadata
- Type: White paper / concept design document
- Client/Agency: Intuitive Research
- Program/Solicitation: Not specified
- Date: June 5-13, 2013 (created/modified)
- BST Products/Systems Referenced: BST autopilot electronics, BST control software, BST autonomous flight control software, BST ground station software, BST mesh networking software
- Key Personnel: Jack Elston (last editor)

## Executive Summary
Black Swift Technologies proposed to develop a micro quad-rotor UAS system for GPS-denied indoor and underground environments. The system would integrate BST's autopilot avionics and control software with a structured laser grid sensor and EO camera for autonomous navigation and 3D mapping. The quad-rotor would transmit video and mapping data in near real-time to a handheld tablet interface, with capability for multi-vehicle operations and data sharing via mesh networking.

## Technical Approach
BST would customize its autopilot electronics and control software with a sensor suite mounted on a micro quad-rotor airframe. For GPS-denied environments (indoors/underground), the primary navigation method uses a **structured laser grid** combined with video image recognition to create surface maps and determine flight paths autonomously. The laser grid continuously rotates with the platform to scan environments and enable obstacle avoidance. A sonic range finder provides supplementary data and emergency landing capability. GPS would be used for waypoint navigation in non-GPS-denied environments. An IMU provides inertial measurement for flight control.

## Products & Capabilities Described

### BST Autopilot Electronics
- Customized for quad-rotor integration
- Core flight control system

### BST Autonomous Flight Control Software
- Enables autonomous navigation through GPS-denied environments
- Processes laser grid and video data for path determination and obstacle avoidance
- Manages multi-vehicle coordination

### BST Ground Station Software
- Receives and displays video and 3D mapping data
- Compatible with handheld tablet and other control devices
- Enables near real-time operator feedback

### BST Mesh Networking Software
- Allows multiple systems to network together
- Shares and combines data between platforms
- Enables signal daisy-chaining across long distances or high radio-loss environments

## Use Cases & Applications
- **Indoor environment mapping and exploration** – buildings, structures, hidden rooms discovery
- **Underground environment navigation** – caves, tunnels, subsurface mapping
- **Multi-system operations** – large environments requiring multiple vehicles with combined data collection
- **External building mapping** – conducted prior, during, or after indoor mapping
- **Search and investigation operations** – minimal operator training required for deployment

## System Architecture & Components

### Airborne Physical Systems
- **IMU**: Inertial measurement unit (specific manufacturer/model marked as "XXX" – details incomplete)
- **GPS**: Global positioning system (details incomplete)
- **Structured Laser Grid**: Primary navigation sensor for GPS-denied environments
- **EO Camera**: Electro-optical camera for video and image recognition
- **Sonic Range Finder**: Supplementary altitude/obstacle detection

### Software Components
- Autonomous flight control software
- Ground station software
- Mesh networking software

### Constraints
- **Mass Budget**: 250-gram payload capacity for airframe
- **Power Budget**: 5-watt excess power supply available

## Notable Details

### Operational Concept
- Man-portable system deployable by minimally-trained operator
- Handheld tablet or compatible device serves as control interface
- Multiple systems can be flown simultaneously by one or more operators
- Daisy-chaining capability for large underground environments with signal relay
- Systems networked to share and combine data to reduce mission timelines

### Development Status
- Document notes TRL (Technology Readiness Level) assessment and development requirements to reach various TRL levels
- Includes projected development timeline for components
- References mass/power budgets in separate Google Drive documents

### Document Structure Notes
The white paper was planned to include five main sections with figures:
1. Executive summary (1 page)
2. Technical approach overview (2 pages)
3. Technical discussion (5 pages) – system architecture, vehicle, sensors, navigation, communication, ground display/control
4. Program development plan (5 pages) – vehicle, sensors, ground element, integration, testing
5. Risk analysis (2 pages) – technology readiness descriptions and risk summary

**Status Note**: This document appears to be a template or outline with significant sections incomplete (indicated by "….." and "XXX" placeholders for specific component details). Reference materials in the project folder appear to contain the detailed specifications for mass and power budgets.