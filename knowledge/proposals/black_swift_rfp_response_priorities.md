# Black Swift RFP Response Priorities

## Document Metadata
- Type: Internal priority document / RFP response planning memo
- Client/Agency: NOAA
- Program/Solicitation: FY27 NOAA UMS (Unmanned Aircraft Systems)
- Date: 2026-05-05
- BST Products/Systems Referenced: S0 (uncrewed systems), STM32MP1 compute modules
- Key Personnel: Beck Cotter (last editor), Sanabia (partnership/contact for C-130 integration)

## Executive Summary
Black Swift Technologies outlines three prioritized technical efforts for a NOAA UMS proposal: scaling multi-UAS hurricane reconnaissance operations with finalized data pipelines, integrating AI-driven autonomy and adaptive sampling for extended on-station time, and expanding beyond hurricane season to cover Atmospheric River events and extended-season operations via C-130 deployment. Total estimated budget: $2.8M–$3.6M over the two-year period of performance.

## Technical Approach

### Priority 1: Multi-UAS Reconnaissance Scaling and R2O Hardening
- **Baseline Achievement**: Successful dual-S0 drone deployment in March 2026
- **Proposed Expansion**: Scale to three or more simultaneous S0 systems per P-3 aircraft sortie
- **Data Pipeline Hardening**: Finalize integration with NHC and EMC for operationally viable data distribution (AirOps/AWIPS2/HDOB BUFR formats)
- **High-Frequency Data Delivery**: Provide 10 Hz meteorological data for HAFS turbulence parameterizations

### Priority 2: AI-Driven Adaptive Sampling and Autonomy
- **Core Technology Transfer**: Port TMML (terrain/mission matching logic) and IT-RRT (Integrated Task-based Rapidly-exploring Random Tree) planner from Navy STTR program onto onboard STM32MP1 compute modules
- **Energy Harvesting Integration**: Leverage NASA atmospheric energy-harvesting algorithms to extend on-station time
- **Adaptive Sampling**: Enable drones to concentrate flight paths and data collection in high-information regions of storms using AI decision-making
- **Prior Experience Base**: Built on edge-AI flight experience from ECS-DoT (Environmental Compliance and Sustainability - Department of Transportation) project

### Priority 3: Atmospheric River and Extended-Season Expansion
- **Geographic/Seasonal Scope**: Extend operations beyond standard Atlantic hurricane season to West Coast Atmospheric River events and other high-impact weather phenomena
- **Deployment Platform**: Utilize 53rd Weather Reconnaissance Squadron (WRS) C-130 aircraft
- **Integration Approach**: "No-mod" (no modification) Pelican-case setup for easy C-130 integration; operationalization pathway brokered by Sanabia
- **Data Pipeline**: Feed AR and extended-season meteorological data into GFS and HRRR forecasting models via established EMC data pipeline

## Products & Capabilities Described

### S0 Uncrewed Systems
- Tactical hurricane reconnaissance platform
- Demonstrated capability for dual-deployment from P-3 aircraft (March 2026)
- Proposed for scaling to 3+ simultaneous launches per sortie
- Capable of carrying meteorological sensors for 10 Hz data collection

### STM32MP1 Compute Modules
- Onboard edge-compute platform for autonomous flight decision-making
- Proposed host for ported TMML/IT-RRT autonomy planners
- Enables real-time adaptive sampling without ground control dependency

## Use Cases & Applications

1. **Hurricane Reconnaissance**: Multi-platform coordinated sampling within tropical cyclones; data support for NHC operations and HAFS model improvements
2. **Atmospheric River Monitoring**: Extended-season West Coast operations for high-impact precipitation events
3. **Extended-Season Weather Phenomena**: Beyond traditional hurricane season operations
4. **High-Resolution Turbulence Characterization**: 10 Hz data for parameterization model improvements

## Budget Estimates (Rough Order of Magnitude)
- Multi-UAS Reconnaissance Scaling & R2O Hardening: $1.4M–$1.8M
- AI-Driven Adaptive Sampling & Autonomy: $800K–$1.0M
- Atmospheric River & Extended-Season Expansion: $600K–$800K
- **Aggregate ROM**: $2.8M–$3.6M (two-year period of performance)

## Notable Details

- **R2O Focus**: Emphasis on Research-to-Operations transition; data operationalization with NHC and EMC is a stated requirement
- **Technology Reuse**: Leverages prior Navy STTR-funded autonomy development and NASA energy-harvesting work
- **Minimal Integration Burden**: C-130 pathway uses modular "no-mod" Pelican-case approach to reduce aircraft integration complexity
- **Multi-Model Data Integration**: Same EMC data pipeline used for both hurricane and AR/extended-season operations (GFS, HRRR)
- **Demonstrated Success**: Proposal builds on proven March 2026 dual-S0 deployment achievement, positioning this as incremental scaling rather than new capability demonstration