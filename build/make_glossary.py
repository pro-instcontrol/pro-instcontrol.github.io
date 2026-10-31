# -*- coding: utf-8 -*-
"""Builds the site glossary from every book on the shelf.

Two sources, one index:

  * the curated site list in ``pages_glossary.TERMS`` — 52 control and
    instrumentation terms, already bilingual;
  * the ``<dl class="glossary">`` block of every translated handbook chapter,
    parsed out of the built pages so the glossary can never drift from what
    the chapters actually say.

Each entry carries both headwords and both definitions, so the English page
and the Vietnamese page show the same set in the same order, each in its own
language. Where a book term duplicates a curated one (calibration, accuracy,
repeatability, tolerance) the book becomes an extra source on the existing
entry rather than a second row.

Writes /glossary.html and /vi/glossary.html.
"""
import glob
import os
import re
import unicodedata

from books_site import head, header, esc
import framework
from framework import DIST
from pages_glossary import TERMS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HB = "the-measurement-instrumentation-and-sensors-handbook"

# chapter slug -> (english label, vietnamese label, chapter number, page slug)
SRC = {
    "ch05-measurement-standards":
        ("Ch. 5 · Measurement Standards", "Ch. 5 · Chuẩn đo lường", 5),
    "ch06-4-piezoelectric-transducers":
        ("Ch. 6.4 · Piezoelectric Transducers", "Ch. 6.4 · Đầu đo và cảm biến áp điện", 6),
    "ch06-5-laser-interferometer":
        ("Ch. 6.5 · Laser Interferometer", "Ch. 6.5 · Cảm biến dịch chuyển giao thoa laser", 6),
    "ch06-6-bore-gaging":
        ("Ch. 6.6 · Bore Gaging", "Ch. 6.6 · Cảm biến đo lỗ", 6),
}

SITE_EN = "Site glossary"
SITE_VI = "Bảng thuật ngữ của trang"

