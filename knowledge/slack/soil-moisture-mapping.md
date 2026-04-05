# #soil-moisture-mapping

## Overview

The **#soil-moisture-mapping** channel documents Black Swift Technologies' comprehensive development and deployment of a soil moisture mapping system using Unmanned Aerial Systems (UAS). The project evolved from initial concept in mid-2020 to a fully operational commercial system by 2025, involving integration of multiple sensor payloads (Altum spectral cameras, LDCR radiometers, NDVI sensors, thermal sensors) onto DJI E2 aircraft.

**Key Participants:**
- **Jack Elston** - Primary project lead, firmware/software architecture, overall direction
- **Maciej Olszewski** - Field operations, data collection, project management
- **Joshua Fromm** - Hardware design, 3D printing, mechanical integration, logistics
- **Jake Sahli** - Software development, Python rewrite, data processing
- **Danny Troke** - Hardware assembly, field testing, troubleshooting
- **Eryan Mecham** (OMS partner) - Radiometer calibration, soil moisture analysis
- **Ethan Domagala** - Hardware fabrication, housing design, field operations
- **Dan Prendergast** - Technical direction, commercialization, final deliverables
- **Meredith Needham** - Project coordination, regulatory/medical documentation
- **Mike Ekdahl** - Sod Farm site manager and contact

**Activity Level:** Extensive (3,885 messages across ~5 years). Peak activity: 2020-2022 during hardware development and payload integration; 2024-2025 during USAF SBIR Phase 2 execution and field deployment campaigns.

## Key Decisions

### Hardware Architecture & Integration (2020-2021)

**July 16, 2020** - USGS opportunity identified as strategic priority for becoming "go-to provider" for soil moisture mapping and volcano monitoring support; targeted for regular budget line-item integration.

**October-November 2020** - Two-pass flight methodology adopted: imaging at 400ft altitude with camera enabled, followed by descent for radiometric data collection with camera powered off. This eliminated simultaneous radiometer/camera operation and simplified EMI management.

**January 2021** - Power switching architecture finalized:
- 5V regulator, camera, fan, servo CAN board on switched power line
- LDCR radiometer on battery power (continuous)
- Door servo actuator only device remaining on CAN PWR bus
- Rationale: Prevents electromagnetic interference during radiometer operation

**January 29-February 3, 2021** - Critical firmware breakthrough: Opto-isolation solution implemented for power switch actuator board after extensive EMI troubleshooting. Jake Sahli successfully integrated Sparkfun opto-isolator (https://www.sparkfun.com/products/9118) with block diagram documentation at https://lucid.app/lucidchart/80602878-1b5d-4884-aeee-04c74843121d/edit. This resolved sawtooth pattern noise in radiometer data caused by PWM signals on actuator control lines.

**March 2021** - Decided to completely abandon simultaneous radiometer/camera power; minimal shielding strategy adopted for unpowered equipment (ILS cables). Split power at DB9 connector rather than dual connector on board. UART and battery grounds kept separate (different references).

### Payload Assembly & Manufacturing (2021-2022)

**November 2021** - Procurement challenge for 0.55" thick blue polystyrene foam for antenna assembly: multiple vendor attempts failed. Joshua Fromm sourced foam from personal construction supply sources. Decision: tolerances ±0.5mm acceptable for hand-cut (standard), ±0.2mm preferred for CNC. Final CNC machining capability identified at Loveland facility.

**December 2021** - Altum camera thermal sensor dust issue identified (sticking shutter from debris accumulation). Micasense agreed to thermal sensor replacement and gasket installation at no charge despite expired warranty. Protocol established: Dremel dust intrusion prevention and landing pad usage mandated for future operations.

**April 2022** - After extensive EMI testing on E2 platform (series of experiments isolating noise sources), decision made to mount radiometer on S2 aircraft scaffold configuration (no camera) rather than attempt full E2 integration. Shorter cable routing preferred over semi-rigid extensions to reduce EMI.

### Software Development Strategy (February-May 2021)

**February 24, 2021** - Converted from "poorly-written Matlab code" to Python with Flask web integration. GitLab repository established (https://gitlab.com/thesoilmoisturecompany/smm-processing). Jake Sahli assigned to Python rewrite with emphasis on performance improvements. Decision rationale: original MATLAB implementation had architectural limitations (N-S/E-W flight direction workarounds via switch statements causing data artifacts).

**March 17, 2021** - Jake Sahli completed Python version with split plot functionality (runtime ~10 seconds vs MATLAB's slower execution). Jupyter Hub cluster authorized for repository-based development.

**April 2021** - Jack Elston directed architectural redesign: replace flight-direction switch case statements with proper yaw-based projection equations to eliminate data smearing artifacts.

### Aircraft Platform Decisions (2022-2024)

**October 2022** - E2 adoption confirmed as primary platform for radiometer integration after successful field testing at Avery and Kettle Ponds locations. Decision drivers: superior wind handling (15-20mph gusts manageable, tested to 70mph extremes with tilted rotors), altitude capability, payload capacity.

**April 3, 2024** - New sensor suite firmware completed for NDVI/thermal integration (Apogee Instruments sensors with Raspberry Pi Zero logging). Target: end of September 2024 for complete integrated radiometer/NDVI/thermal system.

### Compliance & Regulatory Path (2024)

**August 28, 2024** - USAF guidance clarified: original comprehensive documentation package may not be necessary for civil Part 107 operations. Ken Green (AFRL) indicated lighter requirements—potentially only critical component list needed. Chinese-origin component waivers confirmed; NDAA compliance not required for R&D contracts (Part 889 applies only to procurement).

**September-October 2024** - FAA Class 3 Medical certification pursued for pilots Jack Elston and Maciej. MedXpress applications pending status update (coordinated by Meredith Needham).

**October 11, 2024** - Milestone 4 submitted successfully; Milestone 5 report submitted same date. Flight testing authorization confirmed for January 2025 onwards.

### Battery Shipping Logistics (August 2025)

**Mid-August 2025** - After initial UPS rejection due to hazmat documentation errors (DGIS software weight calculation failures), decision made to use Old Dominion Freight Line (ODFL) pallet freight pickup (tracking: 13013039295) for 48"x48" pallet with battery case (32"x21"x12"). Cost impact: +$2,000 per demo for battery logistics.

**Future Design Decision** - E3 aircraft development will maintain battery packs under 300Wh limit to enable ground shipping alternatives and avoid hazmat complications. Identified Aeronet Worldwide as viable commercial battery shipping option.

## Projects & Initiatives

### Core Soil Moisture Mapping Payload (2020-2025) - **ACTIVE**

**Status:** Operational with RevD sensor system validated and approved for production use (as of March 2025).

**Technical Configuration:**
- LDCR radiometer (multiple revisions: RevC, C2, RevD) with dual antenna feeds
- Altum multispectral camera (Micasense) with thermal and NDVI bands
- NDVI/thermal sensor suite (Apogee S2-411-SS, S2-412-SS; Melexis MLX90614ESF)
- Raspberry Pi Zero logging architecture
- DB9 connector interface between NDVI housing and back-end housing
- Signal lines: 24VDC, GND, SDI-12 (NDVI), UART RX/TX, I2C (thermal), 5VDC

**Current Capabilities:**
- Brightness temperature mapping from radiometer (water ~180K, dry ground 240K+)
- Volumetric soil moisture approximation without full deconvolution
- Multi-spectral orthomosaic generation via Solvi platform
- Real-time heat map analysis (<1 hour turnaround for field operations)

**Deployed Systems:**
- S2