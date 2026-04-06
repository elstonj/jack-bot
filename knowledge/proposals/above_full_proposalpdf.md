# Evaluating Arctic Radiation Balance and Photosynthesis Characteristics with the Multi-Angle Imaging Unmanned Airborne System (MALIBU)

## Document Metadata
- Type: NASA Research Proposal
- Client/Agency: NASA Earth Science Division (Terrestrial Ecology Program)
- Program/Solicitation: NNH16ZDA001N-TE; NASA Proposal Number 16-TE16-0009
- Date: Submitted 08/01/2016
- BST Products/Systems Referenced: SuperSwift airframe, Tempest "Tornado Chaser" platform
- Key Personnel: Maciej Stachura (Black Swift Technologies, Co-I); Zhuosen Wang (UMD, PI); Miguel Román (NASA/GSFC, Co-I)

## Executive Summary
This proposal seeks NASA funding ($496,264 over 3 years, 2017-2020) to deploy MALIBU (Multi-Angle Imaging Bidirectional reflectance distribution function small-Unmanned aerial system) to assess how Arctic shrub encroachment and boreal forest wildfires affect surface energy exchange and climate. The project will use the SuperSwift unmanned aircraft platform (developed by Black Swift Technologies) to collect high-resolution multi-angle reflectance measurements for validating satellite albedo products and characterizing photosynthesis vegetation indices across Arctic and boreal ecosystems.

## Technical Approach

**MALIBU System Overview:**
- Semi-autonomous small UAS (sUAS) with full blanket exemption for US and Canada operations
- Carries two Tetracam Multiple Camera Array (MCA) multispectral imagers in port and starboard configurations (117.2° combined field-of-view)
- Six spectral channels: 442, 488, 531, 560, 650, 861 nm—matching Landsat-8 OLI, Sentinel-2 MSI, MODIS, MISR, VIIRS, and Sentinel-3 OLCI
- Incident Light Sensor (ILS) for downwelling radiation measurement
- Dual GPS units, dual IMU navigation units, Field of View geotagging system achieving <2 cm per-pixel geolocation accuracy
- Each channel: 1280×1024 pixels with ~10 cm spatial resolution at 100m altitude

**Platform Integration:**
- Deployed on Black Swift Technologies' SuperSwift airframe (ruggedized s-UAS)
- 10-foot wingspan, 3-piece easy-assemble design, portable ("carry in small sized bag")
- Rapid "plug-and-play" payload installation (<30 minutes between flights)
- Dynamic nose cone design allows variable instrument roll angle (nadir to horizon)
- Operating cost: <$350/flight hour vs. $3,500-4,000/hour for heritage NASA systems (CAR, AirMSPI)
- Successfully completed NASA Airworthiness and Flight Safety Review Board (AFSRB) certification

**Data Processing Pipeline:**
1. Raw DN values converted to reflectance using simultaneous ILS measurements
2. Geolocation correction using onboard GPS, ground control points (GCPs), and IMU navigation data
3. MODTRAN5 radiative transfer calculations for atmospheric correction
4. Retrieval of surface reflectances, BRDF model parameters, and hemispherically integrated albedo
5. Characterization of measurement uncertainties and geolocation errors in metadata

## Products & Capabilities Described

### SuperSwift Platform
- **What it is:** Ruggedized small UAS based on Black Swift's Tempest design, specifically engineered for harsh high-latitude environments
- **Capabilities:** 
  - Meets FAA and Canada Transport rules with full blanket exemption (FAA No. 13967)
  - Supports rapid pre/post-flight calibration (maintains <5% targeted accuracy)
  - "Dynamic pointing" for variable instrument roll angles
  - Minimal logistical footprint compared to manned aircraft
  - Total development investment to date: $1,114,890 (SBIR-funded)
- **Performance in ABoVE context:**
  - Much higher success rate for clear-sky acquisitions vs. manned platforms (heritage systems achieve <30% usable data; SuperSwift/MALIBU expected to overcome this)
  - Cost-effective rapid deployment for multi-angle sampling
  - Enables repeat flights under varying cloud conditions

### MALIBU/SuperSwift Integrated System
- **Spatial resolution:** Sub-meter (<10 cm) multi-angle spectral reflectance
- **Angular resolution:** 0.5 degree
- **Products generated:**
  - High-resolution BRDF/albedo reference datasets (SI-traceable)
  - Spectral surface albedo maps
  - Reflectance anisotropy (BRDF shape) characterization
  - Photosynthesis vegetation indices (PRI, CCI) with angular variations quantified
  - Fire severity assessments and post-fire albedo dynamics
  - Shrub cover and structural metrics

## Use Cases & Applications

**1. Arctic Shrub Encroachment Assessment**
- Nine field sites across Arctic tundra, shrub, and boreal forest (Table 1):
  - M-01: NEON Toolik tundra site (68.661°N, -149.370°W)
  - M-02, M-03: Shrub sites along Dalton Highway transect (foundational ABoVE flight lines)
  - Control pairs of shrub-free and shrub-covered locations
- Quantify albedo changes from vegetation structure and composition shifts
- Evaluate regional climate feedbacks from shrub cover expansion on North Slope of Alaska

**2. Post-Fire Boreal Forest Dynamics**
- Six boreal forest sites (M-04 through M-09) in Saskatchewan, Canada (supplemental ABoVE lines)
- Temporal comparison: mature, 9-year post-fire, and 17-year post-fire conditions
- Characterize albedo recovery and vegetation succession
- Assess fire severity and black carbon deposition effects
- Improve carbon emission modeling at sub-hectare scales

