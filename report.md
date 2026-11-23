# Autonomous Book Translation & Publication — Status Report

**Repository:** `github.com/pro-instcontrol/pro-instcontrol.github.io` (GitHub Pages, live at
`https://pro-instcontrol.github.io/`)
**Working copy:** `C:\Users\Phamd\WorkBuddy AI\2026-10-29-10-38-18\`
**Campaign directive (verbatim):** *"always add all figures, split chapters and TOC, links to TOC,
same standard as the last 3 books, do all autonomously"* — EN/VI only, **no Spanish**.
**Status (2026-11-22, stopped by user):** 9 reader books fully live (flagship Book 6
*Valve Selection Handbook* 🟢 21/21), plus a 4-book control/instrumentation campaign in progress
across Books 7–10. **Live HEAD `d487a9cb`** (IIH Ch.3 + Baumann Ch.4 published); all live checks
green. Emerson Ch.3 is built and QA’d locally but **intentionally not committed/pushed** at the
user’s stop request.

---

## 1. What is live right now

### Fully published reader books (all EN + VI, 🟢 complete)
| # | Book | Units | Figures | Status |
|---|------|-------|---------|--------|
| 1 | *The Measurement, Instrumentation and Sensors Handbook* (summary tier) | 113 | redrawn | ✅ live |
| 2 | PC *Process Control* (summary tier) | 14 | 50 redrawn | ✅ live |
| 3 | *Safety Instrumented Systems — Design, Analysis, and Justification* (2nd ed.) | 16 | redrawn | ✅ live |
| 4 | W. Bolton, *Control Systems* (Newnes 2002) | 7 | 19 redrawn | ✅ live |
| 5 | *Inherent Safety in Process Plant Design* (VTT 384) | 16 | redrawn | ✅ live |
| 6 | Crosby *Pressure Relief Valve Engineering Handbook* (TP-V300) | 8 | redrawn | ✅ live |
| 7 | ISA-5.1 *Instrumentation Symbols and Identification* | 7 | redrawn | ✅ live |
| 8 | CSIA *Working with an Integrator Guide* | 9 | 35 redrawn | ✅ live |
| 9 | **Smith & Zappe, *Valve Selection Handbook*, 5th ed. (2004) — flagship** | **21** | **235 redrawn** | ✅ **live, 🟢 21/21** |

### In-progress campaign books (registered, translated chapter by chapter)
| Key | Book | Source | Chapters | Done | Figures so far |
|-----|------|--------|----------|------|----------------|
| `cvp` | **Book 7** — H. D. Baumann, *Control Valve Primer*, 5th ed. (ISA/Wiley 2011) | 204 pp | 32 | **4/32** 🟠 | 7 (ch1–4) |
| `bcv` | **Book 7b** — Borden/Friedmann, *Control Valves* (ISA Practical Guides 1998) — Ch.5 excerpt | 12 pp scan | 1 | **1/1** 🟢 | 4 |
| `cvh6` | **Book 7c** — Emerson, *Control Valve Handbook*, 6th ed. (2020) | 355 pp | 15 | **2/15 live**; 3/15 built locally 🟠 | 29 live; +52 local (ch3) |
| `iih` | **Book 8** — 3G E-learning, *Illustrated Handbook of Industrial Instrumentation & Control* (2018) | 348 pp | 8 | **3/8** 🟠 | 48 (ch1–3) |
| `ppic` | **Book 9** — L. N. Jalali (ed.), *Handbook on Power Plant Instrumentation and Control* (Bibliotex 2019) | 308 pp | 11 | **1/11** 🟠 | 5 (ch1) |
| `ipc` | **Book 10** — Prasad/Jayaswal/Priye, *Instrumentation and Process Control* (I.K. International 2019) | 403 pp | 8 | **1/8** 🟠 | 51 (ch1) |

**Library catalog:** 258 works; new works this campaign: 291 (Baumann), 292 (Borden), 293
(Emerson), 294 (IIH), 295 (PPIC), 296 (IPC).

### Published chapters this campaign (EN + VI each)
- Baumann Ch.1 (3 figs) + Ch.2 "Why Not Use a Speed-Controlled Pump?" (no figs, 3 refs)
  + Ch.3 "What Valve Type Shall I Choose?" (3 figs) + Ch.4 "The Self-Acting Regulator: Why Not?"
  (1 fig, printed pp. 21–23)
- Borden Ch.5 "Control Valve Actuators" (4 figs) — book complete
- Emerson Ch.1 "Introduction to Control Valves" (19 figs, printed pp. 16–33)
  + Ch.2 "Control Valve Performance" (10 figs, printed pp. 34–53)
- IIH Ch.1 "Measurement of Temperature" (6 figs, printed pp. 1–45, 77 refs)
  + Ch.2 "Measurement of Pressure" (21 figs) + Ch.3 "Measurement of Level" (21 figs,
  PDF pp. 97–142 / printed 83–128, 55 refs)
- PPIC Ch.1 "Catalytic Reduction of Dissolved Oxygen" (5 figs, 4 tables)
- IPC Ch.1 "Transducers – I" (51 figs, 7 tables, printed pp. 1–62)
- **Locally built, not published:** Emerson Ch.3 "Valve and Actuator Types" — 28 source pages,
  52 vector figures, full EN/VI prose; QA passed, but the working tree was left uncommitted at
  the user’s stop request.

### Live verification (2026-11-22, at stop)
- Newly published IIH Ch.3 EN/VI and Baumann Ch.4 EN/VI → **HTTP 200** after cache-busting
  retries (Pages briefly 404s deep paths immediately after push, then resolves).
- Live HEAD `d487a9cb` sitemap: **1,030 URLs** (1,015 with language siblings); 512 work-detail
  pages. Local working tree (includes unpublished Emerson Ch.3): 1,032 URLs / 1,017 siblings.
- `check_links.py` at last local build: **broken 0**; 1,034 pages / 30,964 local references.
- Emerson Ch.3 was **not** pushed, so its local TOC/progress changes are not live.

---

## 2. Build standard (applied uniformly to all books)
- **Every source figure redrawn as a vector** (no raster scans). Figures return the standard
  5-tuple `(svg, caption_vi, caption_en, aria_vi, aria_en)`; bilingual captions
  (`Hình …` / `Figure …`), numbered callouts where the source has them.
- **Each chapter = its own standalone page**; book TOC links every built unit (EN + VI).
- **Full bilingual EN/VI prose**; per-language tables (no cross-language leakage).
- QA gates: SVGs XML-valid, unique `fig-N` ids, **0 CJK, 0 bare ampersands**, `check_links.py`
  broken 0, sitemap regenerated, live 200 checks after push.
- Source OCR typos are preserved in EN with VI following intended meaning; end-of-chapter
  `note()` documents source quirks.

## 3. Shared architecture (don't reinvent)
- `build/bolton_common.py` — page shell, markup helpers, central `BOOK`/`SLUGS` tables.
- Per-book shells: `<key>_common.py` (re-import bolton_common, one `BOOK`/`SLUGS` entry +
  `T(vi,en,lang)`) and runners `reader_<key>.py` (`MODULES = {chapter: module}`).
- `build/reader_book.py` — `BOOKS` registry + TOC generator (`chapters` + `done` slug map;
  `done` must contain ONLY built chapters; empty-`done` fallback
  `spec["done"].get(1, spec["first_en"][0])` creates the 4 transient links).
- `build/vfig.py` — vector primitives; per-book figure modules `<key>fig.py`.
- `build/books_site.py` (`DESC`/`TRANSLATED`/`BOOK_SLUG`/`DROP_WORK_IDS={186}`),
  `make_sitemap.py`, `check_links.py`.
- **Chapter registration = 3 edits:** `<key>_common.SLUGS[key][n]`, `reader_book.py` `done[n]`,
  `books_site.py` `TRANSLATED[...]` progress; then rebuild chapter → TOC → site → sitemap →
  check_links → commit → push → live verify.

## 4. Source material map (all under `D:/Ebooks/Process Control and Automation/`)
| Key | PDF | Text dump | Notes |
|-----|-----|-----------|-------|
| cvp | Control-valve-primer-a-users-guide-fifth-edition.pdf | `work/cvp_raw.txt` | 204 pp, 32 ch |
| bcv | Control Valves Selection Handbook - Borden Friedmann.pdf | image-only | rendered `work/borden_p01..12.png` |
| cvh6 | Emerson-control-valve-handbook-en-3661206.pdf | `work/cvh6_raw.txt` | 355 pp, 15 ch |
| iih | Illustrated-handbook-of-industrial-instrumentation-and-process-control.pdf | `work/ihii_raw.txt` | 348 pp, 8 ch |
| ppic | Handbook-on-power-plant-instrumentation-and-control.pdf | `work/ppic_raw.txt` | 308 pp, 11 ch; printed = PDF−16 |
| ipc | Instrumentation-and-process-control.pdf | `work/ipc_raw.txt` → **decoded `work/ipc_decoded.txt`** | 403 pp, 8 ch; body text stored as glyph codes `/Gnn` → `chr(nn)`; printed = PDF−12 |

## 5. Git / credentials (configured — do not redo)
- PAT via credential-helper store; repo-local config clears the GCM chain — **do not remove**.
- Push pattern: `GIT_TERMINAL_PROMPT=0 GCM_INTERACTIVE=never git -c credential.helper= -c
  credential.helper=store push --progress origin main`.
- Session pushes: `0ed011b7` (registration) → `bad2d686` (Baumann ch2 + Emerson ch1) →
  `b370e6f3` (Book 8 registration) → `98bb7d26` (IIH ch1) → `066862d2` (Book 9 registration) →
  `7b60e440` (PPIC ch1) → `671ae45b` (Book 10 registration) → `a15f1de8` (pause/report) →
  `2ca04367` (IPC ch1) → `de891681` (IIH ch2) → `e71e3415` (Baumann ch3) → `fd86e439` (Emerson ch2)
  → `2d19c7d2` (IIH ch3) → `d487a9cb` (Baumann ch4, **live HEAD at stop**).
- Uncommitted at stop: Emerson Ch.3 registration, figure fixes, chapter module and generated
  EN/VI pages. Do **not** assume these are live; commit/push them when resuming.
- GitHub Pages negative caching can briefly 404 deep paths; retry with cache-busting queries.

## 6. Queue (user's stated order)
1. ~~Integrate Book 10 `ipc` Chapter 1~~ — **done** in `2ca04367` (51 figs, 7 tables, broken 0).
2. ~~Book 8 `iih` Ch.3 "Measurement of Level"~~ — **done** in `2d19c7d2` (21 figs); remaining
   Ch.4–8 continue one by one.
3. ~~Baumann `cvp` Ch.3 + Ch.4~~ — **done** (`e71e3415`, `d487a9cb`); remaining Ch.5–32.
4. **Emerson `cvh6` Ch.3 "Valve and Actuator Types" — built/QA’d locally, paused before commit.**
   On resume: commit the existing working tree (or rebuild with `python build/reader_cvh6.py 3`,
   `reader_book.py cvh6`, `books_site.py`, `make_sitemap.py`, `check_links.py`), push, and verify
   EN/VI deep URLs. Then continue Ch.4–15.
5. **Register candidate Book 11** — *Fundamentals of Industrial Instrumentation* (348 pp,
   2.5 MB) — located and surveyed, not registered.
6. **Register candidate Book 12** — *A Guide to the Automation Body of Knowledge*, 2nd ed.
   (511 pp, 34 MB) — located and surveyed, not registered.
7. Book 9 `ppic` Chapters 2–11 after the user's named queues.

### Paused working tree (exact scope)
- Modified: `books/index.html`, `vi/books/index.html`, both Emerson TOCs, `sitemap.xml`,
  `build/books_site.py`, `build/cvh6_common.py`, `build/cvh6fig.py`, `build/reader_book.py`.
- Added: `build/cvh6_ch03.py`, both generated
  `books/read/control-valve-handbook-emerson-6th/ch03-valve-and-actuator-types/index.html`
  files (EN + VI).
- The status documents themselves (`report.md`, `HANDOFF.md`, `TRANSLATION-STATUS.md`, workspace
  memory) were also updated locally but not committed.
- Nothing else is pending; IIH Ch.3 and Baumann Ch.4 are fully committed and live.

See `HANDOFF.md` for the step-by-step continuation recipe and QA gates.
