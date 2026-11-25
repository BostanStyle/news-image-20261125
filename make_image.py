#!/usr/bin/env python3
"""Build the 25 Nov 2026 world-news image (1024x1024 PNG).
Drawn with PIL so every word is exactly as written - no AI text artefacts.
Stories verified from 25 Nov 2026 reporting (SCMP, Economic Times, Japan Times, Manila Times).
"""
from PIL import Image, ImageDraw, ImageFont
import textwrap, os

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(__file__), "entry.png")

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

NAVY = (15, 42, 68)
NAVY2 = (21, 58, 92)
GREY = (90, 96, 104)
LIGHT = (240, 242, 245)
INK = (20, 24, 30)

# Header
d.rectangle([0, 0, W, 168], fill=NAVY)
d.text((32, 22), "WORLD NEWS", font=font(BOLD, 62), fill="white")
d.text((32, 96), "Wednesday, 25 November 2026", font=font(BOLD, 34), fill=(255, 214, 90))
d.text((32, 136), "Six stories that defined the day", font=font(REG, 22), fill=(200, 214, 228))

# Sub-strip
d.rectangle([0, 168, W, 206], fill=LIGHT)
d.text((32, 177), "MIDDLE EAST  •  UNITED STATES  •  CHINA  •  TECHNOLOGY  •  BUSINESS  •  SPACE",
       font=font(BOLD, 18), fill=GREY)

stories = [
    ("MIDDLE EAST  —  RIYADH", (178, 34, 34),
     "Riyadh tower hit again",
     "Houthis strike the Saudi capital's tallest skyscraper for a second time in under a week. 11 people injured."),
    ("MIDDLE EAST  —  GAZA", (178, 34, 34),
     "Hamas security chief killed",
     "An Israeli air strike on Gaza City kills a Hamas security chief, reports say."),
    ("CHINA  —  SPACE", (16, 92, 140),
     "Shenzhou-24 launches",
     "China launches Shenzhou-24, carrying the first Pakistani national to fly to space."),
    ("UNITED STATES  —  TECH", (16, 92, 140),
     "Huawei convicted",
     "A US jury convicts Huawei of stealing trade secrets in a sprawling trial over its Iran business."),
    ("BUSINESS", (24, 110, 60),
     "Shein to pay $100 million",
     "Shein agrees to pay $100 million to settle US trade allegations over deceptive practices."),
    ("UNITED STATES  —  TECH", (24, 110, 60),
     "Nvidia chief in the spotlight",
     "Jensen Huang says he is in therapy as Nvidia's rally fades. Trump says a pardon is 'always an option'."),
]

# Grid: 2 cols x 3 rows
margin, gap = 32, 16
card_w = (W - 2*margin - gap) // 2
card_h = 232
top = 218
for i, (tag, color, headline, body) in enumerate(stories):
    x = margin + (i % 2) * (card_w + gap)
    y = top + (i // 2) * (card_h + gap)
    # card
    d.rounded_rectangle([x, y, x+card_w, y+card_h], radius=12, outline=(210, 216, 222), width=2, fill="white")
    d.rectangle([x, y, x+card_w, y+8], fill=color)
    d.text((x+18, y+22), tag, font=font(BOLD, 17), fill=color)
    # headline, wrapped to 2 lines max
    hl_lines = textwrap.wrap(headline, width=24)
    yy = y + 52
    for line in hl_lines[:2]:
        d.text((x+18, yy), line, font=font(BOLD, 27), fill=INK)
        yy += 32
    # body, wrapped
    body_lines = textwrap.wrap(body, width=38)
    yy = y + 122
    for line in body_lines[:4]:
        d.text((x+18, yy), line, font=font(REG, 21), fill=(55, 62, 70))
        yy += 27

# Footer
fy = top + 3*card_h + 2*gap + 8
d.text((32, fy), "All events happened, or were first reported, on 25 November 2026.",
       font=font(REG, 19), fill=GREY)
d.text((32, fy+28), "Sources: world news reporting from 25 November 2026.",
       font=font(REG, 19), fill=GREY)

img.save(OUT, "PNG", optimize=True)
print(f"saved {OUT} {img.size} {os.path.getsize(OUT)} bytes")
