# ReFlEx Proposal

## Document Metadata
- Type: NSF Research Proposal
- Client/Agency: National Science Foundation (NSF)
- Program/Solicitation: Not explicitly stated; likely AGS (Atmospheric and Geospace Sciences)
- Date: 6 June 2013
- BST Products/Systems Referenced: Tempest Unmanned Aircraft System (UAS)
- Key Personnel: Jack Elston (last editor); PIs mentioned include Brian Argrow, Adam Houston, Eric Frew, Conrad Ziegler, Christopher Weiss, Steven Rasmussen; affiliations with University of Colorado, University of Nebraska-Lincoln, Texas Tech University

## Executive Summary
ReFlEx (Rear Flank Downdraft Experiment) is a proposed collaborative field campaign designed to collect high-resolution observations of rear-flank downdrafts (RFDs) in supercell thunderstorms using coordinated deployments of unmanned aircraft systems, mobile radars, and surface-based instrumentation. The primary research objective is to determine the role of the RFD in tornadogenesis through testing five interconnected hypotheses about RFD structure, internal momentum surges, convergence processes, and gust-front deformation.

## Technical Approach

**Core Research Framework:**
The proposal tests a principal hypothesis that while RFDs may contribute vertical vorticity to nascent tornadoes (necessary condition), the sufficient condition for tornadogenesis is the stretching and convergence of existing rotation to tornado strength. This challenges conventional understanding and emphasizes RFD-driven convergence rather than baroclinic vorticity generation.

**Instrumentation & Deployment Strategy:**
- **Nested domain approach** (similar to VORTEX2): Meso-β-scale observations (~50 km) from 2 Doppler on Wheels (DOW) X-band radars encompassing meso-γ-scale high-resolution domain (~20 km)
- Core sensors in high-resolution domain:
  - 2 Tempest UAS with in situ thermodynamic and wind sensors
  - 2 Texas Tech Ka-band (TTUKa) mobile radars (very high-resolution wind and reflectivity)
  - Mobile mesonet (2 vehicles) for surface observations
  - Mobile GPS advanced upper air sounding system (MGAUS)
  - Balloon-borne in situ system

**Data Analysis Methodology:**
- Multi-Doppler wind synthesis from radar data
- Diabatic Lagrangian Analysis (DLA) for trajectory calculations and thermodynamic evolution (developed/tested by PI Ziegler)
- Ensemble Kalman Filter (EnKF) data assimilation approaches
- Storm-scale numerical modeling initialized with assimilated observations
- Pressure perturbation analysis from kinematic fields

**Three Deployment Modes:**
1. Slow-moving classic supercell (most versatile; tests all hypotheses)
2. Slow-moving high-precipitation supercell (adapted for heavy precipitation)
3. Fast-moving supercell (15-25 m/s; uses "tag-team" UAS operations to extend observation duration)

## Products & Capabilities Described

**Tempest Unmanned Aircraft System:**
- **What it is:** A research UAS developed by collaborative team (RECUV/UNL) capable of semi-autonomous operation with onboard autopilot
- **Composition:** 
  - Aircraft with in situ sensors (temperature, humidity, pressure)
  - Mobile ground control station
  - Tracker vehicle
  - Scout vehicle
  - Networked command and control software
- **Historical performance:** During VORTEX2 (2010), performed first-ever sampling of rear-flank gust front and rear-flank downdraft of a supercell by UAS; exceeded operational expectations
- **Proposed use in ReFlEx:** Collect high-resolution 3D thermodynamic and wind profiles above the ground within RFD outflows, across boundaries, and within internal momentum surges; execute multiple transects across storm boundaries
- **Advantages:** Capable of collecting above-ground thermodynamic data previously unavailable; complements surface observations; can operate in low-level National Airspace System with appropriate FAA authorization

**Texas Tech Ka-band (TTUKa) Mobile Radars:**
- **What they are:** Two high-frequency Ka-band mobile Doppler radars
- **Capabilities:** 
  - Very high-resolution observations of meso-γ-scale regions
  - Low data horizon (enabling initiation of backward trajectories near surface)
  - Demonstrated capability for high-resolution observations of vertical structure of thunderstorm outflows with unprecedented detail
- **Proposed use:** Map 3D wind fields with high spatial resolution within RFD and hook regions; characterize vertical motion and wind shear distribution; provide inputs for multi-Doppler synthesis and DLA

**Mobile Mesonet:**
- **What it is:** Surface-based in situ system (2 vehicles)
- **Use:** Characterize surface thermodynamic conditions, provide along-boundary wind measurements, enable trajectory analysis of surface parcels

## Use Cases & Applications

**Primary Mission:** Rear-flank downdraft (RFD) structure and tornadogenesis in supercell thunderstorms

**Research Contexts:**
- Examination of mesoscale convective phenomena in terrestrial boundary layer (land-based operations in National Airspace System)
- Severe storm research in Great Plains environment (tornado season, spring 2014)
- First-time application: Integrated use of UAS thermodynamic data within comprehensive data assimilation framework for severe storm research

