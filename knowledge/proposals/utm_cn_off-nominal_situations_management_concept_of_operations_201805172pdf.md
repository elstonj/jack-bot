# UTM Communications and Navigation Off-Nominal Situations Management: Concept of Operations & Requirements

## Document Metadata
- **Type:** Proposal / Concept of Operations & Requirements Document
- **Client/Agency:** NASA UAS Traffic Management (UTM) Project; NASA-FAA Research Transition Team
- **Program/Solicitation:** NASA UTM Communications and Navigation Working Group
- **Date:** May 17, 2018 (presentation date); document finalized June 13, 2018
- **BST Products/Systems Referenced:** None explicitly mentioned
- **Key Personnel:** Jaewoo Jung (NASA, jaewoo.jung@nasa.gov); Maciej Stachura (last editor)

## Executive Summary
This document presents early-stage requirements and concept of operations for managing off-nominal situations (communications loss, navigation failure, safe landing capability loss) within the NASA UAS Traffic Management system. The proposal establishes a structured framework using ICAO emergency phases (Uncertainty, Alert, Distress) to ensure predictable operator behavior and safe UAS operations, particularly for flights over people and property. Requirements are designed for formalization and presentation to the FAA side of the NASA-FAA Research Transition Team.

## Technical Approach
The document proposes a two-tier off-nominal situation management framework:

**Overall C&N Off-Nominal Situation Management (9 requirements):**
- Operators must detect and mitigate loss of communication with aircraft (means of detection and mitigation steps to be communicated to USS)
- Operators must detect and mitigate loss of aircraft onboard navigation (means of detection and mitigation steps to be communicated to USS)
- Operators must collect off-nominal situation data for lessons learned

**Operations Over People and Property Specific Management (12 requirements):**
- UAs must have safe landing capability ("landing without causing detrimental impact to people and property")
- Operators must detect loss of safe landing capability and communicate detection means to USS
- Operators must define mitigation steps for safe landing capability loss and communicate these to USS
- Emergency phase declarations (Uncertainty, Alert, Distress) must be made based on safe landing capability status:
  - **Uncertainty Phase (SHOULD):** Off-nominal situation mitigated with intact safe landing capability
  - **Alert Phase (MUST):** Off-nominal situation being mitigated with compromised safe landing capability
  - **Distress Phase (MUST):** Off-nominal situation poses imminent danger to people or property
- Operators must collect off-nominal situation data

Requirements use IETF RFC2119/RFC8174 terminology (MUST, SHOULD, MAY, etc.) with detailed justifications and verification methods (Test, Demo).

## Products & Capabilities Described

### Safe Landing Capability
- **Definition:** Landing of Unmanned Aircraft without causing detrimental impact to people and property
- **Components:** Requires onboard sensors, actuators, safe landing execution algorithms, and safe landing capability health monitoring algorithms
- **Reference Implementation Referenced:** NASA's Safe2Ditch crash management system (autonomous emergency management system for small UAVs that uses remaining control authority and battery life to reach safest ditch location using intelligent algorithms and machine vision)

### Safe Landing Capability Monitoring
Six concurrent monitoring areas identified:
1. **Navigation Health:** Onboard navigation accuracy and integrity
2. **C2 (Command & Control) Health:** Communication link status
3. **Environmental Detection Health:** Sensor systems detecting ground hazards
4. **External Surveillance:** Vehicle position information from non-onboard sources
5. **ADAC Health:** Attitude Determination and Control system status
6. **Resources:** Remaining range to safe-to-land location, thrust for vertical landing, fuel/battery reserves

These six areas together determine which emergency phase (Nominal, Uncertainty, Alert, Distress) the operation is in.

## Use Cases & Applications

**Primary Use Case:** UAS operations over people and property requiring safe landing capability assurance

**Secondary Use Cases:** 
- General UAS operations requiring communication and navigation robustness
- Operations subject to dynamic constraints and directives that may change during mission execution
- Multi-operator UTM environments requiring coordination between individual operators and Unmanned Traffic Management Services (USS)

**Operational Context:**
- Assumes higher complexity operations (TCL3 and above) requiring automated off-nominal detection and contingency management
- Envisions adjacent USSs sharing off-nominal situation data and declarations for coordinated response
- Assumes Service Delivery Service Providers (SDSP) providing communications and navigation quality of service forecasting

## Key Results
This is a requirements/concept document rather than a research report. No experimental results are presented. However, it establishes:

- **21 formal requirements** (labeled UTM-OSM.05 through UTM-OSM.90) with stated justifications and verification approaches
- **Structured emergency phase framework** adapted from ICAO Annex 12 for UAS operations
- **Safe landing capability monitoring model** with six concurrent health monitoring domains
- **Feedback collection mechanism** via Google survey (deadline June 1, 2018) from at least 8 organizations

Document notes intent to incorporate feedback and provide updated version to NASA-FAA Research Transition Team by June 29, 2018, with potential publication as NASA Tech Memo.

## Notable Details

1. **Scope Clarification:** Document explicitly states it provides "no further, generalized insight into UTM" and assumes audience familiarity with UTM concepts; intended for technical working group review, not general audience.

2. **ICAO Framework Adoption:** Requirements harmonize with existing ICAO Convention on International Civil Aviation (Annex 12) emergency phases, providing regulatory alignment pathway.

3. **Safe2Ditch Reference:** Document references NASA's Safe2Ditch system as reference implementation for autonomous crash management, available via NASA patent LAR-TOPS-243 and YouTube demonstration.

4. **USS Integration:** Requirements emphasize USS (Unmanned Traffic Management Service Supplier) visibility into operator capabilities, mitigation procedures, and emergency declarations—implying USS role in coordinating safe resolution of off-nominal situations.

5. **Data Collection Requirement:** All operational scenarios include mandatory off-nominal situation data collection to support lessons learned and continuous operational safety improvement.

6. **Verification Methods:** Requirements use two primary verification approaches:
   - **Test:** For absolute (MUST) requirements and capability verification
   - **Demo:** For recommended (SHOULD) requirements and coordination effectiveness

7. **Document Status:** Explicitly marked as "early version" with requirement labels subject to change during future harmonization; positioned as foundational step toward FAA-NASA coordination on operational UAS regulations.

8. **External Surveillance Inclusion:** Notably includes external surveillance (non-onboard position information) as component of safe landing capability monitoring, indicating integration with ground-based or infrastructure-assisted position determination.