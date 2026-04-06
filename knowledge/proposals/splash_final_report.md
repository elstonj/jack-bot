# SPLASH SMM Campaign Final Report

## Document Metadata
- Type: Final Report
- Client/Agency: University of Colorado / Colorado Citizen Resource Protection Program (CCRPP) implied
- Program/Solicitation: SPLASH (Soil moisture mapping campaign at Crested Butte)
- Date: 2023-11-30
- BST Products/Systems Referenced: S2 (fixed-wing soil moisture UAS), E2 (quadrotor-based soil moisture UAS), radiometer, NDVI sensors, thermal sensors
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
The SPLASH campaign was a soil moisture mapping project conducted by Black Swift Technologies at Crested Butte, Colorado. The project resulted in significant technology advancement including development of a new quadrotor-based soil moisture UAS (E2) better suited to mountainous terrain, major improvements to the radiometer instrument reducing noise by 5x, integration of NDVI and thermal sensors onto a single airframe, and successful completion of 64 UAS flights mapping six areas across seven deployments with no incidents. Results demonstrated excellent agreement between UAS-based soil moisture measurements and in situ ground data.

## Technical Approach

### Systems Development
BST developed and deployed two complementary systems:

1. **S2 (Fixed-wing)**: Capable of mapping large areas but limited in mountainous terrain with difficult landing sites
2. **E2 (Quadrotor)**: New development during SPLASH enabling lower-altitude flights, higher resolution maps, and easier operations in challenging topography

### Radiometer Improvements
- **Noise Reduction**: Reduced noise by ~5x through multiple interventions
  - Identified and replaced 11 faulty onboard voltage regulators causing significant electromagnetic noise
  - Removed sporadic temperature-dependent drift from thermal source
  - Designed new cold source without thermal gradient (2023 version): lighter weight, reduced power usage, better temperature range
  
- **Calibration**: Real-time display and processing system added to identify issues in-flight; pre-flight calibration over water bodies using known L-band brightness temperature

### Sensor Integration
- Replaced expensive Altum multispectral camera with dedicated NDVI and thermal sensors
- System configuration:
  - Two NDVI sensors (upper-looking and downward-looking)
  - Single thermal sensor
  - Raspberry Pi Zero W for data processing
  - SDI-12 protocol converters for sensor connectivity
  - Data stored on USB drive along with autopilot telemetry and radiometer data
- Result: Doubled potential mapping area per flight, significantly reduced cost and weight

### Data Processing
- Improvements to soil moisture map production software
- Early campaigns (initial deployments): >1 month processing time
- Final campaigns (September-October 2023): processed in days
- Maps combine L-band brightness temperature, thermal data, NDVI, and elevation with slope correction

## Products & Capabilities Described

### E2 Quadrotor Soil Moisture UAS
- **Purpose**: Soil moisture mapping in difficult terrain
- **Payload**: L-band radiometer (1427 MHz), NDVI sensors, thermal camera
- **Advantages over S2**: Lower altitude capability, easier landing operations, higher resolution data
- **Use in SPLASH**: Successfully deployed and refined throughout project; performed 64 total UAS flights across 7 deployments

### L-Band Radiometer
- **Principle**: Measures L-band brightness temperature by comparing cosmic microwave background against ground reflection at 1427 MHz
- **Key Improvements**:
  - 5x noise reduction
  - New cold/warm source subsystem with better thermal separation
  - Reduced weight and power consumption
  - Real-time diagnostics capability
- **Calibration**: Pre-flight over water to correct for flight-specific bias
- **Performance**: Noise source upgrade and electromagnetic interference reduction resulted in stable, accurate measurements

### NDVI and Thermal Sensor Suite
- **Replaces**: Expensive Altum camera ($3,000+ range)
- **Configuration**: Upper and downward-looking NDVI sensors plus thermal
- **Integration**: Mounted on single airframe with radiometer payload
- **Benefit**: Significantly reduced system cost and weight

## Use Cases & Applications

### SPLASH Campaign (Primary)
- **Location**: Crested Butte, Colorado (mountainous terrain)
- **Areas Mapped**: 6 areas total (Avery South, Avery Middle, Avery North, and three Kettle Ponds areas)
- **Scope**: 64 UAS flights across 7 deployments (1-3 days each)
- **Timeline**: October 2022 - October 2023 (at least 4+ deployments mentioned)
- **Monitoring**: Soil moisture changes over seasonal cycle; specific observations of seasonal pond drying patterns

