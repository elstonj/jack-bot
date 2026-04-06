# Solfatara Field Campaign Report: Multi-Instrument Volcanic Emissions Measurement

## Document Metadata
- **Type:** Field campaign report with technical methodology
- **Client/Agency:** NASA (supporting ASTER remote sensing calibration and validation project)
- **Program/Solicitation:** NASA ROSES project "ASTER remote sensing calibration and validation using In situ UAS based measurements of volcanic plume emissions"
- **Date:** October 30-31, 2014 (campaign); document prepared January 2016
- **Location:** Solfatara of Pozzuoli, near Naples, Italy
- **Key Personnel:** 
  - Dr. David Pieri (JPL, NASA - PI)
  - Dr. Jorge Andres Diaz (University of Costa Rica - Co-I)
  - Dr. Maria Fabrizia Buongiorno (INGV - collaborator)
  - Multiple INGV staff from Rome and Naples centers
- **Related Systems/Partners:** University of Costa Rica GasLab, JPL, INGV (Italian National Institute of Geophysics and Volcanology)

## Executive Summary
This report documents a field campaign at Solfatara volcano testing miniaturized unmanned aerial systems (UAS) and ground-based instruments for measuring volcanic emissions (CO₂, H₂S, SO₂) and surface temperatures. The campaign successfully demonstrated the feasibility of mounting lightweight sensor payloads on small quadcopters to safely acquire data in high-hazard volcanic environments, while collecting calibration and validation data for satellite remote sensing (Landsat 8, ASTER).

## Technical Approach

### Primary Objectives
1. Test miniaturized instruments developed for NASA's ASTER calibration/validation project
2. Verify feasibility of attaching light payloads to small quadcopters for safe volcanic gas measurement
3. Provide in situ calibration and validation support for remote sensing observations
4. Collect multi-scale measurements (airborne, ground-based) for volcanic plume characterization

### Measurement Strategy
Multi-platform, multi-scale approach:
- **Airborne:** UAS with miniaturized sensor payloads
- **Ground-based:** Portable instruments and fixed stations
- **Remote sensing:** Satellite data (Landsat 8, ASTER)
- **Instruments inter-compared** for validation

## Products & Capabilities Described

### 1. **MiniGas Dα Payload**
- **What it is:** Low-cost (500 g) experimental multisensor platform based on Arduino architecture
- **Developer:** Dr. Jorge Andres Diaz (University of Costa Rica)
- **Sensors included:**
  - Temperature sensor
  - Pressure sensor
  - Relative humidity sensor
  - SO₂ electrochemical sensor
  - H₂S electrochemical sensor
  - Non-dispersing near-infrared CO₂ sensor
  - GPS sensor
  - Onboard data storage
  - Xbee Pro telemetry system (wireless transmission)
- **Operational modes:**
  - 2D ground-based: Hand-portable case for fumarolic emissions
  - 3D airborne: Mounted on DJI Phantom Vision 2 quadcopter for aerial mapping
- **Sample flow:** 1.2 lpm displacement pump for airstream injection
- **Output:** Real-time 3D gas concentration plots, telemetry transmission to ground computer
- **Prior testing:** Flight-tested on VECTOR WING 100 UAV at Turrialba volcano (Costa Rica); tethered balloon platforms

### 2. **UAV-MS-XPR3 Mass Spectrometer System**
- **What it is:** Portable quadrupole-based process gas analysis mass spectrometer for volcanic gas species analysis
- **Base instrument:** Transpector XPR3 (newest generation high-pressure quadrupole MS)
- **Vacuum range:** mTorr (10⁻³ Torr) capable; ion source and quadrupole operate UHV to 20 mTorr; electron multiplier to 10 mTorr
- **Physical specs:** 14.3 × 12.4 × 17.5 cm; ~1 kg weight
- **Pump system:** Paired with small turbo pump (e.g., Pfeiffer Vacuum TPD 11 or Creare LLC MDP)
- **Control/data:** INFICON FabGuard Suite software on single-board computer (Fit PC3)
- **Sample flow:** 4 lpm diaphragm pump; introduced via 2 critical orifices; water vapor bypass option for high-moisture samples
- **Capabilities:** Multiple gas species detection, MS data and MiniGas data acquisition/storage/transmission
- **Smallest miniature commercial MS** suited to volcanic gas analysis

