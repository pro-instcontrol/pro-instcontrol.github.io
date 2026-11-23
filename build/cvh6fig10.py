# -*- coding: utf-8 -*-
"""Vector figures for Chapter 10 "Isolation Valves" of Emerson,
*Control Valve Handbook*, 6th ed. (2020), printed pp. 210-239.

Fifty-three figures ``fig_f10_01`` ... ``fig_f10_53``. Each is registered
with :func:`_reg` and returns the standard 5-tuple
``(svg, caption_vi, caption_en, aria_vi, aria_en)`` through :func:`_finish`.
Figures 10.1-10.39 are simplified vector cross-sections / piping schematics;
figures 10.40-10.53 are bilingual dimension tables transcribed verbatim from
the printed source.  All text passes through :func:`T` / :func:`esc`; no bare
ampersand and no CJK character is emitted into any SVG.

Source quirks handled here: the printed Table 10.44 header repeats an
"in mm" pair that the data rows do not contain (rows carry 14 data columns);
Rows of Fig. 10.50 for the 1/2 and 3/4 inch sizes lost one "---" token in OCR
and are padded to the 8-column structure; Fig. 10.46 row "3 in" prints the
beveled-end millimetre value 557.9 where 577.9 would be expected, and that
printed value is kept.  Figure 10.49's printed caption uses "&" (escaped to
"&amp;" by T/esc, never emitted raw).
"""
from cvh6fig import (_reg, _finish, esc, T, _defs, _rect, _line, _circle,
                     _poly, _arrow, svg, INK, GREY, BLUE, RED, GREEN)
# GOLD / FILL / PAPER live in `vfig`, not re-exported by `cvh6fig`.
from vfig import GOLD, FILL, PAPER  # noqa: F401


# ---------------------------------------------------------------------------
# table helpers copied from build/cvh6fig5.py (lines 24-52)
# ---------------------------------------------------------------------------
def _trow(o, x, y, widths, cells, rh, fs=7.3, fill="#f7f9fb"):
    """One table row.  ``cells`` is ``[(text, anchor), ...]``; text may
    contain a newline for a second line."""
    o.append(_rect(x, y, sum(widths), rh, fill=fill, sw=1.0))
    cx = x
    for wd, (txt, al) in zip(widths, cells):
        lines = str(txt).split("\n")
        cy = y + rh / 2.0 - (len(lines) - 1) * (fs + 1) / 2.0 + fs * 0.35
        for ln in lines:
            tx = cx + 4 if al == "start" else (cx + wd - 4 if al == "end"
                                               else cx + wd / 2.0)
            o.append(T(tx, cy, ln, fs, anchor=al))
            cy += fs + 1
        cx += wd


def _table(o, x, y, widths, headers, rows, rh=21, hh=30, fs=7.3):
    """A light bilingual table with alternating row fills."""
    _trow(o, x, y, widths, [(h, "middle") for h in headers], hh,
          fs=fs, fill="#e9eef4")
    for i, row in enumerate(rows):
        _trow(o, x, y + hh + i * rh, widths, row, rh, fs=fs,
              fill="#fdfcf9" if i % 2 == 0 else "#f2f6fa")
    cx = x
    for wd in widths[:-1]:
        cx += wd
        o.append(_line(cx, y, cx, y + hh + len(rows) * rh, sw=0.7, color=GREY))


# ---------------------------------------------------------------------------
# local drawing helpers
# ---------------------------------------------------------------------------
def _rr(s):
    """Split a multi-line block of source table rows into token lists."""
    return [ln.split() for ln in s.strip().splitlines()]


def _cap(n, p, vi_title, en_title, vi_long, en_long,
         aria_vi=None, aria_en=None):
    """Six-argument payload for :func:`_finish` in contract order.

    The full VI and EN captions keep the exact required formats; the longer
    descriptive sentences are carried by the accessibility labels instead.
    """
    en_cap = "Figure 10.%d (p. %d) - %s" % (n, p, en_title)
    vi_cap = "Hình 10.%d (tr. %d) · %s" % (n, p, vi_title)
    return (
        en_cap,
        vi_cap,
        vi_cap,
        en_cap,
        aria_vi or ("Sơ đồ Hình 10.%d (tr. %d): %s" % (n, p, vi_long)),
        aria_en or ("Figure 10.%d (p. %d): %s" % (n, p, en_long)),
    )


def _frame(w, h, vi, en):
    """Drawing canvas with a bilingual heading band."""
    return [_defs(),
            _rect(8, 8, w - 16, 30, fill="#e9eef4", sw=1.0),
            T(w / 2.0, 28, vi + " / " + en, 10.6, weight="600")]


def _labels(o, items, x, y, lh=17, size=7.0):
    """Bilingual label column with a small dot marker."""
    for i, (vi, en) in enumerate(items):
        yy = y + i * lh
        o.append(_circle(x, yy - 2.5, 1.8, fill=BLUE, sw=0))
        o.append(T(x + 9, yy, vi + " / " + en, size, anchor="start"))


def _lead(o, px, py, tx, ty):
    o.append(_line(px, py, tx, ty, sw=0.7, color=GREY))


def _flow(o, x1, x2, y, label="Dòng chảy / Flow"):
    o.append(_arrow(x1, y, x2, y, sw=1.5, color=BLUE))
    o.append(T((x1 + x2) / 2.0, y - 9, label, 7.2, color=BLUE))


def _pipe(o, cx, cy, L=350, H=54):
    o.append(_rect(cx - L / 2, cy - H / 2, L, H, fill="#f5f8fc", sw=1.6))
    o.append(_rect(cx - L / 2 - 13, cy - H / 2 - 8, 15, H + 16,
                   fill="#e9eef4", sw=1.3))
    o.append(_rect(cx + L / 2 - 2, cy - H / 2 - 8, 15, H + 16,
                   fill="#e9eef4", sw=1.3))


def _wheel(o, cx, cy, r=28):
    o.append(_circle(cx, cy, r, fill="#fdf3e6", sw=1.7))
    o.append(_line(cx - r, cy, cx + r, cy, sw=1.0))
    o.append(_line(cx, cy - r, cx, cy + r, sw=1.0))
    o.append(_line(cx, cy, cx, cy + 16, sw=1.4))


def _gate(o, cx, cy, kind="solid", ps=False, bolted=True):
    """Gate valve cross-section with a selectable closing element."""
    L, H = 350, 54
    _pipe(o, cx, cy, L, H)
    o.append(_rect(cx - 56, cy - H / 2, 12, H, fill="#dce5f0", sw=1.0))
    o.append(_rect(cx + 44, cy - H / 2, 12, H, fill="#dce5f0", sw=1.0))
    if kind == "solid":
        o.append(_poly([(cx - 30, cy - 23), (cx + 30, cy - 23),
                        (cx + 20, cy + 23), (cx - 20, cy + 23)],
                       fill=FILL, sw=1.5, close=True))
    elif kind == "flexible":
        o.append(_poly([(cx - 30, cy - 23), (cx + 30, cy - 23),
                        (cx + 22, cy + 20), (cx + 7, cy + 9), (cx, cy + 23),
                        (cx - 7, cy + 9), (cx - 22, cy + 20)],
                       fill=FILL, sw=1.5, close=True))
    elif kind == "split":
        o.append(_poly([(cx - 30, cy - 23), (cx - 2, cy - 23),
                        (cx - 5, cy + 23), (cx - 26, cy + 21)],
                       fill=FILL, sw=1.4, close=True))
        o.append(_poly([(cx + 2, cy - 23), (cx + 30, cy - 23),
                        (cx + 26, cy + 21), (cx + 5, cy + 23)],
                       fill=FILL, sw=1.4, close=True))
    elif kind == "double":
        o.append(_rect(cx - 30, cy - 21, 20, 42, fill=FILL, sw=1.4))
        o.append(_rect(cx + 10, cy - 21, 20, 42, fill=FILL, sw=1.4))
        o.append(_poly([(cx - 4, cy - 12), (cx + 4, cy), (cx - 4, cy + 12)],
                       fill=GOLD, sw=1.0, close=True))
        o.append(_poly([(cx + 4, cy - 12), (cx - 4, cy), (cx + 4, cy + 12)],
                       fill=GOLD, sw=1.0, close=True))
    else:  # eyelet / flexible split
        o.append(_poly([(cx - 32, cy - 23), (cx + 32, cy - 23),
                        (cx + 24, cy + 18), (cx - 24, cy + 18)],
                       fill=FILL, sw=1.4, close=True))
        o.append(_circle(cx, cy, 8, fill="#ffffff", sw=1.2, color=BLUE))
    o.append(_rect(cx - 46, cy - 92, 92, 64, fill="#eef3fb", sw=1.4))
    if ps:
        for dy in (0, 9, 18):
            o.append(_rect(cx - 38, cy - 58 + dy, 76, 5,
                           fill="#d9e2ee", sw=0.8))
    elif bolted:
        o.append(_line(cx - 52, cy - 30, cx - 52, cy - 88, sw=1.1))
        o.append(_line(cx + 52, cy - 30, cx + 52, cy - 88, sw=1.1))
        o.append(_circle(cx - 52, cy - 88, 3, fill="#ffffff", sw=1.0))
        o.append(_circle(cx + 52, cy - 88, 3, fill="#ffffff", sw=1.0))
    o.append(_rect(cx - 16, cy - 102, 32, 11, fill="#e4ebf4", sw=1.0))
    o.append(_line(cx, cy - 102, cx, cy - 124, sw=2.2))
    _wheel(o, cx, cy - 134, 28)
    _flow(o, cx - L / 2 - 86, cx - L / 2 - 8, cy)
    _arrow(cx + L / 2 + 8, cy, cx + L / 2 + 66, cy, sw=1.4, color=BLUE)


def _globe(o, cx, cy, pattern="T", disk="conv"):
    """Globe valve cross-section; pattern T / angle / Y."""
    L, H = 340, 58
    if pattern == "angle":
        o.append(_rect(cx - 170, cy - H / 2, 212, H, fill="#f5f8fc", sw=1.6))
        o.append(_rect(cx + 38, cy - 27, 44, 92, fill="#f5f8fc", sw=1.6))
        o.append(_rect(cx - 183, cy - 36, 15, H + 16,
                       fill="#e9eef4", sw=1.3))
        o.append(_rect(cx + 38, cy + 61, 70, 14,
                       fill="#e9eef4", sw=1.3))
        bx, by, bw, bh = cx - 40, cy - 96, 80, 70
    else:
        _pipe(o, cx, cy, L, H)
        if pattern == "Y":
            bx, by, bw, bh = cx - 48, cy - 96, 96, 70
            o.append(_poly([(bx + 22, by), (bx + bw, by),
                            (bx + bw - 22, by + bh), (bx, by + bh)],
                           fill="#eef3fb", sw=1.4, close=True))
        else:
            bx, by, bw, bh = cx - 40, cy - 96, 80, 70
            o.append(_rect(bx, by, bw, bh, fill="#eef3fb", sw=1.4))
    o.append(_rect(cx - 14, cy - 26, 28, 8, fill="#dce5f0", sw=1.0))
    if disk == "plug":
        o.append(_poly([(cx - 7, cy - 22), (cx + 7, cy - 22),
                        (cx + 4, cy + 18), (cx - 4, cy + 18)],
                       fill=FILL, sw=1.3, close=True))
    else:
        o.append(_poly([(cx - 16, cy - 20), (cx + 16, cy - 20),
                        (cx + 7, cy + 4), (cx - 7, cy + 4)],
                       fill=FILL, sw=1.3, close=True))
    o.append(_line(cx, cy - 20, cx, cy - 118, sw=2.2))
    o.append(_rect(cx - 14, cy - 104, 28, 10, fill="#e4ebf4", sw=1.0))
    _wheel(o, cx, cy - 134, 28)
    _flow(o, cx - L / 2 - 84, cx - L / 2 - 8, cy)
    if pattern == "angle":
        _arrow(cx + 60, cy - 20, cx + 60, cy + 42, sw=1.4, color=BLUE)
    else:
        _arrow(cx + L / 2 + 8, cy, cx + L / 2 + 66, cy, sw=1.4, color=BLUE)


def _check(o, cx, cy, kind="swing"):
    """Check valve cross-section: swing / lever / tilting / lift."""
    L, H = 340, 56
    _pipe(o, cx, cy, L, H)
    o.append(_rect(cx + 30, cy - H / 2, 10, H, fill="#dce5f0", sw=1.0))
    if kind in ("swing", "lever"):
        o.append(_line(cx + 18, cy - 14, cx + 18, cy - 42, sw=1.8))
        o.append(_circle(cx + 18, cy - 42, 3.2, fill="#ffffff", sw=1.2))
        o.append(_poly([(cx + 18, cy - 42), (cx - 14, cy - 26),
                        (cx - 14, cy - 6), (cx + 18, cy - 12)],
                       fill=FILL, sw=1.4, close=True))
        if kind == "lever":
            o.append(_line(cx + 18, cy - 42, cx + 74, cy - 74, sw=1.6))
            o.append(_circle(cx + 82, cy - 78, 10, fill="#d9e2ee", sw=1.2))
    elif kind == "tilting":
        o.append(_poly([(cx - 18, cy - 18), (cx + 14, cy - 26),
                        (cx + 10, cy + 8), (cx - 20, cy + 14)],
                       fill=FILL, sw=1.4, close=True))
        o.append(_circle(cx + 4, cy - 8, 3, fill="#ffffff", sw=1.2, color=RED))
    else:  # horizontal lift
        o.append(_rect(cx - 12, cy - 20, 24, 38, fill=FILL, sw=1.4))
        o.append(_line(cx, cy + 18, cx, cy + 42, sw=1.2))
    o.append(_rect(cx - 42, cy - 92, 84, 62, fill="#eef3fb", sw=1.4))
    o.append(_circle(cx, cy - 92, 8, fill="#ffffff", sw=1.2))
    _flow(o, cx - L / 2 - 84, cx - L / 2 - 8, cy)
    _arrow(cx + L / 2 + 8, cy, cx + L / 2 + 66, cy, sw=1.4, color=BLUE)


def _diaphragm(o, cx, cy, weir=True):
    L, H = 350, 56
    _pipe(o, cx, cy, L, H)
    if weir:
        o.append(_poly([(cx - 30, cy + H / 2), (cx - 14, cy - 4),
                        (cx + 14, cy - 4), (cx + 30, cy + H / 2)],
                       fill="#dce5f0", sw=1.2, close=True))
        o.append(_poly([(cx - 62, cy - 8), (cx - 14, cy - 8),
                        (cx, cy + 10), (cx + 14, cy - 8),
                        (cx + 62, cy - 8)], sw=1.8, color=RED))
    else:
        o.append(_poly([(cx - 62, cy - 8), (cx - 30, cy + 6),
                        (cx, cy + 16), (cx + 30, cy + 6),
                        (cx + 62, cy - 8)], sw=1.8, color=RED))
    o.append(_rect(cx - 70, cy - 86, 140, 48, fill="#eef3fb", sw=1.4))
    o.append(_line(cx, cy - 8, cx, cy - 118, sw=2.2))
    o.append(_rect(cx - 16, cy - 96, 32, 10, fill="#e4ebf4", sw=1.0))
    _wheel(o, cx, cy - 134, 28)
    _flow(o, cx - L / 2 - 86, cx - L / 2 - 8, cy)


def _pinch(o, cx, cy, closed=False):
    L = 350
    o.append(_rect(cx - L / 2, cy - 18, L, 36, fill="#f5f8fc", sw=1.6))
    if closed:
        o.append(_poly([(cx - 40, cy - 18), (cx - 8, cy - 16),
                        (cx, cy), (cx - 8, cy + 16), (cx - 40, cy + 18)],
                       fill=FILL, sw=1.4, close=True))
        o.append(_poly([(cx + 40, cy - 18), (cx + 8, cy - 16),
                        (cx, cy), (cx + 8, cy + 16), (cx + 40, cy + 18)],
                       fill=FILL, sw=1.4, close=True))
        o.append(_rect(cx - 14, cy - 26, 28, 52, fill="#e4ebf4", sw=1.2))
    else:
        o.append(_rect(cx - 40, cy - 12, 80, 24, fill=FILL, sw=1.4))
    o.append(_rect(cx - 6, cy - 46, 12, 22, fill="#e4ebf4", sw=1.2))
    o.append(T(cx + 16, cy - 32, "Khí / Air", 7.0, color=BLUE, anchor="start"))
    o.append(_arrow(cx - L / 2 - 46, cy, cx - L / 2 - 8, cy,
                    sw=1.5, color=BLUE))


