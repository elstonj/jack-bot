# Development of a SL UAS with Advanced MAD and Acoustic Sensing Capabilities – Phase I Option Period Progress Report

## Document Metadata
- **Type:** SBIR/STTR Progress Report (Phase I Option Period)
- **Client/Agency:** Department of the Navy / NAVAIR
- **Program/Solicitation:** SBIR Topic N251-016; Proposal N251-016-0021
- **Contract Number:** N6833525C0492 CLIN0006
- **Date:** June 29, 2026
- **Reporting Period:** March 23, 2026 – June 29, 2026
- **BST Products/Systems Referenced:** S0-UAS, S0-MAD (Sonobuoy-Launched Unmanned Aerial System with Magnetic Anomaly Detection payload)
- **Key Personnel:** Dr. Jack Elston (Principal Investigator), Dr. Stachura, Meredith Needham
- **Security Classification:** Unclassified; ITAR Restricted; Distribution Statement B
- **Data Rights Expiration:** March 23, 2046

---

## Executive Summary
This progress report documents BST's Phase I Option Period work on developing a Sonobuoy-Launched UAS (S0-UAS) equipped with advanced Magnetic Anomaly Detection (MAD) and acoustic sensing capabilities for the U.S. Navy. The effort bridges Phase I feasibility demonstrations to Phase II integrated prototype development, focusing on maturing magnetometer integration, designing a reusable ground-launched flight-test variant, and preparing for a Navy Technical Capability Evaluation (TCE) in August 2026.

---

## Technical Approach

### Overall Strategy
The Option Period is structured around three primary objectives:
1. **O.1:** Comparing and integrating alternate magnetometer sensors (QuSpin vs. Bartington UAS-MAG)
2. **O.2:** Designing a reusable, ground-launched S0-MAD aircraft variant and elastic launch system
3. **O.3:** Preparation for Navy TCE demonstration (August 2026)

The approach transitions the system from an expendable, air-deployed platform to a reusable, locally-testable configuration while maintaining the magnetic signature critical to end-product validation.

### Key Technical Details

#### O.1: Magnetometer Integration

**QuSpin Sensor Efforts:**
- Phase I achieved magnetic noise floor below Navy's 20 pT/√Hz requirement in controlled laboratory and static ground environments
- Recent ground testing revealed elevated noise levels across frequency ranges (1-10 Hz: 60.1 pT/√Hz vs. historical 4.1 pT/√Hz; 10-50 Hz: 47.9 vs. 4.3; 50-100 Hz: 34.0 vs. 4.2)
- Root cause suspected to be voltage ripple in QuSpin power supply
- Current issue: sensor hangs on initialization and calibration; BST working directly with QuSpin to resolve

**Bartington UAS-MAG Sensor Development:**
- Previous testing limited data to 16-bit precision via DroneCAN interface, insufficient to meet program requirements
- **Solution:** Custom ADC interface board designed using Texas Instruments ADS131M08 ADC providing 24-bit precision
- **Power Architecture:** Four separate supplies (Bartington sensor, ADC digital, ADC analog, Raspberry Pi) with ultra-low-noise, high PSRR low-dropout regulators to minimize ripple current
- **Layout:** Analog inputs, digital circuitry, and power supplies physically separated; metal components kept away from sensor element
- **Status:** ADC boards expected to arrive early week of July 6, 2026; testing pending

#### O.2: Reusable S0-MAD Aircraft Design

**Airframe Modifications:**
The S0-UAS baseline has ~1.3 kg nominal flight weight. Modifications required:
- **Lighter** (flattened glide slope, reduced stall speed for belly landings)
- **Structurally improved** (withstand repeated belly landings)
- **Dimensionally and propulsively identical** (preserve magnetic signature)

