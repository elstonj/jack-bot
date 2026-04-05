# #logparse-website

## Overview
This channel tracks the development and operation of SwiftWeb (logparse), a platform for storing, processing, and analyzing flight logs from multiple aircraft types (S2, E2, Flamewheel, Dronetag, ground stations). The system converts binary logs to NetCDF format for storage in S3 and provides web-based visualization and querying of flight data.

**Key Participants:** Ben Busby (infrastructure/backend), Maciej (SDK/parsing), Jack Elston (flight operations), Dan Prendergast (plotting/analysis), Ethan Domagala (testing), Austin (original code)

**Activity Level:** Highly active with consistent development and maintenance. Covers approximately 2.5 years (Sep 2020–Apr 2026).

## Key Decisions

- **Nov 2022**: Transitioned from storing zipped binary logs to NetCDF format in S3 for better data accessibility and standardization
- **Nov 2022**: Upgraded production server from m5-large to m5-xlarge; downgraded dev to burst instance (cost optimization)
- **Apr 2025**: Launched new SwiftWeb platform (dev.swiftweb.bst.aero) to consolidate and replace legacy logparse sites
- **Dec 2025**: Migrated site from dev to production at https://swiftweb.bst.aero
- **Made site publicly accessible** (removed VPN restriction); later added organizational account access controls
- **Sep 15, 2025**: Decided to migrate plotting tools from matplotlib to Plotly/Dash for better web interactivity and independence from notebooks
- **Oct 2025**: Approved migration of all logs from 14 organizations from old logparse site to new SwiftWeb platform

## Projects & Initiatives

### SwiftWeb Platform
**Status:** Production (launched Dec 2025 at https://swiftweb.bst.aero)
- Consolidated replacement for legacy logparse.bst.aero and dev.logparse.bst.aero
- Supports S2, E2, Flamewheel, Dronetag, and ground station logs
- Passed 2000 flights milestone (Mar 11, 2025)
- Features: flight visualization, 3D flight paths with Google Maps tiles, custom SQL queries on flight metadata, WMO NetCDF generation for S0 aircraft

### Ground Station Logs (GCS) Processing
**Status:** Operational (since Sep 2024)
- Development began Aug 2022 for hurricane/aircraft recovery scenarios
- Implemented SWIG C++/Python wrapper for SDK integration (completed Sep 2024)
- Automatic flight splitting based on sys_init packets
- Known issues: PAYLOAD_DATA_CHANNEL packets often have checksum failures; TELEMETRY_CONTROL data generation in progress
- Outputs NetCDF files per flight in same format as autopilot logs

### WMO NetCDF Generation
**Status:** Feature-complete, optimization pending (as of Jan 2026)
- Automated conversion of S0-VTOL and S0-AD flight logs to WMO NetCDF format
- Three new Python libraries pushed by Maciej (Jun 27, 2025)
- Available on production site with "Generate WMO netCDF" option
- Development site: http://dev.swiftweb.bst.aero/logparse/nc/wmo_test/
- Currently runs in foreground; planned conversion to background task processing pending Maciej's updates

### Comms Version Support
**Status:** Ongoing maintenance
- Most recent: 3.21.0 (Jul 2024), Payload channels (Apr 2024)
- S0 sensors and MHP packets integrated (Oct 2023–Mar 2025)
- SENSORS_GNSS_RTCM packet (ID #14) added Jan 2025
- SENSORS_RTK_HEADING packet (ID #59) support requested (Mar 20, 2026)

### Plotting Tools Migration
**Status:** Decision made, implementation pending (as of Jan 2026)
- Switching from matplotlib to Plotly/Dash for interactive web-based visualization
- Code migration to log-utils repo to allow independent updates by Maciej
- Benefit: Avoids browser/notebook compatibility issues

### MHP Processing Site
**Status:** Operational (brought back online Aug 11, 2025)
- URL: https://logparse.bst.aero/mhp
- Underwent brief maintenance (Sep 12, 2025)

## Action Items & Commitments

### Ben Busby
- ✅ Update packaging instructions for mhp_coeff_2023_02_23.mat file handling (completed)
- ✅ Switch to more reliable transactional email service for verification (completed May 22, 2025)
- ✅ Implement log deletion functionality for BST users (completed Sep 26, 2025)
- **Pending:** Switch WMO generator to background task processing (awaiting Maciej's modifications)
- **Pending:** Add parsing support for SENSORS_RTK_HEADING packet (ID #59) (requested Mar 20, 2026)
- **Pending:** Investigate S1-19 flight NAN value issues (assigned Apr 1, 2026)
- **Pending:** Revisit migration of old flights from legacy site to new platform (in progress as of Oct 2025)

### Maciej
- ✅ Complete automation of WMO netCDF generation code (planned for weekend following Jun 27, 2025)
- ✅ Investigate and resolve S0-64 flight separation issues (completed Jan 26, 2026)
- ✅ Identify protocol issue in S10019 flight (PAYLOAD_S0_SENSORS packet missing) (completed Mar 19, 2025)
- ✅ Update log_utils repo for new SDK (completed Nov 2025)

### Jack Elston
- ✅ Retry S2 Costa Rica flights upload (May 23, 2025)
- ✅ Confirm organizations for migration (completed Oct 22, 2025)
- ✅ Request removal of invalid log_S00076_log_2 (completed Sep 26, 2025)

### Dan Prendergast
- **Pending:** Database schema expansion with PIC, takeoff time, land time columns (requested Jan 20, 2026)

## Client & External References

### NASA Accounts Added (May 2025)
- william.o.wade@nasa.gov (NASA Ames)
- isaac.e.anderson@nasa.gov (NASA Ames)
- tyler.willhite@nasa.gov (NASA Langley)
- jay.m.tomlin@nasa.gov (NASA Ames)

### Organizations with Site Access
Free access provided to: NREL, Alerion, INSTAAR, UVA, NASA, UMES (added Aug 2025)

### Organizations Migrated from Legacy Site (Oct 2025)
INSTAAR, WCE, AboveAndBeyondAS, GeoTech, CureCUV, NOAA-TDD, JakeAeroic, AeroIC, VerticalGeo, Alerion, Howard University, NREL, UVA, Rainmaker, ERAU

## Recurring Topics & Themes

### NetCDF Conversion Performance & Reliability
- Initial conversion slow (10–15 min per file) due to CONTROL_COMMAND variable size; improved dramatically with new parser (Sep 2024)
- Wind data missing from initial batches due to type mismatch (fixed Dec 2022)
- Logs frequently stuck in conversion pipeline; resolved by restarting netcdf generation
- Ongoing packet parsing issues requiring version-specific fixes

### Data Quality & Packet Parsing Issues
- Regular discovery of missing or malformed packets (PAYLOAD_DATA_CHANNEL checksums, SENSORS_RTK_HEADING, S0_SENSORS)
- False flight separation due to system time resets (resolved Jan 26, 2026)
- Partial uploads or file corruption from Slack data transfer

### Infrastructure & Cost Management
- Monthly AWS costs ~$150–200/month (two m5-large servers + S3); colocation alternative explored at $49/month for 1U
- Recurring storage capacity issues requiring upgrades
- Database connection pool exhaustion on old site (Apr 2025)
- Server segfault issues in netcdf python library (resolved via upgrade)

### User