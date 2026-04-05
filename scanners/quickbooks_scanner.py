"""QuickBooks Online scanner — fetches financial actuals (transactions, invoices,
bills, POs) from QBO API and organizes by project/class.

Produces:
  knowledge/quickbooks/by_project/{class_name}.md  — per-project financials
  knowledge/quickbooks/summary.md                  — company-wide financial overview

QuickBooks uses "Classes" for project tracking. Each class maps to a BST project code.

Required env vars:
  QUICKBOOKS_CLIENT_ID      — OAuth2 app client ID
  QUICKBOOKS_CLIENT_SECRET  — OAuth2 app client secret
  QUICKBOOKS_REFRESH_TOKEN  — OAuth2 refresh token (long-lived)
  QUICKBOOKS_REALM_ID       — Company/realm ID (visible in QBO URL)

Modes:
  full        — all data (current fiscal year + prior year)
  1yr         — last 365 days
  incremental — since last scan
"""

import json
import os
import re
import time
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import requests

from .base import (
    KNOWLEDGE_DIR,
    distill_to_markdown,
    get_last_scan,
    update_scan_timestamp,
    write_knowledge_file,
    get_claude_client,
    DISTILL_MODEL,
)

QBO_KNOWLEDGE_DIR = KNOWLEDGE_DIR / "quickbooks"
QBO_PROJECT_DIR = QBO_KNOWLEDGE_DIR / "by_project"

# QuickBooks Online API endpoints
# Set QUICKBOOKS_SANDBOX=true for sandbox/development companies
QBO_PRODUCTION_BASE = "https://quickbooks.api.intuit.com/v3/company"
QBO_SANDBOX_BASE = "https://sandbox-quickbooks.api.intuit.com/v3/company"
QBO_TOKEN_URL = "https://oauth.platform.intuit.com/oauth2/v1/tokens/bearer"


def _get_qbo_base():
    """Return the correct QBO API base URL (sandbox or production)."""
    if os.environ.get("QUICKBOOKS_SANDBOX", "").lower() in ("true", "1", "yes"):
        return QBO_SANDBOX_BASE
    return QBO_PRODUCTION_BASE

# Rate limiting
REQUEST_DELAY = 0.3  # seconds between API calls

# Token cache file (so we don't refresh every call)
TOKEN_CACHE_FILE = KNOWLEDGE_DIR / ".qbo_token_cache.json"


def _get_qbo_config():
    """Get QuickBooks config from env vars."""
    required = ["QUICKBOOKS_CLIENT_ID", "QUICKBOOKS_CLIENT_SECRET",
                "QUICKBOOKS_REFRESH_TOKEN", "QUICKBOOKS_REALM_ID"]
    config = {}
    for key in required:
        val = os.environ.get(key)
        if not val:
            raise RuntimeError(f"Missing env var: {key}")
        config[key] = val
    return config


def _get_current_refresh_token(config):
    """Get the most current refresh token — from cache if rotated, else from env."""
    if TOKEN_CACHE_FILE.exists():
        try:
            cache = json.loads(TOKEN_CACHE_FILE.read_text())
            cached_refresh = cache.get("refresh_token")
            if cached_refresh:
                return cached_refresh
        except Exception:
            pass
    return config["QUICKBOOKS_REFRESH_TOKEN"]


def _refresh_access_token(config):
    """Exchange refresh token for a new access token.

    QuickBooks access tokens expire after 1 hour. Refresh tokens last 100 days
    and are rotated on each refresh (new refresh token returned).
    """
    # Check cache first — use cached access token if still valid
    if TOKEN_CACHE_FILE.exists():
        try:
            cache = json.loads(TOKEN_CACHE_FILE.read_text())
            expires_at = cache.get("expires_at", 0)
            if time.time() < expires_at - 60:  # 60s buffer
                return cache["access_token"]
        except Exception:
            pass

    # Use the most recent refresh token (may have been rotated)
    refresh_token = _get_current_refresh_token(config)

    resp = requests.post(
        QBO_TOKEN_URL,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": config["QUICKBOOKS_CLIENT_ID"],
            "client_secret": config["QUICKBOOKS_CLIENT_SECRET"],
        },
        timeout=30,
    )
    if resp.status_code != 200:
        print(f"  [ERROR] Token refresh failed ({resp.status_code}): {resp.text[:300]}")
        resp.raise_for_status()

    data = resp.json()
    access_token = data["access_token"]
    new_refresh = data.get("refresh_token", refresh_token)

    # Cache both access token AND refresh token (refresh tokens rotate on each use)
    cache = {
        "access_token": access_token,
        "expires_at": time.time() + data.get("expires_in", 3600),
        "refresh_token": new_refresh,
    }
    TOKEN_CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    TOKEN_CACHE_FILE.write_text(json.dumps(cache))

    if new_refresh != refresh_token:
        print(f"  [NOTE] Refresh token rotated and cached.")

    return access_token


