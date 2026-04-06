# Uncrewed Aircraft System Data Assimilation for Improved Wildland Fire Fighting Decision Support

## Document Metadata
- Type: Phase I SBIR Final Report
- Client/Agency: NASA Langley Research Center (LaRC)
- Program/Solicitation: NASA SBIR 2023-I, Subtopic A3.02 (Advanced Air Traffic Management for Nontraditional Airspace Operations)
- Date: February 2024
- Contract Number: 80NSSC23PB371
- BST Products/Systems Referenced: S0 VTOL, S1 UAS, SwiftTab User Interface, SwiftCore (implied)
- Key Personnel: Jack Elston (PI), Maciej Stachura (Lead Engineer), James Pinto (co-I, NCAR)

## Executive Summary
Black Swift Technologies conducted a Phase I SBIR project demonstrating how uncrewed aircraft system (UAS) observations can improve wind and turbulence forecasts around wildland fires using data assimilation techniques. The effort developed an updated S0 VTOL platform optimized for mountainous/fire conditions, created software tools for converting meteorological data to WMO standards, demonstrated significant forecast improvements through ensemble Kalman filter assimilation, and established partnerships with fire agencies to enable operational integration via the Team Awareness Kit (TAK).

## Technical Approach

**Core Methodology:**
- Partner with NCAR/RAL to perform Ensemble Sensitivity Analysis (ESA) on high-resolution (1 km) model ensembles to identify optimal UAS profiling locations for gap-filling observations
- Deploy S0 VTOL in identified sensitive regions to conduct 2-3 hour continuous profiling using spiral flight patterns (30m-120m AGL)
- Assimilate UAS meteorological observations using NCAR's Ensemble Kalman Filter (EnKF) framework within the Data Assimilation Research Testbed
- Convert raw UAS data into WMO standard netCDF and PREPBUFR formats for rapid ingestion into operational weather models
- Distribute improved wind/turbulence products to wildland fire incident commanders via TAK and other decision support systems

**ESA Approach:**
- Extract relationships between response variables (e.g., maximum 10-m wind gust speed) and predictor fields (e.g., sea-level pressure from 3 hours earlier)
- Use 40-member ensemble to identify error-growth regions where additional observations would have maximum impact on critical fire weather parameters
- Deployed two UAS simultaneously to capture spatial variability across sensitivity regions

**Data Assimilation Validation:**
- Tested on 5 January 2024 case with strong east-to-west wind gradient in Boulder County
- Held out surface observations from ASOS stations to assess independent impact of UAS DA
- 40-member ensemble cycled hourly starting 1800 UTC, initialized from NCEP HRRR forecasts

## Products & Capabilities Described

### S0 VTOL
- **Description:** Small, vertical takeoff and landing UAS designed for weather sensing and deployment from rough terrain
- **Use in this project:** Primary platform for collecting atmospheric data near wildfires; deployed in mountainous Boulder County foothills
- **Specifications/Performance:** 
  - Capable of operating from 30m to 120m AGL in spiral patterns
  - Equipped with multi-hole pressure probe payload for wind/temperature/humidity sensing
  - 2-3 hour continuous profiling capability
  - Can execute spiral climb/descent rates of 0.5–2.0 m/s
  - Hardware redesigned for ruggedization: enhanced multi-hole probe protection against rain/smoke/ash; new high-capacity battery design; resilient pitching motor mounts; higher wing location
  - Structural analysis completed on fuselage loading, thrust/weight/controllability, and wing flutter
  - Planned improvements: tool-less assembly, LED-illuminated servo pockets, high-visibility strobe for night ops, hard-shell carrying case for multi-aircraft transport

### S1 UAS
- **Description:** Companion UAS platform used in data collection efforts
- **Use in this project:** Coordinated multi-UAS operations on 5 January 2024; simultaneous profiling 15 km apart from S0
- **Specifications:** Operated at 400 ft AGL; consistent wind measurements with S0; compared temperature/humidity profiles

### Data Conversion Software
- **Description:** Automated tools to convert raw S0/S1 meteorological data into standardized formats
- **Formats produced:** WMO standard CF-compliant netCDF and PREPBUFR
- **Validation:** Successfully tested with NCAR's data assimilation system; compatible with modeling centers worldwide
- **Special capability:** Developed QC wind orbit calibration technique using GPS ground speed to validate wind estimates without towers/radiosondes; tested against DOE Southern Great Plains 25m and 60m meteorological towers (March-April 2021)

### SwiftTab User Interface
- **Description:** Android-based display interface previously developed by BST
- **Proposed use:** Prototype for enhanced data visualization in wildfire operations, including real-time weather/wind display, scalar value plotting (trace gases, particle sizing), and geo-located shapes (fire perimeter)
- **Integration plan:** Leverage SwiftTab features to inform Phase II updates to ATAK application

### Team Awareness Kit (ATAK) Integration
- **Description:** Existing Android-based platform (AFRL, now TAK Product Center) for team communications and geospatial data dissemination
- **Use context:** Selected as primary pathway for distributing UAS observations and improved forecasts to incident commanders
- **Variants:** COTAK (Colorado wildfire version), WFTAK (broader wildfire community version)
- **Planned implementation:** Custom plugin development via Colorado Center of Excellence to enable all-in-one asset management and data dissemination; automate mid-flight data broadcasting; enable live assimilation updates during persistent monitoring

## Use Cases & Applications

