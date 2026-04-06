# Advancing the Capabilities of UAS to sample Tropical Cyclones at the Ocean Surface to Improve NOAA Forecasts

## Document Metadata
- **Type:** Research proposal / Grant application
- **Client/Agency:** NOAA (National Oceanic and Atmospheric Administration) - Office of Oceanic and Atmospheric Research (OAR) and Office of Marine and Aviation Operations (OMAO)
- **Program/Solicitation:** Internal NOAA 2025 Request for Proposals - "Breakthroughs with UxS Technologies" RFP; OAR UxS Research Transition Office and OMAO UxS Operations Center
- **Date:** Submitted October 18, 2024 (draft)
- **BST Products/Systems Referenced:** Black Swift S0
- **Key Personnel:** 
  - Dr. Joseph J. Cione (Principal Investigator, NOAA/AOML, Miami)
  - Dr. Jun A. Zhang (Co-PI, NOAA/AOML)
  - Dr. Joshua B. Wadler (Co-PI, Embry-Riddle Aeronautical University, Daytona Beach)
  - Dr. Guo Lin (Senior Researcher, NOAA/AOML)
  - Dr. Ghassan Alaka (Division Director, NOAA/AOML)

## Executive Summary
This proposal seeks funding to advance the Black Swift S0 small uncrewed aircraft system (sUAS) toward operational status for routine deployment from NOAA's WP-3D (P-3) reconnaissance aircraft to sample tropical cyclones (TCs). The project aims to improve TC intensity and structure forecasts by providing high-resolution, in-situ observations of atmospheric turbulence, winds, and surface conditions in the planetary boundary layer and ocean surface layer—critical regions currently undersampled by traditional aircraft and dropsondes. Real-time data will be delivered to NOAA's National Hurricane Center (NHC) and Environmental Modeling Center (EMC) to improve situational awareness and data assimilation in operational forecast models.

## Technical Approach

### Overall Strategy
- Deploy Black Swift S0 aircraft from NOAA P-3 aircraft into tropical cyclones to sample the planetary boundary layer (PBL) and surface layer
- Provide real-time, quality-controlled meteorological data to NHC and EMC operational centers
- Analyze sUAS turbulence observations to improve parameterizations in NOAA's coupled Hurricane Analysis and Forecast System (HAFS) and Next-Generation Unified Forecast System (UFS)
- Transition the S0 from research platform (Readiness Level 8-9) to operational status

### Three-Year Project Timeline
- **Project Period:** June 1, 2025 to May 31, 2027
- **Budget:** Not disclosed in draft (marked as "----")

### Key Technical Components

#### 1. **Hardware and Payload Improvements to S0**
- **Dual GPS for heading:** Replace single GPS with dual GPS system to improve heading accuracy and wind velocity measurements, especially when GPS signal weakens in high-precipitation regions
- **Data buffering and re-transmission:** Enable the S0 to buffer data during communication loss and re-transmit once link is reestablished (addressing current limitation where data from communication lapses is lost)
- **Laser optimization for rain:** Reconfigure downward-pointing laser altimeter for optimal performance in heavy precipitation (eyewall, rainbands) to accurately measure wave characteristics for air-sea interaction studies
- **Onboard video camera:** Install real-time video capability for situational awareness and mission documentation

#### 2. **Operational Efficiency Optimization**
- **Firmware and interface customization:** Increase platform autonomy so P-3 crew can operate the S0 without onboard sUAS pilot; streamline user interface to display critical flight parameters
- **Extended endurance:** Improve battery life from current ~1.5 hours to ~2 hours through battery optimization
- **External CAD launch system:** Replace internal free-fall chute deployment (which requires P-3 pressurization and cabin movement) with external Cartridge Actuated Device (CAD) launch to simplify in-storm operations
- **Enhanced airOPS integration:** Add data fields to NOAA's Aircraft Operations Center onboard situational awareness tool (airOPS) including laser altitude, radio signal quality, and time since last communications
- **USB firmware update capability:** Develop system for firmware updates via USB connection on deployment tube without removing aircraft from tube
- **Real-time data file generation:** Automate quality-control processing to create real-time netCDF meteorological files (currently takes days post-mission)

