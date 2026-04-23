"""Per-class QuickBooks data export for Jack Bot's project-state layer.

Reuses the existing `quickbooks_scanner.py` fetch functions but emits one JSON
file per project class at `knowledge/quickbooks/by_class/{code}.json` — the
per-project granularity that the existing scanner throws away when it rolls up
into 4 broad buckets (government/commercial/bst_internal/unclassified).

This is phase 1 of the project-state work. The existing scanner keeps producing
its current output untouched; `scanners/project_state_scanner.py` will consume
THESE per-class JSONs (not the markdown rollups) to populate budget.spent.

Output shape (per project):
    {
      "project_code": "350-4",
      "qbo_class_names": ["[350-4] 2024 USGS - Chile (Mexico)"],
      "period": {"start": "2024-04-21", "end": "2026-04-21"},
      "totals": {
        "revenue": 87000.0,
        "expenses": 42310.5,
        "by_category": {"Subcontractors": 12500, "Travel": 4210, ...}
      },
      "invoices":  [ {date, doc_number, customer, total, balance, memo, lines:[...]} ],
      "bills":     [ ... ],
      "purchases": [ ... ],
      "purchase_orders": [ ... ],
      "payments":  [ ... ]
    }

Unmatched-class transactions go into `_unclassified.json`. The summary across
all classes is written to `_index.json`.
"""

from __future__ import annotations

import json
import re
import time
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

from project_state import load_categories, code_to_filename
from .base import KNOWLEDGE_DIR, get_last_scan, update_scan_timestamp
from .quickbooks_scanner import (
    _get_qbo_config,
    _refresh_access_token,
    _qbo_query,
    _fetch_classes,
    _get_class_from_line,
)


PAGE_SIZE = 1000  # QBO hard cap per request
REQUEST_DELAY = 0.3


def _fetch_paginated(access_token, realm_id, entity: str, start_date: str | None) -> list[dict]:
    """Paginate through a QBO entity (Invoice/Bill/Purchase/etc.) using STARTPOSITION.

    The existing scanner's fetchers cap at MAXRESULTS 1000 with no pagination;
    BST has >1000 purchases per year, so we must paginate here. STARTPOSITION
    is 1-indexed per QBO docs.
    """
    out: list[dict] = []
    position = 1
    while True:
        where = f" WHERE TxnDate >= '{start_date}'" if start_date else ""
        query = (
            f"SELECT * FROM {entity}{where} "
            f"ORDERBY TxnDate DESC "
            f"STARTPOSITION {position} MAXRESULTS {PAGE_SIZE}"
        )
        data = _qbo_query(access_token, realm_id, query)
        batch = data.get(entity, [])
        if not batch:
            break
        out.extend(batch)
        if len(batch) < PAGE_SIZE:
            break
        position += PAGE_SIZE
        time.sleep(REQUEST_DELAY)
    return out


QBO_BY_CLASS_DIR = KNOWLEDGE_DIR / "quickbooks" / "by_class"


# Project codes show up in QBO CustomerRef / ClassRef labels in several forms:
#   [300-3] 2026 IDIQ
#   (001-1) IRAD- General
#   [300] NOAA:[300-3] 2026 IDIQ   ← use the more specific (rightmost) match
# The "XXX-Y" body uses either dash or underscore and the right-hand digit(s)
# may or may not have a leading zero. We canonicalize to `XXX-N` (no leading
# zero, dash) for comparison against categories.md.
# Intentionally permissive on delimiters — BST has at least one typo'd
# sub-customer (`{451-1]` instead of `[451-1]`), and legitimate labels mix
# `(` and `[`. Match anywhere the code is not embedded in other digits.
_CODE_PATTERN = re.compile(r"(?<!\d)(\d{3})[-_](\d{1,2})(?!\d)")


def _canonicalize_code(code: str) -> str:
    """`001-01` / `001_1` / `[001-7]` → `001-1`."""
    s = code.strip().strip("[]()")
    m = re.match(r"^(\d{3})[-_](\d+)$", s)
    if not m:
        return s
    return f"{m.group(1)}-{int(m.group(2))}"


