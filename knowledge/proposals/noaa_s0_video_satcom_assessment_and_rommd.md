# NOAA UxSOC Draft SOW Review — Technical Feedback, Scope Alignment, and ROM

## Document Metadata
- Type: Internal technical review and proposal assessment
- Client/Agency: NOAA OMAO (Office of Marine and Aviation Operations) / UxSOC (Unmanned eXperimental Systems Operations Center)
- Program/Solicitation: IDIQ 1305M226D0012; two draft SOWs under this contract vehicle
- Date: July 30, 2026 (prepared for internal review before NOAA response due August 8, 2026)
- BST Products/Systems Referenced: S0 (fixed-wing sUAS), SwiftCore, SwiftPilot, SwiftTab, SwiftStation ground station
- Key Personnel: Jack Elston (last editor), Nick Underwood (AOC), Joe Cione (NOAA), Jacklyn James (NOAA IDIQ CO), Beck, Maciej, Dan, Josh, Meredith, Dan Prendergast

## Executive Summary

This internal assessment evaluates NOAA's two draft SOWs for video-enabled S0 operations on WP-3D hurricane research aircraft under an existing IDIQ contract. Both efforts are technically feasible and within contract scope, but three specific issues require correction: (1) the link budget reality severely constrains video range to 4–16 nm for live video and 8–32 nm for buffered imagery versus the typical 80 nm operating range; (2) the stated $30,000 NRE figure is anchored to an informal email estimate and understates actual cost by 15–25×; and (3) endurance and expendability trade-offs are unaddressed. The document recommends an enthusiastic but substantively corrected response, a cost-split structure leveraging BST IRAD-funded reusable core plus NOAA-funded integration to fit within existing CLIN constraints, and explicit data-rights protection under FAR 52.227-14 Alternate II/III.

## Technical Approach

### Scope and Feasibility Assessment
- **SOW A**: Six S0 with SATCOM and/or land-based C2 plus video capability
- **SOW B**: Two S0 with line-of-sight (LOS) video over existing P-3 antennae (AVDP1785 dual-band blade: 1755–1815 MHz / 2200–2270 MHz)

Both efforts fit within IDIQ Attachment 1 specification language (§5.1 anticipates "streaming video capability for outreach purposes … anticipated to be available in 2027"; §5.4 names "lightweight EO/IR cameras" as modular payload integration scope). The feasibility is not in question; the problems are pricing, range expectations, and IP protection structure.

### Link Budget — The Core Technical Reality
**Key Finding**: Video is fundamentally a near-field capability; the 1.8–2.2 GHz radio path closes at dramatically shorter range than the proven 80 nm S0 operating envelope from the host aircraft.

#### Radio candidates (all viable, all require carrier-board spin)
- **fDDL9324** (recommended): Octa-band (902–928 MHz, 1350–1400 MHz, 1625–1725 MHz, 1780–1850 MHz, 2020–2110 MHz, 2200–2300 MHz, 2300–2390 MHz, 2400–2500 MHz); up to 1 W adjustable Tx; 19 × 27 × 7.5 mm, 5.5 g; MRC, ML decoding, LDPC, DFS, frequency hopping, MANET mesh; NDAA compliant; 256-bit AES, FIPS 140-2 pending. Covers both AVDP1785 bands (1755–1815 and 2200–2270 MHz) with fallback options in 900 MHz and 1350–1400 MHz.
- **fDDL1624**: Same bands as 9324 except 900 MHz and 1350–1400 MHz options; identical AVDP1785 coverage; part numbers still placeholder ("MHKXXXXXX") suggesting very recent release — lead-time risk.
- **pDDL1800**: Single-band 1.8 GHz only; covers only lower AVDP1785 band; no size/weight published; ruled out due to inflexibility.

#### Range vs. Rate (Conservative and Optimistic Cases)
Conservative assumptions: 30 dBm Tx (derated per modulation), 0 dBi airborne antenna (small 45 mm body element), 2 dBi P-3 blade, 5.1 dB feed-line loss @ 1800 MHz / 5.7 dB @ 2235 MHz (scaled from documented 430 MHz measurements), 10 dB fade/implementation margin.

Optimistic: 2 dBi airborne, 4 dBi blade, 3.0–3.4 dB feed, 6 dB margin.

**Maximum achievable range by mode (1780–1815 MHz / 2200–2270 MHz):**
- BPSK 1/2, 1 MHz channel (~0.39 Mbps): 10.0–32.0 nm / 7.5–24.6 nm
- BPSK 1/2, 2 MHz channel (~0.78 Mbps): 7.1–22.6 nm / 5.3–17.4 nm
- BPSK 1/2, 4 MHz channel (1.57 Mbps): 5.0–16.0 nm / 3.8–12.3 nm
- QPSK 3/4, 4 MHz channel (4.3 Mbps): 3.2–10.1 nm / 2.4–7.8 nm
- 16QAM 3/4, 4 MHz channel (7.4 Mbps): 1.3–4.0 nm / 0.9–3.1 nm
- 64QAM 5/6, 8 MHz channel (21 Mbps): 0.3–0.9 nm / 0.2–0.7 nm

