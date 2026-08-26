# Marine Atmospheric Boundary-Layer and EM Propagation Characterization for Fleet Operations

## Document Metadata
- Type: White paper / capability proposal (initial redline draft)
- Client/Agency: Naval Undersea Warfare Center (NUWC) Division Newport
- Program/Solicitation: SBIR Phase III sole-source or existing NUWC OTA/CRADA pathways; NISE/Section 219 funding eligible
- Date: 5 August 2026
- BST Products/Systems Referenced: S0 (air-deployed variant), S0-VTOL (ship-launched variant)
- Key Personnel: Jack Elston (last editor); Daniel Pendergast (point of contact); coordination with KrateoSky, Inc.

## Executive Summary
Black Swift proposes to characterize marine atmospheric boundary layer (MABL) structure and electromagnetic propagation conditions for Navy fleet operations using the S0 and S0-VTOL platforms. The capability addresses a critical gap in real-time duct profiling that governs radar and communications performance at sea. Two at-sea data-collection events with algorithm development for evaporation duct height estimation would deliver tactical refractivity products and validate against existing propagation models.

## Technical Approach
- **Primary measurement approach**: Deploy S0 variants to hold 10 m above sea surface for 25 minutes while profiling to 15,000 ft altitude
- **Sensor payload**: Measures pressure, temperature, humidity, and sea-surface temperature (SST) for direct modified refractivity computation
- **Real-time processing**: Ground-station algorithm development for evaporation duct height estimation; real-time downlink enables tactical decision aids compatible with AREPS-class inputs
- **Data validation**: Ground-truth comparison against ship-based reference sensors and propagation model predictions
- **MABL sensor package optimization**: Refinement of sensors for improved refractivity retrieval

## Products & Capabilities Described

### S0 (Air-Deployed Variant)
- **Range**: Communicates to 125 nm
- **Endurance**: Over 100 minutes in severe conditions
- **Demonstrated performance**: Proven operation inside tropical cyclones
- **Cost efficiency**: Expendable-tolerant at fraction of legacy platform cost
- **Measurement capability**: 3-D wind, pressure-temperature-humidity (PTH), and SST at vertical resolution adequate to resolve evaporation duct height

### S0-VTOL (Ship-Launched Variant)
- **Deployment**: Launches and recovers from any deck without launchers or nets
- **Application**: Organic shipboard atmospheric characterization
- **Note**: Recovery to moving deck in ship's air wake listed as undemonstrated (editorial concern in redline)

## Use Cases & Applications
- **Primary mission**: Real-time marine atmospheric boundary layer profiling to support Fleet undersea and surface warfare mission planning
- **Specific application**: Characterizing evaporation duct structure that governs radar and communications range prediction
- **Tactical use**: Providing refractivity products as decision aids for tactical operations (AREPS-class tool inputs)
- **Environment**: Demonstrated capability in tropical cyclones and other severe MABL conditions

## Key Results
This is a proposal rather than a completed study; no experimental results are presented. However, claimed demonstrated results include:
- 125 nm communication range
- 100+ minute endurance in severe conditions
- Tropical cyclone operations (successful)
- Measurement of PTH profiles at vertical resolution required for duct-height resolution

## Notable Details

### Funding and Timing
- **Requested amount**: $1,350,000
- **Budget breakdown**:
  - Aircraft systems & MABL payloads (4 aircraft, mixed variants): $520,000
  - Refractivity retrieval algorithm & real-time product development: $310,000
  - Two at-sea collection events & range coordination: $330,000
  - Validation analysis, data package & concept of employment report: $190,000
- **Period of performance**: 12 months with two at-sea data-collection events
- **Funding source eligibility**: FY26 O&M / FY25–26 RDT&E expiring balances; NISE/219 eligible
- **Award timeline target**: Mid-September 2026

### Critical Editorial Notes (Redline Comments)
The document includes several significant editorial flags from the reviewer (Jack Elston):

1. **Duplicate funding risk**: Conflicts with existing ONR 6.4 subcontract under University of Washington (Sanabia PI, ~$317K BST share) on same measurement topic ("Wx + SST + Atmospheric-Refractivity Survey sUAS") and Navy STTR Phase II N6833525C0270. Direct NUWC award could create duplicate-funding and data-rights issues with multiple Navy sponsors.

2. **Wrong solicitation vehicle**: Proposal references SBIR Phase III but the correct pathway is NUWC Newport Tactical Oceanography CSO (presolicitation issued January 2026, awards in FY26-27 prototyping windows). NAVAIR N251-016 LAU-126A integration cited as credibility anchor.

3. **Unresolved technical risks asserted as demonstrated**:
   - Evaporation duct height resolution claimed as demonstrated but listed as "open" in BST risk register
   - Duct heights typically 5-25 m; requires humidity response time resolution within first few meters of surface
   - ONR proposal rates humidity response time and salt accumulation in marine boundary layer as "Medium/Medium unresolved" with possible heated/ventilated mount fix in Year 2
   - Recommendation: "Soften this or we get caught on it"

4. **VTOL recovery capability overstated**: Claim that S0-VTOL recovers from "any deck" is flagged as problematic. Recovery to moving deck in ship's air wake not yet demonstrated (same concern noted in WP-3).

5. **Scope reframing recommendation**: Editor recommends rescoping from second measurement campaign to software integration focused on formatting native pressure/temperature/relative humidity profile output for AREPS-class radar-propagation and EM battle-management tools. Rationale: "Low-cost decision-aid layer on top of measurements two other Navy programs are already paying for, and it is defensible in front of all three sponsors."

### Data Rights
- Deliverable includes data package with Government Purpose Rights on collected data
- SBIR Phase III pathway preserves BST's data rights

### Related Programs
- ONR 6.4 subcontract (Sanabia PI): Wx + SST + Atmospheric-Refractivity Survey sUAS, ~$317K BST share, 3-year duration
- Navy STTR Phase II N6833525C0270: Funds wave-state filter and onboard compute referenced in this proposal
- NAVAIR N251-016 LAU-126A integration: Cited as credibility anchor for shipboard launch capability

---

**DOCUMENT STATUS NOTE**: This is a draft redline with substantial unresolved editorial concerns. The document presents both the proposal content and critical internal reviewer comments identifying funding conflicts, overstated capability claims, and recommended scope adjustments. It does not represent final BST position on this opportunity.