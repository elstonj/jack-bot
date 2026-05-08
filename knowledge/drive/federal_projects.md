# Federal Projects — Shared Drive

## Overview
- **Total files:** 9 | **Folders:** 0
- **Date range:** 2022-02-07 (created) → 2099-01-24 (modified)
- **Primary purpose:** Storage of federal grant proposals, RFIs, reports, budgets, and related correspondence for NASA, DOE, NOAA, and DoD opportunities. Includes budget tracking, proposal development materials, and flight test documentation.

## Folder Structure
- **Root level only:** 9 files (no subdirectories in current snapshot)
  - **Note:** Previous structure included `/Data/` folder with 8 NetCDF flight test files. These are not present in current raw data; verify if archived, moved, or pruned.

## Key Documents by Category

### Proposals & RFPs (1 file)
| Document | Path | Last Modified | Editor |
|-----------|------|---------------|--------|
| Autonomy Phase II-proposal-DRAFT | /Autonomy Phase II-proposal-DRAFT | 2026-05-07 | Beck Cotter |

### Financial (3 files)
| Document | Path | Last Modified | Editor |
|-----------|------|---------------|--------|
| NASA A2.02 Autonomy Phase II budget | /NASA A2.02 Autonomy Phase II budget | 2026-05-07 | Beck Cotter |
| PrecisionTerra budget .xlsx | /PrecisionTerra budget .xlsx | 2026-05-07 | Beck Cotter |
| Budget Justification | /Budget Justification | 2026-05-07 | Beck Cotter |

### Documents & Drafts (2 files)
| Document | Path | Last Modified | Editor |
|-----------|------|---------------|--------|
| NASA AERO.7 Phase I | /NASA AERO.7 Phase I | 2026-05-07 | Beck Cotter |
| Capital Commitments KS draft | /Capital Commitments KS draft | 2026-05-07 | Beck Cotter |

### Other (3 files)
| Document | Path | Last Modified | Editor |
|-----------|------|---------------|--------|
| Phase 2 Sections for BST.docx | /Phase 2 Sections for BST.docx | 2026-05-07 | Beck Cotter |
| RC_VID_0009.MOV | /RC_VID_0009.MOV | 2099-01-24 | Jack Elston |
| RC_VID_0008.MOV | /RC_VID_0008.MOV | 2099-01-24 | Jack Elston |

**Note:** Video files retain anomalous 2099-01-24 timestamp (metadata error).

