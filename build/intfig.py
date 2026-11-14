# -*- coding: utf-8 -*-
"""Vector figures for Book 3 — CSIA *Guide for Selecting & Working with a
Control Systems Integrator*, Volume 1 (2000), 69 pp.

The source has no numbered figures.  Its graphic content is: two CSIA Best
Practices slides (mission, objectives), the criteria/scoring tables of §2,
the blank Kepner-Tregoe worksheet of Appendix B, and ten "Typical Project Mix
of Services" donut charts in Appendix A.  All of those are redrawn here as
true vectors.  A small number of additional schematics (the eight decision
steps, the registration audit, the criteria-domain map) are clearly captioned
as *schematic redraws of the guide's text*, never as source figures.

Every function returns the standard 5-tuple
``(svg, caption_vi, caption_en, aria_vi, aria_en)``.
"""
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GOLD, GREY, GREEN, INK, PAPER, RED,  # noqa: E402
                  _arrow, _box, _circle, _defs, _f as fmt, _fig, _line,
                  _path, _poly, _rect, _txt, svg)

LIGHT = "#eef3fb"
WARM = "#fff4dc"
MINT = "#eaf5ee"
ROSE = "#fbecea"

PALETTE = ["#1f5f8b", "#2e7d9f", "#4aa3b7", "#79c0b0", "#a9d6a0",
           "#d9cf7a", "#e3a857", "#d07a43", "#b45309", "#8a6d9b"]


# ------------------------------------------------------------------ helpers
def esc(s):
    """XML-escape SVG text, preserving entities already present in the data.

    The Appendix A chart labels carry ``&lt;5%`` verbatim from the source; a
    naive ``&``-escape would turn them into ``&amp;lt;5%`` and print the
    literal text "&lt;5%" on the page.
    """
    s = str(s)
    s = re.sub(r"&(?!amp;|lt;|gt;|quot;|apos;|#\d+;)", "&amp;", s)
    return s.replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def _svg(w, h, objs, title=""):
    return svg(w, h, _defs() + "".join(objs), esc(title))


def mk(w, h, objs, cap_vi, cap_en, aria_vi="", aria_en="", title=""):
    return _fig(_svg(w, h, objs, title or cap_vi),
                cap_vi, cap_en, aria_vi or cap_vi, aria_en or cap_en)


def tx(x, y, s, size=8.4, anchor="middle", color=INK, weight=""):
    return _txt(x, y, esc(s), size=size, anchor=anchor, color=color,
                weight=weight)


def rect(x, y, w, h, fill="#ffffff", sw=1.0, color=INK, dash=""):
    return _rect(x, y, w, h, fill=fill, sw=sw, stroke=color, dash=dash)


def line(x1, y1, x2, y2, sw=0.9, color=INK, dash=""):
    return _line(x1, y1, x2, y2, sw=sw, color=color, dash=dash)


def arw(x1, y1, x2, y2, sw=1.2, color=INK):
    return _arrow(x1, y1, x2, y2, sw=sw, color=color)


def wrap(s, width=34):
    """Naive word wrap for vector text drawn with ``tx``."""
    out, cur = [], ""
    for word in s.split():
        if cur and len(cur) + len(word) + 1 > width:
            out.append(cur)
            cur = word
        else:
            cur = (cur + " " + word).strip()
    if cur:
        out.append(cur)
    return out


def panel(x, y, w, h, title, fill="#ffffff", band=BLUE, size=9.4):
    """A rounded-looking card with a coloured header band."""
    o = [rect(x, y, w, h, fill=fill, sw=1.0),
         rect(x, y, w, 24, fill=band, sw=1.0),
         tx(x + 9, y + 16, title, size=size, anchor="start",
            color="#ffffff", weight="bold")]
    return o


def vtab(x, y, widths, headers, rows, rowh=19, headh=27, size=8.0,
         fills=None, align=None):
    """A vector table. ``rows`` may contain strings (group rows)."""
    o = []
    total = sum(widths)
    cx = x
    for j, (wd, hd) in enumerate(zip(widths, headers)):
        o.append(rect(cx, y, wd, headh, fill=BLUE, sw=0.7))
        for k, ln in enumerate(wrap(hd, max(9, int(wd / 5.0)))[:3]):
            o.append(tx(cx + wd / 2.0, y + 10 + k * 8.2, ln, size=7.2,
                        color="#ffffff", weight="bold"))
        cx += wd
    yy = y + headh
    for i, row in enumerate(rows):
        if isinstance(row, str):
            o.append(rect(x, yy, total, rowh, fill="#dce8f3", sw=0.7))
            o.append(tx(x + 7, yy + rowh * 0.68, row, size=size,
                        anchor="start", weight="bold"))
            yy += rowh
            continue
        bg = (fills[i] if fills and i < len(fills) and fills[i]
              else ("#ffffff" if i % 2 == 0 else "#f6f9fc"))
        cx = x
        for j, (wd, cell) in enumerate(zip(widths, row)):
            o.append(rect(cx, yy, wd, rowh, fill=bg, sw=0.6))
            anc = (align[j] if align else "middle")
            px = cx + (6 if anc == "start" else wd / 2.0)
            for k, ln in enumerate(wrap(str(cell), max(9, int(wd / 5.2)))[:2]):
                o.append(tx(px, yy + rowh / 2.0 + 3 + (k - 0.5) * 8.6
                            if len(wrap(str(cell), max(9, int(wd / 5.2)))) > 1
                            else yy + rowh / 2.0 + 3,
                            ln, size=size, anchor=anc))
            cx += wd
        yy += rowh
    return o


def donut(cx, cy, r, items, center, legend_x, legend_y, swatch=9,
          lsize=7.7):
    """Donut chart. ``items`` = [(label, display_pct, numeric_pct), ...]."""
    o = []
    vals = [it[2] for it in items]
    tot = float(sum(vals)) or 1.0
    a = -math.pi / 2.0
    for i, (lab, disp, val) in enumerate(items):
        span = 2.0 * math.pi * val / tot
        b = a + span
        x0, y0 = cx + r * math.cos(a), cy + r * math.sin(a)
        x1, y1 = cx + r * math.cos(b), cy + r * math.sin(b)
        large = 1 if span > math.pi else 0
        d = ("M%s,%s L%s,%s A%s,%s 0 %d 1 %s,%s Z"
             % (fmt(cx), fmt(cy), fmt(x0), fmt(y0), fmt(r), fmt(r),
                large, fmt(x1), fmt(y1)))
        o.append(_path(d, fill=PALETTE[i % len(PALETTE)], sw=0.9,
                       color="#ffffff"))
        a = b
    o.append(_circle(cx, cy, r * 0.49, fill="#ffffff", sw=1.0, color=INK))
    for k, ln in enumerate(center[:4]):
        o.append(tx(cx, cy - 9 + k * 9.2, ln, size=7.0, weight="bold"))
    for i, (lab, disp, val) in enumerate(items):
        ly = legend_y + i * 15.5
        o.append(rect(legend_x, ly - 7.5, swatch, swatch,
                      fill=PALETTE[i % len(PALETTE)], sw=0.5))
        o.append(tx(legend_x + 14, ly, lab, size=lsize, anchor="start"))
        o.append(tx(legend_x + 232, ly, disp, size=lsize, anchor="end",
                    weight="bold"))
    return o


