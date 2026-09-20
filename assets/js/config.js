/* ==========================================================
   EDIT THIS FILE for browser-side settings:
   contact details, payment link, login link, schedule.
   Course text and prices live in data.py (run: python build.py).
   ========================================================== */
window.SITE = {
  brand: "Your Brand",
  email: "training@yourdomain.com",
  whatsappNumber: "910000000000",   // country code + number, digits only

  currency: "₹",
  locale: "en-IN",

  // Optional links. Leave "" until you have them.
  checkoutUrl: "",   // payment link (Razorpay, Stripe, PayPal...). "" = send an enrollment email instead
  loginUrl: "",      // your learning portal / LMS login page
  formEndpoint: "",  // e.g. a Formspree URL. "" = the contact form opens the visitor's email app

  /* ---------- SCHEDULE ----------
     The page builds upcoming sessions from these weekly patterns so dates
     never go stale.  dow: 0=Sun 1=Mon 2=Tue 3=Wed 4=Thu 5=Fri 6=Sat
  */
  weeksAhead: 6,
  patterns: [
    { dow: 4, timezone: "Greenwich Mean Time" },
    { dow: 4, timezone: "US Central Time", popular: true },
    { dow: 6, timezone: "Central European Time", popular: true },
    { dow: 6, timezone: "US Eastern Time" },
    { dow: 1, timezone: "Central European Time" },
    { dow: 1, timezone: "US Eastern Time" }
  ],

  /* Or list exact dates yourself (replaces the automatic schedule):
     customSessions: [
       { start: "2026-10-08", timezone: "US Central Time", hours: "9 AM – 5 PM", popular: true }
     ]
     The number of days for each course comes from the course page itself. */
  customSessions: []
};
