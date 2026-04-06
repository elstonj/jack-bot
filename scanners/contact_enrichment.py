"""Contact enrichment — augments external contacts with cross-source context.

Reads existing contact, email, Slack, and project knowledge files to build
rich contact profiles: who they are, what projects they work on with BST,
recent interactions, and how to reach them.

Produces:
  knowledge/contacts/enriched.md — enriched external contact profiles

Run after other scanners so all source data is available.
"""

import os
import glob
from pathlib import Path

from .base import (
    KNOWLEDGE_DIR,
    get_claude_client,
    update_scan_timestamp,
    DISTILL_MODEL,
)

CONTACTS_DIR = KNOWLEDGE_DIR / "contacts"
MAX_CONTEXT = 80_000  # chars to send to Claude


def _read_file(path, max_chars=None):
    try:
        text = Path(path).read_text()
        return text[:max_chars] if max_chars else text
    except Exception:
        return ""


def _gather_context():
    """Gather all relevant source data for contact enrichment."""
    sections = []

    # External contacts (raw)
    ext = _read_file(CONTACTS_DIR / "external.md", max_chars=15000)
    if ext:
        sections.append(f"=== EXTERNAL CONTACTS (raw) ===\n{ext}")

    # Employee directory for internal reference
    emp = _read_file(CONTACTS_DIR / "employees.md", max_chars=3000)
    if emp:
        sections.append(f"=== BST EMPLOYEES ===\n{emp}")

    # Email patterns — who emails whom about what
    email_dir = KNOWLEDGE_DIR / "email"
    if email_dir.exists():
        for f in sorted(email_dir.glob("*.md")):
            text = _read_file(f, max_chars=3000)
            if text:
                sections.append(f"=== EMAIL: {f.stem} ===\n{text}")

    # Slack channel context — who is mentioned, what's discussed
    slack_dir = KNOWLEDGE_DIR / "slack"
    if slack_dir.exists():
        for f in sorted(slack_dir.glob("*.md")):
            text = _read_file(f, max_chars=2000)
            if text:
                sections.append(f"=== SLACK: {f.stem} ===\n{text}")

    # Project registry — customer contacts, project associations
    proj_dir = KNOWLEDGE_DIR / "projects"
    if proj_dir.exists():
        for f in sorted(proj_dir.glob("*.md")):
            if f.name == "registry.md":
                continue
            text = _read_file(f, max_chars=1500)
            if text:
                sections.append(f"=== PROJECT: {f.stem} ===\n{text}")

    # Proposals — client/partner mentions
    proposals_dir = KNOWLEDGE_DIR / "proposals"
    catalog = proposals_dir / "catalog.md" if proposals_dir.exists() else None
    if catalog and catalog.exists():
        text = _read_file(catalog, max_chars=3000)
        if text:
            sections.append(f"=== PROPOSALS CATALOG ===\n{text}")

    combined = "\n\n".join(sections)
    if len(combined) > MAX_CONTEXT:
        combined = combined[:MAX_CONTEXT]
    return combined


ENRICHMENT_PROMPT = """\
You are building enriched contact profiles for Black Swift Technologies (BST).

Given raw external contacts plus context from emails, Slack, projects, and proposals, \
produce a structured contact directory grouped by organization.

For each organization/person, include:
- Name, title, email, phone (if available)
- Which BST projects they're involved with (use project codes like 301-3)
- Their role in the relationship (client POC, technical lead, contracting officer, etc.)
- Recent interaction context (email threads, Slack mentions, meetings)
- What topics/projects to contact them about

Skip contacts with no meaningful BST interaction context. Focus on the most \
important external relationships.

Format as clean markdown with ## Organization headers and bullet points per person. \
Be concise but include actionable detail — someone should be able to read a contact's \
entry and know exactly who they are and why BST works with them."""


def enrich(progress_callback=None):
    """Run contact enrichment."""
    CONTACTS_DIR.mkdir(parents=True, exist_ok=True)

    if progress_callback:
        progress_callback("Gathering cross-source context...")
    print("Gathering cross-source contact context...")
    context = _gather_context()

    if not context.strip():
        print("No source data available for enrichment.")
        return

    print(f"  Context: {len(context)} chars from email/slack/projects/proposals")

    if progress_callback:
        progress_callback("Enriching contacts via Claude...")
    print("Enriching contacts via Claude...")

    client = get_claude_client()
    response = client.messages.create(
        model=DISTILL_MODEL,
        max_tokens=4000,
        system=ENRICHMENT_PROMPT,
        messages=[{"role": "user", "content": context}],
    )

    enriched = response.content[0].text
    output_path = CONTACTS_DIR / "enriched.md"
    output_path.write_text(f"# Enriched External Contacts\n\n{enriched}")

    update_scan_timestamp("contact_enrichment")
    print(f"  Wrote enriched contacts: {len(enriched)} chars -> {output_path}")
    return output_path
