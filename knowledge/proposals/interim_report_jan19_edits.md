# Sensor Fusion and Algorithms for Mapping at Low Altitude Above Rugged Terrain

## Document Metadata
- **Type**: Interim Report (Phase I)
- **Client/Agency**: NASA
- **Program/Solicitation**: SBIR 2018-I, Topic A2.02-9342
- **Date**: January 2019
- **BST Products/Systems Referenced**: S2 UAS
- **Key Personnel**: Dr. Stachura (PI), Dr. Elston, Mr. Anderson

## Executive Summary
This interim report documents Phase I progress on developing terrain-following and obstacle-avoidance capabilities for the Black Swift S2 fixed-wing UAS operating at low altitudes over rugged terrain. Work completed includes mission requirements analysis, sensor selection and evaluation, algorithm identification, and development of system concepts of operation. The project addresses operational needs identified across multiple mission types including CO₂ sampling, soil moisture mapping, volcano monitoring, and arctic operations.

## Technical Approach

### Mission Analysis
- Analyzed historical flight scenarios and upcoming missions to derive mission requirements
- Identified eight mission categories: safe takeoff/landing, canopy sampling, farm sampling, mountain sampling, volcano sampling, arctic sampling, ocean sampling
- Created obstacle matrix categorizing 21 obstacle types by frequency, severity, size, and height
- Established system requirements: minimum 10 m AGL, maximum 50 W power draw, ≤1 kg mass (500 g goal), ≤$10,000 cost

### Sensor Selection Process
- Evaluated 10 sensor types: 1D laser, LIDAR, automotive radar, radar development kits, single camera, stereo cameras (stock and custom), structured light, thermal camera
- Derived three-zone coverage architecture:
  - **Long Range**: 100 m maximum range, 50 cm resolution, 45° x 17° FOV, 5 Hz update
  - **Short Range**: 50 m maximum range, 5 cm resolution, 60° x 20° FOV, 20 Hz update
  - **Downward**: 100 m range, 5 cm resolution, 45° x 45° FOV, 20 Hz update
- Conducted kinematic analysis of climb-out and turn-out avoidance maneuvers to validate sensor requirements

### Proposed Sensing Package (Primary Configuration)
**Sensors:**
- RDK-S32R27 radar development kit (forward-facing, long-range): 51 x 76 x 30 mm, 100 g, 4 W, $3,500
- MC050CG-SY stereo camera pair (forward-facing, short-range): 2 units, 76 g total, 5.7 W total, $3,330
- LightWare LW20/C 1D laser pair (downward-facing, downward coverage): 40 g total, 1.1 W total, $740
- MC050CG-SY single camera (downward-facing): 38 g, 2.85 W, $1,665
- Lenses: 135 g, $510
- **Processing**: Jetson TX2 embedded GPU: 50 x 87 x 40 mm, 185 g, 7.5 W, $725

**Total**: 574 g, 21 W, $10,470

**Lower-Cost Alternative:**
- µSharp patch radar ($700), lower-resolution cameras (LI-USB30-C570X at $699 each)
- Total: 344 g, 12.93 W, $3,892

**Ground-Truth Alternative:**
- OS-1 16 LIDAR (380 g, 16 W, $3,500) for validation data collection

### Algorithm Development
Identified four algorithm categories for Phase II:

1. **Machine Vision**: Stereo depth computation via epipolar geometry; push-broom stereo approach; structure-from-motion; visual odometry and optical flow
2. **Sensor Fusion**: Extended Kalman Filters (EKFs), modified SLAM with short time history, multiple hypothesis tracking
3. **Obstacle Detection & Tracking**: Voxel-based obstacle aggregation, track expiration logic
4. **Obstacle Avoidance**: Hierarchical discrete controller selection (standard climb, aggressive climb, standard turn, aggressive turn, bail-out); path projection and collision prediction

## Products & Capabilities Described

### S2 UAS Platform
**Specifications:**
- Payload capacity: 2,268 g (5 lbs)
- Cruise speed: 18 m/s
- Maximum speed: 30 m/s
- Stall speed: 12 m/s
- Maximum altitude: 4,267 m AMSL
- Maximum AGL: 300 m
- Standard turn radius: 108 m
- Aggressive turn radius: 51 m
- Standard climb rate: 17.6 m over 100 m
- Aggressive climb rate: 32.5 m over 100 m
- Maximum sustained wind: 10 m/s

**Existing capabilities:**
- Downward-facing 1D laser for AGL estimation
- GPS, IMU, magnetometer, static/dynamic pressure, air temperature sensors
- Optional camera for machine learning/photogrammetry
- Automated landing and takeoff modes

### New Proposed Capabilities
- Real-time obstacle detection at long range (100 m) and short range (50 m)
- Terrain-following mode: maintains commanded AGL with dynamic ground-level estimation
- Obstacle-avoidance mode: autonomous response selection from climb-out, turn-out, or bail-out maneuvers
- Multi-sensor fusion with confidence metrics
- Processing on embedded Jetson TX2 GPU

