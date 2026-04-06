# AFWERX AF_X24.7 CSO Technical Volume: Advanced Air-Deployed UAS for Hurricane Sampling

## Document Metadata
- **Type:** SBIR Phase I Proposal (Technical Volume 2)
- **Client/Agency:** U.S. Air Force (Department of the Air Force)
- **Program/Solicitation:** AFWERX SBIR Topic AFX247-PCSO1
- **Proposal Number:** FX247-PCSO1-0481
- **CAGE Code:** 6PGF9
- **UEI:** C2J3K9NRE3L3
- **Date:** Submitted 2024 (presentation last modified Feb 2025)
- **BST Products/Systems Referenced:** S0 UAS, S2 UAS, SwiftCore flight management system
- **Key Personnel:** 
  - Jack Elston, Ph.D. (CEO, Founder, Principal Investigator)
  - Maciej Stachura, Ph.D. (Chief Technology Officer, Controls & Wind Estimation)
  - Josh Fromm (Lead Engineer, Mechanical Engineering & Platform Development)

---

## Executive Summary

Black Swift Technologies proposes to modify and integrate its S0 UAS (a high-TRL, air-deployable platform originally developed for NOAA) for U.S. Air Force hurricane sampling missions aboard C-130 aircraft operated by the 53rd Weather Reconnaissance Squadron. The effort focuses on enhancing the existing system to meet DOD cybersecurity and network integration requirements while maintaining its proven capability to collect real-time atmospheric data (3D winds, pressure, temperature, humidity, sea surface temperature) from the lower boundary layer and eyewall of tropical cyclones—regions critical for storm intensity forecasting but historically under-sampled by traditional methods.

---

## Technical Approach

### Core Technology
The **S0 UAS** is a disposable, autonomous, air-deployed unmanned aerial system specifically engineered for boundary layer observations in extreme weather. Key technical features:

- **Autonomous Flight & Targeted Sampling:** Active navigation through storm via pre-programmed or adaptive flight paths (unlike passive dropsondes)
- **Extended Data Collection:** Continuous operation within storm environment for prolonged periods vs. brief dropsonde descent
- **Proprietary SwiftCore Flight Management System:** Enables real-time data streaming and secure communication with deploying aircraft
- **Purpose-Built for Extreme Conditions:** Designed to operate in high wind speeds and turbulence of hurricanes

### Proposed Phase I Work

**Task 1: System Integration Requirement Development**
- Identify modifications to S0 UAS and flight control station for C-130 deployment
- Determine autonomous flight software changes for hurricane sampling and integration with C-130 command systems
- Assess deployment mechanism compatibility

**Task 2: Cybersecurity Compliance Requirement Development**
- Identify required DoD-level cybersecurity protocols
- Conduct vulnerability analysis to meet DOD standards
- Define secure communication and data transfer requirements

**Task 3: Flight Profile Requirement Development**
- Develop process for custom flight profiles for autonomous navigation in hurricane boundary layer and eyewall
- Determine airborne deployment system modifications

**Task 4: Stakeholder Identification & Requirements Modification**
- Interview current stakeholders (53rd Squadron, NOAA AOML, etc.) to understand operational benefits
- Identify additional stakeholders and potential post-Phase II customers
- Secure MOU signers for Phase II proposal

**Task 5: Final Reporting**
- Comprehensive feasibility documentation including SF 298 and DD Form 882

---

## Products & Capabilities Described

### S0 UAS
**What it is:** A small, autonomous, disposable air-deployed unmanned aircraft system optimized for atmospheric sampling in extreme weather.

**Proposed use:** Deployed from USAF C-130 aircraft to autonomously collect continuous atmospheric data from within hurricane boundary layer and eyewall.

**Key sensors:**
- Flush-air sensing nose cone (high-rate 3D wind vectors)
- In-situ atmospheric probe (pressure, temperature, humidity)
- Surface temperature sensors
- Wave height measurement capability
- Long-range communications link
- Integration with current NOAA systems