def _find_project_code(label: str) -> str | None:
    """Return the most-specific canonical project code found in a QBO label.

    Takes the LAST match so that `[300] NOAA:[300-3] 2026 IDIQ` resolves to
    `300-3`, not `300`.
    """
    if not label:
        return None
    matches = list(_CODE_PATTERN.finditer(label))
    if not matches:
        return None
    m = matches[-1]
    return _canonicalize_code(f"{m.group(1)}-{m.group(2)}")


def _qbo_label_to_project_code(
    label: str, canonical_codes: set[str]
) -> str | None:
    """Match a QBO CustomerRef/ClassRef label to a canonical code.

    Returns the canonical code if recognized, else None.
    """
    code = _find_project_code(label)
    if code and code in canonical_codes:
        return code
    return None


def _line_amount(line: dict) -> float:
    val = line.get("Amount", 0) or 0
    try:
        return float(val)
    except (TypeError, ValueError):
        return 0.0


def _line_account_name(line: dict) -> str:
    for detail_key in (
        "AccountBasedExpenseLineDetail",
        "ItemBasedExpenseLineDetail",
        "SalesItemLineDetail",
    ):
        detail = line.get(detail_key) or {}
        acct_ref = detail.get("AccountRef")
        if acct_ref:
            return acct_ref.get("name", "") or ""
    return ""


def _format_txn(txn: dict, txn_type: str, attributed_amount: float | None = None) -> dict:
    """Flatten a QBO transaction into a JSON-serializable dict.

    `attributed_amount` is the portion of this transaction attributed to the
    current class when line-level class assignments split across classes. If
    None, falls back to TotalAmt.
    """
    total = float(txn.get("TotalAmt", 0) or 0)
    if attributed_amount is None:
        attributed_amount = total

    lines = txn.get("Line", []) or []
    flat_lines = []
    for line in lines:
        flat_lines.append(
            {
                "amount": _line_amount(line),
                "account": _line_account_name(line),
                "description": (line.get("Description") or "")[:300],
            }
        )

    vendor = (txn.get("VendorRef") or {}).get("name", "")
    customer = (txn.get("CustomerRef") or {}).get("name", "")

    return {
        "type": txn_type,
        "date": txn.get("TxnDate", ""),
        "doc_number": txn.get("DocNumber", ""),
        "total": total,
        "attributed": attributed_amount,
        "vendor": vendor,
        "customer": customer,
        "balance": (
            float(txn["Balance"]) if txn.get("Balance") not in (None, "") else None
        ),
        "memo": (txn.get("PrivateNote") or txn.get("Memo") or "")[:400],
        "lines": flat_lines[:20],
    }


def _line_customer_ref(line: dict) -> dict:
    """Extract CustomerRef from a line item (various detail shapes)."""
    for detail_key in (
        "AccountBasedExpenseLineDetail",
        "ItemBasedExpenseLineDetail",
        "SalesItemLineDetail",
    ):
        detail = line.get(detail_key) or {}
        ref = detail.get("CustomerRef")
        if ref:
            return ref
    return line.get("CustomerRef") or {}


def _attribute_txn_to_projects(
    txn: dict, canonical_codes: set[str]
) -> dict[str | None, float]:
    """Split a transaction's total across project codes.

    BST's QBO tags projects via **sub-customer** CustomerRef on line items
    (names like `[300-3] 2026 IDIQ` or `(001-1) IRAD- General`), NOT Classes
    (which are just Government/Commercial/BST Internal — too broad).

    Strategy:
      1. Prefer line-level CustomerRef — each line's amount attributed there.
      2. Fall back to transaction-level CustomerRef for lines with no ref.
      3. Fall back to transaction-level ClassRef → `_unclassified` (since
         Government/Commercial/BST Internal aren't project-level).
      4. Any lines/amounts we can't place go to None (unclassified).

    Returns {code_or_None: dollar_amount}.
    """
    total = float(txn.get("TotalAmt", 0) or 0)
    lines = txn.get("Line", []) or []
    txn_customer = txn.get("CustomerRef") or {}
    txn_customer_code = _qbo_label_to_project_code(
        txn_customer.get("name", ""), canonical_codes
    )

    out: dict[str | None, float] = defaultdict(float)
    placed = 0.0
    for line in lines:
        amount = _line_amount(line)
        if amount == 0:
            continue
        line_customer = _line_customer_ref(line)
        code = _qbo_label_to_project_code(
            line_customer.get("name", ""), canonical_codes
        )
        if code is None:
            code = txn_customer_code  # fall back to txn-level
        out[code] += amount
        placed += amount

    # Anything left over (e.g. tax lines without detail blocks) goes to the
    # txn-level customer if known, else unclassified.
    leftover = total - placed
    if abs(leftover) > 0.01:
        out[txn_customer_code] += leftover

    return dict(out)


