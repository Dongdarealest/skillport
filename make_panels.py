#!/usr/bin/env python3
"""Before/after panels for SkillPort: ONE shared layout, two executions.
Same product (Fieldnotes), same brief, same slots in the same positions:
nav row, eyebrow, headline, sub, CTA row, three-feature row.
Only the craft differs. That is the whole point of the comparison.
"""
import os
from PIL import Image, ImageDraw, ImageFont

A = os.path.expanduser("~/workspace/skillport/assets")
FD = os.path.expanduser("~/workspace/github-profile-redo/fonts")
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANSB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SERIF = os.path.join(FD, "InstrumentSerif-Regular.ttf")
SERIFI = os.path.join(FD, "InstrumentSerif-Italic.ttf")
INTER = os.path.join(FD, "Inter.ttf")

W, H = 1200, 760
MX = 64            # side margin
NAV_Y = 40
EYEBROW_Y = 128
HEAD_Y = 168
SUB_Y = 316
CTA_Y = 396
FEAT_Y = 512       # top of the feature row zone
FEAT_H = 196

def F(p, s): return ImageFont.truetype(p, s)

def tracked(d, x, y, txt, font, fill, tr):
    for ch in txt:
        d.text((x, y), ch, font=font, fill=fill)
        x += d.textlength(ch, font=font) + tr
    return x

def wrap(d, txt, font, maxw):
    words, lines, cur = txt.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=font) <= maxw: cur = t
        else: lines.append(cur); cur = w_
    if cur: lines.append(cur)
    return lines

# ---------------------------------------------------------------- BEFORE
img = Image.new("RGB", (W, H), (244, 242, 251))
d = ImageDraw.Draw(img)
# purple to blue gradient hero zone
for x in range(W):
    t = x / W
    c = tuple(int((124 + (56 - 124) * t, 58 + (189 - 58) * t, 237 + (248 - 237) * t)[i]) for i in range(3))
    d.line([(x, 0), (x, 470)], fill=c)
d.rectangle([0, 470, W, H], fill=(238, 236, 250))

# nav row
d.text((MX, NAV_Y), "FIELDNOTES", font=F(SANSB, 21), fill=(255, 255, 255))
r = "Pricing · Sign in"; d.text((W - MX - d.textlength(r, font=F(SANS, 20)), NAV_Y + 1), r, font=F(SANS, 20), fill=(235, 235, 255))
# eyebrow (centered)
e = "INTRODUCING FIELDNOTES 2.0"
tw = sum(d.textlength(ch, font=F(SANSB, 19)) + 6 for ch in e) - 6
tracked(d, (W - tw) / 2, EYEBROW_Y, e, F(SANSB, 19), (255, 255, 255), 6)
# headline (centered, chunky)
for i, line in enumerate(["Unlock the Power of", "Seamless Note-Taking"]):
    fnt = F(SANSB, 62)
    d.text(((W - d.textlength(line, font=fnt)) / 2, HEAD_Y + i * 74), line, font=fnt, fill=(255, 255, 255))
# sub (centered)
for i, line in enumerate(wrap(d, "Leverage our robust, cutting-edge platform to elevate your workflow and delve into next-level productivity.", F(SANS, 23), 780)):
    d.text(((W - d.textlength(line, font=F(SANS, 23))) / 2, SUB_Y + i * 32), line, font=F(SANS, 23), fill=(232, 230, 255))