**Performance specifications:**
- Autonomous operation in hurricane wind conditions (validated through deployments in Tammy 2023; Ernesto, Francine, Helene, Milton 2024)
- Extended data collection duration vs. dropsondes
- Low-cost, rapid scalability for manufacturing
- Modular design allowing rapid deployment

### SwiftCore Flight Management System
- Proprietary system enabling real-time data streaming
- Secure communication with deploying aircraft
- Customizable for mission-specific needs
- Supports secure DoD integration (future ISR/swarming capabilities mentioned)

### S2 UAS (Referenced for Related Work)
- Soil moisture mapping platform (NASA-funded, commercialized)
- Advanced autonomous operations and low-altitude data collection expertise

---

## Use Cases & Applications

### Primary Use Case: Hurricane Reconnaissance
- **End-user:** USAF 53rd Weather Reconnaissance Squadron
- **Mission:** In-situ atmospheric data collection from tropical cyclones
- **Operational Benefit:** Autonomous collection of continuous, high-resolution data from lower boundary layer and eyewall—regions where storm intensity is determined

### Current Operational Context
The 53rd Squadron currently deploys disposable dropsondes from C-130 aircraft. These provide only discrete data points during brief descent, with limited spatial/temporal coverage and significant operational risk to manned crews.

### Secondary/Future Applications
- **ISR (Intelligence, Surveillance, Reconnaissance):** Small, deployable platform with potential for camera integration
- **Swarming/Cooperative Control:** Autonomous flight capabilities enable multi-platform operations
- **Cargo Drop Support:** Could deploy ahead of drop zone to measure 3D wind columns (mentioned as alternative to ground-based measurements)

### Scientific/Civilian Applications
- NOAA hurricane boundary layer observations and forecasting
- University research collaboration (University of Colorado noted)
- Commercial market potential: offshore energy, insurance, emergency management for improved hurricane forecasting

---

## Key Results (Previous Deployments)

### Validation Through NOAA Partnership
**Project:** NOAA Boundary Layer Observations (S0 UAS Development)
- **Status:** Ongoing since 2018
- **Achievement:** Validated S0 through deployment into multiple high-wind hurricanes:
  - Hurricane Tammy (2023)
  - Hurricanes Ernesto, Francine, Helene, Milton (2024)
- **Partner POC:** Dr. Joe Cione, NOAA AOML (305-361-4400)
- **Key Finding:** S0 successfully provides continuous atmospheric measurements critical for hurricane intensity forecasting

### Commercialization Revenue (BST Track Record)
- **S2 UAS sales:** $362,732 (soil moisture mapping)
- **Soil moisture mapping services:** $284,004
- **Methane emission detection services:** $46,088
- **Total SBIR-funded commercialization:** >$690,000

---

## Technical Merit & Scientific Advancement

### Problem Addressed
Current hurricane sampling tools (disposable dropsondes) provide only limited data from discrete points during descent, hampering:
- Accurate hurricane model initialization/validation
- Storm intensity, trajectory, and impact forecasting
- Safety of manned aircraft operations

### Advancement Over Baseline
The S0 UAS addresses critical gaps by providing:
1. **Continuous, High-Resolution Data:** Extended duration in storm vs. brief dropsonde descent
2. **Autonomous Operation:** Reduces crew risk; enables targeted flight paths through storm regions
3. **Higher Data Density:** More data points in critical boundary layer and eyewall regions
4. **Extended Spatial Coverage:** Longer operational duration allows larger area monitoring

### Scientific Basis
References cited (Bryan et al. 2017; Cione et al. 2016; Elston et al. 2015) demonstrate:
- Dense, prolonged boundary layer data collection improves hurricane intensity forecasts
- Previous UAS platforms (Coyote) successfully operated in extreme conditions (Hurricane Edouard 2014)
- Small fixed-wing UAS are viable for meteorological sampling

---

## Competitive Landscape & Differentiation

### Current Alternatives & Limitations
**Disposable Dropsondes:**
- Limited data points during descent
- Brief collection window (minutes)
- Expose manned crews to hazardous conditions
- Insufficient temporal/spatial resolution for model initialization

