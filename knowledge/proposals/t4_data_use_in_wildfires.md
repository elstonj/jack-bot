# Data Use in Wildfires

## Document Metadata
- Type: Technical briefing/capability assessment
- Client/Agency: NASA
- Program/Solicitation: 2023 SBIR Phase I (Wildfire)
- Date: 2024-01-03
- BST Products/Systems Referenced: S0 (primary)
- Key Personnel: Alex Lomis (last editor)

## Executive Summary
This document evaluates TAK (Team Awareness Kit) software as the data dissemination platform for Black Swift Technologies' S0 UAS in wildfire operations, detailing how S0 data can be integrated into TAK for incident commanders and firefighting teams. The analysis identifies improved atmospheric forecast models from NCAR as the highest-value data product, with secondary value in video feeds and low-level turbulence data.

## Technical Approach

**Data Dissemination Platform Selection:**
- TAK selected as primary platform due to widespread adoption in emergency response and wildfire operations across multiple states (CoTAK in Colorado, WFTAK across multiple states)
- TAK is open-source with documented APIs for third-party plugins

**S0-to-TAK Integration Methods:**
1. **Direct Feed (Disconnected Operation):**
   - S0 ground station communicates directly to TAK without internet connection
   - Requires only formatted data feed to TAK
   - No real-time processing capability

2. **Cloud-Based Connection:**
   - S0 ground station connects via cellular or satellite
   - Data fed to NCAR for atmospheric model ingestion
   - Processed data returned to multiple TAK instances
   - Enables cross-team information sharing

3. **Portable Server Option (via CoTAK):**
   - CoTAK developers creating portable servers allowing multiple instances to connect without internet
   - Would enable basic S0 data sharing to multiple TAK users

**Plugin Development:**
- TAK UAS Tool (existing plugin) could interface S0 ground station for asset management integration
- Custom plugins proposed to provide:
  - S0-generated 3D wind maps overlay
  - NCAR-improved atmospheric models from S0-collected data
  - Video streaming capability

## Products & Capabilities Described

**S0 (Small Tactical Aerial Resupply and Communications - implied designation):**
- Compact UAS suitable for wildfire operations
- Capability: Atmospheric data collection (wind, temperature, pressure profiles)
- Capability: Video payload (IR/EO - infrared and electro-optical)
- Ground station with data processing capability
- Proposed ground station can interface with TAK via direct feed or cloud connectivity
- Can operate in low-level conditions to collect turbulence and weather data

**Native TAK Features Leveraged:**
- 3D maps with terrain and heat map overlays
- Import Manager with automatic data refresh for live overlays
- Open-source architecture with documented plugin development

## Use Cases & Applications

**Primary Mission:** Wildfire forecast improvement
- Collect atmospheric data using S0 prior to daily firefighting operations
- Process data through NCAR atmospheric models for improved forecasts
- Load improved forecast models onto TAK tablets for incident commander access (pre-loaded, no real-time connection required)

**Secondary Missions:**
- Low-level 3D turbulence mapping for waterbombing operations
  - Mitigation strategies: Early morning flights before manned operations, operations outside Temporary Flight Restrictions (TFRs), S0 operator radio coordination with manned aircraft
- Video reconnaissance (IR/EO) for situational awareness
- Real-time asset tracking and coordination

## Notable Details

**Operational Constraints Addressed:**
- Connectivity challenges in remote wildfire locations solved through portable server option and pre-loaded data model
- Airspace integration with manned aircraft operations managed through scheduling, geographic separation, and radio coordination
- Commercial off-the-shelf solution (TAK) reduces development risk

**Existing Ecosystem Integration:**
- TAK already deployed by Colorado Division of Fire Prevention and Control (since 2018)
- Colorado CoE has operational experience with TAK at public safety incidents
- CoTAK public demo scheduled for February 2024
- Multi-state WFTAK collaborative project indicates industry momentum

**Data Value Hierarchy (per incident commander interviews):**
1. Improved NCAR forecast models from S0-collected data (highest value)
2. Low-level 3D turbulence data (secondary, operationally complex)
3. Video feeds IR/EO (secondary objective)

**Technical Advantages:**
- TAK's open-source nature and existing UAS Tool plugin enable rapid integration
- S0 data can feed both real-time TAK display and NCAR modeling pipelines simultaneously
- Offline capability preserves utility in areas with poor connectivity