**Geographic Domain:** Northeast Colorado, southwest Nebraska, northwest Kansas (approximately 90,000 km² covered by 59 FAA Certificates of Authorization; proposed consolidation to 3 COAs for ReFlEx)

**Field Deployment Period:** 1 May - 30 June 2014 (approximately 30 deployment days)

## Key Results (Not Applicable)
This is a proposal document, not a results/final report. No empirical results are presented. The document references prior NSF-supported work (CoCoNUE, VORTEX2, IHOP) with historical findings but focuses on proposed research methodology.

## Five Specific Research Hypotheses Addressed

1. **Hypothesis 1 (Outflow Wake Dynamics):** Outflow wake dynamics can produce relatively warm RFD outflows and facilitate tornadogenesis by introducing mesocyclonic/inflow air into the outflow, enabling parcels to converge and amplify at the surface.

2. **Hypothesis 2 (Rear Flank Internal Surges):** An important cause of rear-flank internal surges (RFIS) is the intrusion of environmental and mesocyclonic momentum into the RFD outflow driven by outflow wake dynamics; two modes proposed (cold surge and warm surge).

3. **Hypothesis 3 (RFIS Temperature):** RFIS that are too cold undercut the low-level mesocyclone; RFIS that are too warm produce insufficient convergence. Optimal temperature range supports tornadogenesis.

4. **Hypothesis 4 (Frontogenesis at Left-Flank Convergence Boundaries):** Dynamic frontogenesis along left-flank convergence boundaries (LFCB) near the hook echo stem amplifies convergence of angular momentum toward the circulation center through coupling of mass field and kinematics.

5. **Hypothesis 5 (Gust-Front Deformation):** Deformation of the rear-flank gust front (RFGF) in environments with strong low-level vertical shear results in along-boundary gradients in vertical motion that tilt quasi-horizontal vortex lines, generating positive vertical vorticity near the occlusion point.

## Notable Details

**FAA/Regulatory Achievements & Status:**
- RECUV/UNL team has obtained 65 FAA Certificates of Authorization (COAs) for UAS operations
- Successfully operated Tempest during CoCoNUE (2007-2008) and VORTEX2 (2009-2010) field campaigns
- Established cooperative relationship with Denver Air Route Traffic Control Center
- October 2011 debriefing led to FAA approval for consolidated "nomadic" operations COA covering entire ReFlEx domain (March 2013)
- Negotiated authority to operate 2 UAS simultaneously within single COA/NOTAM area (previously prohibited)
- Obtained approval for operations up to 5,000 ft ceiling (1,524 m)
- Proposed single NOTAM with 1-hour lead time requirement for multi-state operations domain

**Scientific Partnerships & Infrastructure:**
- Collaboration with National Severe Storms Laboratory (NSSL): Commitment letter from director Dr. Stephen Koch for mobile mesonet deployment
- Integration with NSF Lower Atmospheric Observing Facilities for DOW and MGAUS provision
- Situational Awareness for Severe Storms Intercept (SASSI) platform (NSSL-hosted server) for real-time coordination
- Multi-institutional coordination: University of Colorado (RECUV), University of Nebraska-Lincoln, Texas Tech University

**Prior NSF Support Summary (Last 5 Years per proposal):**
1. **CoCoNUE (SGER, $99,995, 2007-2008):** First UAS observations of mesoscale phenomena in lower atmosphere over land in National Airspace System
2. **IHOP Data Assimilation ($174,917, 2007-2011):** Boundary layer and convection initiation; 4 peer-reviewed publications, 1 M.S. thesis
3. **VORTEX2 UAS Development ($377,742, 2009-2011):** Tempest UAS development; first-ever RFD sampling by UAS; 5 peer-reviewed publications, 1 Ph.D. dissertation
4. **Texas Tech Ka-band Radar Study ($330,865, 2010-2013):** 3D tornado vortex structure; 1 peer-reviewed publication, multiple conference presentations, 1 M.S. thesis, 1 Ph.D. dissertation

**Broader Impacts:**
- Training component: ~7 undergraduate students and ~15 graduate students in field deployments
- 5 graduate student theses to be based on ReFlEx data
- 2 undergraduate research projects through UCARE program (Pepsi Endowment)
- Integration into existing courses: Radar meteorology (Houston, Weiss); Meteorological Field Experiments (Weiss); aerospace engineering curricula (Argrow, Frew)
- Publication in peer-reviewed journals, conference presentations

**Project Management:**
- PI Houston (UNL) as overall project manager
- Decentralized "collaboration of semi-autonomous teams" strategy (adapted from VORTEX2)
- Dedicated project coordination channels and SASSI real-time data integration
- Year 3 workshop planned (Lincoln, NE) for presentation of results
- Derived data products (quality-controlled data, multi-Doppler winds, DLA thermodynamic fields) shared among all team members

**Safety Philosophy:**
- Crew safety prioritized above mission objectives
- Experienced PIs and senior staff (Rasmussen, Houston, Weiss, Ziegler; Wurman, Kosiba, Robinson from Center for Severe Weather Research)
- Redundant communication systems
- First aid/CPR training for all personnel
- Operations domain positioned west of eastern Great Plains to maximize visibility and situational awareness