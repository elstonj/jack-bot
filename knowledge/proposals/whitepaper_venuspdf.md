# In Situ Exploration of Venus' Clouds by Dynamic Soaring

## Document Metadata
- **Type:** Decadal Survey White Paper
- **Client/Agency:** NASA (for Decadal Survey)
- **Program/Solicitation:** NASA Phase II SBIR grant 80NSSC19C0181
- **Date:** March 22, 2020
- **BST Products/Systems Referenced:** Fixed-wing UAS platform based on dynamic soaring (no specific named product like S2/S3 mentioned)
- **Key BST Personnel:** Jack S. Elston (lead author, BST), Maciej Z. Stachura (BST)
- **Other Key Contributors:** Mark A. Bullock (Science & Technology Corp), Sebastien Lebonnois (Laboratoire de Météorologie Dynamique), Sanjay S. Limaye (University of Wisconsin), David H. Grinspoon (Planetary Science Institute), Michael Pauken (JPL), and co-signers from JPL, Johns Hopkins APL, Southwest Research Institute, NASA centers, and various universities

## Executive Summary
This white paper proposes a novel approach to sustained in situ exploration of Venus' clouds using small, energy-harvesting fixed-wing aircraft that employ dynamic soaring to extract power from atmospheric wind shear. The vehicle design addresses a critical gap in Venus science—the need for long-duration, spatially distributed measurements of the mysterious aerosol layer that absorbs ~50% of incident solar energy. Up to eight aircraft could be deployed from a single aeroshell, enabling multi-point sampling of Venus' cloud chemistry, dynamics, and potential surface imaging.

## Technical Approach

### Core Concept
- **Dynamic soaring** as primary energy source: aircraft climb through increasing wind gradients, then descend to extract net energy, enabling sustained flight without relying on battery capacity or solar panels
- Fixed-wing rigid aircraft (not inflatable) for rapid deployment from aeroshell
- Deployable, foldable high-aspect-ratio wings for compact stowage
- Materials and coatings selected for corrosive sulfuric acid environment (pH 0 to -2)

### Vehicle Design
- Aircraft sized to fit within Pioneer Venus-class aeroshell
- High-g loading capability during atmospheric entry
- Operational envelope: 46–60 km altitude (cloud layer region with Earth-like pressure/temperature but extreme chemistry)
- Deployable in seconds via mechanical release mechanism (proven with tube-launched UAS)
- Up to 8 aircraft per aeroshell or smaller numbers as secondary payloads on balloons/dirigibles

### Energy Harvesting Strategy
- **Primary method:** Dynamic soaring cycles along inclined orbital trajectories aligned with vertical wind shear at cloud tops
- **Secondary methods considered:** RTG power, battery charging via solar panels on wings, on-board turbines to capture energy during high-gain periods
- Simulation demonstrated net energy gain at both 55 km (positive vertical winds) and 60 km (larger gradient per cycle) altitudes
- Flight path design enables continuous sampling while harvesting: upper trajectory traverses upper cloud for aerosol/gas measurements; lower arc enables near-IR surface imaging

### Navigation & Localization
- Wind field estimation via combination of on-board sensor measurements + Earth-based radio tracking + support from spacecraft near Venus (e.g., Lagrange point orbiters)
- On-board algorithms to estimate wind field from sensor data alone (alternative approach being tested)
- Intelligent flight path control to combine dynamic soaring cycles for global mobility while maintaining targeted sampling

### Simulation & Validation
- Custom flight simulation environment using candidate aircraft model + dynamic soaring control algorithms
- Tested with multiple atmospheric models:
  - Simple probe-based wind fields
  - Convective models (Baker et al.)
  - **Large Eddy Simulations (LES)** (highest fidelity, based on Vega balloon data)
  - Mesoscale and general circulation models (GCM); Venus-GRAM
- Simulated flights demonstrated sustained flight and energy gain at target altitudes

## Products & Capabilities Described

### Black Swift Technologies Contribution
**Fixed-Wing Energy-Harvesting Aircraft for Venus Exploration**
- **Design basis:** Proven dynamic soaring platforms; scaled and adapted for Venus deployment
- **Key capability:** Autonomous dynamic soaring with integrated flight path control for both energy harvesting and mission-directed sampling
- **Deployment mechanism:** Rapid mechanical release from aeroshell (seconds)
- **Operability:** Works day and night (unlike solar-only aircraft); can harvest energy during transit over dark side if charged on sunlit side
- **Survivability:** Designed for corrosive cloud environment; materials/coatings under development for long-term survival in high-pH-variance sulfuric acid aerosols

### Related Platforms Compared (for context)
- **Descent probes:** Limited to vertical snapshots; no control
- **Balloons (Vega heritage):** Passive drift at fixed altitude; no path control; limited field of view
- **Aerobots (variable buoyancy):** Slower transitions, limited navigation
- **Rotorcraft:** Require RTG + extended battery charging; impractical for Venus lower atmosphere
- **Prior fixed-wing proposal (Landis et al.):** Solar-electric only; limited to sunlit side; degraded efficiency in cloud environment

## Use Cases & Applications

### Venus Science Objectives (VEXAG-aligned)
1. **Atmospheric dynamics & composition** (VEXAG GOI II.A.DD, II.A.MP)
   - Sustained measurement of wind fields, vertical shear, convective plumes
   - In situ sampling of cloud aerosols (0.1–10 µm sulfuric acid droplets)
   - Identification of unknown near-UV absorber (40% albedo variation over decadal timescales; driver of climate forcing and superrotation anomalies)
   - Trace gas measurements (SO₂, water vapor, other species)

