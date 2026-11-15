/* TerraTwin — etkileşim katmanı */
(function () {
  'use strict';
  const D = window.TT;
  const $ = (s, r) => (r || document).querySelector(s);
  const $$ = (s, r) => Array.from((r || document).querySelectorAll(s));
  document.documentElement.classList.add('js');

  const announce = () => document.dispatchEvent(new CustomEvent('terratwin:state', { detail: { lang: state.lang, profile: state.mProfile, mission: state.mission, site: state.site } }));
  const state = { lang: 'tr', profile: 'all', cats: { nasa: true, test: true, hypo: true, note: true }, site: 'haughton', mProfile: 'base', mission: 0, body: 'all' };
  const t = (o) => (o && typeof o === 'object' && 'tr' in o ? o[state.lang] : o);
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const num = (n, d) => n.toFixed(d).replace('.', state.lang === 'tr' ? ',' : '.');

  /* ---------- dil ---------- */
  const i18nNodes = $$('[data-i18n]');
  i18nNodes.forEach((n) => { n._tr = n.innerHTML; });
  try {
    const saved = localStorage.getItem('tt-lang');
    if (saved === 'tr' || saved === 'en') state.lang = saved;
    else if (!/^tr\b/i.test(navigator.language || 'tr')) state.lang = 'en';
  } catch (e) { /* depolama yoksa Türkçe kalır */ }

  function applyLang() {
    i18nNodes.forEach((n) => {
      const en = D.en[n.dataset.i18n];
      n.innerHTML = state.lang === 'en' && en != null ? en : n._tr;
    });
    document.documentElement.lang = state.lang;
    document.title = state.lang === 'en'
      ? 'TerraTwin — Earth’s twins of the Moon base and of Mars'
      : 'TerraTwin — Ay üssünün ve Mars\'ın Dünya\'daki ikizleri';
    $$('.lang button').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.lang === state.lang)));
    const dn = $('#docs-note'); if (dn) dn.hidden = state.lang !== 'en';
    renderLegend(); renderList(); renderCard(); renderWeights(true); renderCatalog(); updateMap(); mapLabels(); announce();
  }
  $$('.lang button').forEach((b) => b.addEventListener('click', () => {
    state.lang = b.dataset.lang;
    try { localStorage.setItem('tt-lang', state.lang); } catch (e) { /* yok say */ }
    applyLang();
  }));

  /* ---------- işaret şekilleri ---------- */
  const GLYPH = {
    circle: 'M7 1.5a5.5 5.5 0 1 0 0 11a5.5 5.5 0 1 0 0-11z',
    ring: 'M7 1.5a5.5 5.5 0 1 0 0 11a5.5 5.5 0 1 0 0-11z',
    diamond: 'M7 .8L13.2 7L7 13.2L.8 7z',
    square: 'M2.5 2.5h9v9h-9z',
  };
  const glyph = (cat) => `<svg class="glyph g-${cat}" viewBox="0 0 14 14" aria-hidden="true"><path d="${GLYPH[D.cats[cat].shape]}"/></svg>`;

  /* ---------- hero konturları ---------- */
  function hash(i, j, s) { const n = Math.sin(i * 127.1 + j * 311.7 + s * 74.7) * 43758.5453; return n - Math.floor(n); }
  function vnoise(x, y, s) {
    const xi = Math.floor(x), yi = Math.floor(y), xf = x - xi, yf = y - yi;
    const u = xf * xf * (3 - 2 * xf), v = yf * yf * (3 - 2 * yf);
    const a = hash(xi, yi, s), b = hash(xi + 1, yi, s), c = hash(xi, yi + 1, s), d = hash(xi + 1, yi + 1, s);
    return a + (b - a) * u + (c - a) * v + (a - b - c + d) * u * v;
  }
  function fbm(x, y, s) { let v = 0, amp = .5, f = 1; for (let o = 0; o < 4; o++) { v += amp * vnoise(x * f, y * f, s + o * 13); f *= 2; amp *= .5; } return v; }

  const EDGE = { 1: [[3, 2]], 2: [[2, 1]], 3: [[3, 1]], 4: [[0, 1]], 5: [[0, 3], [2, 1]], 6: [[0, 2]], 7: [[0, 3]], 8: [[0, 3]], 9: [[0, 2]], 10: [[0, 1], [3, 2]], 11: [[0, 1]], 12: [[3, 1]], 13: [[2, 1]], 14: [[3, 2]] };

  /* Sol yarı hedefi, sağ yarı Dünya analoğunu temsil eder: sağ taraf solun aynadaki
     görüntüsüdür ama dikişten uzaklaştıkça sapar. Analoglar kısmidir. */
  function drawContours() {
    const cv = $('#contours'); if (!cv) return;
    const box = cv.getBoundingClientRect(), W = box.width, H = box.height;
    if (!W || !H) return;
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr);
    const g = cv.getContext('2d'); g.setTransform(dpr, 0, 0, dpr, 0, 0); g.clearRect(0, 0, W, H);
    const step = W > 900 ? 9 : 7, cols = Math.ceil(W / step) + 1, rows = Math.ceil(H / step) + 1;
    const sc = Math.max(W, H) / 3.1, half = W / 2;
    const cx = half - Math.min(W * .21, 320), cy = H * .4, R = Math.min(W, H) * .17;
    const f = new Float32Array(cols * rows); let lo = Infinity, hi = -Infinity;
    for (let j = 0; j < rows; j++) for (let i = 0; i < cols; i++) {
      const x = i * step, y = j * step, xm = x <= half ? x : W - x;
      let v = fbm(xm / sc, y / sc, 3);
      if (x > half) { const k = Math.min(.55, ((x - half) / half) * .95); v = v * (1 - k) + fbm(x / sc + 9, y / sc + 4, 11) * k; }
      const rr = Math.hypot(xm - cx, y - cy);
      v += -.3 * Math.exp(-(rr * rr) / (2 * (.55 * R) ** 2)) + .16 * Math.exp(-((rr - R) ** 2) / (2 * (.3 * R) ** 2));
      f[j * cols + i] = v; if (v < lo) lo = v; if (v > hi) hi = v;
    }
    const LEVELS = 17;
    for (let n = 1; n < LEVELS; n++) {
      const Lv = lo + ((hi - lo) * n) / LEVELS, major = n % 4 === 0;
      const paths = [new Path2D(), new Path2D()];
      for (let j = 0; j < rows - 1; j++) for (let i = 0; i < cols - 1; i++) {
        const a = f[j * cols + i], b = f[j * cols + i + 1], c = f[(j + 1) * cols + i + 1], d = f[(j + 1) * cols + i];
        const idx = (a > Lv ? 8 : 0) | (b > Lv ? 4 : 0) | (c > Lv ? 2 : 0) | (d > Lv ? 1 : 0);
        const segs = EDGE[idx]; if (!segs) continue;
        const x = i * step, y = j * step;
        const pt = (e) => e === 0 ? [x + ((Lv - a) / (b - a)) * step, y]
          : e === 1 ? [x + step, y + ((Lv - b) / (c - b)) * step]
          : e === 2 ? [x + ((Lv - d) / (c - d)) * step, y + step]
          : [x, y + ((Lv - a) / (d - a)) * step];
        for (const s of segs) {
          const p = pt(s[0]), q = pt(s[1]), side = (p[0] + q[0]) / 2 < half ? 0 : 1;
          paths[side].moveTo(p[0], p[1]); paths[side].lineTo(q[0], q[1]);
        }
      }
      g.lineWidth = major ? 1.15 : .7;
      g.strokeStyle = `rgba(159,192,213,${major ? .6 : .3})`; g.stroke(paths[0]);
      g.strokeStyle = `rgba(229,130,88,${major ? .62 : .32})`; g.stroke(paths[1]);
    }
  }
  let lastW = 0, rz;
  window.addEventListener('resize', () => {
    clearTimeout(rz);
    rz = setTimeout(() => { if (Math.abs(window.innerWidth - lastW) > 4) { lastW = window.innerWidth; drawContours(); } }, 160);
  });

  /* ---------- atlas ---------- */
  const visible = (s) => state.cats[s.cat];
  const ratingOf = (s) => (state.profile === 'all' ? null : s.r[state.profile === 'base' ? 1 : 2]);
  const radius = (s) => { if (state.profile === 'all') return 7.5; const v = ratingOf(s); return v == null ? 5 : 4.5 + 3 * v; };
  const coord = (s) => {
    const U = D.ui, la = `${num(Math.abs(s.lat), 1)}° ${t(s.lat >= 0 ? U.N : U.S)}`, lo = `${num(Math.abs(s.lon), 1)}° ${t(s.lon >= 0 ? U.E : U.W)}`;
    return `≈ ${la} · ${lo}`;
  };

  function selectSite(id, scroll) {
    if (!D.sites.some((s) => s.id === id)) return;
    state.site = id; renderCard(); updateMap(); renderList(); announce();
    if (scroll && window.matchMedia('(max-width: 1020px)').matches) $('#site-card').scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  function renderLegend() {
    const el = $('#cat-legend'); if (!el) return;
    el.innerHTML = Object.keys(D.cats).filter((k) => D.sites.some((s) => s.cat === k)).map((k) => `<button type="button" data-cat="${k}" aria-pressed="${state.cats[k]}">${glyph(k)}<span>${esc(t(D.cats[k].label))}</span></button>`).join('');
    $$('button', el).forEach((b) => b.addEventListener('click', () => {
      const k = b.dataset.cat; state.cats[k] = !state.cats[k];
      if (!Object.values(state.cats).some(Boolean)) state.cats[k] = true;
      const cur = D.sites.find((s) => s.id === state.site);
      if (cur && !visible(cur)) { const first = D.sites.find(visible); if (first) state.site = first.id; }
      renderLegend(); renderList(); renderCard(); updateMap();
    }));
  }

  function renderList() {
    const el = $('#site-list'); if (!el) return;
    el.innerHTML = D.sites.map((s) => `<button type="button" data-id="${s.id}" class="${visible(s) ? '' : 'off'}" aria-pressed="${s.id === state.site}">${glyph(s.cat)}<span>${esc(t(s.name))}</span></button>`).join('');
    $$('button', el).forEach((b) => b.addEventListener('click', () => selectSite(b.dataset.id, true)));
  }

  function dots(v) {
    if (v == null) return '<em class="sc-unrated">—</em>';
    return `<span class="dots" role="img" aria-label="${v} / 3">${[1, 2, 3].map((i) => `<i class="${i <= v ? 'on' : ''}"></i>`).join('')}</span>`;
  }

  function renderCard() {
    const el = $('#site-card'), s = D.sites.find((x) => x.id === state.site); if (!el || !s) return;
    const U = D.ui, rated = s.r.some((v) => v != null);
    const src = s.src
      ? `<a class="sc-src" href="${esc(s.src[1])}" target="_blank" rel="noopener">${esc(t(U.source))}: ${esc(s.src[0])} ↗</a>`
      : (s.doc ? `<a class="sc-src" href="${esc(s.doc)}">${esc(t(U.doc))} ↗</a>` : '');
    const ph = window.TT_PHOTOS && window.TT_PHOTOS[s.id];
    const lic = ph && (state.lang === 'en' ? ({ 'Kamu malı': 'Public domain', 'Atıf': 'Attribution' }[ph.license] || ph.license) : ph.license);
    const photo = ph ? `
      <figure class="sc-photo">
        <img src="${esc(ph.src)}" width="${ph.w}" height="${ph.h}" alt="${esc(t(ph.cap))}"${ph.pos ? ` style="object-position:${esc(ph.pos)}"` : ''} loading="lazy" decoding="async" referrerpolicy="no-referrer" onerror="this.parentNode.hidden=true">
        <figcaption>${esc(t(ph.cap))} · <a href="${esc(ph.page)}" target="_blank" rel="noopener">${esc(ph.artist)}, ${esc(lic)} ↗</a></figcaption>
      </figure>` : '';
    el.innerHTML = `${photo}
      <p class="sc-cat mono">${glyph(s.cat)}<span>${esc(t(D.cats[s.cat].label))}</span></p>
      <h3>${esc(t(s.name))}</h3>
      <p class="sc-loc">${esc(t(s.loc))}</p>
      <p class="sc-coord mono">${coord(s)}</p>
      <p class="sc-tag">${esc(t(s.tag))}</p>
      <div class="sc-ratings">${s.r.map((v, i) => `<div><span class="mono">${esc(t(U.ratingLabels[i]))}</span>${dots(v)}</div>`).join('')}</div>
      <p class="sc-qual mono">${esc(t(rated ? U.qual : U.unrated))}</p>
      <div class="sc-block"><h4>${esc(t(U.basis))}</h4><p>${esc(t(s.basis))}</p></div>
      <div class="sc-block"><h4>${esc(t(s.cat === 'hypo' ? U.likeHypo : U.like))}</h4><p>${esc(t(s.like))}</p></div>
      <div class="sc-block sc-limit"><h4>${esc(t(U.limit))}</h4><p>${esc(t(s.limit))}</p></div>
      <div class="sc-block"><h4>${esc(t(U.data))}</h4><p class="chips">${s.data.map((d) => `<span>${esc(d)}</span>`).join('')}</p>${s.note ? `<p class="sc-note">${esc(t(s.note))}</p>` : ''}</div>
      ${src}`;
  }

  let proj = null, mapReady = false;
  const SYM = () => ({ nasa: d3.symbolCircle, test: d3.symbolCircle, hypo: d3.symbolDiamond, note: d3.symbolSquare });

  function initMap() {
    const svgEl = $('#map'); if (!svgEl) return;
    if (!window.d3) { const off = $('#map-offline'); off.hidden = false; off.textContent = t(D.ui.mapOffline); svgEl.style.display = 'none'; return; }
    const W = 960, H = 500, svg = d3.select(svgEl);
    proj = d3.geoEqualEarth().fitExtent([[8, 8], [W - 8, H - 8]], { type: 'Sphere' });
    const path = d3.geoPath(proj);
    svg.append('path').attr('class', 'sphere').attr('d', path({ type: 'Sphere' }));
    const land = svg.append('path').attr('class', 'land');
    svg.append('path').attr('class', 'grat').attr('d', path(d3.geoGraticule().step([30, 30])()));
    svg.append('g').attr('class', 'lat-labels');
    const layer = svg.append('g').attr('class', 'markers');
    svg.append('text').attr('class', 'm-label');

    const order = { note: 0, hypo: 1, test: 2, nasa: 3 };
    D.sites.slice().sort((a, b) => order[a.cat] - order[b.cat]).forEach((s) => {
      const p = proj([s.lon, s.lat]);
      const gm = layer.append('g').attr('class', `marker m-${s.cat}`).attr('data-id', s.id)
        .attr('transform', `translate(${p[0].toFixed(1)},${p[1].toFixed(1)})`).attr('tabindex', 0).attr('role', 'button');
      gm.append('circle').attr('class', 'hit').attr('r', 15);
      gm.append('circle').attr('class', 'halo');
      gm.append('path').attr('class', 'shape');
      gm.append('title');
      gm.on('click', () => selectSite(s.id, true))
        .on('keydown', (ev) => { if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); selectSite(s.id, true); } });
    });

    if (window.topojson) {
      fetch('https://cdn.jsdelivr.net/npm/world-atlas@2.0.2/land-110m.json')
        .then((r) => { if (!r.ok) throw new Error(r.status); return r.json(); })
        .then((w) => land.attr('d', path(topojson.feature(w, w.objects.land))))
        .catch(() => { const off = $('#map-offline'); off.hidden = false; off.textContent = t(D.ui.mapOffline); });
    }
    mapReady = true; mapLabels(); updateMap();
  }

  function mapLabels() {
    if (!mapReady) return;
    const U = D.ui, g = d3.select('#map .lat-labels'); g.selectAll('*').remove();
    [60, 30, 0, -30, -60].forEach((lat) => {
      const p = proj([-180, lat]);
      g.append('text').attr('class', 'lat-label').attr('x', p[0] + 5).attr('y', p[1] - 3)
        .text(lat === 0 ? '0°' : `${Math.abs(lat)}°${t(lat > 0 ? U.N : U.S)}`);
    });
  }

  function updateMap() {
    if (!mapReady) return;
    const sym = SYM();
    d3.selectAll('#map .marker').each(function () {
      const el = d3.select(this), s = D.sites.find((x) => x.id === el.attr('data-id')), r = radius(s);
      el.classed('off', !visible(s)).classed('sel', s.id === state.site)
        .classed('unrated', state.profile !== 'all' && ratingOf(s) == null)
        .attr('aria-label', t(s.name)).attr('aria-pressed', s.id === state.site);
      el.select('.shape').attr('d', d3.symbol(sym[s.cat], Math.PI * r * r * (s.cat === 'hypo' ? 1.25 : 1))());
      el.select('.halo').attr('r', r + 5);
      el.select('title').text(`${t(s.name)} — ${t(D.cats[s.cat].short)}`);
    });
    const cur = D.sites.find((x) => x.id === state.site), lab = d3.select('#map .m-label');
    if (cur && visible(cur)) {
      const p = proj([cur.lon, cur.lat]), r = radius(cur), right = p[0] < 760;
      lab.attr('x', p[0] + (right ? r + 9 : -(r + 9))).attr('y', p[1] + 4).attr('text-anchor', right ? 'start' : 'end').text(t(cur.name)).style('display', null);
      d3.select(`#map .marker[data-id="${cur.id}"]`).raise();
    } else lab.style('display', 'none');
    const hint = $('#map-hint'); if (hint) hint.hidden = state.profile === 'all';
  }

  $$('#profile-seg button').forEach((b) => b.addEventListener('click', () => {
    state.profile = b.dataset.p;
    $$('#profile-seg button').forEach((x) => x.setAttribute('aria-pressed', String(x === b)));
    updateMap();
  }));

  /* ---------- yöntem: ağırlık gezgini ---------- */
  function renderWeights(rebuild) {
    const P = D.method[state.mProfile], rowsEl = $('#w-rows'); if (!rowsEl) return;
    if (rebuild) {
      $('#m-profile').innerHTML = Object.keys(D.method).map((k) => `<button type="button" data-k="${k}" aria-pressed="${k === state.mProfile}">${esc(t(D.method[k].label))}</button>`).join('');
      $$('#m-profile button').forEach((b) => b.addEventListener('click', () => { state.mProfile = b.dataset.k; state.mission = 0; renderWeights(true); }));
      $('#m-missions').innerHTML = P.missions.map((m, i) => `<button type="button" data-i="${i}" aria-pressed="${i === state.mission}">${esc(t(m.name))}</button>`).join('');
      $$('#m-missions button').forEach((b) => b.addEventListener('click', () => {
        state.mission = +b.dataset.i;
        $$('#m-missions button').forEach((x) => x.setAttribute('aria-pressed', String(x === b)));
        renderWeights(false);
      }));
      rowsEl.innerHTML = P.criteria.map((c) => `
        <div class="w-row">
          <span class="w-code">${c.code}</span>
          <span class="w-name">${esc(t(c.name))}</span>
          <span class="w-meta"><b>${esc(t(c.data))}</b>${esc(t(c.earth))}</span>
          <span class="w-track"><span class="w-bar"></span></span>
          <span class="w-val"></span>
        </div>`).join('');
    }
    /* Ağırlıklar çizim anındaki durumdan okunur; gecikmeli çizim eski seçimi geri yazmasın. */
    const apply = () => {
      const w = D.method[state.mProfile].missions[state.mission].w, max = Math.max.apply(null, w);
      $$('.w-row', rowsEl).forEach((row, i) => {
        $('.w-bar', row).style.width = `${(w[i] / .4) * 100}%`;
        $('.w-val', row).textContent = num(w[i], 2);
        row.classList.toggle('top', w[i] === max);
      });
    };
    if (rebuild) requestAnimationFrame(() => requestAnimationFrame(apply)); else apply();
    announce();
  }

  /* ---------- veri kataloğu ---------- */
  function renderCatalog() {
    const seg = $('#body-seg'), tbl = $('#catalog'); if (!seg || !tbl) return;
    const U = D.ui, count = (b) => (b === 'all' ? D.datasets.length : D.datasets.filter((d) => d.b === b).length);
    seg.innerHTML = ['all', 'earth', 'moon', 'mars'].map((b) => `<button type="button" data-b="${b}" aria-pressed="${b === state.body}">${esc(t(U.bodies[b]))} · ${count(b)}</button>`).join('');
    $$('button', seg).forEach((b) => b.addEventListener('click', () => { state.body = b.dataset.b; renderCatalog(); }));
    const rows = D.datasets.filter((d) => state.body === 'all' || d.b === state.body);
    const loc = (s) => (state.lang === 'en' ? String(s).replace(/(\d),(\d)/g, '$1.$2') : s);
    tbl.innerHTML = `<thead><tr>${U.th.map((h) => `<th>${esc(t(h))}</th>`).join('')}</tr></thead><tbody>${rows.map((d) => `
      <tr>
        <td><span class="body-tag b-${d.b}" title="${esc(t(U.bodies[d.b]))}"></span><a class="cat-name" href="${esc(d.url)}" target="_blank" rel="noopener">${esc(d.n)}</a><span class="cat-short">${esc(t(d.s))}</span></td>
        <td>${esc(loc(t(d.g)))}</td><td>${esc(t(d.u))}</td><td>${esc(t(d.c))}</td>
      </tr>`).join('')}</tbody>`;
  }

  /* ---------- görünüme girince belirme ---------- */
  function initReveal() {
    const els = $$('.reveal');
    if (!('IntersectionObserver' in window)) { els.forEach((e) => e.classList.add('in')); return; }
    const io = new IntersectionObserver((entries) => entries.forEach((en) => { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } }), { rootMargin: '0px 0px -8% 0px', threshold: .08 });
    els.forEach((e) => io.observe(e));
  }

  document.addEventListener('terratwin:select-site', (ev) => selectSite(ev.detail.id, false));
  document.addEventListener('terratwin:select-profile', (ev) => {
    if (!D.method[ev.detail.profile]) return;
    state.mProfile = ev.detail.profile; state.mission = 0; renderWeights(true);
  });
  window.TerraTwinState = () => ({ lang: state.lang, profile: state.mProfile, mission: state.mission, site: state.site });

  /* ---------- başlat ---------- */
  $('#st-sites').textContent = D.sites.length;
  $('#st-datasets').textContent = D.datasets.length;
  lastW = window.innerWidth;
  initMap();
  applyLang();
  drawContours();
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(drawContours);
  initReveal();
})();
