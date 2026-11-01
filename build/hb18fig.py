# -*- coding: utf-8 -*-
"""Figures for Handbook Chapter 18 — Time Measurement (Michael A. Lombardi, NIST).

Source has exactly three figures (18.1 one-way, 18.2 common-view, 18.3 two-way
time transfer). No padding: FIGS is a 3-figure set.
"""
import math as _m

from hbfig import GOLD, INK, MUTED, TXT, _f, svg, _fig

E = "#2a2a2a"
G = "#b45309"
S = "#888888"
P = "#ffffff"


def _lbl(x, y, txt, cls="t", anchor="start"):
    return '<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>' % (
        cls, _f(x), _f(y), anchor, txt)


def _defs():
    return ('<defs>'
            '<marker id="ah18" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<marker id="ah18g" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '</defs>' % (E, G))


def _arr(x1, y1, x2, y2, col=E, marker="ah18", sw=1.4):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-end="url(#%s)"/>' % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, marker))


def _box(x, y, w, h, t, col=E, fill="#ffffff", fs=12):
    o = ['<rect x="%s" y="%s" width="%s" height="%s" rx="6" fill="%s" stroke="%s" stroke-width="1.4"/>'
         % (_f(x), _f(y), _f(w), _f(h), fill, col)]
    lines = t.split("\n")
    for i, ln in enumerate(lines):
        yy = y + h / 2.0 + (i - (len(lines) - 1) / 2.0) * (fs + 3) + fs * 0.35
        o.append(_lbl(x + w / 2.0, yy, ln, "tb", "middle"))
    return "".join(o)


# ---------------------------------------------------------------- 18.1
def fig_18_1():
    o = [_defs()]
    o.append(_box(40, 78, 120, 74, "Máy phát\n(nguồn T)"))
    o.append(_box(520, 78, 120, 74, "Máy thu\n(đích R)"))
    # medium band
    o.append('<rect x="180" y="96" width="320" height="38" fill="#f7f3ea" stroke="%s" '
             'stroke-width="1" stroke-dasharray="5 4"/>' % G)
    o.append(_arr(160, 115, 520, 115, G, "ah18g", 1.6))
    o.append(_lbl(340, 88, "τ_ab  (trễ đường truyền)", "tg", "middle"))
    o.append(_lbl(340, 152, "môi trường: cáp, quang, vô tuyến, điện thoại, mạng…", "ts", "middle"))
    o.append(_lbl(340, 200, "Một chiều — người dùng tự hiệu chỉnh đường truyền (nếu cần)", "ts", "middle"))
    return _fig(
        svg(680, 220, "".join(o),
            "Sơ đồ truyền thời gian một chiều: máy phát, môi trường có trễ τ_ab, máy thu"),
        "Hình 18.1 · Truyền thời gian một chiều. Tín hiệu từ máy phát đến máy thu bị môi trường "
        "làm trễ một lượng τ_ab; muốn kết quả tốt nhất, người dùng phải ước lượng τ_ab và hiệu "
        "chỉnh đường truyền bằng cách bù trễ.",
        "Figure 18.1 · One-way time transfer. The signal from the transmitter to the receiver is "
        "delayed τ_ab by the medium; for the best results the user must estimate τ_ab and "
        "calibrate the path by compensating for the delay.",
        "Sơ đồ khối truyền thời gian một chiều từ máy phát qua môi trường có trễ tới máy thu",
        "Block diagram of one-way time transfer from transmitter through a delay medium to receiver")


# ---------------------------------------------------------------- 18.2
def fig_18_2():
    o = [_defs()]
    # reference transmitter at top centre
    o.append(_box(270, 30, 140, 64, "Máy phát chuẩn\nR", E, "#ffffff"))
    # receiver A bottom-left, B bottom-right
    o.append(_box(60, 168, 150, 64, "Máy thu A\n(R − A)", E, "#ffffff"))
    o.append(_box(470, 168, 150, 64, "Máy thu B\n(R − B)", E, "#ffffff"))
    # arrows from R to A and B
    o.append(_arr(300, 94, 150, 168, G, "ah18g", 1.5))
    o.append(_arr(380, 94, 530, 168, G, "ah18g", 1.5))
    o.append(_lbl(196, 132, "τ_ra", "tg", "middle"))
    o.append(_lbl(484, 132, "τ_rb", "tg", "middle"))
    # exchange arrow between A and B
    o.append('<line x1="210" y1="200" x2="470" y2="200" stroke="%s" stroke-width="1.4" '
             'stroke-dasharray="6 4" marker-end="url(#ah18)"/>' % E)
    o.append('<line x1="470" y1="212" x2="210" y2="212" stroke="%s" stroke-width="1.4" '
             'stroke-dasharray="6 4" marker-end="url(#ah18)"/>' % E)
    o.append(_lbl(340, 196, "trao đổi dữ liệu", "ts", "middle"))
    o.append(_lbl(340, 232, "(Clock A − Clock B) − (τ_ra − τ_rb)", "ts", "middle"))
    return _fig(
        svg(680, 250, "".join(o),
            "Sơ đồ truyền thời gian common-view: một máy phát chuẩn R nhìn thấy đồng thời hai máy thu A và B"),
        "Hình 18.2 · Truyền thời gian common-view. Một máy phát chuẩn R nằm trong “tầm nhìn chung” "
        "của hai máy thu A và B; mỗi máy so sánh tín hiệu nhận đồng thời với đồng hồ cục bộ rồi trao "
        "đổi dữ liệu, nhờ đó các sai số đường truyền chung triệt tiêu và thu được (Clock A − Clock B) "
        "− (τ_ra − τ_rb).",
        "Figure 18.2 · Common-view time transfer. A single reference transmitter R is in “common "
        "view” of two receivers A and B; each compares the simultaneously received signal to its "
        "local clock and the two exchange data, so common path errors cancel and the result is "
        "(Clock A − Clock B) − (τ_ra − τ_rb).",
        "Sơ đồ common-view: máy phát chuẩn R phát tới hai máy thu A và B, hai máy trao đổi dữ liệu",
        "Common-view diagram: reference transmitter R broadcasts to receivers A and B, which exchange data")


# ---------------------------------------------------------------- 18.3
def fig_18_3():
    o = [_defs()]
    o.append(_box(50, 84, 150, 84, "Trạm A\n(Clock A)"))
    o.append(_box(480, 84, 150, 84, "Trạm B\n(Clock B)"))
    # A -> B (top), B -> A (bottom), same medium
    o.append(_arr(200, 108, 480, 108, G, "ah18g", 1.7))
    o.append(_arr(480, 148, 200, 148, E, "ah18", 1.7))
    o.append(_lbl(340, 100, "τ_ab  (A → B)", "tg", "middle"))
    o.append(_lbl(340, 168, "τ_ba  (B → A)", "t", "middle"))
    o.append(_lbl(340, 196, "trao đổi đồng thời qua cùng một môi trường", "ts", "middle"))
    o.append(_lbl(340, 218, "nếu đường truyền thuận nghịch (τ_ab = τ_ba) → A − B xác định chính xác", "ts", "middle"))
    return _fig(
        svg(680, 236, "".join(o),
            "Sơ đồ truyền thời gian hai chiều: hai trạm A và B đồng thời phát và thu qua cùng môi trường"),
        "Hình 18.3 · Truyền thời gian hai chiều. Hai trạm A và B đồng thời phát và thu qua cùng một "
        "môi trường; trạm A ghi A − (B + τ_ba), trạm B ghi B − (A + τ_ab). Hiệu hai tập số đọc cho "
        "2(A − B) − (τ_ba − τ_ab); nếu đường truyền thuận nghịch (τ_ab = τ_ba) thì A − B được xác định "
        "hoàn hảo, đạt tới độ không đảm bảo ±1 ns.",
        "Figure 18.3 · Two-way time transfer. Sites A and B simultaneously transmit and receive "
        "through the same medium; A records A − (B + τ_ba) and B records B − (A + τ_ab). The "
        "difference gives 2(A − B) − (τ_ba − τ_ab); if the path is reciprocal (τ_ab = τ_ba) then "
        "A − B is known perfectly, reaching ±1 ns uncertainty.",
        "Sơ đồ hai chiều: hai trạm A và B trao đổi đồng thời tín hiệu qua cùng môi trường với trễ τ_ab và τ_ba",
        "Two-way diagram: sites A and B exchange signals simultaneously through one medium with delays τ_ab and τ_ba")


FIGS = [fig_18_1, fig_18_2, fig_18_3]


def fig(n):
    return FIGS[n - 1]()
