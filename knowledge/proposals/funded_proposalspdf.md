# NASA FireSense Technology Program (FIRET-23) Funded Proposals

## Document Metadata
- Type: NASA funding announcement / proposal abstracts
- Client/Agency: NASA Science Mission Directorate, Earth Science Technology Office (ESTO)
- Program/Solicitation: NNH23ZDA001N-FIRET; 2023 Research Opportunities in Space and Earth Sciences (ROSES) A.59 - Technology Development for Support of Wildland Fire Science, Management, and Disaster Mitigation
- Date: Updated 12/17/24 (2024)
- Total Funding: Approximately $14.4M over three years (7 projects selected from 49 proposals)
- BST Products/Systems Referenced: None (this document does not reference Black Swift Technologies)

## Executive Summary
This document is a NASA announcement describing seven funded proposals under the FireSense Technology Program (FIRET-23), a technology development initiative seeking innovative Earth system observation capabilities to predict, monitor, and manage wildfires and their impacts. The projects span subcanopy fuel sensing with autonomous drones, stratospheric wildfire detection and communication systems, post-fire water quality forecasting, electrical grid fault-triggered wildfire risk mapping, understory fuel sensing with RF tags, infrared wide-area motion imagery, and fuel-driven wildfire risk mapping algorithms.

---

## Note on Document Content
**This document does not reference Black Swift Technologies or any of its products (S2, S3, SwiftCore, MultiScat, AeroPod, etc.).** The document contains abstracts of seven externally-led wildfire technology projects funded under NASA's FIRET program. The following information is provided for completeness, but is not relevant to BST's portfolio.

---

## Funded Projects Overview

### 1. Jonathan Greenberg / University of Nevada, Reno
**Project:** Subcanopy UAS Development for Watershed-Scale Surface and Ladder Fuel Quantification (Step-2)  
**Award ID:** 23-2FIRET23-0090

**Technical Approach:**
- Development of autonomous drone fleet capable of flying through (rather than over) forest subcanopy
- Autonomous avoidance of trees and obstacles following pre-set flight patterns
- Equipped with LiDAR and multispectral sensor package
- Assessment of 3D subcanopy fuels, bulk characteristics (living vs. dead), and moisture content

**Objectives:**
1. Develop and test UAS system for subcanopy operation during active fuel treatments in topographically complex regions
2. Estimate surface and ladder fuel volumes, living/dead status, and size classes from collected data

**Demonstration Sites:**
- Nevada UAS Test Site
- UNR's Whittell Forest & Wildlife Area (undergoing fuel treatment during project timeline)

**Stakeholder Support:**
- CAL FIRE
- California Air Resources Board (CARB)

---

### 2. Jared Leidich / Urban Sky Theory Inc.
**Project:** Hot Spot: High-Resolution Real-Time Wildfire Detection, Mapping, and Communication Relay System with Persistent Broad-Area Coverage  
**Award ID:** 23-2FIRET23-0015

**Technical Approach:**
Stratospheric persistent platform combining two primary technical components:

**High-Resolution Imaging:**
- Coverage: ~3,000 acres per minute
- Resolution: 3.5m
- Persistence: Days to weeks airborne (hovering over active fire, moving between fires, or scouting high-risk areas)
- Capability: Real-time data transmission to ground personnel

**Communication Component:**
- Mesh-networked communication repeater and transmitter
- Ground firefighter connectivity in areas with sparse communication infrastructure
- Direct transmission of fire location shape files from imager to field personnel
- Real-time fire monitoring for firefighters tens of kilometers below the platform

**Operational History:**
- Over 6 flights conducted with early system versions
- Demonstrated imaging of Pass Wildfire in New Mexico
- Proven ability to map and relay real-time data

**Key Attributes:**
- Affordability and scalability for wide-scale deployment
- Paradigm shift enabling continuous monitoring of entire at-risk or on-fire areas

---

