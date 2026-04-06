# Black Swift Technologies SBIR Phase I Proposal: Machine Learning for UAS Maintenance Schedules

## Document Metadata
- **Type:** SBIR Phase I Proposal
- **Client/Agency:** United States Air Force (USAF)
- **Program/Solicitation:** SBIR Topic AF203-CSO1 (Artificial Intelligence/Machine Learning)
- **Proposal Number:** FX203-CSO1-1421
- **Date:** Submitted October 28, 2020
- **BST Products/Systems Referenced:** SwiftCore Flight Management System; proprietary avionics monitoring system; monitoring nodes for real-time data collection
- **Key Personnel:** Dr. Jack S. Elston (CEO, Principal Investigator); Dr. Maciej Stachura (Chief Technology Officer)

## Executive Summary
Black Swift Technologies proposes a 3-month Phase I feasibility study to develop machine learning-based predictive maintenance software for small UAS platforms. The solution leverages unsupervised learning algorithms for anomaly detection to identify critical system failures and maintenance needs without requiring labeled/tagged failure data, addressing a gap in current UAS maintenance practices that rely on manual owner's manuals and reactive rather than preventative approaches.

## Technical Approach

**Core ML Strategy:**
- Unsupervised learning for anomaly detection to build behavioral models of aircraft across diverse missions and flight conditions
- Anomalies flagged when aircraft performance falls "out of family" from baseline
- Three-layer maintenance system:
  1. **Direct tracking:** Failed sensors, low battery, lost comms
  2. **Supervised learning:** Known failures with labeled telemetry (servo failures, propeller damage, icing detection)
  3. **Unsupervised learning:** Whole-aircraft performance anomalies without labeled training data

**Data Sources:**
- USAF flight logs and telemetry data (primary source)
- BST's proprietary monitoring nodes (supplementary, if needed) for real-time data collection on candidate platforms
- Standardized flight log analysis through web-based dashboard

**Delivery Platform:**
- Web-based system with simplified red/yellow/green diagnostic ratings by subsystem
- Drill-down capability for detailed information
- Designed for accessibility to non-specialist UAS technicians

## Products & Capabilities Described

**SwiftCore Flight Management System:**
- Proprietary autopilot system developed by BST
- Anchors BST's avionics infrastructure
- Integrates payload systems
- Demonstrated in multiple atmospheric sampling campaigns

**Avionics Monitoring System (Baseline):**
- Current system to be adapted for USAF requirements
- Tracks multiple subsystem health parameters
- Foundation for ML-enhanced maintenance capabilities

**Monitoring Nodes:**
- Modular sensor packages developed by BST
- Can be installed on candidate UAS platforms
- Enable real-time data collection and analysis
- Supplement existing flight log data if needed

## Use Cases & Applications

**Defense Applications:**
- UAS maintenance optimization across USAF platforms worldwide
- Mission-critical reliability and readiness improvement
- Safety enhancement for BVLOS operations and operations over populated areas
- Reduction of UAS loss due to undetected failures

**Stakeholder Engagement Focus Areas:**
- Center for Unmanned Aircraft Systems (Air Force Academy)
- AF Life Cycle Management Command (LCMC)
- System Program Offices (SPOs) responsible for fielding/maintaining UAS

**Commercial Applications:**
- Flight management systems market
- UAS surveying operations
- Insurance cost reduction through improved safety profiles
- Commercial operators conducting routine flights in populated areas

**Market Context:**
- Global military drone market: $7.93B (2018) → projected $21.76B (2026), 12.4% CAGR
- 2020 Defense budget: $3.7B for unmanned/autonomous systems; $927M for AI/ML projects

## Phase I Work Plan

**Tasks:**
1. Identify and engage stakeholders (Center for Unmanned Aircraft Systems, USAF Academy leadership)
2. Explore research areas with Dr. George York and Col. Brian Neff; access flight logs and failure records
3. Determine required adaptations to existing BST technology
4. Present adapted solution outline and seek Memoranda of Understanding (MOU)
5. Prepare Phase II timeline and milestone schedule

