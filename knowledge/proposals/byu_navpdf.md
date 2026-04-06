# Obstacle and Terrain Avoidance for Miniature Aerial Vehicles

## Document Metadata
- **Type:** Peer-reviewed academic article
- **Publication:** IEEE Robotics and Automation Magazine, vol. 13, no. 3, pp. 34-43, September 2006
- **Institution:** Brigham Young University (BYU), Provo, Utah
- **Authors:** Stephen Griffiths, Jeff Saunders, Andrew Curtis, Blake Barber, Tim McLain, Randy Beard
- **Funding:** AFOSR (Air Force Office of Scientific Research) award numbers FA9550-04-1-0209 and FA9550-04-C-0032
- **Date:** Published September 2006
- **Related to BST:** Referenced as a background/technical reference document for a NOAA SBIR Phase I proposal (2019)

## Executive Summary
This paper presents research on autonomous obstacle and terrain avoidance for miniature aerial vehicles (MAVs) with 1-2 meter wingspans. BYU researchers developed and flight-tested methods for MAVs to navigate complex urban and canyon environments using laser rangefinders and optic flow sensors, combined with path planning algorithms and reactive avoidance strategies. The work addresses the challenge of enabling non-pilot operators to safely deploy MAVs in constrained environments.

## Technical Approach

### Path Planning
- **Rapidly-exploring Random Tree (RRT) algorithm** adapted for fixed-wing MAV constraints
- Modified RRT searches output space rather than input space to produce feasible waypoint paths
- Paths checked for turn radius, climb rate, and collision-free traversal
- Waypoint-based approach rather than trajectory tracking to account for wind disturbances

### Path Following
- **Vector field method** creates field of desired course commands to drive MAV toward path segment
- Combines linear and circular arc segments
- Uses GPS-measured groundspeed and course (accounting for wind effects) rather than airspeed/heading
- Incorporates transition regions for smooth convergence to desired path

### Reactive Obstacle Avoidance
- Heuristic algorithm using laser ranger to detect unknown obstacles
- Represents detected obstacles as cylinders with radius equal to MAV minimum turn radius
- Generates alternate waypoint paths tangent to map obstacles
- Iteratively adds map obstacles if laser re-detects during avoidance maneuver
- Mathematical bounds established on turn-away distance D to guarantee collision avoidance

### Terrain/Canyon Navigation
- Uses optic flow sensors to measure lateral distance to canyon walls
- Computes path offset δ = ½(D_right - D_left) to center MAV between obstacles
- Shifts preplanned path dynamically while maintaining vector field guidance
- Forward-looking optic sensors angled 30° ahead to reduce lag and detect obstacles earlier

## Products & Capabilities Described

### MAV Airframe
- **Dimensions:** 1.5 m wingspan
- **Construction:** EPP foam core with Kevlar covering
- **Payload capacity:** 0.4 kg
- **Endurance:** 45+ minutes
- **Cruise speed:** 10-20 m/s (22-44 mph)
- **Selected for:** Durability, usable payload, ease of component installation, flight characteristics

### Kestrel Autopilot (Procerus Technologies version 2.2)
- **Processor:** Rabbit 3400 at 29 MHz
- **Dimensions:** 3.8 × 5.1 × 1.9 cm
- **Weight:** 18 grams
- **Sensors onboard:** Three-axis rate gyros, three-axis accelerometers, absolute and differential pressure sensors
- **Data logging:** 175 kbytes at up to 60 Hz
- **Computation:** Collision avoidance algorithms executed on-board processor

### Optic Flow Sensors
- **Base sensor:** Agilent ADNS-2610 optical mouse sensor
- **Specifications:** 10 × 12.5 mm form factor, 1500 fps, 18 × 18 pixel CMOS imager
- **Light requirements:** 80 mW/m² at 639 nm or 100 mW/m² at 875 nm wavelength
- **Configuration:** Three sensors with different lens FOVs
  - Left: 6.5° FOV, 25 mm long, 30 mm lateral, 15 g
  - Center: 2.5° FOV, 35 mm long, 30 mm lateral, 23 g
  - Right: 1.2° FOV, 50 mm long, 30 mm lateral, 23 g
- **Output:** δpx and δpy (optic flow displacement in x, y directions)
- **Integration:** Connected directly to autopilot, outputs integrated over control loop period (Ts = 20 Hz)

### Laser Rangefinder
- **Model:** Opti-Logic RS400
- **Range:** 400 m
- **Update rate:** 3 Hz
- **Weight:** 170 grams
- **Power consumption:** 1.8 W
- **Note:** Non-scanning; single distance measurement, steered by airframe maneuvers

### Additional Payload
- 1000 mW 900 MHz radio modem
- 12-channel GPS receiver
- Video transmitter

## Use Cases & Applications

