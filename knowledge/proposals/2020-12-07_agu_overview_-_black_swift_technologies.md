# 2020-12-07 AGU Overview - Black Swift Technologies

## Document Metadata
- Type: Presentation (conference overview)
- Client/Agency: DOD (SBIR Phase II)
- Program/Solicitation: SBIR 2019.2 - Atmospheric Sounding
- Date: 2020-11-23 (created/modified); presented at AGU December 2020
- BST Products/Systems Referenced: S0 (atmospheric sounding UAS)
- Key Personnel: Jack Elston (last editor)

## Executive Summary
This presentation outlines Black Swift Technologies' S0 UAS design for atmospheric sounding, emphasizing a low-cost, simple-to-operate platform for wind and environmental profiling. The document details design requirements, wind sensing calibration methodology, and field validation approaches being used to develop and prove the system.

## Technical Approach

### S0 Design Philosophy
- Small, simple unmanned aircraft system designed for rapid atmospheric profiling
- Emphasis on user accessibility (<1 day training required)
- Integration of 3D-printed wind sensing components
- Output in standard meteorological formats (BUFR, GRIB, netCDF)

### Wind Sensing Calibration
- **Probe Design**: 3D-printed wind sensing components
- **Calibration Method**: 9th-order polynomial fit
- **Parameters Computed**: cα (angle of attack coefficient), cβ (sideslip coefficient), cq (dynamic pressure coefficient)
- **Calibration Approach**: Non-linear with good symmetry properties
- **Wind Tunnel Testing**:
  - 900 probe positions tested
  - ±15° angle of attack (α) and sideslip (β) range, 1° intervals
  - >1000 measurements per position
  - ~1,000,000 total measurements acquired
  - 3 hours total wind tunnel run time
- **Flight Calibration**: Combined tunnel and flight-based validation

## Products & Capabilities Described

### S0 UAS
- **Purpose**: Rapid atmospheric profiling platform
- **Design Requirements**:
  - Cost: <$5,000 for full setup
  - Operating altitude: Up to 15,000 ft AGL
  - Training requirement: <1 day
  - User interface: Familiar/intuitive design
- **Capabilities**: Wind speed, wind direction, temperature, pressure, humidity profiling
- **Output Formats**: BUFR, netCDF, GRIB (standard meteorological data formats)

## Use Cases & Applications

### Field Validation Operations
- Atmospheric sounding and wind profiling
- Comparison flights with radiosondes (weather balloons)
- Validation against instrumented tower measurements
- Turbulent scale capture evaluation
- Different flight patterns to assess potential biases in measurements

## Key Results & Validation Approach

### Tower Comparison Campaign
- 5-day field test window
- Flights conducted upwind of instrumented tower
- Comparison metrics:
  - Wind speed statistics
  - Wind direction statistics
  - Temperature profiles
  - Pressure profiles
  - Humidity profiles
- Evaluation of system's ability to capture different turbulent scales

### Radiosonde Comparison
- Direct comparison flights following radiosonde launches
- Profile consistency validation between S0-AD and weather balloon systems

## Notable Details
- Emphasis on affordability (<$5K) and operational simplicity as key differentiators
- Sophisticated wind sensing calibration (>1 million measurements) supporting accuracy despite low cost
- Output in familiar meteorological data formats suggests compatibility with existing operational workflows
- S0-AD designation suggests this is an atmospheric dynamics variant
- Phase II SBIR funding indicates DoD validation of concept feasibility