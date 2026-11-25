#!/usr/bin/env python3
"""News-image entry for make.fun news-image-20261125.

Copies the bundled entry.png (world news of Wednesday 25 November 2026)
to the grader's output directory, deterministically, with no network.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        raise FileNotFoundError(src)
    # The gate allows at most 1 MiB and 1024x1024; our image is 1024x1024, ~109 KB.
    if os.path.getsize(src) > 1048576:
        raise ValueError("entry.png is over 1 MiB")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    os.chmod(dst, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