2. **Cloud radiative balance & chemistry** (VEXAG GOI II.B)
   - Multi-point, spatially distributed measurements of aerosol properties
   - Investigation of sulfur cycle chemistry at different latitudes/altitudes
   - Linkage between cloud composition, solar heating, and atmospheric circulation

3. **Surface-atmosphere interactions & geology** (VEXAG GOI III)
   - Near-IR imaging and spectroscopy of surface from cloud layer
   - Microwave altimetry (10× improvement over current orbital imagery)
   - Emissivity mapping; detection of hydrous minerals
   - Evidence of crustal recycling, volcanic activity, weathering patterns

4. **Climate stability questions**
   - Decadal oscillations in Venus' climate (albedo, zonal winds)
   - Comparison to Earth climate stability; general circulation understanding

### Mission Architecture
- **Deployment scenario:** Multiple aircraft released sequentially or simultaneously from aeroshell after parachute descent
- **Coverage:** Ability to navigate to specific latitudes, altitudes, and local times for targeted investigation of observed dynamical phenomena
- **Duration:** Weeks of flight per vehicle (sustained by dynamic soaring)
- **Global mobility:** Intelligent trajectory planning allows incremental position changes; near-global coverage possible through dynamic soaring path optimization

## Key Results (Simulations & Feasibility)

### Simulation Findings
1. **Energy gain confirmed:** Simulated flights at both 55 km and 60 km altitudes demonstrated net positive energy over multi-cycle periods
   - 55 km: larger total energy gain (aided by persistent positive vertical winds in LES)
   - 60 km: larger per-cycle gain (steeper vertical shear)
2. **Downdraft tolerance:** Vertical wind magnitudes ~3 m/s in LES (manageable; minor effect on system energy budget)
3. **Shear availability:** Current GCM and probe data support sustained energy harvesting at cloud-top altitudes; further validation planned

### Design Feasibility
- Aeroshell stowage: High-aspect-ratio wings can be folded to fit Pioneer Venus-class vehicle (assumed mechanism TBD)
- Deployment speed: Mechanical release achieves deployment in seconds (de-risked by tube-launched hurricane research UAS heritage)
- Survivability: Materials testing underway for composites + thin protective coatings in simulated Venus environment

## Notable Details

### Technical Risks & Mitigation
1. **Shear availability assumption:** Based on latest GCM & probe data (reasonable but requires further investigation)
   - *Mitigation:* RTG backup power, on-board turbine, rechargeable battery
2. **Aircraft localization:** Determining position relative to atmospheric structures used for energy harvesting
   - *Mitigation:* Lagrange point orbiter concept; on-board wind estimation algorithms
3. **Material durability:** Corrosive sulfuric acid environment (pH 0 to -2 in lower cloud)
   - *Mitigation:* Composite investigations + protective coatings; operates in upper cloud regime where conditions are more benign

### Payload Considerations
- **Mass budget:** Notional instruments listed for chemical, physical, and optical measurements:
  - Miniaturized GCMS (~5 kg)
  - Polarizing nephelometer (~2 kg)
  - Net flux radiometer (~2 kg)
  - Tunable laser spectrometer (~2 kg)
  - Raman spectroscope (~4 kg)
  - Imaging XRF spectrometer (~5 kg)
  - Microwave altimeter (~2 kg)
  - Optical cameras, accelerometers, chemical sensors, fluorescence/biosignature instruments
  - *Challenge:* Selective deployment to stay within vehicle weight/power limits

- **Data transmission:** Bandwidth support from Lagrange point relay or Earth-based tracking; high-bandwidth data relay from orbiter envisioned

### Scientific Justification
- **Venus climate mystery:** Unknown absorber causes half of cloud-layer solar energy absorption; highly variable temporally and spatially; directly linked to decadal albedo/wind oscillations
- **Unique Earth-like regime:** Cloud layer (48–65 km) has tolerable pressure/temperature for instruments, but extreme chemistry prevents ground-based analogs
- **Static platform limitations:** Prior balloon missions (Vega) provided only westward drifts at fixed altitude; no path control; sparse sampling despite landmark achievement
- **Dynamic soaring precedent:** Used by seabirds, world-record aircraft, proven in Earth atmospheric research (hurricane sampling)

### Competitive Advantage vs. Prior Work
- **vs. Landis et al. (solar-electric fixed-wing):** BST approach uses passive energy harvesting (dynamic soaring) rather than active solar propulsion, enabling night-side operation and sustained energy under cloud cover
- **vs. balloons:** Full flight path control, altitude flexibility, unobstructed 4π steradian field of view (critical for optical & spectroscopic measurements)
- **vs. rotorcraft:** No requirement for ground-based battery charging; no control issues in turbulent upper atmosphere
- **vs. aerobots:** Rapid altitude transitions; proven deployment mechanism

### Broader Context
- Paper positions Venus exploration as high NASA priority (Decadal Survey)
- Funded through NASA SBIR program, indicating government investment in technology development
- Multi-institutional collaboration (JPL, Johns Hopkins APL, NASA centers, universities) signaling broad scientific buy-in
- Links to VEXAG strategic goals, suggesting alignment with planetary science community priorities