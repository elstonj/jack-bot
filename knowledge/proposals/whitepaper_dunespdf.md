# Great Sand Dunes National Park and Preserve Unmanned Aircraft System Aerial Survey

## Document Metadata
- Type: White paper / case study
- Client/Agency: Great Sand Dunes National Park and Preserve (National Park Service)
- Program/Solicitation: NPS Scientific Research and Collecting Permit
- Date: October 19, 2016 (flight date); May 15, 2018 (document creation)
- BST Products/Systems Referenced: SwiftTrainer UAS, SwiftTab flight planning software, SwiftCore Flight Management System (FMS)
- Key Personnel: Jack Elston (Pilot-in-Command, CEO of BST); Brendan Thompson (WCE, UAS Mission Planning); Mary Wohnrade (WCE, Engineering and Surveying); Constantin Diehl (UAS Colorado, Project Coordination)

## Executive Summary
This white paper documents a landmark UAS mission at Great Sand Dunes National Park where Black Swift Technologies' SwiftTrainer aircraft and WCE conducted the first FAA-licensed UAS survey over the park. Two flights on October 19, 2016 collected 1,755 images over a 1-square-mile area centered on the 750-foot Star Dune, producing high-resolution orthomosaics and 145-million-point 3D point clouds for the National Park Service to support change detection and terrain monitoring of the dynamic dune system.

## Technical Approach

**Mission Planning:**
- SwiftTab flight planning software used to generate flight paths with automatic waypoint generation based on specified altitude above ground level and photo overlap percentage
- Software incorporated digital elevation models to maintain uniform ground sample distance across 750-foot terrain variations
- Automatic photo trigger placement based on GPS location to eliminate spacing errors from wind

**Data Collection:**
- Two flights conducted on October 19, 2016, totaling 2 hours 30 minutes
- Flight path maintained significant distance (several miles) from launch/landing site per NPS permit requirements
- 1,755 total images collected: 1,289 from first flight, 466 from second flight
- "Resume mapping" feature used to ensure proper overlap between flight datasets
- Hand-launch and automated landing capabilities essential given NPS site constraints

**Ground Control:**
- Seven surveyed ground control points (GCPs) and check points established over 8 hours by two-person crew on October 18, 2016
- Far below standard 24 GCPs for 1-square-mile survey due to terrain inaccessibility and foot travel requirement
- GPS x,y,z coordinates collected for each point with measures to prevent sand burial or drift

**Post-Processing:**
- Multiple photogrammetry software suites tested; ESRI Drone2map selected as producing best results
- Processing challenged by homogeneous sand surface causing feature detection and tie-point matching difficulties
- Initial image positions compared with computed positions; omitted images resulted from intense elevation change and uniform ground textures

## Products & Capabilities Described

### SwiftTrainer UAS
- **What it is:** Fixed-wing UAS platform designed for aerial mapping campaigns
- **Capabilities:** 
  - Extended range and ability to map up to 2.25 square miles in single flight
  - Hand launch and automated landing
  - Industry-leading AOI coverage through uniform image spacing, tight flight tracking, consistent overlap pattern
  - Accurate geotagging of images
  - "Resume mapping" feature for multi-flight continuity
- **Use in project:** Primary data collection platform; 1,755 images collected over 1 sq-mi area in two flights
- **Performance:** Operated 2+ miles from launch/landing site while maintaining safe voice communications with visual observers

### SwiftTab Flight Planning Software
- **What it is:** User interface software for flight path generation
- **Features:** 
  - Simplified mapping plan creation from minimal parameters (altitude AGL, photo overlap percentage)
  - Automatic track generation
  - GPS-based photo trigger placement
  - Digital elevation model integration for terrain-adaptive flight planning
  - Prevents waypoint intersection with sharp terrain features
- **Use in project:** Generated two separate flight paths to cover 1-square-mile AOI with significant terrain variations

### SwiftCore Flight Management System (FMS)
- **Mention:** Described as foundational system including autopilot, ground station, user interface, and support electronics
- **Advantage noted:** BST controls critical components (avionics electronics, software, mechanical assembly, QC) unlike competitors using open-source avionics

## Use Cases & Applications

**Primary Application: National Park Terrain Monitoring**
- Change detection for dynamic dune features (Star Dune and High Dune)
- Baseline topographic mapping for comparison with future surveys
- Alternative to labor-intensive traditional surveying methods
- High-resolution imagery revealing previously unknown features and new discoveries

**Specific Mission Requirements Addressed:**
- Remote accessibility: Terrain inaccessible by vehicle required foot travel for GCP establishment
- Regulatory compliance: Launch/landing outside park boundary per NPS permit
- Challenging environment: Homogeneous sand surface, extreme elevation variations (750 ft), variable wind and shadow conditions
- Long-range operations: AOI several miles from launch site requiring constant voice communications between visual observers and pilot

## Key Results

**Delivered Data Products:**
1. High-resolution orthomosaic image (3 cm/pixel GSD) of 1-square-mile area
2. One-foot contours in .shp file format
3. 3D point cloud (145+ million points) in .las format at ~1.5 square inch ground resolution
4. 3D model in .obj format

**Accuracy Assessment (ASPRS Standards):**
- Horizontal accuracy: RMSEx = 0.22 ft, RMSEy = 0.72 ft, RMSEr = 0.75 ft
- Horizontal Accuracy Class: 17.50 cm (below typical 10 cm standard due to limited GCPs)
- Vertical accuracy: RMSEz = 1.84 ft
- Vertical Accuracy Class: 33.3-66.7 cm (below typical 2.5-10 cm standard due to limited GCPs and homogeneous terrain)

**Client Satisfaction:**
- NPS Research Team noted results as "definitely the best imagery of the dunes to date"
- High-resolution orthomosaic revealed new information previously unknown to park staff
- Imagery led to recognition of new features and possible new discoveries

**Future Plans:**
- Anticipated annual data collections at same AOI for change detection monitoring
- WCE and BST developing custom UAS platform with LiDAR scanner and 42-megapixel camera for 2017 follow-up survey
- Comparison of 2016 and 2017 datasets planned to evaluate improved accuracy

## Notable Details

**Partnerships:** Collaborative effort between Wohnrade Civil Engineers (FAA Part 107 certified), Black Swift Technologies, UAS Colorado, and National Park Service

**Challenges and Solutions:**
- Limited GCP count (7 vs. ideal 24): Mitigated with careful software selection and manual tie-point intervention
- Homogeneous sand surface: Addressed through photogrammetry software selection and parameter tuning
- Extended mission distance: Enabled by SwiftTrainer's extended range, hand launch, and automated landing
- Terrain variation (750 ft): Handled through SwiftTab's DEM-integrated altitude management

**Regulatory Milestone:** First FAA-licensed operator (WCE) to conduct sanctioned UAS mission over Great Sand Dunes National Park

**Cost Effectiveness:** WCE documentation notes UAS mapping saves clients approximately 40% vs. traditional ground surveying, with data collection in less than 1 hour vs. days for conventional methods

**Technology Differentiation:** Document emphasizes BST's advantage in controlling critical avionics components (unlike open-source competitors) and integrating consulting expertise with product delivery