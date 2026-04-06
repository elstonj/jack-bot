# NTR - LDCR Mods

## Document Metadata
- Type: New Technology Report (NTR)
- Client/Agency: NASA Goddard Space Flight Center
- Program/Solicitation: NASA SBIR Phase II, Contract NNX14CG09C (primary); related to NNX13CG33P and earlier NESSF Award NNX12AO08H
- Date: Submitted 2016-04-06 to 2016-04-07
- BST Products/Systems Referenced: Soil Moisture Mapping sUAS, LDCR (Lobe Differencing Correlating Radiometer), MiCo antenna
- Key Personnel: Jack Elston (BST, Company Tech Rep, elstonj@blackswifttech.com); Albin Gasiewski (University of Colorado, Overall Design); Eryan Dai (University of Colorado, Detailed design/construction/testing); Eric McIntyre (University of Colorado, Initial prototype design)

## Executive Summary
This NTR documents modifications made to the Lobe Differencing Correlating Radiometer (LDCR) during Phase II development to enable integration into an unmanned aircraft system for soil moisture mapping. Three critical issues discovered during ground testing—electrical noise, insufficient output voltage range, and temperature-dependent measurement drift—were resolved through power filtering, amplification, and temperature monitoring implementations, culminating in successful flight tests in September 2015.

## Technical Approach

**Problem Statement:**
Integration of the LDCR into the aircraft revealed three specific issues:
1. Noise sources leaking into the instrument disrupting measurements (initially 6x higher than expected)
2. Insufficient voltage range of output for A/D converter resolution
3. Measurement drift correlated to component temperature variations

**Solutions Implemented:**

**Noise Mitigation (Analog Correlator Board):**
- Added LC filter to input power voltage
- Inserted IF gain amplifiers between LDCR output and analog correlator
- Built low pass filter at analog correlator output with 1.5ms time constant
- Further RF isolation through:
  - DC feed-through: two parallel 0.1 µF and 22 µF decoupling capacitors in parallel; 1 µH inductor in series to reduce high-frequency noise
  - Shielded twisted triple wires for DC power supply to reduce high-frequency and low-frequency electromagnetic interference
  - Pair of 0.1 µF capacitors in parallel at TEC heating/cooling power supply pins to reduce high-frequency noise introduction into downconverter carrier

**Output Voltage Range:**
- Added video amplifier between low-pass filter output of analog correlator and A/D input of data logger

**Temperature Compensation:**
- Installed 5 thermistors on LDCR receiving board to monitor temperature of:
  - TEC (Thermoelectric Cooler) on channels 1 and 2
  - Isolator
  - Local oscillator
  - IF signal filter

## Products & Capabilities Described

**Lobe Differencing Correlating Radiometer (LDCR)**
- What it is: A microwave radiometer originally developed under NASA NESSF Award NNX12AO08H for L-band measurements
- Modified for integration into sUAS platform
- Paired with MiCo antenna for soil moisture mapping
- Achieves 15-meter measurement resolution (compared to ~40 km for SMAP satellite)
- Capable of accurate soil moisture measurements across varying temperature conditions after modifications

**Soil Moisture Mapping sUAS**
- Small unmanned aircraft system carrying LDCR and MiCo antenna
- Primary application: soil moisture validation and measurement
- Cost advantage over manned aircraft for regional monitoring

## Use Cases & Applications

1. **SMAP (Soil Moisture Active Passive) Mission Support:**
   - Validation of satellite measurements
   - Fine-resolution (15m) augmentation of satellite data (40km resolution)
   - Calibration and validation activities before and after spacecraft launch

2. **Hydrological Applications:**
   - Watershed monitoring
   - Drought area assessment
   - Flash flood vulnerability assessment and warning

3. **Historical Precedent:**
   - 2007 effort led by Prof. Gasiewski mapping soil moisture in North Texas and Oklahoma
   - Data used to provide alerts and warnings for flash flood-susceptible areas
   - Demonstrated applicability for FEMA flood prediction support

## Key Results

**Development Timeline:**
- 05/04/2014: Local oscillator leakage identified; initial power circuit filter design work begun
- 07/15/2014: Power filtering circuits completed; amplifier added to output
- 10/06/2014: Outdoor ground testing of updated LDCR
- 04/10/2015: Thermistor installation and testing completed
- 09/08/2015: Successful flight test of updated LDCR in Canton, OK

**Performance Achievements:**
- Reduced noise to acceptable levels (previously 6x higher than expected)
- Achieved adequate output voltage range for A/D conversion
- Demonstrated temperature stability and monitoring capability
- Completed successful flight operations

## Notable Details

- **State of Development:** Classified as "Modification" to existing technology; represents "Substantial Advancement in the Art"
- **Technical Significance:** Not a breakthrough but represents important engineering maturation of instrument for operational flight use
- **Collaborative Effort:** Joint effort between Black Swift Technologies and University of Colorado researchers
- **No Patent Filing:** Patent status section left blank; no indication of patent applications for these modifications
- **Competitive Advantage vs. SMAP:** 27x finer resolution (15m vs. 40km) enabling localized validation and supplementary high-resolution data collection at fraction of manned aircraft cost
- **Regulatory/Agency Support Demonstrated:** Existing relationship with NASA and FEMA for flood prediction applications