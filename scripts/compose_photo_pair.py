#!/usr/bin/env python3
"""Place a source photograph and generated illustration in exact equal halves.

Requires Pillow. Fits each input without cropping or stretching and uses a
solid matte where the aspect ratio differs. Does not generate or outpaint.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageColor, ImageOps


def fit_panel(path: Path, size: tuple[int, int], background: tuple[int, ...]):
    with Image.open(path) as source:
        source = ImageOps.exif_transpose(source).convert("RGBA")
        fitted = ImageOps.contain(source, size, Image.Resampling.LANCZOS)
    panel = Image.new("RGB", size, background)
    left = (size[0] - fitted.width) // 2
    top = (size[1] - fitted.height) // 2
    panel.paste(fitted, (left, top), fitted)
    return panel, [left, top, left + fitted.width, top + fitted.height]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--photo", required=True, type=Path)
    parser.add_argument("--illustration", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--width", type=int, default=1536)
    parser.add_argument("--height", type=int, default=1536)
    parser.add_argument("--background", default="#F7F1E7")
    args = parser.parse_args()
    if args.width <= 0 or args.height <= 0 or args.height % 2:
        parser.error("width must be positive; height must be positive and even")
    args.photo = args.photo.expanduser()
    args.illustration = args.illustration.expanduser()
    args.out = args.out.expanduser()
    if args.out.suffix.lower() != ".png":
        parser.error("output must be a .png file")
    if args.out.exists():
        parser.error("output exists; choose a new filename")
    try:
        background = ImageColor.getrgb(args.background)
        if len(background) != 3:
            raise ValueError("background must be an opaque RGB color")
        panel_size = (args.width, args.height // 2)
        photo, photo_box = fit_panel(args.photo, panel_size, background)
        illustration, illustration_box = fit_panel(args.illustration, panel_size, background)
        result = Image.new("RGB", (args.width, args.height), background)
        result.paste(photo, (0, 0))
        result.paste(illustration, (0, panel_size[1]))
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with args.out.open("xb") as handle:
            result.save(handle, format="PNG")
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    print(json.dumps({
        "output": str(args.out.resolve()),
        "size": [args.width, args.height],
        "split_y": panel_size[1],
        "panel_size": list(panel_size),
        "photo_box_in_panel": photo_box,
        "illustration_box_in_panel": illustration_box,
        "fit": "contain; no crop, no stretch; solid matte if needed",
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
