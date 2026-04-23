# Slack Channels Overview

Last scanned: 2026-04-23 02:18

Total channels scanned: 15

## Channels

- **#2025-nasa-autonomy** -- 1 messages -- [2025-nasa-autonomy.md](2025-nasa-autonomy.md)
- **#25_1-navy-sbir-magnetometer** -- 25 messages -- [25_1-navy-sbir-magnetometer.md](25_1-navy-sbir-magnetometer.md)
- **#25_1-navy-sttr-boundary-layer** -- 4 messages -- [25_1-navy-sttr-boundary-layer.md](25_1-navy-sttr-boundary-layer.md)
- **#by-lite-mustang** -- 2 messages -- [by-lite-mustang.md](by-lite-mustang.md)
- **#commercial-sales** -- 15 messages -- [commercial-sales.md](commercial-sales.md)
- **#emass** -- 42 messages -- [emass.md](emass.md)
- **#emass-bst** -- 40 messages -- [emass-bst.md](emass-bst.md)
- **#flight-testing** -- 66 messages -- [flight-testing.md](flight-testing.md)
- **#general** -- 5 messages -- [general.md](general.md)
- **#grants-and-funding** -- 18 messages -- [grants-and-funding.md](grants-and-funding.md)
- **#logparse-website** -- 21 messages -- [logparse-website.md](logparse-website.md)
- **#marketing** -- 19 messages -- [marketing.md](marketing.md)
- **#operations** -- 13 messages -- [operations.md](operations.md)
- **#s3** -- 95 messages -- [s3.md](s3.md)
- **#sbir-hurricane** -- 53 messages -- [sbir-hurricane.md](sbir-hurricane.md)

## Strategic Summary

# Black Swift Technologies - Strategic Slack Overview

## Cross-Channel Themes

### 1. **Core Business: Aircraft Development & Platforms**
BST operates a diverse fleet of unmanned aircraft systems serving distinct missions:
- **Fixed-wing platforms**: S2, S0 (hurricane reconnaissance), S1-VTOL
- **VTOL platforms**: S3 (hybrid quadcopter with tilting rotors, 2-3hr endurance)
- **Multirotor platforms**: E2, Flamewheel
- **Customer platforms**: By Light Mustang (USAF contract)

All aircraft development channels (#s3, #by-lite-mustang, #flight-testing) converge on Jack Elston and Joshua Fromm for systems/firmware decisions.

### 2. **Government Contracting & Funding (Primary Revenue Driver)**
Active pursuit across federal agencies with structured pipeline:
- **Navy SBIR/STTR**: Magnetometer integration (#25_1-navy-sbir-magnetometer), boundary layer sensing (#25_1-navy-sttr-boundary-layer)
- **NASA**: 2025 autonomy Phase I project (#2025-nasa-autonomy)
- **NOAA/USDA/DOD**: Ongoing proposals tracked in #grants-and-funding
- **Decision pattern**: Jack Elston drives funding strategy; Maciej and Dan Prendergast support technical proposals; Meredith manages budgets

### 3. **Critical Personnel & Decision Authority**

| Person | Primary Role | Key Channels |
|--------|--------------|--------------|
| **Jack Elston** | CEO/Technical Lead | #general, #grants-and-funding, all technical channels |
| **Maciej** | Operations/Flight Testing Lead | #flight-testing, #s3, project coordination |
| **Joshua Fromm** | Hardware/Design Lead | #s3, #flight-testing, #operations |
| **Dan Prendergast** | Project Management/Proposals | #emass, #sbir-hurricane, #grants-and-funding |
| **Ben Busby** | Infrastructure/Backend Dev | #logparse-website, data systems |
| **Beck Cotter** | Hardware Integration | Navy projects, flight testing |

### 4. **Data & Infrastructure (Enabling Layer)**
**#logparse-website**: SwiftWeb platform centralizes flight data management across all platforms
- Converts binary logs to NetCDF format
- Provides analytics/visualization for fleet operations
- Critical dependency for flight testing and mission analysis

### 5. **Active Integration Projects**
- **eMASS partnership** (#emass, #emass-bst): AI hardware integration on E2 for efficiency improvement
- **By Light Mustang** (#by-lite-mustang): USAF contract with phased development approach
- **Navy boundary layer/magnetometer projects**: Sensor payload integration on S0

### 6. **Recurring Decision Patterns**
1. **Technical decisions**: Jack Elston + domain expert (Joshua Fromm for hardware, Maciej for flight ops)
2. **Funding decisions**: Jack Elston drives strategy; proposals coordinated through #grants-and-funding
3. **Flight operations**: Maciej coordinates; issues escalated to Jack Elston
4. **Procurement/logistics**: Joshua Fromm + Meredith Needham in #operations

### 7. **Channel Ecosystem Structure**
- **Strategic**: #general (company-wide), #grants-and-funding (revenue), #operations (execution)
- **Technical Projects**: #sbir-hurricane, #25_1-navy-sbir-magnetometer, #25_1-navy-sttr-boundary-layer, #2025-nasa-autonomy, #s3
- **Customer/Commercial**: #commercial-sales, #by-lite-mustang
- **Infrastructure**: #logparse-website, #flight-testing
- **Partnership**: #emass, #emass-bst
- **Marketing**: #marketing (external communications)

### 8. **Key Connections Across Channels**
- **Flight testing** (#flight-testing) feeds data into **SwiftWeb** (#logparse-website) for all platforms
- **Navy projects** leverage **S0 platform** developed in **#sbir-hurricane**
- **S3 VTOL** development (#s3) informs STTR boundary layer project (#25_1-navy-sttr-boundary-layer)
- **NASA autonomy** (#2025-nasa-autonomy) shares control architecture work with **flight testing** validation
- **eMASS integration** impacts **E2 platform** performance tracked in **#flight-testing**

### 9. **Project Timeline Overview**
- **Long-running**: SBIR Hurricane (2020-2026), S3 VTOL development
- **Current focus**: Navy STTR boundary layer, NASA autonomy Phase I (2025-2026), By Light Mustang USAF contract
- **Recent launches**: 2025 Navy magnetometer SBIR, eMASS integration with E2

### 10. **Organizational Strengths**
- Centralized decision-making (Jack Elston) with clear technical owners
- Strong integration across hardware, firmware, and operations
- Government contracting expertise with active funding pipeline
- Diverse platform portfolio supporting multiple mission types