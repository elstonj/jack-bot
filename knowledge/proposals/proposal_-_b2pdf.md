# Soil Moisture Mapping sUAS - CCRPP Application (Form B2)

## Document Metadata
- **Type:** SBIR/STTR CCRPP Application (Commercialization proposal)
- **Client/Agency:** NASA (SBIR/STTR Civilian Commercial Readiness Pilot Program)
- **Program/Solicitation:** NASA SBIR Phase II/II-E follow-on; Soil Moisture Mapping sUAS project
- **Date:** March 30, 2017
- **BST Products/Systems Referenced:** SuperSwift sUAS, L-band radiometer (3rd revision), SwiftPilot autopilot, SwiftStation ground control station, SwiftTrainer sUAS, SwiftCore avionics
- **Key Personnel:** Jack Elston (editor, Dr., sUAS expert), Maciej Stachura (Dr., sUAS/sensor fusion expert), Bradley Cheetham (Chief Operating Officer), Harvey Gates (advisor), Sid Vedula (advisor), Brian Argrow (advisor), Miguel O. Román (NASA GSFC collaborator)

## Executive Summary
Black Swift Technologies seeks CCRPP matching funds to commercialize two core technologies from its Soil Moisture Mapping sUAS SBIR: an L-band radiometer and the SuperSwift small unmanned aircraft system. The company aims to improve manufacturability, design a production-ready 3rd-generation radiometer, integrate new scientific payloads, and conduct 10 flight validation campaigns over 15 months. This effort is backed by $177,157 in matching investments from NASA MALIBU, University of Colorado, University of Maryland Eastern Shore, and NOAA FIREX projects.

## Technical Approach

### SuperSwift Manufacturability
- Redesign and optimize fuselage construction for outsourcing to Northwind Composites with improved assembly jigs and tolerances
- Simplify internal component mounting and wiring integration
- Redesign tail to reduce complexity and cost while maintaining structural requirements
- Develop wing design for reduced labor intensity and cost
- Improve avionics integration and sensor suite mountings
- Build three aircraft sequentially during CCRPP to validate manufacturing improvements
- Result: repeatable, rapid production capability

### L-band Radiometer (3rd Generation)
- Evolution from labor-intensive Phase II prototype to manufacturable circuit design
- Focus on electronics design, system architecture, mechanical design, tooling, and compliance
- Shift from manual assembly/testing/tuning to manufactured circuit boards
- Improved stability and performance vs. current version
- Enable scaling of production and cost reduction

### SuperSwift for New Applications
- Modular nose cone design allows payload swapping without airframe modification
- MALIBU project: integrate multispectral payload tray for tetracam imaging (satellite cal/val)
- NOAA FIREX project: integrate meteorological/trace gas measurement payload (CO, CO₂, relative humidity, particle density)
- Field-swappable payload architecture to expand SuperSwift market beyond soil moisture

### Flight Validation
- 10 flight campaigns planned across multiple test sites and applications
- Partner with Project Drought (CU), UMES variable irrigation, MALIBU, and FIREX teams
- Validation of manufacturability improvements, radiometer performance, and new payload integrations

## Products & Capabilities Described

### SuperSwift sUAS
- **What it is:** Modular, small unmanned aircraft system designed for scientific payloads; evolved from earlier Tempest design
- **Payload capacity:** Modular front nose cone with dedicated payload bay; EMI-shielded design for sensitive instruments
- **Flight characteristics:** Capable of operating from unimproved areas; simplified operations minimize ongoing costs
- **Unique features:** 
  - Payload modularity allows rapid swapping of different sensors in the field
  - Front-mounted payload configuration reduces EMI issues vs. externally-mounted sensors
  - Based on BST heritage systems with proven commercial reliability
  - Able to carry both soil moisture radiometer and multispectral imaging packages

