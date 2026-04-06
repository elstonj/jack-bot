# AFX236-DPCSO1 Direct-to-Phase II Technical Volume: An All-Weather Multi-Mission UAS

## Document Metadata
- **Type:** SBIR Phase II Direct-to-Phase II Proposal Technical Volume
- **Client/Agency:** U.S. Air Force (DAF) / Department of Defense
- **Program/Solicitation:** AFX236-DPCSO1 – Direct-to-Phase II Call for Innovative Defense-Related Dual-Purpose Technologies/Solutions with a Clear DAF Stakeholder Need
- **Date:** May 2, 2023 (template date); Proposal submitted 2023
- **Proposal Number:** F2D-9055
- **CAGE Code:** 6PGF9
- **BST Products/Systems Referenced:** S2 UAS, S3 UAS (VTOL variant), SwiftCore avionics system, SwiftTab UI, Vision Processing Unit (VPU, Intel Myriad-X based)
- **Key Personnel:** Beck Cotter (last editor), Ed Kase (EKase Consulting LLC – business development consultant)
- **End-User Organizations:** 319 Reconnaissance Wing (319 RW), North Spark Defense Laboratory (NSDL) at Grand Forks Air Force Base; Lt Col Michael Dunn (NSDL Director), Capt Ashley Maestas (Director of Innovation), MSgt Jason Carey, MSgt Harland, others

---

## Executive Summary

Black Swift Technologies proposes to develop an all-weather, multi-mission small unmanned aircraft system (sUAS) based on the S3 VTOL platform for Air Force base perimeter surveillance and incident response. The system will integrate autonomous flight software, artificial intelligence/machine vision for automated target detection, cold-weather readiness modifications, and integration with existing Air Force ground control systems (ATAK). The effort addresses a critical capability gap identified by Grand Forks AFB, where current sUAS solutions fail in extreme North Dakota winter conditions; BST claims only 3 of 13 "Blue List" aircraft completed missions despite favorable conditions, whereas the S3 has heritage flying in extreme environments (-10°F+, 50-knot winds, precipitation/icing).

---

## Technical Approach

### Overall Strategy
BST proposes to adapt its commercially-developed S3 VTOL UAS platform (derivative of the proven S2) into a ruggedized, autonomous base security system through four main modifications:

1. **Payload Integration:** Install an EO/IR gimbal sensor (Trillium HD45 or similar) with onboard machine vision processing for automated object detection/classification
2. **Ground System Integration:** Develop software interfaces to transmit sensor data and control commands via Android Tactical Assault Kit (ATAK) or similar existing Air Force systems
3. **Cold Weather Readiness:** Design hardware/system modifications allowing the S3 to remain outdoors in ready-to-launch state in temperatures ≤-10°F
4. **Workload Reduction:** Implement automated preflight checks, system readiness monitoring, post-flight checks, and mission planning tools reducing setup time to <1 minute

### Technical Foundation
- **Flight Management System:** SwiftCore avionics – a modular architecture with open interfaces designed by UAS experts (not open-source collection); enables subsystem redundancy, automated sensor control, and preventative maintenance monitoring
- **Vision Processing:** Onboard Intel Myriad-X VPU running machine learning neural networks for:
  - Single-shot detector networks for people/object detection
  - Semantic segmentation networks for safe landing site identification
  - GPS-denial capability (jamming/spoofing detection, alternative navigation for GPS-denied recovery)
- **Autonomy:** Advanced flight control for strong-wind operation, automated recovery procedures, minimal operator input required

### Key Technical Characteristics of S3
- **Maximum Takeoff Weight:** 33 lbs
- **Maximum Flight Time:** 90 minutes
- **Maximum Payload:** 5 lbs
- **Cruise/Max Speed:** 45 mph / 100 mph
- **Configuration:** Fixed-wing VTOL (vertical takeoff and landing)
- **Environmental Heritage:** S2 has flown to -10°F in Greenland, 50+ knot winds, precipitation/icing; beyond visual line-of-sight (25+ miles) at 7,000 ft altitude

