# -*- coding: utf-8 -*-
"""Vector redraws of Figures 14.1-14.5 in A. McMillan, *Electrical
Installations in Hazardous Areas*, Chapter 14 "Apparatus using protection
concept 'N' ('n')".

The five drawings are simplified vector redraws of the rendered pages
p461, p462, p466, p467 and p473. Printed English captions (including their
numbered Notes), in-figure labels and printed quirks are retained
verbatim: "In addition of the spring", the alternatives (1)/(2), the
duplicated "20" on the S scale of Fig. 14.5, "end its molecular weight",
"less then 40 °C" and the inconsistent "40 °C"/"40°C". Every displayed
string is literal Unicode with raw ampersands escaped. Each public
callable returns the standard five-tuple through ``vfig._fig()`` and is
registered in ``FIGS`` by the ``_reg`` decorator.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, PAPER, RED, _arrow, _circle,
                  _defs, _fig, _line, _path, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    """Every displayed string is literal Unicode with raw ampersands escaped."""
    return str(s).replace("&", "&amp;")


def T(x, y, s, size=7.6, **kw):
    """Plain text: clamp into the 6.8-9.5 px contract, vet, delegate to vfig."""
    size = min(9.5, max(6.8, float(size)))
    return _txt(x, y, esc(s), size, **kw)


# ------------------------------------------------------------------ helpers

def _title(o, n, vi, en, split=False, size=7.2):
    if split:
        o.append(T(340, 15, "Hình 14.%d · %s" % (n, vi), size,
                   color=INK, weight="600"))
        o.append(T(340, 28, "Figure 14.%d · %s" % (n, en), size,
                   color=INK, weight="600"))
    else:
        o.append(T(340, 15,
                   "Hình 14.%d · %s / Figure 14.%d · %s" % (n, vi, n, en),
                   size, color=INK, weight="600"))


def _sub(o, s, y=29, size=6.8):
    o.append(T(340, y, s, size, color=GREY))


def _lead(x1, y1, x2, y2, sw=0.8):
    return _arrow(x1, y1, x2, y2, sw=sw, color=INK, head="a7")


# ------------------------------------------------------------------ 14.1

@_reg
def fig_f1401():
    """Figure 14.1 - sectioned bayonet lampholder and its four leaders."""
    w, h = 680, 280
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 1, "Đầu đèn kiểu bayonet dùng trong đèn lắp bayonet",
           "Typical bayonet used in bayonet fitting luminaires")
    _sub(o, "Mặt cắt · lò xo, tiếp điểm ma sát ngẫu nhiên, đầu nối và chốt / "
            "Section · coil spring, fortuitous frictional contact, connection facility and bayonet")

    # Sectioned holder body, hollow outer tube and helical spring.
    o.append(_rect(210, 120, 100, 88, fill="url(#h6)", sw=1.1))
    o.append(_circle(262, 164, 21, fill="#ffffff", sw=1.0))
    o.append(_rect(194, 142, 16, 26, fill="#dedede", sw=1.0))
    o.append(_rect(310, 124, 205, 10, fill="url(#h6)", sw=1.0))
    o.append(_rect(310, 194, 205, 10, fill="url(#h6)", sw=1.0))
    o.append(_rect(310, 134, 205, 60, fill="#ffffff", sw=0))
    pts = [(342 + i * 9, 164 + (-9 if i % 2 == 0 else 9)) for i in range(14)]
    o.append(_poly(pts, fill="none", sw=1.3, color=INK))
    o.append(_rect(300, 204, 34, 12, fill="url(#h6)", sw=1.0))

    # Bayonet shaft, its pin and the fortuitous contact at the lower wall.
    o.append(_rect(440, 150, 145, 26, fill="#dedede", sw=1.1))
    o.append(_poly([(585, 150), (605, 163), (585, 176)],
                   fill="#cfcfcf", sw=1.1, close=True))
    o.append(_rect(466, 138, 10, 12, fill="#dedede", sw=1.0))
    o.append(_line(470, 194, 505, 194, sw=2.2, color=RED))
    o.append(_circle(488, 194, 2.4, fill=RED, sw=0))

    # Four printed leader labels, each with a genuine Vietnamese lead-in.
    o.append(T(360, 82, "Lò xo / Coil spring (must not be the only", 6.8, color=INK))
    o.append(T(360, 94, "current carrying element)", 6.8, color=INK))
    o.append(_lead(360, 98, 386, 152))
    o.append(T(550, 82, "Tiếp điểm ma sát ngẫu nhiên / Fortuitous", 6.8, color=INK))
    o.append(T(550, 94, "frictional contact (Note 1)", 6.8, color=INK))
    o.append(_lead(550, 98, 490, 190))
    o.append(T(55, 160, "Đầu nối / Connection facility", 6.8,
               anchor="start", color=INK))
    o.append(_lead(178, 157, 194, 155))
    o.append(T(670, 214, "Chốt bayonet / Bayonet", 6.8,
               anchor="end", color=INK))
    o.append(_lead(576, 211, 596, 176))
    o.append(T(340, 250,
               "Ghi chú in: (1) lò xo lá trong ống ngoài; (2) nối rộng giữa chốt và ống · "
               "Printed Notes (1)/(2) as set out in the caption", 6.8, color=GREY))

    return _fig(svg(w, h, "".join(o), esc("Fig 14.1")),
                "Hình 14.1 · Đầu đèn kiểu bayonet dùng trong đèn lắp bayonet. Ghi chú: Thông thường "
                "không thể tin cậy tiếp điểm này để truyền dòng tới đèn. Ngoài lò xo, cần có thêm "
                "các phần tử dẫn điện khác, ví dụ: (1) Một lò xo lá bên trong ống ngoài để ép chốt "
                "bayonet và bảo đảm tiếp điểm chịu áp lực, nếu điều đó đạt được mà vẫn cho phép chốt "
                "bayonet dịch động thỏa đáng; hoặc (2) Một kết nối rộng giữa chốt bayonet và ống "
                "ngoài, ở bên trong hoặc bên ngoài ống",
                "Figure 14.1 · Typical bayonet used in bayonet fitting luminaires. Notes: This "
                "contact cannot normally be relied upon for transmission of current to the lamp. "
                "In addition of the spring, additional conduction elements are required e.g.: "
                "(1) A leaf spring inside the outer tube to bias the bayonet and thus ensure "
                "pressure connection if this can be achieved while continuing to permit adequate "
                "bayonet movement; or (2) A broad connection between the bayonet and the outer "
                "tube either inside or outside the tube",
                "Mặt cắt đơn giản hóa của đầu đèn bayonet: thân giữ đèn tô gạch chéo bên trái có "
                "một đầu nối nhỏ và lỗ tròn ở giữa, ống ngoài nằm ngang với thành trên và dưới "
                "được tô gạch, cuộn lò xo nằm trong lòng ống, và chốt bayonet dạng trục có chốt "
                "nhỏ nhô ra ăn khớp với đầu ống. Đường đỏ ngắn ở thành dưới biểu thị tiếp điểm ma "
                "sát ngẫu nhiên. Bốn đường dẫn nhãn chỉ vào lò xo, tiếp điểm ma sát, đầu nối và "
                "chốt; dòng ghi chú cuối nhắc đến hai phương án dẫn điện bổ sung (1) và (2)",
                "Simplified section of a bayonet lampholder: a hatched cylindrical body at the "
                "left carries a small connection tab and a central circular recess, a horizontal "
                "outer tube has hatched upper and lower walls, a helical coil spring lies in the "
                "bore, and a shaft-like bayonet with a small pin fits into the tube end. A short "
                "red mark on the lower wall indicates the fortuitous frictional contact. Four "
                "leader lines identify the coil spring, that contact, the connection facility and "
                "the bayonet; a footer echoes the two printed alternative conduction arrangements "
                "(1) and (2)")


# ------------------------------------------------------------------ 14.2

@_reg
def fig_f1402():
    """Figure 14.2 - fluorescent tube pin support with six printed labels."""
    w, h = 680, 340
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 2, "Cách bố trí giá đỡ chân đèn",
           "Method of tube pin support provision")
    _sub(o, "Mặt đầu đèn · hai chân đèn, hai lò xo lá và chốt cách điện trung tâm / "
            "Tube end view · two pins, leaf springs and the central insulating boss")

    # Insulating mounting and the two electrical connection facilities.
    o.append(_rect(210, 100, 260, 12, fill="#e2e2e2", sw=1.0))
    o.append(_path("M210,106 Q200,100 194,106 M470,106 Q480,100 486,106",
                   fill="none", sw=1.0, color=INK))
    o.append(_rect(248, 78, 28, 22, fill="#cfcfcf", sw=1.0))
    o.append(_rect(404, 78, 28, 22, fill="#cfcfcf", sw=1.0))
    o.append(_poly([(250, 78), (256, 70), (268, 70), (274, 78)],
                   fill="#dedede", sw=1.0, close=True))
    o.append(_poly([(406, 78), (412, 70), (424, 70), (430, 78)],
                   fill="#dedede", sw=1.0, close=True))

    # Lamp end, two pins, two leaf springs and the insulating tube pin support.
    o.append(_circle(340, 205, 62, fill="#fbfbfb", sw=1.2))
    o.append(_rect(252, 150, 12, 20, fill="#cfcfcf", sw=1.0))
    o.append(_rect(416, 150, 12, 20, fill="#cfcfcf", sw=1.0))
    o.append(_path("M258,110 C240,140 240,196 258,224",
                   fill="none", sw=2.2, color=INK))
    o.append(_path("M422,110 C440,140 440,196 422,224",
                   fill="none", sw=2.2, color=INK))
    o.append(_rect(328, 264, 24, 10, fill="#cfcfcf", sw=1.0))

    # Top label feeds two arrows; left/right labels mirror each other.
    o.append(T(340, 56, "Tới đầu nối điện / To electrical connection", 6.8, color=INK))
    o.append(T(340, 68, "facilities providing electrical connection", 6.8, color=INK))
    o.append(_lead(300, 72, 262, 80))
    o.append(_lead(380, 72, 418, 80))
    o.append(T(560, 110, "Giá đỡ cách điện / Insulating", 6.8,
               anchor="start", color=INK))
    o.append(T(560, 122, "mounting", 6.8, anchor="start", color=INK))
    o.append(_lead(556, 114, 468, 106))
    for x, sx, ex in ((35, 152, 255), (530, 528, 425)):
        o.append(T(x, 165, "Lò xo lá dẫn điện / Leaf spring", 6.8,
                   anchor="start", color=INK))
        o.append(T(x, 177, "providing electrical", 6.8,
                   anchor="start", color=INK))
        o.append(T(x, 189, "connection", 6.8, anchor="start", color=INK))
        o.append(_lead(sx, 180, ex, 185))
    o.append(T(55, 228, "Chân đèn / Tube pin", 6.8, anchor="start", color=INK))
    o.append(_lead(125, 225, 255, 162))
    o.append(T(545, 228, "Chân đèn / Tube pin", 6.8, anchor="start", color=INK))
    o.append(_lead(543, 225, 425, 162))
    o.append(T(340, 305, "Đỡ chân đèn cách điện / Insulating tube pin support",
               6.8, color=INK))
    o.append(_lead(340, 296, 340, 275))
    o.append(T(340, 325,
               "Chốt cách điện trung tâm chống biến dạng chân đèn / "
               "Central insulating boss prevents the pins distorting inwards",
               6.8, color=GREY))

    return _fig(svg(w, h, "".join(o), esc("Fig 14.2")),
                "Hình 14.2 · Cách bố trí giá đỡ chân đèn",
                "Figure 14.2 · Method of tube pin support provision",
                "Hình mặt đầu của đèn huỳnh quang có hai chân đèn nằm hai bên, mỗi chân được giữ "
                "bởi một lò xo lá dẫn điện uốn cong hướng vào trong; một chốt đỡ cách điện nhỏ nằm "
                "ở đáy thân đèn để chống biến dạng chân đèn. Thanh đỡ lắp cách điện nằm ngang phía "
                "trên mang hai cụm tiếp điểm, và hai mũi tên từ nhãn ở đỉnh chỉ vào các đầu nối "
                "điện tương ứng. Các nhãn bên trái và bên phải được lặp lại đối xứng",
                "End-on view of a fluorescent tube whose two pins are held at either side by "
                "inwardly bowed leaf springs that also provide the electrical connection; a small "
                "insulating pin support sits at the bottom of the tube body to stop the pins "
                "distorting inwards. An insulating mounting spans the top and carries two contact "
                "blocks, with two arrows from the top label pointing to those connection "
                "facilities. The leaf-spring and tube-pin labels are repeated symmetrically on "
                "both sides")


# ------------------------------------------------------------------ 14.3

@_reg
def fig_f1403():
    """Figure 14.3 - two-view automatic lamp isolation with five labels."""
    w, h = 680, 350
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 3, "Tự động ngắt đèn khi tháo đèn bằng kỹ thuật ngắt kín/linh kiện không gây cháy",
           "Automatic isolation of lamp on removal using enclosed break/non-incendive "
           "component technique", split=True)
    _sub(o, "Hai hình chiếu · trái: ngắt kín, pít-tông lò xo, đèn; phải: tiếp điểm đầu và bên",
         y=41)
    _sub(o, "Two views · left: enclosed break, spring loaded plunger, lamp; right: end and side "
            "connections", y=52)

    def holder(cx):
        o.append(_rect(cx - 55, 100, 110, 75, fill="url(#h6)", sw=1.1))
        o.append(_rect(cx - 23, 112, 46, 40, fill="#fbfbfb", sw=1.0))
        o.append(_rect(cx - 12, 118, 24, 18, fill="#dedede", sw=1.0))
        o.append(_line(cx, 175, cx, 232, sw=1.6))
        for k in range(6):
            o.append(_line(cx - 15, 190 + k * 7, cx + 15, 190 + k * 7,
                           sw=1.0, color=INK))
        o.append(_rect(cx - 12, 224, 24, 12, fill="#cfcfcf", sw=1.0))
        o.append(_path("M%d,300 C%d,244 %d,234 %d,232 L%d,232 C%d,234 %d,244 %d,300 Z"
                       % (cx - 50, cx - 50, cx - 25, cx - 18, cx + 18,
                          cx + 25, cx + 50, cx + 50),
                       fill="#f3f3f3", sw=1.2))
        for k in range(4):
            o.append(_line(cx - 18, 244 + k * 8, cx + 18, 244 + k * 8,
                           sw=0.8, color=GREY))

    holder(205)
    holder(475)

    o.append(T(45, 85, "Ngắt kín / Enclosed", 6.8, anchor="start", color=INK))
    o.append(T(45, 97, "break", 6.8, anchor="start", color=INK))
    o.append(_lead(130, 92, 190, 124))
    o.append(T(30, 255, "Pít-tông lò xo / Spring", 6.8, anchor="start", color=INK))
    o.append(T(30, 267, "loaded plunger", 6.8, anchor="start", color=INK))
    o.append(_lead(126, 258, 196, 216))
    o.append(T(205, 330, "Đèn / Lamp", 6.8, color=INK))
    o.append(_lead(205, 320, 205, 292))
    o.append(T(430, 63, "Tiếp điểm điện đầu / End", 6.8, anchor="start", color=INK))
    o.append(T(430, 75, "electrical connection", 6.8, anchor="start", color=INK))
    o.append(_lead(472, 80, 472, 114))
    o.append(T(545, 265, "Tiếp điểm điện bên / Side", 6.8, anchor="start", color=INK))
    o.append(T(545, 277, "electrical connection", 6.8, anchor="start", color=INK))
    o.append(_lead(542, 268, 528, 168))

    return _fig(svg(w, h, "".join(o), esc("Fig 14.3")),
                "Hình 14.3 · Tự động ngắt đèn khi tháo đèn bằng kỹ thuật ngắt kín/linh kiện không "
                "gây cháy",
                "Figure 14.3 · Automatic isolation of lamp on removal using enclosed break/"
                "non-incendive component technique",
                "Hai hình chiếu cạnh của đầu đèn đặt cạnh nhau. Mỗi hình gồm thân đèn tô gạch chéo "
                "với hốc chứa tiếp điểm ngắt kín ở đỉnh, pít-tông lò xo dọc theo trục giữa và thân "
                "đèn hình chuông ở bên dưới. Hình bên trái có ba nhãn: ngắt kín, pít-tông lò xo và "
                "đèn; hình bên phải có hai nhãn cho tiếp điểm điện ở đầu và ở bên. Các đường dẫn "
                "nối mỗi nhãn tới đúng chi tiết tương ứng",
                "Two side views of a lampholder side by side. Each shows a hatched holder body "
                "with an enclosed break recess at the top, a spring loaded plunger along the "
                "centre line and a bell-shaped lamp below. The left view carries three labels - "
                "enclosed break, spring loaded plunger and lamp - while the right view has two "
                "labels for the end and side electrical connections. Leader lines tie every "
                "label to its own feature")


# ------------------------------------------------------------------ 14.4

@_reg
def fig_f1404():
    """Figure 14.4 - microswitch cross-section and its eleven labels."""
    w, h = 680, 340
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 4, "Microswitch dùng kỹ thuật ngắt kín/linh kiện không gây cháy",
           "Microswitch using enclosed break/non-incendive component technique.",
           split=True)
    _sub(o, "Mặt cắt · vỏ công tắc, tiếp điểm cố định và di động, cần thao tác và vỏ che / "
            "Cross-section · switch enclosure, fixed and moving contacts, operating rod and shroud",
         y=41)

    # Enclosure, guide, insulation and the enclosed break mechanism.
    o.append(_rect(228, 126, 224, 96, fill="url(#h6)", sw=1.2))
    o.append(_rect(234, 132, 212, 84, fill="#ffffff", sw=1.0))
    o.append(_line(340, 72, 340, 166, sw=2.0))
    o.append(_rect(330, 88, 20, 18, fill="#dedede", sw=1.0))
    o.append(_rect(332, 108, 16, 25, fill="#cfcfcf", sw=1.0))
    o.append(_circle(300, 180, 6, fill="#dedede", sw=1.0))
    o.append(_line(300, 180, 392, 164, sw=2.6))
    o.append(_line(444, 158, 392, 158, sw=1.5))
    o.append(_line(444, 200, 390, 200, sw=1.5))
    o.append(_circle(392, 158, 3.5, fill="#dedede", sw=1.0))
    o.append(_circle(390, 200, 3.5, fill="#dedede", sw=1.0))
    o.append(_rect(222, 184, 10, 14, fill="#cfcfcf", sw=1.0))
    o.append(_rect(452, 184, 10, 14, fill="#cfcfcf", sw=1.0))
    o.append(_rect(318, 70, 46, 48, fill="none", sw=1.0, dash="4 3", stroke=GREY))
    o.append(_rect(358, 100, 16, 8, fill="#dedede", sw=1.0))

    o.append(T(340, 58, "Cần thao tác / Operating rod", 6.8, color=INK))
    o.append(_lead(340, 62, 340, 76))
    o.append(T(205, 105, "Cách điện / Insulation", 6.8,
               anchor="start", color=INK))
    o.append(_lead(288, 105, 332, 112))
    o.append(T(30, 130, "Điểm quay tiếp điểm / Moving", 6.8,
               anchor="start", color=INK))
    o.append(T(30, 142, "contact pivot point", 6.8, anchor="start", color=INK))
    o.append(_lead(138, 138, 296, 178))
    o.append(T(45, 250, "Tiếp điểm di động / Moving", 6.8,
               anchor="start", color=INK))
    o.append(T(45, 262, "contact", 6.8, anchor="start", color=INK))
    o.append(_lead(142, 248, 330, 180))
    o.append(T(150, 290, "Khít chặt / Tight fit", 6.8,
               anchor="start", color=INK))
    o.append(_lead(175, 286, 232, 208))
    o.append(T(340, 250, "Vỏ công tắc / Switch enclosure", 6.8, color=INK))
    o.append(_lead(340, 240, 340, 220))
    o.append(T(470, 290, "Khít chặt / Tight fit", 6.8,
               anchor="start", color=INK))
    o.append(_lead(470, 286, 450, 208))
    o.append(T(470, 78, "Vỏ che bảo vệ / Protection shroud", 6.8,
               anchor="start", color=INK))
    o.append(T(470, 90, "(Note 1)", 6.8, anchor="start", color=INK))
    o.append(_lead(468, 84, 362, 78))
    o.append(T(470, 118, "Khe hở / Clearance fit", 6.8,
               anchor="start", color=INK))
    o.append(_lead(468, 116, 368, 100))
    o.append(T(560, 155, "Kẹp vỏ che / Shroud", 6.8, anchor="start", color=INK))
    o.append(T(560, 167, "Clamp", 6.8, anchor="start", color=INK))
    o.append(_lead(558, 160, 372, 104))
    o.append(T(560, 200, "Tiếp điểm cố định / Fixed", 6.8,
               anchor="start", color=INK))
    o.append(T(560, 212, "contacts", 6.8, anchor="start", color=INK))
    o.append(_lead(558, 204, 435, 158))
    o.append(T(340, 315,
               "Ghi chú in: tháo vỏ che để thử / Printed Note: The shroud is removed for testing",
               6.8, color=GREY))

    return _fig(svg(w, h, "".join(o), esc("Fig 14.4")),
                "Hình 14.4 · Microswitch dùng kỹ thuật ngắt kín/linh kiện không gây cháy. "
                "Ghi chú: Tháo vỏ che để thử nghiệm",
                "Figure 14.4 · Microswitch using enclosed break/non-incendive component "
                "technique. Note: The shroud is removed for testing",
                "Mặt cắt đơn giản hóa của microswitch có vỏ kín tô gạch chéo, cần thao tác thẳng "
                "đứng xuyên qua đoạn cách điện, tiếp điểm di động quay quanh một điểm tựa và chạm "
                "vào hai tiếp điểm cố định đưa vào từ phía phải. Vỏ che bảo vệ được vẽ bằng đường "
                "đứt nét và có kẹp giữ, với khe hở giữa cần và vỏ; hai vị trí lắp khít ở thành trái "
                "và thành phải được đánh dấu. Mười một nhãn gốc được đặt quanh bản vẽ, kèm dòng "
                "ghi chú in rằng vỏ che được tháo ra khi thử",
                "Simplified cross-section of a microswitch: a hatched sealed enclosure contains a "
                "vertical operating rod passing through insulation, a moving contact pivoting on "
                "a point and meeting two fixed contacts entering from the right. A dashed "
                "protection shroud with a clamp surrounds the upper rod, a clearance fit is shown "
                "beside it, and tight fits are marked at both enclosure walls. All eleven printed "
                "labels surround the drawing, followed by the printed note that the shroud is "
                "removed for testing")


# ------------------------------------------------------------------ 14.5

@_reg
def fig_f1405():
    """Figure 14.5 - nomograph with dashed constructions through Z."""
    w, h = 680, 470
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 5, "Xác định hệ số thở hạn chế (S)",
           "Determination of restricted breathing factor (S)", split=True)
    _sub(o, "Ba thang đứng · S và °C bên trái, M/LEL % bên phải; đường nét đứt đi qua Z / "
            "Three vertical scales · S and °C at left, M/LEL % at right; dashed constructions "
            "via Z", y=41)

    # Scale headings and downward arrows.
    for x, lab in ((120, "S"), (205, "°C"), (480, "M"), (555, "LEL %")):
        o.append(T(x, 56, lab, 7.4, color=INK, weight="600"))
        o.append(_arrow(x, 60, x, 70, sw=1.0, color=INK, head="a7"))

    # Left scale: S values on the left, boiling-point degrees on the right.
    o.append(_line(150, 70, 150, 420, sw=1.1))
    srows = [(88, "40", "40°C (Note 2)"), (108, "30", "50°"),
             (128, "20", "60°"), (148, "20", "70°"), (168, "10", "80°"),
             (188, "9", "90°"), (208, "8", "100°"), (228, "7", "110°"),
             (248, "6", "120°"), (268, "5", "130°"), (296, "4", ""),
             (320, "3", ""), (344, "2", ""), (368, "1", "")]
    for y, sv, deg in srows:
        o.append(_line(145, y, 150, y, sw=0.9, color=INK))
        o.append(T(140, y + 2.4, sv, 6.8, anchor="end", color=INK))
        if deg:
            o.append(T(160, y + 2.4, deg, 6.8, anchor="start", color=INK))

    # Centre Z line, as in the printed figure.
    o.append(_line(340, 90, 340, 390, sw=1.0))
    o.append(T(340, 206, "Z", 8.4, color=INK, weight="600"))
    o.append(T(340, 220, "(Note 1)", 6.8, color=INK))

    # Right scale: M and LEL % columns with the printed value blocks.
    o.append(_line(520, 70, 520, 420, sw=1.1))
    upper = ["20", "10", "9", "8", "7", "6", "5", "4", "3"]
    for i, val in enumerate(upper):
        y = 88 + i * 14
        o.append(_line(515, y, 520, y, sw=0.9, color=INK))
        o.append(_line(520, y, 525, y, sw=0.9, color=INK))
        o.append(T(508, y + 2.4, val, 6.8, anchor="end", color=INK))
        o.append(T(532, y + 2.4, val, 6.8, anchor="start", color=INK))
    mlow = ["30", "40", "50", "60", "70", "80", "90", "100", "200", "300", "400"]
    llow = ["20", "18", "16", "14", "12", "10", "8", "6", "4", "2", "1"]
    for i in range(11):
        y = 224 + i * 12
        o.append(_line(515, y, 520, y, sw=0.9, color=INK))
        o.append(_line(520, y, 525, y, sw=0.9, color=INK))
        o.append(T(508, y + 2.4, mlow[i], 6.8, anchor="end", color=INK))
        o.append(T(532, y + 2.4, llow[i], 6.8, anchor="start", color=INK))
    o.append(T(508, 382, "0.5", 6.8, anchor="end", color=INK))
    o.append(T(575, 155, "(1)", 6.8, color=INK))

    # Dashed constructions: boiling point to molecular weight, then LEL via Z.
    o.append(_arrow(152, 150, 520, 222, sw=1.0, dash="5 4", color=GREY, head="a7"))
    o.append(_arrow(520, 300, 152, 72, sw=1.0, dash="5 4", color=GREY, head="a7"))
    o.append(_arrow(152, 250, 520, 326, sw=1.0, dash="5 4", color=GREY, head="a7"))
    o.append(T(408, 180, "Etan / ethane", 6.8, color=BLUE))
    o.append(T(408, 296, "Etilklorür / ethylchloride", 6.8, color=BLUE))
    o.append(T(340, 455,
               "Nét đứt: nối điểm sôi với khối lượng phân tử, rồi nối LEL qua Z để đọc S · "
               "Dashed construction: boiling point to molecular weight, then LEL via Z to read S",
               6.8, color=GREY))

    return _fig(svg(w, h, "".join(o), esc("Fig 14.5")),
                "Hình 14.5 · Xác định hệ số thở hạn chế (S). Ghi chú: (1) Kẻ một đường thẳng nối "
                "điểm sôi của vật liệu và khối lượng phân tử của nó. Đường này cắt đường tâm tại Z. "
                "Kẻ một đường từ LEL đi qua Z để xác định S – hệ số thở. (2) Khi nhiệt độ sôi nhỏ "
                "hơn 40 °C, người ta lấy 40°C để dùng hình này",
                "Figure 14.5 · Determination of restricted breathing factor (S). Notes: (1) Draw "
                "a line between the material boiling point end its molecular weight. This "
                "crosses the centre line at Z. Draw a line from the LEL via Z to determine S – "
                "the breathing factor. (2) Where boiling temperatures of less then 40 °C occur, "
                "40°C will be assumed for use of figure",
                "Nomograph gồm ba thang đứng: thang trái có các giá trị S từ 40 đến 1 (trong đó "
                "giá trị 20 được in hai lần) và các nhãn nhiệt độ từ 40°C (Note 2) đến 130°; đường "
                "tâm giữa mang nhãn Z và (Note 1); thang phải gồm cột M và cột LEL % với các dãy "
                "giá trị in, kể cả 200, 300, 400 và 0,5 ở chân thang. Ba đường nét đứt có mũi tên "
                "nối điểm sôi tới khối lượng phân tử rồi nối LEL qua Z; các đường này mang nhãn "
                "ethane và ethylchloride",
                "Nomograph with three vertical scales: the left scale carries S values from 40 "
                "down to 1, including the twice-printed 20, alongside temperature marks from "
                "40°C (Note 2) to 130°; the centre line carries the labels Z and (Note 1); the "
                "right scale has an M column and an LEL % column with the printed value blocks, "
                "including 200, 300, 400 and 0.5 at the foot. Three dashed arrowed construction "
                "lines join boiling point to molecular weight and then carry the LEL through Z, "
                "and are labelled ethane and ethylchloride")
