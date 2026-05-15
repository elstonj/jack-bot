# NASA AERO.7 Phase I Technical Proposal: Persistent Wildfire Monitoring and Airspace Safety

## Document Metadata
- **Type:** NASA SBIR Phase I Technical Proposal (Draft)
- **Client/Agency:** NASA (Aeronautics Research Mission Directorate)
- **Program/Solicitation:** NASA SBIR FY26-27, Subtopic AERO.7.S36B (Airspace Operations and Safety)
- **Date:** May 5-14, 2026 (Draft)
- **BST Products/Systems Referenced:** Black Swift S3 fixed-wing UAS, NightFOX payload (NOAA-developed), SwiftCore autopilot
- **Key Personnel:** 
  - Elston (Principal Investigator, 60 est. hours)
  - Stachura (Chief Technology Officer, 60 est. hours)
  - [Unnamed] Pilot (60 est. hours)
  - Beck Cotter (Last editor)

---

## Executive Summary

Black Swift Technologies proposes to demonstrate persistent infrared monitoring of wildfires using autonomous handover procedures with the S3 fixed-wing UAS equipped with the NOAA NightFOX multispectral payload, achieving continuous coverage without surveillance gaps. The project integrates an airborne airspace protection system that detects unauthorized aircraft via Remote ID and Software-Defined Radio (SDR), directly feeding threat data to the Wildland Fire Team Awareness Kit (WFTAK) to protect manned firefighting operations. This Phase I effort validates core capabilities toward a scalable 24-hour persistent wildfire monitoring system for the US Forest Service and incident command resources.

---

## Technical Approach

### Core Innovation: Autonomous On-Station Handover
- **Two S3 aircraft in rotation** to ensure zero gaps in surveillance during extended operations
- Sequential deployment: second S3 launches before first aircraft is recovered
- **Target duration:** 10-12 hour simulation in Phase I, scaling toward 24-hour capability
- FAA-compliant lighting and safety systems for nighttime operations

### Sensor Integration
- **NightFOX Wildfire Detection Payload** (NOAA-developed) mounted on S3
- Multispectral imaging: visible, shortwave infrared (SWIR), midwave infrared (MWIR), thermal infrared (TIR)
- **Resolution:** ~25-meter pixel ground sampling (vastly superior to satellite data)
- Provides real-time fire perimeter, spread, and intensity products

### Airspace Protection System
- **ADS-B signal reception** for cooperative aircraft tracking
- **Long-Range Remote ID detection** for tracking non-cooperative drones
- **Software-Defined Radio (SDR) signal interception** for further characterization
- Automated threat detection and tracking
- Direct integration with WFTAK ground interface for situational awareness
- Protects manned firefighting air assets from hazardous UAS encounters

---

## Products & Capabilities Described

### Black Swift S3 Fixed-Wing UAS
- **What it is:** Small, fixed-wing unmanned aircraft platform originally developed for volcanic monitoring under prior NASA SBIR
- **Heritage:** Operationally deployed by USGS for volcano monitoring; proven in extreme environments
- **Use in this project:** Primary platform for persistent wildfire surveillance; equipped with NightFOX payload and airspace awareness systems
- **Environmental capability:** Enhanced autopilot (via NASA CCRPP funding) for high-wind performance; demonstrated resilience in extreme conditions including hurricanes (20+ hours collected across four storms; world-record gust measurement in Hurricane Milton)
- **Night operations:** FAA-compliant lighting and safety systems for nighttime flight

### NOAA NightFOX Wildfire Detection Payload
- **What it is:** NOAA-developed multispectral sensor package for detailed fire characterization
- **Specifications:**
  - Collects visible, SWIR, MWIR, and TIR imagery
  - ~25-meter pixel resolution (ground sampling distance)
  - Provides geo-rectified imagery and multispectral data
  - Calibrated for fire radiative power and thermal measurements
