# -*- coding: utf-8 -*-
"""Safety Instrumented Systems, Chapter 7 — Choosing a Technology."""
from vfig import (BLUE, GOLD, GREEN, GREY, INK, PAPER, RED, _arrow, _circle,
                  _line, _poly, _rect, _txt)
from pcfig import _finish

DARKRED = "#7f1d1d"
AMBER = "#f6e0b8"
PALE_GREEN = "#dcecdc"
PALE_RED = "#f3d6d2"
PALE_BLUE = "#e8eef6"
WIRE = "#8a8477"


def _vtxt(x, y, s, size=7.0, color=GREY):
    """A text label rotated 90 degrees anticlockwise about (x, y)."""
    return ('<text x="%s" y="%s" text-anchor="middle" transform="rotate(-90 %s %s)" '
            'style="font:%spx Inter,Helvetica,sans-serif;fill:%s;">%s</text>'
            % (x, y, x, y, size, color, s))


def _res(x, y, h, label="", vertical=True):
    """A resistor: a zigzag of height h starting at (x, y)."""
    o = []
    n, amp = 6, 5.0
    step = h / float(n)
    pts = [(x, y)]
    for i in range(n):
        sgn = 1 if i % 2 == 0 else -1
        pts.append((x + sgn * amp, y + step * (i + 0.5)))
    pts.append((x, y + h))
    o.append(_poly(pts, fill="none", sw=1.1, color=INK))
    if label:
        o.append(_txt(x + 14, y + h / 2.0 + 2.4, label, 5.8, anchor="start", color=GREY))
    return "".join(o)


def _npn(cx, cy, r=13, label=""):
    """A simplified NPN phototransistor: bar, collector, emitter, no base lead."""
    o = [_circle(cx, cy, r, fill="none", sw=1.0)]
    o.append(_line(cx - 5, cy - 8, cx - 5, cy + 8, sw=2.0))
    o.append(_line(cx - 5, cy - 4, cx, cy - 11, sw=1.0))
    o.append(_line(cx, cy - 11, cx, cy - r - 5, sw=1.0))
    o.append(_line(cx - 5, cy + 4, cx, cy + 11, sw=1.0))
    o.append(_line(cx, cy + 11, cx, cy + r + 5, sw=1.0))
    o.append(_arrow(cx - 2, cy + 8, cx, cy + 11, sw=0.9))
    if label:
        o.append(_txt(cx + r + 4, cy + 2.4, label, 5.8, anchor="start", color=GREY))
    return "".join(o)


