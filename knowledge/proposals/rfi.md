# Air Force RFI: Small Unmanned Aerial Systems (sUAS) Kit for Aerial Land Survey

## Document Metadata
- Type: Request for Information (RFI) - Market Research
- Client/Agency: Air Force Life Cycle Management Center (AFLCMC), Battlefield Airmen Branch (WISN), Wright-Patterson AFB, OH
- Program: Air Force Special Operations Command (AFSOC) sUAS aerial land survey mission capability assessment
- Date: 2018-02-06 to 2018-02-07
- Document Status: Completed/Inactive Project
- Last Editor: constantin.diehl

## Executive Summary
AFLCMC issued a market research RFI seeking potential sources for a complete fixed-wing sUAS kit capable of hand-launched autonomous flight for aerial land survey missions. The kit must include aircraft, payload (RGB camera for photogrammetry), and subsystems/software for mission planning, flight control, and image processing to produce 3D orthomosaics and digital surface models.

## Technical Requirements

### Aircraft Specifications
- **Configuration**: Fixed-wing, hand-launched, autonomous flight to mission end including automatic landing (no catapult required)
- **Weight**: 3 pounds or less
- **Wingspan**: 115 cm or less; detachable or deployable wings preferred for transport
- **Cruising Speed**: 25-70 mph
- **Endurance**: Minimum 50 minutes total flight time
- **Operational Range**: Limited only by aircraft endurance; operations beyond 2 nm from launch area acceptable with reduced coverage; lost-link continuation of mission permitted
- **Terrain Capability**: Assumes suitable launch/recovery area with terrain variation ≤100 ft vertically, or where Surface Model data available
- **Vegetation Limits**: Areas without tall vegetation (trees/dense brush); individual plants/small groups acceptable
- **Wind Capability**: Specific wind limitations and cross-wind performance to be defined by proposed solution

### Sensor Payload
- **Type**: RGB camera system for photogrammetric drone mapping
- **Resolution**: Minimum 20 megapixels
- **Ground Sampling Distance (GSD)**: 1.5 cm per pixel or less
- **Nominal Coverage**: At 400 feet AGL, 0.85 square miles coverage
- **Image Overlap**: Desired minimum 70% overlap between images for accurate orthomosaic and 3D mapping
- **Environmental Protection**: Dust and shock protection; performance in extreme hot/cold environments required
- **Operations**: Capable of capturing detailed RGB images across range of light conditions; timing requirements for imaging in strong winds

### Flight Control & Mission Planning Software
- Automatic 3D flight planning
- Constant Above-Ground-Level (AGL) altitude maintenance over known terrain for consistent GSD
- Thumbnail image transmission during flight (when communication distance permits)
- Multi-flight mission capability (battery swap and re-launch for mission continuation)
- Built-in flight data manager for geo-referencing and image preparation for photogrammetric processing
- Mission block flight planning tools

### Image Processing & Data Management
- Image processing software comparable to Pix4D and Global Mapper
- Portable workstation (laptop) for data processing and mission planning
- Built-in Real Time Kinematic (RTK) / Post Processed Kinematic (PPK) functionality
- **Absolute Accuracy**: 3 cm with RTK/PPK activated out-of-box or for later activation

### Security & Compliance
- Authentication and encryption for data/imagery communications between aircraft and ground devices
- Data-at-Rest encryption for non-volatile storage
- Preference for NIAP (National Information Assurance Partnership) and DOD Information Network Approved Products List (APL) compliant products
- Secure ground station and processing laptop (noted that Microsoft-based OS systems considered vulnerable)
- Applicable MilSpec standards to be defined by proposed solution

## Sub-Systems & Spares Package
- Spare battery
- Spare wing set
- Spare charger
- Spare propeller
- Portable computer workstation(s) for data processing
- Pocket links and tags for GPS location identification
- End user device(s) (tablet capability for GPS tracking and mission monitoring)

## Use Cases & Applications
- **Mission Type**: Aerial land survey with photogrammetric mapping capabilities
- **Output Products**: 3D orthomosaics, highly precise digital surface models
- **Operational Context**: Theatre operations for AFSOC; assumed remote operations without VLOS requirement

## Key Assessment Focus
AFSOC specifically seeking to assess:
- sUAS aerial land survey mission capability
- System compatibility with operational requirements
- Technology maturity level

## Notable Details

**Document Characteristics**: 
- This RFI includes substantial clarifying questions and assumptions added by respondent (likely BST) to the original Air Force requirements
- Red Consultants identified as associated entity in file location path
- Respondent interpretations address ambiguities in original solicitation regarding:
  - Terrain assumptions
  - Wind operational limits
  - Megapixel vs. GSD trade-offs
  - Image overlap percentage requirements
  - Communications range and lost-link behavior
  - Environmental temperature extremes
  - RTK/PPK base station equipment and weight allocation
  - Computer security considerations
  
**Interpretation Approach**: Respondent (presumed BST) adopted conservative assumptions favoring operational flexibility, noting where specifications could be relaxed if terrain/environmental conditions differ from baseline assumptions.

**No Reimbursement**: Government explicitly stated no reimbursement for RFI response preparation costs.