---

## Products & Capabilities Described

### S2 UAS (Commercial Platform)
- **Status:** In production; commercially available 3+ years
- **Use:** Scientific research missions (volcano monitoring, wildfire assessment, hurricane observation, arctic gas monitoring, soil moisture mapping)
- **Customers:** NASA, NOAA, USGS, university research centers
- **Proven Performance:** 104 missions in Northern Greenland (summer 2023); NASA airworthiness certification issued; extreme weather operations documented
- **Key Advantage:** Reliable, modular, designed for harsh environments; all components US-manufactured

### S3 UAS (VTOL Derivative – Proposed Defense Variant)
- **Status:** Late-stage prototype development; planned Q4 2023 commercial release; early-adopter sales underway
- **Differences from S2:** Vertical takeoff/landing capability, same sensors/avionics core, payload compatible with S2 missions
- **Commercial Traction:** Purchase order from University of Maryland Eastern Shore for 2 aircraft + support contract ($150K total) for winter cargo delivery operations
- **Proposed Defense Configuration:** Base security variant with integrated EO/IR payload, neural network threat detection, ATAK integration, cold-weather modifications
- **Specifications:** Same as S2 (33 lbs MTOW, 90-min flight time, 5 lb payload)
- **Target Unit Cost:** <$50K per aircraft (2-5x cheaper than DoD-specific sUAS alternatives)

### SwiftCore Avionics System
- **Architecture:** Modular with well-defined open interfaces between intelligent nodes
- **Capabilities:**
  - Subsystem redundancy for safety
  - Automated health monitoring and preventative maintenance detection
  - Autonomous sensor-driven control
  - Third-party component integration
  - GPS-denied navigation (jamming/spoofing detection, alternative recovery navigation)
- **Maturity:** Field-proven across multiple aircraft types and difficult applications

### Vision Processing Unit (VPU)
- **Hardware:** Intel Myriad-X based
- **Software:** Machine learning neural networks running onboard
- **Applications in This Effort:**
  - Single-shot detector: people/object detection in perimeter surveillance
  - Semantic segmentation: safe landing site identification (engine-out scenarios)
  - Extensible to additional threat/object classification

### Ground Control & Data Transmission
- **Current Configuration:** Commercial COTS radio, Android tablet, SwiftTab UI
- **Proposed Modification:** Integration with Android Tactical Assault Kit (ATAK) – both military and civilian versions – for command/control and real-time video/threat data relay
- **Additional Features:** Onboard sensor data transmission, higher-level threat classification data (not just raw video), minimal operator training required

---

## Use Cases & Applications

### Primary Use Case: Air Force Base Perimeter Security & Incident Response
- **Location:** Grand Forks Air Force Base, North Dakota (extreme weather environment: -30°F, 45+ mph sustained winds recorded in past year)
- **Mission Requirements:**
  - 5,000+ acre installation perimeter coverage
  - 24/7/365 operation capability
  - Rapid response to anomalous activity
  - Data transmission to security forces
  - Reduced personnel workload vs. traditional patrols
- **Scale Potential:** Applicable to majority of Air Force bases globally; specific emphasis on bases vulnerable to extreme weather (Eielson AFB, Malmstrom AFB identified)

### Secondary Defense Applications (Identified in Feasibility Study)
- Space Force Blue Sky multi-mission sUAS for Space Force Base security, antenna field surveillance
- Autonomous sUAS mission integration across Air Combat Command (ACC)
- Emergency management coordination with security forces

### Non-Defense Commercial Applications (Existing & Projected)
- **Current:** Volcano monitoring, wildfire assessment, hurricane/tornado observation, arctic environmental surveys, soil moisture/gas monitoring, coastal monitoring
- **Projected:** Agriculture (crop health, irrigation monitoring, weed identification), construction/mining inspections, infrastructure inspection, precision agriculture
- **Customers (Existing):** NASA, NOAA, USGS, university research centers, commercial research entities
- **New Markets (S3 Enhancement Potential):** Cargo delivery in extreme conditions (demonstrated by Univ. of Maryland Eastern Shore pre-purchase); disaster response; remote site access

