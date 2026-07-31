# NOAA Statement of Work: Line-of-Sight Video-Enabled Black Swift S0 UAS

## Document Metadata
- **Type:** Statement of Work (SOW) / Delivery Order
- **Client/Agency:** National Oceanic and Atmospheric Administration (NOAA)
- **Program/Solicitation:** NOAA 2026 IDIQ Contract; Delivery Order XXXXX
- **Date:** July 29, 2026 (Draft)
- **BST Products/Systems Referenced:** Black Swift S0 (Air Deployed UAS)
- **Key Personnel:** Beck Cotter (last editor)
- **Status:** Draft

## Executive Summary
NOAA seeks to develop and deliver two video-enabled Black Swift S0 uncrewed aircraft systems capable of transmitting line-of-sight video from the S0 to NOAA's WP-3D Orion (P-3) research aircraft during hurricane operations by leveraging the P-3's existing high-frequency (HF) antennae. The effort includes camera system integration, communication architecture development to handle bandwidth and attenuation constraints, end-to-end demonstration, and delivery of fully configured platforms with technical documentation.

## Technical Approach

### System Architecture
- **Video source:** Integrated camera system on S0 UAS
- **Transmission medium:** Line-of-sight (LOS) via NOAA P-3 existing HF antennae (no new antenna installation required)
- **Challenge:** Hurricane environment with bandwidth limitations, signal attenuation, latency constraints
- **Data handling strategies:** Practical transmission rates, buffering, progressive transmission, still-image stitching/sequencing to create video-equivalent products

### Key Technical Constraints to Address
- S0 airframe weight budget (~1.2 kg baseline, camera must fit within this)
- Size, weight, power (SWaP) constraints of compact platform
- Environmental and electromagnetic compatibility with S0 airframe
- Radio-frequency challenges specific to tropical cyclone conditions
- Compatibility with P-3 HF antenna interface (Government to provide interface specifications)

### Development Path
1. Baseline S0 platform provision
2. Video camera system selection and integration
3. LOS video communication solution design and implementation
4. Transmission rate and data-handling strategy determination
5. End-to-end demonstration under representative conditions
6. Delivery with documentation

## Products & Capabilities Described

### Black Swift S0 (Air Deployed UAS)
**What it is:**
- Compact, U.S.-manufactured uncrewed aircraft system
- Airframe weight: approximately 1.2 kg (2.6 lbs)
- Maximum flight endurance: ≥100 minutes (under standard conditions)
- Currently operated by NOAA for precision atmospheric measurements in extreme conditions

**Current capabilities:**
- Autonomous flight with automated sampling patterns
- Integrated sensor suite: air temperature, wind speed/direction, dewpoint, atmospheric pressure
- Pivotable-wing design enabling P-3 drop-tube launch and deep-stall recovery capability
- Operational in hurricane-force winds with heavy precipitation
- Can be air-deployed from P-3 aircraft

**Proposed enhancement:**
- Integration of video camera system
- LOS video transmission to P-3 using HF antennae
- Unit price (baseline S0): $18,000 per platform

**Constraints for this application:**
- Cannot exceed weight budget while accommodating camera
- Must maintain environmental tolerance to hurricane conditions
- Camera must be electromagnetically compatible with existing S0 systems

## Use Cases & Applications

### Primary Mission Context
- **Hurricane/tropical cyclone operations:** Real-time or near-real-time visual situational awareness during NOAA P-3 reconnaissance missions into tropical cyclones
- **Atmospheric sampling missions:** Enhanced scientific utility through coincident visual observations with meteorological measurements
- **Safety enhancement:** Visual confirmation of S0 status and operational environment during air deployment missions

### Operational Scenario
- S0 deployed from P-3 into hurricane environment
- Visual feedback transmitted back to P-3 via existing HF antenna system
- Mission effectiveness improved through real-time awareness of storm structure, cloud formations, and sea state
- No requirement for new P-3 antenna installations or extensive new infrastructure

## Key Requirements

