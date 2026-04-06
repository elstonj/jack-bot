# Enabling BLOS UAS Operations through a Diverse-Source Global Positioning System

## Document Metadata
- Type: Research Performance Progress Report (RPPR)
- Client/Agency: Department of Commerce / NOAA
- Program/Solicitation: NOAA SBIR Phase I (Topic 9.5.01)
- Date: Submitted 03/31/2020 (Reporting Period: 01/01/2020 – 06/30/2020)
- BST Products/Systems Referenced: S1, S2 (UAS platforms)
- Key Personnel: Austin Anderson (PI), Jack Elston, Maciej Stachura (BST); Phil Hall (NOAA OAR, Technical Monitor)
- Federal Award Number: NA20OAR0210087

## Executive Summary
Black Swift Technologies developed a GPS-independent positioning system (DS-GPS) for UAS operations to enable beyond-line-of-sight (BVLOS) flight in GPS-denied or spoofed environments. The Phase I effort demonstrated feasibility of combining optical flow, inertial navigation, and absolute position estimation algorithms to provide a 20Hz position update without relying on GNSS constellations.

## Technical Approach

### System Architecture
The DS-GPS module comprises four integrated components:

1. **GPS Monitoring**: Detects spoofing/jamming events and triggers system switchover; alerts aircraft and operator of GPS loss
2. **Inertial Estimation**: Fuses optical flow instrument with onboard IMU and airdata sensors (replacing insufficient MEMS-based INS on commercial UAS) to maintain position estimates between absolute corrections
3. **Absolute Position Estimation**: Machine vision algorithms and potentially RF signals of opportunity provide periodic unbiased position measurements
4. **Sensor Fusion**: Kalman filter combines high-rate inertial solution with lower-rate absolute corrections to produce integrated 20Hz position output

### Hardware Configuration
- Single integrated hardware package (form factor compatible with standard GPS units for easy integration)
- Jetson TX2 embedded computer
- IMU board with pressure sensors
- Downward-facing machine vision camera
- Expandable weight and cost margins

### Algorithms Developed/In Development

**Completed (Phase I First Half):**
- **Optical Flow Algorithm** (100%): Estimates aircraft ground speed and odometry; provides stable position estimate over 30-second window; runs at 26 FPS on embedded target
- **Sensor Fusion Algorithm** (100%): Kalman filter design using BST avionics; magnetometer heading calibrations; inertial navigation with air-data wind corrections
- **Hardware Selection & Mechanical Integration** (100%): Machine vision hardware selected and integrated into S1 and S2 aircraft

**In Progress (Phase I Second Half):**
- **Key Frame Following Algorithm** (80%): Vision-based road/coast following for absolute position correction; designed to avoid processor overload
- **SLAM Algorithm Development** (50%): Literature review completed; two algorithm candidates selected for prototype; planning to leverage publicly available code bases
- **GPS Spoofing Detection Plan**: Evaluation phase; hardware selection and simulation methodology under development
- **RF Signals of Opportunity Assessment**: Feasibility study for night/low-visibility operations using cell phone/TV tower signals

### Testing & Validation
- High-fidelity simulation developed to supplement limited flight test data (COVID-19 constraints reduced physical testing)
- Simulation generated synthetic imagery and autopilot data for algorithm prototyping
- Two dedicated flight tests plus related earlier flights provided validation data
- Post-processing of flight data used for algorithm verification and performance benchmarking on embedded hardware

## Products & Capabilities Described

### S1 and S2 UAS Platforms
- Integrated test beds for DS-GPS module hardware and software
- Carried optical flow camera, Jetson TX2 computer, and sensor packages
- Flight-tested during Phase I to gather visual-inertial odometry (VIO) data

### DS-GPS Navigation Module
- Standalone hardware payload (small enough for multiple UAS platforms)
- Provides GPS-equivalent navigation solution without GNSS
- Robust to jamming and spoofing
- Designed for affordability through COTS component leverage
- Scheduled for embedded hardware implementation and full flight testing in Phase II

### Software Deliverables
- Optical flow software (flight-proven)
- Sensor fusion Kalman filter
- Key frame following algorithm design
- SLAM algorithm designs
- Flight test and simulation datasets
- VIO data collection software

## Use Cases & Applications

**Primary Operational Context:**
- Beyond-visual-line-of-sight (BVLOS) UAS operations
- GPS-denied/jamming/spoofing environments

**Specific Applications Identified:**
- Drone delivery services (including critical/life-saving package delivery, COVID-19 pandemic relevance noted)
- Long-range pipeline inspection (energy sector environmental monitoring)
- Remote environmental monitoring
- Industrial inspection operations in national airspace system (NAS)

## Key Results

### Completed Tasks
1. Optical flow algorithm design, prototyping, HWIL simulation, deployment, and flight testing (100%)
2. Sensor fusion algorithm design and deployment (100%)
3. Machine vision hardware selection (100%)
4. Mechanical integration into S1 and S2 aircraft (100%)
5. Flight test data collection and evaluation (100%)

### Performance Achievements
- Optical flow provides stable 30-second position estimate
- Algorithm runs efficiently at 26 FPS on Jetson TX2
- Sensor fusion Kalman filter successfully demonstrated
- Key frame following algorithm nearly complete with performance benchmarked on embedded target
- SLAM candidates identified and plans developed for implementation

### Challenges & Adaptations
- **COVID-19 Impact**: Social distancing reduced flight test opportunities; compensated with expanded high-fidelity simulation work (not in original proposal)
- **Schedule Adjustment**: Task 2.1 (GPS monitoring) pushed to Phase I second half to leverage Task 2.2/2.3 (vision algorithms) completion
- **Mitigation Strategy**: Simulation work and related machine learning advances expected to recover schedule slip during road-following algorithm work

## Notable Details

### Key Competitive Advantages
- Leverages BST's proven rapid UAS design and flight-test capability (demonstrated in prior NOAA SBIR Phase I with full aircraft design and testing)
- Integrates multiple position estimation modes (optical flow, key frame, SLAM, RF signals)
- Hardware package designed for easy COTS GPS replacement in existing systems
- Combines affordability with robustness through COTS component selection

### Phase II Planned Focus
- Implementation on dedicated embedded hardware
- Full system flight testing
- GPS spoofing detection hardware and simulation methodology
- RF signals of opportunity exploitation (night/poor-visibility operations)
- Road/coast following machine learning refinement using datasets developed since proposal submission

### Broader Impact
- Positions UAS for safe NAS integration and BVLOS certification
- Enables new commercial applications (delivery, infrastructure inspection)
- Advances UAS reliability and operational flexibility
- Supports energy sector environmental monitoring and emergency services

### Program Management
- Reported to NOAA Office of Atmospheric Research (OAR)
- Technical monitoring by Phil Hall (NOAA)
- No foreign country budget allocation
- Team: 3 BST personnel (Anderson, Elston, Stachura)
- No training/professional development or dissemination activities reported for Phase I interim