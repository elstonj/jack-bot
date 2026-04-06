# All Weather UAS for Long Term Unattended Environmental Observations

## Document Metadata
- **Type:** NASA SBIR Phase II Proposal
- **Client/Agency:** NASA
- **Program/Solicitation:** SBIR 2022-II, Topic S16.04-2763
- **Date:** Submitted January 2023 (created/modified 2023-01-25 to 2023-08-03)
- **BST Products/Systems Referenced:** S2, S2-VTOL, S3 (proposed), S0-AD, E2, SwiftCore (implied via JSB simulator reference)
- **Key Personnel:** Not explicitly named in document

## Executive Summary

Black Swift Technologies proposes development of the S3 UAS, a revolutionary redesign of the existing S2-VTOL platform for all-weather operations in extreme environments (severe winds, precipitation, icing, and particulates) with autonomous multi-day mission capabilities. The S3 will feature enhanced aerodynamics for high dash speeds (45+ m/s) and climb rates (10+ m/s), weather-resistant design, advanced machine vision for autonomous landing and terrain navigation, and integrated solar charging to enable extended unattended operations spanning days to months—essentially creating a deployable aerial platform that can land autonomously, recharge, and conduct missions with minimal human oversight.

## Technical Approach

### Phase I Results Summary
BST completed three major objectives in Phase I:

**Objective 1: Aerodynamic and Propulsion Design for Strong Winds**
- Evaluated three wing/tail design options using XFLR5 modeling and flight data analysis
- Option 1: 10% performance gain over S2 using existing S3 molds with trailing edge camber
- Option 2: Complete redesign achieving 22.8% improvement in sink rate and 23.3% L/D gain vs. original S2
- Option 3: Hybrid approach replacing only outboard wing tip panels, capturing ~97% of gains with minimal mold investment
- New wing design features 1° washout for elliptical lift distribution, minimal sweep and zero dihedral
- Propulsion system analysis: S3 with 19x10E, 19x12E, or 20x10E propellers achieves 46-52 m/s dash speeds and 15-16 m/s climb rates (exceeding 45 m/s and 10 m/s targets)
- Developed mission-based control algorithms for optimized flight planning in variable wind conditions, demonstrating potential 2.25x power reduction by adjusting cruise speed based on headwind component

**Objective 2: Precipitation and Icing Design Modifications**
- Designed and tested drained pitot-static subsystem for icing and heavy precipitation operation
- Rain tunnel testing showed new pitot design maintains accuracy in moderate precipitation with only ~1 m/s IAS increase in heavy precipitation
- Aircraft waterproofing and dust-proofing modifications maintaining minimal mass increase
- Environmental design specifications: IP56 rating when assembled, IP67 for sensitive components, -40°C to +50°C operating range, 0-100% RH

**Objective 3: Onboard Intelligence/Vision System**
- Selected Luxonis OAK camera system (up to 6 cameras, 3 tera-operations/second processing) paired with Jetson Nano SBC (128-core Maxwell GPU)
- Prototype system with 2 forward-looking stereo monochrome cameras, 2 downward-looking stereo monochrome cameras, 1 downward-looking color camera
- Evaluated landing site detection algorithms: Abuzz AI's OpenLander system vs. BST proprietary semantic segmentation
- Tested SLAM-based point cloud mapping (SpectacularAI) for real-time obstacle detection on final approach
- Demonstrated automated takeoff/landing and obstacle avoidance capability in flight testing

### Proposed Phase II Work Plan

**Technical Objective 1: Strong Wind Operations**
- Flight testing and validation of aerodynamic and propulsion changes
- Implementation of new navigational capabilities to mitigate wind effects and optimize flight planning
- Development of envelope protection during VTOL transitions in high wind conditions

**Technical Objective 2: Extreme Environment Resilience**
- Completion of icing detection and mitigation system (heated pitot-static, embedded heating in leading edges and props)
- System energy monitoring augmented with visual icing detection via onboard cameras
- Completion of waterproofing/dust-proofing design across all aircraft systems
- Subsystem testing for extreme temperature operation (-40°C to +50°C)

**Technical Objective 3: Vision-Based Autonomous Operations**
- Integration and flight testing of forward and downward stereo camera systems
- Development of terrain contouring and obstacle avoidance algorithms
- Completion of automatic landing site identification and terminal guidance system
- Alternative navigation methods for GPS-denied environments using optical flow and object identification

**Technical Objective 4: Intelligent Onboard Systems**
- Solar power system design and integration for in-field recharging
- Adaptive thermal management (heating/cooling) for temperature extremes
- Expansion of machine learning-based preventative maintenance system for fully autonomous preflights and postflights
- Smart power management algorithm for multi-flight daily operations

## Products & Capabilities Described

### S3 UAS (Primary Product - Proposed)
**What it is:** Next-generation tilt-rotor VTOL UAS based on S2-VTOL platform, designed for all-weather autonomous operations in extreme environments.

**Specifications:**
- **Aircraft Type:** Tilt-rotor VTOL
- **Wingspan:** 4m (160 inches)
- **MGTOW:** 14 kg
- **Max Airspeed:** 45 m/s (100 mph) target
- **Max Winds:** 30 kts for VTOL ops, 50 kt gusts in forward flight
- **Climb Rate:** 10 m/s (2000 ft/min) max
- **Endurance:** 60+ minutes cruise (goal without solar)
- **Operating Altitude:** 20,000 ft max
- **Environmental Range:** -40°C to +50°C, 0-100% RH
- **IP Rating:** IP56 assembled, IP67 sensitive components
- **Payload:** Modular nose cone compatible with Earth-science instruments
- **Battery:** 12S Li-Ion 18650 primary propulsion pack (removable), 1S backup avionics pack
- **C2 System:** Android tablet, 900MHz ISM (other frequencies available), Iridium/cellular backup
- **Control Modes:** Manual, augmented manual (envelope protection), fully automated

