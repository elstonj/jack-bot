# Vantis Multi-UAS RFP Technical Proposal

## Document Metadata
- Type: Request for Proposal (RFP)
- Client/Agency: University of North Dakota (UND), Northern Plains UAS Test Site (NPUASTS)
- Program/Solicitation: RFP 210-2022, "Vantis Multi-UAS RFP"
- Date: Issued November 24, 2021; Proposals due December 31, 2021
- BST Products/Systems Referenced: None explicitly mentioned (this is a UND RFP soliciting UAS vendors)
- Key Personnel: Matthew Odom (Procurement Officer); Jack Elston (document editor at BST)

## Executive Summary
The University of North Dakota's Northern Plains UAS Test Site is soliciting proposals from multiple UAS vendors to support testing and integration of the Vantis Beyond Visual Line of Sight (BVLOS) network for FAA approvals. The Vantis network is North Dakota's statewide UAS infrastructure designed to enable routine BVLOS operations through command and control, airspace surveillance, and NAS integration. Up to six vendors may be selected for awards totaling not to exceed $500,000 combined.

## Technical Approach

### Vantis Network Infrastructure
- **Command and Control**: uAvionix microLink airborne radio and SkyStation ground radios
- **Surveillance**: Primary radar and ADS-B sensors
- **Data Network**: Secured backhaul network
- **Operations Center**: Mission and Network Operations Center (MNOC)

### Aircraft Equipage Requirements
1. **C2 Radio Integration**:
   - Must integrate uAvionix microLink (current Vantis C2 radio)
   - Must support simultaneous dual C2 radios (primary Vantis + secondary operator C2)
   - Future C2 will use licensed/aviation-protected spectrum meeting RTCA standards
   - Operator must supply local C2 solution with FCC ID

2. **GCS Integration**:
   - GCS Proxy (Vantis-provided Windows application) installed on GCS or networked computer
   - Windows-based machine required
   - High-speed internet (minimum 20 mbps) during all flights
   - Browser-based connection to Vantis services (Chrome)
   - GCS controlling software interfaces with GCS Proxy over TCP/IP
   - Non-MAVLINK protocols must post telemetry to Vantis endpoint per Interface Control Document (ICD)

3. **Timing and Messaging Requirements**:
   - All C2 messages timestamped with minimum 1-millisecond precision
   - Heartbeat message from UA at least once per second
   - Heartbeat indicates operational state with 1-millisecond precision

4. **Airworthiness**:
   - Must pursue formal airworthiness approval (Special Airworthiness Certificate-Experimental Category [SAC-EC], 44807 approval, or Part 21 Type Certification)
   - Aircraft must be U.S.-owned company property

### Aircraft Preferences
- Minimum 1-hour endurance (longer duration preferred)
- North Dakota weather-capable: wind limit ≥25 knots, outside air temperature minimum ≥-20°F
- Lights visible up to 3 statute miles
- Detect and Avoid (DAA) technology optional

## Products & Capabilities Described

### Vantis Network (State of North Dakota Program)
- **What it is**: Statewide UAS network infrastructure for command and control, surveillance, and NAS integration
- **Proposed use**: Enable routine BVLOS UAS operations with safety and regulatory compliance
- **Components**:
  - uAvionix microLink C2 radio (airborne)
  - SkyStation ground radios
  - Primary radar and ADS-B surveillance
  - Secured backhaul data network
  - Mission and Network Operations Center (MNOC)
- **Scope**: First initiative of its kind in nation; 8-year expansion plan across North Dakota

## Use Cases & Applications

### Flight Test Operations
1. **Short-range Functional Check Flights**: Basic system verification
2. **Extended Range Operations**: Pre-planned, waypoint-driven flights within aircraft endurance
   - May leverage existing NPUASTS Certificate of Authorization (COA)
   - Daisy-chain visual observer operations initially
3. **Manned-Unmanned Encounters**: Test flights with manned aircraft in various geometries to test network capabilities and avoidance procedures

