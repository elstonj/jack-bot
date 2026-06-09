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
- **June 8, 2026**: Flux analysis from 04-07 flight determined to be limited due to insufficient quality flux legs; prioritized focus on 04-09 high-rate data analysis for identifying and resolving calibration issues

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
- **Wind Calculation Method Trade-off (June 4, 2026)**: Identified technical consideration that recomputing winds from low-rate data produces noisier results due to loss of high-rate gyro data access; Maciej flagged this as potential limitation for re-analysis of CAT flights
- **Turbulence Metrics Reproducibility (June 5, 2026)**: Investigating differences in turbulence metrics between two S0 aircraft flying at same low altitude during CAT flights; Josh Wadler seeking reproducibility validation; Maciej exploring multiple post-processing approaches to improve data quality and reduce noise
- **Flux Calculation Methodology (June 8, 2026)**: Josh Wadler calculating turbulent flux components (u, v, w wind components) with mean wind subtraction per leg; focus on high-rate 04-09 data for validation; Maciej investigating whether pressure sensor bias corrections improve or worsen flux results

**Active Field Operations (April-May 2026):**
- S0 UAS ocean deployment missions coordinated through NOAA AOC (Aviation Operations Center) in Lakeland
- CAT (Convective and Atmospheric Turbulence) Flights with P3 platform (P-3 operating at 10,000 ft altitude):
  - **2026-03-26**: First dual S0 test (5 dropsondes deployed) - reprocessed data being reviewed by Josh Wadler for altitude-dependent correction validation; flux legs available for analysis
  - **2026-04-07**: Second dual S0 test with rain (9 sondes: dropsondes, Streamsondes, Sphere sondes; S0 flew at 500m and 1000m for radar comparison) - limited quality flux legs identified
  - **2026-04-09**: Recovered S0 test with scattered rain (4 sondes) - high-rate data prioritized for detailed analysis to identify and resolve calibration issues
- IRC chat coordination system for real-time field communication during flights and landing operations
- 5 test flights completed during validation window; data recovery and post-processing in progress
- Dual S0 aircraft operations at low altitude for turbulence measurement comparison (currently under analysis)
- One recovered S0 aircraft providing