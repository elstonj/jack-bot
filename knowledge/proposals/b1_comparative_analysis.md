# B1: Comparative Analysis

## Document Metadata
- Type: Technical report / Phase I deliverable
- Client/Agency: U.S. Navy
- Program/Solicitation: Navy STTR, Hazardous Weather topic
- Date: 2025 (modified 2025-10-06)
- BST Products/Systems Referenced: S0 (small UAS), Multi-Hole Pressure Probe (MHPP)
- Key Personnel: Maciej Stachura (last editor); cited: Deloach, C.J.; Elston, J.S.

## Executive Summary
This comparative analysis evaluates atmospheric profiling platforms for tropical cyclone (TC) observation, with emphasis on measurement uncertainties and logistical challenges. The report demonstrates that Black Swift Technologies' S0 small UAS provides superior data coverage, temporal resolution, and turbulence measurement capabilities compared to traditional dropsondes, Tail Doppler Radar, and competing UAS platforms (Anduril Altius-600), while offering unique advantages for targeted observations away from flight tracks.

## Technical Approach
The analysis conducted under Task B.1 reviews existing atmospheric profiling systems (NCAR dropsondes, radiosondes, Raytheon Coyote, Anduril Altius-600) and compares them against S0 performance metrics. The comparison focuses on:
- Cost per observation
- Data accuracy and resolution
- Spatial and temporal coverage
- Platform longevity and operational availability
- Specific capabilities for turbulence measurement
- Results from actual S0 missions in 2024-2025 hurricane seasons

## Products & Capabilities Described

### S0 Small UAS
**What it is:** A 3-pound air-deployable UAS developed by Black Swift Technologies for atmospheric sampling in tropical cyclones.

**Sensor suite:**
- Vaisala RSS421 package (pressure, temperature, humidity) — same sensors as Vaisala dropsondes
- Downward-pointing infrared sensor for sea surface temperature (SST) measurement
- Multi-Hole Pressure Probe (MHPP) manufactured by BST, capable of measuring turbulence-quality winds at up to 100 Hz (currently limited to ~3.5 Hz transmission to aircraft, but full 100 Hz available in recoverable operations)
- Dual-GPS system (upgraded 2025) for improved heading accuracy: 0.5° (upgraded from 3° with magnetometers in 2024)
- Radar altimeter (new 2025): activated below 50m altitude for accurate altitude measurement independent of GPS drift or wave height

**Performance metrics (2024 version):**
- Mission duration: 105 minutes typical
- Data points per full flight: ~6,300 observations
- Equivalent to ~18 dropsondes in observation count

**Performance metrics (2025 upgrades):**
- Mission duration: Expected real maximum 2 hours in tropical cyclones (111 minutes demonstrated in Tropical Storm Imelda with remaining battery capacity)
- Data points per full flight: ~25,412 observations (4x increase over 2024)
- Under 500m altitude: 23,807 observations (~286 dropsonde equivalent)
- Under 100m altitude: 23,380 observations (~1,403 dropsonde equivalent)
- Communication range: 210 nmi demonstrated in clear-air testing at 1,500m altitude; 160 nmi achieved in Tropical Storm Imelda at 150m altitude (significantly exceeds Altius-600 capability of 130 nmi)

**Operational record:**
- First successful hurricane flight: Hurricane Tammy (2023)
- 2024 season: 19 launches across Hurricanes Ernesto, Francine, Helene, and Milton
- 2025 season (as of October 1, 2025): Deployed in Tropical Storms Erin, Gabrielle, and Imelda

### Multi-Hole Pressure Probe (MHPP)
- Manufacturer: Black Swift Technologies
- Capability: Measures turbulence-quality winds at up to 100 Hz
- Housing: Waterproof 5-hole design (unique for small UAS applications; team is unaware of other waterproof 5-hole probes with sufficient size/weight/power (SWAP) characteristics for small UAS)
- Status: Only MHPP currently being used to sample winds in tropical cyclones
- Historical context: P-3 previously used MHPP to determine turbulent characteristics

### Competing/Comparative Systems

**Vaisala Dropsonde (NCAR)**
- Sensor resolution/accuracy: Temperature 0.01°C (±0.1°C repeatability); RH 0.1% (±2% repeatability); Pressure 0.01 hPa (±0.4 hPa); Horizontal Wind 0.1 m/s (±0.5 m/s)
- Fall rate: ~10 m/s
- Profile duration: 2–5 minutes
- Measurement rates: Wind at 4 Hz, thermodynamic at 2 Hz
- Data coverage: Vertical profiles only along/near flight track
- Post-processing: ASPEN software (NCAR) corrects for sensor response times, wind shear, data aliasing; no methods exist to correct sensor lag without additional smoothing
- Limitation: Cannot measure turbulent-scale processes
- Research variant: Adds downward-pointing passive IR for SST

**Skyfora StreamSonde**
- Sensor resolution: Temperature 0.01°C (±0.3°C repeatability); RH 0.01% (±4% repeatability); Pressure 0.01 hPa (±0.5 hPa); Horizontal Winds 0.01 m/s (±0.1 m/s)
- Fall rate: ~5 m/s (half that of Vaisala dropsonde, yielding double the data per profile)
- Simultaneous deployment: Up to 50 (vs. 8 for Vaisala)
- Limitation: Cannot target specific regions beyond directly downwind of flight track

