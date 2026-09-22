# -*- coding: utf-8 -*-
"""Generate og-image.png (1200x630) and apple-touch-icon.png (180x180)."""
import math
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1200, 630
BG = (7, 8, 13)
INDIGO = (99, 102, 241)
CYAN = (34, 211, 238)
FG = (232, 234, 242)
MUTED = (154, 163, 181)

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

def gradient_text(draw_size, text, font, c1, c2):
    """Render text as an RGBA image filled with a horizontal gradient."""
    w, h = draw_size
    mask = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(mask)
    d.text((0, 0), text, font=font, fill=255)
    grad = Image.new("RGBA", (w, h))
    gd = ImageDraw.Draw(grad)
    for x in range(w):
        gd.line([(x, 0), (x, h)], fill=lerp(c1, c2, x / max(w - 1, 1)))
    out = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    out.paste(grad, (0, 0), mask)
    return out

# ---------- og-image ----------
img = Image.new("RGB", (W, H), BG)

# glow orbs (indigo top-right, cyan bottom-left)
orb = Image.new("RGB", (W, H), BG)
od = ImageDraw.Draw(orb)
od.ellipse([W - 620, -360, W + 260, 380], fill=(46, 52, 110))
od.ellipse([-420, H - 420, 380, H + 320], fill=(18, 76, 88))
orb = orb.filter(ImageFilter.GaussianBlur(120))
img = Image.blend(img, orb, 0.85)

d = ImageDraw.Draw(img)
# subtle grid
for x in range(0, W, 56):
    d.line([(x, 0), (x, H)], fill=(20, 22, 32))
for y in range(0, H, 56):
    d.line([(0, y), (W, y)], fill=(20, 22, 32))

f_mono_big = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 170)
f_sub = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", 38)

name_txt, name_font = "LYT.dev", f_mono_big
nb = name_font.getbbox(name_txt)
name_img = gradient_text((nb[2] - nb[0] + 8, nb[3] - nb[1] + 8), name_txt, name_font, INDIGO, CYAN)
img.paste(name_img, ((W - name_img.width) // 2, 150), name_img)

sub = "Full-Stack Developer & AI Product Engineer"
sb = d.textbbox((0, 0), sub, font=f_sub)
d.text(((W - (sb[2] - sb[0])) // 2, 400), sub, font=f_sub, fill=MUTED)

# gradient underline
bar_h = 6
for x in range(0, 260):
    d.line([(W // 2 - 130 + x, 480), (W // 2 - 130 + x, 480 + bar_h)],
           fill=lerp(INDIGO, CYAN, x / 259))

img.save("og-image.png", optimize=True)

# ---------- apple-touch-icon ----------
S = 180
icon = Image.new("RGBA", (S, S), (0, 0, 0, 0))
di = ImageDraw.Draw(icon)
for y in range(S):
    di.line([(0, y), (S, y)], fill=lerp(INDIGO, CYAN, (x := y) / (S - 1)))
f_icon = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 110)
tb = di.textbbox((0, 0), "L", font=f_icon)
tw, th = tb[2] - tb[0], tb[3] - tb[1]
di.text(((S - tw) / 2 - tb[0], (S - th) / 2 - tb[1] - tb[3] + th // 2), "L",
        font=f_icon, fill=(255, 255, 255, 255))
icon.save("apple-touch-icon.png")

print("og-image.png", img.size, "| apple-touch-icon.png", icon.size)
