# Phase II Proposal Strategy

## Document Metadata
- Type: Internal strategy document for Phase II SBIR proposal preparation
- Client/Agency: NASA
- Program/Solicitation: NASA SBIR 2012, Soil Moisture topic
- Date: 2014-06-06
- BST Products/Systems Referenced: S3 (SuperSwift), SP Pro (SwiftPilot Pro), Tempest, LDCR sensor
- Key Personnel: Jack Elston (last editor), Geoff Bland (strategy input)

## Executive Summary
This document outlines BST's strategic approach to a Phase II SBIR proposal for a soil moisture measurement system using an unmanned aircraft system (UAS). The strategy emphasizes positioning the SuperSwift airframe with integrated avionics and a novel soil moisture sensor as the solution to NASA's needs for suborbital Earth science observations, while demonstrating sufficient technical maturity without overstating system readiness to avoid losing Phase II funding.

## Technical Approach

### Core System Architecture
- **Airframe**: SuperSwift with modular nose cone design enabling payload flexibility; hand-launch capability (no launcher required)
- **Avionics**: SwiftPilot Pro autopilot with:
  - Precise/repeatable flight path control
  - GPS RTK capability
  - Terrain following for low-altitude missions
  - Support for science-grade missions
- **Sensor Integration**: Payload bus capable of integrating multiple sensors including soil moisture instrument (LDCR) and laser altimeter
- **Data Acquisition**: High-speed data acquisition unit (DAC) designed for science-grade data rates not previously available on sUAS; designed with 32 SD card array and FPGA

### Operational Capabilities
- Capability for Arctic operations (critical differentiator for NASA)
- Low-altitude, precision flight control for repeat-pass Earth monitoring
- Precise altitude maintenance above ground level via laser altimeter integration
- Remote operation with graphical user interfaces (GUIs) for mission control
- Ground and on-board calibration capabilities

## Products & Capabilities Described

### SuperSwift Airframe
- Hand-launch capable small UAS
- Modular nose cone for different sensor configurations
- Supports Arctic deployment
- Builds on Tempest platform's storm flight heritage

### SwiftPilot Pro (SP Pro)
- First autopilot designed specifically for science-grade missions
- Enables GPS RTK positioning
- Precise terrain following with low-cost systems
- Coverage control with UI capabilities
- Described as novel technology requiring Phase II completion and demonstration

### Data Acquisition Unit (DAC)
- Novel technology enabling very high data rates for sUAS platforms
- Designed with single SD card version in Phase I
- Phase II will complete full version with 32 SD card array and FPGA
- Enables science-grade data collection previously unavailable at this platform scale

### NDVI Sensor Board
- Novel, lightweight, low-cost sensor providing science-grade data
- Represents new technology advancement

### Soil Moisture Sensor (LDCR)
- NASA-developed sensor being adapted for airborne deployment
- Centerpiece of the proposed system for Phase II
- Phase I identified key specifications but Phase II required for detailed implementation

## Use Cases & Applications

### Primary Mission: Soil Moisture Measurement
- Support SMAP (Soil Moisture Active Passive) satellite calibration and validation
- Support Aquarius salinity satellite operations
- High-resolution measurements near major watersheds
- Drought-stricken area monitoring for water management decisions
- On-demand, local-scale measurements complementing global satellite observations
- Wildfire prevention and control management

### Secondary Applications
- Arctic and Antarctic research activities (Ice Bridge program alignment)
- Flash flood prediction (FEMA application mentioned)
- U.S. Global Change Research Program support
- Climate research and environmental monitoring
- Atmospheric and surface sampling in polar regions

## Testing & Deployment Strategy

### Phase II Timeline
**Year 1**: Oklahoma test site validation (alternative: University of Nebraska-Lincoln)
- Validate Phase I prototype system early
- Leverage NASA's EV-1 mission currently operating there (through 2015)
- Develop SuperSwift as lower-cost alternative to G-III aircraft

**Year 2**: California test site deployment
- Larger-scale deployment demonstration
- Preparation for Greenland operations
- SMAP calibration site co-location
- Proof of concept for calibration support role

**Beyond Phase II** (Phase II-E/X or Phase III):
- SMAP terrestrial validation operations
- Greenland deployment
- Phase II focuses on preparation, not execution
- Funding/matching from SMAP and Aquarius programs

## NASA Program Goals Alignment

BST mapped their proposed system to S3.05 Program Goals across four areas:

1. **New Technologies for Extreme Environments**: SuperSwift changeable nose cone, SP Pro payload capabilities, Greenland Arctic deployment plan, Tempest storm heritage
2. **Scientific Observation & Climate Research**: Local-scale measurements augmenting SMAP and Aquarius; support for U.S. Global Change Research Program and Arctic/Antarctic activities
3. **Precise Flight Control**: SP Pro GPS RTK and terrain following capabilities; repeat-path observations for seasonal and multi-year monitoring
4. **Unique Earth Science Capabilities**: sUAS-specific capabilities that large platforms cannot provide; LDCR sensor integration; on-demand local information for applications like flash flood prediction

## Key Strategic Messaging

### What to Sell Reviewers
1. Technology fits NASA needs, is novel, and BST is executing based on Phase I results
2. Phase II is essential for transitioning to commercially viable form for NASA scientists, non-NASA research programs, and commercial customers
3. Avoid overstating system maturity—critical risk is reviewers think BST can commercialize without Phase II support

### Intellectual Property & Novel Technologies
- SwiftPilot Pro autopilot
- Data Acquisition Unit (DAC) with high data rate capability
- NDVI sensor board
- SuperSwift airframe
- Precise terrain following with low-cost systems
- Coverage control UI
- Document notes DAC may be protectable IP

## Phase I Reviewer Feedback Summary

### Scientific/Technical Merit (Positive)
- Detailed sensor design centerpiece well-supported by avionics, mission planning, airframe modifications
- Clear focus on improving spatial and temporal resolution of soil moisture observations
- Solid understanding of regulatory and operational issues
- Feasible and well-outlined proposed solutions
- Infusion for societal benefit clearly articulated

### Experience & Qualifications (Positive)
- BST specializes in UAS avionics and sensing systems
- PI and team exceptionally well-suited for practical small UAS research implementation
- Team experience well-aligned with objectives
- Combines platform systems and sensor expertise coherently
- Clear awareness of NASA research objectives and airborne/space-based missions

### Work Plan (Positive)
- Extremely detailed with 1-week resolution for Phase I
- Clear vision toward successful UAS-based capability
- Benefits clearly outlined and well-organized
- Strong focus on Phase II success
- Notional Phase III considerations provided

### Identified Gaps
- Soil moisture sensor specifications not fully detailed in Phase I proposal (depth of penetration, polarization, aperture size, angle of incidence) due to separate sensor funding
- Need for well-defined sensor specifications before Phase II

## Notable Details

- **Risk Management**: Strategy explicitly warns against appearing too mature to avoid losing Phase II funding
- **Partnership Model**: BST partners with airframe manufacturer and remote sensing partner with separate sensor development funding
- **Market Positioning**: System addresses gaps in capability for polar regions where current sUAS technology is insufficient
- **Cost Advantage**: Proposed as lower-cost alternative to existing platforms (e.g., G-III aircraft for similar missions)
- **Regulatory Path**: Phase I included addressing regulatory approval for soil moisture measurement missions
- **Facilities**: Oklahoma test site used; mentions University of Nebraska-Lincoln as alternative; California site identified for Year 2; Greenland as final deployment
- **Commercial Viability**: Document emphasizes both NASA and non-NASA market opportunities, with NASA mission infusion as primary path