# Earth UAS Aeroelastic Assessment

## Document Metadata
- Type: Executive summary / technical assessment report
- Client/Agency: Black Swift Technologies
- Program/Solicitation: NASA SBIR Phase II – Project 70068: Aeroelastic Parameter Study for a Venus Exploration Glider
- Date: August 2020
- BST Products/Systems Referenced: Earth UAS (baseline vehicle and glider variation)
- Key Personnel: Anthony Ricciardi, David Cloutier, Satya Ghoman (ATA Engineering); prepared for BST

## Executive Summary
ATA Engineering developed and analyzed aeroelastic models of two Earth UAS configurations—a baseline vehicle with onboard propulsion and a glider variant with a parametrized wing hinge—to assess flutter, divergence, maneuver response, buckling, and gust response. Results establish recommended hinge stiffness parameters and operational constraints for a Venus exploration glider derived from the Earth platform.

## Technical Approach

### Structural Modeling
- **Baseline FEM Development**: Modal test executed to measure Earth UAS wing modes; wing mesh created from CAD and correlated to test data via optimization of material and plate properties. Remaining aircraft FEM built from CAD geometry, material property data, and BST weight measurements.
- **Ruddervator Modeling**: Highly detailed tetrahedron model created to capture complex geometry; reduced using Hurty/Craig-Bampton method.
- **Mass & CG Verification**: Aircraft mass and center of gravity details verified against available data.

### Aerodynamic Modeling
Two aerodynamic models developed for comparison:
1. **ZAERO ZONA6-based panel model**: Higher geometric fidelity (captures wing thickness and camber); superior mesh convergence; higher computational cost.
2. **Nastran doublet lattice model**: Faster engineering workflow and run times; geometric approximations may produce slightly more conservative maneuver loads.
- Bend/torsion flutter onset speed predictions agreed within 1% between ZAERO and Nastran.
- Structural modes up to 200 Hz retained; velocities analyzed between 50–200 m/s; sea level density assumed; compressibility effects equivalent to Mach 0.441 prescribed.

### Flutter Analysis
- **Method**: Linear aeroelastic stability analysis using p-k method (Nastran) and g method (ZAERO); system eigenvalues assessed for stability.
- **Baseline Results**:
  - Classical bend/torsion flutter: onset at 107 m/s and 69 Hz (critical instability for hinge studies)
  - Nonclassical antisymmetric flutter: onset at 111 m/s at 114 Hz (less critical in glider configuration)
  - Symmetric and antisymmetric divergence modes predicted but less critical than bend/torsion flutter

### Maneuver Analysis
- **Aeroelastic Trim Method**: Trim solver selects control inputs (angle of attack, ruddervator rotation) to satisfy flight dynamic constraints: vertical acceleration = specified value (e.g., 3g); pitch acceleration = zero.
- **Approach**: Accounts for elastic deformations and inertia relief due to distributed mass; maneuver loads calculated by integrating stresses through three chordwise section cuts.
- **Scaling**: Reported loads can be linearly scaled by maneuver load factor.

### Hinge Parameter Study Configuration
- Baseline propulsion system mass retained as ballast, moved to fuselage centerline (to avoid geometric conflict with hinge).
- Forward spar: 6 inches removed to accommodate hinge.
- Aft spar: unchanged (no conflict).
- **Hinge Geometry**: 4-inch hinge section with 2-inch transition regions to stiffen adjacent skin; outboard transition adjacent to aileron.
- **Parametric Variation**: Hinge shell thickness varied; results reported as shell stiffness values (membrane and bending stiffness).

### Gust Response
- **Method**: Pratt method (FAA Part 23 certification standard) used to relate discrete gust response to equivalent maneuver load.
- **Assumptions**: 1-cosine gust profile with 25-chord wavelength; sea level density.
- **Key Finding**: Earth UAS exhibits extremely low wing loading, causing considerable responsiveness to turbulence; fair-weather operations recommended.

## Products & Capabilities Described

### Earth UAS
- **Baseline Configuration**: Fixed-wing UAS with onboard propulsion system; high aspect ratio, low wing loading (~0.4 psf inferred from sensitivity to gusts).
- **Glider Configuration**: Variant with parametrized wing hinge replacing propulsion; enables folding or variable wing stiffness for Venus exploration mission.
- **Wing Specifications**: 54.3-inch span; highly detailed geometry including ruddervator (combined rudder/elevator) control surface.
- **Flutter Characteristics**: Baseline aircraft shows classical bend/torsion flutter onset at 107 m/s; critically sensitive to aileron servo stiffness (not ruddervator servo stiffness).

## Use Cases & Applications

**Primary Mission Context**: Venus Exploration Glider
- Earth UAS serves as atmospheric sampling/sensing platform for Earth; aeroelastic analysis supports design of Venus-adapted glider variant.
- Glider would operate in Venus atmosphere (denser, higher temperatures) where flutter dynamics differ from Earth baseline; Earth-based aeroelastic assessment informs Venus design constraints.

