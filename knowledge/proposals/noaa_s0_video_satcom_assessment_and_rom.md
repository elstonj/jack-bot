# NOAA UxSOC Draft SOW Review — Technical Feedback, Scope Alignment, and ROM

## Document Metadata
- **Type:** Internal technical review and response guidance
- **Client/Agency:** NOAA OMAO/UxSOC (Office of Marine and Aviation Operations / Uncrewed Systems Operations Center)
- **Program/Solicitation:** IDIQ 1305M226D0012; two draft Statements of Work under this IDIQ
- **Date:** August 5, 2026 (draft, internal working document)
- **BST Products/Systems Referenced:** S0, S0-AD, SwiftCore, SwiftStation, SwiftTab, SwiftPilot
- **Key Personnel:** Jack Elston (last editor); references to Nick Underwood (AOC), Josh (mechanical), Alex, Dan Prendergast, Maciej, Joe Cione, Beck, Evan Wolff

## Executive Summary

This internal document provides BST's technical assessment of two draft SOWs from NOAA for S0 integration with video and satellite communications. The recommendation is to rescope both efforts: SOW B (video via P-3 antennae) focused on near-field LOS video capability with realistic range constraints (4–32 nm depending on mode), and SOW A (BLOS operations) rescoped to meteorological data over Iridium 9603N satellite with video removed. The document identifies critical drafting errors (unachievable deep-stall recovery requirement, inverted endurance specs), proposes realistic link budgets, and recommends a cost-split approach where BST funds the reusable video core (IRAD) while NOAA funds NOAA-specific integration and qualification.

## Technical Approach

### Core Positioning

Both efforts are achievable within existing IDIQ scope (Attachment 1, §5.1 already anticipates streaming video capability by 2027). The key is proper scope separation:

- **SOW B** = near-field LOS video using the existing Hascall-Denke AVDP1785 dual-band blade antenna (1755–1815 MHz and 2200–2270 MHz) already fitted on the P-3. Separate from the proven 430 MHz command/control chain (Microhard P400, 2 W, 215 nm demonstrated range).
- **SOW A** = beyond-line-of-sight meteorological data over satellite (Iridium 9603N, L-band, negligible rain fade), with video removed to eliminate dependency on SOW B and expand design space.

### Radio Selection

**For SOW B (Video):**
- Recommended: **Femto fDDL9324** (octa-band, covers both AVDP1785 bands 1780–1815 MHz and 2200–2270 MHz)
- Alternative: **fDDL1624** (hexa-band, same coverage)
- Both are 19 × 27 × 7.5 mm, 5.5 g; support 1–8 MHz selectable channels, up to 1 W adjustable power, MRC/ML decoding, DFS, frequency hopping
- Baseline **2200–2270 MHz** (70 MHz usable width, better margin, below 2280 MHz sensitivity-penalty threshold); carry 1780–1815 MHz as fallback; enable in-flight band switching

**For SOW A (BLOS):**
- Recommended: **Iridium 9603N** (31.5 × 29.6 × 8.1 mm, 11.4 g, 11.4 g, 340 B MOD / 270 B MTD, under-one-minute latency, pole-to-pole coverage, AT commands over serial UART, SIM-less, 5 V at ~190 mA)
- Drop-in-class for serial connectivity; only satellite option whose SWaP is unquestioned
- Upgrade path: Iridium Certus 9704 (100 kB messages, still fits 45.7 mm bay, more integration work)
- Reject: cellular (cannot reach operating area beyond 10–20 nm offshore; hurricanes destroy coastal towers; Ku-band terminals 22–45 lb with severe rain fade)

Both radios require autopilot PCB carrier-board revision with 54-pin SMT footprint, UFL antenna connector, split 3.3 V digital / 5 V RF rails.

### Antenna Strategy

**No new P-3 antenna installation required.** The AVDP1785 is already fitted on at least one aircraft tail number (confirm N42RF vs. N43RF coverage). Video rides this blade at 1.8 or 2.2 GHz completely separately from the 430 MHz P400 command/telemetry chain. Critical government-furnished information: measured feed-line loss at 1.8 and 2.2 GHz (not the documented 430 MHz figures; coax loss scales roughly with √frequency, so 1.7–2.5 dB at 430 MHz implies 3.5–5.7 dB at 1800–2235 MHz); antenna gain pattern; VSWR curve; mounting location; connector types.

## Products & Capabilities Described

### S0 Aircraft (Expendable Tactical UAS)
- **Current baseline:** 430 MHz narrowband C2 (Microhard P400, 12.5 kHz, 2 W) delivers 215 nm demonstrated range; 100–120 minute endurance in clear air
- **Payload bay:** 1.8 in (45.7 mm) diameter, field-swappable, 100 g modular interface
- **Video configuration (SOW B):** Adds second radio (fDDL) on 1.8/2.2 GHz, EO camera with global-shutter module, onboard encoding and store-and-forward; removes multi-hole probe (MHP) to clear nose for camera, requiring drained pitot system development
- **BLOS configuration (SOW A):** Replaces P400 with Iridium 9603N for met-data backhaul while P-3 is in-range on 430 MHz; switches to satellite after P-3 departs
- **Note:** Aircraft are expendable/non-recovered (ditched on termination). Anything not transmitted before loss is gone. No onboard archival value.

