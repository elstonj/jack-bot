# 2024 NOAA/AOML/HRD Hurricane Field Program - APHEX Mature Stage Experiment Flight Patterns - RICO SUAVE

## Document Metadata
- **Type:** Experiment flight pattern description / operations plan
- **Client/Agency:** NOAA/AOML/HRD (Atlantic Oceanographic and Meteorological Laboratory / Hurricane Research Division)
- **Program/Solicitation:** 2024 NOAA Hurricane Field Program (HFP); APHEX (Airborne Phased Experiment); RICO SUAVE (Research In Coordination with Operations Small Uncrewed Air Vehicle Experiment)
- **Date:** 2024 (field season document)
- **BST Products/Systems Referenced:** S0, Altius 600
- **Key Personnel:** 
  - PIs: Joseph Cione, Josh Wadler (ERAU)
  - Co-Investigators: Lev Looney (NOAA/U Miami), Guo Lin, Ron Dobosy (NOAA/ARL-ret), Altug Aksoy, Sim Aberson, Frank Marks, Kelly Ryan, Brittany Dahl, Johna Rudzin-Schwing (MS State), Xiaomin Chen (UAH), George Bryan (NCAR), Josh Alland (NCAR), Rosimar Rios-Berrios (NCAR), Don Lenschow (NCAR), Chris Rozoff (NCAR), Eric Hendricks (NCAR), Falko Judt (NCAR), Jonathan Vigh (NCAR)

## Executive Summary
RICO SUAVE is a mature-stage hurricane experiment coordinating small uncrewed air vehicles (sUAS) with NOAA P-3 manned aircraft to collect advanced measurements within hurricane cores. The experiment uses BST's S0 and Altius 600 systems to fill spatial and temporal gaps in existing hurricane observations, particularly improving three-dimensional wind field representation, boundary layer thermodynamic sampling, and ocean surface wind velocity measurements. Six coordinated flight pattern modules address hurricane inner-core structure and intensity change processes.

## Technical Approach

### Overall Coordination Strategy
- sUAS deployed from P-3 aircraft at 10 kft radar altitude
- P-3 and sUAS maintain command and control separation of ≤125 nm (230 km)
- Coincident P-3 instrumentation (flight level data, Tail Doppler Radar, dropwindsondes, StreamSondes, AXBT, SFMR, CDR) provides validation and comparison data
- Deconfliction with other aircraft (AF C-130s) per 2024 National Hurricane Operations Plan (NHOP)
- Release in eye or inflow regions depending on module; sUAS does not require P-3 to loiter after deployment

### Six Primary Flight Pattern Modules

#### **P-3 Pattern #1: sUAS Eyewall Circumnavigation**
- **Target:** Maximize azimuthal coverage of mature TC core
- **Timing:** After eye formation
- **sUAS Deployment:** Within eye, no eye-diameter limitation
- **Primary Objective:** Sample maximum wind speed at various altitudes within eyewall
- **Flight Approach (Eyewall/RMW Module):**
  - Counterclockwise spiral descent to 5,000 ft after P-3 separation
  - Increasing-radius flight until eyewall penetration detected by wind speed peak
  - Maintains local wind direction at tail once RMW located
  - Three operational concepts:
    1. Full eyewall circumnavigation at single altitude (data assimilation)
    2. Rapid descent to 1,000 ft (or lower) for surface layer measurement
    3. **Stepped descent maintaining 7 flight altitudes:** 5,000 / 3,000 / 1,000 / 500 / 250 / 150 / 100 ft
  - **Duration:** After 20-30 min launch/stabilization/transit, 210-220 min available for Altius 600; 60 min for S0
  - **S-pattern technique:** After each descent, gradual S-pattern to locate RMW at new altitude
  - **Optional continuation:** If power remains after 100-ft leg, attempt direct headwind approach until exhaustion

#### **P-3 Pattern #2: sUAS Inflow**
- **Target:** Document thermodynamic and kinematic structure of TC inflow layer
- **Timing:** After eye formation
- **Deployment Location:** Downshear-left quadrant; released at ~1.5× RMW radius
- **P-3 Pattern:** Inflow pattern in rain-free region between rainbands; Figure-4 or rotated Figure-4 after reaching upshear direction or precipitation
- **Expendable Deployment:** Up to 10 equally-spaced dropsondes/StreamSondes along inflow trajectory (every 30° azimuth preferred)
- **sUAS Flight Methodology:**
  - **Option 1 (Parcel Tracking):** Follow local winds at constant altitude throughout inflow trajectory; targets downdraft-cooled air; ideal for matching P-3 flight path with sonde/AXBT combos deployed
  - **Option 2 (Stepped Boundary Layer Sampling):** Maximize sampling for model evaluation via 4-altitude stepped descent:
    - **Descent phase:** 3,500 / 2,500 / 1,500 / 500 ft
    - **Ascent phase (add-ons):** 1,000 / 2,000 / 3,000 ft (reaching eyewall penetration)
    - **For Altius 600 long-duration:** Continue ascent to 5,000 / 6,500 ft in eyewall
    - **Outward radial spiral:** ~30-45° angle for 15 min at 6,500 ft
    - **Descent back to inflow:** 4,500 / 2,500 / 500 / 250 ft while maintaining wind-relative track
    - **Final penetration:** Gradual radial inward to low-wind-speed eye
  - **Duration:** ~120 min mission assumption with ~30 min vertical adjustments
  - **Optional:** Center fix if sufficient battery remains upon eye entry

