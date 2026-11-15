/* 分別根品測試一: answer key unchanged from the author's original page */
(function () {
  var form = document.getElementById('quiz');
  var key = JSON.parse(form.getAttribute('data-key'));
  var out = document.getElementById('score');
  var showBtn = document.getElementById('show-key');
  var resetBtn = document.getElementById('reset');
  function sel(n) {
    var a = []; Array.prototype.forEach.call(form.querySelectorAll('input[name="q' + n + '"]:checked'), function (i) { a.push(i.value); });
    return a.sort().join('');
  }
  function mark(showKey) {
    var total = 0;
    Object.keys(key).forEach(function (n) {
      var box = document.getElementById('qz' + n);
      var right = key[n].split('').sort().join('');
      var got = sel(n);
      var ok = got === right;
      if (ok) total += 10;
      box.classList.toggle('ok', ok); box.classList.toggle('bad', !ok);
      var res = box.querySelector('.res');
      var zh = ok ? '正确，得 10 分。' : (got ? '不正确，不得分。' : '未作答。');
      var en = ok ? 'Correct: 10 points.' : (got ? 'Incorrect: 0 points.' : 'Not answered.');
      if (showKey) { zh += '正确答案：' + right.toUpperCase().split('').join('、'); en += ' Answer: ' + right.toUpperCase().split('').join(', '); }
      res.innerHTML = '<span class="zh" lang="zh-Hans">' + zh + '</span><span class="en" lang="en">' + en + '</span>';
      Array.prototype.forEach.call(box.querySelectorAll('label'), function (l) {
        var v = l.querySelector('input').value;
        l.classList.toggle('right', showKey && right.indexOf(v) >= 0);
        l.classList.toggle('wrong', showKey && got.indexOf(v) >= 0 && right.indexOf(v) < 0);
      });
    });
    out.textContent = total;
  }
  form.addEventListener('submit', function (e) { e.preventDefault(); mark(false); showBtn.hidden = false; });
  showBtn.addEventListener('click', function () { mark(true); });
  resetBtn.addEventListener('click', function () {
    form.reset(); out.textContent = '—'; showBtn.hidden = true;
    Array.prototype.forEach.call(form.querySelectorAll('.qz'), function (b) { b.classList.remove('ok', 'bad'); b.querySelector('.res').innerHTML = ''; });
    Array.prototype.forEach.call(form.querySelectorAll('label'), function (l) { l.classList.remove('right', 'wrong'); });
  });
})();
