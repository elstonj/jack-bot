# ONR-BST: Edge AI Learning for Autonomous Hurricane Response

## Document Metadata
- **Type**: STTR Phase I Report / Technical Progress Document
- **Client/Agency**: Office of Naval Research (ONR)
- **Program/Solicitation**: Navy STTR - Hazardous Weather
- **Date**: 2025 (document created/modified September 14, 2025)
- **BST Products/Systems Referenced**: Hunter-sUAS (small Unmanned Aerial System), Edge AI learning platform, multimodal sensor fusion systems
- **Key Personnel**: Park (author of referenced KDD 2022 paper and trajectory work); Folsom (2021 publication); collaborative team at NASA JPL and AFRL

## Executive Summary
This document describes collaborative research across three major threads: (1) optimal path planning for Mars rovers adapted to hurricane forecasting using WRF-EnKF data assimilation, (2) AFRL-led trajectory tracking for heterogeneous aerial assets under extreme uncertainty and wind shear, and (3) BST's Edge AI learning for real-time multimodal sensor fusion and information-theoretic decision-making on autonomous platforms. The work addresses coordinated navigation of High-Value Aerial Assets (HVAA) and Sensing Aerial Assets (SAA) in severe weather with temporal, multimodal, multivariate uncertainty quantification.

## Technical Approach

### Thread 1: NASA JPL - Optimal Path Planning (Mars → Hurricane)
- **Information-Theoretic RRT* (Rapidly-exploring Random Tree)**: Scalable path planning for rover-helicopter teams in uncertain environments
- **Model Performance**: Successfully run on 40,000 and 673,854 one-square-meter cells with reasonable computational time
- **Hurricane Forecasting Foundation**:
  - Weather Research and Forecasting model with Ensemble Kalman Filtering (WRF-ARW)
  - Community Radiative Transfer Model (CRTM) integration
  - Hourly temporal resolution hurricane forecasts
  - Surrogate utility development on multimodal payloads to guide target observations
- **Helicopter Role**: Scout high-uncertainty regions for ground rover; reduces rover travel time vs. naive approaches
- **Sequential Bilevel "Drop-off/Routing"**: sUAS with multimodal onboard computing for intelligent deployment

### Thread 2: AFRL - Optimal Trajectory Tracking
**Multiagent Risk-Aware Navigation Framework**:
- **Dual Asset Structure**:
  - **HVAA (High-Value Aerial Asset)**: Seeks risk-avoiding optimal path; benefits from SAA reconnaissance
  - **SAA (Sensing Aerial Asset)**: Seeks information-maximizing paths; explores high-uncertainty regions

**Three Research Sub-threads**:
1. Direct information gain / basic concept demonstration
2. Indirect information gain / probabilistic inference
3. Scalable integration of dynamics with parameterized heterogenous risk sources (weather & threat)

**Bimodal Wind Shear Modeling**:
- Addresses rapid transitions between distinct wind regimes (e.g., veering vs. backing winds in supercells)
- Models using Gaussian Mixture Models fitted to wind vector differences
- Accounts for wind shear at storm boundaries where rapid mode transitions are unknown spatiotemporal phenomena
- Look-ahead mechanism in vehicle dynamics model improves tracking of upcoming paths with guidance command upper bounds

**Wind Velocity Constraint for RRT***:
- Angular difference θ ≤ 50° between sub-path segment and wind velocity at location i
- Minimal energy utilization for navigation
- Increased coverage range for same endurance: relative speed of SAA to ocean surface > SAA airspeed

**Trajectory Tracking Control**:
- Stochastic wind-aware UAV control with expected cost formulation across multiple wind realizations
- Shifted Target design: 10–40m outward shift via normal vector to avoid sharp turns under wind stress
- Look-ahead control angle (θ_L): ~90° when far from path (correction), ~0° when close (alignment)
- Wind direction sensitivity based on λ (angle between wind and desired path)
- Groundspeed feasibility condition ensures desired heading achievable given wind constraints
- Maintains unicycle dynamics under wind disturbances

