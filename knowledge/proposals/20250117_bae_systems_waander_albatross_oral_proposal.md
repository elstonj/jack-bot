# Wind-powered Autonomous Albatross-like Navigation Developed for Endurance and Range (WAANDER)

## Document Metadata
- Type: DARPA Albatross Program Oral Proposal Presentation
- Client/Agency: DARPA
- Program/Solicitation: DARPA Albatross
- Date: January 16, 2025
- BST Products/Systems Referenced: SwiftCore Flight Management System, SwiftFlow, SwiftPilot, SwiftTab UI, S0 production s-UAS
- Key Personnel: Dr. Jack Elston (BST SHCS Lead), Dr. Maciej Stachura (BST I&T Lead), Dr. Frank Stolle (BAE PI), Spencer Lisenby (Test Pilot/Consultant)

## Executive Summary
WAANDER proposes a wind-powered autonomous small uncrewed aircraft system (s-UAS) that harvests energy from atmospheric soaring conditions to enable persistent, long-endurance missions. Led by BAE Systems as prime with Black Swift Technologies and NSF NCAR as key subcontractors, the $9.35M program develops integrated planning, sensing, and control systems to predict soaring opportunities, navigate efficiently through thermal/ridge/dynamic soaring conditions, and execute extended-range missions over land and ocean environments.

## Technical Approach

### System Architecture
The proposal integrates three major technical components:

1. **PF2P (Preflight Planning Perk)**
   - Microscale weather prediction using NSF NCAR's FastEddy™ model at 25 m grid resolution across 100 km × 100 km zones with 100 vertical levels
   - Multi-objective shortest-path search using adapted versions of BAE's TRL 5 Terrain Flight Auto-Router (TFAR) and TRL 9 Multi-Asset Scheduling, Tasking, and Routing (MASTR) solver
   - Graph-based planning with nodes mapping energy harvesting regions and edges encoding transitions
   - Produces operating airspaces and flight profiles parameterized for onboard execution
   - Integration into BST SwiftTab™ UI baseline with cloud-based mission planning workflow
   - Achieves 44% energy reduction in sample planning scenarios (32.1 Wh vs 73.1 Wh baseline)

2. **SHCS (Sensing, Hardware, Control System)**
   - All-weather baseline avionics proven at TRL 9
   - SwiftPilot high-performance flight control baseline (S0 production for NOAA)
   - SwiftFlow 3D wind probe with high-rate (~100 Hz) altimetry and 3D wind sensing
   - Novel Newton-based extremum-seeking controller for dynamic soaring
   - 3D stereo vision for real-time sea surface estimation using physics-driven CNN model
   - On-board mission planner with compact soaring condition graph
   - Fast (~25 Hz) 3D stereo vision for local (~50 m range) obstacle detection
   - Integrated flight safety system

3. **Hardware Platform**
   - 10 x NAN Compass s-UAS airframes designed in collaboration with world-record dynamic soaring pilot Spencer Lisenby
   - Cost: $25K per platform/avionics/case
   - Equipped with BST SwiftCore avionics
   - Integrated sensor suite: dual GPS, IMU, altimeter, magnetometer, 3D wind probe, stereo vision, laser range finder

### Soaring Condition Coverage
Development targets progressive capability across:
- **Test Event 1**: Thermal, ridge, wave, and dynamic soaring over 2,000 sq miles (land-based)
- **Test Event 2**: Ocean dynamic soaring over 500 sq miles with sea surface sensing
- **Test Event 3**: Combined land and ocean operations over extensive areas

### Development Approach
- BST simulation tools integrate NCAR predictive weather models for algorithm optimization
- Flight-test-heavy iterative prototyping with continuous validation against metrics
- Over 100 testing days allocated combining manual and automated soaring flights
- Two competition pilots on team for rapid progression from data gathering to refinement

## Products & Capabilities Described

### SwiftCore™ Flight Management System
- End-to-end avionics solution for fully autonomous UAS flight
- Enables control, communication, and commanding of UAS
- Modular design with open interfaces for easy integration
- Firmware and software designed for rapid updates
- Only known s-UAS 3D wind probe operating in heavy rain
- Successfully deployed on S0 production aircraft for NOAA

### SwiftFlow
- 3D wind measurement system
- Validated against NIST towers
- Deployed on 17 S0 s-UAS in four hurricanes
- Measured maximum wind speeds of 209 knots (record-breaking)

### SwiftTab™ User Interface
- Cloud-based mission planning and execution monitoring
- Supports mission ingress zones, objectives, timing/airspace constraints
- New extensions for route alternatives, energy profiles, microscale weather prediction overlays, operating airspaces, flight profiles
- Real-time plan execution and mission updates
- Auto-return and geofencing support
- Tablet-based planning capability

### SwiftPilot
- High-performance flight control baseline
- TRL 9 maturity
- Developed with NASA, NOAA, and Air Force
- Calibrated against NIST towers and radiosondes
- Used in record-breaking 2024 hurricane missions

### S0 Production Aircraft
- 17 aircraft deployed in four hurricanes
- Demonstrated world records: 105 minutes endurance, 166 nm comms range, 209 knot wind speed measurement

## Use Cases & Applications

### Military Applications
- Persistent ISR over large areas
- Anti-access/area-denial (A2AD) persistent missions
- Efficient ISR using wind-powered energy harvesting

### Scientific & Research
- Atmospheric sensing and scientific research
- Volcano monitoring (demonstrated in Aleutian Islands - 20+ mile flights using ridge soaring)
- Wildland fire monitoring
- Tornado and hurricane sampling
- Oceanographic research

