# Elston-Jack-1-RFI: Black Swift Technologies Response to NASA SMD "Science as a Service" RFI

## Document Metadata
- **Type:** Request for Information (RFI) response
- **Client/Agency:** NASA Science Mission Directorate (SMD)
- **Program/Solicitation:** NNH26ZDA006L — Advancement of "Science as a Service" for NASA and Commercial Partners
- **Date:** 2026-04-29
- **Primary Topic:** D — Transition from Demonstration to Commercial Operations
- **Secondary Topics:** B (Demonstration Pathways), E (Partnerships/Ecosystem), A (Commercial Business Case Technology Needs)
- **BST Products/Systems Referenced:** S0, S2, S2-VTOL, S3
- **Key Personnel:** Jack Elston, Ph.D. (Chief Executive Officer); Beck Cotter (last editor)

## Executive Summary
Black Swift Technologies responds to NASA's SaaS RFI from the perspective of a small commercial UAS provider that has successfully executed SBIR-to-operations transitions multiple times. BST argues that the primary bottleneck in technology commercialization is not technical capability but structural gaps in contracting, productization funding, operational transition support, and lifecycle maintenance. The response also contends that the RFI's exclusively orbital platform list is incomplete and that airborne sub-orbital demonstrations are a necessary complement for atmospheric boundary-layer measurements, persistent fixed-geography monitoring, and instrument pre-maturation before orbital deployment.

## Technical Approach

### BST's Lived Transition Experience
BST frames its response around **five key findings from portfolio experience:**

1. **Phase III Gap is Contracting, Not Technology:** Most SBIR awards terminate after Phase II because Phase III requires a specific federal customer with sole-source contracting authority and aligned budget. BST's successful Phase III transition (80NSSC22CA192, CCRPP 2022–present) occurred because NASA SMD-funded science teams had continuing operational requirements that translated into Phase III scope.

2. **Productization Requires Unfunded Investment:** The transition from prototype ("one that worked") to production fleet ("ten that perform identically") requires $200K–$500K in company-internal investment in tooling, calibration jigs, manufacturing documentation, and QA. This gap is not funded by NASA Phase III, NOAA AOC, or commercialization-assistance programs (NIIN, I-Corps).

3. **Operational Transition Needs Exceed Engineering:** Deployment to operational platforms (e.g., NOAA WP-3D for hurricane reconnaissance) requires FAA approvals, operator training documentation, integration with mission-planning workflows, and crew-resource-management procedures—none of which are NASA scope or Phase III funded.

4. **Reference Data is Highest-Leverage NASA Contribution:** NASA-validated reference datasets (e.g., co-located dropsondes with BST atmospheric sensors during Hurricane Helene 2024) are worth more for commercial customer acquisition than cost reduction. Customers purchase based on quantitative validation against authoritative references, which only NASA can provide.

5. **Long-Term Lifecycle Support is Most Under-Funded:** NASA validation typically ends at demonstration, but customers require 5–10 years of maintenance, calibration updates, re-flights, and software upgrades. Without funded lifecycle paths, validated technology becomes orphaned within 2–3 years.

## Products & Capabilities Described

### S-Series Aircraft Platforms
**S0, S2, S2-VTOL, S3**
- Multi-rotor and fixed-wing UAS platforms
- Deployed operationally by NOAA AOC for hurricane reconnaissance (23 documented S0 deployments from NOAA WP-3D in 2025 Atlantic season across Hurricanes Helene, Milton, Francine, Tammy)
- Used for atmospheric boundary-layer profiling, inflow-layer wind and humidity measurement
- Capable of 25 km BVLOS operations (demonstrated at Makushin Volcano with SO₂/CO₂ payloads)
- Night-and-day IR persistence demonstrated (24-hour continuous flight at Sunny Slope Sod Farm, August 2025)
- Arctic atmospheric profiling capability to 14,000 ft AGL

### Sensor Fusion Stack
**Terrain Following / Obstacle Avoidance (TFOA)**
- Developed under NASA SBIR Phase II (2018–19)
- Integrates radar, lidar, and stereo vision
- Transitioned to operational NOAA WP-3D hurricane reconnaissance
- Required FAA approval and extensive ConOps documentation beyond Phase II scope

### Atmospheric & Geochemical Payloads
- SO₂ and CO₂ sensors for volcanic plume sampling
- Inflow-layer wind and humidity measurement packages
- IR sensors for persistent wildfire monitoring
- Soil-moisture validation payloads for SMAP-class cal/val campaigns
- Methane point-source detection (sub-ppb sensitivity)

### Supporting Technologies
- ML-based predictive maintenance / augmented onboard intelligence (Phase II 2017–20, partially deployed in BST avionics)
- Adaptive and secure autonomy systems (Phase I award 80NSSC25C0155, 2025)

## Use Cases & Applications

### Operational Deployments (Current)
1. **Hurricane Reconnaissance:** 268 NOAA P-3 missions analyzed (2022–25); 23 S0 deployments in 2025 season providing inflow-layer dynamics unavailable from orbital platforms
2. **Persistent Wildfire Monitoring:** 24-hour continuous demonstration (NightFOX program, NASA Ames + USFS partnership, August 2025)
3. **Volcanic Plume Sampling:** Makushin Volcano (Aleutians) with planned Chile deployment Q1 2026 under USGS VDAP partnership
4. **Arctic Atmospheric Profiling:** Greenland ice sheet operations
5. **Soil-Moisture Cal/Val:** Costa Rican rainforest canopy campaigns (NOAA WPO SPLASH 2023–24, NASA-funded campaigns)

### Geographical Reach
- Seven continents flown

## Key Findings & Recommendations

