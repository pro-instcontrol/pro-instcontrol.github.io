# -*- coding: utf-8 -*-
"""Convert the vector artwork of a PDF page into a compact standalone SVG.

ANSI/ISA-5.1 draws its symbol sheets as PDF path operators (``m l c h re``
painted with ``S`` / ``f`` / ``B``); the sheet labels are outlined glyphs, so
there is no text layer to extract.  Rather than hand-trace several hundred
symbols, this module interprets the drawing operators and emits real SVG
paths.  Text-showing operators (page headers / footers) are skipped, the
content is cropped to the drawing area, and every path is simplified with
Ramer-Douglas-Peucker so the result stays small.

Typical use::

    from pdfvec import page_svg
    svg = page_svg(PDF_PATH, 29, title="General instrument or function symbols")
"""
from __future__ import annotations

import math
import re

from pypdf import PdfReader

# ---------------------------------------------------------------------------
# tokenizer
# ---------------------------------------------------------------------------
_NUM = re.compile(rb"[+-]?(?:\d+\.?\d*|\.\d+)")
_TOKEN = re.compile(
    rb"(?s)("
    rb"\[|\]|<<|>>|"                 # delimiters
    rb"/[^\s/\[\]<>(){}]+|"         # names
    rb"\([^()\\]*(?:\\.[^()\\]*)*\)|"  # literal strings (balanced-ish)
    rb"[+-]?(?:\d+\.?\d*|\.\d+)|"  # numbers
    rb"[A-Za-z*'\"][A-Za-z*'\"]*"  # operators / keywords
    rb")"
)


def _tokens(data):
    """Yield (kind, value) for the content stream."""
    i, n = 0, len(data)
    while i < n:
        ch = data[i:i + 1]
        if ch in b" \t\r\n\x00\f":
            i += 1
            continue
        if ch == b"%":
            j = data.find(b"\n", i)
            i = n if j < 0 else j + 1
            continue
        m = _TOKEN.match(data, i)
        if not m:
            i += 1
            continue
        raw = m.group(1)
        i = m.end()
        if raw in (b"[", b"]", b"<<", b">>"):
            yield ("delim", raw)
        elif raw.startswith(b"/"):
            yield ("name", raw[1:])
        elif raw.startswith(b"("):
            yield ("str", raw[1:-1])
        elif _NUM.fullmatch(raw):
            yield ("num", float(raw))
        else:
            yield ("op", raw.decode("latin-1"))


def _instructions(data):
    """Yield (operator, operand_list). Nested arrays are flattened into lists."""
    stack, arr, arrays = [], None, []
    for kind, val in _tokens(data):
        if kind == "delim":
            if val == b"[":
                arrays.append([])
                arr = arrays[-1]
            elif val == b"]":
                done = arrays.pop() if arrays else []
                arr = arrays[-1] if arrays else None
                if arr is None:
                    stack.append(done)
                else:
                    arr.append(done)
            continue
        if kind == "op":
            yield val, stack
            stack = []
        else:
            if arr is not None:
                arr.append(val)
            else:
                stack.append(val)


# ---------------------------------------------------------------------------
# geometry
# ---------------------------------------------------------------------------
def _mul(m1, m2):
    """m1 then m2, i.e. PDF's ``cm`` concatenation (m2 applied first)."""
    a1, b1, c1, d1, e1, f1 = m1
    a2, b2, c2, d2, e2, f2 = m2
    return (a1 * a2 + c1 * b2, b1 * a2 + d1 * b2,
            a1 * c2 + c1 * d2, b1 * c2 + d1 * d2,
            a1 * e2 + c1 * f2 + e1, b1 * e2 + d1 * f2 + f1)


def _apply(m, x, y):
    a, b, c, d, e, f = m
    return (a * x + c * y + e, b * x + d * y + f)


def _rdp(pts, eps):
    """Ramer-Douglas-Peucker simplification of a polyline."""
    if len(pts) < 3 or eps <= 0:
        return pts
    x1, y1 = pts[0]
    x2, y2 = pts[-1]
    dx, dy = x2 - x1, y2 - y1
    den = math.hypot(dx, dy)
    best, idx = -1.0, 0
    for i in range(1, len(pts) - 1):
        px, py = pts[i]
        if den < 1e-9:
            d = math.hypot(px - x1, py - y1)
        else:
            d = abs(dy * px - dx * py + x2 * y1 - y2 * x1) / den
        if d > best:
            best, idx = d, i
    if best <= eps:
        return [pts[0], pts[-1]]
    return _rdp(pts[:idx + 1], eps)[:-1] + _rdp(pts[idx:], eps)