### 3. Mary Miller / Michigan Technological University
**Project:** Sediment Plumes and Blooms: Using Earth Observations and Modeling to Forecast Post-Fire impacts to Reservoir Water Quality and Quantity  
**Award ID:** 23-2FIRET23-0017

**Problem Statement:**
- 67 of 100 largest U.S. cities obtain drinking water solely from surface sources
- Post-fire impacts include: excess nitrogen, carbon, phosphorous; high sediment loads; increased stream temperatures; suspended ash
- Post-fire peak flows can reach 300 m³/s/km² (catastrophic floods)
- Example cost: Hermits Peak-Calf Canyon Fire water treatment plant replacement projected at $145M

**Technical Approach / Three Primary Objectives:**

1. **Risk Identification & Hydrological Modeling:**
   - Identify reservoirs and watersheds at risk by merging fire detections and burn scars
   - Leverage both process-based models (Water Erosion Prediction Project) and empirical models (curve number models used by Burned Area Emergency Response teams)
   - Integration with NASA Rapid Response Erosion Database
   - Development of ESRI toolbox (created with CAL FIRE) for rapid model input generation
   - Incorporation into online watershed database with easy verification tools

2. **Remote Sensing for Monitoring Recovery:**
   - Use NASA remote sensing tools for sediment plume mapping
   - Monitor vegetation recovery
   - Track post-fire influx of sediments, nutrients, and metals threatening water quality and quantity

3. **Harmful Algal Bloom (HAB) Detection:**
   - Adapt existing Great Lakes algal bloom detection algorithms to smaller watersheds
   - Provide reservoir managers with monitoring tools for sedimentation, water quality, and HAB protection

---

### 4. Hamidreza Nazaripouya / Oklahoma State University
**Project:** Near Real-Time Updated Wildfire Risk Map Model Informed by Powerline Fault Status  
**Award ID:** 23-2FIRET23-0018

**Problem Statement:**
Electrical infrastructure failures regularly ranked among top causes of wildfires; effective risk assessment requires systematic understanding of electrical wildfire triggers.

**Technical Approach / Three Primary Objectives:**

1. **Improved Wildland Fire Potential Mapping:**
   - Enhance fuel models using fine spatial and temporal resolution multispectral data from PlanetScope CubeSats
   - Develop novel AI-based fire danger indices incorporating spatial fuel type information and high-resolution fuel properties (vegetation biomass, greenness)

2. **Electrical Fault Ignition Probability:**
   - Combine experimental fire ignition tests with power-hardware-in-the-loop grid simulation
   - Understand ignition dynamics and propagation patterns under different environmental conditions
   - Generate unique dataset for machine learning-based ignition probability determination

3. **Operational Field Demonstration:**
   - Advance wildfire risk mapping through field demonstration with utility companies and forest services
   - Contribute to FireSense field campaign

**Stakeholder Involvement:**
- Fire departments
- State forestry services
- Electric utilities
- Insurance companies
- Additional collaborators: other electric utilities, fire departments, state and federal fire management agencies

---

### 5. Elahe Soltanaghai / University of Illinois, Urbana-Champaign
**Project:** UAS-Mounted Canopy Penetrating Radar-Tag System for Understory Fuel Sensing  
**Award ID:** 23-2FIRET23-0087

**Problem Statement:**
Remote sensing approaches offer limited vertical resolution for understory fuels obscured by canopy, resulting in errors >100% in predicting fire perimeter and burned areas.

**Technical Approach:**
- **Passive RF Tags:** Designed to pair with radar systems for higher sensing resolution
- **Deployment:** Distributed sparsely (every 50-200 meters) in areas of interest (e.g., Wildland Urban Interfaces)
- **No infrastructure required:** Tags require no power or communication infrastructure
- **Operation:** Remotely interrogated from UAS-mounted radar; RF channels characterize understory fuels
- **Function:** RF tags act as ground references (conceptually similar to NISAR calibration corner reflectors) enabling separation of understory and canopy signal echoes

