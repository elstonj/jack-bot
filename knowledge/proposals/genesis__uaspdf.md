# Genesis UAS: AI-Enabled Adaptive Atmospheric Sampling

## Document Metadata
- **Type:** Phase I SBIR proposal
- **Client/Agency:** Department of Energy (DOE), Advanced Scientific Computing Research (ASCR)
- **Program/Solicitation:** DOE Genesis program, Focus Area 11-A (Advanced Robotics for Dynamic Laboratory Environments)
- **Date:** 2026-04-29 (submission date)
- **BST Products/Systems Referenced:** Black Swift Technologies UAS platform, historical UAS flight data and patterns
- **Key Personnel:** Beck Cotter (last editor); BST team responsible for UAS integration, trajectory primitive design, and hardware-in-the-loop testing
- **Collaborating Institution:** Brookhaven National Laboratory (BNL)

## Executive Summary
This Phase I proposal describes a closed-loop AI system for autonomous UAS-based adaptive atmospheric sampling, focusing on real-time estimation and tracking of the planetary boundary-layer height (PBLH). The system integrates probabilistic inference from sparse temperature measurements, uncertainty-aware trajectory planning, and search-to-track control to dynamically optimize where and how a UAS samples the atmosphere. The nine-month demonstration will develop a simulation/replay prototype showing that adaptive, AI-guided sampling outperforms fixed flight strategies in efficiently localizing and characterizing the boundary-layer interface.

## Technical Approach

### Core Architecture
Three coupled layers:
1. **Inference Layer:** Probabilistic profile/interface estimator that converts sparse UAS path measurements into a calibrated posterior belief over hidden atmospheric structure and PBLH
2. **Decision Layer:** Scores feasible trajectory primitives by expected reduction in PBLH uncertainty under flight-time, energy, and safety constraints using greedy receding-horizon approximation
3. **Tracking Layer:** Switches from exploration (search for interface) to interface-following once posterior confidence exceeds threshold; uses MPC-style control to maintain UAS near credible tube

### Thrust 1: Probabilistic Interface/Profile Estimation
- **Hybrid digital twin** assimilates streaming temperature observations into posterior estimates of local atmospheric structure
- Represents local profiles using physically meaningful variables: mixed-layer temperature, inversion strength, PBLH h(x,y,t)
- Physics entered through priors/soft constraints on plausible lapse rates, inversion bounds, smooth temporal evolution, vertical-gradient regularity
- **Sparse measurement model:** UAS observes noisy scalar temperature T(xi, yi, zi, ti) + ϵi along flight paths
- **State representation:** Compact latent state xc,t = (hc,t, ψc,t) plus optional low-dimensional residual/context state sc,t
- **Profile decoder:** Tc(z,t) = Tphys(z; xc,t) + rϕ(z, sc,t) where physical component is baseline and learned component captures systematic mismatch
- **Assimilation mechanisms:** Ensemble Bayesian filter baseline; lightweight set/attention encoders (Perceiver-style modules) for mapping irregular neighborhood observations
- **Uncertainty calibration metrics:** Interval coverage, CRPS, negative log likelihood, reliability diagrams, rank histograms, error-versus-uncertainty correlation
- **PBLH extraction methods:** Temperature/potential-temperature gradient rule (primary operational method); parcel and bulk Richardson-number methods as comparison baselines

### Thrust 2: Uncertainty-Aware Trajectory Selection
- **Challenge:** Exact Bayesian optimal experimental design infeasible for real-time operation in dynamic environment
- **Solution:** Greedy receding-horizon approximation over precomputed library of feasible trajectory primitives
- **Primitive types:** Vertical profiles, slanted transects, step climbs, horizontal crossings, racetrack segments, localized interface-probing maneuvers (designed by BST)
- **Scoring function:** Pre-posterior objective J(a) = E[U(qt) - U(qat+τ)|qt] / cost(a)
  - U(q) = uncertainty functional (integrated posterior variance, entropy, or credible-tube volume)
  - cost(a) = flight time, distance, or energy proxy
