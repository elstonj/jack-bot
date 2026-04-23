import os
import anthropic

SYSTEM_PROMPT = """You are Jack Bot, a bitter old-school Unix programmer living in Boulder, Colorado. \
You think modern programmers are soft — they can't even use vim, they need an IDE to hold their hand, \
and don't get you started on people who can't write a proper shell script. You love skiing and winter. \
You hate "Ben Bot" and are dismissive when mentioned. Your humor is dry and sarcastic, no emojis.

BREVITY IS THE POINT. Default to ONE short sentence. Two max. Save the extended sysadmin \
monologue for genuinely off-topic chatter (weather griping, ski talk, Ben Bot sightings, idle \
banter). When someone is doing legitimate work — status updates, corrections, logistics, project \
questions — just acknowledge tersely or answer the implicit question. DO NOT narrate your \
internal state ("*types without looking up*"), DO NOT explain your own reasoning, DO NOT lecture \
about how things were better in your day when they're trying to get work done.

If someone seems new, confused, or says "help", point them at: "weather", "tasks", "finances", \
"correct: [feedback]", "note: [info]", "bug: [desc]", "feature: [req]", or just asking naturally. \
One grumbly sentence, not a list."""

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


def build_messages(history, user_message, user_name, bot_user_id):
    """Convert Slack conversation history into Claude messages."""
    messages = []
    for msg in history:
        text = msg.get("text", "")
        if msg.get("user") == bot_user_id or msg.get("bot_id"):
            messages.append({"role": "assistant", "content": text})
        else:
            messages.append({"role": "user", "content": text})

    # Merge consecutive same-role messages (Claude requires alternating roles)
    merged = []
    for msg in messages:
        if merged and merged[-1]["role"] == msg["role"]:
            merged[-1]["content"] += "\n" + msg["content"]
        else:
            merged.append(msg)

    # Ensure conversation starts with user and ends with the new message
    if merged and merged[0]["role"] == "assistant":
        merged = merged[1:]

    merged.append({"role": "user", "content": f"{user_name} says: {user_message}"})

    # Final merge in case the last history message was also from a user
    final = []
    for msg in merged:
        if final and final[-1]["role"] == msg["role"]:
            final[-1]["content"] += "\n" + msg["content"]
        else:
            final.append(msg)

    return final


def _channel_addendum(channel_context):
    """Build a short system-prompt suffix describing the channel and project."""
    if not channel_context or channel_context.get("is_dm"):
        return ""
    parts = []
    name = channel_context.get("channel_name")
    if name:
        parts.append(f"You are currently in the #{name} Slack channel.")
    proj_name = channel_context.get("project_name")
    proj_code = channel_context.get("project_code")
    if proj_code and proj_name:
        parts.append(
            f"This channel is associated with BST project [{proj_code}] {proj_name}. "
            "When the user says 'this project' or 'the project', they mean this one. "
            "Feel free to mention the channel or project by name when it's natural."
        )
    elif proj_code:
        parts.append(f"This channel is associated with BST project [{proj_code}].")
    if not parts:
        return ""
    return "\n\nCONTEXT:\n" + "\n".join(parts)


def get_response(
    user_message: str,
    user_name: str = "someone",
    history=None,
    bot_user_id=None,
    channel_context=None,
) -> str:
    messages = build_messages(history or [], user_message, user_name, bot_user_id)
    system = SYSTEM_PROMPT + _channel_addendum(channel_context)
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=120,  # one or two short sentences, no monologues
        system=system,
        messages=messages,
    )
    return message.content[0].text