### Task One: Baseline S0 UAS Platforms
- Two (2) baseline S0 systems meeting current datasheet specifications
- Airworthy and ready for video/communication integration
- Weight: ~1.2 kg
- Endurance: ≥100 minutes standard conditions
- Hurricane-capable
- Integrated meteorological sensors maintained
- Pivotable-wing, autonomous capable

### Task Two: Video Camera System Integration
- Selection and integration of suitable camera for tropical-cyclone environment
- Must address SWaP constraints
- Environmental and electromagnetic compatibility required
- Capability to provide useful visual situational awareness

### Task Three: LOS Video Communication Development
- Design communication solution leveraging existing P-3 HF antennae
- LOS geometry consistent with air-deployed UAS operations
- Determination of practical transmission rates
- Data-handling approach addressing:
  - Bandwidth limitations
  - Latency
  - Signal attenuation
  - RF challenges in hurricane environment
- May employ: buffering, progressive transmission, still-image stitching/sequencing
- Government to provide P-3 HF antenna interface information
- No new antenna installation on P-3 assumed or required

### Task Four: Demonstration and Delivery
- End-to-end LOS video demonstration under operationally representative conditions
- Full camera → link → P-3 reception path (or Government-approved surrogate)
- Delivery of two (2) fully configured video-enabled S0 UAS
- Technical documentation including:
  - Camera system description
  - Communication architecture
  - Data-handling approach
  - Operator guidance
  - Design materials from R&D effort

## Project Management & Administrative Requirements

### Schedule & Duration
- **Period of Performance:** Not to exceed 12 months from award date
- **Post-Award Conference:** Within 10 business days of award
- **Draft Project Plan:** At Post Award Conference
- **Final Project Plan:** Within 10 business days after Post Award Conference
- **Monthly Progress Reports:** Throughout period of performance
- **Demonstration:** Prior to final delivery
- **Final Delivery:** Per approved Project Plan

### Staffing & Personnel
- Contractor responsible for adequate workforce with expertise in:
  - UAS systems
  - Video imaging
  - Radio-frequency communications
- Designated Project Manager as single point of contact
- PM availability during Eastern Time business hours; 1-business-day response time required

### Deliverables (Mandatory Items Marked with *)
1. Post Award Conference (NLT 10 business days after award)
2. Draft Project Plan (at Post Award Conference)
3. Final Project Plan (NLT 10 business days after conference)
4. Monthly Progress Reports (throughout period)
5. Camera & LOS video-link design approach—technical description (per approved Project Plan)
6. End-to-end LOS video capability demonstration (prior to final delivery)
7. Two (2) video-enabled S0 UAS systems (per approved Project Plan)
8. Technical documentation, operator guidance, design materials (concurrent with final delivery)

### Place of Performance
- Primary: Contractor's facilities
- Coordination/interface meetings: Government-designated locations (NOAA Aircraft Operations Center or teleconference)
- Delivery: NOAA-designated facility

## Notable Details

### Leveraging Existing Assets
- **Critical cost/complexity benefit:** Uses P-3's existing HF antennae rather than requiring new antenna hardware procurement and installation
- This significantly reduces aircraft modification scope and operational impact

### Scope Exclusions (Not Covered)
- Installation of new antennae on P-3
- Pilot training beyond system delivery/documentation
- Long-term sustainment

### Risk Considerations Implied
- Hurricane environment presents significant RF propagation and data-transmission challenges
- Bandwidth and latency limitations may necessitate creative approaches (image stitching, buffering)
- Integration of camera on weight-critical platform requires careful engineering
- Interface coordination with Government for P-3 HF antenna specs is critical path item

### Information Protection & Export Control
- Contractor must safeguard proprietary and Government-sensitive information
- P-3 antenna interface data treated as sensitive
- Department of Commerce/NOAA security and export-control requirements apply
- No classified information required but data protection protocol mandated

### Intellectual Property
- To be defined in resulting contract
- Contractor must identify any preexisting proprietary technology incorporated

### Quality & Compliance
- FAA regulations for public-aircraft-status UAS operations
- Section 508 accessibility standards for any Electronic/Information Technology developed
- Government review/approval period: 10 business days per deliverable; 10 business days for correction of deficiencies