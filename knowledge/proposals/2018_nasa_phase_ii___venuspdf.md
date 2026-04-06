# Dynamic Soaring for Persistent Venus Upper Atmosphere Observations

## Document Metadata
- **Type:** NASA SBIR Phase II Proposal
- **Client/Agency:** NASA
- **Program/Solicitation:** SBIR 2018 Phase II, Topic S3.05
- **Date:** Submitted February 2019 (proposal period)
- **BST Products/Systems Referenced:** Dynamic soaring UAS platform, deployable high aspect ratio glider, Venus Flytrap aeroshell deployment system
- **Key Personnel:**
  - Dr. Jack S. Elston (Principal Investigator)
  - Dr. Maciej Stachura (Lead Engineer)
  - Dr. Mark Bullock (Venus Atmospheric Science)
  - Dana Turse (Deployable Structures and Material Science)
  - Dr. Nicholas Jenkins (Computational Fluid Dynamics Lead)

## Executive Summary
Black Swift Technologies proposes to develop a dynamic soaring unmanned aircraft system (UAS) for persistent observations of Venus's upper atmosphere (50-60 km altitude). The system would harvest energy from atmospheric wind shear to enable long-duration flight without propulsion systems, addressing limitations of existing balloon and solar-powered approaches. Up to eight aircraft could deploy from a single Pioneer aeroshell ("Venus Flytrap") for redundancy and multi-sensor capability.

## Technical Approach

### Core Concept
- **Energy Source:** Dynamic soaring—extracting energy from atmospheric wind shear gradients rather than relying on batteries or solar power
- **Platform:** High aspect ratio deployable glider designed to carry 10 kg payload
- **Deployment:** Rigid, foldable aircraft deploying from standard aeroshell in seconds (eliminating need for inflatable systems)
- **Mission Duration:** Sustained flight on both day and night sides of Venus by continuously harvesting wind energy; solar charging on light side supplements battery for control systems during dark side transit
- **Navigation:** Intelligent flight path control algorithms enabling targeted global mobility while maintaining soaring cycles

### Key Technical Objectives (Phase II)
1. **High Fidelity Venus Simulation** for dynamic soaring investigation
2. **Earth Analog Demonstration** of dynamic soaring capability
3. **Deployable UAS Design** suitable for Venus environment
4. **Venus Aircraft Design** with material/construction emphasis on corrosive atmosphere survival

## Products & Capabilities Described

### Dynamic Soaring Aircraft
- **Configuration:** Fixed-wing glider with deployable/foldable composite wings
- **Wing Design:** High aspect ratio (AR = 12 in baseline simulations), three-section folding design for aeroshell stowage
- **Payload Capacity:** 10 kg
- **Deployment Mechanism:** Composite hinges allow folding to compact configuration; deploys in seconds via mechanical release
- **Materials:** High-strain composite hinges combined with rigid composites; modified for sulfuric acid resistance
- **Airspeed:** ~20-28 m/s (from Phase I testing data)

### Venus Flytrap Aeroshell Concept
- Pioneer-class aeroshell can accommodate up to 8 aircraft
- Enables scalability to Pathfinder or Flagship missions
- Allows secondary payloads on larger dirigible/balloon missions
- Provides surface protection and deployment mechanism

### Dynamic Soaring Control Algorithms (Two variants developed in Phase I)
1. **Position-Hold Controller:** Station-keeping with inclined orbit at fixed procession angle; suitable for small-scale Earth wind shears
2. **Wind-Relative Controller:** Inclined orbit in wind frame with gradual translation ("corkscrew" pattern); designed for Venus's planet-spanning wind shear layers

## Use Cases & Applications

### Venus Upper Atmosphere Science Priorities
- **In-situ cloud aerosol sampling:** Targeted investigation of unidentified absorber in upper clouds (responsible for ~50% of sunlight absorption)
- **Atmospheric chemistry:** Direct photochemical measurements in 60-70 km region
- **Cloud profiling:** Ability to traverse latitude and altitude, unlike balloons constrained by prevailing winds
- **Surface imaging:** Descent capability to middle cloud (50-55 km) for near-infrared surface observation
- **Multi-zenith radiometry:** Unobstructed 4π steradian field of view (unlike balloons obscured by balloon envelope)
- **Dynamic phenomena investigation:** Targeted sampling of wind fields, superrotation mechanisms, gravity waves
- **Vertical profiling:** Routine profiling above and through cloud tops

### Earth Analog Testing Applications
- Dynamic soaring in thunderstorm/hurricane eyewall wind shear
- Ridge lift and gravity wave exploitation
- High-altitude wind shear layer sampling (similar to Venus cloud-top shear)

## Key Results (Phase I Accomplishments)

### Venus Atmospheric Model Development
- Integrated Pioneer Venus and Venera probe data into BST simulation environment
- Collaboration with Dr. Sebastien Lebonnois (LMD) on high-fidelity GCM output
- Created three Venus atmospheric models for simulation:
  - **Model A:** VIRTUS/Venus Express data, 61-66 km, 61-103 m/s wind
  - **Model B:** Baker model, 48-68 km, 75-120 m/s wind (less pronounced gradient)
  - **High Fidelity Model:** Lebonnois GCM with convective plumes (3 m/s), detailed 46-55 km region