def _categorize_line_amount(lines: list[dict]) -> dict[str, float]:
    """Aggregate line amounts by account name (cost category)."""
    out: dict[str, float] = defaultdict(float)
    for line in lines:
        acct = _line_account_name(line) or "Uncategorized"
        out[acct] += _line_amount(line)
    return dict(out)


def _ensure_bucket(buckets: dict, code: str | None) -> dict:
    key = code if code else "_unclassified"
    if key not in buckets:
        buckets[key] = {
            "project_code": code or "_unclassified",
            "qbo_class_names": set(),
            "totals": {
                "revenue": 0.0,
                "expenses": 0.0,
                "by_category": defaultdict(float),
            },
            "invoices": [],
            "bills": [],
            "purchases": [],
            "purchase_orders": [],
            "payments": [],
        }
    return buckets[key]


_TXN_TYPE_OUT_KEY = {
    "Invoice": "invoices",
    "Bill": "bills",
    "Purchase": "purchases",
    "PurchaseOrder": "purchase_orders",
    "Payment": "payments",
}

_REVENUE_TYPES = {"Invoice", "Payment"}


def _process_transactions(
    txns: list[dict],
    txn_type: str,
    canonical_codes: set[str],
    buckets: dict,
) -> None:
    out_key = _TXN_TYPE_OUT_KEY[txn_type]
    for txn in txns:
        attribution = _attribute_txn_to_projects(txn, canonical_codes)
        for code, attributed in attribution.items():
            if attributed == 0:
                continue
            bucket = _ensure_bucket(buckets, code)

            # Record source labels that actually resolved to THIS bucket's
            # project code — don't pollute with other lines' customers.
            for line in txn.get("Line", []) or []:
                cust_name = (_line_customer_ref(line).get("name")) or ""
                if _qbo_label_to_project_code(cust_name, canonical_codes) == code:
                    bucket["qbo_class_names"].add(cust_name)
            txn_cust_name = (txn.get("CustomerRef") or {}).get("name") or ""
            if txn_cust_name and _qbo_label_to_project_code(
                txn_cust_name, canonical_codes
            ) == code:
                bucket["qbo_class_names"].add(txn_cust_name)

            bucket[out_key].append(_format_txn(txn, txn_type, attributed))

            if txn_type in _REVENUE_TYPES:
                bucket["totals"]["revenue"] += attributed
            else:
                bucket["totals"]["expenses"] += attributed

            # Category breakdown (expenses only — revenue categorization is noise)
            if txn_type not in _REVENUE_TYPES:
                category_sums = _categorize_line_amount(txn.get("Line", []) or [])
                total = float(txn.get("TotalAmt", 0) or 0) or 1.0
                share = attributed / total
                for cat, amt in category_sums.items():
                    bucket["totals"]["by_category"][cat] += amt * share


def _serialize_bucket(bucket: dict, period: dict) -> dict:
    return {
        "project_code": bucket["project_code"],
        "qbo_class_names": sorted(bucket["qbo_class_names"]),
        "period": period,
        "totals": {
            "revenue": round(bucket["totals"]["revenue"], 2),
            "expenses": round(bucket["totals"]["expenses"], 2),
            "by_category": {
                k: round(v, 2)
                for k, v in sorted(
                    bucket["totals"]["by_category"].items(),
                    key=lambda kv: -kv[1],
                )
            },
        },
        "invoices": bucket["invoices"],
        "bills": bucket["bills"],
        "purchases": bucket["purchases"],
        "purchase_orders": bucket["purchase_orders"],
        "payments": bucket["payments"],
    }