---

## Phase II Technical Objectives & Key Results

### Technical Objective 1: Perimeter Search Capability Development
**Deliverable:** Integration and validation of EO/IR payload (Trillium HD45 gimbal) with machine vision processing

**Key Results (Measurable):**
- Payload selection document with pros/cons analysis of multiple sensor options
- Performance metrics: sensor range vs. target size, coverage area per flight/per hour
- **Demonstration of 90% success rate** in detecting and identifying pre-placed test object in subscale perimeter search equivalent using machine learning-based real-time classification

### Technical Objective 2: Data Transmission to Operators
**Deliverable:** Real-time anomalous activity alert integration with ATAK or similar Air Force interface

**Key Results:**
- Demonstrated integration of S3 sensor data into ATAK interface
- Transmission of anomalous activity with <measured lag> to operators
- Continuous data transmission over full mission duration via ATAK

### Technical Objective 3: All-Weather Operation
**Deliverable:** Hardware/software modifications enabling sustained operation in extreme North Dakota conditions

**Key Results:**
- **Successful mission in temperatures <-10°F** (on-site or within 50 miles of Grand Forks AFB)
- Documented lowest operating temperature threshold
- Maximum sustained wind speed and wind gust limits for takeoff/landing validated
- Maximum precipitation/snow operability parameters validated

### Technical Objective 4: Workload Reduction
**Deliverable:** Reduced man-hours for mission execution, setup, flight, and post-flight operations

**Key Results:**
- Documented baseline workload metrics from current AFB UAS operations
- Ranked areas for autonomy enhancements
- **One-page assessment of UAS equipment and personnel requirements** for daily perimeter security operations with S3
- Quantified personnel workload reduction vs. baseline

---

## Key Results (Phase I Feasibility Study)

### Customer Discovery & Engagement
- **Total Federal Government contacts attempted:** 64
- **Successful contacts:** 39 (31 email, 8 phone, 1 in-person)
- **Unique Federal organizations reached:** 9 of 10 targeted
- **Unique USAF organizations contacted:** 37

### Empowered End-User Identified
- **Organization:** 319 Reconnaissance Wing / North Spark Defense Laboratory (NSDL), Grand Forks AFB
- **Key Contacts:** Lt Col Michael Dunn (NSDL Director), Capt Ashley Maestas (Director of Innovation)
- **Mission Context:** UAV ISR critical to national defense; Security forces cover 5,000+ acre installation with 2,700 on-base residents, 6,500 daily transients, $3B in aircraft/radar assets
- **Current Pain Points:** 
  - Limited sUAS reliability in winter (Grand Forks has evaluated 40+ UAS systems)
  - Weather-dependent operations (North Dakota temperature/wind extremes)
  - High personnel overhead for perimeter patrols
  - Absence of centralized database for workflow management
  - Existing Blue List aircraft: only 3 of 13 completed missions (dismal 23% success rate)
- **Customer Roadmap:** NSDL will facilitate follow-on socializations across Air Combat Command; Phase III funding strategy via 3400 funding, AFWERX TACFI/STRATFI programs ($350K-$15M matching); long-term integration into Integrated Base Defense Security System (IBDSS) program of record

### Roadmap Output
BST created development roadmap and timeline for Phase II initiatives and multi-organization collaboration framework with 319 SFS (Security Forces Squadron), 319 OSS (Operations Support Squadron), 319 AMXS (Aircraft Maintenance Squadron).

---

## Phase II Work Plan & Deliverables

### Task Structure (7 Major Task Areas)

**Task 1: Requirements & Interface Definition**
- Current S3 specifications documentation
- Pain-point analysis for AFB UAS operator/maintenance workload
- Autonomy, AI, and payload requirements research
- Communications requirements (frequencies, bandwidth, telemetry, C2)
- Requirements/verification document
- Interface control document