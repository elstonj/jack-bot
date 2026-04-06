# 2020-12-07 AGU Overview - Black Swift Technologies

## Document Metadata
- Type: Conference presentation overview / technical briefing
- Client/Agency: DoD (SBIR program)
- Program/Solicitation: SBIR Phase II - Atmospheric Sounding (2019.2)
- Date: December 7, 2020
- BST Products/Systems Referenced: S0, S0-AD (atmospheric sounding UAS)
- Key Personnel: Jack Elston (last editor)

## Executive Summary
This document presents the design requirements and validation approach for the S0 atmospheric sounding UAS, a low-cost, simple-to-operate unmanned system for vertical atmospheric profiling. It details wind sensing methodology using 3D-printed probe components and describes field validation testing comparing UAS measurements against instrumented towers and radiosondes.

## Technical Approach

**Wind Sensing Method:**
- Uses 3D-printed probe components to measure wind from pressure differentials
- Employs 9th order polynomial fitting for wind calculation accuracy
- Computes cα (angle of attack coefficient), cβ (sideslip coefficient), and cq (dynamic pressure coefficient)
- Non-linear response with good symmetry properties

**Calibration & Testing:**
- Extensive wind tunnel and flight calibration conducted
- Probe positioned at 900 different test points during calibration
- Coverage: ±15° angle of attack (α) and sideslip angle (β) at 1° intervals
- Over 1,000 measurements at each probe position
- Approximately 10⁶ total calibration measurements
- Total calibration run time: ~3 hours

**Field Validation Protocol:**
- Ground truth comparison against instrumented meteorological tower
- 5-day validation window with varied flight patterns upwind of tower
- Statistical comparison of wind speed, wind direction, temperature, pressure, and humidity
- Evaluation of system's ability to capture different turbulent scales
- Coordinated flights immediately following radiosonde launches to compare vertical profiles
- Consistency validation between S0-AD and weather balloon measurements

## Products & Capabilities Described

**S0 / S0-AD (Atmospheric Sounding UAS)**
- **Form Factor:** Small, simple-to-operate unmanned system
- **Training Requirements:** Operates with <1 day training
- **Cost Target:** <$5,000 for full setup
- **Altitude Capability:** Profiles up to 15,000 feet AGL
- **User Interface:** Familiar interface design
- **Data Outputs:** Common meteorological formats (BUFR, GRIB, netCDF)
- **Performance:** Rapid yet accurate atmospheric measurements

## Use Cases & Applications

- Vertical atmospheric profiling for meteorological research
- Rapid deployment alternative to weather balloons (radiosondes)
- Field meteorology and atmospheric validation studies
- Comparison validation against ground-based instrumentation

## Notable Details

- Design emphasizes simplicity and accessibility (low cost, minimal training)
- Innovative use of 3D-printed aerodynamic probe elements
- Comprehensive calibration approach (900 probe positions, ~10⁶ measurements)
- Direct comparison methodology with established meteorological instruments validates capability and builds confidence in autonomous atmospheric sensing
- Part of DoD SBIR Phase II atmospheric sounding research program
- Suggests BST was positioning S0-AD as a practical, deployable alternative to traditional radiosonde networks