# NOAA SICLON Proposal

## Document Metadata
- **Type:** Research proposal / Funding application
- **Client/Agency:** NOAA Office of Oceanic and Atmospheric Research (OAR)
- **Program/Solicitation:** NOAA-OAR-WPO-2025-28602, Priority OBS-4
- **Date:** 2025 (submitted for August 2025 – July 2027 project period)
- **BST Products/Systems Referenced:** Black Swift Technologies S0 (small uncrewed aerial system/sUAS)
- **Key Personnel:** 
  - Lead PI: Dr. Hyoshin (John) Park (Old Dominion University)
  - Co-PIs: Dr. Joe Cione (NOAA/AOML), Drs. Derek Posselt and Longtao Wu (UCLA JIFRESSE), Joshua B. Wadler (Embry-Riddle Aeronautical University)
  - Collaborators: Dr. Yuh Lang Lin (NCA&T), Dr. Masashi Minamide (University of Tokyo), Dr. Yu Gu (UCLA), Sarah Kirkland (ODU), Kyle Spencer (City of Norfolk)

## Executive Summary
SICLON (Sequential Inflation & Covariance Localization for Observing Network) proposes developing a self-learning, computationally efficient preprocessing system that uses probabilistic superobbing of high-resolution airborne reconnaissance data (sUAS, Tail Doppler Radar, dropsondes) to improve tropical cyclone (TC) forecasting. The system employs meta-learning and uncertainty quantification to automatically determine optimal grid spacing for combining observations, enabling real-time adaptive sampling strategies for sUAS deployment in TC operations. The project aims to advance from Readiness Level 3 to RL 5 over two years, transitioning this capability toward operational use with NOAA's Hurricane Research Division and National Hurricane Center.

## Technical Approach

### Core Innovation: Probabilistic Superobbing with Meta-Learning
SICLON combines four key technical components:

1. **Uncertainty Quantification (UQ) for Superobbing (Activity 1 - ODU Lead)**
   - Replaces traditional static grid spacing (e.g., fixed 5 km radial / 5° azimuthal) with adaptive, data-driven resolution selection
   - Uses Temporal Multimodal Multivariate Learning (TMML) to rapidly access background error covariance and identify optimal superobbing grid spacing for new TC data
   - Employs entropy-based metrics (superior to standard deviation) to measure observation contributions to reducing forecast uncertainty, particularly for non-Gaussian distributions
   - Implements mixture modeling using Gaussian probability density functions (PDFs) to handle multimodal distributions common in boundary layer observations from sUAS
   - Applies Graph Convolutional Networks (GCN) to represent spatiotemporal error correlations and map interconnected variables (wind, pressure, temperature)
   - Introduces covariance localization via weighting functions that decrease with distance, with influence radii adapted per observation type

2. **TC Data Assimilation with Reconnaissance Data (Activity 2 - UCLA Lead)**
   - Develops 80-member ensemble using WRF-Ensemble Kalman Filter (WRF-EnKF) with Advanced Research WRF (ARW) v4.6.1
   - Uses three two-way-nested domains with finest resolution of 1 km, 60+ vertical levels to 10 hPa
   - Assimilates conventional observations (reconnaissance, dropsondes, satellite) within 3-hour windows and 600 km radius around storm center
   - Applies differentiated localization radii: 405/135/45 km for surface/flight-level observations; 810/270/90 km for dropsondes
   - Transitions from WRF-EnKF to NOAA's Hurricane Analysis and Forecast System (HAFS) for operational compatibility
   - Tested on 2024 major hurricanes (Ernesto, Francine, Helene, Milton) with sUAS deployments

3. **Meta-Learning for Grid Spacing Optimization (Activity 3 - ODU Lead)**
   - Uses invertible deep learning with Graph Convolutional Networks to train on prior/posterior error pairs
   - Trains on ≥100 simulated TC scenarios with uniformly distributed observations around storm eye
   - Employs bijective transformation functions and likelihood estimation for conditional density computation
   - Upon new sUAS observations, grid spacing self-adjusts based on trained model, enabling finer-scale superobbing closer to model probability distribution

4. **Validation Through Observing System Experiments (Activity 4 - UCLA Lead)**
   - Conducts data denial experiments using OSE framework with HAFS at 3-hour temporal resolution
   - Compares against static benchmarks (200 km × 100 hPa × 3 hr superobbing)
   - Evaluates forecast error as difference in maximum wind speed / minimum sea level pressure vs. best track data
   - Tests on rapid intensification scenarios and multiple TC stages
   - Assesses whether allowing more data in initial DA cycle better represents observed vortex structure

### Computational Architecture
- Onboard processing: Self-generates superobs directly on aircraft/sUAS before transmission, enabling faster data relay and real-time decision-making
- Ground processing: ODU's Wahab HPC with 6,320 cores, 72 NVIDIA V100 GPUs, 100 Gbps Infiniband interconnect
- Software containerization (Docker) for reproducibility; shared Git repositories; PyTorch optimization framework

## Products & Capabilities Described

### Black Swift Technologies S0 (sUAS)
- **What it is:** Small uncrewed aerial system (~3 pounds) with up to 100 minutes battery life and 190 nautical mile communications range
- **Use in SICLON:** Primary in-situ reconnaissance platform deployed from P-3 aircraft
- **Specifications & capabilities:**
  - Typical operational altitude: 5,000 ft or below (for P-3 deconfliction)
  - Collects standard meteorological data: temperature, pressure, humidity, 3D winds
  - Wind measurement derived from turbulence-quality multi-hole pressure probe
  - Current data transmission: 4–5 Hz (aiming for >10 Hz by project end)
  - Customizable flight patterns: eye center-fix, eyewall flight, or inflow layer spiral
  - Vertical stepped descent patterns with 5–10 minute legs designed for turbulence parameter computation
  - Bandwidth-limited transmission to P-3

