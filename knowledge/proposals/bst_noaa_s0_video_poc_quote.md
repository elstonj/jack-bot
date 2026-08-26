# BST NOAA S0 Video POC Quote

## Document Metadata
- Type: Revised quote/proposal for proof of concept development
- Client/Agency: NOAA OMAO (Office of Marine and Aviation Operations) / UxS Operations Center
- Program/Solicitation: IDIQ 1305M226D0012; in response to LCDR N. Pawlenko direction (5-6 August 2026)
- Date: 7 August 2026 (Draft for internal BST review)
- BST Products/Systems Referenced: S0 Uncrewed Aircraft System
- Key Personnel: Jack Elston (Founder and CEO); LCDR Nick Pawlenko (NOAA point of contact, Associate Director Requirements & Capabilities, UxSOC)

## Executive Summary
BST proposes a two-part proof of concept to develop and demonstrate line-of-sight video capability on the S0 uncrewed aircraft platform for integration with NOAA's P-3 aircraft. The effort converts two S0 airframes already on order to video configuration through non-recurring engineering (NRE) costing $64,900 NOAA-funded plus $169,800 BST private expense contribution ($234,700 total development value), with Part A demonstrating capability at BST facilities and Part B conducting integration and flight test aboard the P-3.

## Technical Approach

### Link Architecture & Range Analysis
- **Existing S0 C&DL**: 12.5 kHz narrowband at 430 MHz; demonstrated 215 nm range
- **Video challenge**: Video-rate data costs 30-40 dB link margin not recoverable on 1.2 kg airframe
- **Selected band**: Hascall-Denke AVDP1785 dual-band antenna (1755-1815 MHz and 2200-2270 MHz), already installed on WP-3D; BST recommends baselining 2200-2270 MHz with 1780-1815 MHz as in-flight selectable alternate
- **Typical S0 operating range from host**: ~80 nm; **Video-capable range**: 1-32 nm depending on modulation/bandwidth, making it a near-field capability

### Modulation & Data Rate Options
| Transmitted Product | Approx. Rate | Estimated Usable Range |
|---|---|---|
| Low-rate imagery (1 MHz channel) | ~0.39 Mbps | 8-32 nm |
| Compressed video (4 MHz, BPSK) | ~1.57 Mbps | 4-16 nm |
| Higher-rate video (4 MHz, QPSK 3/4) | ~4.3 Mbps | 2-10 nm |
| Maximum-rate video (8 MHz, 64QAM) | ~21 Mbps | <1 nm |

### Imagery Architecture (Three-Layer Approach)
1. **Continuous proxy feed**: ~640×480, 5 fps, ~200 kbps; real-time capable wherever link closes
2. **Onboard recording**: Continuous 1080p30 (requires 2-3 Mbps, above available link rate except closest ranges) to onboard buffer; acts as rate-smoothing mechanism
3. **Operator-selected retrieval**: Full-resolution segments transferred when link permits; 30-second 1080p segment = ~7.5 MB, transfers in ~38 seconds at 1.57 Mbps (~8 segments possible during 5-minute close pass)

### Camera Placement Recommendation
**Side-looking or downward-looking installation** (BST recommendation):
- Retains multi-hole probe for high-rate wind measurement and turbulence capability
- Supports eyewall imagery, sea-surface observation, launch/descent sequence
- Resolves sensor-suite requirement conflicts

**Forward-looking alternative** (deferred to follow-on):
- Requires removing multi-hole probe; wind derived from vehicle state estimate only (filtered, lower rate, unable to resolve turbulence)
- Requires drained pitot development and wind-tunnel calibration (~$66,500, not included)

## Products & Capabilities Described

### S0 Uncrewed Aircraft System
- **What it is**: Small air-deployed UAS launched from larger host aircraft (P-3 in this case)
- **Proposed use**: Demonstration platform for video-enabled air-deployed reconnaissance
- **Specifications/modifications**: 
  - Baseline endurance: 100+ minutes (statement deferred pending integration analysis due to added power draw from camera/radio/antenna)
  - Mass: 1.2 kg
  - Recovery method: Expendable air-deployment; not recovered
  - Standard sensor suite: Multi-hole pressure probe for wind/turbulence measurement
  - Proposed video configuration: Camera module, video radio carrier board, AVDP1785 antenna, harness

### Video-Enabled S0 Components (Hardware Kit)
- **Camera module**: 1080p30-capable EO camera with optical window
- **Video radio**: Multi-band radio supporting AVDP1785 bands (1.8 GHz and 2.2 GHz)
- **Carrier board**: Video and radio integration board with link-adaptive bitrate control
- **Antenna**: AVDP1785-compatible antenna for L/S-band transmission
- **Cost**: $6,000 for hardware kit (two aircraft configuration)

### Ground Station
- **Functionality**: Video receive radio, recording, display, retransmission
- **Capabilities**: Record, display, and retransmit video to P-3 cabin network
- **Integration**: Cabin network retransmission and operator display build-out ($12,300 in Part B)
- **Constraints**: Must fit within Aircraft Operations Center rack, power, and cooling constraints

## Use Cases & Applications

### Primary Demonstrated Application
- **NOAA P-3 hurricane/severe weather operations**: Air-deployed S0 for eyewall imagery and sea-surface observation during proximity to host aircraft
- **Range implications**: Aircraft must remain nearby (4-32 nm depending on configuration) or depart and re-acquire, unlike 215 nm C&DL range