### EO Camera Integration
- **Preferred candidates:** e-con Systems AR0234 MIPI CSI-2 modules (1/2.6" global-shutter sensor, 3 µm pixel, 1080p@120fps, onboard ISP); Leopard Imaging MIPI modules (US-based, NDAA supply-chain consideration); XIMEA xiMU USB3 variants (smallest industrial options, <5g, global-shutter options)
- **Critical decision:** Global shutter (not rolling) to prevent skew/jello artifacts in 200 mph winds with airframe vibration
- **Integration path:** Use SwiftCore's existing Linux SBC with hardware encoder; MIPI CSI-2 input directly to SoC encoder, dramatically lower power/weight/cost than standalone IP camera with its own ASIC
- **Limitation:** Daylight-only capability; no usable output at night (hurricane missions routinely fly in darkness; low-light performance is binding constraint)
- **Mechanical challenge:** Optical window in 45 mm nose or side fairing must survive tube launch, resist spray and water film, not fog on altitude descent, not disrupt 5-hole probe flow field

### Link Budget and Range Reality (Critical Finding)

**Video is a near-field capability; the SOW has to say so.**

Conservative case: 30 dBm Tx (derated per modulation), 0 dBi airborne element in 45.7 mm body, 3 dBi P-3 blade, 2.5 dB feed loss (measured worst case N43 aft), 10 dB fade/implementation margin.

Optimistic case: +2 dBi airborne, 5 dBi P-3 blade, 1.1 dB feed (best case N42 forward), 6 dB margin.

**Maximum range by mode off AVDP1785 (conservative – optimistic):**

| Mode | 1780–1815 MHz | 2200–2270 MHz |
|------|---|---|
| 1 MHz, BPSK 1/2 (~0.39 Mbps) | 10.0–32.0 nm | 7.5–24.6 nm |
| 2 MHz, BPSK 1/2 (~0.78 Mbps) | 7.1–22.6 nm | 5.3–17.4 nm |
| 4 MHz, BPSK 1/2 (1.57 Mbps) | 5.0–16.0 nm | 3.8–12.3 nm |
| 4 MHz, QPSK 3/4 (4.3 Mbps) | 3.2–10.1 nm | 2.4–7.8 nm |
| 4 MHz, 16QAM 3/4 (7.4 Mbps) | 1.3–4.0 nm | 0.9–3.1 nm |
| 8 MHz, 64QAM 5/6 (21 Mbps) | 0.3–0.9 nm | 0.2–0.7 nm |

**At 80 nm (typical operating range from P-3 host), received signal is −108 to −117 dBm vs. best sensitivity of −100 dBm (−106 dBm extrapolated at 1 MHz). Nothing closes. Video only works in near field.**

**Video link cannot carry 1080p30 continuously.** 1080p30 in H.265 runs 2–3 Mbps (requires 1.9–7.7× real-time bandwidth at available 1.57–0.39 Mbps links). A 100-minute flight generates ~1.5 GB; even at perfect 0.39 Mbps over entire flight, only ~20% could transfer.

**Three-layer architecture that works:**
1. **Continuous low-rate proxy:** 640×480 @ 5 fps (~200 kbps) real-time capable at any range where link closes. Situational-awareness feed.
2. **Continuous 1080p recording to onboard buffer:** 1.5 GB for full flight, cheap, always on. Buffer rate-smoothes since nothing is recovered.
3. **Operator-selected 1080p clip retrieval:** Operator marks interesting moments from proxy feed, pulls corresponding 1080p segments when link quality allows. 30-second clip ~7.5 MB, transfers in 38 sec @ 1.57 Mbps or 154 sec @ 0.39 Mbps. On a 5-minute close pass, 8 clips at high rate or 2 at low rate feasible.

**Two operationally valuable use cases:**
- **Launch and eyewall-entry phase:** First minutes after release while S0 still close to P-3, covers deployment/wing-out/descent/eyewall entry—exactly the imagery NOAA wants for outreach and situational awareness.
- **Deliberate close passes:** If P-3 flight plan brings S0 within 10–20 nm at chosen points, buffered imagery from intervening period can be flushed down on each pass. Turns link constraint into mission-planning parameter.

### Meteorological Data over Satellite (SOW A)

**Met data fits the pipe:** 340-byte Iridium message carries binary-packed observation (time, position, altitude, temp, dewpoint, wind, pressure) in 20–30 bytes = 11–17 records per message. At one message per minute (reasonable SBD cadence), that is a met observation every 3.5–5.5 seconds continuously from BLOS.

**Operationally valuable product:** First time NOAA would get S0 data after P-3 leaves the area. Because aircraft is not recovered, whatever is not transmitted is lost—satellite downlink is the dataset, not a backup.

**Cadence set by SBD economics, not airframe:** Higher rates = more messages = more airtime cost. Put defined cadence in SOW rather than "telemetry"; let NOAA trade cost vs. resolution.

### Ground Station Integration