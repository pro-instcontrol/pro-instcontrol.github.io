# -*- coding: utf-8 -*-
"""Shared kit for the §32.6–§32.11 section modules of Handbook Chapter 32.

The six remaining sections are large enough that each lives in its own module
(hb32_s6.py … hb32_s11.py).  They need the helpers in reader_hb_ch32.py, but
that module imports *them* — so a plain top-level import would be circular.
`R` is a lazy proxy: attribute lookup happens at call time, by which point
reader_hb_ch32 is fully loaded.  Nothing is imported from reader_hb_ch32 at
module-import time.

House rules (same as §32.1–§32.5):
  * Every section has sec_vi(), sec_en(), refs(lang), TITLE_EN, TITLE_VI,
    SUBS (flat (en, vi, depth) tuples — depth 0 for h3, 1 for h4/h5).
  * On the VI page h3/h4 take (Vietnamese, English); on the EN page just the
    English title.  h2 is "32.N <title>" with the *other* language as arg 2.
  * sec_index() builds #s32-N-<slug of English title>, so SUBS must use the
    exact English strings passed to the headings.
  * figure() takes a pre-built SVG body and the five caption/aria strings and
    returns R.fig(...), which swaps the aria-label to English on the EN page.
"""
import hb32fig as F
from hbfig import svg as _svg, STYLE, _f

# primitives re-exported so a section module can build a schematic directly
from hb32fig import (E, G, S, FILL, DARK, _defs, _lbl, _fs, _mix, _line,
                     _rect, _path, _poly, _pl, _circ, _ell, _arr, _darr,
                     _band, _arc, _on_line, _therm, _zz, _batt, _res_h,
                     _res_v, _source, _term, _dot, _gnd, _chart, _blk)


def _R():
    import reader_hb_ch32
    return reader_hb_ch32


class _Proxy(object):
    """Late-bound view of reader_hb_ch32's helpers."""

    def __getattr__(self, name):
        return getattr(_R(), name)


R = _Proxy()


def figure(num, W, H, body, title_vi, cap_vi, cap_en, aria_vi, aria_en, lang):
    """Build a figure from an SVG *body* string and call the reader's fig().

    `svg()` bakes title_vi into aria-label; reader.fig() replaces it with the
    English aria on the EN page, exactly as hb32fig's own figures do.
    """
    s = _svg(W, H, body, title_vi)
    return R.fig(num, (s, cap_vi, cap_en, aria_vi, aria_en), lang)


def chart(num, W, H, xr, yr, xt, yt, curves, xlab, ylab,
          cap_vi, cap_en, aria_vi, aria_en, lang, title_vi, extra="",
          pad=(56, 20, 18, 42)):
    """A line-chart figure. `curves` is a list of (points, css-class) pairs;
    classes c1/c2/c3/d1 come from hbfig.STYLE. `extra` is appended to the SVG
    body after the axes and curves, for annotations."""
    o = [_defs()]
    F._chart(o, xr, yr, xt, yt, curves, xlab, ylab, w=W, h=H, pad=pad)
    if extra:
        o.append(extra)
    return figure(num, W, H, "".join(o), title_vi, cap_vi, cap_en,
                  aria_vi, aria_en, lang)


def diagram(num, W, H, parts, cap_vi, cap_en, aria_vi, aria_en, lang, title_vi):
    """A schematic figure from a list of SVG primitive strings."""
    return figure(num, W, H, "".join([_defs()] + parts), title_vi,
                  cap_vi, cap_en, aria_vi, aria_en, lang)
