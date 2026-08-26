# BST Response to NOAA Draft Statement of Work: S0 Satellite Communication and Command/Control

## Document Metadata
- Type: RFI Response / Technical Feedback on Draft SOW
- Client/Agency: NOAA OMAO / UxS Operations Center
- Program/Solicitation: IDIQ 1305M226D0012; Task Order for acquisition of 6 S0 UAS with satcom/C2 capability
- Date: 5 August 2026
- BST Products/Systems Referenced: S0 Uncrewed Aircraft System
- Key Personnel: Jack Elston (last editor); addressed to Jacklyn C. James, NOAA Management Analyst

## Executive Summary
BST responds to NOAA's draft SOW for acquiring six S0 aircraft with satellite communication and/or land-based command/control capability. BST recommends rescoping the requirement to remove video (to avoid duplication with a companion SOW and to eliminate technical infeasibility) and to focus on beyond-line-of-sight (BLOS) command, control, telemetry, and meteorological data via L-band satellite. BST proposes the Iridium 9603N transceiver as the baseline architecture, argues that terrestrial/cellular solutions cannot reach the required operating area, and provides a detailed ROM estimate of approximately $448K for NRE and six aircraft.

## Technical Approach

### Recommended Architecture: L-Band Satellite (Iridium 9603N)
BST recommends the Iridium 9603N transceiver module as the baseline:

| Parameter | Specification |
|-----------|---------------|
| Dimensions | 31.5 × 29.6 × 8.1 mm |
| Mass | 11.4 g |
| Power | 5V, ~190 mA average |
| Interface | AT commands over serial UART; no SIM required |
| Message capacity | 340 bytes mobile-originated; 270 bytes mobile-terminated |
| Latency | <1 minute |
| Coverage | Global, pole to pole |

**Rationale:**
- Fits within S0's 1.8 in (45.7 mm) diameter payload bay with margin
- Simple serial interface reduces integration risk vs. Ethernet/IP terminals
- L-band (1616–1626 MHz) has negligible rain attenuation—decisive for tropical cyclone operations
- Selected over higher-throughput alternatives (Iridium Certus 9704, Certus 100) due to form factor and simplicity, though those are offered as priced alternatives

### Data Capacity and Cadence
A 340-byte message can carry a binary-packed meteorological observation (~20–30 bytes) containing time, position, altitude, temperature, dewpoint, wind speed/direction, and pressure. This yields 11–17 observations per message. At one message per minute, provides a meteorological observation every 3.5–5.5 seconds continuously from beyond line of sight—first time NOAA would receive S0 data after P-3 departs the area.

**Key consideration:** Observation cadence is driven by satellite airtime economics, not airframe capability. BST recommends SOW specify required cadence rather than generic "telemetry" to allow deliberate trade-off of recurring airtime cost vs. temporal resolution.

### Why Video Should Be Removed
BST argues video should be struck from this SOW for three reasons:

1. **Duplication risk:** Video development work in §2.3 overlaps substantially with companion line-of-sight video SOW, either duplicating non-recurring engineering or making this task order contingent on the other being funded.

2. **Technical infeasibility:** §2.3 requires video to be "compatible with the communication architecture established under Task 2.2." No satellite terminal fitting the S0 airframe supports video-rate throughput (megabits/second); constellation, antenna size, and available power all preclude it.

3. **Architectural constraint:** Video requirement forecloses the satellite path and forces design toward terrestrial cellular—the one architecture that cannot meet the §1.3 objective of offshore operation.

**Recommendation:** Scope this task order as BLOS command, control, telemetry, and meteorological data only; address video exclusively under the companion LOS video requirement.

### Why Terrestrial/Cellular C2 Cannot Work
BST investigated land-based options seriously, including direct discussions with T-Mobile and Gogo Business Aviation:

- **LTE Coverage:** Reliable coverage extends 10–20 nm offshore in populated U.S. coastal areas, commonly less. High-gain low-band antennas can extend toward 30 nm under favorable conditions, but coastal macro cells are down-tilted for terrestrial users and networks are neither engineered nor authorized for aeronautical use.

- **Infrastructure survivability:** Tropical cyclones destroy coastal cellular infrastructure—the network being relied upon would be disabled by the system being measured.

- **T-Satellite (Starlink direct-to-cell):** Currently limited to 12 nm from U.S. coast absent special authorization; requires specific 3GPP Release 17 modules. FCC Special Temporary Authority path exists but authorization doesn't exist today. Throughput reported in low hundreds of kilobits/second.

- **Airborne broadband terminals (Gogo):** Galileo HDX ~24 × 12 in, just under 22 lb; FDX ~30 × 25 in, 45 lb—neither installable on 1.2 kg airframe. Both Ku-band, wrong for this mission.

### Radio Frequency Attenuation: Band Selection Resolves the Problem

| Band | Rain behavior in tropical cyclone |
|------|-----------------------------------|
| L-band (Iridium, 1616–1626 MHz) | Rain attenuation negligible. **Decisive argument for recommended architecture.** |
| Ku-band (Starlink, OneWeb, ~10.7–14 GHz) & Ka-band | Severe rain fade, precisely in conditions NOAA operates. Terminal performing in clear air can drop out entirely in convective core. |
| Cellular (700 MHz–2.6 GHz) | Rain not limiting factor; coverage is (per §1.4). |

