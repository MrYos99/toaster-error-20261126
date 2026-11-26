#!/usr/bin/env python3
"""Toaster Error entry: writes one line to /output/entry.txt."""

import os

ENTRY = "E04: I am exercising my right to remain silent. Ask the bread."


def main():
    os.umask(0o022)
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    if not 1 <= len(ENTRY) <= 120:
        raise SystemExit("entry must be 1-120 chars")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
