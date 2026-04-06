# Cooperative Balloon-borne Gliders for Exploration of Venus' Clouds and Atmosphere

## Document Metadata
- Type: NASA SBIR Phase I Proposal
- Client/Agency: NASA
- Program/Solicitation: NASA SBIR 2020 Phase I (Proposal Number: SBIR-2020-I-S3.05-5927)
- Date: March 20, 2020
- BST Products/Systems Referenced: S0-AD (Air Deployed) UAS, SwiftCore Flight Management System, Tempest UAS
- Key Personnel: Dr. Jack S. Elston (Principal Investigator/CEO), Dr. Maciej Stachura (Lead Engineer/CTO), Dr. Mark Bullock (Planetary Scientist)

## Executive Summary
Black Swift Technologies proposes to design and develop tube-launched gliders that would be deployed from a Venus balloon to complement atmospheric measurements and overcome the mobility limitations of balloons alone. The gliders would be based on BST's proven S0-AD platform currently used for hurricane research, modified for Venus' extreme upper atmosphere conditions (40-70 km altitude) and equipped with dynamic soaring capabilities to harvest energy from wind shear layers and continue operations even during descent to the surface.

## Technical Approach

**Core Concept:**
- Modify BST's existing S0-AD UAS (tube-launched, air-deployed aircraft) for Venus deployment from a balloon gondola
- Multiple small gliders (small enough to carry multiple units) released from a single balloon
- Energy harvesting via dynamic soaring to prolong mission duration and potentially maintain station-keeping with the balloon
- Vehicles capable of altitude excursions from 70 km down to approximately 55 km
- Fuselage designed to continue transmitting data via high-temperature SiC UHF transmitter even after aircraft descent ends

**Key Technical Modifications:**
- Design for operation in Venus upper atmosphere (50-70 km) where atmospheric density and pressure differ dramatically from Earth
- Removal of motor/propulsion system, pure glider configuration
- Dynamic soaring algorithms optimized for smaller aircraft with lower aspect ratio wings
- Materials selection to withstand corrosive Venus atmosphere and extreme temperatures
- Simplified tube fuselage design for thermal management and structural integrity

**Simulation and Modeling:**
- Utilize high-fidelity Venus atmospheric simulation developed in parallel Phase II SBIR effort
- Employ Community Aerosol and Radiation Model for Atmospheres (CARMA) to simulate Venus cloud conditions with 1-meter resolution and second-level timescales
- Model vehicle performance across altitude range from 40-70 km on Venus
- Validate Earth variant against historical S0-AD hurricane flight data

**Payload and Instrumentation:**
- Minimal basic payload (<1 kg): pressure, temperature, vertical/horizontal winds, aerosol size distribution, atmospheric composition using MEMS sensors
- Consuming <1W power
- Advanced instrumentation option: mass spectrometers, laser diode spectrometers, IR/UV/Raman spectrometers (3-10 kg, 2-85W)
- High-temperature SiC electronics from NASA Glenn (operate to 500°C) enabling surface-level operations
- Vehicle serves as relay for balloon communications

## Products & Capabilities Described

**S0-AD (Air Deployed) UAS:**
- Originally designed for hurricane observation missions
- Tube-launched capability
- Proven design foundation for the Venus variant
- Currently being tested for strong-wind environments
- Will be scaled and modified for Venus atmosphere

**SwiftCore Flight Management System:**
- Highly capable autopilot system developed by BST
- Used for integration of payloads into UAS for scientific research
- Will support advanced mission profiles including station-keeping, altitude traversing, and coordinated formation flight

**Modifications for Venus:**
- Control algorithms enabling: station keeping near balloon, altitude traversal (55-70 km), coordinated multi-glider flight
- Dynamic soaring optimization for Venus wind shear layers
- High-temperature subsystems and materials for cloud/below-cloud environment
- Tuned descent profiles for controlled gliding to surface

## Use Cases & Applications

**Venus Atmospheric Science:**

1. **Cloud Composition Mapping:**
   - Identify unidentified UV-absorbing substances in Venus clouds (currently absorb ~50% of penetrating sunlight)
   - Highly heterogeneous and ephemeral distribution requires in-situ spatial sampling
   - Balloons cannot navigate to specific cloud features; gliders provide directed sampling capability

2. **Atmospheric Dynamics and Superrotation:**
   - Map vertical winds and chemical gradients (highly variable at 10m-1000km scales)
   - Target specific features: updrafts, downdrafts, mountain waves, thermally anomalous regions
   - Study cloud-interface wind shear and phenomena above high-elevation terrain
   - Investigate atmospheric superrotation (winds circle planet in ~90 hours)

3. **Thermodynamic Profiling:**
   - Multi-altitude measurements through upper cloud (60-70 km) and middle cloud (50-55 km) regions
   - Study photochemical reactions in upper cloud requiring rapid in-situ chemistry measurements
   - Investigate troposphere chemistry below clouds

4. **Radiative Transfer Measurements:**
   - Multi-zenith angle measurements of visible and infrared radiation at different altitudes
   - Fixed-wing platforms avoid gondola obscuration issues of balloons
   - Measure sunlight scattering and absorption, thermal radiation fields

5. **Surface Imaging and Below-Cloud Observations:**
   - Near-infrared imaging of Venus surface through middle cloud layer
   - Extended mission duration allowing controlled descent to surface
   - Could carry imaging equipment with high-bandwidth link to balloon relay

6. **Diurnal Variation Studies:**
   - Extended mission duration enables sampling on both sunlit and night sides of Venus
   - Controlled descent profiles allow measurement of temporal variations below cloud deck

## Technical Objectives (Phase I Focus)

