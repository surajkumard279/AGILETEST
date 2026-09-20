# Agile training website (multi-page, GitHub Pages ready)

A complete static site. Every menu item opens a real internal page.
Plain HTML, CSS and JavaScript. No framework, no server, no build step needed to publish.

## Pages

| Menu item | Page |
| --- | --- |
| Logo | `index.html` (home) |
| AI Courses | `categories/ai.html` |
| Consulting | `consulting.html` |
| Training (drop-down) | `training.html` and one page per topic in `categories/` |
| Coaching | `coaching.html` |
| Tools (drop-down) | `tools.html` |
| Team | `team.html` |
| Contact | `contact.html` |
| Login | `login.html` |
| Each course card | `courses/<course>.html` |
| Footer | `privacy-policy.html`, `terms-of-service.html` |

Also included: `404.html`, `sitemap.xml`, `robots.txt`.
The cart works on every page and is remembered in the visitor's browser.

## Publish on GitHub Pages

1. Create a repository on GitHub (for example `agile-site`).
2. Upload everything in this folder to the repository root, so `index.html` is at the top level. Keep the hidden `.nojekyll` file.
3. Go to **Settings > Pages**. Under **Build and deployment**, choose **Deploy from a branch**, branch `main`, folder `/ (root)`, then Save.
4. After a minute or two the site is live at `https://<username>.github.io/<repo>/`.

All links are relative, so the site works at a project address like the one above, on a custom domain, and when you open `index.html` straight from your computer.

## Change the content

Two ways, pick one:

**A. Edit `data.py`, then rebuild (recommended).**
`data.py` holds the brand name, all categories, all courses (title, price, days, description, topics), the team, and the consulting and coaching lists.
After editing, run this in the folder (Python 3, nothing to install):

    python build.py

That rewrites every `.html` page so menus, cards, related courses, breadcrumbs and the sitemap all stay in sync. To add a course, copy one block in `COURSES` and change it. To add a topic, add an entry to `CATEGORIES`.

**B. Edit the `.html` files directly.**
Fine for small text fixes. Note that running `build.py` again overwrites those edits.

## Other settings

| What | Where |
| --- | --- |
| Email, WhatsApp number, payment link, learning-portal link, contact-form endpoint, class schedule | `assets/js/config.js` |
| Brand name, email, WhatsApp (used in the generated pages) | top of `data.py` |
| Public web address (canonical links, sitemap, 404 page) | `SITE_URL` in `data.py`, then rebuild |
| Colors, fonts, spacing | `:root` block at the top of `assets/css/style.css` |

Set `SITE_URL` to your real address, for example `https://yourname.github.io/agile-site/`, and run `python build.py`.

## What GitHub Pages cannot do

GitHub Pages serves static files only, so:

- **Payments:** the cart's "Request enrollment" button emails you the order. To take payments, paste a Razorpay, Stripe or PayPal link into `checkoutUrl` in `config.js`.
- **Login:** the Login page sends visitors to your learning portal. Put its address in `loginUrl` in `config.js`. The site itself has no accounts.
- **Contact form:** it opens the visitor's email app by default. For a form that submits without email, create a free endpoint (for example on Formspree) and paste it into `formEndpoint`.
- **Class dates:** upcoming sessions are generated from the weekly patterns in `config.js`. They are display dates only. Replace them with `customSessions` when you have a real schedule.

## Before you publish

- The prices, course descriptions, team entries and legal pages are placeholders. Replace them.
- Replace the brand name, logo mark (`assets/img/favicon.svg` and the logo SVG in `build.py`), email and WhatsApp number.
- Certification and framework names (SAFe®, Scrum Alliance, ICAgile and so on) belong to their owners. Use them only if you are authorized to, and follow their branding rules.
