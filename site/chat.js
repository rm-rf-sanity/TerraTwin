/* TerraTwin Rehberi — yalnızca bu sitenin içeriğine dayanan soru-cevap penceresi.
   Uzak mod: TT_CHAT_CONFIG.endpoint tanımlıysa sorular ara sunucu üzerinden Claude'a gider.
   Yerel mod: anahtar gerektirmeyen site içi arama. Uzak mod yanıt veremezse yerel moda düşülür. */
(function () {
  'use strict';
  const D = window.TT;
  if (!D || !document.body) return;
  const CFG = Object.assign({ endpoint: '' }, window.TT_CHAT_CONFIG || {});
  const REMOTE = typeof CFG.endpoint === 'string' && /^https?:\/\//.test(CFG.endpoint);
  const $ = (s, r) => (r || document).querySelector(s);
  const $$ = (s, r) => Array.from((r || document).querySelectorAll(s));
  const el = (tag, cls, text) => { const n = document.createElement(tag); if (cls) n.className = cls; if (text != null) n.textContent = text; return n; };
  const pick = (o, lang) => (o && typeof o === 'object' && !Array.isArray(o) ? (o[lang] != null ? o[lang] : o.tr != null ? o.tr : o.en || '') : (o == null ? '' : String(o)));
  const finite = (v) => typeof v === 'number' && Number.isFinite(v);

  const STR = {
    tr: {
      launch: 'Soru sor', title: 'TerraTwin Rehberi', close: 'Rehberi kapat', inputLabel: 'Sorunuz', send: 'Gönder',
      modeAi: 'Yapay zeka · Claude', modeLocal: 'Site içi arama · yapay zeka bağlı değil',
      placeholder: 'TerraTwin hakkında bir soru yazın…',
      noteAi: 'Yalnızca TerraTwin ile ilgili soruları yanıtlar. Yanıtları yapay zeka üretir ve hata yapabilir; sorular yanıt için Anthropic’e iletilir.',
      noteLocal: 'Yalnızca TerraTwin ile ilgili soruları yanıtlar. Yanıtlar bu sitedeki metinlerden derlenir.',
      hello: 'Merhaba. TerraTwin’in görevi, hedefleri, atlastaki sahalar, yöntem, NASA verileri ve analogların sınırları hakkında soru sorabilirsiniz.',
      about: 'Ben TerraTwin Rehberi’yim. Yalnızca bu projeyle ilgili soruları yanıtlarım: görev, hedefler, atlastaki sahalar, yöntem, NASA veri ürünleri ve analogların sınırları.',
      thanks: 'Rica ederim. Başka bir sorunuz olursa buradayım.',
      offTopic: 'Bu soruyu sitedeki içerikle eşleştiremedim. Yalnızca TerraTwin ile ilgili soruları yanıtlıyorum: görev, hedefler, atlastaki sahalar, yöntem, NASA verileri ve sınırlar.',
      unsure: 'Tam karşılığını bulamadım. Şu başlıklar ilgili olabilir:',
      related: 'İlgili', more: 'Devamı ilgili bölümde.', goSection: 'Bölüme git', showAtlas: 'Atlasta göster', source: 'Kaynak', product: 'Ürün sayfası',
      thinking: 'Yanıt hazırlanıyor', fallback: 'Yapay zeka şu an yanıt veremedi · site içi arama sonucu',
      refusal: 'Bu soruya yanıt veremiyorum. TerraTwin ile ilgili başka bir soru sorabilirsiniz.',
      suggestions: ['TerraTwin nedir?', 'Salda Gölü neden Mars analoğu?', 'Shackleton hedefi nedir?', 'Hangi NASA verileri kullanılıyor?', 'Analogların sınırları neler?'],
      project: 'Proje hakkında', sitesTitle: 'Atlastaki sahalar', datasetsTitle: 'NASA veri ürünleri kataloğu', catsTitle: 'Kanıt düzeyleri ve atlas işaretleri',
      criteria: 'Ölçütler', weights: 'Görev ağırlıkları', methodSuffix: 'ölçütler ve görev ağırlıkları',
      category: 'Kanıt düzeyi', ratings: 'Niteliksel not (3 üzerinden)', datasets: 'Veri', coverage: 'Kapsam', use: 'Kullanım', caveat: 'Uyarı', aka: 'Diğer adı',
      bodies: { earth: 'Dünya', moon: 'Ay', mars: 'Mars' },
      pilot: 'Pilot analiz', pilotLimits: 'Pilot analizin sınırlamaları', pilotScores: 'Hesaplanan görev skorları',
      period: 'Gözlem dönemi', validation: 'Doğrulama', target: 'hedef', noScore: 'yeterli veri kapsamı olmadığı için skor açıklanmadı',
      scoreNote: 'Skorlar 0–100 ölçeğinde kısmi operasyonel ön elemedir; NASA onayı veya tam analog doğrulaması değildir. Ayrıntı Atlas bölümündeki analiz panelindedir.',
      scored: 'alan skor aldı', top: 'En yüksek', noRank: 'veri kapsamı çoğu alanda yetersiz olduğundan sıralama anlamlı değil',
      roles: { candidate: 'aday', negative_control: 'negatif kontrol' }
    },
    en: {
      launch: 'Ask a question', title: 'TerraTwin Guide', close: 'Close the guide', inputLabel: 'Your question', send: 'Send',
      modeAi: 'AI · Claude', modeLocal: 'On-site search · no AI connected',
      placeholder: 'Ask something about TerraTwin…',
      noteAi: 'Answers TerraTwin questions only. Replies are AI-generated and can be wrong; questions are sent to Anthropic to produce a reply.',
      noteLocal: 'Answers TerraTwin questions only. Replies are compiled from the text on this site.',
      hello: 'Hello. You can ask about TerraTwin’s mission, targets, the atlas sites, the method, NASA data and the limits of analogs.',
      about: 'I am the TerraTwin Guide. I only answer questions about this project: the mission, targets, atlas sites, method, NASA data products and the limits of analogs.',
      thanks: 'You’re welcome. I’m here if you have another question.',
      offTopic: 'I couldn’t match that to anything on this site. I only answer TerraTwin questions: the mission, targets, atlas sites, method, NASA data and limits.',
      unsure: 'I couldn’t find an exact match. These topics may be related:',
      related: 'Related', more: 'More in the related section.', goSection: 'Go to section', showAtlas: 'Show in atlas', source: 'Source', product: 'Product page',
      thinking: 'Preparing a reply', fallback: 'The AI could not reply right now · on-site search result',
      refusal: 'I can’t answer that. You can ask another question about TerraTwin.',
      suggestions: ['What is TerraTwin?', 'Why is Lake Salda a Mars analog?', 'What is the Shackleton target?', 'Which NASA data are used?', 'What are the limits of analogs?'],
      project: 'About the project', sitesTitle: 'Sites in the atlas', datasetsTitle: 'NASA data product catalog', catsTitle: 'Evidence levels and atlas markers',
      criteria: 'Criteria', weights: 'Mission weights', methodSuffix: 'criteria and mission weights',
      category: 'Evidence level', ratings: 'Qualitative rating (out of 3)', datasets: 'Data', coverage: 'Coverage', use: 'Use', caveat: 'Caveat', aka: 'Also known as',
      bodies: { earth: 'Earth', moon: 'Moon', mars: 'Mars' },
      pilot: 'Pilot analysis', pilotLimits: 'Limitations of the pilot analysis', pilotScores: 'Computed mission scores',
      period: 'Observation period', validation: 'Validation', target: 'target', noScore: 'no score released because data coverage is insufficient',
      scoreNote: 'Scores are a partial operational pre-screen on a 0–100 scale; they are not NASA endorsement or full analog validation. Details are in the analysis panel of the Atlas section.',
      scored: 'areas received a score', top: 'Highest', noRank: 'data coverage is insufficient in most areas, so a ranking is not meaningful',
      roles: { candidate: 'candidate', negative_control: 'negative control' }
    }
  };

  const state = {
    lang: (window.TerraTwinState ? window.TerraTwinState().lang : document.documentElement.lang) === 'en' ? 'en' : 'tr',
    open: false, busy: false, history: [], analysis: null, analysisTried: false, greeted: false
  };
  const S = () => STR[state.lang];
  const cache = {};

  /* ---------- içerik: sitedeki metinlerden pasajlar ---------- */
  const parser = new DOMParser();
  const strip = (html) => (parser.parseFromString(String(html), 'text/html').body.textContent || '').replace(/\s+/g, ' ').trim();
  function nodeText(n, lang) {
    const key = n.dataset.i18n;
    if (lang === 'en' && D.en && D.en[key] != null) return strip(D.en[key]);
    return strip(n._tr != null ? n._tr : n.innerHTML);
  }

  function blockTitle(c, lang) {
    if (c.matches('article, .formula')) { const own = c.querySelector('h3[data-i18n]'); if (own) return nodeText(own, lang); }
    let prev = (c.parentElement && c.parentElement.matches('.tbl-scroll') ? c.parentElement : c).previousElementSibling;
    while (prev) {
      if (prev.matches('h3[data-i18n]')) return nodeText(prev, lang);
      if (prev.matches('h2, .head')) break;
      prev = prev.previousElementSibling;
    }
    return '';
  }

  function blockLines(c, nodes, lang) {
    const tx = (n) => nodeText(n, lang);
    if (c.matches('table')) return $$('tr', c).map((tr) => $$('[data-i18n]', tr).map(tx).join(' — ')).filter(Boolean);
    if (c.matches('.versus')) {
      const heads = $$('.vs-head h3', c).map(tx);
      return $$('.vs-row', c).map((row) => {
        const a = row.nextElementSibling, b = a && a.nextElementSibling;
        return `${tx(row)} — ${heads[0] || 'A'}: ${a ? tx(a) : ''} / ${heads[1] || 'B'}: ${b ? tx(b) : ''}`;
      });
    }
    if (c.matches('.say')) return $$('p.no', c).map((no) => `✗ ${tx(no)} → ✓ ${no.nextElementSibling ? tx(no.nextElementSibling) : ''}`);
    if (c.matches('dl')) return $$(':scope > div', c).map((d) => { const dt = $('dt', d), dd = $('dd', d); return dt && dd ? `${tx(dt)}: ${tx(dd)}` : ''; }).filter(Boolean);
    if (c.matches('.principles')) return $$(':scope > div', c).map((d) => { const h = $('h3', d), p = $('p', d); return h && p ? `${tx(h)}: ${tx(p)}` : ''; }).filter(Boolean);
    if (c.matches('.formula')) { const eq = $('.eq', c); return [eq ? eq.textContent.replace(/\s+/g, ' ').trim() : ''].concat(nodes.filter((n) => !n.matches('h3')).map(tx)).filter(Boolean); }
    if (c.matches('article')) return nodes.filter((n) => !n.matches('h3')).map(tx);
    return nodes.map(tx);
  }

  function domPassages(lang) {
    const out = [], L = STR[lang];
    $$('main > section, footer.foot').forEach((sec, si) => {
      const idx = $('.idx[data-i18n]', sec);
      const short = sec.matches('.hero') ? 'TerraTwin' : sec.matches('footer') ? L.project : idx ? nodeText(idx, lang).replace(/^[\d\s—–-]+/, '') : 'TerraTwin';
      const anchor = sec.id ? '#' + sec.id : sec.matches('.hero') ? '#top' : '';
      const groups = new Map();
      $$('[data-i18n]', sec).forEach((n) => {
        if (n.matches('button, .idx, .ctl-label, .hero-tag, .btn, .map-hint, h3.label') || n.closest('.stats, .atlas-controls, .w-controls, .foot-link')) return;
        const c = n.closest('article') || n.closest('table, ol, ul, dl, .versus, .say, .principles, .formula') || sec;
        if (!groups.has(c)) groups.set(c, []);
        groups.get(c).push(n);
      });
      let gi = 0;
      groups.forEach((nodes, c) => {
        const lines = c === sec ? nodes.map((n) => nodeText(n, lang)) : blockLines(c, nodes, lang);
        if (!lines.length) return;
        const own = c === sec ? '' : blockTitle(c, lang);
        const p = { id: `sec:${si}:${gi++}`, kind: 'section', title: own || short, section: own ? short : '', lines, anchor };
        if (c.matches && c.matches('article')) p.chips = $$('.chips span', c).map((s) => s.textContent.trim());
        out.push(p);
      });
    });
    return out;
  }

  function dataPassages(lang) {
    const out = [], L = STR[lang], U = D.ui || {}, other = lang === 'tr' ? 'en' : 'tr';
    const catLabel = (k) => (D.cats && D.cats[k] ? pick(D.cats[k].label, lang) : k);
    const sites = D.sites || [], datasets = D.datasets || [];

    sites.forEach((s) => {
      const name = pick(s.name, lang), alt = pick(s.name, other);
      const ratings = (s.r || []).map((v, i) => `${pick((U.ratingLabels || [])[i], lang)}: ${v == null ? pick(U.unrated, lang) : v}`).join(' · ');
      const blocks = [
        { h: L.category, p: catLabel(s.cat) },
        { h: pick(U.basis, lang), p: pick(s.basis, lang) },
        { h: pick(s.cat === 'hypo' ? U.likeHypo : U.like, lang), p: pick(s.like, lang) },
        { h: pick(U.limit, lang), p: pick(s.limit, lang) },
        { h: L.ratings, p: ratings + (s.r && s.r.some((v) => v != null) ? ` — ${pick(U.qual, lang)}` : '') }
      ].filter((b) => b.h && b.p);
      if (s.note) blocks.push({ h: lang === 'tr' ? 'Not' : 'Note', p: pick(s.note, lang) });
      out.push({
        id: 'site:' + s.id, kind: 'site', title: name, sub: [pick(s.loc, lang), pick(s.tag, lang)].filter(Boolean).join(' · '),
        section: L.sitesTitle, keys: alt, alt: alt !== name ? alt : '', blocks, chips: s.data || [],
        siteId: s.id, url: s.src ? s.src[1] : '', urlLabel: s.src ? `${L.source}: ${s.src[0]}` : ''
      });
    });

    if (sites.length) out.push({
      id: 'sites', kind: 'overview', title: `${L.sitesTitle} (${sites.length})`, keys: 'saha sahalar liste analog analoglar site sites list analogs', anchor: '#atlas',
      lines: Object.keys(D.cats || {}).map((k) => { const list = sites.filter((s) => s.cat === k); return list.length ? `${catLabel(k)} (${list.length}): ${list.map((s) => pick(s.name, lang)).join(', ')}` : ''; }).filter(Boolean)
    });
    if (D.cats) out.push({
      id: 'cats', kind: 'overview', title: L.catsTitle, anchor: '#atlas',
      lines: Object.keys(D.cats).map((k) => `${catLabel(k)} — ${sites.filter((s) => s.cat === k).length}`).concat(U.qual ? [pick(U.qual, lang)] : [])
    });

    datasets.forEach((d, i) => out.push({
      id: 'data:' + i, kind: 'dataset', title: d.n, sub: [pick(d.s, lang), L.bodies[d.b] || d.b].filter(Boolean).join(' · '), section: L.datasetsTitle,
      blocks: [{ h: L.coverage, p: pick(d.g, lang) }, { h: L.use, p: pick(d.u, lang) }, { h: L.caveat, p: pick(d.c, lang) }].filter((b) => b.p),
      url: d.url || '', urlLabel: L.product, anchor: '#veri'
    }));
    if (datasets.length) out.push({
      id: 'datasets', kind: 'overview', title: L.datasetsTitle, anchor: '#veri',
      lines: ['earth', 'moon', 'mars'].map((b) => { const list = datasets.filter((d) => d.b === b); return list.length ? `${L.bodies[b]} (${list.length}): ${list.map((d) => d.n).join(', ')}` : ''; }).filter(Boolean)
    });

    Object.keys(D.method || {}).forEach((k) => {
      const P = D.method[k]; if (!P || !Array.isArray(P.criteria)) return;
      const codes = P.criteria.map((c) => c.code);
      out.push({
        id: 'method:' + k, kind: 'method', title: `${pick(P.label, lang)} — ${L.methodSuffix}`, anchor: '#yontem',
        lines: P.criteria.map((c) => `${c.code} ${pick(c.name, lang)}: ${pick(c.earth, lang)} (${pick(c.data, lang)})`)
          .concat((P.missions || []).map((m) => `${L.weights} · ${pick(m.name, lang)}: ${(m.w || []).map((w, i) => `${codes[i]} ${w}`).join(', ')}`))
      });
    });
    return out;
  }

  function analysisPassages(lang) {
    const A = state.analysis, L = STR[lang], out = [];
    if (!A) return out;
    try {
      const ex = A.experiment || {}, v = A.validation || {};
      const lines = [pick(ex.description, lang)];
      if (ex.period) lines.push(`${L.period}: ${ex.period.start} – ${ex.period.end}`);
      if (v.conclusion) lines.push(`${L.validation}: ${pick(v.conclusion, lang)}`);
      if (Array.isArray(v.checks)) lines.push(`${L.validation} (${v.checks.length}): ${v.checks.map((c) => `${c.id} = ${c.status}`).join('; ')}`);
      out.push({ id: 'pilot', kind: 'analysis', title: pick(ex.title, lang) || L.pilot, section: L.pilot, lines: lines.filter(Boolean), anchor: '#analysis-panel' });
      if (Array.isArray(A.limitations) && A.limitations.length) out.push({ id: 'pilot-limits', kind: 'analysis', title: L.pilotLimits, section: L.pilot, lines: A.limitations.map((x) => pick(x, lang)), anchor: '#analysis-panel' });

      const api = window.TerraTwinAnalysis, sites = Array.isArray(A.sites) ? A.sites : [];
      const first = sites.find((s) => s.scores);
      if (api && first) {
        const scoreLines = [];
        Object.keys(first.scores).forEach((profile) => {
          const block = first.scores[profile], target = (A.targets || []).find((t) => t.id === block.targetId);
          (block.missions || []).forEach((m, i) => {
            const ok = api.rankSites(sites, profile, i).map((s) => ({ s, r: api.scoreFor(s, profile, i) })).filter((x) => x.r && x.r.status !== 'insufficient' && finite(x.r.score));
            const head = `${target ? pick(target.name, lang) : profile} (${L.target}) · ${pick(m.name, lang)}`;
            const role = (s) => (s.role && s.role !== 'reference' ? ` [${L.roles[s.role] || String(s.role).replace(/_/g, ' ')}]` : '');
            scoreLines.push(!ok.length ? `${head} — ${L.noScore}`
              : ok.length * 2 < sites.length ? `${head} — ${ok.length}/${sites.length} ${L.scored}; ${L.noRank}`
              : `${head} — ${ok.length}/${sites.length} ${L.scored}. ${L.top}: ${ok.slice(0, 5).map((x) => `${pick(x.s.name, lang)}${role(x.s)} ${x.r.score.toFixed(1)}`).join('; ')}`);
          });
        });
        if (scoreLines.length) out.push({ id: 'pilot-scores', kind: 'analysis', title: L.pilotScores, section: L.pilot, lines: scoreLines.concat([L.scoreNote]), anchor: '#analysis-panel' });
      }
    } catch (e) { /* analiz özeti üretilemezse rehber sayfa içeriğiyle çalışmaya devam eder */ }
    return out;
  }

  /* ---------- arama ---------- */
  const STOP = new Set(('ve ile bir bu su o mi mu ne nedir nelerdir neler nasil neden niye hangi hangisi kac icin de da ki hakkinda bilgi ver verir misin musun anlat anlatir soyle lutfen var yok daha en cok olan olarak gibi gore kadar nerede neresi kim kimdir midir mudur acaba bana bize ' +
    'the a an is are was were what which how why where who whom of in on at for to and or about tell me us please do does did can could you it its this that these those with there any be has have').split(' '));
  const fold = (s) => String(s).toLocaleLowerCase('tr').normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/ı/g, 'i');
  const tokens = (s) => fold(s).replace(/['’`][a-z]+/g, ' ').split(/[^a-z0-9]+/).filter((t) => t.length > 1 && !STOP.has(t));
  const uniq = (a) => Array.from(new Set(a));

  function match(q, d) {
    if (q === d) return 1;
    const a = q.length <= d.length ? q : d, b = a === q ? d : q;
    if (a.length >= 3 && b.startsWith(a) && b.length - a.length <= 4) return .8;
    if (a.length >= 5 && a.slice(0, 5) === b.slice(0, 5)) return .6;
    return 0;
  }
  const best = (q, set) => { let w = 0; for (const d of set) { const m = match(q, d); if (m > w) { w = m; if (w === 1) break; } } return w; };

  const plainLines = (p) => [p.sub || ''].concat((p.blocks || []).map((b) => `${b.h}: ${b.p}`), p.lines || [], p.chips && p.chips.length ? [p.chips.join(', ')] : []).filter(Boolean);

  function passages(lang) {
    if (!cache[lang]) {
      const list = domPassages(lang).concat(dataPassages(lang), analysisPassages(lang));
      list.forEach((p) => { p.tt = uniq(tokens(`${p.title} ${p.keys || ''}`)); p.bt = uniq(tokens(`${plainLines(p).join(' ')} ${p.section || ''}`)); });
      cache[lang] = list;
    }
    return cache[lang];
  }

  function search(q, lang) {
    const P = passages(lang), qt = uniq(tokens(q));
    if (!qt.length) return [];
    const rows = qt.map((t) => {
      const w = P.map((p) => { const wt = best(t, p.tt); return { wt, wb: wt === 1 ? 0 : best(t, p.bt) }; });
      const df = w.filter((x) => x.wt || x.wb).length;
      return { t, w, df, idf: Math.log(1 + P.length / (df + .5)) };
    });
    const total = rows.reduce((s, r) => s + r.idf, 0);
    return P.map((p, i) => {
      let score = 0, matched = 0, n = 0, distinct = false;
      rows.forEach((r) => {
        const { wt, wb } = r.w[i], m = Math.max(wt, wb);
        if (!m) return;
        score += r.idf * Math.max(wt * 2.5, wb); matched += r.idf * m; n += 1;
        /* Başlıkta geçen ender bir sözcük (saha, ürün veya hedef adı) tek başına yeterli sayılır. */
        if (r.t.length >= 5 && r.df <= 6 && wt >= .8) distinct = true;
      });
      return { p, score, n, cov: matched / total, distinct };
    }).filter((h) => h.score > 0).sort((a, b) => b.score - a.score);
  }

  /* ---------- arayüz ---------- */
  const MARK = '<svg viewBox="0 0 34 20" aria-hidden="true"><circle cx="11" cy="10" r="8"/><circle cx="23" cy="10" r="8"/></svg>';
  const root = el('div', 'ttc');
  root.id = 'tt-chat';
  root.innerHTML = `
    <button type="button" class="ttc-launch" aria-expanded="false" aria-controls="ttc-panel">${MARK}<span></span></button>
    <section class="ttc-panel" id="ttc-panel" role="dialog" aria-labelledby="ttc-title" hidden>
      <header class="ttc-head">
        <div><p class="ttc-mode${REMOTE ? ' is-ai' : ''}"><i></i><span></span></p><h2 class="ttc-title" id="ttc-title"></h2></div>
        <button type="button" class="ttc-close">×</button>
      </header>
      <div class="ttc-log" role="log" aria-live="polite" tabindex="0"></div>
      <div class="ttc-suggest"></div>
      <form class="ttc-form">
        <label class="ttc-sr" for="ttc-input"></label>
        <textarea id="ttc-input" rows="1" maxlength="600" autocomplete="off"></textarea>
        <button type="submit">↑</button>
      </form>
      <p class="ttc-note"></p>
    </section>`;
  document.body.appendChild(root);
  const ui = {
    launch: $('.ttc-launch', root), panel: $('.ttc-panel', root), log: $('.ttc-log', root), suggest: $('.ttc-suggest', root),
    form: $('.ttc-form', root), input: $('#ttc-input', root), send: $('.ttc-form button', root), close: $('.ttc-close', root)
  };

  const scrollEnd = () => { ui.log.scrollTop = ui.log.scrollHeight; };
  /* Uzun bir yanıtta okuma yanıtın başından başlasın; kısa yanıtlar yine en alta oturur. */
  const showTop = (node) => {
    if (!node || !node.isConnected) return;
    const prev = node.previousElementSibling, anchor = prev && prev.classList.contains('ttc-user') ? prev : node;
    ui.log.scrollTop = anchor.offsetTop - ui.log.offsetTop - 8;
  };
  const narrow = () => window.matchMedia('(max-width: 620px)').matches;

  function relabel() {
    const L = S();
    $('span', ui.launch).textContent = L.launch;
    $('.ttc-title', root).textContent = L.title;
    $('.ttc-mode span', root).textContent = REMOTE ? L.modeAi : L.modeLocal;
    $('.ttc-note', root).textContent = REMOTE ? L.noteAi : L.noteLocal;
    $('.ttc-sr', root).textContent = L.inputLabel;
    ui.input.placeholder = L.placeholder;
    ui.send.setAttribute('aria-label', L.send);
    ui.close.setAttribute('aria-label', L.close);
    if (!ui.suggest.hidden) renderSuggestions();
    const hello = $('.ttc-hello', ui.log);
    if (hello) hello.textContent = L.hello;
  }

  function renderSuggestions() {
    ui.suggest.textContent = '';
    S().suggestions.forEach((q) => { const b = el('button', '', q); b.type = 'button'; b.addEventListener('click', () => submit(q)); ui.suggest.appendChild(b); });
    ui.suggest.hidden = false;
  }

  function addMsg(role, cls) {
    const n = el('div', `ttc-msg ttc-${role}${cls ? ' ' + cls : ''}`);
    ui.log.appendChild(n);
    return n;
  }

  /* Model yanıtı için küçük ve güvenli biçimlendirme: kalın, kod, bağlantı, madde listesi. */
  function inline(parent, s) {
    const re = /\*\*([^*]+)\*\*|`([^`]+)`|\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)|(https?:\/\/[^\s<>()]+[^\s<>().,;:!?])/g;
    let last = 0, m;
    while ((m = re.exec(s))) {
      if (m.index > last) parent.append(s.slice(last, m.index));
      if (m[1]) parent.append(el('strong', '', m[1]));
      else if (m[2]) parent.append(el('code', '', m[2]));
      else { const a = el('a', '', m[3] || m[5]); a.href = m[4] || m[5]; a.target = '_blank'; a.rel = 'noopener noreferrer'; parent.append(a); }
      last = re.lastIndex;
    }
    if (last < s.length) parent.append(s.slice(last));
  }
  function mdLite(text) {
    const frag = document.createDocumentFragment();
    let list = null;
    String(text).split('\n').forEach((raw) => {
      const line = raw.trim();
      if (!line) { list = null; return; }
      const item = line.match(/^(?:[-*•]|\d+[.)])\s+(.*)$/);
      if (item) {
        const tag = /^\d/.test(line) ? 'OL' : 'UL';
        if (!list || list.tagName !== tag) { list = el(tag.toLowerCase()); frag.append(list); }
        const li = el('li'); inline(li, item[1]); list.append(li);
        return;
      }
      list = null;
      const p = el('p'), h = line.match(/^#{1,6}\s+(.*)$/);
      if (h) { const b = el('strong'); inline(b, h[1]); p.append(b); } else inline(p, line);
      frag.append(p);
    });
    return frag;
  }

  function renderPhoto(node, id) {
    const ph = window.TT_PHOTOS && window.TT_PHOTOS[id];
    if (!ph) return;
    const fig = el('figure', 'ttc-photo'), img = el('img'), cap = el('figcaption'), a = el('a');
    img.src = ph.src; img.width = ph.w; img.height = ph.h; img.alt = pick(ph.cap, state.lang);
    img.decoding = 'async'; img.referrerPolicy = 'no-referrer';
    if (ph.pos) img.style.objectPosition = ph.pos;
    img.addEventListener('load', () => showTop(node));
    img.addEventListener('error', () => fig.remove());
    const lic = state.lang === 'en' ? ({ 'Kamu malı': 'Public domain', 'Atıf': 'Attribution' }[ph.license] || ph.license) : ph.license;
    a.href = ph.page; a.target = '_blank'; a.rel = 'noopener noreferrer'; a.textContent = `${ph.artist}, ${lic} ↗`;
    cap.append(`${pick(ph.cap, state.lang)} · `, a);
    fig.append(img, cap);
    node.append(fig);
  }

  function renderPassage(node, p, related) {
    const L = S();
    if (p.siteId) renderPhoto(node, p.siteId);
    if (p.section) node.append(el('p', 'ttc-a-kicker', p.section));
    node.append(el('p', 'ttc-a-title', p.title));
    if (p.sub) node.append(el('p', 'ttc-a-sub', p.sub));
    (p.blocks || []).forEach((b) => { const d = el('div', 'ttc-a-block'); d.append(el('h4', '', b.h), el('p', '', b.p)); node.append(d); });
    const lines = p.lines || [];
    if (lines.length === 1) node.append(el('p', '', lines[0]));
    else if (lines.length) {
      const ul = el('ul');
      lines.slice(0, 7).forEach((t) => ul.append(el('li', '', t)));
      node.append(ul);
      if (lines.length > 7) node.append(el('p', 'ttc-a-sub', L.more));
    }
    if (p.chips && p.chips.length) { const c = el('p', 'ttc-chips'); p.chips.forEach((t) => c.append(el('span', '', t))); node.append(c); }
    const actions = el('p', 'ttc-actions');
    if (p.siteId) {
      const b = el('button', '', L.showAtlas); b.type = 'button';
      b.addEventListener('click', () => {
        document.dispatchEvent(new CustomEvent('terratwin:select-site', { detail: { id: p.siteId } }));
        const card = $('#site-card'); if (card) card.scrollIntoView({ behavior: 'smooth', block: 'center' });
        if (narrow()) toggle(false);
      });
      actions.append(b);
    }
    if (p.anchor && $(p.anchor)) { const a = el('a', '', L.goSection); a.href = p.anchor; a.addEventListener('click', () => { if (narrow()) toggle(false); }); actions.append(a); }
    if (p.url) { const a = el('a', '', `${p.urlLabel} ↗`); a.href = p.url; a.target = '_blank'; a.rel = 'noopener noreferrer'; actions.append(a); }
    if (actions.childNodes.length) node.append(actions);
    if (related && related.length) {
      const r = el('div', 'ttc-related'); r.append(el('span', '', L.related));
      related.forEach((h) => { const b = el('button', '', h.p.title); b.type = 'button'; b.addEventListener('click', () => { const n = addMsg('bot'); renderPassage(n, h.p); showTop(n); }); r.append(b); });
      node.append(r);
    }
  }

  function answerLocal(q, notice) {
    const L = S(), node = addMsg('bot'), f = fold(q).trim();
    if (notice) node.append(el('p', 'ttc-notice', notice));
    let text;
    if (/^(merhaba|selam|hey|gunaydin|iyi (gunler|aksamlar)|hi|hello|good (morning|evening))\b/.test(f) && tokens(q).length <= 2) { text = L.hello; node.append(el('p', '', text)); renderSuggestions(); }
    else if (/(tesekkur|sagol|sag ol|thanks|thank you)/.test(f) && tokens(q).length <= 3) { text = L.thanks; node.append(el('p', '', text)); }
    else if (/(sen kimsin|kimsin|nesin|ne yapabilirsin|who are you|what can you do)/.test(f)) { text = L.about; node.append(el('p', '', text)); renderSuggestions(); }
    else {
      /* Tek sözcük tutan çok sözcüklü sorular (ör. "Kanada'da hava nasıl") konu dışı sayılır. */
      const hits = search(q, state.lang), words = uniq(tokens(q)).length, top = hits[0];
      const good = (h) => h.distinct || (h.cov >= .5 && (h.n >= 2 || words === 1));
      if (top && good(top)) {
        renderPassage(node, top.p, hits.slice(1, 6).filter(good).slice(0, 2));
        text = `${top.p.title}\n${plainLines(top.p).join('\n')}`;
      } else if (top && top.n >= 2 && top.cov >= .35) {
        text = L.unsure; node.append(el('p', '', text));
        const r = el('div', 'ttc-related');
        hits.slice(0, 3).forEach((h) => { const b = el('button', '', h.p.title); b.type = 'button'; b.addEventListener('click', () => { const n = addMsg('bot'); renderPassage(n, h.p); showTop(n); }); r.append(b); });
        node.append(r);
      } else { text = L.offTopic; node.append(el('p', '', text)); renderSuggestions(); }
    }
    state.history.push({ role: 'assistant', content: text.slice(0, 1400) });
    showTop(node);
  }

  async function askRemote(q) {
    const L = S(), node = addMsg('bot', 'is-pending');
    node.textContent = L.thinking;
    scrollEnd();
    let text = '', refused = false;
    try {
      const init = { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ lang: state.lang, messages: state.history.slice(-12) }) };
      if (typeof AbortSignal !== 'undefined' && AbortSignal.timeout) init.signal = AbortSignal.timeout(90000);
      const res = await fetch(CFG.endpoint, init);
      if (!res.ok || !res.body) throw new Error('HTTP ' + res.status);
      const reader = res.body.getReader(), dec = new TextDecoder();
      let buf = '', done = false;
      while (!done) {
        const r = await reader.read();
        if (r.done) break;
        buf += dec.decode(r.value, { stream: true });
        let i;
        while ((i = buf.indexOf('\n\n')) >= 0) {
          const frame = buf.slice(0, i); buf = buf.slice(i + 2);
          frame.split('\n').forEach((line) => {
            if (!line.startsWith('data:')) return;
            let ev; try { ev = JSON.parse(line.slice(5)); } catch (e) { return; }
            if (ev.error) throw new Error('upstream');
            if (ev.reset) text = '';
            if (ev.refusal) refused = true;
            if (ev.done) done = true;
            if (typeof ev.t === 'string') {
              text += ev.t;
              node.classList.remove('is-pending'); node.textContent = ''; node.append(mdLite(text)); scrollEnd();
            }
          });
        }
      }
      if (refused) text = L.refusal;
      if (!text.trim()) throw new Error('empty');
      node.classList.remove('is-pending'); node.textContent = ''; node.append(mdLite(text));
      state.history.push({ role: 'assistant', content: text.slice(0, 1400) });
      scrollEnd();
    } catch (e) {
      node.remove();
      answerLocal(q, L.fallback);
    }
  }

  async function submit(q) {
    q = String(q || '').trim();
    if (!q || state.busy) return;
    state.busy = true; ui.send.disabled = true; ui.suggest.hidden = true;
    addMsg('user').textContent = q;
    state.history.push({ role: 'user', content: q.slice(0, 600) });
    ui.input.value = ''; ui.input.style.height = '';
    try { if (REMOTE) await askRemote(q); else answerLocal(q); }
    finally { state.busy = false; ui.send.disabled = false; }
  }

  function loadAnalysis() {
    if (state.analysisTried) return;
    state.analysisTried = true;
    fetch('site/analysis-results.json').then((r) => (r.ok ? r.json() : null)).then((data) => {
      if (data && Array.isArray(data.sites)) { state.analysis = data; delete cache.tr; delete cache.en; }
    }).catch(() => { /* dosya okunamazsa rehber sayfa içeriğiyle çalışır */ });
  }

  function toggle(open) {
    state.open = open;
    root.classList.toggle('is-open', open);
    ui.panel.hidden = !open;
    ui.launch.setAttribute('aria-expanded', String(open));
    if (open) {
      if (!state.greeted) { state.greeted = true; addMsg('bot').append(el('p', 'ttc-hello', S().hello)); renderSuggestions(); }
      loadAnalysis();
      ui.input.focus();
    } else ui.launch.focus();
  }

  ui.launch.addEventListener('click', () => toggle(true));
  ui.close.addEventListener('click', () => toggle(false));
  root.addEventListener('keydown', (ev) => { if (ev.key === 'Escape' && state.open) { ev.stopPropagation(); toggle(false); } });
  ui.form.addEventListener('submit', (ev) => { ev.preventDefault(); submit(ui.input.value); });
  ui.input.addEventListener('keydown', (ev) => { if (ev.key === 'Enter' && !ev.shiftKey && !ev.isComposing) { ev.preventDefault(); submit(ui.input.value); } });
  ui.input.addEventListener('input', () => { ui.input.style.height = ''; ui.input.style.height = Math.min(ui.input.scrollHeight, 120) + 'px'; });
  document.addEventListener('terratwin:state', (ev) => {
    const lang = ev.detail && ev.detail.lang === 'en' ? 'en' : 'tr';
    if (lang !== state.lang) { state.lang = lang; relabel(); }
  });
  relabel();

  /* Ara sunucudaki bilgi metnini yenilemek için: konsolda copy(TTChat.knowledge('en')) */
  window.TTChat = {
    open: () => toggle(true),
    ask: (q) => { if (!state.open) toggle(true); return submit(q); },
    search: (q, lang) => search(q, lang || state.lang).slice(0, 5).map((h) => ({ title: h.p.title, score: +h.score.toFixed(2), cov: +h.cov.toFixed(2), n: h.n, distinct: h.distinct })),
    knowledge,
    /* Ara sunucu dosyasındaki KNOWLEDGE bloğuna yapıştırmaya hazır (kaçışlı) metin. */
    workerKnowledge: () => knowledge('en').replace(/\\/g, '\\\\').replace(/`/g, '\\`').replace(/\$\{/g, '\\${')
  };

  function knowledge(lang) {
    const l = lang === 'tr' ? 'tr' : 'en';
    return passages(l).map((p) => `## ${p.section ? p.section + ' › ' : ''}${p.title}${p.alt ? ` (${STR[l].aka}: ${p.alt})` : ''}\n${plainLines(p).map((t) => '- ' + t).join('\n')}${p.url ? '\n- ' + p.url : ''}`).join('\n\n');
  }
})();