# ---------------------------------------------------------------- 7.1
def fig_7_1():
    """The solid-state system: separate modules wired together by hand."""
    o = [_txt(330, 18, "Hệ bán dẫn rắn: các khối rời, đấu dây thủ công",
              8.2, weight="600")]
    heads = [(62, "Cảm biến"), (161, "Khối vào"), (293, "Khối logic"),
             (405, "Khối ra"), (535, "Đầu ra")]
    for x, t in heads:
        o.append(_txt(x, 40, t, 6.4, weight="600", color=GREY))

    ins = [(56, "áp suất"), (88, "mức"), (120, "nhiệt độ"), (152, "lưu lượng"),
           (184, "vị trí")]
    for k, (y, lab) in enumerate(ins, 1):
        o.append(_txt(62, y + 17, lab, 6.0, color=INK))
        o.append(_rect(122, y, 78, 26, "#f3f1ea", sw=0.9))
        o.append(_txt(161, y + 17, "Vào số %d" % k, 6.0, color=INK))
        o.append(_arrow(104, y + 13, 120, y + 13, sw=0.9, color=WIRE))

    # the collection bus and its fan-out into the logic modules
    o.append(_line(224, 69, 224, 197, sw=1.2, color=WIRE))
    for y, _lab in ins:
        o.append(_line(200, y + 13, 224, y + 13, sw=0.9, color=WIRE))
        o.append(_circle(224, y + 13, 2.2, fill=WIRE, sw=0.6, color=WIRE))

    logics = [(74, "VÀ"), (122, "HOẶC"), (170, "ĐỊNH THỜI")]
    for y, lab in logics:
        o.append(_arrow(224, y + 17, 248, y + 17, sw=0.9, color=WIRE))
        o.append(_rect(250, y, 86, 34, PALE_BLUE, sw=0.9))
        o.append(_txt(293, y + 21, lab, 6.4, color=INK))

    outs = [(74, "Ra số 1", "van XV-1"), (122, "Ra số 2", "bơm P-1"),
            (170, "Ra số 3", "còi báo")]
    for y, mod, dev in outs:
        o.append(_arrow(336, y + 17, 364, y + 17, sw=0.9, color=WIRE))
        o.append(_rect(366, y, 78, 34, "#f3f1ea", sw=0.9))
        o.append(_txt(405, y + 21, mod, 6.0, color=INK))
        o.append(_arrow(444, y + 17, 470, y + 17, sw=0.9, color=WIRE))
        o.append(_txt(474, y + 21, dev, 6.0, anchor="start", color=INK))

    o.append(_txt(330, 224, "Mỗi khối phải được đấu dây thủ công vào đúng cấu hình logic — "
                            "trong một hệ lớn, đó có thể là hàng dặm dây",
                  6.2, color=GREY))
    return _finish(o, 660, 236,
                   "Hình 7-1. Hệ bán dẫn rắn điển hình. Cảm biến vào các khối vào rời, các khối này "
                   "được đấu dây tới những khối logic rời, rồi tới các khối ra. Không có thẻ vào/ra "
                   "nhiều kênh như PLC — mọi thứ nối với nhau bằng dây, và mọi thay đổi logic đều "
                   "phải sửa dây và sửa bản vẽ.",
                   "Figure 7-1. A typical solid-state system. Sensors feed separate input modules, "
                   "which are wired to separate logic modules, then to output modules. There are no "
                   "multi-channel I/O cards as in a PLC — everything is joined by wire, and every "
                   "logic change means changing wire and changing drawings.",
                   "Năm khối vào xếp thành cột, ba khối logic ở giữa, ba khối ra bên phải, tất cả nối "
                   "với nhau bằng một thanh góp dây dọc.",
                   "Five input modules in a column, three logic modules in the middle, three output "
                   "modules on the right, all joined by a vertical wire bus.")


# ---------------------------------------------------------------- 7.2
def fig_7_2():
    """Hot back-up: one CPU online, one waiting, and a switch between them."""
    o = [_txt(230, 20, "PLC dự phòng nóng: một CPU chạy, một CPU chờ", 8.2, weight="600")]
    o.append(_rect(110, 50, 120, 40, PALE_GREEN, sw=1.1))
    o.append(_txt(170, 68, "CPU A", 7.4, weight="600"))
    o.append(_txt(170, 81, "trực tuyến", 5.8, color=GREY))
    o.append(_rect(270, 50, 120, 40, "#f3f1ea", sw=1.1))
    o.append(_txt(330, 68, "CPU B", 7.4, weight="600"))
    o.append(_txt(330, 81, "dự phòng", 5.8, color=GREY))

    o.append(_rect(180, 130, 140, 44, PALE_BLUE, sw=1.1))
    o.append(_txt(250, 150, "BỘ CHUYỂN", 6.8, weight="600"))
    o.append(_txt(250, 163, "chuyển khi phát hiện hỏng", 5.4, color=GREY))
    o.append(_line(170, 90, 215, 130, sw=1.1))
    o.append(_line(330, 90, 285, 130, sw=1.1))

    o.append(_rect(185, 210, 130, 34, "#f3f1ea", sw=1.1))
    o.append(_txt(250, 231, "I/O đơn", 6.6))
    o.append(_line(250, 174, 250, 210, sw=1.1))
    o.append(_rect(170, 272, 160, 30, "#f3f1ea", sw=1.1))
    o.append(_txt(250, 291, "Thiết bị trường", 6.6))
    o.append(_line(250, 244, 250, 272, sw=1.1))

    notes = [(60, "Hỏng trong CPU mà chẩn đoán không bắt được", "→ hệ không chuyển, không báo"),
             (130, "Chuyển sang dự phòng nhưng không bumpless", "→ dừng quy trình"),
             (200, "Dự phòng cũng đã hỏng sẵn", "→ dừng toàn hệ")]
    for y, a, b in notes:
        o.append(_circle(404, y - 2, 2.2, fill=DARKRED, sw=0.5, color=DARKRED))
        o.append(_txt(412, y, a, 5.8, anchor="start", color=INK))
        o.append(_txt(412, y + 11, b, 5.8, anchor="start", color=GREY))

    o.append(_txt(250, 250, "", 5))
    return _finish(o, 660, 312,
                   "Hình 7-2. Hệ PLC dự phòng nóng. Hai CPU nhưng chỉ một chạy tại một thời điểm, còn "
                   "các khối vào/ra thì đơn tuyến. Ba cách hệ này hỏng đều nằm ở chỗ then chốt: chẩn "
                   "đoán CPU không phủ hết mọi hỏng hóc, nên có những hỏng mà hệ không hề biết để "
                   "chuyển; việc chuyển có thể không bumpless; và bản dự phòng có thể đã hỏng từ trước.",
                   "Figure 7-2. A hot back-up PLC system. Two CPUs, but only one online at a time, and "
                   "simplex I/O. All three failure routes sit at the same joint: CPU diagnostics do not "
                   "cover every failure, so some failures never trigger a switch; the switch itself may "
                   "not be bumpless; and the standby may already be dead.",
                   "Hai CPU đặt cạnh nhau, một bộ chuyển bên dưới, rồi tới khối vào/ra đơn và thiết bị "
                   "trường; ba ghi chú lỗi ở bên phải.",
                   "Two CPUs side by side above a switch, then simplex I/O and field devices; three "
                   "failure notes down the right side.")


