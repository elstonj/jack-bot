# Mixture Earth Lookahead Observing Strategy (MELOS)

## Document Metadata
- **Type:** SBIR Phase I Proposal (Unfunded)
- **Client/Agency:** Navy/NOAA (Navy STTR: Hazardous Weather program)
- **Program/Solicitation:** Navy STTR Topic (specific topic number not explicitly stated in header, but document shows as "AIST23 MELOS")
- **Date:** 2023 (submission date not explicitly stated, but referenced as "AIST23")
- **BST Products/Systems Referenced:** None directly mentioned (this is not a BST proposal—see note below)
- **Key Personnel:** PI Hyung Park (Old Dominion University); Co-Is: Christopher Cione (NOAA), David Posselt (NASA JPL), Luca Ono (NASA JPL), Carolyn Miller-Hooks (GMU), Carlos Ferreira (GMU), Abdulla Iftekharuddin (GMU), Shahab Jha (NCA&T), Tommer Iftekharuddin (GMU); Collaborators: Yoichi Minamide (U of Tokyo), Dorton (SECOORA), Wei (ODU)

## Executive Summary

MELOS proposes an advanced, fully automated observing strategy for improving tropical cyclone (TC) intensity and flood forecasting by intelligently directing small unmanned aerial systems (sUAS) and other multi-tier assets to collect critical meteorological observations. The system integrates an Earth System Digital Twin (ESDT) surrogate model with machine learning-based Novel Observing Strategies (NOS) to enable real-time, adaptive decision-making that targets the highest-value observations for reducing uncertainty in TC-driven coastal and inland flooding predictions. The proposal aims to advance TC forecast accuracy from the current 32% to enable effective rapid intensification (RI) prediction, addressing a critical gap exposed by hurricanes like Idalia (2023) and Harvey (2017).

## Technical Approach

**Core Strategy:** MELOS combines four key innovations to overcome knowledge gaps in federated observing:

1. **Mixture Ensemble Correlation:** Analyzes how multivariate observations (pressure, temperature, wind speed, relative humidity, mixing ratio, dry air mass) collectively impact TC and flood forecasting uncertainty, moving beyond univariate post-processing.

2. **Invertible Neural Network (INN) Framework:** Develops a physics-informed deep learning surrogate that:
   - Integrates Graph Convolutional (GC) networks to capture spatiotemporal dynamics
   - Uses Long Short-Term Memory (LSTM) for temporal dependencies
   - Employs invertible (bijective) transformations to explicitly map latent variables z to input-output pairs [x, y], enabling explainable feature extraction
   - Trains on ensemble data assimilation outputs to uncover hidden heterogeneity and multivariate covariance structures
   - Supports both forward learning (initial condition → TC forecast → flood forecast) and inverse learning (recovering latent variables from observations)

3. **Lookahead Non-Myopic Observing Strategy:** Uses probabilistic ESDT surrogate to:
   - Generate "what-now, -next, -if" scenarios with anticipated time-varying information flow
   - Account for TC trajectory changes and sUAS arrival timing at target locations
   - Make launch location and flight path decisions based on confidence levels in TC modeling
   - Implement penalty functions for observations arriving after critical time windows

4. **Agile and Adaptive Artificial Intelligence (AAAI):** Enables:
   - On-board, real-time decision-making compatible with high-performance computing (HPC) devices (e.g., NVIDIA NANO)
   - Sequential and concurrent observation request handling via offline-online ML scenarios
   - Online surrogate updates incorporating realized observation uncertainty reduction
   - Active learning for critical sample selection to update latent space representations

**Five-Step Federated Multi-Tier Asset Planning:**
1. Develop ESDT surrogate from remote sensing/in-situ data and joint data assimilation
2. Guide first sUAS launch/path via utility map to improve TC and flood prediction
3. Update GC network through active sampling and posterior approximation
4. Guide secondary assets (Autonomous Surface Vehicle gliders, LiDAR) with shared utility models
5. Validate NOS effectiveness and retrain ESDT after mission

