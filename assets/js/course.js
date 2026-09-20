(function () {
  'use strict';
  var Site = window.Site;
  var $ = Site.$;
  var buy = $('#buy');
  if (!buy) return;

  var course = {
    sku: buy.getAttribute('data-sku'),
    title: buy.getAttribute('data-title'),
    price: Number(buy.getAttribute('data-price')),
    days: parseInt(buy.getAttribute('data-days'), 10) || 2
  };

  var sessions = Site.buildSessions(course.days);
  var tzFilter = $('#tzFilter');
  var sessionSelect = $('#sessionSelect');
  var summary = $('#sessionSummary');
  var hint = $('#sessionHint');
  var errorEl = $('#sessionError');

  function label(s) { return Site.dateRange(s) + ', ' + Site.dayRange(s) + (s.popular ? ' (popular)' : ''); }

  function fillTimezones() {
    var zones = [];
    sessions.forEach(function (s) { if (zones.indexOf(s.timezone) === -1) zones.push(s.timezone); });
    tzFilter.innerHTML = '';
    var all = document.createElement('option');
    all.value = ''; all.textContent = 'All time zones';
    tzFilter.appendChild(all);
    zones.forEach(function (z) {
      var o = document.createElement('option');
      o.value = z; o.textContent = z;
      tzFilter.appendChild(o);
    });
  }

  function fillSessions() {
    var zone = tzFilter.value;
    sessionSelect.innerHTML = '';
    var first = document.createElement('option');
    first.value = ''; first.textContent = 'Choose a course date';
    sessionSelect.appendChild(first);
    sessions.forEach(function (s, i) {
      if (zone && s.timezone !== zone) return;
      var o = document.createElement('option');
      o.value = String(i);
      o.textContent = label(s) + (zone ? '' : ' – ' + s.timezone);
      sessionSelect.appendChild(o);
    });
    updateSummary();
  }

  function selected() { return sessionSelect.value === '' ? null : sessions[Number(sessionSelect.value)]; }

  function updateSummary() {
    var s = selected();
    errorEl.hidden = true;
    if (!s) { summary.hidden = true; hint.hidden = false; return; }
    $('#ssDates').textContent = Site.dateRange(s) + ' (' + Site.dayRange(s) + ')';
    $('#ssTime').textContent = s.hours + ', ' + s.timezone;
    summary.hidden = false;
    hint.hidden = true;
  }

  tzFilter.addEventListener('change', fillSessions);
  sessionSelect.addEventListener('change', updateSummary);
  $('#clearSession').addEventListener('click', function () {
    tzFilter.value = '';
    fillSessions();
    sessionSelect.focus();
  });
  fillTimezones();
  fillSessions();

  var qty = $('#qty');
  function clampQty() {
    var n = parseInt(qty.value, 10);
    if (isNaN(n) || n < 1) n = 1;
    if (n > 20) n = 20;
    qty.value = n;
    return n;
  }
  $('#qtyMinus').addEventListener('click', function () { qty.value = clampQty() - 1; clampQty(); });
  $('#qtyPlus').addEventListener('click', function () { qty.value = clampQty() + 1; clampQty(); });
  qty.addEventListener('change', clampQty);

  $('#addToCart').addEventListener('click', function () {
    var s = selected();
    if (!s) {
      errorEl.hidden = false;
      hint.hidden = true;
      sessionSelect.focus();
      return;
    }
    Site.addToCart({
      sku: course.sku,
      title: course.title,
      price: course.price,
      dates: Site.dateRange(s) + ' (' + Site.dayRange(s) + ')',
      time: s.hours + ', ' + s.timezone,
      qty: clampQty()
    });
  });
})();
