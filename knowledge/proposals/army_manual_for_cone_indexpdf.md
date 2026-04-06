# Army Manual for Cone Index

## Document Metadata
- **Type:** Technical Manual / Standard Operating Procedure
- **Client/Agency:** U.S. Army Engineer Research and Development Center (ERDC); Joint Program Office - Joint Light Tactical Vehicles (JPO-JLTV)
- **Program/Solicitation:** JLTV Vehicle Acquisition Support
- **Date:** August 2013
- **Report Number:** ERDC/GSL SR-13-2
- **BST Products/Systems Referenced:** None (this is a reference document for BST's AFWERX SBIR Phase I project on Soil Moisture Mapping)
- **Key Personnel:** Maria T. Stevens, Brent W. Towne, George L. Mason, Jody D. Priddy, Javier E. Osorio, Clint A. Barela (ERDC authors)

## Executive Summary

This ERDC technical report establishes standardized procedures for measuring Vehicle Cone Index (VCI1)—the minimum soil strength required for a vehicle to consistently complete one pass over soft terrain without immobilization. The procedures define site selection criteria, test lane layouts, soil data collection methods using cone penetrometers and remolding equipment, and analysis methodology. VCI1 is used as a vehicle performance metric for ground vehicle acquisition to quantify mobility on soft soils.

## Technical Approach

### VCI1 Measurement Methodology

**Vehicle Testing Procedures:**
- Vehicles operate in optimal off-road configuration (lowest gear, all-wheel-drive, locked differentials where available)
- Slow, steady speed (2-3 mph) through test lanes
- For zero-pass tests: vehicle driven until immobilized; reverse attempted to confirm no-go condition
- For multi-pass tests: vehicle makes forward and reverse passes in same tracks until immobilization occurs
- Typically 5-10 zero-pass tests and equal number of multi-pass tests required to establish VCI1

**Soil Strength Characterization:**
- Measured via **Rating Cone Index (RCI) = Cone Index (CI) × Remold Index (RI)**
- **Cone Index (CI):** Soil shear strength obtained using standardized trafficability cone penetrometer
  - 30° cone with 0.5 sq-in. base area
  - Standard 300 psi dial (0-300 psi range; 300 psi = 150 lb vertical force)
  - Optional 750 psi dial available for firmer soils
  - Penetration rate: ~0.1 ft/s
  - Minimum 20 measurements per lane (10 per side, with 6 minimum adjacent to immobilized vehicle)
  
- **Remold Index (RI):** Soil sensitivity to strength loss under traffic
  - Measured on soil samples from three depths: surface-6", 6-12", 12-18"
  - Hvorslev sampler collects undisturbed samples
  - Cone measurements taken at 0-4" depth in sample, then sample remolded with 100 drops of 2.5-lb hammer
  - RI = remolded strength / initial strength (minimum RI = 1.0 if remolded strength exceeds initial)

### Site Selection Criteria

Test lanes must meet strict requirements:
1. **Location:** Naturally occurring off-road areas; floodplains, swampy areas, seasonal lakebeds
2. **Soil Type:** High Plasticity Clay (CH) per USCS—worst-case fine-grained soil for vehicle mobility
   - Minimal sand content (< ~2% sand acceptable)
   - No visible sand grit feel during cone penetration
3. **Physical Characteristics:**
   - Flat, level terrain
   - Minimum 2 vehicle lengths long
   - Straight with uniform consistency
   - Free of rocks, logs, tree roots, debris
   - No prior ruts or disturbance; natural sedimentary shaping only
4. **Moisture:** Appropriate moisture for necessary strength range; no excess free surface water
5. **Soil Properties Documentation:**
   - USCS classification per ASTM standards
   - Natural moisture content and density for each 6" layer
   - Liquid limit (LL), plastic limit (PL), plasticity index (PI)
   - Sand and fines percentages

## Products & Capabilities Described

### Cone Penetrometer
- **What it is:** Standardized trafficability measurement device consisting of 30° cone, 18"-long rod (can be extended to 36"), proving ring, dial gage (0-300 psi or 0-750 psi), and handle
- **Use:** Direct measurement of soil shear strength (Cone Index) by forcing cone into ground at constant rate; stress indicated on dial indicates soil resistance
- **Specifications:** 0.5 sq-in. base area cone; 300 psi dial calibrated to 150 lb vertical force; penetration rate ~0.1 ft/s

### Remolding Equipment Kit
**Components:**
- Hvorslev sampler (piston sampler for undisturbed soil samples)
- 2.5-lb drop hammer with 12-inch drop
- Cylindrical remold tube and base plate
- Cone penetrometer (same as above)
- Wire saw for sample preparation
- Sample containers

