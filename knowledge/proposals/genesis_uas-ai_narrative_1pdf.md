# AI-Enabled Mobile Autonomous Laboratories for Real-Time Adaptive Experimentation in Dynamic Environmental Systems

## Document Metadata
- **Type:** SBIR Phase I Proposal
- **Client/Agency:** U.S. Department of Energy (DOE), Advanced Scientific Computing Research (ASCR)
- **Program/Solicitation:** Genesis Missions: Transforming Science and Energy with AI (RFA DE-FOA-0003612); Challenge 11-A (Advanced Robotics for Dynamic Laboratory Environments)
- **Date:** Submitted April 15, 2026 (resubmission)
- **BST Products/Systems Referenced:** S0-VTOL UAS (S0)
- **Key Personnel:** 
  - Black Swift Technologies: Dr. Jack Elston (Principal Investigator, CEO); Dr. Maciej Stachura (CTO)
  - Brookhaven National Laboratory: Dr. Gijs de Boer (Co-PI); Dr. Nathan Urban

## Executive Summary

This Phase I proposal seeks to develop a closed-loop AI workflow for adaptive atmospheric sampling using instrumented UAS platforms. The system will estimate the planetary boundary-layer height (PBLH) from sparse, noisy temperature measurements, quantify calibrated uncertainty, and use that uncertainty to autonomously select information-rich trajectories in real time. The project combines probabilistic inference, uncertainty-aware planning, and search-to-track behavior into a simulation/replay prototype that demonstrates computational feasibility and scientific advantage over fixed sampling strategies.

## Technical Approach

**Three Coupled Layers:**

1. **Inference Layer (Thrust 1: Probabilistic Interface/Profile Estimation)**
   - Develops a hybrid digital twin assimilating sparse UAS temperature observations into posterior estimates of atmospheric profiles
   - Represents local atmospheric structure using physically meaningful variables: mixed-layer temperature, inversion strength, and PBLH h(x,y,t)
   - Constructs continuous vertical profiles T_c(z,t) with explicit interface dependence
   - Physics enters via priors/soft constraints on lapse rates, inversion strength bounds, smooth temporal evolution, and entrainment-zone structure
   - Implements ensemble Bayesian filter on compact latent state x_c,t = (h_c,t, ψ_c,t)
   - Augments with low-dimensional residual state and learned profile decoder: T_c(z,t) = T_phys(z; x_c,t) + r_φ(z, s_c,t)
   - Evaluates set/attention encoders for assimilating irregular sparse observations
   - Calibrates uncertainty using interval coverage, CRPS, negative log likelihood, reliability diagrams, rank histograms, and error-versus-uncertainty correlation

2. **Decision Layer (Thrust 2: Uncertainty-Aware Trajectory Selection)**
   - Uses greedy receding-horizon approximation over precomputed library of feasible trajectory primitives (~20–50 primitives)
   - Primitive types include: short vertical profiles, slanted transects, step climbs, horizontal crossings, racetrack segments, localized interface-probing maneuvers
   - Scores candidates via approximate pre-posterior objective: J(a) = E[U(q_t) − U(q^a_{t+τ})|q_t]/cost(a)
   - U(q) uncertainty functional: integrated posterior variance, entropy, or credible-tube volume
   - cost(a) represents flight time, distance, or energy
   - Samples candidate future measurements from posterior predictive, passes through approximate update rule, estimates expected uncertainty reduction
   - Target latency: <5 seconds per cycle for combined inference and candidate scoring

3. **Tracking Layer (Thrust 3: Search-to-Track Integration)**
   - Search mode prioritizes reducing uncertainty about PBLH location and structure
   - Transition to tracking triggered when posterior uncertainty falls below prescribed threshold and spatial-continuity criteria met
   - Defines credible tube: T_t = {(x,y,z): |z − μ_h(x,y,t)| ≤ βσ_h(x,y,t)}
   - Uses receding-horizon or MPC-style selection to keep UAS near/across credible tube while maintaining safety, energy, and flight-envelope constraints

**Data Sources:**
- Historical BST UAS atmospheric data and flight patterns (realistic path geometries, platform constraints, sampling rates)
- Radiosonde and public meteorological profile datasets (PBLH labels, comparison methods)
- DOE ARM and UAS-relevant atmospheric datasets (DOE measurement practices)
- Simulated atmospheric fields and replay trajectories (controlled scenarios with known truth)

**Baseline Comparisons:**
- Fixed vertical profiling
- Raster/lawnmower sampling
- Human-designed BST strategy
- Profile-method, GP/Kalman/EnKF estimators
- Mean-only (non-uncertainty-aware) adaptation

## Products & Capabilities Described

