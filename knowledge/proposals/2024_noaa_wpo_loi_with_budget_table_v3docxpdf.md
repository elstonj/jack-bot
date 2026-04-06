# Demonstrating and Evaluating Adaptive, Targeted UAS Sensing Capabilities at the Hazardous Weather Testbed and Using Observing System Experiments

## Document Metadata
- Type: Letter of Intent (LOI)
- Client/Agency: NOAA Office of Atmospheric Research (OAR), Weather Prediction Operations (WPO)
- Program/Solicitation: NOAA-OAR-WPO-2025-28601, Hazardous Weather Testbeds Program Priority 3 (HWT-3), with overlap to HWT-1
- Date: October 2, 2024 (submitted/last edited)
- BST Products/Systems Referenced: Hurricane eye hunter fixed-wing UAS, hybrid VTOL UAS (new), flight planning software, inter-UAS communications systems
- Key Personnel: Jack Elston (Black Swift, Co-PI), Maciej Stachura (Black Swift, Co-PI); James Pinto and Matthew Wilson (NSF NCAR, lead institution); Tammy Weckwerth (NSF NCAR, Co-I)

## Executive Summary
Black Swift Technologies and NSF NCAR propose a three-year project to develop, demonstrate, and evaluate a coordinated network of up to 10 adaptive, targeted weather-sensing UAS to fill observational gaps in the lower atmosphere for improving convection-allowing model (CAM) predictions of severe weather. The effort leverages observing system experiments (OSEs) and simulation experiments (OSSEs) to optimize UAS sampling strategies, with demonstrations at the NOAA Hazardous Weather Testbed and deployments in Colorado during spring 2027 and 2028.

## Technical Approach

**Overall Strategy:**
- Use Observing System Simulation Experiments (OSSEs) in Year 1 to determine ideal sampling strategies for a distributed UAS network
- Develop advanced flight planning software with environmental adaptation capabilities
- Conduct pilot testing near Boulder, CO (Spring 2026)
- Progressively larger operational deployments in Years 2-3 with real data assimilation
- Perform retrospective OSE studies to evaluate impact on CAM analyses and predictions

**Technical Details:**
- **Data Assimilation:** Will use MPAS-JEDI as the assimilation system (planned next dynamical core/DA system for RRFS v2), developed in collaboration with NOAA Global Systems Laboratory (GSL)
- **Modeling:** Year 1 nature runs generated using WRF; OSSE studies using MPAS-JEDI
- **UAS Flight Planning:** Black Swift to develop environmentally adaptive flight planning software that monitors moisture gradients, cap strength variations, and wind shift patterns; software will inform UAS operations based on OSSE nature runs
- **Networking:** Black Swift developing networking algorithms and inter-UAS communications for coordinated operations
- **Data Transmission:** Methods for transmitting real-time data to HWT and incorporating into operational workflow

## Products & Capabilities Described

### Black Swift UAS Systems

**Hurricane Eye Hunter (Fixed-Wing)**
- Existing system with demonstrated capability
- Successfully deployed from NOAA Hurricane Hunter Aircraft
- Proven operation in extreme atmospheric conditions: hurricane eyewalls, volcanic environments, and other severe weather
- Provides baseline technology for adaptation

**New Hybrid VTOL UAS**
- Recently developed system
- Vertical take-off and landing capability
- Fixed-wing efficiency and speed for long-range sampling missions
- Enables deployment in operationally constrained environments
- Will be primary platform for weather testbed deployments

**Flight Planning Software**
- Will be enhanced with environmental adaptation capabilities
- Will monitor pre-convective environment parameters (moisture gradients, CAPE/CIN evolution, low-level convergence)
- Autonomously determines sampling strategies based on atmospheric conditions
- Will be documented and suitable for use with any UAS fleet
- Outputs will support coordinated multi-UAS mission planning

**Inter-UAS Communications**
- Distributed network coordination capability
- Enable real-time data sharing between coordinated aircraft
- Real-time data transmission to ground systems

### Data & Observational Capabilities

- High-accuracy measurements of thermodynamic and kinematic properties of lower atmosphere
- Long-endurance flight capability for sustained monitoring
- Vertical and horizontal sampling of atmospheric variability at scales not possible with fixed-site instrumentation
- Profiling observations suitable for AWIPS ingestion
- Observations in remote areas, over water, and complex terrain where conventional observations are sparse

