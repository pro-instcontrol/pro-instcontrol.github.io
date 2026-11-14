# HANDOFF — Finish Book 4 (Crosby PRV Engineering Handbook)

**Goal:** build Chapters 7 & 8 so Book 4 is 8/8, then regenerate infra, QA, commit, push.

Book 4 Ch1–6 are **already live**. Only Ch7 + Ch8 remain. All source text already extracted to
`work/prv_raw.txt`.

---

## A. Git / credentials (already configured — do not redo)
- PAT stored: `git config --global credential.helper store` + `git credential approve` (token
  `ghp_…` for `pro-instcontrol`). Pushes need **no prompt**.
- **Always run `git push` with `dangerouslyDisableSandbox: true`** (sandbox SIGTERMs network egress
  otherwise). If a push returns `SIGTERM` with empty output, just retry — network egress is granted
  intermittently.
- Verify live after push: `curl -s -o /dev/null -w "%{http_code}" https://pro-instcontrol.github.io/books/read/pressure-relief-valve-engineering-handbook/chNN-…/`

## B. Chapter 7 — Engineering Support Information (pages 39–69, `work/prv_raw.txt` lines 2706–4301)
**Figures to redraw as vectors** (add to `build/prvfig.py`, return the 5-tuple
`(svg, cap_vi, cap_en, aria_vi, aria_en)`; register in `prvfig.FIGS`):
- `fig_f71()` — Compressibility factor Z (generalized chart) — schematic curve, axes Z vs Pr.
- `fig_f72()` — Kb for balanced (JBS/Series BP) valves, gas/vapor (F7-2A/B).
- `fig_f73()` — Kw for balanced valves, liquid (F7-3A/B).
- `fig_f74()` — Kn high-pressure steam (F7-4).
- `fig_f75()` — Kv viscosity (F7-5, axes Kv 0.3–1.0 vs Reynolds 10–100,000).
- `fig_f76()` — k vs C curve (F7-6, from T7-3 data).
- `fig_f77()` — Noise intensity vs pressure ratio (F7-7, L 20–70 vs PR 1.5–10).
- `fig_f712()` — Fire-sizing logic diagram (F7-12, flowchart boxes+arrows).
- `fig_f713()` — Vessel/tank selection diagram (F7-13, sphere / horizontal / vertical cylinder).
- (Reaction-force graphs F7-8…F7-11 are product-specific; represent with one generic
  "reaction force vs P₁" note referencing the formula, or omit — they are not general reference.)

**Lookup tables to render as HTML** (use `table(header, rows, caption)` helper):
- T7-1 Kb vs Pb/P1 (pairs 55→1.00 … 96→0.39 — in raw lines 2822–2829)
- T7-2 Ksh superheat (full grid, lines 2974–3033)
- T7-3 k→C (1.01–2.00 → 317–400, lines 3053–3072)
- T7-4 relative noise levels (qualitative list)
- T7-5 k→Kr (1.01–2.00, lines 3291–3312)
- T7-6 environmental factor F (lines 3382–3393)
- T7-7 typical gas properties (M, k, C, G, Pc, Tc — lines 3787–3828)
- T7-8 water saturation (lines 3875–3952), T7-9 ANSI flange dims (3960–4007),
  T7-10 conversions (4022–4141), T7-11/12 orifice areas (4149–4190) — include as tables or
  condensed reference.

**Module:** create `build/prv_ch07.py` (mirror `prv_ch05.py`): `PAGES_SRC=31`, `BYLINE` same,
`note_terms(lang)`, `body_vi()`, `body_en()` using `from prv_common import p,h2,h3,h4,ul,ol,note,eq,table,fig`
and `import prvfig as F`. Use `fig(n, F.fig_f7x())` for each figure.
Sections: Back-pressure theory → Kb/Kw/Kv/Ksh/Kn/Kr coefficients → Noise → Reaction forces →
Fire conditions (vaporizing liquids + gas/vapor vessels) → Two-phase/flashing → Typical gas
properties → Water saturation → Flange dims → Conversions → Orifice areas.

## C. Chapter 8 — Appendix ASME Section VIII Div. 1 Excerpts (pages 70–93, lines 4302–6363)
- **0 figures** expected (excerpts of code text). Bilingual prose only, mirror `prv_ch03.py`.
- Create `build/prv_ch08.py`, `PAGES_SRC=24`, `BYLINE` same.

## D. Wire-up (after each chapter)
1. `build/prv_common.py` → add `7: "ch07-engineering-support"` (and `8: "ch08-asme-appendix"`) to
   `SLUGS["prv"]`.
2. `build/reader_book.py` → extend the `"done"` map for `"prv"` to include `7: …` / `8: …`.
3. `python3 build/reader_prv.py 7` (then `8`).
4. `python3 build/reader_book.py prv`  (TOC 8 rows / N done)
5. `python3 build/books_site.py`  (bump `TRANSLATED` `"pressure relief valve engineering handbook": ("progress", 8, N)` to 7 then 8)
6. `python3 build/make_sitemap.py`
7. `python3 build/check_links.py`  → must print **broken 0**
8. QA each page: 0 Spanish markers, `fig` count correct, `<figure>` present for each vector, `nav()`
   prev+TOC wired.
9. `git add -A && git commit -q -m "Book 4 Chapter N … (N/8)"`
10. `git push origin main` (with `dangerouslyDisableSandbox: true`).
11. Verify live + update `TRANSLATION-STATUS.md` (Session log) + `.workbuddy-ai/memory/YYYY-MM-DD.md`.

## E. Gotchas
- `h4(t, en="")` now accepts an optional EN subtitle (updated in `bolton_common.py`).
- `eq(body, num="")` renders `<div class="eq">`; build fractions with inline `border-bottom` spans or
  the `_fr()`/`_sq()` helpers used in `prv_ch05.py`.
- SVG `<defs>` ids are auto-namespaced — no manual id juggling needed.
- If `git push` is `SIGTERM`'d, the commit is already safe locally; just retry the push.
