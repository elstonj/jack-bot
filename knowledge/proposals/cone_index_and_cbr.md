# Cone Index and California Bearing Ratio

## Document Metadata
- Type: Technical reference paper / academic article
- Client/Agency: U.S. Army Engineer Research and Development Center (ERDC); U.S. Air Force; U.S. Army Corps of Engineers
- Program/Solicitation: Joint Rapid Airfield Construction Program; Opportune Landing Site Program
- Date: ~2006–2007 (based on references and context; created in BST system 2023-10-23)
- BST Products/Systems Referenced: None directly—document is a reference material for AFWERX SBIR Phase I Soil Moisture Mapping project
- Key Personnel: George L. Mason, Ph.D., P.E. (ERDC); E. Alex Baylot, P.E. (ERDC)

## Executive Summary
This technical paper reviews the relationship between soil moisture content and soil strength parameters—specifically Cone Index (CI), Rating Cone Index (RCI), and California Bearing Ratio (CBR)—used to predict vehicle trafficability and expedient airfield/construction site selection. The paper presents empirical equations and field data correlations developed by ERDC to enable prediction of soil bearing capacity and mobility under varying moisture and soil type conditions.

## Technical Approach

### Soil Strength Measurement Methods
- **Cone Index (CI)**: Penetration resistance (pounds) measured by a 30° apex cone with 0.5 in² base area; vertical force divided by sleeve surface area.
- **Rating Cone Index (RCI)**: Modified CI accounting for soil remolding via drop hammer test (100 blows of 2.5 lb hammer falling 12 inches). RCI = CI × Remolding Index (RI).
- **California Bearing Ratio (CBR)**: Load ratio (%) to cause 0.1-inch penetration in test sample vs. standard crushed-stone reference; uses 3-square-inch cylindrical plunger. Primary use: flexible pavement and runway design.

### Mathematical Models
**Equation 1 (CI vs. moisture):**  
CI = a × exp(b × mg)  
where mg = percent moisture by weight, a and b = USCS soil-type coefficients

**Equation 3 (RCI vs. moisture):**  
RCI = a′ × exp(b′ × mg)  
where a′, b′ = coefficients modified for remolded soil

**Equations 6 & 7 (CBR correlations from 2004+ field data):**  
- Equation 6: Logarithmic form, CBR = a × ln(mg) + b
- Equation 7: Power form, CBR = a′ × (RCI)^b′  
Better linear/near-linear fit; accounts for USCS soil type groupings

### Data Foundation
- ERDC compilation of field data (2004 onwards) from 1948–present: **14,000+ records** including geospatial coordinates, soil type (USCS), gravimetric moisture, specific gravity, dry density, CI, RCI, CBR.
- Usable dataset for regression: **209 records** with simultaneous mg, RCI, and CBR values.
- USCS soil types analyzed: CH, MH, CL, ML, SC, GC, SM, SP, and grouped categories.

### Key Moisture-Strength Relationships
- **Inverse relationship**: Soil strength decreases with increasing moisture content.
- **Immobilization threshold**: RCI ≤ 40 indicates high probability of vehicle immobilization.
- **Liquid limit boundary**: As soil moisture approaches liquid limit, immobilization risk increases sharply.
- **Saturation effects**: Surface saturation (≥0.25 inch rain in 15 minutes) causes >50% traction loss; slippery conditions defined as RCI ≤ 50 for top 1 cm in fine-grain soils.

### Temporal/Spatial Modeling
- **Water budget model** (Figure 3) uses finite-difference approach: Q (flow through layer) = R (runoff) − E (evaporation)
- **NRMMII (NATO Reference Mobility Model II)** employed for vehicle speed/trafficability forecasting under varying moisture and weather scenarios.
- Soil properties affecting water migration: permeability, tension, tortuosity, pore connectivity, compaction state.

## Products & Capabilities Described

### NATO Reference Mobility Model II (NRMMII)
- Sub-models describe temporal and spatial soil strength changes as function of weather and soil properties.
- Used to define opportune landing zones and forecast mobility under different precipitation/evaporation scenarios.
- Example: Philippines island scenario (Figure 2) shows 50–70% speed variation based on soil moisture state (Wet-Slippery vs. Normal conditions).

### Soil Moisture-Strength Prediction Model (SMSP / SMSP II)
- Generalized model using Equations 1 and 3 with USCS coefficients (Table 1).
- Correlates moisture to CI/RCI for forecasting seasonal mobility.
- Employed in Short-Term Operational Forecasts of Trafficability (SOFT).

### Soil Type Classification Framework
- **Fine-grain groupings**: (a) SC, GC; (b) CH, MH, OH; (c) ML, ML-CL, CL, OL
- **Coarse-grain groupings**: (d) SM, SM-SC, GM, GM-GC; (e) SP, SW, GP, GW
- **Special**: (f) Pt (peat); (g) rock
- Grouping strategy allows unified parameter treatment in NRMMII simulations.

