# -*- coding: utf-8 -*-
"""Vector redraws of Figures 1-4 to 1-6 in A. McMillan, *Electrical
Installations in Hazardous Areas*, Chapter 1 "Introduction".

Fig. 1-4 shows typical certification logos, Fig. 1-5 an example equipment
certificate and Fig. 1-6 the two routes to certification (panels (a)
Directive 76/117/EEC and (b) Directive 94/9/EC drawn as one figure).
All are simplified bilingual VI/EN SVG vectors, no raster art. Architecture
mirrors `expbfig01.py`: each function returns the standard five-tuple
through `vfig._fig()` and is registered in `FIGS` by `_reg`.
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (BLUE, GREY, INK, PAPER, _arrow, _circle, _defs, _ellipse,
                  _fig, _line, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def T(x, y, s, size=8.2, **kw):
    return _txt(x, y, esc(s), size, **kw)


def _panel(o, x, y, w, h, vi, en):
    o.append(_rect(x, y, w, h, fill=PAPER, sw=1.0, stroke="#b9b0a0"))
    o.append(T(x + 8, y + 14, vi, 6.8, anchor="start", color=GREY))
    o.append(T(x + w - 8, y + 14, en, 6.6, anchor="end", color=GREY))


# Exact printed codes from the sample certificate, in their numbered order.
_ROWS = [
    ("1", "Số chứng nhận", "Certificate No.", "BAS No. Ex 96D9999"),
    ("2", "Thiết bị", "Apparatus", "CONTROL CONSOLE TYPE ABC.123"),
    ("3", "Nhà sản xuất", "Manufacturer", "A. MANUFACTURER LTD"),
    ("4", "Tiêu chuẩn 1", "Standard 1", "EN50014 (1977) + Amd 1 to 5"),
    ("5", "Tiêu chuẩn 2", "Standard 2", "EN50018 (1977) + Amd 1 to 3"),
    ("6", "Báo cáo thử nghiệm", "Test report",
     "report 96(C)9999 dated 27 February 1996"),
    ("7", "Ký hiệu bảo vệ", "Marking", "EEx d IIB T4"),
    ("8", "Số hồ sơ", "File number", "File No. EECS 9999/01/001"),
    ("9", "Số trang", "Sheet", "Sheet 1 of 2"),
]


def _flowbox(o, x, y, w, h, vi, en, code=""):
    o.append(_rect(x, y, w, h, fill="#eef3fb", sw=1.0))
    o.append(T(x + w / 2.0, y + 16, vi, 6.8, color=INK, weight="600"))
    o.append(T(x + w / 2.0, y + 29, en, 6.2, color=GREY))
    if code:
        o.append(T(x + w / 2.0, y + 40, code, 6.2, color=BLUE))


def _branchbox(o, x, y, w, h, l1, l2, l3):
    o.append(_rect(x, y, w, h, fill="#f4f7fb", sw=1.0))
    o.append(T(x + w / 2.0, y + 11, l1, 6.2, color=INK))
    o.append(T(x + w / 2.0, y + 21, l2, 6.0, color=GREY))
    o.append(T(x + w / 2.0, y + 31, l3, 5.9, color=BLUE))


@_reg
def fig_f104():
    """Figure 1-4 - Typical certification logos."""
    w, h = 680, 396
    o = [_defs()]
    o.append(T(340, 18, "Các dấu chứng nhận điển hình / Typical certification logos",
               9.8, color=INK, weight="600"))
    o.append(T(340, 33,
               "EECS/BASEEFA · sira/SCS · PTB — các ví dụ từ Chương 1 / examples from Chapter 1",
               6.8, color=GREY))

    # Panel A: EECS / BASEEFA shield with Ex.
    _panel(o, 24, 44, 308, 150, "EECS / BASEEFA", "EECS / BASEEFA")
    o.append(_poly([(60, 84), (132, 84), (132, 126), (96, 150), (60, 126)],
                   fill=PAPER, sw=1.8, color=INK, close=True))
    o.append(T(96, 126, "Ex", 26, color=INK, weight="600"))
    o.append(T(148, 104, "Thiết bị điện", 7.2, anchor="start", color=INK))
    o.append(T(148, 116, "Dịch vụ chứng nhận", 7.2, anchor="start", color=INK))
    o.append(T(148, 132, "Electrical Equipment", 7.2, anchor="start", color=GREY))
    o.append(T(148, 144, "Certification Service", 7.2, anchor="start", color=GREY))
    o.append(T(96, 168, "EECS / BASEEFA", 7.6, color=INK, weight="600"))

    # Panel B: sira Certification Service with UKAS-style check, number 011.
    _panel(o, 348, 44, 308, 150, "SCS / sira", "sira Certification Service")
    o.append(T(364, 108, "sira", 30, anchor="start", color=INK, weight="600"))
    o.append(T(366, 128, "Certification Service", 9.5, anchor="start", color=INK))
    o.append(T(366, 143, "Dịch vụ chứng nhận", 6.6, anchor="start", color=GREY))
    o.append(T(366, 168, "SCS", 8.0, anchor="start", color=INK, weight="600"))
    o.append(_rect(520, 64, 124, 110, fill=PAPER, sw=1.0))
    o.append(_poly([(572, 74), (576, 68), (580, 72), (584, 68), (588, 74)],
                   fill=INK, sw=0.6, close=True))
    o.append(_poly([(530, 92), (550, 120), (632, 80)],
                   fill="none", sw=7, color=INK))
    o.append(T(582, 132, "Công nhận quốc gia", 5.2, color=GREY))
    o.append(T(582, 140, "NATIONAL ACCREDITATION", 5.2, color=INK))
    o.append(T(582, 148, "OF CERTIFICATION BODIES", 5.2, color=INK))
    o.append(T(582, 164, "Reg. No. / Số ĐK 011", 6.0, color=GREY))

    # Panel C: PTB round Ex mark.
    _panel(o, 24, 204, 308, 150, "PTB", "PTB")
    o.append(_circle(96, 282, 44, fill=PAPER, sw=1.8))
    o.append(T(96, 292, "Ex", 28, color=INK, weight="600"))
    o.append(T(96, 340, "PTB", 8.0, color=INK, weight="600"))
    o.append(T(156, 272, "Physikalisch-Technische", 6.6, anchor="start", color=INK))
    o.append(T(156, 283, "Bundesanstalt", 6.6, anchor="start", color=INK))
    o.append(T(156, 304, "Viện Vật lý - Kỹ thuật", 6.4, anchor="start", color=GREY))
    o.append(T(156, 315, "Liên bang Đức", 6.4, anchor="start", color=GREY))
    o.append(T(156, 332, "Cơ quan chứng nhận của Đức", 6.4,
               anchor="start", color=GREY))

    # Panel D: bilingual explanatory note.
    _panel(o, 348, 204, 308, 150, "Các tổ chức chứng nhận", "Certification bodies")
    o.append(T(362, 240, "Chứng nhận kết cấu thiết bị,", 7.2,
               anchor="start", color=INK))
    o.append(T(362, 252, "không phải cách lắp đặt.", 7.2, anchor="start", color=INK))
    o.append(T(362, 268, "Certifies construction, not installation.", 6.6,
               anchor="start", color=GREY))
    o.append(T(362, 296, "EECS · sira/SCS · PTB · DEMKO · KEMA · TÜV", 6.4,
               anchor="start", color=INK))
    o.append(T(362, 314, "Các tổ chức được phê chuẩn / Approved bodies", 6.4,
               anchor="start", color=GREY))
    o.append(T(362, 332, "Chỉ dẫn không thay thế tiêu chuẩn / Guidance only", 6.2,
               anchor="start", color=GREY))

    o.append(T(340, 382,
               "Hình 1-4 · Các dấu chứng nhận điển hình / Figure 1-4 · Typical certification logos",
               6.5, color=GREY))
    return _fig(svg(w, h, "".join(o),
                    esc("Bốn dấu chứng nhận: EECS BASEEFA, sira viền UKAS số 011, SCS và PTB dạng tròn")),
                "Hình 1-4 · Các dấu chứng nhận điển hình: EECS/BASEEFA, sira Certification Service "
                "với dấu kiểm tra UKAS số đăng ký 011, SCS và dấu Ex tròn của PTB",
                "Figure 1-4 · Typical certification logos: EECS/BASEEFA, sira Certification "
                "Service with the UKAS-style check and registration number 011, SCS, and the "
                "round Ex mark of PTB",
                "Bốn ô chứa các dấu: khiên Ex EECS/BASEEFA, dòng chữ sira với ô kiểm tra UKAS số 011, "
                "chữ SCS và vòng tròn Ex của PTB, kèm nhãn song ngữ",
                "Four panels: the EECS/BASEEFA Ex shield, sira lettering with a UKAS check box "
                "numbered 011, SCS, and the round PTB Ex mark, all with bilingual labels")


@_reg
def fig_f105():
    """Figure 1-5 - Example of an equipment certificate, nine fields."""
    w, h = 680, 560
    o = [_defs()]
    o.append(_rect(24, 30, 632, 490, fill="#ffffff", sw=1.4))
    o.append(_rect(30, 36, 620, 478, fill="none", sw=0.6, stroke="#999999"))

    # Header: BASEEFA oval on the left, Ex hexagon on the right.
    o.append(_ellipse(110, 68, 40, 17, fill=INK, sw=1.0))
    o.append(T(110, 65, "Ex", 7.6, color=PAPER, weight="600"))
    o.append(T(110, 76, "BASEEFA", 7.2, color=PAPER, weight="600"))
    o.append(T(60, 98, "EECS · Dịch vụ chứng nhận thiết bị điện", 6.0,
               anchor="start", color=GREY))
    hx, hy, hr = 594, 68, 22
    dy = hr * 0.866
    o.append(_poly([(hx + hr, hy), (hx + hr / 2.0, hy + dy),
                    (hx - hr / 2.0, hy + dy), (hx - hr, hy),
                    (hx - hr / 2.0, hy - dy), (hx + hr / 2.0, hy - dy)],
                   fill="none", sw=3.0, color=INK, close=True))
    o.append(T(hx, hy + 4, "Ex", 12, color=INK, weight="600"))
    o.append(T(340, 64, "Certificate of Conformity", 12, color=INK, weight="600"))
    o.append(T(340, 80, "Chứng nhận phù hợp", 7.6, color=GREY))
    o.append(_line(40, 106, 640, 106, sw=0.8, color=INK))

    # Nine numbered fields with the exact printed codes.
    for i, (num, vi, en, code) in enumerate(_ROWS):
        y = 128 + i * 40
        o.append(_circle(50, y - 3, 8, fill="#eef2f7", sw=0.9))
        o.append(T(50, y + 1, num, 7.6, color=INK, weight="600"))
        o.append(T(66, y - 4, vi, 6.6, anchor="start", color=GREY))
        o.append(T(66, y + 6, en, 6.2, anchor="start", color=GREY))
        o.append(T(228, y + 2, code, 8.0, anchor="start", color=INK, weight="600"))
        o.append(_line(42, y + 14, 638, y + 14, sw=0.5, color="#dddddd"))

    # Footer marks and signature block.
    o.append(_line(42, 462, 638, 462, sw=0.8, color=INK))
    o.append(_ellipse(76, 486, 26, 10, fill=INK, sw=0.8))
    o.append(T(76, 490, "Ex", 7.0, color=PAPER, weight="600"))
    o.append(T(340, 478,
               "Dịch vụ chứng nhận thiết bị điện / Electrical Equipment Certification Service",
               6.4, color=INK))
    o.append(T(340, 492, "EECS · 27 February 1996 · I M Cleare, Director", 6.2,
               color=GREY))
    o.append(_circle(606, 486, 11, fill="none", sw=1.0))
    o.append(T(606, 490, "CE", 6.6, color=GREY, weight="600"))

    o.append(T(340, 546,
               "Hình 1-5 · Ví dụ chứng nhận thiết bị / Figure 1-5 · Example of equipment certificate",
               6.5, color=GREY))
    return _fig(svg(w, h, "".join(o),
                    esc("Mẫu chứng nhận phù hợp gồm chín trường, mang các mã BAS No. Ex 96D9999 và EEx d IIB T4")),
                "Hình 1-5 · Ví dụ chứng nhận thiết bị với chín trường: BAS No. Ex 96D9999, "
                "CONTROL CONSOLE TYPE ABC.123, A. MANUFACTURER LTD, EN50014 (1977) và EN50018 "
                "(1977), báo cáo 96(C)9999 ngày 27 tháng 2 năm 1996, ký hiệu EEx d IIB T4, "
                "File No. EECS 9999/01/001, Sheet 1 of 2",
                "Figure 1-5 · Example equipment certificate with nine fields: BAS No. Ex "
                "96D9999, CONTROL CONSOLE TYPE ABC.123, A. MANUFACTURER LTD, EN50014 (1977) "
                "and EN50018 (1977), report 96(C)9999 dated 27 February 1996, marking EEx d "
                "IIB T4, File No. EECS 9999/01/001 and Sheet 1 of 2",
                "Tài liệu chứng nhận có viền hoa văn, hai dấu Ex ở đầu, chín dòng đánh số kèm "
                "mã chứng nhận, tiêu chuẩn, báo cáo, ký hiệu bảo vệ và số hồ sơ, cùng dấu chân "
                "BASEEFA và CE",
                "A bordered certificate with two Ex marks in the header, nine numbered fields "
                "carrying certificate, standard, report, marking and file codes, plus BASEEFA "
                "and CE style marks in the footer")


@_reg
def fig_f106():
    """Figure 1-6 - Routes to certification, panels (a) and (b) in one figure."""
    w, h = 680, 464
    o = [_defs()]
    o.append(_line(348, 40, 348, 432, sw=0.8, color="#b9b0a0", dash="3 3"))

    # ---------------- Panel (a): Directive 76/117/EEC, six-step vertical flow.
    o.append(T(175, 16, "(a) Lộ trình chứng nhận / Route to certification", 8.8,
               color=INK, weight="600"))
    o.append(T(175, 30, "Chỉ thị 76/117/EEC · Directive 76/117/EEC", 7.0, color=GREY))
    steps = [
        ("Thiết kế, chế tạo mẫu thử theo EN",
         "Design and build prototype to EN Standard", ""),
        ("Gửi hồ sơ cho tổ chức thông báo",
         "Apply to approved (notified) body", ""),
        ("Tổ chức kiểm tra hồ sơ, thử nghiệm",
         "Body examines documentation and tests", ""),
        ("Tổ chức báo cáo các điểm chưa phù hợp",
         "Body advises non-compliances", ""),
        ("Nhà sản xuất sửa các điểm chưa phù hợp",
         "Manufacturer corrects non-compliances", ""),
        ("Tổ chức cấp chứng nhận phù hợp",
         "Body issues certificate of conformity", ""),
    ]
    for i, (vi, en, code) in enumerate(steps):
        y = 48 + i * 54
        _flowbox(o, 40, y, 270, 44, vi, en, code)
        if i < len(steps) - 1:
            o.append(_arrow(175, y + 44, 175, y + 54, sw=1.1, color=INK))
    o.append(_rect(40, 374, 270, 50, fill="#f7f3e8", sw=0.8, stroke="#b9b0a0"))
    o.append(T(52, 387, "Lưu ý: tại Anh, các tổ chức được phê chuẩn", 6.2,
               anchor="start", color=INK))
    o.append(T(52, 398, "yêu cầu hệ thống chất lượng đã chứng nhận", 6.2,
               anchor="start", color=INK))
    o.append(T(52, 409, "theo BS/EN/ISO 9002. / Note: UK approved bodies", 6.0,
               anchor="start", color=GREY))
    o.append(T(52, 420, "require a certified quality system to BS/EN/ISO 9002.", 6.0,
               anchor="start", color=GREY))

    # ---------------- Panel (b): Directive 94/9/EC, two category branches.
    o.append(T(503, 16, "(b) Lộ trình theo danh mục / Route by category", 8.8,
               color=INK, weight="600"))
    o.append(T(503, 30, "Chỉ thị 94/9/EC · Directive 94/9/EC", 7.0, color=GREY))

    o.append(T(503, 50, "Loại 1 (Vùng 0) / Category 1 (Zone 0)", 7.6,
               color=INK, weight="600"))
    cat1_left = [
        ("Đăng ký tổ chức thông báo", "Apply to notified body", "QA system: BS/EN/ISO 9002"),
        ("Tổ chức chứng nhận hệ thống", "Notified body certifies", "the quality system"),
        ("Tổ chức giám sát hệ thống", "Notified body monitors", "system and product"),
    ]
    cat1_right = [
        ("Tự chịu trách nhiệm về", "Own-responsibility", "quality system"),
        ("Tổ chức kiểm tra, thử", "Notified body examines", "and tests all equipment"),
    ]
    for i, (a, b, c) in enumerate(cat1_left):
        y = 58 + i * 46
        _branchbox(o, 358, y, 128, 38, a, b, c)
        if i < len(cat1_left) - 1:
            o.append(_arrow(422, y + 38, 422, y + 46, sw=1.0, color=INK))
    for i, (a, b, c) in enumerate(cat1_right):
        y = 58 + i * 46
        _branchbox(o, 520, y, 128, 38, a, b, c)
        if i < len(cat1_right) - 1:
            o.append(_arrow(584, y + 38, 584, y + 46, sw=1.0, color=INK))
    o.append(T(503, 108, "HOẶC", 6.2, color=INK))
    o.append(T(503, 117, "OR", 6.0, color=GREY))

    o.append(T(503, 212, "Loại 2 (Vùng 1) / Category 2 (Zone 1)", 7.6,
               color=INK, weight="600"))
    cat2_left = [
        ("Đăng ký tổ chức thông báo", "Apply to notified body", "QA system: BS/EN/ISO 9003"),
        ("Tổ chức chứng nhận hệ thống", "Notified body certifies", "the quality system"),
        ("Tổ chức giám sát hệ thống", "Notified body monitors", "system and product"),
    ]
    cat2_right = [
        ("Tự chịu trách nhiệm về", "Own-responsibility", "quality system"),
        ("Tổ chức kiểm tra thiết bị", "Notified body examines", "all equipment produced"),
    ]
    for i, (a, b, c) in enumerate(cat2_left):
        y = 220 + i * 46
        _branchbox(o, 358, y, 128, 38, a, b, c)
        if i < len(cat2_left) - 1:
            o.append(_arrow(422, y + 38, 422, y + 46, sw=1.0, color=INK))
    for i, (a, b, c) in enumerate(cat2_right):
        y = 220 + i * 46
        _branchbox(o, 520, y, 128, 38, a, b, c)
        if i < len(cat2_right) - 1:
            o.append(_arrow(584, y + 38, 584, y + 46, sw=1.0, color=INK))
    o.append(T(503, 268, "HOẶC", 6.2, color=INK))
    o.append(T(503, 277, "OR", 6.0, color=GREY))

    # Category 3 note.
    o.append(_rect(358, 360, 290, 64, fill="#f7f3e8", sw=0.8, stroke="#b9b0a0"))
    o.append(T(370, 374, "Loại 3 (Vùng 2): không cần chứng nhận tổ chức thông báo.", 6.2,
               anchor="start", color=INK))
    o.append(T(370, 386, "Category 3 (Zone 2): no notified-body certification.", 6.0,
               anchor="start", color=GREY))
    o.append(T(370, 398, "Nhà sản xuất tự khai báo phù hợp + dấu CE.", 6.2,
               anchor="start", color=INK))
    o.append(T(370, 410, "Manufacturer declaration of conformity + CE mark.", 6.0,
               anchor="start", color=GREY))

    o.append(T(340, 452,
               "Hình 1-6 · Lộ trình chứng nhận / Figure 1-6 · Routes to certification",
               6.5, color=GREY))
    return _fig(svg(w, h, "".join(o),
                    esc("Hai bảng: lộ trình sáu bước theo 76/117/EEC và lộ trình phân loại 1, 2, 3 theo 94/9/EC")),
                "Hình 1-6 · Lộ trình chứng nhận: (a) Chỉ thị 76/117/EEC gồm sáu bước từ mẫu thử "
                "đến chứng nhận và ghi chú BS/EN/ISO 9002; (b) Chỉ thị 94/9/EC với nhánh danh mục "
                "1 (Vùng 0) và 2 (Vùng 1), kèm ghi chú danh mục 3 (Vùng 2) tự khai báo và dấu CE",
                "Figure 1-6 · Routes to certification: (a) Directive 76/117/EEC in six steps "
                "from prototype to certificate with a BS/EN/ISO 9002 note; (b) Directive 94/9/EC "
                "with category 1 (Zone 0) and category 2 (Zone 1) branches and a category 3 "
                "(Zone 2) note on manufacturer declaration plus CE mark",
                "Hai bảng cạnh nhau: bảng (a) sáu ô xếp dọc nối bằng mũi tên và ô ghi chú 9002; "
                "bảng (b) hai nhánh song song cho danh mục 1 và 2 nối bằng chữ HOẶC/OR, cộng ô "
                "ghi chú danh mục 3",
                "Two side-by-side panels: (a) six stacked boxes joined by arrows with a 9002 "
                "note; (b) parallel branches for categories 1 and 2 joined by OR labels, plus a "
                "category 3 note panel")
