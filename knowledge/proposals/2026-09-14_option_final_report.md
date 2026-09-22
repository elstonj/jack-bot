# 2026-09-14 Option Final Report

## Document Metadata
- Type: Phase I Option Final Report (presentation)
- Client/Agency: U.S. Navy
- Program/Solicitation: Navy STTR - Hazardous Weather
- Date: 2026-09-14
- BST Products/Systems Referenced: S0 (multiple variants: S0-97, S0-87, S0-76), LALA, Moke
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
This Phase I Option final report documents completion of wave height algorithm development, additional calibration/validation work with NOAA and ISARRA data, and stakeholder engagement activities. The team successfully developed a sequential wave height estimation algorithm and conducted operational flights with SOCOM and the 53rd Wing, while also securing follow-on contracts for PCLT and METAR S0 developments.

## Technical Approach

### Wave Height Algorithm Development
- **Primary Method**: Exponentially-weighted moving average (EWMA) cross-covariance approach
  - Reformulates batch processing as low-pass filter
  - Minimal computational burden (only requires storing 4 values)
  - Most practical for sequential/real-time implementation
  
- **Algorithm Basis**: Uses high-rate radar and altitude data to estimate Significant Wave Height (SWH) over 5 and 10km segments
  - Formula: var(surface) = var(agl) − cov(alt, agl)
  - Operates consistently from 40m to 5m above ocean surface

- **Validation Approach**: 
  - Comparison against ERA5 and GFS wave forecast models
  - Batch Welch cross-spectrum analysis
  - Stepped descent validation flights to test altitude independence

### Alternative Approaches Evaluated
- Spectral Kalman Filter: Rejected due to computational complexity and tuning difficulty
- Exponentially-weighted Welch: 10km segment processing
- Selected EWMA cross-covariance as most practical

### Simulator Development
- Rebuilt S0 simulator to run aircraft physics at 1000 Hz
- Ingests atmospheric data at up to 25 Hz
- Tested with multiple tropical cyclone (TC) models and NCAR datasets
- Planned testing with 1m resolution NCAR wind model

## Products & Capabilities Described

### S0 Variants
- High-rate radar sensor platform deployed on multiple aircraft
- Operational variants: S0-97, S0-87, S0-76
- Equipped with altitude measurement and radar capability
- Successfully flown in conjunction with NOAA operations (Moke flights)
- Integrated for SOCOM and 53rd Wing operations

### LALA Platform
- Wave height comparison baseline
- Identified dry bias potentially due to lack of reflective tape
- Humidity bias closely matches temperature bias (solar heating effect)

### Moke (NOAA-operated aircraft)
- Flight platform for validation work
- Multi-flight campaign conducted 2026-08-13 and other dates
- Wind comparison and wave height validation missions

## Use Cases & Applications

### Hazardous Weather Operations
- Naval hazardous weather monitoring and forecasting support
- Tropical cyclone characterization and monitoring

### Wave Height Estimation
- Real-time ocean state estimation for maritime operations
- Integration with GFS and ERA5 forecast models

### Military Stakeholder Engagement
- SOCOM operations (10kft and 20kft altitude drops with 2 S0 systems)
- 53rd Wing partnership for operational deployment

### Follow-on Development (Recently Contracted)
- PCLT (Pressure and Consistency Lidar Technique) S0 development
- METAR S0 development for meteorological data collection

## Key Results

### Wave Height Algorithm Performance
**Moke comparison with GFS forecast model:**
- Bias: 0.55m
- RMS Error: 0.66m

**LALA comparison with GFS forecast model:**
- Bias: 0.24m
- RMS Error: 0.66m

**Algorithm Comparison (Track Length 24-127km):**
- Batch Welch shows good baseline performance (3.97-4.41m)
- EWMA approach demonstrates comparable accuracy while reducing computational requirements
- Altitude invariance demonstrated from 40m to surface (stepped descent validation)

### Operational Metrics
- Full mission success for SOCOM operations
- Successful OOI Cal/Val event participation (rescheduled for late September 2026)

## Notable Details

### Technical Achievements
- Humidity bias tracking closely with temperature bias indicates predominant solar heating effects
- Batch method altitude independence from 40m to surface represents significant validation milestone
- Sequential algorithm development reduces data storage requirements from full spectral data to 4-value state

### Stakeholder Integration
- Direct military engagement with SOCOM and 53rd Wing
- NOAA partnership for Cal/Val validation
- Commercial follow-on contracts secured (PCLT and METAR S0) indicating validated approach

### Bonus Work Prior to Phase II
- TC simulation capability developed with realistic aircraft physics (1000 Hz) and atmospheric data integration (25 Hz)
- Multi-model testing (multiple TC models, NCAR datasets)
- Prepared for fine-resolution wind model testing (1m NCAR model)