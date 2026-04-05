# Week Nine Summary – Mustang Project Effort 1

## Document Metadata
- **Type:** Weekly progress report
- **Client/Agency:** ByLight (via Black Swift Technologies)
- **Program/Solicitation:** Mustang Project - Effort 1
- **Date:** 5 December 2025
- **BST Products/Systems Referenced:** Mustang 2 aircraft (formerly "Chilli"), Hawkeye payload
- **Key Personnel:** Ethan Domagala (last editor)

## Executive Summary
Black Swift Technologies conducted additional flight testing on the Mustang 2 aircraft with propeller adaptations and weight variations, measuring power consumption to validate battery requirements for the mission profile. In parallel, BST completed significant redesign and prototype construction of the new Mustang 2 fuselage, including a reworked Hawkeye payload attachment system and aerodynamic fairings, with raw material costs under $1,000.

## Technical Approach

### Power & Endurance Analysis
- Conducted weighted flights at ~25, 30, and 35 lbs with 14x14 propeller; extended to 40 lbs with 15x13 propeller
- Measured average power consumption: **475W**
- Mission requirement: 30 m/s airspeed, 400 km range
- **Calculated endurance requirement:** 3.7 hours of flight time
- **Battery requirement:** 1,750 Wh minimum
- **Battery configuration:** 78 SA112 cells in 6s configuration (13 cells per section)

### Propeller Testing & Efficiency
- Tested 14x14 and 15x13 propellers; identified efficiency targets above 8.5 at 30 m/s
- **14x14 propellers:** Achieved very good efficiency at 30–35 lbs at 30 m/s; insufficient power for 40 lbs
- **15x13 propellers:** Good efficiency at 30 lbs and 25 m/s; significant degradation at higher weights/speeds
- Additional propellers on test: two 17x13 (in-house); 15x15 and 16x16 on order (likely to arrive after project end)
- Aircraft achieved 9.6 efficiency at 35 lbs with 14x14 propeller (including drag from test plates)

### Range Projections
Four scenario plots analyzed across weight range 35–40 lbs:
1. **Current fuselage with Amprius cells (315 Wh/kg, scaled to 299 Wh/kg for pack):** System efficiency 8–10
2. **Optimized fuselage (carbon tube, reduced weight):** Same parameters, improved range
3. **400 Wh/kg Amprius pouch cells:** Better specific energy
4. **Sea level scaled performance:** Accounts for altitude effects
- **Conclusion:** Sufficient margin exists to achieve 400 km mission within 35–40 lbs weight range with appropriate battery and propeller selection

## Products & Capabilities Described

### Mustang 2 Aircraft
- **Description:** Lightweight UAV platform for extended-range missions
- **Current configuration:** Modular propeller system, incremental mass adjustment mechanism (steel plate carrier)
- **Target airspeed:** 30 m/s
- **Target mission range:** 400 km
- **Expected endurance:** 3.7 hours at target conditions
- **Status:** Prototype fuselage under construction; power/efficiency validation in progress

### Hawkeye Payload
- **Description:** Sensor payload for Mustang 2
- **Integration approach:** Nested attachment system using fuselage tube interfaces
- **Status:** Mounting system redesigned in Week 8; integration protocol now finalized

### Mustang 2 Fuselage Prototype
- **Design approach:** Fiberglass construction with carbon-tube optimization in progress
- **Key features:**
  - Hawkeye payload nested in front fuselage tube with majority of diameters intersecting
  - Custom fiberglass cuts for clean, consistent payload positioning
  - Forward and aft aerodynamic fairings to minimize drag
  - Raw material cost: **<$1,000**
- **Status:** Prototype build complete; performance flights to follow in subsequent weeks

### Incremental Mass Adjustment Mechanism
- **Purpose:** Carrier system for variable-weight test payloads (steel plates)
- **Capability:** Supports testing up to 40 lbs in 5-lb increments
- **Status:** Modified in Week 8 to carry additional plates; used in all Week 9 flights

## Use Cases & Applications

- **Extended-range surveillance missions:** 400 km range at 30 m/s cruise speed
- **Rapid deployment scenarios:** Lightweight, modular design enables quick fuselage swaps and propeller adaptations
- **Payload-agnostic platform:** Designed to accommodate Hawkeye sensor payload with potential for other sensors

## Key Results

1. **Power consumption validated:** 475W average across test weights, confirming 1,750 Wh battery requirement
2. **Propeller optimization in progress:** 14x14 and 15x13 tested; 17x13, 15x15, and 16x16 pending
3. **Fuselage prototype complete:** Meets dimensional and weight targets; aerodynamic fairings integrated
4. **Range margin confirmed:** Analysis shows 400 km achievable within 35–40 lbs system weight using appropriate batteries and propellers
5. **Efficiency achieved:** 9.6 at 35 lbs with 14x14 propeller (exceeds 8.5 target)

## Notable Details

- **Battery selection impact:** Switching from Amprius 315 Wh/kg cells to 400 Wh/kg pouch cells significantly improves range margin
- **Carbon tube optimization:** Planned fuselage weight reduction via composite materials will further extend range
- **Payload integration:** Redesigned Hawkeye attachment system eliminates previous structural conflicts; mounting now cleaner and more aerodynamic
- **Cost efficiency:** Prototype fuselage raw materials procured for <$1,000, indicating potential for affordable manufacturing scale-up
- **Project timeline constraint:** Latest propellers (15x15, 16x16) may not arrive before project completion; performance validated with in-house alternatives
- **Test rigor:** All power/efficiency metrics include drag from test apparatus (steel plates), providing conservative real-world estimates