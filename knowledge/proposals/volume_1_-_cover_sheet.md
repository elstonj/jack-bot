# UAS Predictive Maintenance System Using Unsupervised Machine Learning

## Document Metadata
- **Type:** SBIR Phase II Proposal Cover Sheet
- **Client/Agency:** U.S. Air Force (AFWERX)
- **Program/Solicitation:** SBIR 2020.3 (DAF/AFWERX)
- **Date:** Submitted 2020 (document modified May 31, 2021)
- **BST Products/Systems Referenced:** 
  - Avionics monitoring system (baseline)
  - Proprietary monitoring nodes
  - Web-based delivery/dashboard platform
- **Key Personnel:** Jack Elston (last editor)

## Executive Summary
Black Swift Technologies proposes developing an advanced predictive maintenance system for small UAS using unsupervised machine learning algorithms for anomaly detection. The system addresses critical gaps in UAS maintenance practices by automating detection of subsystem failures and performance degradation across diverse flight logs without requiring labeled training data, reducing mission failures and improving safety for operations in populated areas and BVLOS environments.

## Technical Approach

### Core Strategy
BST proposes using three-tiered maintenance tracking methodology:

1. **Direct Tracking for Failures:** Rule-based detection of known failures (failed sensors, low battery, lost comms, etc.)

2. **Supervised Learning:** Statistical methods tied to labeled telemetry data to detect known anomalies:
   - Compromised/failed servo motors
   - Damaged propellers
   - Severe weather conditions (icing, etc.)
   - Outputs directly inform maintenance personnel of what requires repair/replacement

3. **Unsupervised Learning for Anomaly Detection (Primary Phase II Focus):**
   - Novel approach: Build models of normal aircraft behavior across wide range of missions and flight conditions
   - Flag aircraft as "out of family" without requiring labeled failure data
   - Enables analysis of tens of thousands of flight logs at scale without manual tagging
   - Represents first capability to perform this at operational scale

### Data Sources & Implementation
- Primary: Existing USAF-collected avionics data
- Supplemental: BST proprietary monitoring nodes installed on candidate platforms if existing data proves insufficient
- Real-time analysis and feedback capability

### User Interface
- Web-based dashboard delivery platform
- Simplified red/yellow/green diagnostic rating system for each subsystem
- Hierarchical drill-down capability for detailed subsystem information
- Designed for non-specialist operators (no highly skilled UAS technician required)

## Products & Capabilities Described

### Current Avionics Monitoring System
- Existing baseline product
- Collects telemetry data from UAS flights
- Foundation for enhanced predictive maintenance system

### Proprietary Monitoring Nodes
- Custom hardware developed by BST
- Installed aboard candidate aircraft
- Supplements telemetry data collection
- Enables real-time ML algorithm deployment

### Web-Based Maintenance Dashboard
- High-level decision-quality information presentation
- Subsystem-level diagnostics with color-coded severity
- Scalable to multiple UAS platforms
- Modular and customizable architecture

## Use Cases & Applications

### Military Applications (Primary)
- **USAF asset maintenance:** Improving readiness and reliability of small UAS fleet
- **BVLOS operations:** Enhanced safety for beyond-visual-line-of-sight missions
- **Populated area operations:** Risk mitigation for UAS flying over civilian populations
- **Airspace dominance:** Better understanding of performance inhibitors and optimal maintenance scheduling

### Commercial Applications (Dual-Use)
- Routine flights in populated areas requiring commercial UAS
- Insurance cost reduction through improved vehicle safety
- Standardized maintenance protocols for commercial UAS operators
- Does not rely solely on USAF ongoing support for long-term viability

## Key Problems Addressed

### Current UAS Maintenance Gaps
1. **Lack of onboard monitoring:** Most small UAS lack systematic monitoring or state awareness
2. **Manual maintenance schedules:** Users rely on limited owner's manual guidance
3. **Unmonitored critical subsystems:** Components like servos typically open-loop, unmonitored
4. **Unstandardized telemetry:** UAS flight log recording and storage highly inconsistent across platforms
5. **Labor-intensive data analysis:** Manual tagging of failure modes extremely time-consuming, hindering ML deployment
6. **High failure costs:** Loss of vehicle, avionics, payload; potential injury/loss of life if BVLOS or over populated areas

### Contrast with Manned Aircraft
- Manned aircraft have certified mechanics, detailed maintenance logs, redundant systems, experienced pilots
- Small UAS lack all these safeguards despite carrying fuel or explosive payloads

## Competitive Advantages & Novelty

- **Unsupervised learning at scale:** First capability to perform anomaly detection across thousands of flight logs without labeled training data
- **Aircraft behavior modeling:** Build statistical models of normal performance across diverse missions and flight conditions
- **Non-specialist interface:** Simplified dashboard accessible to operators without specialized technical training
- **Modular architecture:** Flexible system design to integrate with various UAS platforms
- **Data-agnostic:** Works with existing USAF telemetry; can supplement with proprietary monitoring nodes

## Commercial Path Forward

- Strong dual-purpose product addressing both military and commercial markets
- Commercial viability independent of USAF ongoing support
- Reduces operational costs and insurance premiums for commercial UAS operators
- Potential Phase III transition partners within DoD identified through keyword categorization

## Keywords
Machine Learning; UAS Failure; Modular Systems; Monitoring; Early Warning Diagnostics; Small UAS; Flight Logs; Unsupervised data

## Notable Details

- **Dual-use focus:** Document explicitly frames commercial applications as equally important to military applications
- **Safety emphasis:** Multiple mentions of preventing loss of life from UAS failures
- **Standardization opportunity:** Addresses lack of industry standards in UAS telemetry/maintenance
- **Scalability:** System designed to handle tens of thousands of flight logs
- **Accessibility:** Non-expert operator interface critical to adoption
- **Data efficiency:** Eliminates expensive manual data labeling/tagging bottleneck that typically constrains ML deployment