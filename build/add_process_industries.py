# -*- coding: utf-8 -*-
"""Ingest the books in D:/Process Industries into the library catalogue.

Six works are genuinely new; two already exist and only need the Process
Industries copy present:
  * work 100  Instrumentation and Sensors for the Food Industry (already points
              at D:/Process Industries) — nothing to add.
  * work 149  Process Engineering Equipment Handbook (chapters from D:/Ebooks) —
              append the single-file Process Industries PDF so that copy is
              downloadable too.

Run, then upload the PDFs and rebuild:

    python build/add_process_industries.py
"""

import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_works import doc_entry, refresh, upsert  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAT = os.path.join(ROOT, "library", "catalog.json")
PI = "D:/Process Industries"

SPECIAL = {
    "fm": "Front matter", "toc": "Table of contents",
    "indx": "Index", "ind": "Index",
    "glos": "Glossary", "gl": "Glossary",
    "acro": "Acronyms", "acr": "Acronyms",
    "symb": "Symbols", "pref": "Preface", "fore": "Foreword",
    "app": "Appendices", "appa": "Appendix A", "appb": "Appendix B",
    "appc": "Appendix C", "appd": "Appendix D",
    "asq": "Appendix \u00b7 ASQ food sanitation",
}

# ordering: front matter first, chapters next, back matter last
FRONT = {"fm", "toc", "pref", "fore"}
BACK = {"indx", "ind", "glos", "gl", "acro", "acr", "symb",
        "app", "appa", "appb", "appc", "appd", "asq"}


def suffix(fn):
    return fn.rsplit(".", 1)[0].rsplit("_", 1)[-1].lower()


def doc_title(fn):
    base = fn.rsplit(".", 1)[0]
    m = re.search(r"_(\d+)$", base)
    if m:
        return "Chapter %d" % int(m.group(1))
    return SPECIAL.get(suffix(fn), suffix(fn).capitalize())


def sort_key(fn):
    s = suffix(fn)
    if s in FRONT:
        return (0, {"fm": 0, "toc": 1, "pref": 2, "fore": 3}.get(s, 4), 0)
    m = re.search(r"_(\d+)\.pdf$", fn, re.I)
    if m:
        return (1, int(m.group(1)), 0)
    if s in BACK:
        return (2, 0, fn.lower())
    return (1, 9999, fn.lower())


def folder_docs(d):
    files = [f for f in os.listdir(d.replace("/", os.sep))
             if f.lower().endswith(".pdf")]
    files.sort(key=sort_key)
    return [doc_entry("%s/%s" % (d, f), doc_title(f)) for f in files]


def single(path, title="Complete book (single file)"):
    return [doc_entry(path, title)]


