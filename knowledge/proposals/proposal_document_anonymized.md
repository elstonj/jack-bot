# On-demand Wildfire Susceptibility from Fuel Moisture and Vegetative Index Maps

## Document Metadata
- **Type:** NASA ROSES proposal (Step 2 submission)
- **Client/Agency:** NASA Earth Science Division
- **Program/Solicitation:** ROSES 2023, Topic A.59 (NNH23ZDA001N-FIRET) - FireSense
- **Date:** Submitted 2024 (created 2024-03-29, modified 2024-08-21)
- **BST Products/Systems Referenced:** E2 UAS Flight Systems (multirotor and fixed-wing variants with L-band radiometer)
- **Key Personnel:** PI (UAS expert, project lead since 2013), Co-I #4 (multi-aircraft UAS design/operations expert), Co-I #3 (L-band radiometer design lead), Co-I #2 (microwave radiometry/radar specialist, NISAR algorithm lead), Co-I #1 (field sampling/wildfire community liaison), Co-I/Science PI (hydrologist, soil/live fuel moisture expert)

## Executive Summary
This proposal describes a three-year effort to develop an operational, on-demand wildfire decision support system based on real-time soil moisture and live fuel moisture mapping. The system will combine a swarm of up to 8 small UAS equipped with L-band radiometers (flown by a single operator) with NASA satellite data (UAVSAR in Year 1, NISAR in Years 2-3) to provide high-resolution (2m) soil moisture and live fuel moisture maps across 3,200+ acres in a single day. The system addresses a critical gap in wildfire management by providing near-real-time situational awareness for pre-fire activities like prescribed burns and rapid response to ignition sources.

## Technical Approach

### System Architecture
- **Multi-tiered coverage strategy:** High-resolution UAS data (2m resolution at 15m altitude via multirotor) covers priority areas identified by satellite data; satellite/airborne data (6m-200m resolution) provides wider area coverage to guide UAS tasking
- **UAS platform:** Up to 8 multirotor platforms (quadrotors) operated simultaneously by a single pilot from a ground station, enabled by:
  - Automated terrain-aware flight planning and autonomous terrain avoidance
  - Automated pre-flight checks and sensor initialization
  - Real-time onboard soil moisture computation via FPGA-based digital correlator
  - Multi-aircraft communications and coordinated re-planning capability

### Data Processing Pipeline
- **Onboard processing:** L-band brightness temperature computed in real-time on each UAS using new FPGA-based digital correlator with improved gain stability and self-calibration capability
- **Field-to-decision latency:** Soil moisture and live fuel moisture maps generated within 30 minutes of landing (by Year 3)
- **Data fusion approach:** UAS data cross-validated with P-band UAVSAR (Year 1) and L-band NISAR satellite data (Years 2-3); satellite data used to task UAS swarm to high-risk areas

### Sensor Technology
- **L-band radiometer:** Miniaturized soil moisture sensing package (1.5kg on multirotor, 2.2kg on fixed-wing), draws <50W
- **Auxiliary sensors:** NDVI and thermal imaging sensors for vegetation and surface characterization
- **New correlator design:** FPGA-based, enables real-time brightness temperature calculation, improved thermal stability for hot-day operations, new slope correction algorithm for steep terrain

### Soil Moisture to Live Fuel Moisture Conversion
- Strong empirical relationship demonstrated at test site between soil moisture anomaly and live fuel moisture (LFM) for multiple chaparral species
- Maps derived by applying calibrated soil moisture-LFM relationships to UAS soil moisture maps
- Validation against in situ tree moisture sensors and field LFM samples from oak and chaparral species

