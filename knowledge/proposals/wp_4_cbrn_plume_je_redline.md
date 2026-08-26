# Autonomous Aerial CBRN Plume Characterization and Atmospheric Transport Support

## Document Metadata
- **Type:** Whitepaper / proposal (in development/redline draft)
- **Client/Agency:** Joint Program Executive Office for CBRN Defense (JPEO-CBRND)
- **Program/Solicitation:** SBIR Phase III sole-source; direct award opportunity (new customer)
- **Date:** 5 August 2026
- **BST Products/Systems Referenced:** S0-VTOL, S3, SwiftCore FMS
- **Key Personnel:** Jack Elston (editor); Daniel Pendergast (POC); KrateoSky, Inc. coordination

## Executive Summary
Black Swift proposes to integrate government-nominated CBRN point and standoff sensors onto the S0-VTOL and S3 platforms to autonomously characterize chemical/biological/radiological plumes and provide real-time meteorological and concentration profiles for atmospheric transport and dispersion (ATD) modeling. The 12-month effort would include payload integration, chamber/field trials, and capstone demonstration, aimed at delivering hazard-prediction accuracy for CBRN incident response.

## Technical Approach

**Core Capability:**
- Deploy S0-VTOL (autonomous profiling to 15,000 ft AGL) and S3 aircraft with integrated CBRN sensors and meteorological instrumentation
- Capture wind, temperature, and atmospheric stability profiles that drive ATD/dispersion models (JEM/HPAC family)
- Provide real-time data feed formatted for ATD model ingest and common operating picture (COP) display
- Autonomous operations via SwiftCore FMS sensor-driven autonomy (capable of concentration-gradient following, though editors note response-time limitations with CBRN detectors)

**Integration & Validation:**
- Payload integration engineering for two sensor types across two airframes
- Chamber and open-air simulant trials characterizing detection performance and plume-mapping concept of employment
- Real-time data pathway integration with JEM-compatible systems

## Products & Capabilities Described

### S0-VTOL
- Autonomous vertical profiling to 15,000 ft AGL
- Modular payload architecture supporting trace-gas detection and air-quality sensors
- Proven in corrosive, particulate-dense environments (volcanic plume missions)
- All-U.S. design and manufacture; NDAA section 848 and covered-entity compliant supply chain

### S3
- Modular payload interface compatible with CBRN point and standoff sensors
- Designed for atmospheric profiling and hazard characterization

### SwiftCore FMS
- Sensor-driven autonomy enabling concentration-gradient-following flight patterns
- Keeps operator out of hazard area by autonomous plume tracking (qualified by volcanic plume heritage, but editors note practical limitations with slow-response CBRN detectors)

## Use Cases & Applications
- **CBRN incident response:** Real-time plume characterization and hazard prediction
- **Atmospheric transport modeling:** In-situ meteorological profiling to improve dispersion model accuracy
- **Operational support:** Autonomous data collection for common operating picture and command decision support
- **Hazard avoidance:** Autonomous flight keeps personnel out of contaminated areas during sampling

## Proposed Scope & Rough Order of Magnitude

| Element | Budget |
|---------|--------|
| Payload integration engineering (2 sensor types, 2 airframes) | $540,000 |
| Aircraft systems, spares & ground stations (4 aircraft) | $430,000 |
| Simulant trials & capstone demonstration | $330,000 |
| ATD/JEM data pathway & COP integration | $200,000 |
| **Total** | **$1,500,000** |

**Period of Performance:** 12 months (integration, trials, demonstration)

## Notable Details

**Funding Alignment:**
- FY2026 O&M and FY2025 RDT&E funds expire 30 September 2026; proposal targets year-end execution requirements ($1–2M band)
- Executable via SBIR Phase III sole-source authority under 15 U.S.C. § 638(r), enabling award in weeks without further competition
- Direct award to new customer (first JPEO-CBRND relationship)
- Provides small-business participation credit for agency

**Supply Chain & Compliance:**
- All-U.S. design and manufacture
- Consistent with NDAA section 848 and covered-entity restrictions

---

## **EDITOR'S CRITICAL NOTES** (from redline feedback)
The document contains several unresolved technical and programmatic issues flagged by internal review:

1. **Payload Weight Problem:** JCAD-class point detectors (~1.6 kg) consume nearly the entire useful load of S0-VTOL before radiological sensors are added. "Promising point AND standoff across two airframes with no payload budget is the physics problem in this paper."

2. **Sensor Response Time Mismatch:** Autonomous gradient-following requires fast-responding sensors; most CBRN point detectors have multi-second to multi-minute response times and duty cycles incompatible with real-time plume tracking.

3. **Simulant Trials Unexecutable:** BST lacks chamber, simulant handling facility, surety procedures, decontamination protocols, and trained/cleared personnel for agent-simulant work. The $330K trial line does not fund required subcontract to national lab or West Desert Test Center. Additionally, separate KrateoSky kickoff material identifies decontamination hardening as a required enhancement, which this proposal omits.

4. **JEM/HPAC Integration Unfunded:** $200K allocated for ATD/JEM interface work; editors note BST has no heritage in this area and recommends either finding a partner or removing the line.

5. **Lack of CBRN Heritage:** Editors recommend reframing as trace-gas/aerosol profiling (proven heritage on S0) swapped into CBRN point detector interface, rather than overstating autonomous plume-tracking capability.

**Recommendation:** Address payload SWaP constraints, subcontract modeling, and technical realism before formal submission.