NEW_WORKS = [
    dict(
        title="Handbook for Plant Process Engineer",
        dir=PI, domain="process", year=2010, why=7,
        docs=lambda: single(PI + "/Handbook for Plant Process Engineer.pdf"),
        desc=(
            "A plant-floor handbook for the process engineer: equipment, materials, "
            "piping, instrumentation and the day-to-day problems of keeping a process "
            "running. Practical rather than theoretical.",
            "Sổ tay hiện trường cho kỹ sư quá trình: thiết bị, vật liệu, đường ống, "
            "thiết bị đo và những vấn đề hằng ngày để giữ một quá trình vận hành. "
            "Thực dụng hơn là lý thuyết."),
    ),
    dict(
        title="Process Management",
        dir=PI, domain="process", year=None, why=6,
        docs=lambda: single(PI + "/Process_Management.pdf"),
        desc=(
            "A management-side view of running a process plant — organisation, "
            "planning, quality and the human systems around the equipment.",
            "Góc nhìn quản lý về vận hành nhà máy quá trình — tổ chức, lập kế hoạch, "
            "chất lượng và các hệ thống con người quanh thiết bị."),
    ),
    dict(
        title="Essentials of Food Sanitation",
        dir=PI + "/Essentials of Food Sanitation", domain="safety", year=1998, why=6,
        docs=lambda: folder_docs(PI + "/Essentials of Food Sanitation"),
        desc=(
            "A working text on food sanitation: microbiology, cleaning and sanitising, "
            "HACCP pre-requisites and the hygiene practice that keeps a food plant safe.",
            "Giáo trình thực hành về vệ sinh thực phẩm: vi sinh, làm sạch và khử trùng, "
            "các tiên quyết HACCP và thực hành vệ sinh giữ cho nhà máy thực phẩm an toàn."),
    ),
    dict(
        title="Food Processing Technology \u2014 Principles and Practice (2nd Edition)",
        dir=PI + "/Food Processing Technology - Principles and Practice (2nd Edition)",
        domain="process", year=2000, why=7,
        docs=lambda: folder_docs(
            PI + "/Food Processing Technology - Principles and Practice (2nd Edition)"),
        desc=(
            "Fellows' standard text on food processing: the unit operations — heat, "
            "freezing, drying, separation — and the equipment and control behind each.",
            "Giáo trình chuẩn của Fellows về chế biến thực phẩm: các quá trình đơn vị — "
            "gia nhiệt, làm lạnh, sấy, tách — cùng thiết bị và điều khiển đằng sau mỗi quá trình."),
    ),
    dict(
        title="Industrial Hygiene Handbook",
        dir=PI + "/Industrial Hygene Handbook", domain="safety", year=None, why=6,
        docs=lambda: folder_docs(PI + "/Industrial Hygene Handbook"),
        desc=(
            "A reference on industrial hygiene: exposure, ventilation, noise, dust and "
            "chemical hazards, and the monitoring that keeps a plant within limits.",
            "Sách tham khảo về vệ sinh công nghiệp: phơi nhiễm, thông gió, tiếng ồn, bụi "
            "và mối nguy hóa chất, cùng việc quan trắc giữ nhà máy trong giới hạn."),
    ),
    dict(
        title="Making the Most of HACCP \u2014 Learning from Others' Experience",
        dir=PI + "/Making the Most of HACCP - Learning from Others' Experience",
        domain="safety", year=2000, why=6,
        docs=lambda: folder_docs(
            PI + "/Making the Most of HACCP - Learning from Others' Experience"),
        desc=(
            "Case-based lessons on putting HACCP into practice — what worked, what failed, "
            "and why food-safety plans live or die on the plant floor.",
            "Bài học từ tình huống thực tế khi áp dụng HACCP — điều gì hiệu quả, điều gì "
            "thất bại, và vì sao kế hoạch an toàn thực phẩm sống hay chết ở sàn nhà máy."),
    ),
]


def main():
    cat = json.load(io.open(CAT, encoding="utf-8"))

    # 1. the six new works
    for spec in NEW_WORKS:
        def fill(w, spec=spec):
            w["dir"] = spec["dir"]
            w["domain"] = spec["domain"]
            w["year"] = spec["year"]
            w["why"] = spec["why"]
            w["desc"] = {"en": spec["desc"][0], "vi": spec["desc"][1]}
            w["docs"] = spec["docs"]()
        upsert(cat, spec["title"], fill)

    # 2. work 149: add the Process Industries single-file copy if missing
    hb = next(w for w in cat["works"]
              if w["title"] == "Process Engineering Equipment Handbook")
    single_path = PI + "/ProcessEngineering EquipmentHandbook.pdf"
    have = {d["path"] for d in hb["docs"]}
    if single_path not in have and os.path.exists(single_path.replace("/", os.sep)):
        hb["docs"].append(doc_entry(single_path,
                                    "Complete book (single file \u00b7 Process Industries copy)"))
        refresh(hb)
        print("work 149: appended Process Industries single file -> %d docs"
              % hb["ndocs"])
    else:
        print("work 149: Process Industries single file already present")

    cat["totals"]["works"] = len(cat["works"])
    io.open(CAT, "w", encoding="utf-8", newline="\n").write(
        json.dumps(cat, ensure_ascii=False, indent=1))
    print("catalogue now has %d works" % len(cat["works"]))


if __name__ == "__main__":
    main()
