# BST Response to NOAA Draft Statement of Work: Line-of-Sight Video-Enabled S0 UAS

## Document Metadata
- Type: RFI Response / Technical Feedback on Draft SOW
- Client/Agency: NOAA (National Oceanic and Atmospheric Administration) / OMAO (Office of Marine and Aviation Operations) / UxS Operations Center
- Program/Solicitation: IDIQ 1305M226D0012; Draft SOW dated 29 July 2026
- Date: 5 August 2026
- BST Products/Systems Referenced: S0 (uncrewed aircraft system), Microhard P400 radio
- Key Personnel: Jack Elston (last editor); submitted to Jacklyn C. James (NOAA Management Analyst)

## Executive Summary
BST provides detailed technical feedback on a draft NOAA SOW requesting development and delivery of two line-of-sight video-capable S0 UAS for deployment on NOAA WP-3D aircraft. BST confirms the capability is achievable under the existing IDIQ but identifies several technical and contractual issues requiring clarification before task order award, most critically the fundamental constraint that video transmission is a near-field capability limited to 2–32 nm depending on data rate, not compatible with the S0's demonstrated 80 nm operational range.

## Technical Approach

### Link Analysis & Range Constraints
BST's core technical finding is that video-rate data transmission fundamentally trades away the link margin that enables the S0's 215 nm range at 430 MHz. Preliminary link analysis for the proposed AVDP1785 antenna (1755–1815 MHz and 2200–2270 MHz dual-band blade antenna already installed on WP-3D aircraft) shows:

| Transmitted Product | Approx. Rate | Usable Range |
|---|---|---|
| Low-rate imagery (1 MHz channel) | ~0.39 Mbps | 8–32 nm |
| Compressed video (4 MHz channel, BPSK) | ~1.57 Mbps | 4–16 nm |
| Higher-rate video (4 MHz, QPSK 3/4) | ~4.3 Mbps | 2–10 nm |
| Maximum-rate video (8 MHz, 64QAM) | ~21 Mbps | Under 1 nm |

Assumptions: 1 W transmit power, small airborne element, blade antenna at aircraft, measured feed-line losses, normal fade margin. Typical S0 operating range from host aircraft is ~80 nm (430 MHz link), but video is not feasible at this distance.

### Proposed Three-Layer Architecture for 1080p Imagery
1. **Continuous low-rate proxy feed**: ~640×480 at 5 fps, ~200 kbps, real-time at any range where link closes (situational awareness product)
2. **Continuous 1080p recording to onboard buffer**: ~1.5 GB per 100-minute flight; storage not a constraint
3. **Operator-selected 1080p segment retrieval**: Operator marks moments of interest from proxy feed and retrieves full-resolution segments when link permits. A 30-second 1080p30 segment (~7.5 MB) transfers in ~38 seconds at 1.57 Mbps or ~154 seconds at 0.39 Mbps

This delivery method addresses the physical impossibility of transmitting full-flight 1080p30 (requires 2–3 Mbps, exceeding available link rate except at closest ranges). A 100-minute flight generates ~1.5 GB; even at continuous 0.39 Mbps link, only about one-fifth could be transferred. Because S0 aircraft are expendable and not recovered, onboard buffer functions as rate-smoothing mechanism; any imagery not transferred before vehicle loss is unrecoverable.

### Operational Use Cases for Video Capability
- **Launch and eyewall-entry phase**: Deployment, wing deployment, descent, and entry into weather while S0 is near P-3 (described as "likely the most compelling imagery")
- **Deliberate close passes**: If P-3 flight plan brings aircraft within 10–20 nm of S0 at chosen points, buffered imagery from intervening period can be transferred on each pass, converting link constraint into mission-planning parameter

### Antenna & Spectrum
- Draft SOW incorrectly identified antenna as "high-frequency (HF)" (3–30 MHz), which cannot support video
- Correct antenna: Hascall-Denke AVDP1785 dual-band blade antenna (1755–1815 MHz and 2200–2270 MHz), already installed on WP-3D aircraft N42RF and N43RF
- Separate installation from 430 MHz command, control, telemetry antennas
- Requires NTIA/IRAC spectrum authorization process for S0 video emitter in 1755–1815 MHz and 2200–2270 MHz bands

### Imaging Resolution & Performance
- 1080p is achievable as recorded-and-retrieved product (not continuous transmission)
- 1080p30 in H.265 requires 2–3 Mbps, exceeding available link rate at all but closest ranges
- BST does not recommend committing to full-flight 1080p transmission as it is not physically available

### Meteorological Sensor Tradeoffs
Multi-hole probe removal required for camera forward-view obstruction creates three consequences:

1. **High-rate wind measurement lost**: Wind speed/direction derived from vehicle state estimate rather than direct measurement. Filtered, substantially lower-rate product that will not resolve high-frequency turbulence.
2. **Drained pitot system development required**: Port may be partially occluded, requiring wind-tunnel calibration; inherently less accurate than current probe. Development task not contemplated in draft SOW (priced separately at B-4).
3. **Conflict with SOW §2.1**: Draft requires "integrated sensor suite for air temperature, wind speed and direction, dewpoint, and atmospheric pressure." Video configuration would report all four, but wind at reduced fidelity and rate.

### Endurance Implications
- Camera, video radio, and antenna add power draw and mass; BST may need to remove battery capacity
- No endurance figure can be responsibly committed until trade study complete
- Mission-level consideration: endurance worth substantially less on video aircraft than meteorological aircraft
- Imagery not useful for entire flight; P-3 must either remain in area or re-acquire UAS
- Endurance beyond window when P-3 nearby yields little additional imagery
- BST recommends striking 100-minute endurance floor and replacing with characterize-and-report obligation

