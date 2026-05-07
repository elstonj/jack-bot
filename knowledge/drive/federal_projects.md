# Federal Projects — Shared Drive

## Overview
- **Total files:** 15 | **Folders:** 1
- **Date range:** 2022-02-07 (created) → 2099-01-24 (modified)
- **Primary purpose:** Storage of federal grant proposals, RFIs, reports, and related correspondence for NASA, DOE, NOAA, and DoD opportunities. Includes budget tracking, proposal development materials, and flight test data collection.

## Folder Structure
- **Root level:** 7 files (proposals, templates, presentations, videos)
- **Data/** — 8 files (NetCDF flight test data files, time-stamped from April 2026)

## Key Documents by Category

### Proposals & RFPs (1 file)
| Document | Path | Last Modified | Editor |
|-----------|------|---------------|--------|
| Autonomy Phase II-proposal-DRAFT | /Autonomy Phase II-proposal-DRAFT | 2026-05-06 | Beck Cotter |

### Reports & Analysis (2 files)
| Document | Path | Last Modified | Editor |
|-----------|------|---------------|--------|
| Phase_I_Final_Report_Instructions_CLIN0007 | /Phase_I_Final_Report_Instructions_CLIN0007 | 2026-05-06 | Beck Cotter |
| Progress_Report_Template_2-1-24 | /Progress_Report_Template_2-1-24 | 2026-05-06 | Beck Cotter |

### Documents & Drafts (2 files)
| Document | Path | Last Modified | Editor |
|-----------|------|---------------|--------|
| Phase 2 Sections for BST.docx | /Phase 2 Sections for BST.docx | 2026-05-06 | Daniel Prendergast |
| Planning doc | /Planning doc | 2026-05-06 | Daniel Prendergast |

### Media (2 files)
| Document | Path | Last Modified | Editor |
|-----------|------|---------------|--------|
| RC_VID_0009.MOV | /RC_VID_0009.MOV | 2099-01-24 | Jack Elston |
| RC_VID_0008.MOV | /RC_VID_0008.MOV | 2099-01-24 | Jack Elston |

### Flight Test Data (8 files)
| Document | Path | Last Modified | Editor |
|-----------|------|---------------|--------|
| D20260409_164309QC.nc | /Data/D20260409_164309QC.nc | 2026-05-06 | Joshua Wadler |
| D20260409_164316QC.nc | /Data/D20260409_164316QC.nc | 2026-05-06 | Joshua Wadler |
| D20260409_141143QC.nc | /Data/D20260409_141143QC.nc | 2026-05-06 | Joshua Wadler |
| D20260409_152056QC.nc | /Data/D20260409_152056QC.nc | 2026-05-06 | Joshua Wadler |
| D20260407_181504QC.nc | /Data/D20260407_181504QC.nc | 2026-05-06 | Joshua Wadler |
| D20260407_181445QC.nc | /Data/D20260407_181445QC.nc | 2026-05-06 | Joshua Wadler |
| D20260407_170314QC.nc | /Data/D20260407_170314QC.nc | 2026-05-06 | Joshua Wadler |
| D20260407_170320QC.nc | /Data/D20260407_170320QC.nc | 2026-05-06 | Joshua Wadler |

**Note:** NetCDF files are quality-controlled (.QC) flight test data from autonomous aircraft operations (April 7–9, 2026). Timestamps in filename format YYYYMMDD_HHMMSS indicate multiple test runs per day.

## Recent Activity Patterns
- **Most active editor:** Joshua Wadler (8 files, 100% flight test data) — owns data acquisition and QC pipeline
- **Secondary contributors:**
  - Beck Cotter (3 files) — proposal drafting and report template management; reduced activity from previous cycle
  - Daniel Prendergast (2 files) — Phase 2 proposal sections and planning documentation
  - Jack Elston (2 files, video media with timestamp errors)
- **Activity concentration:** All substantive edits clustered on **2026-05-06** (proposal finalization, template updates, data processing). Video files show persistent metadata error (2099-01-24 timestamp).
- **Notable shift:** Introduction of **flight test data directory** indicates transition from proposal/planning phase to **active platform testing and validation**. Data processing (QC flagging) suggests mission readiness activities supporting Phase II proposal claims.

## Client/Project Document Mapping

### NASA Autonomy Program (Phase II SBIR/STTR)
- **Autonomy Phase II-proposal-DRAFT** — active proposal in development
- **Phase 2 Sections for BST.docx** — section drafts (updated by Daniel Prendergast 2026-05-06; originally from Precision Terra contributor)
- **Planning doc** — associated planning materials
- **Progress_Report_Template_2-1-24** — template for Phase II progress reporting
- **Phase_I_Final_Report_Instructions_CLIN0007** — instructions for Phase I closeout/transition reporting
- **Flight test data (Data/ folder)** — autonomous aircraft platform validation data likely supporting Phase II technical proposal and demonstrating TRL advancement

### AFRL/SBIR Program
- **Phase_I_Final_Report_Instructions_CLIN0007** — may relate to prior AFRL Phase I (AFX22.4) completion and Phase II transition

### Cross-Cutting Federal Programs
- **Master Proposal Tracking** — *not present in this dataset; verify in drive root or archived*
- Documents suggest ongoing NASA Autonomy focus with potential parallel DOE, NOAA, or DoD activities not reflected in current drive snapshot

### Flight Test Campaign (April 2026)
- **Data/** directory contains 8 quality-controlled telemetry files from April 7–9, 2026
- Timestamps suggest 2–4 test flights per day across two days
- **Associated media:** RC_VID_0008/0009.MOV may be video documentation of flight tests (dates to be verified)
- **Purpose:** Platform validation for atmospheric monitoring/autonomy capabilities; likely generates claims and validation data for Phase II proposal

## Important Templates & Shared Resources

### Reporting & Compliance
- **Progress_Report_Template_2-1-24** — standardized template for NASA SBIR Phase II progress reporting; reusable across grant cycles
- **Phase_I_Final_Report_Instructions_CLIN0007** — instruction set for final Phase I closeout; ensures compliance with NASA/AFRL contract requirements

### Proposal Development
- **Phase 2 Sections for BST.docx** — modular Phase II proposal sections; enables rapid proposal adaptation and subcontractor/team collaboration

### Data Management
- **Data/** folder structure with NetCDF QC files — suggests formalized data pipeline (acquisition → quality control → archive) supporting both research and proposal validation

## Outstanding Issues & Recommendations

1. **Video timestamp errors:** RC_VID_0008/0009.MOV retain 2099-01-24 timestamps. Correct metadata and clarify relationship to April 2026 flight tests.

2. **Data organization improvement:** Flight test data in `/Data/` lacks metadata, README, or context documentation. Recommend adding:
   - Data dictionary/README describing NetCDF variable structure
   - Flight log or test plan cross-reference
   - Sensor configuration and calibration notes
   - Data provenance (platform, mission ID, conditions)

3. **Proposal tracking gap:** Previous knowledge file referenced **Master Proposal Tracking** document. Verify current location — if removed, rebuild centralized NASA/DOE/NOAA pipeline tracker to prevent proposal schedule conflicts or overlapping resource demands.

4. **Reduced Beck Cotter activity:** Shift from 6→3 files edited suggests potential delegation or resource reallocation. Confirm proposal management ownership and review timelines for Autonomy Phase II draft maturity.

5. **New investigator:** Joshua Wadler emergence as primary editor (flight data) indicates team expansion or specialized role assignment in data acquisition. Document his responsibilities and access controls.

6. **Archive/cleanup needed:** Verify whether previous 24-file dataset (including RFI documents, budgets, NOAA materials) was intentionally pruned or resides elsewhere in drive. If archived, establish clear versioning and retrieval procedures.

7. **Organizational scaling (continued):** Current 15-file structure remains flat. Recommend implementing proposal-year-based hierarchy:
   - `/FY27/` (NOAA UMS, new RFPs)
   - `/NASA_Autonomy_Phase2/` (active draft, data, templates)
   - `/Data/` → consider sub-folders by test date or mission ID
   - `/Templates/` (consolidate progress reports, final report instructions)
   - `/Archive/` (RFIs, prior proposals, closed projects)