# Machine Vision Based Obstacle Classification

## Document Metadata
- Type: Workshop presentation/overview deck
- Client/Agency: NASA (via SBIR funding)
- Program/Solicitation: NASA Phase I and Phase II SBIR (NNX17CD08P, 80NSSC18C0042)
- Date: September 21, 2021
- BST Products/Systems Referenced: S0, S1, S2 fixed-wing UAS
- Key Personnel: Jack Elston (presenter/last editor)

## Executive Summary
Black Swift Technologies presented their development of an automated "Safe to Land" system using machine vision and machine learning to enable fixed-wing UAS to safely land autonomously in emergency situations during beyond-visual-line-of-sight (BVLOS) operations. The system uses semantic segmentation networks to identify hazards and safe landing areas, processes data on-board in real-time without cloud computing, and has been successfully tested on BST S1 and S2 aircraft.

## Technical Approach

### Core Problem
Fixed-wing UAS have higher failure rates than general aviation and require long landing corridors. In BVLOS operations, pilots cannot visually guide emergency landings. The system needed to replicate pilot decision-making for landing site selection.

### Technical Solution
- **Backbone Technology**: Advanced semantic segmentation neural networks that map images to pixel-by-pixel object labeling
- **Training Data**: Combination of open-source labeled imagery and custom curated datasets, leveraging transfer learning from self-driving car networks
- **Processing Pipeline**:
  1. Continuous semantic segmentation mapping during flight
  2. Conversion of segmentation maps to hazard/safe area classifications
  3. Fitting of landing corridors (circles for VTOL, 100m × 5m rectangles for fixed-wing)
  4. GPS coordinate estimation of safe areas
  5. Storage of landing candidates in onboard memory
  6. On-engine-failure: selection of nearest landing area and transmission to autopilot
  7. Pilot retains final decision authority

### Hardware Integration
- Downward-facing camera
- Embedded processor with sufficient compute power
- Integrated into S1 and S2 fuselages with minimal SWaP impact

### Key Constraints Met
- Size, Weight, Power, and Cost (SWaP-C) compliant
- Fully autonomous onboard processing (no cloud/radio link dependency)
- Real-time operation at >1 Hz
- Reaction time <60 seconds from engine failure to landing plan execution
- No requirement for pre-planned landing areas or visual markers
- Handles both discrete hazards (cars, buildings, fences) and nebulous hazards (water)

## Products & Capabilities Described

### BST Fixed-Wing UAS Family
| Model | Role in Project |
|-------|-----------------|
| **S0** | Smallest platform in product line |
| **S1** | Medium platform; underwent flight testing with Safe to Land system |
| **S2** | Largest platform; underwent flight testing with Safe to Land system; better wind speed capability |

**Common Advantages**: Superior range/endurance compared to similarly-sized multirotor, capable of operation in higher wind speeds, but require ~100m landing corridors.

### Safe to Land System
- **Type**: Automated emergency landing system based on semantic segmentation neural networks
- **Detection Categories**: People, low vegetation, pavement, water, dirt, clutter, person on bicycle, fencing
- **Operating Modes**: 
  - Safe to VTOL (fits small circles in safe areas)
  - Safe to Land/Fixed-Wing (fits 100m × 5m runway rectangles)
- **Performance**: Identifies safe landing areas at >1 Hz; processes hundreds of landing candidates during a flight
- **Status**: Deployed and flight-tested; demonstrated capability; undergoing refinement toward more conservative selection criteria

### Autopilot System
- BST-developed in-house autopilot handles autonomous landing dynamics
- Accepts GPS coordinates from Safe to Land system
- Executes landing maneuvers autonomously

## Use Cases & Applications

### Primary Applications Driving Development
1. **Infrastructure Inspection**: Pipeline inspection over hundreds of miles requiring autonomous operation
2. **Autonomous Delivery**: Long-range drone delivery (Amazon/Google referenced as comparable effort)
3. **Precision Agriculture**: Extended-range agricultural monitoring
4. **BVLOS Operations**: Any mission requiring operation beyond visual line of sight

### Regulatory Context
- System designed to improve UAS safety/reliability record to justify FAA regulatory relief for BVLOS operations
- Current FAA regulations require multiple pilots every few miles for long-range operations or high-bandwidth video links
- System enables single-pilot BVLOS operations

## Key Results

### Flight Testing Outcomes
- **System Deployment**: Successfully integrated onto S1 and S2 aircraft
- **Open-Loop Testing**: Multiple flight tests conducted with system in recording mode (not controlling aircraft)
- **Safe Landing Identification**: System successfully identified safe landing zones during flight
- **Processing Speed**: Achieved >1 Hz landing area detection and identification
- **Landing Candidate Generation**: Produced hundreds of viable landing candidates from short flight durations
- **Accuracy Demonstration**: Correctly matched computed GPS coordinates to actual landing areas (validated via Google Maps overlay)

### Refinement Results
- Initial testing revealed overly-aggressive landing site selection (e.g., 100m runway between grain silo and fence)
- Parameter adjustment produced more conservative selection criteria in subsequent testing
- Validated on sod farm near Longmont, Colorado with successful performance

## Future Work & Capability Development

### Near-Term Development
- **Drop-In Module**: Assembly of Safe to Land system components as upgradeable module for third-party aircraft integration
- **UI Development**: Simple user interface for non-BST platform integration

### Optical Navigation Enhancement
Development of secondary navigation capabilities using the machine vision package:

1. **Optical Flow**: 
   - Computes aircraft velocity without GPS
   - Enables navigation during GPS jamming/spoofing
   - Tested successfully in post-flight analysis

2. **Visual Navigation**: 
   - Uses critical ground features for absolute position correction
   - Corrects drift in velocity-integrated position estimates
   - Enables position correction during GPS denial

3. **SLAM (Simultaneous Localization and Mapping)**:
   - Reconstructs flight trajectory with high precision using only visual references
   - Builds environmental map while localizing
   - Enables robust BVLOS navigation without GPS
   - Flight-tested with demonstrated trajectory accuracy

### Integration Benefits
- Optical techniques can augment semantic segmentation by mapping across multiple image frames
- Combined approach can produce safer landing plans using information from larger scanning areas
- Addresses FAA requirement for GPS-independent fallback navigation

## Notable Details

### Competitive Context
- Amazon recently announced similar safe landing detection for their delivery drones (vertical takeoff/landing)
- BST's approach addresses additional complexity of fixed-wing skid-to-land dynamics
- Semantic segmentation approach superior to object detection for identifying thin structures (e.g., fencing)

### Technical Distinctions
- **Semantic Segmentation vs. Object Detection**: Chosen semantic segmentation specifically because it can identify thin/small hazards (fencing, people) that object detection might miss
- **Transfer Learning Efficiency**: Leveraged pre-trained self-driving car networks to rapidly and affordably train custom networks
- **Conservative Design**: Pilot maintains final decision authority on emergency landing execution; system operates continuously during flight to pre-identify safe areas rather than computing during emergency

### Development Funding
- Supported by NASA SBIR Phase I and Phase II grants totaling significant funding
- Demonstrates NASA investment in UAS safety/autonomy improvements

### In-House Capability
- BST designs and develops autopilot systems, cameras, processors, and airframes internally, enabling tight systems integration
- Custom imaging and processing solution sized specifically for their aircraft platforms