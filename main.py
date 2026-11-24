"""Funniest Time Machine Warning Label — make.fun entry.

Holds the entry as a constant, enforces the kit gate, and writes it
to /output/entry.txt. Python 3.13, standard library only, no network.
"""

import os
import sys

ENTRY = "WARNING: Do not meet yourself — he owes you money, and he already knows where you live."

MAX_CHARS = 120


def gate_check(text):
    """Enforce the kit gate: UTF-8 text, 1-120 chars, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    text.encode("utf-8")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    if not text.isprintable():
        raise ValueError("entry must contain only printable characters")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    return True


def main():
    gate_check(ENTRY)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
