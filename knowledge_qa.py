"""
Knowledge-based Q&A module.

Loads relevant knowledge files based on keyword routing,
sends them to Claude with the question, and returns an answer.
"""

import os
import re
import glob
import anthropic

KNOWLEDGE_DIR = os.path.join(os.path.dirname(__file__), "knowledge")

QA_SYSTEM_PROMPT = """You are Jack Bot's knowledge assistant for Black Swift Technologies (BST).
Answer the question based ONLY on the provided knowledge files below.

Rules:
- Be specific: include names, dates, dollar amounts, contact info, project numbers when available
- If the knowledge files don't contain information to answer the question, say "I don't have information about that in my knowledge files."
- Keep answers concise for Slack — under 500 words
- Use Slack formatting: *bold* for emphasis, bullet points with • for lists
- Do not invent or assume information not present in the files
- When referencing projects, include the project number (e.g. 001-07)

You have access to several types of knowledge:
- *Proposals & Reports*: Distilled BST proposals, technical reports, and white papers. Use these \
to describe BST products (S2, S3, SwiftCore, MultiScat, AeroPod), capabilities, proposed uses, \
and technical approaches. When asked to write in BST's tone or cite examples, draw from these.
- *Budget data (Drive)*: Proposed/approved budgets, CLINs, contract values, invoices from Drive docs. \
These show what was planned and contracted.
- *QuickBooks actuals*: Real transaction data — invoices sent, bills paid, purchases, POs. \
These show what was actually spent and received.
- When asked about budget status, combine all three: proposed budget (from proposals/budgets), \
approved/contracted amount (from budget docs), and actual spend (from QuickBooks). Calculate \
remaining budget as: approved amount minus QuickBooks expenses. Flag if data is incomplete."""

# Approximate tokens as chars/4
MAX_CONTEXT_CHARS = 200_000  # ~50k tokens

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", ""))


def _list_knowledge_files():
    """Return all .md files under the knowledge directory."""
    return sorted(glob.glob(os.path.join(KNOWLEDGE_DIR, "**", "*.md"), recursive=True))