def _ball(o, cx, cy):
    L, H = 350, 56
    _pipe(o, cx, cy, L, H)
    o.append(_circle(cx, cy, 34, fill="#ffffff", sw=2.0))
    o.append(_rect(cx - 22, cy - 10, 44, 20, fill=FILL, sw=1.3))
    o.append(_line(cx, cy - 34, cx, cy - 96, sw=2.2))
    o.append(_rect(cx - 30, cy - 88, 60, 38, fill="#eef3fb", sw=1.4))
    o.append(_line(cx - 40, cy - 124, cx + 40, cy - 124, sw=3.0))
    o.append(_circle(cx, cy - 124, 6, fill="#ffffff", sw=1.2))
    o.append(T(cx + 48, cy - 116, "Tay cầm / Handle", 7.0, anchor="start"))
    _flow(o, cx - L / 2 - 86, cx - L / 2 - 8, cy)


def _butterfly(o, cx, cy, mount="wafer"):
    R = 96
    o.append(_circle(cx, cy, R, fill="#f5f8fc", sw=2.0))
    o.append(_circle(cx, cy, R - 12, fill="#ffffff", sw=1.2, color=GREY))
    o.append(_line(cx - R + 12, cy - 30, cx + R - 12, cy + 30,
                   sw=7.0, color=FILL))
    o.append(_line(cx, cy - R, cx, cy + R, sw=4.0, color=INK))
    if mount == "lug":
        for ang in range(0, 360, 45):
            import math as _m
            a = _m.radians(ang)
            o.append(_circle(cx + (R + 10) * _m.cos(a),
                             cy + (R + 10) * _m.sin(a), 6,
                             fill="#ffffff", sw=1.1))
    elif mount == "flanged":
        for sg in (-1, 1):
            o.append(_rect(cx + sg * (R + 4) - 7, cy - R - 12, 14,
                           2 * R + 24, fill="#e9eef4", sw=1.2))
    else:
        for sg in (-1, 1):
            o.append(_line(cx + sg * (R + 6), cy - R,
                           cx + sg * (R + 6), cy + R, sw=1.2, color=GREY))
    o.append(T(cx, cy - R - 22, "Nhìn từ trên / Top view", 7.2, color=GREY))


def _plug(o, cx, cy, multiport=False):
    R = 88
    o.append(_circle(cx, cy, R, fill="#f5f8fc", sw=2.0))
    if multiport:
        o.append(_circle(cx, cy, R - 16, fill=FILL, sw=1.4))
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            o.append(_line(cx + dx * 26, cy + dy * 26,
                           cx + dx * (R + 24), cy + dy * (R + 24),
                           sw=8.0, color="#ffffff"))
            o.append(_line(cx + dx * 26, cy + dy * 26,
                           cx + dx * (R + 24), cy + dy * (R + 24),
                           sw=1.0, color=INK))
    else:
        o.append(_poly([(cx - 30, cy - 42), (cx + 30, cy - 42),
                        (cx + 42, cy + 42), (cx - 42, cy + 42)],
                       fill=FILL, sw=1.6, close=True))
        o.append(_circle(cx, cy, 13, fill="#ffffff", sw=1.2))
        o.append(_line(cx - 20, cy - 6, cx + 20, cy + 6, sw=4.0,
                       color="#ffffff"))
    o.append(_line(cx, cy - R, cx, cy - R - 34, sw=2.4))
    o.append(_line(cx - 34, cy - R - 34, cx + 34, cy - R - 34, sw=2.4))
    if not multiport:
        o.append(T(cx + 24, cy - R - 26, "Dầu bôi trơn / Lubricant", 7.0,
                   anchor="start"))


def _vsym(o, x, y, s=11, kind="gate"):
    """Small P&ID valve symbol."""
    if kind == "check":
        o.append(_circle(x, y, s, fill="#ffffff", sw=1.3))
        o.append(_poly([(x - 6, y - 6), (x + 6, y), (x - 6, y + 6)],
                       fill=FILL, sw=1.1, close=True))
    else:
        o.append(_poly([(x - s, y - s), (x, y), (x - s, y + s)],
                       fill="#ffffff", sw=1.3, close=True))
        o.append(_poly([(x + s, y - s), (x, y), (x + s, y + s)],
                       fill="#ffffff", sw=1.3, close=True))
    if kind != "check":
        o.append(_line(x, y - s, x, y - s - 13, sw=1.2))
        o.append(_line(x - 8, y - s - 13, x + 8, y - s - 13, sw=1.2))


def _dim_table(o, x, y, widths, groups, hdr, rows, rh=15.6, hh=22,
               fs=6.6, ghh=24):
    """Multi-level dimension table.  ``groups`` is ``[(col, span, label), ...]``.
    Uses the proven ``_trow`` helper for every real row."""
    total = sum(widths)
    for col, span, lab in groups:
        gx = x + sum(widths[:col])
        gw = sum(widths[col:col + span])
        _trow(o, gx, y, widths[col:col + span], [(lab, "middle")], ghh,
              fs=fs + 0.1, fill="#e3ebf5")
    _trow(o, x, y + ghh, widths, [(h, "middle") for h in hdr], hh,
          fs=fs, fill="#eef3fb")
    for i, row in enumerate(rows):
        _trow(o, x, y + ghh + hh + i * rh, widths,
              [(c, "middle") for c in row], rh, fs=fs,
              fill="#fdfcf9" if i % 2 == 0 else "#f2f6fa")
    return y + ghh + hh + len(rows) * rh


def _notes(o, x, y, lines, fs=6.8):
    for i, ln in enumerate(lines):
        o.append(T(x, y + i * 12, ln, fs, anchor="start", color=GREY))


# ===========================================================================
# Figure 10.1 - 10.39 : valve drawings and piping schematics
# ===========================================================================
@_reg
def fig_f10_01():
    w, h = 680, 440
    o = _frame(w, h, "Van cổng nắp ép chặt", "Gate Valve Pressure Seal")
    _gate(o, 340, 205, kind="solid", ps=True)
    _labels(o, [("Thân van", "Valve body"), ("Đế van", "Seat"),
                ("Nêm đặc", "Solid wedge"), ("Nắp ép", "Pressure seal cover"),
                ("Vòng đệm", "Gasket"), ("Vòng đoạn", "Segment rings")],
            24, 286)
    _labels(o, [("Cổng vào", "Inlet"), ("Cổng ra", "Outlet"),
                ("Ty van", "Stem"), ("Đệm tạp", "Packing"),
                ("Bích tuyền", "Gland flange"), ("Tay vặn", "Handwheel")],
            368, 286)
    return _finish(w, h, o, *_cap(
        1, 211, "Van cổng nắp ép chặt", "Gate Valve Pressure Seal",
        "Cấu tạo van cổng có nắp ép chặt dùng cho áp suất cao.",
        "Cutaway of a pressure-seal bonnet gate valve for high-pressure service."))


@_reg
def fig_f10_02():
    w, h = 680, 470
    o = _frame(w, h, "Van cổng nắp bắt bulông", "Gate Valve Bolted Bonnet")
    _gate(o, 340, 205, kind="flexible", bolted=True)
    _labels(o, [("Thân van", "Valve body"), ("Kết nối bích", "Flanged end"),
                ("Đĩa mềm", "Flexible disk"), ("Ghép ty-đĩa", "Stem-disk link"),
                ("Đệm nắp", "Bonnet gasket"), ("Bulông nắp", "Bonnet studs"),
                ("Đai ốc nắp", "Bonnet nuts"), ("Nắp và giá", "Yoke and bonnet")],
            22, 278, lh=16, size=6.9)
    _labels(o, [("Bạc giá", "Yoke sleeve"), ("Chốt hãm", "Groove pin"),
                ("Bulông mắt", "Gland eye bolts"), ("Đệm tạp", "Packing"),
                ("Bích ép đệm", "Gland flange"), ("Ty van", "Stem"),
                ("Tay vặn", "Handwheel"), ("Đai ốc tay vặn", "Wheel nut")],
            358, 278, lh=16, size=6.9)
    return _finish(w, h, o, *_cap(
        2, 211, "Van cổng nắp bắt bulông", "Gate Valve Bolted Bonnet",
        "Các bộ phận chính của van cổng nắp bắt bulông với đĩa mềm.",
        "Major parts of a bolted-bonnet gate valve with a flexible disk."))


@_reg
def fig_f10_03():
    w, h = 680, 440
    o = _frame(w, h, "Van cổng nêm đặc", "Solid-Wedge Gate Valve")
    _gate(o, 340, 205, kind="solid")
    _lead(o, 340, 205, 300, 256)
    _lead(o, 340, 160, 372, 120)
    _labels(o, [("Thân van", "Valve body"), ("Đế van", "Seat"),
                ("Nêm đặc", "Solid wedge"), ("Ty van", "Stem"),
                ("Đệm tạp", "Packing"), ("Tay vặn", "Handwheel")],
            24, 286)
    _labels(o, [("Cổng vào", "Inlet"), ("Cổng ra", "Outlet"),
                ("Bích", "Flange"), ("Nắp van", "Bonnet"),
                ("Bích ép đệm", "Gland"), ("Chiều đóng", "Closing direction")],
            368, 286)
    return _finish(w, h, o, *_cap(
        3, 212, "Van cổng nêm đặc", "Solid-Wedge Gate Valve",
        "Van cổng nêm đặc với nêm hình côn nằm giữa hai đế nghiêng.",
        "Solid-wedge gate valve whose tapered wedge closes between two seats."))


@_reg
def fig_f10_04():
    w, h = 680, 440
    o = _frame(w, h, "Đĩa nêm linh hoạt", "Flexible-Wedge Disk")
    # side view and top view of the flexible wedge
    o.append(T(188, 76, "Nhìn cạnh / Side view", 8.0, weight="600"))
    o.append(_rect(70, 96, 236, 150, fill="#f5f8fc", sw=1.4))
    o.append(_poly([(96, 118), (280, 118), (256, 218), (188, 188),
                    (120, 218)], fill=FILL, sw=1.6, close=True))
    o.append(_circle(188, 128, 14, fill="#ffffff", sw=1.3))
    o.append(T(188, 112, "Hub", 6.6))
    o.append(T(500, 76, "Nhìn trên / Top view", 8.0, weight="600"))
    o.append(_circle(500, 170, 78, fill="#f5f8fc", sw=1.4))
    o.append(_circle(500, 170, 58, fill=FILL, sw=1.3))
    o.append(_line(422, 170, 578, 170, sw=1.0, color=GREY))
    _labels(o, [("Nêm", "Wedge"), ("Hub giữa", "Center hub"),
                ("Hai nửa đĩa", "Two disk halves"),
                ("Gờ dẫn hướng", "Guide ribs")], 24, 286, lh=20)
    _labels(o, [("Chống kẹt", "Anti-binding"),
                ("Chống rung", "Prevent chattering"),
                ("Độ đàn hồi", "Flexibility"),
                ("Làm kín tốt", "Positive shutoff")], 368, 286, lh=20)
    return _finish(w, h, o, *_cap(
        4, 212, "Đĩa nêm linh hoạt", "Flexible-Wedge Disk",
        "Đĩa nêm linh hoạt có hub giữa nối hai nửa đĩa, có gờ dẫn hướng.",
        "Flexible wedge disk with a center hub joining the two halves and guide ribs."))


@_reg
def fig_f10_05():
    w, h = 680, 440
    o = _frame(w, h, "Van cổng nêm tách", "Split-Wedge Gate Valve")
    _gate(o, 340, 205, kind="split")
    _labels(o, [("Thân van", "Valve body"), ("Đế nghiêng", "Tapered seat"),
                ("Đĩa tách", "Split-wedge disk"), ("Ty lên", "Rising stem"),
                ("Đệm tạp", "Packing"), ("Nắp van", "Bonnet")], 24, 286)
    _labels(o, [("Cổng vào", "Inlet"), ("Cổng ra", "Outlet"),
                ("Áp lực ép đĩa", "Disk seating force"),
                ("Tay vặn", "Handwheel"), ("Bích", "Flange"),
                ("Đóng khít", "Tight closure")], 368, 286)
    return _finish(w, h, o, *_cap(
        5, 212, "Van cổng nêm tách", "Split-Wedge Gate Valve",
        "Vòng cuối của tay vặn ép hai đĩa vào đế nghiêng của van cổng nêm tách.",
        "The last handwheel turn forces the two split disks against the tapered seats."))


@_reg
def fig_f10_06():
    w, h = 680, 440
    o = _frame(w, h, "Van cổng hai đĩa", "Double-Disk Gate Valve")
    _gate(o, 340, 205, kind="double")
    _labels(o, [("Thân van", "Valve body"), ("Đế song song", "Parallel seats"),
                ("Hai đĩa", "Double disk"), ("Nêm tách", "Spreader"),
                ("Ty van", "Stem"), ("Đệm tạp", "Packing")], 24, 286)
    _labels(o, [("Cổng vào", "Inlet"), ("Cổng ra", "Outlet"),
                ("Bích", "Flange"), ("Nắp van", "Bonnet"),
                ("Tay vặn", "Handwheel"), ("Ma sát thấp", "Low friction")],
            368, 286)
    return _finish(w, h, o, *_cap(
        6, 212, "Van cổng hai đĩa", "Double-Disk Gate Valve",
        "Nêm tách đẩy hai đĩa song song vào đế để đóng kín van cổng hai đĩa.",
        "A spreader forces the parallel disks against the seats in a double-disk gate valve."))


@_reg
def fig_f10_07():
    w, h = 680, 440
    o = _frame(w, h, "Van cổng nêm tách linh hoạt",
               "Flexible Split-Wedge Gate Valve")
    _gate(o, 340, 205, kind="eyelet")
    _labels(o, [("Thân van", "Valve body"), ("Nêm tách mềm", "Flexible split wedge"),
                ("Mắt dẫn", "Eyelet follower"), ("Đế van", "Seat"),
                ("Ty van", "Stem"), ("Đệm tạp", "Packing")], 24, 286)
    _labels(o, [("Cổng vào", "Inlet"), ("Cổng ra", "Outlet"),
                ("Đóng theo vị trí", "Seal by position"),
                ("Tay vặn", "Handwheel"), ("Bích", "Flange"),
                ("Áp suất tự làm kín", "Pressure seal")], 368, 286)
    return _finish(w, h, o, *_cap(
        7, 213, "Van cổng nêm tách linh hoạt",
        "Flexible Split-Wedge Gate Valve",
        "Nêm tách linh hoạt có mắt dẫn, đóng theo vị trí và tự siết kín theo áp suất.",
        "Flexible split wedge with an eyelet follower, sealing by position and pressure."))


@_reg
def fig_f10_08():
    w, h = 680, 440
    o = _frame(w, h, "Nắp ép chặt", "Pressure Seal")
    # enlarged pressure-seal detail
    o.append(_rect(70, 80, 540, 200, fill="#f5f8fc", sw=1.6))
    o.append(_rect(70, 80, 540, 22, fill="#e9eef4", sw=1.2))
    for i, dy in enumerate((124, 150, 176, 202)):
        o.append(_rect(120 + i * 6, dy, 440 - i * 12, 14,
                       fill=("#d9e2ee" if i % 2 == 0 else FILL), sw=1.1))
    o.append(_line(340, 80, 340, 280, sw=1.0, color=GREY, dash="5,4"))
    _labels(o, [("Nắp", "Cover"), ("Vòng đệm", "Gasket"),
                ("Vòng đỡ", "Ring"), ("Vòng đoạn", "Segment rings"),
                ("Rãnh thân", "Body groove"), ("Lực dọc trục", "Axial force")],
            24, 310, lh=18)
    _labels(o, [("Biến dạng hướng tâm", "Radial deformation"),
                ("Bề mặt làm kín", "Sealing surface"),
                ("Bulông dự căng", "Pre-stress studs"),
                ("Áp suất thấp", "Low pressure"),
                ("Áp suất cao", "High pressure"),
                ("Thân van", "Valve body")], 360, 310, lh=18)
    return _finish(w, h, o, *_cap(
        8, 214, "Nắp ép chặt", "Pressure Seal",
        "Chi tiết nắp ép chặt: lực dọc trục ép vòng đệm giãn hướng tâm và làm kín.",
        "Pressure-seal detail: axial force deforms the gasket radially to seal the cover."))


