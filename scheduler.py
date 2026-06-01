import html
import os
import time
from apscheduler.schedulers.background import BackgroundScheduler
from slack_sdk import WebClient

import anthropic

from daily_research import run_daily_pipeline
from research_cache import get_team_summary, get_per_user_sections  # noqa: F401  per_user still used by DM path via cache
from snow_day import check_and_post as check_snow_day
from snow_day import check_and_post_eod as check_snow_day_eod
from eldora import check_and_post as check_eldora
from marketing_check import check_and_post as check_marketing
from weather import format_weather
from google_client import get_latest_email_by_subject
from commercial_sales import (
    load_builds,
    load_support_cases,
    render_card_sequence,
)


PURCHASING_REFORMAT_PROMPT = """\
You are reformatting a daily purchasing summary email for Slack. The input is the body of
a Gemini-generated report. It may arrive in any of these shapes — handle them all:
  (a) markdown with pipe-delimited tables (| Vendor | Order ID | ... |)
  (b) one long run-on line where field labels are concatenated with no separators
      ("Vendor: XOrder Date: YItems Ordered: Z...") — split on the labels
  (c) loose prose with one entry per paragraph

Rules:
- Decode any HTML entities you see (&#39; → ', &quot; → ", &amp; → &, etc.)
- Drop preamble like "Here is the summary..." / "Below is a summary..." and any
  date-range header — the parent message already has a title
- Use *bold* for section headers and vendor names (Slack mrkdwn, not markdown headings)
- Group entries under section headers like *New / Confirmed Orders*,
  *Shipped / In Transit*, *Delivered*. If the source has no sections, infer them
  from each entry's status. Skip empty sections.
- Format each order as exactly:
    *<Vendor>* — Order `<id>`
    • Items: <short summary, ≤ 120 chars; collapse long part lists>
    • Total: $X    (omit this line if no amount given)
    • Status: <tracking #, ETA, backorder note, etc.>
- Drop fields that say "Not provided", "Not specified", "N/A", "Unknown", or are empty
- Preserve concrete data: dollar amounts, tracking numbers, expected ship/delivery dates
- Don't add commentary, recommendations, or invent details
- One blank line between entries; no horizontal rules; no markdown headings (#, ##)
- Output the formatted body only — no preamble, no closing remarks, no code fences"""


def _reformat_purchasing_for_slack(raw_body: str) -> str:
    """Convert the purchasing email body into Slack-friendly mrkdwn.

    Falls back to the (entity-decoded) raw body if Claude is unavailable.
    """
    decoded = html.unescape(raw_body)
    try:
        client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
        msg = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=3000,
            system=PURCHASING_REFORMAT_PROMPT,
            messages=[{"role": "user", "content": decoded[:15000]}],
        )
        return msg.content[0].text.strip()
    except Exception:
        return decoded


def _bot_dm_footer(client) -> str:
    """One-line nudge telling the team how to get their personal top 3 via DM.

    Per-user sections are still generated and cached every run — they're just
    no longer broadcast to #operations. Anyone can pull their own list (and
    leave feedback) by DMing the bot.
    """
    try:
        bot_user_id = client.auth_test()["user_id"]
        mention = f"<@{bot_user_id}>"
    except Exception:
        mention = "@Jack Bot"
    return (
        f":speech_balloon: _DM {mention} `tasks` for your personal top 3 today — "
        f"or just chat to give feedback / corrections._"
    )


def post_daily_tasks():
    """Run the daily research pipeline and post the team summary to #operations.

    Per-user sections are still generated (DM `tasks` command pulls them from
    the cache) but are no longer broadcast — the channel post is now strictly
    a team-level overview.
    """
    channel = os.environ.get("DAILY_TASKS_CHANNEL", "#general")
    client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
    try:
        run_daily_pipeline(client)

        team = get_team_summary()
        if team:
            client.chat_postMessage(channel=channel, text=team)
            time.sleep(0.5)
            client.chat_postMessage(channel=channel, text=_bot_dm_footer(client))

    except Exception as e:
        from knowledge import store_entry
        try:
            store_entry(client, "ERROR", f"Scheduled daily pipeline failed: {e}")
        except Exception:
            pass


