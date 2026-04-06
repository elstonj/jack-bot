# Uncrewed Aircraft System Data Assimilation for Improved Wildland Fire Fighting

## Document Metadata
- Type: NASA SBIR Phase I Final Report
- Client/Agency: NASA LaRC (Langley Research Center)
- Program/Solicitation: NASA SBIR 2023-I, Topic A3.02 Advanced Air Traffic Management for Nontraditional Airspace Operations
- Contract Number: 80NSSC23PB371
- Date: February 2024
- BST Products/Systems Referenced: S0 VTOL, S1 UAS, SwiftTab User Interface
- Key Personnel: Jack Elston (PI), Maciej Stachura (Lead Engineer), James Pinto (co-I, NCAR)

## Executive Summary
Black Swift Technologies conducted a Phase I study demonstrating how targeted Uncrewed Aircraft System (UAS) observations can improve the accuracy of wind and turbulence forecasts around wildland fires using data assimilation. The effort demonstrated significant meteorological prediction improvements, developed standardized data formats for model ingestion, established pathways for UAS integration with fire operations, and produced hardware revisions to the S0 VTOL for deployment in harsh wildfire conditions.

## Technical Approach

**Core Mission Concept:**
The project proposes a seven-step operational cycle:
1. Extract critical parameters from weather models 12-24 hours before sampling
2. Use Ensemble Sensitivity Analysis (ESA) to identify error-growth regions
3. Deploy UAS for autonomous spiral profiling (2-3 hour operations) in ESA-identified sensitive regions
4. Disseminate temperature, pressure, humidity, and 3D winds data for real-time and modeling use
5. Format and distribute observations to modeling centers via WMO standard formats
6. Provide updated weather products to incident commanders via Team Awareness Kit (TAK)
7. Repeat cycle as needed for persistent monitoring

**Ensemble Sensitivity Analysis (ESA):**
- Identifies areas where lacking observations lead to model error growth
- Uses 40-member ensemble approach with NOAA HRRR model initialization
- Relates response variables (e.g., 10-m wind gust speeds) to predictor fields (e.g., sea level pressure)
- Guides UAS deployment to maximize forecast impact

**Data Assimilation:**
- Ensemble Kalman Filter (EnKF) approach developed by NCAR/RAL
- Multi-UAS coordinated operations (15km+ spacing demonstrated)
- Real-time and post-processing data ingestion
- Observing System Experiments (OSEs) to quantify impact

## Products & Capabilities Described

### S0 VTOL UAS
- **What it is:** Vertical take-off and landing weather-sensing UAS developed by BST
- **Phase I modifications:** Significant hardware revisions for mountainous terrain and wildfire conditions
- **Specific improvements:**
  - Enhanced multi-hole probe payload protection (rain, smoke, ash resistant)
  - High-capacity battery design and resilient propulsion system
  - Reinforced motor mounts and wing structure
  - Higher wing placement to accommodate new propulsion components
  - LED-illuminated servo pockets and high-visibility strobe for night operations
  - Tool-less assembly for field deployment
  - Hard-shell carrying case for transport of multiple units
- **Operational capability:** Continuous spiral profiling from 30m to 120m AGL with 0.5-2.0 m/s climb/descent rates
- **Advantages:** Can operate in severe weather, rough terrain deployment, persistent monitoring capability

### S1 UAS
- Referenced as companion aircraft in multi-UAS coordinated operations
- Conducted test flights with full meteorological sensor suite

### Data Conversion Software
- **Purpose:** Rapidly convert raw S0/S1 data into standard formats for model assimilation
- **Output formats:**
  - WMO Standard (CF-compliant NetCDF)
  - PREPBUFR (international modeling center standard)
- **Validation:** Tested with NCAR's Data Assimilation Research Testbed
- **Wind validation technique:** Orbit calibration method using GPS ground speed to verify wind measurements without meteorological towers

### SwiftTab User Interface
- Android-based interface for data display
- Capabilities: real-time weather/wind display, scalar value plotting (trace gases, particle distribution), geo-located shape display
- Planned integration with ATAK for wildfire operations

## Use Cases & Applications

**Primary Use Case: Wildland Firefighting Decision Support**
- Improving low-level wind and turbulence forecasts during active fire operations
- Supporting mixed (crewed and uncrewed) aircraft operations
- Enabling nighttime aerial firefighting operations
- Case study: Calwood Fire (October 17, 2020) - 10,000+ acres in first hours, explosive growth fueled by gusty winds

**Operational Scenario Details:**
- Pre-incident planning 12-24 hours before high-risk fire weather days
- Mid-fire operations providing 6-12 hour wind and turbulence guidance
- Integration with fire command and control systems via Team Awareness Kit (TAK)
- Coordination with incident commanders for deployment decisions

**Secondary Applications:**
- Advanced Air Mobility (AAM) support in mountainous and urban corridors
- NASA Earth Science programs (3D-Winds mission)
- General environmental monitoring in complex terrain

## Key Results