**3. Satellite Product Validation**
- Generate reference BRDF/albedo datasets for validating:
  - MODIS (Terra/Aqua)
  - Sentinel-2 MSI, Sentinel-3 OLCI
  - Landsat-8 OLI
  - MISR (Terra)
  - VIIRS (Suomi-NPP/JPSS)
- Address heterogeneous landscape validation gaps (tower albedometers insufficient)
- Support GCOS Terrestrial Observing Panel on Climate (TOPC) Action 01 and CEOS-WGCV international commitments

**4. Photosynthesis and Light-Use-Efficiency Modeling**
- Expand PRI (Photochemical Reflectance Index) and CCI (Chlorophyll-Carotenoid Index) characterization beyond previous tower-based forest/cropland studies
- Evaluate angular effects on LUE and gross ecosystem production (GEP) estimates
- Improve carbon cycle modeling in rapidly shifting Arctic/boreal climate zones

## Key Research Objectives

**Objective 1: Characterize BRDF/Albedo Scaling Effects**
- Analyze subpixel reflectance anisotropy biases across satellite retrieval geometries
- Quantify interaction between surface BRDF shape and instrument spatial resolution
- Discriminate end-member components: shrub canopy, forest crown, non-woody background, char, moss
- Compare against NEON tower albedometer data at Toolik site
- Document MALIBU measurement uncertainties (radiometric, geolocation) in metadata

**Objective 2: Assess Albedo Impacts from Shrub Encroachment and Fire**
- Analyze spatial scaling within and across post-fire boreal ecosystems
- Conduct radiative forcing analysis at fine scales (<1 ha)
- Generate fire severity assessments improving carbon emission predictions
- Link shrub structure changes to surface energy exchange and permafrost vulnerability

**Objective 3: Evaluate Angular Photosynthesis Index Effects**
- Assess PRI and CCI angular variations across tundra, shrub, and boreal post-fire ecosystems
- Compare airborne multi-angle indices against tower-based LUE/GEP measurements
- Improve utility of long-term satellite records for carbon modeling

## Project Structure

**Team Composition:**
- **PI:** Zhuosen Wang (University of Maryland, ESSIC)
- **Co-Investigators (6):**
  - Miguel O. Román (NASA/GSFC) – institutional PI
  - Crystal B. Schaaf (University of Massachusetts Boston)
  - Mark J. Chopping (Montclair State University)
  - Brendan M. Rogers (Woods Hole Research Center)
  - John A. Gamon (University of Nebraska–Lincoln)
  - **Maciej Stachura (Black Swift Technologies)** – platform development and operations
- **Collaborators (4):** Karl Huemmrich (UMBC), Joel McCorkel (NASA/GSFC), Bin Tan (SSAI), Jill Johnstone (University of Saskatchewan), Syndonia Bret-Harte (University of Alaska Fairbanks)

**Budget ($496,264 total over 3 years):**
- Year 1 (2017): $229,279 (includes $120,350 subcontracts; $19,062 to NASA/GSFC Miguel Roman)
- Year 2 (2018): $144,295 (includes $79,356 subcontracts; $19,689 NASA/GSFC)
- Year 3 (2019-2020): $122,690 (includes $60,686 subcontracts; $20,388 NASA/GSFC)
- Subaward/consortium total: $260,392 (52% of direct costs)
- Primary personnel: 2.4 cal-months/year for PI
- Graduate students: 2 students, 24 student-months total
- Travel: $24,000 total (8 domestic, 6 international)

**Field Campaign Timeline:**
- 9 sites across ABoVE study domain (Alaska North Slope, Saskatchewan boreal)
- Collocated in-situ, tower-based, and terrestrial LiDAR measurements
- Ground control points: Trimble GPS with <3 cm accuracy
- Fiducial reflectance standards: ASD FieldSpec and Spectralon per CEOS IVOS guidelines

## Notable Details

**Innovation & Competitive Advantages:**
1. **First NASA s-UAS with full blanket exemption:** Unique regulatory status for cross-US/Canada operations
2. **Cost efficiency:** <$350/flight hour vs. $3,500-4,000 for manned platforms; solves high-latitude logistics challenges
3. **Unprecedented spatial-angular resolution:** 10 cm spatial, 0.5° angular at <10 cm resolution
4. **Dynamic instrument pointing:** Overcomes high-latitude solar geometry constraints (SZA ~49° at Barrow mid-summer)
5. **Spectral channel alignment:** Matched to 6+ satellite sensors (MODIS, Landsat, Sentinel, MISR, VIIRS, OLCI) for seamless validation
6. **Multi-scale measurement suite:** Integrates in-situ, tower, terrestrial LiDAR, and airborne observations

**International Collaboration:**
- Field campaigns in Canada (Saskatchewan boreal sites)
- University of Saskatchewan collaborator (Jill Johnstone) for coordination
- CEOS international calibration/validation commitments

**Regulatory/Safety Achievement:**
- Completed lengthy NASA AFSRB review (first of its class)
- Test flights at Pawnee National Grasslands (June 2016) with Landsat-8 OLI colocation demonstrated instrument consistency and <2 cm pointing accuracy

**Alignment with ABoVE Science Goals:**
- Directly addresses Tier 2 Science questions on disturbance regimes and ecosystem response
- Contributes to ABoVE Science Objective 1: "Determine how interactions among vegetation, soil, hydrology, and disturbances influence surface energy exchange and permafrost vulnerability"
- Supports broader NASA calibration/validation framework and GCOS essential climate variables

**Data Products & Dissemination:**
- SI-traceable reference BRDF/albedo datasets for global satellite validation
- Publication costs: $3,000 over 3 years
- Will contribute to ABoVE Science Cloud and broader open data ecosystems