# A Ruggedized Unmanned Aircraft and Sensor Package for Measurement of Hazardous Airborne Emissions from Wildfires on Forest Lands

## Document Metadata
- **Type**: USDA Phase I SBIR Application (Proposal)
- **Client/Agency**: USDA National Institute of Food and Agriculture (NIFA)
- **Program/Solicitation**: FY 2018 Small Business Innovation Research (SBIR); Topic 8.1 Forests and Related Resources; Subtopic 6: Developing Technology that Facilitates the Management of Wildfires on Forest Lands
- **Date**: 5 October 2017
- **BST Products/Systems Referenced**: Unmanned aircraft platform with ruggedized sensor package (specific model designation not clearly stated in notes)
- **Key Personnel**: Maciej Stachura (noted as last editor)

## Executive Summary
Black Swift Technologies proposed developing a ruggedized unmanned aircraft system equipped with a miniaturized multi-gas and particulate sensor payload to measure hazardous airborne emissions from wildfires on forest lands. The system would integrate multiple electrochemical gas sensors, photoionization detection, and optical particle counting to provide comprehensive characterization of wildfire smoke composition in real-time during active fire management operations.

## Technical Approach

**Aircraft Platform**: Ruggedized unmanned aircraft designed for hazardous wildfire conditions (specifications not detailed in notes)

**Sensor Payload Integration Strategy**:
- **CO₂ Measurement**: SenseAir K30FR sensor (response time 2s, range 0-5000 ppm, accuracy >30 ppm; literature indicates calibration can reduce error to 3-5 ppm) selected over standard K30
- **Multi-Gas Species**: Alphasense electrochemical sensors selected as primary platform for trace gas integration, with justification from successful volcano monitoring applications (Roberts et al., 2017)
- **Volatile Organic Compounds (VOCs)**: Alphasense PID (photoionization detector) sensor, miniaturized configuration
- **Particulates**: Alphasense OPC-N2 optical particle counter for PM₁, PM₂.₅, and PM₁₀ measurement
- **Additional Species**: H₂S, SO₂, CO, NO, NO₂, HCN, Cl₂, O₃, and other trace gases using Alphasense electrochemical sensor suite

**Sensor Selection Rationale**:
- Alphasense platform chosen over alternatives based on precedent in multi-gas volcano monitoring applications with published validation
- Response times: range from 2s (CO₂) to 50s (HCN) considered acceptable for airborne work, though acknowledged that standard Alphasense HCl response time (200s) deemed too slow for airborne applications
- Miniaturization emphasized to integrate comprehensive payload on aircraft platform

## Products & Capabilities Described

### Unmanned Aircraft System
- **Purpose**: Deliver sensor payload into wildfire smoke plumes for in-situ measurements
- **Attributes**: Ruggedized design for wildfire environment operations
- **Application**: Real-time hazardous emission characterization during active fire management

### Integrated Multi-Parameter Sensor Package
**Electrochemical Gas Sensors** (Alphasense primary manufacturer):
- CO₂: SenseAir K30FR (2s response, 0.5 L/min flow)
- SO₂/H₂S: SOH A2 (15/25s response, ranges 20/100 ppm)
- CO/H₂S: COH-A2 (25/30s response)
- NO: D4 (15s response, 0-100 ppm, ±1.5 ppm accuracy)
- NO₂: 35s response, 0-20 ppm range, ±0.6 ppm accuracy
- CO: CO-A4 (20s response, 0-500 ppm, ±1 ppm accuracy)
- Cl₂: CL2-D4 (35s response, 0-20 ppm, ±0.5 ppm accuracy)
- O₃: OX-A431 (45s response, 0-20 or 0-50 ppm)
- H₂, HCN: Additional species with dedicated sensors

**Photoionization Detector (PID)**:
- Alphasense AH2 (response time 3s, range ppb-ppm, weight 8g)
- Purpose: Detect volatile organic compounds

**Optical Particle Counter**:
- Alphasense OPC-N2 (PM₁/PM₂.₅/PM₁₀ measurement, weight <105g)
- Reference data: Validated in Alphasense OPC-N2 literature; comparison studies cited (Crilley et al., 2017; Sinan Sousan et al., 2016)

