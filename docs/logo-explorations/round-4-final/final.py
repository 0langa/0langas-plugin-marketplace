"""Round 4, final set: the round-3 crest (F) with the folded shading of G and the hard two-ink split of H.

Every mark sits on a brand-colour disc inside a thin ring. Its shapes come in two families:
  main   - light tones on dark discs, ink tones on light discs
  second - the hard split: ink on dark discs, a deep brand tone on light discs
The whole mark is folded once along a crease: the upper-left side is lit, the rest in shadow.

Shape roles: solid (main fill), shade (second fill), line (main stroke), ghost (dashed stroke),
cut (knocks out what was drawn before it). `sep` cuts a gap around a shape, `self` shrinks it,
`fam` moves a shape to the other family, `side` keeps a small shape in one tone so the crease never
cuts a sliver off it, `facet` gives a Web.de flap its own tone.
"""
import math
import random
from pathlib import Path

OUT = Path(__file__).parent

PLUGINS = [
    ("recall", "RECALL", "#256D5A"),
    ("agent-handoff", "Agent Handoff", "#2F7BFF"),
    ("usage-pulse", "Usage Pulse", "#19D39A"),
    ("plugin-forge", "Plugin Forge", "#F05A3A"),
    ("webde-access", "Web.de Access", "#E7B93B"),
    ("plugin-evaluation-kimi", "Plugin Evaluation Kimi", "#7C5CFF"),
    ("customization-control", "Customization Control", "#F2A11A"),
    ("addonry", "Addonry", "#7C3AED"),
    ("computer-custom", "Computer Custom", "#E0457B"),
]

IDEAS = {
    "recall": "Memory lives as cards in the project. One card is lifted out of the stack: the one that matters now.",
    "agent-handoff": "Two agents, two halves. The work packet sits across the gap and belongs to both.",
    "usage-pulse": "Tally marks that beat like a pulse. It counts quietly and never keeps the words.",
    "plugin-forge": "A plug-in with three identical pins: one spec, three matching provider manifests.",
    "webde-access": "A letter folded shut. The four folds now meet cleanly in the centre.",
    "plugin-evaluation-kimi": "Three rings for three layers of judgement; the dots are Monte Carlo runs landing near the centre.",
    "customization-control": "One canonical copy stays solid. The duplicates wait in quarantine as outlines.",
    "addonry": "A browser window, and a new piece dropping into its toolbar slot.",
    "computer-custom": "The pointer is split in two: the server decides and never acts, the helper acts and never decides.",
}

INK, CREAM = "#15161A", "#F4EEDD"


# ---------------- geometry helpers ----------------

def f(x):
    return f"{x:.2f}".rstrip("0").rstrip(".")


def poly(points):
    return "M" + " L".join(f"{f(x)} {f(y)}" for x, y in points) + " Z"


def rrect(x, y, w, h, r):
    return (f"M{f(x + r)} {f(y)} H{f(x + w - r)} Q{f(x + w)} {f(y)} {f(x + w)} {f(y + r)} V{f(y + h - r)} "
            f"Q{f(x + w)} {f(y + h)} {f(x + w - r)} {f(y + h)} H{f(x + r)} Q{f(x)} {f(y + h)} {f(x)} {f(y + h - r)} "
            f"V{f(y + r)} Q{f(x)} {f(y)} {f(x + r)} {f(y)} Z")


def circle(cx, cy, r):
    return f"M{f(cx - r)} {f(cy)} A{f(r)} {f(r)} 0 1 0 {f(cx + r)} {f(cy)} A{f(r)} {f(r)} 0 1 0 {f(cx - r)} {f(cy)} Z"


def clip_half(points, a, b, c):
    """Keep the part of a polygon where a*x + b*y + c <= 0."""
    out = []
    for i in range(len(points)):
        p, q = points[i], points[(i + 1) % len(points)]
        fp, fq = a * p[0] + b * p[1] + c, a * q[0] + b * q[1] + c
        if fp <= 0:
            out.append(p)
        if (fp < 0 < fq) or (fq < 0 < fp):
            t = fp / (fp - fq)
            out.append((p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1])))
    return out


def S(role, d, sep=0.0, width=0.0, **extra):
    shape = {"role": role, "d": d, "sep": sep, "w": width}
    shape.update(extra)
    return shape


# ---------------- the marks ----------------

