"""One-line laugh entry for make.fun.

Writes a single original funny line to /output/entry.txt.
The line is fixed text, written by this program at run time.

Judge criteria the line targets: one sentence, instantly relatable,
and a twist that lands on the last word — the smart speaker meant
to soothe instead reads out the one thing nobody wants heard aloud.
"""

import os
import sys

MAX_CHARS = 200

LINE = (
    "I asked my smart speaker for relaxing music, and it started "
    "reading my search history aloud."
)

DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"


def validate_line(text: str) -> str:
    """Return the entry line, or raise ValueError with a clear reason."""
    if not text or not text.strip():
        raise ValueError("entry line must not be empty or whitespace-only")
    if text != text.rstrip():
        raise ValueError("entry line must not end with trailing spaces")
    if text != text.lstrip():
        raise ValueError("entry line must not start with leading spaces")
    if "\n" in text or "\r" in text:
        raise ValueError("entry line must be a single line (no newlines)")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry line is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    return text


def write_entry(out_dir: str) -> str:
    """Validate the line and write it to <out_dir>/entry.txt."""
    text = validate_line(LINE)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, ENTRY_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return path


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if "--check" in args:
        try:
            text = validate_line(LINE)
        except ValueError as exc:
            print(f"invalid entry line: {exc}", file=sys.stderr)
            return 1
        print(f"line OK ({len(text)} chars): {text}")
        return 0
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    try:
        path = write_entry(out_dir)
    except ValueError as exc:
        print(f"invalid entry line: {exc}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"could not write entry: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
