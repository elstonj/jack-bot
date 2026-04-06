# All Weather UAS for Long Term Unattended Environmental Observations (S3 Development)

## Document Metadata
- **Type:** NASA SBIR Phase I Proposal
- **Client/Agency:** NASA (Earth Science Division)
- **Program/Solicitation:** SBIR 2022-I, Topic S16.04-2763
- **Date:** Submitted 2022 (created/modified 2023-06-14)
- **BST Products/Systems Referenced:** S2, S2-VTOL, S3 (proposed), S0, S0-AD, SwiftCore avionics, MultiScat, various payloads
- **Key Personnel:** Dr. Jack S. Elston (PI, CEO/Co-founder), Dr. Maciej Stachura (CTO/Lead Engineer)

## Executive Summary
Black Swift Technologies proposes development of the S3 UAS, a revolutionary redesign of the proven S2-VTOL platform engineered for all-weather operations (extreme winds, precipitation, icing, particulates) and autonomous multi-day/multi-week/multi-month unattended missions. The S3 will combine severe weather resilience with solar-powered autonomous landing and recharging capability, enabling persistent Earth-science data gathering in previously inaccessible extreme environments such as volcanic plumes, wildfires, and severe storms.

## Technical Approach

### Core Innovation
The S3 represents a dual innovation:
1. **All-Weather Capability:** Redesigned airframe for sustained operations in extreme conditions (winds up to 45 m/s / 100 mph, severe turbulence, heavy precipitation, icing, volcanic ash/dust)
2. **Persistent Operations:** Autonomous landing, onboard power management, and solar panel integration enabling continuous multi-day to multi-month missions without return to base

### Key Design Modifications

**Aerodynamic & Structural Redesign:**
- New wing and tail design optimized for high dash speeds (45+ m/s) and climb rates (10+ m/s / 2000 ft/min)
- Maintained sub-55 lbs weight class (S2-VTOL currently 33 lbs)
- Control geometry and structure sized for severe turbulence loadings comparable to hurricanes
- Efficient cruise speed ~20 m/s maintained despite performance increases

**Precipitation & Icing Mitigation:**
- New dual redundant pitot/static system:
  - High-accuracy thin pitot tube for clear-air operations
  - Secondary robust pitot with larger opening, drain hole for rain, and 3D-printed heated metal tip for icing
- Airframe waterproofing to IP55 rating (protected against dust and low-pressure water jets from all directions)
- Icing detection via atmospheric sensors (temperature/humidity monitoring) + machine vision surveillance
- Icing mitigation strategy: avoidance through altitude changes, area departure, or emergency landing (active mitigation techniques like boots/weeping wings deemed infeasible for aircraft class)

**Onboard Monitoring System:**
- Multi-camera vision system (planned for up to 5 cameras total) using Luxonis OAK platform for inference
- Forward/side-facing cameras (3) monitoring wings, rotors, pitot tube, tail for ice buildup and mechanical failures
- Downward stereo camera pair for terrain classification and autonomous landing area selection
- Integration with existing machine vision capabilities: safe-to-land system, real-time 3D terrain mapping, GPS-denied navigation (SLAM)

**Power & Autonomy:**
- Solar panels integrated into wings for autonomous battery recharge between flights
- Intelligent onboard power monitoring system
- VTOL (vertical takeoff/landing) maintained from S2-VTOL for remote deployment
- Advanced machine vision for autonomous landing spot selection in remote locations
- Capable of multiple 1-2 hour flights per day with autonomous land-recharge cycles

**Modular Design Preservation:**
- Retains S2's modular nose cone for instrument payload swaps
- Tool-less assembly maintained
- Minimal mass penalties from waterproofing via creative design techniques

## Products & Capabilities Described

