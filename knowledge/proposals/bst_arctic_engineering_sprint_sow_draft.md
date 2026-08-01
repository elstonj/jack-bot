# Arctic UAS Engineering Sprint – Black Swift S3 Cold-Weather Configuration

## Document Metadata
- **Type:** Statement of Work (SOW) – Final Draft (Tab 2) with preliminary draft (Tab 1) for internal review
- **Client/Agency:** NexTech Solutions LLC (NTS), on behalf of Canadian Joint Forces Command (CJFC)
- **Program/Solicitation:** Arctic UAS Phase II – Engineering Sprint and Whitehorse Test Event
- **Date:** 31 July 2026 (Final); 24 July 2026 (Draft A)
- **BST Products/Systems Referenced:** S3 tube-launched VTOL fixed-wing UAS, SwiftCore FMS, SwiftTab ground station, REX110-class EO/IR gimbal, encrypted BLOS datalink
- **Key Personnel:** Jack Elston, Ph.D., Founder and CEO (BST point of contact); Beck Cotter (last editor)

---

## Executive Summary

BST proposes an engineering sprint to advance the S3 from its current operational floor of –30 °C (operationally established) to a demonstrated capability at –30 to –40 °C with a documented path to –55 °C. The sprint combines airframe, avionics, battery, and ground-system cold-weather modifications with integration of an EO/IR gimbal and encrypted datalink. The work culminates in environmental chamber qualification and field validation prior to a Whitehorse demonstration event (scheduled November 2026). Eleven tasks are defined; four are internally funded by BST (electronics, ingress protection, payload integration, and ground station); seven are chargeable to CJFC. Total chargeable effort is approximately 950 hours over 26 weeks (nominal) or 14–16 weeks (compressed schedule for November event).

---

## Technical Approach

### Core Cold-Weather Modification Strategy

BST's approach addresses four critical domains:

1. **Airframe & Mechanical Systems (Task 2 – ~240 hrs)**
   - Replace epoxy laminating resin with low-temperature-compatible system; qualify on structural coupons first
   - Characterize and mitigate temperature-sensitive mechanical COTS (servos, motors, actuators, bearings)
   - Apply cold-rated lubricants and greases to all actuators and joints
   - Implement drained pitot-static installation with heated pitot and static ports to prevent moisture accumulation and freezing
   - Optional additions: increase propeller-to-ground clearance (~8 in), connector-free wing/tail removal

2. **BST-Manufactured Electronics (Task 3 – ~750 hrs; BST-funded)**
   - Update PCB assembly process: low-temperature-capable solder alloy, mechanical staking of large components, conformal coating
   - Change PCB substrate from FR4 to material with better low-temperature performance; requalify for impedance-controlled and high-current traces
   - Add thermostatic heating elements to temperature-sensitive sensors: inertial measurement unit (IMU), differential pressure sensors, magnetometers
   - Insulate avionics enclosure and provide conditioned volume for SwiftCore FMS warm boot
   - Characterize total active-heating power consumption; confirm energy budget against mission endurance
   - Assess antenna placement for arctic configuration

3. **Battery Thermal Management (Task 4 – ~120 hrs)**
   - Instrument battery packs and characterize cell temperature over representative mission profile from warm start
   - Validate hypothesis that self-heating under load maintains pack within operating limits once mission begins warm
   - Add insulation or active thermostatically-controlled heating only if testing shows it necessary
   - Define documented battery preconditioning and handling procedure for arctic crews with maximum cold-exposure limits

4. **Ground System & Staging (Task 5 – ~100 hrs)**
   - Convert two-case system into heated staging platform
   - Add heating elements with external power input (vehicle/snowmobile electrical systems)
   - Integrate temperature controller with setpoint control and over-temperature protection
   - Replace foam/padding with materials rated for extended temperature range; retain current case external dimensions
   - Verify warm-up time from arctic ambient to staging temperature and corresponding power draw

