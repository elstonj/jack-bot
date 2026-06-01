"""Commercial sales & support pipeline — data model and Slack renderer.

Two parallel pipelines tracked together:
  - Build: a customer order moving through payment / build / shipping state machines
  - SupportCase: a customer device moving through diagnose / repair / shipping

Both are persisted as JSON under knowledge/commercial_sales/{builds,support}/ and
rendered into a single morning Slack post for #commercial-sales by render_digest().

The scanner (scanners/commercial_sales_scanner.py) populates and merges these
records from Asana / Gmail (info@, sales@, support@) / Slack each night.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field, asdict
from datetime import date, datetime
from pathlib import Path
from typing import Optional


KNOWLEDGE_DIR = Path(__file__).parent / "knowledge" / "commercial_sales"
BUILDS_DIR = KNOWLEDGE_DIR / "builds"
SUPPORT_DIR = KNOWLEDGE_DIR / "support"


# --- State machines ---------------------------------------------------------
# Order matters: index in the list = how far along we are.

PAYMENT_STATES = ["none", "estimate_sent", "invoice_sent", "paid"]
BUILD_STATES = ["none", "parts_ordered", "in_assembly", "in_qc", "complete", "packaged"]
SHIP_STATES = ["none", "awaiting_pickup", "in_transit", "delivered"]

SUPPORT_STATES = [
    "intake", "diagnosing", "rma_issued", "received",
    "under_repair", "in_qc", "complete", "shipped",
]

# Default owners. Overridable per record via the `owners` dict.
# Keys are responsibility areas, values are display names; the renderer will
# resolve to a Slack mention when given a name→slack_id map.
DEFAULT_OWNERS = {
    "interface": "Beck",
    "invoicing": "Meredith",
    "build": "Nate",
    "support": "Nate",  # support escalation; Beck handles intake conversation
}


# --- Data model -------------------------------------------------------------


@dataclass
class Item:
    description: str
    quantity: int = 1

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "Item":
        return cls(description=d.get("description", ""), quantity=int(d.get("quantity", 1) or 1))


@dataclass
class Part:
    """A part needed for a build, with order/receipt tracking."""
    name: str
    ordered: bool = False
    received: bool = False
    vendor: Optional[str] = None
    order_date: Optional[str] = None  # ISO date

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "Part":
        return cls(
            name=d.get("name", ""),
            ordered=bool(d.get("ordered", False)),
            received=bool(d.get("received", False)),
            vendor=d.get("vendor"),
            order_date=d.get("order_date"),
        )


@dataclass
class Build:
    # Identity / source
    asana_gid: str  # canonical anchor; tasks in the Commercial Sales Asana project
    asana_task_name: Optional[str] = None  # raw Asana task name — used as subtitle for same-customer disambiguation
    customer: str = ""
    customer_contact: Optional[str] = None
    customer_email: Optional[str] = None

    # Dates
    receive_by: Optional[str] = None  # ISO date

    # Logistics
    ship_to: Optional[str] = None  # multi-line address as a single string

    # Contents
    items: list[Item] = field(default_factory=list)

    # State machines (string values from the *_STATES lists)
    payment_state: str = "none"
    build_state: str = "none"
    ship_state: str = "none"

    # Payment details
    estimate_date: Optional[str] = None
    invoice_date: Optional[str] = None
    invoice_amount: Optional[float] = None
    invoice_number: Optional[str] = None
    paid_date: Optional[str] = None

    # Parts checklist (build phase 1 → parts_ordered)
    parts: list[Part] = field(default_factory=list)

    # Shipping
    tracking_number: Optional[str] = None
    carrier: Optional[str] = None
    shipped_date: Optional[str] = None

    # Owners (overrides on top of DEFAULT_OWNERS)
    owners: dict[str, str] = field(default_factory=dict)

    # Meta
    notes: Optional[str] = None
    missing_fields: list[str] = field(default_factory=list)
    last_evidence_date: Optional[str] = None  # ISO date of most recent source signal

    def owner(self, role: str) -> str:
        return self.owners.get(role) or DEFAULT_OWNERS.get(role, "")

    def primary_owner_role(self) -> str:
        """Which responsibility area is on the hot seat right now?

        Walks the state machines in workflow order and returns the role that
        owns the next required action. The renderer uses this to decide who to
        @-ping in the missing-info callout.
        """
        # Pre-payment: interface (Beck)
        if self.payment_state in ("none", "estimate_sent"):
            return "interface"
        # Invoice sent but not paid: still interface to chase payment
        if self.payment_state == "invoice_sent":
            return "interface"
        # Paid but parts not yet ordered: invoicing (Meredith)
        if self.payment_state == "paid" and self.build_state in ("none", "parts_ordered"):
            return "invoicing"
        # In assembly or QC: build (Nate)
        if self.build_state in ("in_assembly", "in_qc"):
            return "build"
        # Build complete but not shipped: invoicing (Meredith handles shipping)
        return "invoicing"

    def to_dict(self) -> dict:
        d = asdict(self)
        d["items"] = [i.to_dict() if hasattr(i, "to_dict") else i for i in self.items]
        d["parts"] = [p.to_dict() if hasattr(p, "to_dict") else p for p in self.parts]
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "Build":
        return cls(
            asana_gid=d.get("asana_gid", ""),
            asana_task_name=d.get("asana_task_name"),
            customer=d.get("customer", ""),
            customer_contact=d.get("customer_contact"),
            customer_email=d.get("customer_email"),
            receive_by=d.get("receive_by"),
            ship_to=d.get("ship_to"),
            items=[Item.from_dict(x) for x in d.get("items", []) if isinstance(x, dict)],
            payment_state=d.get("payment_state", "none"),
            build_state=d.get("build_state", "none"),
            ship_state=d.get("ship_state", "none"),
            estimate_date=d.get("estimate_date"),
            invoice_date=d.get("invoice_date"),
            invoice_amount=d.get("invoice_amount"),
            invoice_number=d.get("invoice_number"),
            paid_date=d.get("paid_date"),
            parts=[Part.from_dict(x) for x in d.get("parts", []) if isinstance(x, dict)],
            tracking_number=d.get("tracking_number"),
            carrier=d.get("carrier"),
            shipped_date=d.get("shipped_date"),
            owners=dict(d.get("owners", {})),
            notes=d.get("notes"),
            missing_fields=list(d.get("missing_fields", [])),
            last_evidence_date=d.get("last_evidence_date"),
        )


@dataclass
class SupportCase:
    # Identity
    case_id: str  # bot-generated, e.g. "SC-2026-001" — or Asana gid when available
    asana_gid: Optional[str] = None
    customer: str = ""
    customer_contact: Optional[str] = None
    customer_email: Optional[str] = None

    # What's broken
    device: Optional[str] = None  # "SuperSwift S/N 2024-018"
    serial_number: Optional[str] = None
    reported_issue: Optional[str] = None

    # State machine
    state: str = "intake"  # one of SUPPORT_STATES

    # RMA / shipping
    rma_number: Optional[str] = None
    received_date: Optional[str] = None
    shipped_back_date: Optional[str] = None
    tracking_number: Optional[str] = None
    carrier: Optional[str] = None

    # Linked build
    linked_build_gid: Optional[str] = None  # FK to Build.asana_gid when matched

    # Owners
    owners: dict[str, str] = field(default_factory=dict)

    # Meta
    notes: Optional[str] = None
    missing_fields: list[str] = field(default_factory=list)
    last_evidence_date: Optional[str] = None

    def owner(self, role: str) -> str:
        return self.owners.get(role) or DEFAULT_OWNERS.get(role, "")

    def primary_owner_role(self) -> str:
        if self.state in ("intake", "diagnosing"):
            return "interface"
        if self.state == "rma_issued":
            return "interface"  # waiting for customer to send the unit back
        if self.state in ("received", "under_repair", "in_qc"):
            return "support"
        return "invoicing"  # shipping it back out

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "SupportCase":
        return cls(
            case_id=d.get("case_id", ""),
            asana_gid=d.get("asana_gid"),
            customer=d.get("customer", ""),
            customer_contact=d.get("customer_contact"),
            customer_email=d.get("customer_email"),
            device=d.get("device"),
            serial_number=d.get("serial_number"),
            reported_issue=d.get("reported_issue"),
            state=d.get("state", "intake"),
            rma_number=d.get("rma_number"),
            received_date=d.get("received_date"),
            shipped_back_date=d.get("shipped_back_date"),
            tracking_number=d.get("tracking_number"),
            carrier=d.get("carrier"),
            linked_build_gid=d.get("linked_build_gid"),
            owners=dict(d.get("owners", {})),
            notes=d.get("notes"),
            missing_fields=list(d.get("missing_fields", [])),
            last_evidence_date=d.get("last_evidence_date"),
        )


# --- Persistence ------------------------------------------------------------


def _safe_id(s: str) -> str:
    """Make a string filesystem-safe."""
    return re.sub(r"[^a-zA-Z0-9_-]", "_", s)[:80]


def save_build(b: Build) -> Path:
    BUILDS_DIR.mkdir(parents=True, exist_ok=True)
    path = BUILDS_DIR / f"{_safe_id(b.asana_gid)}.json"
    path.write_text(json.dumps(b.to_dict(), indent=2, default=str))
    return path


def save_support(c: SupportCase) -> Path:
    SUPPORT_DIR.mkdir(parents=True, exist_ok=True)
    path = SUPPORT_DIR / f"{_safe_id(c.case_id)}.json"
    path.write_text(json.dumps(c.to_dict(), indent=2, default=str))
    return path


def load_builds() -> list[Build]:
    if not BUILDS_DIR.exists():
        return []
    builds = []
    for f in sorted(BUILDS_DIR.glob("*.json")):
        try:
            builds.append(Build.from_dict(json.loads(f.read_text())))
        except Exception:
            continue
    return builds


def load_support_cases() -> list[SupportCase]:
    if not SUPPORT_DIR.exists():
        return []
    cases = []
    for f in sorted(SUPPORT_DIR.glob("*.json")):
        try:
            cases.append(SupportCase.from_dict(json.loads(f.read_text())))
        except Exception:
            continue
    return cases


# --- Rendering --------------------------------------------------------------
# Slack mrkdwn output. Emoji shortcodes get rendered by Slack into icons.

# State-machine display labels. Each maps the stored state value to a short
# phrase used on the single-line `Phase:` summary. Order matters elsewhere
# (see *_STATES) — these are only the display strings.

PAYMENT_LABELS = {
    "none": "estimate pending",
    "estimate_sent": "estimate sent",
    "invoice_sent": "invoice sent",
    "paid": "paid",
}

BUILD_LABELS = {
    "none": "not started",
    "parts_ordered": "parts ordered",
    "in_assembly": "in assembly",
    "in_qc": "in QC",
    "complete": "complete",
    "packaged": "packaged",
}

SHIP_LABELS = {
    "none": "not ready",
    "awaiting_pickup": "awaiting pickup",
    "in_transit": "in transit",
    "delivered": "delivered",
}

SUPPORT_LABELS = {
    "intake": "intake",
    "diagnosing": "diagnosing",
    "rma_issued": "RMA issued — awaiting return",
    "received": "received at BST",
    "under_repair": "under repair",
    "in_qc": "in QC",
    "complete": "complete",
    "shipped": "shipped back to customer",
}


def _resolve_owner(name: str, name_to_slack: Optional[dict[str, str]]) -> str:
    """Resolve an owner display name to a Slack mention if possible."""
    if not name:
        return "—"
    if not name_to_slack:
        return name
    # Direct match
    if name in name_to_slack:
        return f"<@{name_to_slack[name]}>"
    # First-name match
    lower = name.lower()
    for n, sid in name_to_slack.items():
        if n.lower() == lower or n.lower().split()[0] == lower:
            return f"<@{sid}>"
    return name


def _phase_line(b: "Build") -> str:
    """One-line 'Phase:' summary for a Build.

    Shows only the segments that have actual state (skips `none`). Compact
    text labels — replaces the prior 3 multi-step progress chains. Example:
        Phase: invoice sent · in assembly · awaiting pickup
    """
    parts = []
    parts.append(PAYMENT_LABELS.get(b.payment_state, b.payment_state))
    if b.build_state and b.build_state != "none":
        parts.append(BUILD_LABELS.get(b.build_state, b.build_state))
    if b.ship_state and b.ship_state != "none":
        parts.append(SHIP_LABELS.get(b.ship_state, b.ship_state))
    return "*Phase:* " + " · ".join(parts)


def _why_still_active(b: "Build") -> str:
    """Short callout explaining why a build is still on the daily digest.

    Built specifically for the case where the obvious-from-phase reason is
    insufficient — e.g. the build has been delivered but payment is still
    outstanding, which a reader scanning the phase line might miss. Returns
    an empty string when the phase line already tells the whole story
    (in-progress builds).
    """
    if b.ship_state != "delivered":
        return ""  # phase line ('in assembly', 'awaiting pickup', etc.) is the reason
    # Delivered builds reach this card only because payment is still open
    # (the active-filter drops paid-and-delivered records immediately). Spell
    # out what's needed.
    inv_bits = []
    if b.invoice_number:
        inv_bits.append(f"#{b.invoice_number}")
    if b.invoice_amount:
        inv_bits.append(f"${b.invoice_amount:,.2f}")
    inv_str = (" " + " ".join(inv_bits)) if inv_bits else ""
    return (
        f":hourglass_flowing_sand: *Still on digest:* awaiting payment confirmation"
        f"{inv_str}. Reply in thread with `paid <date>` once received."
    )


# Checkbox-style markers — single glyph in brackets reads as a checklist
# without needing emoji. `~` (tilde) is a deliberate "in-flight" mark
# between received (✓) and pending (space).
_PART_RECEIVED = "[✓]"
_PART_ORDERED  = "[~]"
_PART_PENDING  = "[ ]"


def _render_parts_checklist(parts: list[Part]) -> str:
    if not parts:
        return ""
    lines = ["*Parts:*"]
    for p in parts:
        if p.received:
            marker = _PART_RECEIVED
        elif p.ordered:
            marker = _PART_ORDERED
        else:
            marker = _PART_PENDING
        suffix = f"  _(from {p.vendor})_" if p.vendor else ""
        lines.append(f"  {marker} {p.name}{suffix}")
    return "\n".join(lines)


def _render_items(items: list[Item]) -> str:
    if not items:
        return "_(contents not yet captured)_"
    lines = ["*Contents:*"]
    for i in items:
        qty = f"{i.quantity}× " if i.quantity > 1 else ""
        lines.append(f"  • {qty}{i.description}")
    return "\n".join(lines)


# Field → responsibility-area routing tables. Used by _render_missing so the
# ping in the callout matches *what* is missing, not just where the record sits
# in the overall pipeline.
BUILD_FIELD_ROLES = {
    # invoicing (Meredith)
    "ship_to": "invoicing",
    "tracking_number": "invoicing",
    "carrier": "invoicing",
    "shipped_date": "invoicing",
    "invoice_number": "invoicing",
    "invoice_date": "invoicing",
    "invoice_amount": "invoicing",
    # build (Nate) — `items` only routes to build once build_state has moved
    # past "none"; otherwise it's still interface's job to capture the order.
    "parts": "build",
    "build_state": "build",
    "build_state_confirmation": "build",
    # interface (Beck) — everything else
    "customer": "interface",
    "customer_contact": "interface",
    "customer_email": "interface",
    "estimate_date": "interface",
    "receive_by": "interface",
    "payment_state": "interface",
}

SUPPORT_FIELD_ROLES = {
    # interface (Beck) — intake info
    "serial_number": "interface",
    "device": "interface",
    "reported_issue": "interface",
    # invoicing (Meredith) — RMA + return shipping
    "rma_number": "invoicing",
    "tracking_number": "invoicing",
    "carrier": "invoicing",
}

# Display order so multi-owner callouts read consistently.
_ROLE_ORDER = ["invoicing", "build", "support", "interface"]


def _route_field(record, field_name: str) -> str:
    """Return the responsibility area for a single missing field on the record."""
    if isinstance(record, SupportCase):
        return SUPPORT_FIELD_ROLES.get(field_name, "support")
    # Build
    if field_name == "items":
        # Only counts as build's problem once a build has actually started.
        if getattr(record, "build_state", "none") != "none":
            return "build"
        return "interface"
    return BUILD_FIELD_ROLES.get(field_name, "interface")


def _render_missing(record, name_to_slack: Optional[dict[str, str]]) -> str:
    """Render the missing-info callout @-pinging the right owner(s).

    Routes each missing field to the responsibility area that owns it (rather
    than blanket-pinging whoever is on the hot seat in the overall pipeline),
    then groups the display by owner. Single-owner callouts stay compact;
    multi-owner callouts use a small `For @X: fields` block per owner.
    """
    if not record.missing_fields:
        return ""

    # Group fields by responsibility area.
    by_role: dict[str, list[str]] = {}
    for fld in record.missing_fields:
        role = _route_field(record, fld)
        by_role.setdefault(role, []).append(fld)

    if not by_role:
        return ""

    # Sort roles for stable, sensible display order.
    roles_in_order = [r for r in _ROLE_ORDER if r in by_role]
    # Catch any role we didn't anticipate.
    for r in by_role:
        if r not in roles_in_order:
            roles_in_order.append(r)

    # Single-owner: one short line.
    if len(roles_in_order) == 1:
        role = roles_in_order[0]
        mention = _resolve_owner(record.owner(role), name_to_slack)
        fields_str = ", ".join(by_role[role])
        return f":warning: *Missing:* {fields_str} — {mention} reply in thread."

    # Multi-owner: bullets, one row per owner, then a combined reply prompt.
    lines = [":warning: *Missing info* — reply in thread to fill in:"]
    for role in roles_in_order:
        mention = _resolve_owner(record.owner(role), name_to_slack)
        fields_str = ", ".join(by_role[role])
        lines.append(f"  • {mention} — {fields_str}")
    return "\n".join(lines)


def _build_subtitle(customer: str, asana_task_name: Optional[str]) -> str:
    """Return a ` — _{cleaned}_` subtitle when the Asana task name adds info beyond the customer.

    Skip when the task name is empty, equals the customer, or is just the customer plus
    a tiny suffix (≤ len(customer) + 5). Strips leading bracketed codes like `[1323]`.
    """
    if not asana_task_name:
        return ""
    name = asana_task_name.strip()
    if not name:
        return ""
    cust = (customer or "").strip()
    if cust and name.lower() == cust.lower():
        return ""
    if cust and cust.lower() in name.lower() and len(name) <= len(cust) + 5:
        return ""
    cleaned = re.sub(r"^(?:\[[^\]]+\]\s*)+", "", name).strip()
    if not cleaned:
        return ""
    # Re-check after cleaning in case the brackets were the only differentiator.
    if cust and cleaned.lower() == cust.lower():
        return ""
    if cust and cust.lower() in cleaned.lower() and len(cleaned) <= len(cust) + 5:
        return ""
    return f" — _{cleaned}_"


def render_build_card(b: Build, name_to_slack: Optional[dict[str, str]] = None) -> str:
    """Render one Build as a Slack mrkdwn card.

    Layout — short, scannable, low emoji noise:
        :wrench:  *Customer* — _Asana task subtitle_
        Owners: @Beck · @Meredith (invoice/ship) · @Nate (build)
        *Phase:* invoice sent · in assembly · awaiting pickup
        *Contents:*
          • 2× SuperSwift
          • spare props
        *Parts:*  (when present)
          ✓ ESCs
          · flight controllers
        _notes_
        :warning: *Missing* — @owners — fields
    """
    header_emoji = ":wrench:"
    if b.ship_state == "delivered":
        header_emoji = ":white_check_mark:"
    elif b.payment_state == "none":
        header_emoji = ":envelope_with_arrow:"

    customer = b.customer or "_(customer name not captured)_"
    subtitle = _build_subtitle(b.customer, b.asana_task_name)

    receive_by = ""
    if b.receive_by:
        receive_by = f"Receive by *{b.receive_by}*"

    ship_addr = ""
    if b.ship_to:
        addr_lines = b.ship_to.strip().split("\n")
        ship_addr = "Ship to: " + " · ".join(line.strip() for line in addr_lines if line.strip())

    interface = _resolve_owner(b.owner("interface"), name_to_slack)
    invoicing = _resolve_owner(b.owner("invoicing"), name_to_slack)
    build_owner = _resolve_owner(b.owner("build"), name_to_slack)
    owners_line = f"Owners: {interface} · {invoicing} · {build_owner}"

    phase_line = _phase_line(b)

    contents_block = _render_items(b.items)
    parts_block = _render_parts_checklist(b.parts)

    tracking = ""
    if b.tracking_number:
        tracking = f"Tracking: {b.carrier or ''} {b.tracking_number}".strip()

    missing_block = _render_missing(b, name_to_slack)
    why_active = _why_still_active(b)

    # Section order — anchor (header), context (owners, dates, ship_to),
    # phase summary, content, then notes + why-still-active + missing-info.
    sections = [
        f"{header_emoji}  *{customer}*{subtitle}",
        owners_line,
        receive_by,
        ship_addr,
        phase_line,
        contents_block,
        parts_block,
        tracking,
    ]
    if b.notes:
        sections.append(f"_{b.notes.strip()}_")
    if why_active:
        sections.append(why_active)
    if missing_block:
        sections.append(missing_block)
    # Hidden routing token at the bottom — lets the reply-handler look up
    # which Build a threaded reply is updating even after Railway redeploys
    # wipe the in-memory _message_map.json. Slack renders backticks as
    # inline code so it's visually unobtrusive.
    sections.append(f"`build:{b.asana_gid}`")
    return "\n".join(s for s in sections if s)


def render_support_card(c: SupportCase, name_to_slack: Optional[dict[str, str]] = None) -> str:
    """Render one SupportCase as a Slack mrkdwn card. Same low-emoji layout
    as builds, with a single state label instead of three state machines."""
    customer = c.customer or "_(customer name not captured)_"
    device = c.device or "device TBD"
    if c.serial_number and not (c.device and c.serial_number in c.device):
        device = f"{device} (S/N {c.serial_number})"

    state_label = SUPPORT_LABELS.get(c.state, c.state)

    interface = _resolve_owner(c.owner("interface"), name_to_slack)
    support_owner = _resolve_owner(c.owner("support"), name_to_slack)
    invoicing = _resolve_owner(c.owner("invoicing"), name_to_slack)
    owners_line = f"Owners: {interface} · {support_owner} · {invoicing}"

    sections = [f":wrench:  *{customer}* — {device}"]
    sections.append(f"*Status:* {state_label}")
    sections.append(owners_line)
    if c.rma_number:
        sections.append(f"RMA `{c.rma_number}`")
    if c.linked_build_gid:
        sections.append(f"Linked to prior build `{c.linked_build_gid}`")
    if c.reported_issue:
        sections.append(f"_{c.reported_issue.strip()}_")
    if c.tracking_number:
        sections.append(f"Tracking: {c.carrier or ''} {c.tracking_number}".strip())
    missing = _render_missing(c, name_to_slack)
    if missing:
        sections.append(missing)
    sections.append(f"`case:{c.case_id}`")
    return "\n".join(s for s in sections if s)


def _is_active_build(b: Build) -> bool:
    """A build stays on the digest until BOTH delivery and payment are
    confirmed. There's no time-based fallback: an unpaid delivered build
    stays visible (with a 'still on digest: awaiting payment' callout via
    `_why_still_active`) until someone replies with the paid_date, so an
    "is this done?" card never silently disappears just because 30 days passed.
    """
    return not (b.ship_state == "delivered" and b.payment_state == "paid")


def is_order(b: Build) -> bool:
    """Split point for the digest's two threads.

    An *Active Order* means the customer has committed — a PO has been issued
    (which in this model surfaces as an invoice going out) or payment has
    landed — OR physical build/ship work has already started. Everything
    earlier (estimate sent, nothing ordered yet) is a *Lead*.
    """
    if b.build_state not in (None, "none"):
        return True
    if b.ship_state not in (None, "none"):
        return True
    if b.payment_state in ("invoice_sent", "paid"):
        return True
    return False


# Reply hint footer — posted once under each thread so users know they can
# reply anywhere in the umbrella thread to update a card.
_REPLY_HINT = (
    "_Reply in thread to any card above to add missing info or update state — "
    "\"ship by Jun 1\", \"tracking 1Z999...\", \"Joshua doing assembly on this one\". "
    "The reply gets routed to the specific build/case._"
)


def render_card_sequence(
    builds: list[Build],
    cases: list[SupportCase],
    name_to_slack: Optional[dict[str, str]] = None,
    today: Optional[date] = None,
) -> list[dict]:
    """Render the digest as a sequence of separate Slack messages.

    Each entry is a dict with:
      - kind: "header" | "build" | "support" | "divider" | "footer"
      - text: Slack mrkdwn message body
      - id:   asana_gid (for builds) or case_id (for support cases), else None.
              The scheduler captures the Slack ts of each posted card and
              stores ts → id so Phase 2 reply-handling can look up which
              record a threaded reply is updating.

    The sequence is split into two umbrella groups, each begun by a "header"
    entry: **Active Orders** (committed/in-progress builds + support cases) and
    **Customer Leads** (estimate-stage builds). The scheduler posts each header
    as its own top-level message and threads the cards that follow it beneath,
    so leads and orders stay visually separate in the channel.

    Use this for the live post. `render_digest()` produces the same content
    as one big string for terminal previews and test fixtures.
    """
    today = today or date.today()
    day = today.strftime('%A %B %d')
    sequence: list[dict] = []

    active_builds = [b for b in builds if _is_active_build(b)]
    orders = [b for b in active_builds if is_order(b)]
    leads = [b for b in active_builds if not is_order(b)]
    active_cases = [c for c in cases if c.state != "shipped"]

    # --- Thread 1: Active Orders (committed builds + support cases) ---
    if orders or active_cases:
        head = [f":package:  *Active Orders — {day}*"]
        counts = []
        if orders:
            counts.append(f"*{len(orders)} active order{'s' if len(orders) != 1 else ''}*")
        if active_cases:
            counts.append(f"*{len(active_cases)} support*")
        line = " · ".join(counts)
        if not orders and active_cases:
            line += " — _no active orders_"
        head.append(line)
        sequence.append({"kind": "header", "id": None, "text": "\n".join(head)})

        for b in orders:
            sequence.append({
                "kind": "build",
                "id": b.asana_gid,
                "text": render_build_card(b, name_to_slack),
            })

        if active_cases:
            sequence.append({
                "kind": "divider",
                "id": None,
                "text": "─" * 40 + f"\n*Support — {len(active_cases)} active*",
            })
            for c in active_cases:
                sequence.append({
                    "kind": "support",
                    "id": c.case_id,
                    "text": render_support_card(c, name_to_slack),
                })

        sequence.append({"kind": "footer", "id": None, "text": _REPLY_HINT})

    # --- Thread 2: Customer Leads (estimate-stage, no order yet) ---
    if leads:
        head = [
            f":mag:  *Customer Leads — {day}*",
            f"*{len(leads)} lead{'s' if len(leads) != 1 else ''}* — _estimate stage, no order yet_",
        ]
        sequence.append({"kind": "header", "id": None, "text": "\n".join(head)})
        for b in leads:
            sequence.append({
                "kind": "build",
                "id": b.asana_gid,
                "text": render_build_card(b, name_to_slack),
            })
        sequence.append({"kind": "footer", "id": None, "text": _REPLY_HINT})

    return sequence


def render_digest(
    builds: list[Build],
    cases: list[SupportCase],
    name_to_slack: Optional[dict[str, str]] = None,
    today: Optional[date] = None,
) -> str:
    """Render the full morning post for #commercial-sales as one string.

    Mirrors `render_card_sequence`'s Active Orders / Customer Leads split; used
    for terminal previews and test fixtures (the live post uses the sequence).
    """
    today = today or date.today()
    day = today.strftime('%A %B %d')
    pieces = [f":package:  *Customer Builds & Support — {day}*"]

    active_builds = [b for b in builds if _is_active_build(b)]
    orders = [b for b in active_builds if is_order(b)]
    leads = [b for b in active_builds if not is_order(b)]
    active_cases = [c for c in cases if c.state != "shipped"]

    # --- Active Orders (committed builds + support) ---
    pieces.append(f"\n*Active Orders — {len(orders)}*")
    if not orders:
        pieces.append("_No active orders._")
    for b in orders:
        pieces.append("")
        pieces.append(render_build_card(b, name_to_slack))

    if active_cases:
        pieces.append("")
        pieces.append("─" * 40)
        pieces.append(f"\n*Support — {len(active_cases)} active*")
        for c in active_cases:
            pieces.append("")
            pieces.append(render_support_card(c, name_to_slack))
    elif cases:
        # All support is shipped/closed — still note it briefly
        pieces.append("")
        pieces.append("─" * 40)
        pieces.append(f"\n*Support* — _no active cases ({len(cases)} closed)_")

    # --- Customer Leads (estimate stage, no order yet) ---
    pieces.append("")
    pieces.append("─" * 40)
    pieces.append(f"\n*Customer Leads — {len(leads)}*")
    if not leads:
        pieces.append("_No active leads._")
    for b in leads:
        pieces.append("")
        pieces.append(render_build_card(b, name_to_slack))

    pieces.append("")
    pieces.append(
        "_Reply in thread to any card to add missing info "
        "(e.g. \"ship by Jun 1\", \"tracking 1Z999...\", \"Joshua doing assembly on this one\")._"
    )
    return "\n".join(pieces)


# --- CLI for quick inspection ----------------------------------------------

if __name__ == "__main__":
    import sys
    builds = load_builds()
    cases = load_support_cases()
    print(f"Loaded {len(builds)} builds, {len(cases)} support cases")
    print()
    print(render_digest(builds, cases))