# =========================================================== Chapter 1
def fig_mission():
    o = panel(10, 10, 660, 154, "CSIA Best Practices & Benchmarks · Mission",
              fill=PAPER)
    txt = ("Provide Control System Integrators a Means to Both Evaluate and "
           "Continuously Improve Their Practices by Providing Sound CSI "
           "Industry “Benchmarks”, to Be Used in a Self-Deterministic "
           "Fashion for the Markets They Serve.")
    for k, ln in enumerate(wrap(txt, 82)):
        o.append(tx(30, 62 + k * 15, ln, size=10.2, anchor="start"))
    o.append(line(30, 132, 650, 132, sw=0.7, color=GREY))
    o.append(tx(30, 150, "CSIA Guide, Volume 1, front matter (page v)",
                size=7.4, anchor="start", color=GREY))
    return mk(680, 174, o,
              "Hình 1.1 · Sứ mệnh của chương trình Thực hành tốt & Chuẩn đối sánh CSIA, "
              "được vẽ lại từ trang bìa trong của tập sách.",
              "Figure 1.1 · Mission of the CSIA Best Practices & Benchmarks program, "
              "redrawn from the guide's front matter.",
              "Thẻ văn bản trình bày sứ mệnh chuẩn đối sánh CSIA.",
              "Text card stating the CSIA benchmarking mission.")


def fig_objectives():
    o = panel(10, 10, 660, 196, "CSIA Best Practices & Benchmarks · Objectives",
              fill=PAPER)
    items = [
        "1)  Establish CSI Industry Benchmarks",
        "2)  Develop Procedure for Self Evaluation",
        "3)  Develop “Mechanism” To Facilitate Outside Assistance",
        "4)  Establish “Mechanism” for CSIA to Quantify Progress / Results",
        "5)  Obtain Endorsement From Industry Associations",
    ]
    for i, s in enumerate(items):
        yy = 48 + i * 28
        o.append(_circle(36, yy - 4, 11, fill=LIGHT, sw=0.9))
        o.append(tx(36, yy, str(i + 1), size=9.2, weight="bold"))
        o.append(tx(56, yy, s, size=10.0, anchor="start"))
    return mk(680, 216, o,
              "Hình 1.2 · Năm mục tiêu của chương trình, vẽ lại từ tờ mục tiêu ở phần mở đầu.",
              "Figure 1.2 · The program's five objectives, redrawn from the front-matter slide.",
              "Năm mục tiêu được đánh số của chương trình chuẩn đối sánh.",
              "Five numbered objectives of the benchmarking program.")


def fig_beliefs():
    o = panel(10, 10, 660, 236, "<00> CSIA Beliefs", fill=PAPER)
    beliefs = [
        "The end customer must be the focus and ultimate beneficiary of our efforts.",
        "Dedication to continuous improvement is a prerequisite to ongoing success.",
        "A broad-based, effective quality management system benefits CSI and customer.",
        "Quality efforts are more productive when directed toward prevention, not correction.",
        "A good reputation in industry and community is essential.",
        "Compliance with all local, state and federal regulations is essential.",
        "Our greatest resources are the knowledge, skill, creativity and productivity of people.",
        "Sound policies, practices and standards provide a superior product at reduced cost.",
        "All employees have the right to a safe working environment; all accidents are preventable.",
        "The use of benchmarks will raise the standard of excellence of our industry.",
    ]
    for i, s in enumerate(beliefs):
        yy = 47 + i * 18.5
        o.append(_circle(26, yy - 3, 2.6, fill=BLUE, sw=0))
        for k, ln in enumerate(wrap(s, 92)[:1]):
            o.append(tx(36, yy, ln, size=8.3, anchor="start"))
    return mk(680, 256, o,
              "Hình 1.3 · Mười tín điều CSIA, được sơ đồ hóa từ danh sách ở trang iv.",
              "Figure 1.3 · The ten CSIA beliefs, schematised from the list on page iv.",
              "Danh sách mười tín điều về chất lượng, con người và chuẩn đối sánh.",
              "Ten beliefs about quality, people and benchmarking.")


CSI_SERVICES = [
    ("Process / Technology\nKnowledge", "Process / Technology\nKnowledge"),
    ("Consulting", "Consulting"),
    ("Integrated Solutions", "Integrated Solutions"),
    ("Design & Application\nDevelopment", "Design & Application\nDevelopment"),
    ("Support Services", "Support Services"),
    ("Value-Add services\n(staff augmentation,\ntraining, site supervision,\nmaintenance)",
     "Value-Add services\n(staff augmentation,\ntraining, site supervision,\nmaintenance)"),
]


def fig_csi_services():
    o = [tx(340, 24, "A Control Systems Integrator delivers", size=11.5,
            weight="bold")]
    cx, cy = 340, 178
    o.append(_circle(cx, cy, 62, fill=BLUE, sw=1.2))
    o.append(tx(cx, cy - 6, "CSI", size=17, color="#ffffff", weight="bold"))
    o.append(tx(cx, cy + 12, "value-added", size=8, color="#ffffff"))
    o.append(tx(cx, cy + 23, "engineering", size=8, color="#ffffff"))
    n = len(CSI_SERVICES)
    for i, (vi, en) in enumerate(CSI_SERVICES):
        ang = -math.pi / 2.0 + 2 * math.pi * i / n
        bx = cx + 214 * math.cos(ang)
        by = cy + 104 * math.sin(ang)
        bw, bh = 176, 48
        o.append(line(cx + 62 * math.cos(ang), cy + 62 * math.sin(ang),
                      bx - (bw / 2.0) * math.cos(ang),
                      by - (bh / 2.0) * math.sin(ang), sw=0.9, color=GREY))
        o.append(rect(bx - bw / 2.0, by - bh / 2.0, bw, bh,
                      fill=(LIGHT if i % 2 == 0 else WARM), sw=0.9))
        for k, ln in enumerate(en.split("\n")):
            o.append(tx(bx, by - 8 + k * 10.5, ln, size=7.6))
    return mk(680, 302, o,
              "Hình 1.4 · Sơ đồ hóa sáu nhóm dịch vụ mà một CSI cung cấp theo định nghĩa ở điều 1.2.",
              "Figure 1.4 · Schematic of the six service groups a CSI delivers, from the §1.2 definition.",
              "Vòng tròn trung tâm CSI nối tới sáu nhóm dịch vụ.",
              "A central CSI hub linked to six service groups.")


# =========================================================== Chapter 2
DECISION_STEPS = [
    "1  State the Decision",
    "2  Develop Criteria",
    "3  Classify into Musts (M) / Wants",
    "4  Weigh the Wants (1–10)",
    "5  Screen candidates through Musts",
    "6  Evaluate & score against Wants",
    "7  Assess risks to manage",
    "8  Make the decision",
]


