# AFWERX 20.3 SBIR Phase I Final Report

## Document Metadata
- Type: SBIR Phase I Final Report (draft answers to final report questions)
- Client/Agency: U.S. Air Force (AFWERX)
- Program/Solicitation: AFWERX 20.3 Open Topic RFP
- Date: Submitted 2020, report finalized 2021-04-26 to 2021-05-03
- BST Products/Systems Referenced: AI/ML preventive maintenance platform for UAS; web portal for maintenance data; embedded sensors on UAS platforms
- Key Personnel: Not named in this document

## Executive Summary
Black Swift Technologies conducted Phase I research to validate an AI/ML-based preventive maintenance system for USAF unmanned aircraft systems (UAS) using the company's existing technology as a baseline. The research identified that the USAF currently relies on manual maintenance logs and multiple disparate software systems to track aircraft maintenance states. BST concluded that supervised and unsupervised machine learning techniques—particularly generative adversarial networks (GANs) for time series anomaly detection—could significantly improve USAF aircraft readiness rates by providing early warning of critical system failures.

## Technical Approach

### Unsupervised ML for UAS Maintenance Diagnostics
- Primary technique: Unsupervised machine learning algorithms to provide early warning and diagnostics of potential critical system failures on UAS using onboard telemetry
- Specific focus: Time series data analysis using generative adversarial networks (GANs)
- Advantage of GANs: Detect anomalies with fewer false positives than previously considered methods

### Phase II Proposed Work
- Further development of time series-based ML methods
- Comparison against supervised algorithms using datasets from hundreds of BST UAS flights
- Addition of novel embedded sensors: acoustic and thermal sensors
- Planned failure induction to increase anomaly training data
- Potential application to both BST internal UAS and USAF assets

### Data Integration Strategy
- Combine supervised and unsupervised ML techniques to analyze:
  - Data from manual flight logs
  - Actual flight data from UAS telemetry
  - Data from various software maintenance systems

## Products & Capabilities Described

**AI/ML Preventive Maintenance Platform**
- Current state: Existing system embedded in BST UAS platforms with onboard sensors generating data for predictive maintenance algorithms
- Delivery mechanism: Web portal for viewing AI/ML diagnostics
- Phase I finding: The sensor integration and algorithm approach concept could potentially be extended to larger Group 3 UAS platforms

**Embedded Sensor Systems**
- Current capability: Already embedding sensors in existing BST UAS platforms
- Novel sensors identified in Phase I: Acoustic sensors and thermal sensors
- Technical precedent: These sensor types show promise in other fields (industrial machinery, offshore refineries) for anomaly detection in maintenance applications

## Use Cases & Applications

**Primary Use Case: USAF Aircraft Readiness**
- Target: Improving readiness rates for manned and unmanned aircraft across all Air Force units operating Gen 4 aircraft
- Specific problem: Units currently rely on combination of manual maintenance logs and various software maintenance systems to assess aircraft maintenance states
- Proposed benefit: AI/ML algorithms coupled with integrated aircraft sensors could provide early warning of failures requiring maintenance

**Scalability Path:**
- Phase I validation on BST UAS platforms
- Potential extension to Group 3 UAS platforms
- Eventual application to broader USAF assets beyond UAS

## Key Results / Phase I Conclusions

1. **Problem Validation:** Confirmed that manned and unmanned aircraft readiness rates are a significant issue for the Air Force; all Air Force units operating Gen 4 aircraft experience this problem

2. **Technical Feasibility:** Concluded that the machine learning techniques proposed could be very helpful in diagnosing maintenance states of USAF assets

3. **ML Methodology Identified:** Determined that combination of supervised and unsupervised ML techniques is best approach for analyzing data from manual flight logs, flight data, and maintenance software systems

4. **Sensor Innovation:** Developed ideas for novel embedded sensors (acoustic, thermal) that would produce new data sources for AI/ML preventive maintenance systems, potentially extendable to Group 3 UAS and other USAF assets

5. **Proof of Concept Foundation:** Phase I work on BST's existing sensor-embedded UAS platforms and web portal demonstrated the viability of the overall concept

## Notable Details

### Stakeholder Engagement Mechanisms (Most to Least Effective)
1. **Most Effective:** Small Business Offices at Air Force Sustainment Centers (specifically Robins and Tinker AFBs)
2. **Highly Effective:** RapidX (AFRL contact working with Group 1 UAS) - introduced by Capital Factory
3. **Supporting Resources:** 
   - Spark Collider event
   - SBIR Accelerator at Capital Factory (where BST is full member)
   - IN3 (JAIC ecosystem navigation)
   - Air Force Academy stakeholders (from proposal)

### Barriers to DOD Collaboration
- USAF ecosystem complexity makes identifying correct stakeholders difficult
- Multiple potential stakeholder locations across the organization
- Particularly challenging for companies unfamiliar with USAF organizational structure

### Organizational Context
- BST is full member of Capital Factory Accelerator
- Company has established relationships with RapidX and other AFRL contacts
- Phase I involved direct outreach to Edwards AFB Small Business Office and Air Force Sustainment Centers

### Technical Foundation
- BST possesses datasets from hundreds of UAS flights (to be used for Phase II algorithm validation)
- Company has existing experience embedding sensors in UAS platforms
- Web portal infrastructure already established for maintenance data presentation