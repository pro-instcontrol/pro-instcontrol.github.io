# -*- coding: utf-8 -*-
"""Ingest D:/Process Control and Automation and D:/BCIT into the catalogue.

Both folders are on-theme instrument / control / automation material. Every
top-level directory becomes one work (all PDFs inside it are its documents);
every top-level .pdf becomes its own single-document work. Anything already in
the catalogue (by path) is skipped, so the script is idempotent and safe to
re-run.

Run, then upload the PDFs and rebuild:

    python build/add_pca_bcit.py
"""

import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from add_works import refresh  # noqa: E402
from pypdf import PdfReader  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAT = os.path.join(ROOT, "library", "catalog.json")

PCA = "D:/Process Control and Automation"
BCIT = "D:/BCIT"

# personal / administrative files that are not library material
SKIP_PERSONAL = re.compile(
    r"transcript|tuition|student card|receipt|payment|login|certificate|"
    r"declaration|code of conduct|backcheck|mybackcheck", re.I)

# files larger than this are not worth parsing for a page count
PAGE_CAP = 30 * 1048576


def doc_entry_fast(path, title):
    full = path.replace("/", os.sep)
    pages = 0
    try:
        if os.path.getsize(full) <= PAGE_CAP:
            pages = len(PdfReader(full).pages)
    except Exception:                         # noqa: BLE001 - metadata only
        pages = 0
    return {
        "path": path,
        "title": title,
        "pages": pages,
        "bytes": os.path.getsize(full),
        "copies": [],
        "head": "",
    }


def collect_pdfs(d):
    out = []
    for root, _dirs, files in os.walk(d.replace("/", os.sep)):
        for f in files:
            if f.lower().endswith(".pdf"):
                out.append(os.path.join(root, f).replace(os.sep, "/"))
    return out


def clean_title(name):
    base = name.rsplit(".", 1)[0]
    base = re.sub(r"^\d{10,13}\s+", "", base)        # drop leading ISBN
    base = re.sub(r"\s*[-\u2013\u2014]\s*$", "", base)  # trailing dash
    base = re.sub(r"\s+", " ", base).strip()
    return base or name


def domain_for(title):
    t = title.lower()
    if any(k in t for k in ("plc", "scada", "dcs", "network", "wiring",
                            "automation", "autocad", "robot", "fieldbus",
                            "ethernet", "samson", "siemens")):
        return "automation"
    if any(k in t for k in ("sensor", "measurement", "instrument", "flow",
                            "valve", "analyzer", "transmitter", "thermometer",
                            "pressure", "level", "temperature")):
        return "instruments"
    if any(k in t for k in ("control", "pid", "theory", "process", "feedback",
                            "loop", "safety", "boiler", "hazard", "power",
                            "sis", "functional")):
        return "process"
    return "instruments"


def norm_title(t):
    return re.sub(r"[^a-z0-9]", "", t.lower())


def desc(title):
    return (
        "%s \u2014 part of the instrument & control library's reference and "
        "teaching collection." % title,
        "%s \u2014 m\u1ed9t ph\u1ea7n b\u1ed9 s\u01b0u t\u1eadp t\u00e0i li\u1ec7u tham "
        "kh\u1ea3o v\u00e0 gi\u1ea3ng d\u1ea1y v\u1ec1 \u0111i\u1ec1u khi\u1ec3n thi\u1ebft b\u1ecb." % title,
    )


def make_entry(root, entry, is_bcit):
    full = os.path.join(root, entry)
    if os.path.isdir(full):
        pdfs = collect_pdfs(full)
        if not pdfs:
            return None
        title = ("BCIT \u2014 " + entry) if is_bcit else entry
        return title, sorted(pdfs)
    if entry.lower().endswith(".pdf"):
        if is_bcit and SKIP_PERSONAL.search(entry):
            return None
        return clean_title(entry), [full.replace(os.sep, "/")]
    return None


def main():
    cat = json.load(io.open(CAT, encoding="utf-8"))
    existing = {d["path"] for w in cat["works"] for d in (w.get("docs") or [])}
    seen = {norm_title(w["title"]) for w in cat["works"]}
    next_id = max(w["id"] for w in cat["works"])

    added = skipped = 0
    for root, is_bcit in ((PCA, False), (BCIT, True)):
        if not os.path.isdir(root.replace("/", os.sep)):
            print("missing root:", root)
            continue
        for entry in sorted(os.listdir(root.replace("/", os.sep))):
            res = make_entry(root, entry, is_bcit)
            if not res:
                continue
            title, pdfs = res
            if norm_title(title) in seen:
                skipped += 1
                continue
            docs = []
            for p in pdfs:
                if p in existing:
                    continue
                docs.append(doc_entry_fast(p, os.path.basename(p).rsplit(".", 1)[0]))
                existing.add(p)
            if not docs:
                skipped += 1
                continue
            work = {
                "id": next_id + 1,
                "title": title,
                "dir": root,
                "domain": "training" if is_bcit else domain_for(title),
                "why": 9,
                "docs": docs,
                "ndocs": 0, "pages": 0, "bytes": 0,
                "year": None, "copies": 0, "head": "",
                "desc": {"en": desc(title)[0], "vi": desc(title)[1]},
            }
            refresh(work)
            cat["works"].append(work)
            seen.add(norm_title(title))
            next_id += 1
            added += 1
            print("added work %d: %-55s %3d docs, %5d pages"
                  % (work["id"], title[:55], work["ndocs"], work["pages"]))

    cat["totals"]["works"] = len(cat["works"])
    io.open(CAT, "w", encoding="utf-8", newline="\n").write(
        json.dumps(cat, ensure_ascii=False, indent=1))
    print("catalogue now has %d works (+%d, skipped %d)"
          % (len(cat["works"]), added, skipped))


if __name__ == "__main__":
    main()
