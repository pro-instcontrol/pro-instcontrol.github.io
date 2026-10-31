# -*- coding: utf-8 -*-
"""Handbook Chapter 6 — Displacement Measurement, Linear and Angular.

167 pages / 63k words in the source, so it is published as a chapter landing
page plus one reader page per section (hb06_sNN.py).

Run:  python build/reader_hb_ch06.py            # landing + every section that exists
      python build/reader_hb_ch06.py 3          # one section only
"""
import importlib
import os
import sys

from hb06_common import (BASE_EN, BASE_VI, BYLINE, LANDING, SECTIONS, SLUG_OF,
                         TITLE_EN, TITLE_VI, nav, p)
from reader_handbook import SLUG, footer, head, header

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BLURB_VI = {
    1: "Chiết áp: cầu phân áp, độ tuyến tính, sai số do tải, mài mòn và cách lắp.",
    2: "LVDT, RVDT, biến áp từ trở, cảm biến dòng xoáy và che chắn nhiễu điện từ.",
    3: "Đo điện dung vi sai, cảm biến thông minh, áp suất, gia tốc, mức chất lỏng.",
    4: "Hiệu ứng áp điện: phương trình, vật liệu, cách đo và ứng dụng.",
    5: "Giao thoa kế Michelson với laser He–Ne và chiết suất không khí.",
    6: "Đo đường kính lỗ: nguyên lý, đầu đo, sai số và kỹ thuật thực hành.",
    7: "Siêu âm thời gian bay: xung, đầu dò, nhiễu và giới hạn độ phân giải.",
    8: "Mã hoá quang học tuyệt đối và gia số, lệch pha, nội suy và xử lý tín hiệu.",
    9: "Cảm biến từ trở, từ giảo, Hall và encoder từ — nguyên lý và giới hạn.",
    10: "Synchro và resolver: biến áp quay, chuyển đổi sang số và vòng servo.",
    11: "Cách tử Bragg trong sợi quang, Fabry–Perot ngoại và nội, so sánh bốn sơ đồ.",
    12: "Cảm biến vị trí quang điện (PSD) và đo độ lệch chùm tia.",
}
BLURB_EN = {
    1: "The potentiometer: voltage divider, linearity, loading error, wear and mounting.",
    2: "LVDT, RVDT, variable-reluctance and eddy-current sensors, and EMI shielding.",
    3: "Differential capacitance, smart sensors, pressure, accelerometers, level.",
    4: "Piezoelectricity: governing equations, materials, measurement, applications.",
    5: "Michelson interferometry with a He–Ne laser and the refractive index of air.",
    6: "Bore diameter measurement: principles, heads, errors and shop-floor practice.",
    7: "Time-of-flight ultrasound: pulses, transducers, noise and resolution limits.",
    8: "Absolute and incremental optical encoders, quadrature, interpolation, decoding.",
    9: "Magnetostrictive, magnetoresistive, Hall and magnetic encoder sensors.",
    10: "Synchros and resolvers: rotary transformers, R/D conversion, type II servo loops.",
    11: "Fiber Bragg gratings, extrinsic and intrinsic Fabry–Perot, four schemes compared.",
    12: "Position-sensitive detectors and the measurement of optical beam deflection.",
}