### Satellite Integration Strategy
- **P-band UAVSAR (Year 1):** Test utility of root-zone soil moisture data for fire management; retrieve soil moisture using lookup-table forward model with three axes (dielectric constant, surface roughness, vegetation water content)
- **NISAR (Years 2-3):** Operate with 6-day revisit (ascending + descending combined); extend L-band retrieval algorithm to P-band; compare against UAS and UAVSAR data for cross-platform validation
- **Intelligent tasking:** NISAR/UAVSAR data analyzed to identify information gaps and high-risk areas; this classification directs UAS swarm to maximize value of limited flight resources
- **Fire perimeter detection (Year 3):** Explore NISAR disturbance algorithm for detecting active/post-fire perimeters during controlled burns at test site

## Products & Capabilities Described

### E2 UAS Flight Systems
- **What it is:** Small multirotor (quadrotor) and fixed-wing platforms developed by BST, equipped with L-band radiometer for soil moisture mapping
- **Heritage:** Originally developed under competitive SBIR grant; commercialized and used operationally in 100+ flights across government agencies, universities, and commercial partners
- **Proposed use in this project:**
  - **Multirotor variant:** Primary platform for wildfire application; slower flight speed (3 m/s vs. 18 m/s for fixed-wing) enables longer integration time for more accurate radiometer measurements and measurements through sparse canopy; terrain-following capability at 15m altitude enables 5m resolution mapping on variable, mountainous terrain
  - **Fixed-wing variant:** Candidate for efficiency in large-area coverage (8x more efficient than multirotor), but found less suitable for steep terrain and low-altitude requirements at test site
- **Year 1 procurement:** 3 systems at $18,500 each ($55,500 total)
- **Year 2 procurement:** 2 systems at $18,500 each ($37,000 total)
- **Year 3 procurement:** 4 systems at $18,500 each ($74,000 total)
- **Mass/power specs:** Compliant with RFP requirements (1.5kg payload with <50W draw for multirotor version)

### L-Band Radiometer Instrument
- **What it is:** Microwave radiometer operating at L-band (~1.4 GHz) for measuring soil moisture via brightness temperature
- **Key improvements in this project:**
  - New FPGA-based digital correlator calculating coherence matrix
  - Improved immunity to gain fluctuation
  - Self- and real-time calibration capability
  - Slope correction algorithm for steep terrain (developed during pilot campaigns)
  - Expanded temperature envelope for hot-day operations (hardware/firmware improvements)
  - Thermal calibration technique updates
- **Performance demonstrated:** Over 900 mobile TDR measurements collected during 2021-2023 pilot campaigns for validation; strong agreement between UAS-derived soil moisture maps and in situ station data (Figure 9) including measurements through moderate forest canopy

### Multi-UAS Autonomy & Operations Capability
- **What it is:** Flight planning, communications, and control software enabling single-operator control of up to 8 coordinated UAS
- **Key components:**
  - Automated terrain-aware flight planning (avoids manual path planning for each mission)
  - Active terrain tracking and avoidance during flight
  - Automated pre-flight checks and sensor setup
  - Intelligent re-planning when a platform is removed (e.g., due to sensor failure)
  - Single ground station interface for monitoring/controlling 8 aircraft
- **Development approach:** Incremental capability growth (2 UAS in Year 1, 4 in Year 2, 8 in Year 3), with each step demonstrating FAA/NASA compliance before expansion
- **TRL progression:** Entry TRL 4 → Exit TRL 7 (operational demonstration)

### NISAR Soil Moisture Algorithm Implementation
- **What it is:** Existing retrieval algorithm (developed for SMAP SAR) adapted for NISAR L-band and extended to P-band UAVSAR
- **Technical approach:** Minimizes difference between modeled and observed dual-polarization radar backscatter (σ⁰) using lookup-table forward model with axes for dielectric constant, surface roughness, and vegetation water content
- **Outputs:** 200m resolution global soil moisture maps with 6-day revisit from NISAR
- **Validation:** Cross-compared against UAS high-resolution data and P-band UAVSAR; used to identify priority areas for UAS deployment
- **TRL status:** Entry TRL 7 (flight-qualified) → Exit TRL 8 (operational)

## Use Cases & Applications