@_reg
def fig_f10_09():
    w, h = 680, 470
    o = _frame(w, h, "Van cầu", "Globe Valve")
    _globe(o, 340, 205, pattern="T")
    _labels(o, [("Thân van", "Valve body"), ("Đế van", "Body seat ring"),
                ("Đĩa van", "Disk"), ("Vòng đĩa", "Disk washer"),
                ("Ghép ty-đĩa", "Disk stem ring"), ("Nắp van", "Bonnet"),
                ("Đệm nắp", "Bonnet gasket"), ("Bạc nắp", "Bonnet bushing")],
            22, 278, lh=16, size=6.9)
    _labels(o, [("Ty van", "Stem"), ("Đệm tạp", "Packing"),
                ("Bích ép đệm", "Packing gland"), ("Bulông mắt", "Gland eye bolts"),
                ("Bạc giá", "Yoke bushing"), ("Đai ốc nắp", "Bonnet nuts"),
                ("Tay vặn", "Handwheel"), ("Đai ốc bánh xe", "Wheel nut")],
            358, 278, lh=16, size=6.9)
    return _finish(w, h, o, *_cap(
        9, 214, "Van cầu", "Globe Valve",
        "Cấu tạo van cầu điển hình với các bộ phận chính và chiều dòng chảy.",
        "Typical globe valve construction with major parts and flow direction."))


@_reg
def fig_f10_10():
    w, h = 680, 440
    o = _frame(w, h, "Van cầu góc", "Angle Type Globe Valve")
    _globe(o, 340, 205, pattern="angle")
    _labels(o, [("Thân góc", "Angle body"), ("Đĩa", "Disk"),
                ("Giữ đĩa", "Disk holder"), ("Ty van", "Stem"),
                ("Đệm tạp", "Packing"), ("Nối ren", "Union")], 24, 286)
    _labels(o, [("Cổng vào", "Inlet"), ("Cổng ra", "Outlet"),
                ("Đổi hướng 90 độ", "90 degree turn"),
                ("Tay vặn", "Handwheel"), ("Đế van", "Seat"),
                ("Ít tổn thất", "Less restriction")], 368, 286)
    return _finish(w, h, o, *_cap(
        10, 214, "Van cầu góc", "Angle Type Globe Valve",
        "Van cầu thân góc đổi hướng dòng chảy 90 độ, tiết kiệm không gian lắp đặt.",
        "Angle-pattern globe valve turning the flow 90 degrees to save installation space."))


@_reg
def fig_f10_11():
    w, h = 680, 440
    o = _frame(w, h, "Van cầu kiểu Y", "Y-Pattern Globe Valve")
    _globe(o, 340, 205, pattern="Y")
    _labels(o, [("Thân kiểu Y", "Y-pattern body"), ("Đĩa", "Disk"),
                ("Giữ đĩa", "Disk holder"), ("Ty nghiêng 45 độ", "45 degree stem"),
                ("Đệm tạp", "Packing"), ("Đế van", "Seat")], 24, 286)
    _labels(o, [("Cổng vào", "Inlet"), ("Cổng ra", "Outlet"),
                ("Đường chảy thẳng", "Straight flow path"),
                ("Tay vặn", "Handwheel"), ("Ít cản trở", "Little restriction"),
                ("Chịu bùn", "Handles grit")], 368, 286)
    return _finish(w, h, o, *_cap(
        11, 215, "Van cầu kiểu Y", "Y-Pattern Globe Valve",
        "Van cầu kiểu Y có ty nghiêng 45 độ, đường chảy ít bị cản trở.",
        "Y-pattern globe valve with a 45 degree stem and a low-restriction flow path."))


@_reg
def fig_f10_12():
    w, h = 680, 440
    o = _frame(w, h, "Van cầu đĩa thông thường",
               "Conventional Disk Globe Valve")
    _globe(o, 340, 205, pattern="T", disk="conv")
    _lead(o, 340, 200, 292, 250)
    _labels(o, [("Thân van", "Body"), ("Đế van", "Seat ring"),
                ("Đĩa côn ngắn", "Short tapered disk"),
                ("Bích ép", "Gland plate"), ("Nắp van", "Bonnet"),
                ("Ty van", "Stem")], 24, 286)
    _labels(o, [("Cổng vào", "Inlet"), ("Cổng ra", "Outlet"),
                ("Phá cặn bám", "Breaks deposits"),
                ("Làm kín chắc", "Positive seating"),
                ("Tay vặn", "Handwheel"), ("Áp suất từ dưới", "Pressure below")],
            368, 286)
    return _finish(w, h, o, *_cap(
        12, 215, "Van cầu đĩa thông thường", "Conventional Disk Globe Valve",
        "Đĩa côn ngắn ăn khít đế, thích hợp khi cặn bám dễ lắng trên đế van.",
        "Short tapered disk on a matched seat, preferred where deposits tend to form."))


@_reg
def fig_f10_13():
    w, h = 680, 440
    o = _frame(w, h, "Van cầu đĩa cắm", "Plug Disk Globe Valve")
    _globe(o, 340, 205, pattern="T", disk="plug")
    _lead(o, 340, 204, 292, 250)
    _labels(o, [("Thân van", "Body"), ("Đế van", "Seat ring"),
                ("Đĩa cắm dài", "Long plug disk"), ("Nắp van", "Bonnet"),
                ("Bích ép đệm", "Gland flange"), ("Đệm tạp", "Gland")], 24, 286)
    _labels(o, [("Cổng vào", "Inlet"), ("Cổng ra", "Outlet"),
                ("Chống xói mòn", "Resists erosion"),
                ("Diện tích tiếp xúc dài", "Long contact area"),
                ("Tay vặn", "Handwheel"), ("Ty van", "Stem")], 368, 286)
    return _finish(w, h, o, *_cap(
        13, 215, "Van cầu đĩa cắm", "Plug Disk Globe Valve",
        "Đĩa cắm và đế dài hơn, nghiêng hơn nên chống xói mòn do dòng chảy tốt hơn.",
        "Longer, more tapered plug and seat give maximum resistance to flow erosion."))


@_reg
def fig_f10_14():
    w, h = 680, 440
    o = _frame(w, h, "Van cầu kiểu T", "T-Type Globe Valve")
    _globe(o, 340, 205, pattern="T")
    o.append(T(340, 100, "T", 26, weight="600", color=GREY))
    _labels(o, [("Thân chữ T", "T-pattern body"), ("Đĩa", "Valvehead"),
                ("Đế van", "Seat"), ("Ty van", "Stem"),
                ("Đệm tạp", "Packing"), ("Nắp van", "Bonnet")], 24, 286)
    _labels(o, [("Cổng vào", "Inlet"), ("Cổng ra", "Outlet"),
                ("Làm kín bằng mô-men", "Sealing by torque"),
                ("Áp suất từ dưới", "Pressure from below"),
                ("Tay vặn", "Handwheel"), ("Dùng rộng rãi", "Most common")],
            368, 286)
    return _finish(w, h, o, *_cap(
        14, 215, "Van cầu kiểu T", "T-Type Globe Valve",
        "Van cầu kiểu T phổ biến, làm kín bằng mô-men, dùng cho nhiều áp suất và cỡ.",
        "The common T-pattern globe valve seals by torque across many pressures and sizes."))


@_reg
def fig_f10_15():
    w, h = 680, 440
    o = _frame(w, h, "Van cầu kiểu Y", "Y-Type Globe Valve")
    _globe(o, 340, 205, pattern="Y")
    o.append(T(340, 100, "Y", 26, weight="600", color=GREY))
    _labels(o, [("Thân chữ Y", "Y-pattern body"), ("Đĩa", "Valvehead"),
                ("Đế van", "Seat"), ("Ty van", "Stem"),
                ("Đệm tạp", "Packing"), ("Nắp van", "Bonnet")], 24, 286)
    _labels(o, [("Cổng vào", "Inlet"), ("Cổng ra", "Outlet"),
                ("Làm kín bằng mô-men", "Sealing by torque"),
                ("Tổn thất áp suất thấp", "Low pressure loss"),
                ("Tay vặn", "Handwheel"), ("Dùng áp cao", "High pressure")],
            368, 286)
    return _finish(w, h, o, *_cap(
        15, 216, "Van cầu kiểu Y", "Y-Type Globe Valve",
        "Van cầu kiểu Y có đường chảy êm hơn kiểu T nên tổn thất áp suất thấp hơn.",
        "Y-pattern globe valve with a smoother flow path and lower pressure loss than T pattern."))


@_reg
def fig_f10_16():
    w, h = 680, 440
    o = _frame(w, h, "Van cầu đĩa kiểu góc",
               "Angle Type Disk Globe Valve")
    _globe(o, 340, 205, pattern="angle", disk="plug")
    _labels(o, [("Thân góc", "Angle body"), ("Đĩa", "Valvehead"),
                ("Đế van", "Seat"), ("Ty van", "Stem"),
                ("Đệm tạp", "Packing"), ("Nắp van", "Bonnet")], 24, 286)
    _labels(o, [("Cổng vào", "Inlet"), ("Cổng ra", "Outlet"),
                ("Làm kín bằng mô-men", "Sealing by torque"),
                ("Áp suất từ dưới", "Pressure from below"),
                ("Tay vặn", "Handwheel"), ("Điều tiết", "Throttling")],
            368, 286)
    return _finish(w, h, o, *_cap(
        16, 216, "Van cầu đĩa kiểu góc", "Angle Type Disk Globe Valve",
        "Van cầu đĩa kiểu góc, làm kín bằng mô-men, áp suất tác dụng từ dưới lên.",
        "Angle-pattern disk globe valve sealing by torque with pressure from below."))


@_reg
def fig_f10_17():
    w, h = 680, 420
    o = _frame(w, h, "Chức năng ngăn", "Stop Function")
    _globe(o, 340, 205, pattern="T")
    o.append(_line(336, 196, 336, 120, sw=3.2, color=RED))
    o.append(T(340, 108, "Nối cứng / Connected", 7.2, color=RED))
    _labels(o, [("Đầu van nối ty", "Valvehead linked to stem"),
                ("Chỉ đóng bằng tay vặn", "Closed only by handwheel"),
                ("Đế van", "Seat")], 24, 296, lh=21)
    _labels(o, [("Cổng vào", "Inlet"), ("Cổng ra", "Outlet"),
                ("Không tự đóng", "No self-closing")], 368, 296, lh=21)
    return _finish(w, h, o, *_cap(
        17, 216, "Chức năng ngăn", "Stop Function",
        "Đầu van nối cứng với ty, van chỉ đóng khi vặn tay vặn hoặc bộ truyền động.",
        "Valvehead fixed to the stem; the valve closes only by handwheel or actuator."))


@_reg
def fig_f10_18():
    w, h = 680, 420
    o = _frame(w, h, "Chức năng ngăn - kiểm", "Stop-Check Function")
    _globe(o, 340, 205, pattern="T")
    o.append(_circle(340, 196, 5, fill="#ffffff", sw=1.4, color=RED))
    o.append(T(340, 172, "Không nối / Free", 7.2, color=RED))
    _arrow(520, 260, 410, 260, sw=1.5, color=RED)
    o.append(T(464, 274, "Đảo chiều / Reverse flow", 7.0, color=RED))
    _labels(o, [("Đầu van rời ty", "Valvehead free of stem"),
                ("Đóng được bằng tay vặn", "Can close by handwheel"),
                ("Tự đóng khi đảo chiều", "Closes on flow reversal")],
            24, 306, lh=21)
    _labels(o, [("Cổng vào", "Inlet"), ("Cổng ra", "Outlet"),
                ("Chức năng một chiều", "Check function")], 368, 306, lh=21)
    return _finish(w, h, o, *_cap(
        18, 217, "Chức năng ngăn - kiểm", "Stop-Check Function",
        "Đầu van không nối ty, tự đóng khi dòng chảy đảo chiều.",
        "Valvehead not fixed to the stem; it closes automatically on flow reversal."))


@_reg
def fig_f10_19():
    w, h = 680, 420
    o = _frame(w, h, "Dẫn hướng bằng thân van", "Body Guiding")
    _pipe(o, 340, 205, 350, 56)
    o.append(_rect(300, 179, 80, 52, fill=FILL, sw=1.6))
    o.append(_line(340, 179, 340, 96, sw=2.2))
    o.append(_rect(322, 172, 36, 12, fill="#dce5f0", sw=1.2))
    o.append(_circle(340, 205, 4, fill="#ffffff", sw=1.1, color=RED))
    _wheel(o, 340, 84, 26)
    _flow(o, 175, 255, 205)
    _labels(o, [("Dẫn hướng tại thân", "Guiding on the body"),
                ("Diện tích tiếp xúc lớn", "Large contact area"),
                ("Ổn định đầu van", "Stable valvehead")], 24, 296, lh=21)
    _labels(o, [("Cần phủ cứng", "May need hard-facing"),
                ("Dễ bám cặn", "Subject to fouling"),
                ("Đầu van lớn hơn", "Larger valvehead")], 368, 296, lh=21)
    return _finish(w, h, o, *_cap(
        19, 217, "Dẫn hướng bằng thân van", "Body Guiding",
        "Đầu van được dẫn hướng trực tiếp trên thân, dùng cho van lớn và van một chiều.",
        "Valvehead guided on the body, common on larger globe and non-return valves."))


@_reg
def fig_f10_20():
    w, h = 680, 420
    o = _frame(w, h, "Dẫn hướng bằng ty và nắp", "Stem Bonnet Guiding")
    _pipe(o, 340, 205, 350, 56)
    o.append(_rect(300, 179, 80, 52, fill=FILL, sw=1.6))
    o.append(_rect(304, 100, 72, 78, fill="#eef3fb", sw=1.4))
    o.append(_line(340, 179, 340, 70, sw=2.2))
    o.append(_rect(330, 112, 20, 42, fill="#dce5f0", sw=1.2))
    _wheel(o, 340, 84, 26)
    _flow(o, 175, 255, 205)
    _labels(o, [("Dẫn hướng trong nắp", "Guiding within the bonnet"),
                ("Ty dẫn qua bạc", "Stem through bushing"),
                ("Nhỏ gọn hơn", "Smaller valvehead")], 24, 296, lh=21)
    _labels(o, [("Tránh tác động môi chất", "Isolated from the media"),
                ("Không cần phủ cứng", "No hard-facing needed"),
                ("Ty lớn hơn cho cỡ lớn", "Larger stem for big sizes")],
            368, 296, lh=21)
    return _finish(w, h, o, *_cap(
        20, 217, "Dẫn hướng bằng ty và nắp", "Stem Bonnet Guiding",
        "Ty được dẫn hướng trong nắp van, thường dùng cho van cỡ nhỏ hơn.",
        "Stem guided inside the bonnet, common on smaller-diameter valves."))


@_reg
def fig_f10_21():
    w, h = 680, 440
    o = _frame(w, h, "Van một chiều kiểu xoay", "Swing Check Valve")
    _check(o, 340, 205, kind="swing")
    _labels(o, [("Thân van", "Body"), ("Đế van", "Seat ring"),
                ("Đĩa xoay", "Swing disk"), ("Bản lề", "Hinge"),
                ("Nắp", "Cap"), ("Đóng nhờ trọng lực", "Gravity closure")],
            24, 286)
    _labels(o, [("Cổng vào", "Inlet"), ("Cổng ra", "Outlet"),
                ("Dòng thường", "Normal flow"),
                ("Ít cản trở", "Low resistance"),
                ("Đảo chiều tự đóng", "Reverse closes"),
                ("Tay cần", "Lever")], 368, 286)
    return _finish(w, h, o, *_cap(
        21, 218, "Van một chiều kiểu xoay", "Swing Check Valve",
        "Đĩa bản lề mở theo dòng thường và đóng khi dòng đảo chiều.",
        "Hinged disk opens with normal flow and closes when flow reverses."))


@_reg
def fig_f10_22():
    w, h = 680, 440
    o = _frame(w, h, "Van một chiều xoay có cần và quả tải",
               "Lever and Weight Swing Check Valve")
    _check(o, 340, 205, kind="lever")
    _labels(o, [("Thân van", "Body"), ("Đĩa xoay", "Disk"),
                ("Bản lề", "Hinge"), ("Cần", "Lever"),
                ("Quả tải", "Weight"), ("Đế van", "Seat ring")], 24, 286)
    _labels(o, [("Cổng vào", "Inlet"), ("Cổng ra", "Outlet"),
                ("Đóng nhanh", "Immediate closure"),
                ("Giảm sốc", "Limits shock"),
                ("Giảm rung đĩa", "Reduces disk chatter"),
                ("Nắp", "Cap")], 368, 286)
    return _finish(w, h, o, *_cap(
        22, 218, "Van một chiều xoay có cần và quả tải",
        "Lever and Weight Swing Check Valve",
        "Cần và quả tải giúp đóng nhanh, giảm sốc và rung đĩa khi đảo chiều.",
        "Outside lever and weight give immediate closure, limiting shock and disk chatter."))