def _qbo_query(access_token, realm_id, query_str):
    """Execute a QBO query and return the response data.

    Uses the QBO Query API which accepts SQL-like queries.
    """
    url = f"{_get_qbo_base()}/{realm_id}/query"
    resp = requests.get(
        url,
        headers={
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json",
        },
        params={"query": query_str},
        timeout=30,
    )
    if resp.status_code != 200:
        print(f"    [ERROR] QBO query failed ({resp.status_code}): {resp.text[:500]}")
        resp.raise_for_status()
    return resp.json().get("QueryResponse", {})


def _qbo_report(access_token, realm_id, report_name, params=None):
    """Fetch a QBO report (P&L, Balance Sheet, etc.)."""
    url = f"{_get_qbo_base()}/{realm_id}/reports/{report_name}"
    resp = requests.get(
        url,
        headers={
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json",
        },
        params=params or {},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def _fetch_classes(access_token, realm_id):
    """Fetch all classes (project codes) from QBO."""
    data = _qbo_query(access_token, realm_id,
                       "SELECT * FROM Class MAXRESULTS 1000")
    return data.get("Class", [])


def _fetch_invoices(access_token, realm_id, start_date=None):
    """Fetch invoices, optionally filtered by date."""
    query = "SELECT * FROM Invoice"
    if start_date:
        query += f" WHERE TxnDate >= '{start_date}'"
    query += " ORDERBY TxnDate DESC MAXRESULTS 1000"
    data = _qbo_query(access_token, realm_id, query)
    time.sleep(REQUEST_DELAY)
    return data.get("Invoice", [])


def _fetch_bills(access_token, realm_id, start_date=None):
    """Fetch bills (vendor invoices / expenses)."""
    query = "SELECT * FROM Bill"
    if start_date:
        query += f" WHERE TxnDate >= '{start_date}'"
    query += " ORDERBY TxnDate DESC MAXRESULTS 1000"
    data = _qbo_query(access_token, realm_id, query)
    time.sleep(REQUEST_DELAY)
    return data.get("Bill", [])


def _fetch_purchases(access_token, realm_id, start_date=None):
    """Fetch purchases (checks, credit card charges, expenses)."""
    query = "SELECT * FROM Purchase"
    if start_date:
        query += f" WHERE TxnDate >= '{start_date}'"
    query += " ORDERBY TxnDate DESC MAXRESULTS 1000"
    data = _qbo_query(access_token, realm_id, query)
    time.sleep(REQUEST_DELAY)
    return data.get("Purchase", [])


def _fetch_purchase_orders(access_token, realm_id, start_date=None):
    """Fetch purchase orders."""
    query = "SELECT * FROM PurchaseOrder"
    if start_date:
        query += f" WHERE TxnDate >= '{start_date}'"
    query += " ORDERBY TxnDate DESC MAXRESULTS 1000"
    data = _qbo_query(access_token, realm_id, query)
    time.sleep(REQUEST_DELAY)
    return data.get("PurchaseOrder", [])


def _fetch_payments(access_token, realm_id, start_date=None):
    """Fetch received payments."""
    query = "SELECT * FROM Payment"
    if start_date:
        query += f" WHERE TxnDate >= '{start_date}'"
    query += " ORDERBY TxnDate DESC MAXRESULTS 1000"
    data = _qbo_query(access_token, realm_id, query)
    time.sleep(REQUEST_DELAY)
    return data.get("Payment", [])


def _get_class_from_line(line_item):
    """Extract class (project) info from a transaction line item."""
    class_ref = line_item.get("ClassRef")
    if class_ref:
        return {"id": class_ref.get("value"), "name": class_ref.get("name", "Unknown")}
    # Check AccountBasedExpenseLineDetail or ItemBasedExpenseLineDetail
    for detail_key in ["AccountBasedExpenseLineDetail", "ItemBasedExpenseLineDetail",
                       "SalesItemLineDetail"]:
        detail = line_item.get(detail_key, {})
        class_ref = detail.get("ClassRef")
        if class_ref:
            return {"id": class_ref.get("value"), "name": class_ref.get("name", "Unknown")}
    return None


def _classify_transactions(transactions, txn_type):
    """Group transactions by class/project.

    Returns dict: class_name -> list of formatted transaction strings.
    """
    by_class = defaultdict(list)

    for txn in transactions:
        txn_date = txn.get("TxnDate", "")
        total = txn.get("TotalAmt", 0)
        doc_number = txn.get("DocNumber", "")
        vendor = (txn.get("VendorRef") or {}).get("name", "")
        customer = (txn.get("CustomerRef") or {}).get("name", "")
        memo = txn.get("PrivateNote", "") or txn.get("Memo", "")
        balance = txn.get("Balance", "")

        # Check for class at transaction level
        txn_class = None
        class_ref = txn.get("ClassRef")
        if class_ref:
            txn_class = class_ref.get("name", "Unknown")

        # Check line items for class assignments and account categories
        line_classes = set()
        lines = txn.get("Line", [])
        line_details = []
        for line in lines:
            lclass = _get_class_from_line(line)
            if lclass:
                line_classes.add(lclass["name"])
            amount = line.get("Amount", 0)
            desc = line.get("Description", "")

            # Extract account name (cost category) from line item details
            account_name = ""
            for detail_key in ["AccountBasedExpenseLineDetail", "ItemBasedExpenseLineDetail",
                               "SalesItemLineDetail"]:
                detail = line.get(detail_key, {})
                acct_ref = detail.get("AccountRef")
                if acct_ref:
                    account_name = acct_ref.get("name", "")
                    break

            if amount:
                parts = [f"    ${amount:,.2f}"]
                if account_name:
                    parts.append(f"[{account_name}]")
                if desc:
                    parts.append(f"— {desc}")
                line_details.append(" ".join(parts))

        # Build transaction summary
        entity = vendor or customer or ""
        summary = f"  {txn_date} | {txn_type}"
        if doc_number:
            summary += f" #{doc_number}"
        summary += f" | ${total:,.2f}"
        if entity:
            summary += f" | {entity}"
        if balance and txn_type == "Invoice":
            summary += f" | Balance: ${float(balance):,.2f}"
        if memo:
            summary += f"\n    Memo: {memo[:200]}"
        if line_details:
            summary += "\n" + "\n".join(line_details[:10])

        # Assign to class(es)
        classes = line_classes or ({txn_class} if txn_class else {"Unclassified"})
        for cls in classes:
            by_class[cls].append(summary)

    return dict(by_class)


def _safe_filename(name):
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'\s+', '_', name.strip())
    return name[:80].lower()