# CTA pills (centered pair)
b1, b2 = "Get Started Free", "Watch Demo"
f1 = F(SANSB, 21)
w1 = d.textlength(b1, font=f1) + 56; w2 = d.textlength(b2, font=f1) + 56
x = (W - w1 - 18 - w2) / 2
d.rounded_rectangle([x, CTA_Y, x + w1, CTA_Y + 54], 27, fill=(255, 255, 255))
d.text((x + 28, CTA_Y + 15), b1, font=f1, fill=(99, 62, 240))
x += w1 + 18
d.rounded_rectangle([x, CTA_Y, x + w2, CTA_Y + 54], 27, outline=(255, 255, 255), width=2)
d.text((x + 28, CTA_Y + 15), b2, font=f1, fill=(255, 255, 255))
# feature cards
cards = [("bolt", "Lightning Fast", "Blazing-fast performance that supercharges your entire workflow."),
         ("lock", "Secure and Robust", "Enterprise-grade security you can trust, built for peace of mind."),
         ("inf", "Scale Infinitely", "From personal notes to enterprise, our platform grows with you.")]
cw = (W - 2 * MX - 2 * 22) // 3
for i, (ic, t1, blurb) in enumerate(cards):
    x = MX + i * (cw + 22)
    d.rounded_rectangle([x, FEAT_Y, x + cw, FEAT_Y + FEAT_H], 18, fill=(255, 255, 255))
    d.rounded_rectangle([x + cw / 2 - 33, FEAT_Y + 26, x + cw / 2 + 33, FEAT_Y + 92], 16, fill=(124, 78, 245))
    cx = x + cw / 2
    if ic == "lock":
        d.arc([cx - 13, FEAT_Y + 38, cx + 13, FEAT_Y + 64], 180, 360, fill=(255, 255, 255), width=5)
        d.rounded_rectangle([cx - 17, FEAT_Y + 52, cx + 17, FEAT_Y + 78], 5, fill=(255, 255, 255))
        d.ellipse([cx - 3, FEAT_Y + 60, cx + 3, FEAT_Y + 66], fill=(124, 78, 245))
    else:
        glyph = "⚡" if ic == "bolt" else "∞"
        tw = d.textlength(glyph, font=F(SANS, 32)); d.text((cx - tw / 2, FEAT_Y + 40), glyph, font=F(SANS, 32), fill=(255, 255, 255))
    tw = d.textlength(t1, font=F(SANSB, 23)); d.text((x + cw / 2 - tw / 2, FEAT_Y + 108), t1, font=F(SANSB, 23), fill=(24, 22, 46))
    for j, line in enumerate(wrap(d, blurb, F(SANS, 15), cw - 36)):
        tw = d.textlength(line, font=F(SANS, 15)); d.text((x + cw / 2 - tw / 2, FEAT_Y + 142 + j * 21), line, font=F(SANS, 15), fill=(100, 98, 124))
img.save(os.path.join(A, "before.png"))

# ---------------------------------------------------------------- AFTER
# Same wireframe as BEFORE, coordinate for coordinate. Only the craft differs.
img = Image.new("RGB", (W, H), (251, 249, 244))
d = ImageDraw.Draw(img)
INK = (38, 34, 25); MUT = (109, 103, 90); GOLD = (169, 139, 79); HAIR = (227, 221, 207)
d.rectangle([0, 470, W, H], fill=(243, 239, 228))
# nav row
d.text((MX, NAV_Y), "FIELDNOTES", font=F(INTER, 21), fill=INK)
r = "Pricing · Sign in"; d.text((W - MX - d.textlength(r, font=F(INTER, 20)), NAV_Y + 1), r, font=F(INTER, 20), fill=MUT)
# eyebrow (centered, gold)
e = "FOR TEAMS OF THREE TO THIRTY"
tw = sum(d.textlength(ch, font=F(INTER, 18)) + 5 for ch in e) - 5
tracked(d, (W - tw) / 2, EYEBROW_Y, e, F(INTER, 18), GOLD, 5)
# headline (centered, serif)
for i, line in enumerate(["Notes that stay", "out of your way."]):
    fnt = F(SERIF, 72)
    d.text(((W - d.textlength(line, font=fnt)) / 2, HEAD_Y + i * 80), line, font=fnt, fill=INK)
