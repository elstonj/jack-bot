# 03-07-2025 Budget Estimate Update - OMAO

## Document Metadata
- Type: Budget estimate/cost proposal update
- Client/Agency: NOAA OMAO (Office of Marine and Aviation Operations)
- Program/Solicitation: Not explicitly stated (appears to be pending proposal)
- Date: March 7, 2025
- BST Products/Systems Referenced: S0 (tube-launched aircraft), AirOps (ground station software), MHTP (Multisonde Thermal Platform), deployment tube
- Key Personnel: Beck Cotter (last editor)

## Executive Summary
This document provides a detailed budget breakdown for engineering, testing, and operational improvements to BST's tube-launched UAS platform for NOAA operations. It covers three years of development (Y1-Y3) with a total budget of $381,000 for core modifications, plus additional costs for platform migration and prototype development, totaling approximately $1.2M including all line items.

## Technical Approach
Budget items indicate a phased development approach:

**Year 1 Focus (Y138,667):** Foundational work including firmware customization for autonomous operations, onboard video systems, high-frequency meteorological data (10Hz), battery endurance optimization, and dual-GPS heading improvements. Includes initial operational deployments (2025 hurricane season, clear air testing).

**Year 2 Focus ($125,667):** CAD-based launching system (no depressurization required for AVAPS compatibility), integration with Skyfora sensor alongside existing Vaisala systems, wind measurement improvements (laser-relative flight capability), and tunnel testing for aerodynamic characterization.

**Year 3 Focus ($116,667):** Data handling robustness (buffering/re-transmission for lost comms), advanced firmware updates via USB (in-tube capability), laser configuration optimization for rain operations, and documentation/training materials.

## Products & Capabilities Described

### S0 (Tube-Launched Aircraft)
- Tube-deployed UAS system for NOAA hurricane and atmospheric operations
- Current endurance baseline with potential 30-minute extension through battery optimization
- Equipped with meteorological sensors (Vaisala, planned Skyfora integration)
- Laser altimeter system that can be used for relative flight control
- Onboard video capability for situational awareness
- Budget line for "Tube launched S0" prototype: $720,000 (separate from operational modifications)

### Deployment Tube
- Pressurized launch container
- Planned USB firmware update port (top of tube) to enable in-vehicle updates
- Compatibility with AVAPS (Atmospheric Vertical Access Profiling System) for NOAA operations
- Data handling improvements for missed communication recovery

### AirOps (Ground Station Software)
- P3 aircraft ground control station software
- Planned enhancements: laser altitude display, radio signal quality monitoring, UAS communication status tracking
- Automated NetCDF file generation capability for data post-processing and QC

### MHTP (Multisonde Thermal Platform)
- Existing system with planned migration to new platform alternatives (Dragoon or Strato Solutions)
- Budget line: $104,000 for integration work (separate from core modifications)

## Use Cases & Applications
- **Hurricane operations:** 4 flights budgeted per year for years 2025-2027 ($16,000/year operations cost)
- **Clear air testing:** 2025 characterization flights ($6,000)
- **Atmospheric profiling:** Integration with AVAPS and meteorological sensors for wind/temperature/humidity measurements
- **Real-time adaptation:** Firmware and UI customization to allow scientists to modify flight parameters during operations

## Key Budget Allocations

| Category | Total | Y1 | Y2 | Y3 |
|----------|-------|----|----|-----|
| **Engineering NRE** | $381,000 | $138,667 | $125,667 | $116,667 |
| **Operational flights** | $48,000 | $22,000 | $16,000 | $16,000 |
| **Sensor/integration work** | $13,000-$34,000 per item | Varies | Varies | Varies |
| **MHTP migration** | $104,000 | (separate) | (separate) | (separate) |
| **S0 prototype dev** | $720,000 | (separate) | (separate) | (separate) |

## Notable Details

**Key Technical Improvements Prioritized:**
1. **Autonomous operation** - Extensive firmware customization for reduced operator burden and real-time scientist control
2. **Wind measurement accuracy** - Dual GPS with RTK moving baseline to replace magnetometer-dependent heading estimates
3. **Operational robustness** - Communication resilience features, in-situ firmware updates, manufacturability improvements
4. **Sensor compatibility** - Multi-sensor support (Vaisala + Skyfora) and NOAA tool integration (AVAPS)
5. **Environmental adaptation** - Laser optimization for rain operations, aerodynamic testing

**Manufacturing & Sustainability:**
- Manufacturability improvements to reduce cost and increase reliability ($18,000 over 3 years)
- Future-proofing approach with modular firmware and in-tube update capability

**Personnel Effort:** Total of 1,200 engineering hours budgeted across three years (mix of firmware, integration, testing, documentation, and meetings)

**Document Status:** Marked as "pending" proposal to NOAA, suggesting this budget estimate was prepared in advance of formal submission/approval.