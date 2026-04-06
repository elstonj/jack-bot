# July Interim Report: Soil Moisture Mapping sUAS Phase II-E

## Document Metadata
- **Type:** Phase II Interim Report (NASA SBIR)
- **Client/Agency:** NASA (NASA Goddard Space Flight Center)
- **Program/Solicitation:** NASA SBIR Phase II-E, Contract Number NNX14CG09C
- **Date:** July 2016
- **BST Products/Systems Referenced:** SuperSwift (S2), Tempest, LDCR (L-band Dual-polarization Correlation Radiometer)
- **Key Personnel:** Maciej Stachura (contact), Dr. Gasiewski (advisor on FPGA work)

## Executive Summary
This interim report documents the first three months of Phase II-E work on a soil moisture mapping small unmanned aircraft system (sUAS). BST completed electromagnetic interference (EMI) mitigation improvements to the SuperSwift airframe, developed and tested FPGA logging software and interface boards for the LDCR radiometer, and obtained flight certification (AFSRB and FRRB) from NASA Goddard for flight testing at Pawnee National Grasslands in Colorado.

## Technical Approach

### SuperSwift EMI Mitigation Strategy
- **Shielding methodology:** Copper mesh bonded to fuselage structure around high-EMI components (motor, ESC, batteries, servo motors); all internal cables wrapped with EMI shielded braid
- **Radio options being evaluated:** Testing alternative 900MHz radio (Xeta9m-T from Xetawave) and 2.4GHz radio options to replace current XTend from Digi, which produces side-lobe noise in the LDCR frequency band
- **Antenna positioning:** Moving 900MHz telemetry radio antenna as far as possible from radio source; exploring post-processing noise removal

### Structural Redesign (CAD Updates)
- **Payload tray:** Redesigned from wooden scaffolding to tube-in-tube carbon fiber system for increased torsional stiffness and reduced vibration of MiCo antenna
- **Fuselage interior:** Updated carbon fiber tubing with carbon-on-carbon sliding interfaces for payload tray mounting; self-interlocking design to improve manufacturability and reduce assembly labor
- **Battery flexibility:** Two mounting locations designed (primary in center rails, secondary forward location) to accommodate changing battery technology (LiHV vs. standard LiPO) and allow center-of-gravity adjustment; removable battery boxes for future modifications

### New SuperSwift Nose Cone
- **Manufacturing improvement:** Transitioned from male mold to two-part female mold using wet layup (2 layers fiberglass)
- **Design features:** Added guide holes for cutting nose cones to different lengths, enabling modularity across different mission profiles
- **Weight reduction:** 503g (compared to 654g previously) = 151g weight savings
- **Cost reduction:** 8.6x cost reduction ($3,000 to $350 per nose cone)
- **Durability improvement:** Thinner walls provide more flexibility, better suited to hard landings

### FPGA Logging Software Development
- **LDCR Rev-B with CESYS EFM-02 FPGA board:** Debugged VHDL code for proper logging of three data types
  - **ADC data fixes:** Corrected clock mismatch (system clock vs. ADC clock); now properly samples ADC output with valid data signals
  - **UART data fixes:** Corrected status signal logic to prevent UART data stream from blocking ADC logging
  - **Time tick fixes:** Changed from request-triggered to free-running 26-bit counter (increments every 8192 ADC clock cycles) to identify missing data blocks
- **Data format:** 32-bit samples with priority ordering (time > UART > ADC); ADC samples include 2 header bits, 2 overflow bits, 14-bit data per channel
- **UART configuration:** STM32F405 microcontroller transmits 71-byte navigation packets at 115,200 bps
- **Sampling rate:** 80MHz ADC sampling
- **Current limitation:** Intermittent data logging gaps between continuous blocks (brief periods skipped); investigation ongoing

### FPGA Interface Board
- New interface board between LDCR and FPGA built and tested
- Performs signal conditioning for A/D converters
- Iteration on Phase II design
- Board modifications made: 50Ω resistors to ground replaced with 200kΩ resistors on differential inputs (Ch1, Ch2) to enable proper lab testing and balun board interfacing

### Antenna Integration
- MiCo antenna integrated into new SuperSwift payload scaffolding
- Payload tray redesigned with increased structural strength to support antenna

## Products & Capabilities Described

