/* Cut-paper toolkit for "Satış Yolculuğu · Satışın Yeni Tanımı".
   Everything is seeded, so every frame renders the same way on every seek. */
(function () {
  const NS = "http://www.w3.org/2000/svg";
  const C = {
    yellow: "#FFFF00",
    y: "#FFFF00",
    ink: "#151413",
    cream: "#F4EEDC",
    rust: "#D9452B",
    shade: "#2A2826",
    paper2: "#E9E1C9",
  };

  function rng(seed) {
    let a = (seed * 2654435761) >>> 0 || 1;
    return function () {
      a |= 0;
      a = (a + 0x6d2b79f5) | 0;
      let t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  // A rectangle whose edges wobble like hand-cut paper.
  function jagRect(w, h, seed, amp, step) {
    const r = rng(seed || 1);
    amp = amp == null ? 3 : amp;
    step = step || 28;
    const j = () => (r() * 2 - 1) * amp;
    const pts = [];
    for (let x = 0; x < w; x += step) pts.push([x, j()]);
    for (let y = 0; y < h; y += step) pts.push([w + j(), y]);
    for (let x = w; x > 0; x -= step) pts.push([x, h + j()]);
    for (let y = h; y > 0; y -= step) pts.push([j(), y]);
    return "M" + pts.map((p) => p[0].toFixed(1) + " " + p[1].toFixed(1)).join(" L") + "Z";
  }

  // A hand-cut circle.
  function jagCircle(cx, cy, rad, seed, amp, n) {
    const r = rng(seed || 7);
    amp = amp == null ? rad * 0.025 + 1 : amp;
    n = n || Math.max(18, Math.round(rad / 5));
    const pts = [];
    for (let i = 0; i < n; i++) {
      const a = (i / n) * Math.PI * 2;
      const rr = rad + (r() * 2 - 1) * amp;
      pts.push([cx + Math.cos(a) * rr, cy + Math.sin(a) * rr]);
    }
    return "M" + pts.map((p) => p[0].toFixed(1) + " " + p[1].toFixed(1)).join(" L") + "Z";
  }

  // Any polygon with hand-cut wobble between its corners.
  function jagPoly(points, seed, amp, step) {
    const r = rng(seed || 3);
    amp = amp == null ? 2.5 : amp;
    step = step || 26;
    const out = [];
    for (let i = 0; i < points.length; i++) {
      const [x1, y1] = points[i];
      const [x2, y2] = points[(i + 1) % points.length];
      const len = Math.hypot(x2 - x1, y2 - y1);
      const n = Math.max(1, Math.round(len / step));
      for (let k = 0; k < n; k++) {
        const t = k / n;
        const jx = k === 0 ? 0 : (r() * 2 - 1) * amp;
        const jy = k === 0 ? 0 : (r() * 2 - 1) * amp;
        out.push([x1 + (x2 - x1) * t + jx, y1 + (y2 - y1) * t + jy]);
      }
    }
    return "M" + out.map((p) => p[0].toFixed(1) + " " + p[1].toFixed(1)).join(" L") + "Z";
  }

  function svg(w, h, inner, cls) {
    return (
      '<svg xmlns="' + NS + '" width="' + w + '" height="' + h + '" viewBox="0 0 ' + w + " " + h +
      '" style="overflow:visible;display:block"' + (cls ? ' class="' + cls + '"' : "") + ">" + inner + "</svg>"
    );
  }

  // Inner markup for a paper strip, with an optional soft drop shadow (a darker copy, offset).
  function strip(w, h, fill, seed, opts) {
    opts = opts || {};
    const d = jagRect(w, h, seed, opts.amp, opts.step);
    const sh = opts.shadow === false ? "" : '<path d="' + d + '" fill="rgba(21,20,19,.22)" transform="translate(5 7)"/>';
    return svg(w, h, sh + '<path d="' + d + '" fill="' + fill + '"/>');
  }

  function disc(rad, fill, seed, opts) {
    opts = opts || {};
    const s = rad * 2;
    const d = jagCircle(rad, rad, rad, seed, opts.amp);
    const sh = opts.shadow === false ? "" : '<path d="' + d + '" fill="rgba(21,20,19,.22)" transform="translate(4 6)"/>';
    return svg(s, s, sh + '<path d="' + d + '" fill="' + fill + '"/>');
  }

  // Fill an element with paper markup and size it.
  function mount(el, html, w, h) {
    el.innerHTML = html;
    if (w) el.style.width = w + "px";
    if (h) el.style.height = h + "px";
    return el;
  }

  // Render all [data-paper] placeholders inside root:
  //   data-paper="strip|disc" data-w data-h data-r data-fill data-seed data-amp data-noshadow
  function build(root) {
    root.querySelectorAll("[data-paper]").forEach((el) => {
      const kind = el.getAttribute("data-paper");
      const fill = C[el.dataset.fill] || el.dataset.fill || C.ink;
      const seed = +(el.dataset.seed || 1);
      const amp = el.dataset.amp != null ? +el.dataset.amp : undefined;
      const opts = { amp: amp, shadow: el.hasAttribute("data-noshadow") ? false : true };
      if (kind === "strip") {
        const w = +el.dataset.w, h = +el.dataset.h;
        mount(el, strip(w, h, fill, seed, opts), w, h);
      } else if (kind === "disc") {
        const r = +el.dataset.r;
        mount(el, disc(r, fill, seed, opts), r * 2, r * 2);
      } else if (kind === "poly") {
        const pts = JSON.parse(el.dataset.pts);
        const w = +el.dataset.w, h = +el.dataset.h;
        const d = jagPoly(pts, seed, amp);
        const sh = opts.shadow ? '<path d="' + d + '" fill="rgba(21,20,19,.22)" transform="translate(5 7)"/>' : "";
        mount(el, svg(w, h, sh + '<path d="' + d + '" fill="' + fill + '"/>'), w, h);
      }
    });
    // Jaunty words: each word gets a small seeded tilt and offset.
    root.querySelectorAll("[data-jaunty]").forEach((el) => {
      const r = rng(+(el.dataset.seed || 11));
      const amt = el.dataset.jaunty ? +el.dataset.jaunty : 2.5;
      const words = el.textContent.trim().split(/\s+/);
      el.innerHTML = words
        .map((w) => {
          const rot = ((r() * 2 - 1) * amt).toFixed(2);
          const y = ((r() * 2 - 1) * 6).toFixed(1);
          return '<span class="jw" style="display:inline-block;transform:rotate(' + rot + "deg) translateY(" + y + 'px)"><span class="jwi" style="display:inline-block">' + w + "</span></span>";
        })
        .join(" ");
    });
  }

  // Jagged clip-path polygon (percent + px jitter), so a strip can wrap any text without measuring it.
  function jagClip(seed, amp, n) {
    const r = rng(seed || 5);
    amp = amp == null ? 2.5 : amp;
    n = n || 9;
    const j = () => ((r() * 2 - 1) * amp).toFixed(1) + "px";
    const pts = [];
    for (let i = 0; i < n; i++) pts.push("calc(" + ((i / n) * 100).toFixed(2) + "% + " + j() + ") " + j());
    for (let i = 0; i < 4; i++) pts.push("calc(100% + " + j() + ") " + "calc(" + ((i / 4) * 100).toFixed(1) + "% + " + j() + ")");
    for (let i = n; i > 0; i--) pts.push("calc(" + ((i / n) * 100).toFixed(2) + "% + " + j() + ") calc(100% + " + j() + ")");
    for (let i = 4; i > 0; i--) pts.push(j() + " calc(" + ((i / 4) * 100).toFixed(1) + "% + " + j() + ")");
    return "polygon(" + pts.join(",") + ")";
  }

  // [data-tag="fill"]: text on a paper strip that fits the text.
  function tags(root) {
    root.querySelectorAll("[data-tag]").forEach((el, i) => {
      if (el.querySelector(":scope > .tagbg")) return;
      const fill = C[el.dataset.tag] || el.dataset.tag || C.cream;
      const bg = document.createElement("span");
      bg.className = "tagbg";
      bg.style.cssText = "position:absolute;inset:0;z-index:0;background:" + fill + ";clip-path:" + jagClip(+(el.dataset.seed || 31 + i * 7), 2.2, 10);
      el.insertBefore(bg, el.firstChild);
      if (!el.hasAttribute("data-noshadow")) el.style.filter = "drop-shadow(5px 7px 0 rgba(21,20,19,.22))";
    });
  }

  // Hard cut: show el from t0 to t1 (seconds, local).
  function cut(tl, el, t0, t1) {
    tl.set(el, { opacity: 1 }, t0);
    if (t1 != null) tl.set(el, { opacity: 0 }, t1);
  }

  window.PAPER = { tags, jagClip, cut, C, rng, jagRect, jagCircle, jagPoly, svg, strip, disc, build };
})();
