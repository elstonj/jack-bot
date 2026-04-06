# Colorado Orphan Wells as confirmed by USGS

## Document Metadata
- Type: Data spreadsheet / database listing
- Client/Agency: USGS (U.S. Geological Survey); likely for DOE/FECM (Department of Energy, Fossil Energy and Carbon Management)
- Program/Solicitation: DOE_FECM orphan well remediation initiative
- Date: Created/Modified November 1, 2024; data reflects wells with 7/1/2019 status date
- BST Products/Systems Referenced: None
- Key Personnel: Beck Cotter (last editor)

## Executive Summary
This is a database listing of confirmed orphan oil and gas wells in Colorado, curated from USGS records. The spreadsheet contains geolocation data, API numbers, well names, counties, and status indicators ("Planned Footage" vs. "ACTUAL LatLong") for approximately 140+ orphan wells (identified with "OWP" designation) across multiple Colorado counties.

## Document Content & Structure
The document is a structured data table with the following fields for each well entry:
- **API Number**: Unique identifier for each well (format: state-county-sequence)
- **County**: Colorado county location (Baca, Cheyenne, Delta, Fremont, Huerfano, Kiowa, Kit Carson, Las Animas, Lincoln, Logan, Mesa, Morgan, Ouray, Weld)
- **Well Name**: Property or operator name
- **Status**: "WELL" designation (all entries)
- **Coordinates**: Latitude and longitude in decimal degrees
- **Section/Township**: Quarter-quarter section location (e.g., "SE C CO", "NW NW")
- **Status Date**: 7/1/2019 (uniform across all entries)
- **Location Confidence**: Either "Planned Footage" or "ACTUAL LatLong" indicating whether coordinates are estimated or verified

## Geographic Distribution
Wells are distributed across 14 Colorado counties:
- **Logan County**: Highest concentration (~80 wells), including multiple units: NW Graylin D-Sand Unit, Logan J Sand Unit, Mount Hope Unit, Mount Hope-Green Unit
- **Mesa County**: ~15 wells, including DB Orphan series, Lake/Brown House, Canfield, Silvey Flats
- **Fremont County**: ~9 wells (Hassler, Redband, Croaker, Javernic, HW-series)
- **Morgan County**: ~20 wells (Huey, George E Huey, Rosener-Johnson, State-Milliron, etc.)
- **Weld County**: ~15 wells scattered across locations
- **Baca County**: ~6 wells (Cogburn, Baughman Farms, Deeds, Hunt, Newlin)
- **Other counties** (Cheyenne, Delta, Huerfano, Kiowa, Kit Carson, Las Animas, Lincoln, Ouray): 1-4 wells each

## Data Quality Indicators
- **Actual LatLong**: Approximately 60-70 wells have verified actual coordinates
- **Planned Footage**: Remaining ~70 wells have estimated locations or pending survey data
- Coordinate precision: Decimal degree format (6+ decimal places) = ~0.1 meter precision

## Notable Details
- **OWP Designation**: Most wells marked "(OWP)" indicating formal orphan well program status
- **Multi-well Units**: Several well groupings suggest coordinated remediation opportunities (Mount Hope Unit, NW Graylin D-Sand Unit, Logan J Sand Unit)
- **Data Source**: Explicitly confirmed by USGS, suggesting this is official federal inventory data
- **Temporal Gap**: Last status update appears to be 7/1/2019; document created November 2024 indicates this may be historical baseline data for current remediation planning
- **No BST Content**: This is a data reference document with no indication of Black Swift Technologies involvement; likely included in BST's DOE proposals as supporting environmental/baseline data

## Potential Use Case
This orphan well database would support BST proposals for aerial survey, mapping, or monitoring of orphan well sites, particularly if BST's UAS platforms (S2, S3, AeroPod) were being proposed for rapid assessment, environmental sampling, or methane detection at these known locations.