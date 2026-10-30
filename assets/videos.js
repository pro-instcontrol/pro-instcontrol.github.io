/* Video library — search, level and source filters.
   The cards are already in the HTML; this file only hides and counts. */
(function () {
  "use strict";

  var search = document.getElementById("vsearch");
  var srcSel = document.getElementById("vsrc");
  var countEl = document.getElementById("vcount");
  var emptyEl = document.getElementById("vempty");
  var chips = [].slice.call(document.querySelectorAll(".vchip"));
  var sections = [].slice.call(document.querySelectorAll(".vid-sec"));
  var cards = [].slice.call(document.querySelectorAll(".vcard"));
  if (!cards.length) return;

  var total = cards.length;
  var level = "all";
  var tpl = countEl ? countEl.getAttribute("data-tpl") || "%d / %d" : "";
  var current = null;

  cards.forEach(function (c) {
    c._q = (c.getAttribute("data-q") || "").toLowerCase();
  });

  sections.forEach(function (s) {
    s._cards = [].slice.call(s.querySelectorAll(".vcard"));
    s._count = s.querySelector(".vcount");
    s._orig = s._count ? s._count.textContent : String(s._cards.length);
  });

  function apply() {
    var q = (search && search.value ? search.value : "").trim().toLowerCase();
    var src = srcSel ? srcSel.value : "all";
    var shown = 0;

    sections.forEach(function (s) {
      var vis = 0;
      s._cards.forEach(function (c) {
        var ok = (!q || c._q.indexOf(q) !== -1) &&
                 (level === "all" || c.getAttribute("data-level") === level) &&
                 (src === "all" || c.getAttribute("data-src") === src);
        c.classList.toggle("is-hide", !ok);
        if (ok) vis++;
      });
      shown += vis;
      s.hidden = vis === 0;
      if (s._count) s._count.textContent = vis === s._cards.length ? s._orig : vis + "/" + s._orig;
    });

    if (countEl) countEl.textContent = tpl.replace("%d", shown).replace("%d", total);
    if (emptyEl) emptyEl.hidden = shown !== 0;
  }

  function fmt() {
    if (!countEl) return;
    tpl = countEl.getAttribute("data-tpl") || "%d / %d";
  }

  if (search) {
    var t;
    search.addEventListener("input", function () {
      clearTimeout(t);
      t = setTimeout(apply, 90);
    });
    search.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { search.value = ""; apply(); }
    });
  }

  if (srcSel) srcSel.addEventListener("change", apply);

  [].slice.call(document.querySelectorAll(".vid-levels .pill")).forEach(function (b) {
    b.addEventListener("click", function () {
      [].slice.call(document.querySelectorAll(".vid-levels .pill")).forEach(function (x) {
        x.classList.remove("on");
      });
      b.classList.add("on");
      level = b.getAttribute("data-level") || "all";
      apply();
    });
  });

  /* "/" focuses search, the way a docs site does */
  document.addEventListener("keydown", function (e) {
    if (e.key !== "/" || e.metaKey || e.ctrlKey || e.altKey) return;
    var tag = (document.activeElement && document.activeElement.tagName) || "";
    if (/^(INPUT|TEXTAREA|SELECT)$/.test(tag)) return;
    e.preventDefault();
    if (search) search.focus();
  });

  /* active chip follows the section in view */
  if ("IntersectionObserver" in window) {
    var byId = {};
    chips.forEach(function (c) { byId[c.getAttribute("href").slice(1)] = c; });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var chip = byId[en.target.id];
        if (!chip || chip === current) return;
        if (current) current.classList.remove("on");
        chip.classList.add("on");
        current = chip;
        var box = document.getElementById("vchips");
        if (box && box.scrollWidth > box.clientWidth) {
          var left = chip.offsetLeft - box.offsetLeft - 40;
          if (Math.abs(box.scrollLeft - left) > 60) box.scrollTo({ left: left, behavior: "smooth" });
        }
      });
    }, { rootMargin: "-140px 0px -70% 0px", threshold: 0 });
    sections.forEach(function (s) { io.observe(s); });
  }

  /* mobile menu */
  var burger = document.getElementById("burger");
  if (burger) {
    burger.addEventListener("click", function () {
      var open = document.body.classList.toggle("menu-open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  fmt();
  apply();
})();
