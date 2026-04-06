# BluFlux Subcontract Services Agreement

## Document Metadata
- Type: Subcontract Services Agreement (legal/commercial contract)
- Client/Agency: BluFlux, LLC (Prime Contractor); End Customer: Skyward IO, Inc.
- Program/Solicitation: DCA PoC (Proof of Concept) Testbed project
- Date: December 2020 (Effective Date); Document signed January 5, 2021
- BST Products/Systems Referenced: S2 aircraft, E2 aircraft
- Key Personnel: Dr. Jack S Elston (BST CEO & Founder); Benjamin Wilmhoff (BluFlux President)

## Executive Summary
Black Swift Technologies agreed to serve as a subcontractor to BluFlux for development and flight testing of a DCA (Distributed Cellular Architecture) Proof of Concept Testbed. The work includes electronics unit requirements definition, firmware development for cellular data logging, payload integration onto BST's S2 aircraft, and two rounds of flight testing to evaluate directional versus omnidirectional antenna performance for cellular connectivity.

## Technical Approach

**Overall Project Structure:**
- Schedule 1 (Phase 0B): Requirements definition and options development for Electronics Unit (substantially completed as of agreement date)
- Schedule 2: Initial flight testing campaign with five phases (0C, 1B, 2B, 2C, 2D)

**Electronics Unit Development (Schedule 1):**
- Define mechanical, electrical, and electronics requirements compatible with Primary UAVs and Antenna System
- Electronics Unit must incorporate Sierra Wireless WP-7610 or similar cellular module supporting LTE B66
- Include RF switching for up to 5 antenna ports (MP-B-O configuration maximum)
- Battery must power the unit and cellular module for at least 40 minutes
- Data logging to SD card with user-accessible download interface
- Evaluate need for separate microprocessor versus WP7610 Linux executable capability
- Present design implementation options including:
  - Initial functional prototype (evaluation board with WP7610)
  - Robust custom PCB option for flight testing

**Firmware & Software Development (Schedule 2, Phase 1B):**
- Implement cellular connectivity data logging to SD card
- Develop "EU OK" real-time beacon over cellular link for flight test monitoring
- Implement iPerf-based throughput parameter logging
- Create web-based software for data storage and retrieval
- BST to provide BluFlux with source code repository access and credentials
- BST to maintain web-based data hosting with BluFlux access until authorized termination

**Payload Integration (Schedule 2, Phase 2B):**
- Integrate Electronics Unit with S2 aircraft
- Prepare EU interfaces and access for field operations (battery swap, antenna cable swap, SD card removal)
- Procure and integrate GPS antennas
- Implement field-accessible power and data logging control
- Perform electromagnetic interference testing with aircraft subsystems
- Load-balance counterweights as necessary

**Flight Testing (Schedule 2, Phases 2C and 2D):**
- Phase 2C: Single antenna cellular connectivity testing at rural location
  - Terrestrial mobility baseline tests preceding flight tests
  - Three flight paths each for omnidirectional and forward-facing patch antenna
  - Deliver PCI (Physical Cell Identity) data logfiles
- Phase 2D: Single antenna cellular throughput testing at rural location
  - iPerf-based throughput tests at same rural site
  - Test plan updated based on Phase 2C results
  - Up to three flight paths depending on Round 1 findings

**Test Site Planning (Schedule 2, Phase 0C):**
- Develop flight plans for rural, suburban, and urban test locations
- Conduct terrestrial pre-test confirmation of datalogging baseline
- Complete Part 107 waiver applications and local agency notifications for suburban/urban sites

## Products & Capabilities Described

### S2 Aircraft
- Primary platform for DCA PoC Testbed payload integration
- Equipped with nose cone to mount antenna assembly and Electronics Unit
- Aircraft rental rate: $1,000/day for flight testing
- Can accommodate payload weight within existing budgets
- Subject to electromagnetic interference assessment with testbed

### E2 Aircraft
- Referenced for payload integration testing in anechoic chamber
- BST performed payload integration of S2 and E2 aircraft to support anechoic chamber tests ($3,356.77 invoice)

### Electronics Unit
- Modular testbed component integrating cellular modem, data logging, and RF distribution
- Sierra Wireless WP-7610 cellular module as primary component
- Supports LTE Band 66 connectivity
- RF interface supporting up to 5 antenna ports
- Data logging capabilities: cellular connectivity parameters, serving/neighbor cell data, throughput metrics
- Battery life: minimum 40 minutes operational duration including cellular transmission
- Data storage: SD card interface for flight test data
- Firmware: WP7610 Linux executable capable with optional separate microprocessor

### Antenna Assembly
- Quad-patch plus omnidirectional antenna configuration
- Forward-facing patch antenna (directional)
- Omnidirectional antenna
- Mounted inside S2 nose cone
- Up to 5 RF connector ports for switching evaluation

## Use Cases & Applications

**Primary Use Case: Cellular Network Performance Evaluation**
- Measure uplink performance (User Equipment to eNodeB)
- Measure downlink performance (eNodeB to User Equipment)
- Assess mobility and connection reliability
- Compare directional versus omnidirectional antenna impact on network performance
- Evaluate LTE Band 66 connectivity over varied terrain and flight conditions

