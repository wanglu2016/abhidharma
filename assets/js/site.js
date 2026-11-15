/* Language switch and small shared helpers */
(function () {
  var root = document.documentElement;
  function setLang(l) {
    root.setAttribute('data-lang', l);
    try { localStorage.setItem('abhi-lang', l); } catch (e) {}
    var bs = document.querySelectorAll('[data-set-lang]');
    for (var i = 0; i < bs.length; i++) bs[i].setAttribute('aria-pressed', bs[i].getAttribute('data-set-lang') === l ? 'true' : 'false');
    document.dispatchEvent(new CustomEvent('langchange', { detail: l }));
  }
  var bs = document.querySelectorAll('[data-set-lang]');
  for (var i = 0; i < bs.length; i++) {
    bs[i].addEventListener('click', function () { setLang(this.getAttribute('data-set-lang')); });
  }
  setLang(root.getAttribute('data-lang') || 'zh');
  window.ABHI = { lang: function () { return root.getAttribute('data-lang'); } };
})();

/* Generic list filter: [data-filter-input] filters [data-filter-item] inside [data-filter-scope] */
(function () {
  var scopes = document.querySelectorAll('[data-filter-scope]');
  Array.prototype.forEach.call(scopes, function (scope) {
    var input = scope.querySelector('[data-filter-input]');
    var selects = scope.querySelectorAll('[data-filter-select]');
    var items = scope.querySelectorAll('[data-filter-item]');
    var groups = scope.querySelectorAll('[data-filter-group]');
    var counter = scope.querySelector('[data-filter-count]');
    function run() {
      var q = input ? input.value.trim().toLowerCase() : '';
      var shown = 0;
      Array.prototype.forEach.call(items, function (it) {
        var ok = !q || (it.getAttribute('data-text') || it.textContent).toLowerCase().indexOf(q) >= 0;
        Array.prototype.forEach.call(selects, function (sel) {
          var key = sel.getAttribute('data-filter-select'), v = sel.value;
          if (v && (' ' + (it.getAttribute('data-' + key) || '') + ' ').indexOf(' ' + v + ' ') < 0) ok = false;
        });
        it.hidden = !ok;
        if (ok) shown++;
      });
      Array.prototype.forEach.call(groups, function (g) {
        g.hidden = !g.querySelector('[data-filter-item]:not([hidden])');
      });
      if (counter) counter.textContent = shown;
    }
    if (input) input.addEventListener('input', run);
    Array.prototype.forEach.call(selects, function (s) { s.addEventListener('change', run); });
    run();
  });
})();
