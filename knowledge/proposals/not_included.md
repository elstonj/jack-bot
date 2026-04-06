# NASA 2012 SBIR Phase II Final Report: Soil Moisture Monitoring via LDCR

## Document Metadata
- **Type:** Final Report (NASA SBIR Phase II)
- **Client/Agency:** NASA
- **Program/Solicitation:** 2012 SBIR - Soil Moisture monitoring topic
- **Date:** ~2016 (last modified April 10, 2016)
- **BST Products/Systems Referenced:** 
  - Tempest UAS (unmanned aerial system)
  - LDCR (Lobe Differencing Correlation Radiometer)
  - MiCo antenna array (Microstrip Colinear)
- **Key Personnel:** 
  - Maciej Stachura (Black Swift Technologies LLC)
  - A.J. Gasiewski (University of Colorado - technical lead)
  - Eryan Dai (University of Colorado)

## Executive Summary

This Phase II report documents development of the Lobe Differencing Correlation Radiometer (LDCR) integrated on BST's Tempest UAS for high-resolution soil moisture mapping. The work covers radiometric calibration methodology, design and optimization of a 2x2 microstrip colinear antenna array operating at L-band (1.4135 GHz), and development of a high-speed data acquisition system capable of logging 60 MS/s at 14-bit resolution with 210 MB/s write speed to solid-state storage.

## Technical Approach

### Radiometric Calibration (Section 5.5 / Section 3)

**LDCR Brightness Temperature Mapping:**
- Developed calibration algorithm to map antenna temperature (TA) to brightness temperature (TB) using Kriging method
- LDCR provides four calibration states with voltage outputs V0-V3 and differential temperature inputs ΔT0-ΔT3
- Reference termination temperatures (Tref1, Tref2) set by thermoelectric cooler/heaters, measured by thermistors
- Calibration performed over known reference regions: still fresh water (nadir) and clear sky (zenith)

**Key Calibration Parameters:**
- Antenna radiation efficiency (η): 95.58% (from HFSS simulations, ±1% accuracy)
- Brightness temperatures for fresh water at nadir (23°C):
  - Horizontal polarization (TBH_water): 64.4 K
  - Vertical polarization (TBV_water): 132.2 K
- Atmospheric downwelling brightness temperatures assumed at 2.73 K (both polarizations)

**Calibration Method:**
- Parameterized V0 and gains G0-G3 as second-order polynomial functions of LDCR receiver temperature
- Used simulated annealing method to estimate unknown parameters (N=1180 calibration cycles, M=6 parameters, 1174 degrees of freedom)
- χ² metric used to assess fit quality; measured χ² values indicated good fit to measured voltages

**Data Collocation:**
- Radiometric sampling interval: ~1 ms
- Navigation data interval: ~22 ms
- Linear interpolation of navigation data to radiometric time grid required for pixel collocation

### MiCo Antenna Array Design (Section 7.2)

**2x1 Antenna Subarray Architecture:**
- Two radiating elements with half-wavelength separation (106 mm centerline-to-centerline)
- Each element: 5-segment microstrip colinear patch antenna
- 0° 3-dB coupler connecting two 100Ω microstrip feed lines
- Fabricated on Rogers 4003C duroid (εr=3.55, thickness=1.534 mm) in three sections for Tempest fuselage integration
- Operating center frequency: 1.4135 GHz
- Omnidirectional radiation pattern per element; null at horizon, broadside in vertical/horizontal directions
- Simulated horizontal radiation rejection: 20-47 dB

**Key Design Parameters (Table 1):**
- Section length: 59.12 mm
- Narrow line width: 1 mm; wide line width: 14 mm
- 100Ω feed line length: 54 mm
- Short matching line length: 4 mm, width: 0.3 mm

**2x2 Antenna Array Architecture:**
- Two 2x1 subarrays stacked with quarter-wavelength vertical separation (~53.5 mm nominal)
- Styrofoam blocks provide mechanical stability and frequency tuning
- ±90° drive phase shift between upper and lower subarray pairs
- Quarter-wavelength separation provides 90° phase shift for quadrature LDCR receiver channels

**Mutual Coupling Analysis:**
- Vertical separation distances tested: 53.5, 55.5, 57.5, 59.5, 61.5, 67.5 mm
- Optimum main-to-back lobe ratio: **55.5 mm** (2.5 mm larger than quarter wavelength)
  - Band-averaged main-to-back lobe ratio: 19.6 dB (Table 3)

**Frequency Tuning Methods:**
- Styrofoam proximity caused 20 MHz frequency pull-down
- Design modified to compensate (section lengths reduced from 59.12 mm to 57.94 mm; matching line length increased from 4 mm to 4.2 mm)
- Blue builder's foam for dielectric loading achieved 5 MHz frequency reduction
- Silicon RTV strips (εr=2.54) being developed for aerodynamic frequency tuning

**Measured vs. Simulated Performance:**
- 2x1 subarray: measured return loss 5 dB lower across 200 MHz band than HFSS; center frequency difference ~4 MHz
- Integrated 2x2 array: measured resonant frequency 9.5 MHz higher than simulation (attributed to board tolerances and HFSS mesh limitations)

### High-Rate Data Logger System (Section 5.2-5.4)

**Requirement Evolution:**
- Original Phase I: 180 MS/s at 16-bit (720 MB/s disk write, 2.6 TB per hour)
- Phase II revision: 60 MS/s at 14-bit (sampling at third Nyquist zone; 210 MB/s write, 756 GB per hour)