**Battery Swap:**
- Replaced 6S, 6500 mAh battery (high-endurance) with 6S, 2000 mAh
- Weight savings: ~350g
- Wing loading reduction: 30%
- Stall speed reduction: ~20%
- Trade-off: Flight time reduced from 2 hours to ~30 minutes (acceptable for iterative testing)
- Charging faster than refurbishment cycle

**Wing Reinforcement:**
- Original wing insufficient for repeated belly landings
- New design: structurally reinforced with additional internal ribs and multi-layered carbon fiber skin
- Weight penalty: only +30g (negligible compared to battery savings)
- Identical external appearance

**Antenna Replacement:**
- Original: 430 MHz folding antenna with 200+ mile range (tendscavage ground on landing)
- New: Lightweight adhesive 430 MHz antenna with 20 mile range (sufficient for local testing)
- Eliminates landing snag issues

**Elastic Launch Rail System:**

*Design Requirements:*
- Minimum exit velocity: 16 m/s for 1.3 kg aircraft
- Portable (packable into checked baggage)
- No active electronic components
- Approximate 10g peak loading observed during SLC tube deployment

*Architecture:*
- 2.5 m launch rail using two extra-extension elastic springs
- Tuned preload: 10.6g peak load, 16.7 m/s exit velocity
- 2-to-1 pulley block arrangement allows springs to sit below rail (extends only half aircraft travel distance)
- Parametric design tool created for real-time optimization of launch characteristics (rail length, spring rate, preload, angle)
- Off-the-shelf aluminum extrusion components for adjustability and field reassembly
- Disassembles into primary components for shipping

*Status:* Initial manufacture and assembly complete; dummy weight and airframe launch tests pending

---

## Products & Capabilities Described

### S0-UAS (Sonobuoy-Launched Unmanned Aerial System)

**Description:**
A small, expendable unmanned aerial system designed for deployment via sonobuoy launch tubes from maritime platforms. Originally developed for sonobuoy deployment (air-deployed); Option Period focuses on ground-launch variant for testing.

**Phase I Achievements:**
- Demonstrated magnetic noise floor <20 pT/√Hz in controlled environments
- Fundamental viability established for MAD payload integration

**Phase I Option Period Configuration (S0-MAD):**
- Baseline weight: ~1.3 kg (with high-endurance battery)
- Modified flight-test variant: ~950 g (with reduced-capacity battery)
- Flight time (reusable variant): ~30 minutes
- Antenna range: 20 miles (ground-test variant)
- Propulsion and avionics placement identical to air-deployed version (magnetic signature preservation)

### S0-MAD Payload

**Magnetometer Options Being Evaluated:**

1. **QuSpin Sensor:**
   - Previously meeting Navy requirement (<20 pT/√Hz noise floor) in controlled conditions
   - Current integration issue with power supply noise and initialization
   - Integration approach: Direct Raspberry Pi interface

2. **Bartington UAS-MAG Sensor:**
   - Rated sensitivity must be achieved via custom ADC interface (24-bit precision)
   - Part of UK Project RAVEN integration (Merlin Mk2 helicopter platform)
   - Custom ADC board with separate power supplies and noise filtering
   - Expected to integrate into S0-MAD for flight testing

**Acoustic/Infrasonic Sensing:**
- Government raised expansion to include acoustic channel on same Raspberry Pi interface as magnetometer (S0-Acoustic configuration)
- Would broaden platform applicability to NAVAIR acoustic-sensor customers
- Requires self-noise characterization and IMU-aided vector compensation (scoping for future consideration)

---

## Use Cases & Applications

### Primary Mission: Anti-Submarine Warfare (ASW)
**Naval Application:**
- Detection of submarine magnetic anomalies via MAD sensor
- Sonobuoy-launched deployment from maritime patrol aircraft and helicopters

### Navy TCE (Technical Capability Evaluation)
- **Venue:** August 2026 (initial); Northern Edge 2027 (June 2027) identified as Phase II window with instrumented underwater target for end-to-end MAD detection testing
- **Demonstration:** S0-MAD prototype data collection and operational validation
- **Venue:** Camp Pendleton (mentioned for TCE participation)

