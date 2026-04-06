# Autonomous and Lagrangian Ocean Observations for Atlantic Tropical Cyclone Studies and Forecasts

## Document Metadata
- **Type:** Scientific journal article / reference publication
- **Client/Agency:** NOAA (National Oceanic and Atmospheric Administration), various institutions
- **Program/Solicitation:** Not a proposal or solicitation—this is a published reference article used in BST's 2018 NOAA SBIR Phase I work
- **Date:** Published June 2017 (Oceanography, Vol. 30, No. 2)
- **BST Products/Systems Referenced:** None directly mentioned
- **Key Personnel:** Multiple NOAA, WHOI, Rutgers, and other institutional researchers (not BST personnel)

## Executive Summary
This peer-reviewed oceanography article surveys the use of autonomous and Lagrangian platforms and sensors (ALPS)—including surface drifters, profiling floats, underwater gliders, and dropsondes—to collect upper-ocean observations in tropical cyclones. The article demonstrates how these platforms provide critical in situ data for initializing hurricane intensity forecast models and improving predictions by 40–50%, addressing a major gap where Atlantic TC intensity forecast errors have plateaued for 25 years despite track forecast improvements.

## Technical Approach
The article reviews multiple observational platforms:

1. **Drifters (SVP, SVPW/Minimet, ADOS)**
   - Measure 15 m depth currents, SST, sea level pressure, surface winds
   - ADOS drifters have 150 m thermistor chains with pressure/temperature sensors spaced 10 m apart, sampling every 15 minutes
   - Deployed ahead of storms via aircraft to intercept forecast track
   - 207 drifters deployed in Atlantic and Pacific over 15 years with 92% success rate

2. **Profiling Floats (ALAMO – Air-Launched Autonomous Micro-Observer)**
   - Air-deployable profiling floats conforming to Hurricane Hunter aircraft sonobuoy launch system
   - Can carry temperature, pressure, salinity sensors, and accelerometers for wave observations
   - Single float provides hundreds of temperature profiles before, during, and after storms
   - 60 ALAMO floats deployed 2014–2016 in Atlantic and eastern North Pacific
   - Programmable mission parameters allow dynamic changes in profile frequency and depth

3. **Underwater Gliders**
   - Autonomous vehicles collecting sustained or targeted observations over continental shelves and open ocean
   - Can attempt to hold station during storm passage
   - Carry CTDs plus optical sensors (plankton/particulates), oxygen sensors, acoustic Doppler current profilers
   - Deployed from 1–2 weeks to full hurricane season
   - Used operationally off Puerto Rico, Bermuda, and US East Coast

4. **Dropsondes (including IRsondes)**
   - GPS dropsondes measure pressure, temperature, humidity, winds
   - Upgraded "IRsonde" (2013+) includes infrared SST measurement capability
   - 200+ IRsondes built; 57 deployed during Hurricane Edouard (2014)
   - Used for first time to capture coincident atmospheric structure and air-sea interface data
   - IRsonde SSTs show good agreement except under heavy rain (>20 dBz reflectivity); R² = 0.901 in light/no-rain conditions

**Real-time data transmission:** All platforms transmit via Global Telecommunication System (GTS) for operational forecast assimilation; data also available through Iridium, FTP, and web services.

## Products & Capabilities Described

### ALAMO (Air-Launched Autonomous Micro-Observer)
- **Function:** Autonomous profiling float deployable from Hurricane Hunter aircraft during operational recon missions
- **Deployment:** 60 floats in 2014–2016; programmed for extended operation before, during, and after storms
- **Key capability:** Hundreds of profiles per float; shown 50% reduction in forecast errors when assimilated (Hurricane Matthew 2016, COAMPS-TC model)
- **Advantages:** Deployable from existing aircraft tasked with hurricane surveillance; long mission life; ability to resolve mesoscale ocean structure

