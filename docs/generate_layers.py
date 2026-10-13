#!/usr/bin/env python3
"""Genera los SVG de cada capa (docs/layers/*.svg) que usa el README.

Las capas se definen a mano abajo; si cambias config/corne.keymap, actualiza
LAYERS y volve a correr:  python docs/generate_layers.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

# Cada capa: 3 filas de 12 teclas (6 izq + 6 der) y 6 pulgares (3 izq + 3 der).
# "" = sin funcion, "▽" = transparente.
LAYERS = {
    "base": ("Base", [
        ["Tab", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "Bksp"],
        ["LShft", "A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "Del"],
        ["LCtl", "Z", "X", "C", "V", "B", "N", "M", ",", ".", "/", "Caps"],
    ], ["LAlt", "Lower", "Space", "Enter", "Raise", "RAlt"]),
    "lower": ("Lower", [
        ["Esc", "!", "@", "#", "$", "%", "", "", "↑", "", "", "\\"],
        ["LShft", "^", "&", "*", "↑", "~", "", "←", "↓", "→", "'", "="],
        ["LCtl", "", "PrtSc", "←", "↓", "→", "(", ")", "[", "]", "-", "`"],
    ], ["LWin", "▽", "Space", "Enter", "▽", "RAlt"]),
    "raise": ("Raise", [
        ["Esc", "", "", "↑", "", "Calc", "+", "7", "8", "9", "×", "Bksp"],
        ["LShft", "", "←", "↓", "→", "", "−", "4", "5", "6", "÷", "Del"],
        ["LCtl", "", "PrtSc", "", "", "", ",", "1", "2", "3", ".", "="],
    ], ["LWin", "▽", "Space", "Enter", "▽", "0"]),
    "adjust": ("Adjust", [
        ["Boot", "BT 0", "BT 1", "BT 2", "BT 3", "BT 4", "", "", "", "", "", "Boot"],
        ["Reset", "USB", "BLE", "", "", "", "", "", "", "", "", "Reset"],
        ["Studio", "", "", "", "", "", "", "", "", "", "", "BT CLR"],
    ], ["▽", "▽", "▽", "▽", "▽", "▽"]),
}

U = 64          # paso entre teclas
KEY = 58        # lado de la tecla
LEFT_OFF = [10, 0, -17, -27, -18, -10]    # escalonado de columnas (izq)
RIGHT_OFF = [-10, -18, -27, -17, 0, 10]   # (der)
X_L, X_R, Y0 = 34, 34 + 6 * U + 190, 78
W, H = X_R + 6 * U + 34, 392

BG, FRAME, KEYC, TXT, DIM = "#251d1b", "#e9c1b2", "#3a3330", "#f3cdbf", "#6d5f5a"


def key(cx, cy, label, rot=0):
    empty = label == ""
    transp = label == "▽"
    fill = "#2f2927" if (empty or transp) else KEYC
    size = 20 if len(label) <= 1 else 15 if len(label) <= 4 else 12
    out = [f'<g transform="translate({cx:.1f} {cy:.1f}) rotate({rot})">',
           f'<rect x="{-KEY/2}" y="{-KEY/2}" width="{KEY}" height="{KEY}" rx="7" '
           f'fill="{fill}" stroke="#4a403c" stroke-width="1"/>']
    if not empty:
        color = DIM if transp else TXT
        # El simbolo transparente no rota con la tecla para que no parezca una flecha.
        unrot = f' transform="rotate({-rot})"' if transp else ""
        out.append(f'<text x="0" y="{size*0.35:.1f}" text-anchor="middle"{unrot} '
                   f'font-size="{size}" font-weight="600" fill="{color}">{escape(label)}</text>')
    out.append("</g>")
    return "".join(out)


def render(title, rows, thumbs):
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
             f'font-family="Segoe UI, Helvetica, Arial, sans-serif">',
             f'<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="14" fill="{BG}" stroke="{FRAME}" stroke-width="6"/>',
             f'<text x="{W/2}" y="40" text-anchor="middle" font-size="22" font-weight="700" '
             f'fill="{FRAME}" letter-spacing="3">{escape(title.upper())}</text>']
    for r, row in enumerate(rows):
        for c in range(6):
            parts.append(key(X_L + c * U + U / 2, Y0 + r * U + U / 2 + LEFT_OFF[c], row[c]))
            parts.append(key(X_R + c * U + U / 2, Y0 + r * U + U / 2 + RIGHT_OFF[c], row[6 + c]))
    ty = Y0 + 3 * U + U / 2 + 4
    left = [(X_L + 3 * U + U / 2 - 4, ty - 4, 0), (X_L + 4 * U + U / 2 + 2, ty + 2, 15),
            (X_L + 5 * U + U / 2 + 12, ty + 14, 30)]
    right = [(X_R + 0 * U + U / 2 - 12, ty + 14, -30), (X_R + 1 * U + U / 2 - 2, ty + 2, -15),
             (X_R + 2 * U + U / 2 + 4, ty - 4, 0)]
    for (x, y, rot), label in zip(left + right, thumbs):
        parts.append(key(x, y, label, rot))
    parts.append("</svg>")
    return "\n".join(parts)


if __name__ == "__main__":
    out = Path(__file__).parent / "layers"
    out.mkdir(exist_ok=True)
    for name, (title, rows, thumbs) in LAYERS.items():
        (out / f"{name}.svg").write_text(render(title, rows, thumbs), encoding="utf-8")
        print("ok", name)
