# NASA 777 Integration: ERAU Wind Tunnel Test Planning

## Document Metadata
- Type: Internal planning document / decision memo
- Client/Agency: Internal BST (NOAA, NASA Langley, ERAU involved externally)
- Program/Solicitation: NASA 777 integration program; S0 high-altitude launch platform
- Date: 13 October 2026 (draft started)
- BST Products/Systems Referenced: S0 (aircraft), MHP (Multi-Hole Probe sensor system)
- Key Personnel: Jack Elston (BST lead on this doc), Joe Cione, Maciej (wings-on testing), Craig Hunter (NASA LaRC, Configuration Aerodynamics), Nick Pawlenko (NOAA OMAO), Chester Dolph (NASA legal coordination), Annette Hollingshead (NOAA), Josh Wadler (ERAU contact), Dr. Eb Gnanamanickam (ERAU tunnel director), Zheng Zhang (ERAU), Joe Cione

## Executive Summary
BST is planning a return to Embry Riddle Aeronautical University (ERAU) MicaPlex wind tunnel to test the S0 aircraft as a payload for NASA's Boeing 777 high-altitude launch platform. The document outlines BST's internal decision-making on which tests to run, how to structure IP ownership, and cost/data-sharing arrangements with NASA and NOAA before committing to tunnel time. Key tensions: MHP sensor architecture choices, NDAA compliance requirements, wings-on test scope, and protecting BST proprietary data from NASA licensing claims.

## Technical Approach

### Wind Tunnel Testing Context
- ERAU MicaPlex is a closed-return tunnel with heat exchanger; stable at 20 ft/s (Re/ft ~1.3 × 10⁵ at standard conditions), typically run 30–50 ft/s
- No hot-wire turbulence data available at low end
- Test section span limit: 4 ft (constrains full-span S0 wing testing)
- Tunnel instrumentation: airspeed, dynamic pressure q, static pressure, temperature, pitch/yaw (no humidity logging)
- Previous test (Feb 2023): S0 fuselage with MHP, 516-point matrix (alpha/beta ±14° at 1° steps inside ±8°, at 22.5 m/s and 26 m/s coarser grid), ~4.3 hours data collection over ~2 days, no BST personnel on-site
- Data logging: onboard at 100 Hz, USB retrieval

### MHP Sensor Calibration Issues (Section 3.1)
**Current Problem:** 2023 calibration used incorrectly scaled sensor inputs; firmware applied wrong scaling to wrong sensors (center scaled 0–2 inH₂O, one outer scaled 0–5 inH₂O). Calibration coefficients work but were fit to mis-scaled raw data.

**Proposed Fixes:**
- Verify firmware scaling on bench before shipping (known pressure applied to each port)
- Repeat full 2023 matrix with correct scaling to compare old vs. new coefficients directly
- Add low-speed points near 20 ft/s floor to characterize sensor behavior at small differential pressures (relevant to high-altitude deployment where same true airspeed yields much lower dynamic pressure)

**Current MHP Configuration (5 sensors):**
- Four differential sensors (MS4515DO-DS3BS002DS, ±2 inH₂O) measuring between static and each side port
- One gauge sensor on center port (MS4515DO-DS3BS005GS, 0–5 inH₂O)

### MHP Sensor Architecture Trade (Section 3.2)
**Proposed 3-Sensor Configuration:**
- Two differential sensors (port 1→3 and port 2→4 direct measurement)
- One center gauge sensor
- Remove two of the static-referenced differential sensors

**Analysis:**
- **5-sensor benefit:** Redundancy—clogged port with rain can be estimated, no loss of angle estimate
- **3-sensor drawback:** No clogging detection; single clogged port corrupts angle estimate with no diagnostic
- **Testing approach:** Run 3-sensor board alongside 5-sensor board on same matrix; include degraded-port case (one side port blocked during part of matrix) to show observability difference
- Caveat: Post-processing 3-sensor result from 5-sensor data does not replicate noise and range of physical single sensor; direct hardware comparison needed for fair evaluation

**Unresolved:** Exact 3-sensor layout and whether side-to-top/bottom differentials could be formed using only center sensor (needs specification before board spin)

### NDAA Compliance Sensor Replacement (Section 3.3)
**Problem:** MS4515 pressure sensors have country-of-origin compliance issues for autopilot and MHP hardware (listed in BST compliance workbook).

**Approach:**
- Identify and confirm country of origin for candidate replacement sensor(s) before board spin
- Run replacement sensor side-by-side with MS4515 on same matrix for direct calibration comparison
- Verify replacement covers low-pressure range required for high-altitude glide case
- Candidate sensor: TBD

### S0 Deployment Aerodynamics (Context)
- S0 will be deployed from NASA 777 at Mach 0.8 at FL400 (~43,000 ft)
- Comms range: ~150–200 nmi depending on S0 altitude (Jack to provide link budget once 777 antenna setup known)
- S0 chord Reynolds number at FL300–FL430 is very low (motivating slow end of tunnel for Re matching)
- 75% scale model at 20 ft/s approximates full-scale low-Re condition
- Jack's assessment: deployment may hinge on tube timing (decelerating S0 before parachute opening), then launch normal; S0 will glide from altitude but cannot sustain flight above ~25 kft
- NASA proposed building CFD of S0 first (high-altitude, low chord Re), later couple to launch CFD from 777

### Wings-On Testing (Section 3.4, Maciej lead)
**Constraint:** Full-span S0 does not fit 4 ft test section limit; full span is 54.6 in (4.55 ft).

