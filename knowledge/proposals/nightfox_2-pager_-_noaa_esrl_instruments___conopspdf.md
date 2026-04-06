# NightFOX 2-pager - NOAA ESRL Instruments & CONOPS

## Document Metadata
- Type: Capability brief / instrument suite description
- Client/Agency: NOAA Earth System Research Laboratories (ESRL), Chemical Sciences Division (CSD)
- Program/Solicitation: NOAA SBIR (CO sensor development); FIREX 2019 campaign planning
- Date: April 19, 2019
- BST Products/Systems Referenced: S2 UAS
- Key Personnel: Ru-Shan Gao, Troy Thornberry (NOAA authors); Jack Elston (BST, last editor)

## Executive Summary
This document describes two instrument suite configurations for the NightFOX project to characterize wildfire emissions and radiative properties using NOAA ESRL sensors integrated onto Black Swift Technologies' S2 UAS. The suites enable simultaneous in-situ plume sampling and remote sensing of fire radiative power and extent during the 2019 FIREX campaign.

## Technical Approach

### In-Situ Instrument Suite
Five instruments mounted in S2 UAS nose cone for fire plume characterization with 1-second time resolution:
- **CO₂ measurement**: NDIR absorption at ~4 µm
- **CO measurement**: New MEMS sensor developed under NOAA SBIR
- **Fine mode aerosol**: POPS (optical particle spectrometer), 0.14–2.5 µm range
- **Coarse mode aerosol**: AlphaSense OPC, 1–10 µm range
- **Aerosol sampling**: Filter-based collector for off-line analysis

**Flight pattern**: Ladder pattern perpendicular to ambient wind direction to sample plume cross-section.

### Remote Sensing Instrument Suite
Four instruments with six measurements types, mounted on S2 UAS:
- **FLIR DUO camera**: Visible + thermal IR (7.5–13.5 µm, 44° × 57° FoV), 1 Hz capture
- **Custom SWIR imager**: ~1.6 µm, 24° × 24° FoV, 1 Hz
- **Cross-track scanner**: Single-element sensors for SWIR (1.6 µm) and MWIR (4 µm), ±30° of nadir, 1° angular resolution (~18 m resolution at 1 km AGL)
- **Laser rangefinder**: Max range 250 m for plume altitude measurement

**Outputs**: Four maps per flight (visible, 1.6 µm FRP, 4 µm FRP, thermal)

**Flight pattern**: Staggered back-and-forth pattern flown directly over wildfire.

## Products & Capabilities Described

### S2 UAS
- Serves as platform for integrated instrument payloads
- Nose cone configured to house in-situ instrument suite
- Capable of sustained operation over fire plumes
- Operating altitude: ~1 km AGL (reference for remote sensing resolution calculations)

## Use Cases & Applications
- **Wildfire emissions characterization**: Real-time measurement of modified combustion efficiency (MCE) and aerosol loading in fire plumes
- **Fire radiative power measurement**: Quantification of fire extent and intensity using multi-spectral radiometry
- **Nighttime fire observations**: Implicit capability to operate during night conditions (project name: NightFOX)
- **Campaign deployment**: 2019 FIREX campaign for coordinated wildfire measurements

## Notable Details
- CO sensor represents new MEMS technology development funded by NOAA SBIR (suggesting BST or partner involvement in sensor innovation)
- Dual-suite approach allows flexible deployment: separate in-situ plume sampling missions vs. remote sensing overflights
- High-resolution cross-track scanner (1° angular resolution) provides detailed spatial mapping of fire radiative properties
- Filter-based aerosol collection enables post-flight laboratory analysis for chemical composition
- Document emphasizes 1-second time resolution across in-situ instruments for detailed temporal evolution of plume properties