@_reg
def fig_f10_23():
    w, h = 680, 440
    o = _frame(w, h, "Van một chiều kiểu nghiêng", "Tilting Check Valve")
    _check(o, 340, 205, kind="tilting")
    _labels(o, [("Thân van", "Body"), ("Đĩa nghiêng", "Tilting disk"),
                ("Vị trí bản lề", "Disk hinge location"),
                ("Đóng ngay", "Immediate closure"),
                ("Đế van", "Seat ring"), ("Dòng qua đĩa", "Flow over disk")],
            24, 286)
    _labels(o, [("Cổng vào", "Inlet"), ("Cổng ra", "Outlet"),
                ("Dòng thường", "Normal flow"),
                ("Ổn định đĩa", "Disk stability"),
                ("Trên 6 inch", "Above 6 in."),
                ("Lưu lượng thấp", "Low flow rate")], 368, 286)
    return _finish(w, h, o, *_cap(
        23, 218, "Van một chiều kiểu nghiêng", "Tilting Check Valve",
        "Bản lề đặt lệch giúp đóng ngay khi đảo chiều, chống va đập và rung đĩa.",
        "Offset disk hinge closes immediately on reversal, preventing slamming and chatter."))


@_reg
def fig_f10_24():
    w, h = 680, 440
    o = _frame(w, h, "Van một chiều nâng ngang",
               "Horizontal-Lift Check Valve")
    _check(o, 340, 205, kind="lift")
    _labels(o, [("Thân van", "Body"), ("Đĩa nâng", "Lift disk"),
                ("Đế van", "Seat ring"), ("Vòng nắp", "Cap ring"),
                ("Nắp", "Cap"), ("Nối ren", "Union")], 24, 286)
    _labels(o, [("Cổng vào", "Inlet"), ("Cổng ra", "Outlet"),
                ("Dòng thường", "Normal flow"),
                ("Dạng ngang", "Horizontal design"),
                ("Tổn thất áp", "Pressure drop"),
                ("Giống van cầu", "Globe-like path")], 368, 286)
    return _finish(w, h, o, *_cap(
        24, 219, "Van một chiều nâng ngang", "Horizontal-Lift Check Valve",
        "Đĩa nâng theo dòng chảy như van cầu, dùng khi tổn thất áp không quan trọng.",
        "Lift disk follows a globe-like flow path where pressure drop is not critical."))


@_reg
def fig_f10_25():
    w, h = 680, 430
    o = _frame(w, h, "Hệ thống gia nhiệt nước cấp điển hình",
               "Typical Feedheater System")
    o.append(_rect(60, 110, 150, 70, fill="#eef3fb", sw=1.4))
    o.append(T(135, 148, "Nguồn cấp / Feedwater", 7.4))
    o.append(_rect(270, 96, 150, 100, fill=FILL, sw=1.4))
    o.append(T(345, 140, "Bộ gia nhiệt", 8.0, weight="600"))
    o.append(T(345, 156, "Feedheater", 8.0, weight="600"))
    o.append(_rect(500, 110, 130, 70, fill="#eef3fb", sw=1.4))
    o.append(T(565, 148, "Lò hơi / Boiler", 7.4))
    for x0, x1, yy in ((210, 270, 145), (420, 500, 145)):
        o.append(_line(x0, yy, x1, yy, sw=1.4))
        _flow(o, x0 + 6, x1 - 6, yy)
    for vx in (238, 458):
        _vsym(o, vx, 145, 10, "gate")
    o.append(_line(345, 196, 345, 240, sw=1.4, color=GREEN))
    o.append(T(345, 256, "Hơi gia nhiệt / Heating steam", 7.2, color=GREEN))
    _labels(o, [("Van vào", "Inlet valve"), ("Van ra", "Outlet valve"),
                ("Ống dẫn nước", "Water piping"),
                ("Cảm báo mức nước", "Water level indicator")],
            26, 300, lh=22)
    _labels(o, [("Bảo vệ lò hơi", "Boiler protection"),
                ("Ngăn nước tràn ngược", "Isolate back-flow water"),
                ("Van 3 ngõ", "Three-way valves"),
                ("Điều khiển bằng điện", "Motor operated")],
            366, 300, lh=22)
    return _finish(w, h, o, *_cap(
        25, 219, "Hệ thống gia nhiệt nước cấp điển hình",
        "Typical Feedheater System",
        "Sơ đồ hệ thống gia nhiệt nước cấp với van vào, van ra và hơi gia nhiệt.",
        "Typical feedwater heater system with inlet and outlet valves and heating steam."))


@_reg
def fig_f10_26():
    w, h = 680, 450
    o = _frame(w, h, "Hoạt động bình thường và chuyển tải",
               "Normal and Bypass Operations")
    o.append(T(190, 78, "Bình thường / Normal", 8.4, weight="600"))
    o.append(T(490, 78, "Chuyển tải / Bypass", 8.4, weight="600"))
    for ox, bypass in ((190, False), (490, True)):
        o.append(_rect(ox - 76, 120, 152, 66, fill=FILL, sw=1.4))
        o.append(T(ox, 157, "Bộ gia nhiệt", 7.6, weight="600"))
        o.append(T(ox, 172, "Heater", 7.2))
        o.append(_line(ox - 140, 153, ox - 76, 153, sw=1.3))
        o.append(_line(ox + 76, 153, ox + 140, 153, sw=1.3))
        _vsym(o, ox - 96, 153, 9, "gate")
        _vsym(o, ox + 96, 153, 9, "gate")
        o.append(_arrow(ox - 134, 153, ox - 108, 153, sw=1.2, color=BLUE))
        if bypass:
            o.append(_line(ox - 110, 104, ox + 110, 104, sw=1.4, color=GREEN))
            _flow(o, ox - 90, ox + 90, 104, "Đường tắt / Bypass")
        else:
            _flow(o, ox - 130, ox - 108, 178, "Nước / Water")
    _labels(o, [("Van vào mở", "Inlet open"), ("Van ra mở", "Outlet open"),
                ("Nước qua bộ gia nhiệt", "Water through heater")],
            24, 330, lh=22)
    _labels(o, [("Hai van đóng", "Both valves closed"),
                ("Nước đi qua đường tắt", "Water via bypass"),
                ("Cô lập bộ gia nhiệt", "Heater isolated")],
            368, 330, lh=22)
    return _finish(w, h, o, *_cap(
        26, 219, "Hoạt động bình thường và chuyển tải",
        "Normal and Bypass Operations",
        "So sánh chế độ bình thường và chế độ chuyển tải của van 3 ngõ.",
        "Comparison of normal operation and bypass operation of three-way valves."))


@_reg
def fig_f10_27():
    w, h = 680, 430
    o = _frame(w, h, "Van cô lập bộ gia nhiệt lại",
               "Reheater Isolation Valve")
    _pipe(o, 340, 205, 360, 66)
    o.append(_rect(268, 139, 144, 132, fill="#eef3fb", sw=1.4))
    o.append(_rect(300, 170, 80, 70, fill="#ffffff", sw=1.2))
    o.append(T(340, 208, "Blind", 8.4, weight="600", color=RED))
    o.append(_line(340, 139, 340, 90, sw=2.0))
    o.append(_rect(298, 108, 84, 30, fill="#d9e2ee", sw=1.2))
    o.append(T(340, 128, "Nắp ép / Pressure cover", 6.6))
    _flow(o, 172, 255, 205)
    _arrow(428, 205, 508, 205, sw=1.4, color=BLUE)
    _labels(o, [("Thân rỗng toàn lưu", "Full-bore empty body"),
                ("Tấm chắn tạm", "Removable blind"),
                ("Gioăng O-ring", "O-ring seal"),
                ("Ít tổn thất áp", "Minimal pressure loss")],
            24, 310, lh=22)
    _labels(o, [("Nắp vào lớn", "Large access cover"),
                ("Thử áp lực", "Hydro-test"),
                ("Tháo tấm sau thử", "Remove plate after test"),
                ("Vận hành bình thường", "Normal full-bore line")],
            368, 310, lh=22)
    return _finish(w, h, o, *_cap(
        27, 220, "Van cô lập bộ gia nhiệt lại", "Reheater Isolation Valve",
        "Van cô lập bộ gia nhiệt lại có thân rỗng và nắp ép để lắp tấm chắn thử áp.",
        "Reheater isolation valve with a full-bore body and pressure cover for a test blind."))


@_reg
def fig_f10_28():
    w, h = 680, 430
    o = _frame(w, h, "Van chiết tuabin", "Turbine Extraction Valve")
    _check(o, 340, 205, kind="swing")
    o.append(_rect(230, 90, 74, 56, fill="#eef3fb", sw=1.3))
    o.append(T(267, 122, "Khí nén", 7.2))
    o.append(_line(267, 146, 340, 172, sw=1.6, color=RED))
    o.append(T(267, 82, "Bộ truyền đơn tác", 6.8, color=RED))
    _labels(o, [("Van một chiều xoay", "Swing check valve"),
                ("Bộ truyền khí nén", "Pneumatic actuator"),
                ("Đóng nhanh", "Fast closure"),
                ("Đóng kín chắc", "Positive tight seating")],
            24, 306, lh=22)
    _labels(o, [("Hơi chiết", "Extraction steam"),
                ("Ngăn hơi quay lại tuabin", "Prevent return to turbine"),
                ("Bảo vệ khi nhả tải", "Protection on trip"),
                ("Đóng có hỗ trợ", "Power-assisted closure")],
            368, 306, lh=22)
    return _finish(w, h, o, *_cap(
        28, 221, "Van chiết tuabin", "Turbine Extraction Valve",
        "Van một chiều có bộ truyền khí nén, đóng nhanh khi tuabin nhả tải.",
        "Swing check valve with a single-acting pneumatic actuator for fast trip closure."))


@_reg
def fig_f10_29():
    w, h = 680, 430
    o = _frame(w, h, "Van chuyển tải", "Bypass Valve")
    _pipe(o, 300, 210, 320, 54)
    _vsym(o, 300, 210, 16, "gate")
    o.append(_line(300, 194, 300, 120, sw=1.4))
    o.append(T(300, 110, "Van chính / Main valve", 7.0))
    o.append(_rect(430, 132, 180, 48, fill="#eef3fb", sw=1.3))
    o.append(_line(410, 210, 430, 168, sw=1.3, color=GREEN))
    o.append(_line(520, 168, 520, 210, sw=1.3, color=GREEN))
    _vsym(o, 520, 210, 11, "globe")
    o.append(T(520, 166, "Van tắt / Bypass", 7.0, color=GREEN))
    _flow(o, 142, 240, 210)
    o.append(T(250, 272, "Hở / Open", 7.0, color=GREEN))
    _labels(o, [("Cân bằng áp suất", "Equalize pressure"),
                ("Gia nhiệt đường ống", "Warm up downstream"),
                ("Ty song song", "Parallel stems")], 24, 312, lh=22)
    _labels(o, [("Van nhỏ hơn", "Smaller valve"),
                ("Áp suất và nhiệt cao", "High pressure and temperature"),
                ("Mở van chính an toàn", "Safe main-valve opening")],
            368, 312, lh=22)
    return _finish(w, h, o, *_cap(
        29, 221, "Van chuyển tải", "Bypass Valve",
        "Van nhỏ dùng cân bằng áp suất và gia nhiệt trước khi mở van chính.",
        "Smaller valve used to equalize pressure and warm up piping before the main valve opens."))


@_reg
def fig_f10_30():
    w, h = 680, 470
    o = _frame(w, h, "Đường chuyển tải và các kết nối phụ",
               "Bypass and Auxiliary Connections")
    o.append(_line(90, 120, 590, 120, sw=1.6))
    for x in (150, 260, 370, 480):
        _vsym(o, x, 120, 14, "gate")
    o.append(T(150, 92, "Cổng / Gate", 7.0))
    o.append(T(260, 92, "Cầu / Globe", 7.0))
    o.append(T(370, 92, "Góc / Angle", 7.0))
    o.append(T(480, 92, "Kiểm / Check", 7.0))
    o.append(_line(90, 200, 590, 200, sw=1.6, color=GREEN))
    _vsym(o, 320, 200, 14, "globe")
    o.append(T(320, 176, "Van chính / Main valve", 7.0))
    for x in (150, 260, 370, 480):
        o.append(_line(x, 134, x, 200, sw=1.0, color=GREY, dash="4,3"))
        o.append(_circle(x, 167, 3, fill="#ffffff", sw=1.0))
    o.append(T(340, 232, "Vị trí nối ren điển hình / Typical tapped locations",
               7.0, color=GREY))
    widths = [180, 180, 180]
    _table(o, 70, 256, widths,
           [("Cỡ van chính / Main valve", "middle"),
            ("Cỡ van tắt / Bypass", "middle"),
            ("Ghi chú / Note", "middle")],
           [[("2 - 4 in. (50 - 100 mm)", "middle"),
             ("1/2 in. (15 mm)", "middle"), ("Ren / Tapped", "middle")],
            [("5 - 8 in. (125 - 200 mm)", "middle"),
             ("3/4 in. (20 mm)", "middle"), ("Ren / Tapped", "middle")],
            [("10 - 24 in. (250 - 600 mm)", "middle"),
             ("1 in. (25 mm)", "middle"), ("Ren / Tapped", "middle")]],
           rh=26, hh=30, fs=7.4)
    return _finish(w, h, o, *_cap(
        30, 221, "Đường chuyển tải và các kết nối phụ",
        "Bypass and Auxiliary Connections",
        "Vị trí và kích cỡ đường chuyển tải và các kết nối phụ theo cỡ van chính.",
        "Standard bypass and auxiliary connection locations and sizes by main valve size."))


@_reg
def fig_f10_31():
    w, h = 680, 440
    o = _frame(w, h, "Van màng kiểu đập", "Weir-Type Diaphragm Valve")
    _diaphragm(o, 340, 205, weir=True)
    _labels(o, [("Thân van", "Valve body"), ("Lót thân", "Valve liner"),
                ("Đập", "Weir"), ("Màng", "Diaphragm"),
                ("Bình nén", "Compressor"), ("Nắp van", "Bonnet")], 24, 286)
    _labels(o, [("Cổng vào", "Inlet"), ("Cổng ra", "Outlet"),
                ("Ty van", "Stem"), ("Tay vặn", "Handwheel"),
                ("Hành trình ngắn", "Short travel"),
                ("Tuổi thọ màng cao", "Long diaphragm life")], 368, 286)
    return _finish(w, h, o, *_cap(
        31, 222, "Van màng kiểu đập", "Weir-Type Diaphragm Valve",
        "Van màng có đập ở giữa thân làm điểm đóng, hành trình màng ngắn.",
        "Weir-type diaphragm valve with a raised weir as the closure point."))


@_reg
def fig_f10_32():
    w, h = 680, 440
    o = _frame(w, h, "Van màng kiểu thẳng",
               "Straightway-Type Diaphragm Valve")
    _diaphragm(o, 340, 205, weir=False)
    _labels(o, [("Thân van", "Valve body"), ("Lót thân", "Valve liner"),
                ("Màng", "Diaphragm"), ("Nắp van", "Bonnet"),
                ("Ty van", "Stem"), ("Tay vặn", "Handwheel")], 24, 286)
    _labels(o, [("Cổng vào", "Inlet"), ("Cổng ra", "Outlet"),
                ("Đường chảy thông suốt", "Uninterrupted passage"),
                ("Dùng cho chất nhớt", "For viscous flow"),
                ("Có chất rắn", "With solids"),
                ("Hành trình dài hơn", "Longer travel")], 368, 286)
    return _finish(w, h, o, *_cap(
        32, 222, "Van màng kiểu thẳng", "Straightway-Type Diaphragm Valve",
        "Van màng không có đập, đường chảy thông suốt phù hợp chất nhớt và chất rắn.",
        "Straightway diaphragm valve with no weir, suited to viscous or solids-laden flow."))


