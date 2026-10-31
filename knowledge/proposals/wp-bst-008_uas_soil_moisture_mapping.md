# High-Resolution UAS Soil Moisture Mapping for NOAA Snow Survey and Water Prediction

## Document Metadata
- **Type:** Technical proposal / white paper
- **Client/Agency:** NOAA Office of Marine and Aviation Operations (OMAO) / Uncrewed Systems Operations Center; NOAA National Weather Service / Office of Water Prediction (OWP)
- **Program/Solicitation:** Potential NOAA IDIQ vehicle (1305M226D0012); leverages NASA SBIR and Air Force SBIR Phase II heritage (FA8649-24-P-0003)
- **Date:** October 7, 2026 (prepared); October 8–30, 2026 (last modified)
- **BST Products/Systems Referenced:** 
  - S3 VTOL fixed-wing aircraft (primary proposed platform)
  - S2 fixed-wing aircraft (fielded reference system)
  - E2 multirotor (validated reference configuration)
  - LDCR RevD radiometer (Lobe Differencing Correlation Radiometer, Revision D)
  - SwiftCore (flight management system)
  - SwiftTab (flight planning software)
  - SwiftPilot™ and related ground-station software
- **Key Personnel:** Jack Elston (last editor); Carrie Olheiser (OWP program lead, cited); collaboration with Weather Stream on RevD radiometer development

---

## Executive Summary

Black Swift Technologies proposes a 12-month pilot program to evaluate how UAS-based passive L-band radiometry can complement NOAA's operationally flown Airborne Gamma Radiation Snow Survey Program. Rather than attempting to carry the heavy RSX-5 gamma detector on a large uncrewed aircraft, BST offers to map NOAA-selected soil moisture flight lines using the lightweight, NASA-developed LDCR (Lobe Differencing Correlation Radiometer) on small Group 2 UAS platforms (S3 VTOL fixed-wing and E2 multirotor). The pilot would deliver gridded soil moisture maps at 15–100 m resolution containing hundreds to thousands of observations per line—versus a single line-average value from crewed gamma flights—while removing the need for crews to fly low over hazardous, high-altitude terrain during snow-free periods. The base effort ($0.95M) includes retrospective comparison against archived SPLASH data, S3 payload integration, co-flown demonstration on up to three NOAA-selected lines, and delivery of two operational S3 systems. Options add regional fall-baseline campaigns, additional systems with NOAA operator transition, and snow water equivalent sensing assessment.

---

## Technical Approach

### Measurement Principle
- **L-band radiometry:** Passive microwave emission measurement near 1.41 GHz (same protected band as SMAP and SMOS satellites)
- **Sensing depth:** Approximately top 5 cm (varies with soil wetness), versus gamma's top 20 cm
- **Output:** Volumetric soil moisture; co-registered vegetation index and surface temperature collected on same flight
- **Instrument:** LDCR RevD radiometer with downward antenna, two-path correlating receiver, digital back end, on-board calibration sources (cold-sky reference and internal calibration), and RFI mitigation
- **Retrieval method:** Brightness temperature combined with surface temperature, vegetation index, terrain, and soil texture using radiative transfer model and linear minimum mean square error estimator; gridding to footprint finer than instantaneous antenna footprint

### Aircraft & Payload Integration
- **Primary platform:** S3 VTOL fixed-wing aircraft (proposed for integration under this effort)
- **Reference platform:** E2 multirotor (fielded; highest-resolution maps, validated)
- **Payload mass:** LDCR and sensors fit within E2's 4.5 lb payload limit
- **Flight envelope:**
  - Altitude: 30–120 m AGL with terrain following
  - Speed: Variable (to be determined during integration)
  - S3 endurance: Up to 110 minutes; 110 km range
  - S3 coverage: Planning estimate—one sortie could cover most or all of a 10-mile line at ~100 m altitude, providing several hundred map cells
- **Flight management:** SwiftCore autonomy; SwiftTab terrain-following pattern generation from line geometry
- **Telemetry:** Real-time brightness temperature display to operator; in-flight sensor-health verification

