# Demonstrating Adaptive, Targeted UAS Sensing Capabilities at the Hazardous Weather Testbed and with Observing System Experiments

## Document Metadata
- Type: Letter of Intent (LOI) with budget
- Client/Agency: NOAA Office of Atmospheric Research (OAR), Weather and Physical Oceanography (WPO)
- Program/Solicitation: NOAA-OAR-WPO-2025-28601, Hazardous Weather Testbeds Program Priority 3 (HWT-3); also addresses HWT-1 Priority
- Date: Prepared September 23 – October 1, 2024; to be submitted
- BST Products/Systems Referenced: S0 hurricane eye hunter, hybrid VTOL WxUAS (new)
- Key Personnel: Jack Elston (PI, Black Swift), Maciej Stachura (Co-PI, Black Swift); NCAR lead: James Pinto, Matthew Wilson; Tammy Weckwerth (NCAR-EOL)

## Executive Summary
This proposal seeks to develop and demonstrate a rapidly deployable coordinated network of up to 10 weather-sensing Uncrewed Aircraft Systems (WxUAS) to fill observational gaps in the lower atmosphere for improved severe weather forecasting and convection-permitting model (CPM) predictions. Black Swift and NCAR will leverage adaptive sampling algorithms, observing system simulation experiments (OSSEs), and data assimilation work to optimize WxUAS deployment strategies, with field demonstrations at the Hazardous Weather Testbed in Years 2 and 3.

## Technical Approach

### Overall Strategy
- **OSSE Framework (Year 1):** NCAR will develop nature runs using WRF and perform OSSEs using MPAS-JEDI to optimize WxUAS sampling strategies for high-impact convective weather events across the High Plains
- **Flight Simulations:** Black Swift will conduct flight simulations using OSSE nature runs to determine expected flight conditions and inform flight planning software logic
- **Pilot Study (Spring 2026):** Local flight-testing near Boulder, CO to test WxUAS deployment, networking, and real-time data communications
- **Field Deployments (Spring 2027, Spring 2028):** Coordinated WxUAS flights into severe weather watch boxes to monitor low-level convergence, CAPE/CIN evolution; data fed to HWT in real-time
- **Iterative Improvement:** Year 3 will incorporate lessons learned from HWT participant feedback for final campaign

### Technical Development Areas
- Adaptive sampling algorithms (monitoring moisture gradients, cap strength variations, wind shift patterns)
- Inter-UAS communications and networking algorithms
- Flight planning software enhancements
- Real-time data transmission methods to HWT and SPC
- Data assimilation integration with MPAS-JEDI/RRFSv2 (next operational CPM model)

## Products & Capabilities Described

### Black Swift S0 Hurricane Eye Hunter
- **What it is:** Adaptive weather-sensing UAS currently deployed from NOAA Hurricane Hunter Aircraft
- **Demonstrated capabilities:** Flight in hurricane eyewall and other severe atmospheric conditions (including volcanic environments)
- **Readiness level:** Already operational for hurricane missions

### Black Swift Hybrid VTOL WxUAS (New Development)
- **What it is:** Newly developed hybrid uncrewed aircraft combining vertical takeoff/landing (VTOL) capability with fixed-wing efficiency
- **Key features:** 
  - Vertical launch and landing capability
  - Efficiency and speed of fixed-wing flight for long-range sampling
  - High-accuracy measurements
  - Long-endurance flight capability
- **Development trajectory:** Project aims to advance technology from RL4 (Technology Demonstrated in Lab) to RL6 (Technology Demonstrated in Relevant Environment) over three years
- **Mission capability:** Coordinated fleet operations with inter-UAS communications

### Flight Planning Software
- **Proposed outputs:** Well-documented module supporting coordinated WxUAS mission planning; designed to be adaptable for any fleet of UAS
- **Inputs:** OSSE nature runs and flight simulation data
- **Functionality:** Optimization of sampling strategies based on atmospheric conditions

## Use Cases & Applications

### Primary Use Case: Severe Weather Observation
- **Mission:** Fill observational gaps in lower atmosphere during high-impact convective weather events
- **Target parameters:** Low-level convergence, CAPE (Convective Available Potential Energy), CIN (Convective Inhibition)
- **Geography:** High Plains region (case studies from recent high-impact convective weather events)
- **Scale:** Sub-1 km grid spacing (commiserate with next-generation NWP models)
- **Time-critical:** Pre-convective environment sampling in severe weather watch boxes

### Operational Integration
- **Denver Weather Forecast Office:** Primary coordination point
- **Hazardous Weather Testbed (NOAA):** Integration with HWT operations and forecaster feedback
- **Storm Prediction Center (SPC):** Real-time data transmission
- **Regional Weather Forecast Offices:** Potential expansion to other WFOs for targeted severe weather guidance

### Data Assimilation Application
- **Model:** MPAS-JEDI (planned next operational CPM model for RRFSv2)
- **Goal:** Improve initial conditions and analyses for convection-allowing models
- **Expected outcome:** More accurate predictions of high-impact weather events

## Key Results
Not applicable — this is a proposal, not a results report. However, anticipated outcomes include:
- Demonstration of coordinated WxUAS observing system capability
- OSSE results for ≥5 high-impact convective weather cases
- Assessment of technical readiness and stakeholder feedback (Spring 2027 HWT deployment)
- Quantified impact of targeted WxUAS observations on severe weather prediction skill
- Operationally-ready flight planning software and networking algorithms

## Notable Details

### Alignment with Broader Initiatives
- Aligns with NOAA's goal to augment mesoscale observing networks
- Leverages WMO Aircraft Based Observations Team recent global demonstration campaign (March–Sept 2024) showing commercial WxUAS readiness for operational meteorology
- Addresses critical gap: 1 km grid spacing in next-generation regional NWP models but lack of commensurate in-situ observations

### Technology Readiness & Demonstration
- Black Swift's proven flight experience in extreme conditions (hurricane eyewall, volcanic environments) demonstrates operational maturity
- Three-year project structure explicitly designed to progress from RL4 to RL6
- Coordination with NOAA Global Systems Laboratory for data assimilation work

### Budget
| | NCAR | Black Swift | Total |
|---|---|---|---|
| Year 1 | $149,405 | $100,000 | $249,405 |
| Year 2 | $170,758 | $150,000 | $320,758 |
| Year 3 | $155,573 | $150,000 | $305,573 |
| **Total** | **$475,736** | **$400,000** | **$875,736** |

### Deliverables & Dissemination
- Well-documented flight planning software and coordination algorithms (shareable with any UAS fleet)
- Updated nature run datasets and OSSE software to be incorporated into git repositories for JEDI and MPAS
- Quality-controlled UAS datasets made available for future research
- Peer-reviewed publications on data assimilation impact studies

### Stakeholder Engagement
- Denver Weather Forecast Office and HWT are critical collaborators and end users
- Forecaster feedback loops built into Years 2 and 3
- Direct integration with operational forecast workflows

---

**Note:** Document contains bracketed annotation [a] questioning JEDI acronym definition ("Maybe define this acronym? I couldn't find what the 'JEDI' portion stands for online"). This was left unresolved in the source material.