# B3: Turbulence And Wave Height

## Document Metadata
- Type: Phase I Deliverable Report
- Client/Agency: U.S. Navy
- Program/Solicitation: Navy STTR, Hazardous Weather topic
- Date: Created 2025-09-11, Modified 2025-12-17
- BST Products/Systems Referenced: S0 UAS
- Key Personnel: Maciej Stachura (last editor); Chris DeLoach (University of Notre Dame, methodology development); Jfödrick Wadler, Gail Lin, James Cione, Jing Zhang, Justin Elston (co-authors on Deloach et al. 2025)

## Executive Summary
This Phase I deliverable addresses two related tasks: (1) measuring atmospheric boundary layer turbulence in tropical cyclones using the S0 UAS's 100 Hz multi-hole pressure probe to calculate drag coefficients (CDN) and momentum flux, and (2) developing onboard wave height measurement capabilities using radar altimetry with a Kalman filter. The work demonstrates that the S0 is the only current mechanism for obtaining high-frequency wind measurements needed to calculate over-water turbulent fluxes near the air-sea interface in tropical cyclones, and establishes validated methodologies for drag coefficient calculation while defining Phase II requirements for wave spectrum estimation.

## Technical Approach

### Turbulence Measurement via Drag Coefficient Calculation

**Core Methodology:**
- Uses 3D wind measurements from S0's multi-hole pressure probe (MHPP) at 100 Hz onboard sampling
- Calculates 10-meter neutral drag coefficient (CDN) using established bulk aerodynamic formulas combined with direct covariance momentum flux measurements
- Methodology follows established procedures from CBLAST (Coupled Boundary Layer Air-Sea Transfer) experiment and peer-reviewed studies (French et al. 2007, Andreas et al. 2012, Vickers et al. 2013)

**Key Equations & Process:**
1. Adjusts measured winds to 10-m neutral equivalent using logarithmic wind profile and stability corrections (Obukhov length scale ζ)
2. Calculates momentum flux (τ) from detrended flight legs at constant altitude: τ = -ρ(u'w') where primes denote deviations from mean
3. Solves for CDN by setting bulk aerodynamic formula equal to direct-covariance measurement
4. Accounts for vertical variations in flux layer (constant flux assumption below 200m, adjusted reduction 200-500m based on CBLAST data)

**Quality Control Steps:**
- Manual leg determination based on relatively-flat flight patterns from stepped descent profiles
- Standardized leg length of 30+ km minimum (legs >60 km broken into segments)
- Stationarity verification: ensures legs don't mix multiple storm regimes (inflow vs. eyewall)
- Spectral analysis validation: confirms data follows -5/3 Kolmogorov law for energy cascade; ensures wavelength of dominant eddies is captured
- Data continuity requirement: minimum 95% data coverage with no gaps >15 seconds
- Final dataset (2024 season): 26 legs ≤200m altitude, 55 legs ≤500m altitude

**Data Frequency Optimization:**
- 2024 flights achieved median 3.5 Hz return rate (downsampled from 100 Hz onboard due to bandwidth)
- Algorithm now runs onboard at 100, 50, 25, 10, and 5 Hz to determine minimum sufficient frequency
- Colorado over-land validation (3 km legs, 90m AGL) showed CDN calculations remain consistent across 100 Hz, 10 Hz, and 1 Hz frequencies, suggesting 1 Hz may suffice for CDN calculation

### Wave Height Measurement

**Sensor & Requirements:**
- Radar altimeter onboard S0 (replaces laser altimeter which struggled in heavy precipitation)
- Target accuracy: Significant Wave Height (Hs) <3% error, Mean Squared Slope (MSS) <10% error (per ONR SASCWATCH project requirements)
- Onboard processing via Kalman filter to estimate wave spectrum

**Analysis Assumptions (Phase I):**
- Ground speed: 50 m/s (actual range in hurricanes: 10-100+ m/s)
- Sampling rate: 50 Hz (range sensor sampling rate; increasing beyond this provides minimal improvement)
- True Hs: 10 m (hurricane range: 10-20 m)
- True MSS: 0.05 rad (hurricane range: 0.05-0.1 rad)
- Wave period: 12 s
- Fixed window length for MSS calculation: 10 m

**Error Analysis Results:**
- Hs error: <3% goal achievable with 20 km track length at 50 m/s ground speed (6.7 min integration)
- MSS error: requires range sensor accuracy <30 cm for 20 km track; improved to ~50 cm for 40 km track (13 min integration)
- Hs remains <3% even with 5 m range error (well within S0 GPS/radar capabilities)
- MSS error can reach 5% with 80 km sample distance (though stationarity assumption may not hold over such distances)

**Phase II Planned Approach:**
- Implement Extended Kalman Filter in spectral domain (standard approach for HF radar, satellite altimetry, lidar buoys, airborne SAR)
- Model surface elevation η as Fourier series along flight track with spectral grid kj matching hurricane sea conditions
- Use Gauss-Markov process with exponential decay factor (|φ| < 1) for state time updates
- Process includes standard EKF steps: time update (state and covariance), measurement update, and final Hs/MSS estimation from Fourier coefficients
- S0 already runs multiple Kalman filters for flight control and 3D wind estimation (hardware/software foundation in place)

## Products & Capabilities Described

