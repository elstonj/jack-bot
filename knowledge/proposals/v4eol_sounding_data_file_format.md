# EOL Sounding Data File Format

## Document Metadata
- Type: Technical reference document / data format specification
- Client/Agency: NOAA / National Center for Atmospheric Research (NCAR) Earth Observing Laboratory (EOL)
- Program/Solicitation: Referenced in context of 2018 NOAA SBIR Phase I
- Date: Created/Modified 2018-01-30
- BST Products/Systems Referenced: None directly (document is reference material for sounding data)
- Key Personnel: Jack Elston (last editor)

## Executive Summary
This document specifies the standard file naming convention and data format for EOL (Earth Observing Laboratory) sounding data files from both dropsondes and radiosondes. It details the metadata header structure, data parameter definitions, and measurement specifications used in atmospheric sounding operations, with specific reference to AVAPS (Airborne Vertical Atmospheric Profiling System) data from platforms like the NASA Global Hawk.

## Technical Approach
The document establishes standardized conventions for:
- **File naming**: "D" + yyyymmdd_hhmmss_v.QC.eol format with version control and QC flags
- **Metadata headers**: 14-line header structure containing identification info, system metadata, and column definitions
- **Data organization**: Time-series columns with specific measurement parameters and sampling rates

## Data Parameters & Specifications

| Parameter | Measurement Rate | Units | Notes |
|-----------|------------------|-------|-------|
| Time | — | seconds | Elapsed from launch; -1.0 indicates reference flight-level data |
| Pressure | 0.5 sec (dropsonde) / 1 sec (radiosonde) | millibars | — |
| Dry Bulb Temperature | 0.5 sec (dropsonde) / 1 sec (radiosonde) | °C | — |
| Dewpoint Temperature | Calculated | °C | From RH and temp via Bolton 1980 vapor pressure equation |
| Relative Humidity | 0.5 sec (dropsonde) / 1 sec (radiosonde) | % | Includes TDDryBiasCorrApplied flag for temperature-dependent bias correction |
| U/V Wind Components | Calculated | m/s | Derived from wind speed and direction |
| Wind Speed | 0.25 sec (dropsonde) / 1 sec (radiosonde) | m/s | — |
| Wind Direction | 0.25 sec (dropsonde) / 1 sec (radiosonde) | degrees | — |
| Descent/Ascent Rate | Computed | m/s | Time-differentiated hydrostatic equation |
| Geopotential Altitude | Computed | meters | Height above MSL from hydrostatic equation |
| GPS Position | Direct | degrees | From GPS sensor; uncertainty <20m |
| GPS Altitude | Direct | meters WGS84 | — |

## Use Cases & Applications
- **Hurricane monitoring**: Dropsonde deployments with NHC Best Track interpolation (radius, azimuth relative to tropical cyclone center)
- **High-altitude aircraft operations**: Data collection from NASA Global Hawk platform at flight levels up to 18,420m
- **Atmospheric research**: NASA HS3 (Hurricane and Severe Storm Sentinel) program (example: Science Flight 1, 2011-09-09)

## Notable Details
- **AVAPS integration**: Data processed through AVAPS software (v3.1 example cited) with specific configuration sets
- **Quality control features**: Version tracking for post-processing corrections; TDDryBiasCorrApplied flag for humidity bias correction (reference: http://opensky.ucar.edu/islandora/object/technotes:542)
- **Additional hurricane parameters**: Optional radius/azimuth and unfiltered/filtered vertical wind calculations for NOAA Hurricane Archive
- **Metadata richness**: Includes launch location (degrees-minutes + decimal), UTC launch times, sonde IDs, operator notes, and processing comments
- **Vertical wind computation**: Based on Wang et al. 2009 algorithm using pressure-calculated and theoretical fall rates

## Context Note
This is a reference document filed within BST's 2018 NOAA SBIR Phase I proposal materials, suggesting it was used as background specification for understanding atmospheric sounding data requirements, likely relevant to proposed dropsonde or atmospheric measurement capabilities.