def tick_snow_day():
    """Hourly check for active snowfall at BST HQ; post a beer call-out if so."""
    client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
    try:
        check_snow_day(client)
    except Exception:
        from knowledge import store_entry
        try:
            store_entry(client, "ERROR", "snow_day check failed")
        except Exception:
            pass


def tick_snow_day_eod():
    """EOD shutdown notice if snow fell any time today."""
    client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
    try:
        check_snow_day_eod(client)
    except Exception:
        from knowledge import store_entry
        try:
            store_entry(client, "ERROR", "snow_day EOD check failed")
        except Exception:
            pass


def tick_eldora_report():
    """6:30 AM MT weekday check for overnight snow at Eldora."""
    client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
    try:
        check_eldora(client)
    except Exception:
        from knowledge import store_entry
        try:
            store_entry(client, "ERROR", "eldora report check failed")
        except Exception:
            pass


def tick_marketing_check():
    """Morning scan for marketing-worthy signals tagging Paige; post to #marketing if any."""
    client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
    try:
        check_marketing(client)
    except Exception as e:
        from knowledge import store_entry
        try:
            store_entry(client, "ERROR", f"marketing check failed: {e}")
        except Exception:
            pass


def post_purchasing_summary():
    """Re-post Jack's daily purchasing summary email to #operations.

    Posts a one-line header as the top-level message ("Daily purchasing summary
    — <date>"), then puts the reformatted email body as a threaded reply under
    it so the channel main view stays clean. Same pattern as
    post_commercial_sales_digest.
    """
    channel = os.environ.get("DAILY_TASKS_CHANNEL", "#general")
    sender = os.environ.get("PURCHASING_SUMMARY_SENDER", "elstonj@blackswifttech.com")
    client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
    try:
        body = get_latest_email_by_subject(
            sender, "Daily Purchasing Summary", sender=sender, max_age_hours=20
        )
        if not body:
            return
        formatted = _reformat_purchasing_for_slack(body.strip())
        today_str = __import__("datetime").date.today().strftime("%A %B %d")
        header_text = f":package:  *Daily Purchasing Summary — {today_str}*"
        header_resp = client.chat_postMessage(channel=channel, text=header_text)
        umbrella_ts = (
            header_resp.get("ts") if isinstance(header_resp, dict)
            else getattr(header_resp, "data", {}).get("ts")
        )
        # Slack hard-limits a single message at 40k chars; trim with a marker.
        if len(formatted) > 39000:
            formatted = formatted[:39000] + "\n…(truncated)"
        client.chat_postMessage(channel=channel, text=formatted, thread_ts=umbrella_ts)
    except Exception as e:
        from knowledge import store_entry
        try:
            store_entry(client, "ERROR", f"purchasing summary post failed: {e}")
        except Exception:
            pass


