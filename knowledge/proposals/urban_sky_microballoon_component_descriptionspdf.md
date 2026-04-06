# Urban Sky Microballoon Component Descriptions

## Document Metadata
- **Type:** Product catalog / component description sheet
- **Client/Agency:** N/A (internal product listing for acquisition; appears to be prepared for NASA Balloon Observations program via subcontract)
- **Program/Solicitation:** UrbanSky_subcontract / NASA Balloon Observations
- **Date:** Current as of 03/18/2025
- **Organization:** Urban Sky (www.UrbanSky.com, Denver, CO)
- **Last Editor:** Beck Cotter
- **Classification:** Confidential and Proprietary

## Executive Summary
Urban Sky manufactures small, rapidly deployable, low-cost zero-pressure stratospheric remote sensing systems called Microballoons™. This document provides itemized descriptions of all available equipment, software, services, and payloads. The company offers two microballoon classes (exempt and non-exempt under US regulations) with payload capacities ranging from 4–50 lbs, along with control systems, fill hardware, mission software, training, and specialized sensor payloads.

## Technical Approach & System Architecture

### Core Microballoon Design Philosophy
- **Zero-pressure design:** Open or poppet nadir allows pressure equilibrium at float altitude
- **Rapid deployment:** Single operator can launch in <10 minutes; capable of launch in winds up to ~20 knots
- **Placeable/fixed-altitude:** Designed for on-station operations above specific target areas
- **Redundant termination:** Primary (Apex) + secondary (RadioTerm) termination devices with geofence and timer-based safeguards
- **Command & control:** Via Iridium satellite network through mission control software

### Avionics Core Components

**Apex Flight Computer (Primary):**
- Provides telemetry (position, health, status) to mission control
- Enables C2 via Iridium satellite network
- Controls lift-gas valve for altitude descent
- Primary termination device (full lift-gas release)
- Accepts programmable geofence boundaries
- Timer-based termination safeguard

**RadioTerm (Secondary Termination Device):**
- Backup valve-controlled descent
- Redundant lift-gas release in case Apex fails
- Accepts separate geofence configuration from Apex
- Autonomous trigger if communication lost

**Additional Systems:**
- SPOT GPS device (backup positioning)
- Pre-rigged flight-ready parachute
- QuickFill™ lift-gas fill port and disconnect
- High-performance, specially treated balloon envelope material
- Nadir payload attachment interface

---

## Products & Capabilities Described

### EXEMPT CLASS: 12-Gore (82 m³) Microballoon

**Item #MBAL2: Apex 2 Microballoon™ (without Ballaster)**
- **Payload capacity:** 4–12 lbs (individual packages ≤6 lbs each)
- **Altitude control:** Downward only (Apex valve venting)
- **Float altitude:** ~65,500 ft with 6 lb payload; ~57,000 ft with 12 lb payload
- **Flight duration:** ~10 hours
- **Parachute:** 1.8m diameter
- **Lead time:** 60 days post-contract
- **Nadir type:** Open (enables zero-pressure equilibrium)
- **Compliance:** 14 CFR Part 101.1(a)(4) – Exempt Unmanned Free Balloon

**Item #MBAL3: Apex 2 Microballoon™ (with Ballaster)**
- **Payload capacity:** 4–12 lbs total (plus 2.1 kg / 4.6 lb ballast media)
- **Altitude control:** Bidirectional—descent (vent gas), ascent (drop ballast in 1-gram increments)
- **Ballast preload:** 2.1 kg for 6 lb payload; supports up to 30 hours operation
- **Float altitude:** ~65,500 ft with 6 lb bottom-of-balloon mass; ~57,000 ft with 12 lb
- **Key capability:** Station-keeping and wind-layer navigation; required for overnight missions (addresses nighttime envelope cooling)
- **Parachute:** 1.8m diameter
- **Lead time:** 60 days post-contract
- **Nadir type:** Open
- **Compliance:** 14 CFR Part 101.1(a)(4) – Exempt Unmanned Free Balloon

---

### NON-EXEMPT CLASS: 16-Gore (205 m³) Microballoon

**Item #MBAL7: Apex 2 Microballoon™ (with Ballaster)**
- **Payload capacity:** 12–50 lbs
- **Altitude control:** Bidirectional—descent (vent gas), ascent (drop ballast in 1-gram increments)
- **Ballast preload:** 3.8 kg / 8.3 lb for 12 lb payload; supports up to 30 hours operation
- **Float altitude:** ~68,500 ft with 12 lb payload; ~51,400 ft with 50 lb payload
- **Flight duration:** Up to 30 hours (depending on launch time)
- **Parachute:** 3m diameter
- **Nadir type:** Poppet (pressure-actuated; improves performance by reducing unwanted air mixture with lift gas)
- **Lead time:** 60 days post-contract
- **Compliance:** 14 CFR Part 101 Subpart D – Non-Exempt Unmanned Free Balloon

---

### Refurbishment Services

**Items #RFURB2, #RFURB3, #RFURB7: Microballoon Refurbishment**
- **Scope:** Apex 2 Microballoon systems (12-gore or 16-gore, with/without ballaster)
- **Services include:**
  - Inspection and servicing of flight avionics hardware, firmware, batteries
  - Refurbishment of Apex, RadioTerm, envelope, parachute, case
  - Ballaster refill (2.1 kg or 3.8 kg) if applicable
  - Envelope replacement (new envelope provided if unrefurbishable)
- **Customer responsibility:** Check/replace SPOT GPS tracker batteries
- **Lead time:** 30 days post-contract