### Operational Workflow
1. OWP nominates candidate flight lines and provides calibration history
2. Operator loads line geometry into SwiftTab; system generates terrain-following pattern at agreed resolution
3. Aircraft launches vertically from road pull-off or field near line
4. Transitions to wing-borne flight, maps assigned segment, returns for battery exchange
5. Processing delivers gridded volumetric soil moisture, vegetation index, surface temperature, gamma-compatible line average with uncertainty, and quality flags (same-day delivery targeted)
6. Data compared with co-flown gamma measurements (where practical), in situ probes at multiple depths, and reference data

### Depth & Unit Reconciliation
- Gamma yields gravimetric soil moisture (% by weight) weighted to upper 10–20 cm
- LDCR yields volumetric soil moisture (m³/m³) at ~5 cm depth (varies with wetness)
- Pilot includes co-located multi-depth sampling and documented method for producing gamma-compatible line average with stated uncertainty
- Success criteria: agreement with gamma line average and in situ sampling within OWP-defined thresholds (to be established in Task 1)

### Operational Constraints & Scope
- **Valid conditions:** Snow-free, unfrozen ground only (fall baseline, pre-snow updates, post-melt surveys, warm-season events)
- **Not covered:** Snow water equivalent surveys over snowpack remain crewed gamma mission
- **Range:** Targets snow-free soil moisture lines on most hazardous/difficult-to-fly terrain—high-altitude, rugged-mountain lines and those with poor historical acquisition
- **Authorization:** Base demonstration can proceed under visual-observer or segmented operations; routine line-scale flights would require beyond-visual-line-of-sight (BVLOS) authorization (documented transition path included)
- **Constraints:** Geofenced, altitude-limited, weather-gated, with lost-link behavior and operator launch/recovery authority
- **Vegetation:** Dense forest canopy reduces sensitivity and will be characterized rather than excluded

---

## Products & Capabilities Described

### LDCR RevD Radiometer
- **What it is:** Passive L-band (1.41 GHz) microwave radiometer designed for soil moisture mapping; developed under NASA SBIR and matured through NOAA, USGS, USDA, and Air Force use
- **Heritage:** Original version designed 2015 with University of Colorado Boulder; RevC2 integrated receiver on single shielded board; RevD (Air Force SBIR Phase II, Nov 2023–Jul 2025) improved radiometric stability, moved all sensors onto one aircraft, added internal calibration sources independent of thermal gradient
- **Performance:**
  - Unbiased RMSE: 0.03–0.07 m³/m³ against in situ (varies by study)
  - Agreement with gamma line average: to be measured in pilot
  - Real-time telemetry capability; processing time reduced to days/hours
  - No prior background survey required (cold-sky and internal calibration)
- **Advantages over gamma RSX-5:**
  - Mass: ~4.5 lb payload (vs. 250–350 lb detector)
  - Aircraft class: Group 2 UAS (vs. MQ-1C Gray Eagle equivalent for gamma)
  - Resolution: Gridded map at 15–100 m cells (vs. one line average)
  - Revisit capability: Can collect before snowfall, after storms, multiple times per season
  - No crew at low altitude
- **Payload:** Radiometer + vegetation sensor (replaced multispectral camera in RevD) + thermal sensor, all on one airframe

### S3 VTOL Fixed-Wing Aircraft
- **What it is:** Vertical-takeoff-and-landing fixed-wing platform proposed for soil moisture line-scale mapping
- **Proposed use:** Endurance for mapping full NOAA flight lines without runway or launcher; terrain-following at 30–120 m AGL
- **Specifications:**
  - Flight time: Up to 110 minutes
  - Range: 110 km
  - Payload: LDCR RevD radiometer system (performance envelope to be measured in Task 3)
  - Launch/recovery: Vertical from road pull-off or field
  - Flight management: SwiftCore autonomy
- **Integration status:** Not yet integrated with LDCR under this proposal; Task 3 addresses mass properties, antenna placement, EMC, thermal behavior, vibration, endurance effects
- **Deliverable:** Two S3 aircraft configured for soil moisture mapping, with Government title proposed at project completion

### E2 Multirotor
- **What it is:** Fielded, operationally proven multirotor platform
- **Use in pilot:** Highest-resolution reference maps; validation baseline for S3 integration
- **Capabilities:** Highest-resolution maps, proven in SPLASH and USGS campaigns, within 4.5 lb payload budget
- **Advantages:** Low altitude recovery practical over hilly terrain where fixed-wing recovery infeasible