def post_commercial_sales_digest():
    """Daily morning post to #commercial-sales summarizing customer builds + support.

    Posts two umbrella threads — "Active Orders" and "Customer Leads" — each as
    a top-level header message with its Build / SupportCase cards threaded
    beneath, so leads and committed orders stay visually separate. Users reply
    anywhere in either umbrella thread; the reply-handler matches the reply text
    against the day's full card list to figure out which record they're updating.

    Writes knowledge/commercial_sales/_message_map.json with:
      {
        "scan_date":   "YYYY-MM-DD",
        "channel":     "<channel id>",
        "umbrella_ts": "<first header ts>",   # back-compat single value
        "umbrellas":   ["<orders header ts>", "<leads header ts>"],
        "cards":       [{ts, kind, id, customer, label}, ...] (ordered),
        "messages":    {ts → {kind, id}} (legacy flat map; same data as cards
                       but keyed by ts for O(1) per-card lookups).
      }

    No LLM call at post time — purely a deterministic render of pre-scanned
    JSON records from knowledge/commercial_sales/{builds,support}/.
    """
    import json
    from pathlib import Path

    channel = os.environ.get("COMMERCIAL_SALES_CHANNEL")
    if not channel:
        return  # Not configured; skip silently
    client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
    try:
        builds = load_builds()
        cases = load_support_cases()
        if not builds and not cases:
            return  # Nothing to report — no empty post

        name_to_slack = {}
        try:
            from user_map import build_user_map
            users = build_user_map(client)
            for u in users:
                if u.get("name") and u.get("slack_user_id"):
                    name_to_slack[u["name"]] = u["slack_user_id"]
                    first = u["name"].split()[0] if u["name"] else ""
                    if first and first not in name_to_slack:
                        name_to_slack[first] = u["slack_user_id"]
        except Exception:
            pass

        sequence = render_card_sequence(builds, cases, name_to_slack=name_to_slack)
        if not sequence:
            return

        builds_by_gid = {b.asana_gid: b for b in builds}
        cases_by_id = {c.case_id: c for c in cases}

        message_map = {
            "scan_date": __import__("datetime").date.today().isoformat(),
            "channel": channel,
            "umbrella_ts": None,   # first umbrella ts (back-compat single value)
            "umbrellas": [],       # every umbrella parent (Active Orders, Leads)
            "cards": [],
            "messages": {},        # ts → {kind, id}
        }

        # The sequence is split into umbrella groups, each begun by a "header"
        # entry. Each header posts as its own top-level message; the cards,
        # dividers, and footer that follow it thread under it — so the "Active
        # Orders" and "Customer Leads" threads stay separate in the channel.
        #
        # Slack rate limit ≈ 1 message / sec for chat.postMessage on the
        # standard tier. Sleep between posts so we don't get throttled.
        current_umbrella_ts = None
        for entry in sequence:
            text = entry["text"]
            if len(text) > 39000:
                text = text[:39000] + "\n…(truncated)"

            if entry["kind"] == "header":
                resp = client.chat_postMessage(channel=channel, text=text)
                current_umbrella_ts = (
                    resp.get("ts") if isinstance(resp, dict)
                    else getattr(resp, "data", {}).get("ts")
                )
                if current_umbrella_ts:
                    message_map["umbrellas"].append(current_umbrella_ts)
                    if message_map["umbrella_ts"] is None:
                        message_map["umbrella_ts"] = current_umbrella_ts
                time.sleep(0.5)
                continue

            # Card / divider / footer → threaded reply under the current header.
            resp = client.chat_postMessage(
                channel=channel,
                text=text,
                thread_ts=current_umbrella_ts,
            )
            ts = (
                resp.get("ts") if isinstance(resp, dict)
                else getattr(resp, "data", {}).get("ts")
            )
            if ts and entry.get("id"):
                message_map["messages"][ts] = {
                    "kind": entry["kind"],
                    "id": entry["id"],
                }
                customer = ""
                label = ""
                if entry["kind"] == "build":
                    b = builds_by_gid.get(entry["id"])
                    if b:
                        customer = b.customer or ""
                        label = b.asana_task_name or customer
                elif entry["kind"] == "support":
                    c = cases_by_id.get(entry["id"])
                    if c:
                        customer = c.customer or ""
                        label = c.device or customer
                message_map["cards"].append({
                    "ts": ts,
                    "kind": entry["kind"],
                    "id": entry["id"],
                    "customer": customer,
                    "label": label,
                })
            time.sleep(0.5)

        # Persist the umbrella + per-card map so the reply-handler can route
        # threaded replies. Overwrites the prior scan's map.
        map_path = Path(__file__).parent / "knowledge" / "commercial_sales" / "_message_map.json"
        map_path.parent.mkdir(parents=True, exist_ok=True)
        map_path.write_text(json.dumps(message_map, indent=2))
    except Exception as e:
        from knowledge import store_entry
        try:
            store_entry(client, "ERROR", f"commercial-sales digest post failed: {e}")
        except Exception:
            pass