---

### Fill Systems & Launch Hardware

**Item #FILL1: Helium Compatible Fill System**
- Main 12-ft hose + 2-ft ganger (connects to 1–2 standard CGA-580 helium T-bottles)
- Pressure-rated fittings, hose, valves for safe gas flow modulation
- Fabric case with spare parts, fittings, O-rings
- Hydrogen-compatible option available upon request

**Item #FILLGANG1: Helium Compatible Fill Hose Single Gang Extension**
- 2-ft ganger for connecting additional helium tanks beyond the max qty 2 with FILL1
- Multiple gang extensions can be combined for heavy-mass payload lift
- Pressure-rated fittings, hose, valve
- **Lead time:** 15 days post-contract

**Item #MAST1: Hitch-Mounted Microballoon™ Launch Mast System**
- Patented Urban Sky launch method
- All hardware for hitch-mounted launch from any compatible vehicle
- Enables single-operator mobile launch
- **Lead time:** 15 days post-contract

---

### Payload Protection & Parachutes

**Items #PCAGE1 & #PCAGE2: Urban Sky Payload Landing Cages**
- **PCAGE1 (12-Gore exempt class):** Plastic fittings + hollow carbon fiber rods + elastic bands
- **PCAGE2 (16-Gore non-exempt class):** Aluminum fittings + solid carbon fiber rods + elastic bands
- Standard mechanical interface, physical size/mass limitations, speeds, and loads documented in ICD (available on request)
- **Lead time:** 15 days post-contract

**Items #USKYCHU1 & #USKYCHU2: Custom Ultra-Lightweight Toroidal Parachutes**
- **USKYCHU1:** 1.8m diameter, drag coefficient 2.2, mass 155 grams (lighter payloads)
- **USKYCHU2:** 3m diameter, drag coefficient 2.2, mass 350 grams (heavier payloads)
- Both for exempt class 12-gore microballoon
- **Lead time:** 15 days post-contract

---

### Lift Gas Supply

**Item #HET300: Helium in T-300 Tanks**
- Standard T-300 carbon steel tanks (~9.25" OD × 55" length)
- Internal volume: 49 liters; weight when filled: ~135 lbs
- Capacity: ~284 cubic feet of helium at 2,400 psi
- Delivered to customer-specified address
- **Lead time:** 30 days post-contract (requires recipient name, phone, delivery address at order)

---

## Software Products

**Item #SKYSOF1: Urban Sky Flight Planning & Mission Control Annual Software License (per user)**

**Features:**
- White-labeled, dedicated customer instance
- Simultaneous mission planning/control (unlimited balloons in air)
- Historical data logging, analysis, document control, user management
- Mobile flight planning & mission control (iOS, Android support)
- Command & control UI for Apex termination system with flight tracking
- Real-time in-flight scenario planning and analysis
- Feature layers: sectionals, population density maps, topographic maps
- Unlimited flight predictions, active missions, archive data for post-flight analysis
- 2 hours/month maintenance support from Urban Sky software team
- Compatible with Esri ArcGIS; ingests 2D/3D shapefile AOIs
- **Licensing:** Per unique user (1-year annual); individual licenses non-transferable; each assigned to one person
- **Lead time:** 1 day post-contract

---

## Services

### Training

**Item #TRAIN1: Microballoon & Mission Control Training – Urban Sky Facility (Denver, HQ)**
- 3-day program for up to 20 students
- Includes 2 balloon launches
- **Day 1:** Classroom instruction (all)
- **Day 2:** Split into 2 groups—Group 1 launches/recovers; Group 2 runs mission control
- **Day 3:** Groups rotate functions
- **Lead time:** 15 days post-contract

**Item #TRAIN2: Microballoon & Mission Control Training – Customer Site**
- 3-day program for up to 20 students at customer site or agreed 3rd party location
- Includes 2 balloon launches
- Same structure as TRAIN1
- **Lead time:** 30 days post-contract (includes location viability validation and travel coordination)

### Operations Support

**Item #OPSSUP: Mission Operations Personnel – Exercise Support**
- On-site launch and recovery operations support by Urban Sky expert
- Includes local flight & recovery planning, actual launch/recovery ops
- 24/7 remote Mission Control support: flight planning, altitude control decisions, navigation planning, landing/recovery planning, technical support
- Quoted in 1-day increments; up to 5 days/week available
- All food, travel, lodging for Urban Sky personnel included
- **Lead time:** 30 days post-contract

---

## Payload Systems

### Buses

**Item #BUS1: Urban Sky High-Altitude Power and Communications Bus with Starlink (SATCOM) and Tactical Radio (LOS)**

**Modular platform for microballoon-deployed payloads. Functions:**

- **Power Management:** Configurable power outputs; modular battery packs
- **Communications:** Secure IP-based data backhaul, live streaming, C2 via interchangeable tactical radio systems
  - Starlink (BLOS)
  - Tactical radio options: MPU5, Silvus, or goTenna (LOS)
- **Positioning & Navigation:** Position, attitude, heading via onboard sensors + Kalman-filter processing (tailored for balloon dynamics)
- **Payload Integration:** Structural mounting, quick-disconnect interfaces, modular accessories for diverse configurations
- **Edge Computing:** Optional Linux-based computing environment for real-time analytics and payload operations

**Item #BUS-Lite: High-Altitude Power and Communications Bus with Starlink (SATCOM) only**
- Same as BUS1 except no tactical radio (no LOS command/control/com