#### 3. **Ensuring Consistent Meteorological Measurements**
- **Wind tunnel characterization:** Test S0 to quantify wing effects on multi-hole pressure probe wind measurements
- **Higher measurement frequency:** Increase measurement reporting from current 2-3 Hz to at least 10 Hz to resolve turbulence-scale processes (currently limited by radio bandwidth)
- **Laser-based altitude control:** Develop capability for S0 to maintain consistent height above sea surface using laser altimeter reading rather than GPS/pressure altitude (to eliminate GPS drift errors at very low altitudes <50 m)

## Products & Capabilities Described

### Black Swift S0 Specifications
- **Mass:** 1.58 kg (~3 pounds)
- **Cruise speed:** 26 m/s
- **Wingspan:** 1.38 m
- **Maximum battery life (current):** ~1.5 hours (proposed: ~2 hours)
- **Maximum altitude:** ~4,600 m
- **Deployment method:** Attached to parachute in cylindrical container, deployed from A-sized sonobuoy chute on P-3; wings unfold after release; recovery to controlled flight within 1,500 ft of deployment altitude
- **Operating range:** Non-recoverable over water; communicates via two-way radio link to P-3 receiver
- **Flight modes:** GPS altitude and pressure altitude capable
- **Key instruments:**
  - Multi-hole pressure probe for turbulence measurements
  - Standard wind measurement system
  - Downward-pointing laser altimeter (operates below 300 ft, optimized for non-precipitating conditions in current version)
  - Temperature and humidity sensors
  - Pressure sensors
  - GPS with heading capability

### Current Operational History
- **Development:** Awarded SBIR (Small Business Innovation Research) contract in 2018
- **Recent deployments:**
  - Hurricane Tammy (2023): 2 S0s deployed
  - Hurricane Ernesto (2024): 4 S0s deployed
  - Hurricane Francine (2024): 4 S0s deployed
- **Current readiness level:** 8-9 (approaching operational transition)

## Use Cases & Applications

### Tropical Cyclone Intensity and Structure Forecasting
- **Primary application:** Sample the planetary boundary layer (PBL) at altitudes of ~10-1,000 m, including down to ocean surface layer—the critical region where TCs exchange momentum and enthalpy with the ocean
- **Specific measurements:**
  - Wind velocity (including turbulent fluctuations and gustiness)
  - Atmospheric pressure
  - Temperature and humidity
  - Sea surface characteristics (wave height/roughness via laser)
  - Turbulent kinetic energy (TKE)
  - Vertical eddy diffusivities of momentum, heat, and moisture

### Near-Surface Wind Observations
- Obtain accurate wind measurements in the high-wind surface layer of hurricanes (hurricane-force regime)
- Support NOAA's prototype 2-D surface wind analysis system (under development by CIRA)
- Improve real-time situational awareness for NHC forecasters

### Upper-Level/Outflow Layer Observations (Proposed Expansion)
- Document notes that the TC outflow layer (~14-16 km) is undersampled and related to TC intensity change and diurnal cycle
- Current capabilities: G-IV aircraft and previous NASA Global Hawk deployments use dropsondes for this region
- Proposal references need for consistent upper-level measurements to improve TC track forecasts

## Key Results (Proposal-Based Objectives, Not Yet Completed)

### Project Objectives
1. **Significantly enhance observations of atmospheric turbulence within the TC PBL and surface layer** (currently only sUAS can obtain in-situ turbulence-quality measurements throughout TC PBL to ocean surface layer)
2. **Provide real-time sUAS data to NOAA operational centers** (EMC for data assimilation; NHC for situational awareness)
3. **Use turbulence observations to improve physics in NOAA's coupled TC operational forecast system** (HAFS and future UFS)
4. **Advance sUAS and profiler data use in model improvement and data assimilation toward operational transition**