- **Historical use:** Previously flown on NOAA Twin Otter over wildfires; proven operational system
- **Use in this project:** Integrated on S3 for persistent fire monitoring; data streamed for near-real-time display and ground-truth validation

### Airspace Awareness Integration
- **What it is:** UAS-based detection and tracking system for cooperative and non-cooperative aircraft
- **Components:**
  - ADS-B receiver for standard cooperative aircraft
  - Long-Range Remote ID decoder
  - Software-Defined Radio (SDR) front-end for broadband signal interception
  - WFTAK interface module for incident command integration
- **Use in this project:** Demonstrated on S3 platform; provides proactive safety layer for coordinated wildfire operations

---

## Use Cases & Applications

### Primary Application: Wildland Fire Operations
- **Persistent overwatch** of active wildfire perimeters
- **Real-time intelligence** for incident command decision-making
- **Tactical support** for manned firefighting air assets (tankers, helicopters)
- **24-hour capability** enabling night operations when large fires persist
- **Data fusion** with fire-weather models (WRF-SFIRE) for extended forecasting

### Specific Test Scenario
- **Sunny Slope Sod Farm, Longmont, CO:** Controlled test environment for demonstrations
- **Simulated fireline monitoring:** Pre-determined transects and orbits to emulate operational fire mapping

### Operational Integration
- Seamless coordination with established air attack channels
- Data dissemination through NASA DAACs and WFTAK
- Support for US Forest Service (USFS) incident management workflows
- Enables routine UAS integration into firefighting airspace

---

## Technical Objectives

1. **Validate Persistent IR Monitoring**
   - Demonstrate NightFOX payload integration and performance on S3
   - Confirm multispectral data collection (visible, SWIR, MWIR, TIR)
   - Validate fire position, spread, and intensity characterization accuracy

2. **Establish Continuous Coverage Protocol**
   - Develop and test autonomous "on-station handover" procedure
   - Validate zero-gap surveillance across sequential aircraft
   - Demonstrate 10-12 hour simulation toward 24-hour capability

3. **Demonstrate Proactive Airspace Safety**
   - Prove S3 capability for ADS-B, Remote ID, and SDR signal reception
   - Validate threat detection and tracking performance
   - Confirm WFTAK integration for incident command situational awareness

4. **Evaluate Operational Utility**
   - Conduct flight demonstration over simulated wildfire scenario
   - Collect calibrated multispectral fire data
   - Stream near-real-time products to ground operators
   - Assess decision-support value for fireline commanders

---

## Work Plan

### Phase 1: System Preparation and Integration
- Equip two S3 UAS with NightFOX payloads
- Install FAA-compliant lighting and safety systems for night flight
- Integrate airspace awareness sensors (ADS-B, Remote ID, SDR receivers)
- Perform pre-mission checks and sensor calibration at BST facilities (Boulder, CO)

### Phase 2: Ground Setup and Calibration
- Deploy calibration target at Sunny Slope test site
- Validate sensor accuracy and performance under simulated conditions
- Establish ground truth data baseline for IR measurements

### Phase 3: Flight Planning and Approval
- Develop detailed flight plan with pre-determined transects and orbits
- Obtain FAA Certificate of Authorization (COA) or Part 107 Waiver
- Establish safety protocols for nighttime operations

### Phase 4: Persistent Operations Demonstration
- Conduct multi-day flight demonstration using two S3 aircraft in rotation
- Validate autonomous handover procedure (launch second aircraft before first recovery)
- Operate in shifts to maintain continuous coverage
- Adhere to all night-flying safety protocols

### Phase 5: Data Collection and Analysis
- Collect geo-rectified IR imagery and multispectral data
- Record system telemetry and uptime metrics
- Process data to evaluate sensor performance
- Assess operational capability for tactical decision support

### Phase 6: Reporting and Recommendations
- Produce comprehensive demonstration report
- Document lessons learned from handover procedures
- Provide recommendations for scaling to 24-hour operations
- Outline refined Concept of Operations (CONOPS)

---

## Related R&D and Heritage

