# S0 UAS Measurement Characterization Campaign - Final Campaign Report

## Document Metadata
- Type: Field campaign final report
- Client/Agency: US Department of Energy (DOE) Atmospheric Radiation Measurement (ARM) Program
- Program/Solicitation: SBIR Phase II, Atmospheric Sounding topic
- Date: October 2021
- BST Products/Systems Referenced: S0 UAS
- Key Personnel: Jack Elston (Black Swift Technologies), Maciej Stachura (Black Swift Technologies), Gijs de Boer (Boreas Consulting, lead), Adam Houston, Ashraful Islam, Daniel Rico, Matthew Wilson (University of Nebraska-Lincoln)

## Executive Summary
Black Swift Technologies and University of Nebraska conducted a week-long field campaign at the DOE ARM Southern Great Plains facility in Oklahoma to evaluate and intercompare small uncrewed aircraft systems (sUAS) for atmospheric research. The campaign involved 95 sUAS flights totaling 18.6 flight hours, comparing data from the BST S0 fixed-wing UAS against radiosondes, tower instruments, and other UAS platforms (University of Nebraska M600 and Meteodrone). Results showed generally good agreement with radiosondes and tower measurements, though identified a ~1-1.5°C warm bias in the S0's temperature sensor.

## Technical Approach
- Conducted coordinated multi-platform flights at ARM SGP facility and Marshall (OK) mesonet site
- S0 operated both north and south of SGP 60 m tower; M600 and Meteodrone operated east of tower
- Flights designed to follow extra radiosondes launched as campaign component and conduct extended statistical sampling at tower instrument heights
- Data collection focused on system evaluation and intercomparison across multiple platforms
- Compared UAS-measured atmospheric quantities (temperature, relative humidity, wind speed/direction) against radiosondes, tower instruments, and sister platforms
- Ground testing conducted comparing UAS sensors against ARM ECOR (Energy Balance Bowen Ratio) system (results not finalized in report)

## Products & Capabilities Described

### Black Swift Technologies S0 UAS
- **What it is:** Fixed-wing small uncrewed aircraft system for atmospheric research
- **Configuration:** Equipped with temperature, relative humidity, and wind measurement sensors
- **Performance in campaign:**
  - Successfully conducted 95 total flights across the campaign
  - Showed capability to conduct extended hover/station-keeping at tower heights for statistical sampling
  - Wind measurements agreed well with radiosondes (mean errors near zero, ±5 m/s spread attributed to spatial variability)
  - Temperature sensor exhibited ~1-1.5°C warm bias relative to radiosondes and other platforms
  - Temperature bias showed slight dependence on solar incidence angle (~0.2°C smaller bias when heading directly into sun)

## Use Cases & Applications
- **Atmospheric boundary layer characterization:** Measuring lower atmosphere conditions critical to weather/climate understanding and numerical prediction models
- **Observing system intercomparison:** Validating UAS platforms against established observing systems (radiosondes, tower instruments, research aircraft)
- **Atmospheric research infrastructure:** Contributing to improved representation of boundary layer in atmospheric models
- **Multi-platform coordination:** Operating alongside established research teams (University of Colorado, University of Oklahoma, Oklahoma State University) in TRACER-UAS initiative

## Key Results

### Quantitative Findings:
- **Campaign scope:** 95 sUAS flights, 18.6 total flight hours
- **Temperature bias (S0):** ~1-1.5°C warm bias relative to radiosondes; slight variation with solar angle
- **Wind measurements:** Both S0 and Meteodrone generally captured wind speeds and directions measured by radiosondes; mean wind errors close to zero
- **Relative humidity variability (M600):** Significant variability noted; unclear if due to measurement bias or pressure-based altitude sensing issues
- **Tower-based wind comparison:** Mean errors near zero, ±5 m/s spread likely due to spatial variability in boundary layer winds
- **Temperature sensitivity to solar orientation:** S0 showed ~0.2°C smaller bias when aircraft heading directly into sun (0° sun angle)

### Qualitative Findings:
- Generally good agreement between UAS measurements and radiosondes/tower instruments
- Wind measurements from UAS platforms validated as reliable (previously considered uncertain)
- S0 temperature sensor housing identified as area for design improvement to address warm bias
- Rich dataset generated for continued UAS platform evaluation

## Notable Details

### Data Archiving & Access:
- All campaign data deposited in ARM Data Portal with digital object identifiers (DOIs)
- S0 data: de Boer et al. (2021), DOI: 10.5439/1824862
- Platform data publicly available through ARM for research community

### Publication Plan:
- Peer-reviewed manuscript in preparation for *Journal of Atmospheric and Oceanic Technology* (J. Tech)
- Will include comparisons with University of Colorado and University of Oklahoma platforms as part of TRACER-UAS initiative
- Conference presentations delivered at AGU Fall Meeting (December 2021) and ARM/ASR PI meeting (June 2021)

### Collaborative Framework:
- Multi-institutional effort: Black Swift Technologies, University of Nebraska-Lincoln, University of Colorado, University of Oklahoma, Oklahoma State University, Boreas Consulting
- Part of broader TRACER-UAS (TRACER Science Team Meeting, April 2021) effort
- Leveraged DOE ARM facility infrastructure and expertise

### Design Improvements Identified:
- S0 temperature sensor housing to be revisited to address documented warm bias
- Design team will use field campaign findings for continued platform advancement
- Suggestion for tower enhancement: adding pressure sensors to enable altitude verification and calculation of derived variables (potential temperature)

### Operational Notes:
- Weather conditions during campaign: generally good with moderate winds, favorable for operations
- High partnership satisfaction; strong collaboration with SGP facility team