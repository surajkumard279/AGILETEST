(function () {
  'use strict';

  var S = window.SITE;
  var $ = function (sel, root) { return (root || document).querySelector(sel); };
  var $$ = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };
  var ROOT = document.body.getAttribute('data-root') || '';
  var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  var DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  var STORE_KEY = 'agile-site-cart-v1';

  function money(n) { return S.currency + Number(n).toLocaleString(S.locale); }
  function addDays(d, n) { var x = new Date(d); x.setDate(x.getDate() + n); return x; }

  /* ---------------- Sessions (shared) ---------------- */
  function buildSessions(days) {
    var out = [];
    var len = days || 2;
    if (S.customSessions && S.customSessions.length) {
      S.customSessions.forEach(function (s) {
        out.push({ start: new Date(s.start + 'T00:00:00'), length: len, timezone: s.timezone,
                   hours: s.hours || '9 AM – 5 PM', popular: !!s.popular });
      });
    } else {
      var base = new Date();
      base.setHours(0, 0, 0, 0);
      for (var w = 0; w < S.weeksAhead; w++) {
        S.patterns.forEach(function (p) {
          var from = addDays(base, 3 + w * 7);
          var diff = (p.dow - from.getDay() + 7) % 7;
          out.push({ start: addDays(from, diff), length: len, timezone: p.timezone,
                     hours: p.hours || '9 AM – 5 PM', popular: !!p.popular });
        });
      }
    }
    return out.sort(function (a, b) { return a.start - b.start; });
  }
  function dateRange(s) {
    var end = addDays(s.start, s.length - 1);
    var a = MONTHS[s.start.getMonth()] + ' ' + s.start.getDate();
    var b = (end.getMonth() === s.start.getMonth() ? '' : MONTHS[end.getMonth()] + ' ') + end.getDate();
    return s.length > 1 ? a + ' – ' + b : a;
  }
  function dayRange(s) {
    var end = addDays(s.start, s.length - 1);
    return s.length > 1 ? DAYS[s.start.getDay()] + ' – ' + DAYS[end.getDay()] : DAYS[s.start.getDay()];
  }

  /* ---------------- Static bindings ---------------- */
  $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
  $$('[data-email]').forEach(function (el) {
    el.textContent = S.email;
    el.href = 'mailto:' + S.email;
  });
  $$('[data-whatsapp]').forEach(function (el) { el.href = 'https://wa.me/' + S.whatsappNumber; });

  /* ---------------- Navigation ---------------- */
  var navToggle = $('#navToggle');
  var mainNav = $('#mainNav');
  if (navToggle && mainNav) {
    navToggle.addEventListener('click', function () {
      var open = mainNav.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', String(open));
      navToggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    });
  }
  function closeSubs() {
    $$('.has-sub.open').forEach(function (o) {
      o.classList.remove('open');
      o.querySelector('.sub-toggle').setAttribute('aria-expanded', 'false');
    });
  }
  $$('.sub-toggle').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var li = btn.parentElement;
      var willOpen = !li.classList.contains('open');
      closeSubs();
      if (willOpen) { li.classList.add('open'); btn.setAttribute('aria-expanded', 'true'); }
    });
  });
  document.addEventListener('click', closeSubs);
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeSubs(); });

  /* ---------------- Cart ---------------- */
  var cart = loadCart();
  function loadCart() {
    try {
      var parsed = JSON.parse(localStorage.getItem(STORE_KEY) || '[]');
      return Array.isArray(parsed) ? parsed : [];
    } catch (e) { return []; }
  }
  function saveCart() { try { localStorage.setItem(STORE_KEY, JSON.stringify(cart)); } catch (e) { /* blocked */ } }

  var drawer = $('#cartDrawer');
  var scrim = $('#scrim');
  var lastFocus = null;
  var live = $('#live');
  function announce(msg) { if (live) live.textContent = msg; }

  function openCart() {
    lastFocus = document.activeElement;
    drawer.inert = false;
    drawer.classList.add('open');
    scrim.hidden = false;
    document.body.classList.add('no-scroll');
    $('#cartClose').focus();
  }
  function closeCart() {
    drawer.classList.remove('open');
    drawer.inert = true;
    scrim.hidden = true;
    document.body.classList.remove('no-scroll');
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }
  $('#cartOpen').addEventListener('click', openCart);
  $('#cartClose').addEventListener('click', closeCart);
  scrim.addEventListener('click', closeCart);
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && drawer.classList.contains('open')) closeCart();
  });

  function renderCart() {
    var list = $('#cartList');
    list.innerHTML = '';
    var count = 0, total = 0;
    cart.forEach(function (item, idx) {
      count += item.qty;
      total += item.qty * item.price;
      var li = document.createElement('li');
      li.className = 'cart-item';
      var info = document.createElement('div');
      [['ci-title', item.title], ['ci-meta', item.dates + ', ' + item.time], ['ci-meta', item.qty + ' × ' + money(item.price)]]
        .forEach(function (row) {
          var p = document.createElement('p');
          p.className = row[0];
          p.textContent = row[1];
          info.appendChild(p);
        });
      var rm = document.createElement('button');
      rm.type = 'button';
      rm.className = 'link-btn';
      rm.textContent = 'Remove';
      rm.setAttribute('aria-label', 'Remove ' + item.title + ', ' + item.dates + ' from cart');
      rm.addEventListener('click', function () {
        cart.splice(idx, 1); saveCart(); renderCart(); announce('Removed from cart');
      });
      li.appendChild(info); li.appendChild(rm);
      list.appendChild(li);
    });
    $('#cartCount').textContent = count;
    $('#cartTotal').textContent = money(total);
    $('#cartSubtotal').textContent = money(total);
    $('#cartEmpty').hidden = cart.length > 0;
    $('#cartFoot').hidden = cart.length === 0;
    updateCheckout(total);
  }

  function updateCheckout(total) {
    var link = $('#checkoutLink');
    if (S.checkoutUrl) {
      link.href = S.checkoutUrl;
      link.textContent = 'Go to checkout';
      link.target = '_blank';
      link.rel = 'noopener';
      return;
    }
    var lines = ['Hello,', '', 'I would like to enroll in:', ''];
    cart.forEach(function (i) {
      lines.push('- ' + i.title + ' (' + i.dates + ', ' + i.time + '), quantity ' + i.qty);
    });
    lines.push('', 'Total: ' + money(total), '', 'Name:', 'Phone:');
    link.href = 'mailto:' + S.email + '?subject=' + encodeURIComponent('Enrollment request') +
      '&body=' + encodeURIComponent(lines.join('\n'));
  }

  $('#cartClear').addEventListener('click', function () { cart = []; saveCart(); renderCart(); });

  function addToCart(item) {
    var existing = cart.filter(function (i) {
      return i.sku === item.sku && i.dates === item.dates && i.time === item.time;
    })[0];
    if (existing) existing.qty = Math.min(20, existing.qty + item.qty);
    else cart.push(item);
    saveCart(); renderCart(); announce('Added to cart'); openCart();
  }

  /* ---------------- Home: next class card ---------------- */
  var next = $('#nextList');
  if (next) {
    var days = parseInt(next.getAttribute('data-days'), 10) || 2;
    var url = next.getAttribute('data-url');
    buildSessions(days).slice(0, 4).forEach(function (s) {
      var li = document.createElement('li');
      var a = document.createElement('a');
      a.href = url;
      var d = document.createElement('strong');
      d.textContent = dateRange(s) + ' (' + dayRange(s) + ')';
      var t = document.createElement('span');
      t.textContent = s.hours + ', ' + s.timezone;
      a.appendChild(d); a.appendChild(t);
      li.appendChild(a);
      next.appendChild(li);
    });
  }

  /* ---------------- Training page: filter ---------------- */
  var filter = $('#courseFilter');
  if (filter) {
    var status = $('#filterStatus');
    filter.addEventListener('input', function () {
      var q = filter.value.trim().toLowerCase();
      var shown = 0;
      $$('.cat-block').forEach(function (block) {
        var any = 0;
        $$('.card', block).forEach(function (card) {
          var match = !q || card.textContent.toLowerCase().indexOf(q) !== -1;
          card.hidden = !match;
          if (match) { any++; shown++; }
        });
        block.hidden = any === 0;
      });
      status.textContent = q ? (shown ? shown + ' course' + (shown === 1 ? '' : 's') + ' found.' : 'No courses match "' + filter.value + '". Try a different word.') : '';
    });
  }

  /* ---------------- Contact form ---------------- */
  var form = $('#contactForm');
  if (form) {
    var note = $('#formNote');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var data = {
        name: form.elements.name.value.trim(),
        email: form.elements.email.value.trim(),
        phone: form.elements.phone.value.trim(),
        topic: form.elements.topic.value,
        message: form.elements.message.value.trim()
      };
      if (S.formEndpoint) {
        note.textContent = 'Sending…';
        fetch(S.formEndpoint, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
          body: JSON.stringify(data)
        }).then(function (r) {
          if (!r.ok) throw new Error('bad status');
          form.reset();
          note.textContent = 'Thanks. We received your message and will reply by email.';
        }).catch(function () {
          note.textContent = 'The message could not be sent. Please email ' + S.email + ' instead.';
        });
      } else {
        var body = 'Name: ' + data.name + '\nEmail: ' + data.email + '\nPhone: ' + data.phone + '\nTopic: ' + data.topic + '\n\n' + data.message;
        window.location.href = 'mailto:' + S.email + '?subject=' + encodeURIComponent(data.topic + ' enquiry from ' + data.name) +
          '&body=' + encodeURIComponent(body);
        note.textContent = 'Your email app should open with the message filled in. If it does not, write to ' + S.email + '.';
      }
    });
  }

  /* ---------------- Login page ---------------- */
  var loginBtn = $('#loginBtn');
  if (loginBtn) {
    if (S.loginUrl) { loginBtn.href = S.loginUrl; }
    else {
      loginBtn.addEventListener('click', function (e) {
        e.preventDefault();
        $('#loginNote').hidden = false;
      });
    }
  }

  renderCart();

  window.Site = {
    ROOT: ROOT, $: $, $$: $$, money: money,
    buildSessions: buildSessions, dateRange: dateRange, dayRange: dayRange,
    addToCart: addToCart
  };
})();