# ---------------------------------------------------------------- 7.3
def fig_7_3():
    """Active parallel redundancy: both channels run, neither can arbitrate."""
    o = [_txt(330, 20, "Hai kênh cùng chạy: không kênh nào có quyền phán xử", 8.2, weight="600")]
    for y, tag, fill in ((58, "A", PALE_GREEN), (152, "B", "#f3f1ea")):
        o.append(_rect(92, y, 78, 46, "#f3f1ea", sw=1.0))
        o.append(_txt(131, y + 21, "Vào " + tag, 6.6))
        o.append(_txt(131, y + 34, "và Ra " + tag, 5.6, color=GREY))
        o.append(_rect(198, y, 128, 46, fill, sw=1.1))
        o.append(_txt(262, y + 24, "CPU " + tag, 7.4, weight="600"))
        o.append(_txt(262, y + 37, "xử lý song song", 5.6, color=GREY))
        o.append(_rect(354, y, 78, 46, "#f3f1ea", sw=1.0))
        o.append(_txt(393, y + 21, "Ra " + tag, 6.6))
        o.append(_arrow(170, y + 23, 196, y + 23, sw=1.0))
        o.append(_arrow(326, y + 23, 352, y + 23, sw=1.0))

    o.append(_arrow(262, 112, 262, 146, sw=1.0, color=GOLD))
    o.append(_arrow(262, 146, 262, 112, sw=1.0, color=GOLD))
    o.append(_txt(274, 132, "so sánh chéo", 5.6, anchor="start", color=GOLD))

    o.append(_txt(470, 96, "Hai kênh bất đồng thì", 5.8, anchor="start", color=INK))
    o.append(_txt(470, 107, "không có cách nào biết", 5.8, anchor="start", color=INK))
    o.append(_txt(470, 118, "kênh nào đúng:", 5.8, anchor="start", color=INK))
    o.append(_txt(470, 133, "2oo2 → bỏ qua hỏng an toàn", 5.6, anchor="start", color=GREY))
    o.append(_txt(470, 144, "1oo2 → bỏ qua hỏng nguy hiểm", 5.6, anchor="start", color=GREY))
    o.append(_txt(470, 155, "phải chọn trước, không", 5.6, anchor="start", color=GREY))
    o.append(_txt(470, 166, "chọn được lúc đang chạy", 5.6, anchor="start", color=GREY))
    return _finish(o, 660, 224,
                   "Hình 7-3. Hệ dự phòng song song chủ động. Cả hai kênh đều xử lý, nên hệ không có "
                   "một bản “dự phòng” để so với bản đang chạy. Khi hai kênh bất đồng, muốn biết kênh "
                   "nào đúng thì phải chọn trước một quy tắc bỏ phiếu — và quy tắc đó quyết định hệ sẽ "
                   "hỏng theo hướng an toàn hay hướng nguy hiểm.",
                   "Figure 7-3. An active parallel redundant system. Both channels process, so there is "
                   "no standby copy to compare against the running one. When the channels disagree, the "
                   "only way to know which is right is a voting rule chosen in advance — and that rule "
                   "decides whether the system fails safe or fails dangerous.",
                   "Hai nhánh song song, mỗi nhánh gồm khối vào, CPU và khối ra; mũi tên hai chiều "
                   "giữa hai CPU; ghi chú về quy tắc bỏ phiếu ở bên phải.",
                   "Two parallel branches, each with an input block, a CPU and an output block; a "
                   "two-way arrow between the CPUs; a voting-rule note at the right.")