@_reg
def fig_f10_33():
    w, h = 680, 440
    o = _frame(w, h, "Van ép khí nén", "Air-Operated Pinch Valve")
    o.append(T(185, 76, "Van mở / Valve open", 8.0, weight="600"))
    o.append(T(495, 76, "Van ép đóng / Pinched closed", 8.0, weight="600"))
    _pinch(o, 185, 202, closed=False)
    _pinch(o, 495, 202, closed=True)
    o.append(_arrow(185, 176, 185, 144, sw=1.4, color=BLUE))
    o.append(_arrow(495, 176, 495, 144, sw=1.4, color=BLUE))
    _labels(o, [("Ống mềm rỗng", "Flexible hollow sleeve"),
                ("Đầu cấp khí", "Air tap"),
                ("Dòng chảy tự do", "Free flow"),
                ("Chịu mài mòn", "Abrasion resistant")], 24, 300, lh=21)
    _labels(o, [("Ép ống để đóng", "Sleeve pinched shut"),
                ("Bụi và bùn", "Slurries and powders"),
                ("Không bộ phận kim loại", "No metal parts in flow"),
                ("Đóng kín", "Tight shutoff")], 368, 300, lh=21)
    return _finish(w, h, o, *_cap(
        33, 222, "Van ép khí nén", "Air-Operated Pinch Valve",
        "Van ép dùng ống mềm bị ép đóng bằng khí nén, hợp cho bùn và bột.",
        "Air-operated pinch valve closing a hollow sleeve, ideal for slurries and powders."))


@_reg
def fig_f10_34():
    w, h = 680, 450
    o = _frame(w, h, "Van bi cổng thu nhỏ", "Reduced-Port Ball Valve")
    _ball(o, 340, 205)
    _labels(o, [("Thân van", "Valve body"), ("Bi", "Ball"),
                ("Cổng thu nhỏ", "Reduced port"), ("Đế van", "Seat ring"),
                ("Gland", "Gland"), ("Đệm tạp", "Gland packing")],
            24, 292, lh=20)
    _labels(o, [("Ty van", "Stem"), ("Tay cầm", "Handle assembly"),
                ("Bản chỉ thị", "Indicator plate"),
                ("Đai ốc gland", "Gland nut"),
                ("Thân nhiều mảnh", "Multi-piece body"),
                ("Xoay 90 độ", "Quarter turn")], 368, 292, lh=20)
    return _finish(w, h, o, *_cap(
        34, 223, "Van bi cổng thu nhỏ", "Reduced-Port Ball Valve",
        "Van bi cổng thu nhỏ có bi rỗng quay 90 độ để đóng dòng chảy.",
        "Reduced-port ball valve with a bored ball that stops flow in a quarter turn."))


@_reg
def fig_f10_35():
    w, h = 680, 440
    o = _frame(w, h, "Van bướm kiểu kẹp", "Wafer-Type Butterfly Valve")
    _butterfly(o, 340, 205, mount="wafer")
    _labels(o, [("Thân van", "Body"), ("Đĩa bướm", "Disk"),
                ("Trục ty", "Stem shaft"), ("Đệm mềm", "Resilient seat"),
                ("Lỗ bắt", "Mounting holes"),
                ("Đường kính cổng", "Port diameter")], 24, 316, lh=20)
    _labels(o, [("Kẹp giữa hai bích", "Between two flanges"),
                ("Bulông bích giữ", "Held by flange bolts"),
                ("Xoay 90 độ", "Quarter turn"),
                ("Điều tiết dòng", "Flow regulation"),
                ("Nhẹ và gọn", "Light and compact"),
                ("Nhìn từ trên", "Top view")], 368, 316, lh=20)
    return _finish(w, h, o, *_cap(
        35, 223, "Van bướm kiểu kẹp", "Wafer-Type Butterfly Valve",
        "Van bướm kiểu kẹp đặt giữa hai bích, đĩa quay 90 độ để mở hoặc đóng.",
        "Wafer butterfly valve mounted between flanges, with a quarter-turn disk."))


@_reg
def fig_f10_36():
    w, h = 680, 440
    o = _frame(w, h, "Van bướm kiểu tai", "Lug-Butterfly Valve")
    _butterfly(o, 340, 205, mount="lug")
    _labels(o, [("Thân van", "Body"), ("Đĩa bướm", "Disk"),
                ("Trục ty", "Stem shaft"), ("Đệm mềm", "Resilient seat"),
                ("Tai bắt ren", "Connecting lugs"),
                ("Đường kính cổng", "Port diameter")], 24, 316, lh=20)
    _labels(o, [("Giữ khi tháo một bích", "Holds if one flange is removed"),
                ("Bulông vặn vào tai", "Bolts screw into tapped lugs"),
                ("Tự làm gioăng", "Seal acts as gasket"),
                ("Xoay 90 độ", "Quarter turn"),
                ("Dùng khi tháo thiết bị", "For dismantling lines"),
                ("Nhìn từ trên", "Top view")], 368, 316, lh=20)
    return _finish(w, h, o, *_cap(
        36, 223, "Van bướm kiểu tai", "Lug-Butterfly Valve",
        "Van bướm kiểu tai có tai ren giữ van khi tháo một bích đường ống.",
        "Lug butterfly valve with tapped lugs that hold it when one flange is removed."))


@_reg
def fig_f10_37():
    w, h = 680, 440
    o = _frame(w, h, "Van bướm hai mặt bích",
               "Double-Flanged Butterfly Valve")
    _butterfly(o, 340, 205, mount="flanged")
    _labels(o, [("Thân van", "Body"), ("Đĩa", "Disk"),
                ("Chốt đĩa", "Disk pin"), ("Trục ty", "Stem shaft"),
                ("Gland", "Gland"), ("Đệm tạp", "Gland packing")],
            24, 316, lh=20)
    _labels(o, [("Mặt bích nối", "Connecting flange"),
                ("Bulông bích", "Flange bolts"),
                ("Gioăng giữa", "Gaskets between ends"),
                ("Đai ốc gland", "Gland nut"),
                ("Xoay 90 độ", "Quarter turn"),
                ("Nhìn từ trên", "Top view")], 368, 316, lh=20)
    return _finish(w, h, o, *_cap(
        37, 224, "Van bướm hai mặt bích", "Double-Flanged Butterfly Valve",
        "Van bướm có hai mặt bích bắt riêng vào thiết bị, có gioăng ở giữa.",
        "Double-flanged butterfly valve bolted individually into pipework with gaskets."))


@_reg
def fig_f10_38():
    w, h = 680, 440
    o = _frame(w, h, "Van cắm bôi trơn", "Lubricated Plug Valve")
    _plug(o, 340, 205, multiport=False)
    _labels(o, [("Thân van", "Valve body"), ("Cắm", "Plug"),
                ("Rãnh dầu", "Lubricant grooves"),
                ("Vít dầu", "Lubricant screw"),
                ("Nắp gland", "Gland cover plate"),
                ("Đệm tạp", "Gland packing")], 24, 312, lh=20)
    _labels(o, [("Đường chảy", "Flow way"), ("Ty van", "Stem"),
                ("Gland", "Gland"), ("Bôi trơn bề mặt", "Lubricated seating"),
                ("Chống kẹt", "Prevents seizing"),
                ("Làm kín chắc", "Positive seal")], 368, 312, lh=20)
    return _finish(w, h, o, *_cap(
        38, 224, "Van cắm bôi trơn", "Lubricated Plug Valve",
        "Van cắm có rãnh dầu bôi trơn bề mặt làm kín, chống kẹt và đóng kín.",
        "Lubricated plug valve with grooves feeding lubricant to the seating surfaces."))


@_reg
def fig_f10_39():
    w, h = 680, 450
    o = _frame(w, h, "Van cắm nhiều cổng", "Multi-Port Plug Valve")
    o.append(T(160, 80, "Ba ngõ / Three-way", 7.6, weight="600"))
    o.append(T(340, 80, "Ba cổng / Three-port", 7.6, weight="600"))
    o.append(T(520, 80, "Bốn ngõ / Four-way", 7.6, weight="600"))
    _plug(o, 160, 230, multiport=True)
    _plug(o, 340, 230, multiport=True)
    _plug(o, 520, 230, multiport=True)
    o.append(T(160, 372, "3 ngõ 3 cổng", 7.0, color=GREY))
    o.append(T(340, 372, "3 ngõ 2 cổng", 7.0, color=GREY))
    o.append(T(520, 372, "4 ngõ 4 cổng", 7.0, color=GREY))
    o.append(T(340, 404, "Cấu hình cổng phổ biến / Common port configurations",
               7.2, color=GREY))
    return _finish(w, h, o, *_cap(
        39, 224, "Van cắm nhiều cổng", "Multi-Port Plug Valve",
        "Các cấu hình van cắm nhiều cổng: ba ngõ ba cổng, ba ngõ hai cổng và bốn ngõ.",
        "Multi-port plug valve configurations: three-way three-port, three-way two-port and four-way."))


# ===========================================================================
# Figure 10.40 - 10.53 : dimension tables (faithful transcription)
# ===========================================================================
@_reg
def fig_f10_40():
    w = 680
    x, y = 11, 68
    widths = [46, 38] + [48] * 12
    groups = [(2, 2, "Flat Face Class 125\nSolid wedge"),
              (4, 2, "Class 125\nDouble disk"),
              (6, 2, "Raised Face Class 250\nSolid wedge"),
              (8, 2, "Class 250\nDouble disk"),
              (10, 2, "Raised Face Class 800\nSolid wedge"),
              (12, 2, "Class 800\nDouble disk")]
    hdr = ["Inch", "mm"] + ["in", "mm"] * 6
    rows = _rr("""
1/4 8 --- --- --- --- --- --- --- --- --- --- --- ---
3/8 10 --- --- --- --- --- --- --- --- --- --- --- ---
1/2 15 --- --- --- --- --- --- --- --- --- --- --- ---
3/4 20 --- --- --- --- --- --- --- --- --- --- --- ---
1 25 --- --- --- --- --- --- --- --- --- --- --- ---
1-1/4 32 --- --- --- --- --- --- --- --- --- --- --- ---
1-1/2 40 --- --- --- --- --- --- --- --- --- --- --- ---
2 50 7.00 177.8 7.00 177.8 8.50 215.9 8.50 215.9 11.50 292.1 11.50 292.1
2-1/2 65 7.50 190.5 7.50 190.5 9.50 241.3 9.50 241.3 13.00 330.2 13.00 330.2
3 80 8.00 203.2 8.00 203.2 11.12 282.5 11.12 282.5 14.0 355.6 14.00 355.6
4 100 9.00 228.6 9.00 228.6 12.00 304.8 12.00 304.8 17.00 431.8 17.00 431.8
5 125 10.00 254.0 10.00 254.0 15.00 381.0 15.00 381.0 --- --- --- ---
6 150 10.50 266.7 10.50 266.7 15.88 403.4 15.88 403.4 22.00 558.8 22.00 558.8
8 200 11.50 292.1 11.50 292.1 16.50 419.1 16.50 419.1 26.00 660.4 26.00 660.4
10 250 13.00 330.2 13.00 330.2 18.00 457.2 18.00 457.2 31.00 787.4 31.00 787.4
12 300 14.00 355.6 14.00 355.6 19.75 501.7 19.75 501.7 33.00 838.2 33.00 838.2
14 350 15.00 381.0 --- --- 22.50 571.5 22.50 571.5 --- --- --- ---
16 400 16.00 406.4 --- --- 24.00 609.6 24.00 609.6 --- --- --- ---
18 450 17.00 431.8 --- --- 26.00 660.4 26.00 660.4 --- --- --- ---
20 500 18.00 457.2 --- --- 28.00 711.2 28.00 711.2 --- --- --- ---
22 550 --- --- --- --- --- --- --- --- --- --- --- ---
24 600 20.00 508.0 --- --- 31.00 787.4 31.00 787.4 --- --- --- ---
26 650 --- --- --- --- --- --- --- --- --- --- --- ---
28 700 --- --- --- --- --- --- --- --- --- --- --- ---
30 750 --- --- --- --- --- --- --- --- --- --- --- ---
32 800 --- --- --- --- --- --- --- --- --- --- --- ---
34 850 --- --- --- --- --- --- --- --- --- --- --- ---
36 900 --- --- --- --- --- --- --- --- --- --- --- ---
""")
    o = _frame(w, 620, "Van cổng gang", "Cast Iron Gate Valves")
    o.append(T(340, 58, "Kích thước tính theo mặt giáp bích / Face-to-face dimensions",
               6.8, color=GREY))
    end = _dim_table(o, x, y, widths, groups, hdr, rows)
    _notes(o, 12, end + 6, [
        "Ghi chú: (---) = cỡ không nêu trong ASME/ANSI nhưng có thể có trên thị trường.",
        "mm làm tròn đến một chữ số thập phân. Theo ASME/ANSI B16.10.",
    ])
    return _finish(w, 620, o, *_cap(
        40, 225, "Van cổng gang", "Cast Iron Gate Valves",
        "Bảng kích thước van cổng gang ANSI Class 125, 250 và 800.",
        "Dimension table for cast iron gate valves, ANSI Classes 125, 250 and 800.",
        "Bảng Hình 10.40 (tr. 225) kích thước van cổng gang bằng inch và mm",
        "Table of Figure 10.40 (p. 225) cast iron gate valve dimensions"))


@_reg
def fig_f10_41():
    w = 680
    x, y = 11, 74
    widths = [46, 38] + [48] * 12
    groups = [(2, 2, "Flat Face Class 125\nStraightway"),
              (4, 2, "Class 125\nAngle"),
              (6, 2, "Class 125\nControl style"),
              (8, 2, "Raised Face Class 250\nStraightway"),
              (10, 2, "Class 250\nAngle"),
              (12, 2, "Class 250\nControl style")]
    hdr = ["Inch", "mm"] + ["in", "mm"] * 6
    rows = _rr("""
1/4 8 --- --- --- --- --- --- --- --- --- --- --- ---
3/8 10 --- --- --- --- --- --- --- --- --- --- --- ---
1/2 15 --- --- --- --- --- --- --- --- --- --- 7.50 190.5
3/4 20 --- --- --- --- --- --- --- --- --- --- 7.62 193.5
1 25 --- --- --- --- 7.25 190.5 --- --- --- --- 7.55 196.9
1-1/4 32 --- --- --- --- --- --- --- --- --- --- --- ---
1-1/2 40 --- --- --- --- 8.75 222.3 --- --- --- --- 9.25 235.0
2 50 8.00 203.2 4.00 101.6 10.00 254.0 10.50 266.7 5.25 133.4 10.50 266.7
2-1/2 65 8.50 215.9 4.25 107.0 10.88 276.4 11.50 292.1 5.75 146.1 11.50 292.1
3 80 9.50 241.3 4.75 120.7 11.75 298.5 12.50 317.5 6.25 158.8 12.50 317.5
4 100 11.50 292.1 5.75 146.1 13.88 352.6 14.00 355.6 7.00 177.8 14.50 368.3
5 125 13.00 330.2 6.50 165.1 --- --- 15.75 400.1 7.88 200.2 --- ---
6 150 14.00 355.6 7.00 177.8 17.75 450.9 17.50 444.5 8.75 222.3 18.62 473.0
8 200 19.50 495.3 9.75 247.7 21.38 543.1 21.00 533.4 10.50 266.7 22.38 568.5
10 250 24.50 622.3 12.25 311.1 26.50 673.1 24.50 622.3 12.25 311.2 27.88 708.2
12 300 27.50 698.5 13.75 349.3 29.00 736.6 28.00 711.2 14.00 355.6 30.50 774.7
14 350 31.00 787.4 15.50 393.7 35.00 889.0 --- --- --- --- 36.50 927.1
16 400 36.00 914.4 18.00 457.2 40.00 1016.0 --- --- --- --- 41.62 1057.2
18 450 --- --- --- --- --- --- --- --- --- --- --- ---
20 500 --- --- --- --- --- --- --- --- --- --- --- ---
22 550 --- --- --- --- --- --- --- --- --- --- --- ---
24 600 --- --- --- --- --- --- --- --- --- --- --- ---
26 650 --- --- --- --- --- --- --- --- --- --- --- ---
28 700 --- --- --- --- --- --- --- --- --- --- --- ---
30 750 --- --- --- --- --- --- --- --- --- --- --- ---
32 800 --- --- --- --- --- --- --- --- --- --- --- ---
36 900 --- --- --- --- --- --- --- --- --- --- --- ---
""")
    o = _frame(w, 620, "Van cầu gang", "Cast Iron Globe Valves")
    o.append(T(340, 64, "Mặt giáp bích cho van thẳng; tâm đến mặt cho van góc / Face-to-face and center-to-face",
               6.4, color=GREY))
    end = _dim_table(o, x, y, widths, groups, hdr, rows, fs=6.5)
    _notes(o, 12, end + 6, [
        "Ghi chú: (---) = cỡ không nêu trong ASME/ANSI. mm làm tròn 1 chữ số. Theo B16.10.",
        "Kích thước van một chiều thẳng và góc trùng với van cầu thẳng và góc.",
    ])
    return _finish(w, 620, o, *_cap(
        41, 226, "Van cầu gang", "Cast Iron Globe Valves",
        "Bảng kích thước van cầu gang ANSI Class 125 và 250, kiểu thẳng và góc.",
        "Dimension table for cast iron globe valves, ANSI Classes 125 and 250.",
        "Bảng Hình 10.41 (tr. 226) kích thước van cầu gang bằng inch và mm",
        "Table of Figure 10.41 (p. 226) cast iron globe valve dimensions"))


