# Statement of Work for Black Swift Technologies (BST) – Venus Drone II

## Document Metadata
- Type: Statement of Work (SOW)
- Client/Agency: Creare (on behalf of Venus exploration mission)
- Program/Solicitation: Venus SBIR (implied from folder structure)
- Date: November 3, 2021 (prepared); November 8, 2021 (finalized)
- BST Products/Systems Referenced: Planetary flight simulation environment, ringlet drone flight controller, autopilot hardware, ground station hardware, hardware-in-the-loop simulation capabilities
- Key Personnel: Jack Elston (last editor)

## Executive Summary
BST will develop a flight simulation environment for Creare's Venus atmospheric drone, evaluate flight performance in simulation, validate through terrestrial prototype testing, and demonstrate autonomous operations. The work spans 22 months (July 2022–June 2024) and includes flight control development, avionics integration, hardware-in-the-loop testing, and terrestrial flight testing with a 1-meter-diameter ring-wing prototype.

## Technical Approach

**Flight Simulation Models:**
- Utilize existing BST planetary flight simulation environment adapted for Venus atmospheric conditions at relevant altitudes (54 km balloon altitude to 46 km cloud deck)
- Extend unmanned aircraft models using Creare's Venus drone specifications
- Develop updated terrestrial prototype models based on ringlet drone variant
- Integrate simulated vision-based sensors for docking demonstrations

**Flight Control Development:**
- Adapt existing ringlet drone flight controller and develop customized control gains
- Customize attitude control algorithms for multi-rotor and tail-sitter aircraft
- Support flight modes: release, rapid descent, cruise, climb (>20° angles), hover, and docking
- Use simulation to develop and tune controls for both Venus and Titan drone designs

**Avionics Integration:**
- Integrate BST autopilot hardware and ground station hardware into Creare's terrestrial prototype
- Interface with airframe structure, motors, speed controllers, and relative position sensor
- Prepare avionics for both simulation and flight test environments

**Hardware-in-the-Loop (HIL) Simulation:**
- Conduct simulated flights using actual hardware before transition to flight testing
- Validate algorithms and control logic prior to physical prototype testing

**Terrestrial Prototype Flight Testing:**
- Develop detailed flight test plan in collaboration with Creare
- Obtain flight permission through NASA Airworthiness and Flight Safety Review Board and Flight Readiness Review Board
- Conduct multiple data-gathering flights at local sites using full-scale 1-meter-diameter ring-wing prototype
- Log system state parameters for model validation and analysis
- Perform final demonstration flights in Boulder, CO, showcasing all flight modes and autonomous mission execution (Venus analog behavior)

## Products & Capabilities Described

**Planetary Flight Simulation Environment:**
- Existing BST capability adapted for Venus atmospheric modeling
- Supports multi-mode flight simulation (descent, cruise, climb, docking)

**Ringlet Drone Flight Controller:**
- Mature control system from prior planetary mission work (Titan)
- Customizable for different airframe specifications and mission profiles

**Autopilot & Ground Station Hardware:**
- BST-provided avionics for autonomous flight and ground control
- Compatible with vision-based sensor integration for docking operations

**Hardware-in-the-Loop Simulation:**
- BST capability enabling algorithm validation before live flight testing

## Use Cases & Applications

**Venus Atmospheric Exploration:**
- Near-infrared imaging below Venus cloud deck (primary mission)
- Deployment from 54 km balloon altitude, descent to 46 km cloud deck
- Autonomous docking with balloon for recovery/data transmission

**Mission Phases Modeled:**
1. Balloon deployment
2. Rapid descent (approach/methodology TBD)
3. Cruise flight at target altitude
4. High-angle climb capability (>20° angles)
5. Autonomous docking with precision sting positioning

## Key Milestones & Deliverables

**Technical Milestones:**
- Month 5 (Dec 2022): Complete simulation environment models
- Month 11 (Jun 2023): Complete drone flight dynamics models
- Month 13 (Aug 2023): Complete avionics integration & obtain flight permission
- Month 16 (Nov 2023): Complete terrestrial flight testing

**Reporting Deliverables:**
- Quarterly progress reports: Sept 14, Dec 14, 2022; Mar 14, Jun 14, Sept 14, Dec 14, 2023; Mar 14, 2024
- Final Report: May 21, 2024

**Physical Deliverables:**
- Simulation environment (Venus atmosphere models, drone dynamics models, sensor simulations)
- Integrated avionics package (autopilot + ground station)
- Flight test data and analysis
- Validated flight control algorithms

## Notable Details

- **Docking Mechanism:** Creare provides prototype docking mechanism and vision-based short-range position/pose sensor; BST integrates into avionics
- **Prototype Scale:** 1-meter-diameter ring-wing airframe (full-scale terrestrial prototype)
- **Navigation:** GPS for terrestrial prototype; vision-based docking sensor for precision positioning
- **Prior Experience Leveraged:** Titan drone development (control algorithms, simulation environment, flight controller maturity)
- **Collaboration Model:** Joint meetings with Creare; Creare provides airframe, mechanisms, sensors; BST provides flight control, simulation, avionics integration, and testing expertise
- **Regulatory Path:** Includes NASA flight safety review and airworthiness approval process

---

**Period of Performance:** July 20, 2022 – June 7, 2024 (22 months)