# ---------------------------------------------------------------- 7.4
def fig_7_4():
    """A PLC input circuit: what a single input channel actually is."""
    o = [_txt(330, 18, "Một kênh vào của PLC: mạch thật, và chỗ chẩn đoán nhìn vào",
              8.0, weight="600")]

    # supply rails
    o.append(_line(60, 58, 300, 58, sw=1.2, color=INK))
    o.append(_txt(62, 51, "+24 V", 6.2, anchor="start", color=INK))
    o.append(_line(60, 212, 300, 212, sw=1.2, color=INK))
    o.append(_txt(62, 224, "0 V", 6.2, anchor="start", color=INK))

    # field switch
    o.append(_line(120, 58, 120, 76, sw=1.1))
    o.append(_line(120, 76, 120, 84, sw=1.1))
    o.append(_line(120, 84, 132, 96, sw=1.3))
    o.append(_circle(120, 84, 2.0, fill=INK, sw=0.5, color=INK))
    o.append(_circle(120, 100, 2.0, fill=INK, sw=0.5, color=INK))
    o.append(_line(120, 100, 120, 120, sw=1.1))
    o.append(_txt(146, 92, "công tắc trường", 5.8, anchor="start", color=GREY))

    o.append(_res(120, 120, 34, "R1"))
    o.append(_line(120, 154, 120, 164, sw=1.1))

    # the opto LED
    o.append(_poly([(110, 164), (130, 164), (120, 180)], fill="none", sw=1.1, close=True))
    o.append(_line(110, 180, 130, 180, sw=1.3))
    o.append(_line(120, 180, 120, 212, sw=1.1))
    o.append(_txt(146, 176, "LED trong opto", 5.8, anchor="start", color=GREY))
    o.append(_arrow(136, 186, 374, 150, sw=0.9, color=GOLD, dash="4 3"))
    o.append(_txt(252, 200, "ánh sáng", 5.8, color=GOLD))

    # isolation barrier
    o.append(_line(330, 42, 330, 226, sw=1.0, dash="4 4", color=GREY))
    o.append(_txt(330, 36, "vách cách ly", 5.8, color=GREY))

    # secondary side
    o.append(_line(360, 58, 620, 58, sw=1.2, color=INK))
    o.append(_txt(362, 51, "+5 V", 6.2, anchor="start", color=INK))
    o.append(_line(360, 212, 620, 212, sw=1.2, color=INK))
    o.append(_txt(362, 224, "0 V", 6.2, anchor="start", color=INK))

    o.append(_line(400, 58, 400, 74, sw=1.1))
    o.append(_res(400, 74, 30, "R2"))
    o.append(_line(400, 104, 400, 123, sw=1.1))
    o.append(_npn(400, 141, 13, "Q1"))
    o.append(_line(400, 159, 400, 212, sw=1.1))

    # the collector node runs off to the processor
    o.append(_circle(400, 112, 2.4, fill=INK, sw=0.5, color=INK))
    o.append(_line(400, 112, 520, 112, sw=1.1))
    o.append(_arrow(520, 112, 560, 112, sw=1.1))
    o.append(_txt(564, 115, "tới bộ xử lý", 6.0, anchor="start", color=INK))

    o.append(_txt(330, 244, "Chẩn đoán chỉ thấy được những gì có đường dây báo về: ở đây là điểm thu "
                             "của Q1, chứ không phải công tắc hay R1 phía ngoài",
                  6.0, color=GREY))
    return _finish(o, 660, 254,
                   "Hình 7-4. Sơ đồ một mạch vào của PLC. Phía trường: điện áp 24 V đi qua công tắc, "
                   "qua R1 và qua LED của bộ ghép quang. Phía logic: quang transistor Q1 nhận ánh sáng "
                   "ấy và kéo điểm thu xuống, báo cho bộ xử lý biết tiếp điểm đã đóng. Vách cách ly "
                   "đảm bảo không có đường dẫn điện nào giữa hai phía — và cũng không có đường báo "
                   "ngược nào để phát hiện công tắc bị kẹt.",
                   "Figure 7-4. One PLC input circuit. Field side: 24 V passes through the switch, "
                   "through R1 and through the opto-coupler LED. Logic side: phototransistor Q1 sees "
                   "that light and pulls the collector node down, telling the processor the contact has "
                   "closed. The isolation barrier guarantees there is no conductive path between the two "
                   "sides — and therefore no return path to detect a stuck switch.",
                   "Sơ đồ mạch điện hai phía một vách cách ly: bên trái là công tắc, điện trở và LED; "
                   "bên phải là quang transistor và điểm thu nối tới bộ xử lý.",
                   "A two-sided circuit diagram split by an isolation barrier: switch, resistor and LED "
                   "on the left; phototransistor and collector node on the right.")


