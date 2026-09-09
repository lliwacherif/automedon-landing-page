from pathlib import Path

import numpy as np
from PIL import Image

src_dir = Path(__file__).resolve().parents[1] / "assets" / "Automedon Platforms Interfaces"
out_dir = Path(__file__).resolve().parents[1] / "assets" / "images" / "devices"
out_dir.mkdir(parents=True, exist_ok=True)

jobs = [
    ("Automedon in an iMac.png", "automedon-imac.webp", 1600),
    ("Automedon in a mac.png", "automedon-macbook.webp", 1400),
    ("Automedon in a phone.png", "automedon-iphone.webp", 1000),
]


def crop_alpha(im, pad=4):
    arr = np.array(im)
    ys, xs = np.where(arr[:, :, 3] > 8)
    if xs.size == 0:
        return im
    x0, x1 = int(xs.min()), int(xs.max())
    y0, y1 = int(ys.min()), int(ys.max())
    x0 = max(0, x0 - pad)
    y0 = max(0, y0 - pad)
    x1 = min(im.width - 1, x1 + pad)
    y1 = min(im.height - 1, y1 + pad)
    return im.crop((x0, y0, x1 + 1, y1 + 1))


for src_name, out_name, max_edge in jobs:
    src = src_dir / src_name
    print("processing", src_name)
    im = crop_alpha(Image.open(src).convert("RGBA"), pad=4)
    w, h = im.size
    scale = max_edge / max(w, h)
    if scale < 1:
        im = im.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
    out = out_dir / out_name
    im.save(out, "WEBP", quality=88, method=6)
    print("  size", im.size, "webp", round(out.stat().st_size / 1024), "KB")

print("done")
