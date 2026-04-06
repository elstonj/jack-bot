# Phase I NASA SBIR: Integration of In Situ Eddy Dissipation Rate Algorithm on Small Uncrewed Aircraft Systems for Estimating Turbulence Intensities

## Document Metadata
- Type: SBIR Phase I Subcontract Statement of Work and Budget
- Client/Agency: NASA (SBIR Program)
- Program/Solicitation: 2021 NASA SBIR, Turbulence Measurement topic
- Date: Due 8 January 2021 (created 22 December 2020)
- BST Products/Systems Referenced: Fixed-wing small UAS (sUAS) fleet with existing flight data capabilities
- Key Personnel: James Pinto (PI), Larry Cornman (PI), Greg Meymaris (PI); Jack Elston (BST, last editor)
- Proposed Budget: $37,070

## Executive Summary
This Phase I SBIR proposes to adapt NCAR's in situ Eddy Dissipation Rate (EDR) algorithm to Black Swift Technologies' small uncrewed aircraft systems to measure atmospheric turbulence in the lowest 120 meters of the atmosphere. The effort addresses a critical gap in turbulence observations needed to support safe UAS Traffic Management (UTM) and commercial small UAS operations, particularly for the emerging Urban Air Mobility sector.

## Technical Approach

**Core Technical Strategy:**
- Adapt NCAR's vertical wind-based in situ EDR algorithm (from Sharman et al. 2014) for implementation on fixed-wing sUAS
- Use existing recorded flight data from Black Swift's previous fixed-wing UAS missions as initial proof-of-concept
- Compare EDR calculations derived from high-rate flight data against calculations from multi-hole probe (MHP) data
- Validate EDR measurements against ground truth via comparison with instrumented turbulence towers (e.g., NCAR Marshall field site, Boulder, CO planned for 2021 deployment)

**Algorithm Basis:**
- Founded on Kolmogorov's (1941) inertial subrange theory for turbulent kinetic energy
- EDR (ε^1/3) is aircraft-independent metric of turbulent intensity (units: m^2/3 s^-1)
- EDR standard used by International Civil Aviation Organization (ICAO) for transport aircraft turbulence reporting
- Algorithm uses onboard accelerometer or vertical wind measurements to compute EDR

**Required Systems & Sensors:**
- High-rate 3D wind calculations from multi-hole probe (MHP) data
- Flight parameters: true airspeed (TAS), altitude, dynamic pressure, angle of attack, angle of sideslip
- Onboard sensors, data rates, and computational capabilities for real-time EDR computation
- Transmission capability to ground control station or via ADS-B Wx protocol
- Quality control algorithms (onboard and ground-based) to flag spurious reports

**Technical Considerations:**
- Determine processor speed and storage specifications for EDR add-on circuit-board vs. software integration into existing flight monitoring systems
- Assess computational requirements for real-time vs. post-flight EDR calculation
- Evaluate sensor specifications per Sharman et al. (2014)

## Products & Capabilities Described

### Black Swift Technologies Fixed-Wing Small UAS Fleet
- **What it is:** Existing small uncrewed aircraft systems with multi-hole probe capability and high-rate flight data recording
- **Proposed use:** Platform for testing and validating EDR algorithm implementation using existing datasets from previous flights
- **Specifications:** Currently equipped to measure true airspeed, altitude, dynamic pressure, angle of attack/sideslip; capable of multi-hole probe data collection

### EDR Measurement & Reporting System (Proposed)
- **What it is:** Real-time turbulence intensity measurement and reporting capability for small UAS
- **Proposed function:** Onboard EDR computation with data transmission to ground station and/or ADS-B Wx network
- **Data reported:** EDR values plus ancillary parameters (power consumption, altitude, location, temperature, derived wind speed)
- **Network capability:** Internet of Things (IoT) broadcast capability to alert other nearby UAS of turbulence conditions along flight paths

## Use Cases & Applications

1. **UAS Traffic Management (UTM) Support:** Provide real-time turbulence guidance to support safe and efficient operation of commercial small UAS in national airspace

