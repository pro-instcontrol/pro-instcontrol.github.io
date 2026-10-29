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
    initTools();
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

  /* ---------------- engineering calculators ---------------- */
  function initTools() {
    if (!document.querySelector(".tool")) return;

    function num(id, fallback) {
      var el = document.getElementById(id);
      if (!el) return fallback;
      var v = parseFloat(el.value);
      return isFinite(v) ? v : fallback;
    }
    function out(id, text) {
      var el = document.getElementById(id);
      if (el) el.textContent = text;
    }
    function fmt(v, d) {
      if (!isFinite(v)) return "—";
      return v.toFixed(d);
    }
    function showVerdict(id, key) {
      var box = document.getElementById(id);
      if (!box) return;
      var items = box.querySelectorAll(".v");
      for (var i = 0; i < items.length; i++) {
        items[i].classList.toggle("on", items[i].getAttribute("data-v") === key);
      }
    }
    function bind(ids, fn) {
      ids.forEach(function (id) {
        var el = document.getElementById(id);
        if (el) el.addEventListener("input", fn);
      });
    }

    /* --- 1. 4-20 mA scaling --- */
    if (document.getElementById("ma-out")) {
      var maPv = function () {
        var lrv = num("ma-lrv", 0), urv = num("ma-urv", 100), pv = num("ma-pv", 0);
        var span = urv - lrv;
        if (Math.abs(span) < 1e-9) span = 1e-9;
        var pct = ((pv - lrv) / span) * 100;
        var ma = 4 + (16 * pct) / 100;
        out("ma-out", fmt(ma, 2));
        out("ma-pct", fmt(pct, 1) + " %");
        var field = document.getElementById("ma-ma");
        if (field && document.activeElement !== field) field.value = ma.toFixed(2);
        var bar = document.querySelector("#ma-band i");
        if (bar) bar.style.left = Math.max(0, Math.min(100, (ma / 24) * 100)) + "%";
        if (ma < 3.6) showVerdict("ma-verdict", "faultlow");
        else if (ma < 4) showVerdict("ma-verdict", "under");
        else if (ma <= 20) showVerdict("ma-verdict", "ok");
        else if (ma <= 21) showVerdict("ma-verdict", "over");
        else showVerdict("ma-verdict", "faulthigh");
      };
      var maVal = function () {
        var lrv = num("ma-lrv", 0), urv = num("ma-urv", 100), ma = num("ma-ma", 4);
        out("ma-eu", fmt(lrv + ((ma - 4) * (urv - lrv)) / 16, 2) + " EU");
      };
      bind(["ma-lrv", "ma-urv", "ma-pv"], function () { maPv(); maVal(); });
      bind(["ma-ma"], function () { maVal(); });
      maPv();
      maVal();
    }

    /* --- 2. DP flow --- */
    if (document.getElementById("dp-out")) {
      var dpRun = function () {
        var qd = num("dp-qd", 100), dpd = num("dp-dpd", 250), dpm = num("dp-dpm", 100);
        var acc = num("dp-acc", 1);
        if (dpd <= 0) dpd = 1e-9;
        var q = qd * Math.sqrt(Math.max(dpm, 0) / dpd);
        var pct = (dpm / dpd) * 100;
        out("dp-out", fmt(q, 2));
        out("dp-dp", fmt(dpm, 1) + " mbar");
        out("dp-pct", fmt(pct, 1) + " %");
        var err = dpm > 0 ? (acc * dpd) / dpm : 999;
        out("dp-td", err > 999 ? "> 999 %" : fmt(err, 2) + " %");
      };
      bind(["dp-qd", "dp-dpd", "dp-dpm", "dp-acc"], dpRun);
      dpRun();
    }

    /* --- 3. valve sizing --- */
    if (document.getElementById("cv-out")) {
      var cvRun = function () {
        var q = num("cv-q", 40), sg = num("cv-sg", 1);
        var p1 = num("cv-p1", 6), p2 = num("cv-p2", 4);
        var pv = num("cv-pv", 0.02), pc = num("cv-pc", 220.6);
        var fl = num("cv-fl", 0.9), rated = num("cv-rated", 60);

        var dp = p1 - p2;
        if (dp <= 0) dp = 1e-6;
        var ff = 0.96 - 0.28 * Math.sqrt(Math.max(pv, 0) / Math.max(pc, 1e-6));
        var dpCh = fl * fl * Math.max(p1 - ff * pv, 1e-6);
        var choked = dp > dpCh;
        var dpUse = choked ? dpCh : dp;

        var kv = q * Math.sqrt(Math.max(sg, 1e-6) / Math.max(dpUse, 1e-6));
        var cv = 1.156 * kv;
        var openPct = rated > 0 ? (cv / rated) * 100 : NaN;

        out("cv-out", fmt(kv, 2));
        out("cv-cv", fmt(cv, 2));
        out("cv-dp", fmt(dpUse, 2) + " bar");
        out("cv-open", isFinite(openPct) ? fmt(openPct, 1) + " %" : "—");

        if (choked) showVerdict("cv-verdict", "choked");
        else if (openPct < 10) showVerdict("cv-verdict", "low");
        else if (openPct > 90) showVerdict("cv-verdict", "high");
        else showVerdict("cv-verdict", "ok");
      };
      bind(["cv-q", "cv-sg", "cv-p1", "cv-p2", "cv-pv", "cv-pc", "cv-fl", "cv-rated"], cvRun);
      cvRun();
    }

    /* --- 4. hydrostatic level --- */
    if (document.getElementById("lvl-out")) {
      var lvlRun = function () {
        var dp = num("lvl-dp-in", 500), rho = num("lvl-rho", 1000), dr = num("lvl-dr", 1);
        if (rho <= 0) rho = 1e-6;
        var h = (dp * 100) / (rho * 9.80665);
        out("lvl-out", fmt(h, 3));
        out("lvl-dp", fmt(dp / 100, 3) + " kPa");
        out("lvl-err", fmt((h * dr) / 100 * 1000, 1) + " mm");
      };
      bind(["lvl-dp-in", "lvl-rho", "lvl-dr"], lvlRun);
      lvlRun();
    }

    /* --- 5. loop error budget --- */
    if (document.getElementById("err-out")) {
      var errRun = function () {
        var a = num("err-a", 0.1), b = num("err-b", 0.5), c = num("err-c", 0.2), d = num("err-d", 0.05);
        var span = num("err-span", 250);
        var rss = Math.sqrt(a * a + b * b + c * c + d * d);
        var worst = a + b + c + d;
        out("err-out", fmt(rss, 2));
        out("err-rss", fmt(rss, 2) + " % span");
        out("err-eu", fmt((rss / 100) * span, 2) + " EU");
        out("err-worst", fmt(worst, 2) + " % span");
      };
      bind(["err-a", "err-b", "err-c", "err-d", "err-span"], errRun);
      errRun();
    }
  }
})();