**Key Deliverables (90-day maximum):**
1. Understanding of Center for Unmanned Aircraft Systems' goals
2. Adaptation plan for ML/early warning technology
3. Commercialization concept for adapted solution

**Timeline Milestones:**
- Kickoff meeting within 30 calendar days of contract start
- Monthly progress reports and interim updates per contract officer direction
- Final SF 298 and DD Form 882 reports upon completion

## Budget & Cost Details

**Total Phase I Award:** $49,973.28
- **Base Cost:** $46,704.00
- **Profit (7%):** $3,269.28

**Cost Breakdown:**
- **Direct Labor:** $41,760.00 (240 hours total)
  - Dr. Jack Elston (CEO/PI): 150 hours @ $174/hr = $26,100
  - Dr. Maciej Stachura (CTO): 90 hours @ $174/hr = $15,660
- **Travel:** $4,944.00
  - Baltimore to Colorado Springs (2 people, 3 days): $2,490
  - San Diego to Colorado Springs (2 people, 3 days): $2,454
- **Other Direct Costs:** $0
- **Overhead:** 0% rate applied
- **G&A:** 0% rate applied

**Labor Rate Justification:** Fully-burdened GSA CALC rates based on FY21 standards with education parameters (both personnel hold PhDs with 16 years experience).

## Related Work & Company Background

**BST History & Experience:**
- Founded 2011, based in Boulder, Colorado
- Design and build UAS systems entirely in-house
- 11 total SBIR awards (5 Phase II efforts); $4.3M+ non-dilutive SBIR funding
- Revenue: $1.5M in 2019
- Current contracts: NASA, NOAA, Department of Energy, U.S. Geological Survey

**Demonstrated Capabilities:**
- High-altitude, arctic, desert operations; corrosive particulate tolerance; strong turbulence capability
- Soil-moisture mapping UAS (NASA SBIR, CCRPP phase) with $417K+ non-NASA investment
- 300+ flight experiments conducted (including VORTEX2 tornadic supercell intercept)
- 100+ Certificate of Authorization (COA) applications authored
- NASA Airworthiness Flight Safety Review Board (AFSRB) and Flight Readiness Review Board process completion

**Key Personnel Publications:**
- Jack Elston et al., "Net-Centric Communication and Control for a Heterogeneous Unmanned Aircraft System" (*Journal of Intelligent and Robotic Systems*, 2009)
- Jack Elston et al., "A Layered Approach to Networked Command and Control of Complex UAS" (*Handbook of Unmanned Aerial Vehicles*, 2013)
- Maciej Stachura & Eric Frew, "Communication-Aware Information-Gathering Experiments with an Unmanned Aircraft System" (*Journal of Field Robotics*, 2017)
- Eryan Dai et al., "L-band Soil Moisture Mapping Using a SUAS" (IEEE IGARSS 2016)

## Notable Details

**Stakeholder Engagement:**
- Established contacts: Dr. George York (george.york@usafa.edu, 719-333-4210) and Col. Brian Neff (brian.neff@usafa.edu, 719-333-3190) at Air Force Academy
- Strategy to obtain MOUs and transition to Phase II with Center for Unmanned Aircraft Systems

**Key Strategic Advantages:**
- Existing proprietary avionics monitoring infrastructure as baseline
- In-house monitoring node technology for real-time data collection capability
- Web-based dashboard design emphasizing accessibility to non-technical users
- No anticipated need for ITAR/EAR controlled data
- No classified work; all R&D at BST Boulder facilities
- No federal facilities required

**Market Positioning:**
- Dual-use commercial/defense product with strong commercial viability
- Addresses critical gap: UAS systems lack onboard monitoring and systematic maintenance compared to manned aircraft
- Insurance/safety angle for commercial operations differentiates from pure DoD solution

**Company Certifications:**
- Small business (8 employees at proposal time)
- Majority-owned, U.S.-controlled
- No unpaid federal tax liabilities
- No fraud-related convictions or civil liabilities

**Regulatory Readiness:**
- Dr. Stachura has led AFSRB and Flight Readiness Review Board processes for NAS-operating UAS
- Experience with airworthiness certification processes indicates path to regulatory approval