**1. Balloon and Instrumentation Study:**
- Review state-of-art Venus balloon designs and payload capacities (VEXAG survey)
- Contact Venus Flagship Mission study team
- Determine compatible payload weights/volumes with multiple glider deployment
- Map proposed balloon payloads and sensor requirements
- Identify complementary small-UAS sensor options

**2. Preliminary Vehicle Design:**
- Scale S0-AD design for Venus operational envelope (40-70 km)
- Remove propulsion motor, optimize for pure gliding
- Design wing and structural modifications for lower atmospheric pressure
- Aerodynamic analysis for gliding descent to surface
- Material and subsystem identification for corrosive environment and extreme temperatures
- Fuselage environmental protection strategy

**3. Simulation Development:**
- Create S0-AD model in high-fidelity Venus atmosphere simulation
- Validate Earth variant against historical hurricane flight data
- Develop balloon model for coordination studies
- Create flight profiles for optimal atmospheric sampling
- Adapt dynamic soaring algorithms for smaller aircraft
- Monte-Carlo runs on Venus models to assess survivability/capability

**4. Earth Analog Flight Campaign Design:**
- Identify meteorological phenomena on Earth analogous to Venus conditions
- Develop balloon + glider coordination experiment designs
- Create detailed test cards for Phase II testing
- Select flight test locations meeting meteorological and regulatory requirements
- Plan NASA high-altitude balloon opportunity participation
- Prepare FAA Part 107 waivers and NASA airworthiness documentation

## Key Deliverables (Phase I)

- Interim and final technical reports detailing design work, identified risks, risk mitigation strategies, and Phase II plans
- Requirements document
- Risk identification and mitigation matrix
- Preliminary vehicle design specifications
- Flight safety documentation (NASA Airworthiness, AFSRB, FRRB paperwork)
- FAA waivers (targeting early Phase II submission)
- Earth analog flight test plan and test cards
- Simulation models (S0-AD variants for Earth and Venus, balloon model)
- Flight profiles and coordinated sampling strategy documentation
- Phase II implementation plan

## Notable Details

**Relevant Competitive Advantages:**
- BST's existing S0-AD design reduces development risk compared to starting from scratch
- Parallel Phase II SBIR effort provides high-fidelity Venus atmospheric simulation environment
- Dynamic soaring expertise from concurrent larger Venus aircraft development
- Proven experience with tube-launched systems and harsh environment operations (hurricanes, Arctic)
- Established relationships with atmospheric instrumentation community

**Science Justification:**
- Addresses high-priority Venus science objectives identified in VEXAG reports
- Solves key limitation of Soviet Vega balloons: lack of navigational control
- Provides multi-altitude sampling capability vs. balloon's fixed float altitude
- Enables targeted sampling of chemical/aerosol gradients and dynamic features
- Small mass budget addition to balloon missions with significant science return multiplier

**Related Prior Work:**
- Previous NASA SBIR funded energy harvesting for Venus aircraft (cited as foundational)
- Current Phase II SBIR on high-fidelity Venus atmospheric simulation
- Current Phase II SBIR on tube-launched UAS for hurricane observations (direct technology base)
- Tempest UAS development (first unmanned intercept of tornadic supercell, VORTEX2)
- Multiple atmospheric sampling campaigns and 300+ flight experiments

**Risk Mitigation Strategy:**
- Glider deployment positioned as complement, not replacement, for primary balloon mission
- Earth analog demonstrations planned to validate key technologies before Venus use
- High modularity ensures primary mission success even if gliders fail
- Extensive use of simulation to reduce flight-testing burden and cost

**High-Temperature Electronics:**
- NASA Glenn SiC technology enables continuous operation to 500°C
- Enables data transmission from surface (or near-surface) all the way up to cloud layers
- SiC UHF transceivers, A/D converters, logic networks, battery power, sensors already developed
- Opens possibility for extended mission profiles beyond cloud-layer operations

**Energy Harvesting Strategy:**
- Venus upper atmosphere (~50-70 km) features extreme wind shear:
  - Strong upward winds at low latitudes creating vertical atmospheric movement
  - High wind shear particularly at cloud interface and above high-elevation terrain
  - Rapid planetary circulation (90-hour period) creates navigation-enabling wind-relative velocities
- Dynamic soaring allows extended flight without large battery capacity
- Enables operation on both sunlit and night sides of Venus despite diurnal power variations

**Mission Architecture Benefits:**
- Multiple coordinated gliders enable formation flying for optimized sampling
- Balloon acts as communications relay and wind-relative navigation aid
- Balloon can direct sampling through higher-level algorithms (sensor-reactive control, model-based path planning)
- Flexibility for multiple science objectives simultaneously (cloud aerosols, dynamics, radiation, chemistry, imaging)

**Key Personnel Background:**
- **Dr. Elston (PI):** CEO/co-founder; Ph.D. from CU Boulder on tornado-intercept UAS; NSF Atmospheric Sciences Postdoc; led Tempest UAS development; 100+ publications; authored 100+ COA applications; extensive Arctic deployment experience
- **Dr. Stachura (CTO/Lead Engineer):** Ph.D. aerospace engineering from CU Boulder; 300+ flight experiments; VORTEX2 participant; 140+ FAA Certificates of Authorization
- **Dr. Bullock (Planetary Scientist):** Expertise in Venus atmospheric modeling and science objectives

**Budget and Schedule:**
- Phase I: 6-month effort
- Significant allocation to simulation work, design trades, and Earth analog campaign planning
- Early in Phase II: FAA waivers, safety documentation complete
- Phase II (implied): full vehicle development, Earth analog flights, final Venus design validation