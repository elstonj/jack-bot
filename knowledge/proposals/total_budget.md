# ROSES 2023: On-demand Wildfire Susceptibility from Fuel Moisture and Vegetative Index Maps — Budget Justification

## Document Metadata
- **Type:** Budget Justification / Grant Proposal (NASA ROSES 2023)
- **Client/Agency:** NASA
- **Program/Solicitation:** ROSES 2023, NNH23ZDA001N-FIRET (Fire Ecology topic)
- **Date:** Submitted 2024 (modified May 7, 2024)
- **BST Products/Systems Referenced:** E2 UAS Flight System
- **Key Personnel:** Dr. Jack Elston (PI), Dr. Maciej Stachura (Co-I)
- **Collaborating Organizations:** Orbital Micro Systems (OMS), Jet Propulsion Laboratory (JPL), Pepperwood Foundation, USGS

## Executive Summary
This NASA ROSES proposal requests funding for a three-year project to develop on-demand wildfire susceptibility maps derived from soil moisture and vegetative index data. Black Swift Technologies will lead the effort using its E2 UAS platform equipped with L-band radiometer, NDVI, and thermal sensors, conducting repeated flight campaigns at Pepperwood Preserve in Sonoma County, California. The project integrates drone-based high-resolution soil moisture mapping with satellite data (NISAR, UAVSAR) and ground validation to create live fuel moisture maps for wildfire risk assessment.

## Technical Approach

**Overall Strategy:**
- Three annual flight campaigns (October, April, July) over three years at Pepperwood Preserve
- Multi-UAS operations: design and certification of eight soil moisture UAS to be flown by single operator
- Real-time and semi-real-time data processing for rapid product generation
- Integration of airborne P-band (UAVSAR) and satellite L-band (NISAR) soil moisture retrievals
- Ground validation through in situ soil moisture sensors, TDR measurements, and live fuel moisture sampling

**BST Technical Lead Role:**
- Dr. Jack Elston (PI): 520 hours/year overseeing flight campaign planning, instrument integration, data collection, and UAS improvements
- Dr. Maciej Stachura (Co-I): 500 hours/year leading design effort for multi-UAS operations and flight certification/NASA approval
- Field teams: Tech/Pilot and Engineer (240 hours/year each) for on-site flight operations
- Focus on active terrain-aware flight modifications and onboard calculation of data products

**Sensor Integration:**
- L-band radiometer for soil moisture retrieval
- NDVI sensor for vegetation monitoring
- Thermal sensor for temperature/moisture relationships
- All sensors require firmware upgrades via FPGA board for real-time processing

## Products & Capabilities Described

### E2 UAS Flight System
- **What it is:** Black Swift Technologies' primary UAS platform for remote sensing operations
- **Specifications:** Priced at $18,500 per flight system; multiple systems deployed annually
- **Equipment quantities requested:**
  - Year 1: 3 systems ($55,500)
  - Year 2: 2 systems ($37,000)
  - Year 3: 4 systems ($74,000)
- **Total equipment cost (all three years):** $166,500
- **Usage context:** Equipped with L-band radiometer, NDVI, and thermal sensors for soil moisture and vegetation mapping
- **Operational innovation:** Designed for autonomous/terrain-aware flight and real-time onboard data product calculation

### Multi-UAS Operational Capability
- **Objective:** Design and certify eight soil moisture UAS for operation by single operator
- **Status:** Under development during project period
- **Significance:** Major advancement in operational efficiency for environmental monitoring

## Use Cases & Applications

**Primary Mission:** Wildfire Fuel Moisture Assessment
- **Location:** Pepperwood Preserve, Sonoma County, California
- **Application:** Develop predictive maps of live fuel moisture as indicator of fire susceptibility
- **Operational frequency:** 3 flight campaigns annually (October pre-fire season, April spring condition, July peak summer)
- **Coverage:** High-resolution drone mapping supplemented by satellite coverage across larger preserve area

**Specific Campaign Focus:**
- **Year 1 (Oct 2024-Sept 2025):** Establish baseline with P-band UAVSAR flights during three campaign periods; validate with ground sensors; develop initial live fuel moisture relationships
- **Year 2 (Oct 2025-Sept 2026):** Integrate NISAR satellite soil moisture data (expected 2025); compare NISAR vs. drone-based products; explore full-preserve fuel moisture estimation using satellite data
- **Year 3 (Oct 2026-Sept 2027):** Detect wildfire perimeters and post-fire disturbance using NISAR; continue NISAR/drone soil moisture comparison and analysis

**Fire Risk Management Context:**
- Enable on-demand assessment of vegetation moisture conditions
- Support informed decision-making for fire prevention and suppression resource allocation
- Provide spatially explicit fuel moisture maps for targeted prescribed burning or defensible space planning

## Budget Summary (3-Year Total: $1,941,857.58)

### Black Swift Technologies Direct Costs: $1,262,778.18
- **Year 1:** $419,590.49
- **Year 2:** $398,859.14
- **Year 3:** $444,328.56

