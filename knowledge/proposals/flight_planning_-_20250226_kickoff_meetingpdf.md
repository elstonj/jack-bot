# Flight Planning - 20250226 (Kickoff Meeting)

## Document Metadata
- Type: Flight planning briefing / kickoff meeting presentation
- Client/Agency: NASA
- Program/Solicitation: S2 Crater (Costa Rica) project
- Date: 26 February 2025
- BST Products/Systems Referenced: S2 (aircraft), Ground station/tablet
- Key Personnel: Meredith Needham (last editor)

## Executive Summary
This document presents flight planning analysis for a NASA S2 UAS mission in Costa Rica to conduct crater/gas emissions monitoring. Multiple takeoff/landing site options and seven distinct flight plan variants are evaluated for feasibility based on distance, flight time, battery usage, and line-of-sight communications, with recommendations on operations logistics.

## Technical Approach
- **Flight altitude:** 25m AGL (standard collection) with some plans using 25-75m or 25-55m altitude profiles
- **Line-of-sight (LoS) analysis:** Geometry-based (does not account for terrain diffraction/bending or tree attenuation)
- **Terrain following:** Intermediate waypoints planned for final flight plans
- **Ground station logistics:** BST proposes bringing ground station/tablet with handoff capability between launch and landing locations (~2 min signal loss during transition)
- **CH4 mapping integration:** Eddy-covariance techniques with online flight plan generation based on measured winds and predicted convective rates (0.75-3 m/s for CH4); not yet validated for CO2

## Products & Capabilities Described

**S2 Aircraft**
- Small UAS platform for crater/emissions monitoring
- Flight time capacity: up to ~72 minutes on battery
- Battery endurance: capable of 28-68% battery usage depending on mission profile
- Operates at very low altitudes (25m AGL minimum)
- Terrain-following capability with waypoint planning

**Ground Station**
- Mobile/portable tablet-based system
- Proposed to be positioned at both launch and landing locations
- Requires shutdown/startup transition (~2 min communications loss)

## Use Cases & Applications
- **Primary mission:** Gas emissions monitoring (CH4 and CO2) in Costa Rica crater region
- **Eddy-covariance mapping:** CH4 source identification and quantification
- **Terrain:** Ridge-dominated volcanic landscape with significant line-of-sight communication challenges
- **Collection targets:** Identified "boxes" for systematic data collection over wet lands (primary CH4 source) and production site (secondary CH4 source)

## Operational Analysis

### Takeoff/Landing Site Options
1. **Powerplant Field** – IDEAL (175m): Plenty of options, good T/O and landing location
2. **Adventure Park Field** – MAYBE (270m × 225m): Requires inspection for obstacles, slope, flatness; needs owner permission
3. **Field off 918** – MAYBE (175m × 130m): Takeoff only; requires inspection; needs owner permission
4. **Santa Maria Ranger Station** – LIMITED (75m): Takeoff only, tight margins, landing not possible; wind concerns

### Flight Plan Variants & Performance
All flight plans assessed at 25m AGL collection altitude unless otherwise noted:

| Plan | Altitude (m) | Distance (km) | Flight Time (min) | Lost LoS (min) | Battery Used (%) | Notes |
|------|--------------|---------------|-------------------|----------------|-----------------|-------|
| 1_SE_Short_EW (RS) | 25 | 49 | 44 | 21 | 48 | Terrain slope exceeds max climb/descent angle |
| 2_SE_Full (RS) | 25 | 34 | 30 | 3 | 32 | Good balance |
| 3_South_Long_A | 25 | 36 | 32 | 5 | 34 | Part A of split plan |
| 3_South_Long_B (RS) | 25 | 42 | 37 | 7 | 34 | Part B of split plan |
| 5_SE_Curtain (RS) | 25-75 | 82 | 72 | 1 | 68 | Longest endurance; minimal LoS loss |
| 6_South_Curtain_and_Cross (RS) | 25-55 | 30 | 27 | 0 | 28 | Zero LoS loss; efficient |
| 6_SE_Transect (RS) | 25-55 | 37 | 33 | 6 | 34 | Transect variant |
| 1_SE_Short (918 Field) | 25 | 47 | 42 | 4 | 45 | Alternative from 918 field |

### Key Findings & Constraints
- **All flight plans are feasible** in terms of distance, flight time, and battery endurance
- **Southeast plans have LoS issues:** Ridge terrain between launch/recovery and SE collection boxes causes significant communications outages (up to 21 min in worst case)
- **Terrain slope limitations:** Several SE orientations exceed aircraft max climb/descent angles; east-west orientation needed for Plan 1
- **South-oriented plans:** Better LoS performance; "South Long" plan requires split into two boxes due to ridge interference
- **Variable altitude plans:** 25-75m profiles provide minimal LoS loss while extending flight time

## Notable Details
- **DSM data request:** BST asks if NASA has access to high-resolution digital surface models (e.g., Maxar) with 1m relative and 3m absolute accuracy for improved safe flight planning
- **Personnel question:** BST seeks clarification on whether NASA requires operators only or additional safety pilot
- **CH4 vs. CO2:** CH4 eddy-covariance approach used but CO2 validation pending
- **Operational logistics:** Ground station handoff concept reduces need for continuous LoS from single location but introduces brief communication gap during transition
- **Spatial resolution:** Multiple collection "boxes" targeting distinct geographic features (wetlands vs. production site) with 4km spacing