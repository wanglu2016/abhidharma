/* Verse drill: chapter filter, masking, random draw, click-to-reveal */
(function () {
  var body = document.body;
  var pinSel = document.getElementById('v-pin');
  var secs = document.querySelectorAll('.pin-sec');
  var maskBtns = document.querySelectorAll('[data-mask]');
  var drawBtn = document.getElementById('v-draw');
  var draw = document.getElementById('draw');
  var search = document.getElementById('v-search');
  var count = document.getElementById('v-count');

  function visibleVerses() {
    var out = [];
    Array.prototype.forEach.call(document.querySelectorAll('.verse'), function (v) {
      if (!v.closest('.pin-sec').hidden && !v.hidden && v.classList.contains('main')) out.push(v);
    });
    return out;
  }
  function applyPin() {
    var p = pinSel.value;
    Array.prototype.forEach.call(secs, function (s) { s.hidden = !!p && s.getAttribute('data-pin') !== p; });
    applySearch();
  }
  function applySearch() {
    var q = search.value.trim();
    var n = 0;
    Array.prototype.forEach.call(document.querySelectorAll('.verse'), function (v) {
      var ok = !q || v.getAttribute('data-text').indexOf(q) >= 0;
      v.hidden = !ok;
      if (ok && !v.closest('.pin-sec').hidden) n++;
    });
    if (count) count.textContent = n;
  }
  function setMask(m) {
    body.classList.remove('mask-tail', 'mask-all');
    if (m !== 'none') body.classList.add('mask-' + m);
    Array.prototype.forEach.call(maskBtns, function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-mask') === m ? 'true' : 'false'); });
    Array.prototype.forEach.call(document.querySelectorAll('.verse.shown'), function (v) { v.classList.remove('shown'); });
  }
  Array.prototype.forEach.call(maskBtns, function (b) { b.addEventListener('click', function () { setMask(this.getAttribute('data-mask')); }); });
  document.addEventListener('click', function (e) {
    var v = e.target.closest && e.target.closest('.verse');
    if (v && (body.classList.contains('mask-tail') || body.classList.contains('mask-all')) && !e.target.closest('a')) v.classList.toggle('shown');
  });
  pinSel.addEventListener('change', applyPin);
  search.addEventListener('input', applySearch);

  drawBtn.addEventListener('click', function () {
    var vs = visibleVerses(); if (!vs.length) return;
    var v = vs[Math.floor(Math.random() * vs.length)];
    Array.prototype.forEach.call(document.querySelectorAll('.verse.hl'), function (x) { x.classList.remove('hl'); });
    var first = v.querySelector('.l .h1').textContent;
    draw.hidden = false;
    draw.querySelector('.where').innerHTML = v.getAttribute('data-where');
    draw.querySelector('.v').textContent = first + '……';
    var link = draw.querySelector('a.go'); link.setAttribute('href', '#' + v.id);
    link.onclick = function () { v.classList.add('hl', 'shown'); };
    draw.querySelector('.reveal').onclick = function () { draw.querySelector('.v').textContent = v.getAttribute('data-text'); };
  });
  setMask('none');
  applyPin();
})();
