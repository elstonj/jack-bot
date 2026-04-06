# Black Swift Folding Wing Analytical Study

## Document Metadata
- Type: Technical analysis report / subcontractor deliverable
- Client/Agency: NASA
- Program/Solicitation: 2018 SBIR Phase II (Venus)
- Date: Created 2021-03-01; Modified 2021-08-13
- BST Products/Systems Referenced: Folding wing UAV
- Key Personnel: Jack Elston (last editor)
- Subcontractors: ATA (system analysis), Roccor (wing development)

## Executive Summary
ATA performed system analyses under subcontract to Black Swift to generate requirements and performance goals for Roccor's development of a foldable UAV wing. The study includes composite laminate design recommendations, finite element analysis of the wing hinge, and sensitivity studies on laminate architecture and hinge geometry to achieve approximately 10g pull-up load capability for a Venus mission UAV.

## Technical Approach

### Hinge Requirements (ATA Recommendations)
- Hinge shell membrane stiffness ET ≥4.8E4 lb/in for flutter stability
- Hinge shell membrane stiffness ET ≥7E4 lb/in to keep tip displacements reasonable
- Hinge shell bending stiffness ET³/12 ≥3 lb-in for buckling stability
- Tabulated hinge loads to be used for subsequent hinge design

### Composite Laminate Design
Two materials surveyed by Roccor:
- **UD**: Unidirectional IM7 fibers with toughened high-Tg epoxy matrix, 55 gsm, 37% resin content
- **PW**: Plain weave M30S fiber with toughened high-Tg epoxy matrix, 60 gsm, 37% resin content

**Baseline laminate architecture**: [±45° PW/±45° PW/0° UD/0° UD/0° UD/0° UD/±45° PW/±45° PW]
- 8-ply laminate
- Total thickness: 0.0189 inch
- Target pull-up load: ~10g

### Strain Analysis
Maximum surface strain evaluated at various bend radii. All strain values kept below 1% (standard for carbon fiber composites). Minimum bend radius of 1.5 inches recommended for this laminate.

### Finite Element Analysis (FEA)
- **Software**: ABAQUS
- **Element type**: Conventional shell elements (S4R)
- **Geometry**: Wing hinge section with reference points (RPs) at inboard and outboard cut faces
- **Worst case 1g loads** (from ATA) applied at outboard location:
  - Z = 1.156 lb
  - My = 0.338 in-lb
  - Mx = 12.273 in-lb

## Products & Capabilities Described

### Folding Wing UAV
- **Purpose**: Venus atmospheric entry/descent vehicle for NASA
- **Key feature**: Foldable composite wing to reduce deployed size for entry
- **Design target**: 10g pull-up capability during atmospheric operations

## Use Cases & Applications
- **Venus Atmosphere Exploration**: Folding wing enables compact entry configuration with in-flight deployment capability
- **Aerodynamic maneuverability**: Design ensures 10g pull-up load rating for atmospheric flight operations

## Key Results

### Baseline Laminate Performance
- First eigenvalue (buckling): **9.884g** (~9.9g pull-up factor)
- Shell membrane stiffnesses calculated as adequate
- Shell bending stiffness in y-axis below recommendation but verified acceptable via FEA

### Laminate Architecture Sensitivity Study
Three alternative designs evaluated (varying 0° IM7 plies from baseline 4):
- **3 plies (UD)**: Buckles at ~7.4g (does **not meet** 10g requirement)
- **4 plies (baseline)**: Buckles at ~9.9g (marginal)
- **5 plies (UD)**: Buckles at ~12.8g (meets and exceeds 10g target) — **recommended for further study**

### Hinge Length Sensitivity Study
Evaluated 2.5", 3.0" (baseline), and 3.5" slit lengths at leading edge:
- Small impact on buckling performance
- Recommendation: optimize hinge length to minimize while maintaining foldability

### Trailing Edge Slit Analysis
Addition of trailing edge slit corresponding to leading edge slit location:
- First eigenvalue: 9.83g (vs. 9.88g baseline)
- Minimal impact on buckling load
- Small benefit to wing foldability

## Notable Details
- Study addresses key trade space for deployable structures: foldability vs. structural performance
- Composite strain management critical for high-strain composite (HSC) foldable designs
- Multiple sensitivity studies provide design margin guidance for Roccor's iterative development
- Five 0° ply laminate recommended as best candidate for meeting 10g requirement with improved margin
- Analysis demonstrates feasibility of composite folding wings for planetary science missions
- Document part of larger NASA SBIR Phase II effort on Venus exploration systems