### ADOS (Autonomous Drifting Ocean Station)
- **Function:** Air-deployed surface drifter with subsurface temperature/pressure chain
- **Design:** 150 m thermistor chain with sensors 10 m apart, inductive data transmission
- **Sampling:** 15-minute intervals; measures currents, SST, sea level pressure, surface winds
- **Deployment:** Preferentially on right side of storm track (stronger winds)
- **Performance:** 92% success rate over 207 deployments

### SVP/SVPW (Surface Velocity Program / SVP Wind)
- **Function:** Standard and wind-enhanced surface drifters
- **Sensors:** Sonic anemometers, internal compass (±2° accuracy)
- **Use:** Sustained hourly observations of SST, SLP, surface winds
- **Operational role:** NOAA Global Drifter Program; air-deployed ahead of TCs

### IRsonde
- **Function:** GPS dropsonde with infrared SST sensor
- **Advantage:** First tool to capture co-located atmospheric and SST data simultaneously
- **Limitations:** Cold bias in moderate-to-heavy rain; good performance in light/no-rain conditions and within hurricane eye
- **Future:** To be integrated into unmanned aircraft systems (UAS), specifically the Coyote autonomous aircraft

## Use Cases & Applications

### Hurricane Intensity Forecasting
The primary application throughout the document:
- Upper-ocean heat content (measured via temperature and salinity profiles) is linked to TC intensification capability
- Assimilation of ALPS observations reduces upper-ocean thermal bias and corrects mesoscale feature errors in forecast model initialization
- Errors in enthalpy flux estimates lead to biased intensity predictions; in situ profiles correct these errors

### Specific Hurricane Cases Analyzed

**Hurricane Isaac (August 2012)**
- 10 drifters deployed August 26, 2012 across Gulf of Mexico
- Captured center passage with high temporal resolution (15-min intervals)
- Documented SLP ~982 hPa, wind speeds >45 kts, storm-induced cooling and post-storm SST recovery
- Provided rare detailed description of pressure/wind structure and cold wake

**Hurricane Joaquin (October 2015)**
- ALAMO float 9068 deployed October 3, 2015
- Documented strong inertial oscillations from storm passage
- Showed programmable profiling frequency/depth adjustments during storm

**Hurricane Gonzalo (2014)**
- Glider deployed north of Puerto Rico; hurricane intensified from Cat 2→3 nearby
- Glider observations revealed low-salinity "barrier layer" (upper 20 m) suppressing hurricane-induced cooling and favoring intensification
- Assimilation of glider data into HWRF-HYCOM coupled model:
  - **50% reduction in maximum wind speed errors** in 126-hour forecast
  - Significantly improved thermal and saline initialization, especially barrier layer representation
- Gonzalo then passed ~85 km northeast of BIOS glider near Bermuda (previously sampling Fay aftermath):
  - Documented 4°C surface cooling, 50 m mixed-layer deepening in cold wake
  - Gonzalo weakened Cat 4→3 over Fay's cold wake

**Hurricane Sandy (2012)**
- Glider (RU23) deployed 5 days ahead on New Jersey continental shelf
- Equipped with acoustic Doppler current profiler for vertical shear measurement
- Findings: Downwelling-favorable winds limited cold bottom water supply; surface cooling limited to 1–2°C
- Contributed to understanding of continental shelf response

**Hurricanes Arthur (2014) and Hermine (2016)**
- TEMPESTS program glider deployments on US northeast continental shelf
- Arthur: rapid transit through region, minimal inertial oscillations
- Hermine: stalled, dissipated south of New England, generated inertial oscillations
- Both caused cooling, mixed-layer deepening, westward flow
- Data assimilated into ESPreSSO (Experimental System for Predicting Shelf and Slope Optics) model

**Hurricane Edouard (2014)**
- 30 IRsonde-bathythermograph pairs deployed September 15–17, 2014
- Demonstrated IRsonde technology maturity: R² = 0.901 for SST comparison in light/no-rain conditions
- Identified rain contamination effect; good eye measurements

