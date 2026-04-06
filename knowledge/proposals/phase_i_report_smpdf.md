# All Weather UAS for Long Term Unattended Environmental Observations

## Document Metadata
- **Type:** Phase I Final Report (SBIR)
- **Client/Agency:** NASA Langley Research Center (LaRC)
- **Program/Solicitation:** NASA SBIR 2022-I, Subtopic S16.04 "Unpiloted Aerial Platforms and Technologies for NASA Science Missions"
- **Contract Number:** 80NSSC22PA964
- **Date:** January 2023
- **BST Products/Systems Referenced:** S2, S2-VTOL, S3 (proposed), SwiftCore avionics, OAK/Luxonis vision platform
- **Key Personnel:** Jack Elston (PI), Maciej Stachura (Lead Engineer)

## Executive Summary
Black Swift Technologies completed Phase I of an SBIR contract to develop an "All Weather UAS" capability for long-term environmental observations in extreme conditions. The work focused on designing the S3 platform—an enhanced version of the proven S2 UAS—with new capabilities for operating safely in severe weather including high winds, heavy precipitation, icing, and turbulent conditions. Phase I achievements include aerodynamic redesigns for improved performance, a prototype heated/drained pitot-static system, weatherproofing plans, and a vision-based monitoring system design.

## Technical Approach

### Design Philosophy
BST's strategy was to leverage the proven S2 UAS platform and incrementally enhance it to create the S3 system capable of routine operations in extreme environments without concern for weather conditions. Key design objectives:

1. **Aerodynamic Redesign:** New wing and tail designs optimized for:
   - Sustained dash speed of 45 m/s (100 mph)
   - Climb rate of 10 m/s (2,000 ft/min)
   - Maintained cruise efficiency (~20 m/s optimal speed)
   - Improved L/D and reduced sink rate

2. **Severe Weather Systems:**
   - Dual redundant pitot-static system with heating for icing mitigation
   - IP55 waterproofing rating (dust/water protection)
   - Structural changes for turbulence tolerance

3. **Vision and Monitoring:**
   - Onboard machine vision for icing detection and terrain monitoring
   - Real-time 3D terrain mapping capability
   - Automated landing area detection and selection

### Technical Work Completed

**Aerodynamic Analysis (XFLR5 & AVL):**
- Redesigned wing planform with 1° washout for elliptical lift distribution
- Twin-boom inverted V-tail configuration to avoid propeller wash on fuselage
- Wing loading held constant with existing S2 (42.9 oz/ft²)
- Aspect ratio limited to 18:1 for structural and handling constraints
- New airfoil selection with 9.5% thickness at root, 8.5% at tip

**Performance Gains Identified:**
- Full redesign option: 22.8% improvement in sink rate, 23.3% in L/D vs. S2-3m (11.2% and 10.6% vs. S2-4m)
- Compromise "tip panel only" option: 97% of full redesign gains by replacing just wing tip panels
- Potential 10% additional gains from concealed linkages, construction improvements, and propulsion optimization

**S2-VTOL Prototype Development:**
- Extended wingspan by 32" to maintain wing loading with added VTOL mass (~2.8 kg increase)
- Extended tail boom by 10" with V-tail angle adjusted from 35° to 40° from horizontal
- Four rotor configuration with 1.5:1 thrust-to-weight ratio minimum
- Flight validation showed ~299W power draw at cruise (19 m/s IAS), supporting ~90-100 minute endurance with 5 lbs payload

## Products & Capabilities Described

### S2 UAS (Baseline System)
- **Description:** Proven small electric fixed-wing platform for scientific missions
- **Specifications:**
  - Mass: 9.3 kg
  - Endurance: ~90 minutes at 20 m/s cruise
  - Payload capacity: 5 lbs
  - Operating altitude: 0-14,000 ft
  - Temperature range proven: -20°C to +40°C
  - Typical power draw: 250W cruise
- **Use Cases in Phase I:** Baseline for aerodynamic analysis and flight validation testbed for new systems

### S3 UAS (Proposed)
- **Description:** Enhanced S2 with extreme weather and long-duration capabilities
- **Key Features:**
  - Redesigned wing and tail for high-speed dash and climb performance
  - Heated, dual-redundant pitot-static system for icing/precipitation
  - IP55 waterproofing for dust and water intrusion
  - Onboard vision system (5 cameras planned)
  - Solar panel integration for extended operations
  - Planned capability: weeks to months of mission duration
- **Planned Specifications:**
  - Dash speed: 45 m/s (100 mph)
  - Climb rate: 10 m/s (2,000 ft/min)
  - Cruise speed: ~20 m/s (optimized)

### Pitot-Static System (New Development)
- **Design:** Dual redundant heated pitot with selective switching
- **Components:**
  - Port 1: High-accuracy thin pitot tube for clear-air operations
  - Port 2: Larger-opening pitot with drain hole for rain/icing mitigation
  - 3D-printed metal heated tip (target: maintain >0°C down to -25°C ambient)
  - Temperature and humidity sensors
  - Automatic switching controller with microcontroller logic for failure detection
  - Heating element with thermal management
- **Validation Completed:**
  - Heating system tested in lab environment
  - Rain tunnel testing performed showing drain system functionality
  - Flight comparison tests planned with calibrated 5-hole probe on S2

### Vision System (Machine Vision Monitoring)
- **Core Hardware:** OAK/Luxonis platform (selected after evaluation)
- **Planned Camera Configuration:** 5 total cameras
  - 3 wing/tail monitoring cameras for icing detection (full field of view coverage)
  - 2 downward-looking stereo cameras for terrain mapping and landing
- **Capabilities:**
  - Real-time 3D terrain model generation
  - Automated landing area detection and classification (11 terrain classes)
  - Icing detection via visual monitoring plus atmospheric sensor fusion
  - GPS-denied navigation using SLAM algorithms
  - Forward-looking obstacle detection and tracking
