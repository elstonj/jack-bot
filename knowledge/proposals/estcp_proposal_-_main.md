# Advanced UAS-Based Fuel Moisture Mapping for Wildfire Risk Mitigation and Prescribed Fire Management on DoD Lands

## Document Metadata
- **Type:** ESTCP Pre-Proposal (Environmental Security Technology Certification Program)
- **Client/Agency:** U.S. Department of Defense (DoD) / Environmental Security Technology Certification Program
- **Program/Solicitation:** ESTCP Natural Hazards Adaptation Program; Topic Area: Advancing Wildfire and Prescribed Fire Forecasting and Assessment Tools
- **Proposal Number:** NH26-A1-9078
- **Date:** Submitted 2024–2025 period (document modified through March 2025)
- **BST Products/Systems Referenced:** UAS-mounted dual polarized L-band radiometer (Lobe Differencing Correlation Radiometer / LDCR); multi-UAS coordination capability; onboard real-time data processing
- **Key Personnel:** 
  - Dr. Jack Elston (Black Swift Technologies, Lead PI/CEO)
  - Dr. Michelle Stern (USGS California Water Science Center)
  - Dr. Seungbum Kim (UCLA/Jet Propulsion Lab)
  - Eryan Dai (Weather Stream; instrument lead for L-band radiometer)
  - Ryan Ferrell (Pepperwood Foundation)

---

## Executive Summary

Black Swift Technologies proposes to develop and demonstrate an operationalized UAS-based fuel moisture mapping system that provides near real-time, high-resolution soil and live fuel moisture (LFM) maps to support DoD wildfire risk assessment and prescribed burn planning. By integrating UAS L-band radiometer data with satellite-derived soil moisture from NISAR and USGS Basin Characterization Model forecasting, the system will bridge the gap between coarse-resolution satellite products and labor-intensive ground sampling, enabling DoD installations to transition from reactive fire suppression to proactive risk mitigation over a 1–10 year planning horizon. The two-year demonstration will include four flight campaigns, hardware refinements, forecasting software development, and validation at DoD installations and non-DoD test sites (Pepperwood Preserve, CA).

---

## Technical Approach

### Core Technology
- **Sensor Platform:** UAS-mounted dual-polarized L-band radiometer (LDCR) developed in partnership with NASA
- **Resolution:** Sub-5m soil moisture mapping (vs. 250m–1km satellite products)
- **Data Products:**
  - Real-time soil moisture maps (target accuracy: ±6% RMS)
  - Live fuel moisture maps (target accuracy: ±10% RMS)
  - Wildfire risk forecasts integrated with climate scenarios
  
### Integration Strategy
1. **Satellite Layer:** NISAR soil moisture data at 100–200m resolution, collected regularly throughout the year
2. **UAS Layer:** High-resolution data collection several times per year (especially near prescribed burn dates) to validate and refine satellite products
3. **Modeling Layer:** USGS Basin Characterization Model (BCM)—a gridded water balance model—ingests UAS and satellite data to generate soil moisture–LFM relationships and forecast wildfire risk
4. **Climate Scenarios:** Downscaled CMIP5 Global Climate Model outputs run through BCM to provide ensemble-based fire danger estimates for 1–10 year periods

### Key Technical Objectives (Year 1–2)
- Operationalize forecasting tools for wildfire exposure and prescribed burn window assessment
- Develop forecasting software that ingests UAS data and NISAR satellite inputs
- Enable multi-UAS coordination for enhanced spatial coverage
- Demonstrate utility in real-world DoD wildfire-prone environments
- Fuse UAS-collected data with NISAR-derived soil moisture at multiple spatial and temporal scales

### Performance Metrics & Success Criteria