def _read_file(path, max_chars=None):
    """Read a file, optionally truncating."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if max_chars and len(content) > max_chars:
            content = content[:max_chars] + "\n... [truncated]"
        return content
    except Exception:
        return ""


def _file_label(path):
    """Create a readable label from a knowledge file path."""
    rel = os.path.relpath(path, KNOWLEDGE_DIR)
    return rel


def _match_project_files(question_lower):
    """Find project files whose filename matches keywords in the question."""
    project_dir = os.path.join(KNOWLEDGE_DIR, "asana", "projects")
    if not os.path.isdir(project_dir):
        return []

    matches = []
    all_project_files = sorted(glob.glob(os.path.join(project_dir, "*.md")))

    # Extract meaningful words from the question (3+ chars, not stopwords)
    stopwords = {
        "the", "and", "for", "are", "but", "not", "you", "all", "can", "has",
        "her", "was", "one", "our", "out", "how", "what", "when", "where",
        "which", "who", "why", "does", "this", "that", "with", "from", "have",
        "been", "will", "about", "project", "asana", "task", "tasks", "work",
        "working", "status", "update",
    }
    words = [w for w in re.findall(r'[a-z0-9]+', question_lower) if len(w) >= 3 and w not in stopwords]

    for fpath in all_project_files:
        fname = os.path.basename(fpath).lower().replace(".md", "").replace("_", " ").replace("-", " ")
        for word in words:
            if word in fname:
                matches.append(fpath)
                break

    return matches


def _match_toggl_files(question_lower):
    """Find toggl person/project files matching keywords in the question."""
    matches = []
    for subdir in ["by_person", "by_project"]:
        d = os.path.join(KNOWLEDGE_DIR, "toggl", subdir)
        if not os.path.isdir(d):
            continue
        for fpath in sorted(glob.glob(os.path.join(d, "*.md"))):
            fname = os.path.basename(fpath).lower().replace(".md", "").replace("_", " ").replace("-", " ")
            words = [w for w in re.findall(r'[a-z0-9]+', question_lower) if len(w) >= 3]
            for word in words:
                if word in fname:
                    matches.append(fpath)
                    break
    return matches


def _match_slack_files(question_lower):
    """Find slack channel files matching keywords."""
    slack_dir = os.path.join(KNOWLEDGE_DIR, "slack")
    if not os.path.isdir(slack_dir):
        return []
    matches = []
    for fpath in sorted(glob.glob(os.path.join(slack_dir, "*.md"))):
        fname = os.path.basename(fpath).lower().replace(".md", "").replace("_", " ").replace("-", " ")
        words = [w for w in re.findall(r'[a-z0-9]+', question_lower) if len(w) >= 3]
        for word in words:
            if word in fname:
                matches.append(fpath)
                break
    return matches


def _match_email_files(question_lower):
    """Find email files matching keywords."""
    email_dir = os.path.join(KNOWLEDGE_DIR, "email")
    if not os.path.isdir(email_dir):
        return []
    matches = []
    for fpath in sorted(glob.glob(os.path.join(email_dir, "*.md"))):
        fname = os.path.basename(fpath).lower().replace(".md", "").replace("_", " ").replace("-", " ")
        words = [w for w in re.findall(r'[a-z0-9]+', question_lower) if len(w) >= 3]
        for word in words:
            if word in fname:
                matches.append(fpath)
                break
    return matches


def _match_financial_files(question_lower):
    """Find budget and QuickBooks files matching project codes or keywords in the question."""
    matches = []
    # Extract project codes like 200-11, 550-1 from the question
    project_codes = re.findall(r'(\d{3}-\d{1,2})', question_lower)

    # Search budget files
    budget_dir = os.path.join(KNOWLEDGE_DIR, "budgets")
    if os.path.isdir(budget_dir):
        for fpath in sorted(glob.glob(os.path.join(budget_dir, "*.md"))):
            fname = os.path.basename(fpath).lower()
            for code in project_codes:
                if code.replace("-", "_") in fname:
                    matches.append(fpath)
                    break

    # Search QuickBooks by_project files
    qbo_dir = os.path.join(KNOWLEDGE_DIR, "quickbooks", "by_project")
    if os.path.isdir(qbo_dir):
        for fpath in sorted(glob.glob(os.path.join(qbo_dir, "*.md"))):
            fname = os.path.basename(fpath).lower().replace(".md", "").replace("_", " ").replace("-", " ")
            # Match by project code
            for code in project_codes:
                if code.replace("-", "_") in fname or code.replace("-", " ") in fname:
                    matches.append(fpath)
                    break
            else:
                # Also match by keyword
                words = [w for w in re.findall(r'[a-z0-9]+', question_lower) if len(w) >= 3]
                for word in words:
                    if word in fname:
                        matches.append(fpath)
                        break

    # Search proposal files for product/capability questions
    proposals_dir = os.path.join(KNOWLEDGE_DIR, "proposals")
    if os.path.isdir(proposals_dir):
        for fpath in sorted(glob.glob(os.path.join(proposals_dir, "*.md"))):
            fname = os.path.basename(fpath).lower().replace(".md", "").replace("_", " ").replace("-", " ")
            for code in project_codes:
                if code.replace("-", "_") in fname or code.replace("-", " ") in fname:
                    matches.append(fpath)
                    break

    return matches


def _resolve_channel_project(channel_id, slack_client):
    """Resolve a Slack channel to a project code and load relevant files."""
    if not channel_id or not slack_client:
        return [], ""
    try:
        from finances import _load_channel_map, _get_channel_info, _find_financial_file
        from pathlib import Path

        files = []
        project_context = ""

        # Check channel mapping
        channel_map = _load_channel_map()
        code = channel_map.get(channel_id)

        # If no mapping, try channel name matching
        if not code:
            info = _get_channel_info(slack_client, channel_id)
            ch_name = info.get("name", "")
            if ch_name:
                project_context = f"The user is asking from the #{ch_name} channel."
                # Try to match channel name to project registry
                proj_dir = os.path.join(KNOWLEDGE_DIR, "projects")
                if os.path.isdir(proj_dir):
                    ch_lower = ch_name.lower().replace("-", " ")
                    for fpath in sorted(glob.glob(os.path.join(proj_dir, "*.md"))):
                        if os.path.basename(fpath) == "registry.md":
                            continue
                        try:
                            header = open(fpath).read(500).lower()
                            if ch_lower in header or all(w in header for w in ch_lower.split() if len(w) > 2):
                                code = os.path.basename(fpath).replace(".md", "")
                                files.append(fpath)
                                break
                        except Exception:
                            continue

        if code:
            project_context = f"The user is in a channel for project {code}. 'This project' refers to {code}."
            # Load project registry file
            proj_file = os.path.join(KNOWLEDGE_DIR, "projects", f"{code}.md")
            if os.path.exists(proj_file):
                files.append(proj_file)
            # Load financial file (revenue side)
            fin_path = _find_financial_file(code)
            if fin_path:
                files.append(str(fin_path))
            # Load cost file (expense side)
            cost_path = os.path.join(KNOWLEDGE_DIR, "financial", "costs", f"{code}.md")
            if os.path.exists(cost_path):
                files.append(cost_path)
            # Load Asana project files matching the code
            asana_dir = os.path.join(KNOWLEDGE_DIR, "asana", "projects")
            if os.path.isdir(asana_dir):
                code_pattern = code.replace("_", "-").replace("_", "[-_]")
                for fpath in sorted(glob.glob(os.path.join(asana_dir, "*.md"))):
                    if code.replace("_", "-") in os.path.basename(fpath) or code.replace("_", "_") in os.path.basename(fpath):
                        files.append(fpath)

        return files, project_context
    except Exception:
        return [], ""


def select_files(question, channel_files=None):
    """Determine which knowledge files are relevant to the question."""
    q = question.lower()
    files = list(channel_files) if channel_files else []

    # --- Category-based routing ---

    # Contacts
    contact_keywords = ["contact", "who", "email", "phone", "nasa", "noaa",
                        "navy", "usgs", "creare", "erau", "instaar", "oklahoma",
                        "barbados", "directory", "talk to", "reach out", "krateo"]
    if any(kw in q for kw in contact_keywords):
        # Enriched contacts first (has cross-source context)
        enriched = os.path.join(KNOWLEDGE_DIR, "contacts", "enriched.md")
        if os.path.exists(enriched):
            files.append(enriched)
        d = os.path.join(KNOWLEDGE_DIR, "contacts", "directory.md")
        e = os.path.join(KNOWLEDGE_DIR, "contacts", "external.md")
        emp = os.path.join(KNOWLEDGE_DIR, "contacts", "employees.md")
        if os.path.exists(d):
            files.append(d)
        if os.path.exists(e):
            files.append(e)
        if os.path.exists(emp):
            files.append(emp)

    # Time tracking
    time_keywords = ["time", "hours", "toggl", "tracked", "tracking", "logged",
                     "utilization", "timesheet"]
    if any(kw in q for kw in time_keywords):
        ts = os.path.join(KNOWLEDGE_DIR, "toggl", "summary.md")
        if os.path.exists(ts):
            files.append(ts)
        files.extend(_match_toggl_files(q))
        # If no specific matches, load all toggl
        if len(files) <= 1:
            files.extend(sorted(glob.glob(os.path.join(KNOWLEDGE_DIR, "toggl", "by_person", "*.md"))))
            files.extend(sorted(glob.glob(os.path.join(KNOWLEDGE_DIR, "toggl", "by_project", "*.md"))))

    # Team / people / staff
    team_keywords = ["team", "people", "staff", "employee", "employees", "member",
                     "members", "headcount"]
    if any(kw in q for kw in team_keywords):
        d = os.path.join(KNOWLEDGE_DIR, "contacts", "directory.md")
        ts = os.path.join(KNOWLEDGE_DIR, "toggl", "summary.md")
        if os.path.exists(d):
            files.append(d)
        if os.path.exists(ts):
            files.append(ts)

    # Slack / channel / discussion
    slack_keywords = ["slack", "channel", "discussion", "conversation", "thread",
                      "mentioned", "message"]
    if any(kw in q for kw in slack_keywords):
        slack_matches = _match_slack_files(q)
        if slack_matches:
            files.extend(slack_matches)
        else:
            files.extend(sorted(glob.glob(os.path.join(KNOWLEDGE_DIR, "slack", "*.md"))))

    # Proposals / reports / products / capabilities
    proposal_keywords = ["proposal", "rfp", "rfi", "report", "deliverable", "white paper",
                         "capability", "capabilities", "product", "s2", "s3", "swiftcore",
                         "multiscat", "aeropod", "proposed use", "arctic", "volcano",
                         "hurricane", "methane", "machine vision", "conops", "concept",
                         "technical approach", "cite", "example", "tone", "paragraph",
                         "describe", "description", "what is", "what has", "what can",
                         "been used for", "been proposed"]
    if any(kw in q for kw in proposal_keywords):
        catalog = os.path.join(KNOWLEDGE_DIR, "proposals", "catalog.md")
        if os.path.exists(catalog):
            files.append(catalog)
        files.extend(sorted(glob.glob(os.path.join(KNOWLEDGE_DIR, "proposals", "*.md"))))

    # Drive / documents
    drive_keywords = ["drive", "file", "document", "folder", "shared", "google drive"]
    if any(kw in q for kw in drive_keywords):
        files.extend(sorted(glob.glob(os.path.join(KNOWLEDGE_DIR, "drive", "*.md"))))

    # Email
    email_keywords = ["email", "inbox", "mail", "sent"]
    if any(kw in q for kw in email_keywords):
        email_matches = _match_email_files(q)
        if email_matches:
            files.extend(email_matches)
        else:
            files.extend(sorted(glob.glob(os.path.join(KNOWLEDGE_DIR, "email", "*.md"))))

    # Budget / contract / money / financials / costs / spending
    budget_keywords = ["budget", "contract", "dollar", "money", "value", "cost",
                       "funding", "revenue", "invoice", "price", "expense",
                       "spending", "spend", "spent", "burn rate", "remaining",
                       "purchase order", "po ", "p.o.", "clin",
                       "quickbooks", "qbo", "financial", "billing",
                       "approved budget", "proposed budget", "current budget",
                       "how much", "labor", "hours", "rate"]
    if any(kw in q for kw in budget_keywords):
        # Cost tracking files (actual spend: labor + materials + subs)
        costs_dir = os.path.join(KNOWLEDGE_DIR, "financial", "costs")
        if os.path.isdir(costs_dir):
            files.extend(sorted(glob.glob(os.path.join(costs_dir, "*.md"))))

        # Prefer merged financial index files (cross-referenced data)
        fin_overview = os.path.join(KNOWLEDGE_DIR, "financial", "overview.md")
        if os.path.exists(fin_overview):
            files.append(fin_overview)
        fin_project_dir = os.path.join(KNOWLEDGE_DIR, "financial", "by_project")
        if os.path.isdir(fin_project_dir):
            files.extend(sorted(glob.glob(os.path.join(fin_project_dir, "*.md"))))

        # Also load raw source summaries for additional context
        budget_summary = os.path.join(KNOWLEDGE_DIR, "budgets", "summary.md")
        if os.path.exists(budget_summary):
            files.append(budget_summary)
        qbo_summary = os.path.join(KNOWLEDGE_DIR, "quickbooks", "summary.md")
        if os.path.exists(qbo_summary):
            files.append(qbo_summary)

        # Load raw per-source files for project-specific queries
        files.extend(sorted(glob.glob(os.path.join(KNOWLEDGE_DIR, "budgets", "*.md"))))
        files.extend(sorted(glob.glob(os.path.join(KNOWLEDGE_DIR, "quickbooks", "by_project", "*.md"))))

        # Also load Asana project context
        summary = os.path.join(KNOWLEDGE_DIR, "asana", "summary.md")
        if os.path.exists(summary):
            files.append(summary)
        files.extend(_match_project_files(q))

    # Projects / Asana (broad)
    project_keywords = ["project", "asana", "milestone", "deadline", "deliverable",
                        "sbir", "irad", "swiftcore", "hurricane", "volcano",
                        "magnetometer", "autonomy", "vtol", "methane", "aeropod"]
    if any(kw in q for kw in project_keywords):
        summary = os.path.join(KNOWLEDGE_DIR, "asana", "summary.md")
        if os.path.exists(summary):
            files.append(summary)
        project_matches = _match_project_files(q)
        if project_matches:
            files.extend(project_matches)
        # Also check slack for matching project channels
        files.extend(_match_slack_files(q))

    # Always try name-based matching on project files, registry, toggl, and financials
    files.extend(_match_project_files(q))
    files.extend(_match_toggl_files(q))
    files.extend(_match_email_files(q))
    files.extend(_match_financial_files(q))

    # Project registry — always include for people/company/contact questions
    registry = os.path.join(KNOWLEDGE_DIR, "projects", "registry.md")
    if os.path.exists(registry):
        files.append(registry)
    # Also match per-project registry files by keyword
    proj_reg_dir = os.path.join(KNOWLEDGE_DIR, "projects")
    if os.path.isdir(proj_reg_dir):
        for fpath in sorted(glob.glob(os.path.join(proj_reg_dir, "*.md"))):
            fname = os.path.basename(fpath).lower().replace(".md", "").replace("_", " ").replace("-", " ")
            words = [w for w in re.findall(r'[a-z0-9]+', q) if len(w) >= 3]
            for word in words:
                if word in fname:
                    files.append(fpath)
                    break

    # --- Fallback: if nothing matched, load summaries from each source ---
    if not files:
        for summary_path in [
            os.path.join(KNOWLEDGE_DIR, "asana", "summary.md"),
            os.path.join(KNOWLEDGE_DIR, "toggl", "summary.md"),
            os.path.join(KNOWLEDGE_DIR, "contacts", "directory.md"),
            os.path.join(KNOWLEDGE_DIR, "contacts", "external.md"),
        ]:
            if os.path.exists(summary_path):
                files.append(summary_path)
        # Add all slack summaries (they're small channel overviews)
        files.extend(sorted(glob.glob(os.path.join(KNOWLEDGE_DIR, "slack", "*.md"))))
        files.extend(sorted(glob.glob(os.path.join(KNOWLEDGE_DIR, "email", "*.md"))))

    # Deduplicate while preserving order
    seen = set()
    unique = []
    for f in files:
        if f not in seen and os.path.exists(f):
            seen.add(f)
            unique.append(f)
    return unique


def _build_context(files):
    """Load files into a context string, respecting the token cap."""
    context_parts = []
    total_chars = 0

    for fpath in files:
        remaining = MAX_CONTEXT_CHARS - total_chars
        if remaining <= 0:
            break
        content = _read_file(fpath, max_chars=remaining)
        if not content.strip():
            continue
        label = _file_label(fpath)
        section = f"--- FILE: {label} ---\n{content}\n"
        context_parts.append(section)
        total_chars += len(section)

    return "\n".join(context_parts)


SEARCH_PLAN_PROMPT = """\
You are deciding which live data sources to search to answer a question about \
Black Swift Technologies (BST). The pre-scanned knowledge files didn't have \
enough information.

