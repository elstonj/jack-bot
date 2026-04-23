# #25_1-navy-sttr-boundary-layer

## Overview
This channel manages Black Swift Technologies' Navy STTR project focused on boundary layer measurements using the S0 UAS platform. The project aims to develop atmospheric sensing capabilities for hazardous weather conditions, particularly tropical cyclones and high wind environments. Key participants include Beck Cotter, Maciej, Josh Wadler, Jun Zhang, Dan Prendergast, Jack Elston, Joshua Fromm, and Joe. The channel shows high activity from July 2024 through April 2026, covering Phase I completion, Phase II proposal development, and active field operations including ocean validation missions.

## Key Decisions
- **July 2024**: Focused Phase 1 on tropical cyclone/high wind measurements rather than cold weather applications
- **July 2024**: Confirmed Phase I Base only scope for initial proposal  
- **October 2024**: Moved turbulence validation experiment with 2000' CAO tower to Phase II due to equipment delays
- **January 2026**: Phase II proposal and final report submitted January 5, 2026 (early to avoid server issues)
- **March 2026**: Modified Option Phase tasks approved with 4 deliverables through September 2026
- **March 2026**: Reorganized technical objectives with calibration/validation as priority #1
- **April 17, 2026**: Confirmed RH (relative humidity) sensor error resolved with post-processing fix applied to all current data; real-time correction now implemented in firmware
- **April 20, 2026**: Approved data format strategy for multi-rate sensor outputs: full-rate dataset as primary deliverable with 1 Hz downsampled version for TDR (Tropical Cyclone Data Repository) comparison

## Projects & Initiatives
**Navy STTR Boundary Layer Measurements Project (Award: N6833535C0270)**
- Phase I Base completed January 2026 with kick-off document, progress report, and final deliverables
- Phase I Option awarded January 26, 2026, funding released March 20, 2026
- Phase II proposal submitted February 20, 2026 (24-month base $1M + 24-month option $1M with 1:1 cost match)
- Current focus: S0 sensor characterization, turbulence measurements, wave height detection, air-sea interactions

**Technical Development Areas:**
- S0 sensor suite: PTH (Vaisala) at 5Hz, wind at 100Hz, additional static pressure sensor at 100Hz
- Cold weather specifications: -40°C to -60°C operation capability
- De-ice heater development for standalone system with COTS process controller
- Ocean validation missions in 4 phases testing sensing, algorithms, wave height, QC, and AI autonomy
- **Humidity Sensor Correction**: Vaisala humidity error identified and corrected with post-processing fix; real-time correction now active in firmware (as of April 17, 2026)

**Active Field Operations (April 2026):**
- S0 UAS ocean deployment missions coordinated through NOAA AOC (Aviation Operations Center) in Lakeland
- IRC chat coordination system for real-time field communication during flights and landing operations
- 5 test flights completed during validation window; data recovery and post-processing in progress

**Data Products (April 20, 2026):**
- Full-rate multi-sensor dataset from 5 test flights (primary deliverable maintaining 5Hz PTH, 100Hz wind, 100Hz static pressure sampling rates)
- 1 Hz downsampled version for TDR (Tropical Cyclone Data Repository) comparison and analysis

## Action Items & Commitments
**Active Commitments:**
- **Beck Cotter**: Coordinate stakeholder engagement, obtain letters of support, schedule TPOC meetings
- **Maciej**: Complete sensor characterization analysis, lead proposal writing, implement humidity sensor corrections; coordinate S0 landing operations during field missions; post-process data from 5 test flights; **deliver full-rate and 1 Hz downsampled data products by end of day April 20, 2026**
- **Josh Wadler**: Develop turbulence metrics code, support data assimilation efforts, coordinate postdoc budget; obtain corrected post-processed data from 5 test flights; **prefer full-rate data format for analysis**
- **Jun Zhang**: Lead data assimilation work with Navy model, budget postdoc position; troubleshoot IRC connectivity issues with Lakeland AOC; **requested 1 Hz version of dataset for TDR comparison**
- **Dan Prendergast**: Complete CONOPS section development
- **Joshua Fromm/Joe**: Support IRC connectivity and field operations coordination; provide status updates on data corrections and validation

**Phase I Option Deliverables:**
- Phase II Cal/Val Plan (due May 20)
- Additional cal/val with NOAA data/ISARRA (due June 20)  
- De-ice heaters design (due July 20)
- Stakeholder engagement (due September 20)

## Client & External References
**Primary Navy Contact:**
- Josh Cossuth (TPOC) - Navy stakeholder providing feedback and reviews

**Collaborators:**
- NOAA: Dropsonde comparisons, CAO tower access in Colorado; AOC (Aviation Operations Center) in Lakeland for field operations coordination
- NASA Glenn IRT: Tunnel access for Phase 2 testing (authorization letter needed)
- NCAR: Terry Hock and Holger providing Vaisala humidity correction formulas
- Kevin Lacroix: Naval Meteorology and Oceanography Command
- Nick Pawlenko: Letter of support provider
- WHOI: Ocean measurements collaboration
- USF: Moorings west of Florida for testing
- OOI buoys: Turbulence comparison data
- TDR (Tropical Cyclone Data Repository): Target repository for 1 Hz downsampled data products
- Lakeland AOC data tech "Mach": Support for field operations connectivity

## Recurring Topics & Themes
- **Technical Performance**: S0 sensor characterization and validation against established platforms
- **Environmental Requirements**: Cold weather performance specifications and de-icing capabilities  
- **Data Quality**: Humidity sensor corrections, turbulence algorithms, automated QC processes
- **Multi-Rate Sensor Data Management**: Handling different sampling rates (5Hz PTH, 100Hz wind, 100Hz static pressure) in WMO-compliant formats; dual data product strategy for full-rate and downsampled outputs
- **Validation Planning**: Ocean arrays, NOAA buoys, tower comparisons for Phase II testing
- **Stakeholder Engagement**: Regular TPOC meetings, letter of support collection, operational transition planning
- **Field Operations Coordination**: Real-time communication systems for S0 deployment missions

## Important Resources
**Documentation:**
- Meeting notes: https://docs.google.com/document/d/1UiSBC5bAeXPg5TmXkQCgDjfXaVGQ0cApGp7pMXogH0U/edit
- Work plan gantt chart: https://docs.google.com/spreadsheets/d/12BKEpLk5307ZSQYOEnzULTR-TKdUv2ZP5Cp72o9fzgw/edit
- Kickoff brief template: https://docs.google.com/presentation/d/12CdhWT4xQpLgt3OGQCEe99Fzdr94ZLVnDpWchSBYMS4/edit
- IRC connectivity instructions (shared via Google Doc by Jun Zhang)

**Data Sources:**
- NDBC buoy data: https://www.ndbc.noaa.gov/obs.shtml
- NOAA CAO tower: 3-second raw data and 1-minute QC'd data at 30m, 100m, 508m
- NOAA dropsonde data from Hurricane Gabrielle flights
- TDR (Tropical Cyclone Data Repository): Target for 1 Hz downsampled dataset distribution

**Field Operations:**
- IRC Server: irc.omao.noaa.gov (updated April 2026, replaces previous IP 140.90.144.132:6697)
- Port: 6697
- Use case: Real-time ground coordination during S0 flight operations

## Recent Activity
**April 8-9, 2026**: Active S0 ocean validation mission preparation with field operations support. Team coordinated real-time communication systems for landing operations. Identified IRC server connectivity issue (