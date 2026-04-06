# Advanced Sensor Fusion for Terrain Following from Autonomous Aircraft

## Document Metadata
- Type: SBIR Phase I Briefing Chart / Proposal
- Client/Agency: NASA
- Program/Solicitation: NASA SBIR 2021, Topic A2.02-1797
- Date: January 6-8, 2021
- BST Products/Systems Referenced: S2 UAS
- Key Personnel: Maciej Stachura (PI), Jack Elston (contact)

## Executive Summary
Black Swift Technologies proposes developing an advanced sensor fusion system for real-time 3D hazard mapping that enables fixed-wing UAS to safely operate at low altitudes in terrain-challenged environments. The system uses pseudo-lidar technology based on stereo depth neural networks to provide terrain and obstacle awareness, addressing a significant gap in autonomous fixed-wing operations over rugged terrain where multi-rotor aircraft are currently the only viable option.

## Technical Approach
- **Core Technology**: Pseudo-lidar capability using deep neural networks trained on stereo imagery
- **Sensor Fusion Strategy**: Combines stereo camera imagery with DEM (Digital Elevation Model) data for enhanced terrain classification
- **Implementation Path**: 
  - Generate training datasets for neural network development
  - Train and evaluate two stereo depth DNN versions (stereo-only and stereo+DEM fusion)
  - Select lightweight, low-cost sensors and compute hardware suitable for small UAS
  - Integrate and test on flight hardware, demonstrating real-time performance at fixed-wing flight speeds
  - Design mechanical integration and prepare flight certification materials for Phase II testing on BST aircraft

## Products & Capabilities Described

**S2 UAS**
- BST's fixed-wing platform already tested in multiple NASA campaigns
- Identified need for terrain-contouring system during volcanic plume sampling mission in Costa Rica
- Proposed as initial platform for incorporating the new terrain-following technology

**Pseudo-Lidar Terrain/Object Classification System**
- Generates low-altitude 3D hazard maps in real-time
- Lightweight and low-cost design for integration on small UAS
- Real-time performance requirement at fixed-wing aircraft speeds
- Provides terrain and obstacle awareness for autonomous low-altitude flight

## Use Cases & Applications

**NASA Applications**
- Volcanic plume measurements with terrain contouring
- High-resolution soil moisture measurements
- Surface flux calculations above arctic tundra
- Legacy NASA UAS integration

**Non-NASA Applications**
- Infrastructure inspection with reliable low-altitude flight capability
- Leak detection systems
- Mountain mapping in rugged terrain
- Rock slide mitigation planning
- Avalanche prediction support

## Technical Objectives & Deliverables

**Phase I Objectives:**
1. Identify and validate algorithms and training data for real-time pseudo-lidar operation at fixed-wing flight speeds
2. Develop preliminary design of pseudo-lidar and terrain/object classification system
3. Integrate, test, and evaluate pseudo-lidar capability
4. Design mechanical system and prepare flight certification materials for Phase II

**Milestones:**
- Completion of training data library
- Build and evaluation of stereo DNN (two versions: stereo-only and stereo+DEM fusion)
- Sensor and compute hardware evaluation and selection
- Real-time system demonstration on flight hardware

## Notable Details
- Problem Statement: Fixed-wing UAS have been restricted to operational areas without obstacles or significant terrain variation; manual multi-rotor operation remains the primary solution for challenging terrain
- Market Positioning: System positioned as transferable to legacy NASA platforms and commercial applications (infrastructure inspection, GIS/surveying)
- TRL Assessment: Document indicates TRL level (specific number not clearly stated in excerpt)
- Contact: Jack Elston, (720) 638-9656, elstonj@blackswifttech.com