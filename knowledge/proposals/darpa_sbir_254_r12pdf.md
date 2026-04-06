# DARPA FY25 SBIR Program Solicitation (Release 12)

## Document Metadata
- **Type:** Program solicitation / Broad Agency Announcement (BAA) instructions
- **Client/Agency:** Defense Advanced Research Projects Agency (DARPA)
- **Program/Solicitation:** DoD 25.4 Small Business Innovation Research (SBIR); FY2025 Annual BAA, Release 12
- **Date:** September 2025 (created Sept 12, 2025; modified Sept 11, 2025)
- **BST Products/Systems Referenced:** None identified in this document
- **Key Personnel:** Beck Cotter (last editor)

## Executive Summary
This document contains DARPA's submission instructions and four SBIR topic solicitations for FY25. It establishes requirements for Phase I (9 months, $250K) and Direct to Phase II (DP2) proposals across multiple technical domains including cybersecurity, advanced computing, space technology, and microelectronics. The solicitation emphasizes high-risk, high-reward innovations with dual-use (military and commercial) potential.

## Technical Topics (Four DARPA SBIR Topics)

### HR0011SB20254-12: Assessing Security of Encrypted Messaging Applications (ASEMA)

**Objective:** Develop models, frameworks, and evaluation methods to defend secure messaging applications (SMAs) from real-world attacks, particularly those targeting the application layer rather than cryptographic protocols.

**Technical Approach:**
- Characterize and model the attack surface of SMAs on mobile devices
- Develop framework identifying security boundaries, protections, and mitigations
- Create tools and techniques for evaluating SMA security features
- Focus on software security beyond cryptographic protocol validation

**Key Technical Challenges:**
- SMAs represent enormous attack surface (network and OS interactions) remotely reachable by attackers
- Advanced Persistent Threat (APT) groups increasingly exploit SMA vulnerabilities
- Need for systematic assessment of application code security while cryptographic protocols are well-tested
- Expanding feature sets continually increase attack surface without corresponding security risk assessment

**Phase II Deliverables/Milestones:**
- Month 1: Kickoff briefing with updated technical approach and risk mitigation
- Month 4, 7, 10: Quarterly technical progress reports
- Month 14: Final briefing with final architecture, prototype demonstration, documented APIs, user manuals, system design document, commercialization plan
- Month 19 (Option): Interim report on prototype maturation vs. state-of-the-art
- Month 24 (Option): Final option period briefing with real-world SMA demonstration

**Award Structure:** Direct to Phase II only; $1,000,000 base period (14 months) + $800,000 option (10 months) [Topic HR0011SB20254-12 variant]

**Phase III Applications:**
- Vulnerability framework supports national efforts in commercial and military secure communications
- Users can mitigate risks and develop proper communication protocols
- Enables informed risk analysis of SMA usage

---

### HR0011SB20254-13: Pulsed High-power Laser Accelerators to Study radiation Hardening (PHLASH)

**Objective:** Demonstrate prototype scalable laser driver for electron beam generation and design a 100-GeV system fitting within 250 m³ footprint for radiation hardness testing of space microelectronics.

**Technical Approach:**
- Utilize laser wakefield acceleration (LWFA) or laser plasma acceleration (LPA) technology
- Develop compact laser driver generating 50-MeV electron beams at >100 Hz repetition rate
- Design for scalability to 100 GeV at 1 kHz
- Create electron packets with extremely small transverse dimensions (≤1 µm) and sub-picosecond longitudinal dimensions

**Key Technical Challenges:**
- LWFA/LPA can reduce acceleration distance 1000x vs. classical RF accelerators, but current high-pulse-power lasers and plasma targets not available
- Physics of electron beam optimization at high energies not fully understood
- Need to maintain size constraints (<250 m³) while achieving higher energies and repetition rates
- Gas target behavior at increased energies and 1-kHz repetition rates
- Focusing optics sizing and maintenance within system footprint limits

**Phase II Deliverables/Milestones (24-month base period):**
- Month 1: Material acquisition plan and detailed technical design
- Months 3, 6, 9, 12, 15, 18, 21: Quarterly progress reports
- Month 12: Interim report on prototype performance and commercialization plan
- Month 23: Prototype demonstration of 50 MeV beam, >100 Hz, with design/workplan for scaling to 100 GeV at 1 kHz
- Month 24: Final report with design, results, and comparison with alternative systems

**Award Structure:** Direct to Phase II only; $1,800,000 (24 months)

**Application Context:**
- Current testing conducted at large, existing heavy-ion accelerator facilities unable to meet demand
- Heavy ions are current gold-standard for single-event effect (SEE) testing
- New methodology using high-energy electron packets as equivalent surrogate for heavy ions
- Could be integrated into semiconductor fabrication facilities

**Phase III Applications:**
- Space-based microelectronics in telecommunications, weather, and other satellites
- High-altitude vehicles (e.g., International Space Station)
- Enables more efficient, reliable radiation testing mechanisms
- Allows components to reach service more rapidly

**References:** Work builds on Stanford Linear Accelerator Center (SLAC), CERN CLEAR, and recent nanoparticle-assisted hybrid wakefield accelerator achievements

---

### HR0011SB20254-14: Narcissus

**Objective:** Develop computational imaging capability to sense-make from a novel imaging system using commercial building window glass as primary optical collecting surface for space domain awareness applications.

**Context (WITH-US Program Heritage):**
- Previous DARPA effort (WITH-US) validated concept of using building windows as telescope primary optics
- Millions of square meters of commercial float glass on skyscrapers could enable rapid proliferation of upward-looking imagers
- Order-of-magnitude jump in transient target awareness potential

