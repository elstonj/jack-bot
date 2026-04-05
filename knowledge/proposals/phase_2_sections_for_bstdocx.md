# Phase 2 Sections for BST - PrecisionTerra Subcontract

## Document Metadata
- Type: Proposal section (Phase 2 work plan for subcontract)
- Client/Agency: NASA (via PrecisionTerra as prime contractor)
- Program/Solicitation: PrecisionTerra Phase 2 NASA project
- Date: Created 2026-03-24, Modified 2026-04-03
- BST Products/Systems Referenced: S3 UAS, E2 UAS, S2 UAS (predecessor)
- Key Personnel: Daniel Prendergast (last editor), Maithreyi Gopalakrishnan, Dmitriy Zusin, Surendra Makam

## Executive Summary
This document outlines Black Swift Technologies' role as a subcontractor to PrecisionTerra for a 24-month NASA Phase 2 project focused on GPS signal lock maintenance and positioning accuracy testing during wildfire conditions. BST will provide two UAS platforms (S3 and E2), conduct FAA and NASA airworthiness certifications, integrate PrecisionTerra's Software-Defined Radio (SDR) and IMU equipment, and execute data collection flights to evaluate how flight dynamics affect GPS signal reception.

## Technical Approach

**Certification & Clearance Tasks:**
- Task 9: Obtain NASA Airworthiness certification for S3 and E2 UAS
- Task 10: Obtain FAA Certificate of Authorization (COA) or Part 107 Waiver for data collection flights

**Payload Integration (Task 11):**
- Install PrecisionTerra's complete SDR and Analog Devices IMU on BST S3 UAS (moving platform for data collection)
- Install second PrecisionTerra SDR on BST E2 UAS (hovering reference platform)
- Coordinate with PrecisionTerra to verify payload weights against UAS maximum payload capacities
- Potential addition of metal enclosure to artificially degrade GPS signals if flight-testing locations lack sufficient natural signal degradation
- Leverage existing uBlox receiver modules on BST platforms for detailed receiver data

**Flight Testing Approach (Task 12):**
- E2 UAS operates as hovering "control" platform at similar altitude to S3
- S3 UAS operates as moving platform following defined flight paths
- Allows analysis of how flight dynamics affect GPS signal lock maintenance and positioning accuracy
- BST will conduct test flights with full payloads before final data collection
- BST pilots will conduct all flights; BST will determine flight paths

## Products & Capabilities Described

**BST S3 UAS:**
- Maximum payload capacity: 5.5 lbs
- Primary data collection platform (moving configuration)
- Equipped with uBlox receiver modules
- Will carry PrecisionTerra SDR + Analog Devices IMU + RF shielding

**BST E2 UAS:**
- Maximum payload capacity: 4.39 lbs
- Reference/hovering platform for comparative testing
- Equipped with uBlox receiver modules
- Will carry PrecisionTerra SDR + RF shielding

**BST S2 UAS:**
- Predecessor to S3
- Referenced as basis for 2024 NASA wildfire monitoring contract
- Demonstrates wildfire monitoring capability

## Use Cases & Applications

**Primary Application:** Wildfire monitoring and GPS signal integrity testing
- Testing GPS signal lock maintenance and positioning accuracy in conditions that degrade GPS signals
- Relevant to active wildfire environments where signal degradation occurs
- Simulated testing with metal enclosures if natural signal degradation insufficient

**Historical BST Expertise Areas:**
- Wildland fire monitoring and assessment
- Scientific payload deployment in wide range of operating environments

## Notable Details

**Company Background:**
- Black Swift Technologies founded in 2011, based in Boulder, Colorado
- Specializes in UAS platforms for flying scientific payloads

**2024 Relevant Contract:**
- BST won NASA contract to develop wildfire monitoring system for S2 UAS, demonstrating prior successful government work in this domain

**BST Project Responsibilities:**
- All flight clearances and certifications (FAA COA)
- Payload integration and RF shielding installation
- Test flight validation
- Final data collection flights
- Flight path determination and pilot services

**Collaborative Elements:**
- Close coordination with PrecisionTerra on payload integration
- Coordination on RF shielding requirements
- Potential collaboration on signal degradation test methodology

**Gaps Noted in Document:**
- Personnel hours and labor rates table referenced but not included in provided text
- Specific month assignments (M__) for tasks not filled in
- NASA Airworthiness certification requirements (Task 9) description incomplete
- Document requests additional materials: S3/E2 UAS diagrams and descriptions of BST's other wildfire-related projects