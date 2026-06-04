# #25_1-navy-sttr-boundary-layer

## Overview
This channel manages Black Swift Technologies' Navy STTR project focused on boundary layer measurements using the S0 UAS platform. The project aims to develop atmospheric sensing capabilities for hazardous weather conditions, particularly tropical cyclones and high wind environments. Key participants include Beck Cotter, Maciej, Josh Wadler, Jun Zhang, Dan Prendergast, Jack Elston, Joshua Fromm, Joe, and Meredith Needham (Navy contact/administrator). The channel shows high activity from July 2024 through June 2026, covering Phase I completion, Phase II proposal development, and active field operations including ocean validation missions and CAT (Convective and Atmospheric Turbulence) flights.

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
- **May 18, 2026**: Confirmed P-3 altitude at 10,000 ft during CAT flights; validated for TDR analysis comparison with S0 wind data
- **May 20, 2026**: Team attending SASCWATCH meeting with focus on identifying calibration opportunities for flux and sea surface state measurements (Maciej, Jun Zhang, and Jack Elston joining remotely; Josh Wadler attending in person)
- **May 26, 2026**: Scheduled Phase II Cal/Val plan meeting for Thursday May 28 at 11 AM ET; Progress Report (Task O.2) in good shape; Cal/Val plan (Task O.1) prioritized for discussion
- **May 27, 2026**: Phase II Cal/Val plan meeting rescheduled to 11:30 AM ET (moved from 11:00 AM due to Jun Zhang's conflict); confirmed attendance: Maciej and Josh Wadler
- **May 28, 2026**: Phase II Cal/Val plan meeting held; Maciej shared working document for review
- **June 1, 2026**: Interim report (Progress Report, Task O.2) due June 3, 2026 by 3 PM Mountain time (5 PM Eastern) with early submission recommended per Meredith Needham to avoid technical difficulties
- **June 2, 2026**: S0-63 flight wind data errors identified and resolved: firmware error in 5-hole probe center port reading and new magnetometer calibration method issues corrected; post-correction wind speeds now show good agreement with dropsonde data (4.2-4.4 m/s consistent across 3 box segments)
- **June 2, 2026**: Approved P-3 overflight of OOI array as near-term validation approach with potential additional flight hours available in July
- **June 3, 2026**: Updated TDR data confirmed to cover test region for 04-07 flights; noted temporal smoothing in TDR analyses from multi-leg averaging causing lower wind speed readings compared to S0 and dropsondes (per Josh Wadler technical explanation)

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
- **5-Hole Probe & Magnetometer Calibration (June 2, 2026)**: S0-63 flight analysis revealed firmware error in 5-hole probe center port and issues with new magnetometer calibration method; both issues resolved with post-processing corrections showing improved agreement with dropsonde measurements

**Active Field Operations (April-May 2026):**
- S0 UAS ocean deployment missions coordinated through NOAA AOC (Aviation Operations Center) in Lakeland
- CAT (Convective and Atmospheric Turbulence) Flights with P3 platform (P-3 operating at 10,000 ft altitude):
  - **2026-03-26**: First dual S0 test (5 dropsondes deployed)
  - **2026-04-07**: Second dual S0 test with rain (9 sondes: dropsondes, Streamsondes, Sphere sondes; S0 flew at 500m and 1000m for radar comparison)
  - **2026-04-09**: Recovered S0 test with scattered rain (4 sondes)
- IRC chat coordination system for real-time field communication during flights and landing operations
- 5 test flights completed during validation window; data recovery and post-processing in progress

**Data Products (May 6-10, 2026):**
- Full-rate multi-sensor dataset from 5 test flights and CAT flights (primary deliverable maintaining 5Hz PTH, 100Hz wind, 100Hz static pressure sampling rates)
- 1 Hz downsampled version for TDR (Tropical Cyclone Data Repository) comparison and analysis
- Processed dropsonde data (post-processed with Aspen QC)
- TDR radar data from CAT flights (confirmed coverage for 04/07 as of June 3, 2026; earlier data gaps in eastern region resolved through reprocessing)
- Streamsonde data (post-processing status: TBD on real-time QC files)

**Data Repository Structure (May 6, 2026):**
- Centralized Google Drive: Maciej's NOAA folder → 2026 subfolder → CAT subfolder for organized data management
- Contains: Dropsonde data, TDR data, Streamsonde data, S0 files with improved wind estimates

**Phase II Cal/Val Plan (Task O.1)**
- Working document created and shared by Maciej on May 28, 2026: https://docs.google.com/document/d/1FBAJUxPo6J2_zkStvdUN6M6cff3619yzRSb0g3MYB9k/edit?tab=t.0
- Team actively developing calibration and validation