**Observing System Simulation Experiments (OSSE):** Will use WRF-EnKF framework to test surrogate effectiveness and compare TC forecast improvements with vs. without MELOS observations across different pressure levels.

## Products & Capabilities Described

### ESDT (Earth System Digital Twin) Surrogate
- **What it is:** Machine learning surrogate trained on ensemble data assimilation outputs to predict TC-driven coastal and inland flooding from meteorological initial conditions
- **Proposed use:** Replace expensive physics-based model simulations to enable rapid, real-time information gain calculations and adaptive observation planning
- **Technical specs:**
  - Input: Ensemble of WRF-EnKF meteorological initial conditions (60 ensemble members per TC case)
  - Output: Ensemble forecasts of coastal/inland flooding uncertainty (12-24 hour window)
  - Architecture: GC-LSTM with INN integration
  - Training data: 60 ensemble WRF-EnKF simulations × flood models (ADCIRC for coastal, runoff models for inland)
  - Loss function: Conditional likelihood logfθ(y|x) minimized with L2 regularization
  - Evaluation metrics: MAE, MAPE, RMSE compared against benchmarks (ARIMA, Dynamic GCRN, Adaptive GCRN, Diffusion CNN)

### NOS (Novel Observing Strategy)
- **What it is:** Physics-informed machine learning framework for autonomous target selection and adaptive routing of observation platforms
- **Proposed use:** Direct sUAS, gliders, and LiDAR deployments to locations maximizing information gain for TC-flood forecasting
- **Key capabilities:**
  - Utility map generation showing ensemble spread reduction across spatial domain
  - Multimodal mixture entropy calculation accounting for direct and indirect observation gains
  - Graph clustering to identify cells with similar uncertainty distributions (e.g., wind speed, pressure combinations)
  - Posterior belief updates via variational Bayesian inference
  - Wind-constrained path planning with angular difference constraints between sUAS trajectory and wind velocity
  - Online active learning to quantify whether new observations exceed uncertainty reduction threshold
  - Temporal lookahead mapping for sequential asset deployment planning
  - Resilience to observation noise through non-myopic decision-making

### Multimodal Mixture Learning Framework
- **What it is:** Extension of prior work (NSF-funded Sequential Temporal Multimodal Multivariate Learning / TMML) to handle multivariate observations from heterogeneous sensors
- **Proposed use:** Integrate 4+ atmospheric state variables (pressure, temperature, wind speed, relative humidity) to capture indirect sensing benefits
- **Innovation:** Updates all cells within a cluster sharing similar uncertainty distributions, not just directly observed cells, enabling global uncertainty reduction from local observations

### Graph Convolutional Network (GC) for Physics Semantics
- **What it is:** Deep learning layer that encodes spatial relationships between model grid cells
- **Proposed use:** Capture TC dynamics through learned (data-driven) and prescribed (physics-informed) adjacency matrices
- **Physics parameters:** CAPE (Convective Available Potential Energy), vertical wind shear, atmospheric instability indices, moist convection
- **Semantic adjacency:** Derived via Wasserstein distance between bivariate kernel density estimates of joint probability distributions

## Use Cases & Applications

### Primary Use Case: Hurricane-Driven Flooding Forecasting
- **Mission:** Improve 12-24 hour forecasts of TC rapid intensification and resulting coastal/inland flooding
- **Problem addressed:** Current NWP models correctly predict RI in only 32% of cases (up from 12% in 2010s); rapid intensification changes forecasting windows from days to hours
- **Historical examples:** 
  - Hurricane Idalia (2023): RI from Category 1 to 4 in 24 hours; Hampton Roads evacuation challenges
  - Hurricane Harvey (2017): No model correctly predicted RI; subsequent storm surge/inundation forecasting failed
  - Hurricane Ian (2022): Case study for proposed system validation
  - Also references: Hurricanes Maria (2017), Michael (2018), Tammy (2023), Nigel (2023), Edouard (2014)
