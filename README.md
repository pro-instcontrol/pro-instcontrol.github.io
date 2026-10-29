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
| `instruments.html` | 31 filterable instruments — principle, accuracy, best application, failure mode |
| `control.html` | Loop anatomy, PID terms, six tuning methods, dead time, advanced strategies, an interactive PID simulator |
| `tools.html` | Five live calculators — 4–20 mA scaling with NE 43 bands, DP flow square root, valve Kv/Cv with choked flow, hydrostatic level, loop error budget |
| `comparison.html` | The 21-row process-vs-geotechnical matrix, controllability conditions, hybrid cases, vocabulary traps |
| `geotechnical.html` | Observational method, ISO 18674 series, 12 sensor families, vibrating wire vs 4–20 mA, field failures |
| `standards.html` | ISA / IEC / API / ISO / CEN index with what each one governs |
| `glossary.html` | 52 bilingual terms with live search |

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
  pages_control.py  control, block diagram, simulator markup
  pages_tools.py    five engineering calculators
  pages_compare.py  the comparison matrix
  pages_ref.py      geotechnical + standards
  pages_glossary.py glossary
  build.py          entry point
assets/
  style.css         design system (light theme, P&ID-inspired)
  app.js            language engine, filters, glossary search, PID simulator, calculators
  favicon.svg
dist/               generated output (not committed)
```

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