def landing(lang):
    vi = lang == "vi"
    other = (BASE_EN if vi else BASE_VI) + LANDING + "/"
    title = ("Chương 6 — Dịch chuyển: đo tuyến tính và góc · Sổ tay Đo lường, Thiết bị đo và Cảm biến" if vi
             else "Chapter 6 — Displacement Measurement, Linear and Angular · Measurement, Instrumentation "
                  "and Sensors Handbook")
    desc = ("Bản dịch tiếng Việt Chương 6 của Sổ tay Đo lường, Thiết bị đo và Cảm biến (CRC Press, 1999) — "
            "mười hai mục về cảm biến dịch chuyển, từ chiết áp đến giao thoa kế laser." if vi else
            "Chapter 6 of the CRC Measurement Handbook, published one section per page — twelve families of "
            "displacement sensor, with the full Vietnamese translation.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 6' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors Handbook</a> · '
             'Chapter 6' % BASE_EN)

    b = []
    b.append('<div class="note"><b>%s</b> %s</div>' % (
        "Vì sao chương này chia thành 12 trang." if vi else "Why this chapter is twelve pages.",
        ("Chương 6 dài 167 trang và khoảng 63.000 từ — gấp mười lần một chương thường. Để đọc được trên web, "
         "mỗi mục 6.1–6.12 được dịch và xuất bản thành một trang riêng, có điều hướng qua lại giữa các mục. "
         "Trang này là mục lục của chương." if vi else
         "Chapter 6 runs to 167 pages and about 63,000 words — ten times a normal chapter. To keep it readable "
         "on the web, each of sections 6.1–6.12 is translated and published as its own page, with previous / "
         "next navigation between them. This page is the chapter index.")))
    b.append(p(
        "Dịch chuyển là đại lượng gốc của phần lớn phép đo công nghiệp: vị trí van, hành trình piston, độ dày, "
        "độ rung, mức chất lỏng và góc trục đều quy về nó. Chương này đi qua mười hai họ cảm biến, từ chiết áp "
        "rẻ tiền đến giao thoa kế laser đếm từng nửa bước sóng, và với mỗi họ nêu rõ nguyên lý, giới hạn và "
        "cách chọn." if vi else
        "Displacement is the root quantity behind most industrial measurement: valve position, piston stroke, "
        "thickness, vibration, level and shaft angle all reduce to it. The chapter walks through twelve sensor "
        "families, from the cheap potentiometer to the laser interferometer that counts half wavelengths, and "
        "for each one states the principle, the limits and how to choose."))

    b.append('<h2>%s</h2>' % ("Mười hai mục" if vi else "The twelve sections"))
    rows = []
    for n, slug, tvi, ten in SECTIONS:
        rows.append(
            '<li class="done"><span class="n">6.%d</span>'
            '<a href="%s%s/"><span class="t">%s</span>'
            '<span class="d">%s</span></a></li>'
            % (n, BASE_VI if vi else BASE_EN, slug, tvi if vi else ten,
               (BLURB_VI if vi else BLURB_EN)[n]))
    b.append('<ul class="toc-list">%s</ul>' % "".join(rows))

    b.append('<h2>%s</h2>' % ("Cách đọc chương này" if vi else "How to read it"))
    b.append(p(
        "Mỗi trang mục giữ nguyên cách đánh số hình và công thức của bản gốc (Hình 6-1, công thức 6.1…), nên "
        "có thể đối chiếu trực tiếp với bản in. Trang tiếng Anh của mỗi mục là bản đồng hành: hình vẽ lại, "
        "bảng và phần bình luận, không phải bản dịch ngược." if vi else
        "Each section page keeps the original figure and equation numbering (Figure 6.1, Equation 6.1 …), so it "
        "can be checked against the printed book directly. The English page for each section is a companion — "
        "redrawn figures, tables and commentary — not a back-translation."))

    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Chương 5</span>Chuẩn đo lường</a>'
             '<a href="%sch07-thickness-measurement/" style="text-align:right;">'
             '<span class="k">Chương 7 →</span>Đo chiều dày</a></div>'
             % (BASE_VI, BASE_VI) if vi else
             '<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Chapter 5</span>Measurement Standards</a>'
             '<a href="%sch07-thickness-measurement/" style="text-align:right;">'
             '<span class="k">Chapter 7 →</span>Thickness Measurement</a></div>'
             % (BASE_EN, BASE_EN))

    body = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div></article></main>'
            % (crumb,
               "Dịch chuyển: đo tuyến tính và góc" if vi else "Displacement Measurement, Linear and Angular",
               "Keith Antonelli và cộng sự · 12 mục" if vi else "Keith Antonelli et al. · 12 sections",
               "Chương 6 · 167 trang gốc · 12 mục · 63.000 từ" if vi
               else "Chapter 6 · 167 source pages · 12 sections · 63,000 words",
               "".join(b)))
    return head(lang, title, desc) + header(lang, other) + body + footer(lang)


def build_section(num, lang):
    mod = importlib.import_module("hb06_s%02d" % num)
    body = mod.body_vi() if lang == "vi" else mod.body_en()
    figs = body.count('class="figure"')
    txt = body
    words = len("".join(c if c in " " else c for c in txt).split())
    from hb06_common import page
    return page(num, lang, body, figs, words)


def write(lang, path, html):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(html)
    print("wrote %s  %d kB" % (os.path.relpath(path, ROOT), len(html) // 1024))


def main():
    only = int(sys.argv[1]) if len(sys.argv) > 1 else None
    for lang in ("en", "vi"):
        base = os.path.join(ROOT, "books" if lang == "en" else os.path.join("vi", "books"),
                            "read", SLUG)
        if only is None:
            write(lang, os.path.join(base, LANDING, "index.html"), landing(lang))
        for num, slug, _tvi, _ten in SECTIONS:
            if only is not None and num != only:
                continue
            try:
                html = build_section(num, lang)
            except ImportError:
                print("  (section 6.%d not written yet — skipped)" % num)
                continue
            write(lang, os.path.join(base, slug, "index.html"), html)


if __name__ == "__main__":
    main()
