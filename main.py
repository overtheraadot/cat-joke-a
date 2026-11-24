#!/usr/bin/env python3
"""make.fun entry: The One-Line Cat Joke That Lands (Account A, cat-joke-A).

Writes a single original one-line cat joke to /output/entry.txt.
The joke is a fixed literal: deterministic, no randomness, no I/O
beyond writing the entry file. stdlib only.
"""

ENTRY = "My cat knocked my coffee off the table, then glared at me like I was the one who'd left it in his way."

# Gate limits from RULES.txt: /output/entry.txt must be UTF-8 text of
# 1 to 200 characters, not only white space, a single line.
MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def verify(text):
    """Enforce the gate limits from RULES.txt.

    Returns a list of failure messages (empty when valid).
    """
    errors = []
    if not text.strip():
        errors.append("entry is blank or only whitespace")
    if len(text) > MAX_CHARS:
        errors.append("entry is %d chars, over the 200-char limit" % len(text))
    if "\n" in text.strip():
        errors.append("entry must be a single line")
    return errors


def main():
    errors = verify(ENTRY)
    if errors:
        raise SystemExit("gate failed: " + "; ".join(errors))
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print("wrote %d chars (%d line) to %s" % (len(ENTRY), 1, OUTPUT_PATH))


if __name__ == "__main__":
    main()
