# [001-15] MHP IRAD

## Overview
- **Client/customer:** Internal Research and Development (IRAD) project
- **Dollar value:** Not specified in available data
- **Timeline:** Active 2021–2022; **ARCHIVED** as of late 2022
- **Status:** ARCHIVED — Project complete; 8 technical debt items remain unassigned and unprioritized
- **Team members involved:** Jack Elston (primary developer), Kay (Aeropod integration), Geoff (customer contact)
- **Risk signals:** None — project is archived. 8 open tasks have no due dates and no assignments, indicating they are backlog items not planned for completion.

## Key Deliverables & Milestones
- **Q4 2021:** MHP board setups — 6 boards for Aeropods, 2 boards for L3
- **Q2 2021:** GNSS/IMU orientation and calibration system implementation (complete)
- **Q2 2021:** SDK interface development for sensor configuration (complete)
- **Q2 2021:** Aeropod kit integration, costing, and QuickBooks productization (complete)
- **End 2022:** GPS velocity issue resolution (completed Dec 2022)

## Task Summary
- **Total tasks:** 21 (8 open, 13 completed) — **62% completion rate**
- **Tasks by assignee:**
  - Jack Elston: 9 completed tasks (69% of completed work)
  - Unassigned: 4 completed tasks (business/costing), 8 open tasks (technical backlog)
- **Notable patterns:** 
  - Technical implementation and hardware integration dominated by Jack Elston
  - Business tasks (costing, QuickBooks, customer estimates) completed by unassigned team members (likely Geoff, Kay)
  - No tasks assigned after 2022; all open items are unscheduled technical improvements

## Recent Activity
Last task completed **December 12, 2022** (GPS velocity issue). Most active period: **2021**, with heavy focus on orientation fixes, SDK development, and customer board setups. No activity since late 2022.

## Notes & Context
**MHP = Micro-Hardware Platform** — a sensor integration system combining IMU, GNSS, and pressure sensors with SDK-configurable orientation. Successfully productized with two customer deliveries (Aeropods, L3). 

**Open backlog (8 items, no priority):**
- Sensor data improvements: accelerometer filters, real-time wind measurement, sensor temperatures (IMU/pressure), acceleration units (m/s²)
- Logging enhancements: serial number/code hash, timestamped filenames
- Hardware UX: power switch design (accidental activation risk)

**No timeline or budget assigned to open items** — these represent optional enhancements, not blocking issues.