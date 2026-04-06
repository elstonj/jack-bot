# Sensor Payload Overview – NightFOX Project

## Document Metadata
- Type: Technical overview / payload specification document
- Client/Agency: NOAA
- Program/Solicitation: FY17 UASPO (Unmanned Aircraft Systems Program Office); FIREX (Fire and Smoke Research)
- Project Name: NightFOX (Nighttime Fire Observations)
- Date: Created/Modified December 26, 2019
- BST Products/Systems Referenced: 5-hole probe (wind measurement)
- Key Personnel: Jack Elston (last editor), Troy Thornberry and Ru-Shan Gao (payload development leads)

## Executive Summary
NightFOX developed dual sensor payloads (in situ and remote sensing) for small UAS to measure wildfire emissions and characteristics. The in situ package measures CO2, CO, aerosols, and atmospheric conditions with 1-second response time at $10-15K cost. The remote sensing package uses multi-spectral detectors including mid-infrared sensors to map fire extent and measure fire radiative power (FRP) at $15-20K cost.

## Technical Approach

### In Situ Payload Development
- **Sensors included:** CO2, CO, fine-mode aerosols (140-3000 nm), coarse-mode aerosols (1-10 μm), relative humidity, temperature, pressure
- **Wind measurement:** BST 5-hole probe
- **Key requirement:** Achieve 1-second response time (vs. typical 10-60 second commercial sensors) to maintain ~0.5 km spatial resolution at 20 m/s cruise speed
- **Strategy:** Evaluate commercial/OEM CO and CO2 sensors; modify for response time; develop custom sensors where commercial options insufficient (e.g., fine-mode aerosol)
- **Fine-mode aerosol sensor:** Custom instrument previously developed (reference: Gao et al., 2016)
- **Environmental sensors:** InterMet RH/T/p sensors (iMet-XQ)
- **Cost target:** $10-15K per package (~10× cheaper than manned aircraft equivalents)

### Remote Sensing Payload Development
- **Spectral coverage:** Multiple detectors across visible, mid-infrared (MIR, ~4 μm), and long-wavelength infrared (LWIR, 7-14 μm)
- **Primary objectives:** Map fire perimeter and measure fire radiative power (FRP)
- **Technical challenge:** LWIR thermal imagers saturate at fire radiances; MIR imagers costly and bulky
- **Solution:** Single-element 4 μm sensors (small, low-cost) for FRP determination
- **Scanning approach:** Cross-track scanning with narrow field-of-view MIR sensor; visible/thermal cameras for high-resolution context
- **Data management:** Onboard computer for full data storage; real-time subset transmitted to ground for decision-making
- **Cost target:** $15-20K per package

## Products & Capabilities Described

### BST 5-Hole Probe
- **What it is:** Wind measurement probe
- **Application in NightFOX:** Integrated into in situ payload for wind velocity measurements on small UAS
- **Context:** Identified as suitable solution for UAS wind measurement requirements

### Payload Integration
- **Multi-sensor fusion:** Simultaneous in situ and remote sensing measurements from single platform
- **Real-time telemetry:** Subset of sensor data downlinked for operational fire monitoring
- **Data archival:** Full datasets submitted to FIREX data archive

## Use Cases & Applications

**Primary Application:** Nighttime and daytime wildfire characterization

**Specific measurements:**
- Fire combustion efficiency (via CO2/CO ratio analysis)
- Wildfire-produced aerosol characterization (health impact assessment)
- Fire extent mapping
- Fire radiative power distribution
- Ambient atmospheric conditions in fire plumes

**Mission context:** NOAA FIREX campaign; small fixed-wing UAS operations (cruise speed ~20 m/s)

## Development Timeline
- **Year 1:** Laboratory evaluation of candidate sensors and imagers; selection of optimal components
- **Year 2:** Prototype in situ and remote payload integration; custom sensor modifications; test flights on UAS
- **Year 3:** Finalization of both payloads; construction of two spare payloads

## Notable Details

- **SWaP optimization challenge:** Document emphasizes difficulty of reducing size, weight, power, and cost while maintaining research-grade sensor performance for UAS
- **Response time criticality:** Highlights synchronization problem when sensors have different response times; advocates for 1-second standard
- **Commercial sensor limitations:** Identifies insufficient sensitivity and cross-species interferences in industrial solid-state sensors; justifies custom development approach
- **Cost efficiency:** Target of $10-15K in situ package represents ~10× cost reduction vs. manned aircraft instruments without performance loss
- **Partnerships/References:** References InterMet Systems for environmental sensors; cites prior work (Gao et al., 2016) on fine-mode aerosol sensing
- **Sensor redundancy:** Two separate aerosol sensors targeting complementary particle size ranges for comprehensive aerosol characterization

---

**Note:** This document is an excerpt/overview. Full proposal content referenced but not included in this file.