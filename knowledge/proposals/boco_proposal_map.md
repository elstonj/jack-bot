# UAV Multispectral Vegetation Mapping for Fire Fuel Models (BOCO Proposal)

## Document Metadata
- Type: Research proposal
- Client/Agency: Boulder County Parks and Open Space (primary); HSI Geo / Black Swift Technologies collaboration
- Program/Solicitation: Not specified (appears to be unsolicited/custom proposal)
- Date: January 15, 2018
- BST Products/Systems Referenced: S1 (fixed-wing UAV), SwiftCore (ground station/flight management system)
- Key Personnel: Jack Elston, Ph.D. (Founder and CEO, BST); Maciej Stachura, Ph.D. (Founder and CTO, BST); Joe Zamudio, Ph.D. (Remote Sensing Consultant, HSI Geo)

## Executive Summary
This proposal describes a research project to develop and validate UAV-based multispectral imagery for accurate mapping of wildfire fuel parameters in a Ponderosa Pine–Douglas Fir forest in Boulder County, Colorado. The project combines multispectral and RGB imagery collected by a Black Swift S1 UAV to generate 3D point clouds and vegetation classifications that can feed into wildfire behavior models (FARSITE) and emissions models (FOFEM), enabling land managers to make better fuel management and fire prediction decisions.

## Technical Approach

**Data Collection:**
- Fixed-wing UAV (Black Swift S1) equipped with 5-band multispectral sensor (MicaSense RedEdge) plus RGB camera
- Flights over two potential areas: Riverside Ranch (primary, ~640 acres) in northern Boulder County and a previously burned area in southern Boulder County
- High spatial resolution: ~3 cm/pixel for RGB; lower GSD for multispectral
- Imagery collection near local solar noon under cloudless skies to maximize signal strength
- Separate flights for RGB and multispectral data
- Field spectrometer (ASD FieldSpec) to collect reflectance measurements of ground vegetation for calibration

**Data Processing:**
- Mosaicking with Pix4D software (includes radiometric and atmospheric correction to convert radiance to reflectance)
- Image analysis with ENVI software including:
  - Vegetation index calculations
  - Principal component analysis
  - Supervised classification
  - Feature extraction
- Production of 3D point clouds from photogrammetric processing of multi-perspective imagery
- Vegetation species mapping output (grass, shrubs, trees)

**Validation:**
- Field spectrometer measurements to calibrate imagery
- Field visits to evaluate classification accuracy

## Products & Capabilities Described

### Black Swift S1 UAV
- Fixed-wing platform
- 1-hour flight time
- Considerably quieter than multi-copters
- Capable of covering 640 acres at ~3 cm/pixel with RGB camera in single flight
- Can carry multiple sensor payloads (multispectral and RGB)

### SwiftCore Flight Management System
- Ground station for UAV flight control

### MicaSense RedEdge Multispectral Sensor
- 5-band sensor
- Includes vegetation red edge capability
- Used to map vegetation types and discriminate fuel groups

## Use Cases & Applications

**Primary Application: Wildfire Fuel Mapping**
- Map primary fuel groups: grass, shrubs, trees
- Determine secondary fuel parameters from 3D point clouds:
  - Tree density, size, canopy closure, height, species
  - Canopy height, canopy bulk density, available canopy fuel
- Generate spatially explicit fuel layers for input into:
  - FARSITE (wildfire behavior model)
  - FOFEM (fire emissions model)

**End User Benefits:**
- Enable land managers to make smart fuel management decisions
- Improve fire behavior prediction capabilities
- More accurate crown fire risk assessment
- More accurate smoke emission predictions

## Key Results
No results reported; this is a proposal for work to be conducted. Project schedule specified:
- UAV data collection: Spring 2018
- Field accuracy checks: Late summer 2018
- Final report delivery: Before December 9, 2018

## Project Location & Scope

**Primary Study Area: Riverside Ranch**
- Located in northern Boulder County, approximately 5 miles west of Lyons and 1.5 miles north of Highway 7
- Approximately 640 acres
- Elevation: 6,600'–8,000'
- Vegetation: Ponderosa Pine–Douglas Fir forest
- Remote location with minimal visitation expected

**Secondary Area (if funds/time allow):**
- Previously burned area in southern Boulder County (location pending)

**Timing Rationale:**
- Spring collection: Maximizes phenological differences between species, improving species differentiation accuracy
- Late summer collection (if feasible): Captures additional phenological differences

## Notable Details

**Hypotheses & Innovation Claims:**
- High spatial resolution UAV multispectral imagery should provide more precise species and fuel maps than satellite data
- UAV-derived point clouds from photogrammetry can compete with lidar-derived point clouds for 3D vegetation metrics
- Finer spatial resolution should enable accurate quantification of vegetation metrics critical to fuel models

**Budget Summary:**
- Total project cost: $8,600
- Equipment already procured (S1 UAV, SwiftCore, ASD FieldSpec)
- New software subscriptions: Pix4D ($700/month), ENVI
- Labor: Field work ($3,000), mosaicking ($400), image analysis ($4,800), report writing ($400)

**Regulatory/Permitting Requirements:**
- UAS Authorization Application required for flying over Boulder County Open Space
- Research Permit required for work on county open space

**Collaboration:**
- Partnership between Black Swift Technologies (UAV platform and operations) and HSI Geo/Joe Zamudio (remote sensing expertise and analysis)

**Notable Document Issues:**
- Multiple editorial notes embedded (marked with [a]–[f]), indicating this is a draft or working document
- Several incomplete sentences and pending details (e.g., "finish sentence" at [f])
- Questions about equipment choices and survey logistics (landing sites, sensor specifications)