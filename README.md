# Instrumentation &amp; Control — a bilingual field guide

A static, bilingual (English / Tiếng Việt) reference site for **process instrumentation and
control**, with a companion section on **geotechnical monitoring** and a structured comparison
between the two disciplines.

Live: https://pro-instcontrol.github.io/

---

## What is in here

| Page | Contents |
|---|---|
| `index.html` | Positioning, the closed-loop idea, five measurement families, the dividing line |
| `fundamentals.html` | Measurement chain, signal standards, 4–20 mA, error vocabulary, environment, installation rules |
| `advanced/` | Where the fundamentals stop: cascade / feedforward / MPC, the safety paper trail, a 12-video **Trends & standards watch** section linking into the library, and the **total-plant** layer stack from field device to boardroom — with what the vendor numbers are worth (VI mirror at `vi/advanced/`) |
| `instruments.html` | 31 filterable instruments — principle, accuracy, best application, failure mode |
| `install.html` | Tapping points and impulse lines by service, hazardous area zones and gas groups, the IS entity concept with a cable-length calculation, grounding and shielding, commissioning checks |
| `control.html` | Loop anatomy, PID terms, six tuning methods, dead time, advanced strategies, an interactive PID simulator |
| `applications.html` | Boiler control, power-plant C&I, oil refining, food & beverage — then the one dominant variable in each of the seven sectors those four leave out (water, mining, pulp & paper, pharma, cement, hydrogen, biomass) |
| `safety.html` | SIS vs BPCS, the IEC 61511 lifecycle, what SIL bounds, redundancy and the common-cause floor, proof test coverage, independence, six ways a safety system stops being one |
| `tools.html` | Five live calculators — 4–20 mA scaling with NE 43 bands, DP flow square root, valve Kv/Cv with choked flow, hydrostatic level, loop error budget |
| `comparison.html` | The 21-row process-vs-geotechnical matrix, controllability conditions, hybrid cases, vocabulary traps |
| `geotechnical.html` | Observational method, ISO 18674 series, 12 sensor families, vibrating wire vs 4–20 mA, field failures |
| `standards.html` | ISA / IEC / API / ISO / CEN index with what each one governs |
| `glossary.html` | 52 bilingual terms with live search |
| `video-library/` | 214 curated videos across 21 topics, a six-stage learning path, and search / level / source filters (VI mirror at `vi/video-library/`) |

## How the bilingual system works

There is no runtime build step and no server. Every translatable leaf element carries a key:

```html
<h2 data-i18n="cmp.31">Twenty-one lines that separate the disciplines</h2>
```

The paired strings for that page are serialised once into the document:

```js
window.I18N = { "cmp.31": { "en": "...", "vi": "..." }, ... };
```

`assets/app.js` swaps `innerHTML` for every `[data-i18n]` node, updates `<html lang>`, the
document title and meta description, and remembers the choice in `localStorage`.

- Toggle: the `EN / VI` button in the header.
- Shareable link: append `?lang=vi` (or `?lang=en`) to any page.
- Attribute strings (placeholders, aria-labels) use `data-i18n-attr="placeholder"`.
- Elements whose text is generated at runtime (simulator readouts) keep the value outside the
  translated node.

Three sections exist twice as **real URLs** rather than as swapped text — `/books/`,
`/video-library/` and `/advanced/`, each with a `/vi/` twin. `app.js` retargets those three nav
links on every language change (`retargetNav`, the `TWINS` map), so a reader who has switched to
Tiếng Việt stays in the Vietnamese tree instead of being dropped back into English. The pages
themselves use a plain `<a class="lang">` link to the sibling URL, because a JS swap cannot change
the address bar.

## Editing content

Content lives in Python modules under `build/`, one pair of strings per element:

```python
pg.p("English text", "Văn bản tiếng Việt")
pg.h3("Heading", "Tiêu đề")
pg.span("Label", "Nhãn")
```

`Page.el()` registers the pair and returns markup in English; Vietnamese is applied client-side.
Keys are generated sequentially per page (`fun.1`, `fun.2`, …) so nothing has to be named by hand.

```bash
python build/build.py     # writes ./dist
```

Then publish the contents of `dist/` to the repository root (the served site) and commit.

## Structure

```
build/
  framework.py      page shell, i18n registry, layout helpers, tidy()
  pages_home.py     index
  pages_core.py     fundamentals + instrument table
  pages_install.py  installation, hazardous area, commissioning
  pages_control.py  control, block diagram, simulator markup
  pages_advanced.py advanced practice (EN + VI pages, links into the library)
  pages_safety.py   safety instrumented systems, SIL, proof test
  pages_tools.py    five engineering calculators
  pages_compare.py  the comparison matrix
  pages_ref.py      geotechnical + standards
  pages_glossary.py glossary
  pages_videos.py   video library (EN + VI pages)
  videos_data.py    the curated video dataset
  check_videos.py   dataset + dead-link check for the library
  make_og.py        renders the library share card from the dataset
  build.py          entry point
assets/
  style.css         design system (light theme, P&ID-inspired)
  app.js            language engine, filters, glossary search, PID simulator, calculators
  videos.js         video library search / level / source filters
  favicon.svg
dist/               generated output (not committed)
```

## Video library

`/video-library/` and `/vi/video-library/` are two static pages generated from
`build/videos_data.py`. Each entry carries an id, one primary category, a level, a
duration, the source channel and a one-line editorial note in both languages.

- Sourced from the supplied Instrumentation & Control playlist, the @InstruNexus
  channel, manufacturer / standards-body channels, and Vietnamese-language channels.
- Cards are written into the HTML at build time, so the library reads without
  JavaScript; `assets/videos.js` only adds search, level and source filtering.
- Durations and titles come from the YouTube metadata; commercial and pricing
  videos from the source channels were left out.
- A six-stage learning path (`PATH` in `pages_videos.py`) gives a beginner an
  order; each entry links to `#v-<id>`, and the targeted card highlights.
- `python build/check_videos.py` validates the dataset (duplicate ids, unknown
  categories, bad durations) and checks every link through YouTube oEmbed.
  `--offline` skips the network pass. Exits 1 on any failure, so it can gate a push.
- The 21st category, **Trends & standards watch** (`trends`), is linked from
  `/advanced/` and `/vi/advanced/` at `#cat-trends` — that page is the entry point
  for a reader who has not yet met Ethernet-APL or OPC UA FX.
- The share card is `assets/og-video-library.png`, referenced from both pages. It is
  rendered by `python build/make_og.py`, which reads the headline stats (videos,
  topics, hours, sources) straight from the dataset — rerun it whenever content
  changes so the card cannot drift from the page.

## Design notes

- Light theme only, system font stack with Inter / IBM Plex Mono loaded from Google Fonts.
- No framework, no bundler, no dependencies. Roughly 21 kB of CSS and 17 kB of JS.
- Diagrams are hand-written inline SVG so they inherit the palette and stay crisp at any size.
- The simulator is a first-order-plus-dead-time plant with a PID controller, simulated at
  dt = 0.1 s for 150 s on every slider change.

## Standards caveat

The standards index is a reading aid, not a substitute for the documents. Editions move —
confirm the current edition (for example ISO 18674-6 is still a draft, and ISO 18674-7 was
published in 2025) before citing anything in a specification.

## License

Content is provided for reference and training. Verify against the applicable standard and
project specification before design use.