### L-band Radiometer (Soil Moisture Measurement)
- **What it is:** Core sensor for soil moisture mapping; passive microwave instrument measuring at L-band frequency
- **Measurement capability:** ~15-meter spatial resolution (vs. ~40 km for satellite SMAP)
- **Current status:** Phase II prototype requires extensive manual assembly and tuning; electromagnetic interference issues with external mounting
- **Proposed improvement (Rev 3):** Manufactured circuit design, improved stability, reduced production labor, better sensor performance
- **Applications:** 
  - Soil moisture mapping for precision agriculture
  - Satellite mission calibration and validation (SMAP, Aquarius, SMOS)
  - Flash flood prediction support (via soil moisture data assimilation into rainfall-runoff models)

### MALIBU Multispectral Payload
- **What it is:** Tetracam multispectral imaging package for satellite calibration/validation
- **Integration:** Swappable payload for SuperSwift nose cone
- **Applications:** Calibration/validation for JPSS-1, GOES-R, Sentinel 2a/b, 3a/b, Landsat-8, Meteosat (MSG-3)
- **Benefit:** Single SuperSwift airframe can support both MALIBU imaging and soil moisture radiometer missions

### NOAA FIREX Payload
- **What it is:** Meteorological and trace gas measurement package for wildfire monitoring
- **Parameters:** Relative humidity, particle number density, CO, CO₂ for modified combustion efficiency
- **Configuration:** Both in-situ and remote sensing payloads
- **Integration:** Swappable with soil moisture payload on SuperSwift

### SwiftTrainer
- **What it is:** Smaller, lower-cost UAS variant
- **Role in CCRPP:** Delivery to UMES (University of Maryland Eastern Shore) in summer 2017 for training prior to SuperSwift operations
- **Purpose:** Accelerate customer readiness and expand operational capability

### Existing Commercial Products
- **SwiftPilot autopilot:** Avionics/control system
- **SwiftStation ground control station:** Tablet-based software interface
- **SwiftCore avionics package:** Control algorithms, intelligent sensor fusion, data post-processing (held as trade secrets)

## Use Cases & Applications

### 1. Satellite Calibration & Validation (Primary NASA Market)
- Support NASA Earth Science satellite missions (SMAP, Aquarius, SMOS)
- Support CEOS-Space agencies: ESA, NOAA, USGS, EUMETSAT
- MALIBU project: provide reference measurements for validation of JPSS-1, GOES-R, Sentinel, Landsat-8, Meteosat
- High-resolution, on-demand augmentation data to satellite measurements
- Superior spatial resolution (15m vs. 40km for SMAP) for validation in variable areas (watersheds, coasts)

### 2. Precision Agriculture (Large Commercial Market)
- **Project Drought (University of Colorado):** Variable rate irrigation optimization at Irrigation Research Foundation (IRF) test site
  - Demonstrated >15% water savings while maintaining crop yields using soil moisture data
  - Currently using in situ probes; SMM sUAS provides remote sensing alternative
  - Flight validation Q3 2017, finalized system Q2 2018
- **UMES Variable Rate Irrigation:** University of Maryland Eastern Shore test farm
  - Planned operations Q2 2018
  - UMES positioned as potential system owner/operator given aviation heritage
- **Potential customers identified:** Oklahoma State University, St. Louis University, Bristol University, Colorado State University, Monash University (Australia), National Geospatial-Intelligence Agency (NGA)
- **Market potential:** ~1,400 in situ soil moisture monitoring sites globally; ~2.2 million farms in US alone
- **Value proposition:** Reduce water usage while maintaining crop yields; supplement/replace expensive manual ground probing

### 3. Flash Flood Prediction & Emergency Management
- Historical precedent: 2007 NASA-funded study using P-3 aircraft with Polarimetric Scanning Radiometer over Texas/Oklahoma flooding region
- Data assimilation into rainfall-runoff models to calculate flooding thresholds and improve FEMA alerts
- sUAS capability would reduce operational costs vs. manned aircraft
- BST was contacted for potential deployment during 2017 landslide events in Grand Junction, CO and Washington (system not ready at time)
- FEMA potentially interested in validation capability

