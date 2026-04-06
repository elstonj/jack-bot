# DARPA-PS-24-13: Albatross Program Solicitation

## Document Metadata
- Type: Program Solicitation
- Client/Agency: Defense Advanced Research Projects Agency (DARPA), Strategic Technology Office (STO)
- Program/Solicitation: Albatross (DARPA-PS-24-13)
- Date: September 26, 2024
- BST Products/Systems Referenced: None (this is a DARPA solicitation document, not a BST proposal)
- Key Personnel: Beck Cotter (last editor)

## Executive Summary
This DARPA solicitation seeks innovative approaches for autonomous soaring capabilities on small uncrewed aerial systems (s-UAS) to extend range and endurance by harvesting energy from natural wind conditions. The 24-month program will use real-world flight testing across multiple environments (thermal, ridge, wave, and dynamic soaring) with three test cycles, each featuring practice test events and formal test events. Multiple awards are anticipated under Other Transaction (OT) agreements for prototype development.

## Technical Approach
The Albatross program focuses on three integrated technical areas:

### 1. Preflight Planning Perk (PF2P)
- Weather forecast-informed mission planning incorporating historical, current, and forecasted weather data
- Integration of geographical features and their effects on airflow patterns
- Aircraft performance prediction tools generating flight plans that maximize power conservation
- Outputs: initial flight plan, environmental condition forecasts, power profile predictions
- Operator interface showing multiple route options with trade-off information (expected flight time, probability of reaching destination)
- Graphical constraint definition (keep-out zones, geofences, altitude limitations, time constraints)

### 2. Sensing and Harnessing Control System (SHCS)
- Real-time onboard detection of soaring conditions
- Autonomous commands to harness environmental energy while maintaining mission progress
- Leverages existing sensor data (IMU, GPS, airspeed)
- Additional sensors as needed: pressure sensors on wings, 3D airflow sensors, LIDAR, visual cameras
- Integration emphasis over custom sensor development
- Terrain avoidance capabilities for close-proximity operations in boundary layer conditions
- Coordination with PF2P to balance energy harvesting with mission objectives and safety

### 3. Integrated Approach
- Real-time flight path adjustment based on sensed wind conditions
- Mission progress maintained while opportunistically harvesting soaring energy
- Operator receives continuous updates on anticipated mission duration and performance vs. predictions

## Products & Capabilities Described

### Small Uncrewed Aircraft Systems (s-UAS) Requirements
**Physical Characteristics:**
- Weight: <20 lbs (preferred, Group 1 UAS) or <55 lbs (Group 2, if well justified)
- Battery-powered
- Environmental protection: IP54 equivalent (sand and saltwater exposure expected)
- Launch/recovery from boat highly desired (no improved runway required)
- Foreign sourcing compliance (Section 848 NDAA, Executive Order 13981)
- Approved for flight on U.S. military ranges

**Performance Characteristics:**
- Flight range: >50 miles
- Flight endurance: >2 hours

**Navigation Characteristics:**
- Autonomous GPS waypoint navigation
- 3D geofence capability
- Programmable loss-of-link behaviors
- Guidance, Navigation, Control subsystem suitable for modification

**Communication/Data Characteristics:**
- >50 mile communication link range
- Ground control station handoff or non-line-of-sight (SATCOM) capability
- 3D position output to government systems (MAVLINK format preferred)
- Battery level and power output recording/downlink capability

## Use Cases & Applications

### Test Event Environments

**TE-1: Land-Based Range (Thermal, Ridge, Wave, Dynamic Soaring)**
- ~2000 square miles target area
- Long traversal paths
- Thermal soaring: 2-4 m/s vertical velocities
- Ridge soaring over mountainous terrain with prominent ridges
- Potential sites: Fort Irwin, California; Yuma Proving Ground, Arizona

**TE-2: Sea-Based Range (Ridge and Dynamic Soaring)**
- ~500 square miles (ocean and land)
- Dynamic soaring with consistent 10-15 mph winds
- Close-proximity operations near sea surface amidst moving ocean waves
- Potential sites: Pacific Missile Range Facility (Hawaii); San Clemente Island, California; Roosevelt Roads, Puerto Rico

**TE-3: Combined Land and Sea (Extensive Coverage)**
- Multi-environment testing across large distances (exemplar: 78 nautical miles)
- Potential sites: Vandenberg Space Force Base, California; Kodiak, Alaska; south of Agadir, Morocco

### Mission Types
- **Extended Range Missions**: Fly from point A to point B using minimal energy
- **Extended Endurance Missions**: Loiter at a location while remaining available at specific time (coordination with other mission events)

## Program Structure & Key Results Metrics

