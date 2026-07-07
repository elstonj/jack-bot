# #sbir-hurricane

## Overview
The #sbir-hurricane channel is the primary workspace for Black Swift Technologies' SBIR Hurricane project, focused on developing the S0 unmanned aircraft system for hurricane reconnaissance missions. The channel is highly active with extensive technical discussions, operational updates, and mission planning spanning 2020-2026. Key participants include Joshua Fromm, Jack Elston, Maciej, Danny Troke, Dan Prendergast, Alex Lomis, Nate, Sam Hild, Beck Cotter, Paige Smith, and Meredith Needham.

## Key Decisions

**Aircraft Design & Configuration:**
- User panel positioned on bottom of NOAA S0 for easier access through outer tube (June 2020)
- Selected T-Motor F60 for propulsion due to discontinued KDE motor (September 2020)
- Switched from Castle ESC to 36A version for improved reliability (November 2020)
- Spring steel antenna wrapped around fuselage confirmed as optimal design (November 2020)
- Wing pivot system designed to "fall away" after deployment to save weight (December 2020)
- Deployment timing set at 1s door open detection, 3s later chute deploy, 5s later tube jettison, 5s later aircraft release (updated July 6, 2026; previously April 2021: 5 seconds parachute flap, 10 seconds tube release)

**Sensor & Electronics:**
- Selected SF20 laser altimeter over SF22 due to Ardupilot/PX4 integration issues (January 2021)
- Eliminated datalogging requirement after presentation feedback (April 2021)
- Selected MLX90614ESF-DCH thermal sensor per Terry's recommendation (December 2021)
- Direct soldering battery/ESC to AP due to space constraints (November 2021)
- Dual USB-A ports on front panel instead of USB-C for GCS (May 2022)

**Manufacturing & Components:**
- 50/50 cost split between Air Force and Hurricane for KMac tubes (June 2020)
- Lee selected for deployment tube machining at $700 NRE, $95 per additional tube (March 2022)
- Aluminum caps chosen over 3D printed ones after high-Q deployment failure (May 2022)
- Switched to Samsung INR21700-50S cells replacing Panasonic NCR18650GA (February 2024)
- Decision to use 76gsm wing skins instead of 160gsm for 50g weight savings (October 2024)
- **Winsource removed from future supplier selection due to defective PMXB120EBE parts and other questionable components (June 29, 2026)**

**Ground Control Station Operations (April 2026):**
- Single operator per aircraft confirmed as acceptable by NOAA operational rules (April 2026)
- GCS firmware updates for dual-channel radio control implemented (April 2026)
- Use of Channel 1 designated for flight operations over Avon Park (April 2026)
- Channel 1 selected for operational use after RF cable replacement on Channel 2 (April 2026)

**Ground Control Station Silkscreen Labeling (May 7, 2026):**
- Radio channel designation decided as "RADIO A / RADIO B" to minimize confusion with other numbering schemes (May 7, 2026)
- Jack Elston approved RADIO A/B nomenclature over alternatives (RADIO 1/2, CH 1/2, etc.) (May 7, 2026)

**Ground Control Station Design & Procurement (May 7-8, 2026):**
- Joshua Fromm to review and modify ground station parts procurement list before finalization (May 7, 2026)
- RF connector modification implemented for radio compatibility (May 7, 2026)
- Jack Elston's suggested quantities approved as baseline for testing + 2 upcoming builds with overage on cheap parts (May 7, 2026)
- Joshua Fromm confirmed procurement list would only require cable change; most major components (USB hub, power brick, etc.) can be ordered (May 8, 2026)
- Jack Elston submitted openups and batteries for purchase to avoid duplication (May 8, 2026)
- Joshua Fromm updated comprehensive procurement spreadsheet (2026 DUAL tab) with all components except stocked materials like ring terminals and clikmates (May 8, 2026)

**Ground Control Station Operational Handover Planning (May 7, 2026):**
- Discussion initiated regarding whether GCS units being produced are intended for NOAA operational handover (May 7, 2026)
- Proposal suggested: duplicate testing station at BST for troubleshooting issues NOAA may encounter with remotely operated stations (May 7, 2026)
- Status: Under consideration for decision (May 7, 2026)

**Higher-Rate Data Recording Capability (May 27, 2026):**
- NOAA requested modification to ground stations to enable higher-rate data availability, potentially for operational use as early as 2026 season (May 27, 2026)
- Jack Elston planning to integrate this modification into new GCS builds (May 27, 2026)
- Plan to develop P3 simulator at BST for testing prior to implementation (May 27, 2026)

**Humidity Sensor Configuration (April 2026):**
- Vaisala RSS421 heating mode confirmed as critical for accurate readings (April 2026)
- New PSNS firmware with corrected humidity reference validation implemented (April 8, 2026)
- Battery tracking logging enabled on all PSNS boards for sleep mode diagnostics (April 8, 2026)
- Sensor boom compatibility identified as critical - older booms incompatible with newer sensors (April 10, 2026)
- Reconditioning cycle confirmed effective for correcting humidity sensor bias (April 17, 2026)

**Display Aircraft Production (April 21-22, 2026):**
- Approved production of 4 display S0 units: 2x 2025 models for near-term delivery (end of May target), 2x 2026 models for early-mid July delivery (April 21, 2026)
- Display units to ship without tripods/mounts/carry cases in cardboard tubes or boxes, shipped folded (April 22, 2026)
- Special thicker-skin wings to be commissioned for display models to improve appearance (April 21, 2026)
- Wing springs and antenna NOT to be pre-installed on display units to reduce shipping damage risk (April 22, 2026)
- All 4 display S0 units approved to include tripods: 2 units shipping end of May + 2 units for early-mid July (May 7, 2026)
- Jack Elston confirmed all display aircraft should have tripods included (May 7, 2026)
- Tripod and mount solution added to 2x display units at ~$200 cost (5 min labor) (April 22, 2026)
- Delivery deadline: June 5, 2026 for DC event requirement; shipment to AOC or HQ for redistribution (April 22, 2026)

**Inventory Management (April 23, 2026):**
- SASCWATCH has one S0 left over from previous season; decision made not to allow NOAA to use it (April 23, 2026)
- Jack Elston confirmed awareness of leftover aircraft status (April 23, 2026)

**Stock Inventory Build (May 6, 2026):**
- Jack Elston initiated procurement of 20 additional S0 aircraft units to maintain stock inventory for operational opportunities (May 6, 2026)
- Decision made to use current 2026 configuration without waiting for 2027 mods (May 6, 2026)

**Meeting Structure Decision (June 3, 2026):**
- Jack Elston proposed discontinuing regular S0 meetings in favor of Slack-based coordination (June 3, 2026)
- Joshua Fromm approved the change to Slack-only coordination (June 3, 2026)

**Sparv Dropsonde Partnership Discussion (June 9, 2026):**
- Decision deferred on Sparv dropsonde drop payload concept - insufficient funding currently; other R&D with NOAA prioritized instead (June 9, 2026)
- Sparv sensor integration as secondary comparison to