L-band selection largely eliminates rain attenuation rather than mitigating it. Residual propagation challenges are sea-surface multipath at low altitude, airframe blockage during banked orbits, polarization mismatch on rolling airframe, and water film on radome—real and tractable problems.

## Products & Capabilities Described

### S0 Uncrewed Aircraft System

**What it is:**
- A man-portable, expendable UAS deployable from NOAA P-3 via drop-tube launch
- Baseline endurance: 100 minutes in clear air; 60 minutes in tropical cyclone conditions
- Maximum demonstrated endurance: 119 minutes
- Current configuration: Microhard P400 radio (~$350), approximately 1.2 kg airframe
- Unit price: $18,000 (Ordering Period One); $18,630 (Ordering Period Two)
- Payload bay: 1.8 in (45.7 mm) diameter

**Proposed enhancement:**
- Integration of Iridium 9603N L-band satellite transceiver for BLOS command, control, telemetry, and meteorological data return
- Estimated unit price delta: $0–$500 per aircraft for L-band antenna and harness changes
- Delivers continuous data beyond P-3 line-of-sight range

**AVAPS-enabled backhaul:** Existing capability that must be preserved in modified configuration.

## Use Cases & Applications

### Primary Mission: Tropical Cyclone Operations
- Extended data collection beyond dependence on continuous line-of-sight support from parent P-3 aircraft
- Meteorological observation collection (temperature, dewpoint, wind, pressure, position) from within and beyond storm systems
- First NOAA capability to receive S0 data after P-3 departs the area
- Observation cadence: 3.5–5.5 seconds (at one satellite message per minute)
- Operation in tropical cyclone environment with heavy rain and infrastructure damage

### Operational Scenario
Aircraft is deployed from P-3, operates in line-of-sight contact initially, then transitions to beyond-line-of-sight phase where satellite link becomes the primary data path for continued meteorological observation. BLOS data integrated with existing NOAA data paths (AVAPS and HDOB product continuity required).

## Key Results / Recommendations

### Scope Changes Recommended
1. **Remove video** from this SOW; address exclusively under companion LOS video requirement
2. **Base on L-band satellite** (Iridium 9603N) rather than "satellite and/or land-based"
3. **Structure as satellite (base) plus terrestrial/cellular (separately-priced option)**—not "and/or"
4. **Remove 120-minute endurance requirement** (exceeds baseline specification and maximum demonstrated endurance); replace with characterize-and-report obligation
5. **Remove deep-stall recovery requirement**—S0 air-deployed configuration does not incorporate this; appears drawn from different BST platform
6. **Clarify period of performance**: "not exceed twelve (18) months"—which governs?

### Contract Structure Items Recommended
- **NRE CLIN structure:** Add communications integration CLIN or clarify application against existing CLINs (three NRE CLINs capped at $66K each = $198K combined)
- **Ordering period clarification:** Award in Q4 FY26 with 18-month PoP crosses 31 Jan 2027 boundary; confirm which period governs
- **Pricing placement:** Remove unit price and NRE figures from §2.2 (SOW), place in Schedule of Items and Prices
- **Unit price revision:** $18,000 tied to current P400 radio configuration; quote delta for Iridium 9603N configuration separately

### Intellectual Property & Data Rights
BST proposes structure mirroring SBIR construct:
- BST retains title to underlying technology and unlimited, royalty-free right to use, reproduce, modify, license for other products/customers/programs
- NOAA receives paid-up, non-exclusive, royalty-free license for Government purposes
- NOAA access to underlying design only on failure-to-supply basis
- Reference FAR 52.227-20 (SBIR Data Rights)
- Note: S0 platform carries existing SBIR data rights from NOAA SBIR Phase I 1305M218CNRMW0059 and Phase II 1305M219CNRMW0030; this work contemplated for S0 SBIR Phase III status

### Government-Furnished Information Requested
1. NOAA's operational concept for BLOS phase: required observation cadence, latency tolerance, expected duration after P-3 departure
2. AOC constraints on antenna placement and L-band interference considerations aboard aircraft
3. Safe-separation test plan and report confirming modified payload doesn't invalidate prior qualification
4. Written confirmation that delivered articles are expendable and will not be recovered
5. NOAA's position on FCC Special Temporary Authority path for T-Satellite beyond 12 nm; whether requirement contingent upon it
6. Requirements for integration of BLOS data stream with existing NOAA paths (AVAPS, HDOB product continuity)

## Rough Order of Magnitude Estimate

All figures assume **video is removed** from this requirement. Retaining video would add $28K–$40K NRE and make this task order dependent on companion effort.

### Hardware
- S0 UAS, beyond-line-of-sight configuration (6 units): **$108,000 + delta**
  - Iridium 9603N estimated comparable cost to P400 it replaces
  - Delta for L-band antenna and harness: $0–$500 per aircraft (to be confirmed by quotation)

### Non-Recurring Engineering

| Code | Line Item | Hours (Prin/Lead/Engr/Tech) | Labor | M&ODC | Total | Required? |
|------|-----------|----------------------------|-------|-------|-------|-----------|
| A-1 | Trade study and CONOPS; satellite path selection vs. required cadence | 32/48/16/0 | $20,000 | — | **$20,000** | Required |
| A-2 | Iridium 9603N integration; autopilot board revision and fabrication spin | 0/120/100/48 | $42,600 | $16,000 | **$58,600** | Required |
| A-3 | L-band antenna design and placement on airframe | 16/56/40/0 | $21,200 |