#!/usr/bin/env python3
"""Export mermail-yc-deck.html to a PDF — one slide per landscape page.

The deck renders one slide at a time (others are opacity:0), so we drive headless
Chrome to each slide via its #sN hash, screenshot at 2x for crispness, and stitch
the frames into a single PDF. Run from the project root after building the deck:
    python3 scripts/build-yc-deck.py && python3 scripts/export-pdf.py
"""
import pathlib
import re
import subprocess
import tempfile

from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
HTML = ROOT / "mermail-yc-deck.html"
OUT = ROOT / "mermail-yc-deck.pdf"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

WIDTH, HEIGHT, SCALE = 1600, 900, 2  # 16:9 page, rendered at 2x

n_slides = len(re.findall(r'<section class="slide', HTML.read_text()))
tmp = pathlib.Path(tempfile.mkdtemp(prefix="yc-pdf-"))
frames = []

for i in range(n_slides):
    png = tmp / f"slide{i:02d}.png"
    subprocess.run(
        [
            CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            f"--force-device-scale-factor={SCALE}",
            f"--window-size={WIDTH},{HEIGHT}",
            f"--screenshot={png}", "--virtual-time-budget=3000",
            f"file://{HTML}#s{i}",
        ],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    frames.append(Image.open(png).convert("RGB"))
    print(f"  captured slide {i + 1}/{n_slides}")

frames[0].save(OUT, save_all=True, append_images=frames[1:], resolution=150.0)
print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB, {n_slides} pages)")