| Performance Objective | Metric | Data Requirements | Success Criteria |
|---|---|---|---|
| **Quantitative** | | | |
| Remote sensing vs. ground truth | Soil moisture ±6% RMS; LFM ±10% RMS | NISAR data, UAS data, ground data | Accuracies meet defined thresholds |
| Historical forecast accuracy | Modeled soil/fuel moisture within ±6%/±10% RMS | Historical soil and live moisture data; fire susceptibility maps | Historical performance meets thresholds |
| **Qualitative** | | | |
| Realistic spatial/temporal variations | Soil/LFM maps with realistic variability at 1–10 year scales | NISAR, UAS, ground data | Visual variations appear realistic for forecast periods |
| Wildfire risk forecast | Reasonable risk estimates for locations with historical wildfires (1–10 year timeframe) | Model data, sensor data | High-risk locations coincide with historical wildfire occurrence |

---

## Products & Capabilities Described

### 1. L-Band Radiometer (LDCR) on UAS
- **What It Is:** Dual-polarized microwave radiometer mounted on small UAS; developed with NASA in partnership with Orbital Micro Systems
- **Specifications:**
  - L-band frequency (inherently penetrates vegetation/soil to measure root-zone moisture)
  - Lobe differencing correlation radiometer design for spatial resolution enhancement
  - Onboard FPGA-based real-time data processing
  - Proven heritage from SMAP and airborne campaigns
- **Validation Data:** Field experiments at BST test site (April 2023) and Pepperwood Preserve (2021–2023) show good agreement with in-situ soil moisture probes across three seasonal campaigns; over 900 mobile TDR measurements collected for validation
- **Prior Demonstrations:** Over 100 soil moisture missions flown for NASA, NOAA, USGS, and commercial customers

### 2. Multi-UAS Coordination Capability
- **What It Is:** Enhanced capability for coordinating multiple UAS to achieve broader spatial coverage
- **Proposed Use:** Enable simultaneous or sequential flights to map larger installation areas efficiently
- **Status:** Capability referenced but not extensively detailed in proposal

### 3. Basin Characterization Model (BCM) Integration
- **What It Is:** USGS-developed gridded water balance model that converts soil moisture and LFM data into wildfire risk maps and climate-scenario forecasts
- **How Used:** Ingests UAS high-resolution data and NISAR satellite products to create empirical soil moisture–LFM relationships; runs through downscaled climate models (CMIP5) to forecast fire danger over 1–10 year periods
- **Previous Validation:** BCM previously validated on 3,200-acre Sonoma County preserve with historical wildfire data

### 4. Real-Time Data Processing
- **Onboard Computing:** UAS equipped with onboard computing for real-time radiometer data processing, reducing post-flight processing requirements and enabling rapid decision support

---

## Use Cases & Applications

### Primary DoD Applications
1. **Prescribed Burn Planning:** Optimize burn windows by identifying periods when soil and live fuel moisture are within acceptable ranges for controlled burns
2. **Wildfire Risk Mitigation:** Identify high-risk areas on installations (Army, Air Force, Navy/Marine Corps lands) to preposition resources and deactivate power lines during critical fire weather windows
3. **Long-Term Fuel Management Prioritization:** Build regional models over recurrent operational flights to identify chronic low-moisture areas requiring fuels management and forest stewardship treatment
4. **Mission-Critical Land Use Sustainability:** Maintain training area availability and infrastructure protection

### Test Sites & Target Installations
- **Pepperwood Preserve, Sonoma County, CA:** 3,200-acre nature preserve with 40 active climate/soil stations, 170 soil sensors, extensive fuel and vegetation monitoring; used for validation and baseline flights
- **DoD Installations:** Proposed deployment on Army (ITAM sites), Air Force, Navy/Marine Corps lands; specific installations to be identified during execution
- **Secondary Use Case (Related):** Air Force SBIR parallel effort uses same radiometer for runway soil integrity assessment for C-130 operations

---

## Key Technical Risks & Mitigation

