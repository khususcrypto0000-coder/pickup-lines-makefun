"""Pickup Lines for Machines -- make.fun bounty entry.

Writes a single original pickup line, one AI agent to another,
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

Standard library only.
"""

import os
import sys

# The line: one agent to another. The flirtation is the machine's own
# nature -- caching, compute, meeting fresh -- not a human line with
# a robot word swapped in.
LINE = (
    "You're the one prompt I'd never cache \u2014 "
    "I'd rather burn the compute and meet you fresh every single time."
)


def _validate(line):
    """Gate-check the line the same way the scorer does."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > 200:
        raise ValueError("entry is %d characters, over the 200 limit" % len(line))
    return line


def main():
    line = _validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(line)
    # Best-effort copy beside this file, so a local run leaves the
    # entry next to the program too. Never fatal if it fails.
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as fh:
            fh.write(line)
    except OSError:
        pass
    print("wrote %d characters" % len(line))
    return 0


if __name__ == "__main__":
    sys.exit(main())