**At 80 nm operating range**, received signal is −108 to −117 dBm; fDDL best sensitivity is −100 dBm (−106 dBm extrapolated at 1 MHz). **Nothing closes at 80 nm at any rate.**

#### Why C2 and Video Cannot Share the Same Link
- **430 MHz P400 chain** (proven): 12.5 kHz narrowband, 2 W, achieves demonstrated 215 nm; back-calculated receiver sensitivity ~−113 to −123 dBm; tens of kbps max throughput.
- **Video waveform requirement**: Demands orders of magnitude higher sensitivity and bandwidth incompatible with narrowband C2.
- **Architecture conclusion**: Three separate links are correct, not a compromise: 430 MHz for long-range C2/telemetry (215 nm), 1.8/2.2 GHz for near-field video (4–32 nm), L-band SATCOM for BLOS capability.

#### Recommended Video Operating Modes
Rather than unqualified "video," propose two specific deliverables:

1. **Live video, near-field**: 1.5–4 Mbps adaptive modulation, 3–16 nm range; delivered during launch, wing-out, descent, and eyewall-entry phases. Operationally most valuable imagery NOAA seeks.
2. **Progressive still imagery, opportunistic**: Low-rate compressed stills at 1 MHz channel (~0.39 Mbps), 8–32 nm range, buffered onboard and flushed on deliberate P-3 close passes or when link quality permits. Sequenced into video-like product on ground. (SOW B §2.3 already anticipates this.)

Frame deliverable as: "Live video at 640 × 480 / 10 fps with S0 within 10 nm of host; buffered still imagery at reduced cadence to 25 nm."

#### Antenna and Spectrum Resolution
- **No new antenna required**: AVDP1785 dual-band blade already fitted on both P-3s; both fDDL radios cover both bands (1755–1815 and 2200–2270 MHz).
- **Spectrum**: Federal allocations (US Government, not ISM); NOAA holds assignment; low-interference environment; NTIA/IRAC path with NOAA operator.
- **Recommended primary band**: 2200–2270 MHz (70 MHz usable width vs. 35 MHz at 1780–1815; below 2280 MHz sensitivity penalty threshold; room for 8 MHz channel + frequency hopping + DFS).
- **Secondary band**: 1780–1815 MHz for flexibility; slight better propagation but narrower bandwidth.
- **GFI required**: Measured AVDP1785 feed-line loss at 1.8 and 2.2 GHz (not 430 MHz figures), gain pattern, VSWR, mounting location, connector types, confirmation of which tail numbers (N42RF / N43RF) are fitted.

### Propagation Physics (Non-rain factors)
Rain attenuation at 1.8–2.3 GHz is small (<0.05 dB/km even at hurricane rain rates). Actual limiting factors in this environment:
- Sea-surface multipath at low altitude
- Airframe blockage during banked orbits
- Polarization mismatch on rolling airframe
- Spray/water film on radome
- Rolling-shutter jello/skew artifacts (argues for global-shutter camera)

### EO Camera Selection for 45.7 mm (1.8") Payload Bay

S0 payload bay: field-swappable, 100 g modular interface, fixed optics (gimbals ruled out — smallest micro-gimbal ~160 g on a 12–13 g expendable airframe).

**Candidates:**
- **e-con Systems AR0234 modules (e-CAM217_CUMI0234_MOD)** — PRIMARY: 1/2.6" AR0234 global-shutter sensor, 3 µm pixel, 1080p to 120 fps, onboard ISP, 4-lane MIPI CSI-2, interchangeable M12 (S-mount) lens. US/India supply chain (Onsemi sensor). Best fit to MIPI-in, hardware-encode-on-SoC architecture.
- **Leopard Imaging global-shutter MIPI modules** — FALLBACK: US-based (Fremont, CA); clean NDAA 848 / Buy American answer.
- **XIMEA xiMU** — USB3 variant; 15 × 15 to 17 × 17 mm, <5 g, <1 W; global-shutter BSI options; EU-manufactured (Slovakia); check NDAA compliance workbook.
- **Onsemi AR0144 / AR0234 raw modules** — Cost-reduced path; raw sensor board + BST-designed carrier; most firmware work; cheapest per unit.

**Design constraints:**
- **Global shutter mandatory** (not rolling): Rolling shutter in 200 mph winds + airframe vibration → skew/jello artifacts that undermine perceived quality regardless of link performance. Single highest-leverage camera decision.
- **Use S0's existing Linux SBC for encoding**: SwiftCore architecture carries NixOS Linux SBC; MIPI CSI-2 sensor + SoC hardware encoder is dramatically lighter, cheaper, lower-power than self-contained IP camera; puts adaptive bitrate and store-and-forward logic under BST control.
- **Daylight-only capability**: Low-light performance is binding limitation; hurricane missions routinely fly in darkness. Confirm with NOAA that delivered capability is daylight-only; low-light trade (BSI, larger pixel, higher-gain readout) should be on record before October.
- **Optical window mechanical challenge**: Nose or side window must survive tube launch, resist spray/water film, not fog on descent, not disturb 5-hole probe flow field. Budget real mechanical hours.

### Ground Segment

Recommended approach — record + retransmit over WiFi for cabin viewing — is correct. Existing July ground-station shipment already added second radio and external TNC