## Recent Activity Patterns
- **Most active editor:** Beck Cotter (7 files, 78% of activity) — owns proposal drafting, budget development, and phase planning; significantly increased focus on financials
- **Secondary contributor:** Jack Elston (2 files) — video media ownership; unchanged from prior cycle
- **Activity concentration:** All substantive document edits clustered on **2026-05-07** (one day after prior cycle's 2026-05-06), suggesting continued proposal finalization and budget refinement sprint
- **Notable shift:** 
  - **Flight test `/Data/` folder has been removed** from root-level view; 8 NetCDF files and associated directory no longer appear in current snapshot. **Action required:** Determine if moved to separate archive, reassigned to another drive, or intentionally pruned.
  - **New financial focus:** Introduction of three budget files (NASA A2.02, PrecisionTerra, Justification) indicates **cost proposal development phase**; suggests NASA Autonomy Phase II proposal approaching submission deadline
  - **New program entry:** "NASA AERO.7 Phase I" document indicates potential parallel opportunity or early-phase portfolio expansion beyond existing Autonomy track

## Client/Project Document Mapping

### NASA Autonomy Program (Phase II SBIR/STTR)
- **Autonomy Phase II-proposal-DRAFT** — active proposal in development (updated 2026-05-07)
- **Phase 2 Sections for BST.docx** — modular proposal sections (updated 2026-05-07)
- **NASA A2.02 Autonomy Phase II budget** — Phase II cost proposal and budget spreadsheet
- **Budget Justification** — narrative justification for Phase II budget line items
- **Flight test data** — *previously located in `/Data/` folder; currently missing from drive snapshot; verify archival status*

### NASA AERO.7 Program (Phase I - New or Emerging)
- **NASA AERO.7 Phase I** — Phase I proposal or planning document (newly visible, updated 2026-05-07)
- **Capital Commitments KS draft** — may relate to facilities/infrastructure commitments for AERO.7 or other programs

### PrecisionTerra (Subcontractor/Partner)
- **PrecisionTerra budget .xlsx** — budget allocation or cost share for subcontractor involvement
- **Phase 2 Sections for BST.docx** — noted in prior cycle as containing Precision Terra contributor input; continues to reflect multi-party proposal development

### AFRL/DOE/NOAA Programs
- No active documents currently visible; verify if proposals under development in other drives or archived

### Flight Test Campaign (Status TBD)
- **RC_VID_0008.MOV, RC_VID_0009.MOV** — video documentation of autonomous platform testing
- **Associated flight test data** — previously stored in `/Data/` (8 NetCDF files from April 7–9, 2026); **current location unknown**

## Important Templates & Shared Resources

### Budget Development
- **NASA A2.02 Autonomy Phase II budget** — standardized budget spreadsheet for NASA SBIR Phase II submissions; likely reusable template for future federal proposals
- **Budget Justification** — narrative template supporting cost proposals

### Proposal Sections
- **Phase 2 Sections for BST.docx** — modular proposal sections enabling rapid assembly and multi-author collaboration across BST and subcontractor teams

### Financial Planning
- **PrecisionTerra budget .xlsx** — subcontractor/partner cost allocation template

## Outstanding Issues & Recommendations

### **CRITICAL: Data Archival/Loss**
1. **Flight test `/Data/` folder has disappeared** from current drive snapshot. The prior knowledge file documented 8 NetCDF files (D20260407_*.nc, D20260409_*.nc) as critical validation data for Phase II proposal claims.
   - **Action:** Immediately verify whether:
     - Data was moved to a separate "Flight Data" or "Testing" drive
     - Data was archived in Google Vault or organizational archive
     - Data was deleted intentionally (if so, document justification)
     - Sync/export error in raw data pull
   - **Impact:** If lost, re-obtain from Joshua Wadler (prior editor) or regenerate from source platforms

2. **Video timestamp errors persist:** RC_VID_0008/0009.MOV retain anomalous 2099-01-24 metadata. Confirm:
   - Actual date/time of recording (likely April 2026 to align with flight test data)
   - Relationship to flight test campaign
   - Whether videos should be co-located with flight data or retained at root level

### **Portfolio & Program Expansion**
3. **NASA AERO.7 Phase I emergence:** New program document indicates proposal pipeline expansion. Clarify:
   - Is AERO.7 in preparation for Phase I submission, or Phase I active with Phase II planning underway?
   - Resource allocation between Autonomy Phase II (active) and AERO.7 (new)?
   - Budget relationship between programs (overlap, separate budgets, shared infrastructure)?

4. **Capital Commitments KS draft:** Unclear whether this relates to facilities for AERO.7, Autonomy Phase II, or shared infrastructure. Recommend:
   - Add explicit program tag to filename (e.g., "Capital Commitments KS draft - AERO.7")
   - Clarify scope (land, facilities, equipment, personnel commitments)

### **Organization & Documentation**
5. **Root-level flatness increases clutter:** As proposal portfolio grows (Autonomy Phase II + AERO.7 + subcontractor budgets), recommend immediate restructuring:
   ```
   /NASA_Autonomy_Phase2/
     - Autonomy Phase II-proposal-DRAFT
     - Phase 2 Sections for BST.docx
     - NASA A2.02 Autonomy Phase II budget
     - Budget Justification
     - [Flight test data - pending recovery]
   
   /NASA_AERO7_Phase1/
     - NASA AERO.7 Phase I
     - Capital Commitments KS draft
   
   /Subcontractors/
     - PrecisionTerra budget .xlsx
   
   /Media/
     - RC_VID_0008.MOV
     - RC_VID_0009.MOV
   
   /Archive/
     - [Prior cycle documents, RFIs, closed proposals]
   ```

6. **Missing documentation from prior cycle:** Previous knowledge file referenced:
   - Progress_Report_Template_2-1-24
   - Phase_I_Final_Report_Instructions_CLIN0007
   - Planning doc
   
   These are no longer visible in raw data. If intentionally archived, document location. If deleted, confirm they are not needed for active proposals.

7. **Beck Cotter workload concentration:** 7 of 9 files last edited by Beck Cotter (78%) indicates single point of failure for proposal management. Recommend:
   - Cross-train Daniel Prendergast or other team member on proposal drafting
   - Establish peer review process for budget documents before submission
   - Document proposal timeline and milestone ownership

### **Data Governance**
8. **Flight test data repatriation:** Joshua Wadler (prior primary editor of `/Data/` files) should be contacted to:
   - Confirm data archival location
   - Provide data dictionary/README for NetCDF files
   - Clarify data retention requirements for Phase II proposal validation and reporting
   - Establish permanent home for test data (consider dedicated "Flight Testing" drive if expanding UAS operations)

### **Upcoming Deadlines (Inferred)**
- **NASA Autonomy Phase II proposal:** Active draft with budget finalization (2026-05-07 edits suggest imminent submission)
- **NASA AERO.7 Phase I:** Early-stage planning; capital commitments draft suggests facility/infrastructure decisions needed

---

## Summary of Changes from Prior Knowledge File
| Item | Prior State | Current State | Interpretation |
|------|-------------|---------------|-----------------|
| Total files | 15 | 9 | Net loss of 6 files (primarily flight test data) |
| Folder structure | Root + `/Data/` subdirectory | Root level only | Data folder removed; archival status unknown |
| Flight test data | 8 NetCDF files, complete | Missing | **Critical action required** |
| Financial documents | 0 | 3 (budgets + justification) | Proposal entering cost phase |
| Program count | 1 (Autonomy Phase II) | 2 (+ AERO.7) | Portfolio expansion |
| Most active editor | Joshua Wadler (flight data) | Beck Cotter (proposals/budgets) | Shift from testing to proposal finalization phase |