**Technical Approach:**
- Develop computational/lensless imaging methods for building-scale light collection
- Focus on "software over hardware" approach for low-mass scalability
- Perform coherent and incoherent combination of incident photon flux
- Enable compensated image reconstruction accounting for:
  - Surface imperfections and waviness
  - Skyglow
  - Temperature variation
  - Wind effects
  - Atmospheric turbulence

**Specific Test Case:**
- 10-story building, 30m × 30m footprint
- 900 m² total imaging area
- 900 windowpanes (each 1m × 1m)
- 100% fill factor (all glass)
- Example: "The Edge," 30 Hudson Yards, New York City
- Expected: ~100 secondary apertures required if limited to 3×3 grid coherent collection

**Phase I Deliverables (9-month base period):**
- Month 1: Virtual kickoff with computational imaging/ML technical approach presentation
- Month 3: Initial caustic image simulator demonstrating detector images from arbitrary focal planes with various window configurations; baseline hardware solution; initial incoherent image analysis algorithm
- Month 6: Interim update (government-only)
- Month 9: Final demonstration with simulation tools, algorithms, updated hardware baseline, scalability/cost study

**Phase II Deliverables (12-month base period):**
- Month 15: Preliminary Design Review (PDR) level design
- Month 18: PI Meeting
- Month 21: Small-scale laboratory demonstration of window characterization software, optical correction, and image compensation with building-level simulator integration; performance projections under varying conditions
- Month 24: Critical Design Review (CDR) level design with fieldable prototype capable of measuring known dim objects (e.g., stars)

**Award Structure:** Phase I option; $250,000 (9 months)

**Technical Requirements:**
- Caustic image simulator for arbitrary focal planes
- Coherent and incoherent light combination methods
- Self-calibrating algorithms (accommodate slow window shape/distortion changes)
- Performance in presence of noise sources

**Phase III Dual-Use Applications:**
- Ground-to-space: Space Domain Awareness (SDA) and satellite surveillance
- Air-to-air: Advanced targeting pod sensors for low-cost UAS
- Ground-based telescopes: mm-scale glass mirrors enabling order-of-magnitude mass reduction
- Very Large Telescope (VLT) systems for cost/size-scalable applications
- Distant satellite tracking (GEO, cislunar)
- Commercial astronomy
- Direct benefit to USSTRATCOM Space Domain Awareness architecture goals
- Widespread commercial and civil astronomy applications

---

### HR0011SB20254-15: Unbiased Behavioral Discovery Platforms

**Status:** Document text appears truncated at this topic

---

## Proposal Submission Requirements

### General Structure (All Topics)

**Phase I Proposals:**
- White Paper: 10 pages max
- Slide Deck: 5 pages max
- Cost Proposal (Volume 3): Using provided Excel template
- Award: $250,000 for 8-9 months

**Direct to Phase II (DP2) Proposals:**
- DP2 Feasibility Documentation: 10 pages max
- Technical Proposal: 20 pages max
- Commercialization Strategy: 5 pages max
- OR White Paper format: 20 pages + 15-slide deck
- Cost Proposal: Using provided templates
- Awards: $1,000,000-$2,000,000 range depending on topic

**Supporting Materials Required:**
- Company Commercialization Report (CCR) - Volume 4 (not evaluated)
- Supporting Documents - Volume 5 (certifications, etc.)
- Fraud, Waste & Abuse training completion - Volume 6
- Foreign Affiliations/Relationships disclosures - Volume 7 (webform, not PDF)

### Submission Portal
- Defense SBIR/STTR Innovation Portal (DSIP)
- Electronic submission required; no other submission method accepted
- Early registration recommended
- Early submission recommended to avoid deadline congestion

### Question Deadline
- Technical questions deadline: October 15, 2025
- Submit to: SBIR_BAA@darpa.mil
- Reference topic number in subject line

## Award Information

### Contract Type Options
- FAR-based Firm-Fixed Price contracts
- FAR-based Cost-Plus Reimbursement (requires DCMA Final Determination Letter)
- Other Transactions (OT) for Prototype agreements (10 U.S.C. § 4021)

### Special Funding Structures

**Topic HR0011SB20254XL-01 (Not detailed in text, but noted):**
- Maximum $3,000,000 total
- $2,000,000 base period (12 months, fully DARPA-funded)
- $1,000,000+ option minimum (12 months, fully DARPA-funded)
- DARPA will match up to $500,000 of non-DARPA partner funding
- Partner funding agreement must be written, signed, and received 60 days before end of base period

### Support Programs

**Transition and Commercialization Support Program (TCSP):**
- Available to Phase II and DP2 awardees at no cost
- Goal: Move technology beyond Phase II into other R&D programs or commercial markets
- Available upon contract execution

**Embedded Entrepreneurship Initiative (EEI):**
- Available to selected SBIR awardees (at government discretion)
- Components:
  - Senior Commercialization Advisor (SCA) from DARPA
  - Connections to U.S. industry and private investor partners
  - Additional funding (typically max $310,000) to hire embedded entrepreneur
  - One commercialization workshop attendance
- Selection criteria: DoD/Government need, competitive approaches, sustainability, manufacturability, scalability, supply chain, regulatory requirements, IP considerations

## Evaluation Criteria

- Proposals evaluated on individual merit against stated criteria, not against each other
- Conformance with requirements is mandatory (non-conforming proposals not evaluated)
- Strengths vs. weaknesses documented for each criterion
- "Selectable" proposal: strengths outweigh weaknesses; no accumulated weaknesses requiring extensive negotiation
- "Non-selectable" proposal: weaknesses outweigh strengths

### Selection Timeline
- Notification within 90 calendar days of BAA closing date
- Technical evaluation narrative provided to all proposers
- Informal feedback available upon request

## Notable Details

1. **