### Civilian & Emergency Response
- Zero-logistics awareness in remote places (poles, oceans, deserts)
- Emergency and humanitarian response
- Oil and gas exploration (commercial roadmap)
- Agricultural applications

### Space Exploration
- Long endurance missions on Mars and Venus (referenced in Elston21)
- Venus exploration: entry via aeroshell, parachute descent, multiple s-UAS operations

### Demonstrated Performance
- Africa to North Atlantic routes: 20 days, 12,000 km range using wind fields
- Hurricane missions: 2024 season set world records vs. 2023 Anduril Altius-600 performance

## Key Results & Historical Performance

### 2024 Hurricane Missions (Record-Breaking)
- Endurance: 105 minutes
- Communications range: 166 nautical miles
- Maximum wind speed measurement: 209 knots
- Platform: 17 S0 s-UAS deployed in four hurricanes

### Prior Demonstration Achievements
- Multiple NASA and USGS volcanic sampling missions in Aleutian Islands using ridge soaring
- Extreme operations in Arctic and volcanic conditions
- Simulation-aided development of extrema-seeking control for riding hurricane eyewalls
- Validated baseline sensor suite and energy-aware flying in demanding environments

### FastEddy™ Validation
- Validated against Perdigão Field Data LIDAR measurements
- Spectral analysis shows FastEddy predictions (red) match observations (black) at small scales critical for soaring cues
- Extensive literature validation through peer-reviewed publications

## Program Milestones & Schedule

### Key Test Events Over 24-Month Performance Period
1. **System Checkout (6 months)**: Baseline integration, safety validation
2. **TE-1 (12 months)**: Land-based thermal, ridge, wave, and dynamic soaring over 2,000 sq miles
3. **TE-2 (18 months)**: Ocean soaring over 500 sq miles with sea state sensing
4. **TE-3 (24 months)**: Combined land/sea operations

### Major Milestones & Payments
- Month 1: Kickoff ($1,172,722)
- Month 3: Interim Report ($532,018)
- Month 6: TE-0 System Checkout ($637,531)
- Month 8-22: Practice test events and main test events with associated payments
- Month 24: Final Report & Software TDP ($216,754)

### Total Budget: $9,349,264
- BAE Systems: $4,807,115 (51.4%)
- Black Swift Technologies: $3,586,486 (38.4%)
- NSF NCAR: $831,224 (8.9%)
- BAE Consultants: $124,439 (1.3%)

## Key Performance Metrics

Program uses 12 primary metrics tracked throughout test events:

| ID | Metric | Target |
|----|--------|--------|
| 1 | Energy use reduction | Above 75% |
| 2 | Accuracy of predicted energy use | 85%-115% |
| 3 | Mission completion | 100% |
| 4 | Baseline onboard energy use | <400 Wh |
| 5 | Albatross-enabled onboard energy use | <100 Wh |
| 6 | Predicted mission energy use | <100 Wh |
| 7 | Distance to target (extended range) | <10 m |
| 8 | Total time elapsed (extended range) | Within allotted time |
| 9 | Distance to station at on-station time | <50 m |
| 10 | Average distance from loitering pattern | <10 m |
| 11 | Max distance from loitering pattern | <50 m |
| 12 | Time elapsed in loitering pattern | Above minimum assigned |

## Notable Details

### Team Composition & Key Expertise
- **BAE Systems (Prime)**: 30+ years deploying operational mission planning systems; 40+ years designing/certifying fly-by-wire systems; 150+ million flight hours in production fly-by-wire systems
- **Black Swift Technologies**: Founded 2011; world-record holder in turbulence sensing; exclusive avionics provider; 15+ years operating s-UAS in extreme conditions
- **NSF NCAR**: World-class atmospheric research center; FastEddy® validated across multiple applications
- **Key Consultants**: 
  - Dr. Francesco Ventura (WHOI): Pelagic seabird expert with 5+ decades of tracking data
  - Prof. Joao Hespanha (UCSB): Controls/optimization expert with 54K+ citations
  - Spencer Lisenby: World-record dynamic soaring pilot

### Competitive Advantages
1. **TRL 9 Baseline Avionics**: Immediately integrable systems with proven performance
2. **World-Record Performance**: 2024 hurricane missions outperformed 2023 Anduril Altius-600 baseline
3. **All-Weather Capability**: Only known s-UAS 3D wind probe operating in heavy rain
4. **Validated Weather Prediction**: FastEddy microscale predictions extensively peer-reviewed and field-tested
5. **Experienced Test Team**: Over 100 testing days allocated; two competition pilots; former Air Force test pilots
6. **Access to Premium Test Sites**: Colorado FAA-approved sites up to 5,000' over 20×20 mi areas; California ocean/ridge sites

### Commercial Transition Pathways
- Wind energy-aware military/commercial mission planning (BAE)
- New sensors/payloads enabled by wind-powered flight (BAE)
- s-UAS sensing and avionics commercialization (BST)
- FastEddy commercial aviation applications (NCAR)
- Ocean current-aware AUV planning systems (BAE)
- Oceanographic/seabird research with long-endurance s-UAS (Ventura/BST)

### Data Rights & Deliverables
- **GPR**: BAE Systems retains government purpose rights for PF2P and route planning algorithms
- **SBIR**: BST retains rights to SwiftCore and UAS simulation environment
- Deliverables include SW source code, test readiness reviews, test reports, final report with technology development plan

### Regulatory & Safety Posture
- Team routinely executes FAA-regulated UAS operations
- Familiar with flight safety requirements
- Safety focus integrated throughout all operations
- Flight Safety System integrated into baseline avionics