- **Geographic focus:** Atlantic coast (focus on Virginia/Mid-Atlantic, Florida), Gulf of Mexico, Chesapeake Bay

### Secondary/Future Applications Mentioned:
- **Arctic sea ice evolution monitoring** (adaptive timing of observations to capture variability)
- **Wildfire detection** (applying broader sensing strategy utility)
- **Validation for satellite missions:** NASA PACE (Plankton, Aerosol, Cloud, ocean Ecosystem) and PACE-PAX postlaunch airborne experiments
- **Low Earth orbit satellite control:** Direct satellite slewing up to 15° off-nadir for targeted observations
- **City-level applications:** Norfolk, VA street-level hydrodynamic modeling for flood resilience (letter of support from city's Office of Resilience)
- **Hydrological forecasting:** Inland streamflow prediction for water resource management

## Key Results (for reports)

**This is a proposal, not a completed report**, so no empirical results are presented. However, the document outlines anticipated deliverables and TRL progression:

### Technology Readiness Level (TRL) Targets:
- **Input TRL:** 2 (concept/simulation-based work from prior NSF/JPL funding)
- **Output TRL:** 4 (technology demonstration with sUAS field deployment)
  - Task 1 (NOS validation): TRLout3 by end of Year 1
  - Task 2 (ESDT validation): TRLout3 by end of Year 1
  - Task 3 (Integrated NOS-ESDT demonstration): TRLout4 by end of Year 2

### Anticipated Performance Improvements:
- **Specific improvements not quantified**, but proposal claims:
  - "Fully integrate NOS on executable, on-board, high-performance computing systems"
  - Improved forecast accuracy through active targeting of critical PBL variables
  - Capture "more variability than manned measurements"
  - Reduced computational cost for ensemble flood simulations via surrogate models
  - Resilience to observation noise without oversimplification of high-resolution latent state space

## Notable Details

### Partnership & Institutional Collaboration:
- **Lead:** Old Dominion University (ODU, PI Hyung Park) — Minority-serving institution with 30% underrepresented population
- **Co-Investigators:**
  - NOAA (Christopher Cione, sUAS deployment expert, White House ICAMS executive director, DoC Gold Medal recipient for Hurricane Ian sUAS work)
  - NASA JPL (David Posselt—OSSE framework; Luca Ono—onboard HPC robotics integration)
  - George Mason University (GMU, Carolyn Miller-Hooks—time-dependent path planning; Carlos Ferreira—coastal hydrodynamic modeling ADCIRC/SWAN; Iftekharuddin—invertible ML)
  - North Carolina A&T University (NCA&T, Shahab Jha—inland hydrological modeling, SWAT/LSTM integration)
- **Collaborators:**
  - University of Tokyo (Yoichi Minamide—WRF-EnKF simulations, ensemble correlation analysis)
  - SECOORA (Glider/autonomous surface vehicle data)
- **External Support Letters:** City of Norfolk Office of Resilience (STORM Map real-time flood integration)

### Existing Prior Work & Datasets:
- **WRF-EnKF ensemble simulations:** Available for all 2017 hurricanes; additional simulations planned for Ian (2022) and other RI cases
- **NOAA sUAS eye-of-the-storm data:** Historical missions to Edouard (2014), Maria (2017), Michael (2018), Ian (2022), Tammy (2023), Nigel (2023)
- **Coastal flooding data:** High-resolution, unstructured-grid ADCIRC+SWAN models for Arctic, South Atlantic, Bay of Bengal, Gulf of Mexico, North Atlantic; real-time forecast system operational in Mid-Atlantic
- **Inland runoff data:** Existing SWAT/LSTM model outputs for streamflow prediction
- **Remote sensing:** Surface Water & Ocean Topography (SWOT), Reflected Global Navigation Satellite System (RGNSS), radiometer systems under ESTO development

### Competitive Advantages:
1. **