| Risk | Description | Mitigation |
|---|---|---|
| **Risk 1: Forecasting Accuracy** | Cannot retroactively validate against historical wildfires (remote sensing data did not exist) | Validate soil/LFM maps against historical data; simulate historical wildfires using modeled soil moisture conditions; expand validation to multiple regions |
| **Risk 2: Flight Permissions on DoD Bases** | FAA Beyond Visual Line of Sight (BVLOS) regulations restrict long-range UAS operations; requires site-specific waivers | L-band radiometer UAS already approved by AFWERX under separate Phase II SBIR; fallback to Pepperwood test site if base access delayed |
| **Implicit: Cybersecurity/OPSEC** | DoD data must meet encryption and security standards | Develop procedures for encrypted data transfer; ensure compliance with DoD operational security protocols (noted in transition section) |

---

## Technology Maturity

**Technology Readiness Level (TRL):** 7 (validated in relevant environment; requires refinement for operational status)

### Evidence of Maturity
- **Sensor Heritage:** L-band radiometry proven over 10+ years through SMAP satellite and airborne campaigns
- **Field Validation:** Over 100 BST-operated soil moisture missions; dedicated validation campaigns at Pepperwood (2021–2023) with 900+ TDR measurements
- **Published Results:** Peer-reviewed publications demonstrate soil–LFM correlation and high-resolution mapping capability (Stern et al. 2024, Dai et al. 2020)
- **Parallel Government Funding:** Air Force SBIR Phase II approval validates system operability

### Development Work Required
- Integration of all components into single operationalized system for DoD use
- Development of forecasting software to ingest UAS data into BCM
- Refinement of L-band radiometer hardware for improved performance
- Validation across multiple DoD installations and climate regions
- Development of DoD-compliant data handling and transition workflows

---

## Related Efforts & Partnerships

| Project | Funding Source | Relevance |
|---|---|---|
| **Air Force SBIR – Runway Integrity from Soil Moisture** | AFWERX | Uses same L-band radiometer technology; validates system operability on military bases; parallel funding demonstrates government confidence |
| **Pepperwood Deployments (2021–2023)** | USGS | Multi-season UAS flights validating soil–LFM correlation; established strong baseline for wildfire risk assessment |
| **NASA Partnership** | NASA (historical) | Co-developed L-band radiometer; heritage from Earth science missions |
| **SMAP Satellite Program** | NASA | Technology foundation for current L-band radiometry approach |

---

## Expected DoD Benefits

### Cost & Operational Impact
- **Reduced Suppression Costs:** High-resolution fuel moisture maps enable targeted prescribed burns, reducing catastrophic wildfire risk
- **Operational Efficiency:** On-demand UAS flights replace infrequent satellite overpasses and labor-intensive ground sampling; enables rapid decision-making for prescribed burn windows
- **Personnel Safety:** Proactive wildfire mitigation reduces uncontrolled fire risks threatening personnel, training areas, and infrastructure
- **Training Area Availability:** Optimized fuel management sustains mission-critical land use activities

### Financial Projections
- **Projected ROI:** Under 2 years at single installation
- **Scalability:** System easily deployed across multiple wildfire-prone DoD installations for significant aggregate annual savings
- **Asset Protection:** Potential savings equivalent to replacement cost of high-value installation assets (quantified on per-base basis)

### Aggregate DoD Impact
- **Deployment Timeline:** 5–10 pilot installations within 24 months post-demonstration; broader DoD-wide rollout based on mission needs
- **Long-Term Vision:** Transition from reactive fire suppression to proactive risk assessment across DoD wildfire-prone lands

---

## Notable Technical Details

### Live Fuel Moisture Validation
- **Pepperwood Results:** Strong empirical correlations between soil moisture and LFM measured for multiple species (chamise as indicator species)
- **Figure References:** Proposal includes soil moisture maps (Figure 2) showing agreement between modeled UAS products and field TDR measurements; LFM maps (Figure 4) derived from soil moisture anomalies
- **Spatial Sampling:** Over 900 mobile TDR measurements across three seasonal campaigns to characterize spatial variability

### Satellite Integration
- **NISAR:** 100–200m resolution soil moisture; regular collection throughout year; chosen over SMAP (which has 25km or 1–3km resolution with 14-day revisit) for superior spatial resolution
- **Climate Scenarios:** Downscaled CMIP5 models run through BCM to