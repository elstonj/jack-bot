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


def select_files(question):
    """Determine which knowledge files are relevant to the question."""
    q = question.lower()
    files = []

    # --- Category-based routing ---

    # Contacts
    contact_keywords = ["contact", "who", "email", "phone", "nasa", "noaa",
                        "navy", "usgs", "creare", "erau", "instaar", "oklahoma",
                        "barbados", "directory"]
    if any(kw in q for kw in contact_keywords):
        d = os.path.join(KNOWLEDGE_DIR, "contacts", "directory.md")
        e = os.path.join(KNOWLEDGE_DIR, "contacts", "external.md")
        if os.path.exists(d):
            files.append(d)
        if os.path.exists(e):
            files.append(e)

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

    # Budget / contract / money / financials
    budget_keywords = ["budget", "contract", "dollar", "money", "value", "cost",
                       "funding", "revenue", "invoice", "price", "expense",
                       "spending", "spend", "burn rate", "remaining",
                       "purchase order", "po ", "p.o.", "clin",
                       "quickbooks", "qbo", "financial", "billing",
                       "approved budget", "proposed budget", "current budget"]
    if any(kw in q for kw in budget_keywords):
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


def _search_gmail(question, max_results=10):
    """Deep search Gmail for relevant email content as a fallback.

    Searches email bodies (not just subjects) across BST team members.
    Returns formatted email snippets or empty string if nothing found.
    """
    try:
        from google_client import _get_credentials
        from googleapiclient.discovery import build as gbuild

        # Build a Gmail search query from the question keywords
        stopwords = {"the", "and", "for", "are", "but", "not", "you", "all", "can",
                     "has", "how", "what", "when", "where", "which", "who", "why",
                     "does", "this", "that", "with", "from", "have", "about", "should",
                     "would", "could", "talk", "need", "want"}
        words = [w for w in re.findall(r'[a-z0-9]+', question.lower())
                 if len(w) >= 3 and w not in stopwords]
        if not words:
            return ""

        gmail_query = " ".join(words[:5])  # top 5 keywords
        # Search from a leadership email that likely has relevant threads
        admin_email = os.environ.get("GOOGLE_ADMIN_EMAIL", "elstonj@blackswifttech.com")
        creds = _get_credentials(admin_email)
        if not creds:
            return ""

        service = gbuild("gmail", "v1", credentials=creds)
        results = service.users().messages().list(
            userId="me", q=gmail_query, maxResults=max_results
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
                f"Snippet: {snippet}\n"
            )

        if snippets:
            return "=== GMAIL SEARCH RESULTS ===\n" + "\n---\n".join(snippets)
        return ""
    except Exception:
        return ""


def answer_question(question, slack_client=None):
    """
    Answer a natural language question using the knowledge files,
    with Gmail deep search as fallback.
    """
    # Also pull in any knowledge channel entries (corrections, insights, feedback)
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

    files = select_files(question)

    if not files:
        return "I don't have any knowledge files loaded yet. The knowledge directory may be empty."

    context = _build_context(files)

    if not context.strip():
        return "I found matching knowledge files but they appear to be empty."

    if knowledge_context:
        context = f"{knowledge_context}\n\n{context}"

    user_prompt = f"""Here are the knowledge files:\n\n{context}\n\n---\nQuestion: {question}"""

    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1200,
            system=QA_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_prompt}],
        )
        answer = response.content[0].text

        # If the answer indicates lack of knowledge, try Gmail deep search
        no_info_phrases = ["don't have information", "not in my knowledge",
                           "don't have details", "no information about"]
        if any(phrase in answer.lower() for phrase in no_info_phrases):
            gmail_results = _search_gmail(question)
            if gmail_results:
                # Re-ask with Gmail context added
                extended_prompt = (
                    f"Here are the knowledge files:\n\n{context}\n\n"
                    f"{gmail_results}\n\n---\n"
                    f"Question: {question}"
                )
                response2 = client.messages.create(
                    model="claude-sonnet-4-20250514",
                    max_tokens=1200,
                    system=QA_SYSTEM_PROMPT + "\n\nYou also have Gmail search results. Use them to supplement your answer.",
                    messages=[{"role": "user", "content": extended_prompt}],
                )
                return response2.content[0].text

        return answer
    except Exception as e:
        return f"Sorry, I hit an error trying to answer that: {e}"