def recall():
    tf = "rotate(-9 6 -14)"
    return [
        S("shade", rrect(-27, 8, 42, 22, 3)),
        S("solid", rrect(-23, 0, 42, 22, 3), sep=3),
        S("solid", rrect(-14, -29, 42, 23, 3), sep=3.2, tf=tf),
        S("cut", "M-8 -20.5 H18", width=2.6, tf=tf),
        S("cut", "M-8 -13.5 H10", width=2.6, tf=tf),
    ]


def handoff():
    left = "M-3 -26 H-20 Q-30 -26 -30 -16 V8 Q-30 18 -20 18 H-3 Z"
    right = "M3 -18 H20 Q30 -18 30 -8 V16 Q30 26 20 26 H3 Z"
    return [
        S("solid", left),
        S("shade", right),
        S("cut", rrect(-16, -8, 32, 16, 8)),
        S("solid", rrect(-11.5, -3.6, 23, 7.2, 3.6)),
    ]


def pulse():
    """Four tally strokes in a heartbeat rhythm, crossed by the fifth stroke."""
    bars = [(-18, -2, 11), (-6, -8, 22), (6, 8, 19), (18, -3, 14)]   # x, centre, half-length
    out = [S("line", f"M{x} {c - h} V{c + h}", width=7.5, side="lit" if x < 0 else "shadow") for x, c, h in bars]
    out.append(S("line", "M-30 13 L28 -13", sep=3, width=6.5))
    return out


def forge():
    """A plug with three identical pins, set on the diagonal."""
    r2 = math.sqrt(0.5)
    at = lambda s, t: (s * r2 + t * r2, -s * r2 + t * r2)   # s along the plug, t across it

    def pin(t, w=3.3, s0=10, s1=23):
        a0, a1 = at(s0, t - w), at(s1, t - w)
        b1, b0 = at(s1, t + w), at(s0, t + w)
        return (f"M{f(a0[0])} {f(a0[1])} L{f(a1[0])} {f(a1[1])} A{w} {w} 0 0 1 {f(b1[0])} {f(b1[1])} "
                f"L{f(b0[0])} {f(b0[1])} Z")

    c0, c1 = at(-34, 0), at(-15, 0)
    body = poly([at(s, t) for s, t in [(-17, -7), (-10, -17), (10, -17), (10, 17), (-10, 17), (-17, 7)]])
    return [
        S("line", f"M{f(c0[0])} {f(c0[1])} L{f(c1[0])} {f(c1[1])}", width=6.5),
        S("solid", body, round=4),
    ] + [S("shade", pin(t), side="shadow") for t in (-10.9, 0, 10.9)]


def webde():
    """Four flaps meeting exactly in the centre, each one turned a little: a folded letter."""
    R, t = 33.5, 0.15
    V = [(0, -R), (R, 0), (0, R), (-R, 0)]
    E = [(V[i][0] + t * (V[i - 1][0] - V[i][0]), V[i][1] + t * (V[i - 1][1] - V[i][1])) for i in range(4)]
    return [S("solid", poly([(0, 0), E[i], V[i], E[(i + 1) % 4]]), self=2.6, facet=i) for i in range(4)]


def evaluation():
    """Three rings, and a tight group of Monte Carlo runs with two strays."""
    dots = [(2, -3), (9, -6), (8, 2), (-5, -1), (1, 5), (-1, -11), (15, -1), (-12, 9), (20, -15)]
    out = [S("line", circle(0, 0, r), width=3.4) for r in (31, 20.5, 10)]
    out += [S("shade", circle(x, y, 3), sep=2, side="shadow", sep_roles=("line",)) for x, y in dots]
    return out


def customization():
    return [
        S("ghost", rrect(-6, -26, 32, 32, 7), width=2.8, fam="second", side="lit"),
        S("ghost", rrect(-15, -17, 32, 32, 7), width=2.8, fam="second", side="lit", sep=2.4, sep_roles=("ghost",)),
        S("solid", rrect(-26, -7.2, 32, 32, 7), sep=3.2),
    ]


def addonry():
    return [
        S("solid", rrect(-30, -18, 60, 44, 6)),
        S("cut", "M-30 -4 H30", width=2.6),
        S("cut", rrect(10.5, -21, 13.5, 13.5, 2.5)),
        S("shade", rrect(12.75, -32, 9, 9, 2), side="shadow"),
    ]


def computer():
    arrow = [(-12, -31), (-12, 17), (-1.5, 7.5), (6, 25), (13, 22), (5.5, 5), (20, 5)]
    top = clip_half(arrow, 0.5, 1, 4)
    bottom = clip_half(arrow, -0.5, -1, 0.5)
    return [S("shade", poly(top), side="shadow"), S("solid", poly(bottom))]


