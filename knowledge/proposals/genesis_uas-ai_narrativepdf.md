# AI-Enabled Mobile Autonomous Laboratories for Real-Time Adaptive Experimentation in Dynamic Environmental Systems

## Document Metadata
- **Type:** Phase I SBIR proposal submission
- **Client/Agency:** U.S. Department of Energy (DOE) / Advanced Scientific Computing Research (ASCR)
- **Program/Solicitation:** Genesis Missions: Transforming Science and Energy with AI (RFA DE-FOA-0003612, Challenge 11-A: Advanced Robotics for Dynamic Laboratory Environments)
- **Date:** Submitted April 15, 2026; document created/modified April 30, 2026
- **BST Products/Systems Referenced:** S0-VTOL UAS (fixed-wing/multirotor hybrid)
- **Key Personnel:** 
  - Black Swift: Dr. Jack Elston (PI, CEO), Dr. Maciej Stachura (CTO)
  - Brookhaven National Laboratory: Dr. Gijs de Boer (PI), Dr. Nathan Urban

## Executive Summary
This Phase I proposal describes an edge-deployable AI agent that estimates the hidden planetary boundary-layer height (PBLH) from sparse UAS path measurements using set/attention-based assimilation. The system uses uncertainty-aware trajectory planning with greedy receding-horizon scoring to select information-rich flight paths in real time, then transitions to MPC-style interface-tracking once the boundary layer is sufficiently localized. The 9-month Phase I will deliver a simulation/replay prototype with separated inference, adaptation, and control layers, benchmarked against fixed and human-designed baselines.

## Technical Approach

**Three Coupled Layers:**

1. **Thrust 1: Probabilistic Interface/Profile Estimation** 
   - Develops a hybrid digital twin assimilating streaming temperature observations into posterior estimates of local atmospheric structure
   - Represents each target column c=(x,y) using physically meaningful variables: mixed-layer temperature, inversion strength, PBLH h(c,t)
   - Generates continuous vertical profiles T_c(z,t) with explicit interface dependence; includes physics via priors on lapse rates, inversion strength, smooth temporal evolution, and mixed-layer/entrainment structure
   - PBLH extracted operationally using temperature/potential-temperature gradient rules; Richardson-number methods available as comparison baselines
   - Observes sparse, irregular, noisy scalar measurements o_i = T(x_i, y_i, z_i, t_i) + ε_i along flight paths
   - Implements ensemble Bayesian filter as practical online baseline over compact latent state x_c,t = (h_c,t, ψ_c,t)
   - Augments state with low-dimensional residual/context state s_c,t and profile decoder T_c(z,t) = T_phys(z; x_c,t) + r_φ(z, s_c,t) to capture systematic mismatch
   - Evaluates lightweight set/attention encoders (DeepSets, Set Transformer, Perceiver-style) for assimilating irregular neighborhood observations
   - Calibrates uncertainty via interval coverage, CRPS, negative log likelihood, reliability diagrams, rank histograms, and error-versus-uncertainty correlation

2. **Thrust 2: Uncertainty-Aware Trajectory Selection**
   - Uses greedy receding-horizon approximation over precomputed library of feasible trajectory primitives (vertical profiles, slanted transects, step climbs, horizontal crossings, racetrack segments, interface-probing maneuvers)
   - Scores candidates using approximate pre-posterior objective J(a) = E[U(q_t) − U(q^a_{t+τ}) | q_t] / cost(a), where U(q) is integrated posterior variance/entropy/credible-tube volume and cost(a) represents flight time, distance, or energy
   - Samples candidate future measurements from posterior predictive, passes through update rule, estimates expected uncertainty reduction
   - Offline processing includes model training, primitive generation, safety screening; online scoring uses ~20–50 feasible primitives, small ensemble/posterior sample count, vectorized profile decoding, cached neighborhood assignments
   - **Target latency:** <5 seconds per inference-and-planning cycle

