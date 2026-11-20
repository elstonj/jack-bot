# S0 Air-Deployed UAS from the NASA 777 Integration

## Document Metadata
- Type: Presentation / Meeting Agenda & Status Briefing
- Client/Agency: NASA LaRC, NOAA, Embry-Riddle Aeronautical University (ERAU)
- Program/Solicitation: NASA 777 Integration (NURTURE program)
- Date: 18 November 2026
- BST Products/Systems Referenced: S0, S0-AD (S0 Air-Deployed variant), Deployment tube, Base station (1U rack, 430 MHz Microhard P400), 5-hole air-data probe
- Key Personnel: Jack Elston (BST, last editor); Referenced: Hunter, Meek, Dolph, Petty (NASA LaRC); Cione, Pawlenko, Hollingshead (NOAA); Gnanamanickam, Zhang, Wadler (ERAU); Maciej (BST)

## Executive Summary
This presentation aligns NASA LaRC, NOAA, ERAU, and Black Swift Technologies on integrating and demonstrating the S0-AD (air-deployed S0 UAS) for high-altitude deployment from a NASA 777 research aircraft at FL300–430. The team has defined the technical scope, identified integration requirements, and laid out a path to demonstration via ERAU wind-tunnel testing, bench checkout, risk-reduction flights, and eventual 777 integration.

## Technical Approach

### S0-AD Platform
- **Starting point**: Mature platform already operating from NOAA P-3 aircraft; proven in coastal/ocean operations
- **Vehicle specs**: 32.25 in wingspan, 4.25 in constant chord, aspect ratio ≈ 7.6
- **Altitude envelope**: Analysis shows controlled glide and stability at 45 kft; 60 kft assessed as likely feasible (extrapolated from 20 kft SOCOM drop data)
- **Control link**: 430 MHz radio link (Microhard P400), range ~150–200 nmi depending on S0 altitude
- **Launch method**: Deployment from 777 cruise altitude via existing launcher (5.000 in OD deployment tube; 777 carries compatible 5.25 in ID launcher)

### Deployment Architecture
- **Host**: NASA 777 aircraft (NURTURE program, available through March 2027)
- **Launcher**: NRD41 dropsondes launcher on 777; P-3-equivalent deployment tube and peripherals
- **Ground station**: 1U rack-mount base station with 430 MHz Microhard P400, requiring GPS (or repeater), external antenna, 110 VAC power (battery option available)
- **Avionics**: 5-hole air-data probe with recalibration work planned for high-altitude/low-dynamic-pressure operation

## Products & Capabilities Described

### S0-AD (S0 Air-Deployed)
- **What it is**: Small atmospheric sampling UAS, proven in NOAA P-3 operations
- **Performance claim**: 240 mph record (achieved in Milton); controllable glide at altitude
- **High-altitude capability**: Core technical objective—extend envelope from P-3 operations (~FL150) to 777 cruise (FL300–430)
- **Sensor suite**: "Basic atmospheric sensor package" (specific sensors not detailed in this document)
- **Quantities ordered**: 2 aircraft plus base station (funded by NASA in late October 2026)

### Base Station (1U Rack, 430 MHz)
- **Configuration**: Single-unit rack mount, Microhard P400 radio, requires GPS/repeater, external antenna, power
- **Interface**: To be defined per 777 integration
- **Power options**: 110 VAC or battery

### Air-Data Probe (5-hole)
- **Current state**: Operates on P-3; requires recalibration for high-altitude glide and low-dynamic-pressure regimes
- **Work planned**: 
  - Sensor scaling correction
  - Low-q (dynamic pressure) points for high-altitude deployment
  - 3-sensor vs 5-sensor layout optimization
  - Blocked-port detection
  - NDAA-compliant pressure sensor qualification

## Use Cases & Applications

### Primary Mission
- **Scientific measurement from high altitude**: Deploy S0 from 777 to measure atmospheric properties (exact parameters not specified) at FL300–430 altitudes
- **Extension of existing operations**: Currently operate from P-3 at ~FL150; 777 enables ~3× altitude increase
- **Range expansion**: 430 MHz link budget permits 150–200 nmi standoff range, enabling broader sampling footprint

### Potential Alternate Platforms
- G-III and G-550 aircraft listed as alternates if 777 unavailable

## Key Technical Decisions & Requirements

### Integration Requirements Needing Definition
1. **777 ICD (Interface Control Document)**: Built from P-3 ICD and S0 System Integration Reference (Rev B)
   - Covers: launcher, rack configuration, power delivery, GPS integration, antenna placement, cabling
   - Leads: BST + NASA LaRC

2. **Deployment Envelope**: 
   - Defines release altitude/Mach (e.g., M0.8 at FL400), tube timing, chute loads, cabin differential (9 psi noted)
   - Leads: NASA + BST

3. **Air-Vehicle Performance Envelope**:
   - Glide characteristics, control authority, Reynolds number effects FL300–430, cold soak, battery performance at altitude
   - Lead: BST

4. **RF & Link Budget**:
   - 430 MHz antenna placement on 777, link budget analysis, spectrum authorization (RF authorization and 565 forms already filed for P400 at 433 MHz)
   - Leads: BST + NASA LaRC

5. **Safety & Airworthiness**:
   - Hazard analysis, 777 airworthiness review, airspace/range safety
   - Lead: NASA

6. **ConOps & Data**:
   - Mission profiles, crew roles, data products, data sharing protocols
   - Leads: NOAA + all partners

