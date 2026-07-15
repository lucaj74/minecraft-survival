# -*- coding: utf-8 -*-
# Genera og.html (anteprima social). Poi va renderizzato in PNG 1200x630 con Chrome headless:
#   python3 _assets-src/og_make.py
#   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu \
#       --window-size=1200,630 --force-device-scale-factor=1 --screenshot=og-image.png \
#       --virtual-time-budget=5000 "file://$(pwd)/_assets-src/og.html"
# (l'og-image.png va nella ROOT del progetto)
import os
HERE = os.path.dirname(os.path.abspath(__file__))

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
rects = "".join(
    f'<rect x="{x}" y="{y}" width="1" height="1"/>'
    for y, row in enumerate(grid) for x, ch in enumerate(row) if ch == "#"
)

html = f'''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Silkscreen:wght@400;700&display=swap" rel="stylesheet">
<style>
  * {{ margin:0; box-sizing:border-box; }}
  body {{ font-family:'Silkscreen','Courier New',monospace; }}
  .card {{ width:1200px; height:630px; background:linear-gradient(180deg,#1A1A2E 0%,#16213E 100%);
    border-bottom:16px solid #5D8C3E; display:flex; flex-direction:column;
    align-items:center; justify-content:center; gap:30px; padding:48px; text-align:center; }}
  .badge {{ width:200px; height:200px; background:#5D8C3E; border-radius:26px;
    display:flex; align-items:center; justify-content:center; box-shadow:0 12px 34px rgba(0,0,0,.4); }}
  .title {{ color:#7CB454; font-size:66px; font-weight:700; line-height:1.08; letter-spacing:2px; text-shadow:4px 4px 0 #000; }}
  .sub {{ color:#87CEEB; font-size:27px; max-width:900px; line-height:1.4; }}
  .dom {{ color:#FFD700; font-size:26px; letter-spacing:3px; }}
</style></head>
<body>
  <div class="card">
    <div class="badge">
      <svg width="150" height="150" viewBox="0 0 16 16" shape-rendering="crispEdges"><g fill="#ffffff">{rects}</g></svg>
    </div>
    <div class="title">MINECRAFT SURVIVAL<br>COMPANION</div>
    <div class="sub">Missioni giornaliere e ricette di crafting per le tue avventure in Survival</div>
    <div class="dom">minecraftsurvival.it</div>
  </div>
</body></html>'''

open(os.path.join(HERE, "og.html"), "w", encoding="utf-8").write(html)
print("og.html scritto in _assets-src/ (ora renderizzalo con Chrome, vedi commento in cima)")
