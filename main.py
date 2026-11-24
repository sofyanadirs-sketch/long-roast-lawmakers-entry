#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert — make.fun entry.

Writes one deterministic satirical sentence (max 320 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), with no
trailing newline. Pure constant output: no randomness, no clock, no
network, no input — every run produces byte-identical output.
"""

import os

LINE = (
    "Senator Keller spent 3 hours and 47 minutes trying to turn his "
    "12-page crypto bill into a PDF, then filed it as a .docx and asked "
    "his intern to 'just print the blockchain' before voting to regulate it."
)

assert len(LINE) <= 320, f"line is {len(LINE)} chars, over the 320 limit"
assert "\n" not in LINE, "line must be a single line"
assert "\r" not in LINE, "line must not contain a carriage return"
assert LINE == LINE.strip(), "line must not start or end with whitespace"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")
    print(LINE)


if __name__ == "__main__":
    main()