### Operational Approval Strategy
- Development of use case proof-of-concepts
- Special Airworthiness Certificate in Experimental Category (SAC-EC) pursuit
- Waiver to 14 CFR 91.113
- Exemptions to applicable 14 CFR regulations
- Data collection to verify Vantis system performance and operational procedures

## Operator Requirements

### Flight Crew Minimum
- **Remote Pilot in Command (RPIC)**:
  - Part 61 Pilot Certificate
  - Part 107 Remote Pilot Certificate
- **Flight Support Personnel**:
  - Part 61 Pilot Certificate OR Part 107 Remote Pilot Certificate
  - U.S. Driver's License
  - Vantis will provide training for non-standard duties

### Operational Availability
- Available throughout contract term on per-test-event basis
- Expected operations: Monday-Friday, up to 12 hours/day, occasionally weekends
- Test events: 1 week to 2 months duration
- For 1-month event: approximately 12 flight days expected

### Support Requirements
- Aircraft technical subject matter expert (SME)
- Original Equipment Manufacturer (OEM) support preferred
- Optional: Additional flight crew for daisy-chain visual observer operations
- Integration and engineering support for Vantis network compatibility

### Preferred Qualifications
- Prior experience with advanced FAA approvals
- Existing NPUASTS relationships

## Contract Terms

### Duration & Renewal
- **Initial term**: 2 years (January 1, 2022 start date)
- **Extension option**: Up to 90 days
- **Renewal options**: Up to 3 additional 12-month periods
- **No automatic renewal**

### Financial Terms
- **Contract type**: Fixed price with adjustment
- **Multiple awards**: Up to 6 vendors
- **Total budget**: Not to exceed $500,000 (combined for all awards)
- **Cost sharing**: Preference for operators providing cost-sharing; intent is to offset operator costs such as Vantis radio integration and North Dakota travel expenses
- **Payment terms**: Within 30 days of correct invoice receipt
- **Travel reimbursement**: GSA rates for lodging, coach air travel, per diem meals

### Insurance Requirements (Mandatory)
- Commercial General Liability: $1,000,000 per occurrence
- Workers' Compensation: Per statutory requirements
- Employer's Liability: $1,000,000 minimum
- **Aircraft Hull Insurance**: Value as specified in Schedule A (not provided in excerpt)
- **Aircraft Liability Insurance**: $5,000,000 (bodily injury, property damage, personal injury)
- UND and officers/employees to be added as additional insureds
- Aircraft hull insurance must include waiver of subrogation in favor of UND
- All insurance must be primary to UND's coverage

### Evaluation Criteria (100-point scale)
- **Technical Proposal (95 points)**:
  - Experience and Qualifications (40 points)
  - Approach to Work (55 points)
- **Cost Proposal (5 points)**

### Minimum Prior Experience Requirement
- 3 years prior UAS operational experience (mandatory for responsive bid)
- Must provide: number of aircraft manufactured/owned/operated, flight hours with proposed aircraft, total years of operational experience

## Notable Details

### Key Project Goals
- Verify Vantis Network meets performance and operational requirements with safety and regulatory compliance
- Expand network capabilities across North Dakota over 8 years
- Establish viable, self-sustaining network enabling routine BVLOS operations
- First statewide UAS network infrastructure initiative in the nation

### Procurement Process
- Submission via State Procurement Online (SPO) system
- Maximum 5 documents per submission (50MB per file)
- No pre-proposal conference held
- Verbal presentations required for top 6 scoring proposals
- Site inspections not required

### Regulatory/Compliance Context
- Operations under 14 CFR Part 107, Part 91
- Subject to FAA waivers/authorizations for advanced operations
- Compliance with North Dakota public records law
- North Dakota venue (Northeast Central Judicial District Court, Grand Forks County)

### Intellectual Property
- All work products, software, and materials are "works for hire" owned by UND
- Contractor assigns all rights to UND
- Contractor responsible for executing necessary IP protection documents

### Document Quality
This is a complete, comprehensive RFP document with substantial technical and operational requirements. The document provides clear specifications for aircraft equipage, network integration, operational procedures, crew qualifications, and contract terms. It reflects a sophisticated, well-planned state program for UAS integration.