**Architecture:**
- **Signal Conditioning:** Analog/RF Board (designed to separate signal conditioning from high-rate logging)
  - Processes 2 LDCR analog channels
  - 8 thermistor inputs (5 LDCR, 2 antenna, 1 reference)
  - 50 Hz digital navigation data from autopilot (includes 2 NDVI/thermal measurements, laser altimeter elevation)
  - Adds gain and balun circuit to LDCR data
  - Performs analog correlation at 32 kS/s (averaged to 1 kS/s)

- **Data Digitization:** A/D Board
  - ADC: LTC2143-14 (14-bit, 80 MS/s dual converter)
  - Connects to Spartan-6 FPGA module (EFM-02)

- **FPGA Processing:** Spartan-6 EFM-02 FPGA Module
  - Routes data from ADC to USB 3.0 (625 MB/s capability)
  - Simplified design: FPGA moves data from ADC to USB channel only

- **Data Storage:** VIA EPIA-P910-10Q Pico ITX Board + SSD
  - Host for USB 3.0 interface
  - Writes to SSD2GO Pocket (tested write speed: 394 MB/s)
  - Enables quick SSD swaps between flights

**Data Output (three streams to SSD):**
1. Processed analog LDCR data (60 MS/s)
2. 50 Hz telemetry (autopilot + digitized thermistors)
3. Analog correlated data (1 kS/s)
- Written to single binary file with common timestamp; post-processing software separates streams

## Products & Capabilities Described

### LDCR (Lobe Differencing Correlation Radiometer)
- **What it is:** L-band passive microwave radiometer designed for soil moisture measurement from UAS platforms
- **Operating frequency:** 1.4135 GHz (SMAP frequency band: 1400-1427 MHz)
- **Key components:** 
  - MiCo 2x2 antenna array (nadir- and zenith-looking beams)
  - Quadrature receiver with 4 calibration states
  - Internal resistive loads with thermoelectric cooler/heaters
  - IR sensor for physical temperature measurement
  - Four thermistors monitoring receiver temperatures
- **Spatial resolution:** ~15 m from Tempest altitude (~15-50 m)
- **Coverage:** >0.6 km² in one hour of flight
- **Soil penetration:** ~5-10 cm under most conditions
- **Application context:** Validation of NASA SMAP mission; precision agriculture; boundary layer heat transport studies

### Tempest UAS
- **What it is:** Lightweight unmanned aerial system
- **Integration:** MiCo antenna array integrated into fuselage; LDCR electronics payload
- **Operational capability:** Sub-watershed (~km scale) coverage at high spatial resolution; low operator cost compared to manned aircraft

## Use Cases & Applications

1. **SMAP Validation:** Provide complementary ground-truth measurements for NASA's Soil Moisture Active/Passive mission (launched 2015)
2. **Precision Agriculture:** Soil moisture mapping at scales too fine for satellite missions
3. **Hydrological Studies:** Watershed-scale soil moisture assessment (0.6 km² per flight hour)
4. **Boundary Layer Studies:** Evapotranspiration and surface heat transport measurement
5. **Scaling Studies:** Sub-watershed coverage enabling research on scaling relationships between point and satellite measurements
6. **Diurnal Time Sampling:** Capture soil moisture at arbitrary times (not fixed crossing times like SMAP)

## Key Results

### Calibration Performance
- Successfully calibrated LDCR using pre-flight data over still fresh water
- χ² metric validation confirmed good fit to measured voltages across 1,180 calibration cycles
- Identified ~3 dB gain differences between calibration states due to RF losses in internal MiCo quadrature hybrid and coaxial cables
- Residual atmospheric radiation correction needed (~2-3 K)
- Elevation angle dependence of surface emission temperatures identified but not yet incorporated

### Antenna Array Performance
- **Return loss:** -18.5 dB or better across working band after tuning
- **Radiation pattern:** 20-47 dB rejection of horizontal radiation (horizon null achieved)
- **Mutual coupling:** Optimized vertical separation (55.5 mm) achieves 19.6 dB main-to-back lobe ratio
- **Frequency stability:** Successfully tuned to target frequency despite 20 MHz pull-down from styrofoam and proximity effects

### Data Logger Performance
- **Bandwidth achieved:** 210 MB/s write speed (designed requirement)
- **Storage:** 756 GB per 60-minute sortie
- **Simplification:** Single SSD instead of 36 microSD cards (original design) or 11 microSD cards (intermediate design)
- **System advantages:** Quick SSD swap capability; reduced complexity; lower power draw; lower risk profile

## Notable Details

### Design Challenges & Solutions
1. **LDCR receiver front-end losses:** Internal quadrature hybrid exhibited larger-than-acceptable losses; identified through gain intercomparison analysis
2. **Antenna frequency drift:** Styrofoam proximity caused 20 MHz downshift; compensated through design parameter modification
3. **Data logger simplification:** Shift to third Nyquist zone sampling reduced bandwidth requirements from 720 MB/s to 210 MB/s, enabling single-SSD architecture
4. **Calibration ill-conditioning:** Design matrix ill-conditioned due to slow temperature variation; addressed using simulated annealing (Tikhonov regularization not yet implemented)

### Technical Collaborations
- University of Colorado (ECEE Department) provided antenna and radiometer design expertise
- CU instrument design team (CET) specified reduced sampling requirements enabling simpler data logger
- References cite HFSS simulations and CU course materials (ECEN 5004, 5254)

### Remaining Work/Open Issues
1. Elevation angle dependence