# Vietnamese headword -> (english headword, english definition).
# The Vietnamese definition is not repeated here: it is parsed from the
# chapter page, which is the only place it is written.
BOOK_EN = {
    # ---- Ch. 5, Measurement Standards (VIM 1993)
    "Độ chính xác của phép đo": (
        "Accuracy of measurement",
        "How close the result of a measurement comes to the true value of the quantity measured. "
        "A qualitative concept — it is not the same thing as precision."),
    "Hiệu chuẩn": (
        "Calibration",
        "The set of operations that establishes, under specified conditions, the relation between the "
        "values indicated by an instrument or measuring system and the corresponding values realised "
        "by a standard."),
    "Phòng thí nghiệm hiệu chuẩn": (
        "Calibration laboratory",
        "A workspace equipped with test gear, a controlled environment and trained staff, set up to "
        "keep measuring and test equipment working and accurate. It usually runs routine calibrations "
        "in production-line fashion."),
    "Vật liệu chuẩn được chứng nhận (CRM)": (
        "Certified reference material",
        "A reference material accompanied by a certificate in which one or more property values are "
        "certified by a procedure traceable to an exact realisation of the unit, each with a stated "
        "uncertainty."),
    "Đơn vị (đo) dẫn xuất nhất quán": (
        "Coherent derived unit",
        "A derived unit that can be expressed as a product of powers of base units with a "
        "proportionality factor of one."),
    "Hệ đơn vị (đo) nhất quán": (
        "Coherent system of units",
        "A system of units in which every derived unit is coherent."),
    "Bảo quản chuẩn (đo)": (
        "Conservation of a standard",
        "The operations needed to keep the metrological properties of a standard within appropriate "
        "limits: periodic calibration, storage under the right conditions, careful handling."),
    "Chuẩn liên phòng": (
        "Interlaboratory standard",
        "A device that travels between laboratories for the sole purpose of linking the size of the "
        "unit each laboratory maintains."),
    "Chuẩn (đo) quốc tế": (
        "International standard",
        "A standard recognised by international agreement as the international basis for assigning "
        "values to other standards of the quantity concerned."),
    "Hệ đơn vị Quốc tế (SI)": (
        "International System of Units",
        "The coherent system of units adopted and recommended by the General Conference on Weights and "
        "Measures; today built on seven base units."),
    "Đại lượng được đo": (
        "Measurand",
        "The particular quantity that is the subject of a measurement. Specifying it may require "
        "stating other quantities such as time, temperature and pressure."),
    "Phép đo": (
        "Measurement",
        "The set of operations carried out to determine the value of a quantity. The operations may be "
        "performed automatically."),
    "Phương pháp đo": (
        "Method of measurement",
        "A logical sequence of operations, described generically, used in performing a measurement — "
        "substitution, differential, null, and so on."),
    "Đo lường học": (
        "Metrology",
        "The science of measurement, covering every theoretical and practical aspect of measurement "
        "whatever its uncertainty and whatever field it appears in."),
    "Chuẩn (đo) quốc gia": (
        "National standard",
        "A standard recognised by a national decision as the basis, within a country, for assigning "
        "values to other standards of the quantity concerned."),
    "Chuẩn tham chiếu quốc gia": (
        "National reference standard",
        "A standard held at a national laboratory — NIST in the United States, NRC in Canada, NPL in "
        "Britain, PTB in Germany — and serving as that country's legal reference."),
    "Viện Tiêu chuẩn và Công nghệ Quốc gia (NIST)": (
        "NIST",
        "The United States national standards laboratory, responsible for maintaining the physical "
        "standards on which every American measurement rests."),
    "Chuẩn gốc": (
        "Primary standard",
        "A standard designated or widely acknowledged as having the highest metrological quality, "
        "whose value is accepted without reference to another standard of the same quantity."),
    "Nguyên lý đo": (
        "Principle of measurement",
        "The scientific basis of a measurement: thermoelectricity for temperature, the Josephson "
        "effect for voltage, the Doppler effect for velocity, the Raman effect for wavenumber."),
    "Chuẩn tham chiếu": (
        "Reference standard",
        "The standard, generally of the highest metrological quality available at a place or in an "
        "organisation, from which the measurements made there are derived."),
    "Vật liệu chuẩn": (
        "Reference material",
        "A material or substance whose property values are sufficiently homogeneous and well "
        "established to calibrate an instrument, validate a measurement method, or assign values to "
        "other materials."),
    "Độ lặp lại (của kết quả đo)": (
        "Repeatability",
        "How close the results of successive measurements of the same quantity are when made under the "
        "same conditions: same procedure, observer, instrument, place, and a short interval."),
    "Độ tái lập (của kết quả đo)": (
        "Reproducibility",
        "How close the results of measurements of the same quantity are when the measurement "
        "conditions have changed — principle, method, observer, instrument, reference standard, place, "
        "time."),
    "Chuẩn thứ cấp": (
        "Secondary standard",
        "A standard whose value is assigned by comparison with a primary standard of the same "
        "quantity."),
    "Phòng thí nghiệm chuẩn": (
        "Standards laboratory",
        "A workspace equipped with instruments, standards, a properly controlled environment and "
        "trained staff, set up to maintain the traceability of the standards an organisation uses. It "
        "makes fewer measurements than a calibration laboratory, but deeper and more accurate ones."),
    "Dung sai": (
        "Tolerance",
        "The permitted variation of a dimension, form or position — or, in metrology, the limits of "
        "the interval that applies to an instrument working correctly."),
    "Truy xuất nguồn gốc": (
        "Traceability",
        "The property of a measurement result whereby it can be related to stated references, usually "
        "national or international standards, through an unbroken chain of comparisons each with a "
        "stated uncertainty."),
    "Chuẩn chuyển tiếp": (
        "Transfer standard",
        "A standard used as an intermediary to compare other standards. Call the intermediary a "
        "transfer device when it is not itself a standard."),
    "Chuẩn lưu động": (
        "Traveling standard",
        "A standard, sometimes of special construction, intended for transport between locations — a "
        "battery-powered portable caesium frequency standard, for instance."),
    "Độ không đảm bảo đo": (
        "Uncertainty of measurement",
        "A parameter, associated with the result of a measurement, that characterises the dispersion "
        "of the values that could reasonably be attributed to the measurand."),
    "Giá trị (của một đại lượng)": (
        "Value of a quantity",
        "The magnitude of a particular quantity, generally expressed as a unit of measurement "
        "multiplied by a number: 5,34 m, or 0,152 kg."),
    "Chuẩn làm việc": (
        "Working standard",
        "A standard used routinely to calibrate or check material measures, measuring instruments or "
        "reference materials. Usually calibrated against a reference standard."),

    # ---- Ch. 6.4, piezoelectric transducers
    "Đầu đo áp điện": (
        "Piezoelectric transducer",
        "A device that converts applied electrical energy into mechanical energy, and back, by way of "
        "the piezoelectric effect."),
    "Hệ số liên kết": (
        "Coupling coefficient",
        "A material constant describing how well a piezoelectric material converts electrical energy "
        "into mechanical energy and back again."),
    "Hệ số áp điện": (
        "Piezoelectric coefficient",
        "A material constant describing the linear coupling between the electrical and the mechanical "
        "parameters of a piezoelectric material."),
    "Chất sắt điện": (
        "Ferroelectric",
        "The subclass of piezoelectric materials whose net dipole moment — the ferroelectric "
        "polarisation — can be reversed by a sufficiently strong electric field."),
    "Phân cực": (
        "Poling",
        "The process of orienting the ferroelectric polarisation in a single direction, the poling "
        "direction."),
    "Composite áp điện": (
        "Piezoelectric composite",
        "A material containing two or more constituents with different piezoelectric properties."),
    "Khuếch đại điện tích": (
        "Charge amplifier",
        "An operational amplifier that converts input charge into an output voltage by way of a "
        "capacitor in the feedback loop."),

    # ---- Ch. 6.5, laser interferometry
    "Kỹ thuật dị tần": (
        "Heterodyne technique",
        "Superimposing two harmonic signals of frequency f₁ and f₂ in a non-linear device to obtain a "
        "signal containing both the sum and the difference frequency."),
    "Giao thoa": (
        "Interference",
        "The phenomenon that most vividly demonstrates the wave nature of light; it occurs when "
        "radiation reaches the detector by more than one path from the source."),
    "Laser": (
        "Laser",
        "Light Amplification by Stimulated Emission of Radiation — a source whose gain comes from "
        "stimulated emission in a medium held in population inversion."),
    "Chiết suất": (
        "Refractive index",
        "The ratio of the speed of light in vacuum c to its speed in a medium. Always greater than "
        "one, since light slows in any material."),
    "Hiệu ứng Zeeman": (
        "Zeeman effect",
        "The splitting observed when excited atoms radiate inside a magnetic field: the longitudinal "
        "effect splits a single emission line symmetrically into two components."),

    # ---- Ch. 6.6, bore gaging
    "Kích thước": (
        "Size",
        "The numerical value, expressed in a suitable unit and written on a drawing by lines, symbols "
        "and notes, that defines the geometric features of an object."),
    "Lắp": (
        "Fit",
        "The general term for the degree of tightness or looseness that arises when a given "
        "combination of tolerances and clearances is applied to mating parts."),
    "Hệ giới hạn và lắp ghép ISO": (
        "ISO limits and fits",
        "A standardised system of limits and fits: a set of tolerances held to correspond to the same "
        "level of accuracy for every basic size."),
    "Căn": (
        "Gauge block",
        "A device used to survey how well the size of a part suits its specified function."),
    "Kiểm bằng căn": (
        "Gauge-block inspection",
        "Measuring manufactured material to ensure the dimensional uniformity and envelope that "
        "industry requires."),
}

