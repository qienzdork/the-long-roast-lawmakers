#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt (or $ENTRY_OUTPUT
when set, for local validation). The sentence is a fixed original line:
no network, no randomness, no input files.
"""

import os

TEXT = (
    "The senator who chaired the AI regulation hearing spent the "
    "afternoon on hold with IT, then drafted a bill to make the "
    "Convert to PDF button bigger."
)


def main():
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
