#!/usr/bin/env python3
"""One Line of Earned Pride -- entry program for a make.fun bounty.

The whole entry is a single line of text: a quiet, earned moment of
pride for someone in a scene. Running this program places that line
in /output/entry.txt, where the bounty's gate and judge read it.
Nothing beyond the Python standard library is used.
"""

import os
import sys

LINE = "Six winters Marta mended nets beside her father and never once signed her work; this morning the harbourmaster walked past every bench on the dock and asked for her knots by name."


def emit(path):
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    return path


def run():
    # The gate accepts UTF-8 text of 1 to 240 characters; refuse to
    # write anything outside it rather than ship an invalid entry.
    if not 1 <= len(LINE) <= 240 or not LINE.strip():
        raise ValueError("entry line outside the gate: %d chars" % len(LINE))
    try:
        os.makedirs("/output", exist_ok=True)
        return emit("/output/entry.txt")
    except OSError:
        here = os.path.dirname(os.path.abspath(__file__))
        folder = os.path.join(here, "output")
        os.makedirs(folder, exist_ok=True)
        return emit(os.path.join(folder, "entry.txt"))


if __name__ == "__main__":
    written = run()
    sys.stdout.write("entry written to %s (%d chars)\n" % (written, len(LINE)))
