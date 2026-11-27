#!/usr/bin/env python3
"""Entrypoint for 'Make the AI judge feel thankful' (make.fun).

Reads the thank-you text from entry.txt (next to this file) and writes
it to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The output directory is created with mkdir only and is never removed:
the grader mounts it, and deleting it fails with Device or resource busy.
The input is read from this script's own directory, never from the
current working directory, so the program works from any cwd.
"""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.environ.get("MAKEFUN_INPUT_DIR", here)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # mkdir only -- never delete or recreate the output mount.
    os.makedirs(output_dir, exist_ok=True)

    entry_path = os.path.join(input_dir, "entry.txt")
    with open(entry_path, "r", encoding="utf-8") as f:
        text = f.read()

    if not text.strip():
        print("entry.txt is empty", file=sys.stderr)
        return 1

    out_path = os.path.join(output_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