def fig_decision_steps():
    o = [tx(340, 22, "Kepner-Tregoe® decision analysis — eight structured steps",
            size=11, weight="bold")]
    for i, s in enumerate(DECISION_STEPS):
        y = 40 + i * 34
        o.append(rect(96, y, 488, 27,
                      fill=(LIGHT if i % 2 == 0 else MINT), sw=0.9))
        o.append(_circle(118, y + 13.5, 10.5, fill=BLUE, sw=0.8))
        o.append(tx(118, y + 17, str(i + 1), size=9.0, color="#ffffff",
                    weight="bold"))
        o.append(tx(138, y + 18, s[2:], size=9.0, anchor="start"))
        if i < 7:
            o.append(arw(340, y + 27, 340, y + 34, sw=1.0))
    o.append(tx(340, 322, "Steps 1–4 define the decision; steps 5–8 execute it.",
                size=8.2, color=GREY))
    return mk(680, 336, o,
              "Hình 2.1 · Sơ đồ hóa tám bước có cấu trúc của điều 2.2 (phương pháp Kepner-Tregoe).",
              "Figure 2.1 · Schematic of the eight structured steps in §2.2 (Kepner-Tregoe method).",
              "Tám ô được đánh số xếp thành hai cột.",
              "Eight numbered boxes arranged in two columns.")


def fig_musts_wants():
    o = panel(10, 10, 320, 200, "Musts (M)  ·  go / no-go", fill=ROSE,
              band=RED)
    o.append(panel(350, 10, 320, 200, "Wants  ·  weight 1–10", fill=MINT,
                   band=GREEN)[0])
    o.append(rect(350, 10, 320, 24, fill=GREEN, sw=1.0))
    o.append(tx(359, 26, "Wants  ·  weight 1–10", size=9.4, anchor="start",
                color="#ffffff", weight="bold"))
    left = ["Over $X.XM in sales  →  M",
            "Office procedures manual  →  M",
            "Adequate backup system  →  M",
            "Formulated owner/management transition  →  M"]
    right = ["Low turnover rate  →  7",
             "Application experience  →  9",
             "Commit to project team  →  10",
             "Support system  →  8"]
    for i, s in enumerate(left):
        o.append(tx(24, 62 + i * 34, s, size=8.3, anchor="start"))
    for i, s in enumerate(right):
        o.append(tx(364, 62 + i * 34, s, size=8.3, anchor="start"))
    o.append(tx(340, 232,
                "Musts screen candidates out; wants are weighted and scored 0–5.",
                size=8.6, color=GREY))
    return mk(680, 246, o,
              "Hình 2.2 · Phân loại tiêu chí thành «phải» (M) và «mong muốn» có trọng số, "
              "sơ đồ hóa từ các ví dụ ở điều 2.2 và bảng mẫu điều 2.5.",
              "Figure 2.2 · Classifying criteria into musts (M) and weighted wants, "
              "schematised from the §2.2 examples and the §2.5 sample table.",
              "Hai cột: tiêu chí bắt buộc và tiêu chí mong muốn có trọng số.",
              "Two columns: mandatory criteria and weighted desired criteria.")


def fig_screen():
    rows = [
        ["CSI A", "Over $X.XM in sales", "GO", "continued"],
        ["CSI B", "Over $X.XM in sales", "GO", "continued"],
        ["CSI C", "Under $X.XM in sales", "NO GO", "eliminated"],
    ]
    o = [tx(340, 22, "Step 5 — screen candidates through the musts", size=11,
            weight="bold")]
    o += vtab(24, 42, [70, 250, 90, 240],
              ["Candidate", "Must criterion", "Result", "Consequence"], rows,
              rowh=32, size=8.6, fills=["#ffffff", "#ffffff", ROSE],
              align=["middle", "start", "middle", "start"])
    o.append(tx(340, 190,
                "Only candidates passing every must proceed to weighted scoring.",
                size=8.6, color=GREY))
    return mk(680, 206, o,
              "Hình 2.3 · Ví dụ sàng lọc ba ứng viên qua tiêu chí «phải» ở điều 2.2, bước 5.",
              "Figure 2.3 · Worked must-screening example for three candidates, §2.2 step 5.",
              "Bảng ba ứng viên, CSI C bị loại vì không đạt tiêu chí bắt buộc.",
              "Table of three candidates; CSI C is eliminated by a must.")


def fig_score_worked():
    rows = [
        ["CSI A", "7 × 4 = 28", "9 × 3 = 27", "55"],
        ["CSI B", "7 × 3 = 21", "9 × 4 = 36", "57"],
    ]
    o = [tx(340, 22, "Step 6 — weight × performance = total score", size=11,
            weight="bold")]
    o += vtab(24, 42, [90, 190, 190, 180],
              ["Candidate", "Low turnover (w=7)", "Application experience (w=9)",
               "TOTAL SCORE"], rows, rowh=34, size=8.8,
              fills=["#ffffff", MINT])
    o.append(tx(340, 178,
                "CSI B wins on score — but step 7 still requires a risk assessment.",
                size=8.6, color=GREY))
    return mk(680, 198, o,
              "Hình 2.4 · Tính điểm có trọng số cho CSI A và CSI B theo ví dụ điều 2.2, bước 6.",
              "Figure 2.4 · Weighted scoring of CSI A and CSI B from the §2.2 example, step 6.",
              "Bảng tính điểm: CSI B đạt 57, CSI A đạt 55.",
              "Scoring table: CSI B reaches 57, CSI A 55.")


# =========================================================== Chapter 3
SCORE_SCALE = [
    ("0", "No evidence of policy, practice or standards systems in place; no work initiated."),
    ("1", "Basic elements initiated; implementation, training and documentation minimal or absent."),
    ("2", "Basic elements partially implemented; training, documentation and records incomplete."),
    ("3", "Mostly implemented with supporting documentation; minimally adequate, room to improve."),
    ("4", "Higher elements implemented with good documentation; uniformly applied, good effectiveness."),
    ("5", "Well thought out, documented and implemented to the point of outstanding; CI demonstrated."),
]


def fig_score_scale():
    o = [tx(340, 22, "§2.3 — suggested performance scoring system (0–5)",
            size=11, weight="bold")]
    for i, (n, s) in enumerate(SCORE_SCALE):
        yy = 40 + i * 40
        o.append(rect(24, yy, 44, 34, fill=BLUE if i >= 4 else LIGHT, sw=0.8))
        o.append(tx(46, yy + 23, n, size=14,
                    color="#ffffff" if i >= 4 else INK, weight="bold"))
        o.append(rect(68, yy, 588, 34,
                      fill=("#ffffff" if i % 2 == 0 else "#f6f9fc"), sw=0.7))
        for k, ln in enumerate(wrap(s, 96)[:2]):
            o.append(tx(78, yy + 15 + k * 11, ln, size=8.1, anchor="start"))
    return mk(680, 292, o,
              "Hình 3.1 · Thang điểm hiệu năng 0–5 của điều 2.3, được vẽ lại thành thẻ vector.",
              "Figure 3.1 · The §2.3 performance scoring scale 0–5, redrawn as a vector ladder.",
              "Sáu mức từ 0 đến 5 kèm mô tả mức trưởng thành.",
              "Six maturity levels from 0 to 5 with descriptions.")


