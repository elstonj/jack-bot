# Phase II Proposal Checklist – NASA SBIR Wildfire Topic

## Document Metadata
- **Type:** Phase II SBIR Proposal Checklist (working document/planning outline)
- **Client/Agency:** NASA
- **Program/Solicitation:** 2023 NASA SBIR – Wildland Firefighting (Phase II)
- **Date:** Created 2024-01-24; Modified 2024-02-02
- **BST Products/Systems Referenced:** S0 VTOL UAS, Team Awareness Kit (TAK) plugin
- **Key Personnel:** Jack, Maciej, Josh, James, Alex, Ed
- **Partners:** NCAR (National Center for Atmospheric Research), Colorado Center of Excellence for Advanced Technology Aerial Firefighting (CoE), FireSense, ACERO

## Executive Summary
This is an internal proposal planning checklist for Black Swift Technologies' Phase II SBIR submission to NASA focused on wildland firefighting operations. The proposal aims to operationalize the S0 VTOL UAS for real-time atmospheric data collection and forecasting around active fires, develop automated UAS site-selection tools, integrate meteorological products into the TAK platform for incident commanders, and conduct multi-UAS demonstrations in prescribed burns and active wildfire conditions.

## Technical Approach

### Core Technical Objectives (4 objectives):

**Objective 1: Improved Fire Weather Forecasting**
- Collect atmospheric data in critical locations around fires
- Assimilate data to generate accurate predictions of wind maps and evolution
- Provide enhanced decision-support for incident commanders on resource deployment

**Objective 2: Automated UAS Deployment Site Selection**
- Develop multi-modal automated tool to select optimal UAS flight locations
- Build on Phase I Ensemble Sensitivity Analysis (ESA) and Observing System Experiment (OSE) methods
- Optimize based on: impact on weather forecasts, airspace coordination, communications availability, reachability by operators
- Goal: reduce operator workload and enable rapid, efficient UAS asset dispersal

**Objective 3: End-to-End Data Infrastructure & Integration**
- Develop BST plugin for Team Awareness Kit (TAK) ecosystem
- Integrate aircraft flight information for situational awareness
- Generate and overlay improved wind forecast maps in real-time
- Establish data dissemination pathways to incident commanders
- Enable immediate over-the-air transfer of flight data
- Provide cloud-based and TAK-based delivery mechanisms

**Objective 4: Field Validation in Active Fire Conditions**
- Conduct multiple UAS flight operations in and around prescribed burns
- Validate S0 VTOL flight and sampling capabilities in fire weather
- Demonstrate near real-time wind product collection and dissemination
- Prove decision-support value for ground crew and manned aircraft safety

### Work Plan (10 Tasks):

1. **Task 1: Automating UAS Deployment Strategies** – Generate multi-modal automated site-selection method; refine ESA/OSE for minimal human workload
2. **Task 2: S0 VTOL Finalization & Validation** – Document design updates, conduct flight safety review, complete field-ready configuration
3. **Task 3: Ground Station Hardware Development** – Enable immediate over-the-air transfer of flight data and interfacing with fire operations
4. **Task 4: Multi-UAS & Meteorological TAK Integration** – Develop comprehensive BST TAK/COTAK/WFTAK plugin
5. **Task 5: Large-Area Forecasting Improvements Assessment** – Demonstrate concrete evidence of forecast improvements in isolated, sensitive terrain vs. existing methods
6. **Task 6: Modeling Output Framework Integration** – Ensure new outputs deliver products to incident commanders (cloud-based and TAK platforms)
7. **Task 7: End-to-End Complete Run** – Conduct realistic-timeline data collection and dissemination demonstration in meteorologically significant location
8. **Task 8: Multi-UAS Active Fire Deployments** – Operate in fire conditions and coordinate with fire teams
9. **Task 9: Commercial Interest Establishment** – Secure S0 VTOL purchase commitments; expand fire agency relationships and airspace permissions
10. **Task 10: Reports** – Prepare and submit required documentation

## Products & Capabilities Described

### S0 VTOL UAS
- **What it is:** Black Swift's vertical take-off and landing unmanned aircraft system
- **Phase I achievements:** Demonstrated capability in rough winds (Hurricane Tammy); proven weather data recording capability
- **Proposed Phase II use:** Primary platform for fire weather data collection; field-ready design updates and validation; demonstrations in prescribed burns and active wildfires
- **Design updates:** Pending completion of design finalization and Flight Safety Review documentation
- **Target TRL:** Level 7 by Phase II close

### Team Awareness Kit (TAK) Plugin
- **What it is:** Integration tool for the widely-used incident command platform
- **Proposed capabilities:**
  - Real-time aircraft flight information overlay
  - Wind forecast map generation and display
  - Multi-UAS coordination and visualization
  - Data from automated site-selection tools
- **Strategic value:** Adoption of existing, widely-trusted platform minimizes learning curve for fire agencies and incident commanders