### Primary Use Case: Pre-Fire Wildfire Management
- **Application:** On-demand, high-resolution soil moisture and live fuel moisture maps to support:
  - **Prescribed burn planning:** Real-time fuel moisture data informs burn boss decisions on timing and extent of controlled burns
  - **Ignition response:** Rapid (same-day) assessment of fire danger conditions following detected ignition sources
  - **Pre-fire situational awareness:** Land managers, first responders, and residents understand relative wildfire threat in their area
- **Geographic focus:** 3,200-acre heavily instrumented nature preserve (test site) in California; extensible to other fire-prone regions in western US
- **Integration requirement:** Data format must be compatible with existing fire management systems and decision-making workflows

### Test Site Characteristics
- Highly instrumented with 40+ active climate and soil monitoring stations (15-min to hourly data, 1m+ depth)
- Active fuel management program (mechanical thinning, prescribed burns) in coordination with state/local agencies
- Multi-disciplinary research site studying process-based hydrology, vegetation, and fire ecology
- Diverse vegetation: oak trees, chaparral species (e.g., Chamise), aspen forest
- Challenging terrain: mountainous with variable elevation, steep slopes; sparse to moderate tree canopy coverage

### Extended Applications (Year 3 demonstration)
- **Fire perimeter detection:** NISAR disturbance algorithm demonstration during and after controlled burns at test site (showing applicability beyond pre-fire stage)

## Key Results (from pilot study, 2021-2023)

### Soil Moisture Mapping Performance
- **Data collection:** Four separate government-sponsored field deployments at test site using earlier versions of E2 UAS
- **Validation dataset:** 900+ mobile TDR soil moisture measurements across campaigns (dry, intermediate, and wet soil conditions)
- **Accuracy improvement:** System underwent major iterative improvements between deployments:
  - Slope correction algorithm for steep terrain
  - Hardware thermal stability improvements (expanded operating temperature range for hot-day operations)
  - Updated thermal calibration technique
  - New multirotor platform design (slower flight speed for longer integration time)
- **Final campaign result (Figure 9):** Excellent correlation between UAS-derived soil moisture map and in situ station data, including measurements through moderate forest canopy

### Soil Moisture–Live Fuel Moisture Relationship
- **Correlation analysis:** High correlation found between soil moisture anomaly (from UAS) and in situ live fuel moisture samples for multiple species (Chamise, oak, etc.) across test site (Figure 4)
- **LFM map generation:** Successfully converted soil moisture maps to LFM maps for May 2022, August 2022, and May 2023 (Figure 5)
- **Spatial validation:** Mobile TDR measurements conducted with random sampling strategy to reduce spatial autocorrelation in validation statistics

### Cross-Platform Demonstration
- **L-band UAVSAR validation:** Soil moisture retrieval algorithm demonstrated at 6m resolution over fire-prone areas (grass-forest hills, farms, aspen forest) with visual agreement to UAS estimates
- **NISAR simulation:** Global demonstration at 200m resolution showing algorithm applicability

## Notable Details

### Project Milestones & Timeline
- **Year 1 focus:** Retire highest-risk items: (1) fuse UAS data with UAVSAR P-band data and produce live fuel moisture maps, (2) demonstrate real-time onsite soil moisture calculation, (3) fly 2 UAS simultaneously with single pilot
- **Year 2 focus:** Expand to 4 UAS single-pilot operation; integrate NISAR data for large-area tasking; implement terrain-aware flight planning
- **Year 3 focus:** Full operational demonstration: 8 UAS flown by single pilot, maps delivered within 30 min of landing, integration with wildfire management partner's prescribed burn operations

### Risk Mitigation Strategy
1. **Data Quality Risk:** Addressed by demonstrated past performance on same test site with multiple iteration cycles; team capable of making hardware/software changes to meet quality metrics
2. **Flight Permissions Risk:** Co-I #4 has PhD-level expertise in multi-UAS flight operations,