### Ground Station Modifications
- Requires installing additional radio in BST ground station and updating firmware
- Needed functions: receive, store, display, and retransmit video for in-cabin viewing
- Requires coordination with Aircraft Operations Center on cabin WiFi retransmission acceptability
- Existing AVAPS/HDOB data path must be preserved without displacement
- Priced separately at B-7

### Configuration Conflicts
- Draft §2.1 requires "deep-stall recovery" and "pivotable-wing design compatible with P-3 drop-tube launch." S0 air-deployed configuration does not incorporate deep-stall recovery; this appears drawn from different BST platform datasheet. BST cannot meet this as written and requests it be struck.

## Products & Capabilities Described

### S0 Uncrewed Aircraft System
- **General characteristics**: Lightweight (1.2 kg airframe), air-deployed from P-3, pivotable-wing design, expendable (not recovered)
- **Baseline configuration**: Includes Microhard P400 radio (~$350), operates at 430 MHz for command/control/telemetry
- **Baseline performance**: 215 nm demonstrated range at 430 MHz using 12.5 kHz narrowband channel; typical operating range from host aircraft ~80 nm
- **Video configuration delta**: Unit price increase estimated $1,500–$2,500 per aircraft (vendor quotations pending)
- **Payload integration**: Modular payload bay capable of carrying lightweight EO/IR cameras (per IDIQ Attachment 1, §5.4)
- **Meteorological capabilities**: Air temperature, wind speed and direction, dewpoint, atmospheric pressure (wind degraded in video configuration)

### Proposed Video Payload
- Electro-optical camera module with optical window
- Video radio (carrier board design with custom radio module)
- Airborne antenna element (dual-band for AVDP1785 integration)
- Onboard recording buffer for H.265 1080p footage (~1.5 GB per 100-minute flight)
- Firmware for capture, encoding, link-adaptive rate control, store-and-forward, operator-selected retrieval

### Ground Station Enhancement
- Additional radio installation in BST ground station
- Firmware update to receive, store, display, retransmit video for cabin viewing
- Bandwidth: video receiver, storage system, display interface, WiFi retransmission capability

## Use Cases & Applications

1. **Hurricane research and operations**: Launch and eyewall-entry phase imagery during tropical cyclone missions
2. **Atmospheric sampling coordination**: Real-time situational awareness via proxy feed to guide P-3 flight planning
3. **Outreach and communication**: High-resolution 1080p footage captured during critical mission phases for public communication and scientific documentation

## Notable Details

### Scope & Contract Structure
- BST assesses effort falls within general scope of IDIQ 1305M226D0012
- Streaming video capability identified as platform requirement anticipated to be available in 2027 (Attachment 1, §5.1)
- Task order would cross 31 January 2027 ordering period boundary (aircraft unit price $18,000 OP1, $18,630 OP2); BST requests confirmation of which period governs
- Base IDIQ provides three NRE CLINs per ordering period ($66,000 each, $198,000 combined limit), none titled for communications/video integration; BST requests Contracting Officer direction on whether to: (a) add communications-and-video NRE CLIN by bilateral modification, (b) apply against existing CLINs, or (c) phase across ordering periods
- $9.9M IDIQ ceiling is not a constraint for this effort

### Intellectual Property & Data Rights
- BST proposes mirroring SBIR construct already contemplated by IDIQ:
  - BST retains title to underlying technology and unlimited, royalty-free right to use, reproduce, modify, and license for other products/customers/programs
  - NOAA receives paid-up, non-exclusive, royalty-free license for Government purposes
  - NOAA obtains access to underlying design only on failure-to-supply basis
- Request task order state by reference to FAR 52.227-20 (SBIR Data Rights) with confirmation of BST's retained licensing rights unrestricted
- S0 platform carries SBIR data rights from prior NOAA SBIR Phase I (1305M218CNRMW0059) and Phase II (1305M219CNRMW0030); this work could enable SBIR Phase III status
- Request design-material deliverable be narrowed to what NOAA requires to operate, maintain, integrate systems (interface descriptions, operator guidance, configuration/calibration data, test results) rather than all residual design material
- BST will identify limited-rights technical data and restricted-rights computer software at proposal time per FAR 52.227-14

### Acceptance Testing
- Draft SOW §2.4 allows "or a Government-approved surrogate"
- BST proposes hangar-roof-to-aircraft flyaway signal-strength test at Aircraft Operations Center as measurable acceptance criterion not dependent on tropical cyclone occurrence within period of performance

### Government-Furnished Information Requested
1. AVDP1785 interface data for N42RF and N43RF: measured feed-line loss at 1.8 GHz and 2.2 GHz (430 MHz measurements not usable; coaxial loss scales ~√frequency), gain pattern, VSWR curve, mounting location, connector types, confirmation of which tail numbers fitted
2. NOAA's existing spectrum assignment in 1755–1815 MHz and 2200–2270 MHz, current band occupancy aboard P-3, NTIA/IRAC process for adding S0 video emitter
3. Safe-separation test plan and report to confirm modified nose/payload configuration does not invalidate prior separation qualification
4. AOC rack, power, cooling constraints for ground station; cabin WiFi policy
5. Written confirmation that delivered articles are expendable and will not be recovered

### Partnerships & Prior Work
- S0 platform previously funded through NO