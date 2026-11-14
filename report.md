# Autonomous Book Translation & Publication — Status Report

**Repository:** `github.com/pro-instcontrol/pro-instcontrol.github.io` (GitHub Pages, live at
`https://pro-instcontrol.github.io/`)
**Working copy:** `C:\Users\Phamd\WorkBuddy AI\2026-10-29-10-38-18\`
**Campaign directive (verbatim):** *"always add all figures, split chapters and TOC, links to TOC,
same standard as the last 3 books, do all autonomously"* — EN/VI only, **no Spanish**.

---

## 1. What is live right now

### Published books (fully complete)
| # | Book | Chapters | Vector figures | Status |
|---|------|----------|----------------|--------|
| 1 | *Measurement & Control Basics* (Bolton) | 10 | redrawn | ✅ live |
| 2 | *ISA-5.1 Instrumentation Symbols* | 9 | redrawn | ✅ live |
| 3 | *CSIA Working with an Integrator Guide* | 9 | 35 redrawn | ✅ live |

### Book 4 — in progress (Crosby *Pressure Relief Valve Engineering Handbook*, TP-V300, 1997)
| Chapter | Topic | Figures | Status |
|---------|-------|----------|--------|
| 1 | Introduction | 0 | ✅ **live** (EN/VI 200) |
| 2 | Design Fundamentals | 6 vectors | ✅ **live** |
| 3 | Terminology | 0 | ✅ **live** |
| 4 | Codes & Standards (Summary) | 0 | ✅ **live** |
| 5 | Valve Sizing — U.S.C.S. Units | 0 (5 equations) | ✅ **live** |
| 6 | Valve Sizing — Metric Units | 0 (5 equations) | ✅ **live** |
| 7 | Engineering Support Information | **9 charts/tables** | ⏳ pending |
| 8 | Appendix — ASME Section VIII Div.1 Excerpts | 0 | ⏳ pending |

**6 of 8 chapters live.** Library badge: 🟠 Translating · 6 of 8.

### Live verification (this session)
- Book TOC (`/books/read/pressure-relief-valve-engineering-handbook/`) lists ch01–ch06 ✅
- Ch6 EN + VI return HTTP **200** ✅
- Sitemap 902 URLs; `check_links.py` **broken 0** (904 pages, 27,718 refs) ✅
- 0 Spanish markers on every new page; all equations render with fraction markup; bilingual
  `class="en"` subtitles present; `nav()` links prev-chapter + TOC ✅

---

## 2. Build standard (applied uniformly to Books 1–4)
- **Every figure redrawn as a vector** (no raster scans). Book 2/3/4 schematics drawn with a shared
  `vfig` primitive library; SVG `<defs>` ids namespaced per-page to avoid duplicate-id breakage
  (`build/svg_ids.py`, wired into `bolton_common.write()`).
- **Each chapter = its own standalone page**; **book TOC links to every chapter** (one page per
  chapter, EN + VI variants).
- **Full bilingual EN/VI prose**; headings carry an optional `class="en"` subtitle so each language
  page shows the other language's heading.
- **Autonomous progression** — no pause for confirmation; QA (Spanish scan, dup-id/malformed-SVG
  check, link check) runs after every chapter.
- **No Spanish ever** (`(?i)\b(figura|capítulo|tabla|…)` regex guard → 0 hits).

## 3. Shared architecture (don't reinvent)
- `build/bolton_common.py` — page shell, markup helpers (`p, h2, h3, h4, eq, note, ul, ol, table,
  fig, keyterms, nav, page, write, build`), central `BOOK`/`SLUGS` tables.
- `build/isa51_common.py`, `build/int_common.py`, `build/prv_common.py` — per-book shells that
  re-import `bolton_common` and add one `BOOK`/`SLUGS` entry + `T(vi,en,lang)`.
- `build/reader_book.py` — `BOOKS` registry + `build(lang, spec)` TOC generator.
- `build/reader_prv.py` — generator for Book 4 (`MODULES = {1..8: "prv_chNN"}`).
- `build/vfig.py` + `build/prvfig.py` — vector primitives + Book 4 figure library.
- `build/books_site.py` (`TRANSLATED`/`BOOK_SLUG`/`DESC`), `build/make_sitemap.py`,
  `build/check_links.py` — site index, sitemap, QA.
- `build/prv_ch01..ch08.py` — chapter content modules (`PAGES_SRC, BYLINE, TITLE_EN/VI,
  note_terms(lang), body_vi(), body_en()`).

## 4. Source material
- PDF: `D:/Process Control and Automation/Instrumentation and Control/Pressure Relief Valve
  Engineering Handbook.pdf` (text layer extracted to `work/prv_raw.txt`, 6,364 lines).
- Ch1 3–5 · Ch2 6–11 · Ch3 12–15 · Ch4 16–18 · Ch5 19–28 · Ch6 29–38 · Ch7 39–69 ·
  Ch8 (Appendix) 70–93.

## 5. Git / credentials
- A GitHub PAT (`ghp_…`, account `pro-instcontrol`) was supplied and stored via
  `git config --global credential.helper store` + `git credential approve`. Pushes now succeed
  without a prompt (verified: `dc6d2d70..e84132f5 main -> main`).
- **Push requires `dangerouslyDisableSandbox: true`** in the Bash tool because the sandbox may
  otherwise SIGTERM network egress. Network egress is granted intermittently — if a push is
  SIGTERM'd, retry; the credential is already cached.

## 6. Remaining work
1. **Ch7 Engineering Support** — 9 figures (F7-1 compressibility Z, F7-2 Kb, F7-3 Kw, F7-4 Kn,
   F7-5 Kv, F7-6 k–C, F7-7 noise, F7-12 logic diagram, F7-13 vessel-selection diagram) redrawn as
   vectors; plus lookup tables T7-1…T7-12 (Kb, Ksh, k–C, k–Kr, env-factor, gas properties,
   water-saturation, flange dims, conversions, orifice areas). All extracted in `work/prv_raw.txt`
   (lines 2706–4301).
2. **Ch8 ASME Appendix** — excerpts of ASME Section VIII, Div. 1 (pp. 70–93), bilingual prose.
3. Register each in `SLUGS` + `done`, regenerate TOC/site/sitemap, run `check_links.py`, bump the
   `TRANSLATED` progress count, commit, push.
4. After Book 4 ships, pick the next Tier-A title and continue the same standard.

See `HANDOFF.md` for the exact step-by-step continuation recipe.
