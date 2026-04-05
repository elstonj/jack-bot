# B4: Automatic Sampling

## Document Metadata
- **Type:** Phase I deliverable / technical report (Navy STTR program)
- **Client/Agency:** U.S. Navy
- **Program/Solicitation:** Navy STTR - Hazardous Weather (Topic 550-2)
- **Date:** Document created 2025-09-11, last modified 2026-01-02
- **BST Products/Systems Referenced:** sUAS (small Unmanned Aircraft Systems), SwiftCore (implied flight control architecture)
- **Key Personnel:** Maciej Stachura (last editor), Josh Darko, Jack (pilot), Zun, Joe, references to collaborators at ODU, NOAA, ERAU

## Executive Summary
This deliverable describes Black Swift Technologies' development of autonomous sampling algorithms for tropical cyclone reconnaissance using small unmanned aircraft systems (sUAS). The work progresses from three operational sampling modes (Center Fix, Eye-Wall Following, In-Flow) tested during 2024-2025 hurricane seasons to advanced closed-loop autonomy incorporating machine learning-based adaptive superobbing, surrogate forecasting models, and information-theoretic path planning. Phase 2 will implement self-learning sampling that compresses observations onboard while dynamically adjusting flight paths in real-time based on forecasting uncertainty.

## Technical Approach

### Current Operational Algorithms (Phase 1)

**Center Fix Controller**
- Autonomously navigates sUAS to estimated tropical cyclone center using GPS coordinates from P-3 aircraft or onboard observations
- Couples inertial and GPS navigation with closed-loop guidance algorithm for storm-relative drift correction
- Uses Kalman-filter-based estimator to smooth position updates despite erratic wind fields
- Transitions to slow circular pattern at center (1–2 nm radius) for pressure, temperature, wind measurements
- Triggered automatically on UAS drop or operator handoff command

**Eye-Wall Following (Radius of Maximum Winds - RMW) Controller**
- Executes dynamic loiter pattern along region of peak wind velocity surrounding storm eye
- Maintains prescribed radial distance (5–15 nm) from vortex center using onboard wind vector estimation and relative position tracking
- Uses lateral acceleration control and adaptive gain scheduling to compensate for gust-induced roll/yaw excursions
- Continuously recalculates wind field to track shifting eyewall and eye
- Collects critical data on turbulence spectra, eyewall slope, boundary-layer exchanges

**In-Flow Controller**
- Guides sUAS along radial legs extending outward from storm center to sample low-level inflow
- Leverages real-time wind correction for storm-relative heading maintenance despite high shear
- Computes cross-track error relative to predicted flow direction from anticipated storm structure or dropsonde data
- Typically performs inbound legs below 2,000 ft until eyewall interception
- Supports energy budget assessments and boundary-layer model validation

**Ocean Towers Module** (Most recent addition)
- Designed for persistent vertical profiling at fixed oceanic locations within/near storm environment
- GPS-based positioning with precision wind-relative control to maintain aircraft within 100 m horizontal box
- Modified altitude controller with adaptive gain to counter large vertical gusts, maintains constant height above sea level
- Coordinates with ocean assets or operates at multiple altitudes to form vertical sampling column
- Measures turbulent fluxes, sea spray generation, air-sea interface dynamics with temporal/spatial resolution exceeding moored buoys

### Phase 2: Advanced Closed-Loop Architecture

**Three Principal Feedback Loops:**
1. **Data Loop:** Raw sensor data → Generative compression → Uncertainty map → Planner
2. **Control Loop:** Planner → Trajectory → Flight controller → New observations
3. **Learning Loop:** Assimilated observations → Model retraining → Updated priors

#### Data Loop: Adaptive Generative Superobbing Architecture

**Problem Identified:** Conventional superobbing uses fixed-resolution averaging (e.g., 5 km radial × 5° azimuthal grids), assumes uniform information density and linear covariance. Hurricane environments exhibit non-stationary, multimodal distributions (turbulence, microphysical gradients, mesoscale vortices) that fixed kernels cannot capture.

