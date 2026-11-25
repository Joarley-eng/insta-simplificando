"""Gera as 7 artes da semana 1 do @simplificandoexatas02 (1080x1350 JPEG)."""
from PIL import Image, ImageDraw, ImageFont
import os, sys

OUT = sys.argv[1]
W, H = 1080, 1350
G = "/usr/share/fonts/truetype/google-fonts/"
DJ = "/usr/share/fonts/truetype/dejavu/"
B = lambda s: ImageFont.truetype(G + "Poppins-Bold.ttf", s)
R = lambda s: ImageFont.truetype(G + "Poppins-Regular.ttf", s)
M = lambda s: ImageFont.truetype(DJ + "DejaVuSans.ttf", s)       # matemática
MB = lambda s: ImageFont.truetype(DJ + "DejaVuSans-Bold.ttf", s)

BG = (14, 27, 51); GRID = (22, 38, 68); ACC = (255, 196, 0)
WHITE = (245, 245, 240); MUTED = (150, 168, 198); CARD = (24, 42, 74)
GREEN = (80, 200, 120); RED = (240, 90, 90); BLUE = (90, 160, 255)
NIVEL = {"FUNDAMENTAL": (80, 200, 120), "MÉDIO": (90, 160, 255), "SUPERIOR": (200, 120, 255)}


def base(nivel, titulo):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    for x in range(0, W, 54):
        d.line([(x, 0), (x, H)], fill=GRID)
    for y in range(0, H, 54):
        d.line([(0, y), (W, y)], fill=GRID)
    c = NIVEL[nivel]
    f = B(30)
    w = d.textlength(nivel, font=f)
    d.rounded_rectangle([70, 70, 70 + w + 48, 126], 28, fill=c)
    d.text((94, 76), nivel, font=f, fill=BG)
    y = 160
    for linha in titulo.split("\n"):
        d.text((70, y), linha, font=B(64), fill=WHITE)
        y += 82
    d.rectangle([70, y + 14, 230, y + 22], fill=ACC)
    # rodapé
    d.line([(70, 1240), (1010, 1240)], fill=CARD, width=2)
    d.text((70, 1262), "SIMPLIFICANDO EXATAS", font=B(30), fill=ACC)
    h = "@simplificandoexatas02"
    d.text((1010 - d.textlength(h, font=R(30)), 1262), h, font=R(30), fill=MUTED)
    return img, d, y + 60


def ctext(d, text, y, font, fill, cx=W / 2):
    d.text((cx - d.textlength(text, font=font) / 2, y), text, font=font, fill=fill)


def card(d, box):
    d.rounded_rectangle(box, 28, fill=CARD)


def save(img, nome):
    img.save(os.path.join(OUT, nome), "JPEG", quality=92)


# 002 — MÉDIO — Função afim
def p002():
    img, d, y = base("MÉDIO", "Função afim\nem 1 imagem")
    card(d, [70, y, 1010, y + 150])
    ctext(d, "f(x) = a·x + b", y + 35, MB(72), ACC)
    # gráfico
    ox, oy, s = 300, 1010, 70
    d.line([(110, oy), (560, oy)], fill=MUTED, width=3)
    d.line([(ox, 1170 - 0), (ox, 620)], fill=MUTED, width=3)
    d.text((570, oy - 22), "x", font=M(36), fill=MUTED)
    d.text((ox - 12, 570), "y", font=M(36), fill=MUTED)
    # reta y = 2x + 1  (de x=-2 a x=2)
    p = lambda x, yy: (ox + x * s, oy - yy * s)
    d.line([p(-1.6, -2.2), p(2.4, 5.8)], fill=ACC, width=7)
    bx, by = p(0, 1)
    d.ellipse([bx - 13, by - 13, bx + 13, by + 13], fill=GREEN)
    # degrau da inclinação
    d.line([p(1, 3), p(2, 3)], fill=BLUE, width=4)
    d.line([p(2, 3), p(2, 5)], fill=BLUE, width=4)
    d.text((p(1.2, 3)[0], p(1.2, 3)[1] + 6), "+1", font=MB(32), fill=BLUE)
    d.text((p(2, 4)[0] + 12, p(2, 4)[1] - 20), "+2", font=MB(32), fill=BLUE)
    # explicações
    x0 = 620
    d.text((x0, 640), "a = inclinação", font=B(40), fill=BLUE)
    d.text((x0, 692), "andou 1 pra direita,", font=R(32), fill=WHITE)
    d.text((x0, 734), "subiu a = 2", font=R(32), fill=WHITE)
    d.text((x0, 820), "b = onde corta o y", font=B(40), fill=GREEN)
    d.text((x0, 872), "x = 0  →  y = b = 1", font=M(32), fill=WHITE)
    d.text((x0, 960), "a > 0: sobe ↗", font=M(34), fill=WHITE)
    d.text((x0, 1008), "a < 0: desce ↘", font=M(34), fill=WHITE)
    d.text((x0, 1056), "a = 0: reta deitada", font=M(34), fill=WHITE)
    ctext(d, "Exemplo do gráfico: f(x) = 2x + 1", 1170, R(34), MUTED)
    save(img, "002-funcao-afim.jpg")