### BST Competitive Advantages
- **Proven technology:** Validated in 5+ actual hurricanes (2023-2024)
- **Cost-effectiveness:** Disposable platform with low manufacturing costs, scalable production
- **Performance balance:** Longer duration, higher resolution than dropsondes; lower cost and simpler than larger UAS platforms
- **Operational fit:** Designed for C-130 integration; modular design for rapid deployment
- **Modularity:** Adaptable for ISR, swarming, and other defense applications

### Market Position
No identified competing systems offering similar combination of:
- Disposable design optimized for hurricane conditions
- Extended autonomous operation
- Cost-effective scalability
- Integration with military platforms

---

## Notable Details

### Defense Relevance & Strategic Value
- **Strategic Capability Area:** Enhanced weather intelligence for operational planning and safety
- **Risk Reduction:** Reduces exposure of manned crews to extreme weather
- **Decision Support:** Improved hurricane forecasts inform defense disaster management and military operations planning
- **Previous DoD Funding:** BST received SBIR funding for ground-launched 3D wind measurement UAS and machine learning maintenance scheduling software, demonstrating prior DoD relationship and cybersecurity awareness

### Stakeholder Engagement Plan
- **FAA/Certification Authorities:** Beyond Visual Line of Sight (BVLOS) operations approval
- **DoD Cybersecurity Specialists:** Secure communication protocol implementation
- **Test & Acquisition Authorities:** Phase II validation pathway
- **53rd Weather Reconnaissance Squadron:** Primary end-user for requirements validation
- **NOAA AOML:** Ongoing collaboration for scientific validation

### Transition Strategy to DAF
1. **System integration & testing** with DAF engineers; ground/flight validation during Phase II
2. **Cybersecurity compliance** with DoD protocols
3. **Operational deployment & training** for DAF personnel
4. **Ongoing support & development** for evolving operational needs

### Team Expertise
- **Jack Elston (PI/CEO):** 15+ years UAS development; Ph.D. Aerospace Engineering (CU Boulder); led projects for NOAA/NASA hurricane, tornado, wildfire sampling
- **Maciej Stachura (CTO):** Ph.D. Aerospace Engineering; expertise in control systems, wind estimation, National Airspace System integration
- **Josh Fromm (Lead Engineer):** Mechanical engineering, platform development for harsh/storm conditions

### Phase I Timeline & Deliverables
- **Kickoff:** Within 30 days of contract award
- **Preliminary Report:** Following initial integration/testing (documenting feasibility progress)
- **Final Report:** With SF 298 and DD Form 882 (technical feasibility results, Phase II roadmap)
- **Stakeholder Travel:** Estimated $1,107 for PI travel to Keesler AFB, Biloxi, MS (April 2025) for collaboration with 53rd Squadron

### Foreign National Disclosure
- **Maciej Stachura:** Canadian national with U.S. Green Card/Lawful Permanent Resident status; involved in technical discussions and customer feasibility research (Tasks 1-4)

### Commercialization Pathway
**Government Market:**
- USAF 53rd Weather Reconnaissance Squadron (primary customer)
- NOAA hurricane forecasting operations
- Other federal weather reconnaissance needs

**Commercial Market:**
- Offshore energy companies
- Insurance industry (hurricane risk assessment)
- Emergency management agencies
- Environmental monitoring services

---

## Summary Assessment

This proposal demonstrates BST's ability to transition a proven, validated atmospheric research platform (S0 UAS) into a military-operational system meeting DoD cybersecurity and operational requirements. The technical approach is well-grounded in actual hurricane deployments (2023-2024), strong government partnerships (NOAA, NASA, prior AFWERX funding), and clear understanding of end-user needs (53rd Squadron). Phase I focuses on feasibility and requirement development, with clear pathways to Phase II testing and operational transition. The S0 offers significant advancement over existing dropsondes while maintaining lower cost and complexity than alternative UAS platforms.