**Solution: Generative AI Compression**
Built on Temporal Multimodal Multivariate (TMM) Learner (Park et al. 2022):

- **Encoder:** Maps multivariate input vectors (pressure, wind speed/direction, humidity, temperature, brightness temperature, derived quantities) into compact latent representation using gated recurrent layers for temporal dependencies

- **Latent Generator/Decoder:** Reconstructs probability-weighted field of virtual observations as mean–covariance pairs representing expected measurement and uncertainty at virtual points (not single values)

- **Meta-Learning Controller:** Monitors reconstruction error and entropy of latent distribution to dynamically adjust sampling kernel size/weighting, determines when additional observations necessary vs. synthetic generation suffices

**Training:** Offline using historical P-3 and sUAS datasets (dropsonde, TDR measurements); during flight, only compact inference network runs onboard for near-real-time operation

#### Meta-Probabilistic TMM Learner for Surrogate Training

**Uncertainty Quantification Approach:**
- Uses entropy (not standard deviation) as primary metric for uncertainty
- Implements mixture-of-Gaussians approach to model multimodal PDFs in boundary-layer dynamics
- Addresses non-Gaussian PDFs from PBL dynamics; conventional ensemble methods ignore correlated observations during superobbing

**Temporal Multimodal Learning:**
- **Temporal modeling:** Recurrent neural units preserve context across consecutive observations; distinguish transient noise from sustained change
- **Multimodal learning:** Mixture-density outputs represent multiple simultaneous physical regimes (e.g., updraft cores vs. downdrafts)
- **Multivariate learning:** Groups variables by shared covariance structure rather than pairwise correlations; clusters cells with similar uncertainty distributions

**Technical Implementation:**
- Built on Graph Convolutional (GC) deep learning with Kalman Filtering (KF) network
- GC-KF parameters trained offline using available data, robust to occlusions not present in training dataset
- Captures both local and global dynamics (eyewall replacement, rapid intensification, secondary wind maxima)
- Each raw observation assigned information weight proportional to contribution to reducing posterior uncertainty

#### Surrogate Model Development

**GC-LSTM Surrogate for TC Forecasting**
- Replaces linear operations with Graph Convolutional modules aggregating information from neighboring grid cells
- Uses two forms of adjacency: (1) geographical adjacency from physical grid, (2) semantic adjacency from joint probability distributions of TC variables (wind speed, pressure, temperature, humidity)
- Enhanced with physics-based indicators (CAPE, vertical wind shear, instability indices) ensuring physically meaningful relationships

**Invertible Neural Networks (INNs)**
- Complement GC-LSTM by modeling full probability distribution of short-term TC evolution
- Use normalizing-flow architectures to preserve reversible relationship between initial storm states and forecasted outcomes
- Enable exact likelihood evaluation and ensemble-consistent prediction for uncertainty-aware forecasting within data assimilation workflows

**Training Data Generation:**
- Uses ensemble data assimilation (DA) system producing evolving atmospheric states with uncertainty
- For each historical TC: 60-80 ensemble members created by perturbing initial conditions
- Ensemble generates high-frequency short-term forecasts (hourly for 12–24 hours) forming input–output sequences
- Validation via physics-informed graph recurrent baselines with mean absolute error / root-mean-square error metrics
- Data denial experiments using Observing System Experiment (OSE) framework with 3-hour temporal resolution
- Forecast error: difference in maximum wind speed or minimum sea level pressure vs. best track data
- Comparison against static benchmarks (e.g., 200 km × 100 hPa × 3 hr superobbing)

#### Control Loop: Drop Location & Path Planning

**Approach:** Information-Theoretic Rapidly-Exploring Random Tree (IT-RRT*) algorithm (Folsom et al. 2021)

- Explores environment by incrementally growing tree of feasible trajectories
- Each node = potential sUAS state (position, altitude, energy); edges = dynamically feasible flight segments
- Evaluates utility function based on predicted information gain from generative model's uncertainty map + risk factors (wind shear, precipitation, obstacles)