### 3. **DJI Phantom Vision 2 Quadcopter (Airframe)**
- **Camera:** Integrated high-quality still/video system
- **Video:** Full HD at 1080p 30/60i
- **Still photos:** 14 megapixel
- **Storage:** 4GB micro SD card
- **Navigation/Stability:** Integrated GPS auto-pilot with position holding, altitude lock, stable hovering
- **Battery:** 25 minutes flight time (longer than competitors' 10-15 minutes)
- **Operational range:** Acceptable for intended use
- **Ready to fly:** Within minutes
- **Payload:** Capable of carrying MiniGas Dα (~500 g)

### 4. **Thermal Imaging Systems**

**FLIR SC640** (TTM, INGV-OV)
- Resolution: 640 × 480 pixels
- Thermal sensitivity: 0.06°C at +30°C
- Accuracy: ±2°C (or ±2% of reading)
- K-type thermocouple integration: Fluke 52 II thermometer, range -200°C to 1260°C (±0.1°C accuracy)
- Measurement distance: Close-range (few meters), small acquisition distances minimize atmospheric attenuation

**Thermotecnix VISIR640** (optical lab UF-8, INGV-CNT)
- Resolution: 640 × 480 pixels
- Spectral range: 7.5 to 13 µm
- Accuracy: ±2°C (or ±2% of reading)
- Thermal sensitivity: 60 mK

**Fixed thermal camera stations (monitoring)**
- FLIR SC325 (320 × 240 pixels) - SF1 station: frames SE inner slope at ~300 m distance, captures Bocca Grande/Bocca Nuova intersection
- FLIR SC645 (640 × 480 pixels) - SF2 station: frames northern sector inner slope; operative since June 2013
- Purpose: Real-time continuous monitoring of fumarole field surface temperatures

### 5. **Spectroradiometer - ASD FieldSpec Pro**
- **Type:** Portable spectrometer with optical fiber
- **Spectral range:** 250-2500 nm
- **Spectral resolution:** Up to 3 nm
- **Calibration:** Internal calibration system; performed at each measuring cycle or with environmental condition changes
- **Measurement modes:** Radiance or reflectance capture
- **Data management:** Laptop-controlled acquisition procedures
- **Output:** Power measurements for radiance/reflectance analysis
- **Use case:** Verify portable spectro-radiometer capability to detect different gases in degassing fumaroles

### 6. **Ground-Based Gas Measurement Equipment**
- **Soil CO₂ flux:** Accumulation chamber method with LICOR Li-820 IR spectrometer (0-20,000 ppm range), diaphragm pump (~1 L/min), thermocouple
- **Air CO₂ concentration:** LICOR Li-800 IR spectrometer (0-5,000 ppm) with ~1 L/min pump
- **H₂S concentration:** Portable multigas XAM 7000 (Draeger, electrochemical sensor, 0-1000 ppm full scale)
- **Soil temperature:** K-type thermocouple at 10 cm depth

## Use Cases & Applications

### Solfatara Volcano Context
- **Location:** Pozzuoli, near Naples, Italy; part of Campi Flegrei volcanic complex
- **Characteristics:** Extensive fumarolic field; steam and high-sulfur gas emissions
- **Hazard:** Densely populated area; last explosive activity 1538 (Monte Nuovo); recent bradyseism episodes (1969-1972, 1982-1984 with evacuations of ~40,000 people)
- **Study sites:** Bocca Grande and Bocca Nuova fumaroles (main thermal sources)

### Primary Applications
1. **Safe volcanic hazard monitoring:** In situ measurements without exposing personnel to dangerous gas concentrations
2. **Satellite data calibration/validation:** Ground-truth data for Landsat 8 and ASTER thermal/spectral retrievals
3. **Transport model validation:** Understanding chemical/physical properties of emissions
4. **Multi-scale plume characterization:** 3D concentration mapping from airborne + ground measurements
5. **Species detection verification:** Validating retrieval algorithms for CO₂, H₂S, SO₂ from remote sensing

### Key Demonstrated Capability
**UAS-based safe access to high-emission zones:** Quadcopter successfully flew into active fumarole plumes with MiniGas payload, generating real-time 3D concentration maps without personnel exposure to toxic gas levels.

## Key Results

### Gas Measurement Results (October 30-31, 2014)

**MiniGas Quadcopter Measurements - Bocca Grande/Bocca Nuova Area:**
- **3D H₂S concentration mapping:** Successfully acquired vertical concentration profiles showing plume structure
- **3D CO₂ concentration mapping:** Generated Google Earth-compatible 3D visualizations with altitude-dependent concentration trends
- **Correlations demonstrated:**
  - Strong correlation between water vapor and volcanic gas concentrations (H₂S, CO₂)
  - Excellent H₂S vs CO₂ correlation confirming plume penetration capability
- **Data types:** Concentration vs. time, altitude, relative humidity, pressure

**UAV-MS-XPR3 Mass Spectrometer (Bocca Nuova & Bocca Grande Fumaroles):**
- **Main gases:** H₂O and CO₂ (major constituents)
- **Trace gases:** H₂S and SO₂ (10-100 ppmv range)
- **CO₂ concentration:** Tens of percent levels
- **SO₂ concentration:** Very low (10× smaller than H₂S); 10-100 ppmv
- **Key finding:** SO₂ concentration higher when condenser removed, indicating condenser partially removes SO₂ during collection
- **Detection note:** Successfully detected all target species including SO₂ at low ppm levels

**In Situ Ground Measurements (20 sampling points):**
- **Soil CO₂ flux range:** 25.8 to 42,853.6 g/m²/day (extreme variation reflecting proximity to fumaroles)
- **Air CO₂ concentration:** 338-3,175 ppm (background ~410 ppm; measurements 30 Oct - 31 Oct 2014)
- **Standard deviation range:** 39-1,621 ppm
- **Soil temperature at 10 cm depth:** 33.3°C to 94°C (influenced by fumarole proximity)
- **H₂S in air:** 7-17 ppm at selected measurement points

### Thermal Imaging Results

**Hand-held thermal camera comparison:**
- Successfully inter-calibrated FLIR SC640 and Thermotecnix VISIR640 for simultaneous measurements
- Demonstrated effects of acquisition distance and view angle on measured temperatures
- **Bocca Nuova measurements (Oct 30, 10:50 local time):**
  - K-type thermocouple: 144.7°C
  - FLIR SC640 & VISIR640: Comparable results post-correction
- **Atmospheric corrections applied:** Temperature and humidity compensations
- Day/night comparison: No substantial differences, validated by small measurement distances and high target temperatures minimizing atmospheric effects

**Fixed thermal camera monitoring (SF1 station, Oct 30, 10:30-11:30 local time):**
- Continuous acquisition of Bocca Grande area fumarole field
- Demonstrated long-term monitoring