def fig_levels():
    rows = [
        ["Annual sales", "$0.5 to $2 Mill.", "$1.5 to $5 Mill.", "$5 Mill. Plus"],
        ["Number of personnel", "Less than 20", "15 to 50", "30 Plus"],
        ["% of staff that are engineers", "Less than 40%", "40 to 60%", "Over 60%"],
    ]
    o = [tx(340, 22, "§2.4 — CSIA suggested classification levels", size=11,
            weight="bold")]
    o += vtab(24, 42, [212, 148, 148, 148],
              ["Criterion", "Level 3", "Level 2", "Level 1"], rows,
              rowh=34, size=8.6, align=["start", "middle", "middle", "middle"])
    o.append(tx(340, 200,
                "Larger CSIs require more business infrastructure; evaluate CSIs by level.",
                size=8.6, color=GREY))
    return mk(680, 218, o,
              "Hình 3.2 · Ba cấp phân loại CSI theo quy mô của điều 2.4, vẽ lại nguyên vẹn.",
              "Figure 3.2 · The three CSIA classification levels of §2.4, reproduced in full.",
              "Bảng so sánh doanh thu, nhân sự và tỷ lệ kỹ sư giữa ba cấp.",
              "Table comparing sales, staff and engineer ratio across three levels.")


def fig_sample_table():
    rows = [
        "4.1  General Management",
        ["A. Define / clear strategic objectives", "—", "2", "3 (6)",
         "1,2,2 (4)", "0,1,0 (0)"],
        ["B. Monitored short-range objectives", "—", "4", "3 (12)",
         "4,4,5 (16)", "2,2,2 (8)"],
        ["C. Owner / management transition", "M", "—", "—", "GO", "GO"],
        ["B. Office procedures manual", "M", "8", "4 (32)",
         "GO", "NO GO"],
    ]
    o = [tx(340, 20, "§2.5 — sample criteria / analysis table (abridged)",
            size=10.6, weight="bold")]
    o += vtab(14, 36, [226, 52, 78, 78, 110, 110],
              ["Criterion", "Must", "Weight", "Max / good",
               "CSI A* scores", "CSI B* scores"], rows,
              rowh=26, headh=30, size=7.6,
              align=["start", "middle", "middle", "middle", "middle", "middle"])
    o.append(tx(340, 214,
                "* Three resources judged each CSI; the number in ( ) is weight × average score.",
                size=7.8, color=GREY))
    return mk(680, 230, o,
              "Hình 3.3 · Trích đoạn bảng tiêu chí / phân tích mẫu ở điều 2.5, vẽ lại dạng vector.",
              "Figure 3.3 · Abridged redraw of the §2.5 sample criteria / analysis table.",
              "Bảng tiêu chí với cột bắt buộc, trọng số và điểm ba người chấm.",
              "Criteria table with must, weight and three-judge score columns.")


def fig_three_judges():
    o = [tx(340, 22, "How a performance score is computed", size=11,
            weight="bold")]
    boxes = [
        (24, "1st resource", "1", LIGHT),
        (154, "2nd resource", "2", LIGHT),
        (284, "3rd resource", "2", LIGHT),
    ]
    for x, lab, v, fill in boxes:
        o.append(rect(x, 52, 112, 62, fill=fill, sw=0.9))
        o.append(tx(x + 56, 72, lab, size=8.0))
        o.append(tx(x + 56, 100, v, size=17, weight="bold"))
    o.append(tx(408, 88, "1 + 2 + 2 = 5", size=11, anchor="start",
                weight="bold"))
    o.append(tx(408, 106, "average 5 / 3 = 1.66 → 2", size=8.6,
                anchor="start"))
    o.append(arw(340, 122, 340, 142))
    o.append(rect(150, 146, 380, 46, fill=MINT, sw=1.0))
    o.append(tx(340, 175,
                "User weight (2) × average score (2) = 4", size=10.4,
                weight="bold"))
    o.append(tx(340, 214,
                "Worked example for criterion 4.1.1 A, as printed in §2.2.",
                size=8.0, color=GREY))
    return mk(680, 230, o,
              "Hình 3.4 · Sơ đồ hóa cách tính điểm trung bình của ba người chấm tại điều 2.2 "
              "(ví dụ tiêu chí 4.1.1 A).",
              "Figure 3.4 · Schematic of the three-judge averaging calculation in §2.2 "
              "(criterion 4.1.1 A example).",
              "Ba ô điểm riêng lẻ dẫn tới trung bình và tích với trọng số.",
              "Three individual scores lead to an average and a weighted product.")


# =========================================================== Chapter 4
def fig_registration_flow():
    o = [tx(340, 22, "§3.1 — CSIA registration: who audits whom", size=11,
            weight="bold")]
    steps = [
        (18, "CSI applies", LIGHT),
        (174, "Independent\nthird-party audit", WARM),
        (330, "CSIA Best Practices\n& Benchmarks criteria", MINT),
        (486, "Registered CSI\nlisted on controlsys.org", LIGHT),
    ]
    for x, lab, fill in steps:
        o.append(rect(x, 64, 146, 74, fill=fill, sw=1.0))
        for k, ln in enumerate(lab.split("\n")):
            o.append(tx(x + 73, 94 + (k - 0.5) * 13, ln, size=8.6))
    for x in (164, 320, 476):
        o.append(arw(x - 12, 101, x + 8, 101, sw=1.2))
    o.append(rect(18, 164, 614, 52, fill=PAPER, sw=0.9))
    o.append(tx(32, 186,
                "Client benefit: immediate evaluation, lower selection effort, cost and risk.",
                size=9.2, anchor="start"))
    o.append(tx(32, 204,
                "Registration criteria = §4.1 through §4.6; an established industry metric.",
                size=8.2, anchor="start", color=GREY))
    return mk(680, 230, o,
              "Hình 4.1 · Sơ đồ hóa quy trình đăng ký CSIA và lợi ích cho khách hàng theo điều 3.1.",
              "Figure 4.1 · Schematic of the CSIA registration process and client benefit, from §3.1.",
              "Bốn ô từ đăng ký đến danh sách công bố, kèm lợi ích cho khách hàng.",
              "Four boxes from application to published register, plus client benefit.")