### International Application: UK Project RAVEN
**Platform:** Merlin Mk2 Helicopter Force (UK Ministry of Defence)
- **Start Date:** July 1, 2026
- **Duration:** Two-year funded program
- **Prime Integration Lead:** Lockheed Martin UK
- **Payload:** Bartington MAD sensor (UK-supplied)
- **Form Factor:** NATO A-size-compatible outer diameter ~12.5 cm for gravity launch from Merlin carousel
- **Scope:** Potential extension to other UK maritime platforms
- **Coordination:** ONR Global London facilitating US–UK coordination

---

## Key Results & Technical Findings

### Phase I Achievements (Baseline for Option Period)
- Demonstrated magnetic noise floor <20 pT/√Hz in laboratory and static ground conditions
- Fundamental viability of S0-UAS + MAD concept established

### Option Period Progress (as of June 29, 2026)

**Magnetometer Testing:**
- **QuSpin Issue Identified:** Recent ground tests show elevated noise (60.1 pT/√Hz at 1-10 Hz range vs. 4.1 pT/√Hz historically)
  - Root cause: suspected voltage ripple in power supply
  - Resolution: working with QuSpin on initialization/calibration fixes
  
- **Bartington ADC Integration:** Custom ADC board designed with 24-bit precision
  - Power architecture: Four isolated supplies with ultra-low-noise regulation
  - Expected delivery: early July 2026
  - Testing to begin immediately upon arrival

**Airframe Modifications:**
- Lightweight battery swap: 350 g weight reduction achieved
- Wing reinforcement: designed with only +30 g penalty
- Antenna replacement: low-profile design tested and ready
- All modifications maintain magnetic signature compatibility

**Launch System:**
- Parametric design tool created and validated
- Elastic launcher manufactured and assembled
- Design specifications: 2.5 m rail, 10.6 g peak load, 16.7 m/s exit velocity
- Status: awaiting dummy weight and airframe launch tests

### Technical Issues Identified

1. **QuSpin Power Supply Noise:** Elevated noise floor in recent tests; initialization hang on new power supply; resolution in progress with vendor

2. **Bartington ADC Board Delays:** Unexpected delays in board assembly; expected early July 2026

3. **Bartington Testing on Hold:** Additional magnetometer testing paused pending ADC board arrival and integration

---

## Notable Details

### Government Collaboration (NAWCAD)
- Engagement escalated from programmatic check-ins to direct engineer-to-engineer collaboration with NAWCAD Airborne ASW Battlespace Division (AC15400)
- Government provided:
  - Bartington ADC reference design
  - Sensor noise-floor references
  - Loaned Bartington UAS-MAD sensor
  - Procured additional sensor unit for BST
  - Offered access to magnetic test chamber for baseline characterization
- Government raised acoustic/infrasonic payload expansion concept (S0-Acoustic)

### Phase II Competition Status
- BST invited to submit full Phase II proposal (Proposal No. N2-9618) after Phase I technical review
- Submitted March 27, 2026
- Down-selected as one of two performers for full Phase II proposal stage
- Proposal in Government evaluation

### Transition Pathway to Production
**US Navy Path:**
- Option Period structured to establish technically integrated, demonstration-validated baseline for Phase II
- Northern Edge 2027 (June 2027) identified as experimentation venue with instrumented underwater target for end-to-end MAD testing

**UK MOD Path (Project RAVEN):**
- Funded two-year program starting July 1, 2026
- Lockheed Martin UK as prime and Merlin Mk2 integration lead
- BST engaged in vendor onboarding and statement of work with LMUK
- Form-factor targeting: NATO A-size compatible, ~12.5 cm outer diameter for Merlin carousel gravity launch
- UK-supplied Bartington MAD sensor reinforces Option Period Bartington integration priority

###