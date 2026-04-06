# NASA ROSES 2024 A.59 Wildfire Soil Moisture Project - Budget Justification

## Document Metadata
- Type: Budget Justification (NASA ROSES Step 2 Proposal)
- Client/Agency: NASA
- Program/Solicitation: 2024 ROSES A.59 (Research Opportunities in Space and Earth Sciences)
- Date: Submitted March 2024 (created March 7, 2024; modified March 28, 2024)
- BST Products/Systems Referenced: E2 UAS Flight System, Soil Moisture Mapping System
- Key Personnel: Dr. Jack Elston (PI, Chief Designer of BST UAS), Dr. Maciej Stachura (Co-I, design lead)

## Executive Summary
This budget justifies a three-year NASA-funded project (FY 2024-2026) led by Black Swift Technologies to advance wildfire prediction and monitoring through drone-based soil moisture and live fuel moisture mapping at Pepperwood Reserve in Sonoma County, California. The project integrates BST's E2 UAS systems with soil moisture radiometer payloads, advanced data processing from Orbital Micro Systems, satellite validation from JPL, and ground-truth campaigns from USGS and Pepperwood Foundation.

## Technical Approach

### Core BST Contribution
- **Project Leadership**: Dr. Jack Elston (PI) leads overall direction including flight campaign planning, flight testing, data collection, and UAS modifications for active terrain-aware flight and onboard data product calculation.
- **Design & Certification**: Dr. Maciej Stachura leads design effort culminating in eight (8) soil moisture UAS capable of being flown by a single operator, plus flight certification and NASA flight permission.
- **Flight Operations**: Two additional BST staff (Tech/Pilot and Engineer) support field campaigns.

### System Integration & Data Processing
**Orbital Micro Systems (OMS)** subaward ($79,996.80/year, 3.5 weeks labor per year):
- Firmware upgrade for L-band radiometer, NDVI, and thermal sensor measurements via FPGA board
- Post-processing software updates for real-time and semi-real-time data mapping
- Deliverables: Updated firmware/software; geo-reregistered brightness temperature, NDVI, thermal, and soil moisture maps (brightness temperature/NDVI/thermal in semi-real time)

### Satellite Validation & Analysis
**Jet Propulsion Laboratories / Dr. Seungbum Kim** subaward (~$80k/year, 0.18 FTE):
- **Year 1**: Soil moisture estimation at surface and root zone using P-band airborne UAVSAR; validation against in situ sensors
- **Year 2**: NISAR soil moisture product validation (expected 2025); comparison with drone-based soil moisture over entire Preserve
- **Year 3**: Fire perimeter detection from NISAR disturbance products; continued drone-vs.-satellite soil moisture analysis

### Ground Truth & Field Support
**Pepperwood Foundation / Ryan Ferrell** subaward ($65,998/year, 7.5 weeks labor per year):
- Ground validation sampling plan development for each flight campaign
- Field measurements: in situ soil moisture (pre-existing sensors, mobile TDR), soil cores for calibration, live fuel moisture sampling at varying heights
- Field logistics: scheduling, lodging at Bechtel House ($50/night), vehicular transport, equipment storage
- Data delivery: tabular and spatial datasets following each of 9 annual flight campaigns; annual and final data reports

**USGS / Dr. Michelle Stern** subaward (~$53k-$67k/year):
- Field work including three campaigns per year for soil moisture and live fuel moisture measurements
- Development of live fuel moisture maps from soil moisture data
- Year 1: 7.5 weeks (300 hours); Years 2-3: 9.75 weeks (390 hours)

## Products & Capabilities Described

### E2 UAS Flight System
- **What it is**: BST's primary unmanned aircraft system for environmental sensing
- **Specifications**: Sale price $18,500 per unit
- **Proposed use**: Delivery of soil moisture radiometer payload to map wildfire-critical soil moisture
- **Quantities**: 3 units Year 1, 2 units Year 2, 4 units Year 3 (total 9 systems across project)

### Soil Moisture Mapping System
- **What it is**: Integrated payload combining L-band radiometer, NDVI sensor, and thermal camera
- **Specifications**: Sale price $5,000 per unit
- **Proposed use**: Direct soil moisture estimation and supporting vegetation/thermal data collection
- **Quantities**: 3 units Year 1, 2 units Year 2, 4 units Year 3 (total 9 systems)
- **Key capability**: Achieves high spatial resolution soil moisture mapping via drone platform with real-time/semi-real-time processing

### Terrain-Aware Flight Capability
- **Development goal**: Modify E2 UAS for active terrain-aware flight (Dr. Elston leading technical effort)
- **Benefit**: Maintains constant altitude above terrain for consistent radiometer measurement geometry

## Use Cases & Applications

### Primary Mission: Wildfire Monitoring & Prevention
- **Site**: Pepperwood Reserve, Sonoma County, CA (post-2017 Tubbs Fire site)
- **Specific focus**: Live fuel moisture (LFM) estimation for wildfire prediction
- **Key relationship**: Soil moisture as proxy for vegetation water stress → LFM → wildfire risk
- **Campaign schedule**: 3 flight campaigns per year (October, April, July) over 3 years = 9 total campaigns

