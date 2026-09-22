# Attachment A - Statement of Work UAS Services Final

## Document Metadata
- Type: Statement of Work (SOW) for Master IDIQ Contract
- Client/Agency: National Oceanic and Atmospheric Administration (NOAA), Office of Marine and Aviation Operations (OMAO), Uncrewed Systems Operations Center (UxSOC)
- Program/Solicitation: RFQ1305M226Q0069; Authorized under Commercial Engagement through Ocean Technology Act (Public Law 115-394) and Consolidated Appropriations Act, 2023; Supports Autonomous and Uncrewed Technology Operations (AUTO) program
- Date: Document created/modified 2026-08-30
- BST Products/Systems Referenced: None explicitly named (this is a NOAA requirement document, not a BST proposal response)
- Key Personnel: Jack Elston (last editor)

## Executive Summary
NOAA's UxSOC is soliciting a Master IDIQ contract for Contractor-provided Uncrewed Aircraft Systems (UAS) Data-as-a-Service (DaaS) to support climate, weather, ocean, and coastal monitoring missions. The contract is performance-based with individual Task Orders specifying missions, and requires full platform support, sensor integration, real-time data delivery, and compliance with FAA and NOAA regulations over a 5-year period.

## Technical Approach
The SOW establishes baseline requirements for a contractor to provide:
- Fully supported UAS platforms with capacity for multiple sensor suites
- Platform adaptation and enhancement as needed per Task Orders
- Aircraft operation during missions with reliable data storage and transmission
- Program management oversight for multiple simultaneous Task Orders
- Non-Recurring Engineering (NRE) for sensor integration and software configuration

**Platform Requirements:**
- Variable endurance capabilities: short-range (<2 hrs), medium-range (2-10 hrs), long-endurance (>10 hrs)
- Payload capacity suitable for sensor types listed below
- Capable of operations across altitudes over land, water, or ice
- BVLOS operations require FAA waivers, Detect and Avoid (DAA) technologies, or equivalent safety mitigation

**Data Management:**
- Raw and processed data delivery per Task Order specifications
- Real-time data streams via secure API or cloud transfer
- Machine-to-machine services for data retrieval at mission-specific frequencies
- Monthly progress reports
- Sensor calibration logs traceable to NIST or equivalent standards
- Quality Control Plan (QCP) with data validation protocols and recollection strategy at no additional cost if data doesn't meet accuracy/resolution thresholds

## Products & Capabilities Described

### Mission Focus Areas (not specific products, but operational domains):

**Living Marine Resource Surveys and Research**
- Marine mammal and protected species observations
- Fisheries stock assessments

**Meteorological and Oceanographic Observations**
- Air-sea interaction observations
- Atmospheric flux measurements
- Long-range, mid- to high-altitude measurements for forecasting and climate research

**Ocean Exploration and Characterization**
- Harmful algal bloom (HAB) characterization
- Ocean color mapping
- Satellite calibration/validation data collection

**Land, Cryospheric, and Hydrographic Mapping**
- High-resolution shoreline verification
- Shallow water bathymetry for nautical charting, coastal resilience, and habitat modeling
- Surface feature mapping

**Other Priority Areas**
- As identified by Congress through appropriations

### Sensor/Data Collection Capabilities Required:

**Atmospheric Data Services**
- In-situ meteorological data (pressure, temperature, humidity, wind)
- Aerosol collection
- Trace gas sampling from boundary layer to high altitudes

**Remote Sensing Services (Imagery/Lidar)**
- High-resolution RGB ("visible") imagery
- Thermal Infrared (IR) data
- Multispectral and Hyperspectral imagery
- Lidar data for mapping and bathymetric characterization

**Visual Data & Scientific Observation**
- High-resolution video and optical imaging
- Biological classification (biota detection, quantification)
- Ground truthing and environmental monitoring
- Integrated multi-sensor operations for:
  - Chemical parameters (environmental DNA, dissolved oxygen, CO2, nutrients, methane, salinity)
  - Physical parameters (temperature, pressure, currents, wave features, ocean energy)

**Extreme Environments & Specialized Capabilities**
- Operations in Arctic conditions (high wind, freezing temperatures)
- Tropical cyclone eyewall operations (heavy precipitation, strong turbulence)
- Very high altitude operations

**Data Processing & Analytics**
- Post-processing of raw data into derived products (orthomosaics, point clouds)

