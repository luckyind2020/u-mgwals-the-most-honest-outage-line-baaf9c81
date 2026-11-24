"""The Most Honest Outage Line — entry runner.

Reads the single status-page line from entry.txt, checks it against the
bounty's limits (one line, at most 160 characters), and prints it.
"""

import sys
from pathlib import Path

MAX_CHARS = 160
ENTRY_FILE = Path(__file__).with_name("entry.txt")


def load_line() -> str:
    text = ENTRY_FILE.read_text(encoding="utf-8").strip()
    lines = text.splitlines()
    if len(lines) != 1:
        raise ValueError(f"expected exactly one line, found {len(lines)}")
    line = lines[0]
    if not line:
        raise ValueError("entry line is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} chars, limit is {MAX_CHARS}")
    return line


def main() -> None:
    line = load_line()
    print(line)
    print(f"({len(line)}/{MAX_CHARS} chars)", file=sys.stderr)


if __name__ == "__main__":
    main()