**Analysis Applications**:
- Flutter and divergence prediction at various altitudes/densities
- Maneuver load envelope definition for control authority
- Structural dynamic response to atmospheric gusts and turbulence
- Hinge mechanism design validation (stiffness, buckling limits)

## Key Results

### Flutter Stability vs Hinge Stiffness
- **Critical Finding**: Bend/torsion flutter remains controlling instability across hinge stiffness range studied.
- **Membrane Stiffness Limit**: Below 4.8E4 lb/in, stability trends deteriorate due to excessive flexibility; **4.8E4 lb/in recommended minimum** for flutter margin.
- **Upper Limit**: No upper stiffness limit recommended for flutter stability; slight flutter speed decrease observed as wing-bending mode frequency shifts closer to wing-pitch mode, but not concerning.
- **Divergence**: Symmetric and antisymmetric divergence predicted but remain less critical than flutter for all cases.

### Servo Stiffness Sensitivity
- **Ruddervator Servo**: Negligible effect on bend/torsion flutter response.
- **Aileron Servo**: Flutter speed increases with increasing aileron servo stiffness; critical parameter.
  - Recommended value: 1e3 lb/in (corresponds to 90 Hz uncoupled rigid-body aileron-rotation modal frequency).
  - **Action Item**: Flutter should be reassessed if observed aileron modal frequencies drop below 90 Hz.

### Maneuver Loads in Hinge
- **Insensitivity to Hinge Flexibility**: Trimmed maneuver loads insensitive to hinge flexibility across stiffness range 9.7E3 lb/in < membrane stiffness < 3.9E5 lb/in.
- **Velocity Independence**: Maneuver loads remain proportional to trimmed load factor; insensitive to velocity within current modeling approach.
- **Design Input**: Tabulated hinge loads provided in attached PowerPoint slides for subsequent hinge design.

### Wing Tip Displacement
- **Recommended Hinge Stiffness**: ≥ 7E4 lb/in membrane stiffness to keep displacements reasonable.
- **Scaling**: Reported as %span per g; can be dimensionalized by multiplying by 54.3-inch span and maneuver load factor.
- **Velocity Independence**: Displacements remain proportional to load factor within current modeling.

### Maneuver Load Buckling
- **Analysis Method**: Simplified static boundary conditions derived to be statically equivalent to 1g trimmed maneuver.
- **Recommended Hinge Bending Stiffness**: ≥ 3 lb·in for shell bending stiffness (I/12) at 10g pull-up load factor (without 50% knockdown factor or safety factor applied).
  - **Note**: Result is material and geometry dependent; requires refinement as part of detailed hinge design process.
- **Pull-up vs Push-over**: Both load cases analyzed and plotted; pull-up typically more limiting.

### Gust Response
- **Pratt Method Results**: Earth UAS exhibits extreme sensitivity to atmospheric gusts due to very low wing loading.
- **Operational Constraint**: Fair-weather operations recommended; aircraft unsuitable for moderate turbulence or bad-weather flight.
- **Altitude Effect**: Gust loads reduce at higher altitudes (sea level density assumed in baseline analysis).

## Notable Details

### Analysis Rigor & Validation
- **Model Correlation**: Finite element model correlated to measured wing modal test data; high confidence in structural dynamic representation.
- **Solver Cross-Check**: ZAERO and Nastran results compared and agreed within 1% on critical flutter onset speed, validating aerodynamic modeling approach.
- **Conservative Estimates**: Nastran maneuver loads expected to be slightly more conservative due to geometric approximations shifting aerodynamic lift distribution outboard.

### Venus Mission Context
- Earth UAS serves as proof-of-concept platform; glider configuration designed to operate in Venus atmosphere.
- Aeroelastic analysis on Earth baseline provides foundational design data; Venus vehicle will require re-analysis at different air density (Venus atmosphere ~90x Earth sea level).
- Hinge mechanism is key technology enabler for Venus mission (enables wing folding or stiffness modulation).

### Design Recommendations Hierarchy
1. **Flutter Stability** (primary): Membrane stiffness ≥ 4.8E4 lb/in; aileron servo stiffness monitoring at 90 Hz threshold.
2. **Wing Tip Displacement** (secondary): Membrane stiffness ≥ 7E4 lb/in for dimensional control.
3. **Buckling Resistance** (tertiary): Bending stiffness I/12 ≥ 3 lb·in as starting point; requires material-specific refinement.
4. **Operational Limits**: Fair-weather only; not suitable for moderate turbulence.

### Open Items
- Detailed hinge design and buckling analysis recommended as follow-on work, using tabulated maneuver loads provided.
- Flutter reassessment required if aileron modal frequency design changes.
- Venus-adapted vehicle will require aeroelastic re-analysis at Venus atmospheric density.