## Use Cases & Applications

**Primary Application**: Wildfire Management on Forest Lands
- Real-time measurement of hazardous emissions during active wildfires
- Support for firefighter safety assessment
- Quantification of smoke plume composition and dispersion
- Validation of smoke transport models
- Characterization of emissions for air quality impact assessment

**Specific Hazards Addressed**:
- Mercury emissions (research notes cite 44 tons/year from North American wildfires)
- Particulate matter (PM₂.₅, PM₁₀)
- Carbon monoxide, hydrogen sulfide, sulfur dioxide
- Volatile organic compounds and secondary organic aerosol precursors
- Brown carbon in upper troposphere

**Environmental/Health Context**:
- Wildfire smoke health impacts (Global mortality estimates cited: 335,000 deaths/year from landscape fire smoke, Johnston et al., 2012)
- Real-time data to inform evacuation and public health decisions during fire events

## Technical Specifications & Performance Claims

**Sensor Specifications Table** (from proposal):
| Species | Response Time (s) | Range (ppm) | Accuracy (ppm) | Weight | Manufacturer |
|---------|-------------------|-------------|----------------|--------|--------------|
| CO₂ | 2 | 0-5000 | >30 (3-5 post-cal) | — | SenseAir K30FR |
| SO₂/H₂S | 15/25 | 20/100 | 2/5 | — | Alphasense SOH A2 |
| NO | 15 | 0-100 | 1.5 | — | Alphasense D4 |
| CO | 20 | 0-500 | 1 | — | Alphasense CO-A4 |
| NO₂ | 35 | 0-20 | 0.6 | — | Alphasense |
| Cl₂ | 35 | 0-20 | 0.5 | — | Alphasense CL2-D4 |
| O₃ | 45 | 0-20 | — | — | Alphasense OX-A431 |
| HCN | 50 | 0-250 | — | — | Alphasense |
| PID | 3 | ppb-ppm | — | 8g | Alphasense AH2 |
| PM Counter | — | PM 1, 2.5, 10 | — | <105g | Alphasense OPC-N2 |

**Design Considerations**:
- Comprehensive payload integrating gas species, organics, and particulates
- Miniaturization emphasized for aircraft integration
- Response times range 2-50 seconds (suitable for airborne transect work)

## Notable Details

**Competitive Research Foundation**:
- Extensive literature review on wildfire emissions, health impacts, and measurement precedents
- Specific reference to Roberts et al. (2017) Multi-Gas volcano monitoring validation as proof-of-concept for Alphasense sensor suite in airborne applications
- Acknowledgment of prior airborne wildfire smoke measurement campaigns (Urbanski et al. on Rocky Mountain fires; Liu et al. 2017 on western U.S. wildfires)

**Sensor Development Precedents Cited**:
- Volcanic gas monitoring (Alphasense Multi-Gas at Mt. Etna, validated for H₂S/SO₂/HCl ratios)
- Airborne ash measurements (Eyjafjallajökull eruption, Weber et al. 2012; Mt. Sakurajima, Eliasson et al. 2014)
- These precedents suggest viability of miniaturized optical particle counters and electrochemical sensors in airborne hazardous environments

**USDA Program Alignment**:
- Directly addresses NIFA Strategic Goal 1 (Science), Sub-Goal 1.2 (climate adaptation for forest systems) and Sub-Goal 1.3 (sustainable resource management and environmental protection)
- Fits Subtopic 6 mandate: "systems for detecting and managing wildfires... tools and equipment for improving efficacy and safety of firefighters on the ground and in the air; and communication and navigation systems"

**Project Status**: 
- Document labeled as from "Completed/Inactive/Unsubmitted Projects" folder, suggesting this proposal was not funded or was later abandoned
- No results or outcomes documented in this notes file

**Document Character**:
This appears to be working notes/reference materials for the proposal rather than the full proposal document itself. It contains primarily the technical sensor specification table, literature references on wildfire emissions/health impacts, and research precedents, but lacks detailed description of the aircraft platform, project management plan, budget, or formal proposal sections.