**How proposed to be used:**
- Extended multi-day autonomous missions with multiple flights per day
- Autonomous landing, recharging via integrated solar panels, repositioning without operator intervention
- Operations in volcanic plumes, wildfire smoke, severe storms, hurricane periphery, precipitation, and icing
- Remote deployment in areas inaccessible to operators (e.g., volcano summits, Arctic regions)
- Continuous monitoring with long-term unattended operations

### S2 / S2-VTOL (Existing Product - Referenced)
- Proven platform with 3m wingspan for rapid weather operations
- Existing operational experience in extreme environments (volcanoes, wildfires, storms)
- Flight data and operational experience informing S3 design decisions

### Advanced Sensors & Subsystems Developed

**Drained Pitot-Static System:**
- High-accuracy heated pitot for normal operations
- Robustly designed drained pitot with heating and drainage for heavy precipitation and icing
- Dual system design provides redundancy and fault tolerance
- Rain tunnel validated; heavy precipitation testing shows <1 m/s error

**Vision System Architecture:**
- Luxonis OAK camera (6-camera capable, 3 TOPS processing)
- Jetson Nano single-board computer with 128-core Maxwell GPU
- Multiple camera configuration for 360° awareness and autonomous landing
- Semantic segmentation for landing site classification (building, car, clutter, dirt, low vegetation, road)
- SLAM-based point cloud mapping for obstacle detection

**Propulsion Options (S3):**
- Motors: KDE5215 220kV 12S
- Propellers: 19x10E, 19x12E, 20x10E (APC)
- Performance: 46-52 m/s dash, 15-16 m/s climb, ~60-86 min endurance at cruise

**Power Management:**
- Integrated solar panel system (wing-mounted)
- Smart battery charging for in-field recharging
- 20W estimated system power draw (sensors + avionics)

## Use Cases & Applications

### Historical Missions (Validation for S3 Design)

**Mission 1: Wildfire Monitoring**
- Past operations: S2 flown over controlled burns (NOAA NightFOX campaign)
- Challenges: Extreme gusts, vertical wind shear, terrain-restricted landing sites, long ingress distances
- S3 Benefits: Sustained high wind operation, autonomous landing in forest service roads, multi-day persistence

**Mission 2: Arctic Volcano Sampling**
- Past operation: S2 mission over Makushin Volcano, Alaska (Fall 2021) - 20+ mile BVLOS, 7000 ft elevation gain
- Challenges: Strong downdrafts, horizontal wind gusts caused 3 of 4 missions to turn back; icing/precipitation limited 10 of 13 campaign days; survey/sampling payload underperformed due to altitude constraints
- S3 Benefits: Increased climb/dash performance, all-weather capability, multiple collection days, autonomous multi-mission capability

**Mission 3: CO₂ Volcanic Vent Mapping**
- Past operations: Two campaigns in Costa Rica (2019 with fixed-wing S2, 2022 with quadrotor E2)
- Challenges: Rain and high winds limited mission days; jungle canopy requires low-altitude flight; landing sites difficult for fixed-wing
- S3 Benefits: All-weather capability, VTOL for low canopy operations, machine vision for obstacle avoidance in dense vegetation

**Mission 4: NEON Satellite Calibration/Validation**
- Past operations: Multiple missions at NEON ground sites (MALIBU project with NASA GSFC)
- Challenges: Requires dedicated UAS crew for each flight; difficult to achieve regular, year-round coverage
- S3 Benefits: Autonomous daily flights with zero human intervention, year-round operations including cold/wind/precipitation, reduced personnel requirements

**Mission 5: Perimeter Security (Grand Forks AFB)**
- Current operations: 40-50 UAS for inspections and perimeter security
- Challenges: High down-time due to severe North Dakota weather (cold, icing, high winds); automated operation needed for rapid deployment
- S3 Benefits: All-weather cold/icing/wind resilience, rapid autonomous launch on short notice, minimal maintenance downtime

**Mission 6: Methane Detection (Oil & Gas)**
- Commercial partnership: Local oil and gas producer
- Mission profile: Low-altitude flights over pump stations and pipelines with in-situ methane sensor; terrain obstacle monitoring required
- S3 Benefits: Maximizes flight days for area coverage, BVLOS capability for scalable monitoring of 40,000+ wells in Permian Basin alone, eventual full autonomous operations

### New Mission Opportunities Enabled by S3

**Extended Autonomous Sampling (Multi-Month Operations):**
1. **Greenland Ice Sheet Monitoring** - Multiple S3 UAS deployed for months, collecting high-resolution surface data and near-surface measurements with minimal regulatory oversight
2. **Permafrost Methane Characterization** - Large-scale Arctic tundra mapping across Alaska/Canada, integrating methane sensing with multi-month autonomous operations
3. **US Coastline Mapping** - NOAA National Geodetic Survey project: 95,000-mile US coastline could theoretically be covered in one year with reasonable S3 fleet (requires ~1,695 flights)
4. **Volcanic Monitoring & Emergency Response** - S3 positioned near active volcanoes for continuous autonomous monitoring with rapid response to eruption events; solar-powered extended operations enable landing near summits for long-term in-situ measurement

## Key Results

### Phase I Achievements

**Aerodynamic Design:**
- Wing redesign achieves 22.8% improvement in sink rate, 23.3% L/D gain vs. original S2
- 11.2% sink rate, 10.6% L/D improvement vs. existing 4m S3
- Option 3 (wing tip replacement only) captures 97% of performance gains at minimal tooling cost
- New design features elliptical lift distribution, minimal sweep, zero