### Simulated Dynamic Soaring Feasibility
- **Key Finding:** Dynamic soaring achieves net energy gain in all three Venus models
- High Fidelity Model at 55 km: Positive energy accumulation over 10-minute simulated flight with inclined orbit pattern
- High Fidelity Model at 60 km: Higher energy per cycle due to strong vertical shear (8 m/s/km)
- Vertical wind components (convective plumes) observed to gradually increase altitude, providing additional energy
- Wind-relative algorithm demonstrated superior to position-hold for high-wind Venus conditions

### Flight Testing (Graecalis Dynamic Soaring Glider)
- **Test Date:** January 12, 2019
- **Aircraft Specifications:** 2.9 m wingspan, Bex 1809 airfoil, 5.6 m² wing area, 4.4 kg empty weight, 5.2 kg flying weight
- **Flight Duration:** 13.3 minutes total (3.9 min autonomous, 9.4 min manual)
- **Average Cruise Speed:** 28 m/s
- **Autopilot Power (Autonomous):** 258 W average
- **Wind Conditions:** Max 4 m/s (insufficient for true dynamic soaring; used propulsion baseline)
- **Dynamic Soaring Pattern Results (5 cycles, propulsion-powered):**
  - Average height change: 27 m per cycle
  - Average IAS: 28.3 m/s
  - Average input energy: 377.2 W
- **Validation:** Confirmed airframe, avionics, and autopilot functionality for Phase II testing

### Deployable Wing Development
- **Prototype 1:** Composite hinges tested on foam wing
- **Prototype 2:** Full-scale hinge integrated into Graecalis composite wing, 180° deployment tested
- **Design Features:**
  - Three-fold wing sections for compact stowage
  - High-strain composite hinges maintain airfoil shape when deployed (minimize drag)
  - Airfoil-conforming hinge design deployed successfully
- **Strength Testing Results:**
  - Positive wing load capacity: 3.5 ft-lbf (initial prototype)
  - Negative wing load capacity: 1.75 ft-lbf (initial prototype)
  - **Status:** Prototype not yet flight-worthy; Phase II to develop internal bending structures and flexible film covering for leading edge cutouts

### Composite Material Survivability (Venus Atmosphere)
- Trade study conducted on composite materials for corrosive sulfuric acid environment
- Testing and validation of candidate composites completed in Phase I
- Material selection process informed wing hinge and airframe design

## Notable Details

### Competitive Advantages Over Existing Approaches
1. **vs. Balloons (Vega heritage):**
   - Directional flight control enables targeted sampling (balloons drift with 100 m/s winds)
   - Multi-altitude capability (balloons limited to 50-55 km)
   - Unobstructed imaging (balloon envelope blocks zenith view)
   - Rapid altitude profiling for chemistry/aerosol studies

2. **vs. Solar-Powered Heavier-Than-Air:**
   - No need to exceed wind speeds (only known alternative proposed ~40-60 m/s to stay on day side)
   - Operates on dark side via battery charging on light side + energy harvesting
   - Simplified sealed design (no exposed motors/propellers vulnerable to corrosion)

3. **vs. Dirigibles:**
   - Better control of flight path and altitude
   - Simpler, faster deployment (seconds vs. inflation time)
   - Rigid structure simplifies protection against corrosion
   - Multiple aircraft for redundancy and distributed sensing

### Mission Architecture Advantages
- **Scalability:** 8 aircraft per Pioneer aeroshell; can scale to larger missions or fly as secondary payloads
- **Redundancy:** Multiple aircraft enable mission continuation if one fails
- **Distributed Sensing:** Different sensors on different aircraft
- **Cooperative Navigation:** Aircraft can communicate wind feature locations to optimize soaring paths

### Technical Innovations
- Custom composite hinges maintaining aerodynamic integrity through deployment
- Wind-relative dynamic soaring algorithm tailored for planet-spanning shear (vs. localized ridge lift)
- Integration of high-fidelity GCM output into flight simulation environment
- Successful demonstration of tube-launched UAS deployment methodology (applied from hurricane observation experience)

### Risk Mitigation Completed in Phase I
- Venus atmospheric model validation against decades of probe/orbital data
- Simulation-proven feasibility before expensive hardware development
- Prototype wing hinges tested to validate folding mechanism
- Material testing initiated for corrosive environment survival
- Earth flight testing demonstrates autonomous soaring capability and avionics integration

### Regulatory/Administrative Success
- Negotiated with NASA Armstrong Flight Safety Review Committee to avoid lengthy (9-month, $8,000) flight review process for non-NASA-owned aircraft; Phase I flight testing proceeded without review under standard FAA rules

## Proposed Phase II Work Plan
- Refinement of high-fidelity Venus simulation
- Earth analog demonstrations (hurricane/thunderstorm sampling)
- Deployable aircraft design optimization with improved structural rigidity
- Extended flight testing with autonomous dynamic soaring algorithms
- Additional material testing and surface coating development for Venus environment
- Prototype fabrication of scaled Venus-suitable aircraft