PROJECT_DISTILL_PROMPT = """\
You are distilling QuickBooks financial transaction data for a Black Swift Technologies (BST) \
project into a structured knowledge file. This will be combined with Drive-based budget data \
to answer questions about project financial status.

Output a markdown file:

# {Project/Class Name} — QuickBooks Financials

## Financial Summary
- Total invoiced (revenue)
- Total expenses (bills + purchases)
- Total purchase orders
- Net position
- Date range of transactions

## Revenue (Invoices & Payments)
List invoices with: number, date, amount, customer, balance remaining.
Summarize total invoiced and total collected.

## Expenses by Cost Category
Group ALL expenses (bills + purchases) by their account name / cost category. \
Use the [Account Name] tags on line items to categorize. Standard categories:
- **Direct Labor** (wages, salaries allocated to this project)
- **Subcontractors** (direct cost subcontracting)
- **Equipment** (direct cost equipment purchases)
- **Materials & Supplies** (direct cost purchases, materials)
- **Travel** (direct cost travel, per diem, lodging, transport)
- **Shipping/Freight** (direct cost shipping)
- **Indirect Costs** (overhead, G&A, fringe, indirect R&D)
- **Rent/Facilities** (allocated facility costs)
- **Other** (anything not fitting above)

For each category show: total amount, number of transactions, and largest individual items.

## Purchase Orders
List POs with: number, date, vendor, amount, description.

## Monthly Spend by Category
Show monthly totals broken down by cost category to reveal burn rate and spending patterns.

## Notable Transactions
Flag any large or unusual transactions.

Be precise with dollar amounts. Use actual transaction data, don't estimate."""


