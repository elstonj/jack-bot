# 2021-02-13 BluFlux BST Agreement Update for SOW2 Change Order and SOW3

## Document Metadata
- **Type:** Subcontract Agreement Amendment / Statement of Work Update
- **Client/Agency:** BluFlux, LLC (Prime Contractor)
- **Related Agreement:** Subcontract Services Agreement between Black Swift Technologies LLC and BluFlux, LLC, dated December 2, 2020
- **Date:** February 13, 2021 (created/modified February 25, 2021)
- **BST Personnel Named:** Maciej Stachura (CTO, designated as BST Project Manager)
- **Document Classification:** Change order to SOW#2 and new SOW#3

## Executive Summary
This document amends the existing BluFlux subcontract agreement by introducing a change order to SOW#2 (extending the deadline to March 12, 2021 and adding cellular-based remote control capabilities) and establishing SOW#3, which focuses on detailed data logging and telemetry collection with specified formats and deliverable schedules through April 2021.

## Statement of Work #2 Change Order #1

### Additional Objectives
1. Implement iPerf Server throughput results logging
2. Implement remote start/stop of testbed client datalogging and iPerf functions via cellular links:
   - Between test operator and MQTT server
   - Between DCA PoC Testbed client and MQTT server
3. Enable external team members (from entities other than Black Swift) to compile firmware and use project software, servers, and conduct datalogging and throughput tests

### Schedule Change
- **Original deadline:** December 24, 2020
- **Revised deadline:** Week ending March 12, 2021 (or week ending March 19, 2021 if weather delays required)
- **Includes:** Flight Testing Round 2 and all associated deliverables

### Role Change
- Maciej Stachura (BST CTO) designated as BST Project Manager for this work

### Deliverables, Required Results & Pricing (SOW#2 CO1)

**Deliverable CO1.D1 & CO1.D2:**
- Due: Friday, February 26, 2021
- Invoicing upon Prime Contractor acceptance
- 10 working days for Prime approval/revision requests

**Deliverable CO1.D3:**
- Due: Upon completion of all SOW#2 deliverables
- Invoicing upon completion of all SOW#2 deliverables
- 3 working days for Prime approval/revision requests

## Statement of Work #3

### Deliverables 1-7 Overview
Seven deliverables specified with detailed logging and data collection requirements (specific deliverable descriptions not fully detailed in document excerpt).

### Required Results for Logs and Logfiles

**CSV Logfile Format:**
Timestamped data with GMT to nearest microsecond, format: YYYY-MM-DD HH:MM:SS.uuuuuu

**Parameters per timestamped row:**
- Date and Time (YYYY-MM-DD HH:MM:SS.uuuuuu)
- Latitude (degrees)
- Longitude (degrees)
- Accuracy (meters)
- Latency (milliseconds)
- Tx power (dBm)
- SINR (dB)
- iPerf Throughput (bps)
- Throughput Direction (UPLOAD or DOWNLOAD)

**Per Serving or Neighbor Cell PCI:**
- NeighborNumber (sequential, 0 = serving cell)
- PCI n (Physical Cell Identity number)
- RSRP n (Reference Signal Received Power in dBm)
- RSRQ n (Reference Signal Received Quality in dB)
- EARFCN n (E-UTRA Absolute Radio Frequency Channel Number, integer)

**Additional Log Types:**
- Server log of received OK beacon signals (example file format TBD)
- iPerf server log (example file format TBD)

### Budget Allocations for SOW#3

**Hours Budget for Technical Support & Meeting Attendance:**
- 40 hours at $174/hour = up to $6,960.00
- For software technical support, testing support, and meeting attendance
- Applies after SOW#2 completion
- Requested by BluFlux Project Manager or at BST Project Manager's request

**Reimbursable Materials & Equipment Rental Budget:**
- $3,000 allocated for:
  - Landing gear parts
  - Payload mount parts
  - GPS and other needed parts
  - Equipment rental for battery charging (as needed)
- Items over $200 require prior Prime Contractor approval

### Invoicing Procedures (SOW#3)

**For Deliverables 1-7:**
- Subcontractor submits upon Prime acceptance
- Prime has 10 working days to approve or request revisions

**For Hours Budget:**
- Weekly accounting of hours used/remaining
- Monthly invoices with line items and activity descriptions submitted end-of-month

**For Materials & Equipment:**
- Monthly invoices with receipts attached, submitted end-of-month

### Schedule (SOW#3)

| Deliverable | Primary Deadline | Backup Deadline (Weather Delays) |
|------------|-----------------|--------------------------------|
| Deliverable 1 | March 12, 2021 | — |
| Deliverable 2 | March 25, 2021 | April 2, 2021 |
| Deliverable 3 | April 9, 2021 | April 16, 2021 |

## Technical Context
- **System Referenced:** DCA PoC Testbed (Development/Proof of Concept testbed)
- **Key Technologies:** MQTT server, cellular connectivity, iPerf throughput testing, LTE/4G metrics (RSRP, RSRQ, SINR, EARFCN, PCI)
- **Primary Focus:** Wireless/cellular performance characterization with detailed telemetry logging

## Notable Details
- Emphasizes remote operability via cellular links (no direct physical access required for test control)
- Requires external stakeholder capability to compile and operate firmware independently of BST
- Detailed microsecond-precision GPS and cellular signal quality metrics indicate scientific/research-grade data collection
- Weather contingency windows built into spring 2021 schedule suggests field testing operations
- Multiple file format examples pending from BluFlux (suggests iterative data format refinement)