### Prior BST Development (Foundation for This Project)
- **S3 Platform Origin:** Initial development under prior NASA SBIR for volcanic monitoring; now operationally deployed by USGS
- **Autopilot Refinement:** Enhanced S3 autopilot performance in high-wind environments funded through NASA CCRPP Program; applicable to wildfire and volcanic summit conditions
- **Payload Integration Experience:** Successful integration and testing of NightFOX on S3 platform
- **Extreme Environment Operations:** 20+ hours of air-deployed UAS data collection across four hurricanes; world-record gust measurement in Hurricane Milton; validates platform resilience
- **Airspace Awareness Systems:** Previous S3 integration and testing of ADS-B, Long-Range Remote ID, and RF signal interception systems

### Government Partnerships
- **NOAA:** Provided NightFOX payload and technical expertise; payload previously demonstrated on Twin Otter over actual wildfires
- **US Forest Service (USFS):** Key operational partner ensuring outputs are relevant for wildfire management and integration pathways
- **USGS:** Operationally flies S3 for volcanic monitoring

---

## Facilities and Equipment

### Facilities
- **Black Swift Technologies, Boulder, CO:** System setup, pre-mission checks, sensor calibration, post-mission data analysis
- **Sunny Slope Sod Farm, Longmont, CO:** Controlled test environment for extended daytime and nighttime UAS operations; minimal logistical constraints

### Equipment
- **Two Black Swift S3 fixed-wing UAS** (minimum requirement for rotational persistent operations)
- **NOAA NightFOX Wildfire Detection Payloads** (calibrated multispectral IR and visible sensors)
- **Ground Support Equipment:** Launchers, batteries, charging infrastructure, ground control stations, ancillary equipment for continuous operations

---

## Commercialization and Business Plan

### Target Market
- **Primary:** US Forest Service (USFS) and incident command resources for wildfire management
- **Secondary:** Other federal and state natural resource agencies; commercial firefighting contractors

### Value Proposition
- **Improvement over current methods:** Superior resolution (~25m pixels vs. satellite; continuous vs. 4-hour intervals), cost-effective vs. manned persistent operations, true 24-hour capability
- **Operational advantages:** 
  - Low-cost, modular S3 platform
  - Seamless aircraft handoff enabling sustained operations
  - Integrated airspace protection for safe mixed manned/unmanned operations
  - Real-time fire intelligence for tactical decision-making
  - Data integration with operational tools (WFTAK) and fire-weather models

### Commercialization Pathway
- **Phase I/II demonstrations** establish operational CONOPS and de-risk adoption
- **Coordination with established air attack channels** ensures safe integration
- **Data sharing through NASA DAACs** provides science community access
- **Scalability:** Streamlined process for collecting, sharing, and archiving fire data; repeatable procedures for deployment across multiple wildfire regions
- **Transition potential:** Demonstrated safe operations with USFS and partners enables Phase III or direct government/commercial adoption

---

## Key Personnel
- **Elston:** Principal Investigator (60 estimated hours)
- **Stachura:** Chief Technology Officer (60 estimated hours)
- **[Unnamed] Pilot:** Flight operations (60 estimated hours)
- **Supporting staff:** All technical work and flight operations conducted in-house; no subcontractors planned for Phase I

---

## Notable Details

### Alignment with NASA SBIR Topic AERO.7.S36B
The proposal directly addresses **"Nontraditional Aviation Operations for Wildfire Response"** critical gaps:
- ✓ Persistent wildfire monitoring and data dissemination
- ✓ Extended UTM for wildfire operations in disconnected environments
- ✓ Improved communication and situational awareness for emergency responders
- ✓ Common operating picture for coordinated incident management

### Unique Technical Innovation
**Autonomous on-station handover procedure** with zero-gap coverage is the core innovation—enables true persistent operations without ground crew burden of rapid turnaround or complex coordinated flight plans. Critical differentiator for operational feasibility.

### Safety Integration
The airspace protection system (ADS