def fig_criteria_map():
    o = [tx(340, 22, "§4 — the seven suggested-criteria domains", size=11,
            weight="bold")]
    cx, cy, r = 340, 152, 108
    o.append(_circle(cx, cy, 56, fill=BLUE, sw=1.1))
    o.append(tx(cx, cy - 4, "§4", size=15, color="#ffffff", weight="bold"))
    o.append(tx(cx, cy + 12, "CSI criteria", size=8, color="#ffffff"))
    labels = ["4.1 General\nManagement", "4.2 Human\nResources",
              "4.3 Project\nManagement", "4.4 Quality\nManagement",
              "4.5 Financial\nManagement", "4.6 Business\nDevelopment",
              "4.7 Technical"]
    for i, lab in enumerate(labels):
        a = -math.pi / 2.0 + 2 * math.pi * i / len(labels)
        bx, by = cx + r * 1.75 * math.cos(a), cy + r * 1.05 * math.sin(a)
        o.append(line(cx + 56 * math.cos(a), cy + 56 * math.sin(a),
                      bx - 66 * math.cos(a), by - 22 * math.sin(a),
                      sw=0.8, color=GREY))
        o.append(rect(bx - 66, by - 22, 132, 44,
                      fill=(LIGHT if i % 2 == 0 else WARM), sw=0.9))
        for k, ln in enumerate(lab.split("\n")):
            o.append(tx(bx, by - 2 + (k - 0.5) * 11, ln, size=7.8))
    o.append(tx(340, 288,
                "Clients may add their own criteria in the blank rows provided.",
                size=8.2, color=GREY))
    return mk(680, 302, o,
              "Hình 4.2 · Sơ đồ hóa bảy nhóm tiêu chí gợi ý của điều 4 (4.1–4.7).",
              "Figure 4.2 · Schematic of the seven suggested-criteria domains in §4.1–4.7.",
              "Bảy nhóm tiêu chí bao quanh tâm §4.",
              "Seven criteria groups arranged around a §4 hub.")


# =========================================================== Chapter 5
def fig_hr_tree():
    o = [tx(340, 22, "§4.2 — Human Resources criteria", size=11, weight="bold")]
    o.append(rect(240, 40, 200, 42, fill=BLUE, sw=1.0))
    o.append(tx(340, 66, "Human Resources", size=10.4, color="#ffffff",
                weight="bold"))
    subs = [("4.2.1 Administration", "Records, policies, benefits, training records"),
            ("4.2.2 Recruiting", "Sourcing, screening, retention practices"),
            ("4.2.3 User Defined", "Client-specific criteria (blank rows)")]
    for i, (h, s) in enumerate(subs):
        x = 20 + i * 220
        o.append(line(340, 82, x + 100, 112, sw=0.8, color=GREY))
        o.append(rect(x, 112, 200, 74, fill=(LIGHT if i < 2 else PAPER),
                      sw=0.9, dash=("4 3" if i == 2 else "")))
        o.append(tx(x + 100, 134, h, size=8.8, weight="bold"))
        for k, ln in enumerate(wrap(s, 30)[:2]):
            o.append(tx(x + 100, 153 + k * 11, ln, size=7.4, color=GREY))
    return mk(680, 204, o,
              "Hình 5.1 · Sơ đồ hóa ba nhóm con của tiêu chí Nhân sự, điều 4.2.",
              "Figure 5.1 · Schematic of the three Human Resources sub-groups, §4.2.",
              "Một ô cha nối tới ba ô con, trong đó có ô do người dùng tự định nghĩa.",
              "One parent node linking three children, one user-defined.")


def fig_project_lifecycle():
    o = [tx(340, 22, "§4.3 — Project Management across the project lifecycle",
            size=10.8, weight="bold")]
    stages = [
        ("4.3.1", "Planning &\nmethodologies"),
        ("4.3.2", "Design\nstandards"),
        ("4.3.3", "Quality\nprocedures"),
        ("4.3.4", "Documentation"),
        ("4.3.5", "Testing &\nimplementation"),
        ("4.3.6", "Safety training\non projects"),
        ("4.3.7", "User\ndefined"),
    ]
    for i, (n, lab) in enumerate(stages):
        x = 14 + i * 94
        o.append(rect(x, 58, 86, 76,
                      fill=(PAPER if i == 6 else (LIGHT if i % 2 == 0 else MINT)),
                      sw=0.9, dash=("4 3" if i == 6 else "")))
        o.append(tx(x + 43, 76, n, size=8.0, weight="bold", color=BLUE))
        for k, ln in enumerate(lab.split("\n")):
            o.append(tx(x + 43, 98 + k * 11, ln, size=7.6))
        if i < len(stages) - 1:
            o.append(arw(x + 86, 96, x + 94, 96, sw=1.0))
    o.append(rect(14, 154, 652, 46, fill=PAPER, sw=0.9))
    o.append(tx(26, 174,
                "Each stage is a set of questions the client asks the CSI, not a pass/fail test.",
                size=8.8, anchor="start"))
    o.append(tx(26, 191,
                "§4.3.7 and the trailing A/B/C/D blank rows are reserved for client criteria.",
                size=7.8, anchor="start", color=GREY))
    return mk(680, 214, o,
              "Hình 5.2 · Sơ đồ hóa bảy nhóm câu hỏi quản lý dự án ở điều 4.3 theo trình tự vòng đời.",
              "Figure 5.2 · Schematic of the seven §4.3 project-management question groups in lifecycle order.",
              "Bảy ô nối tiếp nhau từ lập kế hoạch đến đào tạo an toàn.",
              "Seven linked boxes from planning through safety training.")


# =========================================================== Chapter 6
def fig_quality_loop():
    o = [tx(340, 22, "§4.4 — Quality Management: continuous, measurable improvement",
            size=10.4, weight="bold")]
    cx, cy, r = 340, 132, 84
    labels = ["4.4.1 Leadership", "4.4.2 Effective\ncommunication",
              "4.4.3 Continuous,\nmeasurable improvement",
              "4.4.4 Customer service", "4.4.5 User defined"]
    for i, lab in enumerate(labels):
        a = -math.pi / 2.0 + 2 * math.pi * i / len(labels)
        px, py = cx + r * math.cos(a), cy + r * math.sin(a)
        o.append(_circle(px, py, 40, fill=(PAPER if i == 4 else LIGHT),
                         sw=1.0, color=INK if i < 4 else GREY))
        for k, ln in enumerate(lab.split("\n")):
            o.append(tx(px, py + (k - 0.5) * 10 + 3, ln, size=7.4))
        b = -math.pi / 2.0 + 2 * math.pi * (i + 1) / len(labels)
        qx, qy = cx + r * math.cos(b), cy + r * math.sin(b)
        o.append(arw(px + 34 * math.cos(a + 0.55), py + 34 * math.sin(a + 0.55),
                     qx - 34 * math.cos(a + 0.55), qy - 34 * math.sin(a + 0.55),
                     sw=0.9))
    o.append(tx(340, 246,
                "Prevention over correction: quality efforts are more productive when preventive.",
                size=8.2, color=GREY))
    return mk(680, 262, o,
              "Hình 6.1 · Sơ đồ hóa vòng lặp năm nhóm tiêu chí quản lý chất lượng ở điều 4.4.",
              "Figure 6.1 · Schematic of the five §4.4 quality-management criteria as a loop.",
              "Năm vòng tròn nối thành vòng lặp cải tiến liên tục.",
              "Five circles joined into a continuous-improvement loop.")


