"""Add newly supplied material to the library catalogue.

Three jobs, applied in one pass so the site is regenerated only once:

1. Work 100 (Instrumentation and Sensors for the Food Industry) was catalogued as
   a single 868-page PDF with a messy filename-derived title. It is now described
   properly and gains the 28 chapter files, so each chapter can be read or
   downloaded on its own.
2. Two chapter files that were missing from the Process Engineering Equipment
   Handbook (work 149) are added to that work.
3. Two genuinely new works from D:/Ebooks are added: Vietnamese lecture notes on
   automatic control theory, and a process-control course pack (homework, MATLAB
   handouts, syllabus).

Run before uploading the PDFs and rebuilding the site:

    python build/add_works.py
"""

import io
import json
import os
import re

from pypdf import PdfReader

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAT = os.path.join(ROOT, "library", "catalog.json")

FOOD_DIR = "D:/Process Industries/Instrumentation and Sensors for the Food Industry (2nd Edition)"
FOOD_TITLES = [
    (1, "Instrumentation for food quality assurance"),
    (2, "Instrumental measurements and sensory parameters"),
    (3, "Principles of colour measurement for food"),
    (4, "Colour measurement of foods by colour reflectance"),
    (5, "Sorting by colour in the food industry"),
    (6, "Food compositional analysis using near infra-red absorption technology"),
    (7, "Practical aspects of infra-red remote thermometry"),
    (8, "In-line and off-line FTIR measurements"),
    (9, "Microwave measurements of product variables"),
    (10, "Pressure and temperature measurement in food process control"),
    (11, "Level and flow measurement in food process control"),
    (12, "Ultrasonic instrumentation in the food industry"),
    (13, "Ultrasound propagation in foods and ambient gases: principles and applications"),
    (14, "In-line and on-line rheology measurement"),
    (15, "Rheological measurements of foods"),
    (16, "Water activity and its measurement in food"),
    (17, "Conductance/impedance techniques for microbial assay"),
    (18, "Modern methods of texture measurement"),
    (19, "Sensors for food flavour and freshness: electronic noses, tongues and testers"),
    (20, "Chemosensors, biosensors, immunosensors and DNA probes: the base devices"),
    (21, "Biosensors for process monitoring and quality assurance in the food industry"),
    (22, "Commercial devices based on biosensors"),
    (23, "New biosensors"),
]
FOOD_OTHER = {
    "fm": "Front matter",
    "pref": "Preface",
    "toc": "Table of contents",
    "app": "Part IV · Appendices",
    "indx": "Index",
}

HBN_DIR = "D:/Ebooks/Process Control and Automation/Process Engineering Equipment Handbook"

VI_DIR = "D:/Ebooks/Process Control Training/Control Theory"
VI_CHAPTERS = [
    (1, "Chương 1 · Phần tử và hệ thống điều khiển tự động"),
    (2, "Chương 2 · Mô tả toán học hệ thống điều khiển liên tục"),
    (3, "Chương 3 · Đánh giá tính ổn định của hệ thống"),
    (4, "Chương 4 · Chất lượng của hệ thống điều khiển"),
    (5, "Chương 5 · Thiết kế hệ thống điều khiển liên tục"),
    (6, "Chương 6 · Mô tả toán học hệ thống điều khiển rời rạc"),
    (7, "Chương 7 · Phân tích và thiết kế hệ thống điều khiển rời rạc"),
    (8, "Chương 8 · Hệ thống điều khiển phi tuyến"),
]

COURSE_DIR = "D:/Ebooks/Process Control Training"
COURSE_DOCS = [
    ("CMPE293_syllabus.pdf", "Course syllabus (CMPE 293)"),
    ("MATLAB.pdf", "MATLAB primer"),
    ("matlabhandout.pdf", "MATLAB handout"),
] + [("Homework_%d.pdf" % n, "Homework %d" % n) for n in range(1, 10)] + [
    ("Homework_1_pages.pdf", "Homework 1 · worked pages"),
] + [("Homework_%d_answers.pdf" % n, "Homework %d · answers" % n)
     for n in (2, 3, 4, 5)]


def doc_entry(path, title):
    full = path.replace("/", os.sep)
    pages = 0
    head = ""
    try:
        reader = PdfReader(full)
        pages = len(reader.pages)
        head = re.sub(r"\s+", " ", reader.pages[0].extract_text() or "")[:400]
    except Exception as exc:                       # noqa: BLE001 - metadata only
        print("  ! could not read %s: %s" % (os.path.basename(path), exc))
    return {
        "path": path,
        "title": title,
        "pages": pages,
        "bytes": os.path.getsize(full),
        "copies": [],
        "head": head,
    }