3. **Thrust 3: Search-to-Track Integration**
   - Search mode prioritizes reducing uncertainty about PBLH interface location and structure
   - Transition to tracking triggered when posterior uncertainty meets spatial-continuity criteria (e.g., credible interval width threshold or confidence that interface lies in target altitude band)
   - Defines credible tube T_t = {(x, y, z) : |z − μ_h(x, y, t)| ≤ β σ_h(x, y, t)} around inferred interface
   - Selects feasible trajectory primitives to keep UAS near/across tube while respecting safety, energy, and flight-envelope constraints
   - Uses receding-horizon or MPC-style selection as practical implementation

## Products & Capabilities Described

**S0-VTOL UAS**
- **What it is:** Black Swift's vertical takeoff and landing fixed-wing hybrid system
- **Proposed use:** Primary platform for sparse atmospheric profiling; will conduct search-to-track missions estimating PBLH
- **Specifications:**
  - Flight ceiling: 15,000 ft
  - Max winds endured: 50 mph
  - Flight time: 60 minutes nominal
  - Cruise speed: 47 mph
  - Max speed: 100 mph
  - MTOW: 5.75 lbs
  - Wingspan: 62 inches
  - Payload capacity: 100 grams
  - **Sensor suite:** Air temperature, 3D wind speed/direction, dewpoint, atmospheric pressure, laser altimeter, thermal IR sensor, lightweight EO/IR cameras, laser target designators

**Hybrid AI-Enabled Autonomy Architecture**
- Edge-deployable, onboard inference layer
- Real-time uncertainty quantification and adaptive planning
- Search-to-track state machine with event-triggered transitions
- Integration with BST flight systems and constraints

## Use Cases & Applications

**Exemplar Application: Planetary Boundary-Layer (PBL) Monitoring**
- Primary Phase I demonstrator is adaptive sampling of the dynamic atmospheric boundary-layer interface with the free troposphere
- Target: maximize measurement at PBL top (h_c(x, y, t)), which regulates momentum, heat, moisture, and particulate transfer between surface layer and free troposphere
- Concrete, measurable interface for testing sparse-observation inference, uncertainty-aware planning, and control
- **Broader applicability:** cloud characterization, aerosol plume tracking, dynamic gradient detection, hazardous material transport monitoring

**DOE Mission Alignment**
- Atmospheric science and weather/water processes (BER)
- Nuclear nonproliferation monitoring (NNSA)
- Nuclear facility monitoring and environmental safety (NE, EM)
- Critical mineral exploration and mapping (FECM)

## Milestones & Success Criteria

| Period | Milestone | Success Criterion |
|--------|-----------|------------------|
| Months 1–3 | Reduced replay/simulation benchmark, PBLH labels, historical BST flight-pattern baselines, fixed vertical/raster baselines, feasible primitive library | Reproducible benchmark, label workflow, primary baselines, executable primitive library |
| Months 1–3 | Minimum viable probabilistic profile/interface estimator specified with explicit atmospheric variables; set/attention assimilation modules implemented and benchmarked | Estimator produces posterior samples of profiles and h on held-out static/replay cases |
| Months 4–6 | Calibrated online estimator from sparse UAS path measurements | Estimator improves PBLH uncertainty calibration/accuracy vs. profile method or GP/Kalman/EnKF baseline |
| Months 4–6 | Uncertainty-aware planner demonstrated with approximate pre-posterior scoring | Planner improves resource-to-localization or accuracy-at-budget vs. non-adaptive baseline |
| Month 6 | **Go/no-go decision gate** | Useful PBLH uncertainty; adaptive planner beats primary baseline; inference + scoring <5 sec/cycle |
| Months 7–9 | Event-triggered search-to-track workflow integrated | Closed-loop replay/simulation executes exploration-to-tracking without manual intervention |
| Months 7–9 | Ablations and Phase II requirements defined | Quantify AI advantage drivers; define Phase II field, data, onboard-compute, multi-agent requirements |

## Month 6 Decision Gate Metrics