def fig_financial_map():
    o = [tx(340, 20, "§4.5 Financial Management · §4.6 Business Development",
            size=10.6, weight="bold")]
    cols = [
        ("§4.5 Financial Management", BLUE,
         ["4.5.1 Measures of financial performance",
          "4.5.2 Financial planning", "4.5.3 Billing procedures",
          "4.5.4 Project financial reporting", "4.5.5 Tax policy",
          "4.5.6 User defined"]),
        ("§4.6 Business Development", GREEN,
         ["4.6.1 Business development practices",
          "4.6.2 Development of proposals",
          "4.6.3 Negotiating and contracting", "4.6.4 User defined"]),
    ]
    for j, (head, band, items) in enumerate(cols):
        x = 18 + j * 330
        o += panel(x, 40, 312, 190, head, fill=PAPER, band=band, size=8.8)
        for i, s in enumerate(items):
            yy = 80 + i * 24
            o.append(_circle(x + 18, yy - 3, 2.6, fill=band, sw=0))
            o.append(tx(x + 28, yy, s, size=8.1, anchor="start"))
    return mk(680, 244, o,
              "Hình 6.2 · Sơ đồ hóa sáu nhóm tài chính (4.5) và bốn nhóm phát triển kinh doanh (4.6).",
              "Figure 6.2 · Schematic of the six §4.5 financial and four §4.6 business-development groups.",
              "Hai cột liệt kê các nhóm tiêu chí tài chính và phát triển kinh doanh.",
              "Two columns listing financial and business-development criteria groups.")


def fig_business_flow():
    o = [tx(340, 22, "From business development to a signed contract", size=10.8,
            weight="bold")]
    steps = ["4.6.1\nPractices", "4.6.2\nProposals",
             "4.6.3\nNegotiating &\ncontracting", "4.6.4\nUser defined"]
    for i, s in enumerate(steps):
        x = 22 + i * 164
        o.append(rect(x, 58, 146, 84,
                      fill=(PAPER if i == 3 else LIGHT), sw=1.0,
                      dash=("4 3" if i == 3 else "")))
        for k, ln in enumerate(s.split("\n")):
            o.append(tx(x + 73, 88 + (k - 1) * 11, ln, size=8.4))
        if i < 3:
            o.append(arw(x + 146, 100, x + 164, 100, sw=1.2))
    o.append(rect(22, 164, 636, 46, fill=PAPER, sw=0.9))
    o.append(tx(34, 184,
                "For each: what is documented, who is responsible, how is it reviewed and improved?",
                size=8.8, anchor="start"))
    o.append(tx(34, 201,
                "Volume 2 of the CSIA Guide covers RFP development and proposal evaluation.",
                size=7.8, anchor="start", color=GREY))
    return mk(680, 222, o,
              "Hình 6.3 · Sơ đồ hóa chu trình phát triển kinh doanh ở điều 4.6.",
              "Figure 6.3 · Schematic of the §4.6 business-development sequence.",
              "Bốn ô nối tiếp từ thực hành đến hợp đồng.",
              "Four linked boxes from practices through contracting.")


# =========================================================== Chapter 7
def fig_technical_domains():
    o = [tx(340, 20, "§4.7 — Technical qualifications, experience, services, risk",
            size=10.4, weight="bold")]
    rows = [
        "4.7.1 Technical Qualifications",
        ["A", "Software / hardware platform experience", "Training, recency, in-house support"],
        ["B", "Hardware", "Client-standard hardware capability"],
        ["C", "Software", "Client-standard software capability"],
        ["D", "Industry", "Sector regulations, standards, professional bodies"],
        ["E–F", "User defined", "Blank rows for client criteria"],
        "4.7.2 Project Experience  ·  4.7.3 Type of Services  ·  4.7.4 Risk Considerations",
    ]
    o += vtab(14, 38, [52, 238, 360],
              ["Ref", "Area", "What the client asks"], rows,
              rowh=27, headh=28, size=8.0,
              align=["middle", "start", "start"])
    return mk(680, 246, o,
              "Hình 7.1 · Sơ đồ hóa bốn nhóm câu hỏi kỹ thuật ở điều 4.7.1 cùng ba nhóm còn lại của điều 4.7.",
              "Figure 7.1 · Schematic of the §4.7.1 technical question groups and the other §4.7 sub-sections.",
              "Bảng bốn nhóm kỹ thuật và một hàng tóm tắt ba nhóm cuối.",
              "Table of four technical groups plus a summary row for the final three.")


def fig_risk_balance():
    o = [tx(340, 22, "Step 7–8 — balance total score against manageable risk",
            size=10.8, weight="bold")]
    o.append(rect(22, 46, 310, 116, fill=MINT, sw=1.0))
    o.append(tx(38, 68, "CSI B — highest score (57)", size=9.6,
                anchor="start", weight="bold"))
    o.append(tx(38, 92, "Risk: turnover rate is borderline high.", size=8.4,
                anchor="start"))
    o.append(tx(38, 112, "Mitigation: secure commitment of key", size=8.4,
                anchor="start"))
    o.append(tx(38, 128, "project resources before award.", size=8.4,
                anchor="start"))
    o.append(rect(348, 46, 310, 116, fill=WARM, sw=1.0))
    o.append(tx(364, 68, "CSI A — lower score (55)", size=9.6,
                anchor="start", weight="bold"))
    o.append(tx(364, 92, "Risk: application experience is marginal.", size=8.4,
                anchor="start"))
    o.append(tx(364, 112, "Mitigation: review the specification", size=8.4,
                anchor="start"))
    o.append(tx(364, 128, "carefully before award.", size=8.4, anchor="start"))
    o.append(rect(22, 178, 636, 42, fill=PAPER, sw=0.9))
    o.append(tx(340, 204,
                "Select the CSI with the best criterion balance AND acceptable, manageable risks.",
                size=9.0))
    return mk(680, 232, o,
              "Hình 7.2 · Sơ đồ hóa bước đánh giá rủi ro và ra quyết định (điều 2.2, bước 7–8) "
              "và điều 4.7.4.",
              "Figure 7.2 · Schematic of risk assessment and the final decision "
              "(§2.2 steps 7–8) alongside §4.7.4.",
              "Hai thẻ so sánh rủi ro của CSI A và CSI B.",
              "Two cards comparing the risks of CSI A and CSI B.")


