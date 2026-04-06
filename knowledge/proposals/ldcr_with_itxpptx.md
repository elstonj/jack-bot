# LDCR With ITX Testing Document

## Document Metadata
- Type: Test plan / technical presentation
- Client/Agency: NASA
- Program/Solicitation: SBIR Phase II-E, Soil Moisture topic
- Date: Created/Modified January 8, 2017
- BST Products/Systems Referenced: LDCR (L-band Downconverter Receiver), ITX Computer, SSD
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
This document outlines a series of electromagnetic compatibility and integration tests (Tests 26-34) for BST's LDCR (L-band Downconverter Receiver) system paired with an ITX industrial computer. The tests progress from controlled laboratory conditions to real-world airborne integration, systematically evaluating RF shielding effectiveness, antenna performance, and system operation in an aircraft frame with various electrical systems active.

## Technical Approach
Systematic testing progression across nine test cases designed to isolate variables:
1. **Laboratory baseline tests** (26-31): Evaluate LDCR and ITX computer performance with and without RF shielding, using both matched loads and antenna configurations
2. **Integration tests** (32-34): Mount shielded LDCR/ITX system in aircraft frame with increasingly realistic operational conditions:
   - Test 32: Baseline airborne configuration (all aircraft electronics off, motor off)
   - Test 33: Aircraft electronics energized, motor off
   - Test 34: Full aircraft operation (electronics and motor on)

## Products & Capabilities Described

**LDCR (L-band Downconverter Receiver)**
- RF receiver system operating at L-band frequencies
- Can be housed in shielded enclosure to manage electromagnetic interference
- Tested with antenna input for signal reception
- Capable of receiving matched load signals for baseline measurements

**ITX Computer**
- Industrial computing platform used as control/processing unit
- Integrated with LDCR system
- Tested both shielded and unshielded configurations
- SSD (solid-state drive) storage for data logging
- Successfully operates in aircraft electrical environment

## Use Cases & Applications
- Airborne soil moisture measurement (NASA SBIR context)
- L-band radiometer system requiring integration with aircraft platforms
- Applications requiring RF signal reception in electromagnetically noisy environments (aircraft with active electrical systems, motors)

## Notable Details
- Progressive environmental complexity: from RF-shielded box to open aircraft frame
- Identifies RF shielding as key mitigation for electromagnetic interference
- LDCR housing shielding was implemented by Test 30 onwards, suggesting earlier tests identified shielding necessity
- Testing included motor operation (Test 34), indicating potential motor-generated RF interference was a concern
- Tests conducted outside shielded box in final three iterations, demonstrating real-world operational validation