## Use Cases & Applications

### Primary Use Case: Severe Weather Forecasting
- Monitor pre-convective environment evolution (CAPE, CIN, low-level convergence)
- Detect moisture gradients and wind shift patterns
- Provide gap-filling observations to improve initial conditions for convection-allowing models
- Support high-impact weather event predictions (severe thunderstorms, extreme precipitation)

### Specific Test Deployments
- **Spring 2026 (Year 1):** Pilot study near Boulder, CO proving ground; testing deployment, networking, and data communications
- **Spring 2027 (Year 2):** Deployment in Colorado with up to 3 coordinated UAS in severe weather watch box; monitor low-level convergence and CAPE/CIN evolution
- **Spring 2028 (Year 3):** Campaign with at least 4 UAS distributed across wider area; integrated with HWT operations

### Geographic Focus
- High Plains region (using cases from TORUS—Targeted Observation by Radars and UAS of Supercells)
- Colorado (primary testing and deployment region due to Black Swift proximity to Boulder)
- Denver Weather Forecast Office area

### End User Integration
- NOAA Hazardous Weather Testbed (HWT) for real-time observation and feedback
- Denver Weather Forecast Office (WFO) for integration with AWIPS
- NSSL's Warn-on-Forecast System (WoFS)
- NOAA GSL's RRFS (Rapid Refresh Forecast System)

## Key Results
This is a Letter of Intent proposing future work; no results are reported. However, the document articulates expected outcomes:

**Demonstration Outcomes:**
- Operational readiness of coordinated UAS network for severe weather sampling
- Proof-of-concept integration with HWT workflow and real-time data delivery
- Stakeholder feedback on utility and operational feasibility

**Scientific Outcomes:**
- OSSE-derived optimal sampling strategies for multi-UAS networks
- Quantified impact of UAS observations on CAM analyses and forecast skill for severe weather
- Documentation of pre-convective environment evolution during high-impact weather events

## Notable Details

### Technology Readiness Level Progression
- Current: RL4 (technology demonstrated in relevant environment)
- Target by end of Year 3: RL6 for UAS systems (technology demonstrated in operational environment)
- Data assimilation component: RL7 by end of Year 3 (operational system ready for release in RRFSv2)

### Alignment with Broader Initiatives
- References WMO Aircraft-Based Observations Team global demonstration campaign (March-Sept 2024) as validation of weather-sensing UAS readiness
- Builds on prior OSE/OSSE studies indicating UAS potential to improve CAM skill
- Leverages ongoing UAS data assimilation work at NSF NCAR
- Supports NOAA goal of augmenting nationwide mesoscale observing networks
- Targets 1-km grid spacing resolution gap in next-generation regional NWP models

### Deliverables & Products
- Well-documented flight planning software module and documentation for coordinated UAS mission planning (transferable to any UAS fleet)
- Nature run datasets and OSSE software contributed to git repositories for JEDI and MPAS
- Quality-controlled UAS datasets made available for future studies
- Peer-reviewed journal publications detailing data assimilation study results
- Standardized data format documentation for HWT and operational integration

### Partnership Structure
- **Lead Institution:** NSF NCAR (James Pinto, PI; Matthew Wilson, Co-PI; Tammy Weckwerth, Co-I) — responsible for OSSE development, data assimilation studies, and case study analysis
- **Industry Partner:** Black Swift Technologies (Jack Elston, Maciej Stachura, Co-PIs) — responsible for UAS systems development, flight planning software, networking algorithms, and flight operations
- **Operational Partners:** NOAA HWT, Denver WFO, NOAA GSL, NSSL

### Budget
- **Total Project Cost:** $875,000 over 3 years
- **Year 1:** NCAR $175,000 + Black Swift $100,000 = $275,000
- **Year 2:** NCAR $150,000 + Black Swift $150,000 = $300,000
- **Year 3:** NCAR $150,000 + Black Swift $150,000 = $300,000
- Black Swift's budget increases in Years 2-3 reflecting intensified operational deployment and UAS testing phases

### Competitive Advantages Highlighted
- Black Swift's demonstrated experience operating UAS in extreme conditions (hurricanes, volcanic environments)
- Existing hybrid VTOL platform suited to operational deployment constraints
- Direct collaboration with NOAA GSL and use of MPAS-JEDI ensures pathway to operational implementation in RRFS
- NSF NCAR expertise in OSSE methodology and data assimilation research