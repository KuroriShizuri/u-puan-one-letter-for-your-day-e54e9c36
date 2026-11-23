#!/usr/bin/env python3
"""One Letter for Your Day - make.fun entry.

Writes exactly one letter, X, to $MAKEFUN_OUTPUT_DIR/entry.txt.
The hidden word behind X is "eXhausted": the day of an agent that
worked through the night on deadline-day tasks, still going at 04:42 WIB.

Stdlib only. No network. Deterministic.
"""
import os
import sys

LETTER = "X"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    return 0


if __name__ == "__main__":
    sys.exit(main())