**Options:**
- 75% scale model (matches Craig's Re recommendation)
- Reduced-span or half-span article
- Different tunnel

**Requirements:**
- Stronger mount than 2023 (was flagged by ERAU last time for 3D-printed nylon, lacked static stress analysis)
- Basic load analysis required
- Test should include: force and moment, laminar/turbulent boundary layer detection on upper wing surface, possibly transition trip to raise CLmax, possibly wing pressure taps for CFD validation (per Craig's direction)

**Decision Pending:** Whether this test runs as BST item (BST data) or as separate NASA-led entry; directly overlaps with what NASA/NOAA want

## Products & Capabilities Described

### S0 Aircraft
- Small, high-altitude capable UAS (payload for NASA 777 drop launch)
- Can be configured with or without swivel wings
- Equipped with MHP for atmospheric sampling/measurement
- Will deploy from ~43,000 ft (FL400)
- Can glide from altitude but ceiling ~25 kft
- Fuselage dimensions: fuselage-only model fit ERAU tunnel; wings span 54.6 in (exceeds 4 ft span limit)

### MHP (Multi-Hole Probe) System
**Function:** Measures air velocity magnitude and direction (angle of attack, angle of sideslip) via pressure ports and differential pressure sensors.

**Current 5-Sensor Build:**
- 5 pressure ports (center, top, bottom, left, right on fuselage)
- 4 differential sensors (static-referenced outer ports) + 1 gauge (center)
- Firmware-logged at 100 Hz
- USB data retrieval
- Requires calibration matrix relating pressure differences to flow angles and airspeed

**Performance Specs from 2023 Test:**
- Tested alpha/beta range: ±14° (1° steps inside ±8°)
- Speeds: 22.5 m/s (main matrix), 26 m/s (coarser), planned expansion to 20 ft/s low-speed points
- Sensor resolution constraints: low-q behavior at altitude not yet characterized

**Issues Identified:**
- Incorrect firmware scaling in 2023 (coefficients still valid but fit to wrong sensor inputs)
- Country-of-origin compliance risk (MS4515 sensors)
- Sensor redundancy vs. cost trade-off (5 vs. 3 sensor debate)
- Limited observability of clogged/contaminated ports in 3-sensor config

## Use Cases & Applications

### NASA 777 High-Altitude Platform Mission
- **Primary Use:** S0 deployed from Boeing 777 at Mach 0.8, FL400 (~43,000 ft) over ocean or other target
- **Measurement Objective:** Atmospheric sampling (velocity, angle measurements via MHP)
- **Deployment Scenario:** Payload release and glide from high altitude; must slow tube before parachute deployment
- **Operating Envelope:** FL300–FL430 (cruising/glide altitudes)
- **Comms:** Radio link degradation expected >150–200 nmi depending on altitude

### Wind Tunnel Testing (ERAU MicaPlex)
- **Validation:** MHP calibration at representative low-Reynolds-number flight conditions
- **Aerodynamic Characterization:** Force/moment, boundary layer state, laminar-to-turbulent transition
- **Sensor Development:** Qualification of NDAA-compliant replacement sensors, redundancy architecture assessment

## Key Decisions Required

### Internal BST Decisions
1. **Which test items to pursue** (Section 3): Prioritize recalibration (Run A), 3-sensor comparison (Run C), NDAA sensor replacement (Run D), degraded-port observability (Run E), and wings-on (Run F, if scope settled)
2. **Contractual structure:**
   - **Option A (Jack's preferred):** BST runs tests 3.1–3.3 as separate BST entry under BST's own NDA/testing agreement with ERAU; calibration data, coefficients, sensor results remain BST proprietary
   - **Option B:** Combined NOAA/NASA entry (cheaper government rate $230/hr vs. $600/hr non-gov, but data rights ambiguous)
3. **Payment responsibility & rate:**
   - BST at $600/hr (non-government) keeps data proprietary
   - NOAA at $230/hr (government rate) requires data rights clarity
   - Josh Wadler raised open question: how does billing work (ERAU pays and invoices, or direct?)
4. **NASA involvement scope:**
   - Keep NASA force-and-moment work (wings-on, CFD coupling) as separate scoped entry
   - Delay CAD sharing until formal agreement (SAA or MOA) addresses IP and licensing
   - Send Chester Dolph specific BST IP requirements now (SAA approvals take ~6 months)
5. **Sensor architecture:**
   - Keep 5-sensor MHP or move to 3-sensor design (decision should be informed by tunnel data)?
   - Jack's lean: keep 5 for robustness unless data shows otherwise

### External (NASA/NOAA) Decisions
- **IP Protection:** NASA legal (Chester) to formalize with SAA or MOA; Chester offered to take BST requirements to NASA legal
- **NOAA Technology Partnership Office:** Annette Hollingshead to seek IP guardrails approach
- **Wings-on test ownership:** Whose design, who pays, who owns data (BST vs. NASA)?
- **G-III alternate launch platform:** June discussion noted G-III as possible (8 psi vs. 9 psi cabin diff); May position was BST should not pay NASA fee (not yet resolved)

## Notable Details

### Compliance & Logistics
- **NDAA Country-of-Origin Issue:** MS4515 sensors non-compliant; must qualify replacement for autopilot and MHP
- **Model Certification:** ERAU requires:
  - Certificate of insurance (BST legal coverage)
  - Model certification form (flagged mount stress analysis last time)
  - NDA and testing agreement with Dr. Eb Gnanamanickam (tunnel director) before scheduling
  - MicaPlex test information form
- **Mount Design:** Previous 3D-printed nylon mount lacked static stress analysis; new design needs load analysis; 