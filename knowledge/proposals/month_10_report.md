# Autonomous Quad-Biplane Flight Controller - Month 10 Interim Report

## Document Metadata
- Type: Interim Project Report
- Client/Agency: Creare (subcontractor to NOAA/Navy SBIR)
- Program/Solicitation: SBIR Project "A Compact and Agile Fixed-Wing UTAS for VTOL Shipboard Operations"
- Contract Number: S649
- Date: 2020-03-20
- BST Products/Systems Referenced: SwiftPilot autopilot, SwiftTab UI, Double Eagle aircraft platform
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
Black Swift Technologies is developing an autonomous flight controller for Creare's Quad-Biplane aircraft to enable VTOL shipboard operations. Month 10 focused on implementing UI changes for VTOL functionality, refactoring the SwiftTab codebase to support this new vehicle type, and testing improved control and navigation algorithms. The autopilot now supports all navigation capabilities in VTOL mode including mapping and precision landing functionality.

## Technical Approach

### Autopilot Algorithm Development
- Adapted BST's existing fixed-wing autopilot flight control algorithms for Quad-Biplane multi-rotor application
- Customized attitude control algorithms to enable stable flight across multiple modes: vertical hovering (takeoff), transition to horizontal flight, horizontal cruise, and precision landing
- Developed "outer loop" controller for mission objectives (flight trajectory, altitude) that sets control targets for stable flight algorithms
- Leveraged existing SwiftPilot software architecture to minimize implementation effort

### Control System Improvements (Month 10)
- Implemented new controller using reduced state control mixed with yaw control authority (replacing previous full state attitude control that was artificially limiting control authority)
- Corrected navigation tracking issues ("curvy" paths) observed in earlier testing
- Optimized control parameters: p-value of 0.4 produced best simulation results
- Generated control signal equations incorporating pitch, roll, yaw, and throttle commands

### Navigation System Updates
1. **Transition/Hover/Orbit**: UI allows users to input radius for waypoints; zero radius = hover transition; non-zero radius = forward flight orbit around point
2. **Landing Logic**: Aircraft takes fixed-wing path to landing waypoint with feature to approach from specified angle relative to wind
3. **Mapping Logic Fixes**: Aircraft can now execute standard mapping plans (zamboni, sequential, volumetric) in forward flight mode

### Precision Landing
- Creare developing Landing Location Detection software to visually identify shipboard landing target coordinates
- BST autopilot will receive relative coordinates to fine-tune flight path
- Target accuracy: 0.1 m in no-wind conditions
- Testing planned for moving platform simulating shipboard operations

### Ground Control Station
- Integration of Quad-Biplane algorithms into SwiftTab ground flight controller UI
- Features for operators to plan, monitor, and execute autonomous mission profiles
- Significant codebase refactoring to support VTOL as third vehicle type

### Integration & Testing
- Working with Creare to identify suitable avionics and radios
- Flight test plan includes local testing near Boulder, CO, and Beyond Visual Line of Sight (BVLOS) testing at Griffiss UAS test site (Rome, NY)
- Initial local flights within 14 CFR Part 107 regulations; requesting waivers for >400 ft altitude
- Demonstration of all flight modes including precision landings on moving platform
- Static thrust stand testing of motors on Double Eagle aircraft

## Products & Capabilities Described

### SwiftPilot Autopilot
- Existing fixed-wing flight control system adapted for VTOL operations
- Supports multiple flight modes and autonomous navigation
- Implements attitude control, state management, and mission execution

### SwiftTab UI (Ground Control Station)
- Mission planning and flight monitoring interface
- Waypoint creation with radius parameters for orbit/hover
- Multiple mapping pattern generation:
  - **Zamboni mapping**: Minimum-distance coverage patterns with 3D terrain avoidance
  - **Sequential mapping**: Sequential leg execution with feasible path generation based on aircraft turn rate
  - **Volumetric mapping**: Multi-layer altitude mapping (e.g., volcano trace gas sampling)
- Additional atmospheric sampling plans: helical and long-baseline repeated patterns
- Full flight simulation capability showing takeoff, transition, cruise, orbit, and landing phases

### Double Eagle Aircraft
- VTOL-capable quad-biplane platform being equipped with BST autopilot
- Motor testing performed on static thrust stand
- Parachute recovery system planned

## Use Cases & Applications

### Primary Mission
- Autonomous shipboard operations from moving platforms (Navy/NOAA application)
- VTOL takeoff/landing on naval vessels

### Secondary Capabilities Demonstrated
- **Mapping surveys**: Terrain mapping with intelligent obstacle avoidance
- **Atmospheric sampling**: Volcanic trace gas sampling with multi-layer altitude profiles
- **Precision geolocation**: Helical and long-baseline sampling patterns for scientific measurement
- **Beyond Visual Line of Sight (BVLOS) operations**: Autonomous navigation without operator line-of-sight

## Key Results (Month 10)

### Navigation Performance
- New reduced-state controller showed significant improvement over full-state controller
- Eliminated "curvy" tracking paths from previous control approach
- Simulation validation across full flight envelope: takeoff → transition → forward flight → orbit → return → transition → landing

### Demonstrated Capabilities
- Seamless transitions between all flight modes (mapping, square flight plan, orbit, landing)
- Successful execution of all mapping types in forward flight mode
- 3D terrain avoidance functioning in complex topography
- Automated path generation based on aircraft turn rate and wind direction considerations

### Simulation Test Results
- Full 4-phase mission executed: takeoff + transition to forward + orbit + flyback + transition + land
- Landing alignment logic functions (aircraft creates trajectory to land in optimal wind direction)
- Mission interruption and transition to alternate plans (mapping → square pattern → orbit) executed smoothly

## Notable Details

### Project Status
- Schedule on pace for completion; most tasks on schedule for end of April 2020 (testing) and May 2020 (project conclusion)
- Final demonstration moved to Colorado due to travel restrictions (document dated March 2020, likely COVID-related)

### Remaining Milestones (as of Month 10)
- Week 1: Return old Double Eagle, integrate avionics into new aircraft, small prototype high-wind testing
- Week 2: Double Eagle ground and hover tests; prototype repeated testing
- Week 3: Parachute integration; timeline discussion
- Week 4: Double Eagle full flight envelope testing

### Technical Innovations
- Quad-Biplane vehicle type represents new platform category for BST (required SwiftTab UI refactoring to support fixed-wing, rotorcraft, and quad-biplane)
- Precision landing algorithm designed for moving platform operations (novel for UTAS systems)
- Reduced-state control approach solved practical tracking issues while maintaining stability

### Partnerships
- Creare: Primary contractor with landing detection algorithm development
- Griffiss UAS Test Site (Rome, NY): BVLOS testing facility
- NOAA: End user for aerosol sensor integration
- Navy/DoD: Implied end customer for shipboard operations capability