# Open Science and Data Management Plan (OSDMP)

## Document Metadata
- Type: Data Management Plan (component of NASA proposal)
- Client/Agency: NASA
- Program/Solicitation: 2024 ROSES A.59
- Date: Created 2024-03-07, Modified 2024-03-29
- BST Products/Systems Referenced: Small UAS (for soil moisture mapping)
- Key Personnel: Maciej Stachura (last editor), PI (Principal Investigator - name not specified in document)

## Executive Summary
This OSDMP outlines data management, software management, and open science protocols for a 3-year NASA-funded research project focused on soil moisture and live fuel moisture mapping. The project integrates data from a small UAS platform, NISAR satellite, and UAVSAR, with all data to be archived and shared publicly upon validation, and operational codes to be released at project completion.

## Technical Approach
The project employs three complementary data sources for soil moisture mapping:
- **Small UAS platform**: 192 flights per year generating 2m resolution soil moisture maps
- **NISAR satellite**: 200m resolution soil moisture maps at 6-day intervals beginning October 2025
- **UAVSAR**: 6m resolution soil moisture maps (9 flights planned in Year 1)

Data processing codes are developed in IDL and Python for generating soil moisture and live fuel moisture products.

## Products & Capabilities Described

### Small UAS
- **What it is**: Unmanned aerial system for high-resolution remote sensing
- **Proposed use**: Generate soil moisture maps at 2m spatial resolution
- **Specifications**: 192 flights per year; produces 10GB of image data annually in HDF format

### NISAR (NASA-ISRO Synthetic Aperture Radar)
- **What it is**: Satellite-based SAR platform
- **Proposed use**: Large-scale soil moisture mapping
- **Specifications**: 200m resolution, 6-day repeat interval, operational from October 2025 onward; produces 6GB of image data in HDF format

### UAVSAR (Uninhabited Aerial Vehicle Synthetic Aperture Radar)
- **What it is**: Airborne SAR system
- **Proposed use**: Medium-resolution soil moisture mapping
- **Specifications**: 6m resolution, 9 flights planned for Year 1; produces 0.3GB of image data in GeoTIFF format

## Use Cases & Applications
- Soil moisture monitoring and mapping
- Live fuel moisture assessment (relevant to vegetation/fire risk monitoring)
- Cal/val (calibration/validation) activities for satellite systems

## Data Management Approach
- **Data archiving philosophy**: Data archived and shared once validated and uncertainty characterized
- **Policy compliance**: Adherence to NASA Earth Science Data and Information Policy
- **Storage locations**: 
  - NISAR outputs → NISAR cloud
  - UAVSAR and small UAS outputs → PI institution (publicly available)
- **Data sharing exemptions**: None—all data to be publicly shared
- **Timeline**: Data shared upon validation completion

## Software Management Approach
- **Languages**: IDL and Python
- **Repositories**: 
  - Operational codes → NISAR cloud
  - Analysis codes → NASA repository (https://data.nas.nasa.gov/) and PI GitHub
- **Release timeline**: Software posted at end of project
- **Sharing exemptions**: None—all software to be publicly shared

## Publication Strategy
Peer-reviewed manuscripts identified as primary project outcomes, reflecting the science-driven nature of the effort.

## Notable Details
- Project duration: 3 years
- Total data volume over project period: ~16.3GB across all sources
- All team responsibilities for data management assigned to PI
- Zero exemptions from open science sharing requirements (full open science commitment)
- Integration of NASA flagship satellite systems (NISAR) with smaller airborne platforms suggests emphasis on multi-scale validation and operational transition