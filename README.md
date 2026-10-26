# Tinny Lianna's Daycare

A responsive, single-page website for Tinny Lianna's Daycare in Bonaero Park, Kempton Park. Its tagline is “Nurturing Little Minds, Building Bright Futures.” Visit the live website at [tinny-lianna.github.io](https://tinny-lianna.github.io/).

## Features

- Daycare information, opening hours, and location
- Weekend Visit Programme details and downloadable form
- Parent review submission form
- Moderated testimonials section for approved parent reviews
- Moderated parent reviews and overall rating
- Free honeypot protection on online forms
- Registration information and an online Intent form
- Facebook and TikTok search links for Tinny Lianna's Daycare
- Gallery sections for meals, facilities, and school information
- Responsive layout and image-preview modal
- Launch-ready assets published from the `live-assets` branch

## Run locally

Run `python -m http.server 8000` from the website folder, then open `http://localhost:8000`. Keep the `css`, `js`, `forms`, and `assets` folders alongside `index.html`.

## Images

The website includes the logo, banner, daily programme, facility photos, and meal photos. Event gallery photos are not currently included.

## Intent form

The downloadable form in `forms/` and online form let a family express interest and share information so the daycare can consider availability and follow up about next steps. Neither is final registration, and neither guarantees or reserves a place.

Online submissions use Formspree's Vanilla JavaScript Ajax integration and a typed parent/guardian signature. The form displays a confirmation after a successful submission, and families can download the original Intent form if they prefer to complete it separately. Configure the notification recipient in the Formspree account. The public form ID is wired in `index.html`; it is not an API key or password. Do not add account credentials to the site. Keep submissions limited to the information needed to respond to an enquiry.

## Parent reviews

The Reviews section accepts a parent or guardian's name, a one-to-five star rating, written feedback, and permission to review the submission for possible publication. Formspree's free hosted form collects submissions and sends them through its configured notification process, but the public site does not access private submissions automatically. Add approved reviews to `reviews.json`; include a `date` field when the review date should be shown. The site calculates the overall average from that public feed. Do not place account credentials in website files or client-side JavaScript.

## Form protection

The online Reviews and Intent forms use Formspree's free spam filtering plus hidden honeypot fields. Genuine visitors leave the trap fields empty; simple automated submissions that fill them can be rejected by Formspree. The Weekend Visit option is a downloadable PDF and WhatsApp enquiry link, not an online HTML form. These free measures reduce form spam but are not DDoS mitigation; a true DDoS attack requires provider-level protection.
