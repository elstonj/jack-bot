# Coordinated Drone-Based Plume Tracking

## Document Metadata
- Type: Statement of Work (SOW) / SBIR Phase I Proposal
- Client/Agency: Defense Threat Reduction Agency (DTRA), U.S. Department of Defense
- Program/Solicitation: DoD 2025.2 SBIR Program; FOA Number 2025.2
- Date: 2025-05-21 (submission date)
- BST Products/Systems Referenced: Black Swift Technologies UAS (drone systems with mounted sensors)
- Key Personnel: Gijs de Boer (Environmental Science and Technologies), Beck Cotter (last editor)
- Partner Organization: Brookhaven National Laboratory (BNL) - supporting organization

## Executive Summary
Black Swift Technologies, in partnership with Brookhaven National Laboratory, proposes to develop an automated plume tracking and reconstruction system using AI/ML techniques applied to drone-mounted sensor imagery. The system will use neural volumetric capture methods (neural radiance fields or gaussian splatting) to reconstruct and track plume evolution from explosive test sources, with testing conducted on BST UAS platforms.

## Technical Approach

**Core Technology:**
- Neural volumetric capture, representation, and rendering techniques
- Specifically: neural radiance fields (NeRF) or gaussian splatting
- These ML/AI methods use neural networks to implicitly represent multidimensional volumes

**Key Advantages Over Traditional Methods:**
- Reconstructs volumes from sparse measurements
- Eliminates stringent geometric constraints of photogrammetry
- Reduces computational burden compared to traditional techniques
- Enables real-time analysis for navigation and multi-node (multi-drone) sampling
- Can incorporate additional measurements beyond RGB imagery
- Can be informed by governing physics

**Implementation Plan:**
- Reconstruct and track explosive test plumes from multiple non-overlapping images
- Images acquired by drone-mounted cameras
- Development and testing of software and flight planning algorithms
- Preliminary analysis through laboratory and local flight tests at BNL
- Initial operational test using sensors mounted on Black Swift UAS

**BNL's Role:**
- Software development and testing
- Flight planning implementation
- Laboratory and field testing at BNL facilities
- Reporting and documentation
- Team coordination and project execution support

## Products & Capabilities Described

**Black Swift Technologies UAS:**
- Drone platforms with mounted sensor capability
- Capable of multi-node coordinated operations
- Proposed for integration of plume tracking payload
- Operational testing platform for neural volumetric capture algorithms

## Use Cases & Applications

**Primary Application:**
- Explosive test plume tracking and reconstruction
- Source area monitoring for plume evolution analysis
- Multi-drone coordinated sampling to minimize uncertainty

**Broader Defense Applications:**
- CBRN (Chemical, Biological, Radiological, Nuclear) detection and tracking
- Threat characterization and analysis
- Autonomous plume source identification

## Notable Details

- **Sparse Data Capability:** System designed to work with non-overlapping imagery, reducing flight coordination requirements
- **Multi-drone Optimization:** Recent advances in neural volumetric techniques enable efficient multi-node sampling patterns
- **Physics-Informed:** Approach can incorporate domain knowledge about plume physics
- **Real-time Capability:** Technology supports real-time processing for autonomous navigation and adaptive flight planning
- **Phase I Scope:** Limited to preliminary analysis and initial technology demonstration; full operational testing outcomes to be determined