### SuperSwift (S2)
- **Primary platform:** 3.5m wingspan sUAS for soil moisture mapping
- **Configurations tested:** Equipped with LDCR radiometer for microwave soil moisture measurement
- **EMI status:** Phase II prototype had unshielded wiring and inadequate shielding; Phase II-E implements systematic copper mesh and braided cable shielding throughout
- **Modularity enhancements:** New nose cone design allows quick reconfiguration for different mission profiles; flexible payload bay supports different antenna/instrument configurations
- **Endurance capability:** Can carry two flight battery packs to increase usable flight time for lighter payloads
- **Flight certification:** AFSRB and FRRB completed June 2, 2016

### Tempest sUAS
- **Role:** Comparison baseline for EMI improvements
- **Configuration:** Same soil moisture mapping payload
- **Flight certification:** AFSRB and FRRB completed June 2, 2016
- **Plan:** Fly immediately before SuperSwift flights to provide baseline measurements

### LDCR (L-band Dual-polarization Correlation Radiometer)
- **Function:** Microwave radiometer for measuring soil moisture
- **Antenna:** MiCo antenna
- **Operating frequency:** L-band
- **EMI sensitivity issue:** Susceptible to side-lobe noise from 900MHz telemetry radio
- **Instrument improvements:** Rev-B version with improved FPGA logging and interface boards developed in Phase II-E

## Use Cases & Applications

### Primary Mission: Soil Moisture Mapping
- **Geography:** Testing at Pawnee National Grasslands, Colorado (90 min from BST)
- **Site advantages:** No nearby airports, no residents in grasslands, minimal road traffic, cooperative park ranger
- **Secondary site identified:** Near Yuma, CO with in situ soil moisture sensors for validation
- **Flight profile:** Pre- and post-rain event measurements to validate EMI reduction improvements
- **Phase II-E objective:** Reduce instrument noise through EMI mitigation; Phase II-E testing site does not require in situ sensors, though validation site available for future work

### Broader Applications Enabled by New Nose Cone Design
- Multiple mission profiles through quick nose cone reconfiguration
- Document mentions soil moisture mapping as primary focus but modularity enables future applications

## Key Results (First Three Months)

### Completed Deliverables
1. ✅ EMI mitigation strategy designed and materials sourced (copper mesh, shielded cable wrap)
2. ✅ Revised CAD models for fuselage interior and payload tray (tube-in-tube structure, carbon-on-carbon interfaces)
3. ✅ New SuperSwift nose cone mold fabricated and first article produced (503g, 8.6x cost reduction)
4. ✅ FPGA logging software debugged for ADC, UART, and time tick data streams
5. ✅ New FPGA interface board built and tested
6. ✅ Flight certifications obtained (AFSRB/FRRB from NASA Goddard) for both SuperSwift and Tempest

### Test Results
- **FPGA ADC Performance:** Successfully logged 10 kHz sine wave at 80 MHz sampling; tested up to 10 MHz signals
- **Spurious features noted:** 8k-point FFT analysis revealed certain spurious features on one channel requiring further investigation
- **Data logging status:** ADC, UART, and time tick data logging functional; intermittent gaps in continuous logging blocks under investigation

### Outstanding Issues
- **EMI improvements:** Anechoic chamber testing of copper mesh and shielded cable modifications planned for remainder of Phase II-E
- **Radio selection:** Testing of alternative 900MHz and 2.4GHz radio options to replace XTend still pending
- **FPGA data logging gaps:** Root cause of brief logging interruptions between continuous data blocks not yet identified
- **ADC spurious features:** Source and impact of spurious features in FFT spectrum under investigation

## Notable Details

### Manufacturing & Cost Improvements
- New nose cone production method (female mold wet layup) reduced cost from $3,000 to $350 per unit (8.6x reduction)
- Weight reduction of 151g per nose cone improves payload capacity and flight time
- Self-interlocking fuselage interior design reduces manual assembly labor
- Modular nose cone design (with guide holes) allows production of different lengths from single mold

### Design Flexibility for Future Missions
- Battery mounting flexibility designed to accommodate rapidly evolving battery technology (LiHV vs. standard LiPO)
- Dual battery locations enable increased flight endurance or center-of-gravity adjustment for different payloads
- Modular nose cone concept explicitly noted as "very advantageous for missions beyond soil moisture mapping"

### Testing Site Selection Rationale
- Pawnee National Grasslands selected as primary testing location despite lacking in situ sensors because Phase II-E goal is EMI noise reduction, not absolute calibration
- Site closer to Boulder (90 min vs. remote location) enables repeat testing and timing around precipitation events
- Secondary site near Yuma, CO available if validation against in situ sensors becomes necessary

### Certification Pathway
- Noted that adding new sites to NASA Goddard COA (Certificate of Authorization) is straightforward, requiring only updated flight test plans
- Suggests Phase II-E testing can expand to multiple sites as needed