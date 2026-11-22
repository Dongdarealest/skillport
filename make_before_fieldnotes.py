#!/usr/bin/env python3
"""BEFORE redone: same product as AFTER (Fieldnotes), bare-AI execution. PIL only."""
import os
from PIL import Image, ImageDraw, ImageFont
A = os.path.expanduser("~/workspace/skillport/assets")
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANSB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def f(p, s): return ImageFont.truetype(p, s)
W, H = 1200, 760
img = Image.new("RGB", (W, H), (238, 240, 255))
d = ImageDraw.Draw(img)
# gradient hero
for x in range(W):
    t = x / W
    r = int(123 + (76 - 123) * t); g = int(47 + (201 - 47) * t); b = int(247 + (240 - 247) * t)
    d.line([(x, 0), (x, 470)], fill=(r, g, b))
def center(y, txt, font, fill):
    w = d.textlength(txt, font=font); d.text(((W - w) / 2, y), txt, font=font, fill=fill)
center(52, "I N T R O D U C I N G   F I E L D N O T E S   2 . 0", f(SANSB, 17), (255, 255, 255))
center(96, "Unlock the Power of", f(SANSB, 58), (255, 255, 255))
center(162, "Seamless Note-Taking", f(SANSB, 58), (255, 255, 255))
center(248, "Leverage our robust, cutting-edge platform to elevate", f(SANS, 22), (240, 240, 255))
center(280, "your workflow and delve into next-level productivity.", f(SANS, 22), (240, 240, 255))
d.rounded_rectangle([330, 336, 590, 396], 30, fill=(255, 255, 255))
d.text((362, 354), "Get Started Free", font=f(SANSB, 21), fill=(90, 61, 240))
d.rounded_rectangle([622, 336, 872, 396], 30, outline=(255, 255, 255), width=3)
d.text((676, 354), "Watch Demo", font=f(SANSB, 21), fill=(255, 255, 255))
# cards
cards = [("⚡", "Lightning Fast", "Blazing-fast performance that", "supercharges your entire workflow."),
         ("🔒", "Secure and Robust", "Enterprise-grade security you", "can trust, built for peace of mind."),
         ("📈", "Scale Infinitely", "From personal notes to enterprise,", "our platform grows with you.")]
for i, (ic, t1, l1, l2) in enumerate(cards):
    x = 44 + i * 382
    d.rounded_rectangle([x, 500, x + 356, 716], 22, fill=(255, 255, 255))
    d.rounded_rectangle([x + 140, 522, x + 216, 598], 18, fill=(124, 93, 250))
    tw = d.textlength(ic, font=f(SANS, 34)); d.text((x + 178 - tw / 2, 540), ic, font=f(SANS, 34), fill=(255, 255, 255))
    tw = d.textlength(t1, font=f(SANSB, 23)); d.text((x + 178 - tw / 2, 616), t1, font=f(SANSB, 23), fill=(20, 20, 43))
    tw = d.textlength(l1, font=f(SANS, 16)); d.text((x + 178 - tw / 2, 656), l1, font=f(SANS, 16), fill=(92, 92, 116))
    tw = d.textlength(l2, font=f(SANS, 16)); d.text((x + 178 - tw / 2, 680), l2, font=f(SANS, 16), fill=(92, 92, 116))
img.save(os.path.join(A, "before.png"))
from PIL import Image as I
a = I.open(os.path.join(A, "after.png"))
combo = I.new("RGB", (W + a.width + 8, H), (20, 20, 20))
combo.paste(img, (0, 0)); combo.paste(a, (W + 8, 0))
combo.save(os.path.join(A, "before-after.png"))
print("before + combo rebuilt:", combo.size)