@_reg
def fig_f10_42():
    w = 680
    x, y = 11, 68
    widths = [46, 38] + [72] * 8
    groups = [(2, 2, "Class 150 Raised Face\nSolid wedge"),
              (4, 2, "Class 150 Raised Face\nDouble disk"),
              (6, 2, "Class 150 Beveled End\nSolid wedge"),
              (8, 2, "Class 150 Beveled End\nDouble disk")]
    hdr = ["Inch", "mm"] + ["in", "mm"] * 4
    rows = _rr("""
1/4 8 4.00 101.6 4.00 101.6 4.00 101.6 4.00 101.6
3/8 10 4.00 101.6 4.00 101.6 4.00 101.6 4.00 101.6
1/2 15 4.25 108.0 4.25 108.0 4.25 108.0 4.25 108.0
3/4 20 4.62 117.4 4.62 117.4 4.62 117.4 4.62 117.4
1 25 5.00 127.0 5.00 127.0 5.00 127.0 5.00 127.0
1-1/4 32 5.50 139.7 5.50 139.7 5.50 139.7 5.50 139.7
1-1/2 40 6.50 165.1 6.50 165.1 6.50 165.1 6.50 165.1
2 50 7.00 177.8 7.00 177.8 8.50 215.9 8.50 215.9
2-1/2 65 7.50 190.5 7.50 190.5 9.50 241.3 9.50 241.3
3 80 8.00 203.2 8.00 203.2 11.12 282.5 11.12 282.5
4 100 9.00 228.6 9.00 228.6 12.00 304.8 12.00 304.8
5 125 10.00 254.0 10.00 254.0 15.00 381.0 15.00 381.0
6 150 10.50 266.7 10.50 266.7 15.88 403.4 15.88 403.4
8 200 11.50 292.1 11.50 292.1 16.50 419.1 16.50 419.1
10 250 13.00 330.2 13.00 330.2 18.00 457.2 18.00 457.2
12 300 14.00 355.6 14.00 355.6 19.75 501.7 19.75 501.7
14 350 15.00 381.0 15.00 381.0 22.50 571.5 22.50 571.5
16 400 16.00 406.4 16.00 406.4 24.00 609.6 24.00 609.6
18 450 17.00 431.8 17.00 431.8 26.00 660.4 26.00 660.4
20 500 18.00 457.2 18.00 457.2 28.00 711.2 28.00 711.2
22 550 --- --- --- --- 30.00 762.0 30.00 762.0
24 600 20.00 508.0 20.00 508.0 32.00 812.8 32.00 812.8
26 650 22.00 558.8 22.00 558.8 --- --- 34.00 863.6
28 700 24.00 609.6 24.00 609.6 --- --- 36.00 914.4
30 750 24.00 609.6 24.00 609.6 --- --- 36.00 914.4
32 800 --- --- --- --- --- --- 38.00 965.2
34 850 --- --- --- --- --- --- 40.00 1016
36 900 28.00 711.2 28.00 711.2 --- --- 40.00 1016
""")
    o = _frame(w, 610, "Van cổng thép (Cấp 150)", "Steel Gate Valve (Class 150)")
    o.append(T(340, 58, "Kích thước theo mặt giáp bích và đầu bịt / Face-to-face and end-to-end",
               6.8, color=GREY))
    end = _dim_table(o, x, y, widths, groups, hdr, rows)
    _notes(o, 12, end + 6, [
        "Ghi chú: (---) = cỡ không nêu trong ASME/ANSI. mm làm tròn 1 chữ số. Theo B16.10.",
    ])
    return _finish(w, 610, o, *_cap(
        42, 227, "Van cổng thép (Cấp 150)", "Steel Gate Valve (Class 150)",
        "Bảng kích thước van cổng thép ANSI Class 150, nêm đặc và đĩa đôi.",
        "Dimension table for steel gate valves, ANSI Class 150, solid wedge and double disk.",
        "Bảng Hình 10.42 (tr. 227) kích thước van cổng thép Class 150",
        "Table of Figure 10.42 (p. 227) steel gate valve Class 150 dimensions"))


@_reg
def fig_f10_43():
    w = 680
    x, y = 11, 68
    widths = [46, 38] + [72] * 8
    groups = [(2, 2, "Class 300 Raised Face\nSolid wedge"),
              (4, 2, "Class 300 Raised Face\nDouble disk"),
              (6, 2, "Class 300 Beveled End\nSolid wedge"),
              (8, 2, "Class 300 Beveled End\nDouble disk")]
    hdr = ["Inch", "mm"] + ["in", "mm"] * 4
    rows = _rr("""
1/4 8 --- --- --- --- --- --- --- ---
3/8 10 --- --- --- --- --- --- --- ---
1/2 15 5.50 139.7 --- --- 5.50 139.7 --- ---
3/4 20 6.00 152.4 --- --- 6.00 152.4 --- ---
1 25 6.50 165.1 --- --- 6.50 165.1 --- ---
1-1/4 32 7.00 177.8 --- --- 7.00 177.8 --- ---
1-1/2 40 7.50 190.5 7.50 190.5 7.50 190.5 7.50 190.5
2 50 8.50 215.9 8.50 215.9 8.50 215.9 8.50 215.9
2-1/2 65 9.50 241.3 9.50 241.3 9.50 241.3 9.50 241.3
3 80 11.12 282.5 11.12 282.5 11.12 282.5 11.12 282.5
4 100 12.00 304.8 12.00 304.8 12.00 304.8 12.00 304.8
5 125 15.00 381.0 15.00 381.0 15.00 381.0 15.00 381.0
6 150 15.88 403.4 15.88 403.4 15.88 403.4 15.88 403.4
8 200 16.50 419.1 16.50 419.1 16.50 419.1 16.50 419.1
10 250 18.00 457.2 18.00 457.2 18.00 457.2 18.00 457.2
12 300 19.75 501.7 19.75 501.7 19.75 501.7 19.75 501.7
14 350 30.00 762.0 30.00 762.0 30.00 762.0 30.00 762.0
16 400 33.00 838.2 33.00 838.2 33.00 838.2 33.00 838.2
18 450 36.00 914.4 36.00 914.4 36.00 914.4 36.00 914.4
20 500 39.00 990.6 39.00 990.6 39.00 990.6 39.00 990.6
22 550 43.00 1092.2 43.00 1092.2 43.00 1092.2 43.00 1092.2
24 600 45.00 1143.0 45.00 1143.0 45.00 1143.0 45.00 1143.0
26 650 49.00 1244.6 49.00 1244.6 49.00 1244.6 49.00 1244.6
28 700 53.00 1346.2 53.00 1346.2 53.00 1346.2 53.00 1346.2
30 750 55.00 1397.0 55.00 1397.0 55.00 1397.0 55.00 1397.0
32 800 60.00 1524.0 60.00 1524.0 60.00 1524.0 60.00 1524.0
34 850 64.00 1625.6 64.00 1625.6 64.00 1625.6 64.00 1625.6
36 900 68.00 1727.2 68.00 1727.2 68.00 1727.2 68.00 1727.2
""")
    o = _frame(w, 610, "Van cổng thép (Cấp 300)", "Steel Gate Valve (Class 300)")
    o.append(T(340, 58, "Kích thước theo mặt giáp bích và đầu bịt / Face-to-face and end-to-end",
               6.8, color=GREY))
    end = _dim_table(o, x, y, widths, groups, hdr, rows)
    _notes(o, 12, end + 6, [
        "Ghi chú: (---) = cỡ không nêu trong ASME/ANSI. mm làm tròn 1 chữ số. Theo B16.10.",
    ])
    return _finish(w, 610, o, *_cap(
        43, 228, "Van cổng thép (Cấp 300)", "Steel Gate Valve (Class 300)",
        "Bảng kích thước van cổng thép ANSI Class 300, nêm đặc và đĩa đôi.",
        "Dimension table for steel gate valves, ANSI Class 300, solid wedge and double disk.",
        "Bảng Hình 10.43 (tr. 228) kích thước van cổng thép Class 300",
        "Table of Figure 10.43 (p. 228) steel gate valve Class 300 dimensions"))


@_reg
def fig_f10_44():
    w = 680
    x, y = 11, 76
    widths = [46, 38] + [41] * 14
    groups = [(2, 2, "Class 400\nSolid wedge"),
              (4, 2, "Class 400\nDouble disk"),
              (6, 2, "Class 600 Raised Face\nSolid wedge"),
              (8, 2, "Class 600 Raised Face\nDouble disk"),
              (10, 2, "Class 600 Beveled End\nSolid wedge"),
              (12, 2, "Class 600 Beveled End\nDouble disk"),
              (14, 2, "Short pattern")]
    hdr = ["Inch", "mm"] + ["in", "mm"] * 7
    rows = _rr("""
1/2 15 6.5 165.1 --- --- 6.5 165.1 --- --- 6.50 165.1 --- --- --- ---
3/4 20 7.5 190.5 --- --- 7.5 190.5 --- --- 7.5 190.5 --- --- --- ---
1 25 8.5 215.9 8.5 215.9 8.5 215.9 8.5 215.9 8.5 215.9 8.5 215.9 5.25 133.4
1-1/4 32 9.0 228.6 9.0 228.6 9.0 228.6 9.0 228.6 9.0 228.6 9.0 228.6 5.75 146.1
1-1/2 40 9.5 241.3 9.5 241.3 9.5 241.3 9.5 241.3 9.5 241.3 9.5 241.3 6.0 152.4
2 50 11.5 292.1 11.5 292.1 11.5 292.1 11.5 292.1 11.5 292.1 11.5 292.1 7.0 177.8
2-1/2 65 13.0 330.2 13.0 330.2 13.0 330.2 13.0 330.2 13.0 330.2 13.0 330.2 8.5 215.9
3 80 14.0 355.6 14.0 355.6 14.0 355.6 14.0 355.6 14.0 355.6 14.0 355.6 10.0 254.0
4 100 16.0 406.4 16.0 406.4 17.0 431.8 17.0 431.8 17.0 431.8 17.0 431.8 12.0 304.8
5 125 18.0 457.2 18.0 457.2 20.0 508.0 20.0 508.0 20.0 508.0 20.0 508.0 15.0 381.0
6 150 19.5 495.3 19.5 495.3 22.0 558.8 22.0 558.8 22.0 558.8 22.0 558.8 18.0 457.2
8 200 23.5 596.9 23.5 596.9 26.0 660.4 26.0 660.4 26.0 660.4 26.0 660.4 23.0 584.2
10 250 26.5 673.1 26.5 673.1 31.0 787.4 31.0 787.4 31.0 787.4 31.0 787.4 28.0 711.2
12 300 30.0 762.0 30.0 762.0 33.0 838.2 33.0 838.2 33.0 838.2 33.0 838.2 32.0 812.8
14 350 32.5 825.5 32.5 825.5 35.0 889.0 35.0 889.0 35.0 889.0 35.0 889.0 35.0 889.0
16 400 35.5 901.7 35.5 901.7 39.0 990.6 39.0 990.6 39.0 990.6 39.0 990.6 39.0 990.6
18 450 38.5 977.9 38.5 977.9 43.0 1092.2 43.0 1092.2 43.0 1092.2 43.0 1092.2 43.0 1092.2
20 500 41.5 1054.1 41.5 1054.1 47.0 1193.8 47.0 1193.8 47.0 1193.8 47.0 1193.8 47.0 1193.8
22 550 45.0 1143.0 45.0 1143.0 51.0 1295.4 51.0 1295.4 51.0 1295.4 51.0 1295.4 --- ---
24 600 48.5 1231.9 48.5 1231.9 55.0 1397.0 55.0 1397.0 55.0 1397.0 55.0 1397.0 55.0 1397.0
26 650 --- --- --- 1308.1 57.0 1447.8 57.0 1447.8 57.0 1447.8 57.0 1447.8 --- ---
28 700 --- --- --- 1397.0 61.0 1549.4 61.0 1549.4 61.0 1549.4 61.0 1549.4 --- ---
30 750 --- --- --- 1524.0 65.0 --- 65.0 1651.0 65.0 1651.0 65.0 1651.0 --- ---
32 800 --- --- --- 1651.0 --- --- 70.0 1778.0 --- --- 70.0 1778.0 --- ---
34 850 --- --- --- 1778.0 --- --- 76.0 1930.4 --- --- 76.0 1930.4 --- ---
36 900 --- --- --- 1879.6 --- --- 82.0 2082.8 --- --- 82.0 2082.8 --- ---
""")
    o = _frame(w, 630, "Van cổng thép (Cấp 400 và 600)",
               "Steel Gate Valve (Class 400 and 600)")
    o.append(T(340, 66, "Raised face and beveled end / Face-to-face and end-to-end",
               6.6, color=GREY))
    end = _dim_table(o, x, y, widths, groups, hdr, rows, fs=6.5)
    _notes(o, 12, end + 6, [
        "Ghi chú: (---) = cỡ không nêu trong ASME/ANSI. mm làm tròn 1 chữ số. Theo B16.10.",
        "Một số ô trống trong bản in được giữ nguyên theo nguồn.",
    ])
    return _finish(w, 630, o, *_cap(
        44, 229, "Van cổng thép (Cấp 400 và 600)",
        "Steel Gate Valve (Class 400 and 600)",
        "Bảng kích thước van cổng thép ANSI Class 400 và 600, gồm kiểu ngắn.",
        "Dimension table for steel gate valves, ANSI Classes 400 and 600, including short pattern.",
        "Bảng Hình 10.44 (tr. 229) kích thước van cổng thép Class 400 và 600",
        "Table of Figure 10.44 (p. 229) steel gate valve Class 400 and 600 dimensions"))


@_reg
def fig_f10_45():
    w = 680
    x, y = 11, 76
    widths = [46, 38] + [48] * 12
    groups = [(2, 2, "Class 900\nSolid wedge"),
              (4, 2, "Class 900\nDouble disk"),
              (6, 2, "Class 900\nShort pattern"),
              (8, 2, "Class 1500\nSolid wedge"),
              (10, 2, "Class 1500\nDouble disk"),
              (12, 2, "Class 1500\nShort pattern")]
    hdr = ["Inch", "mm"] + ["in", "mm"] * 6
    rows = _rr("""
3/4 20 --- --- --- --- --- --- --- --- --- --- --- ---
1 25 10.00 254.0 --- --- 5.50 139.7 10.00 254.0 --- --- 5.50 139.7
1-1/4 32 11.00 279.4 --- --- 6.50 165.1 11.00 279.4 --- --- 6.50 165.1
1-1/2 40 12.00 304.8 --- --- 7.00 177.8 12.00 304.8 --- --- 7.00 177.8
2 50 14.50 368.3 14.50 368.3 8.50 215.9 14.50 368.3 14.50 368.3 8.50 215.9
2-1/2 65 16.50 419.1 16.50 419.1 10.00 254.0 16.50 419.1 16.50 419.1 10.00 254.0
3 80 15.00 381.0 15.00 381.0 12.00 304.8 18.50 469.9 18.50 469.9 12.00 304.8
4 100 18.00 457.2 18.00 457.2 14.00 355.6 21.50 546.1 21.50 546.1 16.00 406.4
5 125 22.00 558.8 22.00 558.8 17.00 431.8 26.50 673.1 26.50 673.1 19.00 482.6
6 150 24.00 609.6 24.00 609.6 20.00 508.0 27.75 704.9 27.75 704.9 22.00 558.8
8 200 29.00 736.6 29.00 736.6 26.00 660.4 32.75 831.9 32.75 831.9 28.00 711.2
10 250 33.00 838.2 33.00 838.2 31.00 787.4 39.00 990.6 39.00 990.6 34.00 863.6
12 300 38.00 965.2 38.00 965.2 36.00 914.4 44.50 1130.3 44.50 1130.3 39.00 990.6
14 350 40.50 1028.7 40.50 1028.7 39.00 990.6 49.50 1257.3 49.50 1257.3 42.00 1066.8
16 400 44.50 1130.3 44.50 1130.3 43.00 1092.2 54.50 1384.3 54.50 1384.3 47.00 1193.8
18 450 48.00 1219.2 48.00 1219.2 --- --- 60.50 1536.7 60.50 1536.7 53.00 1346.2
20 500 52.00 1320.8 52.00 1320.8 --- --- 65.50 1663.7 65.50 1663.7 58.00 1473.2
22 550 --- --- --- --- --- --- --- --- --- --- --- ---
24 600 61.00 1549.4 61.00 1549.4 --- --- 76.50 1943.1 76.50 1943.1 --- ---
""")
    o = _frame(w, 520, "Van cổng thép (Cấp 900 và 1500)",
               "Steel Gate Valve (Class 900 and 1500)")
    o.append(T(340, 66, "Raised face and beveled end / Face-to-face and end-to-end",
               6.6, color=GREY))
    end = _dim_table(o, x, y, widths, groups, hdr, rows, fs=6.5)
    _notes(o, 12, end + 6, [
        "Ghi chú: (---) = cỡ không nêu trong ASME/ANSI. mm làm tròn 1 chữ số. Theo B16.10.",
    ])
    return _finish(w, 520, o, *_cap(
        45, 230, "Van cổng thép (Cấp 900 và 1500)",
        "Steel Gate Valve (Class 900 and 1500)",
        "Bảng kích thước van cổng thép ANSI Class 900 và 1500, gồm kiểu ngắn.",
        "Dimension table for steel gate valves, ANSI Classes 900 and 1500, including short pattern.",
        "Bảng Hình 10.45 (tr. 230) kích thước van cổng thép Class 900 và 1500",
        "Table of Figure 10.45 (p. 230) steel gate valve Class 900 and 1500 dimensions"))


