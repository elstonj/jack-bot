# S0-VTOL Fire-Weather Profiling: Filling the Boundary-Layer Gap in Wildfire Forecast Operations

## Document Metadata
- Type: Proposal / White Paper (in development, marked "redline")
- Client/Agency: NOAA National Weather Service (NWS), OAR Weather Program, Incident Meteorologist (IMET) cadre
- Program/Solicitation: NOAA standing BAA (open through 30 Sep 2026) or SBIR Phase III
- Date: 6 August 2026 (FY26 year-end)
- BST Products/Systems Referenced: S0-VTOL UAS, SwiftCore flight management system
- Key Personnel: Jack Elston (last editor), Daniel Pendergast (point of contact), coordination with KrateoSky Inc.

## Executive Summary
Black Swift proposes to field 10 S0-VTOL fire-weather profiling systems to NOAA National Weather Service Weather Forecast Offices and the IMET program to provide automated vertical atmospheric profiles (wind, temperature, humidity, pressure) over wildfire incidents—filling a critical gap in boundary-layer observation that surface stations and sparse radiosondes cannot address. The effort includes data pipeline development for AWIPS integration, operator training, and one fire season of field support, requested at $1.25M in expiring FY26 ORF funds for 2027 operational capability.

## Technical Approach
- **Autonomous profiling missions**: S0-VTOL operates fully autonomous to 15,000 ft AGL with 90-minute endurance at 3.5 lb gross weight
- **Launch/deployment**: Vertical takeoff from any clearing; no launcher, runway, or specialized personnel required; deployable by single IMET
- **Wind estimation**: Custom algorithms deliver accurate 3-D wind profiles with 0.38 m/s velocity resolution, plus temperature, humidity, and pressure data
- **Data pipeline**: Profile data formatted for AWIPS ingest and HRRR/RRFS verification studies with OAR/GSL
- **Flight management**: All systems operate under SwiftCore™ flight management system (U.S.-designed, U.S.-manufactured)
- **Recovery**: Designed as recoverable, reusable alternative to expendable radiosondes at incident command posts

## Products & Capabilities Described

### S0-VTOL UAS
- **What it is**: Vertical-takeoff UAS at 3.5 lb gross weight with 90-minute endurance to 15,000 ft AGL
- **Fire-weather mission profile**: Autonomous profiling missions generating 3-D wind, temperature, humidity, and pressure profiles
- **Modular payload architecture**: Supports wind-estimation sensors plus smoke/air-quality and trace-gas sensors for plume characterization
- **Demonstrated operations**: Validated in volcanic plumes, wildfire environments, and mountainous terrain; autoland precision demonstrated (10 consecutive autolands within 10 ft radius per AF192-005 validation)
- **Specification**: 0.38 m/s wind velocity resolution

### SwiftCore™ Flight Management System
- U.S.-designed, U.S.-manufactured autonomous flight control
- Enables fully autonomous profiling missions

## Use Cases & Applications
- **Primary**: Boundary-layer profiling over active wildfire incidents to support fire-weather forecasting and incident meteorologist operations
- **Secondary**: Smoke/air-quality and trace-gas plume characterization missions using same airframe
- **Historical context**: NightFOX/FIREX plume penetration work; 2023 wildfire payload research (Stachura/Elston); NASA Phase I wildfire autonomy proposal (AERO.7.S26B)

## Proposed Scope & Deliverables
- **Ten S0-VTOL fire-weather profiling systems** fielded to priority Weather Forecast Offices and IMET program (western region focus)
- **Automated profile-to-forecast pipeline**: AWIPS-formatted data ingest; HRRR/RRFS verification studies with OAR/GSL
- **IMET operator training and certification support**: COA/Part 107 operational documentation templates
- **Field engineering support**: One fire-season on-call support and consumables

## Budget Breakdown (Rough Order of Magnitude)
| Element | Amount |
|---------|--------|
| S0-VTOL systems (10) with fire-weather sensor payloads & spares | $780,000 |
| AWIPS/model-verification data pipeline development | $190,000 |
| IMET training, certification & airspace documentation | $145,000 |
| Season field support & consumables | $135,000 |
| **Total** | **$1,250,000** |

## Key Problems Addressed
- **Boundary-layer observation gap**: Fire behavior governed by inversion strength, low-level jets, and moisture recovery invisible to surface RAWS stations and too sparse in radiosonde network
- **IMET operational deficit**: Incident meteorologists deployed to incidents forecast with almost no vertical profile data over the fire itself
- **Regulatory advantage**: Covered-foreign-entity UAS restrictions exempt marine and atmospheric science procurement, favoring U.S.-manufactured systems

## Period of Performance & Obligation Path
- **Duration**: 12 months (target 2027 fire season initial operating capability)
- **Funding vehicle**: NOAA standing BAA (award before 30 Sep 2026 obligates expiring FY26 ORF funds) or SBIR Phase III
- **Strategic alignment**: Non-severable capability deliverable (fielded, trained, verified fire-weather profiling system) positions NWS with concrete uncrewed-systems success for FY27 congressional budget process (H.R. 8845, H. Rept. 119-652)

## Notable Details & Critical Editor Notes

**Strengths identified in redline:**
- Demonstrated precedent: NightFOX/FIREX plume penetration, 2023 Stachura/Elston wildfire payload paper, NASA Phase I wildfire autonomy proposal
- Regulatory advantage from U.S. manufacturing and marine/atmospheric science exemptions
- Congressional attention to wildfire forecasting and domestic UAS procurement

**Critical gaps flagged by editor (Jack Elston):**

1. **Airspace authority conflict**: Proposal treats airspace as paperwork. Part 107 caps at 400 ft AGL; 15,000 ft profiling requires COA or waiver. Over an active incident, interagency aviation approval and air operations branch (not FAA alone) govern access. "An IMET launching to 15,000 ft inside a fire TFR alongside air attack and tanker traffic is not a documentation exercise."

2. **Recovery risk under-addressed**: Recovery in fire-weather winds and terrain-driven turbulence with no published gust limit on S0-VTOL is flagged as "real risk item." Partial mitigation: AF192-005 validated 10 consecutive autolands within 10 ft radius.

3. **Mission conflict**: Paper promises both 15,000 ft profiling AND plume characterization on same 60-minute airframe. Trace-gas payload cuts endurance and climb performance; ROM budget does not account for it. Editor notes: "Pick one mission per sortie and say so."

4. **Customer continuity overstated**: Paper implies continuity from NOAA hurricane work; editor notes "there isn't any." Directive: "Say plainly that NWS is a new customer" and rely on documented precedent (NightFOX/FIREX, wildfire papers, NASA proposal).

5. **Training/airspace budget unrealistic**: $145K line item scoped as if COA templates settle interagency aviation approval question; editor notes "does not buy interagency aviation approval."

## Status
Document is in active redline phase (draft with substantial editorial comments); not yet final proposal submission.