# =========================================================== Chapter 8
def fig_taxonomy():
    o = [tx(340, 20, "Appendix A — positioning providers by type", size=10.8,
            weight="bold")]
    o.append(rect(24, 40, 632, 40, fill=BLUE, sw=1.0))
    o.append(tx(340, 65, "Control System Integration market", size=10.4,
                color="#ffffff", weight="bold"))
    branches = [
        (18, "1–2  CSI", BLUE,
         ["Control Systems Integrator (>61% services)",
          "Types: Design/Build, CS, MES, IT"]),
        (338, "3–4  CSP", GREEN,
         ["Control Systems Provider (<61% services)",
          "Types: Equipment, Control, Panel, Construction"]),
    ]
    for x, head, band, items in branches:
        o.append(line(340, 80, x + 155, 108, sw=0.9, color=GREY))
        o += panel(x, 108, 310, 96, head, fill=PAPER, band=band, size=9.2)
        for i, s in enumerate(items):
            o.append(tx(x + 12, 148 + i * 22, s, size=7.8, anchor="start"))
    o.append(rect(24, 218, 632, 40, fill=PAPER, sw=0.9))
    o.append(tx(36, 243,
                "5  Other Control System Integrators   ·   6  Other System Integrators (commercial)",
                size=8.6, anchor="start"))
    return mk(680, 270, o,
              "Hình 8.1 · Sơ đồ hóa sáu mục của Phụ lục A: CSI, CSP và các nhóm còn lại.",
              "Figure 8.1 · Schematic of Appendix A's six entries: CSI, CSP and the remaining groups.",
              "Sơ đồ nhánh phân loại CSI và CSP cùng các nhóm khác.",
              "Branch diagram classifying CSI and CSP plus other groups.")


# (label, display, numeric) — "<X%" plotted at its upper bound (noted in caption)
PIES = [
    ("CSI", "Control Systems Integrator (CSI)", "Greater than 61%",
     [("Consulting", "&lt;5%", 5), ("Project Management", "&lt;5%", 5),
      ("Specification/Design", "15%", 15), ("Development/Test", "30%", 30),
      ("Purchase Hardware/Software", "12%", 12), ("Panels/Stations", "&lt;5%", 5),
      ("Construction", "23%", 23), ("Commissioning/Training", "7%", 7),
      ("Ongoing Support", "&lt;5%", 5)]),
    ("DESIGN_BUILD", "Design/Build Integrator / Services", ">61% after construction",
     [("Consulting", "&lt;5%", 5), ("Project Management", "10%", 10),
      ("Specification/Design", "10%", 10), ("Development/Test", "20%", 20),
      ("Purchase Hardware/Software", "8%", 8), ("Panels/Stations", "&lt;5%", 5),
      ("Construction", "35%", 35), ("Commissioning/Training", "7%", 7),
      ("Ongoing Support", "&lt;5%", 5)]),
    ("CS", "Control Systems Integrator / Services", ">61% integration services",
     [("Consulting", "&lt;5%", 5), ("Project Management", "&lt;5%", 5),
      ("Specification/Design", "15%", 15), ("Development/Test", "30%", 30),
      ("Purchase Hardware/Software", "12%", 12), ("Panels/Stations", "&lt;5%", 5),
      ("Construction", "23%", 23), ("Commissioning/Training", "7%", 7),
      ("Ongoing Support", "&lt;5%", 5)]),
    ("MES", "Manufacturing Execution Systems Integrator", "much greater than 61%",
     [("Consulting", "&lt;10%", 10), ("Project Management", "7%", 7),
      ("Specification/Design", "10%", 10), ("Development/Testing", "30%", 30),
      ("Purchase Hardware/Software", "15%", 15), ("Construction", "&lt;5%", 5),
      ("Commissioning/Training", "10%", 10), ("Ongoing Support", "15%", 15)]),
    ("IT", "IT Systems Integration / Services", "much greater than 61%",
     [("Consulting", "&lt;10%", 10), ("Project Management", "10%", 10),
      ("Specification/Design", "10%", 10), ("Development/Testing", "30%", 30),
      ("Purchase Hardware/Software", "15%", 15), ("Construction", "&lt;5%", 5),
      ("Commissioning/Training", "10%", 10), ("Ongoing Support", "15%", 15)]),
    ("CSP", "Control Systems Provider (CSP)", "less than 61%",
     [("Consulting", "&lt;5%", 5), ("Project Management", "&lt;5%", 5),
      ("Specification/Design", "&lt;10%", 10), ("Application Engineering/Test", "20%", 20),
      ("Purchase Equipment/HW/SW", "30%", 30), ("Panels/Stations", "&lt;5%", 5),
      ("Installation", "20%", 20), ("Commissioning/Training", "7%", 7),
      ("Warranty/Ongoing Support", "&lt;5%", 5)]),
    ("EQUIP", "Equipment Solutions Provider", "less than 61%",
     [("Consulting", "&lt;5%", 5), ("Project Management", "10%", 10),
      ("Specification/Design", "&lt;10%", 10), ("Application Engineering/Test", "15%", 15),
      ("Purchase Equipment/HW/SW", "35%", 35), ("Panels/Stations", "&lt;5%", 5),
      ("Construction", "15%", 15), ("Commissioning/Training", "&lt;5%", 5),
      ("Warranty/Ongoing Support", "&lt;5%", 5)]),
    ("CONTROL", "Control Solutions Provider", "less than 61%",
     [("Consulting", "&lt;5%", 5), ("Project Management", "5%", 5),
      ("Specification/Design", "&lt;10%", 10), ("Application Engineering/Test", "20%", 20),
      ("Purchase Hardware/Software", "35%", 35), ("Panels/Stations", "10%", 10),
      ("Construction", "15%", 15), ("Commissioning/Training", "7%", 7),
      ("Warranty/Ongoing Support", "&lt;7%", 7)]),
    ("PANEL", "Control Panel Shop Provider", "less than 61%",
     [("Consulting", "&lt;1%", 1), ("Project Management", "&lt;1%", 1),
      ("Specification/Design", "5%", 5), ("Application Engineering/Test", "10%", 10),
      ("Purchase Hardware/Software", "55%", 55), ("Panels/Stations", "15%", 15),
      ("Installation Support", "&lt;10%", 10), ("Commissioning/Training", "&lt;5%", 5),
      ("Warranty/Ongoing Support", "&lt;3%", 3)]),
    ("CONSTRUCT", "Construction / Control Systems Provider", "less than 61%",
     [("Consulting", "&lt;5%", 5), ("Project Management", "12%", 12),
      ("Specification/Design", "6%", 6), ("Development/Test", "15%", 15),
      ("Purchase Hardware/Software", "20%", 20), ("Panels/Stations", "7%", 7),
      ("Construction", "30%", 30), ("Commissioning/Training", "7%", 7),
      ("Ongoing Support", "&lt;5%", 5)]),
]

PIE_VI = {
    "CSI": "Nhà tích hợp hệ thống điều khiển (CSI)",
    "DESIGN_BUILD": "Nhà tích hợp thiết kế / thi công trọn gói",
    "CS": "Nhà tích hợp dịch vụ hệ thống điều khiển",
    "MES": "Nhà tích hợp hệ thống điều hành sản xuất (MES)",
    "IT": "Nhà tích hợp hệ thống CNTT",
    "CSP": "Nhà cung cấp hệ thống điều khiển (CSP)",
    "EQUIP": "Nhà cung cấp giải pháp thiết bị",
    "CONTROL": "Nhà cung cấp giải pháp điều khiển",
    "PANEL": "Xưởng sản xuất tủ điện điều khiển",
    "CONSTRUCT": "Nhà cung cấp thi công / hệ thống điều khiển",
}