### Testing & Qualification Protocol (Tasks 1 & 10 – ~240 hrs combined)

**Environmental Chamber Campaign:**
- Cold-soak complete air vehicle, payload, and ground station to target temperature (–30 to –40 °C) for minimum four hours to thermal equilibrium
- At temperature: perform power-on, full avionics/FMS boot, motor spin-up, and datalink verification with data logging
- Repeat over thermal cycles to expose intermittent failures and solder/connector fatigue
- Generate qualification report documenting demonstrated cold floor and explicit path to –55 °C
- Chamber access: Boulder-area facility to approximately –20 °C; commercial facility for colder soak

**Thermal Survey & Instrumentation:**
- Identify temperature-sensitive components and instrument for chamber campaign
- Produce requirements verification matrix traceable to CJFC questionnaire and SOW

### Payload Integration & Qualification (Tasks 7 & 8 – ~240 hrs BST internally funded + ~130 hrs chargeable)

**EO/IR Gimbal & Datalink Integration (Task 7 – BST-funded; not charged to CJFC):**
- Mechanical and electrical integration of REX110-class EO/IR gimbal with payload bay provisions, power, and thermal interface
- Integrate long-range encrypted datalink and payload antenna; coordinate placement with avionics assessment
- Verify video stabilization, image roll compensation, recording, and H.264/H.265 compression through integrated chain
- Verify gimbal modes: object tracking, geolocation stare, manual slew
- Flight-test to confirm modeled 160 km / 120 min endurance and range with payload installed
- **Note:** Full BLOS range qualification is follow-on work; sprint deliverable is demonstrated integration at standard temperature, not production configuration

**EO/IR Payload Cold-Weather Qualification (Task 8 – Chargeable; ~130 hrs BST + subcontract):**
- Characterize payload at temperature: gimbal motor torque and slew rate, bearing and lubricant drag, focus/zoom mechanism behavior, optical window frost/condensation, detector performance shift
- Define cold-weather requirement set to be flowed to sensor manufacturer (equivalent to airframe/avionics modifications)
- Manage subcontract with sensor manufacturer; review design approach, analysis, and test evidence
- Integrate payload heating and insulation into S3 payload bay, including optical window defogging/de-icing provisions (coordinated with heated-case approach)
- Include payload in Task 10 chamber campaign; verify gimbal modes and full-motion video chain at temperature
- **Sensor Manufacturer Subcontracted Tasks:**
  - Cold-weather design revisions equivalent to BST modifications: conformal coating, low-temperature lubricants, component-level heating, staking, substrate/process changes
  - Vendor requalification of modified payload at target cold floor; deliver test evidence to BST

### Integrated Control Station (Task 9 – ~140 hrs; BST-funded)
- Unified SwiftCore/SwiftTab ground station controlling both air vehicle and payload from single interface
- Design for gloved operation and legibility in high-glare snow conditions
- Reduce operator workload in arctic environment

### Field Validation & Event Support (Task 11 – ~120 hrs)
- Conduct cold-weather field flights at Colorado high-altitude winter site prior to deployment
- Update crew procedures, checklists, operator handbook for arctic configuration
- Ship system and batteries to Whitehorse with hazmat documentation
- Provide two BST personnel on-site for 8 days (setup, demonstration flights, teardown)
- Produce post-event report capturing performance against objectives and lessons learned

---

## Products & Capabilities Described

### Black Swift S3
- **What it is:** U.S.-manufactured, EAR99 classified, tube-launched VTOL fixed-wing UAS
- **Current baseline performance:**
  - Operational temperature floor: –30 °C (operationally established, not chamber-qualified)
  - Operational temperature ceiling: +46 °C
  - Maximum sustained wind: 30 kt
  - Endurance/range: 160 km / 120 min with EO/IR payload (modeled); 200 km / 150 min clean (sea level, standard day)
  - Ingress protection: IP42/43 with sealed avionics bay
  - Stored footprint: Two hard cases – airframe 62 × 27 × 13 in / 85 lb; payload and GCS 42 × 25 × 12 in / 75 lb
