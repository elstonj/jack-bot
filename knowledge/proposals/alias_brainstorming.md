# ALIAS Brainstorming

## Document Metadata
- Type: Internal brainstorming/concept development document
- Client/Agency: DARPA
- Program/Solicitation: FY25 ALIAS (Autonomous Logistics and Integrated Supply - implied from solicitation context)
- Date: 2025-09-16 (created), 2025-09-17 (modified)
- BST Products/Systems Referenced: S2, NightFOX, Multi-hole probe, soil moisture sensors, MATRIX autonomy system
- Key Personnel: Daniel Prendergast (last editor)

## Executive Summary
Internal brainstorming document exploring six potential technical approaches for the DARPA FY25 ALIAS solicitation, focusing on autonomous aircraft capabilities for emergency services and wildfire operations. Concepts range from external load stability control to wildfire prediction systems, with emphasis on integration with the MATRIX autonomy framework and interoperability with incident command systems.

## Technical Approach

### 1. Model Predictive Control for Stable External Loads
- **Problem Statement:** External loads (e.g., sling-loaded Humvee under SH-60 helicopter) frequently jettisoned during flight due to dynamic/aerodynamic instability
- **LM/Sikorsky Role:** Develop MPC model of pendulum external load coupled with SH-60 helicopter for in-flight load stability, accounting for real-time 3D winds
- **BST Role:** Provide standalone module with GPS, IMU, and multi-hole probe that wirelessly reports 3D winds at external load location to MATRIX autonomy system MPC component
- **Note:** Document indicates this may not align well with Emergency Services focus of solicitation

### 2. Automated Landing Site Selection and Vision-based Precision Landing
- **Automated Site Selection:** Extension of prior BST work using image segmentation; adds analysis for landing site slope, smoothness, obstacle identification, and dynamic landing point adjustment during final approach
- **Vision-based Precision Landing (Optional):** Computer vision-based landing to achieve <1 meter accuracy (vs. 1-5 meters from GPS alone); includes obstacle detection/avoidance
- **Integration Points:**
  - ICS/WFTAK (Incident Command System/Wildland Fire Tactical Awareness Kit): Send locations and images of potential landing sites
  - MATRIX: Perform automated landing site selection and vision-based precision landing via MATRIX SDK

### 3. Soil Moisture Sensor Integration on SH-60
- **Fuel Assessment:** Mount soil moisture sensors on SH-60 for assessment of wildfire fuel conditions
- **Landing Zone Assessment:** Same sensors used during short final approach to assess suitability of landing zone

### 4. Multiple S2 with NightFOX Integration
- **System Configuration:** Networked S2 aircraft integrated with NightFOX sensor suite
- **Mission:** Continuous wildfire hotspot monitoring
- **Integration:** Via MATRIX autonomy framework
- **Open Question:** Document notes unclear whether MATRIX handles single-aircraft autonomy only or also multi-UAS tasking/allocation (MUM-T aspect mentioned in solicitation)

### 5. Wildfire Prediction System
- **Data Fusion Approach:**
  - **Inputs:**
    - Fuel Map (GIS database of fuel types and amounts)
    - NightFOX (hotspot and fireline mapping)
    - ASOMMS (fuel moisture levels)
    - DEM (topography)
  - **Processing:** Grid-based calculation (latitude/longitude) to determine rate of spread, intensity, heat
- **Integration Points:**
  - ICS/WFTAK: Send data over ICS network
  - MATRIX: Send cues to Fire Attack Assets via MATRIX SDK

## Products & Capabilities Described

**S2 (fixed-wing UAS)**
- Proposed for continuous wildfire hotspot monitoring when equipped with NightFOX
- Networked multi-aircraft operations capability under consideration

**NightFOX (sensor suite)**
- Provides mapping of hotspots and fireline
- Integrated with S2 for continuous monitoring
- Data fed into wildfire prediction system

**Multi-hole Probe**
- Provides 3D wind measurement at external load location
- Wireless reporting capability to autonomy system
- Application: External load stability control

**Soil Moisture Sensors**
- Dual application: wildfire fuel assessment and landing zone assessment
- Proposed integration on SH-60 helicopter platform

**MATRIX Autonomy System**
- SDK-based integration capability
- Proposed for: automated landing site selection, vision-based precision landing, multi-S2 hotspot monitoring, wildfire prediction cueing
- **Unclear:** Whether it supports single-aircraft autonomy only or multi-UAS tasking/allocation

## Use Cases & Applications

1. **Emergency Services / Wildland Firefighting Support**
   - Automated supply delivery to firefighters
   - Precision landing in constrained areas
   - Real-time fuel and landing zone assessment

2. **Wildfire Monitoring and Prediction**
   - Continuous hotspot tracking
   - Rate-of-spread prediction
   - Fire intensity/heat mapping
   - Fireline visualization

3. **External Load Operations**
   - Stable sling-load transport under helicopters
   - Prevention of load jettisoning due to instability

4. **Incident Command Integration**
   - Real-time situational data transmission to ICS/WFTAK network
   - Automated asset cueing to fire attack resources

## Notable Details

- **Integration Focus:** Document emphasizes multi-system integration (MATRIX autonomy, ICS/WFTAK, sensor fusion) rather than single-point capabilities
- **Phased Approach:** Some concepts marked optional (vision-based precision landing), suggesting tiered development strategy
- **Partnership:** Lockheed Martin/Sikorsky involved in Model Predictive Control work; unclear if they are prime contractor or partner on ALIAS
- **Solicitation Alignment Questions:** Document notes concern about MPC external load work fitting Emergency Services focus and uncertainty about MATRIX capabilities scope (single vs. multi-aircraft autonomy)
- **Technical Maturity:** Automated landing site selection described as "extension of previous work," suggesting some prior capability baseline exists
- **Sensor Fusion Complexity:** Wildfire prediction concept combines 4 data sources (fuel map, NightFOX, ASOMMS, DEM) with grid-based modeling for operational decision support