**Preliminary Results** (Direct Information Gain):
- SAA IT RRT* paths shorter than HVAA-only paths
- Grid size currently 50×50 (2,500 cells); target expansion to 2,500×50 (125,000 cells) for realism
- Uncertainty constraint threshold sensitivity:
  - SD < 40: 100% chance of not finding naive HVAA path
  - SD < 45: Naive HVAA takes longer detour; less SAA benefit
  - SD < 55: Shorter detour; reduced SAA advantage
- HVAA may follow different path than SAA if realized wind speed exceeds threshold

### Thread 3: BST - Edge AI Learning

**Temporal Multimodal Multivariate Learning for Sensor Fusion**:
- **Problem**: Standard entropy (Shannon) and divergence measures (KL) fail to distinguish multimodal distributions; bimodal distributions with different spacing have same entropy but different standard deviations
- **BST Solution** (KDD 2022 publication by Park et al., ranked 1st in data mining):
  - New utility function: f(sampling-based weighted entropy, standard deviation)
  - Formula: u_j(x) = ω(x, o_ntype) × H'_j(x, ntype, t) + SD'_j(x)
  - Weights account for number of observations of similar-type cells and probability of category in cell of each cluster at time k ∈ K
  - Normalized entropy: max(0, [O²_ntype − o²_ntype] / [O²_ntype + o²_ntype])

**Multimodal Sensor Fusion on Autonomous Surface Vehicles (ASVs)**:
- Each ASV equipped with multimodal sensors; information value changes over time
- Sequential revelation of uncertainty by grouping samples within similar-type distributions
- Direct gain (immediate observation value) + Indirect gain (learning from other agents) + Temporal gain

**Graph-Based Explainable Deep Learning**:
- Maintains information flow without losing interpretability
- Prior Univariate: Cluster mixture of 9 classifications with box size representing probability
- Learning stage: Reduces number of columns per row as errors decrease
- Posterior: Big red boxes indicate correctly classified clusters with higher probability
- Example: Observing 64 cells out of 2,500 updates belief classifications

**Improvement Results** (Prediction Reliability):
| Distribution Type | Univariate | Multivariate | Deep Multivariate |
|---|---|---|---|
| Unimodal | 2.66% | 3.28% | — |
| Temporal Non | 4.34% | 6.25% | 7.37% |
| Temporal Multimodal | — | 11.26% | 13.45% |

## Products & Capabilities Described

### Hunter-sUAS
- **Type**: Small Unmanned Aerial System for hazardous weather operations
- **Use in This Context**: Sequential bilevel drop-off and routing platform with multimodal onboard computing
- **Role**: Primary platform for SAA operations; carries multiple sensor types for data collection and fusion

### Edge AI Learning Platform (BST)
- **What It Is**: Real-time machine learning system for multimodal sensor fusion aboard autonomous vehicles
- **Technical Basis**: Graph-based explainable deep learning with temporal multimodal multivariate distribution modeling
- **Key Innovation**: Handles bimodal and multimodal uncertainty quantification; outperforms standard entropy/divergence metrics
- **Performance**: 13.45% improvement in prediction reliability for deep multivariate temporal multimodal cases
- **Deployment**: ASVs with Hunter-sUAS coordination

### Multimodal Payload Integration
- Diverse sensors generating different types of information (e.g., wind speed, direction, precipitation, pressure)
- BST system fuses this data to maximize information gain and reduce entropy across space and time
- Supports "inverse surrogate machine learning" integrated with differential game theory

## Use Cases & Applications

### Primary: Hurricane Response and Monitoring
- **Hurricane Path Forecasting**: WRF-EnKF data assimilation for hourly temporal resolution predictions
- **Real-Time Reconnaissance**: SAA (e.g., Hunter-sUAS) scouts high-uncertainty regions of hurricane field
- **Risk-Aware Asset Protection**: HVAA takes safer paths informed by SAA intelligence; reduces detour length by ~20–30% under optimal conditions
- **Wind Shear Navigation**: Handles bimodal vertical wind shear (veering vs. backing) near storm boundaries during rapid intensification
- **Operational Scenario**: Hurricane Harvey 2017 data used for validation

