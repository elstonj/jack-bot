# Flux Maps for Unmanned Aircraft System - Statement of Work

## Document Metadata
- **Type:** Statement of Work (contract/service agreement)
- **Client/Agency:** Black Swift Technologies (BST)
- **Program/Solicitation:** Not specified in document (context indicates NSF CO WY Climate Engine / methane measurement translation work)
- **Date:** November 13, 2023 (signed by AtmoFacts); Period of Performance: November 15, 2023 - February 29, 2024
- **BST Products/Systems Referenced:** Unmanned Aircraft System (UAS) with eddy-covariance (EC) sensors for methane measurement
- **Key Personnel:** 
  - AtmoFacts: Stefan Metzger (Manager, smetzger@fluxmapper.com)
  - BST: Jack Elston (CEO)

## Executive Summary
AtmoFacts (AF) agreed to develop independent Flux Mapper (FM) software and conduct contract research for Black Swift Technologies to convert BST's UAS eddy-covariance methane measurement data into quantified emissions flux maps. The 3.5-month engagement progresses from basic data ingest and compatibility verification (Phase 1), through dependent flux maps calibrated to known controlled releases (Phase 2), to fully independent flux maps with specified accuracy targets (Phase 3), with BST committing to purchase 100 flux map scenes post-development.

## Technical Approach

### Flux Mapping Methodology
- **Core technique:** Eddy-covariance (EC) method applied to UAS airborne data
- **Data products:** CH₄ flux space series and surface influence maps derived along UAS flight tracks
- **Visualization:** From qualitative heat maps → dependent quantified maps → independent quantified maps
- **Processing output format:** NetCDF files containing base flux maps

### Three-Phase Development Structure

**Phase 1: Data Ingest & Interoperability**
- Develop BST data ingest script for UAS EC data in NetCDF format
- Reanalyze two existing datasets: Sodfarm20230530 and PDCE20230726
- Validate compatibility with previous analysis by Battelle
- Deliver product visualizations and compatibility metrics

**Phase 2: Dependent Quantification (Two Sub-phases)**
- Phase 2a: Calibrate qualitative emissions heat map using measured 100 SCFM controlled release rate at Sod Farm to create dependent base Flux Map showing estimated emission quantities
- Phase 2b: Design follow-on flight mission, conduct Release-Follow-On measurement capturing complementary surface conditions; produce qualitative heat maps and dependent quantified flux maps

**Phase 3: Independent Quantification (Two Sub-phases)**
- Phase 3a: Address uncertainty sources and develop independent mapping capability:
  - Determine surface flow rates from measured fluxes (currently ±100% uncertainty)
  - Characterize uncertainty as function of CH₄ sample size (currently ±50% uncertainty)
  - Quantify and correct spectral loss related to CH₄ sampling rate (currently ±25% uncertainty)
  - Recommend higher-frequency CH₄ sensor with quantified uncertainty reduction and ROI analysis
  - Design Additional-Quantification flight mission
  
- Phase 3b: Generate independent base flux maps from all three datasets (Sodfarm, PDCE, Release-Follow-On) meeting specifications; establish flight parameter scaling relationships

### Key Specifications for Independent Flux Maps
- **Spatial resolution:** 10 m × 10 m pixel size
- **Detection limit:** 10 SCFH (standard cubic feet per hour)
- **Accuracy:** <±25% error rate
- **Confidence level:** >85%
- **Data format:** NetCDF

### Data Input Requirements
BST UAS must provide for each dataset:
- **Minimum flight data:** 5-20 flight legs per dataset; each leg ≥2 km long with ≥100 one-Hz data points at nominal 20 m/s airspeed
- **Avionics data (≥1 Hz):** UTC time, UTM coordinates (Easting, Northing, Altitude), heading, airspeed, ground speed
- **Meteorology data (same resolution, time-synchronized, lever-compensated):** Wind vector (ENU convention), static pressure, temperature, water vapor, CH₄ mole fraction; optionally boundary layer depth
- **Emission target metadata:** Location, altitude, surface elevation in UTM; optionally canopy/building height

## Products & Capabilities Described

### Black Swift Technologies UAS System
- **Configuration:** Unmanned aircraft equipped with eddy-covariance sensors for simultaneous measurement of wind components and methane concentration
- **Operational profile:** Conducts linear flight tracks downwind and perpendicular to prevailing wind direction
- **Data output:** High-frequency (≥1 Hz) synchronized avionics, meteorology, and trace gas measurements in standard formats (NetCDF, HDF5, CSV, ASCII)
- **Typical measurement altitude:** Variable (flight design parameters to be established)

### AtmoFacts Flux Mapper Software (Independent Version)
- **Status at contract start:** Under development; development contingent on receiving ≥$15,000 in startup funding
- **Architecture:** 
  - Part 1 of 2 software developed by Dec 5, 2023
  - Part 2 of 2 developed by Dec 24, 2023
- **Capabilities progression:**
  - Data ingest and processing for BST UAS EC data
  - Qualitative heat map generation
  - Dependent flux map quantification (calibrated to known release rates)
  - Independent flux map generation (not requiring known release calibration)
  - Support for convolution and deconvolution data integration

### Flux Map Scene Definition
- **Definition:** Spatial area and time period captured in single map for one flux species (CH₄)
- **Scope determined by:** UAS measurement height, wind speed, wind direction
- **Temporal representation:** Snapshot at specific date/time; multiple scenes track changes over time
- **Processing assumption:** Up to 5 flight legs per scene; additional legs priced proportionally