### Expected Impact Areas
- **Model improvements:** Calculate exchange coefficients (momentum and enthalpy transfers) in hurricane force regime for first time; improve PBL parameterizations and surface layer physics in HAFS
- **Forecast skill:** Enhanced data coverage in undersampled PBL and near-surface regions should improve TC intensity and structure forecasts
- **Operational integration:** Real-time data dissemination to HOT (Hurricane and Ocean Testbed) infrastructure and Cloud AWIPS2 system; integration into AirOPS situational awareness tool; future integration into operational AWIPS2 at NHC
- **Societal benefit:** Improved TC forecasts have potential to save lives, reduce property damage, and increase public confidence in NOAA forecasts

### Data Analysis Plan
- Compute exchange coefficients (drag and enthalpy) from direct turbulent flux measurements via sUAS multi-hole probe and collocated dropsonde/Streamsonde data
- Calculate vertical eddy diffusivities using strain rate and vertical gradients from combined sUAS and Streamsonde observations
- Evaluate HAFS-predicted mean and turbulence structure (TKE, boundary layer height, vertical velocity distribution, eyewall slope, warm core strength/height, vortex tilt) against observations
- Identify model biases to guide future physics upgrades

## Notable Details

### Technical Challenges Addressed
- **GPS reliability in high precipitation:** Dual GPS system to maintain accurate heading when single GPS signal weakens in eyewall/rainband areas
- **Data loss during communications loss:** Buffering and re-transmission capability to capture all measurements despite intermittent radio contact
- **Laser operation in rain:** Reconfiguration for optimal performance in heavy precipitation regions
- **Operational simplicity:** External CAD deployment removes need for P-3 cabin crew movement and pressurization changes during in-storm operations
- **Measurement accuracy at low altitude:** Laser-based altitude control to eliminate GPS drift errors below 50 m altitude
- **Wind measurement integrity:** Wind tunnel testing to characterize wing effects on pressure probe

### Stakeholder Integration
- **Real-time data delivery architecture:**
  - NHC: Via Hurricane and Ocean Testbed (HOT) and Cloud AWIPS2 system; dedicated CIRA Research Associate (HOT facilitator) to maintain dataflow and coordinate visualization displays
  - EMC: Data assimilation into HAFS and future UFS
  - Aircraft Operations Center: Real-time tactical data via AirOPS tool
- **Coordination with CIRA:** Development and testing of prototype 2-D surface wind analysis system for eventual NHC operational transition
- **Data management:** All data stored at NOAA's Atlantic Oceanographic and Meteorological Laboratory (AOML); real-time copies to NHC, EMC, and Aircraft Operations Center; public release after one-year period; code in public repository

### Research Context
- **Prior work:** Team has successfully deployed sUAS in Hurricanes Tammy (2023), Ernesto (2024), and Francine (2024); previous SBIR-funded development by Black Swift Technologies
- **Operational motivation:** Current operational reconnaissance flights at ~3,000 m altitude (700 mb) are too high to sample TC PBL due to safety constraints; dropsondes provide only single vertical profiles with 10-20 per mission; remote sensing limited by spatial/temporal resolution; turbulence observations particularly rare
- **Scientific foundation:** Multiple studies cited demonstrating strong sensitivity of TC intensity simulations to PBL turbulent mixing parameterizations; identification of PBL and surface-layer energy exchange as critical to intensity and intensity change; recognition that high-resolution forecast models require better turbulence parameterization validation

### Partnership and Support
- Principal funding through NOAA OAR/OMAO "Breakthroughs with UxS Technologies" initiative
- Support from Cooperative Institute for Research in the Atmosphere (CIRA) for NHC integration and surface wind analysis system development
- Collaboration with Embry-Riddle Aeronautical University (Dr. Wadler)
- Black Swift Technologies as hardware provider (S0 platform