**S0-VTOL UAS**
- **Description:** Hybrid VTOL platform combining multirotor deployability with fixed-wing range/endurance
- **Specifications:**
  - Flight ceiling: 15,000 ft
  - Max winds endured: 50 mph
  - Flight time: 60 minutes nominal
  - Cruise speed: 47 mph
  - Max speed: 100 mph
  - Max takeoff weight: 5.75 lbs
  - Wingspan: 62 inches
  - Payload weight capacity: 100 grams
- **Sensor Suites:** Air temperature, 3D wind speed/direction, dewpoint, atmospheric pressure, laser altimeter, thermal IR sensor, lightweight EO/IR cameras, laser target designators
- **Proposed Use:** Platform for sparse path sampling of atmospheric profiles; delivers noisy scalar temperature observations along flight path; enables adaptive trajectory execution with real-time onboard decision-making

## Use Cases & Applications

**Primary Exemplar: Atmospheric Boundary-Layer Profiling**
- Target: Estimate and track planetary boundary-layer height (PBLH) interface h(x,y,t)
- Science Driver: PBL top regulates transfer of momentum, heat, moisture, and particulates between surface layer and free troposphere; critical for weather prediction, air quality, hazard transport
- Broader Applications (as class representative):
  - Cloud edge characterization
  - Aerosol plume tracking and dilution
  - Boundary layer transitions and entrainment
  - Regions of strong temperature/moisture/particulate gradients
  - Three-dimensional structure mapping across scales

**DOE Mission Alignment:**
- Atmospheric science (weather/water availability, process-level understanding)
- Nuclear nonproliferation monitoring
- Nuclear facility monitoring and environmental safety
- Critical mineral exploration and mapping

## Key Results (for reports)

This is a Phase I proposal, not a completed study. No results reported, but project includes month-6 decision gate with quantitative benchmarks:

**Decision Gate Metrics (Month 6):**
1. **Calibrated PBLH Uncertainty:** Assessed by interval coverage, CRPS, negative log likelihood, reliability/rank diagnostics, error-versus-uncertainty correlation
2. **Resource-to-Localization Improvement:** Target >20% reduction in flight time/path length/energy/measurement count vs. baseline to reach target-quality PBLH estimate
3. **Accuracy-at-Budget Improvement:** Target >10% improvement in RMSE, MAE, posterior interval width, or CRPS at equal sensing budget
4. **Reduced-Loop Latency:** Combined inference + candidate scoring <5 seconds per cycle
5. **Ablation Evidence:** Uncertainty-aware planning outperforms mean-only adaptation; AI-assisted estimator improves over simpler baselines

**Milestones:**
- Months 1–3: Benchmark setup, PBLH labels, baseline strategies, primitive library
- Months 4–6: Calibrated online estimator, uncertainty-aware planner demonstrated
- Month 6: Go/no-go gate decision
- Months 7–9: Search-to-track workflow integration, ablations, Phase II requirements

## Notable Details

**Partnership & Collaboration:**
- BNL co-investment: $293,186 (BNL covers ~46% of total budget)
- BNL leads probabilistic modeling, sequential inference, UQ, adaptive planning objectives, baseline benchmarking
- BST leads UAS integration, trajectory primitive design, flight constraints, vehicle interfaces, optional hardware-in-the-loop testing

**Budget:**
- Total Phase I (9-month): $629,821
  - BST: $336,635
  - BNL: $293,186

**Differentiated Approach:**
- Emphasis on **calibrated uncertainty** driving planning decisions, not just point estimates
- Integration of **physical priors** (atmospheric constraints) with **learned residuals** to combine domain knowledge and data-driven correction
- Real-time onboard AI inference (<5 sec latency) compatible with deployed UAS
- Explicit search-to-track behavior mimics human adaptive sampling strategy
- Benchmarks designed for AmSC (Advanced Scientific Computing) evaluation protocols and future reuse

**Facility & Resources:**
- BST Boulder facility: state-of-the-art UAS integration lab, sensor calibration, real-time data processing, mission planning
- BNL: High-performance computing resources for data processing/storage; access to ARM atmospheric datasets and UAS operations expertise

**Ownership:**
- BST is privately held with 4 equity holders (all U.S. citizens except CTO Maciej Stachura, Canadian):
  - Jack Elston: 51% (U.S.)
  - Maciej Stachura: 39% (Canada)
  - Bradley Cheetham: 5% (USA)
  - Cory Dixon: 5% (USA)
- No foreign investment, offshore entities, or malign foreign talent recruitment program involvement

**Compliance & Security:**
- Completed DOE Transparency of Foreign Connections (TFC) disclosure (no foreign connections of concern identified)
- Project does not involve prohibited FASC unmanned aircraft systems, coded equipment from foreign source, or foreign-country-of-concern equipment with internet connectivity