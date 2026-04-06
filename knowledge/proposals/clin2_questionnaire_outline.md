# CLIN2 Questionnaire Outline - AFWERX SBIR Phase I Final Report

## Document Metadata
- Type: SBIR Phase I Final Report Questionnaire Outline
- Client/Agency: U.S. Air Force Research Laboratory (AFRL), Air Force Special Operations Command (AFSOC)
- Program/Solicitation: AFWERX Open Topic Phase I; Contract FA864923P0168; Proposal FX224-OCSO1-0531
- Date: November 4, 2022
- BST Products/Systems Referenced: S2 (fixed-wing UAS), E2 (multirotor UAS), SwiftCore Flight Management System, Lobe Differencing Correlating Radiometer (LDCR) soil moisture sensor, Tempest UAS
- Key Personnel: Dr. Jack S. Elston (CEO/Co-founder, US), Dr. Maciej Stachura (CAN), Ben Busby (US), Josh Fromm (US)

## Executive Summary
Black Swift Technologies proposes adapting its patented soil moisture mapping sensor technology—already commercialized for NASA and NOAA—to create a rapid, high-resolution soil integrity assessment system for USAF runway validation and landing zone operations. The soil moisture data will be collected via small unmanned aerial systems (S2 fixed-wing or E2 multirotor platforms) to enable global reach and reduce operational risk by eliminating the need for personnel-based ground measurements.

## Technical Approach

**Core Technology:** Lobe Differencing Correlating Radiometer (LDCR) operating at L-band frequencies
- Measures soil moisture with 5-7cm sensing depth
- Already proven in operational deployments for NASA, NOAA, USGS, and commercial clients
- Will be integrated into BST UAS platforms for autonomous aerial mapping

**Phase I Focus:**
- Customer discovery and technical discussions with AFRL researchers
- Assessed how soil moisture mapping compares to alternative methods: electromagnetic induction (EMI), capacitive resistivity imaging (CRI), ground penetrating radar (GPR), and time domain electromagnetic (TDEM)
- Engaged with 16 individuals/groups; conducted meetings with 6 DAF organizations to define solutions and necessary adaptations
- Established that soil moisture + known soil type = cone index (soil integrity metric currently measured manually on ground)

**Phase II Plan (intended):**
- Validate and iterate the soil moisture sensor for soil integrity mapping application
- Develop processing software to convert soil moisture measurements into cone index equivalent
- Test at AFRL's calibrated test site at University of Rouen
- Integrate data products with Air Force command and control systems

**Technology Readiness Level:** TRL 3 for soil integrity mapping capability (soil moisture sensor itself is TRL 6-7 with proven operations)

## Products & Capabilities Described

### S2 UAS (Fixed-Wing)
- Purpose: High-altitude, large-area soil moisture mapping
- Payload: LDCR soil moisture sensor
- Application: Mapping larger runway/landing zone areas
- Custom design developed to accommodate sensor integration

### E2 UAS (Multirotor)
- Purpose: Lower-altitude, smaller-area soil moisture mapping
- Payload: LDCR soil moisture sensor
- Application: Focused surveys of specific landing zones
- Custom design developed to accommodate sensor integration

### LDCR Soil Moisture Sensor
- Specification: L-band radiometer with 5-7cm sensing depth
- Status: Patented; previously deployed for USGS, NASA, NOAA missions
- Commercial applications: Already sold to USGS (Pepperwood, CA; Crested Butte, CO), University of Colorado, Western Colorado University, University of Virginia
- Defense adaptation: Will add specialized processing software layer to produce soil integrity maps for runway evaluation

### SwiftCore Flight Management System
- Advanced autopilot system developed by Dr. Elston
- Enables autonomous UAS operations needed for rapid deployment
- Supports complex flight patterns for systematic area coverage

## Use Cases & Applications

**Primary Defense Use Case: Runway Integrity Validation**
- Enable C-130 aircraft to land safely on unimproved/unconventional runways globally
- Reduce personnel risk by eliminating ground-based cone penetrometer surveys
- Enable Air Mobility Command operations in forward/austere locations
- Application: ~300 C-130s in current USAF inventory

**Broader Military Applications:**
- Landing zone suitability assessment in potentially unstable terrain (river valleys, wetlands, coastal regions)
- Support for ground vehicle movement in challenging environments
- Operations in areas susceptible to heavy precipitation/flooding