# sub (centered)
for i, line in enumerate(wrap(d, "One quiet place for your team's writing. No feeds, no badges, no AI summaries nobody asked for.", F(INTER, 23), 780)):
    d.text(((W - d.textlength(line, font=F(INTER, 23))) / 2, SUB_Y + i * 32), line, font=F(INTER, 23), fill=(76, 70, 56))
# CTA pair (centered): dark pill + quiet text link, same slots as BEFORE
b1 = "Start free"; f1 = F(INTER, 21)
w1 = d.textlength(b1, font=f1) + 56
b2 = "14 days, no card"; w2 = d.textlength(b2, font=f1)
x = (W - w1 - 18 - w2) / 2
d.rounded_rectangle([x, CTA_Y, x + w1, CTA_Y + 54], 27, fill=INK)
d.text((x + 28, CTA_Y + 15), b1, font=f1, fill=(251, 249, 244))
d.text((x + w1 + 18, CTA_Y + 15), b2, font=f1, fill=MUT)
# feature cards: same geometry as BEFORE, paper cards with outline icons
feats = [("search", "Instant search", "Any note, found as you type. No folders to keep tidy."),
         ("lock", "Private by default", "Your writing stays yours. Export everything, anytime."),
         ("moon", "Quiet by design", "Nothing competes for your attention. It just holds notes.")]
cw = (W - 2 * MX - 2 * 22) // 3
for i, (ic, t1, blurb) in enumerate(feats):
    x = MX + i * (cw + 22)
    d.rounded_rectangle([x + 3, FEAT_Y + 4, x + cw + 3, FEAT_Y + FEAT_H + 4], 18, fill=(232, 226, 208))
    d.rounded_rectangle([x, FEAT_Y, x + cw, FEAT_Y + FEAT_H], 18, fill=(255, 255, 255), outline=HAIR, width=2)
    cx = x + cw / 2
    d.ellipse([cx - 33, FEAT_Y + 26, cx + 33, FEAT_Y + 92], outline=GOLD, width=2)
    if ic == "search":
        d.ellipse([cx - 11, FEAT_Y + 48, cx + 7, FEAT_Y + 66], outline=INK, width=3)
        d.line([(cx + 5, FEAT_Y + 64), (cx + 15, FEAT_Y + 74)], fill=INK, width=3)
    elif ic == "lock":
        d.arc([cx - 10, FEAT_Y + 44, cx + 10, FEAT_Y + 64], 180, 360, fill=INK, width=3)
        d.rounded_rectangle([cx - 13, FEAT_Y + 54, cx + 13, FEAT_Y + 76], 4, outline=INK, width=3)
        d.ellipse([cx - 2, FEAT_Y + 62, cx + 2, FEAT_Y + 66], fill=INK)
    else:
        d.ellipse([cx - 12, FEAT_Y + 47, cx + 12, FEAT_Y + 71], outline=INK, width=3)
        d.ellipse([cx - 4, FEAT_Y + 43, cx + 18, FEAT_Y + 67], fill=(255, 255, 255))
        d.ellipse([cx - 4, FEAT_Y + 43, cx + 18, FEAT_Y + 67], outline=INK, width=3)
    tw = d.textlength(t1, font=F(INTER, 22)); d.text((cx - tw / 2, FEAT_Y + 108), t1, font=F(INTER, 22), fill=INK)
    for j, line in enumerate(wrap(d, blurb, F(INTER, 15), cw - 36)):
        tw = d.textlength(line, font=F(INTER, 15)); d.text((cx - tw / 2, FEAT_Y + 142 + j * 21), line, font=F(INTER, 15), fill=MUT)
img.save(os.path.join(A, "after.png"))

# combined
combo = Image.new("RGB", (W * 2 + 8, H), (10, 10, 10))
combo.paste(Image.open(os.path.join(A, "before.png")), (0, 0))
combo.paste(Image.open(os.path.join(A, "after.png")), (W + 8, 0))
combo.save(os.path.join(A, "before-after.png"))
print("panels rebuilt")
