# Week Three Summary - Mustang Project Effort 1

## Document Metadata
- Type: Project status/progress report
- Client/Agency: By Light (ByLight)
- Program/Solicitation: Mustang Project - Effort 1
- Date: 24 October 2025
- BST Products/Systems Referenced: Mustang aircraft platform, autopilot systems
- Key Personnel: Jack Elston (last editor)

## Executive Summary
Black Swift Technologies conducted the third week of the Mustang Project for By Light, focusing on testing the current Mustang platform with increased payload and initiating design of a new, higher-performance aircraft variant. Testing included a 5 lb payload flight to validate performance predictions, while design efforts began on a new platform based on a SoaringUSA Chilli GPS airframe with custom fuselage and empennage to meet mission range and payload requirements.

## Technical Approach

### Current Platform Testing
- Added 5 lb (2.27 kg) payload to existing Mustang fuselage with optimal weight placement to maintain center of gravity (CG) at 75mm aft of leading edge
- Conducted flight test on 10/24/2025 at 10 AM MST with Gross Take Off Weight (GTOW) of 17.84 lbs (8,092g)
- Car launch speed: 65 mph (increased from baseline due to added weight)
- Cruise speed: 30 m/s; estimated stall speed: 26 m/s
- Flight duration: 31.8 minutes with ~26% battery consumption
- Average cruise power: 253W
- Used modified propeller selection to improve efficiency from previous test

### New Aircraft Design Platform
- Selected SoaringUSA Chilli GPS Double Carbon as COTS prototype airframe
- 15.25 foot wingspan for increased efficiency and range capability
- Plans for custom fuselage and empennage design (weeks 4-5)
- Propulsion system: KDE Direct 465Kv brushless motor + TBS Lucid 90A ESC
- Propeller: Starting with APC 12x12 (efficiency study ongoing)
- Motor pylons: One per wing, detailed trade analysis in progress for week 4

## Products & Capabilities Described

### Mustang Platform
- Current aircraft being tested and incrementally loaded
- Capable of sustained flight at 30 m/s cruise speed
- Responsive autopilot control system
- Battery-powered electric propulsion
- Suitable for payload testing and performance validation

### New Chilli-based Platform (in development)
- Long-range design targeting 400 km range capability
- High-efficiency wing design (15.25 ft span)
- Custom fuselage/empennage to optimize for specific mission
- Motor pylon design for twin-engine configuration (one per wing)

## Use Cases & Applications
Long-range autonomous aircraft mission with the following requirements:
- Minimum 400 km range
- Cruise speed ≥ 30 m/s
- 4.14 kg payload capacity
- High efficiency for extended endurance operations

## Key Results

**5 lb Payload Flight Test:**
- Aircraft successfully flew at increased weight with manageable handling characteristics
- Validated telemetry collection including airspeed, altitude, roll, pitch, power consumption, and throttle settings
- Propeller change resulted in substantial power efficiency improvement (253W average cruise vs. "fairly poor" previous efficiency)

**Performance Extrapolation Analysis:**
- At current 5 lb test weight: achievable payload approximately 2.9 kg at 35 lbs total weight (30% below 4.14 kg requirement)
- Critical constraint identified: At 35 lbs total weight, required cruise speed is 42 m/s, necessitating 90 mph car launch speed (exceeds safe 65 mph limit)
- Propeller efficiency expected to decrease substantially at higher speeds, likely insufficient for required thrust
- **Realistic capability at safety-limited 65 mph car launch:** ~1 kg payload maximum
- Alternative configuration at 30 lbs total + 4 kg payload: maximum range of 214 km (below 400 km requirement)

**Conclusion:** Current Mustang platform will not satisfy the 400 km range + 4.14 kg payload mission requirements; new COTS-based platform development justified.

## Notable Details

- BST engineers have prior success with KDE Direct 465Kv motors
- Payload mounting points designed for reliable, repeatable installation/removal while maintaining consistent CG
- Prototype COTS Chilli build-up estimated for mid-week 4 completion
- Custom fuselage/empennage design strategy to be documented in weeks 4-5 reports with CAD and material analysis
- Document notes confidentiality restrictions on proprietary information
- Flight testing conducted with estimated stall speed monitoring for safety during fast landings