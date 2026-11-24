#!/usr/bin/env python3
"""The Houseplant Out-of-Office — a make.fun entry.

Writes one out-of-office auto-reply, as if a houseplant sent it,
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
The line is the whole entry: at most 120 characters, UTF-8,
no trailing newline.
"""

import os
import sys

LINE = (
    "Out of office: I am a fern, unwatered since March. "
    "For urgent matters, please photosynthesize your own reply."
)


def main() -> int:
    if not LINE.strip() or not 1 <= len(LINE) <= 120:
        print(
            f"entry must be 1-120 non-blank characters, got {len(LINE)}",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)  # no trailing newline: the line is the entry
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