### S3 UAS (Proposed)
- **Classification:** Small fixed-wing UAS with vertical takeoff/landing capability
- **Weight Class:** <55 lbs
- **Endurance:** Currently 90+ minutes cruise (S2-VTOL baseline); Phase II will quantify with solar panels
- **Dash Speed:** 45+ m/s (100+ mph)
- **Max Climb Rate:** 10+ m/s (2000+ ft/min)
- **Cruise Speed:** ~20 m/s (optimal efficiency)
- **Operational Environment:** Extreme winds, heavy precipitation, icing conditions, volcanic ash, dust, severe turbulence
- **Payload Capacity:** Up to 5 lbs scientific instruments (modular nose cone)
- **Autonomous Capabilities:** GPS waypoint navigation, BVLOS operations (demonstrated to 25 km), autonomous landing and terrain selection, solar recharge, multi-day unattended operation

### S2 UAS (Baseline)
- **Status:** Proven operational system with hundreds of missions
- **Configuration:** Fixed-wing, electric propulsion
- **Proven Deployments:** 
  - High-altitude CO₂ sampling in Greenland (<-25°C)
  - Landsat calibration (grassland, desert, alpine forest)
  - Volcanic plume sampling (Turrialba/Costa Rica, Fissure 8/Hawaii, Makushin/Alaska)
  - Arctic emissions measurement
- **Payload Capacity:** 12 unique instruments tested, modular nose cone design
- **Operational Range:** BVLOS to 25+ km demonstrated

### S2-VTOL UAS (Baseline)
- **Key Feature:** Vertical takeoff and landing capability (basis for S3)
- **Weight:** 33 lbs
- **Current Capabilities:** Dust/volcanic plume resistance, modular payload design

### S0 & S0-AD UAS
- **S0-AD:** Air-deployed minimal UAS for NOAA hurricane deployment from P3
  - Cruise endurance >1 hour with high dash speed
  - Designed for strong wind hurricane environments
- **S0 (reusable variant):** Land-based extreme wind platform
  - Developed under Air Force SBIR
  - Flight-proven in very strong winds and turbulence
  - Atmospheric profiling capability
  - Follow-on investment planned for landfalling hurricane sampling

### SwiftCore Avionics
- **Description:** Distributed, modular avionics architecture
- **Concept:** Entire electro-mechanical system viewed as sensor network with independent lifetime monitoring
- **Current Integration Status:** TRL 5 overall (component TRL 2-8)
- **Capabilities:** Real-time failure detection, mitigation, and impending failure warnings across motors, speed controllers, actuators, sensors

### Additional Technologies (Supporting S3, Various TRL)
- **Redundant Satellite Comms Board (TRL 8):** Dual wireless + satellite link monitoring with automatic failover; validated on S2 Aleutian Islands mission (2021)
- **Safe-to-Land System (TRL 5):** Machine vision semantic segmentation classifying terrain into 11 categories (roads, people, cars, forests, grassland, etc.); identifies safe landing corridors and "safe-to-crash" alternatives; real-time processing <1 second
- **Wind-Based Planning (TRL 4):** Flight path planning leveraging wind knowledge for feasibility and efficiency
- **Onboard Monitoring/Health System (TRL 5):** Machine learning-based reliability tracking for maintenance prediction and failure avoidance

## Use Cases & Applications

### NASA Earth Science Missions (Proposed S3 Applications)

**Volcanic Monitoring & Sampling:**
- Autonomous persistent observation at active volcanoes
- Remote deployment near volcanic vents with autonomous landing capability
- Long-duration trace gas sampling (CO₂, SO₂, H₂S) downwind of plumes
- Thermal and visible imaging of calderas
- Ability to reposition autonomously as wind shifts plume location
- Example: Multi-day campaign analyzing spatial scaling effects on surface albedo over Arctic shrub/boreal forest (proposed MALIBU sensor integration)

**Severe Storm & Hurricane Research:**
- In-situ atmospheric profiling (wind, temperature, humidity, pressure) in extreme turbulence
- Data collection with minimal down-time due to weather
- Improved validation for weather and hurricane intensity models