**Secondary Use Case: GPS Waypoint-Based Antenna Switching Development**
- Flight test data to inform later-phase GPS waypoint-based antenna selection algorithm
- Support Verizon and BluFlux in developing autonomous antenna switching for preferred antenna selection during flight path segments

**Test Scenarios:**
- Rural location: Initial connectivity and throughput baseline testing
- Suburban location: Extended evaluation with Part 107 waiver requirements
- Urban location: High-density cellular environment evaluation

**Testing Methodology:**
- Terrestrial mobility tests to establish baseline before each flight test
- Cellular data logging during flight paths
- iPerf throughput measurement tool integration
- Real-time "EU OK" beacon monitoring via cellular link during flights

## Contractual Terms & Deliverables

**Schedule 1 (Phase 0B) - Electronics Unit Requirements & Options:**
- Total Cost: $10,316.77 (partially paid as of agreement date)
  - Requirements Portion: $4,872.00 (paid)
  - Options Development: $2,088.00 (at BluFlux confirmation)
  - Payload Integration (S2 & E2 for anechoic chamber): $3,356.77 (paid)

**Schedule 2 - Initial Flight Testing:**
- Total Fixed Price: $41,192.00
  - Phase 0C (Flight Planning): $10,440.00 (60 hours @ $174/hr)
  - Phase 1B (Firmware Development): $15,312.00 (88 hours @ $174/hr)
  - Phase 2B (S2 Payload Integration): $4,872.00 (28 hours @ $174/hr)
  - Phase 2C (Flight Test Round 1): $5,284.00
    - Pilot/Spotter: $1,500/day
    - Flight test engineering: 8 hours @ $174/hr = $1,392
    - S2 aircraft rental: $1,000/day
    - Non-flight-test engineering: 8 hours @ $174/hr = $1,392
  - Phase 2D (Flight Test Round 2): $5,284.00 (same breakdown as 2C)

**Payment Terms:**
- Down payment: Up to 25% of phase fee upon acceptance
- Remaining fees due upon Prime Contractor acceptance of deliverables
- Additional out-of-scope work: Monthly invoice at $174/hour standard rate
- Invoices payable within 45 days of receipt

**Schedule 2 Completion Target:** December 24, 2020

**Authorized Start Phases as of agreement date:**
- Phase 0C: DCA PoC Testbed Flight Planning
- Phase 1B: Firmware Development for Initial Datalogging
- Phase 2B: S2 Initial Payload Integration

**Conditional Start Phases:**
- Phase 2C: Upon completion of Phase 0C deliverables
- Phase 2D: Upon completion of Phase 2C deliverables

## Deliverables Summary (Schedule 2)

**Phase 0C - Flight Planning (2 deliverables):**
1. Rural Location Flight Plan Document
2. Suburban and Urban Flight Plans Document

**Phase 1B - Firmware Development (5 deliverables):**
3. Initial Cellular Connectivity Sample Logfile
4. Logfiles From Initial Terrestrial Mobility Tests
5. Timestamped Entries in "EU OK" Beacon Tracking Table
6. Initial Sample Throughput Parameter Logfile
7. Logfile From Terrestrial Mobility Throughput Test

**Phase 2B - Payload Integration (2 deliverables):**
8. Payload Component Access Readiness Report
9. Payload Integration Report

**Phase 2C - Flight Testing Round 1 (2 deliverables):**
10. Flight Test Cellular Connectivity Logfiles For Three Flight Paths, Omni Antenna and Forward Patch Antenna
11. Cellular Connectivity Flight Test Findings and Recommendations Report

**Phase 2D - Flight Testing Round 2 (2 deliverables):**
12. Flight Test Throughput Logfiles For Omni Antenna and Forward Patch Antenna
13. Throughput Flight Test Findings and Recommendations Report

## Notable Details

**Intellectual Property:**
- BluFlux (Prime Contractor) retains ownership of all deliverables created specifically for Skyward IO (End Customer)
- BST retains ownership of "Subcontractor Property" (pre-existing tools, software, designs, and works created outside this agreement scope)
- Deliverables deemed "work made for hire" under 17 U.S.C. § 101

**Source Code & Data Hosting Access:**
- BST must provide BluFlux with complete access to firmware and software source control repository
- BST must supply all credentials and notify BluFlux of updates
- BST must maintain repository and web-based data hosting until authorized termination by BluFlux
- Requirement for collaborative access suggests ongoing project management and integration needs

**Insurance & Compliance:**
- BST maintains $1,000,000 per occurrence / $1,000,000 aggregate commercial general liability insurance
- Independent contractor relationship; BST responsible for all payroll taxes and withholdings

**Performance Metrics:**
- 7 business day test period for Prime Contractor to review deliverables
- Non-conformity rejection must occur within test period or deliverables deemed accepted
- Corrective action: BST to remedy deficiencies at no additional charge or provide pro rata refund

**Status as of Agreement Date (December 2020):**
- Phase 0B requirements definition substantially complete
- Electronics Unit design constraints confirmed
- Implementation options under development
- Three WP7610 IMEI/Verizon SIM configurations pre-qualified for testing

**Project Context:**
- Continuation of prior phases (2A Phase confirmed testbed performance in S2 nose cone configuration)
- Part of larger Verizon/cellular network evaluation initiative
- Data from this testbed will inform development of autonomous antenna selection algorithms in later project phases
- Terrestrial baseline testing methodology to precede each flight test for data validation