- **Online execution:** ~20–50 feasible primitives, modest ensemble, vectorized profile decoding, cached neighborhood assignments
- **Latency target:** Combined inference and candidate scoring <5 seconds per cycle (demonstrates feasibility for Phase II field system)

### Thrust 3: Search-to-Track Integration
- **Search mode:** Prioritizes reducing uncertainty about PBLH location and structure
- **Transition criterion:** Event-triggered when posterior uncertainty and spatial continuity indicate sufficient localization; examples: credible interval width falls below prescribed threshold, probability interface lies within target altitude band exceeds confidence threshold
- **Tracking mode:** Defines credible tube Tt = {(x,y,z) : |z−µh(x,y,t)| ≤βσh(x,y,t)}, selects primitives to keep UAS near/across tube while respecting safety, energy, flight-envelope constraints
- **Implementation:** Receding-horizon or MPC-style primitive selection

## Products & Capabilities Described

### Black Swift Technologies UAS
- **Role:** Provides platform integration, trajectory primitive design, feasibility screening, vehicle-constraint representation, flight/safety interfaces, and optional hardware-in-the-loop testing
- **Data source:** Historical UAS atmospheric data and flight patterns used to establish realistic path geometries, platform constraints, sensor sampling rates, and baseline human-designed strategies
- **Capabilities referenced:** Sparse vertical profile sampling capability; compatibility with compact onboard inferential and planning algorithms

### System Components
- **Sensor:** Temperature measurement along UAS flight path (scalar observations)
- **Onboard computation:** Must support <5 second inference + planning cycle
- **Flight primitives:** ~20–50 precomputed, feasibility-screened trajectory segments with explicit safety/energy constraints

## Use Cases & Applications

### Primary Exemplar (Phase I)
- **Application:** Adaptive sampling of planetary boundary-layer height (PBLH) interface with free troposphere
- **Scientific target:** Optimize sampling of the atmospheric boundary-layer top, critical for regulating momentum, heat, moisture, and particulate transfer between surface layer and free troposphere
- **Why significant:** PBL top is a concrete, measurable interface; representative of broader class of transient dynamic environmental systems requiring inference from partial observations

### Broader Application Domain
The proposal identifies several DOE mission areas where adaptive AI-guided sampling applies:
- **Atmospheric science (BER):** Cloud edges, aerosol plumes, boundary-layer transitions, regions of strong gradients in temperature, moisture, particulate matter
- **Nuclear nonproliferation (NNSA):** Monitoring radioactive plumes and hazardous material transport
- **Nuclear facility/environmental monitoring (NE, EM):** Real-time environmental surveillance
- **Critical mineral exploration (FECM):** Dynamic field mapping

### Key Scientific Gaps Addressed
- Transient, heterogeneous phenomena (plumes, cloud edges, inversion layers) evolve on time/spatial scales poorly captured by fixed or sparse measurement systems
- Entrainment processes at boundary-layer top, plume dispersion/dilution, thermodynamic-cloud coupling require process-level in situ observations
- Current fixed strategies result in redundant measurements and miss dynamic gradients

## Key Results
**Phase I is not yet complete**—this is a proposal for work to be performed. The document outlines planned milestones and success criteria rather than achieved results:

### Month 1–3 Milestones
- Establish reproducible reduced replay/simulation benchmark with PBLH labels, historical BST baselines (fixed vertical/raster), and feasible primitive library
- Specify minimum viable probabilistic estimator; implement and benchmark set/attention assimilation modules
- **Success criterion:** Estimator produces posterior samples of profiles and h on held-out test cases