## Key Results

### Impact on Forecast Skill
- **Hurricane Gonzalo (2014):** ~50% reduction in 126-hour maximum wind speed forecast errors with glider data assimilation
- **Hurricane Matthew (2016):** Significant ocean forecast error reductions with ALAMO data assimilation in COAMPS-TC model
- **Drifters (general):** Proven to constrain satellite SST errors and biases; improve numerical weather prediction (examples: Centurioni et al. 2016; Horányi et al. 2017)

### Platform Deployment Success & Scale
- **Drifters:** 207 deployed (1993–2008+) with 92% success rate; operational in Cat 1–5 storms
- **ALAMO floats:** 60 deployed 2014–2016; long mission life demonstrated
- **Gliders:** Operational in Atlantic (Puerto Rico, Bermuda, US East Coast); sustained and rapid-response modes
- **Dropsondes:** 57 IRsondes deployed during Edouard; demonstrating new SST measurement capability

### Ocean-Atmosphere Coupling Insights
- Barrier layers (low-salinity upper layers) suppress storm-induced SST cooling and can favor TC intensification
- Cold wakes from previous storms weaken subsequent TCs
- Mesoscale ocean structure (fronts, eddies, stratification) has significant impact on intensity evolution
- Upper-ocean heat content (TCHP) above 26°C isotherm is critical predictor

### Data Availability & Real-Time Performance
- Near-real-time data transmission via GTS enables operational assimilation
- ALAMO and gliders transmit via Iridium; drifters via multiple routes (GTS, FTP, web)
- Data quality control and distribution support operational forecast centers

## Notable Details

### Motivation for BST Interest (Inferred)
This article was cited in BST's 2018 NOAA SBIR Phase I proposal, likely because:
1. **ALPS observing systems** (drifters, floats, gliders, dropsondes) address a critical gap in TC forecasting
2. **Real-time data needs** from remote platforms suggest opportunity for autonomous systems innovation
3. **Air-deployment emphasis** (ALAMO, ADOS, IRsonde via aircraft) aligns with potential BST aircraft/UAS capabilities
4. **Operational integration** with Hurricane Hunter aircraft and National Hurricane Center reflects mature transition pathway

### Key Recommendations from Authors
- Continue assessing quantitative impact of upper-ocean thermal and salinity structure on TC intensification
- Enhance autonomous vehicle and Lagrangian observations in Caribbean, Gulf of Mexico, and tropical North Atlantic
- Develop comprehensive rapid-response effort for pre-storm upper-ocean heat content assessment
- Conduct Observing System Experiments (OSEs) with actual observations and OSSEs with synthetic observations
- Design optimal horizontal spacing (0.5–1.0° or better) for mesoscale structure resolution
- Deploy multiple ALPS platforms covering region at least as large as TC diameter
- Coordinate international effort given global scope (7 TC-genesis regions)

### Platforms Mentioned for Future Development
- **Coyote UAS** (Unmanned Aircraft System): autonomous aircraft to carry IRsonde sensors for remote SST measurement within hurricane environment (transition starting fall 2017)
- **Enhanced drifter sensors:** directional surface wave properties; added relative humidity and air temperature to ADOS/Minimet packages
- **HWRF-HYCOM coupling:** high-resolution coupled forecast system benefiting from data assimilation

### Institutions & Programs Referenced
- NOAA AOML (Atlantic Oceanographic and Meteorological Laboratory)
- National Hurricane Center (NHC)
- WHOI (Woods Hole Oceanographic Institution)
- BIOS (Bermuda Institute of Ocean Sciences)
- CARICOOS (Caribbean Coastal Ocean Observing System)
- Rutgers University, University of Puerto Rico
- TEMPESTS program (The Experiment to Measure and Predict East coast STorm Strength)
- CBLAST, ITOP field programs (earlier foundational work)

### Competitive Advantage Indicators
- Platforms with **air-deployability** and **real-time tel