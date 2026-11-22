from PIL import Image, ImageDraw, ImageFont
import os
A = os.path.expanduser("~/workspace/skillport/assets")
F = os.path.expanduser("~/workspace/github-profile-redo/fonts")
SERIF = f"{F}/InstrumentSerif-Regular.ttf"; SERIFI = f"{F}/InstrumentSerif-Italic.ttf"; INTER = f"{F}/Inter.ttf"
def f(path, size, weight=None):
    ft = ImageFont.truetype(path, size)
    if weight:
        try: ft.set_variation_by_axes([weight])
        except Exception: pass
    return ft
def tracked(d, xy, txt, font, fill, tr):
    x, y = xy
    for ch in txt:
        d.text((x, y), ch, font=font, fill=fill); x += d.textlength(ch, font=font) + tr

# BANNER
bg = Image.open(f"{A}/media-generation-skillport-banner-bg-0-023dc5ac-0dcc-47e6-af78-c2d48186778a.webp").convert("RGB")
W, H = bg.size; d = ImageDraw.Draw(bg)
tracked(d, (110, 96), "SKILLPORT", f(INTER, 34, 700), (201, 163, 95), 14)
d.text((106, 210), "Your AI is", font=f(SERIF, 150), fill=(243, 240, 233))
d.text((106, 372), "running bare.", font=f(SERIF, 150), fill=(243, 240, 233))
d.text((110, 580), "Give it skills.", font=f(SERIFI, 84), fill=(201, 163, 95))
tracked(d, (110, H - 92), "SKILL PACKS FOR CLAUDE · MUSE · CURSOR · CODEX · CHATGPT", f(INTER, 25, 600), (196, 192, 182), 4)
bg.save(f"{A}/banner.png")
bg.resize((1280, 640)).save(f"{A}/social.png")

# AFTER v2: product-led, warm charcoal
W2, H2 = 1200, 760
img = Image.new("RGB", (W2, H2), (22, 20, 17)); d = ImageDraw.Draw(img, "RGBA")
INK = (243, 240, 233); MUT = (168, 162, 150); GOLD = (201, 163, 95)
d.text((64, 58), "FIELDNOTES", font=f(INTER, 21, 700), fill=INK)
t = "Pricing · Sign in"; d.text((W2 - 64 - d.textlength(t, font=f(INTER, 19)), 60), t, font=f(INTER, 19), fill=MUT)
d.line([(64, 108), (W2 - 64, 108)], fill=(58, 54, 47), width=2)
d.text((64, 150), "FOR TEAMS OF THREE TO THIRTY", font=f(INTER, 17, 600), fill=GOLD)
d.text((62, 190), "Notes that stay", font=f(SERIF, 76), fill=INK)
d.text((62, 272), "out of your way.", font=f(SERIFI, 76), fill=INK)
d.text((64, 386), "One quiet place for your team's writing.", font=f(INTER, 21), fill=(206, 201, 190))
d.text((64, 418), "No feeds, no badges, no AI summaries", font=f(INTER, 21), fill=(206, 201, 190))
d.text((64, 450), "nobody asked for.", font=f(INTER, 21), fill=(206, 201, 190))
d.rectangle([(64, 510), (64 + 208, 510 + 56)], fill=GOLD)
t = "Start free"; d.text((64 + (208 - d.textlength(t, font=f(INTER, 20, 700))) / 2, 510 + 16), t, font=f(INTER, 20, 700), fill=(22, 20, 17))
d.text((292, 530), "14 days, no card", font=f(INTER, 18), fill=MUT)
d.text((64, 640), "4,100 teams switched this spring.", font=f(SERIFI, 25), fill=(206, 201, 190))
# app window mock, right side
wx, wy, ww, wh = 620, 150, 516, 470
d.rounded_rectangle([(wx, wy), (wx + ww, wy + wh)], 14, fill=(245, 242, 234))
d.rounded_rectangle([(wx, wy), (wx + ww, wy + 44)], 14, fill=(233, 228, 216))
d.rectangle([(wx, wy + 30), (wx + ww, wy + 44)], fill=(233, 228, 216))
for i, c in enumerate([(196, 90, 80), (216, 178, 90), (120, 170, 110)]):
    d.ellipse([(wx + 18 + i * 26, wy + 15), (wx + 32 + i * 26, wy + 29)], fill=c)
d.text((wx + 108, wy + 12), "Fieldnotes · Spring launch", font=f(INTER, 16, 600), fill=(90, 86, 78))
d.rectangle([(wx, wy + 44), (wx + 168, wy + wh)], fill=(238, 234, 224))
notes = [("Launch plan", True), ("Pricing notes", False), ("Hiring: designer", False), ("User interviews", False), ("Roadmap Q3", False)]
for i, (n, act) in enumerate(notes):
    y = wy + 68 + i * 52
    if act: d.rounded_rectangle([(wx + 10, y - 6), (wx + 158, y + 34)], 8, fill=(255, 255, 255), outline=(201, 163, 95), width=2)
    d.text((wx + 20, y + 2), n, font=f(INTER, 16, 600 if act else 400), fill=(30, 29, 26) if act else (110, 106, 98))
ex = wx + 196
d.text((ex, wy + 66), "Launch plan", font=f(SERIF, 30), fill=(24, 23, 21))
lines = [(430, (176, 171, 158)), (398, (176, 171, 158)), (430, (176, 171, 158)), (300, (201, 163, 95)), (430, (176, 171, 158)), (368, (176, 171, 158))]
for i, (wln, col) in enumerate(lines):
    y = wy + 122 + i * 34
    d.rounded_rectangle([(ex, y), (ex + wln - 76, y + 13)], 6, fill=col)
d.text((ex, wy + 348), "Ship the quiet version first.", font=f(SERIFI, 22), fill=(90, 86, 78))
img.save(f"{A}/after.png")
combo = Image.new("RGB", (1200 * 2 + 36, 760 + 64), (16, 16, 18)); cd = ImageDraw.Draw(combo)
combo.paste(Image.open(f"{A}/before.png"), (0, 64)); combo.paste(img, (1236, 64))
cd.text((24, 18), "BEFORE · BARE AI", font=f(INTER, 24, 700), fill=(240, 238, 232))
t = "AFTER · WITH SKILLPORT"; cd.text((2436 - 24 - cd.textlength(t, font=f(INTER, 24, 700)), 18), t, font=f(INTER, 24, 700), fill=(201, 163, 95))
combo.save(f"{A}/before-after.png")
print("banner + after v2 ok")