MARKS = {
    # name: (builder, transform applied to the whole mark)
    "recall": (recall, "translate(0 1)"),
    "agent-handoff": (handoff, "scale(0.95)"),
    "usage-pulse": (pulse, "translate(0 1)"),
    "plugin-forge": (forge, "translate(2.5 -2.5)"),
    "webde-access": (webde, ""),
    "plugin-evaluation-kimi": (evaluation, ""),
    "customization-control": (customization, ""),
    "addonry": (addonry, "scale(0.92) translate(0 3)"),
    "computer-custom": (computer, "translate(-4 3)"),
}


# ---------------- colour ----------------

def luma(c):
    h = c.lstrip("#")
    return sum(w * int(h[i:i + 2], 16) for w, i in ((0.299, 0), (0.587, 2), (0.114, 4)))


def mix(c, t, amt):
    a = [int(c.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)]
    b = [int(t.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)]
    return "#%02X%02X%02X" % tuple(round(x + (y - x) * amt) for x, y in zip(a, b))


def palette(color):
    light = {"lit": mix(CREAM, color, 0.05), "shadow": mix(CREAM, color, 0.27)}
    ink = {"lit": mix(INK, color, 0.30), "shadow": mix(INK, color, 0.07)}
    deep = {"lit": mix(color, INK, 0.40), "shadow": mix(color, INK, 0.56)}
    if luma(color) > 145:   # light disc: ink marks, deep-brand second ink
        return {"main": ink, "second": deep, "ring": ink["shadow"]}
    return {"main": light, "second": ink, "ring": light["lit"]}


def facet_colors(color, i):
    """Web.de flaps: one tone per flap, lit from the upper left."""
    amt = {3: 0.32, 0: 0.18, 2: 0.13, 1: 0.03}[i]
    base = INK if luma(color) > 145 else CREAM
    c = mix(base, color, amt)
    return c, c


# ---------------- rendering ----------------

def shape_masks(shapes, uid):
    defs, refs = [], {}
    for j, s in enumerate(shapes):
        if s["role"] == "cut":
            continue
        knocks = []
        for k in range(j, len(shapes)):
            t = shapes[k]
            closed = t["d"].endswith("Z")
            tfk = f' transform="{t["tf"]}"' if t.get("tf") else ""
            if t["role"] == "cut":
                knocks.append(f'<path d="{t["d"]}"{tfk} fill="#000"/>' if closed else
                              f'<path d="{t["d"]}"{tfk} fill="none" stroke="#000" stroke-width="{t["w"]}" '
                              f'stroke-linecap="round"/>')
            elif t["sep"] and k > j and s["role"] in t.get("sep_roles", (s["role"],)):
                if closed:
                    knocks.append(f'<path d="{t["d"]}"{tfk} fill="#000" stroke="#000" '
                                  f'stroke-width="{f(2 * t["sep"])}" stroke-linejoin="round"/>')
                else:
                    knocks.append(f'<path d="{t["d"]}"{tfk} fill="none" stroke="#000" '
                                  f'stroke-width="{f(t["w"] + 2 * t["sep"])}" stroke-linecap="round" '
                                  f'stroke-linejoin="round"/>')
            elif t.get("self") and k == j:
                knocks.append(f'<path d="{t["d"]}"{tfk} fill="none" stroke="#000" stroke-width="{f(t["self"])}" '
                              f'stroke-linejoin="round"/>')
        if knocks:
            mid = f"{uid}-m{j}"
            defs.append(f'<mask id="{mid}" maskUnits="userSpaceOnUse" x="-60" y="-60" width="120" height="120">'
                        f'<rect x="-60" y="-60" width="120" height="120" fill="#fff"/>{"".join(knocks)}</mask>')
            refs[j] = mid
    return "".join(defs), refs


