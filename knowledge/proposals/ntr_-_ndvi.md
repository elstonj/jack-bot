# NDVI Sensor Suite

## Document Metadata
- Type: New Technology Report (NTR)
- Client/Agency: NASA Goddard Space Flight Center
- Program/Solicitation: 2012 SBIR Phase I; Contract NNX13CG33P
- Date: June 6, 2014 (document creation)
- BST Products/Systems Referenced: S3 (sUAS platform for Soil Moisture Mapping)
- Key Personnel: 
  - Jack Elston (BST, Company Tech Rep)
  - Maciej Stachura (BST, Initial Sensor Design)
  - Raymond Oung (BST, PCB Design)
  - Albin Gasiewski (University of Colorado, Initial Sensor Design)

## Executive Summary
Black Swift Technologies designed and built a compact NDVI/Thermal sensor board during Phase I of a NASA SBIR for soil moisture mapping applications. The system measures vegetation indices (red and near-infrared) from both nadir and zenith directions while simultaneously capturing thermal data, providing sky-corrected NDVI measurements and surface temperature estimates for integration into small unmanned aircraft systems.

## Technical Approach

**Core Components:**
- **Red & NIR Sensing**: Si-J146 photodiodes with amplifiers from Electro Optical Components
  - Spectral range: 400–1100 nm
  - Filters applied to isolate red (550–700 nm) and near-infrared (700–1300 nm) bands
  - Dual sensors: one nadir-facing, one zenith-facing
  
- **Thermal Imaging**: MLX90615 infrared sensor for 10 μm temperature measurements
  - Captures surface and cloud bottom temperatures
  
- **Data Processing**: STM32F103 Cortex-M3 microcontroller samples all three sensors and outputs digital data packets

**Development Timeline:**
- 5/28/2013 – Initial discussion and conceptual design
- 8/16/2013 – Photodiode and filter selection for red/NIR
- 8/20/2013 – Thermal temperature sensor selection
- 10/28/2013 – Sensor board design complete
- 11/8/2013 – Circuit boards printed and delivered
- 11/18/2013 – Boards populated and initial testing

## Products & Capabilities Described

**NDVI/Thermal Sensor Board:**
- **Function**: Provides sky-corrected Normalized Difference Vegetation Index (NDVI) measurements and soil surface temperature estimates
- **Use Case**: Corrects L-band radiometer soil moisture measurements using vegetation and thermal data
- **Platform**: Designed for integration into small unmanned aircraft systems (sUAS)
- **Key Specifications**:
  - Wavelength coverage: Red (550–700 nm), NIR (700–1300 nm), thermal (10 μm)
  - Dual nadir/zenith sensor capability
  - Low size, weight, and power consumption
  - Microcontroller-based digital output

**State of Development**: Prototype (completed Phase I)

## Use Cases & Applications

1. **Soil Moisture Mapping via sUAS**: Primary application within NASA SBIR—using NDVI and thermal data as correction factors for L-band radiometer soil moisture estimates
2. **Precision Agriculture**: Identified as largest potential commercial market; over 2.2 million farms in the US; sensor provides integrated value to low-cost sUAS operators for vegetation monitoring

## Key Results (Phase I Deliverables)

- Completed functional prototype of NDVI/Thermal board
- Demonstrated integration of compact, low-power multi-spectral and thermal sensing
- Documentation: Circuit diagram, prototype photos, specification sheets (EOC JI 546-547-548, 3901090615-1)
- Ready for Phase II validation and flight testing with Soil Moisture Mapping sUAS

## Notable Details

**Competitive Advantages:**
- **Unique nadir/zenith dual-sensor architecture** for improved NDVI accuracy with sky correction
- **First system to integrate thermal measurements** with NDVI in a compact, low-cost format
- Low cost and low power compared to higher-end alternatives (e.g., TetraCam)
- Significantly smaller and lighter than prior-art solutions, enabling sUAS integration

**Prior Art Considerations:**
- Previous NDVI solutions relied on low-cost EO cameras with filters (lacked precision) or expensive professional systems like TetraCam (higher cost, no thermal capability, larger form factor)
- This innovation bridges the gap with scientific-grade accuracy at sUAS-compatible scale/power

**Phase II Work:**
- Validation testing against known standards planned
- Flight testing integration with Soil Moisture Mapping sUAS to assess full operational capabilities
- No patent applications filed as of this NTR submission

**Funding/Oversight:**
- NASA COTR: Geoff Bland
- WBS: 939869.03.06.01 (FY 2013); Program S3.05-8971