**Breakdown:**
- Direct Labor (3 years): Dr. Elston (520 hrs/yr @ $150/hr = $234,000), Dr. Stachura (500 hrs/yr @ $150/hr = $225,000), Tech/Pilot (240 hrs/yr @ $75/hr = $54,000), Engineer (240 hrs/yr @ $125/hr = $90,000)
- Equipment: $166,500 (9 E2 Flight Systems @ $18,500 each)
- Travel: $106,391.04 (6-week field campaigns 3x/year, three people; includes flights $34,608.60/yr, car rental, per diem, shipping)
- Shipping of equipment: ~$23,877 total (3 deployments/year, 2-way trips)
- Equipment shipping costs increase annually due to distance/scale: $6,886.08 (Year 1), $7,809.72 (Year 2), $9,181.44 (Year 3)
- MPS and F&A: $27,322 (allocated and general admin across 3 years)

### Partner Organization Subawards:
- **Orbital Micro Systems:** $239,900.40 (firmware/software upgrades, real-time data processing, L-band radiometer calibration)
- **Jet Propulsion Laboratory:** $239,368.00 (UAVSAR deployment/retrieval, NISAR data processing and validation)
- **Pepperwood Foundation:** $198,426.00 (ground validation, field logistics, site management)
- **USGS (Michelle Stern):** $178,359.00 (field measurements, live fuel moisture sampling, map development)

## Key Results & Deliverables

**Orbital Micro Systems Deliverables:**
- Upgraded firmware for L-band radiometer, NDVI, and thermal sensor processing (FPGA-based)
- Updated post-processing software for real-time and semi-real-time mapping
- Georegistered brightness temperature maps
- Soil moisture maps (daily per flight)
- NDVI and thermal maps (semi-real-time)

**JPL Deliverables:**
- Annual progress reports with UAVSAR and NISAR soil moisture products
- Fire perimeter maps from NISAR disturbance detection
- Computer codes for data generation
- Monthly teleconference participation and science team meeting attendance
- NISAR soil moisture validation at surface and root zone (200m resolution)
- Comparison analysis of drone vs. satellite retrievals

**Pepperwood Foundation Deliverables:**
- Ground validation sampling plans (pre-flight)
- In situ soil moisture measurements (pre-existing sensors, TDR, soil cores)
- Live fuel moisture samples (canopy collection at multiple heights)
- Tabular and spatial datasets post-campaign
- Annual and final data summary reports
- Geospatial shapefiles and processed sample data

**USGS Deliverables:**
- Field measurements of soil moisture and live fuel moisture
- Live fuel moisture maps derived from soil moisture data
- Field campaign participation (3 campaigns/year)

## Notable Details

**Partnerships & Institutional Integration:**
- Multi-agency collaboration: NASA-funded lead organization (BST) with JPL (satellite validation), USGS (ground science), small business partner (OMS for sensor processing)
- Academic/non-profit engagement: Pepperwood Foundation provides site access and ground truth infrastructure
- Cost-share arrangement: Pepperwood provides existing sensors and onsite housing ($50/night for field staff vs. commercial lodging)

**Technical Innovation Highlights:**
- Real-time/semi-real-time soil moisture and vegetation mapping (contrast with traditional delayed processing)
- Multi-UAS single-operator design (operational scalability advance)
- Active terrain-aware flight capability (precision positioning in complex topography)
- Integrated drone-satellite validation framework (bridging high-resolution and broad-scale coverage)
- FPGA-based onboard firmware processing (reduced data transmission/storage burden)

**Competitive Advantages Demonstrated:**
- BST's E2 platform proven track record (Elston involved with radiometer project since 2013)
- OMS partnership provides specialized sensor processing expertise
- JPL provides world-class radar satellite data integration capability
- Three-year sustained campaign allows seasonal variation analysis and multi-year validation

**Project Risk Mitigation:**
- Multiple equipment units deployed (3, 2, and 4 systems across years) to ensure campaign continuity
- Dual technical leads (Elston and Stachura) ensuring expertise continuity
- Pre-existing relationships with JPL and OMS reduce integration risk
- Ground validation by USGS experts provides independent quality control

**Operational Context:**
- Site: 3,200-acre Pepperwood Preserve represents mixed oak woodland and chaparral ecosystems typical of California fire-prone regions
- Timeline: 9 total flight campaigns over 3 years (3 per year)
- Team structure: 4-6 person field teams (PI, Co-I, tech/pilot, engineer, plus Pepperwood and USGS field staff)
- Cost efficiency: $106K/year travel for multi-week field campaigns across 3 people and equipment shipping

**Budget Justification Methodology:**
Document explicitly states grassroots cost estimate derived from:
- Expert judgment of experienced team members
- Vendor quotes (UPS shipping calculator, travel booking sites, GSA per diem rates)
- Historical experience with similar radiometer projects
- Analogous project data from team's past work