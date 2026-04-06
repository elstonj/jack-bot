# End-to-End Soil Integrity Measurement System

## Document Metadata
- Type: Technical proposal / RFI response
- Client/Agency: U.S. Army
- Program/Solicitation: ARMY25-COE02
- Date: April 30 – May 3, 2016
- BST Products/Systems Referenced: Soil Moisture Mapping (SMM) Small Unmanned Aircraft System (sUAS); SuperSwift aircraft
- Key Personnel: Dr. Maciej Stachura (PI), Dr. Cory Dixon (BST, SuperSwift integration lead); Partners: Prof. Albin J. Gasiewski (University of Colorado CET, sensor technical lead), Prof. Venkat Lakshmi (University of South Carolina, soil integrity algorithms)

## Executive Summary
Black Swift Technologies proposes to adapt its existing NASA-developed Soil Moisture Mapping sUAS platform into an end-to-end soil integrity measurement system for the U.S. Army. The system combines an airborne L-band radiometer with soil integrity processing software to provide low-latency soil moisture and trafficability assessments at 15-meter spatial resolution to ~10 cm depth, enabling Army personnel to evaluate terrain suitability for heavy vehicle trafficking and aircraft landing operations.

## Technical Approach

**Core System Architecture:**
- Leverages the existing SMM sUAS (developed under NASA Phase II SBIR) as primary data source
- Integrates soil moisture measurements with soil type data and soil integrity algorithms to produce permissible vehicle tire pressure assessments
- Incorporates state-of-the-art RF interference (RFI) mitigation via digital detecting and processing receiver technology
- Uses SuperSwift airframe (radio-quiet aircraft design) necessary for robust radiometer performance

**Key Technical Tasks:**

1. **Aircraft/sUAS Modifications:**
   - Ruggedization of airframe and support equipment for Army field operations
   - Adoption of wireless communication system for control and data downlink on approved DoD frequencies with encryption
   - Development of third-generation sensor electronics using mil-spec components
   - Enhanced RFI/EMI mitigation for reliable operations in difficult environments
   - Local flight testing throughout project to validate modifications

2. **Software Development:**
   - Soil integrity processing algorithms to convert soil moisture + soil type into maximum permissible surface soil pressure data products
   - Integration of antecedent rainfall and drying data
   - Formatting of outputs for existing Army data systems
   - Ground control station ruggedization and redesign
   - Algorithm refinement using local flight test data

**Validation Approach:**
- Local flight experiments at Irrigation Research Fund (IRF) test site, Yuma, Colorado (existing BST FAA authorization)
- Final demonstration and evaluation at Army Corps of Engineers ERDC Environmental Laboratory, Vicksburg, Mississippi
- Army personnel feedback incorporated into final modifications

## Products & Capabilities Described

**Soil Moisture Mapping (SMM) sUAS:**
- Existing platform developed in collaboration with University of Colorado CET under NASA Phase II SBIR
- High-resolution L-band radiometer (currently used in precision agriculture applications)
- Measurement capability: 15-meter spatial resolution, ~10 cm soil depth penetration
- Current TRL: 7; expected TRL 8 by fall 2016
- Already validated against in situ sensors and NASA calibration sites
- Demonstrated soil moisture mapping at 30-meter resolution (example: Canton, OK)

**SuperSwift Aircraft:**
- Radio-quiet airframe design essential for radiometer performance
- Will be modified for Army operational requirements
- Integration point for ruggedized third-generation sensor electronics

**Soil Integrity Data Product:**
- Measures permissible vehicle tire pressure thresholds
- Relates soil moisture to soil strength based on soil type
- Incorporates temporal rainfall/drying factors
- Provides low-latency operational decision support

## Use Cases & Applications

**Primary Army Applications:**
- Heavy vehicle trafficking assessment over varied terrain
- Aircraft landing zone suitability evaluation
- Operations in unstable/high-risk terrain: river valleys, wetlands, coastal regions
- Post-precipitation terrain assessment (thunderstorm/heavy rainfall scenarios)
- Pavement integrity assessment (soil foundation stability under vehicular loads)

**Technical Rationale:**
The system addresses critical gaps in existing soil moisture assessment methods:
- *In situ probes:* Impractical for Army field operations
- *Satellite sensors (e.g., SMAP):* Insufficient spatial resolution (km-scale vs. sub-100m Army requirement) and temporal frequency (2x/day vs. rapidly changing soil conditions)

The spatial heterogeneity of soil moisture directly determines soil strength and vehicle load-bearing capacity—only achievable at the high spatial resolution provided by the SMM sUAS.

## Key Results
No results reported; this is a proposal document. The document references prior validation:
- SMM sUAS successfully flight-tested at NASA calibration site
- Extensive in situ sensor comparison completed
- Phase II-E ongoing validation over different vegetation densities at Yuma, Colorado test site
- Soil moisture maps generated at 30-meter resolution in Canton, Oklahoma

## Notable Details

**Technology Readiness:**
- SMM sUAS: TRL 7 (TRL 8 expected by fall 2016)
- Soil integrity system overall: TRL 5
- Proposed project goal: Advance complete system to TRL 7 and position for Army TRL 8-9 qualification

**Institutional Partnerships:**
- University of Colorado Center for Environmental Technology (Prof. Gasiewski): sensor development, 64 competitively awarded environmental remote sensing projects
- University of South Carolina (Prof. Lakshmi): soil integrity algorithm development
- Leptron Unmanned Systems: identified as potential partner for DoD certification and approval pathway
- Army Corps of Engineers ERDC: proposed test/demonstration site

**Facilities:**
- BST facility: 6,700 sq ft in Boulder, Colorado with prototyping, simulation, testing, and manufacturing capability
- CET facility access at University of Colorado for radiometric/radar sensing equipment
- Existing FAA authorization for UAS operations at IRF Yuma test site

**Budget & Schedule:**
- 2-year effort; $2,463,800 total budget
  - BST: ~$1,963,800
  - University of Colorado CET (Gasiewski, PhD student, equipment): $250K
  - University of South Carolina (Lakshmi, PhD student, equipment): $250K
- Milestones: System PDR, Year 1 report (acts as CDR), Army facility flight operations, final report
- Risk mitigation through frequent local testing prior to Army facility deployment

**Competitive Advantages:**
- Unique high-spatial-resolution radiometer capability already mature and tested
- Radio-quiet aircraft design specifically engineered for radiometer performance
- Existing collaboration structure and validated partnerships
- Prior DoD experience (Dr. Dixon's two Phase II SBIR programs)
- Ready-to-transition technology reducing Army acquisition risk