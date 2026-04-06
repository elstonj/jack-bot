# A Novel Aerial Drone Platform for Exploration of Titan – 2019 Phase II Interim Report

## Document Metadata
- Type: Interim Report
- Client/Agency: NASA (Contract under SBIR program)
- Program/Solicitation: 2019 Phase II SBIR; Contract Number 80NSSC19C0332
- Date: June 15, 2021
- BST Products/Systems Referenced: Flight simulation environment (Gazebo-based), Python-based autopilot, JSBSim, Titan-gram atmospheric model, hardware-in-the-loop (HWIL) capabilities
- Key Personnel: Maciej Stachura (last editor)
- Partner: Creare (developing Ringlet drone airframe)

## Executive Summary
Black Swift Technologies is developing flight simulation and control systems for Creare's Ringlet drone platform, with the goal of enabling aerial exploration of Titan's atmosphere. The interim report documents progress on creating a Titan-capable flight simulator, implementing a Python-based autopilot architecture, and validating the Ringlet's flight dynamics in simulation for both Titan and terrestrial prototype variants.

## Technical Approach

**Flight Simulation Environment:**
- Extended BST's planetary flight simulation capabilities to model Titan's atmosphere alongside Earth and Venus
- Modified Gazebo simulator to ingest external atmospheric models (Titan-gram), switch between celestial bodies via command-line flags, and interface with multiple autopilot architectures
- Replaced Euler angle outputs with quaternions to handle 90° transition maneuvers without singularity issues
- Standard JSBSim was hardcoded for Earth; modifications enable dynamic planetary parameter switching (gravity, radius, oblateness terms)

**Atmosphere Modeling:**
- Developed Titan-gram web server (running on AWS at atmosphere.bst.aero) that returns JSON-formatted atmospheric data (temperature, density, pressure, lateral wind) for any Titan latitude/longitude/altitude coordinate
- Server automatically queried by Python wrapper; publicly accessible for external users

**Autopilot & Control:**
- Built Python-based APTemplate class for rapid development of specialized autopilots vs. monolithic top-down avionics solutions
- Implemented controllers for Ringlet hover, transition, and position-hold flight modes
- Developed customized attitude control algorithms for multi-rotors and tail-sitter aircraft
- Python wrapper integrates atmosphere server, autopilot (SWIL or Python-based), and JSBSim via single command-line interface

**Hardware Integration:**
- BST to integrate autopilot hardware and ground station equipment into terrestrial prototype built by Creare
- Hardware-in-the-loop simulation planned prior to full flight testing

## Products & Capabilities Described

**Titan-gram Atmospheric Model:**
- Web-accessible JSON API returning: latitude, longitude, altitude (validation), temperature (K), density (kg/m³), pressure (Pa), lateral wind (m/s)
- Accessible at: atmosphere.bst.aero/titan_gram/<lat>/<lon>/<alt>

**JSBSim Modifications:**
- Ingestion of external atmospheric models
- Quaternion attitude output (vs. Euler angles)
- Command-line celestial body selector (Earth, Titan, Venus currently)
- External autopilot interface via XML input/output ports
- Multi-rotor and aerosurface control inputs supported

**Python-Based Autopilot:**
- APTemplate class enables aircraft-specific implementations (ringlet_hover, fixed-wing variants tested)
- Rapid iteration and algorithm testing capability
- Shareable codebase architecture (vs. proprietary black-box systems)

**JSBInterface.py Wrapper:**
- Single-command simulation execution: `./JSBInterface.py --aircraft ringlet --init reset01 --import-ap-script ap_scripts.ringlet_hover --atmosphere titan_gram --realtime`
- Integrates all simulation components (aircraft selection, initialization, autopilot script, atmosphere model, planetary parameters, real-time flag for HWIL)

## Use Cases & Applications

- **Titan Aerial Exploration:** Ringlet drone designed to operate in Titan's dense nitrogen atmosphere (1.5 bar pressure, -179°C), performing autonomous missions (hover, transition, horizontal flight, precision landing)
- **Terrestrial Prototype Validation:** Sub-scale ring-wing prototypes flown in Boulder, CO to validate simulation models and demonstrate all flight modes as analog to Titan operations
- **Mission Scenarios:** Fixed-altitude hover, position hold, aggressive pitch maneuvers, transition between vertical and horizontal flight, autonomous mission execution

## Key Results (Interim)

**Completed this reporting period:**
1. Titan-gram web server operational and publicly accessible
2. Gazebo modifications validated for external atmosphere ingestion, quaternion outputs, celestial body switching, external autopilot interface
3. Python-based APTemplate autopilot class implemented and tested for Ringlet and fixed-wing variants
4. JSBInterface.py wrapper validated with integrated command-line control
5. Initial Ringlet hover and position-hold simulations run on Titan model (46 kg airframe, starting from horizontal orientation)
   - Good tracking observed on position, altitude, vertical rate, position hold
   - Rotor thrust generation lower than expected (flagged for further refinement)
6. Aggressive pitch maneuvers and transition-back simulations completed successfully

**Remaining project milestones:**
- Complete simulation environment models (month 5) – *appears complete per interim results*
- Complete drone flight dynamics models (month 11)
- Complete avionics integration with terrestrial prototype (month 13)
- Obtain flight permission via NASA Airworthiness and Flight Safety Review Board, Flight Readiness Review Board (month 13)
- Complete terrestrial flight testing (month 16)

## Notable Details

- **Multi-planetary capability:** BST extended simulation to Earth and Venus analogs, enabling pre-flight testing and algorithm validation before committing to Titan operations
- **Web-accessible infrastructure:** Titan-gram server allows external researchers/stakeholders to query atmospheric models without direct BST involvement
- **Python-based autopilot strategy:** Contrasts with traditional monolithic avionics; enables sharing with 3rd parties and rapid iteration—key advantage for collaborative research
- **Hardware-in-the-loop pathway:** HWIL testing (pre-flight validation with actual hardware running algorithms) planned before full terrestrial prototype flights
- **Ring-wing aircraft novelty:** Ringlet tail-sitter design requires novel flight control approaches (quaternion tracking, 90° transitions); standard attitude control inadequate
- **Creare partnership:** Creare responsible for ringlet airframe/mechanics; BST providing simulation, flight control, avionics integration
- **Sub-scale validation strategy:** Initial flights use existing sub-scale prototypes to validate simulator fidelity before final full-scale prototype missions
- **NASA oversight:** Project subject to NASA Airworthiness and Flight Safety Review Board approval—emphasizes mission-critical reliability requirements