def _pie_figure(idx):
    key, en, note, items = PIES[idx]
    o = [tx(340, 18, en, size=10.4, weight="bold")]
    center = ["% Revenue", "derived from", "services", note[:22]]
    o += donut(158, 148, 96, items, center, 300, 74)
    o.append(tx(340, 268,
                "'<X%' plotted at its upper bound; original labels shown verbatim in the legend.",
                size=7.4, color=GREY))
    n = idx + 2
    vi = PIE_VI[key]
    return mk(680, 284, o,
              "Hình 8.%d · Cơ cấu dịch vụ điển hình — %s, vẽ lại từ biểu đồ Phụ lục A "
              "(trang %d)." % (n, vi, 40 + idx),
              "Figure 8.%d · Typical project mix of services — %s, redrawn from the "
              "Appendix A chart (page %d)." % (n, en, 40 + idx),
              "Biểu đồ vòng tròn thể hiện tỷ trọng doanh thu theo từng nhóm dịch vụ.",
              "Donut chart showing the revenue share of each service group.")


def pie(idx):
    return _pie_figure(idx)


# =========================================================== Chapter 9
def fig_blank_worksheet():
    rows = [
        "4.1  General Management",
        ["4.1.1 Strategic Management", "", "", "", "", "", ""],
        ["A. Define/clear strategic objectives", "", "", "3", "3", "4", ""],
        ["B. Monitored short-range objectives", "", "", "2", "3", "4", ""],
        ["C. Owner/management transition", "", "", "2", "2", "3", ""],
        ["D.  (client defined)", "", "", "", "", "", ""],
        "4.2  Human Resources  ·  …  ·  4.7  Technical",
        ["SECTION TOTAL / %", "", "", "", "", "", ""],
    ]
    o = [tx(340, 20, "Appendix B — blank Kepner-Tregoe® decision analysis worksheet",
            size=10.4, weight="bold")]
    o += vtab(10, 38, [206, 46, 58, 84, 84, 84, 84],
              ["Criterion", "Must", "Weight", "Suggested max",
               "Level 3 / 2 / 1", "CSI A", "CSI B / C"], rows,
              rowh=23, headh=30, size=7.4,
              align=["start", "middle", "middle", "middle", "middle",
                     "middle", "middle"])
    o.append(tx(340, 264,
                "Empty cells are for the client's own musts, weights and scores.",
                size=7.8, color=GREY))
    return mk(680, 280, o,
              "Hình 9.1 · Phiếu phân tích quyết định trống ở Phụ lục B, vẽ lại dạng bảng vector.",
              "Figure 9.1 · The blank Appendix B decision-analysis worksheet, redrawn as a vector table.",
              "Bảng tiêu chí với nhiều ô trống dành cho khách hàng điền.",
              "Criteria table with empty cells for the client to fill in.")


def fig_totals():
    rows = [
        ["GOAL SCORE", "347", "100%", "—"],
        ["CSI A", "190", "55%", "GO"],
        ["CSI B", "172", "50%", "GO"],
        ["CSI C", "—", "—", "NO GO"],
    ]
    o = [tx(340, 22, "§2.5 worked totals — General Management section",
            size=10.8, weight="bold")]
    o += vtab(40, 44, [180, 150, 150, 160],
              ["", "Score", "% of goal", "Must screen"], rows,
              rowh=30, size=8.8, fills=["#dce8f3", "#ffffff", "#ffffff", ROSE])
    o.append(tx(340, 208,
                "CSI C failed a must criterion, so its score is not calculated.",
                size=8.4, color=GREY))
    return mk(680, 226, o,
              "Hình 9.2 · Dòng tổng kết mẫu của mục Quản lý chung (347 / 190 / 172), vẽ lại từ điều 2.5.",
              "Figure 9.2 · The §2.5 sample General Management totals (347 / 190 / 172), redrawn.",
              "Bảng bốn dòng tổng kết điểm và tỷ lệ so với mục tiêu.",
              "Four-row table of scores and percentages against the goal.")


def fig_closing_map():
    o = [tx(340, 22, "Volume 1 in one view — from criteria to a defensible choice",
            size=10.4, weight="bold")]
    steps = [
        ("§1", "Know the market", "CSIA, CSI definition"),
        ("§2", "Structure the decision", "Kepner-Tregoe, 8 steps"),
        ("§3", "Use the register", "Third-party audited CSIs"),
        ("§4", "Choose your criteria", "7 domains, 4.1–4.7"),
        ("App. A", "Position the providers", "CSI vs CSP, 10 service mixes"),
        ("App. B", "Score and record", "Blank analysis worksheet"),
    ]
    for i, (n, h, s) in enumerate(steps):
        col, row = i % 3, i // 3
        x, y = 16 + col * 222, 44 + row * 108
        o.append(rect(x, y, 206, 88, fill=(LIGHT if row == 0 else MINT),
                      sw=1.0))
        o.append(tx(x + 103, y + 20, n, size=9.4, weight="bold", color=BLUE))
        o.append(tx(x + 103, y + 44, h, size=9.0, weight="bold"))
        o.append(tx(x + 103, y + 64, s, size=7.6, color=GREY))
    o.append(tx(340, 268,
                "Volume 2 continues with RFP development, proposal evaluation and project management.",
                size=8.2, color=GREY))
    return mk(680, 284, o,
              "Hình 9.3 · Sơ đồ tổng kết sáu phần của Tập 1 và vị trí của Tập 2.",
              "Figure 9.3 · Closing map of Volume 1's six parts and where Volume 2 takes over.",
              "Sáu ô tóm tắt từ hiểu thị trường đến chấm điểm và ghi nhận.",
              "Six boxes summarising the path from market knowledge to scoring.")


FIGS = {
    "mission": fig_mission, "objectives": fig_objectives,
    "beliefs": fig_beliefs, "csi_services": fig_csi_services,
    "decision_steps": fig_decision_steps, "musts_wants": fig_musts_wants,
    "screen": fig_screen, "score_worked": fig_score_worked,
    "score_scale": fig_score_scale, "levels": fig_levels,
    "sample_table": fig_sample_table, "three_judges": fig_three_judges,
    "registration_flow": fig_registration_flow, "criteria_map": fig_criteria_map,
    "hr_tree": fig_hr_tree, "project_lifecycle": fig_project_lifecycle,
    "quality_loop": fig_quality_loop, "financial_map": fig_financial_map,
    "business_flow": fig_business_flow,
    "technical_domains": fig_technical_domains, "risk_balance": fig_risk_balance,
    "taxonomy": fig_taxonomy, "blank_worksheet": fig_blank_worksheet,
    "totals": fig_totals, "closing_map": fig_closing_map,
}