def scan_all(mode: str = "full") -> list[Path]:
    """Fetch QBO transactions and write per-class JSON files.

    Returns list of output paths.
    """
    config = _get_qbo_config()
    realm_id = config["QUICKBOOKS_REALM_ID"]

    print("Authenticating with QuickBooks Online...")
    access_token = _refresh_access_token(config)

    # Always pull ≥2 years for budget math; the project_state scanner will
    # snapshot current cumulative, but historical detail helps burn-rate calc.
    if mode == "1yr":
        start_date = (date.today() - timedelta(days=365)).isoformat()
    elif mode == "incremental":
        last = get_last_scan("qbo_by_class")
        start_date = last.strftime("%Y-%m-%d") if last else (
            date.today() - timedelta(days=730)
        ).isoformat()
    else:
        start_date = (date.today() - timedelta(days=730)).isoformat()

    end_date = date.today().isoformat()
    period = {"start": start_date, "end": end_date}
    print(f"Period: {start_date} → {end_date}")

    # Canonical project codes from categories.md, canonicalized to the form
    # QBO uses (no leading zero on second component: `001-01` → `001-1`).
    canonical_codes: set[str] = set()
    for code, _, _ in load_categories():
        stripped = code.strip("[]")
        if re.match(r"^\d{3}[-_]\d+$", stripped):
            canonical_codes.add(_canonicalize_code(stripped))
    print(f"Canonical project codes: {len(canonical_codes)}")

    # Fetch classes (just for logging — attribution happens via CustomerRef)
    classes = _fetch_classes(access_token, realm_id)
    print(f"QBO classes: {len(classes)} (broad buckets; actual project codes live in CustomerRef)")

    # Fetch every transaction type (paginated — BST can have >1000 purchases/yr)
    print("Fetching invoices...")
    invoices = _fetch_paginated(access_token, realm_id, "Invoice", start_date)
    print(f"  {len(invoices)}")
    print("Fetching bills...")
    bills = _fetch_paginated(access_token, realm_id, "Bill", start_date)
    print(f"  {len(bills)}")
    print("Fetching purchases...")
    purchases = _fetch_paginated(access_token, realm_id, "Purchase", start_date)
    print(f"  {len(purchases)}")
    print("Fetching purchase orders...")
    pos = _fetch_paginated(access_token, realm_id, "PurchaseOrder", start_date)
    print(f"  {len(pos)}")
    print("Fetching payments...")
    payments = _fetch_paginated(access_token, realm_id, "Payment", start_date)
    print(f"  {len(payments)}")

    # Attribute everything
    buckets: dict = {}
    _process_transactions(invoices, "Invoice", canonical_codes, buckets)
    _process_transactions(bills, "Bill", canonical_codes, buckets)
    _process_transactions(purchases, "Purchase", canonical_codes, buckets)
    _process_transactions(pos, "PurchaseOrder", canonical_codes, buckets)
    _process_transactions(payments, "Payment", canonical_codes, buckets)

    # Write per-class JSON
    QBO_BY_CLASS_DIR.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    index_entries = []
    for key, bucket in buckets.items():
        filename = code_to_filename(key) if key != "_unclassified" else "_unclassified"
        path = QBO_BY_CLASS_DIR / f"{filename}.json"
        serialized = _serialize_bucket(bucket, period)
        path.write_text(json.dumps(serialized, indent=2))
        written.append(path)
        index_entries.append(
            {
                "project_code": serialized["project_code"],
                "revenue": serialized["totals"]["revenue"],
                "expenses": serialized["totals"]["expenses"],
                "invoice_count": len(serialized["invoices"]),
                "bill_count": len(serialized["bills"]),
                "purchase_count": len(serialized["purchases"]),
                "po_count": len(serialized["purchase_orders"]),
                "payment_count": len(serialized["payments"]),
                "qbo_class_names": serialized["qbo_class_names"],
            }
        )

    # Index
    index_path = QBO_BY_CLASS_DIR / "_index.json"
    index_path.write_text(
        json.dumps(
            {
                "period": period,
                "scanned_at": date.today().isoformat(),
                "projects": sorted(index_entries, key=lambda e: e["project_code"]),
            },
            indent=2,
        )
    )
    print(f"Wrote {len(written)} per-class files + _index.json → {QBO_BY_CLASS_DIR}")

    update_scan_timestamp("qbo_by_class")
    return written