### Secondary: Mars Rover Operations
- Technology developed for Mars rover-helicopter teams adapted to hurricane operations
- Information-theoretic path planning scales to massive grids (673,854 cells)
- Helicopter scout pattern translates to aerial reconnaissance in hurricane context

### Threat/Adversarial Scenarios
- Framework extended to threat environments where gaining critical information without being captured is vital
- SAA constrained by maximum risk only; HVAA constrained by both maximum uncertainty and risk

## Key Results (Phase I Deliverables)

### Path Planning (SAA vs. HVAA)
- **Direct Information Gain Configuration**:
  - SAA takes longer paths through high-uncertainty regions (SD 40–120)
  - HVAA with SAA support takes shortest safe route (20–30% shorter than HVAA alone without SAA)
  - HVAA without SAA avoids obstacles and uncertainty regions via longer detours
- **Scalability Achieved**: RRT* algorithm handles 2,500-cell grids; target is 125,000-cell operational grid
- **Wind Constraint Impact**: 50° maximum angular difference increases coverage endurance; groundspeed ≥ airspeed in favorable wind

### Trajectory Tracking
- **Error Bound Design**: Shifted target (10–40m outward) prevents sharp turns; look-ahead control smooths convergence
- **Bimodal Wind Handling**: Successfully tracks desired RRT path under stochastic wind with two distinct modes (blue vs. green path variants shown)
- **Feasibility**: Unicycle dynamics maintained; control input design balances curvature correction with wind misalignment

### Edge AI Learning (Sensor Fusion)
- **Temporal Multimodal Learning Outperforms Baselines**: 13.45% improvement over standard entropy for temporal multimodal deep learning
- **Explicit Multimodal Advantage**: Accounting for bimodal distributions and variance improves predictions by ~7–11% vs. unimodal or standard multivariate approaches
- **Real Deployment**: 64 targeted observations in 2,500-cell grid suffice to update utility map and retrain surrogate models
- **Cluster Classification**: Graph-based approach produces interpretable posterior belief clusters; large red boxes indicate high-confidence correct classifications

## Notable Details

### Partnerships & Collaboration
- **NASA JPL**: Path planning methodology; Mars-to-hurricane mission analogy
- **AFRL**: Trajectory tracking under extreme uncertainty; threat parameterization
- **Penn State University**: Advanced WRF-ARW and CRTM data assimilation for hurricane forecasting
- **KDD 2022 Conference**: Park et al. published top-ranked data mining work on temporal multimodal multivariate learning (1st rank publication)

### Competitive Advantages
1. **Information-Theoretic RRT***: Outperforms standard benchmarks (DESPOT, SARSOP) on large-scale problems; POMDP stuck in local minima at >400 cells, but IT-RRT handles 673,854 cells
2. **Bimodal Uncertainty Theory**: Novel entropy+SD formulation (KDD 2022) handles multimodal distributions unavailable in standard KL divergence; critical for wind shear scenarios
3. **Heterogeneous Asset Coordination**: Principled framework for HVAA (risk-averse) and SAA (information-seeking) collaboration under threat and weather uncertainty
4. **Graph-Explainable AI**: Maintains interpretability while scaling; suitable for edge deployment on resource-constrained sUAS platforms

### Client Requirements Addressed
- **ONR Hazardous Weather STTR Focus**: Direct application to hurricane reconnaissance and forecasting improvement
- **Real-Time Decision-Making**: Edge AI on Hunter-sUAS eliminates communication latency; multimodal fusion at aircraft level
- **Scalability**: From Mars (673,854 cells) to hurricane field (millions of cells); computational tractability achieved
- **Risk Mitigation**: SAA reduces HVAA exposure to extreme wind shear and uncertain