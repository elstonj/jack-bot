# Multi-UAS RFP Questions & Amendment

## Document Metadata
- Type: Solicitation Amendment with Clarification Questions & Answers
- Client/Agency: University of North Dakota (UND) Procurement Services
- Program/Solicitation: Solicitation Number 210-2022, Vantis multi-UAS RFP
- Date: December 14, 2021
- Related Systems: Vantis C2 system, uAvionix Microlink, GCS Proxy
- Key Personnel: Jack Elston (last editor), Matthew Odom (Procurement Officer)

## Executive Summary
This amendment to the UND Solicitation 210-2022 addresses 80+ technical, operational, and contractual questions submitted by potential bidders regarding requirements for integrating small/medium UAS platforms with the Vantis command-and-control system. The RFP seeks 2-3 vendors per category to conduct Beyond Visual Line of Sight (BVLOS) UAS operations, develop use cases, and conduct functional test flights using Vantis C2 integration. Total budget is $500,000 for the initial 2-year period with options for three 1-year extensions.

## Program Overview

**Vantis System:**
- A developing command-and-control network designed to enable BVLOS UAS operations under both Part 91 and Part 107 regulations
- Currently functional from 0-5,000 ft AGL (anticipated to increase)
- Provides integration services for UAS onboarding
- Has been running for several years prior to this RFP
- Provides Microlink airborne radio (required) and GCS proxy software
- Will provide Interface Control Document (ICD) and APIs post-award
- Does not provide Primary Radar or ADS-B sensors (these are Vantis services, not aircraft-mounted)

**Operational Parameters:**
- Initial operations in Class G and E airspace; anticipated expansion to other classes
- Short-range flights: Visual line of sight (VLOS)
- Extended-range flights: 1-10 NM for small/medium UAS (longer for capable aircraft)
- Operators may initially leverage existing NPUASTS COA with daisy-chain visual observers
- Expected to include test encounters with manned aircraft to verify network capabilities and avoidance procedures
- Functional test flights to verify successful Vantis C2 and GCS integration

## Technical Requirements & Clarifications

**Command & Control (C2):**
- Integration of Vantis C2 radio is MANDATORY
- Aircraft must have TWO C2 radios operating simultaneously (primary and secondary):
  - Primary: Vantis C2 radio (provided by Vantis)
  - Secondary: Operator-supplied local C2 solution with FCC ID (can be LTE-based cellular modem)
  - "Simultaneous" may include: concurrent operations, instantaneous/automatic switchover, or manual switchover
- Operator responsible for defining simultaneous C2 link management approach in proposal
- MAVLINK protocol suggested for C2 messaging from CGS, but other protocols acceptable with team coordination
- Microlink airborne radio: provided by Vantis with integration support
- GCS Proxy: required component, installed on operator's GCS computer (provided by Vantis)
  - Operates on Windows-based systems
  - Requires 20 mbps internet connection from GCS laptop to internet (not backbone requirement)
  - Vantis can consider porting to other operating systems if proposed
- IDEs and APIs will be available post-award (subject to modification as system develops)

**Aircraft Requirements:**
- Aircraft endurance: 1-hour minimum flight time preferred (NOT mandatory; aircraft with lesser flight time not excluded)
- Weather capability: preferences specified but not mandatory
- US registration and US company ownership MANDATORY
- Country of aircraft origin: no restrictions, but must be registerable in US
- Special Airworthiness Certificate – Experimental (SAC-EC): NOT required at proposal stage; will be pursued as part of project with configuration change support if existing SAC-EC proposed
- Part 91.113 waiver: can be obtained in parallel during onboarding
- Canadian operator certificates and PPL(A) NOT acceptable; minimum requirement is US Part 61 pilot certificate and Part 107 remote pilot certificate
- Flight controller must support two simultaneous C2 radios (clarified that existing autopilots like MQ-1/MQ-9 referenced can achieve this through various switchover methods)
- No minimum flight hour requirement for specific aircraft model (both aircraft that will participate AND all aircraft of that type produced should be documented)

**Sensor Requirements:**
- Primary radar and ADS-B: provided by Vantis services, NOT aircraft-mounted
- UA telemetry must post to Vantis service endpoint per Interface Control Document (ICD) - ICD to be provided post-award

**Airspace & Regulatory:**
- Initial operations: Class G and E airspace
- Part 91 and/or Part 107 operations supported per respondent's concept
- Vantis will assist in obtaining BVLOS approvals but operator is applicant (waiver to 91.113 + SAC-EC minimum for Part 91)
- COVID-19 restrictions qualify as Force Majeure

**GCS Proxy Connectivity:**
- 20 mbps requirement applies to GCS laptop-to-internet connection
- GCS can be operated from field locations
- Geographic location limitations may result in exclusion of operational areas due to connectivity constraints
- Test locations will be defined jointly with operators

## Operational Requirements & Concepts

**Use Cases & Demonstrations:**
- Use cases to be specified by each respondent in their Concept of Operations (ConOps)
- Vantis does not prescribe specific use cases; manufacturers propose their concepts
- Demonstrations required (cost borne by offerors)
- Both short-range functional check flights and extended-range waypoint-driven flights
- Test encounters with manned aircraft for network and avoidance testing