# 003 — FUNDAMENTAL — Divisão de frações
def p003():
    img, d, y = base("FUNDAMENTAL", "Divisão de frações\nsem decorar nada")
    card(d, [70, y, 1010, y + 130])
    ctext(d, "Mantém a 1ª, inverte a 2ª e multiplica", y + 40, B(40), ACC)

    def frac(cx, top, n, dd, cor=WHITE, f=MB(96)):
        ctext(d, n, top, f, cor, cx)
        d.line([(cx - 60, top + 122), (cx + 60, top + 122)], fill=cor, width=6)
        ctext(d, dd, top + 132, f, cor, cx)

    t = y + 170
    frac(200, t, "3", "4"); ctext(d, "÷", t + 60, MB(90), MUTED, 360)
    frac(520, t, "2", "5")
    ctext(d, "=", t + 60, MB(90), MUTED, 680)
    frac(840, t, "?", "", ACC)
    t2 = t + 290
    frac(200, t2, "3", "4"); ctext(d, "×", t2 + 60, MB(90), ACC, 360)
    frac(520, t2, "5", "2", ACC)
    ctext(d, "=", t2 + 60, MB(90), MUTED, 680)
    frac(840, t2, "15", "8", GREEN)
    ctext(d, "↑ invertida", t2 + 262, M(32), ACC, 520)
    ctext(d, "3 × 5 = 15   e   4 × 2 = 8", 1170, M(38), MUTED)
    save(img, "003-divisao-fracoes.jpg")


# 004 — SUPERIOR — Regra da potência (derivada)
def p004():
    img, d, y = base("SUPERIOR", "Derivada: a\nregra da potência")
    card(d, [70, y, 1010, y + 170])
    ctext(d, "d/dx (xⁿ) = n · xⁿ⁻¹", y + 45, MB(76), ACC)
    ctext(d, "o expoente desce multiplicando e diminui 1", y + 200, R(36), WHITE)
    rows = [("x³", "3x²"), ("5x²", "5 · 2x = 10x"), ("x", "1"), ("7", "0  (constante)")]
    ty = y + 290
    for f, df in rows:
        card(d, [70, ty, 1010, ty + 120])
        d.text((120, ty + 30), "(" + f + ")'", font=MB(54), fill=WHITE)
        d.text((420, ty + 30), "=", font=MB(54), fill=MUTED)
        d.text((500, ty + 30), df, font=MB(54), fill=GREEN)
        ty += 145
    save(img, "004-regra-potencia.jpg")


