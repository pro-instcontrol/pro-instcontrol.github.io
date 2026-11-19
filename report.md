# Autonomous Book Translation & Publication — Status Report

**Repository:** `github.com/pro-instcontrol/pro-instcontrol.github.io` (GitHub Pages, live at
`https://pro-instcontrol.github.io/`)
**Working copy:** `C:\Users\Phamd\WorkBuddy AI\2026-10-29-10-38-18\`
**Campaign directive (verbatim):** *"always add all figures, split chapters and TOC, links to TOC,
same standard as the last 3 books, do all autonomously"* — EN/VI only, **no Spanish**.
**Status (2026-11-18): the campaign's flagship book, Book 6 — Smith & Zappe, *Valve Selection
Handbook* — is COMPLETE: all 21 units live in EN + VI, catalog badge 🟢.**

---

## 1. What is live right now

### Published reader books (all EN + VI)
| # | Book | Chapters | Figures | Status |
|---|------|----------|---------|--------|
| 1 | *The Measurement, Instrumentation and Sensors Handbook* (summary tier) | 113 | redrawn | ✅ live |
| 2 | PC *Process Control* (summary tier) | 14 | 50 redrawn | ✅ live |
| 3 | *Safety Instrumented Systems — Design, Analysis, and Justification* (2nd ed.) | 16 | redrawn | ✅ live |
| 4 | W. Bolton, *Control Systems* (Newnes 2002) | 7 | 19 redrawn | ✅ live |
| 5 | *Inherent Safety in Process Plant Design* (VTT 384) | 16 | redrawn | ✅ live |
| 6 | Crosby *Pressure Relief Valve Engineering Handbook* (TP-V300) | 8 | redrawn | ✅ live |
| 7 | ISA-5.1 *Instrumentation Symbols and Identification* | 7 | redrawn | ✅ live |
| 8 | CSIA *Working with an Integrator Guide* | 9 | 35 redrawn | ✅ live |
| 9 | **Smith & Zappe, *Valve Selection Handbook*, 5th ed. (2004) — Book 6, flagship** | **21** | **235 redrawn** | ✅ **live, 🟢 21/21** |

### Book 6 — all 21 units (EN/VI, vector figures per unit)
| Unit | Title | Source (book pp.) | Figures |
|------|-------|-------------------|---------|
| 1 | Introduction | 1–… | 1 |
| 2 | Fluid Tightness and Sealing | … | 2 |
| 3 | Seatings, Gaskets, Stem Seals | … | 1 |
| 4 | Fundamentals: Flow Through Valves | … | 9 |
| 5 | Manual Valves I — Selection, Globe | … | 24 |
| 6 | Manual Valves II — Piston & Parallel Gate | … | 9 |
| 7 | Wedge Gate Valves | … | 15 |
| 8 | Plug Valves | … | 11 |
| 9 | Ball Valves | … | 9 |
| 10 | Butterfly and Pinch Valves | … | 24 |
| 11 | Diaphragm and Stainless Steel Valves | … | 7 |
| 12 | Check Valves | 153–168 | 15 |
| 13 | Direct-Loaded Pressure Relief Valves | 169–… | 34 |
| 14 | Pilot-Operated Pressure Relief Valves | … | 10 |
| 15 | Rupture Discs I — Construction | … | 33 |
| 16 | Rupture Discs II — Selection | 261–267 | 5 |
| 17 | Sizing Pressure Relief Devices | 269–292 | 9 |
| 18 | Actuators | 293–308 | 5 |
| 19 | Double Block and Bleed Ball Valves | 309–313 | 3 |
| 20 | Mechanical Locking Devices for Valves | 314–326 | 8 |
| 21 | Appendices — Abbreviations, Standards, SI Units, Glossary | 327–361 | 1 |

**Total: 235 vector figure instances × 2 languages; 21 language-specific summary tables.**

### Live verification (2026-11-18, Book 6 completion)
- Units 19/20/21 EN + VI → all **HTTP 200** with correct titles.
- Both book TOCs list all 21 chapters; both catalog cards show
  **🟢 Fully translated · 21 of 21 chapters / 🟢 Đã dịch đầy đủ · 21/21 chương**.
- Removed duplicate `/books/work/186/` still **404**.
- `sitemap.xml` 982 URLs (967 with language siblings); `check_links.py`
  **984 pages / 29,714 refs / broken 0**.

---

## 2. Build standard (applied uniformly to all books)
- **Every source figure redrawn as a vector** (no raster scans). Figures return the standard
  5-tuple `(svg, caption_vi, caption_en, aria_vi, aria_en)`; each carries a numbered bilingual
  legend (VI main line + EN subtext) and source credits.
- **Each unit = its own standalone page**; **book TOC links to every unit** (EN + VI variants).
- **Full bilingual EN/VI prose** with `class="en"` subtitles on headings; language-specific
  summary tables (no cross-language leakage — verified per page).
- **Autonomous progression** — no pause for confirmation; full QA after every unit.
- **No Spanish ever**; 0 CJK characters; 0 Python artifacts; no truncated aria labels.

## 3. Shared architecture (don't reinvent)
- `build/bolton_common.py` — page shell, markup helpers (`p, h2, h3, h4, eq, note, ul, ol, table,
  fig, keyterms, nav, page, write, build`), central `BOOK`/`SLUGS` tables.
- Per-book shells: `build/isa51_common.py`, `build/int_common.py`, `build/prv_common.py`,
  `build/isd_common.py`, **`build/vsh_common.py`** (Book 6) — re-import `bolton_common`, add one
  `BOOK`/`SLUGS` entry + `T(vi,en,lang)`.
- `build/reader_book.py` — `BOOKS` registry + TOC generator (`chapters` titles + `done` slug map).
- Per-book reader generators: `build/reader_vsh.py` (Book 6 `MODULES = {1..21}`), `reader_prv.py`,
  `reader_isd.py`, etc.
- `build/vfig.py` + `build/vshfig3.py` — vector primitives + shared op-emitters
  (`_emit`, `_emit_legend`). Book 6 figure libraries: `vshfig.py`, `vshfig2…vshfig18.py`
  (one per unit where needed).
- `build/books_site.py` (`TRANSLATED`/`BOOK_SLUG`/`DESC`, `FLAG_LABEL`), `build/make_sitemap.py`,
  `build/check_links.py` — site index, sitemap, QA.
- `build/vsh_ch01…ch21.py` — Book 6 unit content modules (`PAGES_SRC, BYLINE, TITLE_EN/VI,
  note_terms(lang), body_vi(), body_en()`).
- Book 6 unit registration (three edits): `vsh_common.SLUGS["vsh"][N]`,
  `reader_book.py` vsh `done` map, `books_site.py` `TRANSLATED["valve selection handbook"]`.

## 4. Book 6 source material
- PDF: `D:/Ebooks/Process Control and Automation/Elsevier - Valve Selection Handbook 5th Ed -
  2004 - (By Laxxuss).pdf` (text layer extracted to `work/vsh_raw.txt`; unit spans documented in
  `TRANSLATION-STATUS.md` per unit).
- Book pp. 1–399 total; 21 units cover the whole book including Appendices A–E.
- Figure pages rendered locally with `pypdfium2` (installed into git-ignored `work/qalib`) to
  guide the vector redraws.

## 5. Git / credentials (configured — do not redo)
- PAT stored via `git credential approve` + credential helper store; repo-local config clears the
  GCM chain (`git config --local credential.helper ""` + `--add credential.helper store`).
  **Do not remove these local config entries.**
- Pushes: `git push origin main` completes in seconds (latest: `27f72c01..e8e832b4`).
- After each push, GitHub Pages propagation can briefly 404 deep paths (negative caching);
  retry `curl --retry N --retry-delay M` with cache-busting query strings until 200.

## 6. Remaining work / next steps
1. **Book 6 is fully done — no pending units.** Optionally deepen Appendix tables (verbatim
   reproduction was intentionally avoided in Unit 21).
2. **Next campaign step:** pick the next Tier-A instrumentation/control title (EN/VI only, no
   Spanish), extract to `work/<slug>_raw.txt`, create `<slug>_common.py` + reader + figure
   module following the Book 6 pattern (`build/vsh_common.py`, `build/reader_vsh.py`,
   `build/vshfig3.py`, `build/vsh_ch13.py` as the reference implementation), then build units
   one at a time with the QA gates below.
3. Keep the standing duplicate-card filter (`DROP_WORK_IDS = {186}` in `books_site.py`).

See `HANDOFF.md` for the exact step-by-step continuation recipe and QA gates.