**P-3 Tail Doppler Radar (TDR)**
- Coverage: ~50 km horizontal range from aircraft
- Spatial resolution: 2 km horizontal, 0.5 km vertical (profile mode: 0.15 km vertical)
- Altitude coverage: 0.5–18 km typical
- Data: 3D winds via variational analysis (solves radar equations and mass continuity)
- Wind accuracy: Horizontal RMSEs generally <2 m/s; vertical wind <1 m/s
- Limitations: Constrained by P-3 flight patterns (often inflexible during operations); no thermodynamic data in boundary layer; provides kinematic data only

**Anduril Altius-600**
- Weight: ~25 pounds
- First TC deployment: Hurricane Ian (2022), 102-minute flight
- Theoretical max range: 240 minutes
- Communication range: 130 nmi (Hurricane Ian)
- Sensor suite: Same as S0 (Vaisala RSS421 + downward IR + optional MHPP)
- Current status: Slower communication range and shorter demonstrated flight time than S0

**Historical systems (no longer manufactured):**
- Aerosonde (first generation, deployed 2005 Hurricane Ophelia)
- Raytheon Coyote (second generation, 2014–2018; data coverage shown in Figure 1)

## Use Cases & Applications

**Primary mission:** Real-time atmospheric profiling and turbulence measurement in tropical cyclones for operational forecast and research purposes.

**Specific deployments documented:**
- Hurricane Ian (2022) — Altius-600
- Hurricane Tammy (2023) — S0 first deployment
- Hurricane Ernesto (2024) — S0
- Hurricane Francine (2024) — S0
- Hurricane Helene (2024) — S0 (detailed comparative analysis provided)
- Hurricane Milton (2024) — S0
- Tropical Storm Erin (2025) — S0
- Tropical Storm Gabrielle (2025) — S0
- Tropical Storm Imelda (2025) — S0 (111-minute mission; detailed turbulence data analysis provided)

**Operational context:** Deployed from NOAA WP-3D Orion (P-3) or USAF C-130J Hercules during operational and research reconnaissance missions into tropical cyclones.

## Key Results

### Data Coverage & Quantity Advantage
- **S0 vs. Dropsondes (2024):** Single S0 flight collected ~6,300 observations vs. 18 dropsonde equivalents (~$18K in dropsonde cost for equivalent data)
- **S0 vs. Dropsondes (2025):** Single S0 flight collected ~25,412 observations vs. 76 dropsonde equivalents (~$76K in dropsonde cost)
- **Inner core advantage:** Figure 3 shows S0 provides much better spatial coverage in inner core region (r<100 km) compared to dropsondes
- **Lower-level observations (high-value region):**
  - Under 500m: 23,807 observations (~286 dropsonde equivalent; ~$286K value)
  - Under 100m: 23,380 observations (~1,403 dropsonde equivalent; ~$1.4M value)

### Unique Turbulence Measurement Capability
- **Example case: Tropical Storm Imelda (September 29, 2025):**
  - S0 flight path: ~300 km trajectory (vs. single vertical profile from dropsonde)
  - Vertical wind structure: Nearly 4x increase in turbulence intensity from 100m to 50m altitude
  - Dropsonde comparison: While dropsonde captured mean wind profile accurately, it provided no insight into turbulence structure variation with altitude
  - This capability is unique to small UAS; cannot be replicated by dropsondes, TDR, or previous-generation Coyote

### System Reliability & Evolution
- **2025 improvements demonstrate rapid advancement:**
  - Battery upgrade: Real maximum mission time increased to 2 hours (from 105 minutes in 2024)
  - Heading accuracy: Improved from 3° (magnetometer-based) to 0.5° (dual-GPS)
  - Communication range: 210 nmi clear-air; 160 nmi in actual storm conditions (exceeds Altius performance)
  - Radar altimeter: Provides wave-height-independent altitude measurement below 50m; unique among TC-deployed UAS

### Turbulence Data Quality
- Deloach et al. (2025) demonstrated that S0 measurements in low winds are already usable for computing turbulence parameters near the air-sea interface
- Waterproof 5-hole MHPP design allows turbulence measurement in rain (sonic anemometers struggle in precipitation)

## Notable Details

### Historical Context
- Dropsondes have been deployed in TCs since late 1940s; GPS technology incorporated since 1997
- Dropsonde data cited in over 400 peer-reviewed manuscripts (Aberson et al. 2023)
- Previous Coyote operations (2014–2018) demonstrated ~100x more thermodynamic observations than dropsondes in lower 2 km (Figure 1b), but aircraft is no longer manufactured

### Operational Constraints & Solutions
- **Bandwidth limitation (addressed as ongoing effort):** Current sUAS-to-P-3 data transmission limited to ~3.5 Hz (down from MHPP's native 100 Hz capability); full 100 Hz data obtainable in recoverable operations
- **GPS altitude drift:** Radar altimeter upgrade (2025) addresses GPS accuracy issues below 50m, especially critical for low-altitude sampling in high sea states
- **Range limitations:** S0's 160+ nmi communication range "essentially allows for any type of flight pattern on an operational mission," vs. prior systems' constraints

### Competitive Positioning
- **Only TC-deployed MHPP:** S0 is unique in deploying turbulence-capable multi-hole pressure probe
- **Waterproof 5-hole probe uniqueness:** Team states it is "not aware of any other waterproof 5 hole probe that has SWAP low enough for small UAS"
- **Data density advantage:** At comparable kinematic observation levels to P-3 TDR, S0 provides ~100x more thermodynamic observations (supporting Figure 1b)

### Institutional Partners
- ERAU (Embry-Riddle Aeronautical University)
- UM (University of Miami)
- BST (Black Swift