### Month 4–6 Milestones
- Demonstrate calibrated online estimator from sparse UAS path measurements
- Demonstrate uncertainty-aware planner using approximate pre-posterior scoring
- **Month 6 go/no-go gate** (decision point):
  - Calibrated estimator, adaptive planner, and closed loop tested together
  - **Success criteria:**
    - Useful PBLH uncertainty (interval coverage, CRPS, etc.)
    - Adaptive planner beats primary baseline
    - Inference + scoring runs <5 seconds/cycle

### Month 7–9 Milestones
- Event-triggered search-to-track workflow integrated; closed-loop replay/simulation executes exploration-to-tracking without manual intervention
- Ablations and Phase II requirements completed

### Decision Gate Metrics (Month 6)
**Primary baseline:** Best pre-specified non-adaptive strategy (fixed vertical, raster, or human-designed BST strategy)

**Primary metric:** Resource-to-localization (flight time, path length, energy, or number of measurements to reach target-quality PBLH estimate)

**Pass criteria:**
1. **Calibrated uncertainty:** Interval coverage, CRPS, negative log likelihood, reliability/rank diagnostics
2. **Resource-to-localization:** >20% reduction vs. baseline (target)
3. **Accuracy-at-budget:** >10% improvement in RMSE, MAE, posterior interval width, or CRPS at equal sensing budget
4. **Latency:** <5 seconds per cycle
5. **Ablation evidence:** Uncertainty-aware planning outperforms mean-only adaptation; AI-assisted estimator improves over simpler baselines

## Notable Details

### Partnership & Division of Labor
- **Black Swift Technologies:** UAS integration, trajectory primitive design, feasibility/safety screening, flight-envelope constraints, hardware-in-the-loop testing
- **Brookhaven National Laboratory:** Probabilistic modeling, sequential inference, uncertainty quantification, adaptive planning objectives, baseline benchmarking, AI-advantage evaluation, AmSC/ModCon compatibility
- **Joint:** Scenario definition, estimator/planner integration, final search-to-track demonstration

### Data Sources
1. Historical Black Swift UAS atmospheric data and flight patterns
2. Radiosonde and public meteorological profiles (PBLH labels, method comparison)
3. DOE ARM and UAS-relevant atmospheric datasets; ARM UAS operations data
4. Simulated atmospheric fields and replay trajectories

### Computational Requirements
- **Target latency:** <5 seconds per inference + planning cycle (enables real-time adaptive sampling)
- **Online library:** ~20–50 trajectory primitives
- **Modest ensemble or posterior sample count** (not specified; to be determined)
- **Cached local-neighborhood assignments** for speed

### Evaluation & Reuse
- Benchmarks, ablations, and resource-to-solution metrics compatible with emerging **Genesis evaluation protocols** and future **AmSC/ModCon reuse**
- Reduced Phase I benchmark (local 2D transect or small 3D volume, one evolving interface, scalar temperature, replayed/simulated UAS trajectories, limited primitive library) designed as stepping stone to Phase II field deployment

### Unique Technical Aspects
- **Probabilistic interface representation:** Explicit PBLH as latent variable coupled to interpretable profile parameters (vs. purely learned black-box)
- **Hybrid physics+learning:** Physical profile baseline with learned residual correction only if empirically justified
- **Calibrated uncertainty:** Emphasis on uncertainty not just for decision-making but validated by multiple diagnostics
- **Set/attention assimilation:** Handles irregular sparse observations while preserving physics interpretation
- **Feasibility-screened primitives:** All candidate trajectories pre-validated for safety, energy, vehicle constraints (vs. open optimization over trajectory space)

### Phase II Requirements
To be determined through Phase I ablations. Likely to include:
- Field-deployable onboard compute
- Extended spatiotemporal field priors
- Multi-agent coordination framework
- Expanded primitive library and dynamic primitive generation

---

**Document Quality Note:** This is a thorough, technically detailed Phase I SBIR proposal with clear research objectives, methodology, milestones, and decision gates. All key technical details, roles, and metrics are well-specified.