**BST's Role in SICLON:** The S0 serves as the primary adaptive sampling platform. SICLON's "importance/utility map" (Figure 2) identifies high-uncertainty regions, enabling optimal sUAS drop location and flight routing. Real-time superobbing onboard the S0 reduces data transmission burden and allows rapid operator decisions about next sampling point. This closes the loop: observations → utility map update → new sUAS target selection.

### Complementary Platforms
- **Tail Doppler Radar (TDR):** Airborne radar from P-3; provides high-resolution wind retrievals
- **Dropsondes:** Expendable profilers; assimilated with larger localization radii (810/270/90 km for 3 domains)
- **HAFS (Hurricane Analysis and Forecast System):** NOAA operational forecast model; transition target for operational deployment

## Use Cases & Applications

### Primary Mission: Tropical Cyclone Reconnaissance and Forecasting
- **TC Intensity and Track Prediction:** Improved DA from optimally-sampled high-resolution observations reduces forecast errors in TC maximum wind speed and minimum sea level pressure
- **Rapid Intensification Detection:** Targeting high-uncertainty regions helps capture processes driving rapid TC intensification
- **Operational Flight Planning:** Real-time utility maps enable crews aboard P-3/sUAS to make adaptive sampling decisions mid-mission
- **NHC Decision Support:** Provides National Hurricane Center with quantified understanding of how specific flight paths and observation networks improve forecasts

### Specific Historical Test Cases
- 2024 Hurricanes: Ernesto, Francine, Helene, Milton (tested with 19 sUAS deployments total)
- Range of TC conditions: weak vs. strong, early-stage vs. mature lifecycle stages

### Secondary Applications
- **Coastal Flood Forecasting:** Improved TC forecasts enhance coupled ocean-atmosphere models for storm surge/flood prediction
- **Hampton Roads / Norfolk Resilience:** City of Norfolk uses TC forecasts for flood risk planning; SICLON outputs integrate into "Waze"-like flood awareness app for road inundation mapping
- **Transferability:** Framework can extend to flood forecasting, coastal city emergency management

## Key Results (Anticipated, Not Yet Realized)

This is a proposal for a 2-year project (Aug 2025 – Jul 2027), so results are prospective. However, the proposal outlines expected milestones:

### Readiness Level Progression
- **Starting RL:** 3 (existing superobbing/optimal observing work at RL 2–3; deployment technology at RL 7)
- **Year 1 Target:** RL 4 (integration with new TC DA; self-learning prototype functioning in simulations)
- **Final (Year 2) Target:** RL 5 (self-learning prototype demonstrated operational in NOAA reconnaissance aircraft/sUAS with accurate operational data stream management)

### Expected Outputs
1. **Self-supervised superobbing tool** that autonomously samples high-resolution in-situ observations, validated in P-3 environment
2. **Open-source software package** (via Zenodo/GitHub) with Python, MATLAB, C++ code for superobbing, self-resolution modeling, correlation mapping, parallel computing
3. **Courseware and training materials** for K–12 and university curricula
4. **Operational decision-support module** for onboard aircraft/sUAS: real-time utility map computation, observation-steering capability
5. **Observing system experiment database** documenting TC forecast sensitivity to SICLON-optimized sampling vs. traditional methods

### Validation Metrics
- Reduction in TC forecast error (wind speed, sea level pressure) relative to static superobbing benchmarks
- Faster data transmission cycles (fewer observations, higher information density)
- Demonstration of improved handling of asymmetric observation distributions and non-Gaussian boundary layer dynamics

## Notable Details

### Budget & Duration
- **Total Budget:** $600,000 over 2 years
  - Year 1: $300,000
  - Year 2: $300,000
- **Institutional Distribution:**
  - Old Dominion University (Lead): $380,000
  - UCLA/JIFRESSE: $200,000
  - NOAA HRD/AOML: $20,000
  - ERAU Subaward (via ODU): ~$60,000 total
- **Additional Support:** ODU and UCLA will support NCA&T faculty travel and student internships

### Key Partnerships & Collaborations
- **Academic:** Old Dominion University (lead), UCLA JIFRESSE, Embry-Riddle Aeronautical University, North Carolina Agricultural & Technical University (HBCU), University of Tokyo
- **Operational:** NOAA Hurricane Research Division (HRD), NOAA Atlantic Oceanographic and Meteorological Laboratory (AOML), National Hurricane Center (NHC)
- **City/Resilience:** City of Norfolk Resilience Office (flood forecasting application)
- **Industry:** Black Swift Technologies (sUAS provider)

### Technology Transfer & Intellectual Property
- Pending patent on TMML-based TC observing network (Park et al. 2023)
- Open-source release planned for final project year
- Compatible with NOAA operational frameworks (HAFS, data protocols)

### Education & Diversity Initiatives
- Partnership with Kempsville High School (Virginia Beach) recognized as "model partnership" by VBCPS
- Collaboration with NCA&T (HBCU); support for underrepresented minorities in STEM
- PI Park's track record: mentored 6 female graduate students (4 Black women) over 6 years
- ODU ranked Top 10 in ethnic diversity; 30% underrepresented population
- Engagement of K–12 students through local storm-based curriculum integration
- Graduate/undergraduate research assistantships; conference presentation opportunities

### Computational Resources
- **Primary HPC:** ODU Wahab Research Environment
  - 6,320 computational cores
  - 72 NVIDIA V100 GPUs
  - 40 cores/node at 2.4 GHz, 368 GB RAM per node
  - 100 Gbps Mellanox