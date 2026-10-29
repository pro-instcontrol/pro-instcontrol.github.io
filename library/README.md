# Process Control & Automation Library — knowledge base

An index of the material in `G:\Process Control and Automation`, built by reading every
file rather than trusting the folder names.

**Open `index.html`.** It is self-contained — no server, no internet, no dependencies.
Double-click it, or drag it into a browser.

---

## What is in the folder

| | |
|---|--:|
| Works (books, standards, courses, magazine runs) | **194** |
| Documents (unique PDFs) | **583** |
| Pages | **36,531** |
| Files of all types | **2,683** |
| Size on disk | **2.11 GB** |
| Byte-identical duplicate copies | **545 MB** |

The 583 documents come from 808 PDF files — **225 of them are exact duplicates**, the
same book stored twice under slightly different names. Deduplication is by full MD5,
so these are genuinely identical files, not merely similar titles.

## The four tabs

**Catalogue** — every work, searchable and filterable. Search covers titles, chapter
file names, folder paths and the first page of text, so searching `shinskey` or
`orifice` finds things whose filenames never mention them. Click a row to expand its
file list; the button beside each file copies its full Windows path.

**Reading paths** — eight ordered sequences (measurement → control theory → process
control → final elements → systems → safety → power plant), each resolved against works
that are actually in the library, with page counts.

**File inventory** — everything by extension, including the 2,100 non-PDF files.

**Duplicates** — each redundant copy with the space it wastes.

---

## What the inventory found

1. **The library is bigger than it looks, and smaller than it looks.** 808 PDFs, but
   only 583 distinct documents. A third of the apparent volume is duplication.

2. **Most "books" are chapter-split.** `A Guide to the Automation Body of Knowledge` is
   42 files, `The Measurement, Instrumentation and Sensors Handbook` is 117, the
   SIS book is 19. Counting files would have reported 194 works as ~500. The catalogue
   groups them, so a work reads as one entry with a chapter count.

3. **≈545 MB is recoverable** by deleting duplicate copies. The largest single waste is
   `Automatic Control Systems 9th Edition.pdf` at 117 MB, stored twice.

4. **305 SWF files are dead weight.** They are the animation layer of the French
   `FORMATION-BASE` / `FORMATION-ADVANCED` PLC courses, and Flash no longer runs in any
   current browser. The surrounding HTML pages survive; the animations do not.

5. **114 `.bc!` files (43 MB) are abandoned BitTorrent downloads** — incomplete, unopenable,
   and safe to delete. Same for 3 `.dl_` partial downloads.

6. **Some material is out of scope.** The `Electronic Reconnaissance and Warface Systems`
   folder is Russian-language military equipment documentation, unrelated to process
   control. It is catalogued and marked `Unclassified` rather than silently dropped.

7. **A real safety gap in the collection**: only three works cover functional safety
   (the SIS design book, an Ex protection primer, and a VTT thesis on inherent safety),
   against 33 on instrumentation and 28 on PLCs. For anyone working toward SIL-rated
   loops, that is the thin area.

8. **A quarter of the catalogue is one Spanish university programme.** 47 of the 194 works
   are UOC course material — analytical chemistry, PLC programming, industrial
   automation, interference — filed under `Instrumentation and Control`. It is genuine
   teaching material, but it is coursework, not reference literature.

---

## How it was built

Three passes, each in `../kb/`:

| Script | What it does |
|---|---|
| `scan.py` | Walks the folder, MD5-hashes every PDF, groups duplicates, reads page count, metadata and the first three pages of text from each unique document. |
| `build_model.py` | Collapses chapter-split files into works, derives a readable title, and classifies each work into one of 21 domains by weighted keyword scoring plus an explicit override list. |
| `render.py` | Emits `index.html` (data embedded), `LIBRARY.md`, `INVENTORY.md` and `catalog.json`. |

Rebuild after adding material:

```
python kb/scan.py && python kb/build_model.py && python kb/render.py
```

`catalog.json` is the machine-readable index — every work, its documents, pages, size,
domain and duplicate copies.

## How classification actually works

Titles and domains are inferred, not hand-entered, so the method matters:

- **Works, not files.** A folder whose files are mostly chapter or front-matter parts
  (`Ch01.pdf`, `1811_03.pdf`, `9614x_01a.pdf`, `DC-04 Ch01 ver3`) is one work. A folder
  holding genuinely separate publications stays separate.
- **Titles** come from the folder name, the PDF's embedded title, or — for files named
  after an ISBN, a part code or a download URL — the first page of text, accepted only
  if it reads like prose.
- **Domains** are scored on the title and folder path; explicit overrides handle the
  cases a keyword cannot know. Overrides deliberately do **not** read the body text:
  an early version did, and filed a magazine article titled "Level Measurement" under
  *Level Measurement* because the article mentioned its own publication.

## Known limits

- 47 works are Catalan/Spanish university course files named `EE00400C`, `QU00403C` and
  the like. Their titles are recovered from folder names and page text, and a few remain
  approximate. Their classification (analysers, electrical, PLC) is reliable; their
  titles are best-effort.
- Page counts come from the PDF itself; a handful of malformed files report 0.
- The catalogue covers PDFs as documents. The HTML/Flash courses are counted in the
  file inventory but are not broken out work by work.
- Domain boundaries are judgement calls. A book on boiler control could sit under
  *Boiler & power-plant control* or *Process control*; it is in the former.
