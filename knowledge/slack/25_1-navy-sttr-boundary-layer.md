# #25_1-navy-sttr-boundary-layer

## Overview
This channel manages Black Swift Technologies' Navy STTR project focused on boundary layer measurements using the S0 UAS platform. The project aims to develop atmospheric sensing capabilities for hazardous weather conditions, particularly tropical cyclones and high wind environments. Key participants include Beck Cotter, Maciej, Josh Wadler, Jun Zhang, Dan Prendergast, Jack Elston, Joshua Fromm, Joe, and Meredith Needham (Navy contact/administrator). The channel shows high activity from July 2024 through May 2026, covering Phase I completion, Phase II proposal development, and active field operations including ocean validation missions and CAT (Convective and Atmospheric Turbulence) flights.

## Key Decisions
- **July 2024**: Focused Phase 1 on tropical cyclone/high wind measurements rather than cold weather applications
- **July 2024**: Confirmed Phase I Base only scope for initial proposal  
- **October 2024**: Moved turbulence validation experiment with 2000' CAO tower to Phase II due to equipment delays
- **January 2026**: Phase II proposal and final report submitted January 5, 2026 (early to avoid server issues)
- **March 2026**: Modified Option Phase tasks approved with 4 deliverables through September 2026
- **March 2026**: Reorganized technical objectives with calibration/validation as priority #1
- **April 17, 2026**: Confirmed RH (relative humidity) sensor error resolved with post-processing fix applied to all current data; real-time correction now implemented in firmware
- **April 20, 2026**: Approved data format strategy for multi-rate sensor outputs: full-rate dataset as primary deliverable with 1 Hz downsampled version for TDR (Tropical Cyclone Data Repository) comparison
- **May 6, 2026**: Established CAT flights (2026-03-26, 2026-04-07, 2026-04-09) as primary focus for Phase I Option Progress Report analysis; confirmed 53rd Weather Wing partnership for S0 dropsondes over WHOI arrays during Phase II
- **May 7, 2026**: Data analysis underway on rain flight (1,000 m box) showing good agreement with dropsondes; P3 wind measurements showing larger discrepancies than expected, investigating potential radar data gaps for eastern region coverage needed for S0 comparisons

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
- **Wind Data Improvements**: Dual GPS heading data enabling improved wind estimation techniques for CAT flights

**Active Field Operations (April-May 2026):**
- S0 UAS ocean deployment missions coordinated through NOAA AOC (Aviation Operations Center) in Lakeland
- CAT (Convective and Atmospheric Turbulence) Flights with P3 platform:
  - **2026-03-26**: First dual S0 test (5 dropsondes deployed)
  - **2026-04-07**: Second dual S0 test with rain (9 sondes: dropsondes, Streamsondes, Sphere sondes; S0 flew at 500m and 1000m for radar comparison)
  - **2026-04-09**: Recovered S0 test with scattered rain (4 sondes)
- IRC chat coordination system for real-time field communication during flights and landing operations
- 5 test flights completed during validation window; data recovery and post-processing in progress

**Data Products (May 6-10, 2026):**
- Full-rate multi-sensor dataset from 5 test flights and CAT flights (primary deliverable maintaining 5Hz PTH, 100Hz wind, 100Hz static pressure sampling rates)
- 1 Hz downsampled version for TDR (Tropical Cyclone Data Repository) comparison and analysis
- Processed dropsonde data (post-processed with Aspen QC)
- TDR radar data from CAT flights (available for 04/07 and 04/09; 04/07 data sparse at 1-km coverage with insufficient eastern region data per May 7 findings; reprocessing by Paul/NOAA TDR team pending as of May 10)
- Streamsonde data (post-processing status: TBD on real-time QC files)

**Data Repository Structure (May 6, 2026):**
- Centralized Google Drive: Maciej's NOAA folder → 2026 subfolder → CAT subfolder for organized data management
- Contains: Dropsonde data, TDR data, Streamsonde data, S0 files with improved wind estimates

## Action Items & Commitments
**Active Commitments:**
- **Beck Cotter**: Provided Progress Report (CLIN0007) and Final Report (CLIN0007) templates by May 6, 2026; continue stakeholder engagement coordination
- **Maciej**: 
  - Analyze 5 CAT flights with focus on winds using dual GPS heading data (in progress May 6)
  - Work with James Pinto on ISARRA wind data improvements for publication (week of May 6)
  - Lead Phase II Cal/Val plan development; schedule brief meeting next week (week of May 13)
  - Compile updated CAT files with improved wind estimation techniques
  - Contribute to centralized data folder structure
  - Assess P3 wind measurement discrepancies relative to dropsonde measurements (May 7 investigation)
- **Josh Wadler**: 
  - Post-processed dropsonde data uploaded to shared folder (completed May 6)
  - Streamsonde post-processing: actively working on real-time QC files (TBD)
  - Uploaded sonde and comparison data to folder (completed May 6)
  - Support QC analysis from CAT flights
  - **Unavailable week of May 10-16, 2026** (out Friday to next Friday)
  - Will participate in Phase II Cal/Val planning upon return
  - Investigate TDR radar data gaps and salvage options for eastern region coverage needed for S0 comparisons (May 7, involving Paul from NOAA/TDR team)
- **Jun Zhang**: 
  - Sourcing dropsonde data from HRD or AOC for CAT flights (in progress May 6)
  - Radar data retrieval for 04/07 flight from raw TDR files (in progress May 6)
  - TDR data processing (uploaded to CAT folder May 6)
  - Creating centralized CAT subfolder in NOAA folder for team data organization
  - Coordinating data access and organization for analysis
  - **Following up with Paul (NOAA/TDR team) on reprocessing TDR data for better eastern region coverage** (May 10)
  - Gathering P3 altitude information for wind measurement comparison analysis
- **Team**: 
  - **Progress Report (CLIN0006) due Wednesday, June 3, 2026** - utilize templates from https://navysbir.com/links_forms.htm and Google Docs templates
  - Gather Phase II Cal/Val partnership info (WHOI arrays via 53rd Weather Wing, ocean arrays contacts from Josh W., other sources)
  - Meeting planned week of May 13, 2026 for Phase II Cal/Val plan finalization

**Phase I Option Deliverables:**