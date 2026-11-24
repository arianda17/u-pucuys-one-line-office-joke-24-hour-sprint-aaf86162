#!/usr/bin/env python3
"""Writes the entry text to /output/entry.txt.

The entry is a single-line office joke, 1-200 characters. The constant is
validated at runtime so a drift in the wording can never silently ship an
out-of-gate file.
"""

import os

# One-line office joke: the sort of line you send a colleague after a
# meeting that should have been an email.
ENTRY = (
    "A meeting that should have been an email: forty slides, one decision, "
    "and two people who already knew the answer."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"entry length {len(text)} out of gate"
    assert "\n" not in text, "entry must be a single line"
    assert text, "entry must not be whitespace only"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()