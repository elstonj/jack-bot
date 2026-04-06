# Terrain Following - Phase I Interim Report Outline

## Document Metadata
- Type: Interim Report Outline (planning document)
- Client/Agency: NASA
- Program/Solicitation: 2018 SBIR, Terrain Following topic
- Date: October 22, 2018
- BST Products/Systems Referenced: S2 or S3 (implied through hardware/sensor integration context)
- Key Personnel: Not named in this outline

## Executive Summary
This outline documents Phase I progress on a NASA SBIR terrain-following project. BST completed significant work on system design, requirements, and sensor identification, and has begun algorithm development for flight modes and obstacle avoidance. The project is pivoting toward hardware evaluation and exploring commercialization partnerships.

## Technical Approach

**System Design (Completed)**
- Requirements definition
- Concept of operations (ConOps)
- Mission categories definition
- Obstacle identification

**Sensor Selection (Completed)**
- State-of-the-art review of sensing modalities
- Camera evaluation
- Laser evaluation
- Radar evaluation

**Algorithm Development (In Progress)**
- New flight mode design
- Obstacle avoidance system design
  - Discretized controllers
  - Hierarchical response architecture
- Sensor fusion identified as requirement
- Terrain estimation algorithm development
- SLAM-like system planned for obstacle avoidance

**Hardware Evaluation (Newly Initiated)**
- Representative processing hardware selection
- Camera evaluation (with photographic documentation planned)
- Laser evaluation (with photographic documentation planned)

## Products & Capabilities Described

**Sensing Systems:**
- Camera systems: Desired coverage range 20-60 meters
- Laser systems: Evaluated for terrain following
- Radar systems: Assessed as coarse and slow in 20-60m range; deemed insufficient for primary ranging
- Stereo vision: Identified as needed for adequate coverage in target range

**Processing Hardware:**
- Representative processing platform being evaluated for onboard autonomy

## Use Cases & Applications
- Terrain-following autonomous flight
- Obstacle avoidance in flight
- Terrain estimation and mapping

## Notable Details

**Technical Findings:**
- Analysis determined stereo vision preferable to radar for 20-60m obstacle detection coverage
- Sensor fusion required for robust operation
- Discretized control architecture with hierarchical response strategy

**Commercialization Pivot:**
- Partnership discussion with IPOZ for underwater photogrammetry application (leveraging same camera and processor systems)
- Outreach to CEI as potential partner for radiometer/radar development

**Project Status:**
- Significant progress on system design and sensor selection
- Hardware evaluation newly initiated
- Algorithm work ongoing but not yet complete
- Document notes this is pivoting strategy (suggesting course correction or scope adjustment)