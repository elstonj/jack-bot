# WAWF Invoice and Receiving Report COMBO 101 Training Guide

## Document Metadata
- Type: Web-based training / instructional guide
- Client/Agency: DoD (Department of Defense) / PIEE (Procurement Integrated Enterprise Environment)
- Program/Solicitation: Navy SBIR - Magnetometer Phase I Contract
- Date: 2023
- BST Products/Systems Referenced: None
- Key Personnel: Meredith Needham (last editor)

## Executive Summary
This is a DoD training document explaining how vendors (including Black Swift Technologies) submit invoices and receiving reports through the WAWF (Wide Area Workflow) system. It provides step-by-step instructions for creating a combined Invoice and Receiving Report (COMBO) document for government contracts, focusing on required data entry, CAGE codes, contract information, line items, and submission procedures.

## Technical Approach
The document outlines a web-based workflow process for vendors to:
1. Register for WAWF vendor role access through PIEE
2. Select CAGE code and contract/delivery order numbers from dropdown menus
3. Enter Pay Official DoDAAC (Defense Logistics Agency Activity Address Code)
4. Select currency and document type (Invoice and Receiving Report COMBO)
5. Populate routing information (Issue By DoDAAC, Admin By, Ship To addresses)
6. Complete header tab with shipment details, invoice information, and transportation data
7. Enter line items with quantities shipped and required product/service data
8. Review via Preview CI (Commercial Invoice) and Preview RR (Receiving Report) tabs
9. Submit with system validation and error correction as needed

## Key Requirements & Fields

**Header Tab Fields:**
- Supplies/Services designation
- Shipment Number and Date
- Final Shipment designation (Yes/No)
- Invoice Number and Date
- Final Invoice designation (Yes/No)
- Transportation data (conditional)

**Required Contract Locations by Form Type:**
- DD1155, SF1449, SF26, SF33 forms have different block locations for CAGE, Contract Number, Delivery Order, Pay Official

**Line Item Tab:**
- Quantity shipped (required, must be entered manually)
- Product/Service IDs and Qualifiers
- UID, MILSTRIP, Batch/Lot & Shelf Data (conditional)
- Document supports up to 999 line items (multiple documents required if exceeded)

## Routing & Address Information
The document emphasizes that routing information (Issue By DoDAAC, Admin By, Ship To) should:
- Prepopulate from EDA (Electronic Data Access) when possible
- Be manually entered if not prepopulated
- Match contract specifications exactly
- Ship To address must be identical for all items on a single WAWF document

## Error Handling & Validation
- System displays ERROR (must be corrected), WARNING (review carefully), and INFO messages
- Errors identified by tab, field, or section
- Document must pass validation before submission
- Preview tabs allow full data review before final submission

## Notable Details
- **Critical Note:** Correct Pay Office identification is essential for payment success; errors may result in rejection or delays
- Vendors must have active PIEE account with "Vendor" role before accessing WAWF
- Contract data should be reviewed before beginning document creation
- Reference Procurement Identifier fields auto-populate when applicable (most contracts do not have one)
- Success confirmation and email notifications sent after submission
- Additional detailed training available at: https://pieetraining.eb.mil/wbt/xhtml/wbt/wawf/roles/VendorIndex.xhtml

## Context Notes
This is an administrative/procedural document, not a technical proposal or capability brief. It serves as instructional material for BST personnel managing invoicing and receiving reports for the Navy SBIR Magnetometer Phase I contract. The document itself contains no BST-specific technical content or capabilities.