# S0 Direct-to-Cell (Starlink Mobile) Pilot — Brainstorm ROM

## Document Metadata
- Type: Whitepaper / Rough Order of Magnitude (ROM) planning document
- Client/Agency: NOAA
- Program/Solicitation: WP-BST-006 (Uncrewed S0 Carrier Aircraft); proposed as Task 13
- Date: 2026-10-20 (created); 2026-10-27 (last modified)
- BST Products/Systems Referenced: S0 (uncrewed aircraft); WP-006 carrier aircraft
- Key Personnel: Jack Elston

## Executive Summary
This document proposes a three-phase, ~30-month integration of Starlink direct-to-cell (D2C) connectivity onto the S0 uncrewed aircraft, with a total ROM of ~$680K ($549K NRE + $130K airframes). Phase 0 (~$47K, 4 months) assesses feasibility and authorization pathways; Phase 1 ($252K, 9 months) demonstrates Gen1 T-Satellite capability within 12 nm of US coast; Phase 2 ($250K, 12 months) transitions to Gen2 Starlink Mobile for storm operations in 2028. The proposal structures funding as separable gates so NOAA avoids paying for integration against hardware or authorizations that may not materialize.

## Technical Approach

**Core Architecture:**
- 3GPP Release 17 NTN (non-terrestrial network) modem module on a custom carrier board, with omnidirectional 2 GHz antenna element
- Module does not fit existing 45.7 mm S0 payload bay (Telit FN990B40 is ~30 × 52 mm M.2 form factor); new carrier-board spin required (analogous to prior Iridium integration under SOW A)
- 800 MHz as a stretch goal; antenna efficiency on small airframe is a known risk
- Data packing and decimation to stay within service caps
- Shore endpoint to feed existing NOAA data pipeline

**Spectrum and Service Evolution:**
- **Gen1 (T-Satellite):** T-Mobile PCS G-block (LTE Band 25), 1910–1915 MHz up / 1990–1995 MHz down; available now; usable within 12 nm of US coast; 15 MB/month IoT test cap (~20 minutes of full-rate S0 data at 100 kbps)
- **Gen2 (Starlink Mobile V2):** Announced 8 Oct 2026; ~65 MHz at 2 GHz spectrum (purchased from EchoStar) plus up to 14 MHz low-band (800 MHz); launches late 2027; EchoStar spectrum usable after ~30 Nov 2027; claimed up to 150 Mbps per user (shared beam); no IoT module announced yet

**Authorization Strategy:**
- Phase 1 flights within 12 nm require no STA (Special Temporary Authority); beyond 12 nm requires FCC ESAA STA (under review as of Aug 2026)
- Airborne use of terrestrial cellular spectrum unresolved
- Gen2 terms for aircraft unconfirmed
- Assumption: NOAA or T-Mobile (via NOAA/T-Mobile CRADA) arranges service access, test SIMs, airtime, and any STA; BST provides technical support only

## Products & Capabilities Described

**S0 (Uncrewed Aircraft):**
- Small uncrewed platform with 45.7 mm payload bay
- Returns science data to shore; proposed integration enables data return without host aircraft in radio range
- Existing airframe order available at Ordering Period 2 price ($18,630/unit)
- If carrier aircraft (WP-006) proceeds, D2C link becomes candidate backhaul

**Starlink Direct-to-Cell Service (Partner: T-Mobile / SpaceX):**
- Gen1 (T-Satellite) testable now; Gen1 offshore reach 12 nm; data cap 15 MB/month for IoT
- Gen2 launches late 2027; higher data rate and extended reach (details TBD)
- FCC waived carrier-lease rule, enabling SpaceX direct sales (as of Oct 2026)

## Use Cases & Applications

- **Primary Mission:** Return meteorological and health telemetry from S0 flights to NOAA shore endpoint feeding existing data pipeline
- **Phase 1 Target:** Coastal and near-shore operations within 12 nm, or expanded range under STA authorization
- **Phase 2 Target:** Storm sampling from P-3 aircraft using Gen2 Starlink Mobile; higher data rate modes enable potential live video from storm core (scoped post-Phase 2)
- **Carrier Aircraft Backhaul:** If WP-006 uncrewed carrier proceeds, D2C link serves as beyond-line-of-sight backhaul candidate (not included in this ROM)

## Proposed Tasking & Gates