## Use Cases & Applications

### Military Off-Road Mobility
- Prediction of vehicle trafficability for wheeled and tracked vehicles (e.g., Marine Corps, Army ground mobility).
- Speed forecasting under varying weather/soil conditions.
- Off-road route planning during poor weather (high-moisture periods).

### Expedient Airfield Construction
- Evaluation of surface and subsurface bearing capacity for landing zone selection.
- Design of rapidly deployable runway pavement thickness based on CBR.
- Support for Joint Rapid Airfield Construction Program operations.

### Opportune Landing Site Selection
- Real-time assessment of landing zones under dynamic weather conditions.
- Identification of slippery/immobile regions during precipitation events.
- Geospatial forecasting to support tactical decision-making.

### Pavement & Foundation Design
- CBR used since 1940s for flexible pavement design (roads, airfields, runways).
- Correlation to RCI/CI enables rapid in-situ strength estimation for expedient construction.

## Key Results

### Empirical Correlations (Table 2, Field Data)

**CI vs. Moisture (R² values):**
- **CL (Clay, Low plasticity)**: R² = 0.908 (logarithmic fit); practical CBR range 5–15
- **ML (Silt, Low plasticity)**: R² = 0.985 (6 samples, use with caution)
- **CH (Clay, High plasticity)**: R² = 0.919 (non-linear); practical CBR range 3–5
- **MH (Silt, High plasticity)**: R² = 0.737 (linear fit)
- **CL + ML (combined)**: R² = 0.914 (linear); CBR 5–15
- **CH + MH (combined)**: R² = 0.874 (non-linear); CBR 3–8
- **All fine-grain soils**: R² = 0.738; CBR 3–15

**RCI vs. CBR (Linear relationship):**
- Fine-grain soils (CL, ML, CH, MH): **Average ratio CBR:RCI = 1:56**
- Individual soil types or selected groupings provide better practical estimation than lumped "all" category.

### Soil Type Performance Patterns
- **High-plasticity clays (CH)**: Non-linear response to moisture; narrower CBR range (3–5); steeper strength loss near liquid limit.
- **Low-plasticity silts/clays (CL, ML)**: Linear or near-linear response; broader CBR range (5–15); more gradual strength degradation.
- **Medium-plasticity silts (MH)**: Intermediate behavior; R² = 0.737 (moderate fit quality).

### Physical Property Correlations
Soil strength correlates with:
- Density (dry unit weight γd)
- Volume of water (Vw) and saturation state
- Liquid/plastic limits (Atterberg properties)
- Percent fines and clay content
- Permeability and soil water tension
- Compaction/void ratio (surface compaction → early saturation, reduced pore space)

### Prediction Accuracy
- Spread in field data is broad; R² values for CBR vs. moisture range 0.51–0.99, indicating high variability.
- Better fits achieved for grouped soil types vs. individual types.
- CL + ML grouping most reliable for practical CBR estimation (R² ≥ 0.91).

## Notable Details

### Data Maturity
- Largest compilation of U.S. Army soil strength field data: 14,000+ records spanning 56 years (1948–2004+).
- Supports Opportune Landing Site and Joint Rapid Airfield Construction programs.
- Enables validation of NRMMII and SMSP models under diverse terrain/climate conditions.

### Technical Innovations
- Remolding Index (RI) concept: captures effect of vehicle traffic/soil compaction on strength, differentiating dynamic field conditions from static measurements.
- Finite-difference water budget approach: models temporal soil moisture migration via precipitation, evaporation, runoff, and subsurface flow.
- **Coefficient of variation errors in measurement**: 40% for cohesion, 12% for friction angle, 30% for compression index—acknowledges measurement device and strain-rate sensitivity.

### Methodological Insights
- CBR-RCI relationship is fairly linear, enabling inference of CBR from cheaper/faster cone penetrometer tests (CI/RCI).
- Non-linear moisture-strength curves in high-plasticity soils (CH, MH) indicate threshold behavior near liquid limit—critical for predicting immobilization risk.
- Surface compaction reduces void ratio, causing early saturation with reduced penetration resistance change but significant traction loss.

### Relevance to Soil Moisture Mapping (SMM)
Document stored in BST's AFWERX SBIR Phase I Soil Moisture Mapping project folder, indicating its use as reference material for correlating remote/proximal soil moisture measurements to trafficability and bearing capacity—supporting tactical decision-making for landing zone evaluation and off-road mobility forecasting.

---

**Note**: This is a technical reference paper, not a BST original work. It is compiled from ERDC research and serves as foundational literature for BST's soil moisture mapping SBIR project to enable correlation of moisture data to trafficability metrics.