# 005 — MÉDIO — Desafio PA
def p005():
    img, d, y = base("MÉDIO", "Desafio rápido:\nprogressão aritmética")
    card(d, [70, y, 1010, y + 200])
    ctext(d, "3,  7,  11,  15,  ...", y + 55, MB(80), WHITE)
    ctext(d, "Qual é o 20º termo?", y + 270, B(64), ACC)
    opts = ["A) 76", "B) 79", "C) 80", "D) 83"]
    for i, o in enumerate(opts):
        cx = 70 + (i % 2) * 480
        cy = y + 400 + (i // 2) * 150
        card(d, [cx, cy, cx + 460, cy + 120])
        ctext(d, o, cy + 28, B(54), WHITE, cx + 230)
    ctext(d, "Dica: aₙ = a₁ + (n − 1)·r", 1130, M(40), MUTED)
    ctext(d, "Responda nos comentários 👇".replace(" 👇", ""), 1180, R(34), MUTED)
    save(img, "005-desafio-pa.jpg")


# 006 — FUNDAMENTAL — Regra de sinais
def p006():
    img, d, y = base("FUNDAMENTAL", "Regra de sinais\nna multiplicação")
    ty = y + 10
    linhas = [("(+) × (+)", "+", GREEN), ("(−) × (−)", "+", GREEN),
              ("(+) × (−)", "−", RED), ("(−) × (+)", "−", RED)]
    for a, r, c in linhas:
        card(d, [70, ty, 1010, ty + 130])
        d.text((130, ty + 28), a, font=MB(66), fill=WHITE)
        d.text((560, ty + 28), "=", font=MB(66), fill=MUTED)
        d.ellipse([700, ty + 18, 794, ty + 112], fill=c)
        ctext(d, r, ty + 14, MB(76), BG, 747)
        ty += 155
    ctext(d, "Sinais iguais: positivo", ty + 20, B(44), GREEN)
    ctext(d, "Sinais diferentes: negativo", ty + 80, B(44), RED)
    ctext(d, "Ex.: (−4) × (−3) = 12    (−4) × 3 = −12", 1160, M(36), MUTED)
    save(img, "006-regra-sinais.jpg")


# 007 — MÉDIO — Tabela dos ângulos notáveis
def p007():
    img, d, y = base("MÉDIO", "Ângulos notáveis:\nsalve essa tabela")
    cols = ["", "30°", "45°", "60°"]
    data = [("sen", "1/2", "√2/2", "√3/2"), ("cos", "√3/2", "√2/2", "1/2"), ("tg", "√3/3", "1", "√3")]
    x0, cw, rh = 70, 235, 150
    ty = y + 20
    for j, c in enumerate(cols):
        if c:
            card(d, [x0 + j * cw + 8, ty, x0 + (j + 1) * cw - 8, ty + 110])
            ctext(d, c, ty + 22, MB(56), ACC, x0 + j * cw + cw / 2)
    ty += 130
    for name, *vals in data:
        card(d, [x0 + 8, ty, x0 + cw - 8, ty + rh - 20])
        ctext(d, name, ty + 35, B(50), BLUE, x0 + cw / 2)
        for j, v in enumerate(vals, 1):
            ctext(d, v, ty + 35, MB(54), WHITE, x0 + j * cw + cw / 2)
        ty += rh
    ctext(d, "Truque: no sen, os numeradores sobem 1, 2, 3", ty + 30, R(34), MUTED)
    ctext(d, "(√1/2, √2/2, √3/2) e no cos é o contrário", ty + 76, R(34), MUTED)
    save(img, "007-angulos-notaveis.jpg")


# 008 — SUPERIOR — Integral como área
def p008():
    img, d, y = base("SUPERIOR", "Integral definida\né área")
    card(d, [70, y, 1010, y + 150])
    ctext(d, "∫₀² x dx = ?", y + 35, MB(76), ACC)
    ox, oy, s = 160, 1080, 170
    p = lambda x, yy: (ox + x * s, oy - yy * s)
    d.polygon([p(0, 0), p(2, 0), p(2, 2)], fill=(60, 90, 150))
    d.line([(120, oy), (620, oy)], fill=MUTED, width=3)
    d.line([(ox, 1120), (ox, 640)], fill=MUTED, width=3)
    d.line([p(0, 0), p(2.5, 2.5)], fill=ACC, width=6)
    d.text((p(2.5, 2.5)[0] - 60, p(2.5, 2.5)[1] - 50), "y = x", font=MB(36), fill=ACC)
    d.text((p(2, 0)[0] - 10, oy + 10), "2", font=M(36), fill=WHITE)
    d.text((ox - 40, p(0, 2)[1] - 20), "2", font=M(36), fill=WHITE)
    d.line([p(0, 2), p(2, 2)], fill=MUTED, width=2)
    x0 = 650
    d.text((x0, 660), "Pela geometria:", font=B(38), fill=WHITE)
    d.text((x0, 714), "triângulo", font=R(34), fill=MUTED)
    d.text((x0, 760), "(2 × 2) / 2 = 2", font=M(38), fill=WHITE)
    d.text((x0, 860), "Pelo cálculo:", font=B(38), fill=WHITE)
    d.text((x0, 914), "[x²/2] de 0 a 2", font=M(36), fill=MUTED)
    d.text((x0, 960), "4/2 − 0 = 2", font=M(38), fill=WHITE)
    card(d, [x0 - 10, 1040, 1010, 1130])
    ctext(d, "Resposta: 2", 1060, B(44), GREEN, (x0 - 10 + 1010) / 2)
    save(img, "008-integral-area.jpg")


for f in (p002, p003, p004, p005, p006, p007, p008):
    f()
print("ok")
