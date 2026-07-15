# -*- coding: utf-8 -*-
# Genera favicon (SVG + PNG) con piccone bianco pixel-art su sfondo verde Minecraft.
# Uso:  python3 _assets-src/make_icons.py
# Scrive nella ROOT del progetto: favicon.svg, favicon-16/32.png, apple-touch-icon.png, icon-512.png
from PIL import Image, ImageDraw
import os

PROJ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GREEN = (93, 140, 62)      # #5D8C3E verde erba Minecraft
WHITE = (255, 255, 255)

# mappa 16x16 del piccone (# = bianco). Testa ad arco con punte in giù + manico centrale.
grid = [
"................",
".....######.....",
"...###.##.###...",
"..###..##..###..",
".###...##...###.",
".......##.......",
".......##.......",
".......##.......",
".......##.......",
".......##.......",
".......##.......",
".......##.......",
".......##.......",
".......##.......",
".......##.......",
"................",
]
N = 16

# --- SVG (vettoriale, crisp) ---
rects = []
for y, row in enumerate(grid):
    for x, ch in enumerate(row):
        if ch == "#":
            rects.append(f'<rect x="{x}" y="{y}" width="1" height="1"/>')
svg = (
'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" shape-rendering="crispEdges">\n'
'  <rect width="16" height="16" fill="#5D8C3E"/>\n'
'  <g fill="#ffffff">\n    ' + "\n    ".join(rects) + '\n  </g>\n'
'</svg>\n'
)
open(os.path.join(PROJ, "favicon.svg"), "w", encoding="utf-8").write(svg)

# --- PNG a varie dimensioni (pixel-perfect) ---
def render_png(size, path, pad=0):
    img = Image.new("RGBA", (size, size), GREEN + (255,))
    d = ImageDraw.Draw(img)
    inner = size - 2 * pad
    cell = inner / N
    for y, row in enumerate(grid):
        for x, ch in enumerate(row):
            if ch == "#":
                x0 = pad + x * cell; y0 = pad + y * cell
                d.rectangle([x0, y0, x0 + cell - 0.001, y0 + cell - 0.001], fill=WHITE)
    img.save(path)

render_png(16,  os.path.join(PROJ, "favicon-16.png"))
render_png(32,  os.path.join(PROJ, "favicon-32.png"))
render_png(180, os.path.join(PROJ, "apple-touch-icon.png"), pad=18)
render_png(512, os.path.join(PROJ, "icon-512.png"))
print("favicon.svg + PNG generati nella root del progetto")