# ---------------------------------------------------------------- 7.5
def fig_7_5():
    """TMR: three channels and a voter."""
    o = [_txt(330, 20, "Hệ ba kênh (TMR): ba bộ xử lý, một bộ bỏ phiếu", 8.2, weight="600")]
    for y, tag, fill in ((52, "A", PALE_GREEN), (110, "B", PALE_GREEN),
                         (168, "C", PALE_GREEN)):
        o.append(_rect(76, y, 66, 34, "#f3f1ea", sw=0.9))
        o.append(_txt(109, y + 22, "Vào " + tag, 6.2))
        o.append(_rect(168, y, 92, 34, fill, sw=0.9))
        o.append(_txt(214, y + 22, "CPU " + tag, 6.6, weight="600"))
        o.append(_rect(286, y, 66, 34, "#f3f1ea", sw=0.9))
        o.append(_txt(319, y + 22, "Ra " + tag, 6.2))
        o.append(_arrow(142, y + 17, 166, y + 17, sw=0.9))
        o.append(_arrow(260, y + 17, 284, y + 17, sw=0.9))
        o.append(_line(352, y + 17, 392, y + 17, sw=1.0, color=WIRE))
        o.append(_arrow(392, y + 17, 412, 127, sw=1.0, color=WIRE))

    o.append(_rect(412, 96, 84, 62, PALE_BLUE, sw=1.2))
    o.append(_txt(454, 120, "BỎ PHIẾU", 6.6, weight="600"))
    o.append(_txt(454, 134, "2 trên 3", 6.6))
    o.append(_txt(454, 147, "không cần thoả thuận", 5.2, color=GREY))

    o.append(_arrow(496, 127, 528, 127, sw=1.2))
    o.append(_rect(528, 108, 108, 38, "#f3f1ea", sw=1.1))
    o.append(_txt(582, 132, "Phần tử chấp hành", 6.0))

    o.append(_txt(330, 226, "Một kênh hỏng — an toàn hay nguy hiểm — vẫn còn hai kênh bỏ phiếu; "
                            "hệ chịu được lỗi đơn",
                  6.2, color=GREY))
    return _finish(o, 660, 238,
                   "Hình 7-5. Hệ ba kênh dự phòng (TMR). Ba kênh độc lập cùng xử lý, mỗi kênh có khối "
                   "vào và khối ra riêng, và một bộ bỏ phiếu 2 trên 3 quyết định đầu ra chung. Hệ chịu "
                   "được một hỏng hóc bất kỳ, kể cả hỏng nguy hiểm, mà vẫn còn hai kênh đồng thuận. "
                   "Nhưng ba kênh chỉ bảo vệ phần logic — cảm biến và van vẫn có thể là điểm yếu duy nhất.",
                   "Figure 7-5. A triple modular redundant system. Three independent channels process in "
                   "parallel, each with its own input and output block, and a two-out-of-three voter "
                   "decides the common output. The system survives any single failure, including a "
                   "dangerous one, because two channels still agree. But the three channels protect only "
                   "the logic — the sensor and the valve can still be a single point of failure.",
                   "Ba nhánh ngang song song, mỗi nhánh có khối vào, CPU và khối ra, cùng hội tụ vào "
                   "một khối bỏ phiếu 2 trên 3 rồi tới phần tử chấp hành.",
                   "Three parallel horizontal branches, each with an input block, a CPU and an output "
                   "block, converging on a 2oo3 voter and then a final element.")