**Research Components:**
1. Commoditize tag-radar prototypes for reliable field testing
2. Develop physics-informed models for RF signature generalization across different fuel types and forestry sites
3. Leverage vegetative dielectric and moisture content alterations in RF signatures (frequency and time domain) learned via physics-guided synthesizer
4. Integrate sparse accurate sensing data with landscape-scale orbital data (UAVSAR, NISAR) for wall-to-wall fuel maps using label propagation techniques

**Field Validation:**
- Partnership with three stakeholders leading prescribed burn activities and serving as burn bosses
- System demonstration during prescribed burns and field experiments
- Impact assessment of large-scale high-resolution fuel characterization

**Key Innovation:**
First technique with such high spatial measurement capability for fuel moisture; provides new data type complementary to orbital SAR and augments NASA data products with ground truthing.

---

### 6. Christopher Stellman / Logos Technologies LLC
**Project:** WAMI for Support of Wildland Fire Science, Management, and Disaster Mitigation  
**Award ID:** 23-2FIRET23-0065

**System:** BlackKite - Low-SWaP Infrared Wide Area Motion Imagery (WAMI) system

**Technical Specifications:**
- **Modality:** Mid-Wave Infrared (MWIR) low-rate, high-pixel-count video over large areas
- **Sensor Package:** Includes processing, storage, communications in compact, lightweight package
- **Control:** Digital data link for in-flight control; real-time imagery via cell or ad hoc networks
- **Data Capacity:** Up to 6 hours continuous collection; full data download capability post-flight
- **Weight:** <40 lb
- **Integration:** NATO 14" Munitions Rack lugs or DT-1-11 Dovetail mounting

**Performance Characteristics:**
- **Ground Sample Distance (GSD):** 0.25-1 m
- **Collection Rate:** Hundreds of km²/hour
- **Revisit Rate:** 1 Hz while maintaining >10 km² coverage
- **Geolocation Accuracy:** <5m Global Location Error (GLE) in orbiting mode
- **Sensitivity:** Mid-wave infrared sensitive to small hot-spots
- **Remote Operation:** MPU-5 Wave Relay radio

**Operational Capabilities:**
- Persistent orbiting and mapping missions
- Real-time and DVR (digital video recording) modes
- Asynchronous operations; flexible data access via phone or ad hoc networks
- Multi-user access to present and historical imagery

**Project Scope:**
1. **Data Acquisition:** 100+ hours covering hot phases of firefighting campaigns with direct operational support
2. **Software Development:** Adapt ESRI ARC-GIS-based tools for USFS needs; develop high dynamic range mode
3. **Benefit Quantification:** Assess value of high dynamic range imaging and temporal/spatial resolution in fire detection, tracking, and prediction
4. **Machine Learning:** Apply ML techniques to support tactical firefighting predictions

---

### 7. Kiley Yeakel / Massachusetts Institute of Technology/Lincoln Laboratory
**Project:** Fuel-Driven Wildfire Risk Mapping Over CONUS to Guide Targeted Resources Allocation  
**Award ID:** 23-2FIRET23-0074

**Problem Statement:**
Dynamic factors (precipitation, fuel accumulation, live fuel moisture content) determine fire risk on differing timescales; operational systems rely on in-situ sampling or CONUS-scale maps updated at nominal 5-year cadence, missing broad-scale and high temporal resolution needed for surveillance.

**Technical Approach - Three ML Algorithms:**

1. **Fuel Category Classification:**
   - Ingests monthly accumulated Sentinel-1A C-band SAR and USGS Landsat multispectral imagery
   - Outputs: Grasses, mixed forests, etc.

2. **Canopy Structure Estimation:**
   - Post-processes ICESat-2 measurements for higher spatial-resolution canopy height (CH) and fractional canopy coverage (CC)
   - ML algorithm trained on monthly Sentinel-1A (C-band), NISAR (L-band) SAR, and Landsat imagery
   - Per-pixel CC and CH estimation

3. **Live Fuel Moisture Content (LFMC):**
   - Time series analysis over 90-day periods
   - Data sources: Sentinel-1A, NISAR, Landsat, VIIRS, S