### ERAU Wind Tunnel Campaign

**Facility**: MicaPlex tunnel (20 ft/s, stable floor, Re/ft ≈ 1.3×10⁵)
- Hits lowest expected chord Re with 75% model; full-scale close
- Full S0-AD span (32.25 in) fits 4 ft width limit
- 64-channel Scanivalve pressure scanners on wing taps
- Balance for low-frequency dynamics
- Government rate: $230/hr (vs. $600/hr non-government)
- Previous run (Feb 2023): 516-point matrix, ±14° α/β, 4.3 h tunnel time, completed in <2 days

**Proposed test agenda (2–3 tunnel days)**:

| Run | Article | Conditions | Purpose |
|-----|---------|-----------|---------|
| A | S0 fuselage, 5-sensor probe, fixed scaling | 2023 matrix at 22.5 & 26 m/s | Baseline probe recalibration |
| B | Same | Reduced grid, 20→22.5 m/s | Low-q behavior |
| C/D | 3-sensor board; NDAA-compliant board | 2023 matrix + low-q points | Sensor trade studies |
| E | A and C with one port blocked | Reduced grid, 22.5 m/s | Clogged-port detection |
| F | Wings-on S0 (×2 airframes) | F&M sweep, low-Re focus | Aero validation + manufacturing variation |
| G | NASA article (full or 75%, BL/taps) | Per NASA test plan | CFD validation |

**NASA aero objectives**:
- Force & moment at low Re, full-span or 75% scale
- Laminar/turbulent boundary-layer state on upper wing
- Transition tripping for CLmax improvement if needed
- Wing pressure taps for CFD validation

**BST objectives**:
- Recalibrate 5-hole probe with corrected sensor scaling
- Characterize low-q points for high-altitude glide
- Optimize 3-sensor vs 5-sensor probe layout, including blocked-port scenarios
- Qualify NDAA-compliant pressure sensor
- Test wings-on S0 configuration to eliminate fuselage-only downwash corrections
- Measure unit-to-unit build variation (two S0 airframes)

**Outstanding**: Decision needed on combined vs. separate tunnel entries, payment route and rates, mount/load analysis, target dates.

## Project Timeline & Milestones

**Now (Nov 2026)**:
- Kickoff & agreements on roles, schedule, ERAU NDA, SAA

**Dec 2026 – Jan 2027**:
- Requirements & ICD definition
- 777 interface, deployment envelope, safety documentation

**Q1 2027** (placeholder dates):
- Hardware delivery: 2× S0-AD aircraft + base station; bench checkout at NASA LaRC
- ERAU tunnel campaign: aero, probe, vehicle runs; feeds CFD

**Spring 2027**:
- Risk-reduction phase: balloon drop at altitude or P-3/G-III launch

**After NURTURE (post-March 2027)**:
- 777 ground integration
- Flight demonstration launch at FL300+

## Critical Path Items & Decisions Needed

**Before next meeting, decisions required on**:
1. Hardware delivery dates and receiving point of contact at LaRC
2. Ownership and due dates for each requirements document
3. Tunnel scope: combined or separate entries, payment/rate structure, target window
4. Risk-reduction approach (balloon vs. aircraft drop) and 777 availability timeline
5. Meeting cadence and next check-in schedule

**Immediate action items**:
- NASA LaRC: 777 antenna specs, GPS repeater, rack & power details → needed for ICD, link budget, base-station config
- BST: Draft 777 ICD from P-3 reference → needed for all integration work
- NASA + BST: Deployment envelope targets (alt, Mach, tube timing) → needed for CFD, tunnel matrix, release design
- BST + ERAU: ERAU NDA, test info form, test plan → needed to book tunnel schedule
- NOAA / NASA / BST: Tunnel funding path and data rights → needed to book the entry
- BST: Probe firmware fix, 3-sensor and NDAA boards → needed for Runs A–E (tunnel)
- All: Risk-reduction flight option selection → needed for pre-777 confidence

## Notable Details

- **Mature baseline**: This is not a new vehicle development; S0-AD is proven operational on NOAA P-3s. Work focuses on altitude envelope, Reynolds number effects, and 777-specific integration.
- **Spectrum authorization**: LF400 RF authorization and 565 forms already filed for 430 MHz Microhard P400 at 433 MHz.
- **Existing infrastructure**: 777 already has compatible deployment launcher (5.25 in ID); quote mirrors NOAA P-3 kit with no custom 777 hardware initially; 777-specific hardware scoped after requirements finalized.
- **Partnerships**: Multi-agency/university team (NASA LaRC, NOAA, ERAU) with clear role division; NOAA science leadership and P-3 operational heritage; ERAU's low-Re wind tunnel capability critical to validation.
- **Schedule driver**: 777 aircraft availability; NURTURE program owns platform through March 2027 with launcher committed to NRD41 (dropsondes). Integration work must be ready when launcher frees up.
- **Risk reduction**: Pre-777 confidence building via balloon drop or alternate-aircraft launch planned for spring 2027.
- **Data products**: ConOps and data-sharing protocols to be defined with NOAA lead; mission profiles and crew roles TBD.

---

**Document Assessment**: This is a working-level status and coordination briefing (not a formal proposal or final report). It captures the current state of a multi-partner integration project with clear technical scope, identified risks, and actionable next steps. Gaps are intentional (marked as TBD) pending decisions in the meeting.