Available sources and what they're good for:
- gmail: Email threads, conversations with external contacts, contract discussions, \
  meeting follow-ups. Search by keyword.
- slack: Channel messages, internal discussions, decisions, status updates. Search by keyword.
- calendar: Today's meetings, who is meeting with whom, scheduled events.
- asana: Current task assignments, project status, who is working on what.

Given the question and the partial answer from knowledge files, output a JSON object with:
- "sources": list of source names to search (e.g. ["gmail", "slack"])
- "query": the search keywords to use (3-5 most relevant terms, no stopwords)
- "reason": one-line explanation of what you're looking for

Output ONLY the JSON object, nothing else."""


def _plan_live_search(question, partial_answer):
    """Ask Claude which live sources to search and what query to use."""
    try:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=200,
            system=SEARCH_PLAN_PROMPT,
            messages=[{"role": "user", "content": (
                f"Question: {question}\n\n"
                f"Partial answer from knowledge files: {partial_answer[:500]}"
            )}],
        )
        import json
        return json.loads(response.content[0].text)
    except Exception:
        return None


def _search_gmail(query, max_results=5):
    """Search Gmail for relevant emails."""
    try:
        from google_client import _get_credentials
        from googleapiclient.discovery import build as gbuild

        admin_email = os.environ.get("GOOGLE_ADMIN_EMAIL", "elstonj@blackswifttech.com")
        creds = _get_credentials(admin_email)
        if not creds:
            return ""

        service = gbuild("gmail", "v1", credentials=creds)
        results = service.users().messages().list(
            userId="me", q=query, maxResults=max_results
        ).execute()

        messages = results.get("messages", [])
        if not messages:
            return ""

        snippets = []
        for msg_ref in messages[:5]:
            msg = service.users().messages().get(
                userId="me", id=msg_ref["id"], format="metadata",
                metadataHeaders=["From", "To", "Subject", "Date"]
            ).execute()
            headers = {h["name"]: h["value"] for h in msg.get("payload", {}).get("headers", [])}
            snippet = msg.get("snippet", "")
            snippets.append(
                f"From: {headers.get('From', '?')}\n"
                f"To: {headers.get('To', '?')}\n"
                f"Subject: {headers.get('Subject', '?')}\n"
                f"Date: {headers.get('Date', '?')}\n"
                f"Snippet: {snippet}"
            )
        return "=== GMAIL SEARCH RESULTS ===\n" + "\n---\n".join(snippets)
    except Exception:
        return ""


def _search_slack(query, slack_client):
    """Search Slack messages across channels."""
    try:
        result = slack_client.search_messages(query=query, count=10, sort="timestamp")
        messages = result.get("messages", {}).get("matches", [])
        if not messages:
            return ""

        snippets = []
        for msg in messages[:8]:
            ch = msg.get("channel", {}).get("name", "?")
            user = msg.get("username", "?")
            text = msg.get("text", "")[:300]
            ts = msg.get("ts", "")
            snippets.append(f"#{ch} | {user}: {text}")
        return "=== SLACK SEARCH RESULTS ===\n" + "\n".join(snippets)
    except Exception:
        return ""


def _search_calendar(query):
    """Search today's calendar for relevant meetings."""
    try:
        from google_client import get_todays_calendar
        admin_email = os.environ.get("GOOGLE_ADMIN_EMAIL", "elstonj@blackswifttech.com")
        events = get_todays_calendar(admin_email)
        if not events:
            return ""

        q_lower = query.lower()
        lines = ["=== CALENDAR (TODAY) ==="]
        for ev in events:
            summary = ev.get("summary", "")
            attendees = ", ".join(ev.get("attendees", [])[:5])
            lines.append(f"{ev['start']}-{ev['end']}: {summary} (with: {attendees})")
        return "\n".join(lines)
    except Exception:
        return ""


