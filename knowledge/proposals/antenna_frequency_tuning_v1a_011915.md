# Antenna Frequency Tuning v1a

## Document Metadata
- Type: Technical report / research paper
- Client/Agency: NASA (SBIR Phase II)
- Program/Solicitation: 2012 SBIR, Soil Moisture topic
- Date: January 19, 2015
- BST Products/Systems Referenced: MiCo Antenna (Microstrip Colinear Antenna Array)
- Key Personnel: Eryan Dai, A.J. Gasiewski (University of Colorado at Boulder), Maciej Stachura (Black Swift Technologies)

## Executive Summary
This technical report presents a method for tuning the resonant frequency of MiCo antenna arrays using dielectric tuning pieces. The study uses HFSS simulation to quantify how the dimensions (width, thickness) and dielectric constant of tuning pieces influence frequency shift, developing an analytical model to predict frequency tuning with adjustable parameters.

## Technical Approach
The approach uses dielectric pieces placed over a MiCo antenna to modify the effective dielectric constant of the upper area above the microstrip line. The analysis:
1. Develops equations for effective dielectric constant of the antenna with and without tuning pieces
2. Derives relationship between dielectric constant change and resonant frequency shift
3. Parameterizes frequency shift as linear function of tuning piece properties: width (W), thickness (T), and dielectric constant (εr)
4. Uses HFSS electromagnetic simulation to validate analytical model and determine coefficients

**Key Formula:** Shifted frequency = K × (A×W + B×T) × (εr - 1), where:
- K relates to antenna/substrate parameters
- A = 0.86 (width influence coefficient)
- B = 0.431 (thickness influence coefficient)
- Maximum effective tuning thickness: 2.4mm (saturation point)

## Products & Capabilities Described

### MiCo Antenna (Microstrip Colinear Antenna Array)
- **What it is:** A microstrip antenna array with multiple apertures along the Y-axis
- **Key specifications:**
  - Substrate dielectric constant: 3.55
  - Effective dielectric constant (untuned): 3.05
  - Substrate thickness: 1.524 mm
  - Microstrip line width: 14 mm
  - Baseline resonant frequency: ~1.4230 GHz (L-band, consistent with soil moisture radiometry)
- **Tuning capability:** Frequency can be shifted by placement of dielectric tuning pieces

## Use Cases & Applications
- **Lobe Differential Correlation Radiometer (LDCR):** Referenced as primary application; consistent with soil moisture remote sensing missions
- The frequency tuning capability enables optimization of antenna performance for specific mission frequencies

## Key Results
1. **Simulation validation:** HFSS simulations confirmed linear relationship between tuning piece properties and frequency shift
2. **Practical performance:** 
   - Theoretical prediction: 14 MHz frequency shift
   - Measured result: 11 MHz frequency shift (3 MHz error margin)
   - Test configuration: Dow Corning 3140 RTV coating (εr = 2.52), 2mm width × 290mm length × 0.7mm thickness
   - Frequency shift measured: 1.4230 GHz → 1.4119 GHz

## Notable Details
- Material used: Dow Corning 3140 RTV coating (dielectric constant 2.52), a practical off-the-shelf material
- The analytical model provides predictive capability for antenna designers to achieve target resonant frequencies through tuning piece design
- Saturation phenomenon observed: frequency shift plateaus when tuning piece thickness exceeds 2.4mm
- This work appears part of larger NASA SBIR Phase II soil moisture remote sensing project
- Collaboration between University of Colorado and Black Swift Technologies indicates academic-industry partnership