### S2 Fixed-Wing Aircraft
- **What it is:** Heritage fixed-wing platform (flight-proven through NASA and SPLASH campaigns)
- **Historical performance:** ~1 km²/hour at 15 m resolution, ~2 km²/hour at 30 m resolution (S3 performance not implied by S2 figures)
- **Use in pilot:** Referenced for historical context and heritage; not primary platform for this effort

### SwiftCore Flight Management System
- **What it is:** Autonomous flight management system (fielded across BST aircraft)
- **Use:** Terrain-following autonomy on S3 for soil moisture mapping

### SwiftTab Flight Planning Software
- **What it is:** Mission planning and data-management tool
- **Proposed enhancements (Task 4):**
  - Flight-line import from NOAA geometry
  - Terrain-following pattern generation
  - Multi-sortie coverage tracking
  - Processing output: gridded volumetric soil moisture, vegetation index, surface temperature, gamma-compatible line average with uncertainty, quality flags
  - Format: OWP-agreed data product and exchange format
  - Latency: Same-day delivery from field

---

## Use Cases & Applications

### Primary Use Case: NOAA Airborne Gamma Radiation Snow Survey Program Support
**Context:** NOAA's Office of Water Prediction maintains 2,400+ flight lines across northern U.S., Alaska, and southern Canada for soil moisture and snow water equivalent measurement. Lines range 1–40+ miles; flown at ~500 ft AGL, ~145 knots, in visual conditions by crewed King Air/Twin Otter. Each line yields one line-average value. Baseline flown once in fall and assumed constant through winter.

**Proposed UAS role:**
- **Snow-free soil moisture surveys** on highest-hazard, hardest-to-acquire lines (high-altitude, rugged-terrain lines)
- **Fall baseline mapping:** Detailed soil moisture map instead of single value; option for pre-snow update immediately before onset
- **Post-melt surveys:** Repeatable observations after melt events
- **Warm-season events:** On-demand revisits not practical with crewed flight
- **Data input:** Soil moisture at tens-of-meters resolution (drainages, hillslopes, vegetation boundaries, burn scars) to inform flood outlooks, water supply forecasts, drought/fire-weather assessment

**Operational fit:** Crewed aircraft retain longer, easier lines and full snow water equivalent missions (requiring gamma over snowpack). UAS removes riskiest low-level terrain flights from crewed schedule.

### Secondary Use Cases (Established from Prior Work)

**NOAA SPLASH Campaign (2021–2023):**
- Mapped East River watershed (Colorado) soil moisture in coordination with gamma flights and ground sampling
- 64 UAS flights across seven deployments
- Validated retrieval against ~200 in situ probes per flight; spatial structure agreement and day-to-day change agreement within ±3%
- Data archived at NOAA NCEI (public Level 3 products); used for HRRR model soil moisture evaluation

**USGS Pepperwood Preserve (Sonoma County, CA):**
- Four campaigns mapping 13 km² mixed oak woodland and grassland at 3–50 m resolution
- Average unbiased RMSE 0.07 m³/m³, bias 0.021 m³/m³ against in situ
- Demonstrated retrieval capability under moderately dense tree canopy
- Supports wildfire and hydrologic research

**Air Force Runway Assessment (SBIR Phase II, Nov 2023–Jul 2025):**
- Adapted system for unimproved airfield evaluation (C-130 operations)
- Soil moisture and California Bearing Ratio maps within minutes of landing
- Real-time telemetry to operator tablet
- Tested on clay loam, silt loam, loam, sandy loam soils
- Cluster-averaged in situ and LDCR soil moisture correlation: 0.90

**USDA Agricultural Research:**
- USDA operates BST soil moisture UAS for agricultural research
- Demonstrates commercial/operational user demand

**Solar Project Site Assessment (2025):**
- Partnered with RES (utility-scale solar builder) for soil moisture and soil strength mapping
- Four test sites evaluated for construction trafficability

---

## Key Results (from Pilot Proposal & Historical Work)

### Validation Against Ground Truth
- **NASA SBIR/Terrestrial Hydrology Program (USDA Beltsville, 2024):**
  - Unbiased RMSE 0.028 m³/m³ for spatial mean during week-long dry-down after storm (RevC2, without in-flight calibration)
  - Dry bias 0.107 m³/m³; recommended more robust internal calibration (now implemented in RevD)

