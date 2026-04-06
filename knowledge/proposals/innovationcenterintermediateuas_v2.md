# An Intermediate UAS for Safe Observation of Volcanic Activity

## Document Metadata
- Type: Proposal/capability brief
- Client/Agency: USGS Volcano Science Center
- Program/Solicitation: USGS volcano monitoring need (not a formal SBIR/contract)
- Date: June 28, 2019
- BST Products/Systems Referenced: Black Swift S2 UAS
- Key Personnel: Jack Elston (last editor)

## Executive Summary
This proposal requests development of an intermediate-size unoccupied aerial system (UAS) for safe, remote volcanic observation during volcanic crises. The USGS Volcano Science Center identified a need for a platform capable of flying 10-15 km from safe staging areas to reach active volcanoes, reaching altitudes of 10,000-15,000 feet, and remaining on station for 15+ minutes to conduct gas composition and emission rate measurements before returning safely. Black Swift Technologies' S2 platform is identified as the preferred technology partner for this mission.

## Technical Approach
The proposed system would integrate multiple gas and environmental sensors into a modular payload package flown on the S2 UAS. The UAS would:

1. **Launch Phase**: Depart from safe distance (10-15 km away), climb to volcanic altitude
2. **Observation Phase**: Conduct low-altitude flights (~150 ft above terrain) to characterize volcanic gases and measure vertical column density
3. **Data Telemetry**: Stream monitoring data in real-time to operating team for adaptive decision-making
4. **Return Phase**: Recover safely to staging area with all data and sensors

**Flight Operations Geometry**:
- "Lawnmower pattern" at low altitude to establish spatial distribution of gas emissions
- "Ladder traverse" geometry downwind to contour gas plumes and measure emission rates
- Multiple passes to characterize composition and rate measurements

**Sensor Package** (modular, integrated design):
- **CO2**: LI-COR 850 instrument, >1 ppm precision (with digital communications port for bench temperature and sample pressure)
- **SO2 and H2S**: CityTech electrochemical sensors, >100 ppb precision
- **Water Vapor**: Relative humidity probe with heated inlet to prevent condensation
- **UV Spectrometry**: Ocean Optics FLAME-S spectrometer with upward-looking optics for SO2 vertical column density measurement (>99.9% signal-to-noise ratio, low stray light)
- **Environmental Data**: 3D wind field measurement (compensating for aircraft motion), temperature, pressure, relative humidity, GPS track, wind speed and direction

## Products & Capabilities Described

### Black Swift S2 UAS
- **Range**: 90 km
- **Flight Ceiling**: 20,000 ft (document note suggests 15,000 ft more realistic for current testing; 20,000 ft requires specialized wing set not yet tested)
- **Maximum Payload**: 2.3 kg
- **Nose Cone**: 8-inch diameter (accommodates full gas sensor suite)
- **Endurance**: Sufficient for 15+ minute observation segment after 10-15 km transit
- **Capabilities**: Real-time data telemetry, flight planning interface optimized for atmospheric sampling missions

### Black Swift Existing Experience/Integrated Sensors
- LI-COR 840A CO2 sensor (previously integrated)
- PP-Systems CO2 sensor (previously integrated)
- CityTech SO2 and H2S sensors (previously integrated)
- Developed in-house 3D wind field sensor
- Temperature, pressure, and relative humidity logging
- Real-time data telemetry capability
- Flight planning interface for atmospheric sampling flights

## Use Cases & Applications

### Volcanic Gas Emissions Characterization
Primary use case: measuring volcanic degassing during crisis periods when in-situ manned observation is impossible due to hazards (explosions, toxic gases, unpredictable activity).

**Key Measurements Enabled**:
- Gas composition (H2O, CO2, SO2, H2S relative abundances)
- SO2 vertical column density and total emission rates
- CO2 emission rates (proxy for magma supply rate to deep plumbing system)
- Spatially distributed degassing features

## Potential Test Sites

### Test Site 1: Kilauea Volcano, Hawaii
**Context**: 2018 volcanic crisis with Lower East Rift Zone (LERZ) fissure eruptions
**Scientific Need**: SO2 emissions at summit dropped to near-detection levels by August 2018 (previously several thousand tons/day), making traditional CO2/SO2 ratio method for measuring CO2 flux impossible. CO2 measurements are critical proxy for magma supply to summit reservoir.

**Proposed Measurement Strategy**:
- Low-altitude lawnmower pattern flights to map spatial distribution of CO2 degassing features at summit
- Ladder traverse geometry downwind of sources to contour CO2 plume
- Interpolate plume contours to determine CO2 burden in plume slice
- Multiply by wind speed to derive total CO2 emission rate
- Enables HVO to resume monitoring of magma supply rate to Kilauea's deep system

**Operational Feasibility**: Established infrastructure and research team at Hawaiian Volcano Observatory (HVO)

### Test Site 2: Makushin Volcano, Alaska
**Context**: Active volcano, rated "Very High Threat" in National Volcano Early Warning System (NVEWS); 25 km west of Dutch Harbor, Unalaska Island, eastern Aleutians; summit elevation 1,800 m

**Current Monitoring**: 2018 gas survey detected hundreds of tons SO2/day (indicates shallow magma). Follow-up survey planned summer 2019, but requires costly helicopter support.

**Proposed Operations**:
- Team deployment via commercial flight to Dutch Harbor
- UAS staging from accessible location near town
- Transit to Makushin (25 km) while climbing to summit elevation
- Multiple low-altitude passes to characterize gas composition
- 1 km downwind passes beneath gas plume using upward-looking spectrometer for SO2 emission rate
- Return to Dutch Harbor with all measurements
- Feasible for annual monitoring missions to detect changes indicating imminent eruption

**Advantages**: Represents archetypal volcano where intermediate-size UAS would revolutionize USGS monitoring capabilities; currently limited by expensive helicopter logistics

## Notable Details

1. **Science Need**: Document emphasizes that close-range volcanic observation with small UAS is insufficient for Cascades and Alaska volcanism, which is often explosive and highly unpredictable, making safe approaches impossible during crises.

2. **Operational Safety**: The entire system design prioritizes safe operations at distance—10-15 km standoff range allows teams to stage at safe locations while still conducting effective observations.

3. **Real-Time Adaptability**: Real-time data telemetry enables operators to adapt observation strategy to actual volcanic conditions, which may be poorly characterized at crisis onset.

4. **Black Swift Competitive Advantage**: Document explicitly notes BST's prior experience with the specific sensors, 3D wind measurement, and atmospheric sampling flight planning—significantly streamlining integration and expediting testing timeline.

5. **Sensor Integration Complexity**: Full gas sensor suite (6 distinct measurement types) is modular and designed for concurrent operation, enabling characterization of both composition AND emission rate in single flight (a capability limitation of previous small UAS work).

6. **Test Site Prioritization**: Document notes that final selection between Kilauea and Makushin should wait until instrument integration is complete, given uncertainties in flight permitting and volcanic activity forecasting in coming year (document written June 2019 for planned 2019-2020 testing).

7. **Technical Note**: Footnote indicates S2 flight ceiling specification of 20,000 ft requires specialized wing set not yet tested; conservative planning suggests 15,000 ft as more realistic near-term capability.