### Timeline (24 months from kickoff)
- **Month 0**: Program Kickoff Meeting
- **Month 6**: System Checkout (TE-0)
- **Months 8-12**: Test Cycle 1 (PTE-1A, PTE-1B, TE-1)
- **Months 14-18**: Test Cycle 2 (PTE-2A, PTE-2B, TE-2)
- **Months 20-24**: Test Cycle 3 (PTE-3A, PTE-3B, TE-3)

### Program Metrics (Key Results)

| Metric | Target |
|--------|--------|
| Energy Use Reduction | 75% from baseline |
| Mission Planning Accuracy | Energy consumption within 15% of prediction |
| Mission Completion | 100% |

**Measurement Approach:**
- Baseline Energy Usage: Same aircraft without soaring (direct point-to-point flight)
- Actual Energy Usage: Albatross-enabled s-UAS during test flight
- Predicted Energy Usage: Pre-flight prediction from mission planner
- Energy = integrated power over time (area under power vs. time curve)
- Baseline and Albatross-enabled aircraft flown simultaneously for comparison

### Flight Testing Structure
- **Practice Test Events (PTEs)**: 6 total (2 per test cycle), ~1 week each, development/verification only, government airspace provided
- **Test Events (TEs)**: 3 total, ~1 week each with 3 test days, formal government evaluation
- **Simultaneous Multi-Aircraft Operations**: Performers operate multiple flight vehicles to efficiently utilize range time

## Notable Details

### Program Emphasis & Constraints
- **NOT airframe design focused**: Albatross is NOT a dedicated aircraft design effort; focus is on planning, sensing, and control applied to existing or quickly assembled s-UAS
- **NOT drag reduction or energy density**: Program avoids custom sensor development; emphasis on integration of existing hardware
- **NOT additional power harvesting**: Solar power and other energy harvesting beyond soaring are discouraged; if used, gains must be differentiated from soaring gains
- **Extensive testing required**: Performers must plan significant independent flight testing beyond formalized events

### Key Safety Requirements
1. Continuous position updates (Lat/Long/Alt) to operator and government repository
2. Operator override capability for immediate control
3. Continuous communications with range control
4. 3D geofence implementation with automatic return if exceeded
5. Pre-flight checklists for each vehicle
6. Emergency landing if GPS/communications lost

### Deliverables
1. Kickoff meeting presentation
2. System Checkout demonstration (TE-0)
3. Six Practice Test Events
4. Three Test Events with readiness reviews and hot-wash reports
5. Software deliverables prior to each TE (to government repository)
6. Final report with all software, documentation, and hardware technical data package
7. Preflight Planning Tool demonstrations (key evaluation component)

### Acquisition Strategy
- **Two-Phase Process**: 
  1. Abstract submissions (5 pages max) evaluating technical comprehension, ability, and approach
  2. Oral Proposals (by government invitation) for selected proposers
- **Award Type**: Other Transaction (OT) for Prototypes under 10 U.S.C. § 4022
- **Multiple Awards Anticipated**: Cost share recommended for traditional defense contractors
- **Fast-Track Opportunity**: OT for Prototypes allows follow-on awards without competition (e.g., direct aircraft procurement)

### IP and Data Rights
- Government assumes unlimited rights to mission-systems hardware and software unless proposer asserts restrictions
- Mature s-UAS or straight-forward subsystem combinations preferred (not prospective capabilities)
- Software: Government Purpose Rights (GPR) over deliverable source code with fully defined interfaces to any licensed software
- Technical data packages required for all hardware and software
- Prior IP assertions must be certified via Appendix 4

### Commercial Application Focus
- Government envisions commercial applications for soaring technology
- Program goals include understanding performer's commercialization strategy and plans
- Cost share consideration as part of commercialization strategy
- Delivery of technology in "easy-to-distribute format" emphasized

### Teaming
- Proposers encouraged to form complete teams addressing all program elements
- Different technological aspects require integration: planning tools, sensors, control solutions
- Nontraditional defense contractors and nonprofit research institutions eligible
- Fewer full-time personnel preferred over more low-time personnel

## Notable Soaring Types Addressed

1. **Thermal Soaring**: Upward winds from solar heating of geographical features; used by large bird species (e.g., Andean condor)
2. **Ridge Soaring**: Vertical wind components from flow over terrain (slope lift, orthographic lift)
3. **Wave Soaring**: Leeward separated wind features from flow over large geographical features; crewed examples: >1,500 miles at >100 mph average speeds
4. **Dynamic Soaring**: Energy from wind speed differences across air mass boundary shear layers; occurs near water or mountain surfaces

---

**Note**: This is a DARPA program solicitation document, not a Black Swift Technologies proposal or report. It describes DARPA's requirements and evaluation criteria for potential contractors (which could include BST) to develop autonomous soaring capabilities for small UAS.