**Phase 0 — Feasibility and Pathway ($46.8K, 4 months)**
- Trade study and concept of operations (CONOPS)
- STA and spectrum authorization pathway support
- Link budget closure for airborne S0
- Data product and cadence definition with NOAA
- Test plan, report, program management
- **Gate:** Module that fits after carrier-board spin; credible authorization path

**Phase 1 — Gen1 T-Satellite Pilot ($252K, 9 months)**
- Module integration and custom carrier board spin
- Band 25 antenna design and fabrication
- Data packing under 15 MB/month cap
- Shore endpoint integration into NOAA data path
- Bench and flight testing
- Power and endurance characterization
- Documentation and PM
- 3 S0 airframes expended/flown
- **Gate:** Measured link availability and throughput from flying S0
- *Optional savings:* If Iridium BLOS task (SOW A) funded first, reuse data-packing logic and routing (~$40–65K savings); or stop at bench/coastal ground test with no S0 flight (~$35K savings)

**Phase 2 — Gen2 Integration and Storm Demonstration ($250.4K, 12 months)**
- Gen2 module swap once available; second carrier-board spin
- Antenna retune for Gen2 bands
- Higher-rate firmware modes
- EMI/EMC and tube-launch requalification
- Power/endurance characterization
- P-3 test flights and travel
- 4 S0 airframes expended in demonstration
- Documentation and PM
- **Gate:** Gen2 module availability and service access (not before early 2028)

**Airframes:** 7 S0 at $18,630 each = $130.4K (plus module cost delta TBD)

## Key Results (Preliminary)
This is a planning/brainstorm document, not a report with results. No data or test outcomes are presented; the document is forward-looking and lays out the ROM contingent on successful completion of each phase gate.

## Assumptions, Risks, and Exclusions

**Assumptions:**
- NOAA or T-Mobile arranges service access, test SIMs, airtime, and any STA; BST provides technical support
- Airframes from Government-furnished NOAA order or purchased at Ordering Period 2 price
- Labor at IDIQ 1305M226D0012 Tab 2 rates, no fee applied

**Risks:**
- **Authorization:** 12 nm limit, airborne use of terrestrial cellular spectrum, and Gen2 aircraft terms all unresolved; any can stop Phase 1 flights or delay Phase 2
- **Partner of Record:** SpaceX now sells service without carrier intermediary; AT&T, Verizon, T-Mobile formed own satellite-to-phone venture (2 Oct 2026); T-Mobile path to Gen2 uncertain
- **Device Availability:** No Gen2 module exists; size and power unknown; part that does not fit ends effort at gate
- **Endurance and Antenna:** Second transmitter at handset power shortens endurance (to be characterized, not committed); omnidirectional element on rolling airframe and 800 MHz efficiency on small body are open questions

**Exclusions (separately scoped/quoted):**
- Live video from storm core (possible with Gen2, pending Phase 2 throughput validation)
- Beyond-line-of-sight command and control over D2C
- Integration on WP-006 carrier aircraft backhaul (Task 5 trade study separate)
- Recurring airtime/service post-delivery; FCC filing fees
- Production configuration, technical data package per IDIQ §5.7, spares

## Notable Details

- **Cost Basis:** Estimates reuse bottom-up lines from BST August 2026 response to NOAA SATCOM/C2 draft SOW (lines A-1 to A-13) and S0 video assessment (B-lines); same airframe, same 45.7 mm bay problem, same "new radio on new board" challenge
- **Schedule Realism:** Phase 1 can fly in 2027 season on Gen1; Phase 2 realistically in 2028 season, moving with SpaceX milestones
- **Separable Value:** Proposal frames D2C as WP-006 Task 13 such that if uncrewed carrier stalls on permissions or technology, S0 still delivers science data without host aircraft in radio range; if carrier proceeds, link becomes backhaul candidate
- **Partner Path:** Leverages existing NOAA/T-Mobile CRADA; June–July 2026 technical work with T-Mobile confirmed Gen1 specifics (12 nm, 15 MB/month cap, FN990B40 recommendation)
- **Device Recommendation:** Telit FN990B40 (3GPP Rel-17 module); Gen2 module must be confirmed for form factor and power envelope
- **Prior Analogues:** Integration strategy reuses Iridium carrier-board methodology from SOW A

---

**Status:** Early planning; only Phase 0 (~$47K) recommended for immediate commitment. Phases 1 and 2 are contingent on device availability, regulatory authorization, and SpaceX service launch timelines, each gated independently.