**Wildfire Monitoring & Tracking:**
- Smoke plume characterization
- Real-time fire behavior observation
- Multi-day persistent surveillance capability

**Satellite Calibration & Validation:**
- High-resolution ground-truth data collection for satellite-derived products
- On-demand operations near satellite overpass windows
- Improved validation of satellite albedo and reflectance anisotropy products (heterogeneous Arctic landscapes)

**Atmospheric Chemistry & Pollution:**
- Cloud sampling and characterization
- Air quality monitoring
- Validation of satellite instruments (CALIPSO, Aura, CATS, OCO-2/3)

**Arctic Operations:**
- Multi-month unattended campaigns with regulatory waiver/platform certification
- Large-area coverage over weeks/months
- MALIBU sensor deployment for Arctic albedo/reflectance studies

**Remote Operations Under Communication Constraints:**
- Deployment near active volcanoes within Temporary Flight Restrictions (TFRs)
- Remote launch/operation via satellite link (telemeter capability demonstrated on S2, Aleutian Islands 2021)
- Minimal operator training requirement; fully automatic unattended operations

### Commercial Applications (Planned)

**Methane Leak Detection:**
- Inspection of 40,000+ wells (Permian Basin alone)
- 100s of miles of pipeline per day coverage
- Addresses scalability limitations of current multirotor VLOS operations
- Regulatory development: BST has conducted BVLOS missions (20+ miles)
- End goal: fully unsupervised operations for economical monitoring

**Infrastructure Monitoring:**
- Powerline inspection
- Rail line monitoring
- Pipeline surveillance

**Mapping & Surveying:**
- LiDAR integration
- High-resolution remote sensing

## Phase I Technical Objectives

**Objective 1:** Complete new wing and tail design with aerodynamic analysis (XFLR5, AVL tools) and structural CAD model for high dash speeds (45+ m/s), climb rates (10+ m/s), and severe turbulence survivability.

**Objective 2:** Design modifications for heavy precipitation and icing operations including dual pitot/static system design and full airframe waterproofing (IP55 rating) with minimal mass penalty.

**Objective 3:** Design of integrated onboard intelligence monitoring system using multiple cameras for icing detection (atmospheric + vision-based) and terrain classification for autonomous landing.

## Phase I Work Plan & Deliverables

**Task 1 - Aerodynamic Redesign (Objective 1):**
- Complete aerodynamic and structural design using XFLR5 and AVL
- CFD simulations in JSBSim with custom wind and gust models
- Structural CAD design of wings and tail
- Deliverable: Fully defined aircraft model and analysis with simulation validation by interim report

**Task 2 - Dual Pitot/Static System Design (Objective 2):**
- Sensor selection and circuit board design (two dynamic sensors, temperature/humidity inputs, heater switching control, microcontroller for failure detection/switching logic)
- Mechanical 3D-printed heated metal tip design with drain hole and large opening
- Deliverables: Three validation tests:
  1. Heating system performance (-25°C freezing protection)
  2. Rain tunnel testing of drain system and precipitation performance
  3. Flight test comparison with calibrated 5-hole probe on S2

**Task 3 - Airframe Waterproofing (Objective 2):**
- Redesign for IP55 dust/water rating
- Leverage existing BST dust mitigation techniques (3D prints with gasket spots)
- Maintain modular payload and tool-less assembly
- Deliverable: CAD design and documentation of waterproofing features

**Task 4 - Vision-Based Monitoring System (Objective 3):**
- Hardware selection study (Luxonis OAK, Coral AI tensor processing units, others)
- Camera quantity/type/rotation optimization analysis
- Mechanical and electrical integration planning
- Training data acquisition planning for icing detection
- Deliverable: Hardware list, wiring diagrams, mechanical integration plan

**Task 5 - Commercial Viability Assessment:**
- Market research and outreach to potential customers/early adopters

**Task 6 - Reporting:**
- Interim and final reports per contract requirements