# HANDOFF — Campaign resumed 2026-11-22 (Books 7–10 in progress)

**State now (resumed 2026-11-22):** 9 reader books fully live 🟢 (flagship Book 6
*Valve Selection Handbook* 21/21). Campaign: Baumann `cvp` **4/32**, Borden `bcv` 1/1 🟢,
Emerson `cvh6` **8/15 live**, IIH `iih` **3/8**, PPIC `ppic` 1/11, IPC `ipc` 1/8.
**Live HEAD `dfac0c08`** (Ch.8); live sitemap 1,042 URLs, catalog badge 8/15, Ch.8 EN/VI deep
URLs 200, `check_links.py` broken 0. Full tables in `report.md`.

**User's queued continuation (verbatim order):** "Book 8 Chapters 2–8, Baumann Chapters 3–32,
and Emerson Chapters 2–15 do one by one" — plus two books located but not registered
(*Fundamentals of Industrial Instrumentation*, 348 pp; *A Guide to the Automation Body of
Knowledge*, 2nd ed., 511 pp).

---

## 0. Done: Book 10 `ipc` Chapter 1 integrated (push `2ca04367`)
Redid the 3 registration edits, built chapter/TOC/site/sitemap, QA'd (51 figs XML-valid,
51 unique fig ids, 0 CJK, 0 ES, broken 0), committed and live-verified both language pages.
Continue with the queue below, one chapter per run. Note: the "bare &" count of 2–3 per page
is the shared Google Fonts URL in the page shell — pre-existing on every published page, not
chapter content.

## 0.5 Emerson Ch.3 pause resolved — published in `8909e5fc`
The earlier pause was lifted: the registered/built/QA’d Emerson Ch.3 working tree was committed
as `8909e5fc` ("Publish Emerson Ch.3: Valve and Actuator Types (EN/VI, 52 vector figures)") and
pushed. Before committing, the paused build was re-validated: 52 XML-valid SVGs, unique
`fig-1..52`, 0 CJK, 0 Spanish, only the 2 shell Google-Fonts bare `&`s, `check_links.py` broken 0,
TOC/catalog/sitemap updated. After push, EN/VI deep URLs initially 404'd (Pages negative
caching) and were verified 200 once deployment propagated; the live TOC lists Ch.3 and the live
sitemap has all 8 Ch.3 URL entries. Visual fixes from the prior session (figs 3.2, 3.6, 3.21,
3.24, 3.29, 3.31–3.34, 3.38, 3.44, 3.50, 3.52) are therefore live.

## A. Continuation queue (user's order)
1. ~~Book 8 `iih` ch2–3~~ — **done**; remaining ch4–8, source `work/ihii_raw.txt`; printed = PDF − 14.
2. ~~Baumann `cvp` ch3–4~~ — **done**; remaining ch5–32, source `work/cvp_raw.txt`.
3. ~~Emerson `cvh6` ch3–ch8~~ — **done** in `8909e5fc`, `cbc667cc`, `56b8a0f9`, `d2a1da0a`,
   `9e136a59`, `dfac0c08`; continue ch9–15. Source `work/cvh6_raw.txt`; printed = PDF page (dump
   pages match). Ch.9 "Standards and Approvals" starts at raw line 12145; check its printed-page
   span and figure count before delegating. Separate per-chapter figure modules (`cvh6fig5.py`…
   `cvh6fig8.py`) are standard; one agent writes prose + figures for mid-size chapters.
   **Watch for the glossary-shadowing bug:** a module-level `def note(lang)` shadows the shared
   note markup helper and makes both glossary boxes render as the English source-note text.
   Name that function `source_notes(lang)` instead; fixed in Ch.3 and Ch.4.
4. Book 9 `ppic` ch2–11 — source `work/ppic_raw.txt`; printed = PDF − 16.
5. Book 10 `ipc` ch2–8 — source **`work/ipc_decoded.txt`** (NOT the raw dump — glyph codes).
6. Register Book 11 / Book 12 from the two located PDFs when the user confirms.

Per-chapter flow: survey source span + figures → delegate writing to a background agent with a
brief modeled on the IIH/PPIC/IPC briefs (architecture pointers, constants, QA commands) →
validate output (SVG XML, CJK, bare `&`, unique fig ids) → 3 registration edits → build chain →
QA → commit/push → live verify → update `TRANSLATION-STATUS.md` + memory log.

## B. Git / credentials (already configured — do not redo)
- PAT stored via credential helper `store`; repo-local config clears the GCM chain
  (`credential.helper ""` + `store`). **Do not remove these two local config entries.**
- Push: `GIT_TERMINAL_PROMPT=0 GCM_INTERACTIVE=never git -c credential.helper= -c
  credential.helper=store push --progress origin main` — completes in seconds.
- **Pages propagation:** deep paths can 404 for minutes after a push (negative caching).
  Retry with cache-busting query strings until 200.

## C. Unit recipe (per chapter)
1. Map the source span from the text dump (`===PDFPAGE N===` markers; check the printed-page
   offset per book, see `report.md` §4) and list figure captions.
2. Vector figure module `<key>fig.py`: each figure function returns
   `(svg, caption_vi, caption_en, aria_vi, aria_en)` via `_fig(...)`; captions `Hình …` / `Figure …`;
   register in `FIGS` (mirror `ppicfig.py`/`iihfig.py`). Escape raw `&` as `&amp;`.
3. Chapter module `<key>_chNN.py` mirroring `ppic_ch01.py`: `PAGES_SRC`, `BYLINE`, `TITLE_EN`,
   `TITLE_VI`, optional `note_terms()`, `body_vi()`, `body_en()`; use `import <key>_common as C`
   helpers; `C.fig(num, key)` embeds figures; `refs([...])` for references; per-language tables.
4. Wire-up (3 edits) — see §0 step 1–3, substituting the book key and chapter number.
5. Build & QA: `python build/reader_<key>.py N` → `reader_book.py <key>` → `books_site.py` →
   `make_sitemap.py` → `check_links.py` (**broken 0**). Page QA: every inline SVG XML-valid;
   unique `fig-N` ids; 0 CJK; 0 bare ampersands; no cross-language leakage; aria labels complete.
6. `git add -A && git commit`, push (§B), update `TRANSLATION-STATUS.md` session log + workspace
   memory daily log, verify live (unit pages EN + VI = 200, TOC lists the unit, badge correct).

## D. QA gates (must pass every chapter)
- `check_links.py` → **broken 0**
- Every inline SVG XML-valid (`ET.fromstring`); unique `fig-N` ids per page
- 0 CJK characters, 0 bare ampersands (`&(?!amp;|lt;|gt;|quot;|apos;|#)`)
- Spanish guard → 0 hits; EN tables contain no Vietnamese; captions match page language
- Sitemap regenerated; `TRANSLATED` badge updated (`progress` → `full` when book completes)
- Live verification after push: chapter pages EN + VI = 200, TOC row present, catalog badge correct

## E. Known gotchas
- `done` maps must contain ONLY built chapters; empty-`done` books get 4 transient TOC links
  (fallback `spec["done"].get(1, spec["first_en"][0])`) that clear when Ch.1 lands.
- IPC PDF: body text is glyph codes; always use `work/ipc_decoded.txt`.
- Image-only sources (Borden) need `pypdfium2` rendering to `work/*.png` (QA libs in `work/qalib`).
- `p()` takes exactly one argument — no second positional argument.
- When inserting a new `BOOKS` spec before `def num(n, lang):`, don't duplicate the closing
  brace of the dict (bit us twice).
- `books_site.py` `SyntaxWarning` (invalid escape sequence, line ~980) is pre-existing noise.