**Primary baseline:** Best pre-specified non-adaptive strategy (fixed vertical profiling, raster/lawnmower, human-designed BST strategy for validation scenario)

**Primary metric:** Resource-to-localization (flight time, path length, energy proxy, or number of scalar measurements to reach target-quality PBLH estimate)

**Gate-passing criteria:**
1. **Calibrated PBLH uncertainty:** Assessed by interval coverage, CRPS, negative log likelihood, reliability/rank diagnostics, error-versus-uncertainty correlation
2. **Resource-to-localization improvement:** Target ≥20% reduction vs. baseline
3. **Accuracy-at-budget improvement:** Target ≥10% improvement in RMSE, MAE, posterior interval width, or CRPS at equal sensing budget
4. **Reduced-loop latency:** <5 seconds per cycle for posterior updating + primitive scoring
5. **Ablation evidence:** Uncertainty-aware planning outperforms mean-only adaptation; AI-assisted estimator improves over simpler baseline

## Data Sources & Models

**Data:**
- Historical UAS atmospheric data and flight patterns from BST (realistic path geometries, platform constraints, sensor sampling rates, human-designed baselines)
- Radiosonde and public meteorological profile datasets (full-column T, humidity, pressure, wind; PBLH label generation; PBLH-detection method comparison)
- DOE ARM and UAS-relevant atmospheric datasets, including ARM UAS operations where appropriate
- Simulated atmospheric fields and replay trajectories (controlled scenarios with known true interface and sparse observations)

**Models:**
- Primary: Interpretable probabilistic profile/interface estimator with h(x, y, t) as explicit latent variable coupled to physically meaningful profile parameters
- Augmentation: Learned residual or low-dimensional latent correction (only if improves calibration/accuracy on validation data)
- Architecture options: Set encoders, attention, Perceiver-style modules for sparse observation assimilation
- Baselines/ablations: GP, Kalman, EnKF-style estimators

## Budget & Collaboration

**Total Phase I Budget (9 months):** $629,821
- Black Swift Technologies: $336,635
- Brookhaven National Laboratory: $293,186

**Lead Responsibilities:**
- BST: UAS integration, trajectory primitive design, flight/safety constraints, vehicle/control interfaces, optional hardware-in-the-loop testing
- BNL: Probabilistic modeling, sequential inference, uncertainty quantification, adaptive-planning objectives, baseline benchmarking, quantitative AI-advantage evaluation
- Joint: Scenario definition, system integration, search-to-track demonstration, benchmark production

## Notable Details

**Ownership & Affiliations:**
- BST is privately held; no external venture capital or institutional investment
- Shareholders: Jack Elston (51%, USA), Maciej Stachura (39%, Canada), Bradley Cheetham (5%, USA), Cory Dixon (5%, USA)
- No foreign ownership, foreign business entities, or foreign country of concern affiliations
- No MFTRP (Malign Foreign Talent Recruitment Program) involvement reported

**Partnerships:**
- Brookhaven National Laboratory provides expertise in probabilistic modeling, AI frameworks, and DOE use-case development
- Historical collaboration with DOE ARM (Atmospheric Radiation Measurement) facilities

**Competitive Advantages & Technical Novelty:**
- **Edge AI + uncertainty quantification:** Converting sparse, irregular path measurements into calibrated belief state over hidden atmospheric interface
- **Real-time adaptive planning:** Greedy receding-horizon scoring enables <5 second inference-and-planning cycles
- **Search-to-track integration:** Event-triggered transition from exploration to targeted interface-following
- **Physics-informed architecture:** Explicit atmospheric variables and soft constraints (lapse rates, inversion structure) combined with learned residuals
- **Evaluation rigor:** Ablations, resource-to-solution metrics, Genesis/AmSC-compatible benchmarks for reuse

**Facilities:**
- BST: State-of-the-art facility in Boulder, Colorado with dedicated UAS integration lab, sensor calibration workspace, real-time data processing, mission planning, and prototyping resources
- BNL: Multi-disciplinary research environment with HPC