#### **P-3 Pattern #3: sUAS Inflow-Layer Turbulence**
- **Target:** Turbulence information at hurricane-force wind speeds (V10 > 65 kt) in inflow layer
- **Timing:** Preferred for mature stage, after eye formation
- **P-3 Pattern:** Inbound leg with "zig-zag" flight pattern (~15 nm / 28 km deviations) to maintain pace with sUAS while slowing radial penetration
- **Deployment:** sUAS released in hurricane-force conditions (V10 35-55 m/s)
- **Dropsonde Strategy:** 7 dropsondes total, deployed at beginning of each sUAS flight leg
- **sUAS Flight Pattern:**
  - **Launch Phase:** 15 min for launch, stabilization, descent to 3,500 ft
  - **Stepped Descent Mode:** 7 flight levels: 3,000 / 2,250 / 1,500 / 900 / 600 / 300 / 150 ft
  - **Leg Duration:** ~8 min each (can be adjusted to 6 min if necessary)
  - **Vertical Transitions:** 2-3 min descending between legs
  - **Wind Orientation:** Heading adjusted to keep local winds at tail
  - **Overall Duration:** 1-1.5 h
  - **Primary Objective:** Retrieve vertical profile of eddy viscosity (Km) at hurricane-force wind speeds
- **Preferred sUAS:** Short-duration systems (1-1.5 h)

#### **P-3 Pattern #4: sUAS Center Fix / Eye Loiter / Eye-Eyewall Sampling**
- **Target:** Hurricane boundary layer eye and eye-eyewall interface
- **Timing:** After eye formation
- **P-3 Pattern:** Any pattern maximizing inner-core coverage; P-3 performs initial center fix from 10 kft
- **Deployment:** sUAS released in eye near circulation center at 10 kft; eye-diameter limitation removed
- **Option 1 (Descent Spirals):**
  - Tight, high-bank-angle counterclockwise spiral to 5,000 ft
  - Navigate to NOAA TC center location lat/lon estimate
  - Continually adjust heading to find minimum wind speed (exact center location) and lowest pressure
  - Repeat pattern descent through: 4,000 / 3,000 / 2,000 / 1,000 ft
  - **Optional extensions:** Travel radially outward at 1,000 ft to eyewall edge; briefly penetrate eyewall for 2 min; return and perform 3rd center fix if time permits
- **Option 2 (Spiral Ascent/Descent):**
  - Spiral ascent from center estimate with intermittent level-flight every 3,000 ft up to 15 kft (pending AOC/ORM approval)
  - 2 orbits per flight level before resuming spiral
  - Reverse process: descend from 12,000 ft in 3,000 ft increments to 1,000 ft
  - Second center fix after final 1,000 ft orbit
  - Tight orbit around new center at 1,000 ft with loiter until 30 min battery remains
  - **Tracking:** Maintain estimated hurricane heading and forward speed during loiter
- **Advanced Center Fix Methodology:** Per NOAA/AOC expertise—employ FD/ARWO methodology of keeping winds 90° off UAS track; program desired track parameter 90° offset to wind; employ GSHTL/GSLTR (groundspeed high/low turn left/right) logic for efficient autonomous center finding

#### **P-3 Pattern #5: Video Capture Module**
- **Target:** Hurricane boundary layer eye and eye-eyewall interface (visual documentation)
- **Timing:** After eye formation
- **Communication Constraint:** P-3 must remain within 20 nm from sUAS
- **P-3 Pattern:** Loiter within eye for duration of sUAS mission (safety permitting); alternatively, short radial legs (similar to NESDIS Ocean Winds module) maintaining ≤20 nm separation with adequate turnaround room beyond eyewall
- **Deployment:** sUAS launched in eye
- **sUAS Flight Pattern:**
  - Descend to 1,000 ft in eye to observe ocean structure
  - Transit toward eyewall for sampling
  - **Adaptive Flight:** May modify pattern to find high-wind, minimal-cloud regions for optimal camera footage
  - **Feature Documentation:** May record unique features or nearby observing platforms
- **Duration:** Up to 3.5 hr battery life possible

#### **P-3 Pattern #6: Saildrone Overflight Module**
- **Target:** Saildrone in TS-force winds or higher (V10 > 34 kt)
- **Timing:** Preferably at saildrone's estimated time of strongest conditions
- **Deployment:** sUAS released ≥20 nm upwind of saildrone in TS-force conditions
- **P-3 Pattern (Figure-4):** 
  - Coordinated overflight of saildrone with sUAS
  - Expendable deployments ~5 nm on either side of saildrone and directly overhead
  - P-3 turn executed to maintain P-3/sUAS communications and synchronized overflight timing/direction
  - P-3 deploys similar expendable pattern with concentration directly over saildrone
  - Continues with other modules maintaining required P-3/sUAS distance
- **sUAS Flight Pattern:**
  - **Stabilization Phase:** Descend to 5 kft (pending conditions)
  - **Saildrone Descent:** Descend to ≤1,000 ft (pending conditions)
  - **Primary Objective:** Flyover of actively-transmitting saildrone
  - **Extended Mission:** If battery permits, circumnavigate TC and conduct second saildrone overflight
  - **Deployment Confirmation:** P-3 confirms saildrone location, active transmission, and relevant storm characteristics (center fix, upwind gradients) before sUAS release
- **Duration:** Minimum 30+ min (highly conditions-dependent