**Drop-Point Selection:**
- Before deployment, system generates global utility maps showing expected entropy reduction
- Identifies optimal drop zones corresponding to maxima of entropy reduction
- P-3 selects release locations based on current TC state and predicted evolution
- Updated in real-time as hurricane environment evolves or new data arrives

**Multi-Agent Optimization:**
- **Simultaneous launch:** Benefits from highly informative small areas with optimal sUAS formation
- **Sequential launch:** Benefits from sparse information in large areas with adaptation to new information
- Distributed Constraint Optimization extends to coordinate multiple sUAS, maximizing sum of benefits by optimizing launch location and route for each sUAS

**Dynamic Bi-level Optimization with Varying Time Window (DBOPVTW):**
- **Upper level:** P-3 decides where/when to launch sUAS with dynamic parameters constrained by arrival time window
- **Lower level:** Each sUAS finds best route to target with dynamic parameters constrained by path selection
- Accounts for: dynamic environmental changes, time limits due to storm motion, risks from partial data/mission loss, coordination constraints, sUAS availability limits, aircraft relocation costs
- At each decision stage, P-3 updates future release decisions based on TC state evolution

**sUAS Path Planning - Information-Theoretic Route Optimization:**

Previously achieved results with STRAP-RRT* (sampling strategy incorporating wind-alignment, uncertainty reduction):
- Temperature uncertainty reduction: improved from 8 K to 21 K (160% improvement) with 73% increase in track distance
- Wind-speed uncertainty: improved from 183 m/s to 264 m/s (44% gain) at 19% increase in track distance
- Relative-humidity uncertainty: 130% improvement with 71% increase in track distance

TMM Learner enhancements over STRAP-RRT*:
- Temporal learning exploiting time-dependent relationships
- Multimodal learning propagating information between regions with similar structure
- Deep multivariate learning grouping variables by shared covariance
- Result: up to 14.5% improvement in multimodal measurement TC forecasting vs. Minimum Distance Method

**Wind-Constraint Feasibility:**
- Imposes upper bound on allowable angular difference between sub-path segments and local wind vector
- Enables up to ~50° deviation for local maneuvering around spatial wind variations without large energy penalties
- When path aligned with wind (0° deviation), ground speed = airspeed + wind speed
- Effectively increases range coverage for same endurance, enabling more extensive reconnaissance

**In-Flight Replanning:**
- IT-RRT* tree pruned and regrown around newly identified uncertainty gradients
- Adapts to rapid storm evolution using local observations
- Maps observed/unobserved locations through similarity; updates upcoming cost changes
- Nonlinear aerodynamic model with attitude dynamics supports control system

#### Vehicle Dynamics & Nonlinear Control

**Nonlinear Path-Following Control:**
- Minimizes cost function balancing path-tracking accuracy against smooth, low-effort control
- Tracking error = distance between vehicle and desired path; control input = commanded normal acceleration
- Weighting factors prioritize path tracking while preventing excessive control effort

**Look-Ahead Guidance:**
- Introduces shifted target vector with deliberate outward offset in path's normal direction
- Magnitude depends on local path curvature, guidance gain, boundary-layer width parameter
- Creates smoother convergence, avoids sharp turns critical in strong wind conditions

**Control Law Implementation:**
- Blends two components: (1) correction direction for tracking error, (2) direction aligned with path tangent
- Smooth transition function (sigmoid) determines influence of each component based on distance from path
- Computes wind-related angle and feasibility parameter determining if desired direction achievable given airspeed/wind magnitude
- Scales by control gain, rotated by curvature-compensation angle
- Projects resulting vector perpendicular to aircraft velocity (preserves unicycle-like fixed-wing kinematics)

**Bimodal Wind Response:**
- Under bimodal wind uncertainty, vehicle dynamics model includes predictive adjustments through look-ahead mechanism
- Proactively adjusts guidance under likely stronger wind conditions
- Total tracking cost treated as random variable dependent on wind mode
- Expected cost combines multiple scenarios (e.g., 50% probability each of two wind speeds)

**Iterative Path Refinement:**
- RRT* planning generates candidate paths using expected wind values
- Trajectory-tracking controller evaluates performance using realistic vehicle dynamics for each