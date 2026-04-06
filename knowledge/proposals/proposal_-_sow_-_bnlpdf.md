# Coordinated Drone-Based Plume Tracking

## Document Metadata
- Type: Statement of Work (SOW) - Phase I SBIR Proposal
- Client/Agency: Defense Threat Reduction Agency (DTRA), Department of Defense
- Program/Solicitation: DoD 2025.2 SBIR Program, FOA Number 2025.2
- Date: 2025-05-20 (submission date)
- BST Products/Systems Referenced: UAS (Unmanned Aerial Systems) with drone-mounted sensors
- Key Personnel: Gijs de Boer (Environmental Science and Technologies - BNL); Beck Cotter (last editor)

## Executive Summary
Black Swift Technologies, in partnership with Brookhaven National Laboratory (BNL), proposes to develop an automated plume tracking and reconstruction system that uses drone-mounted sensors combined with AI/ML techniques (specifically neural volumetric capture methods like neural radiance fields or gaussian splatting) to reconstruct the evolution of plumes emanating from a source area of interest. The Phase I effort will include software development, flight planning implementation, laboratory and flight testing at BNL, and culminate in an initial field test using BST's UAS.

## Technical Approach
- **Core Technology**: Neural volumetric capture, representation, and rendering techniques (neural radiance fields or gaussian splatting)
- **Data Source**: RGB imagery from drone-mounted cameras acquiring non-overlapping images
- **Method**: Use of neural networks to implicitly represent multidimensional volumes, enabling reconstruction of volumes from sparse measurements without stringent geometric or computational requirements of traditional photogrammetry
- **Integration**: Approach allows representation to be informed by multiple measurement types beyond RGB imagery and by governing physics
- **Implementation**: Combination of software development, flight planning optimization for multi-drone sampling to minimize uncertainty, laboratory testing, and local flight tests at BNL
- **Target Application**: Reconstruction and tracking of explosive test plumes
- **Testing Strategy**: Preliminary analysis through lab and local flight tests, leading to initial field test with BST-operated UAS

## Products & Capabilities Described

### Black Swift Technologies UAS
- Drone-mounted sensor platforms
- Equipped with cameras for imagery acquisition
- Capable of multi-node (coordinated multi-drone) operations
- Will be operationally deployed for field testing of the plume tracking system

## Use Cases & Applications
- **Explosive test plume tracking and reconstruction**: Primary application for tracking and characterizing plumes from explosive sources
- **Multi-drone coordinated sampling**: Capability to use multiple drones to optimize measurement coverage and minimize uncertainty
- **Defense/security applications**: DTRA-sponsored work suggests applicability to defense threat assessment and characterization

## Key Deliverables/Milestones
- Software development for neural volumetric capture implementation
- Flight planning algorithms for optimized drone coordination
- Laboratory testing and validation
- Local flight tests at BNL
- Initial field test using BST-operated UAS
- Interim and final reports, presentations, and required materials
- Team meeting participation and project execution support

## Notable Details
- **Partner Organization**: Brookhaven National Laboratory (BNL) providing expertise in AI/ML techniques and testing facilities
- **Technical Innovation**: Focus on emerging neural volumetric capture field (neural radiance fields and gaussian splatting), with recent developments enabling real-time analysis for navigation tasks
- **Advantage Over Traditional Methods**: Does not require stringent geometric constraints or cumbersome computational requirements of photogrammetry; accommodates multi-modal sensor inputs and physics-informed constraints
- **Real-time Capability**: Recent advances in the field enable real-time analysis suitable for dynamic navigation and adaptive sampling
- **Phase I Structure**: Focused on development, preliminary testing, and proof-of-concept validation prior to potential Phase II expansion