### Multi-Scale Integration
- **Drone scale**: High-resolution soil moisture maps (implied sub-meter to meter scale)
- **Satellite scale**: NISAR 200m resolution soil moisture for landscape-wide coverage
- **Ground scale**: In situ validation via TDR sensors, soil cores, and canopy sampling

### Data Products Delivered
- Brightness temperature maps (L-band radiometer)
- Soil moisture maps (calibrated and validated)
- NDVI maps (vegetation index)
- Thermal maps
- Live fuel moisture maps (derived from soil moisture)
- Fire perimeter detection (Year 3, from NISAR)
- Comparison analyses: drone vs. satellite soil moisture validation

## Budget Summary (3-Year Total)

### Black Swift Technologies
- **Year 1**: $401,573.76 (180 hrs Elston + 180 hrs Stachura + Tech/Pilot + Engineer; $70.5k equipment)
- **Year 2**: $452,608.08 (260 hrs Elston + 260 hrs Stachura + support staff; $47k equipment)
- **Year 3**: $453,024.13 (210 hrs Elston + 210 hrs Stachura + support staff; $94k equipment)
- **3-Year BST Total**: $1,307,205.97

### Subaward Partners (3-Year Combined)
- **Orbital Micro Systems**: $239,900.40
- **Jet Propulsion Laboratories**: $239,368.00
- **Pepperwood Foundation**: $197,994.00
- **USGS**: $178,359.00
- **Total Subawards**: $855,621.40

### Combined Project Budget
- **Estimated 3-Year Total**: ~$2.16 million (exact Year 2-3 facility costs redacted in document)

### Equipment Allocation
- **BST Equipment**: $211,500 total (9 x E2 UAS + 9 x Soil Moisture Mapping Systems)
  - Unit pricing: E2 at $18,500; Soil Moisture System at $5,000
- **Pepperwood Equipment**: ~$1,955 total (sampling equipment: Nalgene bottles, scales, tree tags, pole pruners, etc.)

## Key Technical Personnel & Roles

| Person | Organization | Role | Annual Hours |
|--------|--------------|------|--------------|
| Dr. Jack Elston | BST | PI, Chief UAS Designer | 180 (Y1), 260 (Y2), 210 (Y3) @ $350/hr |
| Dr. Maciej Stachura | BST | Co-I, Design Lead (8-UAS system) | 180 (Y1), 260 (Y2), 210 (Y3) @ $350/hr |
| Eryan Dai | Orbital Micro Systems | Firmware/Data Processing Lead | 3.5 weeks/year |
| Dr. Seungbum Kim | JPL | Satellite Validation & Analysis | 0.18 FTE/year (314-316 hours) |
| Dr. Michelle Stern | USGS | Field Work & LFM Mapping | 7.5 weeks (Y1), 9.75 weeks (Y2-Y3) |
| Ryan Ferrell | Pepperwood Foundation | Ground Validation & Logistics | 7.5 weeks/year (776.67 hours) |

## Notable Details

### Unique Capabilities & Competitive Advantages
1. **Single-operator multi-UAS capability**: Design goal of 8 drone systems flown by one operator reduces operational cost and complexity
2. **Real-time data processing**: OMS firmware/software upgrade enables semi-real-time brightness temperature, NDVI, thermal mapping during flight
3. **Multi-scale validation**: Integrated drone + satellite (NISAR/UAVSAR) + ground truth approach provides unprecedented soil moisture validation framework
4. **Live fuel moisture focus**: Direct application to wildfire risk prediction (not just research)

### Partnerships & Coordination
- **Established relationship**: OMS has "cooperated with Black Swift Technologies over the last several years on drone-based high spatial resolution soil moisture mapping"
- **Cross-institutional team**: BST (lead), OMS (firmware/processing), JPL (satellite validation), USGS (field science), Pepperwood (site access/logistics)
- **Site access**: Pepperwood Reserve as multi-year research facility with established infrastructure (Bechtel House lodging, field staff)
- **Regular coordination**: Monthly teleconference meetings between BST and JPL throughout project

### Client Requirements Addressed (NASA ROSES A.59)
- **Scientific innovation**: Integration of drone radiometry with satellite soil moisture (NISAR) for wildfire applications
- **Earth science data**: Production of high-resolution, validated soil moisture and LFM datasets
- **Technology development**: UAS modifications for terrain-aware autonomous flight and onboard data product calculation
- **Deliverables**: Annual progress reports, computer codes, tabular/spatial datasets, final data package

### Travel & Operations
- **Field location**: Sonoma County, CA (Pepperwood Reserve)
- **Flight campaigns**: 3 per year (October, April, July) over 3 years = 9 campaigns total
- **Duration per campaign**: ~2 weeks, with 6 weeks total travel per year (PI + Co-I)
- **GSA per diem**: $157/day for Sonoma County (basis for cost estimates)
- **Nightly lodging**: $50/night at Pepperwood's Bechtel House field station

## Notable Absences/Document Limitations
- Year 2 and Year 3 total costs partially redacted (marked "XXXX") but individual budget lines provided
- No external consultant costs identified
- Chart referenced for labor distribution not included in extracted document
- Invoice details for E2 UAS and budget breakdowns from partner organizations mentioned but not fully visible in text format