### Data Assimilation Impact (January 5, 2024 Case Study)
**Test Setup:** Two coordinated S0/S1 UAS flights in Boulder County demonstrating strong east-to-west wind gradient
- **Wind improvements:**
  - 10m u-wind component bias reduced by >50%
  - RMSE reduced by 30%
  - 10m wind direction improved by up to 50 degrees at Boulder Airport (BDU)
  - Notable improvement at BDU and adjacent foothills locations
  
- **Relative humidity improvements:**
  - Dry bias notably reduced
  - All tested ASOS stations except C99 showed improved skill
  - Impact limited at distant locations (36km away), indicating need for multiple distributed UAS

### Ensemble Sensitivity Analysis Results (Calwood Fire Case)
- ESA successfully identified regions of enhanced forecast sensitivity to sea level pressure
- Two primary sensitivity regions identified: positive values west-northwest of fire, larger negative values to southwest
- Broader negative sensitivity area indicated better potential for gap-filling observations
- Confirms feasibility of targeted UAS deployment strategy

### Data Format Validation
- S0/S1 data successfully converted to WMO NetCDF standard
- Python conversion script successfully transformed WMO format to PREPBUFR
- All formats validated through NCAR data assimilation system ingestion
- Wind calibration technique using orbit analysis validated against DOE meteorological tower data (25m and 60m heights)

### Multi-UAS Coordination
- Successfully demonstrated time-synchronized multi-UAS operations (January 5, 2024)
- Two aircraft spaced 15km apart (exceeding 10km minimum useful spacing threshold)
- Synchronized spiral profiling (30-120m AGL) with 2 m/s climb/descent rates
- Coordinated data collection enabled ESA-guided deployment validation

## Notable Details

### Partnerships & Collaborations
**Primary Partners:**
- NCAR/RAL (National Center for Atmospheric Research, Research Applications Laboratory) - meteorological modeling and data assimilation expertise
- Colorado Center of Excellence for Advanced Technology Aerial Firefighting - operational fire access and TAK integration
- AFRL (Air Force Research Laboratory) - Team Awareness Kit (ATAK) development

**NASA Program Connections:**
- NASA ACERO (Advanced Capabilities for Emergency Response Operations) - UAS coordination and airspace management
- NASA FireSense - Earth science integration with operational agencies
- NASA Ames - Primary customer for wildfire use case
- Contacts: Joey Mercer (ACERO), Haris Riris, Jennifer Fowler, Melissa Yang Martin (FireSense)

**Non-NASA Agency Relationships:**
- National Interagency Fire Center (NIFC)
- CAL FIRE (California's state fire agency)
- Boulder County Parks and Open Space

### Access to Wildfire Airspace
**Key Finding:** No universally-accepted standardized method for gaining UAS access to active fire operations exists
- Each local fire agency maintains unique rule sets and requirements
- Networking and relationship-building identified as most reliable access pathway
- Stepped approach recommended: early flights outside closed airspace or at night when crewed aircraft inactive
- Risk-mitigation techniques identified with fire agencies for safe mixed-aircraft operations

### Integration with Existing Tools
**Team Awareness Kit (TAK) Pathway:**
- ATAK (Android Team Awareness Kit) widely adopted in wildfire community
- Colorado-specific version (COTAK) being actively developed with CoE resources
- Existing pathways identified within TAK for distributing UAS observations
- 3rd party plugin development planned for enhanced integration
- Planned Phase II effort to integrate swiftTab features directly into ATAK

**Commercial Opportunities:**
- Growing demand for UAS in wildfire operations (larger and more destructive fires annually)
- Identified customers: land management agencies, state and federal wildland fire departments
- Market includes drone services, environmental monitoring, remote sensing services sectors
- Investment interest noted; state government purchasing pathways identified

### Regulatory & Operational Requirements
- 2021 fatal air tanker crash (nighttime operation) demonstrated urgent need for improved wind forecasting
- Safety-critical requirement for accurate 3-12 hour wind evolution predictions
- TRL assessment: Begin and End TRL at 4 (technology demonstration in relevant environment)

### Future Development Priorities
1. **Further ESA-based planning:** Improve logistical forecasting with alternative site selection; balance model impact with road access and cellular coverage
2. **End-to-end data pipeline:** Complete software tools for automated mid-flight data broadcasting and real-time model assimilation
3. **Continued flight operations:** Simultaneous multi-UAS flights in prescribed burn operations to validate hardware/methods and demonstrate technology to fire agencies
4. **Hardware improvements:** Tool-less assembly, LED illumination, strobe lighting for night operations, updated carrying case design
5. **Extended flight testing:** Validate new S0 design safety and durability; build critical flight hours and agency relationships

### Phase II Plans
- Conduct Observing System Simulation Experiments (OSSEs) to determine optimal UAS spacing
- Full integration into wildfire airspace with coordinated crewed/uncrewed operations
- Real-time operational capability development with incident commander interface
- Potential integration with NASA FireSense prescribed burn campaigns