def post_flight_weather():
    """Daily 8 AM MT weather report for the flight-testing channel."""
    channel = os.environ.get("FLIGHT_TESTING_CHANNEL", "#flight-testing")
    client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
    try:
        client.chat_postMessage(channel=channel, text=format_weather())
    except Exception as e:
        from knowledge import store_entry
        try:
            store_entry(client, "ERROR", f"flight-testing weather post failed: {e}")
        except Exception:
            pass


def start_scheduler():
    """Start the background scheduler for cron jobs."""
    scheduler = BackgroundScheduler(timezone="America/Denver")
    # Grace window so a Railway redeploy that straddles a scheduled fire time
    # still runs the job once it comes up, instead of silently skipping it.
    scheduler.add_job(
        post_daily_tasks,
        "cron",
        day_of_week="mon-fri",
        hour=8,
        minute=0,
        misfire_grace_time=1800,  # 30 min: briefing is still useful a bit late
    )
    # Snow-day check: top of every hour during typical working hours, Mon-Fri.
    # No point in telling the team to go get a beer at 3am.
    scheduler.add_job(
        tick_snow_day,
        "cron",
        day_of_week="mon-fri",
        hour="9-17",
        minute=0,
        misfire_grace_time=900,  # 15 min: still relevant within the hour
    )
    # EOD shutdown notice: 3:30 PM MT Mon-Fri if snow fell today.
    scheduler.add_job(
        tick_snow_day_eod,
        "cron",
        day_of_week="mon-fri",
        hour=15,
        minute=30,
        misfire_grace_time=1800,  # 30 min
    )
    # Eldora overnight snow-report bulletin: 6:30 AM MT Mon-Fri.
    scheduler.add_job(
        tick_eldora_report,
        "cron",
        day_of_week="mon-fri",
        hour=6,
        minute=30,
        misfire_grace_time=1800,  # 30 min: still useful a bit late
    )
    # Weekday 8 AM MT weather report posted to #flight-testing. No weekend
    # posts — nobody's flight-testing on Saturday/Sunday.
    scheduler.add_job(
        post_flight_weather,
        "cron",
        day_of_week="mon-fri",
        hour=8,
        minute=0,
        misfire_grace_time=1800,  # 30 min: forecast is still useful a bit late
    )
    # Daily purchasing summary re-post to #operations. The source email
    # arrives ~07:56 MDT, so fire at 8:05 to give it slack to land.
    scheduler.add_job(
        post_purchasing_summary,
        "cron",
        day_of_week="mon-fri",
        hour=8,
        minute=5,
        misfire_grace_time=3600,  # 1 hr: still useful later in the morning
    )
    # Marketing assist scan to #marketing. Fires after the 8:00 daily
    # pipeline so it sees fresh knowledge entries from this morning's run,
    # but stays cheap by re-using the same data sources.
    scheduler.add_job(
        tick_marketing_check,
        "cron",
        day_of_week="mon-fri",
        hour=8,
        minute=15,
        misfire_grace_time=3600,  # 1 hr: still useful later in the morning
    )
    # Commercial sales & support pipeline digest to #commercial-sales.
    # Renders pre-scanned knowledge/commercial_sales/ JSON records — no LLM
    # call at post time, so it's safe to fire concurrently with the 8:00 daily.
    scheduler.add_job(
        post_commercial_sales_digest,
        "cron",
        day_of_week="mon-fri",
        hour=8,
        minute=2,
        misfire_grace_time=1800,  # 30 min: still useful a bit late
    )
    scheduler.start()
    return scheduler