**Operator Requirements:**
- Three years of prior experience required (referring to operator organization, not individual aircraft type)
- Operator availability: expected to operate up to 5 days/week, potentially 12 hours/day (60-hour weeks), with cost proposals including weekly/monthly rates up to 50 hours/week
- Multiple crews or companies may operate simultaneously
- Remote Pilot in Command minimum: US Part 107 certificate + US Part 61 pilot certificate
- Part 21 certification budgeting: to be specified by respondent

**Regulatory & Airworthiness:**
- Airworthiness approval does not need to be complete at proposal; preference given to those who have started process
- UND will support pursuit of airworthiness during project
- Obtaining SAC-EC and waivers done as part of project (not prerequisite)
- Vantis will assist in pursuing/obtaining BVLOS approvals; operator is applicant
- Cost-sharing model for COA, SAC-EC, and waiver pursuit to be proposed by respondent

**Testing Locations:**
- Various locations throughout North Dakota
- Exact locations determined by respondent's proposed ConOps
- Cannot be pre-specified due to dependency on concept of operations
- Cellular network coverage at operational areas not guaranteed

## Contract & Budgeting

**Award Structure:**
- Total RFP budget: $500,000 for initial 2-year period
- No minimum or maximum amount per award
- Estimated 2-3 vendors per category selected
- Each category receives primary, secondary, and tertiary provider
- Selection based on amount necessary to meet solicitation requirements
- Fixed-price contract with adjustment provisions

**Cost Proposals Must Include:**
- Itemized list of all direct and indirect costs
- Total hours at various hourly rates
- Direct expenses, payroll, supplies, overhead assigned to each person
- Percentage of each person's time devoted to project
- Profit
- Monthly itemized billing structure
- Weekly/monthly rates (up to 50 hours/week specified; hours over 50/week pricing to be specified by respondent)
- Travel cost estimates (not graded, location-based from vendor location, arranged by mutual agreement)
- Demonstration costs
- Onboarding costs to Vantis system
- Cost-sharing model (respondent-defined)

**Performance Period:**
- 2-year initial term
- Options for up to 3 additional 1-year extensions
- Integration expected to begin upon award
- Flight test operations expected to begin spring/summer 2022
- Vantis and operator to collaboratively define flight test schedule

**Funding Source:**
- Currently state resources; no federal funds used

**Proposal Schedule:**
- Set schedule, not extendable
- Initial evaluations followed by demonstrations/presentations
- Post-award: negotiations of Terms & Conditions allowed (scope/requirements must remain as solicited)

## Intellectual Property & Data

**Software & Materials:**
- Software and materials developed under RFP are property of UND
- In-kind work not owned by UND
- Integration efforts for respondent's equipment not owned by UND
- Only purchased software/equipment owned by UND
- Licensing for products possible if within scope of work
- Interfaces developed for existing equipment (e.g., uAvionix radio interfaces) not owned by UND; vendor can offer to customers

**Records & Proprietary Information:**
- North Dakota Open Records law applies
- Bona fide trade secrets and proprietary information exempt
- PRICING is always an open record (cannot be redacted)

## Integration Activities & Support

**Vantis Provided:**
- Microlink airborne radio + integration support
- GCS Proxy software
- Interface Control Document (post-award)
- APIs (post-award, subject to modification)
- Assistance obtaining BVLOS approvals
- On-site integration capability allowed

**Integration Requirements:**
- System must be capable of operating on Vantis network
- Required integration activities may be outside direct ConOps (mutually agreed upon)
- Concurrent or simultaneous operations of multiple concepts allowed
- Multiple crews may be required per proposed ConOps

**Clarifications on Requirements:**
- Aircraft preferences (endurance, weather) preferred but not mandatory minimums
- Scoring based on ability to perform proposed ConOps
- Simultaneous C2 link management detailed in proposal (no specific master/slave designation)
- Lost link logic concerns acknowledged; operator to address in proposal
- Schedule coordination: Vantis team and operator define test schedule collaboratively

## Notable Details

**Key Definitions Clarified:**
- "Simultaneous" C2 operation includes concurrent, automatic switchover, or manual switchover
- "Cost sharing" undefined by UND; respondent to propose model
- "Vantis PO" = Vantis leadership (not procurement officer)
- SAC-EC waiver possible (not required upfront)
- Schedule A aircraft hull insurance reference was error (disregarded)

**Contingencies & Considerations:**
- Operator availability challenges acknowledged with 2-year performance period and cost-sharing model
- GCS connectivity limitation may exclude some areas
- Vantis system still developing; APIs/IDEs subject to modification
- Multiple test locations expected
- Flexible on autopilot/flight controller approaches to dual C2 link management

**Program Intent:**
- Incentivize industry to commercialize concepts of operations using Vantis
- Support manufacturers onboarding to Vantis system
- Develop operational concepts and use cases
- Conduct functional and extended-range flight tests
- Test network capabilities and manned-unmanned aircraft interaction