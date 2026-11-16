# -*- coding: utf-8 -*-
"""Vector figures for Book 6, Unit 10 — Manual Valves VI: Butterfly and
Pinch Valves (book ch. 3, Figures 3-69 … 3-92).  Each function returns the
standard 5-tuple (svg, caption_vi, caption_en, aria_vi, aria_en).

Manufacturer cutaways are redrawn as simplified vector cross-sections that
keep the topology and the variant features named in the original caption;
a numbered bilingual legend carries the feature names.  Figures 3-73, 3-84
and 3-85…3-87 are schematic redraws of installation precautions, disc
geometry and torque/pressure-drop characteristics described in the text.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GREY, INK, _arrow, _circle, _defs, _fig, _line,
                  _poly, _rect, _txt, svg)
from vshfig3 import (BULB_F, PACK_F, RING_F, _ell, _emit, _emit_legend)

FIGS7 = {}


def _reg7(f):
    FIGS7[f.__name__] = f
    return f


BODY_F = "#f5f5f1"
SEAT_F = "#e2e2dc"
DISC_F = "#d9d9d2"
RUBBER_F = "#c9d5c9"
PTFE_F = "#dfe8dd"


# -------------------------------------------------------- butterfly builder
def _bf_ops(liner="replaceable", disc="single", seal="interference",
            split_body=False, high_perf=False, double_disc=False,
            tilt=14, offset=False):
    """Butterfly valve cross-section; disc centre at local (0, 100)."""
    o = []
    body = [(-88, 66), (-58, 56), (0, 52), (58, 56), (88, 66),
            (88, 136), (58, 146), (0, 150), (-58, 146), (-88, 136)]
    o.append(("poly", body, BODY_F, 1.3, INK, "", True))
    for sx in (-1, 1):
        o.append(("poly", [(sx * 96, 72), (sx * 88, 72), (sx * 88, 130),
                           (sx * 96, 130)], RING_F, 1.2, INK, "", True))
        o.append(("line", sx * 88, 88, sx * 28, 88, 1.2, INK, ""))
        o.append(("line", sx * 88, 112, sx * 28, 112, 1.2, INK, ""))
    if split_body:
        o.append(("line", -88, 101, 88, 101, 1.1, INK, "4 3"))
    # seat / liner
    if liner == "bonded":
        for sx in (-1, 1):
            o.append(("poly", [(sx * 28, 84), (sx * 34, 84),
                               (sx * 34, 116), (sx * 28, 116)],
                      RUBBER_F, 1.1, INK, "", True))
    elif liner == "band":
        for sx in (-1, 1):
            o.append(("poly", [(sx * 26, 82), (sx * 34, 82),
                               (sx * 34, 118), (sx * 26, 118)],
                      RUBBER_F, 1.1, INK, "", True))
            o.append(("line", sx * 34, 80, sx * 34, 120, 1.1, INK, ""))
    elif liner == "ptfe":
        for sx in (-1, 1):
            o.append(("poly", [(sx * 26, 82), (sx * 34, 82),
                               (sx * 34, 118), (sx * 26, 118)],
                      PTFE_F, 1.1, INK, "", True))
    else:
        for sx in (-1, 1):
            o.append(("poly", [(sx * 28, 84), (sx * 32, 84),
                               (sx * 32, 116), (sx * 28, 116)],
                      SEAT_F, 1.0, INK, "", True))
    # special seat features
    if seal == "o-ring-backed":
        for sx in (-1, 1):
            o.append(("circ", sx * 36, 100, 4.2, 1.0, INK, RING_F))
    elif seal == "ptfe-lip":
        for sx in (-1, 1):
            o.append(("poly", [(sx * 26, 86), (sx * 32, 82),
                               (sx * 32, 118), (sx * 26, 114)],
                      PTFE_F, 1.0, INK, "", True))
    elif seal == "titanium":
        for sx in (-1, 1):
            o.append(("poly", [(sx * 24, 86), (sx * 30, 82),
                               (sx * 30, 118), (sx * 24, 114)],
                      PTFE_F, 1.0, INK, "", True))
            o.append(("line", sx * 32, 80, sx * 32, 120, 1.4, INK, ""))
    elif seal == "encapsulated":
        for sx in (-1, 1):
            o.append(("circ", sx * 30, 100, 5.0, 1.0, INK, PTFE_F))
    elif seal == "membrane":
        for sx in (-1, 1):
            o.append(("poly", [(sx * 26, 84), (sx * 30, 78),
                               (sx * 30, 122), (sx * 26, 116)],
                      "none", 1.0, INK, "", False))
    elif seal == "inflatable-body":
        for sx in (-1, 1):
            o.append(("circ", sx * 32, 100, 5.5, 1.1, INK, RUBBER_F))
    # disc — edge-on, tilted through the bore
    dy = math.tan(math.radians(tilt)) * 30
    if double_disc:
        for k in (-1, 1):
            yy = 100 + k * 8
            o.append(("poly", [(-30, yy - dy), (30, yy + dy),
                               (30, yy + dy + 7), (-30, yy - dy + 7)],
                      DISC_F, 1.2, INK, "", True))
    else:
        o.append(("poly", [(-32, 100 - dy), (32, 100 + dy),
                           (32, 100 + dy + 9), (-32, 100 - dy + 9)],
                  DISC_F, 1.3, INK, "", True))
    if disc == "offset":
        o.append(("circ", 0, 92, 3, 1.0, INK, RING_F))
    if seal == "inflatable-rim":
        for sx in (-1, 1):
            o.append(("circ", sx * 30, 100 + sx * dy, 4.6, 1.1, INK,
                      RUBBER_F))
    if high_perf:
        o.append(("line", -6, 100, -6, -46, 1.4, INK, ""))
    else:
        o.append(("line", 0, 100, 0, -138, 2.2, INK, ""))
    o.append(("poly", [(-12, -72), (12, -72), (12, -60), (-12, -60)],
              PACK_F, 1.0, INK, "", True))
    o.append(("poly", _ell(0, -150, 26, 6), "#e8e8e2", 1.2, INK, "", True))
    o.append(("circ", 0, -150, 5, 1.2, INK, RING_F))
    return o


def _bf_fig(num, ten, tvi, marks, ops, courtesy="", sub="",
            w=560, h=380, xleg=402):
    o2 = []
    _emit(o2, ops, rot=0.0, cx=0, cy=0, dx=200, dy=180)
    ay = 280
    o2.append(_line(82, ay, 104, ay, 1.6, color=BLUE))
    o2.append(_poly([(104, ay), (96, ay - 3.5), (96, ay + 3.5)],
                    fill=BLUE, sw=0, close=True))
    o2.append(_line(296, ay, 318, ay, 1.6, color=BLUE))
    o2.append(_poly([(296, ay), (304, ay - 3.5), (304, ay + 3.5)],
                    fill=BLUE, sw=0, close=True))
    if sub:
        o2.append(_txt(200, h - 18, sub, 6.9, color=GREY))
    _emit_legend(o2, xleg, marks)
    if courtesy:
        o2.append(_txt(476, h - 14, courtesy, 6.6, color=GREY))
    return _fig(svg(w, h, _defs() + "".join(o2), ten),
                "Hình 3-%d · %s (vẽ lại).%s"
                % (num, tvi, (" Nguồn: " + courtesy) if courtesy else ""),
                "Figure 3-%d · %s — redrawn.%s"
                % (num, ten, (" (Courtesy of " + courtesy.rstrip(".") + ".)")
                   if courtesy else ""),
                tvi, ten)


# Callout positions are canvas coordinates.  The cutaway is translated to
# dx=200, dy=180, so the bore lies near y=280, the stem packing near y=108.
BF_MARK_POS = {
    69: [(200, 280), (200, 320), (228, 280), (172, 280)],
    70: [(172, 280), (200, 280), (228, 280), (200, 320)],
    71: [(200, 280), (172, 280), (228, 280), (200, 320)],
    72: [(172, 280), (200, 250), (200, 280), (228, 280)],
    76: [(172, 280), (228, 280), (200, 320), (200, 280)],
    77: [(172, 280), (200, 108), (228, 280), (200, 320)],
    78: [(172, 280), (228, 280), (200, 250), (200, 280)],
    79: [(172, 280), (200, 108), (228, 280), (200, 320)],
    80: [(172, 280), (228, 280), (200, 108), (200, 320)],
    82: [(172, 280), (228, 280), (200, 320), (200, 280)],
    83: [(200, 280), (172, 280), (228, 280), (200, 320)],
}


def _m(cfg, sub="", **kw):
    num, ten, tvi, marks, courtesy = cfg
    if num in BF_MARK_POS:
        marks = [((vi, en), pos)
                 for ((vi, en), _), pos in zip(marks, BF_MARK_POS[num])]
    return _bf_fig(num, ten, tvi, marks, _bf_ops(**kw),
                   courtesy=courtesy, sub=sub)


# ------------------------------------------------------- butterfly cutaways
@_reg7
def fig_vsh_3_69():
    cfg = (69, "Butterfly valves with metal disc and metal seat "
           "(nominal- and low-leakage)",
           "Van bướm đĩa kim loại và chỗ kín kim loại (rò rỉ danh nghĩa và thấp)",
           [(("đĩa và chỗ kín đều kim loại", "metal disc and metal seat"),
             (200, 116)),
            (("phù hợp khống chế lưu lượng", "for throttling and flow control"),
             (166, 300)),
            (("có thể có xít piston trên mép đĩa",
             "piston ring on the disc rim available"), (234, 116)),
            (("rò rỉ danh nghĩa / thấp", "nominal / low leakage"),
             (176, 322))],
           "GEC-Elliot Control Valves Limited.")
    return _m(cfg, liner="none")


@_reg7
def fig_vsh_3_70():
    cfg = (70, "Butterfly valve with resilient replaceable liner and "
           "interference-seated disc",
           "Van bướm có lớp lót đàn hồi thay được và đĩa ép kín ghen",
           [(("lớp lót chữ U lồng vào thân, không dán",
             "U-shaped liner slipped over body, unbonded"), (166, 300)),
            (("đĩa ép kín ghen", "interference-seated disc"), (200, 116)),
            (("dễ thay lớp lót", "liner readily replaceable"), (234, 300)),
            (("đĩa quay tẩy qua lớp lót", "disc wipes against the liner"),
             (176, 322))],
           "Keystone International, Inc.")
    return _m(cfg, liner="replaceable")


@_reg7
def fig_vsh_3_71():
    cfg = (71, "Butterfly valve with resilient liner and interference-seated "
           "double disc for double block and bleed, isolating foodstuffs "
           "from cleaning-in-place fluids",
           "Van bướm có lớp lót đàn hồi và đĩa kép ép ghen cho chặn kép xả "
           "trung gian, cô lập thực phẩm khỏi chất tẩy rửa tại chỗ",
           [(("đĩa kép ép ghen", "interference-seated double disc"),
             (200, 116)),
            (("lớp lót đàn hồi", "resilient liner"), (166, 300)),
            (("chặn kép xả trung gian", "double block and bleed"),
             (234, 300)),
            (("cô lập thực phẩm / CIP", "isolates foodstuffs from CIP"),
             (176, 322))],
           "Amri SA.")
    return _m(cfg, liner="bonded", double_disc=True)


@_reg7
def fig_vsh_3_72():
    cfg = (72, "Butterfly valve with resilient replaceable liner and "
           "interference-seated disc, liner bonded to a steel band, body "
           "split in two halves",
           "Van bướm có lớp lót thay được dán vào băng thép, thân chia đôi, "
           "đĩa ép ghen",
           [(("lớp lót dán vào băng thép", "liner bonded to a steel band"),
             (166, 300)),
            (("thân chia làm hai nửa", "body split in two halves"),
             (234, 148)),
            (("đĩa ép ghen", "interference-seated disc"), (200, 116)),
            (("lót PTFE cứng đưa vào được", "rigid PTFE liner insertable"),
             (176, 322))],
           "DeZurik.")
    return _m(cfg, liner="band", split_body=True)


# ------------------------------------------------------ installation detail
@_reg7
def fig_vsh_3_73():
    """Proper vs improper installation of rubber-lined butterfly valves."""
    w, h = 560, 380
    o = [_defs()]

    def panel(x, y, good, label):
        o.append(_rect(x - 108, y - 46, 216, 92, fill=BODY_F, sw=1.2))
        # pipe flanges and the wafer liner
        o.append(_rect(x - 108, y - 22, 18, 44, fill=RING_F, sw=1.1))
        o.append(_rect(x + 90, y - 22, 18, 44, fill=RING_F, sw=1.1))
        o.append(_rect(x - 90, y - 18, 180, 36, fill=RUBBER_F, sw=1.0))
        o.append(_line(x, y - 18, x, y + 18, 1.2, INK))
        if good:
            o.append(_txt(x, y + 4, "liner supported", 6.6, color=GREY))
            o.append(_txt(x, y - 62, label, 7.2, color=INK, weight="bold"))
        else:
            o.append(_poly([(x - 70, y - 18), (x - 40, y - 26),
                            (x - 10, y - 18)], "none", 1.1, INK, "",
                           False))
            o.append(_txt(x, y + 4, "unsupported liner", 6.6, color=GREY))
            o.append(_txt(x, y - 62, label, 7.2, color=INK, weight="bold"))
        o.append(_circle(x, y - 46, 7.5, sw=1.2, color=INK))
        o.append(_txt(x, y - 45.5, "1" if good else "2", 8.0, weight="bold"))

    panel(140, 120, True, "Đúng / Proper: weld-neck flanges")
    panel(140, 270, False, "Sai / Improper: slip-on flanges")
    for i, (vi, en) in enumerate([
            ("đặt đĩa gần đóng lúc lắp", "disc near-closed while handling"),
            ("quay đĩa mở hoàn toàn trước khi siết bulông",
             "rotate fully open before tightening bolts"),
            ("dùng bích cổ hàn, không thêm gioăng",
             "use weld-neck flanges, no extra gaskets")]):
        yy = 82 + i * 60
        o.append(_circle(404, yy - 3, 7, sw=1.0, color=INK))
        o.append(_txt(404, yy - 1, str(i + 1), 7.6, weight="bold"))
        o.append(_txt(418, yy - 4, vi, 7.6, anchor="start"))
        o.append(_txt(418, yy + 6, en, 6.6, anchor="start", color=GREY))
    o.append(_txt(476, h - 14, "Keystone International, Inc.", 6.6,
                  color=GREY))
    return _fig(svg(w, h, "".join(o), "Butterfly valve installation"),
                "Hình 3-73 · Cách lắp đúng và sai cho van bướm chỗ kín ghen "
                "có lớp lót cao su thay được (vẽ lại). Nguồn: Keystone "
                "International, Inc.",
                "Figure 3-73 · Proper and improper installation of "
                "interference-seated butterfly valves with replaceable "
                "rubber liner — schematic redrawn. (Courtesy of Keystone "
                "International, Inc.)",
                "Lắp đúng và sai van bướm có lớp lót cao su.",
                "Proper and improper butterfly valve installation.")


# --------------------------------------------------- scrap views and seats
@_reg7
def fig_vsh_3_74():
    """Sealing element carried on the rim of the disc — heavy O-ring w/tail."""
    o = [_defs()]
    cx = 200
    o.append(_poly([(cx - 60, 70), (cx - 28, 70), (cx - 28, 230),
                    (cx - 60, 230)], fill=DISC_F, sw=1.3, close=True))
    o.append(_circle(cx - 28, 150, 12, fill=RUBBER_F, sw=1.2))
    o.append(_poly([(cx - 28, 138), (cx - 8, 126), (cx - 8, 174),
                    (cx - 28, 162)], fill=RUBBER_F, sw=1.1, close=True))
    o.append(_line(cx - 8, 150, cx + 26, 150, 1.2, INK))
    o.append(_txt(cx - 40, 254, "O-ring tiết diện lớn + đuôi kẹp / "
                  "heavy O-ring with clamped tail", 6.8, color=GREY))
    for i, (vi, en) in enumerate([
            ("vòng kín tiết diện lớn trên mép đĩa", "heavy O-ring on disc rim"),
            ("đuôi kẹp chỉnh độ ghen", "clamped tail adjusts interference"),
            ("biến dạng trên mặt rộng, momen thấp",
             "deforms on a wide face, low torque"),
            ("chỉ chế tạo cỡ lớn, áp cao", "large sizes, high pressures")]):
        yy = 74 + i * 42
        o.append(_circle(404, yy - 3, 7, sw=1.0, color=INK))
        o.append(_txt(404, yy - 1, str(i + 1), 7.6, weight="bold"))
        o.append(_txt(418, yy - 4, vi, 7.6, anchor="start"))
        o.append(_txt(418, yy + 6, en, 6.6, anchor="start", color=GREY))
    o.append(_circle(cx - 28, 150, 7.5, sw=1.2, color=INK))
    o.append(_txt(cx - 28, 150.5, "1", 8.0, weight="bold"))
    o.append(_circle(cx - 6, 142, 7.5, sw=1.2, color=INK))
    o.append(_txt(cx - 6, 142.5, "2", 8.0, weight="bold"))
    o.append(_txt(476, 320, "Boving &amp; Co., Limited.", 6.6, color=GREY))
    return _fig(svg(560, 340, "".join(o), "Disc-rim resilient sealing element"),
                "Hình 3-74 · Mảnh cắt van bướm chỗ kín ghen cho thấy phần tử "
                "làm kín đàn hồi trên mép đĩa (vẽ lại). Nguồn: Boving &amp; "
                "Co., Limited.",
                "Figure 3-74 · Scrap view of interference-seated butterfly "
                "valve showing the resilient sealing element carried on the "
                "disc rim — redrawn. (Courtesy of Boving &amp; Co., Limited.)",
                "Phần tử kín đàn hồi trên mép đĩa.",
                "Resilient seal carried on the disc rim.")


@_reg7
def fig_vsh_3_75():
    o = [_defs()]
    cx = 200
    o.append(_poly([(cx - 60, 70), (cx - 28, 70), (cx - 28, 230),
                    (cx - 60, 230)], fill=DISC_F, sw=1.3, close=True))
    o.append(_circle(cx - 30, 150, 14, fill=RUBBER_F, sw=1.2))
    o.append(_circle(cx - 30, 150, 7, fill="#ffffff", sw=1.0))
    o.append(_line(cx - 30, 150, cx + 30, 150, 1.1, INK, "4 2"))
    o.append(_txt(cx - 40, 254, "ống hơi bơm qua trục / hose pressurised "
                  "through the shaft", 6.8, color=GREY))
    for i, (vi, en) in enumerate([
            ("ống hơi gắn mép đĩa", "inflatable hose on disc rim"),
            ("cốt kim loại gia cố bên trong", "internal metallic conduit"),
            ("xì hơi khi mở, bơm căng khi đóng", "deflate to open, inflate "
             "to seal"),
            ("chế tạo đến cỡ lớn nhất", "made to the largest sizes")]):
        yy = 74 + i * 42
        o.append(_circle(404, yy - 3, 7, sw=1.0, color=INK))
        o.append(_txt(404, yy - 1, str(i + 1), 7.6, weight="bold"))
        o.append(_txt(418, yy - 4, vi, 7.6, anchor="start"))
        o.append(_txt(418, yy + 6, en, 6.6, anchor="start", color=GREY))
    o.append(_circle(cx - 30, 150, 7.5, sw=1.2, color=INK))
    o.append(_txt(cx - 30, 150.5, "1", 8.0, weight="bold"))
    o.append(_circle(cx - 4, 150, 7.5, sw=1.2, color=INK))
    o.append(_txt(cx - 4, 150.5, "2", 8.0, weight="bold"))
    o.append(_txt(476, 320, "Boving &amp; Co., Limited.", 6.6, color=GREY))
    return _fig(svg(560, 340, "".join(o), "Inflatable disc-rim seal"),
                "Hình 3-75 · Mảnh cắt van bướm cho thấy phần tử làm kín dạng "
                "ống hơi bơm căng trên mép đĩa (vẽ lại). Nguồn: Boving &amp; "
                "Co., Limited.",
                "Figure 3-75 · Scrap view of butterfly valve showing an "
                "inflatable sealing element carried on the disc rim — "
                "redrawn. (Courtesy of Boving &amp; Co., Limited.)",
                "Ống hơi bơm căng trên mép đĩa.",
                "Inflatable seal on the disc rim.")


@_reg7
def fig_vsh_3_76():
    cfg = (76, "Butterfly valve with inflatable sealing element carried in "
           "a recess of the valve body",
           "Van bướm có phần tử làm kín dạng bơm căng đặt trong hốc thân",
           [(("màng ống tiết diện chữ T", "tubular diaphragm, T section"),
             (166, 300)),
            (("đặt trong rãnh thân", "mounted in a body slot"),
             (234, 300)),
            (("bơm căng lúc đóng, xì lúc mở", "pressurised on closing, "
             "depressurised on opening"), (176, 322)),
            (("đĩa", "disc"), (200, 116))],
           "GEC-Elliot Control Valves, Limited.")
    return _m(cfg, liner="bonded", seal="inflatable-body")


# ------------------------------------------------- high-performance series
@_reg7
def fig_vsh_3_77():
    cfg = (77, "Metal-seated high-performance butterfly valve with tapered "
           "seating faces and sealing of the disc at a non-interlocking angle",
           "Van bướm hiệu năng cao chỗ kín kim loại, mặt kín côn, đĩa kín ở "
           "góc không tự khóa",
           [(("mặt kín côn trên chu vi ê-líp", "tapered faces on elliptical "
             "circumference"), (166, 300)),
            (("bản lề lệch kép", "double offset hinge"), (200, 116)),
            (("tải kín do momen đóng + momen thủy tĩnh",
             "load from closing torque + hydrostatic torque"),
             (234, 300)),
            (("đến 35 bar, −200…650 °C", "up to 35 bar, -200…650 °C"),
             (176, 322))],
           "Clow Corporation.")
    return _m(cfg, liner="none", disc="offset", seal="ptfe-lip",
              high_perf=True, tilt=10)


@_reg7
def fig_vsh_3_78():
    cfg = (78, "High-performance butterfly valve with O-ring-backed plastic seat",
           "Van bướm hiệu năng cao có chỗ kín nhựa đỡ bằng O-ring",
           [(("vòng kín nhựa chữ U", "U-shaped plastic seal ring"),
             (166, 300)),
            (("O-ring đỡ tạo ứng suất ban đầu", "O-ring backing gives "
             "initial compression"), (234, 300)),
            (("lắp trong rãnh chữ T thân", "mounted in a body T-slot"),
             (200, 148)),
            (("áp chất lỏng ép vòng vào mép đĩa", "fluid pressure forces "
             "ring onto disc rim"), (176, 322))],
           "Posi-Seal International, Inc.")
    return _m(cfg, liner="ptfe", seal="o-ring-backed", high_perf=True)


@_reg7
def fig_vsh_3_79():
    cfg = (79, "High-performance butterfly valve with flexible PTFE lip seat",
           "Van bướm hiệu năng cao có chỗ kín môi PTFE mềm",
           [(("môi PTFE có đuôi kẹp", "PTFE lip seal with tail"),
             (166, 300)),
            (("trục đĩa lệch khỏi mặt chỗ kín và tâm van",
             "disc axis offset from seat plane and valve centreline"),
             (200, 116)),
            (("vào chỗ kín bằng tác dụng cam", "camming action into the seat"),
             (234, 300)),
            (("kín hai chiều", "seals in both directions"), (176, 322))],
           "Jamesbury International Corp.")
    return _m(cfg, seal="ptfe-lip", disc="offset", high_perf=True,
              tilt=11)


@_reg7
def fig_vsh_3_80():
    cfg = (80, "High-performance butterfly valve with PTFE lip seal "
           "supported by a titanium metal ring",
           "Van bướm hiệu năng cao có môi kín PTFE đỡ bằng vòng titan",
           [(("môi kín PTFE", "PTFE lip seal"), (166, 300)),
            (("vòng đỡ titan", "titanium support ring"), (234, 300)),
            (("trục lệch kép", "double offset axis"), (200, 116)),
            (("có phiên bản kim loại và chịu lửa", "metal and fire-tested "
             "versions available"), (176, 322))],
           "DeZurik.")
    return _m(cfg, seal="titanium", disc="offset", high_perf=True,
              tilt=11)


@_reg7
def fig_vsh_3_81():
    o = [_defs()]
    cx = 200
    o.append(_poly([(cx - 60, 70), (cx - 28, 70), (cx - 28, 230),
                    (cx - 60, 230)], fill=BODY_F, sw=1.3, close=True))
    o.append(_circle(cx - 22, 150, 15, fill=PTFE_F, sw=1.1))
    o.append(_circle(cx - 22, 150, 9, fill=RING_F, sw=1.1))
    o.append(_line(cx - 22, 150, cx + 26, 150, 1.0, INK, "4 2"))
    o.append(_txt(cx - 42, 254, "O-ring bọc PTFE / PTFE-encapsulated O-ring",
                  6.8, color=GREY))
    for i, (vi, en) in enumerate([
            ("O-ring ê-lô-me bọc PTFE", "PTFE-encapsulated elastomeric O-ring"),
            ("O-ring cho độ đàn hồi", "O-ring supplies elasticity"),
            ("vỏ PTFE bảo vệ khỏi chất lỏng", "PTFE envelope protects it"),
            ("có phiên bản chịu lửa", "fire-tested version available")]):
        yy = 74 + i * 42
        o.append(_circle(404, yy - 3, 7, sw=1.0, color=INK))
        o.append(_txt(404, yy - 1, str(i + 1), 7.6, weight="bold"))
        o.append(_txt(418, yy - 4, vi, 7.6, anchor="start"))
        o.append(_txt(418, yy + 6, en, 6.6, anchor="start", color=GREY))
    o.append(_circle(cx - 22, 150, 7.5, sw=1.2, color=INK))
    o.append(_txt(cx - 22, 150.5, "1", 8.0, weight="bold"))
    o.append(_txt(476, 320, "Bray Valve and Controls.", 6.6, color=GREY))
    return _fig(svg(560, 340, "".join(o), "PTFE-encapsulated O-ring seat"),
                "Hình 3-81 · Mảnh cắt van bướm hiệu năng cao cho thấy chỗ kín "
                "O-ring ê-lô-me bọc PTFE (vẽ lại). Nguồn: Bray Valve and "
                "Controls.",
                "Figure 3-81 · Scrap view of a high-performance butterfly "
                "valve showing a PTFE-encapsulated elastomeric O-ring seat — "
                "redrawn. (Courtesy of Bray Valve and Controls)",
                "Chỗ kín O-ring bọc PTFE.", "PTFE-encapsulated O-ring seat.")


@_reg7
def fig_vsh_3_82():
    cfg = (82, "High-performance butterfly valve with flexible membrane "
           "returning the seat to its original position after each operation",
           "Van bướm hiệu năng cao có màng dẻo đưa chỗ kín về vị trí ban đầu",
           [(("màng dẻo đỡ chỗ kín", "pliant membrane supports the seat"),
             (166, 300)),
            (("chỗ kín PTFE chữ T", "T-shaped PTFE seat member"),
             (234, 300)),
            (("phiên bản chịu lửa: chỗ kín kim loại chữ U có đệm PTFE",
             "fire-tested U metal seat with PTFE insert"), (176, 322)),
            (("PTFE hỏng khi cháy → kim loại kín thay",
             "PTFE destroyed in fire, metal takes over"), (200, 116))],
           "Xomox Corporation.")
    return _m(cfg, seal="membrane", disc="offset", high_perf=True,
              tilt=11)


@_reg7
def fig_vsh_3_83():
    cfg = (83, "High-performance butterfly valve designed for interference "
           "seating, with plastic, elastomer, metal and plastic/metal "
           "composition seats",
           "Van bướm hiệu năng cao thiết kế chỗ kín ghen, với chỗ kín nhựa, "
           "ê-lô-me, kim loại và nhựa/kim loại",
           [(("đĩa lệch kép ép ghen", "double offset disc, interference"),
             (200, 116)),
            (("vòng dây đỡ cho độ cứng khi đóng", "back-up wire winding "
             "gives rigidity when closed"), (166, 300)),
            (("khi mở chỗ kín được uốn cong tự do",
             "seat flexes freely when open"), (234, 300)),
            (("bốn vật liệu chỗ kín", "four seat materials"), (176, 322))],
           "Keystone International, Inc.")
    return _m(cfg, liner="band", disc="offset", high_perf=True,
              tilt=11)


# ------------------------------------------------------- disc & torque maps
@_reg7
def fig_vsh_3_84():
    """Offset disc configuration — top/side schematic."""
    o = [_defs()]
    cx = 200
    o.append(_circle(cx, 170, 86, fill=BODY_F, sw=1.3))
    o.append(_circle(cx, 170, 68, fill="#ffffff", sw=1.1))
    # disc tilted, its axis offset below the valve centreline
    o.append(_poly([(cx - 62, 140), (cx + 62, 140), (cx + 62, 162),
                    (cx - 62, 162)], fill=DISC_F, sw=1.2, close=True))
    o.append(_circle(cx + 12, 170, 6, fill=RING_F, sw=1.1))
    o.append(_line(cx + 12, 170, cx + 12, 66, 1.4, INK))
    o.append(_line(cx, 170, cx + 12, 170, 1.0, INK, "3 2"))
    o.append(_txt(cx, 276, "trục đĩa lệch dưới/ sau tâm / disc axis offset "
                  "below and behind centre", 6.8, color=GREY))
    for i, (vi, en) in enumerate([
            ("đĩa đối xứng", "symmetrical disc"),
            ("đĩa lệch", "offset disc"),
            ("dòng vào phía trục / phía đĩa",
             "flow toward shaft / toward disc"),
            ("momen thủy động khác nhau", "hydrodynamic torque differs")]):
        yy = 82 + i * 52
        o.append(_circle(404, yy - 3, 7, sw=1.0, color=INK))
        o.append(_txt(404, yy - 1, str(i + 1), 7.6, weight="bold"))
        o.append(_txt(418, yy - 4, vi, 7.6, anchor="start"))
        o.append(_txt(418, yy + 6, en, 6.6, anchor="start", color=GREY))
    o.append(_circle(cx + 12, 170, 7.5, sw=1.2, color=INK))
    o.append(_txt(cx + 12, 170.5, "2", 8.0, weight="bold"))
    o.append(_txt(476, 320, "Sơ đồ biên tập / editorial",
                  6.6, color=GREY))
    return _fig(svg(560, 340, "".join(o), "Offset disc configuration"),
                "Hình 3-84 · Cấu hình đĩa lệch trong van bướm (sơ đồ biên tập, "
                "vẽ lại).",
                "Figure 3-84 · Offset disc configuration in butterfly valves "
                "(editorial schematic, redrawn).",
                "Cấu hình đĩa lệch.", "Offset disc configuration.")


def _bf_chart(num, ten, tvi, kind, source):
    """Line charts 3-85…3-87: opening torque / pressure drop vs opening."""
    w, h = 560, 380
    X0, Y0, PW, PH = 62.0, 42.0, 372.0, 282.0
    o = []
    for i in range(5):
        yy = Y0 + i * PH / 4.0
        o.append(_line(X0, yy, X0 + PW, yy, 0.5, color="#d8d5cc"))
    for i in range(5):
        xx = X0 + i * PW / 4.0
        o.append(_line(xx, Y0, xx, Y0 + PH, 0.5, color="#d8d5cc"))
    o.append(_rect(X0, Y0, PW, PH, "none", 1.2, stroke=INK))
    for i in range(5):
        o.append(_txt(X0 + i * PW / 4.0, Y0 + PH + 14,
                      ["0", "25", "50", "75", "100"][i], 7.0, color=INK))
    o.append(_txt(X0 + PW / 2, Y0 + PH + 30,
                  "Độ mở van / Valve opening (%)", 8.2, color=INK,
                  weight="bold"))
    o.append(_txt(X0, Y0 - 10,
                  "Momen mở / Opening torque" if kind != "dp" else
                  "Áp suất giảm / Pressure drop", 7.4, anchor="start",
                  color=INK, weight="bold"))

    def px(v):
        return X0 + v / 100.0 * PW

    def py(v):
        return Y0 + PH - v * PH

    if kind == "const":
        curves = [("a", [0, .22, .40, .55, .72, .84], INK),
                  ("b", [0, .18, .34, .50, .62, .70], BLUE),
                  ("c", [0, .12, .22, .32, .40, .40], "#b45309")]
        o.append(_txt(X0 + 8, Y0 + 12, "Δp không đổi / constant Δp", 7.0,
                      color=GREY))
    elif kind == "dp":
        curves = [("a", [1.0, .86, .62, .35, .14, .04], INK),
                  ("b", [1.0, .88, .66, .39, .16, .05], BLUE),
                  ("c", [1.0, .90, .70, .44, .20, .07], "#b45309")]
        o.append(_txt(X0 + 8, Y0 + 12, "Lắp bơm thực tế / actual pumping",
                      7.0, color=GREY))
    else:
        curves = [("a", [0, .40, .62, .50, .28, .06], INK),
                  ("b", [0, .30, .46, .36, .20, .04], BLUE),
                  ("c", [0, .20, .30, .24, .13, .03], "#b45309")]
        o.append(_txt(X0 + 8, Y0 + 12, "Lắp bơm thực tế / actual pumping",
                      7.0, color=GREY))
    for lab, vals, col in curves:
        pts = [(px(i * 20.0), py(vals[i])) for i in range(6)]
        o.append(_poly(pts, "none", 1.6, col))
        o.append(_txt(pts[-1][0] - 5, pts[-1][1], lab, 7.4, color=col,
                      anchor="end", weight="bold"))
    for i, (vi, en) in enumerate([
            ("đối xứng, hai chiều", "symmetrical, either way"),
            ("lệch, dòng về trục", "offset, toward shaft"),
            ("lệch, dòng về đĩa", "offset, toward disc")]):
        yy = Y0 + 12 + i * 20
        o.append(_line(416, yy - 3, 430, yy - 3, 1.6,
                       [INK, BLUE, "#b45309"][i]))
        o.append(_txt(433, yy - 1, "abc"[i], 7.0, weight="bold"))
        o.append(_txt(442, yy - 4, vi, 6.4, anchor="start"))
        o.append(_txt(442, yy + 4, en, 5.8, anchor="start", color=GREY))
    o.append(_txt(476, h - 14, source, 6.4, color=GREY))
    return _fig(svg(w, h, _defs() + "".join(o), ten),
                "Hình 3-%d · %s (vẽ lại). Nguồn: %s" % (num, tvi, source),
                "Figure 3-%d · %s — redrawn. (Source: %s)" % (num, ten,
                                                               source),
                tvi, ten)


@_reg7
def fig_vsh_3_85():
    return _bf_chart(85, "Opening torque characteristics of butterfly valves "
                     "at constant pressure drop",
                     "Đặc tính momen mở van bướm khi áp suất giảm không đổi",
                     "const", "Schiff &amp; Hafen; VAG-Armaturen GmbH")


@_reg7
def fig_vsh_3_86():
    return _bf_chart(86, "Pressure drop across butterfly valves at all "
                     "opening positions in an actual pumping installation",
                     "Áp suất giảm qua van bướm ở mọi vị trí mở trong lắp "
                     "đặt bơm thực tế", "dp",
                     "Schiff &amp; Hafen; VAG-Armaturen GmbH")


@_reg7
def fig_vsh_3_87():
    return _bf_chart(87, "Opening torque characteristics of butterfly valves "
                     "in an actual pumping installation",
                     "Đặc tính momen mở van bướm trong lắp đặt bơm thực tế",
                     "actual", "Schiff &amp; Hafen; VAG-Armaturen GmbH")


# ----------------------------------------------------------- pinch valves
def _pinch_ops(enclosed=False, prepinch=False, tear_drops=False,
               fluid=False, iris=False):
    """Return low-level op tuples for `_emit` (local frame, sleeve at y=104)."""
    o = []
    if enclosed:
        o.append(("poly", [(-92, 64), (92, 64), (92, 144), (-92, 144)],
                  RING_F, 1.3, INK, "", True))
        o.append(("line", -92, 104, 92, 104, 0.9, INK, "4 3"))
    else:
        for sx in (-1, 1):
            o.append(("line", sx * 92, 62, sx * 92, 146, 1.2, INK, ""))
    # flexible sleeve
    o.append(("poly", [(-84, 84), (84, 84), (84, 124), (-84, 124)],
              RUBBER_F, 1.2, INK, "", True))
    if iris:
        o.append(("circ", 0, 104, 16, 1.2, INK, None))
        o.append(("circ", 0, 104, 24, 1.0, GREY, None))
    elif fluid:
        for sx in (-1, 1):
            o.append(("circ", sx * 42, 104, 18, 1.1, INK, BULB_F))
        o.append(("poly", [(-18, 92), (18, 92), (18, 116), (-18, 116)],
                  "#ffffff", 1.1, INK, "", True))
    else:
        gap = 8 if prepinch else 22
        o.append(("poly", [(-18, 84), (18, 84), (18, 104 - gap),
                           (-18, 104 - gap)], RUBBER_F, 1.0, INK, "", True))
        o.append(("poly", [(-18, 124), (18, 124), (18, 104 + gap),
                           (-18, 104 + gap)], RUBBER_F, 1.0, INK, "", True))
        for sx in (-1, 1):
            o.append(("poly", [(sx * 20, 74), (sx * 34, 74),
                               (sx * 34, 134), (sx * 20, 134)],
                      RING_F, 1.1, INK, "", True))
        if tear_drops:
            for sx in (-1, 1):
                for yy in (92, 116):
                    o.append(("circ", sx * 40, yy, 4, 1.0, INK, PTFE_F))
    for sx in (-1, 1):
        o.append(("poly", [(sx * 92, 72), (sx * 100, 72), (sx * 100, 136),
                           (sx * 92, 136)], RING_F, 1.1, INK, "", True))
    return o


def _pinch_fig(num, ten, tvi, marks, ops, courtesy="", sub="",
               w=560, h=380, xleg=402, fluid=False, iris=False):
    o2 = []
    _emit(o2, ops, rot=0.0, cx=0, cy=0, dx=200, dy=180)
    o2.append(_line(82, 284, 104, 284, 1.6, color=BLUE))
    o2.append(_poly([(104, 284), (96, 280.5), (96, 287.5)],
                    fill=BLUE, sw=0, close=True))
    o2.append(_line(296, 284, 318, 284, 1.6, color=BLUE))
    o2.append(_poly([(296, 284), (304, 280.5), (304, 287.5)],
                    fill=BLUE, sw=0, close=True))
    if fluid and not iris:
        for sx in (-1, 1):
            o2.append(_txt(200 + sx * 42, 267, "P", 7.0, color=BLUE,
                           weight="bold"))
    if sub:
        o2.append(_txt(200, h - 18, sub, 6.9, color=GREY))
    _emit_legend(o2, xleg, marks)
    if courtesy:
        o2.append(_txt(476, h - 14, courtesy, 6.6, color=GREY))
    return _fig(svg(w, h, _defs() + "".join(o2), ten),
                "Hình 3-%d · %s (vẽ lại).%s"
                % (num, tvi, (" Nguồn: " + courtesy) if courtesy else ""),
                "Figure 3-%d · %s — redrawn.%s"
                % (num, ten, (" (Courtesy of " + courtesy.rstrip(".") + ".)")
                   if courtesy else ""),
                tvi, ten)


# The sleeve is translated to dx=200, dy=180, so its bore lies at y=284.
PM_MARK_POS = {
    88: [(166, 284), (200, 284), (234, 284), (200, 324)],
    89: [(166, 284), (200, 284), (200, 324), (234, 284)],
    90: [(166, 284), (234, 284), (200, 284), (200, 324)],
    91: [(166, 284), (200, 284), (234, 284), (200, 324)],
    92: [(200, 284), (166, 284), (234, 284), (200, 324)],
}


def _pm(cfg, sub="", **kw):
    num, ten, tvi, marks, courtesy = cfg
    if num in PM_MARK_POS:
        marks = [((vi, en), pos)
                 for ((vi, en), _), pos in zip(marks, PM_MARK_POS[num])]
    fluid = kw.pop("fluid", False)
    iris = kw.pop("iris", False)
    ops_kw = dict(kw)
    ops_kw["fluid"] = fluid
    ops_kw["iris"] = iris
    return _pinch_fig(num, ten, tvi, marks, _pinch_ops(**ops_kw),
                      courtesy=courtesy, sub=sub, fluid=fluid, iris=iris)


@_reg7
def fig_vsh_3_88():
    cfg = (88, "Pinch valve, open construction",
           "Van kẹp kiểu hở",
           [(("thân hở, nhìn thấy ống", "open casing, sleeve visible"),
             (166, 148)),
            (("ống cao su ép bằng cơ khí", "mechanically pinched rubber "
             "sleeve"), (200, 116)),
            (("bulge / soft spot báo cần thay", "bulges or soft spots signal "
             "replacement"), (234, 148)),
            (("đường dòng thẳng không khe hở", "straight crevice-free "
             "passage"), (176, 322))],
           "Flexible Valve Corporation.")
    return _pm(cfg)


@_reg7
def fig_vsh_3_89():
    cfg = (89, "Pinch valve, enclosed construction, sleeve 50% prepinched "
           "for sensitive flow control, drain plug removable for vacuum "
           "connection",
           "Van kẹp kiểu kín, ống ép sẵn 50% để khống chế nhạy, nút xả tháo "
           "được để nối chân không",
           [(("vỏ kín dọc đường dòng", "casing split along flow axis"),
             (166, 148)),
            (("ống ép sẵn 50%", "sleeve 50% prepinched"), (200, 116)),
            (("nút xả / nối chân không", "drain plug / vacuum connection"),
             (234, 148)),
            (("khống chế nhạy sau 50%", "sensitive control beyond 50%"),
             (176, 322))],
           "RKL Controls, Inc.")
    return _pm(cfg, enclosed=True, prepinch=True)


@_reg7
def fig_vsh_3_90():
    cfg = (90, "Pinch valve, enclosed construction, PTFE valve body fitted "
           "with tear drops",
           "Van kẹp kiểu kín, thân PTFE có gờ hình giọt lệch",
           [(("thân PTFE", "PTFE valve body"), (166, 148)),
            (("gờ hình giọt lệch giảm gập", "tear drops reduce flexing"),
             (234, 148)),
            (("cho phép thân hoàn toàn PTFE", "allows an all-PTFE sleeve"),
             (200, 116)),
            (("xử lý chất mài mòn và ăn mòn", "handles abrasive and "
             "corrosive fluids"), (176, 322))],
           "Resistoflex Corporation.")
    return _pm(cfg, enclosed=True, tear_drops=True)


@_reg7
def fig_vsh_3_91():
    cfg = (91, "Pinch valve, fluid-pressure operated",
           "Van kẹp thao tác bằng áp suất chất lỏng",
           [(("buồng áp quanh ống", "pressure chamber around the sleeve"),
             (166, 148)),
            (("áp chất lỏng ép ống", "fluid pressure pinches the sleeve"),
             (234, 148)),
            (("không dùng khống chế tay", "not for manual flow control"),
             (200, 116)),
            (("áp hạ lưu đổi làm van tự chỉnh",
             "downstream pressure shifts the position"), (176, 322))],
           "RKL Controls, Inc.")
    return _pm(cfg, fluid=True)


@_reg7
def fig_vsh_3_92():
    cfg = (92, "Pinch valve, fluid-pressure operated, with iris-like closing "
           "action — a 360° squeeze giving an always round, always centred hole",
           "Van kẹp thao tác bằng áp suất, đóng kiểu mống mắt — ép 360°, lỗ "
           "luôn tròn và luôn tâm",
           [(("cơ cấu đóng kiểu mống mắt", "iris-like closing action"),
             (200, 116)),
            (("ép tròn 360° quanh ống", "360° squeeze of the sleeve"),
             (166, 148)),
            (("lỗ luôn tròn, luôn tâm", "always round, always centred hole"),
             (234, 148)),
            (("đặc tính equal-percentage; không đóng kín hoàn toàn",
             "equal-percentage; cannot close fully"), (176, 322))],
           "The Clarkson Company.")
    return _pm(cfg, fluid=True, iris=True)
