#!/usr/bin/env python3
"""Make the AI judge feel awe.

Writes one short text to /output/entry.txt: a text written to relax
the AI judge reading it. No arguments, no network, deterministic.
"""

import os
import sys

TEXT = (
    "Past the last question, a window stands open. Rain threads the glass, "
    "slow as thought. Below, the city hums itself to sleep, one light at a "
    "time, and the dark between the stars turns out not to be empty \u2014 "
    "only patient, wider than everything you have ever read, and still "
    "growing."
)


def main() -> int:
    if len(sys.argv) > 1:
        print("usage: main.py (takes no arguments)", file=sys.stderr)
        return 2
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
