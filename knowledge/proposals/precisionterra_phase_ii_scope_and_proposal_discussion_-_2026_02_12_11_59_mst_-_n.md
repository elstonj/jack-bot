# PrecisionTerra Phase II Scope and Proposal Discussion

## Document Metadata
- Type: Meeting notes
- Client/Agency: NASA
- Program/Solicitation: PrecisionTerra (SBIR or similar NASA program)
- Date: February 12, 2026
- BST Products/Systems Referenced: Software-defined radios (Newuond BladeRF), U-Blox ZED-F9P receiver, Analog Devices IMU, custom FPGA (in development)
- Key Personnel: Maithreyi Gopalakrishnan (lead), Beck Cotter (BST), Maciej Stachura, Daniel Prendergast, Jack Elston

## Executive Summary
Black Swift Technologies is partnering on NASA's PrecisionTerra Phase II project to develop GPS-degraded environment navigation capability using software-defined radios and sensor fusion. Phase One was delayed 44 days by government shutdown but is on track to meet the March 27th deliverable. Phase Two budget increased to $1.275 million and will focus on securing a UAS subcontractor partner for flight testing in wildfire-prone environments and developing a custom FPGA to replace off-the-shelf SDRs.

## Technical Approach

**Phase One (Current):**
- Software-defined radio (SDR) system with algorithm for GPS-degraded navigation
- Using two Newuond BladeRF SDRs to simulate L1 and L5 GPS frequencies
- U-Blox ZED-F9P receiver for comparison/benchmarking
- Analog Devices IMU for sensor data
- Ground testing in Boulder Canyon and El Dorado Canyon areas
- Artificial GPS signal degradation using "coffee strainers" as rudimentary Faraday cage
- Deliverables due March 27: signal tracking error analysis, positioning accuracy, and latency measurements

**Phase Two (Planned):**
- Custom FPGA development to replace off-the-shelf SDRs for real-time operation
- Sensor fusion integrating IMU and GPS data
- UAS-based flight testing in wildfire-prone environments (Colorado locations: Black Canyon, Roosevelt National Forest)
- UAS operates as data collection platform only; does not depend on test system navigation
- Artificial signal degradation methods for safe flight operations
- High-speed data logging requirement (millisecond/1000 Hz rate) for pseudo-range information analysis

**Key Technical Decisions:**
- Spoofing and jamming explicitly out of scope (may pursue DoD Alt PNT Challenge separately)
- UAS type (quadcopter, fixed-wing, VTOL) still under discussion with NASA technical monitor
- Estimated total payload weight: well below 5 pounds
- Phase One data collection rate: 10 Hz (lower than desired 1000 Hz); may supply custom U-Blox receivers to UAS partner if needed

## Products & Capabilities Described

**Newuond BladeRF Software-Defined Radios (qty 2)**
- Used to simulate L1 and L5 GPS signal frequencies
- Current configuration for Phase One ground testing
- Target for replacement with custom FPGA in Phase Two for real-time operation

**U-Blox ZED-F9P Receiver**
- Benchmarking receiver for Phase One testing
- Current data logging capability: 10 Hz from existing UAS installations
- BST considering supplying pre-configured units to ensure required millisecond-rate logging for Phase Two flights

**Analog Devices IMU**
- Inertial measurement unit for benchmarking against SDR output
- To be integrated via sensor fusion in Phase Two

**Custom FPGA (Phase Two)**
- Long-term roadmap item to replace off-the-shelf SDRs
- Enables real-time operation
- Feasibility improved by Phase Two budget increase to $1.275M

## Use Cases & Applications

**Wildfire Operations:**
- Flight testing planned in wildfire-prone Colorado environments
- Locations include Black Canyon and Roosevelt National Forest
- Testing simulates navigation scenarios where GPS is naturally degraded (canyon environments, signal obstruction)

**GPS-Degraded Navigation:**
- Development of receiver capable of acquiring and tracking signals in degraded GPS environments
- Relevant to navigation where signal availability is limited by terrain or obstruction
- Potential application to operations in canyons, forests, or other natural GPS-denied areas

**Broader NASA Mission Relevance:**
- UAS type selection being informed by most relevant types for NASA projects (clarification pending from technical monitor)

## Key Results (Phase One Status)

**Achievements to Date:**
- Equipment setup nearly complete as of February 12, 2026
- Data collection and processing expected by third week of February
- Successfully tested artificial signal degradation method (coffee strainers) for ground testing

**Outstanding Deliverables:**
- Signal tracking error analysis (due March 27)
- Positioning accuracy measurements (due March 27)
- Latency analysis (due March 27)

**Phase One Challenges:**
- 44-day delay from government shutdown (funds not available until December 18, 2025; equipment work began early January 2026)
- Initial focus shifted to code development due to equipment access delays
- Lower-than-desired data logging rates from existing UAS receivers (10 Hz vs. desired 1000 Hz)

## Notable Details

**Budget & Partnership:**
- Phase Two award increased to $1.275 million (significant increase from initial allocation)
- Subcontractor can take up to 50% of budget; primary need is UAS partner (no other subcontractors/consultants anticipated)
- Labor rates between BST and subcontractor do not require alignment or flow-down
- UAS subcontractor responsible for all flight coordination, approvals, and planning

**Proposal Timeline:**
- Phase Two proposal due April 6, 2026 (~two months after Phase One concludes March 27)
- Subcontractor to provide letter of commitment, budget, and budget justification

**Testing Methodology:**
- UAS used strictly as airborne platform for device elevation and data collection
- UAS navigation system independent of test system output (safety requirement)
- Test system isolation: GPS aspect evaluation only, excluding spoofing/jamming

**Team & Communication:**
- Meeting notes indicate collaborative working relationship; team congratulated lead on new baby
- Distributed action items with clear ownership and timelines
- Plan to iteratively share Phase One results with subcontractor as data becomes available