## Use Cases & Applications

### Mission Categories Identified
1. **Safe Approach/Landing**: Automated landing with obstacle detection in vegetated/structured environments
2. **Safe Takeoff**: Detection of obstacles in takeoff corridor
3. **Canopy Sampling**: CO₂ measurements 10–30 m above forest canopy (Costa Rica case study)
4. **Farm Sampling**: Soil moisture mapping at low AGL, avoiding structures and power lines
5. **Mountain Sampling**: Terrain following over highly variable topography (Niwot Ridge, Fraser Valley)
6. **Volcano Sampling**: Operations near volcanic plumes and ridge lines
7. **Arctic Sampling**: CO₂ sampling over snowy/icy terrain (Greenland mission)
8. **Ocean Sampling**: Operations over large water bodies

### Key Operational Challenges
- Costa Rica mission: SRTM data limited resolution; CO₂ dynamics only 10–30 m above canopy; terrain highly variable
- Santa Rita landing: narrow streambed landing corridor surrounded by shrubs; pilot frequently aborted automated landings due to perceived obstacle threat
- Farm sampling: low AGL for ground-penetrating radar; need to avoid barns, utility poles, power lines not in SRTM data

## Key Results

### Phase I Completed Work (50% overall completion)
- Kickoff meeting conducted with PI, technical staff, and NASA monitor
- Mission requirements documentation finalized across eight mission categories
- Comprehensive sensor evaluation: 10 sensor types analyzed for SWaP-C and integration feasibility
- Obstacle matrix developed with 21 obstacle types classified by frequency/severity
- Three-zone coverage architecture defined with kinematic validation
- Sensing package designs proposed (three configurations at different cost/performance points)
- TX2 processing hardware procured and initial evaluation begun with Ximea camera
- Flight testing coordination with NASA Armstrong: confirmed that AFSRB review NOT required for this SBIR (no NASA payload, personnel, or aircraft directives), eliminating ~9 months delay and ~$8,000 cost

### Commercialization Activity
**IPOZ Systems LLC Contract**: $20,688 (Phase 1 of 3-phase, $46,088 total)
- Adaptation of Phase I work for underwater UAS imaging system
- Uses global-shutter block camera and TX2 processing board from this SBIR
- Deliverables: integrated camera/SBC solution, image capture at 1–30 Hz, 1 TB data storage, Ethernet access, IMU timing integration, possible machine learning on submarine

## Notable Details

### Competitive Landscape & Partnerships
- **Automotive Radar Evaluation**: Identified three radar classes:
  - Dedicated UAS radars (µSharp patch $4,995, 360° system $8,500, EchoFlight $20k): expensive, optimized for flight
  - Automotive packaged radars (Continental ARS 408-21: $3,060 single, $1,080 at 10-unit volume): 2D only, designed for highway vehicles
  - Radar development kits (~$3,500): provide flexibility, lighter weight, custom processing possible
- **Colorado Engineering Inc. (CEI) Partnership**: BST exploring commercial partnership to develop fixed-wing UAS collision-avoidance radar using CEI development kit; investigating 3D scanning and custom radar processing algorithms

### Risk Mitigation & Flight Testing
- Extensive simulation planned in Phase II to reduce flight test risk
- Gazebo-based high-fidelity environment with aircraft, terrain, obstacle, weather, and sensor models
- Emphasis on emergency procedures and risk mitigation (40 hours per team member for risk documentation)
- No AFSRB review required, enabling faster Phase II flight testing

### Financial Status (as of 10/27/2018)
- Cumulative costs: $82,296
- Physical completion: 50%
- Labor breakdown: PI (400 hrs @ $50/hr = $20,000), two engineers (563.79 hrs @ $50/hr = $28,189.73)
- Overhead (35%) and G&A (15%) included; no materials, subcontractors, or travel costs yet

### Technical Development Priorities for Phase II
1. Camera downselection based on stereo depth design and processing performance
2. S2 integration plan with CAD mockups, EMI/EMC testing
3. High-fidelity Gazebo simulation (major focus)
4. Hardware evaluation (leveraging related projects)
5. Algorithm development (terrain estimation, machine vision, sensor fusion, obstacle avoidance)
6. Flight test planning and CONOPS development

### Standards & Regulatory Coordination
- Coordination with NASA Armstrong sUAS liaison on AFSRB requirements
- Established relationships with NASA Goddard, Ames, Armstrong, and Langley for flight operations over 4 years

---

## Document Quality Notes
- Comprehensive Phase I interim report with detailed technical analysis
- Includes specific flight performance data, obstacle characterization, sensor trade studies, and kinematic validation
- Well-supported by figures, tables, and reference literature
- Clear delineation between completed (Phase I) and planned (Phase II) work