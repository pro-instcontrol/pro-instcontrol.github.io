# HANDOFF — Campaign state: BOOK 6 COMPLETE (all 21 units live)

**Status (2026-11-18):** Smith & Zappe, *Valve Selection Handbook* (5th ed., 2004) — Book 6 — is
**100% LIVE in EN + VI, 21/21 units**, catalog badge 🟢 (EN: "Fully translated · 21 of 21
chapters" / VI: "Đã dịch đầy đủ · 21/21 chương"). Together with the earlier books, the site now
hosts nine reader books (see `report.md` §1 for the full table).

Final Book 6 session commits: `46e7af43` (U19), `a198f2ad` (U20), `e8e832b4` (U21 + book
complete). Infra: sitemap 982 URLs; `check_links.py` **984 pages / 29,714 refs / broken 0**;
duplicate `/books/work/186/` still 404.

**Next campaign step:** select the next Tier-A instrumentation/control title (EN/VI only, NO
Spanish), extract to `work/<slug>_raw.txt`, create `<slug>_common.py` + reader + figure module
following the Book 6 pattern, then build units one at a time with the QA gates in §D.

---

## A. Git / credentials (already configured — do not redo)
- PAT stored: `git config credential.helper store` + `git credential approve`
  (token `ghp_…` for `pro-instcontrol`). Pushes need **no prompt**.
- **Push-hang root cause (fixed):** the system gitconfig chains `credential.helper = manager`
  before `store`; the repo-local config clears the chain
  (`git config --local credential.helper ""` + `git config --local --add credential.helper
  store`). **Do not remove these two local config entries.**
- `git push origin main` completes in seconds. If a push ever returns `SIGTERM` with empty
  output, just retry — the commit is safe locally.
- **Pages propagation:** after a push, deep paths can 404 for several minutes (negative
  caching) while shallow indexes already serve fresh content. Verify with retries:
  `curl -sS -o tmp.html -w "%{http_code}" --retry 40 --retry-delay 9 --retry-all-errors
  "https://pro-instcontrol.github.io/books/read/<slug>/<unit>/?bust=$(date +%s%N)"`.

## B. Unit recipe (identical for every unit of a book)
1. Map the source span: read `work/<slug>_raw.txt` from the `=== PAGE N ===` marker of the
   first page to the next unit's first page; `grep "Figure X-"` for the figure list.
   Render figure pages with `pypdfium2` (in `work/qalib`) to view the originals:
   `PYTHONPATH=work/qalib python -c "import pypdfium2 as pdfium; …"`.
2. Build a vector figure module `build/vshfigNN.py` (Book 6 numbering): each figure function
   returns the 5-tuple `(svg, caption_vi, caption_en, aria_vi, aria_en)`, registers itself in
   `FIGSNN` via `@_regNN`; use `vfig` primitives + `vshfig3._emit/_emit_legend`.
   - Gotcha: `_emit()` handles only op tuples — **strings returned by `_txt()` must go into
     `extra=`, never inside `ops`** (they are silently dropped otherwise).
   - Gotcha: escape raw `&` as `&amp;` and never emit raw `<` inside SVG text.
   - Gotcha: keep the drawing left of x≈390 — the numbered legend column starts at x=402
     (canvas 560×380).
   - Validate: `ET.fromstring(svg)` per figure; render a contact sheet and review it.
3. Create `build/vsh_chNN.py` mirroring `vsh_ch13.py`: `PAGES_SRC`, `BYLINE`, `TITLE_EN`,
   `TITLE_VI`, `note_terms(lang)`, `body_vi()`, `body_en()`; import
   `from vsh_common import fig, h2, h3, p, table, ul, ol`; `import vshfigNN as F`.
   VI prose is the primary text; EN mirrors it. Summary tables must be built per language
   (`… if vi else …`) — never bilingual mixed cells.
4. Wire-up (three edits):
   - `build/vsh_common.py` → `SLUGS["vsh"][N] = "chNN-…"`.
   - `build/reader_book.py` → extend the vsh `done` map (TOC titles already exist for 1–21).
   - `build/books_site.py` → `TRANSLATED["valve selection handbook"] = ("progress", 21, N)`;
     when the book finishes use `("full", 21, 21)` — FLAG_LABEL keys are
     `full` / `progress` / `summary` / `none` (there is no `done` key).
5. Build & QA: `python build/reader_vsh.py N` → `reader_book.py vsh` → `books_site.py` →
   `make_sitemap.py` → `check_links.py` (**broken 0**). Page QA: XML-validate every inline SVG;
   scan for CJK / Python artifacts / Spanish / Vietnamese leakage into EN tables; check aria
   labels are not truncated; then screenshot EN + VI pages (headless Chrome, tall capture,
   crop locally with Pillow from `work/qalib`) and review.
6. `git add -A && git commit`, push (see §A), update `TRANSLATION-STATUS.md` session log +
   workspace memory daily log, verify live.

## C. Book 6 reference map (for style parity)
- Units/figures/tables per unit: see `report.md` §1 (235 vector figure instances total).
- Reference implementations: `build/vsh_ch13.py` (34-figure unit), `build/vshfig10.py`
  (parametric `_prv_fig` + charts), `build/vshfig17.py` (schematics with legend discipline),
  `build/vsh_ch21.py` (appendices as selection tables).
- Unit spans are documented per unit in `TRANSLATION-STATUS.md`; raw text in
  `work/vsh_raw.txt` (`grep -n "=== PAGE"` for the page map).

## D. QA gates (must pass every unit)
- `check_links.py` → **broken 0**
- Spanish guard → **0 hits** on every new page (EN + VI)
- 0 CJK characters, 0 Python artifacts in HTML
- Every inline SVG XML-valid (`ElementTree.fromstring`); aria labels complete
- English tables contain no Vietnamese characters; VI/EN captions match the page language
- Sitemap regenerated; `TRANSLATED` badge updated (`progress`/`full`)
- Styled-page screenshot review in cropped sections (figures, legends, table, nav, footer)
- Live verification after push: unit pages EN + VI = 200, TOC lists the unit, catalog badge
  correct, duplicate `/books/work/186/` still 404