def refresh(work):
    work["ndocs"] = len(work["docs"])
    work["pages"] = sum(d.get("pages") or 0 for d in work["docs"])
    work["bytes"] = sum(d.get("bytes") or 0 for d in work["docs"])
    work["head"] = work["docs"][0].get("head", "") if work["docs"] else ""
    return work


def food_docs():
    docs = []
    # keep the original single-file copy so the whole book is one download
    whole = ("D:/Process Control and Automation/0226.Instrumentation and Sensors for the "
             "Food Industry Second Edition by Erika Kress-Rogers.pdf")
    if os.path.exists(whole):
        docs.append(doc_entry(whole, "Complete book (single file)"))
    for n, title in FOOD_TITLES:
        docs.append(doc_entry("%s/35601_%02d.pdf" % (FOOD_DIR, n),
                              "Ch %d · %s" % (n, title)))
    for key in ("fm", "pref", "toc", "app", "indx"):
        docs.append(doc_entry("%s/35601_%s.pdf" % (FOOD_DIR, key), FOOD_OTHER[key]))
    return docs


def upsert(cat, title, build):
    """Update the work with this title in place, or append a new one.

    Keeps ids stable across re-runs so /books/work/<id>/ links never break.
    """
    for work in cat["works"]:
        if work["title"] == title:
            build(work)
            refresh(work)
            print("updated work %d: %s (%d docs, %d pages)"
                  % (work["id"], title, work["ndocs"], work["pages"]))
            return work
    work = {"id": max(w["id"] for w in cat["works"]) + 1, "title": title,
            "dir": "", "domain": "training", "why": 6, "docs": [],
            "ndocs": 0, "pages": 0, "bytes": 0, "year": None, "copies": 0, "head": ""}
    build(work)
    refresh(work)
    cat["works"].append(work)
    print("added work %d: %s (%d docs, %d pages)"
          % (work["id"], title, work["ndocs"], work["pages"]))
    return work


def main():
    cat = json.load(io.open(CAT, encoding="utf-8"))
    by_id = {w["id"]: w for w in cat["works"]}

    # ---- 1. Food Industry: proper title, year and per-chapter files ----------
    food = by_id[100]
    print("updating work 100:", food["title"])
    food["title"] = "Instrumentation and Sensors for the Food Industry (2nd Edition)"
    food["dir"] = FOOD_DIR
    food["domain"] = "instruments"
    food["why"] = 9
    food["year"] = 2001
    food["docs"] = food_docs()
    refresh(food)
    # the whole-book file duplicates the chapters, so count the book once
    food["pages"] = sum(d["pages"] for d in food["docs"]
                        if d["title"] != "Complete book (single file)")
    print("  docs:", food["ndocs"], "| pages:", food["pages"])

    # ---- 2. Two missing chapters of the Process Engineering Equipment Handbook
    hb = by_id[149]
    existing = {d["path"].rsplit("/", 1)[-1].lower() for d in hb["docs"]}
    added = 0
    for name in ("9614x_01b.pdf", "9614x_03a.pdf"):
        if name.lower() in existing:
            continue
        hb["docs"].append(doc_entry("%s/%s" % (HBN_DIR, name), name.rsplit(".", 1)[0]))
        added += 1
    hb["docs"].sort(key=lambda d: d["path"].lower())
    refresh(hb)
    print("work 149: +%d chapters -> %d docs, %d pages" % (added, hb["ndocs"], hb["pages"]))

    # ---- 3a. Vietnamese automatic control theory lecture notes ---------------
    def fill_vi(w):
        w["dir"] = VI_DIR
        w["domain"] = "training"
        w["why"] = 8
        w["docs"] = [doc_entry("%s/Chuong%d_LTDKTD.pdf" % (VI_DIR, n), title)
                     for n, title in VI_CHAPTERS]

    upsert(cat, "Automatic Control Theory — Vietnamese lecture notes (HCMUT, 2006)", fill_vi)

    # ---- 3b. Process control course pack ------------------------------------
    def fill_course(w):
        w["dir"] = COURSE_DIR
        w["domain"] = "training"
        w["why"] = 6
        docs = []
        for name, title in COURSE_DOCS:
            path = "%s/%s" % (COURSE_DIR, name)
            if os.path.exists(path.replace("/", os.sep)):
                docs.append(doc_entry(path, title))
        w["docs"] = docs

    upsert(cat, "Process Control course pack — homework, MATLAB handouts and syllabus",
           fill_course)


    cat["root"] = "D:/Process Control and Automation"
    cat["totals"]["works"] = len(cat["works"])
    io.open(CAT, "w", encoding="utf-8", newline="\n").write(
        json.dumps(cat, ensure_ascii=False, indent=1))
    print("catalogue now has %d works" % len(cat["works"]))


if __name__ == "__main__":
    main()
