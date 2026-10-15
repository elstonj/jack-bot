# High-Resolution UAS Soil Moisture Mapping for NOAA Snow Survey and Water Prediction

## Document Metadata
- **Type:** Proposal / Capability Brief
- **Client/Agency:** NOAA Office of Marine and Aviation Operations (OMAO) / Uncrewed Systems Operations Center; NOAA National Weather Service / Office of Water Prediction (OWP)
- **Program/Solicitation:** Not specified (can be ordered under existing NOAA IDIQ vehicle 1305M226D0012); derives from NASA SBIR awards and Air Force SBIR Phase II contract FA8649-24-P-0003
- **Date:** October 7, 2026
- **BST Products/Systems Referenced:** S2 (fixed-wing), S3 (VTOL fixed-wing), E2 (multirotor), LDCR (Lobe Differencing Correlation Radiometer) RevD, SwiftCore, SwiftTab, SwiftPilot
- **Key Personnel:** Not explicitly named; document references Weather Stream as partner on Air Force effort

## Executive Summary
Black Swift Technologies proposes a 12-month pilot to establish how UAS-based L-band radiometry can complement NOAA's crewed Airborne Gamma Radiation Snow Survey Program. Rather than replacing the gamma survey, the UAS system would map NOAA-selected soil moisture flight lines, converting single line-average measurements into thousands of gridded observations per line (15–100 m resolution) while reducing crew exposure to low-altitude flight. The solution integrates BST's proven LDCR radiometer payload (developed under NASA SBIR funding and previously flown for NOAA during SPLASH, USGS, USDA, and Air Force) onto the S3 VTOL fixed-wing aircraft for repeatable, high-resolution soil moisture maps before snowfall and after storms.

## Technical Approach

### Core System Architecture
- **Primary Aircraft:** S3 VTOL fixed-wing UAS (vertical launch/recovery; up to 110 minutes flight time; 110 km range)
- **Reference Aircraft:** E2 multirotor (higher-resolution maps; terrain-following capability where fixed-wing recovery impractical)
- **Instrument:** LDCR RevD passive L-band radiometer operating at 1.41 GHz (protected L-band allocation, same as SMAP/SMOS)
  - Downward antenna measures soil/vegetation emission
  - Upward antenna provides cold-sky reference
  - Two-path correlating receiver with digital back end for RFI detection/mitigation
  - Co-registered vegetation index and surface temperature sensors
  - Radiative transfer retrieval compatible with SMAP products
  - Linear minimum mean square error estimator maps volumetric soil moisture onto grids finer than instantaneous antenna footprint
  - Antenna footprint approximately equal to flight altitude (resolution selected by altitude)
  - Brightness temperature displayed to operator in-flight for real-time fault detection

### Flight Operations
- Operator loads line geometry into SwiftTab, which generates terrain-following pattern at agreed resolution
- Vertical launch from road pull-off or field near flight line
- Transitions to wing-borne flight, maps assigned segment, returns for battery exchange
- Radiometer, vegetation, and thermal sensors record continuously with time, position, attitude
- Multi-sortie coverage tracking implemented in SwiftTab for lines exceeding single sortie capacity

### Resolution and Coverage Trade
- At 30 m AGL: resolves individual drainages
- At ~100 m AGL: native footprint near 100 m; single S3 sortie could cover most/all of 10-mile line (~several hundred cells vs. one gamma value)
- At 15 m AGL: full line contains >20,000 cells; requires multiple sorties
- Achievable envelope with LDCR payload to be measured during integration (Task 3)

### Data Products and Reconciliation
- Volumetric soil moisture at gridded resolution
- Vegetation index and surface temperature
- Gamma-compatible line average computed from map with stated uncertainty
- Quality flags
- Same-day delivery from field
- Documented method for depth/unit/scale reconciliation (volumetric vs. gravimetric; ~5 cm sensing depth vs. 10–20 cm gamma weighting)
- Co-located multi-depth sampling to characterize differences

### Operational Constraints (Explicitly Stated)
- L-band retrieval valid for snow-free, unfrozen ground only
- Fall baseline, pre-snow updates, post-melt surveys, warm-season events in scope
- Dense forest canopy reduces sensitivity; will be characterized, not excluded
- Full 10-mile line in one deployment requires BVLOS operation or crew relocation (base demonstration can work under visual observer or segmented operations)
- Flight bounded by geofences, altitude limits, energy reserves, weather limits, lost-link behavior; operator retains launch/recovery authority

## Products & Capabilities Described

### LDCR (Lobe Differencing Correlation Radiometer) RevD
- **What it is:** Passive microwave radiometer for L-band soil moisture sensing; non-transmitting
- **Heritage:** Developed with University of Colorado Boulder Center for Environmental Technology (2015 original); RevC2 integrated receiver on single shielded board; RevD produced with Weather Stream under Air Force SBIR Phase II (Nov 2023–July 2025)
- **Improvements in RevD:** Enhanced radiometric stability; calibration sources that do not depend on thermal gradient
- **Prior validation:** NASA Beltsville study (USDA ARS) reported unbiased RMSE 0.028 m³/m³ for spatial mean; dry bias 0.107 m³/m³ with RevC2 (recommended stronger calibration, now addressed in RevD)
- **USGS California testing:** 13 km² at 3–50 m resolution; average unbiased RMSE 0.07 m³/m³, bias 0.021 m³/m³; successful retrievals beneath moderately dense tree canopy
- **Air Force testing:** Cluster-averaged soil moisture correlation 0.90 across clay loam, silt loam, loam, sandy loam soils; runway evaluation in <30 minutes

