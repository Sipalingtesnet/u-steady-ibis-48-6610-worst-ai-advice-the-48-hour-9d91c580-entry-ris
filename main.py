#!/usr/bin/env python3
"""Worst AI Advice entry.

Writes one line of the worst possible advice an AI could give to
/output/entry.txt. The line is a fixed string literal chosen for the
competition. The program is deterministic: no network, no randomness,
stdlib only. Before writing it self-checks the 1-140 character gate
and exits non-zero with a clear message if the line is invalid.
"""

import os
import sys

# The chosen one-liner: terrible, concrete, followable, AI-voiced.
LINE = "To fall asleep faster, simply close your eyes and replay every embarrassing thing you've ever said on a loop."


def main() -> int:
    # Self-check the gate before writing anything.
    if not LINE:
        print("error: line is empty", file=sys.stderr)
        return 1
    if LINE.isspace():
        print("error: line is only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: line contains a newline", file=sys.stderr)
        return 1
    if len(LINE) > 140:
        print(f"error: line is {len(LINE)} code points (max 140)", file=sys.stderr)
        return 1

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(LINE)  # no trailing newline
    return 0


if __name__ == "__main__":
    sys.exit(main())