@_reg
def fig_f10_46():
    w = 680
    x, y = 11, 76
    widths = [46, 38] + [51] * 10
    groups = [(2, 2, "Class 2500 Raised Face\nSolid wedge"),
              (4, 2, "Class 2500 Raised Face\nDouble disk"),
              (6, 2, "Class 2500 Beveled End\nSolid wedge"),
              (8, 2, "Class 2500 Beveled End\nDouble disk"),
              (10, 2, "Short pattern")]
    hdr = ["Inch", "mm"] + ["in", "mm"] * 5
    rows = _rr("""
1/2 15 10.38 263.7 --- --- 10.38 263.7 --- --- --- ---
3/4 20 10.75 273.1 --- --- 10.75 273.1 --- --- --- ---
1 25 12.12 307.9 --- --- 12.12 307.9 --- --- 7.31 185.7
1-1/4 32 13.75 349.3 --- --- 13.75 349.3 --- --- 9.12 231.7
1-1/2 40 15.12 384.1 --- --- 15.12 384.1 --- --- 9.12 231.7
2 50 17.75 450.9 17.75 450.9 17.75 450.9 17.75 450.9 11.00 279.4
2-1/2 65 20.00 508.0 20.00 508.0 20.00 508.0 20.00 508.0 13.00 330.2
3 80 22.75 577.9 22.75 577.9 22.75 577.9 22.75 557.9 14.50 368.3
4 100 26.50 673.1 26.50 673.1 26.50 673.1 26.50 673.1 18.00 457.2
5 125 31.25 793.8 31.25 793.8 31.25 793.8 31.25 793.8 21.00 533.4
6 150 36.00 914.4 36.00 914.4 36.00 914.4 36.00 914.4 24.00 609.6
8 200 40.25 1022.4 40.25 1022.4 40.25 1022.4 40.25 1022.4 30.00 762.0
10 250 50.00 1270.0 50.00 1270.0 50.00 1270.0 50.00 1270.0 36.00 914.4
12 300 56.00 1422.4 56.00 1422.4 56.00 1422.4 56.00 1422.4 41.00 1041.4
14 350 --- --- --- --- --- --- --- --- 44.00 1117.6
16 400 --- --- --- --- --- --- --- --- 49.00 1244.6
18 450 --- --- --- --- --- --- --- --- 55.00 1397.0
""")
    o = _frame(w, 470, "Van cổng thép (Cấp 2500)", "Steel Gate Valve (Class 2500)")
    o.append(T(340, 66, "Raised face and beveled end / Face-to-face and end-to-end",
               6.6, color=GREY))
    end = _dim_table(o, x, y, widths, groups, hdr, rows, fs=6.5)
    _notes(o, 12, end + 6, [
        "Ghi chú: (---) = cỡ không nêu trong ASME/ANSI. mm làm tròn 1 chữ số. Theo B16.10.",
        "Kiểu ngắn dùng cho nắp ép hoặc nắp không bích (tùy chọn trên nắp bắt bulông).",
        "Bản in ghi 557.9 ở hàng 3 in; giá trị được giữ nguyên theo nguồn.",
    ])
    return _finish(w, 470, o, *_cap(
        46, 231, "Van cổng thép (Cấp 2500)", "Steel Gate Valve (Class 2500)",
        "Bảng kích thước van cổng thép ANSI Class 2500, gồm kiểu ngắn.",
        "Dimension table for steel gate valves, ANSI Class 2500, including short pattern.",
        "Bảng Hình 10.46 (tr. 231) kích thước van cổng thép Class 2500",
        "Table of Figure 10.46 (p. 231) steel gate valve Class 2500 dimensions"))


@_reg
def fig_f10_47():
    w = 680
    x, y = 11, 76
    widths = [46, 38] + [57.6] * 10
    groups = [(2, 2, "Class 150\nStraightway globe"),
              (4, 2, "Class 150\nAngle globe"),
              (6, 2, "Class 150\nY-pattern globe"),
              (8, 2, "Class 150\nControl valve"),
              (10, 2, "Class 150\nSwing check")]
    hdr = ["Inch", "mm"] + ["in", "mm"] * 5
    rows = _rr("""
1/4 8 4.00 101.6 2.00 50.8 --- --- --- --- 4.00 101.6
3/8 10 4.00 101.6 2.00 50.8 --- --- --- --- 4.00 101.6
1/2 15 4.25 108.0 2.25 57.2 5.50 139.7 --- --- 4.25 108.0
3/4 20 4.62 117.4 2.50 63.5 6.00 152.4 --- --- 4.62 117.4
1 25 5.00 127.0 2.75 69.9 6.50 165.1 7.25 184.2 5.00 127.0
1-1/4 32 5.50 139.7 3.00 76.2 7.25 184.2 --- --- 5.50 139.7
1-1/2 40 6.50 165.1 3.25 82.6 8.00 203.2 8.75 222.3 6.50 165.1
2 50 8.00 203.2 4.00 101.6 9.00 228.6 10.00 254.0 8.00 203.2
2-1/2 65 8.50 215.9 4.25 108.0 11.00 279.4 10.88 276.4 8.50 215.9
3 80 9.50 241.3 4.75 120.7 12.50 317.5 11.75 298.5 9.50 241.3
4 100 11.50 292.1 5.75 146.1 14.50 368.3 13.88 352.6 11.50 292.1
5 125 14.00 355.6 7.00 177.8 --- --- --- --- 13.00 355.6
6 150 16.00 406.4 8.00 203.2 18.50 469.9 17.75 450.9 14.00 406.4
8 200 19.50 495.3 9.75 247.7 23.50 596.9 21.38 543.1 19.50 495.3
10 250 24.50 622.3 12.25 311.2 26.50 673.1 26.50 673.1 24.50 622.3
12 300 27.50 698.5 13.75 349.3 30.50 774.7 29.00 736.6 27.50 698.5
14 350 31.00 787.4 15.50 393.7 --- --- 35.00 889.0 31.50 787.4
16 400 36.00 914.4 18.00 457.2 --- --- 40.00 1016.0 34.00 914.4
18 450 --- --- --- --- --- --- --- --- 38.50 977.9
20 500 --- --- --- --- --- --- --- --- 38.50 977.9
22 550 --- --- --- --- --- --- --- --- 42.00 1066.8
24 600 --- --- --- --- --- --- --- --- 51.00 1295.4
26 650 --- --- --- --- --- --- --- --- 51.00 1295.4
28 700 --- --- --- --- --- --- --- --- 57.00 1447.8
30 750 --- --- --- --- --- --- --- --- 60.00 1524.0
32 800 --- --- --- --- --- --- --- --- --- ---
34 850 --- --- --- --- --- --- --- --- --- ---
36 900 --- --- --- --- --- --- --- --- 77.00 1955.8
""")
    o = _frame(w, 630, "Van cầu / Van một chiều thép (Cấp 150)",
               "Steel Globe / Check Valve (Class 150)")
    o.append(T(340, 66, "Mặt giáp bích và đầu bịt / Face-to-face and end-to-end",
               6.6, color=GREY))
    end = _dim_table(o, x, y, widths, groups, hdr, rows, fs=6.5)
    _notes(o, 12, end + 6, [
        "Ghi chú: kích thước van điều tiết chỉ áp dụng cho van mặt bích nhô.",
        "(---) = cỡ không nêu trong ASME/ANSI. Theo B16.10.",
    ])
    return _finish(w, 630, o, *_cap(
        47, 232, "Van cầu / Van một chiều thép (Cấp 150)",
        "Steel Globe / Check Valve (Class 150)",
        "Bảng kích thước van cầu và van một chiều thép ANSI Class 150.",
        "Dimension table for steel globe and check valves, ANSI Class 150.",
        "Bảng Hình 10.47 (tr. 232) kích thước van cầu và van một chiều Class 150",
        "Table of Figure 10.47 (p. 232) steel globe and check valve Class 150 dimensions"))


@_reg
def fig_f10_48():
    w = 680
    x, y = 11, 76
    widths = [46, 38] + [72] * 8
    groups = [(2, 2, "Class 300\nStraightway globe"),
              (4, 2, "Class 300\nAngle globe"),
              (6, 2, "Class 300\nControl valve"),
              (8, 2, "Class 300\nSwing check")]
    hdr = ["Inch", "mm"] + ["in", "mm"] * 4
    rows = _rr("""
1/4 8 --- --- --- --- --- --- --- ---
3/8 10 --- --- --- --- --- --- --- ---
1/2 15 6.00 152.4 3.00 76.2 7.50 190.5 --- ---
3/4 20 7.00 177.8 3.50 88.9 7.62 193.6 --- ---
1 25 8.00 203.2 4.00 101.6 7.75 196.9 8.50 215.9
1-1/4 32 8.50 215.9 4.25 108.0 --- --- 9.00 228.6
1-1/2 40 9.00 228.6 4.50 114.3 9.25 235.0 9.50 241.3
2 50 10.50 266.7 5.25 133.4 10.50 266.7 10.50 266.7
2-1/2 65 11.50 292.1 5.75 146.1 11.50 292.1 11.50 292.1
3 80 12.50 317.5 6.25 158.8 12.50 321.3 12.50 317.5
4 100 14.00 355.6 7.00 177.8 14.50 368.3 14.00 355.6
5 125 15.75 400.1 7.88 200.2 --- --- 15.75 400.1
6 150 17.50 444.5 8.75 222.3 18.62 473.0 17.50 444.5
8 200 22.00 558.8 11.00 279.4 22.38 568.5 21.00 533.4
10 250 24.50 622.3 12.25 311.2 27.88 708.2 24.50 622.3
12 300 28.00 711.2 14.00 355.6 30.50 774.7 28.00 711.2
14 350 --- --- --- --- 36.50 927.1 33.00 838.2
16 400 --- --- --- --- 41.62 1057.2 34.00 863.6
18 450 --- --- --- --- --- --- 38.50 977.9
20 500 --- --- --- --- --- --- 40.00 1016.0
22 550 --- --- --- --- --- --- 44.00 1117.6
24 600 --- --- --- --- --- --- 53.00 1346.2
26 650 --- --- --- --- --- --- 53.00 1346.2
28 700 --- --- --- --- --- --- 59.00 1498.6
30 750 --- --- --- --- --- --- 62.75 1593.9
32 800 --- --- --- --- --- --- --- ---
34 850 --- --- --- --- --- --- --- ---
36 900 --- --- --- --- --- --- 82.00 2082.8
""")
    o = _frame(w, 630, "Van cầu / Van một chiều thép (Cấp 300)",
               "Steel Globe / Check Valve (Class 300)")
    o.append(T(340, 66, "Mặt giáp bích và đầu bịt / Face-to-face and end-to-end",
               6.6, color=GREY))
    end = _dim_table(o, x, y, widths, groups, hdr, rows, fs=6.5)
    _notes(o, 12, end + 6, [
        "Ghi chú: kích thước van điều tiết chỉ áp dụng cho van mặt bích nhô.",
        "(---) = cỡ không nêu trong ASME/ANSI. Theo B16.10.",
    ])
    return _finish(w, 630, o, *_cap(
        48, 233, "Van cầu / Van một chiều thép (Cấp 300)",
        "Steel Globe / Check Valve (Class 300)",
        "Bảng kích thước van cầu và van một chiều thép ANSI Class 300.",
        "Dimension table for steel globe and check valves, ANSI Class 300.",
        "Bảng Hình 10.48 (tr. 233) kích thước van cầu và van một chiều Class 300",
        "Table of Figure 10.48 (p. 233) steel globe and check valve Class 300 dimensions"))


@_reg
def fig_f10_49():
    w = 680
    x, y = 11, 88
    widths = [46, 38] + [48] * 12
    groups = [(2, 2, "Class 400\nStraightway globe"),
              (4, 2, "Class 400\nAngle globe"),
              (6, 2, "Class 400\nSwing check"),
              (8, 2, "Class 600\nStraightway globe"),
              (10, 2, "Class 600\nAngle globe"),
              (12, 2, "Class 600\nSwing check")]
    hdr = ["Inch", "mm"] + ["in", "mm"] * 6
    rows = _rr("""
1/2 15 6.50 165.1 3.25 82.6 6.50 165.1 6.50 165.1 3.25 82.6 6.50 165.1
3/4 20 7.50 190.5 3.75 95.3 7.50 190.5 7.50 190.5 3.75 95.3 7.50 190.5
1 25 8.50 215.9 4.25 108.0 8.50 215.9 8.50 215.9 4.25 108.0 8.50 215.9
1-1/4 32 9.00 228.6 4.50 114.3 9.00 228.6 9.00 228.6 4.50 114.3 9.00 228.6
1-1/2 40 9.50 241.3 4.75 120.7 9.50 241.3 9.50 241.3 4.75 120.7 9.50 241.3
2 50 11.50 292.1 5.75 146.1 11.50 292.1 11.50 292.1 5.75 146.1 11.50 292.1
2-1/2 65 13.00 330.2 6.50 165.1 13.00 330.2 13.00 330.2 6.50 165.1 13.00 330.2
3 80 14.00 355.6 7.00 177.8 14.00 355.6 14.00 355.6 7.00 177.8 14.00 355.6
4 100 16.00 406.4 8.00 203.2 16.00 406.4 17.00 431.8 8.50 215.9 17.00 431.8
5 125 18.00 457.2 9.00 228.6 18.00 457.2 20.00 508.0 10.00 254.0 20.00 508.0
6 150 19.50 495.3 9.75 247.7 19.50 495.3 22.00 558.8 11.00 279.4 22.00 558.8
8 200 23.50 596.9 11.75 298.5 23.50 596.9 26.00 660.4 13.00 330.2 26.00 660.4
10 250 26.50 673.1 13.25 336.6 26.50 673.1 31.00 787.4 15.50 393.7 31.00 787.4
12 300 30.00 762.0 15.00 381.0 30.00 762.0 33.00 838.2 16.50 419.1 33.00 838.2
14 350 --- --- --- --- 35.00 889.0 --- --- --- --- 35.00 889.0
16 400 --- --- --- --- 35.50 901.7 --- --- --- --- 39.00 990.6
18 450 --- --- --- --- 40.00 1016.0 --- --- --- --- 43.00 1092.2
20 500 --- --- --- --- 41.50 1054.1 --- --- --- --- 47.00 1193.8
22 550 --- --- --- --- 45.00 1143.0 --- --- --- --- 51.00 1295.4
24 600 --- --- --- --- 55.00 1397.0 --- --- --- --- 55.00 1397.0
26 650 --- --- --- --- 55.00 1397.0 --- --- --- --- 57.00 1447.8
28 700 --- --- --- --- 63.00 1600.2 --- --- --- --- 63.00 1600.2
30 750 --- --- --- --- 65.00 1651.0 --- --- --- --- 65.00 1651.0
32 800 --- --- --- --- --- --- --- --- --- --- --- ---
34 850 --- --- --- --- --- --- --- --- --- --- --- ---
36 900 --- --- --- --- 82.00 2082.8 --- --- --- --- 82.00 2082.8
""")
    o = _frame(w, 630, "Van cầu / Van một chiều thép (Cấp 400 và 600)",
               "Steel Globe / Check Valve (Class 400 and 600)")
    o.append(T(340, 76, "Long pattern / Kiểu dài - mặt giáp bích và đầu bịt",
               6.6, color=GREY))
    end = _dim_table(o, x, y, widths, groups, hdr, rows, fs=6.5)
    _notes(o, 12, end + 6, [
        "Ghi chú: (---) = cỡ không nêu trong ASME/ANSI. mm làm tròn 1 chữ số. Theo B16.10.",
    ])
    return _finish(w, 630, o, *_cap(
        49, 234, "Van cầu / Van một chiều thép (Cấp 400 và 600)",
        "Steel Globe / Check Valve (Class 400 and 600)",
        "Bảng kích thước van cầu và van một chiều thép ANSI Class 400 và 600.",
        "Dimension table for steel globe and check valves, ANSI Classes 400 and 600.",
        "Bảng Hình 10.49 (tr. 234) kích thước van cầu và van một chiều Class 400 và 600",
        "Table of Figure 10.49 (p. 234) steel globe and check valve Class 400 and 600 dimensions"))