### S0 UAS
- **Multi-hole pressure probe (MHPP):** Measures 3D wind components at 100 Hz onboard; enables high-frequency turbulence observations not possible with crewed aircraft or radiosondes
- **Radar altimeter:** Small radar system under development for wave height measurement; overcomes weather limitations of laser altimeter in heavy precipitation
- **Onboard computing:** Runs real-time algorithms for wind calculation (100 Hz), drag coefficient calculation, and Kalman filtering for wave spectrum estimation
- **Sensor suite:** Fast-response thermistor, hygrometer, GPS/INS, static pressure sensor
- **Operational capability:** Stepped descent flight patterns in tropical cyclones starting from 1000-1500 m; can maintain ~10 minute level legs at target altitudes

## Use Cases & Applications

### Tropical Cyclone Boundary Layer Research
- Direct measurement of air-sea exchange coefficients and momentum flux in hurricane boundary layer
- Data collection at heights as low as 60 m over open ocean in tropical storm-force winds and higher
- Supports improvement of numerical hurricane models through better parameterization of surface drag and momentum loss
- Wind-wave alignment studies to evaluate impact on surface roughness and drag coefficient

### Specific 2024-2025 Operations:
- **2024 hurricane season (19 S0 flights):** Hurricanes Ernesto, Francene, Helene, Milton
- **2025 hurricane season (17 flights, ongoing QC):** Hurricanes Erin, Gabrielle, Imelda, Melissa
- **New 2025 flight pattern:** "Flux profile" stepped descents with aircraft heading into wind at 500 m and below to evaluate robustness of constant-flux-layer assumption and validate height adjustment methodology

### Broader Applications:
- Co-location of momentum flux with ocean wave properties to understand wind-wave interaction
- Validation framework for large-eddy simulations (LES) of tropical cyclones
- Real-time operational measurements for hurricane forecasting and model improvement

## Key Results (for reports)

### Turbulence/Drag Coefficient Results (2024 Hurricane Season)

**Primary Findings:**
- Calculated CDN values show expected behavior: relatively constant between 15-25 m/s, then drop-off at higher wind speeds (consistent with Powell 2003 and subsequent studies by Bell et al. 2012, Holthuijsen et al. 2012, Curcic & Haus 2020, Richter et al. 2021)
- Best-fit CDN line from 26 legs below 200 m altitude and 55 legs below 500 m (using altitude-adjusted momentum flux) shows good agreement with CBLAST measurements from Black et al. (2007)
- Methodology validation using idealized LES of Category-5 hurricane: CDN calculation within 10% of prescribed value (2.4×10⁻³) below 125 m; error increases with altitude to ~146% at ~375 m due to non-logarithmic profiles and flux layer violations above 100 m

**Data Quality & Consistency:**
- Spectral analysis confirms Kolmogorov -5/3 energy cascade for all flight legs
- Over-land Colorado validation (3 km legs, 100 Hz data): 23% difference in CDN between repeated adjacent flight tracks (orange/black pair), consistent with DeLoach et al. (2025) over-land observations; larger spread in blue/red pair
- Data frequency study: CDN remains remarkably stable from 100 Hz → 10 Hz → 1 Hz for tested leg, suggesting 1 Hz sufficient (though testing in hurricanes/high winds needed before confirming)

**Altitude Correction Key Finding:**
- Statistical analysis of CBLAST data shows:
  - **Below 200 m:** No significant trend in momentum flux with height (p=0.24, constant flux layer assumption valid)
  - **200-500 m:** Statistically significant decrease in momentum flux with height (p<0.001), requiring adjustment factor based on CBLAST height-flux relationship
  - Applied adjustment increases derived CDN values for 200-500 m data points

**Caveats & Uncertainties Identified:**
1. Altitude correction based on CBLAST moat-region data only; unclear if relationship holds in eyewall regions
2. Small sample size of CBLAST observations
3. Wind reduction to 10-m assumes logarithmic profile; individual dropsondes often show non-logarithmic profiles
4. 2024 median data rate (3.5 Hz) much lower than 100 Hz onboard sampling due to bandwidth; 2025 flights with improved data recovery and new flux-profile flight pattern underway for validation

### Wave Height Results (Phase I Analysis)

**Error Budget Analysis:**
- **For 20 km track (6.7 min integration at 50 m/s):**
  - Hs: <3% error achievable (range sensor error up to ~5 m acceptable)
  - MSS: requires <30 cm combined range/altitude error for <10%
  
- **For 40 km track (13.3 min integration):**
  - MSS error improved to achieve target with ~50 cm combined range/altitude error (challenging but likely achievable per document)
  
- **Extended 80 km sample:**
  - MSS can reach ~5% error (assumes water surface remains stationary, which questionable over such distance)

**Practical Findings:**
- Hs measurement is well within capability; primary constraint is MSS accuracy
- Critical limiting factor: fused GPS/INS/static pressure altitude accuracy (not range sensor alone, which can achieve 5 cm)
- 50 Hz radar sampling rate determined adequate; higher rates provide minimal improvement

## Notable Details

### Partnerships & Collaborations
- **University of Notre Dame:** Chris DeLoach performing idealized LES validation and drag coefficient methodology development
- **University of Michigan & Embry-Riddle Aeronautical University (ERAU):** Partners on Phase I task
- **NOAA:** Operates S0 platform; provides operational flight experience in hurricanes
- **ONR (Office of Naval Research):** Primary funding agency; SASCWATCH project defines accuracy requirements

### Historical Context
- References CBLAST experiment (2003-2004) as benchmark dataset for boundary layer turbulence in tropical cyclones; only prior major campaign collecting flux data in hurricane boundary layer using crewed aircraft
- Compares S0 capabilities favorably to Saildrone (20 Hz sonic anemometers, but fixed location <5 m above surface) and dropsondes (snapshot profiles, not continuous flux measurement)

### Unique Capabilities & Competitive Advantages
1. **Only mechanism for high-frequency overwater turbulence