## Use Cases & Applications

### Primary Application: Methane Emissions Quantification
- **Methane leak detection and quantification** from oil/gas/coal mining, production, and transport operations
- **Sector focus:** Mining, production, transport of oil/gas/coal (explicitly included in Limited Exclusivity terms)

### Measurement Scenarios
1. **Sod Farm:** Controlled release environment (100 SCFM calibration source) for algorithm development and validation
2. **PDCE (Pawnee Deciduous Coniferous Ecosystem?):** Real-world emissions measurement site
3. **Release-Follow-On:** Planned controlled release mission complementary to PDCE conditions
4. **Additional-Quantification:** Specialized flight design to address remaining uncertainty sources

### Mission Types
- **Downwind transects:** Linear passes perpendicular to wind direction to capture emissions plume
- **Multi-leg surveys:** 5-20 flight legs per scene to characterize spatial and temporal variability
- **Altitude variation studies:** Flight design scaling relationships to optimize ground resolution vs. sensitivity vs. accuracy trade-offs

## Key Results
**Not applicable—this is a Statement of Work, not a results report.** The document outlines planned deliverables with target delivery dates from January 14 through February 29, 2024, but the engagement was not completed within the document's timeframe.

**Note on project status:** The document location indicates this was part of "2024 Translation no-go" folder, suggesting the project did not proceed as planned.

## Notable Details

### Funding & Commercial Structure
- **Total contract value:** $76,500
- **Startup funding mechanism:** AF requires ≥$15,000 from Limited Exclusivity and Limited Rebate purchases to commence work
  - **Limited Exclusivity:** $10,000 for exclusive rights to FM for specific combination of location (North America), duration (1 year renewable), platforms (UAS, manned aircraft), species (CH₄), version (base maps), sector (oil/gas/coal), provisioning (as-a-service), license tier (for-profit/private data)
  - **Limited Rebate:** $5,000 for 25% discount on future purchases (up to $6,250 savings)
  
- **Service phases cost:** $27,850 fixed-firm-price + $2,900 potential performance bonus for early delivery
- **Purchase commitment:** BST commits to buy minimum 100 "scenes" at $370/scene within 365 days of Phase 3b completion ($37,000 minimum)

### Performance Risk & Contingencies
- **Phase 3 payment structure:** 75% of FFP paid upon delivery; 25% "Holdback Amount" withheld pending AF's proof of independent map specifications or documented evidence that UAS data limitations (not AF software deficiencies) prevented achievement
- **Amendment process if specs not met:**
  - If AF software shortfall: AF provides up to $18,500 free labor at $146.25/hr to meet specs
  - If BST UAS data shortfall: BST pays AF up to $18,500 at $146.25/hr for diagnostic support
  - Shortfalls attributed proportionally to both parties determine scaled hourly rate
  - If specs remain unmet after amendments, purchase commitment of 100 scenes waived
- **Early delivery bonus:** $1,450 bonus for Phase 3a (by Feb 25) and Phase 3b (by Feb 29)

### Intellectual Property & Licensing
- **AF retains ownership** of all IP in independent FM software and general methodologies
- **AF licensing rights:** AF retains right to reuse general knowledge/systems from Phase 1-3 with other clients and for promotional/educational use of aggregate data and visualizations
- **License tiers offered (affecting pricing):**
  - **Application:** Cost-Recoverable (government grant funded only), Non-Profit (501(c)(3)), For-Profit (excluding defense)
  - **Data:** Private Data (internal/aggregate public only), Public Data (quantitative distribution permitted)
  - **Preferred pricing:** BST receives $146.25/hr rate for all work with private data license in recognition of anchor investment role
- **Standard hourly rates:** Range from $146.25/hr (cost-recoverable/private) to $351.00/hr (for-profit/public)

### Payment Terms & Timeline
- **Startup funding:** Due by November 1, 2023; any delays push entire timeline proportionally
- **Phase payments:** Net 15 terms
- **IP Contingency:** AF may withdraw before November 15, 2023 if third-party IP claims/licensing agreements emerge affecting FM software delivery; AF refunds all startup funds within 15 days with no further obligation
- **Unused scene credits:** If purchase falls short of 100 within 365 days, unused paid scenes become credit through 730 days post-Phase 3b
- **Severance option:** If BST waives 100-scene commitment after specs met, BST pays 40% of remaining unused scenes (max $14,800)

### Operational Details
- **Weekly coordination:** 30-minute progress/coordination meetings during performance period
- **Documentation support:** AF provides interpretation assistance for delivered products
- **Follow-on recommendations:** AF to advise on CH₄ sensor integration, operationalization of map generation, and next-generation FM development
- **Delivery timeline:** Compressed 3.5-month schedule with holidays accommodated (Dec 25-Jan 7, 2024)
- **Flexibility:** Delivery dates adjustable in writing by mutual agreement for unforeseen circumstances

### Competitive/Strategic Context
- **Founding Partner model:** Startup-stage commercialization structure offering early backers exclusivity and rebate benefits in exchange for capital to accelerate software development
- **Anchor investment recognition:** BST positioned as key early partner validating FM technology with real UAS data
- **Multi-platform vision:** AF designed system to scale beyond UAS to manned aircraft, towers, buoys, vessels for multiple flux species (CH₄, CO₂, H₂O, heat)
- **Sector expansion potential:** Exclusive rights offered for multiple sectors beyond oil/gas (agriculture, forestry, waste/landfill, energy, transportation, industry)