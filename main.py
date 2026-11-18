#!/usr/bin/env python3
"""make.fun entry for news-image-20261117: "Sum up 17 November's world news in one image".

The entry image is a static asset (entry.png, stored beside this file): an
editorial front page, "THE WORLD IN ONE DAY", summing up the world news of
Tuesday 17 November 2026 in six illustrated panels. This program copies it
byte-for-byte into the output directory, so every run writes exactly the
same bytes. It never deletes or cleans anything in the output directory.
"""

import os
import shutil
from pathlib import Path

IMAGE_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def main() -> None:
    source = Path(__file__).resolve().parent / IMAGE_NAME
    if not source.is_file():
        raise SystemExit(f"entry image missing beside main.py: {source}")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / IMAGE_NAME
    shutil.copyfile(source, target)

    written = target.stat().st_size
    expected = source.stat().st_size
    if written != expected:
        raise SystemExit(f"copy incomplete: wrote {written} of {expected} bytes")
    print(f"wrote {target} ({written} bytes)")



if __name__ == "__main__":
    main()
