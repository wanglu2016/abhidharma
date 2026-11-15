/* Concept atlas: select a concept, show its card, highlight related concepts. Data: window.ATLAS */
(function () {
  var A = window.ATLAS; if (!A) return;
  var byId = {}; A.concepts.forEach(function (c) { byId[c.id] = c; });
  var atlas = document.getElementById('atlas');
  var panel = document.getElementById('panel');
  var chips = atlas.querySelectorAll('.chip[data-id]');
  var tierBoxes = document.querySelectorAll('[data-tier-filter]');
  var memoBox = document.getElementById('f-memo');
  var search = document.getElementById('f-search');
  var current = null;

  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function bi(zh, en) { return '<span class="zh" lang="zh-Hans">' + zh + '</span><span class="en" lang="en">' + en + '</span>'; }
  function pinName(id) { var p = A.pins[id]; return bi(p.s, p.en); }

  function render(c) {
    var t = A.tiers[c.tier];
    var h = '<button type="button" class="close" aria-label="Close">×</button>';
    h += '<h3>' + (t[2] ? '<span class="mk" title="' + esc(t[0]) + '">' + t[2] + '</span>' : '') + esc(c.s) + (c.memo ? '<span class="memo" title="入门必背">背</span>' : '') + '</h3>';
    if (c.t !== c.s) h += '<div class="trad" lang="zh-Hant">' + esc(c.t) + '</div>';
    h += '<div class="meta"><i class="skt">' + esc(c.skt) + '</i><br><span lang="en">' + esc(c.en) + '</span><br>' + pinName(c.pin) + '<br>' + bi(t[0], t[1]);
    if (c.mile) h += '<span class="mile">' + bi(esc(c.mile[0]), esc(c.mile[1])) + '</span>';
    h += '</div><div class="def">';
    for (var i = 0; i < c.zh.length; i++) h += '<p class="zh" lang="zh-Hans">' + esc(c.zh[i]) + '</p><p class="en" lang="en">' + esc(c.enl[i]) + '</p>';
    h += '</div>';
    if (c.note_zh) h += '<div class="callout">' + bi(esc(c.note_zh), esc(c.note_en)) + '</div>';
    if (c.verses.length) {
      h += '<h4>' + bi('颂', 'Verses') + '</h4>';
      c.verses.forEach(function (v) { h += '<div class="vref"><a href="verses.html#' + v.id + '">' + esc(A.pins[v.pin].short) + ' ' + esc(v.label) + '</a>　<span lang="zh-Hant">' + esc(v.text) + '</span></div>'; });
    }
    var links = [];
    if (c.wz.length) links.push(bi('纲要', 'Outline') + ' ' + c.wz.map(function (s) { return '<a href="outline.html#s' + s.replace('.', '-') + '">' + s + '</a>'; }).join(' '));
    if (c.jt.length) links.push(bi('九题', 'Nine Questions') + ' ' + c.jt.map(function (n) { return '<a href="jiuti.html#q' + n + '">' + bi('第' + n + '题', 'Q' + n) + '</a>'; }).join(' '));
    if (c.bx.length) links.push(bi('英译百瑕', 'Translation flaws') + ' ' + c.bx.map(function (n) { return '<a href="translations.html#f' + n + '">#' + n + '</a>'; }).join(' '));
    if (links.length) h += '<h4>' + bi('去处', 'Read further') + '</h4><div>' + links.join('<br>') + '</div>';
    if (c.rel.length) {
      h += '<h4>' + bi('相关', 'Related') + '</h4><div>';
      c.rel.forEach(function (r) { var o = byId[r]; if (o) h += '<button type="button" class="chip" data-go="' + r + '">' + esc(o.s) + '</button>'; });
      h += '</div>';
    }
    h += '<p class="note" style="margin-top:.8rem"><a href="concepts.html#' + c.id + '">' + bi('在概念页查看', 'Open on the concepts page') + '</a></p>';
    panel.innerHTML = h;
    panel.classList.remove('idle');
    panel.querySelector('.close').addEventListener('click', clear);
    Array.prototype.forEach.call(panel.querySelectorAll('[data-go]'), function (b) { b.addEventListener('click', function () { select(this.getAttribute('data-go'), true); }); });
  }

  function clear() {
    current = null;
    atlas.classList.remove('focus');
    Array.prototype.forEach.call(chips, function (ch) { ch.classList.remove('on', 'rel'); ch.setAttribute('aria-pressed', 'false'); });
    panel.classList.add('idle');
    panel.innerHTML = panel.getAttribute('data-empty');
    if (history.replaceState) history.replaceState(null, '', location.pathname);
  }

  function select(id, scroll) {
    var c = byId[id]; if (!c) return;
    current = id;
    var rel = {}; c.rel.forEach(function (r) { rel[r] = 1; });
    A.concepts.forEach(function (o) { if (o.rel.indexOf(id) >= 0) rel[o.id] = 1; });
    Array.prototype.forEach.call(chips, function (ch) {
      var i = ch.getAttribute('data-id');
      ch.classList.toggle('on', i === id); ch.classList.toggle('rel', !!rel[i] && i !== id);
      ch.setAttribute('aria-pressed', i === id ? 'true' : 'false');
    });
    atlas.classList.add('focus');
    render(c);
    if (history.replaceState) history.replaceState(null, '', '#c=' + id);
    if (scroll) { var el = atlas.querySelector('.chip[data-id="' + id + '"]'); if (el && el.scrollIntoView) el.scrollIntoView({ block: 'nearest' }); }
  }

  Array.prototype.forEach.call(chips, function (ch) {
    ch.addEventListener('click', function () { var i = this.getAttribute('data-id'); if (i === current) clear(); else select(i); });
  });

  function filter() {
    var tiers = {}; Array.prototype.forEach.call(tierBoxes, function (b) { if (b.checked) tiers[b.getAttribute('data-tier-filter')] = 1; });
    var memo = memoBox && memoBox.checked;
    var q = (search && search.value || '').trim().toLowerCase();
    var active = memo || q || Object.keys(tiers).length < tierBoxes.length;
    atlas.classList.toggle('filtering', !!active);
    Array.prototype.forEach.call(chips, function (ch) {
      var c = byId[ch.getAttribute('data-id')];
      var ok = tiers[c.tier] && (!memo || c.memo);
      if (q) ok = ok && (c.s + c.t + c.skt + c.en).toLowerCase().indexOf(q) >= 0;
      ch.classList.toggle('off', !ok);
    });
  }
  Array.prototype.forEach.call(tierBoxes, function (b) { b.addEventListener('change', filter); });
  if (memoBox) memoBox.addEventListener('change', filter);
  if (search) search.addEventListener('input', filter);

  var m = /c=([a-z_]+)/.exec(location.hash);
  if (m && byId[m[1]]) select(m[1], true);
})();