- **USGS Sonoma County (2024):**
  - Unbiased RMSE 0.07 m³/m³ across 13 km² mixed terrain
  - Bias 0.021 m³/m³
  - Successful under moderate tree canopy (relevant where satellite baselines fail)

- **NOAA SPLASH (2022–2023):**
  - 64 UAS flights, 7 deployments, zero incidents
  - Updated radiometer performance: reduced measurement noise by ~5×, cut processing time to days
  - Controlled two-day radiometer test: UAS and ground maps showed same spatial structure; day-to-day soil moisture change agreed within ±3%
  - Final two deployments: 6 flight areas mapped twice in 24 flights; Level 3 gridded products archived at NOAA NCEI

### Historical Accuracy Claims
- **Published baseline (gamma RSX-5):** Line-average RMSE ~2.5–4% soil moisture by weight (Jones and Carroll 1983; Carroll and Peck 1988; cited)
- **L-band UAS:** ubRMSE 0.03–0.07 m³/m³ against in situ; agreement with gamma line average to be measured in pilot (primary success criterion)

### Technical Maturation
- **14+ years development history:** Original LDCR designed 2015; RevC2 and RevD released
- **Multi-agency validation:** NASA, NOAA, USGS, USDA, Air Force
- **Radiometric improvements:** RevD calibration sources stable independent of thermal gradient; real-time telemetry; automated processing

---

## Notable Details

### Risk Reduction Strategy
- **Not a new instrument development:** LDCR and retrieval documented in peer-reviewed literature; flown on BST aircraft since 2015; no instrument development risk carried into pilot
- **Already NOAA-proven:** SPLASH co-location provides direct comparison dataset ready for retrospective analysis; same watershed, same science objective, data not yet systematically compared
- **Multi-agency pedigree:** NASA SBIR funding, operational use by USGS/USDA/Air Force reduces integration risk
- **Demonstrated operationalization:** Air Force Phase II completed July 2025 with fielded RevD, automated processing, real-time telemetry

### Comparison with Alternative Approaches
| Approach | Payload | Aircraft | Flight Profile | Product |
|----------|---------|----------|-----------------|---------|
| Gamma (NOAA baseline) | 250–350 lb RSX-5 | Crewed King Air/Twin Otter | ~500 ft AGL, 145 kt, visual, crewed crew low over terrain | One line-average value per line |
| UAS + Gamma (proposed BST alternative) | 4.5 lb LDCR | Group 2 UAS (E2, S3) | 30–120 m AGL terrain-following, no crew at low altitude | Gridded map (hundreds to thousands of cells) + line average |
| Large UAS + Gamma | ~250–350 lb RSX-5 on MQ-1C | Uncrewed large platform (~500 lb payload) | Runway/crew requirements; airspace burden | Same as crewed gamma (unchanged product) |

**BST's rationale:** Complements rather than replaces gamma; targets snow-free lines on most hazardous terrain; reduces crewed low-altitude exposure; no large-aircraft infrastructure overhead; leverages proven light-weight instrument.

### Measurement Complementarity & Limitations
- **Measurement geometry:**
  - Gamma: integrates over ~2 square miles → robust aerial mean but one value per line
  - L-band UAS: footprint ~flight altitude → resolution by altitude selection; gridded map possible
  
- **Sensing depth difference:**
  - Gamma: ~96% signal from top 20 cm (gravimetric, % by weight)
  - L-band: ~5 cm (volumetric, m³/m³; varies with wetness)
  - *Pilot mitigation:* Multi-depth co-located sampling, documented reconciliation method, stated uncertainty

- **Snow/freeze limitations:**
  - L-band valid snow-free, unfrozen ground only
  - *Scope:* Pilot excludes snow water equivalent; crewed gamma retains that mission

- **Vegetation:**
  - Dense canopy reduces L-band sensitivity
  - *Approach:* Characterize rather than exclude; USGS demonstrated capability under moderate canopy

### Data Archive & Accessibility
- **SPLASH Level 3 products:** Public at NOAA NCEI (Accession 0301536), gridded on common 50 cm grid
- **Co-located NOAA probe data:** Also public (Accession 0302136)
- **NOAA PSL use:** Observations assimilated into HRRR model soil moisture evaluation
- **Pilot deliverable:** Observations collected under resulting agreement to be delivered for NOAA use and archive