## Use Cases & Applications
- Arctic operations in extreme cold and high-wind conditions
- Tropical cyclone sampling including eyewall penetration
- Marine mammal and protected species surveys
- Fisheries stock assessment flights
- Harmful algal bloom monitoring and characterization
- Hurricane/cyclone research and forecasting support
- Ocean color and satellite validation missions
- Coastal bathymetry and shoreline mapping
- Climate and atmospheric research flights
- Methane and trace gas detection/sampling
- High-altitude atmospheric measurements

## Deliverables (Baseline Requirements)

| Deliverable | Description | Format | Frequency |
|---|---|---|---|
| Mission Data Sets | Raw and processed atmospheric, remote sensing, or scientific observations | As specified in Task Order | Per TO schedule |
| Real-Time Data Stream | Live telemetry or sensor feeds via machine-to-machine services | Secure API / Cloud Transfer | Real-time during flight operations |
| Progress Reports | Summary of work performed, milestones, and issues | PDF / MS Word | Monthly (unless otherwise specified) |
| Quality Control Plan (QCP) | Procedures for data integrity, calibration, and safety | PDF / MS Word | Within 30 days of contract award; updated per TO |
| Sensor Calibration Logs | Records traceable to NIST or equivalent standards | Digital / Machine Readable | Upon request or with final data delivery |

## Regulatory Compliance & Key Requirements

**FAA & Aviation**
- All operations in strict accordance with 14 CFR Part 107, Certificate of Waiver or Authorization (COA)
- NOAA Administrative Order (NAO) 216-104-A compliance
- Contractor responsible for obtaining all necessary waivers, airspace authorizations, spectrum/frequency approvals
- BVLOS operations require FAA waivers and Detect and Avoid (DAA) technologies or equivalent mitigation

**Accident/Mishap Reporting**
- Immediate verbal/email notification within 2 hours
- Written preliminary accident report within 24 hours
- Compliance with NOAA NAO 209-124, NTSB Part 830, and FAA regulations
- Full cooperation with Government investigation; provide all flight logs, maintenance records, sensor data

**Security Requirements**
- Compliance with NOAA IT security policies
- Commerce Acquisition Regulation (CAR) 1352.239-72 compliance
- NIST SP 800-171 compliance (Protecting Controlled Unclassified Information in Nonfederal Systems)
- Implementation of NIST SP 800-53 Revision 5 control families: Configuration Management, Identification and Authentication, Communication Protection, Risk Assessment, System and Services Acquisition, System Access Control, System Audit and Accountability, System and Information Integrity, Media Protection, Contingency Planning, Incident Response
- Supply Chain Risk Management (SCRM) Program compliance; DOC may audit supply chain processes; failure to resolve identified risks may result in contract termination

**Intellectual Property**
- All deliverables and anything developed with Government funding are sole property of U.S. Government with full title, control, and rights
- Includes: raw sensor data, metadata, data schemas, software, hardware, models, processes, documentation, encryption keys
- Contractor cannot release or disclose data without prior written Government consent
- Contractor must comply with DOC and NOAA IT data security and Controlled Unclassified Information protection policies

**Quality Control & Performance Standards**
- Contractor develops and maintains living QCP within 30 days of award
- QCP must include data validation protocol and recollection strategy at no additional cost if data fails to meet minimum accuracy/resolution thresholds
- Government reserves right to audit QCP adherence at any time
- Performance standards for data delivery, latency, and remedies for nonconforming data specified in individual Task Orders

## Period of Performance
- Master IDIQ period: Five (5) years from date of award
- Mission locations: Anywhere in or outside the United States National Airspace System (NAS)
- Specific dates and locations defined in individual Task Orders

## Notable Details

**Contract Structure**
- Master IDIQ with performance-based individual Task Orders
- Number of projects/missions depends on NOAA funding and requirements
- Non-Recurring Engineering (NRE) available for platform adaptation; contractor provides quotes; NRE provided via FFP Hourly Labor Rates

**Data Sensitivity**
- All data classified as potential Controlled Unclassified Information
- Strict IP provisions give all rights to U.S. Government
- Real-time data delivery capability emphasizes need for robust, secure IT infrastructure

**Extreme Environment Emphasis**
- Specific capability to operate in Arctic, tropical cyclone, and high-altitude environments
- Suggests need for specialized platforms (likely relevant for BST's S2 or S3 systems for extreme weather operations)

**Sensor Calibration Requirements**
- All sensors require pre- and post-mission calibrations traceable to NIST or equivalent international standards
- History of each sensor must be available upon request