**Use:** Measure soil sensitivity to traffic-induced strength loss by comparing undisturbed vs. remolded cone index values

## Use Cases & Applications

**Primary Use Case:** Ground vehicle acquisition support—determining if vehicles meet soft-soil mobility performance requirements

**Application Context:** 
- Specifically for fine-grained soils (CH clay being worst-case scenario)
- Off-road vehicle testing in soft-soil environments
- Vehicle comparison regardless of traction type (wheeled vs. tracked)
- Force projection and modeling/simulation development

**Referenced in BST's Context:** This document was retained as a reference for Black Swift Technologies' AFWERX SBIR Phase I proposal on Soil Moisture Mapping (Project X22.4), suggesting BST's soil moisture mapping capability may support or complement VCI testing operations.

## Key Findings & Standards

### Critical Layer Determination
- **Definition:** Soil layer exerting greatest influence on VCI1 performance (not necessarily where vehicle rests when immobilized)
- **Related to:** Critical depth of sinkage mobilizing stress within soil beneath center of running gear ground contact
- **Selection Method:** 
  - Analyze overlapping 6-inch layers at depths 0-6", 3-9", 6-12", 9-15", 12-18"
  - Select layer with best go/no-go separation and clearest upper-bound trend
  - Reference normal critical layers based on vehicle type (Table 3):
    - **Wheeled:** 3-9" (< 2000 lb wheel load); 6-12" (2000-15000 lb); 0-12" (> 15000 lb)
    - **Tracked:** 3-9" (< 4 psi contact pressure); 6-12" (< 100,000 lb); 0-12" (> 100,000 lb)

### Drop Layer Rule
- For test points where layer below critical layer is weaker, use the weaker soil strength
- Example: If 12-18" RCI < 6-12" RCI, use 12-18" value for analysis
- Significant impact on final VCI1 determination (example shows difference between VCI1 = 33 without rule vs. VCI1 = 29 with rule)

### Data Quality Standards
- **Cone Index:** 
  - Normal profiles uniform or uniformly increasing with depth preferred
  - Anomalies (hardpans, inconsistent layers) cause exclusion
  - Left/right wheel path comparison essential—significant differences (vehicle lean) may warrant exclusion
  - Individual measurement data typically noisy but valuable for trend analysis
  
- **Remold Index:**
  - CH soils unlikely to have RI < 0.5 per Collins (1971) analysis
  - RI values < 0.5 should be scrutinized against nearby measurements
  - Consistency checks across layers and neighboring lanes recommended

### VCI1 Analysis Rules
1. Remove suspect lanes (field observations and office analysis)
2. Use conservative RCI values (round up to next integer)
3. Use FM 5-430-00-1 (1994) critical layer unless superior correlation exists
4. Apply Drop Layer Rule
5. Scrutinize zero-pass lanes with RCI > 10-pass lane values
6. Define VCI1 as minimum of highest legitimate zero-pass RCI + 1

## Notable Details

### Historical Context
- VCI methodology originated with U.S. Army Corps of Engineers (USACE) in 1945 to address WWII mobility issues
- Procedures standardized within Corps for decades but not previously documented in centralized accessible format
- USACE has developed extensive VCI1 database over 5+ decades, predominantly focused on CH soil
- Five to ten test lanes typically required for reliable VCI1 determination despite sparse dataset considerations

### Soil Profile Considerations
- Vehicle sinkage proceeds through critical layer in normal soil profiles
- Standardized test conditions (straight lanes, level terrain, non-slippery conditions) ensure repeatability
- Testing on worst-case CH soil ensures vehicles can operate on any fine-grained soil type
- Sand content significantly skews results downward—even small percentages problematic

### Equipment Standardization
- All equipment calibrated to WES (Waterways Experiment Station) standards
- Cone penetrometer is primary trafficability measurement tool
- Remolding procedures standardized for consistent RI measurement
- Data collection forms standardized for consistent documentation

### Test Duration & Resource Requirements
- Typically 5-10 lanes of zero-pass and 5-10 lanes of multi-pass testing
- Field data collection requires trained operators for cone penetration and soil sampling
- Analysis phase benefits from rapid completion post-testing (for quality decisions on suspect data)
- Ideally hundreds of data points would define go/no-go boundaries, but sparse datasets (5-10 lanes per condition) have historically yielded consistent, predictable results over decades of USACE use

---

**Note:** This document serves as a foundational reference for soil mobility testing standards. It is stored in BST's AFWERX SBIR project files, indicating its relevance to soil characterization methodology supporting BST's proposed soil moisture mapping capabilities, which could potentially integrate with or complement vehicle mobility assessment operations.