SUMMARY_DISTILL_PROMPT = """\
You are creating a company-wide financial overview for BST from QuickBooks data.

# BST Financial Overview (QuickBooks)

## Company Totals
- Total revenue (invoices) for the period
- Total expenses for the period
- Net income estimate

## By Project/Class
For each project, show: name, total revenue, total expenses, net position.
Sort by total activity (highest first).

## Top Vendors
List the top vendors by spend amount.

## Top Customers
List the top customers by revenue.

## Cash Flow Indicators
- Accounts receivable (outstanding invoice balances)
- Recent large expenses
- Any projects with no recent activity (may be complete)

## Unclassified Transactions
Summarize any transactions not assigned to a project class.

Be factual. Include dollar amounts."""


def scan_all(mode="full", progress_callback=None):
    """Scan QuickBooks Online for financial data, organized by project class.

    Returns list of (class_name, txn_count, output_path) tuples.
    """
    config = _get_qbo_config()
    realm_id = config["QUICKBOOKS_REALM_ID"]

    print("Authenticating with QuickBooks Online...")
    access_token = _refresh_access_token(config)
    print("  Authenticated successfully")

    # Determine date range
    start_date = None
    if mode == "1yr":
        start_date = (date.today() - timedelta(days=365)).isoformat()
        print(f"1yr mode: fetching data since {start_date}")
    elif mode == "incremental":
        last = get_last_scan("quickbooks")
        if last:
            start_date = last.strftime("%Y-%m-%d")
            print(f"Incremental: changes since {start_date}")
        else:
            print("No previous scan — falling back to full")
            mode = "full"

    if mode == "full":
        # Full mode: current FY + prior year
        start_date = (date.today() - timedelta(days=730)).isoformat()
        print(f"Full mode: fetching data since {start_date}")

    # Fetch classes (project list)
    print("\nFetching project classes...")
    classes = _fetch_classes(access_token, realm_id)
    class_map = {c["Id"]: c["Name"] for c in classes}
    print(f"  Found {len(classes)} project classes")

    # Fetch all transaction types
    print("\nFetching transactions...")

    print("  Invoices...")
    invoices = _fetch_invoices(access_token, realm_id, start_date)
    print(f"    {len(invoices)} invoices")

    print("  Bills...")
    bills = _fetch_bills(access_token, realm_id, start_date)
    print(f"    {len(bills)} bills")

    print("  Purchases...")
    purchases = _fetch_purchases(access_token, realm_id, start_date)
    print(f"    {len(purchases)} purchases")

    print("  Purchase Orders...")
    pos = _fetch_purchase_orders(access_token, realm_id, start_date)
    print(f"    {len(pos)} purchase orders")

    print("  Payments received...")
    payments = _fetch_payments(access_token, realm_id, start_date)
    print(f"    {len(payments)} payments")

    # Classify all transactions by project
    print("\nClassifying transactions by project...")
    all_by_class = defaultdict(list)

    for txn_type, txns in [("Invoice", invoices), ("Bill", bills),
                           ("Purchase", purchases), ("PO", pos),
                           ("Payment", payments)]:
        classified = _classify_transactions(txns, txn_type)
        for cls_name, entries in classified.items():
            all_by_class[cls_name].extend(entries)

    print(f"  {len(all_by_class)} project classes with transactions")

    # Also fetch P&L report for high-level summary
    pl_text = ""
    try:
        print("\nFetching Profit & Loss report...")
        pl_params = {"start_date": start_date, "end_date": date.today().isoformat()}
        if start_date:
            pl_params["start_date"] = start_date
        pl_report = _qbo_report(access_token, realm_id, "ProfitAndLoss", pl_params)
        # Flatten the report into readable text
        pl_text = _flatten_report(pl_report)
        print(f"  P&L report: {len(pl_text)} chars")
    except Exception as e:
        print(f"  [WARN] Could not fetch P&L report: {e}")

    # Process each project class
    results = []
    class_names = sorted(all_by_class.keys())

    for i, cls_name in enumerate(class_names):
        entries = all_by_class[cls_name]
        print(f"\n[{i + 1}/{len(class_names)}] {cls_name} ({len(entries)} transactions)")

        raw_input = (
            f"PROJECT/CLASS: {cls_name}\n"
            f"Total transactions: {len(entries)}\n"
            f"Date range: {start_date or 'all time'} to {date.today().isoformat()}\n\n"
            f"--- TRANSACTIONS ---\n\n"
            + "\n\n".join(entries)
        )

        filename = _safe_filename(cls_name) + ".md"
        output_path = QBO_PROJECT_DIR / filename

        result = distill_to_markdown(raw_input, PROJECT_DISTILL_PROMPT, output_path, max_tokens=3000)
        if result:
            results.append((cls_name, len(entries), output_path))

    # Generate summary
    if results:
        _generate_summary(results, pl_text)

    update_scan_timestamp("quickbooks")
    return results


