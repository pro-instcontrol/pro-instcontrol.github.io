/* Bilingual engine + page interactions. No dependencies. */
(function () {
  "use strict";

  var DICT = window.I18N || {};
  var META = window.I18N_META || {};
  var KEY = "pic-lang";

  function stored() {
    try { return localStorage.getItem(KEY); } catch (e) { return null; }
  }
  function save(l) {
    try { localStorage.setItem(KEY, l); } catch (e) {}
  }
  function initial() {
    var m = /[?&]lang=(en|vi)/.exec(location.search);
    if (m) return m[1];
    var s = stored();
    if (s === "en" || s === "vi") return s;
    var n = (navigator.language || "en").toLowerCase();
    return n.indexOf("vi") === 0 ? "vi" : "en";
  }

  var lang = initial();

  function apply(l) {
    lang = l;
    document.documentElement.lang = l;

    var nodes = document.querySelectorAll("[data-i18n]");
    for (var i = 0; i < nodes.length; i++) {
      var el = nodes[i];
      var entry = DICT[el.getAttribute("data-i18n")];
      if (!entry) continue;
      var val = entry[l];
      if (val == null) continue;
      var attr = el.getAttribute("data-i18n-attr");
      if (attr) {
        el.setAttribute(attr, val);
      } else if (el.innerHTML !== val) {
        el.innerHTML = val;
      }
    }

    if (META.title && META.title[l]) document.title = META.title[l];
    var md = document.querySelector('meta[name="description"]');
    if (md && META.desc && META.desc[l]) md.setAttribute("content", META.desc[l]);

    var opts = document.querySelectorAll(".lang-opt");
    if (opts.length === 2) {
      opts[0].className = "lang-opt" + (l === "en" ? " on" : "");
      opts[1].className = "lang-opt" + (l === "vi" ? " on" : "");
    }
    var btn = document.getElementById("lang");
    if (btn) btn.setAttribute("aria-label", l === "en" ? "Chuyển sang tiếng Việt" : "Switch to English");

    document.dispatchEvent(new CustomEvent("langchange", { detail: l }));
  }

  document.addEventListener("DOMContentLoaded", function () {
    apply(lang);

    var btn = document.getElementById("lang");
    if (btn) {
      btn.addEventListener("click", function () {
        var next = lang === "en" ? "vi" : "en";
        save(next);
        apply(next);
      });
    }

    var burger = document.getElementById("burger");
    if (burger) {
      burger.addEventListener("click", function () {
        var open = document.body.classList.toggle("menu-open");
        burger.setAttribute("aria-expanded", open ? "true" : "false");
      });
    }

    initFilters();
    initGlossary();
    initSim();
  });

  /* ---------------- instrument filter ---------------- */
  function initFilters() {
    var box = document.getElementById("inst-table");
    if (!box) return;
    var rows = Array.prototype.slice.call(box.querySelectorAll("tbody tr"));
    var pills = Array.prototype.slice.call(document.querySelectorAll(".pill[data-fam]"));
    var input = document.getElementById("inst-search");
    var count = document.getElementById("inst-count");
    var fam = "all";

    function run() {
      var q = (input && input.value || "").toLowerCase().trim();
      var shown = 0;
      rows.forEach(function (r) {
        var okFam = fam === "all" || r.getAttribute("data-fam") === fam;
        var okQ = !q || r.textContent.toLowerCase().indexOf(q) > -1;
        var show = okFam && okQ;
        r.style.display = show ? "" : "none";
        if (show) shown++;
      });
      if (count) count.textContent = shown + " / " + rows.length;
    }

    pills.forEach(function (p) {
      p.addEventListener("click", function () {
        pills.forEach(function (x) { x.classList.remove("on"); });
        p.classList.add("on");
        fam = p.getAttribute("data-fam");
        run();
      });
    });
    if (input) input.addEventListener("input", run);
    document.addEventListener("langchange", run);
    run();
  }

  /* ---------------- glossary search ---------------- */
  function initGlossary() {
    var box = document.getElementById("gloss-list");
    if (!box) return;
    var items = Array.prototype.slice.call(box.querySelectorAll(".gitem"));
    var input = document.getElementById("gloss-search");
    var count = document.getElementById("gloss-count");
    if (!input) return;

    function run() {
      var q = input.value.toLowerCase().trim();
      var shown = 0;
      items.forEach(function (it) {
        var show = !q || it.textContent.toLowerCase().indexOf(q) > -1;
        it.style.display = show ? "" : "none";
        if (show) shown++;
      });
      if (count) count.textContent = shown + " / " + items.length;
    }
    input.addEventListener("input", run);
    document.addEventListener("langchange", run);
    run();
  }

  /* ---------------- PID loop simulator ---------------- */
  function initSim() {
    var canvas = document.getElementById("pid-canvas");
    if (!canvas) return;

    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var W = 760, H = 380;
    canvas.width = W * dpr;
    canvas.height = H * dpr;
    canvas.style.aspectRatio = W + " / " + H;
    var ctx = canvas.getContext("2d");
    ctx.scale(dpr, dpr);

    var ids = { kp: "s-kp", ti: "s-ti", td: "s-td", dl: "s-dl", tc: "s-tc" };
    var vals = { kp: 1.4, ti: 9, td: 0, dl: 2, tc: 6 };

    function read() {
      Object.keys(ids).forEach(function (k) {
        var el = document.getElementById(ids[k]);
        if (el) vals[k] = parseFloat(el.value);
      });
    }

    var result = null;

    function simulate() {
      var dt = 0.1, total = 150, spLow = 40, spHigh = 62, tStep = 5;
      var T = Math.max(vals.tc, 0.5);
      var L = vals.dl;
      var Kp = vals.kp, Ti = vals.ti, Td = vals.td;
      var pv = spLow, integ = 0, pvPrev = pv, u = spLow;
      var BIAS = spLow; // manual reset: output that holds the process at its start value
      var delayLen = Math.max(1, Math.round(L / dt));
      var buf = new Array(delayLen).fill(BIAS); // pipe is already full of fluid at steady state
      var n = Math.round(total / dt);
      var sp = new Array(n), pvv = new Array(n), uu = new Array(n);
      var iae = 0, maxPv = -1e9, settle = total;

      for (var i = 0; i < n; i++) {
        var t = i * dt;
        var s = t >= tStep ? spHigh : spLow;
        var e = s - pv;
        var deriv = (pv - pvPrev) / dt;
        var out = BIAS + Kp * (e + (Ti > 0 ? integ / Ti : 0) - Td * deriv);
        if (out > 100) out = 100;
        if (out < 0) out = 0;
        u = out;

        buf.push(u);
        var uDel = buf.shift();

        pvPrev = pv;
        pv = pv + (dt / T) * (uDel - pv);
        if (Ti > 0) integ += e * dt;
        if (Math.abs(integ) > 1e6) integ = 0;

        sp[i] = s; pvv[i] = pv; uu[i] = u;
        iae += Math.abs(e) * dt;
        if (pv > maxPv) maxPv = pv;
      }

      var os = ((maxPv - spHigh) / spHigh) * 100;
      if (os < 0) os = 0;
      var band = 0.02 * spHigh;
      for (var j = n - 1; j >= 0; j--) {
        if (Math.abs(pvv[j] - spHigh) > band) { settle = j * dt - tStep; break; }
      }
      if (settle < 0) settle = 0;
      result = { sp: sp, pv: pvv, u: uu, n: n, dt: dt, total: total, os: os, settle: settle, iae: iae };
      draw();
      report();
    }

    function css(name, fallback) {
      var v = getComputedStyle(document.documentElement).getPropertyValue(name).trim();
      return v || fallback;
    }

    function draw() {
      if (!result) return;
      var padL = 44, padR = 14, padT = 16, padB = 30;
      var w = W - padL - padR, h = H - padT - padB;
      var ink = css("--ink", "#0b1725");
      var line = css("--line", "#e4eaf1");
      var accent = css("--accent", "#0d7a6f");
      var muted = css("--muted", "#66788d");
      var amber = css("--amber", "#a85a06");

      ctx.clearRect(0, 0, W, H);

      // grid
      ctx.strokeStyle = line;
      ctx.lineWidth = 1;
      ctx.font = "10px 'IBM Plex Mono', monospace";
      ctx.fillStyle = muted;
      for (var g = 0; g <= 100; g += 20) {
        var y = padT + h - (g / 100) * h;
        ctx.beginPath();
        ctx.moveTo(padL, y);
        ctx.lineTo(padL + w, y);
        ctx.stroke();
        ctx.fillText(String(g), 12, y + 3);
      }
      for (var tSec = 0; tSec <= result.total; tSec += 30) {
        var x = padL + (tSec / result.total) * w;
        ctx.beginPath();
        ctx.moveTo(x, padT);
        ctx.lineTo(x, padT + h);
        ctx.stroke();
        ctx.fillText(tSec + "s", x - 6, H - 10);
      }

      function px(i) { return padL + (i / (result.n - 1)) * w; }
      function py(v) { return padT + h - (Math.max(0, Math.min(100, v)) / 100) * h; }

      // setpoint
      ctx.strokeStyle = amber;
      ctx.setLineDash([5, 4]);
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      for (var i = 0; i < result.n; i += 4) {
        if (i === 0) ctx.moveTo(px(i), py(result.sp[i]));
        else ctx.lineTo(px(i), py(result.sp[i]));
      }
      ctx.stroke();
      ctx.setLineDash([]);

      // controller output (faint)
      ctx.strokeStyle = "rgba(102,120,141,.35)";
      ctx.lineWidth = 1;
      ctx.beginPath();
      for (var k = 0; k < result.n; k += 2) {
        if (k === 0) ctx.moveTo(px(k), py(result.u[k]));
        else ctx.lineTo(px(k), py(result.u[k]));
      }
      ctx.stroke();

      // process variable
      ctx.strokeStyle = accent;
      ctx.lineWidth = 2.1;
      ctx.lineJoin = "round";
      ctx.beginPath();
      for (var m = 0; m < result.n; m++) {
        if (m === 0) ctx.moveTo(px(m), py(result.pv[m]));
        else ctx.lineTo(px(m), py(result.pv[m]));
      }
      ctx.stroke();

      // legend
      ctx.font = "10.5px 'IBM Plex Mono', monospace";
      ctx.fillStyle = accent;
      ctx.fillText("PV", padL + 8, padT + 12);
      ctx.fillStyle = amber;
      ctx.fillText("SP", padL + 40, padT + 12);
      ctx.fillStyle = muted;
      ctx.fillText("MV", padL + 72, padT + 12);

      // axis frame
      ctx.strokeStyle = css("--line2", "#ccd7e3");
      ctx.lineWidth = 1;
      ctx.strokeRect(padL, padT, w, h);
    }

    function report() {
      if (!result) return;
      var a = document.getElementById("m-os");
      var b = document.getElementById("m-settle");
      var c = document.getElementById("m-iae");
      var d = document.getElementById("m-mv");
      if (a) a.textContent = result.os.toFixed(1) + " %";
      if (b) b.textContent = result.settle.toFixed(1) + " s";
      if (c) c.textContent = Math.round(result.iae).toString();
      if (d) d.textContent = Math.round(result.u[result.n - 1]) + " %";
    }

    var raf = null;
    function schedule() {
      if (raf) return;
      raf = requestAnimationFrame(function () {
        raf = null;
        read();
        simulate();
      });
    }

    Object.keys(ids).forEach(function (k) {
      var el = document.getElementById(ids[k]);
      if (!el) return;
      var out = document.getElementById("o-" + k);
      function sync() { if (out) out.textContent = el.value; }
      el.addEventListener("input", function () { sync(); schedule(); });
      sync();
    });

    var presets = document.querySelectorAll("[data-preset]");
    Array.prototype.forEach.call(presets, function (p) {
      p.addEventListener("click", function () {
        var v = p.getAttribute("data-preset");
        var set = { kp: 1.4, ti: 9, td: 0 };
        if (v === "p") set = { kp: 2.2, ti: 0, td: 0 };
        if (v === "pi") set = { kp: 1.4, ti: 9, td: 0 };
        if (v === "pid") set = { kp: 1.8, ti: 6, td: 1.4 };
        if (v === "aggr") set = { kp: 6, ti: 4, td: 0 };
        Object.keys(set).forEach(function (k) {
          var el = document.getElementById(ids[k]);
          if (el) { el.value = set[k]; }
          var out = document.getElementById("o-" + k);
          if (out) out.textContent = el ? el.value : "";
        });
        schedule();
      });
    });

    document.addEventListener("langchange", function () { draw(); });
    read();
    simulate();
  }
})();