# ---------------------------------------------------------------- 7.6
def fig_7_6():
    """1oo2D: two channels, each with its own diagnostics, voted one-out-of-two."""
    o = [_txt(330, 20, "Hệ 1oo2D: hai kênh, mỗi kênh tự chẩn đoán, bỏ phiếu 1 trên 2",
              8.0, weight="600")]
    for k, y in ((1, 46), (2, 148)):
        o.append(_rect(56, y, 340, 80, "#fbfaf7", sw=0.9))
        o.append(_txt(64, y + 12, "Kênh %d" % k, 5.8, anchor="start", color=GREY))
        o.append(_rect(70, y + 18, 84, 30, "#f3f1ea", sw=0.9))
        o.append(_txt(112, y + 37, "Vào", 6.2))
        o.append(_rect(176, y + 18, 96, 30, PALE_GREEN, sw=0.9))
        o.append(_txt(224, y + 37, "CPU", 6.6, weight="600"))
        o.append(_rect(294, y + 18, 84, 30, "#f3f1ea", sw=0.9))
        o.append(_txt(336, y + 37, "Ra", 6.2))
        o.append(_arrow(154, y + 33, 174, y + 33, sw=0.9))
        o.append(_arrow(272, y + 33, 292, y + 33, sw=0.9))
        o.append(_rect(70, y + 54, 308, 18, PALE_BLUE, sw=0.8))
        o.append(_txt(224, y + 67, "khối chẩn đoán của kênh", 5.6, color=INK))
        o.append(_arrow(396, y + 33, 436, 112, sw=1.0, color=WIRE))

    o.append(_rect(436, 84, 68, 56, PALE_BLUE, sw=1.2))
    o.append(_txt(470, 106, "1 trên 2", 6.4, weight="600"))
    o.append(_txt(470, 120, "một kênh đủ", 5.2, color=GREY))
    o.append(_txt(470, 131, "để tác động", 5.2, color=GREY))

    o.append(_arrow(504, 112, 532, 112, sw=1.2))
    o.append(_rect(532, 92, 108, 40, "#f3f1ea", sw=1.1))
    o.append(_txt(586, 117, "Phần tử chấp hành", 6.0))

    o.append(_txt(330, 244, "Hai hỏng an toàn cùng lúc mới gây dừng nhầm; hai hỏng nguy hiểm cùng "
                            "lúc mới mất chức năng",
                  6.2, color=GREY))
    return _finish(o, 660, 256,
                   "Hình 7-6. Hệ 1oo2D. Hai kênh chạy song song, nhưng khác với hệ dự phòng nóng, mỗi "
                   "kênh có khối chẩn đoán riêng và một kênh đã đủ để tác động. Vì thế phải hai hỏng "
                   "an toàn cùng lúc mới gây dừng nhầm, và hai hỏng nguy hiểm cùng lúc mới làm mất "
                   "chức năng — tức là chịu lỗi ngang với hệ ba kênh, nhưng bằng hai kênh.",
                   "Figure 7-6. A 1oo2D system. Two channels run in parallel, but unlike a hot back-up, "
                   "each has its own diagnostics and one channel alone is enough to act. Two simultaneous "
                   "safe failures are needed for a nuisance trip, and two simultaneous dangerous "
                   "failures for loss of function — fault tolerance equal to a triple system, achieved "
                   "with two channels.",
                   "Hai kênh xếp trên dưới, mỗi kênh gồm khối vào, CPU, khối ra và một dải chẩn đoán, "
                   "cùng nối vào bộ bỏ phiếu 1 trên 2 rồi tới phần tử chấp hành.",
                   "Two channels stacked, each with an input block, CPU, output block and a diagnostic "
                   "strip, both feeding a 1oo2 voter and then the final element.")


