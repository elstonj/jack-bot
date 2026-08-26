"""Global Slack write guard and output router.

Two independent controls, both read from the environment on every call so they
can be flipped at runtime and importing this module is harmless when neither is
set:

``JACKBOT_SLACK_MUTE=1``
    Suppress every outbound Slack write. Nothing reaches Slack at all.

``JACKBOT_SLACK_REDIRECT=<channel_id>``
    Send every ``chat_postMessage`` to that channel instead of its intended
    destination, tagged with where it was headed. The rest of the workspace
    hears nothing — mentions and DMs go unanswered — while one private channel
    receives the full picture, including replies the team would have gotten.

Mute wins if both are set.

Why it patches the SDK instead of guarding call sites: Slack writes are spread
across ~19 call sites in 9 modules (``scheduler``, ``feedback``, ``app``,
``snow_day``, ``marketing_check``, ``eldora``, ``knowledge``, plus the
``scripts/`` cron jobs), and every one of them builds its own ``WebClient``.
Guarding them individually is easy to get wrong and impossible to keep right as
new call sites appear. Patching ``slack_sdk.WebClient`` at the class level
catches all of them at the one choke point they share — including the client
Bolt builds internally, so handler ``say()`` calls are covered without touching
``app.py``'s handlers.

Reads are deliberately left alone. The nightly scan needs
``conversations_history`` / ``users_info`` / ``conversations_info`` to build
knowledge files, so neither control may break it. Only methods that produce
user-visible output are intercepted.
"""

import functools
import os
import sys

_TRUTHY = {"1", "true", "yes", "on", "y"}

MUTE_ENV = "JACKBOT_SLACK_MUTE"
REDIRECT_ENV = "JACKBOT_SLACK_REDIRECT"
LOG_ENV = "JACKBOT_SLACK_MUTE_LOG"

# Methods that produce user-visible output. conversations_join is on the list
# because joining a channel posts a visible "…joined the channel" system
# message; nothing in this repo calls it, so blocking it costs no reads.
BLOCKED_METHODS = (
    "chat_postMessage",
    "chat_postEphemeral",
    "chat_update",
    "chat_delete",
    "chat_scheduleMessage",
    "chat_deleteScheduledMessage",
    "chat_meMessage",
    "chat_unfurl",
    "files_upload",
    "files_upload_v2",
    "files_delete",
    "reactions_add",
    "reactions_remove",
    "pins_add",
    "pins_remove",
    "conversations_create",
    "conversations_invite",
    "conversations_join",
    "conversations_kick",
    "conversations_archive",
    "conversations_rename",
    "conversations_setPurpose",
    "conversations_setTopic",
    "views_open",
    "views_publish",
    "views_push",
    "views_update",
)

# Only chat_postMessage carries content worth rerouting. Redirecting a reaction
# or a file upload to another channel is meaningless, so under redirect every
# other write is suppressed exactly as if muted.
REDIRECTABLE = ("chat_postMessage",)

# Callers thread replies off the parent's ts (see scheduler umbrella threading).
# Hand back a stable dummy so that logic runs without blowing up when muted.
_FAKE_TS = "0000000000.000000"

_installed = False
_originals = {}

# ts values this process produced *in the redirect target*. A thread_ts is only
# valid in the channel it came from, so a reply may keep its thread_ts only if
# its parent also landed in the target. Anything else gets flattened.
_redirected_ts = set()
_TS_CAP = 2000

_label_cache = {}
_forward_client_cache = []


def is_muted():
    """True when Slack writes should be suppressed entirely."""
    return os.environ.get(MUTE_ENV, "").strip().lower() in _TRUTHY


def redirect_target():
    """Channel id to reroute output to, or "" when redirect is off."""
    return os.environ.get(REDIRECT_ENV, "").strip()


def _log(action, method, channel, text):
    preview = str(text or "").replace("\n", " ⏎ ")[:300]
    line = f"[slack-mute] {action} {method} -> {channel}: {preview}"
    print(line, file=sys.stderr)
    path = os.environ.get(LOG_ENV)
    if path:
        try:
            with open(path, "a") as fh:
                fh.write(line + "\n")
        except OSError:
            pass  # logging must never break the caller


def _muted_response(kwargs):
    """A SlackResponse-shaped stand-in.

    Callers read the result two ways — ``resp.get("ts")`` when it's a dict and
    ``resp.data.get("ts")`` otherwise — so a plain dict satisfies the first
    branch of both checks in scheduler.py.
    """
    return {
        "ok": True,
        "muted": True,
        "ts": _FAKE_TS,
        "channel": kwargs.get("channel", ""),
        "message": {"ts": _FAKE_TS, "text": kwargs.get("text", "")},
    }