2. **Low-Altitude Aviation Operations:** Fill critical gap in turbulence observations at altitudes < 120 meters AGL where commercial sUAS operate but where existing EDR reporting is sparse (most current EDR reports from 1,300+ transport aircraft occur well above sUAS operating altitudes)

3. **Urban Air Mobility (UAM):** Support emerging eVTOL and multi-rotor vehicle operations with turbulence data

4. **Structural Safety:** Support mission-critical operations requiring high confidence in turbulence forecasts:
   - Building/infrastructure inspection (minimize attitude disturbance and structural stress)
   - Video surveillance (reduce excessive attitude disturbance from gusts)
   - Safe navigation within 3D geo-fenced flight corridors

5. **Aircraft Performance & Range:** Enable prediction of turbulence-induced power consumption impacts on UAS operating range and flight endurance

6. **Boundary Layer Research & Model Validation:** Provide unprecedented spatio-temporal coverage of turbulence intensities in lower atmosphere to:
   - Evaluate and improve turbulence guidance products (NCAR/NOAA GTGN, GTG)
   - Validate mesoscale (HRRR) and microscale (WRF LES) model predictions
   - Inform next-generation boundary layer research

## Phase I Work Tasks

**NCAR Tasking (as subcontractor):**

1. Establish onboard sensor, data rate, computational, and transmission requirements for EDR computation and reporting; define target variables and specifications

2. Determine processor speed and storage specifications for EDR circuit-board or software integration options

3. Compare EDR derived from high-rate flight data against MHP-derived EDR using Black Swift fixed-wing UAS data; perform validation flights adjacent to turbulence tower if opportunity arises

4. Perform quality control assessment and diagnose discrepancies between calculation techniques

5. Work with Black Swift to determine requirements and costs for end-to-end EDR capability including software/circuit board development and installation

6. Explore and document techniques for extending EDR calculations to multi-rotor UAS (identify challenges of prop-wash contamination; outline inverse methods requiring tower calibration flights)

7. Support project reporting and stakeholder briefings

## Phase II Preliminary Objectives (Outlined)

- Develop prototype in situ EDR software module and/or circuit board with Black Swift
- Install EDR capability on multiple fixed-wing UAS in Black Swift fleet
- Perform validation flights adjacent to NCAR CAL/VAL tower at Marshall field (Boulder, CO) or other instrumented facility
- Develop methods for extending EDR to multi-rotor and eVTOL vehicles
- Implement quality control methods (onboard and ground-based)
- Establish connectivity with turbulence guidance product developers (specifically GTGN developers)
- Integrate new sUAS-based EDR data stream into operational turbulence nowcasting products

## Notable Details

- **Collaborative Structure:** Partnership between NCAR (algorithm expertise, validation infrastructure) and Black Swift Technologies (UAS platform, flight operations)

- **Existing Algorithm Foundation:** NCAR's EDR algorithm already installed on over 1,300 transport aircraft worldwide; proposed effort adapts proven, operationally validated technology to new platform

- **Addressing a Critical Gap:** Current EDR coverage concentrated along jet routes and major airport hubs at high altitudes; sUAS operations at < 120 m AGL remain largely unmonitored despite high variability and diurnal dependence of turbulence at these altitudes

- **Multi-Phase Approach:** Phase I focuses on fixed-wing feasibility (lower technical risk); Phase II planned to address more challenging multi-rotor implementation (prop-wash contamination requires inverse methods and calibration)

- **Sensor Innovation:** Use of multi-hole probe (MHP) on Black Swift UAS provides high-quality wind measurements for algorithm validation

- **Ground Truth Validation:** Leverages NCAR's planned 2021 turbulence tower deployment at Marshall field site for validation

- **Operational Readiness:** End goal is turn-key system with real-time data transmission, quality control, and integration into existing UTM and turbulence guidance systems

- **Market Potential:** Positions Black Swift to offer new commercial service (turbulence measurement/reporting) while supporting broader national airspace integration of sUAS