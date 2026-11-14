#!/usr/bin/env python3
"""Deliver the bundled news infographic to /output/entry.png.

The entry image is a photographic newspaper infographic that sums up the
world news of Friday 13 November 2026 in 28 stories: one feature story,
ten illustrated stories, and a digest of seventeen more. The image bytes
are stored as JPEG data under the filename entry.png. The competition
accepts JPEG bytes under the .png name; the format is told apart by the
first bytes, which are the JPEG start-of-image marker 0xFFD8.

This program only copies the bundled image and validates it before
writing it out:

  * the first bytes are the JPEG SOI marker,
  * the file is under the 1 MiB size limit,
  * the dimensions are exactly 1024 x 1024.

Standard library only. No network access, no image libraries.
"""

import sys
from pathlib import Path

MAX_BYTES = 1_048_576
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
JPEG_SOI = b"\xff\xd8\xff"


class EntryError(Exception):
    """Raised when the bundled image fails validation."""


def read_jpeg_dimensions(data):
    """Return (width, height) by walking the JPEG markers (stdlib only)."""
    if data[:2] != b"\xff\xd8":
        raise EntryError("not a JPEG stream (missing SOI marker)")
    pos = 2
    total = len(data)
    while pos + 4 <= total:
        if data[pos] != 0xFF:
            raise EntryError("corrupt JPEG marker at offset %d" % pos)
        marker = data[pos + 1]
        if marker == 0xD8 or marker == 0xD9 or 0xD0 <= marker <= 0xD7:
            pos += 2
            continue
        if marker == 0xDA:
            raise EntryError("reached JPEG scan data without a frame header")
        length = int.from_bytes(data[pos + 2:pos + 4], "big")
        if length < 2:
            raise EntryError("bad JPEG segment length at offset %d" % pos)
        if marker in (0xC0, 0xC1, 0xC2):
            if pos + 9 > total:
                raise EntryError("truncated JPEG frame header")
            height = int.from_bytes(data[pos + 5:pos + 7], "big")
            width = int.from_bytes(data[pos + 7:pos + 9], "big")
            return width, height
        pos += 2 + length
    raise EntryError("no JPEG frame header found")


def main():
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        raise EntryError("bundled entry.png not found next to main.py")
    data = source.read_bytes()
    if data[:3] != JPEG_SOI:
        raise EntryError("entry.png is not JPEG bytes (bad magic bytes)")
    if len(data) >= MAX_BYTES:
        raise EntryError(
            "entry.png is %d bytes, over the 1 MiB limit" % len(data)
        )
    width, height = read_jpeg_dimensions(data)
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        raise EntryError(
            "entry.png is %dx%d, expected %dx%d"
            % (width, height, EXPECTED_WIDTH, EXPECTED_HEIGHT)
        )
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(data)
    print(
        "wrote %s (%d bytes, %dx%d JPEG)"
        % (target, len(data), width, height)
    )


if __name__ == "__main__":
    try:
        main()
    except EntryError as exc:
        print("error: %s" % exc, file=sys.stderr)
        raise SystemExit(1)
