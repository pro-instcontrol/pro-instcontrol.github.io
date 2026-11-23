# -*- coding: utf-8 -*-
"""Vector figures for Chapter 11 "Sustainability" of Emerson,
*Control Valve Handbook*, 6th ed. (2020), printed pp. 240-249.

Three faithful vector redrawings ``fig_f11_01`` ... ``fig_f11_03``. Each
function is registered with :func:`_reg` and returns the standard 5-tuple
``(svg, caption_vi, caption_en, aria_vi, aria_en)`` through :func:`_finish`.
All text goes through :func:`T` / :func:`esc` so no bare ampersand can reach
an SVG attribute. The chapter has no numeric figure data; the Scope diagram
and the two bullet charts are conceptual redrawings of the printed material.
"""
from cvh6fig import (_reg, _finish, esc, T, _defs, _rect, _line, _circle,
                     _poly, _arrow, svg, INK, GREY, BLUE, RED, GREEN)
# GOLD / FILL / PAPER live in `vfig`, not re-exported by `cvh6fig`.
from vfig import GOLD, FILL, PAPER  # noqa: F401


def _wrap(s, limit):
    """Break a label into lines of at most `limit` characters."""
    out, cur = [], ""
    for wd in str(s).split():
        if cur and len(cur) + 1 + len(wd) > limit:
            out.append(cur)
            cur = wd
        else:
            cur = (cur + " " + wd).strip()
    if cur:
        out.append(cur)
    return out


def _band(o, x, y, w, h, vi, en, fill="#e9eef4", color=INK):
    """A bilingual heading band."""
    o.append(_rect(x, y, w, h, fill=fill, sw=1.0))
    o.append(T(x + w / 2.0, y + h / 2.0 - 1, vi, 8.0, weight="600",
               color=color))
    o.append(T(x + w / 2.0, y + h / 2.0 + 10, en, 7.0, color=GREY))


def _bullets(o, x, y, items, limit_vi=38, limit_en=42, size_vi=6.8,
             size_en=6.4, gap=6):
    """Compact bilingual bullet column; returns the next free y coordinate."""
    yy = y
    for vi, en in items:
        o.append(_circle(x + 4, yy + 3, 1.5, fill=BLUE, sw=0))
        for ln in _wrap(vi, limit_vi):
            o.append(T(x + 12, yy, ln, size_vi, anchor="start"))
            yy += size_vi + 3.4
        for ln in _wrap(en, limit_en):
            o.append(T(x + 12, yy, ln, size_en, anchor="start", color=GREY))
            yy += size_en + 3.0
        yy += gap
    return yy


# ---------------------------------------------------------------------------
# Figure 11.1 - Greenhouse Gas (printed p. 243)
# ---------------------------------------------------------------------------
def _scope_panel(o, x, y, title, fill, color, desc, examples):
    """One Scope block: heading, definition pair and an example strip."""
    w, h = 196, 204
    o.append(_rect(x, y, w, h, fill="#ffffff", sw=1.2))
    o.append(_rect(x, y, w, 28, fill=fill, sw=1.0))
    o.append(T(x + w / 2.0, y + 18, title, 8.4, weight="600", color=color))
    yy = y + 44
    for vi, en in desc:
        o.append(T(x + w / 2.0, yy, vi, 7.2, weight="600"))
        o.append(T(x + w / 2.0, yy + 12, en, 7.0, color=GREY))
        yy += 28
    ey = y + 130
    o.append(_rect(x + 8, ey, w - 16, 66, fill="#f8fafc", sw=0.8))
    o.append(T(x + w / 2.0, ey + 13, "Ví dụ / Example", 7.2,
               weight="600", color=color))
    yy2 = ey + 28
    for vi, en in examples:
        o.append(T(x + w / 2.0, yy2, vi, 7.0))
        o.append(T(x + w / 2.0, yy2 + 11, en, 6.8, color=GREY))
        yy2 += 26
    return w


