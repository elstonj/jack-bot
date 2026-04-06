# Aeroelastic Parameter Study for a Venus Exploration Glider

## Document Metadata
- Type: Engineering services proposal
- Client/Agency: Black Swift Technologies (BST)
- Program/Solicitation: NASA SBIR Phase II (Venus exploration UAS)
- Date: March 3, 2020
- BST Products/Systems Referenced: Venus UAS (unpowered), Earth demonstration UAS
- Key Personnel: Jack Elston (BST contact); Eric Parker-Martin, Anthony Ricciardi, Sam Dyas, Elliot Haag (ATA)

## Executive Summary
ATA Engineering proposes a comprehensive aeroelastic analysis and parameter study for Black Swift Technologies' NASA SBIR Phase II effort to develop an unpowered UAS capable of operating in Venus's upper atmosphere via dynamic soaring. The work includes finite element modeling, flutter analysis, and hinge stiffness optimization studies for both a Venus-bound aircraft and an Earth demonstration vehicle, with emphasis on characterizing aeroelastic behavior under Venusian atmospheric conditions and establishing wing-fold hinge design requirements.

## Technical Approach

**Overall Strategy:**
- Develop structural finite element models (FEMs) and panel method aerodynamic models for both Venus and Earth UAS
- Perform baseline aeroelastic analyses (flutter, divergence, loads) assuming perfect hinges
- Execute parametric stiffness studies on wing-fold hinges to establish acceptable design space
- Deliver insights into aeroelastic drivers specific to Venusian flight conditions

**Tools & Methods:**
- Structural modeling: 1-D beam or 2-D shell FEM in Nastran format
- Aerodynamic modeling: Panel method using Nastran doublet lattice or ZAERO ZONA6
- Flutter analysis: Computationally efficient subsonic panel methods; CFD-based time-domain techniques when needed
- Nonlinear analysis capability: CFD-FEM co-simulation using Loci/CHEM, FUN3D, STAR-CCM+, and Abaqus

**Key Technical Insight:**
Document highlights unique aeroelastic challenges of Venusian flight: dramatically lower stall speeds (~6.5 knots vs. 50 knots for Cessna at Venus surface) create unusually high reduced frequencies for structural modes and potential for counterintuitive aeroelastic phenomena. Combined with folding wing hinges, this necessitates detailed parametric analysis.

## Products & Capabilities Described

**Venus UAS:**
- Unpowered unmanned aerial system designed for extended flight in Venus upper atmosphere
- Operates via dynamic soaring (extracting energy from wind shear layers)
- Features folding wing with hinged joints to accommodate launch/deployment constraints
- Intended for scientific measurements

**Earth Demonstration UAS:**
- Technology demonstration platform for Venus design
- Similar aeroelastic analysis requirements
- Serves as validation/testing vehicle for Venus concepts

**ATA's Capabilities Applied:**
- 40+ years of aerospace analysis and testing experience
- Expertise in flutter analysis, ground vibration testing (GVT), finite element modeling, and aircraft dynamics
- Specific precedent: Led all aeroelastic work for Airbus Perlan 2 glider (which reached 76,000 ft in 2018), including ground vibration testing
- Subsonic through hypersonic aeroelastic analysis experience
- CFD-based computational aeroelasticity for nonlinear flow regimes

## Use Cases & Applications

**Primary Mission:**
- Scientific measurements in Venus upper atmosphere via long-endurance dynamic soaring flight

**Design Challenges Addressed:**
1. Aeroelastic stability assessment under Venusian atmospheric conditions (pressure, density, speed of sound, turbulence profiles)
2. Wing-fold hinge design optimization for both flight regimes
3. Flutter and divergence onset speed characterization
4. Dynamic load assessment (root bending moment, shear, hinge loads)
5. Comparison of baseline continuous-wing performance vs. hinged configurations

## Scope of Work (8 Tasks)

1. **Earth UAS Model Development** – Structural FEM and panel aerodynamic model
2. **Earth UAS Baseline Aeroelastic Analyses** – Flutter, trim, gust loads for limited flight conditions
3. **Earth UAS Hinge Parameter Study** – Parametric variation of hinge stiffness (5 values assumed) to bound design space
4. **Venus UAS FEM Development** – Structural and aerodynamic models from CAD geometry
5. **Venus UAS Baseline Aeroelastic Analyses** – Flutter, loads analysis tailored to Venusian atmosphere; identifies design drivers
6. **Venus UAS Hinge Parameter Study** – Hinge stiffness parametric exploration for Venus vehicle
7. **Program Management & Meeting Support** – Weekly teleconferences, status presentations, project management
8. **Final Report** – Documentation of methods, results, recommendations for detailed design phase

**Key Tracked Parameters:**
- Flutter onset speed and frequency
- Flutter mode shapes
- Divergence onset speed and mode shapes
- Peak root bending moment and shear
- Hinge loads
- Relative changes from baseline aircraft

## Notable Details

**Relevant Precedent:**
- ATA's Perlan 2 engagement is explicitly positioned as the most relevant experience: high-altitude glider with similar design constraints (long wingspan, flutter risk, dynamic soaring), requiring ground vibration testing and aeroelastic characterization—direct analog to BST's Venus vehicle concept.

**Contractual & Commercial Terms:**
- Fixed-price proposal: **$119,830**
- Delivery: 14 weeks for analysis tasks (Tasks 1–6) plus 2 weeks for final report from receipt of purchase order and all data
- Invoice: Monthly based on progress, net 30 days
- Validity: Until June 30, 2020
- ATA retains right to use similar techniques for other clients (non-proprietary know-how)

**Key Assumptions:**
- Hinge parameter studies assume stiffness as primary variable; span-wise position and rotation axis fixed per initial scope
- Five hinge stiffness values per parametric study
- BST provides timely delivery of CAD geometry, airfoil data, mass properties, and flight envelope definitions
- Scope is fixed; out-of-scope requests require change order

**Dependencies:**
- Requires fully defined CAD models of both Venus and Earth UAS from BST
- Requires flight envelope, atmospheric data (Venus standard atmosphere), and hinge location/axis definitions
- Success dependent on timely delivery of receivables from BST

## Competitive Positioning

ATA emphasizes its unique qualification through:
1. **Deep aeroelastic expertise** – 40+ years, subsonic through hypersonic regimes
2. **Perlan 2 precedent** – Direct experience with high-altitude, long-span, flutter-sensitive glider design and testing
3. **Integrated modeling capability** – FEM-to-flight test pipeline including GVT correlation
4. **Venusian physics insight** – Explicit recognition of unique atmospheric/dynamic conditions and their aeroelastic implications

---

**Note:** This document is ATA's proposal to BST; it is not a BST internal or marketing document. It demonstrates how ATA positioned itself as the specialized partner for a critical technical challenge in BST's NASA SBIR Phase II Venus program.