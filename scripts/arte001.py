from PIL import Image, ImageDraw, ImageFont
import sys

W, H = 1080, 1350
F = "/usr/share/fonts/truetype/google-fonts/"
bold = lambda s: ImageFont.truetype(F + "Poppins-Bold.ttf", s)
reg = lambda s: ImageFont.truetype(F + "Poppins-Regular.ttf", s)

BG = (14, 27, 51)        # azul-lousa escuro
ACC = (255, 196, 0)      # amarelo
WHITE = (245, 245, 240)
MUTED = (160, 175, 200)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# quadriculado sutil de caderno
for x in range(0, W, 54):
    d.line([(x, 0), (x, H)], fill=(22, 38, 68), width=1)
for y in range(0, H, 54):
    d.line([(0, y), (W, y)], fill=(22, 38, 68), width=1)

# fórmulas decorativas
deco = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 44)
for txt, xy in [("x² + 2x + 1", (640, 120)), ("Δ = b² − 4ac", (70, 1080)),
                ("∫ x dx = x²/2 + C", (620, 1010)), ("aₙ = a₁ + (n−1)r", (60, 150))]:
    d.text(xy, txt, font=deco, fill=(40, 62, 100))

def center(text, y, font, fill):
    w = d.textlength(text, font=font)
    d.text(((W - w) / 2, y), text, font=font, fill=fill)

center("SIMPLIFICANDO", 380, bold(104), WHITE)
center("EXATAS", 495, bold(150), ACC)
d.rounded_rectangle([290, 700, 790, 708], 4, fill=ACC)
center("Matemática do Fundamental", 750, reg(48), WHITE)
center("à Faculdade, sem complicação", 812, reg(48), WHITE)
# três níveis
lv = bold(34)
tags = ["FUNDAMENTAL", "MÉDIO", "SUPERIOR"]
ws = [d.textlength(t, font=lv) + 52 for t in tags]
gap = 30
x = (W - sum(ws) - gap * (len(tags) - 1)) / 2
for t, w in zip(tags, ws):
    d.rounded_rectangle([x, 910, x + w, 972], 31, outline=ACC, width=3)
    d.text((x + 26, 918), t, font=lv, fill=ACC)
    x += w + gap

d.rounded_rectangle([250, 1160, 830, 1250], 45, fill=ACC)
center("@simplificandoexatas02", 1178, bold(40), BG)

img.save(sys.argv[1], "JPEG", quality=92)
