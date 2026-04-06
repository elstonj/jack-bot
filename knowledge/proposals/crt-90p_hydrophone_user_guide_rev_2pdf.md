# CRT-90P Hydrophone User Guide Rev 2

## Document Metadata
- Type: User Guide / Technical Manual
- Manufacturer: Cetacean Research Technology (CRT)
- Document Version: Rev. 2 (01/2025); User Guide Rev. 5 (12/2024)
- Context: Found in BST Navy SBIR Magnetometer Phase I proposal folder as a subcontract reference
- Last Editor: Maciej Stachura
- Contact: +1(330) 419-2520 | crtinfo@cetrestec.com | www.cetrestec.com

## Executive Summary
This is a technical user guide for the CRT-90P hydrophone, a submersible acoustic sensor designed for underwater sound recording and monitoring. The document provides operational instructions, specifications, deployment guidance, and wiring information for researchers and field operators using the device.

## Products & Capabilities Described

### CRT-90P Hydrophone
**What it is:**
- Submersible acoustic sensor (hydrophone) designed for underwater sound detection and recording
- Wetmate connector system (MCBH3MSS) for subsea deployment
- Battery-powered or external DC power operation

**Operational Specifications:**
- **Linear Frequency Range (±3dB):** 0.006–50 kHz
- **Useable Frequency Range (+3/-12dB):** 0.002–90 kHz
- **Transducer Sensitivity:** -184 dB (re 1V/μPa)
- **Preamplifier Gain:** 30 dB
- **Effective Sensitivity:** -154 dB (re 1V/μPa)
- **Equivalent Noise Floor (@ 9V operation):**
  - 42 dB @ 0.1 kHz
  - 25 dB @ 1 kHz
  - 15 dB @ 10 kHz
  - 12 dB @ 20 kHz
  - 10 dB @ 50 kHz
- **Power Requirement:** 3.3–36 VDC
- **RMS Overload Acoustic Pressure:** 159–179 dB (re 1μPa)
- **Maximum Operating Depth:** 990 m
- **Operating Temperature Range:** -40 to +85°C
- **Output Impedance:** 10 Ω
- **Directionality:** Omnidirectional below 20 kHz
- **Dimensions:** 102.9 mm length × 25.4 mm outer diameter

**Signal Output:**
- XLR connector on battery box for connection to data acquisition systems, digital recorders, mixers, PA amplifiers, or computer sound cards
- DC voltage offset at output approximately equal to half the power supply voltage
- Optional 500 Hz high-pass filter box accessory available for noise reduction

## Technical Approach: Deployment & Operation

**Power Configuration:**
- Two 9V batteries installed in battery box (primary method)
- Alternative: External DC power supply (3.3–36 VDC, regulated, max 0.5V ripple)
- **Critical:** Phantom power must be OFF if using battery box; use isolated power supply if connecting to AC-powered input devices

**Deployment:**
- Submerge hydrophone sensor end minimum 10 feet (3 m) below surface
- DO NOT submerge battery box
- Glow-blue power indicator on switch
- Self-noise is ~10 dB+ below sea-state zero across full bandwidth

**Cable Connectors:**
- **Hydrophone End:** MCIL3F wetmate connector (male)
  - Pin 1: Hydrophone power (3.3–36 VDC)
  - Pin 2: Ground/common (also shields connector shell)
  - Pin 3: Hydrophone output signal
- **Topside End:** XLR IP67-rated connector (male)
- Cable replacement: Loosen locking sleeve, lubricate connector pins with Molykote 44 Medium silicone-based grease, hand-tighten locking sleeve

**Noise Reduction Techniques:**
- Create S-shaped cable bend ~3 feet (1 m) from hydrophone, hold with rubber bands to dampen cable vibrations
- Wrap soft cloth around cable where it contacts boat
- Use ~2 kg weight with rope ~1 m above connector, taped to cable (NOT tied directly)
- Includes low-noise deployment configuration diagram with buoy, rope, and weight positioning

**Maintenance:**
- Rinse with fresh water after use; dry thoroughly
- Do NOT expose sensor end to direct sunlight when out of water (temperatures >194°F/90°C permanently decrease sensitivity)
- Do NOT disconnect hydrophone from cable unless replacement needed

## Wiring Instructions (Non-Battery Box Operation)

For users not using the CRT battery box, manual wiring connections required at static-safe workstation:
- **Pin 1 & XLR Pin 2:** Hydrophone power (3.3–36 VDC from battery or regulated supply)
- **Pin 2:** Ground/common (power, signal, shield ground; connect to data system ground if experiencing ground loop interference)
- **Pin 3:** Output signal (use blocking capacitor if needed)
- **Low-frequency roll-off:** Determined by input impedance (R) and blocking capacitor (C) per formula f = 1/(2πRC)

## Notable Details

- **Warranty:** 90-day limited warranty; voids if cable damaged or if connected to AC-powered device without isolation transformer or if powered by phantom power
- **Model/Serial Number Location:** On stainless steel connector
- **Design Context:** Integral stainless steel wetmate connector shell serves as ground reference
- **Deployment Supply List:** Nylon rope (~3/8"), ~2kg+ weight, buoy, waterproof tape, anchor
- **Historical Note:** Document shows generic template language ("<INSERT COMPANY NAME HERE>") suggesting CRT uses standardized drawing templates

**Relationship to BST:** This hydrophone specification appears in the Navy SBIR magnetometer proposal folder, suggesting CRT-90P may be considered as a complementary or reference sensor for underwater sensing applications in BST's magnetometer research.