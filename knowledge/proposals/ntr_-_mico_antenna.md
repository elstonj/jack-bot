# NTR - MiCo Antenna

## Document Metadata
- Type: New Technology Report (NTR)
- Client/Agency: NASA Goddard Space Flight Center
- Program/Solicitation: NASA 2012 SBIR Phase II - Soil Moisture Mapping sUAS (WBS 939869.03.06.02, S3.05-8971)
- Date: Submitted July 22, 2014 (modified April 7, 2016)
- Contract Number: NNX14CG09C (primary), NNX13CG33P
- BST Products/Systems Referenced: sUAS (soil moisture mapping small unmanned aircraft system)
- Key Personnel: Jack Elston (BST Tech Rep); Albin Gasiewski, Eryan Dai, Eric McIntyre (University of Colorado innovators)

## Executive Summary
Black Swift Technologies, in collaboration with University of Colorado, developed the Microstrip Colinear (MiCo) antenna array—a lightweight, compact L-band antenna specifically designed for integration into a small unmanned aircraft system (sUAS) for soil moisture mapping. The antenna connects with the Lobe Differencing Correlating Radiometer (LDCR) to enable high-resolution soil moisture sensing at 15-meter resolution, substantially improving upon the 40-km resolution of NASA's SMAP satellite.

## Technical Approach

**Antenna Design Specifications:**
- Configuration: 2x2 rectangular microstrip colinear antenna array (prototype tested as 2x1)
- Operating frequency: 1.4135 GHz (SMAP allocated band: 1400-1427 MHz)
- Each element: 5-segment microstrip colinear patch antenna with omnidirectional radiation pattern
- Element spacing: Half-wave horizontal, quarter-wave vertical separations
- Radiation characteristics: Quarter-wave vertical separation provides 90° phase shift for quadrature-phased LDCR receiver channels
- Beam pattern: Broad end-fire beams in nadir and zenith directions with horizon cancellation
- Probe depth: ~5-10 cm into soil under most conditions

**Design Methodology:**
- Used HFSS simulation software for impedance and radiation pattern analysis
- Validated prototype 2x1 array measurements against simulation results
- Investigated 2x2 array configuration variations: upper/lower pair separation, orientation effects on mutual coupling, resonant frequency, and radiometer sensitivity
- Employed styrofoam blocks for mechanical stability and resonant frequency tuning
- Identified optimal vertical separation distance minimizing mutual coupling and maximizing main-to-back lobe ratio

**Key Design Drivers:**
- Minimize weight and volume for sUAS integration
- Low-cost PCB-based manufacturing for scalability
- Provide adequate antenna pattern for LDCR radiometer

## Products & Capabilities Described

**Soil Moisture Mapping sUAS**
- Purpose: Passive microwave remote sensing system for soil moisture measurement
- Measurement resolution: 15 meters (vs. 40 km for SMAP satellite)
- Applications: SMAP validation, resolution augmentation, FEMA flood risk assessment
- Soil penetration depth: 5-10 cm

**MiCo Antenna**
- Compact L-band antenna array for sUAS integration
- Lightweight, low-cost construction on PCB
- Provides broad-beam radiometer pattern with nadir and zenith viewing lobes
- Directly connects to LDCR (Lobe Differencing Correlating Radiometer)

**LDCR (Lobe Differencing Correlating Radiometer)**
- Lightweight broad-beam radiometer developed to pair with MiCo antenna
- Quadrature-phased receiver channels (driven by antenna's 90° phase shift)

## Use Cases & Applications

1. **SMAP Mission Support:** Validation of SMAP satellite data and provision of finer-resolution soil moisture measurements in selected areas
2. **Drought Monitoring:** High-resolution soil moisture mapping in drought-affected regions
3. **Flood Prediction:** Support FEMA in flash flood vulnerability assessment; demonstrated use in 2007 North Texas/Oklahoma flood mapping
4. **Watershed Monitoring:** Augment SMAP science data products with 15-meter resolution data near watersheds
5. **Calibration & Validation:** Extensive cal/val data collection for SMAP spacecraft missions (pre- and post-launch)

## Development Timeline

- **November 3, 2013:** Initial concept design completed and simulated
- **May 4, 2014:** Refined design and simulations incorporating aircraft fuselage
- **July 1, 2014:** Initial build and lab test of antenna array
- **October 4, 2014:** Antenna integration with fuselage, testing, and tuning
- **April 1, 2015:** Outdoor testing of MiCo antenna fully integrated into airframe
- **September 8, 2015:** First flight test over instrumented field (Canton, OK)

## Key Results

**State of Development:** Prototype built and operational; used in current work

**First Disclosures & Testing:**
- Initial concept and design disclosed at AGU (American Geophysical Union) conference, San Francisco, December 2013 (poster presentation)
- Successful operational test conducted September 2015 in Canton, OK
- Presented at National Radio Science Meeting, January 8, 2016

**Technical Validation:**
- Prototype 2x1 array measurements confirmed HFSS simulation accuracy
- Identified optimal vertical separation distance for mutual coupling minimization
- Validated antenna resonant frequency tuning methods
- Demonstrated pattern performance in outdoor/flight conditions

## Notable Details

**Unique Features:**
- Antenna specifically dimensioned to fit sUAS constraints while maintaining adequate radiation pattern
- PCB-based construction enables rapid manufacturing at scale
- Quarter-wave vertical separation design elegantly provides both mechanical spacing and required 90° phase shift for quadrature receiver channels
- Achieves 15-meter resolution vs. 40-km satellite resolution—enabling hyper-local validation and science augmentation

**Competitive Advantages:**
- Enables cost-effective sUAS deployment for soil moisture mapping (fraction of manned aircraft cost)
- Substantially improved resolution over satellite observations
- Low-cost, manufacturable design suitable for production
- Addresses both NASA science objectives and operational emergency response (FEMA flood warnings)

**Technology Readiness:** Substantial Advancement in the Art (per NASA classification); prototype stage with successful flight testing

**Patent Status:** No patents listed; technology appears to remain unpatented as of NTR submission

**Innovator Contributions:**
- Albin Gasiewski (University of Colorado): Overall design leadership
- Eryan Dai (University of Colorado): Detailed design, simulation, construction, testing
- Eric McIntyre (University of Colorado): Initial colinear antenna design