**Commercial Dual-Use Applications:**
- Construction site assessment for wind/solar farm development (discussions with RES Group, world's largest independent renewable energy company)
- Water resource management and river basin hydrology (ongoing with USGS, University of Colorado)
- Environmental monitoring (NASA, NOAA partnership continuation)
- Agricultural applications (existing BST commercial service)

## Key Results

**Phase I Achievements:**
- Confirmed DAF need for remote soil integrity sensing to replace manual ground measurements
- Established technical feasibility: soil moisture + soil type = cone index (documented in literature)
- Secured verbal commitment for signed MOU from Paul Fleitz (AFRL/RQQC)
- Identified AFRL's 6-year effort to solve this problem using various remote sensing technologies
- Generated $302,749 in commercial revenue (past 12 months) from soil moisture mapping services:
  - USGS Pepperwood, CA: $63,117
  - University of Colorado/Crested Butte, CO basin study: $84,329
  - Western Colorado University: $5,303
  - University of Virginia (complete SMM package sale): $150,000

**Customer Validation:**
- AFRL stakeholders ready and willing to participate in Phase II work plan
- AFRL offering use of test sites for technology validation
- No other viable remote sensing alternatives currently on market; competitors still in development phase

## Notable Details

**Company History & Credentials:**
- Founded: 2011
- Dr. Elston (CEO/Co-founder) background:
  - Ph.D. from CU Boulder on tornado-sampling UAS networks (Tempest system)
  - NSF Postdoctoral Fellowship for in-situ atmospheric sampling with UAS
  - Led first-ever intercept of tornadic supercell by unmanned aircraft (VORTEX2 project, NSF/NOAA funded)
  - 100+ COA applications authored; hundreds of flight experiments conducted including Arctic deployments
  - Currently PI on NOAA Phase II SBIR (tube-launched aircraft for hurricane sampling) and NASA Phase II SBIR (Venus upper-atmosphere glider via dynamic soaring)
  - Technical lead on all BST avionics and SwiftCore autopilot development

**Commercialization Track Record:**
- Successfully commercialized two generations of autopilots
- Developed four different airframe types (multirotor, fixed-wing, VTOL)
- Active in accelerator programs: Capital Factory (Austin), Blackstone Entrepreneurial Network (Colorado), Global Energy Mentors (Houston, oil/gas focus), Larta (climate monitoring)
- Previous expansion into methane detection based on volcano monitoring work

**Dual-Use Strategy:**
- Commercial and defense versions will differ only in processing software/data interfaces
- Plan to eventually push defense enhancements back into commercial system to expand into construction/other markets
- Same production/manufacturing pipeline for both variants

**Identified Technical Risks & Mitigation:**
1. **Measurement accuracy across soil types/environments:** Extensive S2/E2 testing in various climates; modifications possible
2. **Sensor integration on current UAS:** Custom design flexibility; BST designs both instrument and platforms
3. **Sensing depth adequacy:** L-band provides 5-7cm; can convert to P-band (>30cm depth) or use depth-estimation models if needed
4. **Air deployment requirement:** BST has smaller air-deployable UAS (from P3 Orion); can be adapted with additional effort

**Regulatory/Operational:**
- Currently operating under FAA Part 107; sufficient for Phase II work
- Schedule includes margin for additional AF approval requirements
- No flight certification, ATO, or hazmat anticipated beyond current UAS operations

**Competitive Position:**
- No currently viable remote sensing alternatives; only manual ground surveys with personnel
- First-to-market advantage if Phase II/III successfully completed
- Competitors (EMI, GPR, TDEM methods) still in development phase

**Path to Production:**
- Phase II: Prototype development and validation (1 year)
- Phase III (planned): Sole-source SBIR to adapt prototype and prepare for procurement
- Integration with C-130 operations and Air Mobility Command procurement expected post-Phase III

**Commercial Market Scope:**
- ~300 C-130s addressable; potential expansion to other DOD aircraft/vehicles
- Global runway operations market
- Renewable energy construction (wind/solar farms)
- Water resource management
- Agricultural monitoring
- Environmental research

**Funding & Business Development:**
- No prior funding rounds completed
- Interested in STRATFI/TACFI follow-on funding
- Investigating private/third-party investment opportunities
- Angel and venture capital firms have been pitched; receptive feedback
- Phase II funding believed sufficient to bring to market

**Program Experience Feedback:**
- Appreciated weekly calls and transparency on processes
- Requested simplified submission process for small businesses
- Suggested more warm introductions between SBIR/STTR program staff and DoD stakeholders
- Identified barrier: difficulty engaging DoD stakeholders with adequate authority and commitment
- Program rating: 4/5