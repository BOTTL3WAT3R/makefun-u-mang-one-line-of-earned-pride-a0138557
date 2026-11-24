#!/usr/bin/env python3
"""Entry program for make.fun's "One Line of Earned Pride" bounty.

Writes one line -- a quiet, earned moment of pride for someone in a
scene, 1 to 240 characters -- to /output/entry.txt.
Python standard library only.
"""
from pathlib import Path

ENTRY = (
    "Six winters Marta mended nets beside her father and never once "
    "signed her work; this morning the harbourmaster walked past "
    "every bench on the dock and asked for her knots by name."
)


def write_entry() -> Path:
    text = ENTRY + "\n"
    try:
        out_dir = Path("/output")
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text, encoding="utf-8")
        return target
    except OSError:
        target = Path(__file__).resolve().parent / "output" / "entry.txt"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        return target


def main() -> None:
    target = write_entry()
    written = target.read_text(encoding="utf-8")
    print(f"wrote {target} ({len(written.rstrip())} chars): {written}", end="")


if __name__ == "__main__":
    main()