def _channel_label(client, channel_id):
    """Human-readable name for the channel a message was headed to.

    Uses conversations_info/users_info, which are never patched. Best-effort:
    falls back to the raw id so a lookup failure can't break the redirect.
    """
    if not channel_id:
        return "unknown"
    if channel_id in _label_cache:
        return _label_cache[channel_id]

    label = channel_id
    try:
        resp = client.conversations_info(channel=channel_id)
        data = resp.data if hasattr(resp, "data") else resp
        ch = (data or {}).get("channel", {}) or {}
        if ch.get("is_im"):
            who = ch.get("user", "")
            name = ""
            if who:
                u = client.users_info(user=who)
                udata = u.data if hasattr(u, "data") else u
                info = (udata or {}).get("user", {}) or {}
                name = info.get("real_name") or info.get("name") or ""
            label = f"DM with {name}" if name else "DM"
        elif ch.get("name"):
            label = f"#{ch['name']}"
    except Exception:
        pass  # keep the raw id

    _label_cache[channel_id] = label
    return label


def _remember_ts(resp):
    data = resp.data if hasattr(resp, "data") else resp
    ts = (data or {}).get("ts") if isinstance(data, dict) else None
    if ts:
        if len(_redirected_ts) > _TS_CAP:
            _redirected_ts.clear()
        _redirected_ts.add(ts)


def _redirect_kwargs(client, kwargs, target):
    """Rewrite a post so it lands in the target channel, tagged with its origin."""
    new = dict(kwargs)
    origin = new.get("channel", "")
    new["channel"] = target

    thread_ts = new.get("thread_ts")
    if thread_ts and thread_ts in _redirected_ts:
        # Parent also landed in the target, so real threading still works and
        # the parent already carries the origin tag. Leave the body alone.
        return new

    tag = f"_[→ {_channel_label(client, origin)}"
    if thread_ts:
        # thread_ts belongs to another channel; Slack would reject it.
        new.pop("thread_ts", None)
        tag += " · thread reply"
    tag += "]_"

    text = new.get("text") or ""
    new["text"] = f"{tag}\n{text}" if text else tag
    return new


def _wrap(name, original):
    @functools.wraps(original)
    def guarded(self, *args, **kwargs):
        if is_muted():
            _log("suppressed", name, kwargs.get("channel") or "?",
                 kwargs.get("text") if kwargs.get("text") is not None
                 else (args[0] if args else ""))
            return _muted_response(kwargs)

        target = redirect_target()
        if target:
            if name not in REDIRECTABLE:
                _log("suppressed", name, kwargs.get("channel") or "?",
                     kwargs.get("text"))
                return _muted_response(kwargs)
            origin = kwargs.get("channel", "")
            if origin != target:
                _log("redirected", name, origin or "?", kwargs.get("text"))
                kwargs = _redirect_kwargs(self, kwargs, target)
            resp = original(self, *args, **kwargs)
            _remember_ts(resp)
            return resp

        return original(self, *args, **kwargs)

    guarded.__slack_mute_wrapped__ = True
    return guarded


def _forward_client():
    """Lazy WebClient used to forward slash-command responses."""
    if _forward_client_cache:
        return _forward_client_cache[0]
    token = os.environ.get("SLACK_BOT_TOKEN")
    if not token:
        return None
    try:
        from slack_sdk import WebClient
        client = WebClient(token=token)
    except Exception:
        return None
    _forward_client_cache.append(client)
    return client


def _patch_bolt_respond():
    """Slash-command replies bypass WebClient.

    ``respond()`` POSTs to Slack's response_url over plain HTTP, so the
    WebClient patch never sees it. /refresh-tasks is the one path that uses it.
    Under redirect the text is forwarded to the target channel instead of being
    dropped, so an admin running the command still sees the outcome somewhere.
    Best-effort: slack_bolt isn't installed in every context that imports this.
    """
    try:
        from slack_bolt.context.respond.respond import Respond
    except Exception:
        return
    original = Respond.__call__
    if getattr(original, "__slack_mute_wrapped__", False):
        return

    @functools.wraps(original)
    def guarded(self, *args, **kwargs):
        if is_muted():
            _log("suppressed", "respond", "response_url", kwargs.get("text")
                 or (args[0] if args else ""))
            return None

        target = redirect_target()
        if target:
            text = kwargs.get("text")
            if text is None and args:
                text = args[0]
            _log("redirected", "respond", "response_url", text)
            client = _forward_client()
            post = _originals.get("chat_postMessage")
            if client is not None and post is not None:
                try:
                    post(client, channel=target,
                         text=f"_[→ slash-command response]_\n{text}")
                except Exception:
                    pass  # forwarding is best-effort
            return None

        return original(self, *args, **kwargs)

    guarded.__slack_mute_wrapped__ = True
    Respond.__call__ = guarded


def install():
    """Patch the Slack SDK write methods. Idempotent; safe to call anywhere."""
    global _installed
    if _installed:
        return False
    try:
        from slack_sdk import WebClient
    except ImportError:
        return False

    for name in BLOCKED_METHODS:
        original = getattr(WebClient, name, None)
        if original is None:
            continue  # method absent in this SDK version
        if getattr(original, "__slack_mute_wrapped__", False):
            continue
        _originals[name] = original
        setattr(WebClient, name, _wrap(name, original))

    _patch_bolt_respond()
    _installed = True
    return True


# Installed on import so an entry point only needs `import slack_mute`.
install()