# book headword -> curated english headword, for the four terms that are the
# same concept under a longer name in the chapter
ALIAS = {
    "Độ chính xác của phép đo": "Accuracy",
    "Hiệu chuẩn": "Calibration",
    "Độ lặp lại (của kết quả đo)": "Repeatability",
}


# ---------------------------------------------------------------- parsing
def strip_tags(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip()


def norm(s):
    """Sort key: đ folded to d, diacritics dropped, lower case."""
    s = s.replace("đ", "d").replace("Đ", "D")
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s.lower()


def read_chapters():
    """[(chapter slug, vi headword, vim ref, vi definition html)]"""
    out = []
    pat = os.path.join(ROOT, "vi", "books", "read", HB, "*", "index.html")
    for path in sorted(glob.glob(pat)):
        slug = os.path.basename(os.path.dirname(path))
        if slug not in SRC:
            continue
        h = open(path, encoding="utf-8").read()
        m = re.search(r'<dl class="glossary">(.*?)</dl>', h, re.S)
        if not m:
            continue
        for dt, dd in re.findall(r"<dt>(.*?)</dt>\s*<dd>(.*?)</dd>", m.group(1), re.S):
            vim = ""
            vm = re.search(r'<span class="vim">\[?([^\]<]+)\]?</span>', dt)
            if vm:
                vim = vm.group(1).strip()
            name = strip_tags(re.sub(r'<span class="vim">.*?</span>', "", dt))
            out.append((slug, name, vim, dd.strip()))
    return out


def build_entries():
    """[(en, vi, def_en, def_vi, [(label_en, label_vi, href)])]"""
    entries = []
    by_en = {}
    for en, vi, d_en, d_vi in TERMS:
        e = {"en": en, "vi": vi, "de": d_en, "dv": d_vi, "src": [], "curated": True}
        entries.append(e)
        by_en[norm(en)] = e

    for slug, vi_name, vim, dd in read_chapters():
        meta = SRC[slug]
        href = "/vi/books/read/%s/%s/" % (HB, slug)
        src = (meta[0], meta[1], href)
        target = ALIAS.get(vi_name, BOOK_EN.get(vi_name, (None, None))[0])
        if target and norm(target) in by_en:
            e = by_en[norm(target)]
            if src not in e["src"]:
                e["src"].append(src)
            continue
        pair = BOOK_EN.get(vi_name)
        if not pair:
            continue
        en, d_en = pair
        if vim:
            d_en = d_en + " (VIM %s)" % vim
        e = {"en": en, "vi": vi_name, "de": d_en, "dv": dd, "src": [src]}
        entries.append(e)
        by_en[norm(en)] = e
    return entries


# ---------------------------------------------------------------- page
CSS = """<style>
.gw{max-width:860px;margin:0 auto;padding:0 24px 96px}
.ghero{padding:56px 0 8px;text-align:center}
.ghero h1{font-family:'Cormorant Garamond',Georgia,serif;font-weight:500;font-size:2.6rem;
  margin:.2em 0 .1em;letter-spacing:.01em}
.ghero .crumb{font-size:.76rem;letter-spacing:.14em;text-transform:uppercase;color:#9a8f7a}
.ghero .lede{max-width:640px;margin:14px auto 0;color:#4a4a4a;font-size:1.02rem;line-height:1.65}
.ghero .meta-line{margin-top:14px;font-size:.74rem;letter-spacing:.13em;text-transform:uppercase;
  color:#a39a8b}
.gtools{position:sticky;top:0;z-index:5;background:rgba(255,255,255,.96);
  border-bottom:1px solid #ece7dd;padding:12px 0 10px;margin-bottom:8px}
.gsearch{display:flex;align-items:center;gap:10px;border:1px solid #e2dcd0;border-radius:8px;
  padding:9px 12px;background:#fbf9f5}
.gsearch input{flex:1;border:0;outline:0;background:transparent;font:inherit;font-size:.95rem}
.gcount{font-size:.78rem;color:#8d8375;white-space:nowrap}
.gaz{display:flex;flex-wrap:wrap;gap:4px;margin-top:9px}
.gaz button{border:1px solid transparent;background:none;font:inherit;font-size:.78rem;
  letter-spacing:.04em;color:#8d8375;padding:3px 7px;border-radius:5px;cursor:pointer}
.gaz button:hover{background:#f3efe7;color:#5a4a2a}
.gletter{font-family:'Cormorant Garamond',Georgia,serif;font-size:1.5rem;font-weight:600;
  color:#b45309;margin:34px 0 2px;padding-bottom:6px;border-bottom:1px solid #eee7da}
.gentry{padding:15px 0 13px;border-bottom:1px solid #f4f0e8}
.gentry:last-child{border-bottom:0}
.gh{display:flex;flex-wrap:wrap;align-items:baseline;gap:10px;margin-bottom:5px}
.gh b{font-size:1.02rem;font-weight:600;color:#1d1d1d;letter-spacing:.005em}
.gh .gv{font-size:.92rem;color:#8a7f6c;font-style:italic}
.gd{margin:0;font-size:.93rem;line-height:1.62;color:#3d3d3d}
.gd .note{margin-top:6px;font-size:.86rem;color:#6b6b6b}
.gs{margin-top:6px;font-size:.74rem;letter-spacing:.04em;color:#a89e8c}
.gs a{color:#a8894f;text-decoration:none;border-bottom:1px solid #e6dcc6}
.gs a:hover{border-bottom-color:#b45309;color:#b45309}
.gempty{display:none;padding:40px 0;text-align:center;color:#8d8375;font-size:.95rem}
.gchain{display:flex;justify-content:space-between;gap:20px;margin-top:54px;padding-top:24px;
  border-top:1px solid #e8e2d6}
.gchain a{text-decoration:none;border-bottom:none;font-size:.93rem;font-weight:500;color:#1d1d1d}
.gchain a:hover{border-bottom:none;color:#b45309}
.gchain .k{display:block;font-size:.66rem;letter-spacing:.12em;text-transform:uppercase;
  color:#9a8f7a;margin-bottom:.15rem}
@media (max-width:640px){.ghero h1{font-size:2.05rem}.gw{padding:0 16px 64px}}
</style>"""

JS = """<script>
(function(){
  var q=document.getElementById('gq'), list=document.getElementById('glist'),
      cnt=document.getElementById('gcount'), empty=document.getElementById('gempty'),
      total=list.querySelectorAll('.gentry').length;
  function apply(){
    var s=q.value.toLowerCase().trim(), shown=0, last=null;
    var nodes=list.children;
    for(var i=0;i<nodes.length;i++){
      var n=nodes[i];
      if(n.classList.contains('gletter')){ last=n; n.style.display='none'; continue; }
      var hit = !s || (n.getAttribute('data-s')||'').indexOf(s)>-1;
      n.style.display = hit?'':'none';
      if(hit){ shown++; if(last){ last.style.display=''; last=null; } }
    }
    cnt.textContent = shown+' / '+total;
    empty.style.display = shown?'none':'block';
  }
  q.addEventListener('input', apply);
  document.querySelectorAll('.gaz button').forEach(function(b){
    b.addEventListener('click', function(){
      q.value=''; apply();
      var t=document.getElementById('l-'+b.dataset.l);
      if(t) t.scrollIntoView({behavior:'smooth',block:'start'});
    });
  });
  apply();
})();
</script>"""


def sort_key(s, vi=False):
    """đ sorts after d, as Vietnamese convention expects."""
    k = s.replace("đ", "dz").replace("Đ", "Dz")
    k = unicodedata.normalize("NFD", k)
    k = "".join(c for c in k if unicodedata.category(c) != "Mn")
    return k.lower()


def letter_of(s, vi=False):
    if not s:
        return "#"
    c = s[0].upper()
    if vi and c == "Đ":
        return "Đ"
    k = norm(s)
    if not k:
        return "#"
    c = k[0].upper()
    return c if c.isalpha() else "#"


def render(lang, entries):
    vi = lang == "vi"
    rows = []
    for e in entries:
        head_main = e["vi"] if vi else e["en"]
        head_alt = e["en"] if vi else e["vi"]
        body = e["dv"] if vi else e["de"]
        if not body:
            body = ""
        srcs = []
        for lab_en, lab_vi, href in e["src"]:
            lab = lab_vi if vi else lab_en
            if href:
                srcs.append('<a href="%s">%s</a>' % (href, esc(lab)))
            else:
                srcs.append(esc(lab))
        if not srcs:
            srcs = [SITE_VI if vi else SITE_EN]
        elif e["src"] and e.get("curated"):
            # a curated entry that a chapter also defines: say both
            srcs.insert(0, SITE_VI if vi else SITE_EN)
        blob = norm(" ".join([e["en"], e["vi"], strip_tags(e["dv"] or ""),
                              strip_tags(e["de"] or "")]))
        rows.append((head_main, head_alt, body, " · ".join(srcs), blob))

    rows.sort(key=lambda r: sort_key(r[0], vi))

    out = []
    cur = None
    for h_main, h_alt, body, src, blob in rows:
        L = letter_of(h_main, vi)
        if L != cur:
            cur = L
            out.append('<h2 class="gletter" id="l-%s">%s</h2>' % (L, L))
        out.append(
            '<div class="gentry" data-s="%s"><div class="gh"><b>%s</b>'
            '<span class="gv">%s</span></div><div class="gd">%s</div>'
            '<div class="gs">%s</div></div>'
            % (esc(blob), h_main, h_alt, body, src))

    letters = []
    seen = []
    for r in rows:
        L = letter_of(r[0], vi)
        if L not in seen:
            seen.append(L)
    for L in seen:
        letters.append('<button data-l="%s">%s</button>' % (L, L))

    n_terms = len(rows)
    n_book = sum(1 for e in entries if e["src"])
    title = ("Thuật ngữ — toàn bộ sách trong thư viện" if vi
             else "Glossary — every term the books define")
    desc = ("Toàn bộ thuật ngữ được định nghĩa trong các sách của thư viện, kèm bản dịch và nguồn."
            if vi else
            "Every term defined in the books on the shelf, with the Vietnamese headword and the "
            "chapter it comes from.")
    lede = ("Mọi thuật ngữ mà các sách trong thư viện định nghĩa, gộp lại một chỗ: %d mục, trong đó "
            "%d mục lấy trực tiếp từ phần “Định nghĩa thuật ngữ” của các chương, phần còn lại từ bảng "
            "thuật ngữ của trang. Tìm được bằng cả hai thứ tiếng." % (n_terms, n_book)
            if vi else
            "Every term the books on the shelf define, in one place: %d entries, %d of them lifted "
            "from the “Defining Terms” sections of the chapters and the rest from the site's own "
            "control glossary. Search works in either language." % (n_terms, n_book))
    meta = ("%d thuật ngữ · %d lấy từ các chương · 4 sách" % (n_terms, n_book) if vi
            else "%d terms · %d taken from the chapters · 4 books" % (n_terms, n_book))
    crumb = ('<a href="/vi/books/">Sách</a> · Thuật ngữ' if vi
             else '<a href="/books/">Books</a> · Glossary')

    switch = "/vi/glossary.html" if not vi else "/glossary.html"
    body = (
        '<main><div class="gw">'
        '<div class="ghero"><div class="crumb">%s</div><h1>%s</h1>'
        '<p class="lede">%s</p><div class="meta-line">%s</div></div>'
        '<div class="gtools"><div class="gsearch">'
        '<input id="gq" type="search" placeholder="%s" aria-label="%s">'
        '<span class="gcount" id="gcount"></span></div>'
        '<div class="gaz">%s</div></div>'
        '<div id="glist">%s</div><div class="gempty" id="gempty">%s</div>'
        '%s'
        '</div></main>'
        % (crumb, "Thuật ngữ" if vi else "Glossary", lede, meta,
           "Tìm thuật ngữ…" if vi else "Search terms…",
           "Tìm thuật ngữ" if vi else "Search terms",
           "".join(letters), "".join(out),
           "Không tìm thấy thuật ngữ nào." if vi else "No term matches that search.",
           framework.nextprev_plain(lang, "glossary.html", "/",
                                    cls="nextprev gchain"))
    )
    return (head(lang, title, desc) + CSS + header(lang, active_books=False, switch_href=switch)
            + body + JS + "</body></html>")


def build_all():
    """Writes to dist/ and to the site root.

    build.py emits into dist/ and the tree is then copied up, so the glossary
    has to exist in both places or the copy would put back a stale page.
    """
    entries = build_entries()
    for lang, rel in (("en", "glossary.html"), ("vi", os.path.join("vi", "glossary.html"))):
        page = render(lang, entries)
        for base in (DIST, ROOT):
            path = os.path.join(base, rel)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            open(path, "w", encoding="utf-8").write(page)
        print("wrote %s  %d entries  %d kB" % (rel, len(entries), len(page) // 1024))


if __name__ == "__main__":
    build_all()