### Automated UAS Deployment Tool
- **What it is:** Multi-modal site-selection optimization algorithm
- **Inputs:** ESA/OSE methods refined from Phase I
- **Decision criteria:** Forecast impact, airspace coordination requirements, communications availability, operator reachability
- **Benefit:** Minimizes operator workload; enables rapid deployment decisions during active incidents

### Ground Station Hardware
- **Capability:** Over-the-air flight data transfer; real-time interfacing with fire operations systems

## Use Cases & Applications

### Primary Use Case: Wildland Firefighting Operations
- **Application 1: Wind Field Mapping** – Deploy S0 VTOL in strategic locations around active fires to collect atmospheric data for improved wind predictions
- **Application 2: Incident Commander Decision Support** – Deliver real-time wind forecasts and aircraft situational awareness via TAK platform
- **Application 3: Prescribed Burn Operations** – Demonstrate capabilities in controlled fire conditions to validate approach and build agency confidence
- **Application 4: Multi-UAS Coordinated Sampling** – Operate multiple UAS assets to collect networked atmospheric data, optimizing spatial coverage

### Geographic/Operational Contexts Mentioned:
- Prescribed burns (training/validation environment)
- Active wildfires (operational deployment)
- Isolated, sensitive terrain (testing meteorological models)

## Key Results (Phase I Accomplishments to Build Upon)

- **Weather modeling improvements:** Determined effective methods for improving fire weather forecasts through targeted atmospheric sampling
- **Agency relationships:** Established networking and collaboration pathways with fire teams for airspace integration and operational coordination
- **S0 capabilities validation:** Demonstrated rough-weather capability (TS Tammy); proved weather data recording functionality
- **Methodology refinement:** Validated ESA and OSE methods for optimal site selection
- **Data delivery concepts:** Defined desired data outputs and dissemination pathways for incident commander integration

## Project Timeline & Budget
- **Duration:** 24 months
- **Funding:** $850,000
- **Key milestones:**
  1. Expanded ESA methods + automated site-selection tool
  2. Field-ready S0 VTOL with updated design and deployment kit
  3. Completed BST TAK/COTAK/WFTAK plugin
  4. Realistic-timeline end-to-end data process demonstration with forecast improvement validation
  5. Active fire/prescribed burn flight data collection

## Key Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| **Airspace access:** Gaining permission for UAS operations in wildfire TFR (Temporary Flight Restrictions) | Leverage Phase I agency relationships; collect valuable data outside immediate fire area; demonstrate utility through FireSense connection |
| **Operational timeline:** Shortening end-to-end data process for timely incident decision-making | Automate site-selection and data-distribution tools to eliminate time-consuming manual steps |
| **Technology adoption:** Slow acceptance of new systems by fire community | Focus development on widely-used platforms (TAK); conduct multiple successful demonstrations; build documented flight history |
| **Meteorological robustness:** (flagged but not detailed in checklist) | Address via Task 5 forecasting improvements assessment |

## Notable Details

### Strategic Advantages
- **Existing relationships:** Phase I built connections with multiple fire agencies, creating operational pathways and trust
- **Platform integration:** Building on TAK (already widely deployed in fire operations) rather than introducing new software reduces barrier to adoption
- **Demonstrated capability:** Prior S0 operations in Hurricane Tammy and soil moisture studies establish platform credibility
- **Collaborative partnerships:** NCAR brings Ensemble Sensitivity Analysis expertise; CoE brings fire operations insight; FireSense brings airspace experience

### Related Work Referenced
- **LAPSE-RATE campaign** – BST/NCAR collaborative atmospheric observation work (to be emphasized in proposal)
- **S0 deployment in TS Tammy** – Demonstrates rough-weather capability
- **S0 soil moisture work** – Additional BST/NCAR collaborative data collection (may be cited as background)
- **SGP (Southern Great Plains) flights** – Additional S0 flight history available for reference
- **FireSense and ACERO** – External programs providing context and complementary approaches
- **CoE and COTAK** – Fire community platforms and centers of excellence

### Commercialization Focus
- Document S0 VTOL purchase commitments from fire agencies
- Expand fire agency network for future operational permissions
- Establish commercial viability and market demand

### Proposal Development Notes
- Target searchability using exact keywords from NASA SBIR solicitation language
- Include Gantt chart timeline from Asana project planning
- Reference existing extreme environments folder materials (website boxes, budget templates)
- Achieve TRL Level 7 by Phase II completion
- Ensure consistency between technical task descriptions and proposed budget hours for key personnel
- Cross-reference all sections against NASA Phase II proposal guidelines

---

**Status Note:** This is a working checklist with sections marked as incomplete (e.g., "[1/2]" indicates 1 of 2 sections drafted). Final proposal would expand each section with full technical narrative, detailed risk analysis, commercialization strategy, and supporting documentation.