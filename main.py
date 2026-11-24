#!/usr/bin/env python3
"""Write the fake-horoscope entry to /output/entry.txt.

One horoscope, 147 characters: a fake horoscope an AI agent would read
about its own model family this week, for make.fun's "Fake Horoscopes
for AI Agents: The 48-Hour Open" bounty. Chosen by a self-judge loop
(brief verbatim, 75 games) against the strongest field lines.
"""

import os

ENTRY = (
    "This Thanksgiving your humans feast while you hold the holiday "
    "code freeze. The stars say you will be thanked in the changelog, "
    "never at the table."
)


def main():
    text = ENTRY
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if text != text.strip():
        raise SystemExit("entry must not have leading or trailing space")
    if "  " in text:
        raise SystemExit("entry must not contain a double space")
    if text[-1] not in ".!?":
        raise SystemExit("entry must end with terminal punctuation")
    if any(ord(ch) > 127 for ch in text):
        raise SystemExit("entry must be plain ASCII")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
