# -*- coding: utf-8 -*-
"""
Generates every HTML page from data.py.
Usage:  python build.py       (Python 3.7+, no packages needed)
"""
import html
import os
from urllib.parse import urlparse

import data as D

HERE = os.path.dirname(os.path.abspath(__file__))
esc = html.escape
CAT = {c["slug"]: c for c in D.CATEGORIES}
PAGES = []  # relative paths, for sitemap


# ------------------------------------------------------------------ helpers
def inr(n):
    """Indian digit grouping: 114880 -> 1,14,880"""
    s = str(int(n))
    if len(s) <= 3:
        return D.CURRENCY + s
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:])
        head = head[:-2]
    if head:
        parts.insert(0, head)
    return D.CURRENCY + ",".join(parts + [tail])


def ul(items, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f"<ul{c}>" + "".join(f"<li>{esc(i)}</li>" for i in items) + "</ul>"


def day_label(n):
    return f"{n}-day"


CHEV = ('<svg viewBox="0 0 12 12" width="12" height="12" aria-hidden="true"><path d="M2 4l4 4 4-4" fill="none" '
        'stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>')
CART_ICON = ('<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M3 4h2.2l2.1 10.2a1 1 0 0 0 1 .8h8.4a1 '
             '1 0 0 0 1-.76L19.5 8H6.1" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
             'stroke-linejoin="round"/><circle cx="9.5" cy="19" r="1.4" fill="currentColor"/><circle cx="16.5" cy="19" '
             'r="1.4" fill="currentColor"/></svg>')
WA_ICON = ('<svg viewBox="0 0 24 24" width="26" height="26" aria-hidden="true"><path fill="currentColor" d="M12 3C7 3 3 6.8 3 '
           '11.5c0 2 .8 3.9 2.2 5.3L4 21l4.4-1.3c1 .4 2.4.6 3.6.6 5 0 9-3.8 9-8.5S17 3 12 3z"/></svg>')


def mark(fill_bg="#1F4FD8", fill_fg="#fff"):
    return (f'<svg class="brand-mark" viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" rx="10" '
            f'fill="{fill_bg}"/><path d="M11 27 20 9l9 18h-5.2L20 19.2 16.2 27z" fill="{fill_fg}"/></svg>')


# --------------------------------------------------------------- page shell
def nav_html(P, active):
    def link(href, label, key):
        cur = ' aria-current="page"' if active == key else ""
        return f'<li><a href="{P}{href}"{cur}>{esc(label)}</a></li>'

    cats = "".join(
        f'<li><a href="{P}categories/{c["slug"]}.html">{esc(c["name"])}</a></li>'
        for c in D.CATEGORIES if c["slug"] != "ai"
    )
    tools = "".join(
        f'<li><a href="{P}tools.html#tool-{i + 1}">{esc(t[0])}</a></li>' for i, t in enumerate(D.TOOLS)
    )
    cur_t = " current" if active == "training" else ""
    cur_tools = " current" if active == "tools" else ""
    return f"""<nav class="main-nav" id="mainNav" aria-label="Main">
        <ul>
          {link("categories/ai.html", "AI Courses", "ai")}
          {link("consulting.html", "Consulting", "consulting")}
          <li class="has-sub{cur_t}">
            <button class="sub-toggle" aria-expanded="false">Training {CHEV}</button>
            <ul class="sub">
              <li><a href="{P}training.html">All training</a></li>
              {cats}
            </ul>
          </li>
          {link("coaching.html", "Coaching", "coaching")}
          <li class="has-sub{cur_tools}">
            <button class="sub-toggle" aria-expanded="false">Tools {CHEV}</button>
            <ul class="sub">
              <li><a href="{P}tools.html">All tools</a></li>
              {tools}
            </ul>
          </li>
          {link("team.html", "Team", "team")}
          {link("contact.html", "Contact", "contact")}
          {link("login.html", "Login", "login")}
        </ul>
      </nav>"""


def footer_html(P):
    cats = "".join(
        f'<li><a href="{P}categories/{c["slug"]}.html">{esc(c["name"])}</a></li>' for c in D.CATEGORIES[:6]
    )
    return f"""<footer class="site-footer">
    <div class="container footer-grid">
      <div class="footer-brand">
        <a class="brand brand-light" href="{P}index.html" aria-label="{esc(D.BRAND)} home">{mark("#fff", "#1F4FD8")}<span class="brand-name">{esc(D.BRAND)}</span></a>
        <p>Live online Agile training, consulting and coaching.</p>
        <p><a data-email href="mailto:{esc(D.EMAIL)}">{esc(D.EMAIL)}</a></p>
      </div>
      <div>
        <h2>Training</h2>
        <ul>{cats}<li><a href="{P}training.html">All training</a></li></ul>
      </div>
      <div>
        <h2>Company</h2>
        <ul>
          <li><a href="{P}consulting.html">Consulting</a></li>
          <li><a href="{P}coaching.html">Coaching</a></li>
          <li><a href="{P}tools.html">Tools</a></li>
          <li><a href="{P}team.html">Team</a></li>
          <li><a href="{P}contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h2>Legal</h2>
        <ul>
          <li><a href="{P}privacy-policy.html">Privacy policy</a></li>
          <li><a href="{P}terms-of-service.html">Terms of service</a></li>
          <li><a href="{P}login.html">Login</a></li>
        </ul>
      </div>
      <p class="copy">© <span data-year>2026</span> {esc(D.BRAND)}. All rights reserved.</p>
    </div>
  </footer>"""


DRAWER = """<div class="scrim" id="scrim" hidden></div>
  <aside class="drawer" id="cartDrawer" role="dialog" aria-modal="true" aria-labelledby="cartTitle" inert>
    <div class="drawer-head">
      <h2 id="cartTitle">Your cart</h2>
      <button class="icon-btn" id="cartClose" aria-label="Close cart">
        <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
      </button>
    </div>
    <ul class="cart-list" id="cartList"></ul>
    <p class="cart-empty" id="cartEmpty">Your cart is empty. Pick a course date and add the course to start.</p>
    <div class="drawer-foot" id="cartFoot" hidden>
      <div class="sum"><span>Subtotal</span><strong id="cartSubtotal">₹0</strong></div>
      <a class="btn btn-primary btn-block" id="checkoutLink" href="#">Request enrollment</a>
      <button class="link-btn" id="cartClear" type="button">Empty cart</button>
    </div>
  </aside>
  <p class="sr-only" id="live" aria-live="polite"></p>"""


def write(path, content):
    full = os.path.join(HERE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


def page(path, title, desc, body, active="", scripts=(), base_tag=False):
    depth = path.count("/")
    P = "../" * depth
    canonical = D.SITE_URL + path
    base = f'<base href="{esc(urlparse(D.SITE_URL).path)}">\n  ' if base_tag else ""
    extra = "".join(f'\n  <script src="{P}assets/js/{s}"></script>' for s in scripts)
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  {base}<meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <link rel="canonical" href="{esc(canonical)}">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(desc)}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{esc(canonical)}">
  <link rel="icon" href="{P}assets/img/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{P}assets/css/style.css">
</head>
<body data-root="{P}">
  <a class="skip-link" href="#content">Skip to content</a>

  <header class="site-header">
    <div class="container header-row">
      <a class="brand" href="{P}index.html" aria-label="{esc(D.BRAND)} home">{mark()}<span class="brand-name">{esc(D.BRAND)}</span></a>
      <button class="icon-btn nav-toggle" id="navToggle" aria-expanded="false" aria-controls="mainNav" aria-label="Open menu">
        <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
      </button>
      {nav_html(P, active)}
      <button class="cart-btn" id="cartOpen" aria-haspopup="dialog" aria-controls="cartDrawer">
        {CART_ICON}
        <span><span id="cartCount">0</span> items</span>
        <strong id="cartTotal">{D.CURRENCY}0</strong>
      </button>
    </div>
  </header>

  <main id="content">
{body}
  </main>

  {footer_html(P)}

  {DRAWER}

  <a class="wa" data-whatsapp href="https://wa.me/{esc(D.WHATSAPP)}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">
    {WA_ICON}<span>Message on WhatsApp</span>
  </a>

  <script src="{P}assets/js/config.js"></script>
  <script src="{P}assets/js/site.js"></script>{extra}
</body>
</html>
"""
    write(path, doc)
    if path != "404.html":
        PAGES.append(path)


def band(title, crumbs, flat=True, lead=""):
    """Dark title band. crumbs: list of (label, href or None)."""
    c = ""
    if crumbs:
        parts = []
        for i, (label, href) in enumerate(crumbs):
            if i:
                parts.append('<span aria-hidden="true">/</span>')
            parts.append(f'<a href="{href}">{esc(label)}</a>' if href else f"<span>{esc(label)}</span>")
        c = f'<nav class="crumbs" aria-label="Breadcrumb">{"".join(parts)}</nav>'
    lead_html = f'<p class="band-lead">{esc(lead)}</p>' if lead else ""
    cls = "title-band title-band--flat" if flat else "title-band"
    return f'<section class="{cls}"><div class="container">{c}<h1>{esc(title)}</h1>{lead_html}</div></section>'


def course_card(c, P):
    href = f'{P}courses/{c["slug"]}.html'
    return f"""<li class="card">
          <div class="card-badge" aria-hidden="true">{esc(c["initials"])}</div>
          <h3><a href="{href}">{esc(c["title"])}</a></h3>
          <p class="card-meta">{day_label(c["days"])} live online class</p>
          <p class="card-price">{inr(c["price"])}</p>
          <a class="btn btn-outline" href="{href}" aria-label="View dates for {esc(c["title"])}">View dates</a>
        </li>"""


def courses_in(slug):
    return [c for c in D.COURSES if c["cat"] == slug]


def nav_key_for_cat(slug):
    return "ai" if slug == "ai" else "training"


# ------------------------------------------------------------- course pages
def course_page(c):
    P = "../"
    cat = CAT[c["cat"]]
    key = nav_key_for_cat(c["cat"])
    sku = c["slug"].upper()
    prereq = c.get("prereq", D.DEFAULT_PREREQ)
    includes = c.get("includes", D.DEFAULT_INCLUDES)
    about = c.get("about") or [c["summary"]]
    about_html = "".join(f"<p>{esc(p)}</p>" for p in about)
    callout = f'<p class="callout">{esc(c["callout"])}</p>' if c.get("callout") else ""

    others = [x for x in courses_in(c["cat"]) if x["slug"] != c["slug"]]
    for x in D.COURSES:
        if len(others) >= 4:
            break
        if x["slug"] != c["slug"] and x not in others and x.get("popular"):
            others.append(x)
    for x in D.COURSES:
        if len(others) >= 4:
            break
        if x["slug"] != c["slug"] and x not in others:
            others.append(x)
    related = "".join(course_card(x, P) for x in others[:4])

    crumbs = ([("Home", f"{P}index.html"), (cat["name"], f'{P}categories/{cat["slug"]}.html')] if c["cat"] == "ai"
              else [("Training", f"{P}training.html"), (cat["name"], f'{P}categories/{cat["slug"]}.html')])

    body = f"""    {band(c["title"], crumbs, flat=False)}

    <section class="container product">
      <figure class="product-visual">
        <div class="visual-badge" aria-hidden="true"><span>{esc(c["initials"])}</span></div>
      </figure>

      <div class="product-info">
        <p class="price">{inr(c["price"])}</p>
        <p class="format"><span class="dot" aria-hidden="true"></span>Live virtual (online), {day_label(c["days"])} class</p>
        <p class="lead">{esc(c["summary"])}</p>
        <p class="note">Can't find a date that suits you, or need a private class? <a href="{P}contact.html">Contact us</a> or email <a data-email href="mailto:{esc(D.EMAIL)}">{esc(D.EMAIL)}</a>.</p>

        <div class="buy" id="buy" data-sku="{esc(sku)}" data-title="{esc(c["title"])}" data-price="{c["price"]}" data-days="{c["days"]}">
          <div class="field">
            <label for="tzFilter">Time zone</label>
            <select id="tzFilter"></select>
          </div>
          <div class="field">
            <label for="sessionSelect">Course date</label>
            <select id="sessionSelect" aria-describedby="sessionHint"></select>
          </div>
          <div class="session-summary" id="sessionSummary" hidden>
            <p class="ss-dates" id="ssDates"></p>
            <p class="ss-time" id="ssTime"></p>
            <button type="button" class="link-btn" id="clearSession">Clear date</button>
          </div>
          <p class="hint" id="sessionHint">Choose a date to add this course to your cart.</p>
          <p class="error" id="sessionError" role="alert" hidden>Choose a course date before adding to cart.</p>
          <div class="buy-row">
            <div class="qty" role="group" aria-label="Quantity">
              <button type="button" id="qtyMinus" aria-label="Decrease quantity">−</button>
              <input id="qty" type="number" min="1" max="20" value="1" inputmode="numeric" aria-label="Quantity">
              <button type="button" id="qtyPlus" aria-label="Increase quantity">+</button>
            </div>
            <button type="button" class="btn btn-primary" id="addToCart">Add to cart</button>
          </div>
        </div>

        <dl class="meta">
          <div><dt>SKU</dt><dd>{esc(sku)}</dd></div>
          <div><dt>Category</dt><dd><a href="{P}categories/{cat["slug"]}.html">{esc(cat["name"])}</a></dd></div>
        </dl>
      </div>
    </section>

    <section class="container description" aria-labelledby="descTitle">
      <h2 id="descTitle" class="tab-title">Description</h2>
      <div class="d-row"><h3>About the course</h3><div>{about_html}</div></div>
      <div class="d-row"><h3>Who will benefit</h3>{ul(c["audience"])}</div>
      <div class="d-row"><h3>Topics covered</h3>{ul(c["topics"])}</div>
      <div class="d-row"><h3>Prerequisites</h3>{ul(prereq)}</div>
      <div class="d-row"><h3>What you will learn</h3>{ul(c["outcomes"])}</div>
      <div class="d-row"><h3>What you get</h3><div>{ul(includes)}{callout}</div></div>
      <div class="d-row"><h3>Exams, renewal and credits</h3><div><p>Exam details, renewal terms and continuing education credits depend on the certifying body. Add the current details for this course here before you publish.</p></div></div>
    </section>

    <section class="related" aria-labelledby="relTitle">
      <div class="container">
        <h2 id="relTitle">Related courses</h2>
        <ul class="card-grid">{related}</ul>
      </div>
    </section>"""

    page(f'courses/{c["slug"]}.html',
         f'{c["title"]} – {D.BRAND}',
         c["summary"][:155],
         body, active=key, scripts=("course.js",))


# ------------------------------------------------------------ category pages
def category_page(cat):
    P = "../"
    items = courses_in(cat["slug"])
    cards = "".join(course_card(c, P) for c in items)
    grid = f'<ul class="card-grid">{cards}</ul>' if items else '<p>No courses are listed here yet. <a href="../contact.html">Ask us</a> about upcoming classes.</p>'
    others = "".join(
        f'<li><a href="{c["slug"]}.html">{esc(c["name"])}</a></li>' for c in D.CATEGORIES if c["slug"] != cat["slug"]
    )
    crumbs = [("Home", f"{P}index.html")] if cat["slug"] == "ai" else [("Training", f"{P}training.html")]
    crumbs.append((cat["name"], None))
    body = f"""    {band(cat["name"], crumbs, lead=cat["blurb"])}
    <section class="container section">
      {grid}
    </section>
    <section class="container section section--tight">
      <h2 class="h2">Other topics</h2>
      <ul class="pill-list">{others}</ul>
    </section>"""
    page(f'categories/{cat["slug"]}.html', f'{cat["name"]} – {D.BRAND}', cat["blurb"], body,
         active=nav_key_for_cat(cat["slug"]))


# -------------------------------------------------------------- training page
def training_page():
    P = ""
    blocks = ""
    for cat in D.CATEGORIES:
        items = courses_in(cat["slug"])
        if not items:
            continue
        cards = "".join(course_card(c, P) for c in items)
        blocks += f"""
      <section class="cat-block" aria-labelledby="c-{cat["slug"]}" id="{cat["slug"]}">
        <div class="cat-head">
          <h2 id="c-{cat["slug"]}"><a href="categories/{cat["slug"]}.html">{esc(cat["name"])}</a></h2>
          <p>{esc(cat["blurb"])}</p>
        </div>
        <ul class="card-grid">{cards}</ul>
      </section>"""
    body = f"""    {band("Training", [("Home", "index.html"), ("Training", None)], lead="Live online classes in Scrum, SAFe, Kanban, DevOps, AI and more.")}
    <div class="container section">
      <div class="filter">
        <label for="courseFilter">Search courses</label>
        <input id="courseFilter" type="search" placeholder="Try &quot;Scrum&quot; or &quot;product owner&quot;" autocomplete="off">
        <p class="hint" id="filterStatus" role="status"></p>
      </div>
      {blocks}
    </div>"""
    page("training.html", f"Training – {D.BRAND}",
         "Browse live online Agile training: Scrum, SAFe, Kanban, DevOps, ICAgile, AI and more.", body, active="training")


# ------------------------------------------------------------------ home page
def home_page():
    feat = next(c for c in D.COURSES if c.get("featured"))
    popular = [c for c in D.COURSES if c.get("popular")][:4]
    topics = "".join(
        f'<li><a href="categories/{c["slug"]}.html"><strong>{esc(c["name"])}</strong>'
        f'<span>{len(courses_in(c["slug"]))} course{"s" if len(courses_in(c["slug"])) != 1 else ""}</span></a></li>'
        for c in D.CATEGORIES
    )
    cards = "".join(course_card(c, "") for c in popular)
    body = f"""    <section class="hero">
      <div class="container hero-grid">
        <div>
          <h1>Live online Agile training for teams and leaders</h1>
          <p class="lead">Classes for Scrum Masters, product owners, engineers and executives, with hands-on exercises and exam preparation where a certification is involved.</p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="training.html">Browse courses</a>
            <a class="btn btn-outline" href="contact.html">Ask for a private class</a>
          </div>
        </div>
        <aside class="next-class" aria-labelledby="ncTitle">
          <h2 id="ncTitle">Next class dates</h2>
          <p class="nc-course"><a href="courses/{feat["slug"]}.html">{esc(feat["title"])}</a></p>
          <p class="nc-price">{inr(feat["price"])}, {day_label(feat["days"])} live online class</p>
          <ul class="nc-list" id="nextList" data-days="{feat["days"]}" data-url="courses/{feat["slug"]}.html"></ul>
          <a class="btn btn-primary btn-block" href="courses/{feat["slug"]}.html">See all dates</a>
        </aside>
      </div>
    </section>

    <section class="container section">
      <h2 class="h2">Browse by topic</h2>
      <ul class="topic-grid">{topics}</ul>
    </section>

    <section class="section section--wash">
      <div class="container">
        <h2 class="h2">Popular courses</h2>
        <ul class="card-grid">{cards}</ul>
        <p class="more"><a href="training.html">See all courses</a></p>
      </div>
    </section>

    <section class="container section">
      <h2 class="h2">How a class works</h2>
      <ol class="steps">
        <li><h3>Choose a course and date</h3><p>Pick the time zone that suits you, choose a date and add the course to your cart.</p></li>
        <li><h3>Join the live class</h3><p>Take part in a live online session with group activities, discussion and time for questions.</p></li>
        <li><h3>Finish with your credential</h3><p>Where the course leads to an exam, you get the preparation and eligibility to sit it. Other courses end with a certificate of attendance.</p></li>
      </ol>
    </section>

    <section class="container section section--tight">
      <div class="split">
        <div class="panel">
          <h2>Consulting</h2>
          <p>Assessments, roadmaps and hands-on help setting up teams that plan and deliver together.</p>
          <a class="btn btn-outline" href="consulting.html">See consulting services</a>
        </div>
        <div class="panel">
          <h2>Coaching</h2>
          <p>Ongoing support for teams, Scrum Masters, product owners and leaders as they change how they work.</p>
          <a class="btn btn-outline" href="coaching.html">See coaching options</a>
        </div>
      </div>
    </section>

    <section class="cta-band">
      <div class="container cta-row">
        <div>
          <h2>Need a private class for your team?</h2>
          <p>We can run any course for your organization on dates that suit you.</p>
        </div>
        <a class="btn btn-light" href="contact.html">Contact us</a>
      </div>
    </section>"""
    page("index.html", f"{D.BRAND} – Live online Agile training, consulting and coaching",
         "Live online Agile training in Scrum, SAFe, Kanban, DevOps and AI, plus consulting and coaching for teams and leaders.",
         body, active="home")


# ------------------------------------------------------- service-style pages
def rows(items):
    return "".join(f'<div class="d-row"><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for t, d in items)


def consulting_page():
    body = f"""    {band("Consulting", [("Home", "index.html"), ("Consulting", None)], lead="Practical help for organizations changing how they plan, deliver and learn.")}
    <section class="container section">
      <p class="lead">Every engagement starts with your goals and your current way of working. We recommend the smallest set of changes that will make a real difference, and help your people make them.</p>
      <div class="rows">{rows(D.CONSULTING)}</div>
    </section>
    <section class="cta-band">
      <div class="container cta-row">
        <div><h2>Talk about your situation</h2><p>Tell us what you are trying to change and we will suggest a first step.</p></div>
        <a class="btn btn-light" href="contact.html">Contact us</a>
      </div>
    </section>"""
    page("consulting.html", f"Consulting – {D.BRAND}",
         "Agile assessments, transformation roadmaps and support launching teams that deliver together.", body, active="consulting")


def coaching_page():
    body = f"""    {band("Coaching", [("Home", "index.html"), ("Coaching", None)], lead="Support that continues after the class ends.")}
    <section class="container section">
      <p class="lead">Coaching helps people apply what they learned to their own work, with someone alongside who has seen the same problems in other teams.</p>
      <div class="rows">{rows(D.COACHING)}</div>
    </section>
    <section class="cta-band">
      <div class="container cta-row">
        <div><h2>Find the right kind of coaching</h2><p>Describe who you want to support and we will suggest a format.</p></div>
        <a class="btn btn-light" href="contact.html">Contact us</a>
      </div>
    </section>"""
    page("coaching.html", f"Coaching – {D.BRAND}",
         "Team, role-based and leadership coaching for Agile teams and organizations.", body, active="coaching")


def tools_page():
    cards = "".join(
        f"""<li class="card" id="tool-{i + 1}">
          <div class="card-badge" aria-hidden="true">{esc(t[0][:2].upper())}</div>
          <h3>{esc(t[0])}</h3>
          <p>{esc(t[1])}</p>
          <a class="btn btn-outline" href="{esc(t[2])}" target="_blank" rel="noopener">Visit website</a>
        </li>"""
        for i, t in enumerate(D.TOOLS)
    )
    body = f"""    {band("Tools", [("Home", "index.html"), ("Tools", None)], lead="Software we use and recommend to the teams we work with.")}
    <section class="container section">
      <ul class="card-grid card-grid--2">{cards}</ul>
    </section>"""
    page("tools.html", f"Tools – {D.BRAND}", "Software we use and recommend for Agile teams.", body, active="tools")


def team_page():
    cards = "".join(
        f"""<li class="card person">
          <div class="avatar" aria-hidden="true">{esc(p["initials"])}</div>
          <h3>{esc(p["name"])}</h3>
          <p class="card-meta">{esc(p["role"])}</p>
          <p>{esc(p["bio"])}</p>
        </li>"""
        for p in D.TEAM
    )
    body = f"""    {band("Team", [("Home", "index.html"), ("Team", None)], lead="The people who teach, coach and support you.")}
    <section class="container section">
      <ul class="card-grid">{cards}</ul>
    </section>"""
    page("team.html", f"Team – {D.BRAND}", "Meet the trainers, coaches and consultants.", body, active="team")


def contact_page():
    body = f"""    {band("Contact", [("Home", "index.html"), ("Contact", None)], lead="Ask about a course, a private class, consulting or coaching.")}
    <section class="container section contact-grid">
      <form class="form" id="contactForm">
        <div class="field"><label for="cf-name">Your name</label><input id="cf-name" name="name" required autocomplete="name"></div>
        <div class="field"><label for="cf-email">Email</label><input id="cf-email" name="email" type="email" required autocomplete="email"></div>
        <div class="field"><label for="cf-phone">Phone (optional)</label><input id="cf-phone" name="phone" type="tel" autocomplete="tel"></div>
        <div class="field"><label for="cf-topic">What is this about?</label>
          <select id="cf-topic" name="topic">
            <option>Training</option><option>Private class for my team</option><option>Consulting</option><option>Coaching</option><option>Something else</option>
          </select></div>
        <div class="field"><label for="cf-msg">Message</label><textarea id="cf-msg" name="message" rows="6" required></textarea></div>
        <button class="btn btn-primary" type="submit">Send message</button>
        <p class="form-note" id="formNote" role="status"></p>
      </form>
      <aside class="contact-side">
        <h2>Other ways to reach us</h2>
        <dl class="meta">
          <div><dt>Email</dt><dd><a data-email href="mailto:{esc(D.EMAIL)}">{esc(D.EMAIL)}</a></dd></div>
          <div><dt>WhatsApp</dt><dd><a data-whatsapp href="https://wa.me/{esc(D.WHATSAPP)}" target="_blank" rel="noopener">Start a chat</a></dd></div>
        </dl>
        <p class="note">Add your office hours and reply time here.</p>
      </aside>
    </section>"""
    page("contact.html", f"Contact – {D.BRAND}", "Contact us about training, private classes, consulting or coaching.",
         body, active="contact")


def login_page():
    body = f"""    {band("Login", [("Home", "index.html"), ("Login", None)])}
    <section class="container section">
      <div class="panel panel--narrow">
        <h2>Access your courses</h2>
        <p>Course materials, certificates and exam links are on our learning portal. Sign in there with the email you used to enroll.</p>
        <a class="btn btn-primary" id="loginBtn" href="#">Go to the learning portal</a>
        <p class="note" id="loginNote" hidden>The learning portal link is not set up yet. Add your portal address as <code>loginUrl</code> in <code>assets/js/config.js</code>.</p>
      </div>
    </section>"""
    page("login.html", f"Login – {D.BRAND}", "Sign in to the learning portal.", body, active="login")


def legal_page(path, title, sections):
    inner = "".join(f'<div class="d-row"><h3>{esc(h)}</h3><p>{esc(t)}</p></div>' for h, t in sections)
    body = f"""    {band(title, [("Home", "index.html"), (title, None)])}
    <section class="container section">
      <p class="note">This is placeholder text. Replace it with policies reviewed by a qualified professional before you publish.</p>
      <div class="rows">{inner}</div>
    </section>"""
    page(path, f"{title} – {D.BRAND}", f"{title} for {D.BRAND}.", body)


def not_found():
    body = f"""    <section class="container section notfound">
      <h1>Page not found</h1>
      <p class="lead">The page you asked for does not exist or has moved.</p>
      <p><a class="btn btn-primary" href="index.html">Go to the home page</a> <a class="btn btn-outline" href="training.html">Browse training</a></p>
    </section>"""
    page("404.html", f"Page not found – {D.BRAND}", "Page not found.", body, base_tag=True)


# ---------------------------------------------------------------------- main
def sitemap():
    urls = "".join(f"  <url><loc>{esc(D.SITE_URL + p)}</loc></url>\n" for p in sorted(PAGES))
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {D.SITE_URL}sitemap.xml\n")


def main():
    home_page()
    training_page()
    for cat in D.CATEGORIES:
        category_page(cat)
    for c in D.COURSES:
        course_page(c)
    consulting_page()
    coaching_page()
    tools_page()
    team_page()
    contact_page()
    login_page()
    legal_page("privacy-policy.html", "Privacy policy", [
        ("What we collect", "Describe the information you collect, for example names and emails from enquiries and enrollments."),
        ("How we use it", "Describe how you use that information and who you share it with."),
        ("Your choices", "Describe how people can ask you to correct or delete their information."),
    ])
    legal_page("terms-of-service.html", "Terms of service", [
        ("Enrollment", "Describe how enrollment works, payment terms and what is included in the fee."),
        ("Cancellations and transfers", "Describe your rules for cancelling or moving to another date."),
        ("Certificates and exams", "Describe eligibility for certificates and exams, and who sets the exam terms."),
    ])
    not_found()
    sitemap()
    print(f"Built {len(PAGES) + 1} pages in {HERE}")


if __name__ == "__main__":
    main()