### Operational Scenarios Mentioned
- Eyewall imagery
- Sea-surface observation
- Launch and descent sequence observation
- Weather reconnaissance operations from NOAA aircraft

## Key Results (Deliverables)

### Part A Deliverables (Capability Development, $29,800)
- Link and antenna analysis for AVDP1785 band selection
- Ground station design (video receive radio, recording, display)
- Conversion and checkout of two airframes
- Surrogate end-to-end demonstration using BST facilities and surrogate antenna
- Proof-of-concept report with recommended follow-on scope

### Part B Deliverables (P-3 Integration & Flight Test, $29,100)
- P-3 integration and coordination with Aircraft Operations Center
- Flight test aboard WP-3D
- End-to-end acceptance demonstration

### Overall Proof-of-Concept Deliverables
1. Two video-enabled S0 UAS fully configured (converted from airframes already on order)
2. **Measured rate-versus-range curve** for selected band and waveform (central open question the POC addresses)
3. Demonstrated end-to-end imagery chain (camera → encode → link → ground station → display)
4. Ground station capable of receiving, recording, displaying, and retransmitting video
5. End-to-end demonstration on NOAA P-3
6. Defined product specification for operational system: achievable resolution, frame rate, and latency at range
7. Proof-of-concept report with recommended follow-on scope

## Cost Breakdown & Funding Structure

### NOAA-Funded Non-Recurring Engineering: $64,900 (28% of total development value)

**Part A — Capability Development and BST Surrogate Demonstration: $29,800**
| Line Item | Labor Hours | Cost |
|---|---|---|
| Link/antenna analysis; AVDP1785 band selection; airborne design | 8 Pr / 20 Ld / 0 En / 0 Tc | $6,000 |
| Ground station (video RX radio, recording, display) | 0 Pr / 30 Ld / 22 En / 0 Tc | $9,300 |
| Conversion/checkout of two airframes | 0 Pr / 8 Ld / 24 En / 24 Tc | $7,000 |
| Surrogate demonstration and POC report | 4 Pr / 8 Ld / 8 En / 0 Tc | $3,800 |
| Program management and reporting | 4 Pr / 6 Ld / 0 En / 0 Tc | $2,200 |
| Ground station receive hardware | — | $1,500 |

Labor rates (per IDIQ Attachment 2, Tab 2):
- Principal Scientist/Engineer: $250/hr
- Scientist/Engineer – Lead: $200/hr
- Scientist/Engineer: $150/hr
- Technician, Mid-Level: $75/hr

Total Part A labor: 166 hours

**Part B — P-3 Integration, Flight Test, and Acceptance Demonstration: $29,100**
| Line Item | Cost |
|---|---|
| P-3 integration, flight test, acceptance demo on aircraft | $11,800 |
| Cabin network retransmission and operator display build-out | $12,300 |
| Travel (one multi-day trip, Federal Travel Regulation) | $5,000 |

Includes coordination with Aircraft Operations Center on AVDP1785 interface and spectrum authorization support.

**Hardware: $6,000**
- Video conversion kit hardware for two airframes (camera module, video radio, carrier board, antenna, harness)
- No overhead/fee beyond standard treatment

### BST Private-Expense Contribution: $169,800 (72% of total development value)
| Item | Value |
|---|---|
| Video and radio carrier board design and two fabrication spins | $55,600 |
| EO camera selection, optical window, and mechanical integration | $29,400 |
| Airborne firmware: capture, encode, link-adaptive bitrate control | $36,000 |
| Buffering, store-and-forward, operator-selected retrieval | $25,000 |
| Bench characterization (camera, encoder, link) | $16,800 |
| Materials (cameras, PCB fabrication/assembly, radios, RF/bench hardware) | $7,000 |

**Total Development Value: $234,700**

## Notable Details

### Aircraft & Expendability
- **No new aircraft procurement**: Effort converts two S0 airframes already on order to video configuration
- **Airframes as Government-furnished property**: During conversion and demonstration, NOAA-owned or on-order airframes become GFP; BST requests FAR 52.245-1 responsibility clarification and serial number identification in task order
- **Demonstration is one-way flight**: P-3 flight test expends one airframe; one video-enabled aircraft remains after demonstration OR NOAA allocates third airframe to preserve two aircraft post-demonstration
- **Expendable configuration**: Not recovered; no deep-stall recovery capability (correcting draft SOW error)

### Cost-Share Rationale
BST is independently developing air-deployed video for other markets; rather than bill NOAA for reusable core development, BST funds the underlying technology platform (~$170K private expense) while NOAA funds NOAA-specific integration and demonstration work.

### Data Rights & IP
- **Proposed structure**: Mirrors SBIR construct already contemplated in IDIQ
- **BST retains**: Title to underlying technology; unlimited, royalty-free right to use, reproduce, modify, license for other products/customers/programs
- **NOAA receives**: Paid-up, non-exclusive, royalty-free license for Government purposes; failure-to-supply access to underlying design if BST unable/unwilling to produce
- **Technical data scope**: Proposes narrowing design-material deliverable to what NOAA requires to operate/maintain/integrate (interface descriptions, operator guidance, configuration/calibration data, test results) rather than all residual design material
- **SBIR heritage**: S0 carries SBIR data rights from NOAA SBIR Phase I (1305M218CNRMW0059) and Phase II (1305M219CNRMW0030); this effort could qualify S0 for SBIR Phase III status

### Draft