### Wildland Firefighting Operations
- **Primary use case:** Provide real-time low-level wind and turbulence forecasts to support safe operation of crewed and uncrewed aircraft during active fire suppression
- **Specific scenario:** Boulder County foothills wildfires (e.g., Calwood Fire, 17 October 2020)
- **Decision support:** Enable afternoon weather shift predictions, support nighttime operations planning, provide 6-12 hour tactical forecasts for incident commanders
- **Example impact:** Calwood Fire case showed need for accurate forecasts of sudden wind shifts (westerly to easterly with passage of cold front) that drove fire behavior changes

### Prescribed Burn Operations
- **Application:** Support pre-burn planning and real-time operations management for controlled burns
- **Planned partnership:** NASA FireSense team collaboration on prescribed burn demonstrations

### Advanced Air Mobility (AAM)
- **Related application:** Technology expansion to provide 3D wind forecasts for AAM operations in mountainous areas and urban corridors (mentioned as NASA Ames potential customer)

### Earth Science/3D Winds Mission
- **Long-term application:** Support NASA's 3D-Winds mission articulated in National Research Council decadal survey

## Key Results

### Ensemble Sensitivity Analysis Demonstration
- Successfully implemented ESA technique on Calwood Fire case (October 2020) to identify optimal UAS profiling locations
- Identified two regions of enhanced sensitivity: positive values west-northwest of fire; larger area of negative sensitivities southwest
- Broader contiguous sensitivity area indicated multiple UAS should be deployed for maximum impact (recommended 4-6 UAS sites)

### Data Assimilation Impact on Wind Forecasts (5 January 2024 Test)
- **10-m u-wind:** Bias reduced >50%; RMSE reduced 30%
- **10-m v-wind:** Smaller but notable improvements
- **Wind direction:** 50-degree improvement at Boulder Airport (BDU); mean direction shifts at nearby ASOS stations
- **Relative humidity:** Dry bias notably reduced
- **Spatial extent:** Impact greatest at profiling sites (BDU and adjacent foothills); diminished 36 km away at C99, indicating need for denser UAS network in complex terrain

### Data Format Validation
- Successfully converted S0/S1 raw flight logs to WMO netCDF format (October 2023 test with 4 flights)
- NCAR validated compatibility with data assimilation system
- Determined optimal climb/descent rate of 2.0 m/s for future missions (highest data density with lowest sensor variance)

### Multi-UAS Operations Demonstration
- Conducted time-synchronized dual-UAS flights on 5 January 2024
- Aircraft spaced 15 km apart (exceeding 10 km minimum useful spacing for DA)
- Both aircraft executed synchronized spiral patterns (30–120 m AGL, 2 m/s climb/descent rates)
- Successfully ingested coordinated data into models

### Hardware Improvements to S0
- Completed structural analysis (fuselage, propulsion system, wing flutter)
- Redesigned multi-hole probe enclosure for rain/smoke/ash protection
- New high-capacity battery design and resilient motor mounts
- Higher wing location to accommodate new propulsion components
- All modifications validated through analysis

## Notable Details

### Partnerships Established
- **NCAR/RAL:** Critical meteorological component partner; performs ESA analysis, EnKF data assimilation, wind/turbulence product generation
- **Colorado Center of Excellence (CoE) for Advanced Technology Aerial Firefighting:** Interoperability liaison for TAK integration; access pathway to local prescribed burns
- **NASA ACERO:** Airspace management research team; planned demo opportunities for mixed crewed/uncrewed operations
- **NASA FireSense:** Earth science integration with operational fire agencies; future prescribed burn collaboration
- **National Interagency Fire Center (NIFC):** Policy and real-world operations insights; access to federal fire agency perspectives
- **CAL FIRE (California):** Technology adoption criteria and statewide wildfire operations experience
- **Boulder County Parks and Open Space:** Local prescribed burn access

### Regulatory/Operational Barriers Addressed
- **Issue:** No standardized access procedure for UAS in active wildfire airspace; each local fire agency has different requirements
- **Solution:** Stepped approach—early flights outside closed airspace or at night when crewed aircraft inactive; eventual full integration goal
- **Mitigation strategies:** Risk assessment and mitigation techniques compiled based on fire agency input; emphasis on safety demonstrations to gain airspace access

### Commercialization Potential
- Growing market demand due to increasing severity/scale of wildland fires
- Target customers: Land management agencies, state/federal wildland fire departments, incident commanders
- Value proposition: Enhanced situational awareness and safety for mixed crewed/uncrewed operations in complex terrain

### Technology Readiness
- Phase I end TRL: 4 (technology demonstrated in lab/experimental environment)
- Phase II planned: Development toward operational real-time capability; integration into existing fire management tools

### Future Planned Developments
- **Phase II partnerships:** Continue NCAR/RAL and CoE collaboration; scale to real-time capability
- **Mission infusion:** NASA FireSense and ACERO technology demonstration programs
- **Hardware evolution:** Tool-less assembly, night-capable strobes, multi-aircraft transport cases
- **Data pipeline completion:** End-to-end automated data broadcasting; live model assimilation during persistent monitoring
- **Operational flights:** Simultaneous multi-UAS deployment in prescribed burns to validate technology with fire teams and gather flight hours
- **Airspace integration:** Demonstrate S0 safety in rough terrain to enable access to active wildfire spaces

### Market Analysis Scope
- Includes UAS systems market, drone services, environmental monitoring, remote sensing services, wildland fire sector
- Identified government customers at federal, state, and local levels
- Investment landscape and networking/intelligence gathering efforts conducted at industry conferences and LinkedIn forums