def _fmt(v):
    s = "%.1f" % v
    if s.endswith(".0"):
        s = s[:-2]
    return "0" if s in ("-0", "-0.0") else s


# ---------------------------------------------------------------------------
# conversion
# ---------------------------------------------------------------------------
_IDENTITY = (1.0, 0.0, 0.0, 1.0, 0.0, 0.0)


def page_svg(pdf_path, page_no, title="", eps=0.16, crop_top=60.0,
             crop_bottom=58.0, stroke="#243447", fill="#243447",
             bg="#ffffff", rotate=0):
    """Return an SVG string for the vector artwork on ``page_no`` (1-based).

    ``crop_top`` / ``crop_bottom`` are measured from the PDF page edges and
    remove the running header/footer rules.  ``eps`` is the RDP tolerance in
    PDF points; 0.16 keeps circles smooth while cutting glyph outlines hard.
    """
    reader = PdfReader(pdf_path)
    page = reader.pages[page_no - 1]
    box = page.mediabox
    pw = float(box.width)
    ph = float(box.height)
    data = page.get_contents().get_data()

    state = {"ctm": _IDENTITY, "lw": 1.0, "stroke": stroke, "fill": fill,
             "dash": None, "fill_white": False, "stroke_white": False}
    gstack = []
    subpaths, current = [], []
    out = []
    xmin = ymin = 1e9
    xmax = ymax = -1e9

    def pt(x, y):
        return _apply(state["ctm"], x, y)

    def flush(op):
        nonlocal subpaths, current, xmin, ymin, xmax, ymax
        if current:
            subpaths.append(current)
            current = []
        if not subpaths:
            return
        do_fill = op in ("f", "F", "f*", "B", "B*", "b", "b*") and not state["fill_white"]
        do_stroke = op in ("S", "s", "B", "B*", "b", "b*") and not state["stroke_white"]
        if not (do_fill or do_stroke):
            subpaths = []
            return
        dparts, keep = [], False
        for sp in subpaths:
            if len(sp) < 2:
                continue
            sp = _rdp(sp, eps)
            if len(sp) < 2:
                continue
            xs = [p[0] for p in sp]
            ys = [p[1] for p in sp]
            lo_x, hi_x, lo_y, hi_y = min(xs), max(xs), min(ys), max(ys)
            # drop anything wholly in the running header / footer band
            if hi_y < crop_bottom or lo_y > ph - crop_top:
                continue
            keep = True
            xmin, xmax = min(xmin, lo_x), max(xmax, hi_x)
            ymin, ymax = min(ymin, lo_y), max(ymax, hi_y)
            # absolute moveto, then relative lineto: glyph outlines are long
            # chains of tiny deltas, so this is far shorter than absolute L.
            px, py = sp[0][0], -sp[0][1]
            d = "M" + _fmt(px) + " " + _fmt(py)
            for q in sp[1:]:
                qx, qy = q[0], -q[1]
                d += "l" + _fmt(qx - px) + " " + _fmt(qy - py)
                px, py = qx, qy
            dparts.append(d)
        subpaths = []
        if not keep or not dparts:
            return
        attrs = []
        if do_fill and do_stroke:
            attrs.append('fill="%s"' % fill)
            attrs.append('stroke="%s"' % stroke)
        elif do_fill:
            attrs.append('fill="%s"' % fill)
            attrs.append('stroke="none"')
        else:
            attrs.append('fill="none"')
            attrs.append('stroke="%s"' % stroke)
            attrs.append('stroke-width="%s"' % _fmt(max(state["lw"], 0.6)))
            attrs.append('stroke-linejoin="round"')
            attrs.append('stroke-linecap="round"')
        if state["dash"]:
            attrs.append('stroke-dasharray="%s"' % ",".join(
                _fmt(v) for v in state["dash"]))
        out.append((" ".join(attrs), "".join(dparts)))

    for op, args in _instructions(data):
        nums = [a for a in args if isinstance(a, (int, float))]
        try:
            if op == "q":
                gstack.append(dict(state))
            elif op == "Q":
                if gstack:
                    state = gstack.pop()
            elif op == "cm" and len(nums) >= 6:
                state["ctm"] = _mul(state["ctm"], tuple(nums[:6]))
            elif op == "w" and nums:
                state["lw"] = abs(nums[0])
            elif op == "d" and len(args) >= 2:
                seq = args[0] if isinstance(args[0], list) else []
                state["dash"] = [abs(v) for v in seq if isinstance(v, (int, float))] or None
            elif op in ("rg", "sc", "scn", "RG", "SC", "SCN", "g", "G", "k", "K"):
                # The ISA sheets are monochrome.  A white paint is used for the
                # table backgrounds and for knocking out lines; emitting it as
                # ink would cover the whole sheet, so record it explicitly.
                vals = [v for v in nums if isinstance(v, (int, float))]
                white = bool(vals) and (
                    (len(vals) == 1 and vals[0] >= 0.9) or
                    (len(vals) == 3 and min(vals) >= 0.9) or
                    (len(vals) == 4 and vals[3] == 0 and min(vals[:3]) >= 0.9) or
                    (op == "k" and len(vals) == 4 and max(vals) <= 0.02)
                )
                key = ("stroke_white" if op in ("RG", "SC", "SCN", "G", "K")
                       else "fill_white")
                state[key] = white
            elif op == "m" and len(nums) >= 2:
                if current:
                    subpaths.append(current)
                current = [pt(nums[0], nums[1])]
            elif op == "l" and len(nums) >= 2 and current:
                current.append(pt(nums[0], nums[1]))
            elif op == "c" and len(nums) >= 6 and current:
                x1, y1 = pt(nums[0], nums[1])
                x2, y2 = pt(nums[2], nums[3])
                x3, y3 = pt(nums[4], nums[5])
                # flatten a cubic to a short polyline
                x0, y0 = current[-1]
                for k in range(1, 7):
                    t = k / 6.0
                    u = 1 - t
                    current.append((u ** 3 * x0 + 3 * u * u * t * x1
                                    + 3 * u * t * t * x2 + t ** 3 * x3,
                                    u ** 3 * y0 + 3 * u * u * t * y1
                                    + 3 * u * t * t * y2 + t ** 3 * y3))
            elif op in ("v", "y") and len(nums) >= 4 and current:
                current.append(pt(nums[-2], nums[-1]))
            elif op == "h" and current:
                current.append(current[0])
                subpaths.append(current)
                current = []
            elif op == "re" and len(nums) >= 4:
                x, y, w, h = nums[:4]
                if current:
                    subpaths.append(current)
                current = [pt(x, y), pt(x + w, y), pt(x + w, y + h),
                           pt(x, y + h), pt(x, y)]
                subpaths.append(current)
                current = []
            elif op in ("S", "s", "f", "F", "f*", "B", "B*", "b", "b*", "n"):
                if op == "s" and current:
                    current.append(current[0])
                flush(op)
            # everything else (BT/ET/Tf/Tm/Tj/TJ/TD/gs/...) is ignored
        except (ValueError, IndexError, TypeError):
            continue

    if xmax <= xmin:
        return ""
    pad = 6.0
    vx, vy = xmin - pad, -(ymax + pad)
    vw, vh = (xmax - xmin) + 2 * pad, (ymax - ymin) + 2 * pad
    # Some table pages (ISA-5.1 pp. 23-26) are printed sideways.  Rotating
    # the whole path group and swapping the viewBox makes them readable.
    g_open = g_close = ""
    if rotate == -90:                      # (x,y) -> (y,-x)
        bx, by, bw, bh = vy, -(vx + vw), vh, vw
        g_open, g_close = '<g transform="rotate(-90)">', "</g>"
    elif rotate == 90:                    # (x,y) -> (-y,x)
        bx, by, bw, bh = -(vy + vh), vx, vh, vw
        g_open, g_close = '<g transform="rotate(90)">', "</g>"
    else:
        bx, by, bw, bh = vx, vy, vw, vh

    head = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="%s %s %s %s" '
            'role="img" aria-label="%s">' %
            (_fmt(bx), _fmt(by), _fmt(bw), _fmt(bh),
             _esc(title or "Symbol sheet")))
    if title:
        head += "<title>%s</title>" % _esc(title)
    if bg:
        head += '<rect x="%s" y="%s" width="%s" height="%s" fill="%s"/>' % (
            _fmt(bx), _fmt(by), _fmt(bw), _fmt(bh), bg)
    # merge consecutive paths sharing the same paint attributes; this keeps
    # draw order intact while removing tens of thousands of repeated tags.
    merged = []
    for attrs, d in out:
        if merged and merged[-1][0] == attrs:
            merged[-1][1] += d
        else:
            merged.append([attrs, d])
    return (head + g_open
            + "".join('<path %s d="%s"/>' % (a, d) for a, d in merged)
            + g_close + "</svg>")


def _esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


if __name__ == "__main__":
    import sys
    path = sys.argv[1]
    pg = int(sys.argv[2])
    dest = sys.argv[3] if len(sys.argv) > 3 else None
    s = page_svg(path, pg, "Sheet %d" % pg)
    print("svg bytes", len(s), "paths", s.count("<path"))
    if dest:
        open(dest, "w", encoding="utf-8").write(s)
        print("wrote", dest)