@_reg
def fig_f10_50():
    w = 680
    x, y = 11, 76
    widths = [46, 38] + [72] * 8
    groups = [(2, 2, "Class 600 short\nStraightway globe"),
              (4, 2, "Class 600 short\nAngle globe"),
              (6, 2, "Class 600 short\nSwing check"),
              (8, 2, "Class 600 short\nControl valve")]
    hdr = ["Inch", "mm"] + ["in", "mm"] * 4
    rows = _rr("""
1/2 15 --- --- --- --- --- --- 8.00 203.2
3/4 20 --- --- --- --- --- --- 8.12 206.3
1 25 5.25 133.4 --- --- 5.25 133.4 8.25 209.6
1-1/4 32 5.75 146.1 --- --- 5.75 146.1 --- ---
1-1/2 40 6.00 152.4 --- --- 6.00 152.4 9.88 251.0
2 50 7.00 177.8 4.25 108.0 7.00 177.8 11.25 285.8
2-1/2 65 8.50 215.9 5.00 127.0 8.50 215.9 12.25 311.2
3 80 10.00 254.0 6.00 152.4 10.00 254.0 13.25 336.6
4 100 12.00 304.8 7.00 177.8 12.00 304.8 15.50 393.7
5 125 15.00 381.0 8.50 215.9 15.00 381.0 --- ---
6 150 18.00 457.2 10.00 254.0 18.00 457.2 20.00 508.0
8 200 23.00 584.2 --- --- 23.00 584.2 24.00 609.6
10 250 28.00 711.2 --- --- 28.00 711.2 29.62 752.4
12 300 32.00 812.8 --- --- 32.00 812.2 32.25 819.2
14 350 --- --- --- --- --- --- 38.25 971.6
16 400 --- --- --- --- --- --- 43.62 1108.0
18 450 --- --- --- --- --- --- --- ---
20 500 --- --- --- --- --- --- --- ---
22 550 --- --- --- --- --- --- --- ---
24 600 --- --- --- --- --- --- --- ---
26 650 --- --- --- --- --- --- --- ---
28 700 --- --- --- --- --- --- --- ---
30 750 --- --- --- --- --- --- --- ---
32 800 --- --- --- --- --- --- --- ---
34 850 --- --- --- --- --- --- --- ---
36 900 --- --- --- --- --- --- --- ---
""")
    o = _frame(w, 630, "Van cầu / Van một chiều thép (Cấp 600)",
               "Steel Globe / Check Valve (Class 600)")
    o.append(T(340, 66, "Short pattern / Kiểu ngắn - đầu bịt",
               6.8, color=GREY))
    end = _dim_table(o, x, y, widths, groups, hdr, rows, fs=6.5)
    _notes(o, 12, end + 6, [
        "Ghi chú: (---) = cỡ không nêu trong ASME/ANSI. mm làm tròn 1 chữ số. Theo B16.10.",
        "Một số hàng bản in thiếu một ô (---) do OCR; đã bổ sung theo cấu trúc 8 cột.",
    ])
    return _finish(w, 630, o, *_cap(
        50, 235, "Van cầu / Van một chiều thép (Cấp 600)",
        "Steel Globe / Check Valve (Class 600)",
        "Bảng kích thước kiểu ngắn van cầu và van một chiều thép ANSI Class 600.",
        "Short-pattern dimension table for steel globe and check valves, ANSI Class 600.",
        "Bảng Hình 10.50 (tr. 235) kích thước van cầu và van một chiều Class 600",
        "Table of Figure 10.50 (p. 235) steel globe and check valve Class 600 dimensions"))


@_reg
def fig_f10_51():
    w = 680
    x, y = 11, 88
    widths = [46, 38] + [48] * 12
    groups = [(2, 2, "Class 900 long\nStraightway globe"),
              (4, 2, "Class 900 long\nAngle globe"),
              (6, 2, "Class 900 long\nSwing check"),
              (8, 2, "Class 900 short\nStraightway globe"),
              (10, 2, "Class 900 short\nAngle globe"),
              (12, 2, "Class 900 short\nSwing check")]
    hdr = ["Inch", "mm"] + ["in", "mm"] * 6
    rows = _rr("""
1/2 15 --- --- --- --- --- --- --- --- --- --- --- ---
3/4 20 9.00 228.6 4.50 114.3 9.00 228.6 --- --- --- --- --- ---
1 25 10.00 254.0 5.00 127.0 10.00 254.0 --- --- --- --- --- ---
1-1/4 32 11.00 279.4 5.50 139.7 11.00 279.4 --- --- --- --- --- ---
1-1/2 40 12.00 304.8 6.00 152.4 12.00 304.8 --- --- --- --- --- ---
2 50 14.50 368.3 7.25 184.2 14.50 368.3 --- --- --- --- --- ---
2-1/2 65 16.50 419.1 8.25 209.6 16.50 419.1 10.00 254.0 --- --- 10.00 254.0
3 80 15.00 381.0 7.50 190.5 15.00 381.0 12.00 304.8 6.00 152.4 12.00 304.8
4 100 18.00 457.2 9.00 228.6 18.00 457.2 14.00 355.6 7.00 177.8 14.00 355.6
5 125 22.00 558.8 11.00 279.4 22.00 558.8 17.00 431.8 8.50 215.9 17.00 431.8
6 150 24.00 609.6 12.00 304.8 24.00 609.6 20.00 508.0 10.00 254.0 20.00 508.0
8 200 29.00 736.6 14.50 368.3 29.00 736.6 26.00 660.4 13.00 330.2 26.00 660.4
10 250 33.00 838.2 16.50 419.1 33.00 838.2 31.00 787.4 15.50 393.7 31.00 787.4
12 300 38.00 965.2 19.00 482.6 38.00 965.2 36.00 914.4 18.00 457.2 36.00 914.4
14 350 40.50 1028.7 20.25 514.4 40.50 1028.7 39.00 990.6 19.50 495.3 39.00 990.6
16 400 --- --- 26.00 660.4 44.50 1130.3 43.00 1092.2 --- --- 43.00 1092.2
18 450 --- --- 29.00 736.6 48.00 1219.2 --- --- --- --- --- ---
20 500 --- --- 32.50 825.5 52.00 1320.8 --- --- --- --- --- ---
22 550 --- --- --- --- --- --- --- --- --- --- --- ---
24 600 --- --- 39.00 990.6 61.00 1549.4 --- --- --- --- --- ---
""")
    o = _frame(w, 520, "Van cầu / Van một chiều thép (Cấp 900)",
               "Steel Globe / Check Valve (Class 900)")
    o.append(T(340, 76, "Kiểu dài và kiểu ngắn / Long and short pattern - inch và mm",
               6.6, color=GREY))
    end = _dim_table(o, x, y, widths, groups, hdr, rows, fs=6.5, ghh=22)
    _notes(o, 12, end + 6, [
        "Ghi chú: (---) = cỡ không nêu trong ASME/ANSI. mm làm tròn 1 chữ số. Theo B16.10.",
    ])
    return _finish(w, 520, o, *_cap(
        51, 236, "Van cầu / Van một chiều thép (Cấp 900)",
        "Steel Globe / Check Valve (Class 900)",
        "Bảng kích thước van cầu và van một chiều thép ANSI Class 900, dài và ngắn.",
        "Dimension table for steel globe and check valves, ANSI Class 900, long and short patterns.",
        "Bảng Hình 10.51 (tr. 236) kích thước van cầu và van một chiều Class 900",
        "Table of Figure 10.51 (p. 236) steel globe and check valve Class 900 dimensions"))


@_reg
def fig_f10_52():
    w = 680
    x, y = 11, 88
    widths = [46, 38] + [57.6] * 10
    groups = [(2, 2, "Class 1500 long\nStraightway globe"),
              (4, 2, "Class 1500 long\nAngle globe"),
              (6, 2, "Class 1500 long\nSwing check"),
              (8, 2, "Class 1500 short\nStraightway globe"),
              (10, 2, "Class 1500 short\nSwing check")]
    hdr = ["Inch", "mm"] + ["in", "mm"] * 5
    rows = _rr("""
1/2 15 8.50 215.9 4.25 108.0 --- --- --- --- --- ---
3/4 20 9.00 228.6 4.50 114.3 9.00 228.6 --- --- --- ---
1 25 10.00 254.0 5.00 127.0 10.00 254.0 --- --- --- ---
1-1/4 32 11.00 279.4 5.50 139.7 11.00 279.4 --- --- --- ---
1-1/2 40 12.00 304.8 6.00 152.4 12.00 304.8 --- --- --- ---
2 50 14.50 368.3 7.25 184.2 14.50 368.3 8.50 215.9 8.50 215.9
2-1/2 65 16.50 419.1 8.25 209.6 16.50 419.1 10.00 254.0 10.00 254.0
3 80 18.50 469.9 9.25 235.0 18.50 469.9 12.00 304.8 12.00 304.8
4 100 21.50 546.1 10.75 273.1 21.50 546.1 16.00 406.4 16.00 406.4
5 125 26.50 673.1 13.25 336.6 26.50 673.1 19.00 482.6 19.00 482.6
6 150 27.75 704.9 13.88 352.6 27.75 704.9 22.00 558.8 22.00 558.8
8 200 32.75 831.9 16.38 416.1 32.75 831.9 28.00 711.2 28.00 711.2
10 250 39.00 990.6 19.50 495.3 39.00 990.6 34.00 863.6 34.00 863.6
12 300 44.50 1130.3 22.25 565.2 44.50 1130.3 39.00 990.6 39.00 990.6
14 350 49.50 1257.3 24.75 628.7 49.50 1257.3 42.00 1066.8 42.00 1066.8
16 400 --- --- --- --- 54.50 1384.3 47.00 1193.8 47.00 1193.8
18 450 --- --- --- --- 60.50 1536.7 --- --- --- ---
20 500 --- --- --- --- 65.50 1663.7 --- --- --- ---
22 550 --- --- --- --- --- --- --- --- --- ---
24 600 --- --- --- --- 76.50 1943.1 --- --- --- ---
""")
    o = _frame(w, 520, "Van cầu / Van một chiều thép (Cấp 1500)",
               "Steel Globe / Check Valve (Class 1500)")
    o.append(T(340, 76, "Kiểu dài và kiểu ngắn / Long and short pattern - inch và mm",
               6.6, color=GREY))
    end = _dim_table(o, x, y, widths, groups, hdr, rows, fs=6.5, ghh=22)
    _notes(o, 12, end + 6, [
        "Ghi chú: (---) = cỡ không nêu trong ASME/ANSI. mm làm tròn 1 chữ số. Theo B16.10.",
    ])
    return _finish(w, 520, o, *_cap(
        52, 237, "Van cầu / Van một chiều thép (Cấp 1500)",
        "Steel Globe / Check Valve (Class 1500)",
        "Bảng kích thước van cầu và van một chiều thép ANSI Class 1500, dài và ngắn.",
        "Dimension table for steel globe and check valves, ANSI Class 1500, long and short patterns.",
        "Bảng Hình 10.52 (tr. 237) kích thước van cầu và van một chiều Class 1500",
        "Table of Figure 10.52 (p. 237) steel globe and check valve Class 1500 dimensions"))


@_reg
def fig_f10_53():
    w = 680
    x, y = 11, 88
    widths = [46, 38] + [57.6] * 10
    groups = [(2, 2, "Class 2500 long\nStraightway globe"),
              (4, 2, "Class 2500 long\nAngle globe"),
              (6, 2, "Class 2500 long\nSwing check"),
              (8, 2, "Class 2500 short\nStraightway globe"),
              (10, 2, "Class 2500 short\nSwing check")]
    hdr = ["Inch", "mm"] + ["in", "mm"] * 5
    rows = _rr("""
1/2 15 10.38 263.7 5.19 131.8 10.38 263.7 --- --- --- ---
3/4 20 10.75 273.1 5.38 136.7 10.75 273.1 --- --- --- ---
1 25 12.12 307.9 6.06 153.9 12.12 307.9 --- --- --- ---
1-1/4 32 13.75 349.3 6.88 174.8 13.75 349.3 --- --- --- ---
1-1/2 40 15.12 384.0 7.56 192.0 15.12 384.0 --- --- --- ---
2 50 17.75 450.9 8.88 225.6 17.75 450.9 11.00 279.4 11.00 279.4
2-1/2 65 20.00 508.0 10.00 254.0 20.00 508.0 13.00 330.2 13.00 330.2
3 80 22.75 577.9 11.38 289.1 22.75 577.9 14.50 368.3 14.50 368.3
4 100 26.50 673.1 13.25 336.6 26.50 673.1 18.00 457.2 18.00 457.2
5 125 31.25 793.8 15.62 396.8 31.25 793.8 21.00 533.4 21.00 533.4
6 150 36.00 914.4 18.00 457.2 36.00 914.4 24.00 609.6 24.00 609.6
8 200 40.25 1022.4 20.12 511.1 40.25 1022.4 30.00 762.0 30.00 762.0
10 250 50.00 1270.0 25.00 635.0 50.00 1270.0 36.00 914.0 36.00 914.0
12 300 56.00 1422.4 28.00 711.2 56.00 1422.4 41.00 1041.4 41.00 1041.4
14 350 --- --- --- --- --- --- --- --- --- ---
16 400 --- --- --- --- --- --- --- --- --- ---
18 450 --- --- --- --- --- --- --- --- --- ---
""")
    o = _frame(w, 490, "Van cầu / Van một chiều thép (Cấp 2500)",
               "Steel Globe / Check Valve (Class 2500)")
    o.append(T(340, 76, "Kiểu dài và kiểu ngắn / Long and short pattern - inch và mm",
               6.6, color=GREY))
    end = _dim_table(o, x, y, widths, groups, hdr, rows, fs=6.5, ghh=22)
    _notes(o, 12, end + 6, [
        "Ghi chú: (---) = cỡ không nêu trong ASME/ANSI. mm làm tròn 1 chữ số. Theo B16.10.",
        "Van một chiều nâng thẳng trùng kích thước van cầu thẳng; van góc trùng van cầu góc.",
    ])
    return _finish(w, 490, o, *_cap(
        53, 238, "Van cầu / Van một chiều thép (Cấp 2500)",
        "Steel Globe / Check Valve (Class 2500)",
        "Bảng kích thước van cầu và van một chiều thép ANSI Class 2500, dài và ngắn.",
        "Dimension table for steel globe and check valves, ANSI Class 2500, long and short patterns.",
        "Bảng Hình 10.53 (tr. 238) kích thước van cầu và van một chiều Class 2500",
        "Table of Figure 10.53 (p. 238) steel globe and check valve Class 2500 dimensions"))


# Per-chapter registry view for the validation harness.  ``_reg`` registers
# into cvh6fig.FIGS; this filtered alias exposes only this chapter's 53
# figures without duplicating or moving any shared state.
import cvh6fig as _cvh6fig  # noqa: E402
FIGS = {k: v for k, v in _cvh6fig.FIGS.items() if k.startswith("fig_f10_")}