def _flatten_report(report_data):
    """Flatten a QBO report JSON into readable text."""
    lines = []
    header = report_data.get("Header", {})
    lines.append(f"Report: {header.get('ReportName', 'Unknown')}")
    lines.append(f"Period: {header.get('StartPeriod', '')} to {header.get('EndPeriod', '')}")
    lines.append(f"Currency: {header.get('Currency', 'USD')}")
    lines.append("")

    columns = report_data.get("Columns", {}).get("Column", [])
    col_names = [c.get("ColTitle", "") for c in columns]
    lines.append(" | ".join(col_names))

    rows = report_data.get("Rows", {}).get("Row", [])
    _flatten_rows(rows, lines, indent=0)

    return "\n".join(lines)


def _flatten_rows(rows, lines, indent=0):
    """Recursively flatten report rows."""
    prefix = "  " * indent
    for row in rows:
        row_type = row.get("type", "")

        if row_type == "Section":
            header = row.get("Header", {})
            col_data = header.get("ColData", [])
            if col_data:
                vals = [c.get("value", "") for c in col_data]
                lines.append(f"{prefix}{'  '.join(v for v in vals if v)}")

            sub_rows = row.get("Rows", {}).get("Row", [])
            _flatten_rows(sub_rows, lines, indent + 1)

            summary = row.get("Summary", {})
            col_data = summary.get("ColData", [])
            if col_data:
                vals = [c.get("value", "") for c in col_data]
                lines.append(f"{prefix}  TOTAL: {'  '.join(v for v in vals if v)}")

        elif row_type == "Data":
            col_data = row.get("ColData", [])
            vals = [c.get("value", "") for c in col_data]
            lines.append(f"{prefix}{'  |  '.join(v for v in vals if v)}")


def _generate_summary(results, pl_text=""):
    """Generate company-wide financial summary."""
    snippets = []
    for cls_name, txn_count, path in results:
        if path.exists():
            content = path.read_text()
            snippets.append(f"### {cls_name} ({txn_count} transactions)\n{content[:600]}")

    if not snippets:
        return

    combined = "\n\n".join(snippets)
    if pl_text:
        combined = f"=== PROFIT & LOSS REPORT ===\n{pl_text}\n\n=== PER-PROJECT DATA ===\n{combined}"
    if len(combined) > 90000:
        combined = combined[:90000] + "\n\n[TRUNCATED]"

    client = get_claude_client()
    for attempt in range(5):
        try:
            message = client.messages.create(
                model=DISTILL_MODEL,
                max_tokens=3000,
                system=SUMMARY_DISTILL_PROMPT,
                messages=[{"role": "user", "content": f"QuickBooks data:\n\n{combined}"}],
            )
            summary_path = QBO_KNOWLEDGE_DIR / "summary.md"
            write_knowledge_file(summary_path, message.content[0].text)
            print(f"  QBO summary written to {summary_path}")
            return
        except Exception as e:
            if "rate_limit" in str(e).lower():
                wait = 30 * (attempt + 1)
                print(f"  Rate limited, waiting {wait}s...")
                time.sleep(wait)
            else:
                print(f"  [WARN] Summary generation failed: {e}")
                return
