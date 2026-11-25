#!/usr/bin/env python3
"""Write one original funny line for the One-Line Laugh-Off.

Pure standard library, no network. Writes the line to /output/entry.txt
and prints it to stdout.
"""

import os

OUTPUT_PATH = "/output/entry.txt"


def get_line() -> str:
    """Return the entry line: a joke request backfires in public."""
    return (
        "I asked my smart speaker to tell me a joke, so it read my search "
        "history aloud \u2014 the whole room went quiet, and so did I."
    )


LINE = get_line()


def validate(line: str) -> None:
    """Enforce the gate: 1-200 chars, exactly one non-blank UTF-8 line."""
    if line != line.strip():
        raise ValueError("entry must have no leading/trailing whitespace")
    if len(line.splitlines()) != 1:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry line must be 1-200 characters")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    line.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Round-trip check: what the grader reads must be exactly the line.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        assert f.read() == LINE + "\n", "entry.txt round-trip mismatch"
    print(LINE)


if __name__ == "__main__":
    main()