### Intellectual Property & Licensing
- **BST pre-existing IP:** Airframes (S2, S3, E2), SwiftCore, SwiftPilot™, SwiftTab™, ground-station software, soil moisture retrieval algorithms, processing software, autonomy functions, manufacturing know-how
- **Third-party:** Radiometer design elements, third-party sensors, their applicable licenses preserved
- **NASA/Air Force heritage:** Soil moisture system derives from NASA SBIR awards and Air Force SBIR Phase II (FA8649-24-P-0003); may support Phase III sole-source award under 15 U.S.C. § 638(r)
- **Government data rights:** To be negotiated in resulting agreement; observations collected for NOAA delivered for NOAA use and archive

### Proposed Procurement Path
- **Existing vehicle:** NOAA IDIQ contract 1305M226D0012
- **Sole-source authority:** Air Force SBIR Phase II contract FA8649-24-P-0003 supports Phase III sole-source award eligible
- **Implementation:** Base 12-month effort; options for additional campaigns, systems, and SWE assessment

### Cost Estimate (Rough Order of Magnitude)
| Scope | Duration | Scale | ROM |
|-------|----------|-------|-----|
| **Base** | 12 mo | 2 S3 systems, 2 payload sets, SPLASH comparison, up to 3 lines, 1 demo window | $0.95M |
| **Option 1** | 6 mo | Up to 10 flight lines, pre-snow repeat, data service | $0.40M |
| **Option 2** | 9 mo | 2 additional S3 systems, NOAA operator training, first-deployment support | $0.45M |
| **Option 3** | 9 mo | SWE sensing trade study and limited flight evaluation | $0.30M |
| **Maximum (all)** | — | Base + all options | $2.10M |

**Assumptions:** LDCR integrates on S3 without major airframe redesign; NOAA provides gamma data, calibration history, SPLASH reference; demo lines accessible by road in one region; one authorization cycle sufficient; crewed gamma flights Government-furnished where coordinated.

### Timeline & Gating
- **Period of performance:** Base 12 months ARO
- **Task sequence:** Baseline review → SPLASH retrospective + S3 integration (parallel) → line-scale software → co-flown demo → acceptance → delivery
- **Demo gate:** Must fall within fall soil moisture survey window; award timing determines season
- **Critical path:** Airspace/BVLOS authorization, crewed survey coordination, weather, snow onset, component lead times

### Success Criteria (to be defined in Task 1)
- Agreement with gamma line average within OWP-specified threshold
- Agreement with in situ multi-depth sampling within OWP threshold
- Demonstrated resolution and coverage at acceptable trade-off
- Repeatable calibration without prior background survey
- No crew required at low altitude
- Data product and exchange format accepted by OWP
- Authorization pathway for routine operations documented

### Unique Competitive Advantages Claimed
1. **Instrument heritage:** 14-year LDCR development with multi-agency validation (NASA, NOAA, USGS, USDA, Air Force)
2. **No development risk:** Instrument mature and proven; system integration only
3. **Direct NOAA experience:** SPLASH co-location data immediately available for retrospective comparison
4. **Payload efficiency:** 4.5 lb vs. 250–350 lb enables Group 2 UAS operation
5. **Operational maturity:** RevD radiometer, automated processing, real-time telemetry, same-day delivery demonstrated on Air Force Phase II
6. **Multi-depth validation:** Extensive ground sampling protocols and documentation of depth/unit reconciliation
7. **Risk-stratified approach:** Targets hazardous terrain where crewed flight most constrained; complements rather than competes with gamma program

---

## Document Quality & Completeness Notes

- **Substance:** Comprehensive technical proposal with detailed background, operational concept, risk reduction strategy, and integrated task plan
- **Specificity:** Extensive citations of prior work (SPLASH, USGS, Air Force SBIR, NASA awards); archive accession numbers provided; quantitative performance data (RMSE, bias, correlation coefficients)
- **Clarity:** Well-organized sections on technical approach, constraints, and success criteria; comparison tables aid readability
- **Deliverables:** Clear tables of data and hardware deliverables with due dates, quantities, and Government title considerations
- **Known gaps:** Document notes that detailed pricing and BOE (basis of estimate) are under development; detailed S3 integration performance envelope to be measured, not specified in advance (appropriate for preliminary proposal)
- **Proprietary marking:** Document marked BLACK SWIFT PROPRIETARY; caveats on IP and data rights are appropriately noted