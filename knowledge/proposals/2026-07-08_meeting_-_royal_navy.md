# Royal Navy Tag-up: Phase I Option

## Document Metadata
- Type: Meeting presentation / status update
- Client/Agency: Royal Navy (UK Ministry of Defence)
- Program/Solicitation: Navy SBIR - Magnetometer / Phase 1 Option
- Date: July 8, 2026
- BST Products/Systems Referenced: S0 Air-Deployed UAS, SwiftPilot, Jetson autonomy stack
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
BST presented progress on a Royal Navy Phase I Option contract focused on integrating magnetometer sensors into the S0 Air-Deployed UAS platform. The presentation covers magnetometer testing with the Bartington UAS-MAG sensor, airframe modifications for reusability and ground testing, and concurrent progress on related Navy programs (RAVEN, Hazardous Weather). Key challenges include noise characterization, custom logging electronics, and developing autonomous flight control algorithms for magnetic anomaly detection (MAD) sensor operations.

## Technical Approach

### Magnetometer Integration
- **Sensor**: Bartington UAS-MAG (selected over QuSpin alternative for smaller size)
- **Output**: X, Y, Z magnetic vector measurements at 200 Hz via DRONECAN protocol
- **Logging Method**: Converted DRONECAN to USB via adapter board; data written to .CSV during testing
- **Custom Electronics**: Developing ADC circuit and logging board to NAVAIR specifications for improved sensor performance and cleaner power delivery
- **Testing**: Characterization via ground testing rig with carbon fiber boom to mount magnetometer at variable distances; includes 1-hour baseline testing and noise spectral density analysis

### Airframe Modifications for Testing
- Modified S0-AD airframe with reinforced folding wings for repeated landings
- Replaced long-range antenna with short-range adhesive flex antenna to prevent landing damage
- Reduced weight with smaller battery pack (30-minute flight time vs. original 105-minute endurance) for gentler landings
- Ground-launch system: Elastic-driven launch rail calibrated to replicate Standard Launch Container (SLC) launch profile, enabling repeated testing without air-drop requirement

### Autonomy Stack Architecture
- **SBC (Single-Board Computer) Tier**: Runs on Jetson variants or compatible platforms; supports flight control, target prediction algorithms, mission logic, and 3D path planning
- **MCU Tier**: Current SwiftPilot flight controller
- **Integration Challenge**: Determining if autonomy algorithms (autopilot, MAD sensor search, dynamic path planning) fit within onboard processor TOPS budget per SBIR award constraints

## Products & Capabilities Described

### S0 Air-Deployed UAS
**Overview**: Small, low-cost, modular electric fixed-wing UAS originating from SBIR grant for air deployment via P-3 Orion Common Launch Tube or hand-launch from aircraft

**Specifications**:
- Max Takeoff Weight: 2.75 lbs
- Wingspan: 32.5 inches
- Flight Ceiling: 15,000 ft
- Cruise Speed: 40 mph
- Max Speed: 100 mph
- Flight Time: 105 minutes nominal
- Max Winds Endured: 50 mph
- Payload Capacity: 100 grams
- Nose Cone Diameter: 1.8 inches

**Sensor Options**: Air temperature, 3D wind speed/direction, dewpoint, atmospheric pressure, laser altimeter, thermal IR, EO/IR cameras, laser target designators

**Proposed Use**: Magnetometer platform for naval ISR, particularly for magnetic anomaly detection (MAD) searches; all-weather tactical ISR at the edge

### SwiftPilot
- Current MCU-tier flight controller for S0-AD
- Being integrated with higher-level autonomy algorithms on Jetson platforms
- Under development for integration into additional Navy programs (Hazardous Weather program)

## Use Cases & Applications

1. **Magnetic Anomaly Detection (MAD)**: Primary application; autonomous search algorithms for detecting subsurface magnetic signatures (implied submarine detection context)
2. **Tactical ISR**: Air-deployed reconnaissance at the tactical edge from maritime patrol aircraft
3. **Naval Operations**: Arctic and all-weather maritime domain awareness
4. **Multi-platform Operations**: S0 swarm testing (5 aircraft used in NOAA clear air testing; 2 dual-UAS flights demonstrated)

## Key Results (Phase I Option Progress)

### Magnetometer Testing
- Successfully implemented firmware enabling DRONECAN output logging from Bartington UAS-MAG
- Custom ADC circuit designed to NAVAIR specifications; one unit sent to NAVAIR for testing in femto-Tesla measurement cell
- 1-hour and 30-minute ground baseline tests completed with noise spectral density analysis
- Bartington sensor confirmed significantly smaller than QuSpin alternative

### Airframe Modifications
- Ground-launch rail analyzed and designed; launch acceleration profiles documented (G-force, velocity, distance, time plots provided)
- Reinforced folding wing structure validated for repeated landings
- Portable elastic-driven launcher operational, enabling repeatable testing without air-drop logistics

### Related Program Progress
- **NOAA Program**: Wrapped up Clear Air Testing with 5 S0 aircraft, 10 total hours air time; 2 dual-UAS flights completed; 1 aircraft recovered; production on track for 2026 delivery
- **RAVEN Program** (Lockheed Martin workshare):
  - BST responsibilities ongoing
  - Target: Air-drop capable drone Q2 2027 (likely with non-fully-functional payload initially)
  - Coordinating with LM on algorithm integration and processor capability

## Notable Details

1. **Reusability vs. Design Philosophy**: S0-AD normally single-use air-deployed system; Phase I modified version sacrifices range/endurance for testing reusability, allowing gentler landings and repeated flights

2. **Ground Testing Infrastructure**: Custom integrated testing rig (modified aircraft with Raspberry Pi data logging) enables independent magnetic signature characterization with variable sensor standoff distances

3. **Autonomy/AI-ML Trade Study**: Open question regarding split workload between autonomous flight control and tactical AI/ML algorithms; evaluating whether integrated MAD search + 3D path planning can execute within Jetson TOPS constraints specified in SBIR award

4. **Multi-Platform Approach**: Jetson-agnostic SBC tier allows flexibility in processor selection; backwards compatible with current MCU-based SwiftPilot

5. **International Naval Interest**: Royal Navy engagement indicates interest in air-deployed UAS for maritime operations; UK MoD validation of concept

6. **Sensor Selection Rationale**: Bartington UAS-MAG chosen over QuSpin primarily for form-factor and integration advantages on 100-gram payload budget, despite requiring custom DRONECAN-to-USB adaptation