### Transition Outcome Analysis (Table 1)
| NASA Investment | Years | Customer | Status Today | Bottleneck |
|---|---|---|---|---|
| Phase II ML Predictive Maintenance | 2017–20 | None | Internal R&D only; no federal procurement | No Phase III customer pull |
| Phase II TFOA (Radar/Lidar/Stereo Fusion) | 2018–19 | NOAA AOC/HRD | Operational on hurricane missions | Required NOAA-funded ConOps & training outside NASA scope |
| Phase III CCRPP (80NSSC22CA192, S2-VTOL → S3) | 2022–present | NASA SMD + NOAA + USFS | Active operational; multiple campaigns | Multi-customer demand pull is decisive factor |
| Persistence Demo (NightFOX, 24-hr S2) | 2024–25 | NASA Ames + USFS | Validated; commercialization in progress | Productization unfunded; customer ConOps in development |
| Phase I Adaptive/Secure Autonomy (80NSSC25C0155) | 2025 | TBD | TRL maturation | Outcome depends on Phase II selection |

### Complementarity of Sub-Orbital and Orbital Pathways (Table 2)
| Phenomenon | Best Pathway | Why |
|---|---|---|
| Atmospheric boundary layer (0–3 km AGL) | Airborne sub-orbital | Below-cloud, sub-km horizontal scales; orbital cannot resolve |
| Hurricane inner-core dynamics | Airborne sub-orbital | Eyewall penetration in real time; orbital revisits miss event |
| Methane point sources (sub-ppb) | Airborne sub-orbital | Sensitivity unattainable from orbit at relevant spatial scales |
| Persistent fixed-geography monitoring (wildfire perimeter) | Airborne sub-orbital | Minute-to-hour cadence over fixed area; orbital revisit too coarse |
| Pre-orbital instrument maturation | Airborne → orbital | Cheap, fast iteration loop before committing to space build |
| Global synoptic radiation, sea-surface temperature, GHG columns | Orbital | Coverage scale airborne cannot match |
| Soil moisture, snow water equivalent cal/val | Co-located airborne + orbital | In-situ truth required to maintain satellite-product quality (SMAP class) |

## Recommendations for VTA Program Design

### 1. Fund "Phase II.5" Contracting Bridges
- Distinct award class focused on federal customer pre-engagement and sole-source justification packaging
- Not additional R&D, but contracting infrastructure

### 2. Milestone-Based Productization Grants
- Tied to specific commercial-customer milestones (e.g., "first 10 units delivered to non-NASA paying customer")
- Separate from technology development funding

### 3. Fund Operator-Facing Transition Deliverables
- Training packages, ConOps documentation, certification artifacts
- Scoped to receiving federal user's standards
- Gated as milestone achievements

### 4. Bundle Flight Demonstrations with Reference-Data Packages
- Calibration coefficients and comparison against authoritative instruments
- Traceable uncertainty budgets
- Citable in commercial sales

### 5. Include 5-Year Lifecycle Clause in VTA Awards
- NASA-funded calibration, firmware, and re-flight support
- Ramp down as commercial customer base scales

### 6. Integrate Airborne Sub-Orbital Track into VTA
- Standardized cal/val protocols inter-comparable with orbital products of record
- Co-located reference data (dropsonde, radiosonde, lidar) during campaigns
- ConOps documentation for federal-user adoption
- Open-data products with IP protections for commercial sensor providers
- Model precedent: ESTO's Sub-Orbital Research and Airborne Science programs

### 7. Three-Way Co-Funding Pilot Structure
- **(a)** NASA funds validation flight
- **(b)** Federal operational user (NOAA, USFS, USGS, DOI, FEMA, USDA) funds transition deliverables
- **(c)** Commercial provider funds productization
- Implement via milestone-gated three-way MOU aligning incentives across SaaS chain

### 8. Pre-Negotiated IP Licensing Language
- Model on NASA Space Act Agreements, adapted for sub-orbital airborne
- Shared environmental test access (NASA AFRC airworthiness, NASA Ames flight integration)
- Federal-user advisory board for each VTA award to maintain alignment with operational requirements

## Notable Details

### Core Insight on Commercial Bottleneck
BST affirms NASA SMD's core premise: **the bottleneck in technology commercialization is not technical capability but structural gaps in the validation-to-productization-to-contracting-to-customer-acquisition chain.** R&D investment alone cannot bridge these structural breaks.

### Critical Partnership Examples
1. **HS3 → NOAA Operations:** NASA HS3 airborne hurricane research (2012–14) enabled platform maturation that NOAA AOC and HRD now operate routinely
2. **FireSense → USFS:** NASA Ames FireSense and USFS S2 wildfire airspace concept share platforms and ConOps; cross-pollination reduces development cost
3. **Earth Science Volcanology → USGS VDAP:** NASA research enabled platform maturation now deployed at Makushin and Chile under USGS partnership

### Commercial Market Reality
The limiting factor in scaling Earth-observation business is **not sensors** but persistent, low-cost, infrastructure-free deployment. Key technology gaps:
- **Autonomy stacks** for BVLOS persistent operations
- **Low-SWaP communications** (SATCOM, mesh) for remote/maritime/Arctic regions
- **Standardized airborne-to-spaceborne cal/val protocols**
- **Onboard data-reduction pipelines** minimizing comms requirements

These "unglamorous infrastructure problems" represent where NASA's science-mission-grade engineering would have the largest commercial multiplier.

### BST Portfolio Achievement
- 2,500+ legal flight hours
- 17 SBIR Phase I awards
- 7 SBIR Phase II awards
- Multiple NASA, NOAA, and USAF sponsors
- Successful SBIR-to-operations transitions executed repeatedly

### Availability for Follow-On Engagement
BST expressed willingness to participate in follow-on workshops, share operational data, transition lessons learned, and coordinate with federal-user partners (specifically