### USGS California Wildfire Risk Monitoring
- **Application**: Mapping soil moisture in hilly terrain threatened by wildfires
- **Previous Method**: S2 system
- **New Capability**: E2 provided higher resolution data and enabled mapping through tree canopy (new software development)
- **Areas Mapped**: 11 flight areas (some with standard and higher-resolution sub-areas)
- **Results**: High-accuracy maps with excellent correlation between UAS data and in situ measurements through dense vegetation

### Air Force Contract (Future)
- **Value**: $1.25M
- **Objective**: Develop E2 SMM for mapping C-130 landing site conditions
- **Enhancements**: New radiometer version, soil integrity mapping software (in addition to soil moisture)
- **Expected Outcome**: Smaller, cheaper, more robust system for commercial applications

## Key Results

### Radiometer Performance Improvements
- **Noise Reduction**: ~5x improvement through voltage regulator replacement and cold source redesign
- **Calibration Validation**: Raw L-band brightness measurements over water show expected values with proper vertical symmetry
- **Altitude Independence**: Brightness temperature stable regardless of altitude over water (proper radiometer function)

### Soil Moisture Mapping Accuracy
- **Validation**: ~200 ground truth points collected at 3.5 cm depth for two April 2023 flights (April 7 and April 11)
- **Visual Agreement**: Excellent spatial correlation between UAS soil moisture maps and in situ measurements
- **Quantitative Comparison**: UAS vs. in situ data centered on 1:1 line; slight bias toward wetter readings on upper end (expected due to ~15m footprint near water bodies)
- **Change Detection**: April 7 to April 11 showed drying trend, particularly bottom-left areas; ground vs. aircraft change differences contained within ±3%

### Seasonal Monitoring (SPLASH)
- **September-October 2023**: 12 flight areas mapped; clear dry-down pattern visible in Avery areas
- **Kettle Ponds**: Seasonal ponds showed expected signature change from distinct in September to mostly dried by October
- **Note**: October area 2 data potentially biased wetter due to snow on eastern edge

### USGS California Results
- **Through-Canopy Mapping**: Achieved high-quality soil moisture data under moderate to dense tree canopy (previously impossible with fixed-wing systems)
- **Data Quality**: Excellent correlation between UAS SMM and in situ data through trees

### Operational Success
- **Flight Operations**: 64 total UAS flights completed with zero accidents or incidents
- **Stakeholder Management**: No interference with cattle operations, other research, or general public
- **Mission Flexibility**: Missions adapted around presence of livestock and people while maintaining 6-area coverage

### Processing Efficiency
- **Timeline Improvement**: From >1 month for early deployments to days for final (Sept-Oct 2023) campaigns
- **Data Volume**: Successfully processed multiple soil moisture maps (12 shown for final period) with ancillary NDVI, thermal, and elevation data

## Notable Details

### Technology Transfer & Commercialization
1. **E2 Development Success**: New quadrotor platform directly enabled USGS contract work not feasible with previous fixed-wing S2
2. **Software Innovation**: New algorithms developed to enable soil moisture mapping through forest canopy
3. **Cost Reduction**: New NDVI/thermal sensor suite replaces expensive Altum camera, significantly lowering system cost
4. **System Efficiency**: Integrated single-airframe solution doubles potential coverage area vs. previous two-aircraft approach

### Technical Innovations
- **New Cold/Warm Source Design**: Eliminates thermal gradient reliance, reduces weight/power, improves thermal separation
- **Real-Time Diagnostics**: Added ability to identify radiometer issues in-flight via real-time display and processing
- **Software Improvements**: Rapid processing pipeline reduces months to days; new through-canopy mapping capability

### Operational Lessons
- Mountainous terrain and seasonal obstacles (cattle, snow, public presence) required operational flexibility
- Seasonal ponds provide natural calibration targets for radiometer validation
- ~15m radiometer footprint creates edge effects requiring careful interpretation near heterogeneous features

### Future Development Path
- Air Force funding ($1.25M) will advance E2 SMM into soil integrity assessment capability
- Improvements designed for military landing site assessment expected to enhance commercial viability
- Roadmap: smaller, cheaper, more robust system for commercial soil moisture and integrity mapping projects

### Partnership Success
- CU/CCRPP provided test site and data collection support
- USGS recognized value of improved E2 system and contracted for additional campaigns
- Air Force interest validates technology advancement and commercial potential