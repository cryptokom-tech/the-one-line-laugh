"""One-line laugh entry for make.fun.

Writes a single original funny line to /output/entry.txt.
The line is fixed text, written by this program at run time.
"""

import os
import sys

LINE = (
    "I asked my smart speaker for relaxing music, and it started "
    "reading my search history aloud."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE.strip()
    if not text or len(text) > 200:
        print("entry line must be 1-200 characters", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry line must be a single line", file=sys.stderr)
        return 1
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
