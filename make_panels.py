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
img = Image.new("RGB", (W, H), (20, 18, 14))
d = ImageDraw.Draw(img)
CREAM = (242, 238, 228); MUT = (168, 160, 144); GOLD = (201, 163, 95); HAIR = (62, 57, 47)
# nav row
d.text((MX, NAV_Y), "FIELDNOTES", font=F(INTER, 21), fill=CREAM)
r = "Pricing · Sign in"; d.text((W - MX - d.textlength(r, font=F(INTER, 20)), NAV_Y + 1), r, font=F(INTER, 20), fill=MUT)
d.line([(MX, 92), (W - MX, 92)], fill=HAIR)
# eyebrow (left, gold, tracked)
tracked(d, MX, EYEBROW_Y, "FOR TEAMS OF THREE TO THIRTY", F(INTER, 17), GOLD, 4)
# headline (serif, left)
for i, line in enumerate(["Notes that stay", "out of your way."]):
    d.text((MX, HEAD_Y + i * 74), line, font=F(SERIF, 66), fill=CREAM)
# sub (left)
for i, line in enumerate(wrap(d, "One quiet place for your team's writing. No feeds, no badges, no AI summaries nobody asked for.", F(INTER, 23), 780)):
    d.text((MX, SUB_Y + i * 32), line, font=F(INTER, 23), fill=(203, 196, 178))
# CTA row
b = "Start free"; f1 = F(INTER, 21)
w1 = d.textlength(b, font=f1) + 52
d.rectangle([MX, CTA_Y, MX + w1, CTA_Y + 54], fill=GOLD)
d.text((MX + 26, CTA_Y + 15), b, font=f1, fill=(24, 21, 15))
d.text((MX + w1 + 20, CTA_Y + 17), "14 days, no card", font=F(INTER, 19), fill=MUT)
# feature row: three quiet columns, hairline on top, no boxes
d.line([(MX, FEAT_Y), (W - MX, FEAT_Y)], fill=HAIR)
feats = [("Instant search", "Any note, found as you type. No folders to keep tidy."),
         ("Private by default", "Your writing stays yours. Export everything, anytime."),
         ("Quiet by design", "Nothing competes for your attention. It just holds notes.")]
cw = (W - 2 * MX - 2 * 22) // 3
for i, (t1, blurb) in enumerate(feats):
    x = MX + i * (cw + 22)
    d.text((x, FEAT_Y + 26), t1, font=F(INTER, 22), fill=CREAM)
    for j, line in enumerate(wrap(d, blurb, F(INTER, 16), cw - 30)):
        d.text((x, FEAT_Y + 62 + j * 23), line, font=F(INTER, 16), fill=MUT)
d.text((MX, H - 44), "4,100 teams switched this spring.", font=F(SERIFI, 19), fill=MUT)
img.save(os.path.join(A, "after.png"))

# combined
combo = Image.new("RGB", (W * 2 + 8, H), (10, 10, 10))
combo.paste(Image.open(os.path.join(A, "before.png")), (0, 0))
combo.paste(Image.open(os.path.join(A, "after.png")), (W + 8, 0))
combo.save(os.path.join(A, "before-after.png"))
print("panels rebuilt")