def draw(shapes, refs, pal, color, side):
    out = []
    for j, s in enumerate(shapes):
        role = s["role"]
        if role == "cut":
            continue
        fam = s.get("fam") or ("second" if role == "shade" else "main")
        if s.get("side"):
            if side == "lit":
                continue  # drawn once, whole, in the shadow pass
            col = pal[fam][s["side"]]
        else:
            col = pal[fam][side]
        if "facet" in s:
            col = facet_colors(color, s["facet"])[0 if side == "lit" else 1]
        tfs = f' transform="{s["tf"]}"' if s.get("tf") else ""
        closed = s["d"].endswith("Z")
        if role == "ghost":
            el = (f'<path d="{s["d"]}"{tfs} fill="none" stroke="{col}" stroke-width="{s["w"]}" '
                  f'stroke-dasharray="3 6.2" stroke-linecap="round"/>')
        elif role == "line" or not closed:
            el = (f'<path d="{s["d"]}"{tfs} fill="none" stroke="{col}" stroke-width="{s["w"]}" '
                  f'stroke-linecap="round" stroke-linejoin="round"/>')
        elif s.get("round"):
            el = (f'<path d="{s["d"]}"{tfs} fill="{col}" stroke="{col}" stroke-width="{s["round"]}" '
                  f'stroke-linejoin="round"/>')
        else:
            el = f'<path d="{s["d"]}"{tfs} fill="{col}"/>'
        out.append(f'<g mask="url(#{refs[j]})">{el}</g>' if j in refs else el)
    return "".join(out)


def mark(name, color):
    builder, tf = MARKS[name]
    shapes = builder()
    pal = palette(color)
    uid = f"L-{name}"
    mdefs, refs = shape_masks(shapes, uid)
    crease = f'<clipPath id="{uid}-c"><path d="M-80 -80 H80 L-80 80 Z" transform="rotate(-8)"/></clipPath>'
    shadow = draw(shapes, refs, pal, color, "shadow")
    lit = draw(shapes, refs, pal, color, "lit")
    g = f' transform="{tf}"' if tf else ""
    return (f'<defs>{mdefs}{crease}</defs>'
            f'<circle r="49" fill="{color}"/>'
            f'<circle r="43.5" fill="none" stroke="{pal["ring"]}" stroke-width="2.2"/>'
            f'<g{g}>{shadow}<g clip-path="url(#{uid}-c)">{lit}</g></g>')


def svg(inner, size=None, label=""):
    s = f' width="{size}" height="{size}"' if size else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-50 -50 100 100"{s} role="img" '
            f'aria-label="{label}">{inner}</svg>')


def main():
    d = OUT / "svg"
    d.mkdir(exist_ok=True)
    cards = []
    for name, display, color in PLUGINS:
        inner = mark(name, color)
        (d / f"{name}.svg").write_text(svg(inner, 1024, display), encoding="utf-8")
        cards.append(
            f'<figure><div class="big">{svg(inner, 200, display)}</div>'
            f'<div class="small"><span class="on-dark">{svg(inner, 48, display)}{svg(inner, 32, display)}'
            f'{svg(inner, 16, display)}</span><span class="on-light">{svg(inner, 48, display)}'
            f'{svg(inner, 32, display)}{svg(inner, 16, display)}</span></div>'
            f'<figcaption><b>{display}</b><br>{IDEAS[name]}</figcaption></figure>')
    html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Plugin Logos Final</title>
<style>
:root{{--bg:#FAFAF7;--fg:#17181C;--muted:#6B6E76;--card:#FFFFFF;--line:#E6E4DE}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#0B0C10;--fg:#ECECEF;--muted:#9A9DA6;--card:#15171D;--line:#262932}}}}
:root[data-theme="dark"]{{--bg:#0B0C10;--fg:#ECECEF;--muted:#9A9DA6;--card:#15171D;--line:#262932}}
body{{margin:0;background:var(--bg);color:var(--fg);font:15px/1.5 system-ui,Segoe UI,sans-serif}}
main{{max-width:1180px;margin:0 auto;padding:32px 16px 64px}}
h1{{font-size:26px;margin:0 0 4px}} header p{{color:var(--muted);margin:0 0 24px;max-width:760px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:14px}}
figure{{margin:0;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px;text-align:center}}
.big svg{{display:block;margin:0 auto;max-width:100%;height:auto}}
.small{{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin:14px 0 8px}}
.small span{{display:flex;gap:8px;align-items:center;padding:6px 8px;border-radius:10px}}
.on-dark{{background:#1B1D24}} .on-light{{background:#EFEDE8}}
figcaption{{font-size:13px;color:var(--muted);text-align:left}} figcaption b{{color:var(--fg);font-size:14px}}
</style></head><body><main><header><h1>Plugin Logos, Final</h1>
<p>The crest from F, the folded shading from G, the hard two-ink split from H. Each card shows the logo large,
then at 48, 32 and 16 px on a dark and a light background.</p></header>
<div class="grid">{"".join(cards)}</div></main></body></html>"""
    (OUT / "final.html").write_text(html, encoding="utf-8")
    print("ok")


if __name__ == "__main__":
    main()