- **Processing:** Jetson Nano single-board computer with Luxonis inference engine; evaluation of Coral AI tensor processing units

### SwiftCore Avionics System
- **Description:** Distributed, modular onboard monitoring architecture (separate from this SBIR but integrated into S3 plans)
- **Capabilities:**
  - Monitors all critical electromechanical systems as sensor network
  - Real-time failure detection and mitigation
  - Preventative maintenance prediction via machine learning
  - Redundant communications (satellite and wireless) with automatic switching
- **Current TRL:** 5 (component TRL ranges 2-8)

### Autonomous Landing System
- **Current Status:** Prototype demonstrated at TRL 5
- **Planned Phase II Implementation:**
  - Automated landing area identification from altitude
  - Real-time landing site selection
  - Obstacle detection and tracking in landing area
  - Specific landing point selection
  - Automatic abort capability
  - Leverages NASA Safe2Ditch research for obstacle detection

## Use Cases & Applications

### NASA Science Applications
1. **Volcano Monitoring:** Enhanced capability to access volcanic plumes in harsh conditions; demonstrated on Turrialba (Costa Rica), Fissure 8 (Hawaii), Makushin (Alaska)
2. **Atmospheric Science:** Cloud sampling, severe storm research, hurricane research with extended duration capabilities
3. **Satellite Calibration:** Multi-day campaigns over diverse terrain (grassland, desert, alpine forests) via expanded operational envelope
4. **Wildfire Tracking:** Extended range and duration for monitoring fire behavior and smoke dispersal

### Planned Phase II Mission Types
- Multi-day unattended operations in extreme environments
- Weeks-to-months mission concepts (enabled by solar integration)
- Beyond-line-of-sight operations in unexpected weather conditions
- High-altitude CO₂ sampling in cold climates (prior experience: -25°C in Greenland)

### Commercial Applications
- **Methane Leak Detection:** Pipeline monitoring over hundreds of miles per day without human operator; BST partnered with sensor company for this application
- **Extreme Climate Operations:** First small UAS with proven severe weather capabilities for any extreme environment missions
- **Extended Operations:** Multi-day autonomous missions in dangerous environments (volcanic, wildfire smoke, severe weather)

## Key Results

### Completed Deliverables
1. **New Vehicle Model:** Full aerodynamic design with performance analysis completed in XFLR5
2. **Prototype Pitot System:** Drained, heated dual-port pitot validated in laboratory and rain tunnel
3. **Weatherproofing Plan:** Detailed approach for achieving IP55 rating with minimal mass/cost penalty
4. **Vision System Design:** Hardware selection, wiring diagrams, and mechanical integration plan for 5-camera system
5. **VTOL Prototype:** Functional S2-VTOL demonstrator with flight-validated performance

### Performance Analysis Results
- Full S3 redesign option yields 22.8% better sink rate and 23.3% better L/D vs. S2-3m
- S2-VTOL prototype achieved 299W power draw at 19 m/s cruise → ~90-100 min endurance with 5 lbs payload
- Compromise design (new wing tips only) recovers 97% of full redesign performance benefits
- Structural design validated for severe turbulence loads expected in thunderstorms

### Technology Maturation
- **Advanced Pitot System:** Heating validated; rain drain functionality proven; flight calibration planned
- **Waterproofing:** Design approach finalized for IP55 rating; minimal mass penalty estimated
- **Vision Processing:** Hardware selected; prototype assembly completed; icing detection training data plan developed
- **Simulation Capability:** JSBSim-based flight dynamics model developed with wind/gust modeling capability

## Notable Details

### Existing S2 Mission Heritage
The S2 has successfully flown:
- 12 unique payload instruments across multiple science missions
- Operations in volcanic plumes and extreme atmospheric conditions
- High-altitude sampling at -25°C temperatures
- Extended range Landsat calibration surveys
- Proven platform reduces risk of S3 development

### Competitive Positioning
- **Unique Capability:** To BST's knowledge, no other small UAS exists with demonstrated severe weather capabilities
- **Application Potential:** Very interesting for any missions in extreme climates or beyond-line-of-sight where unexpected weather encountered
- **Economic Advantage:** Small UAS repair/replacement costs more economical than crewed or larger platforms

### Planned Phase II Partners & Infusions
- NASA (Langley, Glenn for icing tunnel testing potential)
- NOAA
- Multiple universities for integration and validation
- Focus on proven Earth-science application areas: volcano monitoring, atmospheric science, satellite calibration

### Regulatory & Infrastructure Considerations
- VTOL capability eliminates need for launch site (addresses transportability constraints)
- Tool-less assembly maintained for field modularity
- IP55 design enables operations in previously excluded harsh environments

### Supporting Technology (Outside SBIR Scope, TRL 4-8)
- Redundant satellite communications with automatic link switching (TRL 8, operational)
- Wind-based mission planning algorithms (TRL 4)
- Onboard health monitoring and predictive maintenance (TRL 5)
- Forward-looking terrain following and obstacle avoidance (in development for Phase II)
- Smart power management for solar integration (in development for Phase II)

### Labor and Schedule
Phase I executed over 6 months with key milestones:
1. Wing and tail design in XFLR5 (completed)
2. S3 simulation in strong winds vs. real S2 performance (completed)
3. New pitot testing in rain tunnel (completed)
4. CAD design for waterproof S3 subsystems (completed)
5. Vision-based monitoring system design documentation (completed)

---

**Document Quality Note:** This Phase I report is comprehensive and technical, with substantial supporting analysis including detailed aerodynamic trade studies, flight test data, simulation results, and detailed system designs. The document effectively documents work completed and provides clear roadmap for Phase II development.