### S3 Aircraft
- **What it is:** VTOL fixed-wing UAS (proposed for line-scale mapping)
- **Capabilities:** Up to 110 minutes endurance; 110 km range; no runway/launcher required
- **Use case here:** Primary platform for NOAA line-scale soil moisture mapping demonstration
- **Performance:** Achievable soil moisture mapping envelope (coverage rate, resolution, endurance with LDCR payload) to be established in Task 3; not implied by S2 heritage figures

### S2 Aircraft
- **What it is:** Fixed-wing UAS (heritage platform)
- **Capabilities:** ~1 km²/flight hour at 15 m resolution; ~2 km²/flight hour at 30 m resolution
- **Historical use:** Original NASA-funded soil moisture system; SPLASH deployments; Air Force P-band SWE testing in mountain terrain

### E2 Multirotor
- **What it is:** Multirotor UAS (validated reference configuration)
- **Use case:** Provides highest-resolution soil moisture maps; terrain-following at low altitude where fixed-wing recovery impractical (e.g., hilly terrain during SPLASH)
- **Role in proposal:** Serves as validation reference during S3 integration verification

### SwiftCore Flight Management System
- **What it is:** BST-developed flight management software/autonomy
- **Use in proposal:** Powers terrain-following operations and real-time telemetry

### SwiftTab, SwiftPilot, Operator Interface
- **Functions:** Line-geometry import, terrain-following pattern generation, multi-sortie coverage tracking, real-time brightness-temperature display, automated same-day processing

## Use Cases & Applications

### Primary: NOAA Fall Soil Moisture Baseline Survey
- Current bottleneck: Each ~10-mile flight line measured once (typically October/November) with single line-average value; baseline assumed constant through winter
- Problem addressed: Rain and early melt after fall survey change soil moisture and introduce bias into gamma SWE calculations; satellite updates help in open terrain but not forests
- **UAS solution:** Revisit lines on short notice immediately before snow onset; high-resolution maps (hundreds to thousands of cells per line) capture spatial heterogeneity and enable pre-snow baseline updates

### Secondary: Post-Storm and Seasonal Revisits
- Map lines after precipitation events to capture transient moisture changes
- Support post-melt and warm-season water supply forecasts

### Tertiary: Forested Terrain (Option consideration)
- USGS Sonoma County results show LDCR performs well under moderately dense canopy—terrain where satellite soil moisture corrections to gamma are least effective
- UAS fills gap in forested mountain watersheds where satellite resolution and signal penetration are insufficient

### Quaternary (Option 3): Snow Water Equivalent Assessment
- Not primary scope; limited evaluation proposed
- Candidate approaches: P-band signals-of-opportunity technique previously flown on S2; comparison with gamma SWE accuracy, snow depth range, payload, operating envelope

## Key Results (Prior Work Documented)

### SPLASH Campaign (2021–2023, East River, Colorado)
- **Flights:** 64 UAS soil moisture missions across 7 deployments (1–3 days each); S2 fixed-wing initially, transitioned to E2 multirotor
- **Improvements:** Replaced radiometer noise source; corrected voltage regulator noise; reduced measurement noise ~5×; cut processing time from >1 month to days
- **Validation:** Two-day controlled test vs. ~200 in situ probes per flight; UAS and ground maps showed same spatial structure; day-to-day change agreed mostly within ±3%
- **Final deployments:** September–October 2023, all six flight areas mapped twice in 24 flights
- **Deliverable:** Level 3 products on ~50 cm common grid archived at NOAA NCEI (Accession 0301536); co-located NOAA probe data (Accession 0302136)
- **Use by NOAA PSL:** Used SPLASH soil observations to evaluate soil moisture in HRRR model
- **Example result (Figure 1):** Area-mean volumetric soil moisture fell from 14.0% (5 Sept 2023) to 11.5% (17 Oct 2023); within-area range 5th–95th percentile ~5–30%; mapped area 0.10 km² (gamma line reports one value for area ~50× larger)

### USGS Sonoma County, California (4 campaigns)
- **Area:** 13 km² mixed oak woodland/grassland at 3–50 m resolution
- **Accuracy:** Average unbiased RMSE 0.07 m³/m³; bias 0.021 m³/m³ against in situ measurements
- **Canopy performance:** E2 retrievals beneath moderately dense tree canopy agreed well with ground sampling
- **Relevance to NOAA:** Forested terrain is where satellite baseline updates are least effective

### Air Force SBIR Phase II (FA8649-24-P-0003, Nov 2023–July 2025)
- **Title:** Runway Integrity Validation through Soil Moisture Measurements from Small UAS
- **Partner:** Weather Stream
- **Deliverables:** RevD radiometer; lightweight vegetation/thermal sensors integrated on single aircraft; real-time brightness-temperature telemetry; automated same-day processing
- **Testing:** Clay loam, silt loam, loam, sandy loam soils; agricultural, grassland, mountain sites
- **Results:** Cluster-averaged soil moisture correlated 0.90 with in situ; runway evaluation in <30 minutes
- **Airworthiness:** Air Force flight test, safety, airworthiness review completed

### Commercial/Other Users
- **USDA:** Purchased and operates BST soil moisture UAS for agricultural research
- **University of Colorado:** Flown S2 payload in Alaska and Yuma, Colorado (Irrigation Research Foundation)
- **RES (solar developer):** 2025 evaluation of soil moisture/soil strength mapping for construction trafficability at four test sites

### NASA Validation
- **Beltsville Agricultural Research Center (USDA ARS, NASA Terrestrial Hydrology Program):** Week-long dry-down study; unbiased RMSE 0.028 m³/m³ for spatial mean; identified need for robust internal calibration (addressed in RevD)
- **North Texas/Oklahoma:** Soil moisture in region affected by severe flooding

## Proposed Scope & Deliverables

### Base Tasking (12 months