### 4. Wildfire Monitoring & Meteorological Measurement (NOAA FIREX)
- University of Colorado/NOAA FIREX project investment
- Integration of meteorological payload (humidity, trace gases) with SuperSwift
- Demo flights Q2 2018; sustained deployment by Q2 2019
- Focus on measuring fire impact on atmospheric composition
- Potential for expanded NOAA funding and continued work through 2019

## Key Results (for reports)
Not a results report. This is a forward-looking CCRPP proposal. However, it references prior accomplishments:
- **Phase II/II-E achievements:** 
  - SuperSwift prototype demonstrated with MALIBU team in two flight campaigns
  - L-band radiometer prototype functional but labor-intensive
  - Tempest aircraft with external radiometer (early design) had EMI issues; SuperSwift resolved this
- **Project Drought achievement:** >15% water savings demonstrated with soil moisture-guided irrigation
- **FAA approvals:** Dr. Elston and Dr. Stachura have received ~140 Certificates of Authorization; successfully completed multiple NASA flight safety reviews
- **Prior company launches:** Successfully commercialized SwiftPilot autopilot, SwiftStation ground station, SwiftTrainer sUAS
- **2016 financial:** Company revenue $676,396.76; net income -$39,936.29 (early stage company with heavy R&D investment)
- **2017 expected:** New NASA Phase II SBIR at $750,000 (separate from this CCRPP)

## Notable Details

### Customer/Investor Base
- **Four primary matching investors:**
  1. **NASA MALIBU** ($49,604 + $41,073 = $90,677): SuperSwift integration with multispectral payload; commitment to fly through summer 2018
  2. **University of Colorado - Project Drought** ($49,090): Precision agriculture validation at IRF site
  3. **University of Maryland Eastern Shore** ($15,000): Training and variable rate irrigation integration
  4. **University of Colorado - NOAA FIREX** ($22,390): Wildfire/meteorological payload integration
  
- **Total matching funds:** $177,157
- **Six additional potential customers with expressed interest:** NGA, OSU, SLU, Bristol, CSU, Monash University

### Competitive Advantages
1. **Unique system:** No known sUAS competitor integrating L-band radiometer for soil moisture mapping
2. **First-mover advantage:** Next revision of radiometer positions BST first-to-market
3. **Operational simplicity:** SuperSwift designed for ease of use, reducing operational costs
4. **Modularity:** Payload-swappable design enables single airframe to support multiple scientific missions
5. **Heritage & expertise:** BST team includes industry-leading sUAS experts with 140+ FAA CoAs, hundreds of UAS deployments
6. **Cost advantage:** Manufacturing improvements will enable scalable, affordable production vs. manned aircraft alternatives

### Market Strategy
- **Target markets:** Satellite cal/val (primary NASA focus), precision agriculture (largest civilian market potential: $14M+ addressable with in situ sensor augmentation alone), wildfire monitoring
- **Market entry:** Expected to coincide with CCRPP completion (~Q3 2018)
- **Commercialization approach:** Demonstration-driven (field trials), NASA program integration first, then non-NASA government, then commercial precision ag
- **Go-to-market:** Partnerships with UMES and Project Drought teams for field operations and training; marketing firm support for aerospace/defense sector sales
- **Revenue model:** System sales plus operational services (flying sUAS as a service)

### Manufacturing & Production Plans
- **SuperSwift fuselage:** Outsourcing to Northwind Composites once design optimized
- **L-band radiometer:** Shift from manual assembly to manufactured PCB design
- **Procurement:** Standard commercial parts; no exotic materials or suppliers
- **Technical approach:** Iterative build-test-improve cycle during CCRPP (3 aircraft builds)

### Intellectual Property
- **Patents pending:** Novel science-grade geo-referenced data acquisition unit; normalized difference vegetative index (NDVI) electronics; user interface software features
- **Partnerships:** Legal assistance from University of Colorado Boulder's Entrepreneurial Law Clinic for patent prosecution