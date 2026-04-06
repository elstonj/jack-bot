# Coordinated Drone-Based Plume Tracking

## Document Metadata
- Type: SBIR Phase I Proposal - Statement of Work
- Client/Agency: Defense Threat Reduction Agency (DTRA), Department of Defense
- Program/Solicitation: DTRA DoD 2025.2 Small Business Innovation Research (SBIR) Program, FOA Number 2025.2
- Date: Created 2025-05-07, Modified 2025-05-20
- BST Products/Systems Referenced: UAS (Uncrewed Aerial Systems)
- Key Personnel: Gijs de Boer (Environmental Science and Technologies), Beck Cotter (last editor)
- Partner Organization: Brookhaven National Laboratory (BNL)

## Executive Summary
Black Swift Technologies and Brookhaven National Laboratory propose a Phase I SBIR project to develop an automated plume tracking and reconstruction system that uses drone-mounted sensors combined with AI/ML neural volumetric capture techniques (such as neural radiance fields or Gaussian splatting) to reconstruct and track plumes emanating from source areas, with initial application to explosive test plumes.

## Technical Approach
The project leverages emerging neural volumetric capture and rendering techniques to reconstruct 3D plume evolution from sparse, non-overlapping drone-mounted camera imagery. Key technical aspects include:

- **Core Technology**: Neural radiance fields or Gaussian splatting—neural network-based techniques that implicitly represent multidimensional volumes without requiring traditional photogrammetry's stringent geometric constraints or heavy computational overhead
- **Sparse Measurement Reconstruction**: Ability to reconstruct volume from sparse measurements captured by multiple drones
- **Real-time Analysis**: Recent advances enable real-time analysis suitable for navigation tasks and multi-node sampling
- **Physics-Informed Representation**: The neural representation can be informed by additional sensor measurements beyond RGB imagery and by governing physics
- **Development & Testing**: BNL will conduct software development and testing, flight planning implementation, and preliminary analysis through laboratory tests and local flight tests at BNL, with planned initial field testing using BST-operated UAS

## Products & Capabilities Described

### Black Swift Technologies UAS Platform
- Multi-drone plume sampling and tracking capability
- Equipped with mounted cameras and sensor payloads
- Supports coordinated multi-node operations for uncertainty minimization
- Enables non-overlapping imagery collection from multiple perspectives

### Neural Volumetric Capture System (Under Development)
- Reconstructs explosive test plumes in 3D from drone imagery
- Processes sparse, non-overlapping images from multiple aircraft
- Operates in real-time for navigation and autonomous decision-making
- Integrates additional sensor data beyond RGB (e.g., spectral, chemical sensors)
- Incorporates physics constraints into reconstruction

## Use Cases & Applications
- Explosive test plume tracking and characterization
- Plume evolution reconstruction from source to dispersal
- Multi-drone coordinated sampling missions
- Real-time plume tracking for navigation and response

## Notable Details
- This is a **Phase I SBIR**, suggesting early-stage development with focus on proof-of-concept
- **Partnership Structure**: Black Swift Technologies as the primary contractor with Brookhaven National Laboratory as a supporting partner providing ML/AI expertise and testing facilities
- **Testing Progression**: Laboratory and local flight tests at BNL preceding field trials with BST UAS
- **Defense Application**: DTRA focus suggests potential applications to threats detection, characterization, and monitoring
- **Emerging Technology**: Uses cutting-edge neural volumetric rendering techniques newly developed for multi-agent applications