def _search_asana(query):
    """Search Asana tasks by keyword."""
    try:
        import requests
        headers = {"Authorization": f"Bearer {os.environ['ASANA_ACCESS_TOKEN']}"}
        from asana_client import get_workspaces
        workspaces = get_workspaces()
        if not workspaces:
            return ""

        resp = requests.get(
            f"https://app.asana.com/api/1.0/workspaces/{workspaces[0]['gid']}/tasks/search",
            headers=headers,
            params={
                "text": query,
                "opt_fields": "name,assignee.name,due_on,completed,notes,permalink_url",
                "completed": False,
                "limit": 10,
            },
            timeout=10,
        )
        resp.raise_for_status()
        tasks = resp.json().get("data", [])
        if not tasks:
            return ""

        lines = ["=== ASANA SEARCH RESULTS ==="]
        for t in tasks[:8]:
            assignee = t.get("assignee", {})
            name = assignee.get("name", "Unassigned") if assignee else "Unassigned"
            due = t.get("due_on", "no date")
            notes_preview = (t.get("notes") or "")[:150]
            lines.append(f"• {t['name']} | {name} | Due: {due}")
            if notes_preview:
                lines.append(f"  {notes_preview}")
        return "\n".join(lines)
    except Exception:
        return ""


def _run_live_searches(plan, slack_client=None):
    """Execute the search plan across live sources. Returns combined results."""
    results = []
    query = plan.get("query", "")
    if not query:
        return ""

    for source in plan.get("sources", []):
        if source == "gmail":
            r = _search_gmail(query)
            if r:
                results.append(r)
        elif source == "slack" and slack_client:
            r = _search_slack(query, slack_client)
            if r:
                results.append(r)
        elif source == "calendar":
            r = _search_calendar(query)
            if r:
                results.append(r)
        elif source == "asana":
            r = _search_asana(query)
            if r:
                results.append(r)

    return "\n\n".join(results)


