"""Make inline-SVG ``<defs>`` (and other paint-server) IDs unique within each HTML page.

Problem
-------
Many reader pages embed dozens of inline SVG figures. Each figure module emits its own
``<defs>`` (sometimes markers/gradients without an explicit ``<defs>`` wrapper) with short
IDs such as ``ah28``, ``hatch28``, ``a1.3``. Because every figure redeclares the same IDs,
the page ends up with N duplicate ``id="ah28"`` attributes; N-1 are ignored by the browser.
The definitions are byte-identical so rendering is unaffected, but the HTML is invalid and
trips strict validators.

Fix
---
For each SVG (index k, document order) collect every ``id`` it declares. An id is
"namespaced" when it is either:

* referenced somewhere via ``url(#x)`` / ``href="#x"`` / ``xlink:href="#x"``, or
* declared in two or more different SVGs (a duplicate by construction).

Each declaring SVG gets the id renamed to ``x__sd<k>``. References are rewritten to point at
the *owning* SVG's suffixed id -- the same SVG when it declares the id, otherwise the first
SVG (document order) that declares it. This keeps cross-SVG references resolving (identical
defs), so nothing visually changes.

The transform is pure string surgery on ``<svg>…</svg>`` blocks. ids already carrying the
``__sdN`` marker are left untouched, which makes the function idempotent (safe to run more
than once, and safe to layer on top of ``framework.write()`` output). Section anchors like
``id="fig-28-59"`` live outside ``<svg>`` and are never touched.

Usage
-----
    from svg_ids import namespace_svg_ids
    html = namespace_svg_ids(html)
"""

import re

_SVG_RE = re.compile(r"<svg\b.*?</svg>", re.S | re.I)
_ID_RE = re.compile(r'\bid="([^"]+)"')

# Reference patterns that point at a def:
#   url(#x)  |  url( #x )  |  url('#x')  |  url("#x")
#   href="#x"  |  xlink:href="#x"
_URL_PAT = re.compile(r"url\(\s*['\"]?#([^)\s'\"]+)['\"]?\s*\)")
_HREF_PAT = re.compile(r'href="#([^"]+)"', re.I)
_XHREF_PAT = re.compile(r'xlink:href="#([^"]+)"', re.I)

# Already-namespaced marker; never re-suffix an id that already ends this way.
_SUFFIX_RE = re.compile(r"__sd\d+$")


def _ids_in(svg):
    """All ids declared anywhere inside this <svg> block."""
    return set(_ID_RE.findall(svg))


def _ref_ids_in(svg):
    t = set()
    for pat in (_URL_PAT, _HREF_PAT, _XHREF_PAT):
        for m in pat.finditer(svg):
            t.add(m.group(1))
    return t


def _ref_targets():
    """Reference-pattern -> replacement generator for one id."""
    return (
        (lambda x: "url(#%s)" % x, lambda x: "url(#%s)" % x),
        (lambda x: 'href="#%s"' % x, lambda x: 'href="#%s"' % x),
        (lambda x: 'xlink:href="#%s"' % x, lambda x: 'xlink:href="#%s"' % x),
    )


def namespace_svg_ids(html):
    """Return *html* with every inline-SVG defs ID made unique per SVG.

    Idempotent: already-namespaced ids are left alone, so re-running (or running on
    framework.write() output) is a no-op.
    """
    if "<svg" not in html:
        return html

    svgs = list(_SVG_RE.finditer(html))
    if not svgs:
        return html

    # ids declared per SVG, the first SVG (owner) that declares each id, and how many
    # SVGs declare it.
    ids_per = [_ids_in(m.group(0)) for m in svgs]
    owner = {}
    n_svgs = {}
    for k, ids in enumerate(ids_per):
        for x in ids:
            owner.setdefault(x, k)
            n_svgs[x] = n_svgs.get(x, 0) + 1

    referenced = set()
    for m in svgs:
        referenced |= _ref_ids_in(m.group(0))

    # An id is namespaced if it is referenced or duplicated across SVGs.
    rename = {x for x in referenced}
    for x, n in n_svgs.items():
        if n >= 2:
            rename.add(x)

    ref_forms = _ref_targets()

    out = []
    pos = 0
    for k, m in enumerate(svgs):
        out.append(html[pos:m.start()])
        svg = m.group(0)
        my_ids = ids_per[k]
        if not (rename & my_ids):
            out.append(svg)
            pos = m.end()
            continue

        new_svg = svg
        # 1) Rename this SVG's own declarations.
        for x in my_ids:
            if x in rename and not _SUFFIX_RE.search(x):
                new_svg = new_svg.replace('id="%s"' % x, 'id="%s__sd%d"' % (x, k))

        # 2) Rewrite references inside this SVG to the owning suffixed id.
        for x in _ref_ids_in(svg):
            if x not in rename or _SUFFIX_RE.search(x):
                continue
            # Referenced but declared nowhere in the document (pre-existing broken
            # reference, e.g. a marker id the figure module forgot to declare). Leave
            # it untouched rather than inventing a non-existent suffixed target.
            if x not in owner:
                continue
            tgt = "%s__sd%d" % (x, k if x in my_ids else owner[x])
            for find, repl in ref_forms:
                new_svg = new_svg.replace(find(x), repl(tgt))

        out.append(new_svg)
        pos = m.end()
    out.append(html[pos:])
    return "".join(out)