# ---------------------------------------------------------------- 7.7
def fig_7_7():
    """Centralisation: the same number of I/O, a very different blast radius."""
    o = [_txt(330, 20, "Tập trung hoá: cùng số điểm I/O, nhưng bán kính thiệt hại khác hẳn",
              8.0, weight="600")]

    o.append(_txt(160, 46, "Nhiều hệ nhỏ, phân tán", 6.6, weight="600", color=INK))
    o.append(_txt(500, 46, "Một hệ lớn, tập trung", 6.6, weight="600", color=INK))

    cells = [(52, 58, "Đơn vị 1"), (176, 58, "Đơn vị 2"),
             (52, 140, "Đơn vị 3"), (176, 140, "Đơn vị 4")]
    for x, y, lab in cells:
        o.append(_rect(x, y, 110, 66, "#fbfaf7", sw=0.9))
        o.append(_txt(x + 55, y + 16, lab, 6.0, weight="600"))
        o.append(_rect(x + 10, y + 24, 44, 16, PALE_GREEN, sw=0.7))
        o.append(_txt(x + 32, y + 35, "CPU", 5.2))
        for i in range(4):
            o.append(_circle(x + 66 + (i % 2) * 18, y + 32 + (i // 2) * 18, 3.4,
                             fill="#e2ded2", sw=0.6, color=GREY))

    o.append(_line(66, 166, 102, 182, sw=1.4, color=DARKRED))
    o.append(_line(102, 166, 66, 182, sw=1.4, color=DARKRED))
    o.append(_txt(160, 226, "một CPU hỏng → mất một đơn vị", 5.8, color=GREY))

    o.append(_rect(380, 58, 240, 148, "#fbfaf7", sw=1.0))
    o.append(_txt(500, 76, "Một CPU · 300 điểm I/O", 6.2, weight="600"))
    o.append(_rect(392, 88, 96, 22, PALE_RED, sw=0.8))
    o.append(_txt(428, 103, "CPU duy nhất", 5.8))
    for r in range(5):
        for c in range(11):
            o.append(_circle(396 + c * 20, 126 + r * 15, 3.6, fill="#e2ded2",
                             sw=0.6, color=GREY))
    o.append(_line(464, 91, 484, 107, sw=1.4, color=DARKRED))
    o.append(_line(484, 91, 464, 107, sw=1.4, color=DARKRED))
    o.append(_txt(500, 226, "một CPU hỏng → mất cả 300 điểm", 5.8, color=GREY))

    o.append(_line(300, 50, 300, 214, sw=0.8, dash="3 4", color="#d8d3c6"))
    return _finish(o, 660, 240,
                   "Hình 7-7. Tập trung hoá và bán kính thiệt hại. Bốn hệ nhỏ rời nhau thì một hỏng chỉ "
                   "mất một phần tư. Gộp tất cả vào một hệ lớn cho tiết kiệm thiết bị và công vận hành, "
                   "nhưng khi CPU duy nhất ấy hỏng thì mất toàn bộ — và đó chính là lý do các hệ dựa "
                   "trên phần mềm buộc phải có một dạng dự phòng nào đó.",
                   "Figure 7-7. Centralisation and blast radius. Four separate small systems lose a "
                   "quarter when one fails. Consolidating everything into one large system saves hardware "
                   "and operating effort, but when that single CPU fails everything is lost — which is "
                   "exactly why software-based systems are forced into some form of redundancy.",
                   "Hai khung so sánh: bên trái bốn hệ nhỏ độc lập, bên phải một hệ lớn với một CPU và "
                   "nhiều điểm vào ra.",
                   "Two panels compared: four independent small systems on the left, one large system "
                   "with a single CPU and many I/O points on the right.")


FIGURES = [fig_7_1, fig_7_2, fig_7_3, fig_7_4, fig_7_5, fig_7_6, fig_7_7]
