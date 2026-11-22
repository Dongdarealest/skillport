from PIL import Image, ImageDraw, ImageFont
import os
F = os.path.expanduser("~/workspace/github-profile-redo/fonts")
SERIF = os.path.join(F, "InstrumentSerif-Regular.ttf"); SERIFI = os.path.join(F, "InstrumentSerif-Italic.ttf"); INTER = os.path.join(F, "Inter.ttf")
def f(path, size, weight=None):
    ft = ImageFont.truetype(path, size)
    if weight:
        try: ft.set_variation_by_axes([weight])
        except Exception: pass
    return ft
W, H = 1200, 760

# BEFORE: AI slop
img = Image.new("RGB", (W, H), (24, 18, 48)); d = ImageDraw.Draw(img, "RGBA")
for y in range(H):
    t = y / H
    c = (int(38 + 60*t), int(24 + 10*t), int(92 + 70*t))
    d.line([(0, y), (W, y)], fill=c)
d.ellipse([820, -260, 1420, 340], fill=(124, 58, 237, 90))
d.ellipse([-260, 420, 320, 1000], fill=(59, 130, 246, 80))
def center(txt, y, font, fill, tracking=0):
    if tracking:
        x = (W - sum(d.textlength(ch, font=font) + tracking for ch in txt)) / 2
        for ch in txt:
            d.text((x, y), ch, font=font, fill=fill); x += d.textlength(ch, font=font) + tracking
    else:
        d.text(((W - d.textlength(txt, font=font)) / 2, y), txt, font=font, fill=fill)
center("INTRODUCING INNOVATEHUB 2.0", 84, f(INTER, 21, 600), (196, 181, 253), 3)
center("Unlock the Power of", 140, f(INTER, 66, 800), (255, 255, 255))
center("Seamless Innovation", 216, f(INTER, 66, 800), (196, 181, 253))
center("Leverage our robust, cutting-edge platform to elevate your workflow,", 316, f(INTER, 23, 400), (216, 208, 240))
center("streamline your journey, and delve into next-level productivity.", 350, f(INTER, 23, 400), (216, 208, 240))
bw, bh = 252, 62
d.rounded_rectangle([(W/2 - bw - 14, 424), (W/2 - 14, 424 + bh)], 31, fill=(139, 92, 246))
center("Get Started Free", 0, f(INTER, 1), (0,0,0))
t = "Get Started Free"; d.text((W/2 - bw - 14 + (bw - d.textlength(t, font=f(INTER, 22, 600)))/2, 424 + 18), t, font=f(INTER, 22, 600), fill=(255,255,255))
d.rounded_rectangle([(W/2 + 14, 424), (W/2 + 14 + bw, 424 + bh)], 31, outline=(196, 181, 253), width=2)
t = "Watch Demo"; d.text((W/2 + 14 + (bw - d.textlength(t, font=f(INTER, 22, 600)))/2, 424 + 18), t, font=f(INTER, 22, 600), fill=(230, 224, 250))
for i, (h1, s1) in enumerate([("Lightning Fast", "Blazing speed for your team"), ("Secure and Robust", "Enterprise-grade security"), ("Scale Infinitely", "Grow without any limits")]):
    x = 72 + i * 368
    d.rounded_rectangle([(x, 548), (x + 336, 700)], 20, fill=(255, 255, 255, 22), outline=(255, 255, 255, 46))
    d.text((x + 28, 578), h1, font=f(INTER, 25, 700), fill=(255, 255, 255))
    d.text((x + 28, 622), s1, font=f(INTER, 19, 400), fill=(205, 198, 232))
img.save(os.path.expanduser("~/workspace/skillport/assets/before.png"))

# AFTER: human touch
img = Image.new("RGB", (W, H), (245, 242, 234)); d = ImageDraw.Draw(img)
INK = (18, 18, 20); MUT = (96, 92, 84); GOLD = (169, 139, 79)
d.text((72, 62), "FIELDNOTES", font=f(INTER, 20, 700), fill=INK)
t = "Pricing · Sign in"; d.text((W - 72 - d.textlength(t, font=f(INTER, 19, 400)), 64), t, font=f(INTER, 19, 400), fill=MUT)
d.line([(72, 116), (W - 72, 116)], fill=(214, 208, 194), width=2)
d.text((72, 168), "FOR TEAMS OF THREE TO THIRTY", font=f(INTER, 18, 600), fill=GOLD)
d.text((70, 208), "Notes that stay", font=f(SERIF, 92), fill=INK)
d.text((70, 306), "out of your way.", font=f(SERIFI, 92), fill=INK)
d.text((72, 436), "Fieldnotes keeps your team's writing in one quiet place. No feeds, no badges,", font=f(INTER, 23, 400), fill=(58, 56, 52))
d.text((72, 470), "no AI summaries nobody asked for. 4,100 teams switched this spring.", font=f(INTER, 23, 400), fill=(58, 56, 52))
d.rectangle([(72, 540), (72 + 236, 540 + 60)], fill=INK)
t = "Start free"; d.text((72 + (236 - d.textlength(t, font=f(INTER, 21, 600)))/2, 540 + 18), t, font=f(INTER, 21, 600), fill=(245, 242, 234))
d.text((332, 560), "14 days, no card", font=f(INTER, 19, 400), fill=MUT)
d.line([(72, 668), (W - 72, 668)], fill=(214, 208, 194), width=2)
d.text((72, 688), "“We deleted three apps the week we adopted it.” · Marta K., studio lead, Porto", font=f(SERIFI, 24), fill=(58, 56, 52))
img.save(os.path.expanduser("~/workspace/skillport/assets/after.png"))

# combined
combo = Image.new("RGB", (W * 2 + 36, H + 64), (16, 16, 18)); cd = ImageDraw.Draw(combo)
b = Image.open(os.path.expanduser("~/workspace/skillport/assets/before.png")); a = Image.open(os.path.expanduser("~/workspace/skillport/assets/after.png"))
combo.paste(b, (0, 64)); combo.paste(a, (W + 36, 64))
cd.text((24, 18), "BEFORE · BARE AI", font=f(INTER, 24, 700), fill=(240, 238, 232))
t = "AFTER · WITH SKILLPORT"; cd.text((W * 2 + 36 - 24 - cd.textlength(t, font=f(INTER, 24, 700)), 18), t, font=f(INTER, 24, 700), fill=(201, 163, 95))
combo.save(os.path.expanduser("~/workspace/skillport/assets/before-after.png"))
print("demo images ok", combo.size)
