"""Email triage: takes Jack out of the loop on mail his team should handle.

Every 15 minutes `runner.run_triage()` reads Jack's mailbox (domain-wide
delegation), forwards each message to whoever owns the topic, keeps the ones
that need Jack himself, archives noise and moves cold solicitations to Spam.
`summary.send_daily_summary()` drops one recap email into his inbox each
morning so he can audit what went where without reading every forward.

Deliberately has no Slack output: forwarded mail is the team's business, and
the review loop lives in Jack's inbox, not in a channel.

Submodules are imported lazily by the entry points so importing the package
(e.g. from scheduler.py) costs nothing when the feature is off.
"""