- **Arctic configuration objectives:**
  - Demonstrate cold-soak operation at –30 to –40 °C (chamber-verified and field-validated)
  - Establish documented engineering path to –55 °C (full qualification deferred as follow-on)
  - Improve ingress protection toward IP54 with anti-icing provisions
  - Reduce crew burden for assembly, battery handling, launch with arctic gloves from heated staging case
  - Qualified for sustained arctic operation with staged maintenance

### SwiftCore FMS
- **What it is:** BST-manufactured flight management system with temperature-tolerant COTS electronics
- **Cold-weather modifications:** Avionics enclosure insulation with conditioned volume for warm boot; thermostatic heating of IMU, differential pressure sensors, magnetometers; updated PCB assembly process and substrate selection for low-temperature performance

### REX110-Class EO/IR Gimbal
- **What it is:** Stabilized full-motion video and recording payload (external procurement, manufacturer to be subcontracted for cold-weather qualification)
- **Integration:** Mechanical/electrical integration onto S3 payload bay with gimbal motor heating, lubricant revision, optical window de-icing
- **Performance claims:** Stabilized video with object tracking, geolocation stare, manual slew modes; H.264/H.265 compression; 160 km range / 120 min endurance with S3 (modeled)
- **Cold-weather qualification includes:** Gimbal motor torque and slew rate characterization, bearing drag, focus/zoom behavior, optical window management, detector performance shift at temperature

### Long-Range Encrypted BLOS Datalink
- **What it is:** Encrypted beyond-line-of-sight radio for secure S3 command and payload data downlink
- **Integration:** Coordinated with avionics antenna placement; full range qualification deferred as follow-on work
- **Demonstration maturity:** Demonstrated at standard temperature; arctic environmental qualification included in chamber campaign

### Heated Arctic Staging Cases
- **What it is:** Conversion of baseline two-case system (airframe + payload/GCS) into heated staging platform
- **Capability:** Heating elements with external power input from vehicle/snowmobile electrical systems; temperature controller with setpoint control and over-temperature protection; maintains staging temperature at target arctic ambient; documented warm-up time and power draw
- **Design objective:** Enable staged operation (assembly, battery handling, launch) by two operators in arctic gloves from conditioned environment

---

## Use Cases & Applications

### Arctic Operations
- **Primary focus:** Sustained UAS operation in arctic environment (–30 to –40 °C; path to –55 °C)
- **Staging:** Heated case system enabling deployment from vehicles/snowmobiles without heated facilities
- **Crew efficiency:** Gloved operation reducing dexterity burden; two-operator minimum
- **Mission profile:** 120–150 min endurance, 160+ km range, full-motion EO/IR payload

### Demonstration & Validation
- **June 2026 Area XO Demonstration:** Baseline cold-weather performance assessment; identified handling deficiencies (Ottawa demonstration reference)
- **November 2026 Whitehorse Test Event:** Field validation of sprint modifications under representative arctic conditions; Canadian Joint Forces Command demonstration

### Operational Vignettes (to be confirmed with CJFC)
- Ingress/border surveillance from arctic staging bases
- Infrastructure inspection (pipelines, power lines) under winter conditions
- Search and rescue coordination in remote arctic terrain
- Long-duration ISR from forward-deployed positions

---

## Key Results (for reports)

This is a **Statement of Work and proposal** rather than a results report. However, it establishes baseline performance that will be validated:

### Baseline Cold-Weather Performance (Operationally Established)
- Operational floor: –30 °C (from cumulative field operation in high-altitude and winter campaigns)
- No prior chamber qualification at this floor

### Sprint Exit Criteria (to be demonstrated by project completion)
1. **Airframe:** Structural coupon and flight-surface test data showing integrity