### Demonstrated Applications
1. **Obstacle avoidance in urban environments** - Flight test against 50 m tall Kimball Tower on BYU campus
2. **Canyon navigation** - Autonomous flight through Goshen Canyon (central Utah) with 75+ m walls
3. **Collision avoidance with single obstacles** - Building avoidance with reactive path replanning

### Potential Applications (Cited)
- Environmental monitoring (pollution, weather, scientific research)
- Forest fire monitoring
- Homeland security
- Border patrol
- Drug interdiction
- Aerial surveillance and mapping
- Traffic monitoring
- Precision agriculture
- Disaster relief
- Ad-hoc communications networks
- Rural search and rescue

### Operational Requirements Addressed
- Non-pilot operation (scientists, fire fighters, law enforcement, military personnel)
- Low-altitude flight in proximity to structures/terrain
- Urban canyon navigation
- Complex terrain/canyon operations
- Real-time obstacle detection and avoidance
- Automation of navigation to free operator focus on mission objectives

## Key Flight Test Results

### Obstacle Avoidance (Kimball Tower)
- **Scenario:** MAV directed to fly at 40 m altitude through planned path passing directly through 50 m × 35 m building
- **Performance:** Successfully detected and avoided building without human intervention
- **Behavior:** Executed two avoidance maneuvers (initial detection at 93 m distance, second detection during passing)
- **Result:** Successful autonomous avoidance, rejoined original waypoint path

### Canyon Navigation (Goshen Canyon)
- **First flight:** Planned path followed canyon road; minimal corrections needed
- **Second flight:** Intentionally biased planned path into east wall to validate self-correction
- **Performance:** MAV offset up to 10 m to center itself in canyon
- **Result:** Avoided canyon walls that would have caused crash without path offset algorithm

### Path Following in Wind
- **Wind conditions tested:** Up to 50% of MAV airspeed
- **Performance:** Vector field method demonstrated effectiveness and repeatability across four consecutive path traversals
- **Result:** Consistent trajectory tracking despite significant wind disturbances

## Technical Constraints & Design Trade-offs

### MAV Limitations Addressed
1. **Limited payload** (0.4 kg) - Precludes heavy sensors like scanning LADAR, RADAR
2. **Limited computation** - Autopilot microcontroller has limited excess capacity; cannot use PC104-based systems
3. **High speed** (10-20 m/s) - Cannot stop/slow for algorithm execution; requires immediate reactions
4. **Attitude sensitivity** - Roll/pitch motions alter sensor readings; must be compensated
5. **Catastrophic failure cost** - Crashes result in loss of vehicle and mission failure

### Solutions Implemented
- Lightweight optic flow sensors (optical mouse chips, ~15-23 g)
- Onboard processing limited to fast heuristic algorithms
- Real-time reactive algorithms (3 Hz laser, 20 Hz control loop)
- Attitude compensation in optic flow distance calculations
- Conservative safety margins (minimum turn radius = obstacle cylinder radius)

## Notable Details

### Mathematical/Theoretical Contributions
- Derived expressions for distance calculation from optic flow sensors accounting for aircraft attitude (roll φ, pitch θ, yaw rate χ̇)
- Established geometric bounds on forward distance (2√3 R) and lateral distance (√2/3 R) for path transitions
- Proved collision avoidance guarantee for flat walls with turn-away distance D > (8+2√6)/(2√3) × R ≈ 3.7R
- Derived sampling rate requirement: Ts < 2R/V × sin⁻¹(R/(2√(R²+D²))) to ensure obstacle overlap between laser updates

### Experimental Validation Sites
- **Building avoidance:** BYU campus (Kimball Tower, 50 m × 35 m, 40 m altitude)
- **Canyon navigation:** Goshen Canyon, central Utah (75+ m walls, winding terrain)

### Wind Handling
- Uses course (ground-track direction) and groundspeed instead of heading/airspeed for control
- Successfully tested with wind speeds up to 50% of airspeed
- Demonstrates robustness to typical atmospheric disturbances

### Sensor Integration Approach
- Multiple optic flow sensors with different FOVs (1.2° to 6.5°) for different distance ranges
- Forward-angled sensors (30° off centerline) to detect obstacles ahead, reducing lag
- Single point laser ranger steered by airframe maneuvers (rather than scanning)
- All sensors connected directly to autopilot for tight integration

### Future Work Implied
- Extension from single obstacle to multiple obstacles
- Handling of non-rectangular obstacles
- More sophisticated reactive planning algorithms
- Integration with improved terrain modeling
- GPS bias correction or removal

## Relevance to Black Swift Technologies
This document appears in BST's NOAA SBIR 2019 Phase I proposal references, suggesting BST leveraged BYU's pioneering work on MAV navigation and obstacle avoidance for their own proposal development. The technical approaches (optic flow sensing, laser ranging, reactive path planning) and the application domains (environmental monitoring, canyon flying) align with BST's core competencies in small UAS systems and autonomous navigation.