@_reg
def fig_f11_01():
    """Figure 11.1 (p. 243) - The three GHG protocol emission scopes."""
    w, h = 680, 350
    o = [_defs()]
    o.append(T(340, 28, "Khí nhà kính / Greenhouse Gas", 9.2, weight="600"))
    o.append(T(340, 47,
               "Giao thức khí nhà kính phân loại phát thải thành ba phạm vi / "
               "The GHG protocol groups emissions into three scopes",
               7.2, color=GREY))
    panels = [
        ("PHẠM VI 1 · SCOPE 1", "#e7f0fb", BLUE,
         [("Phát thải trực tiếp", "Direct emissions"),
          ("từ nguồn thuộc sở hữu", "from owned or controlled"),
          ("hoặc kiểm soát", "sources")],
         [("sưởi ấm văn phòng", "office comfort heating"),
          ("sản xuất tại nhà máy", "manufacturing sites")]),
        ("PHẠM VI 2 · SCOPE 2", "#eef7ee", GREEN,
         [("Phát thải gián tiếp", "Indirect emissions"),
          ("từ sản xuất điện năng", "from the generation of"),
          ("điện đã mua", "purchased electricity")],
         [("than hoặc khí đốt", "coal or natural gas"),
          ("tại điểm phát điện", "at the point of generation")]),
        ("PHẠM VI 3 · SCOPE 3", "#fdf3e6", GOLD,
         [("Mọi phát thải gián tiếp", "All other indirect"),
          ("khác trong chuỗi giá trị", "emissions in the value chain"),
          ("gồm 15 danh mục", "15 categories")],
         [("hàng mua, đi công tác", "purchased goods, business travel"),
          ("sản phẩm bán ra", "use of sold products")]),
    ]
    for i, (title, fill, color, desc, examples) in enumerate(panels):
        _scope_panel(o, 20 + i * 222, 66, title, fill, color, desc, examples)
    for i in (0, 1):
        ax = 20 + i * 222 + 200
        o.append(_arrow(ax, 168, ax + 18, 168, sw=1.6, color=GREY))
    o.append(T(340, 290,
               "Phạm vi 1 đến 3: từ nguồn trực tiếp đến toàn bộ chuỗi giá trị / "
               "Scope 1 to 3: from direct sources to the full value chain",
               7.2, weight="600"))
    o.append(T(340, 306,
               "Sơ đồ khái niệm theo mục 11.6 · nguồn không nêu số liệu / "
               "Conceptual diagram per section 11.6 · the source gives no numeric data",
               7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 11.1 (p. 243) - Greenhouse Gas",
                   "Hình 11.1 (tr. 243) · Khí nhà kính / "
                   "Figure 11.1 (p. 243) - Greenhouse Gas",
                   "Hình 11.1 (tr. 243) · Khí nhà kính · Ba phạm vi phát thải theo giao thức khí nhà "
                   "kính: Phạm vi 1 là phát thải trực tiếp từ nguồn sở hữu hoặc kiểm soát, Phạm vi 2 "
                   "là phát thải gián tiếp từ sản xuất điện năng đã mua, Phạm vi 3 là mọi phát thải "
                   "gián tiếp khác trong chuỗi giá trị, gồm 15 danh mục.",
                   "Figure 11.1 (p. 243) - Greenhouse Gas · The three emission scopes of the GHG "
                   "protocol: Scope 1 direct emissions from owned or controlled sources, Scope 2 "
                   "indirect emissions from the generation of purchased electricity, and Scope 3 "
                   "all other indirect emissions in the value chain, in 15 categories.",
                   "Sơ đồ Hình 11.1 (tr. 243) ba phạm vi phát thải khí nhà kính",
                   "Diagram of Figure 11.1 (p. 243) the three greenhouse gas emission scopes")


# ---------------------------------------------------------------------------
# Figure 11.2 - Sustainability and Decarbonization (printed p. 245)
# ---------------------------------------------------------------------------
@_reg
def fig_f11_02():
    """Figure 11.2 (p. 245) - The listed technologies grouped in three streams."""
    w, h = 680, 410
    o = [_defs()]
    o.append(T(340, 28,
               "Bền vững và phi carbon hóa / Sustainability and Decarbonization",
               9.0, weight="600"))
    o.append(T(340, 47,
               "Công nghệ mới và mới nổi theo mục 11.7 / New and emerging technologies "
               "listed in section 11.7",
               7.2, color=GREY))
    cols = [
        (20, "SINH HỌC VÀ TUẦN HOÀN", "Bio and Circular", "#eef7ee", GREEN, [
            ("Giảm phát thải khí nhà kính",
             "Greenhouse gas emissions reduction"),
            ("Nhiên liệu sinh học, năng lượng sinh học, rác thải thành năng lượng",
             "Bio fuel / bio energy / waste to energy"),
            ("Nhiên liệu tái tạo, diesel bền vững: SAF",
             "Renewable fuel - sustainable diesel: SAF"),
            ("Nhựa sinh học", "Bio plastics"),
            ("Tái chế nhựa", "Plastic recycling"),
            ("Nhựa phân hủy sinh học", "Biodegradable plastics"),
            ("Khí sinh học, khí đốt tái tạo", "Biogas - renewable natural gas"),
        ]),
        (242, "NĂNG LƯỢNG TÁI TẠO", "Renewable Energy", "#e7f0fb", BLUE, [
            ("Sản xuất điện mặt trời, chuỗi giá trị polysilicon",
             "Solar - polysilicon value chain"),
            ("Trang trại gió ngoài khơi", "Offshore wind farms"),
            ("Địa nhiệt", "Geothermal"),
        ]),
        (464, "VẬT LIỆU VÀ ĐIỆN HÓA", "Materials and Electrification", "#fdf3e6",
         GOLD, [
             ("Khai thác lithium và nickel", "Lithium and nickel mining"),
             ("Chế biến kim loại pin", "Battery metal processing"),
             ("Tái chế pin", "Battery recycling"),
             ("Điện hóa bộ truyền động", "Actuator electrification"),
             ("Bể chứa muối nóng chảy", "Molten salt reservoirs"),
         ]),
    ]
    for x, vi, en, fill, color, items in cols:
        o.append(_rect(x, 64, 196, 410 - 64 - 58, fill="#ffffff", sw=1.1))
        _band(o, x, 64, 196, 36, vi, en, fill=fill, color=color)
        _bullets(o, x + 8, 112, items, limit_vi=36, limit_en=40,
                 size_vi=6.9, size_en=6.5, gap=7)
    o.append(T(340, 366,
               "15 mục theo bản in, gộp thành ba nhóm để dễ đọc / "
               "15 printed items grouped into three streams for legibility",
               7.2, weight="600"))
    o.append(T(340, 382,
               "Hình trong bản in là danh sách bullet · vẽ lại dạng vector / "
               "The printed figure is a bullet list · redrawn as a vector",
               7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 11.2 (p. 245) - Sustainability and Decarbonization",
                   "Hình 11.2 (tr. 245) · Bền vững và phi carbon hóa / "
                   "Figure 11.2 (p. 245) - Sustainability and Decarbonization",
                   "Hình 11.2 (tr. 245) · Bền vững và phi carbon hóa · 15 mục công nghệ và giải pháp "
                   "trong bản in được gộp thành ba nhóm: sinh học và tuần hoàn, năng lượng tái tạo, "
                   "vật liệu và điện hóa, từ giảm phát thải đến tái chế pin và điện hóa bộ truyền động.",
                   "Figure 11.2 (p. 245) - Sustainability and Decarbonization · The 15 printed "
                   "technology and solution items grouped into three streams: bio and circular, "
                   "renewable energy, and materials and electrification, from emissions reduction "
                   "to battery recycling and actuator electrification.",
                   "Biểu đồ Hình 11.2 (tr. 245) ba nhóm công nghệ bền vững",
                   "Chart of Figure 11.2 (p. 245) three groups of sustainability technologies")


# ---------------------------------------------------------------------------
# Figure 11.3 - ESG Approach by Different Industries (printed p. 246)
# ---------------------------------------------------------------------------
@_reg
def fig_f11_03():
    """Figure 11.3 (p. 246) - Environmental, Social and Governance bullets."""
    w, h = 680, 480
    o = [_defs()]
    o.append(T(340, 28,
               "Tiếp cận ESG theo các ngành công nghiệp / "
               "ESG Approach by Different Industries",
               8.8, weight="600"))
    o.append(T(340, 47, "Theo Hình 11.3 trong bản in / As printed in Figure 11.3",
               7.2, color=GREY))
    cols = [
        (20, "MÔI TRƯỜNG", "Environmental", "#eef7ee", GREEN, [
            ("Giảm phát thải khí nhà kính",
             "Reducing greenhouse gas emissions"),
            ("Theo dõi dấu vết môi trường", "Tracking environmental footprint"),
            ("Phi carbon hóa nguồn năng lượng, hỗ trợ cam kết carbon thấp",
             "Energy source decarbonization: supporting low carbon commitments"),
            ("Quản lý phát thải", "Emissions management"),
            ("Hợp tác với các trường đại học trên thế giới",
             "Collaboration with universities around the world"),
            ("Bảo vệ chất lượng thực phẩm và tính bền vững môi trường",
             "Protecting food quality and environmental sustainability"),
        ]),
        (242, "XÃ HỘI", "Social", "#e7f0fb", BLUE, [
            ("Thúc đẩy an toàn và an ninh", "Enabling safety and security"),
            ("An toàn nơi làm việc", "Workplace safety"),
            ("Đa dạng, công bằng và hòa nhập",
             "Diversity, Equity, and Inclusion"),
            ("Giáo dục khoa học, công nghệ, kỹ thuật và toán học (STEM)",
             "Science, technology, engineering, and mathematics education (STEM)"),
            ("Gắn kết nhân viên", "Employee engagement"),
            ("Đào tạo và phát triển", "Training and development"),
            ("Đào tạo cho nơi làm việc tương lai",
             "Training the workplace of the future"),
            ("Thúc đẩy tương lai của cộng đồng",
             "Advancing the future of communities"),
        ]),
        (464, "QUẢN TRỊ", "Governance", "#fdf3e6", GOLD, [
            ("Cơ cấu và tính đa dạng của hội đồng quản trị",
             "Board diversity and structure"),
            ("Hành động quản trị doanh nghiệp", "Corporate governance actions"),
            ("Quản lý rủi ro và giám sát", "Risk management and oversight"),
            ("Chính trực và đạo đức", "Integrity and ethics"),
        ]),
    ]
    for x, vi, en, fill, color, items in cols:
        o.append(_rect(x, 64, 196, 480 - 64 - 64, fill="#ffffff", sw=1.1))
        _band(o, x, 64, 196, 34, vi, en, fill=fill, color=color)
        _bullets(o, x + 8, 110, items, limit_vi=36, limit_en=40,
                 size_vi=6.6, size_en=6.2, gap=5)
    o.append(T(340, 438,
               "Số mục theo bản in: Môi trường 6, Xã hội 8, Quản trị 4 / "
               "Printed bullet counts: Environmental 6, Social 8, Governance 4",
               7.2, weight="600"))
    o.append(T(340, 454,
               "Ba cột ESG được giữ nguyên nội dung và thứ tự / "
               "The three ESG columns keep the source wording and order",
               7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 11.3 (p. 246) - ESG Approach by Different Industries",
                   "Hình 11.3 (tr. 246) · Tiếp cận ESG theo các ngành công nghiệp / "
                   "Figure 11.3 (p. 246) - ESG Approach by Different Industries",
                   "Hình 11.3 (tr. 246) · Tiếp cận ESG theo các ngành công nghiệp · Ba cột Môi trường "
                   "(6 mục), Xã hội (8 mục) và Quản trị (4 mục) được sao chép đầy đủ từ bản in, từ "
                   "giảm phát thải khí nhà kính đến đạo đức kinh doanh.",
                   "Figure 11.3 (p. 246) - ESG Approach by Different Industries · Three columns, "
                   "Environmental (6 items), Social (8 items) and Governance (4 items), reproduced "
                   "in full from the print, from reducing greenhouse gas emissions to integrity "
                   "and ethics.",
                   "Biểu đồ Hình 11.3 (tr. 246) ba cột ESG",
                   "Chart of Figure 11.3 (p. 246) the three ESG columns")


# Per-chapter registry view for the validation harness. ``_reg`` registers
# into cvh6fig.FIGS; this filtered alias exposes only this chapter's three
# figures without duplicating or moving any shared state.
import cvh6fig as _cvh6fig  # noqa: E402
FIGS = {k: v for k, v in _cvh6fig.FIGS.items() if k.startswith("fig_f11_")}