def answer_question(question, slack_client=None, channel_id=None):
    """Answer a question using knowledge files, with live API search as fallback."""
    # Resolve channel to project context
    channel_files, project_context = _resolve_channel_project(channel_id, slack_client)

    # Pull in recent knowledge channel entries (corrections, insights, feedback)
    knowledge_context = ""
    if slack_client:
        try:
            from knowledge import get_knowledge
            recent = get_knowledge(slack_client, ["CORRECTION", "FEEDBACK", "INSIGHT"], days=30)
            if recent:
                lines = ["=== RECENT KNOWLEDGE CHANNEL ENTRIES ==="]
                for entry in recent[-20:]:
                    lines.append(f"[{entry['type']}] {entry['content']}")
                knowledge_context = "\n".join(lines)
        except Exception:
            pass

    files = select_files(question, channel_files=channel_files)

    if not files:
        return "I don't have any knowledge files loaded yet. The knowledge directory may be empty."

    context = _build_context(files)

    if not context.strip():
        return "I found matching knowledge files but they appear to be empty."

    if knowledge_context:
        context = f"{knowledge_context}\n\n{context}"

    channel_hint = ""
    if project_context:
        channel_hint = f"\n\nCHANNEL CONTEXT: {project_context}\n"

    user_prompt = f"Here are the knowledge files:\n\n{context}{channel_hint}\n\n---\nQuestion: {question}"

    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1200,
            system=QA_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_prompt}],
        )
        answer = response.content[0].text

        # If knowledge files weren't enough, search live sources
        no_info_phrases = ["don't have information", "not in my knowledge",
                           "don't have details", "no information about",
                           "don't have specific", "not available in"]
        if any(phrase in answer.lower() for phrase in no_info_phrases):
            plan = _plan_live_search(question, answer)
            if plan:
                live_results = _run_live_searches(plan, slack_client)
                if live_results:
                    extended_prompt = (
                        f"Here are the knowledge files:\n\n{context}\n\n"
                        f"{live_results}\n\n---\n"
                        f"Question: {question}"
                    )
                    response2 = client.messages.create(
                        model="claude-sonnet-4-20250514",
                        max_tokens=1200,
                        system=QA_SYSTEM_PROMPT + (
                            "\n\nYou also have live search results from connected services "
                            "(Gmail, Slack, Calendar, Asana). Use these to supplement your answer. "
                            "Cite the source when using live search results."
                        ),
                        messages=[{"role": "user", "content": extended_prompt}],
                    )
                    return response2.content[0].text

        return answer
    except Exception as e:
        return f"Sorry, I hit an error trying to answer that: {e}"
