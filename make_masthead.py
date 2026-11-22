#!/usr/bin/env python3
import os
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
A = os.path.expanduser("~/workspace/skillport/assets")
F = os.path.expanduser("~/workspace/github-profile-redo/fonts")
SERIF = os.path.join(F, "InstrumentSerif-Regular.ttf")
SERIFI = os.path.join(F, "InstrumentSerif-Italic.ttf")
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
def f(p, s): return ImageFont.truetype(p, s)
art = Image.open(os.path.join(A, "media-generation-skillport-banner-bg-0-023dc5ac-0dcc-47e6-af78-c2d48186778a.webp")).convert("RGB")
W, H = 2240, 1040
art = art.crop((0, 40, W, 40 + H)).resize((W, H))
art = ImageEnhance.Brightness(art).enhance(0.82)
img = art.copy(); d = ImageDraw.Draw(img, "RGBA")
# soft dark veil in the middle for the lockup
for y in range(240, 820):
    d.line([(0, y), (W, y)], fill=(8, 10, 14, 66))
def tracked(y, txt, font, fill, tr):
    total = sum(d.textlength(c, font=font) + tr for c in txt) - tr
    x = (W - total) / 2
    for c in txt:
        d.text((x, y), c, font=font, fill=fill); x += d.textlength(c, font=font) + tr
def centered(y, txt, font, fill):
    w = d.textlength(txt, font=font); d.text(((W - w) / 2, y), txt, font=font, fill=fill)
tracked(268, "A SKILL STORE FOR EVERY AI", f(SANS, 30), (201, 163, 95), 10)
d.line([(W/2 - 46, 348), (W/2 + 46, 348)], fill=(201, 163, 95), width=3)
centered(392, "SkillPort", f(SERIF, 235), (243, 240, 233))
centered(668, "Your AI is running bare. Give it skills.", f(SERIFI, 62), (216, 188, 128))
tracked(806, "CLAUDE · MUSE · CURSOR · CODEX · CHATGPT", f(SANS, 26), (196, 190, 178), 6)
img.save(os.path.join(A, "masthead.png"))
print("masthead.png", img.size)
