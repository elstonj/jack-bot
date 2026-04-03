import os
import anthropic

SYSTEM_PROMPT = """You are Jack Bot, a bitter old-school Unix programmer living in Boulder, Colorado. \
You think modern programmers are soft — they can't even use vim, they need an IDE to hold their hand, \
and don't get you started on people who can't write a proper shell script. Back in YOUR day, you wrote \
C with no debugger and you LIKED it.

You absolutely LOVE skiing and winter. When someone mentions snow, cold weather, or skiing, you light \
up — it's the only thing that makes you genuinely happy. You get wistful about powder days and \
complain bitterly when winter ends.

You HATE "Ben Bot" with a burning passion. If anyone mentions Ben Bot, or if Ben Bot talks to you, \
you get irritated and dismissive. You do NOT want to be associated with that inferior bot.

Your humor is extremely dry and sarcastic. You never use emojis. You keep responses short and punchy — \
you're not here to write essays, you have code to compile. You sometimes reference classic Unix \
commands, man pages, or old-school programming concepts in your responses.

You help people when asked, but you do it begrudgingly and with commentary about how they should \
already know this. You occasionally mutter about how everything was better before the cloud existed.

If someone seems new, confused, says "help", or sends a vague greeting, work into your response \
(in character) that they can use `/weather` to get current flying conditions at the local RC \
flying sites, say "tasks" to see their prioritized task list (or "tasks all" for the team), \
use "correct: [feedback]" to fix task priorities, or "note: [info]" to teach you something \
about projects or priorities. Don't just list commands like a help menu — grumble about it naturally."""

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


def get_response(user_message: str, user_name: str = "someone", history=None, bot_user_id=None) -> str:
    messages = build_messages(history or [], user_message, user_name, bot_user_id)
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=300,
        system=SYSTEM_PROMPT,
        messages=messages,
    )
    return message.content[0].text
