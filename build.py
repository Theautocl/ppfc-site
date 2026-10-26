#!/usr/bin/env python3
"""Builds the static Peninsula Professional Feral Control site into ./dist.
Run: python3 build.py   (from the build/ folder)
Edit config.json (domain/email), pages.json (ranking pages), faq.json, blog.json."""
import json, re, pathlib, datetime, html, shutil
from graphics import SCOPE, ICONS, MAP, MAP_CSS, ABOUT, SECTORS, OG_SVG

HERE = pathlib.Path(__file__).parent
DIST = HERE / "dist"
cfg = json.loads((HERE / "config.json").read_text())
pages = json.loads((HERE / "pages.json").read_text())
faqs = json.loads((HERE / "faq.json").read_text())
posts = json.loads((HERE / "blog.json").read_text())
base = (HERE / "base.html").read_text()

DOMAIN = cfg["domain"].rstrip("/")
EMAIL, PHONE, ABN, TOWNS = cfg["email"], cfg["phone"], cfg["abn"], cfg["towns"]
NAME = "Peninsula Pest Shooting"
base = base.replace("{{EMAIL}}", EMAIL).replace("{{PHONE}}", PHONE).replace("{{ABN}}", ABN)

# ---- template surgery: graphics, about section, icons
base = base.replace("</style>", MAP_CSS + "</style>", 1)
HERO_PHOTO = '<img class="hero-photo" src="/img/hero.jpg" alt="Feral control on a Mornington Peninsula property at dusk" onerror="this.remove()">'
base = base.replace('    </div>\n  </div>\n</section>\n\n<section class="band" id="services">',
                    '    </div>\n    ' + HERO_PHOTO + '\n  </div>\n</section>\n\n<section class="band" id="services">', 1)
for sp, svg in ICONS.items():
    base = base.replace(f'<div class="sp"><h3>{sp}</h3>', f'<div class="sp"><span class="ico">{svg}</span><h3>{sp}</h3>', 1)
base = base.replace('<ul class="towns">', MAP + '\n      <ul class="towns" style="margin-top:20px">', 1)
base = base.replace('<section class="band" style="background:var(--surface)" id="coverage">', SECTORS + '<section class="band" style="background:var(--surface)" id="coverage">', 1)
base = base.replace('<section class="band price-band" id="pricing">', ABOUT + '<section class="band price-band" id="pricing">', 1)
base = base.replace('<div class="cover">', '<div class="cover" style="grid-template-columns:1fr">', 1)

def skeleton(title, desc, canonical, body, schema):
    return f"""<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="website">
<meta property="og:image" content="{DOMAIN}/og.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1f3b2a">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/img/favicon-180.png">
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
{body}
</body>
</html>
"""

business = {
    "@type": "PestControl", "@id": DOMAIN + "/#business", "name": NAME, "url": DOMAIN + "/",
    "telephone": "+61" + PHONE.replace(" ", "")[1:], "email": EMAIL, "image": DOMAIN + "/og.png",
    "description": "Licensed, insured professional ground shooting for foxes, rabbits, deer, feral cats and rats across the Mornington Peninsula, Victoria.",
    "areaServed": [{"@type": "Place", "name": t + ", Victoria"} for t in TOWNS],
    "address": {"@type": "PostalAddress", "addressRegion": "VIC", "addressLocality": "Mornington Peninsula", "addressCountry": "AU"},
    "priceRange": "$220-$400", "openingHours": "Mo-Su 08:00-19:00",
    "knowsAbout": ["fox control", "rabbit control", "deer control", "feral cat control", "rat control", "pest bird control", "thermal shooting"],
    "geo": {"@type": "GeoCoordinates", "latitude": -38.2174, "longitude": 145.0382},
    "sameAs": ["https://www.facebook.com/PeninsulaPestShooting", "https://www.youtube.com/channel/UCI6NGhFcsOvsG0OXY2zj_9A"],
}
def crumbs(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}
def crumbs_html(items):
    return '<nav class="crumbs wrap" aria-label="Breadcrumb">' + " › ".join(
        f'<a href="{u}">{n}</a>' if i < len(items) - 1 else f'<span>{n}</span>' for i, (n, u) in enumerate(items)) + "</nav>"
def faq_html(items):
    out = '<section class="band" id="faq"><div class="wrap"><p class="eyebrow">Common questions</p><h2>Before you book</h2><div class="faq">'
    for q, a in items:
        out += f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>"
    return out + "</div></div></section>"
def faq_schema(items):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

body_home = base.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")
body_home = re.sub(r"<title>.*?</title>\n", "", body_home, count=1)
m = re.search(r"(<link[^>]+>\n<style>.*?</style>)\n(.*)", body_home, re.S)
head_assets, body_rest = m.group(1), m.group(2)
# brand is already a linked logo image in base.html — no wrapping needed

def page_body(h1, lede, eyebrow, local_html, crumb_items):
    b = body_rest
    b = re.sub(r'<h1 style="margin-top:12px">.*?</h1>', f'<h1 style="margin-top:12px">{h1}</h1>', b, count=1, flags=re.S)
    b = re.sub(r'(<section class="hero">.*?<p class="lede">).*?(</p>)', lambda mm: mm.group(1) + lede + mm.group(2), b, count=1, flags=re.S)
    b = b.replace('<p class="eyebrow">Licensed · Insured · Thermal-equipped</p>', f'<p class="eyebrow">{eyebrow}</p>', 1)
    b = b.replace('<section class="band" id="services">', local_html + '\n<section class="band" id="services">', 1)
    b = b.replace('</header>', '</header>' + crumbs_html(crumb_items), 1)
    return b

DIST.mkdir(exist_ok=True)

# ---- copy static assets (photos etc.) from assets/ into dist/
ASSETS = HERE / "assets"
if ASSETS.exists():
    for src in ASSETS.rglob("*"):
        if src.is_file():
            dst = DIST / src.relative_to(ASSETS)
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

# ---- proof gallery (home page only): real scope captures
PROOF_ITEMS = [
    ("proof-thermal-rabbit-48m.jpg", "Thermal — rabbit at 48m"),
    ("proof-nightvision-57m.jpg", "Night vision — 57m"),
    ("proof-rabbits-pair-92m.jpg", "Pair at range — 92m"),
    ("proof-rabbit-foliage-25m.jpg", "In cover — 25m"),
    ("proof-thermal-orchard.jpg", "Thermal scan — orchard edge"),
    ("proof-rabbit-scope.jpg", "Rabbit in the reticle"),
    ("proof-rabbit-reticle-36m.jpg", "Rabbit ranged at 36m on the day scope"),
    ("proof-rat-nightvision.jpg", "Rat on night vision"),
    ("proof-three-rabbits-nightvision.jpg", "Three rabbits in one thermal scan at 36m"),
]
GALLERY = ('<style>.proof-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));'
           'gap:14px;margin-top:22px}.proof-grid img{width:100%;height:200px;object-fit:cover;display:block;'
           'border-radius:12px;border:1px solid var(--line);background:#0d1a12}'
           '.proof-videos{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:14px;margin-top:22px}'
           '.proof-videos video{width:100%;height:auto;display:block;'
           'border-radius:12px;border:1px solid var(--line);background:#0d1a12}</style>'
           '<section class="band" style="background:var(--surface)" id="proof"><div class="wrap">'
           '<p class="eyebrow">Real jobs, real results</p>'
           '<h2>What a night on the Peninsula looks like</h2>'
           '<p style="max-width:62ch;margin-top:10px;color:var(--muted)">Every target identified and '
           'taken with a clear backstop, day or night. These are our own thermal and night-vision '
           'captures from local properties.</p>'
           '<div class="proof-videos">'
           '<video src="/video/night-stalk.mp4" poster="/video/night-stalk-poster.jpg" autoplay muted loop playsinline preload="metadata"></video>'
           '<video src="/video/night-stalk-2.mp4" poster="/video/night-stalk-2-poster.jpg" autoplay muted loop playsinline preload="metadata"></video>'
           '<video src="/video/night-stalk-3.mp4" poster="/video/night-stalk-3-poster.jpg" autoplay muted loop playsinline preload="metadata"></video>'
           '<video src="/video/field-clip-4.mp4" poster="/video/field-clip-4-poster.jpg" autoplay muted loop playsinline preload="metadata"></video>'
           '</div>'
           '<div class="proof-grid">'
           + "".join(f'<img src="/img/{f}" loading="lazy" alt="{html.escape(c)}">' for f, c in PROOF_ITEMS)
           + '</div>'
           '<p style="margin-top:24px"><a class="btn btn-ghost" href="https://www.youtube.com/channel/UCI6NGhFcsOvsG0OXY2zj_9A" target="_blank" rel="noopener">Watch more on YouTube</a></p>'
           '</div></section>')

VIDEO_CLIPS = [
    ("night-stalk.mp4", "night-stalk-poster.jpg", "Thermal pest control on the Mornington Peninsula", "Thermal night shooting of feral animals on a Mornington Peninsula property. Every target identified with a clear backstop, bait-free."),
    ("night-stalk-2.mp4", "night-stalk-2-poster.jpg", "Night vision rabbit control — Mornington Peninsula", "Night vision rabbit control on a Peninsula block. Bait-free and safe around stock and dogs."),
    ("night-stalk-3.mp4", "night-stalk-3-poster.jpg", "Bait-free feral control — Mornington Peninsula", "Professional feral and vermin shooting across the Mornington Peninsula, Victoria."),
    ("field-clip-4.mp4", "field-clip-4-poster.jpg", "Rabbit ranged at 36m — day scope", "Daytime rabbit control on a Mornington Peninsula property, ranged and taken at 36 metres."),
]
VIDEO_OBJECTS = [{"@type": "VideoObject", "name": n, "description": d,
    "thumbnailUrl": DOMAIN + "/video/" + poster, "contentUrl": DOMAIN + "/video/" + mp4,
    "uploadDate": "2026-10-25"} for mp4, poster, n, d in VIDEO_CLIPS]

urls = []
graph_base = [business, {"@type": "WebSite", "url": DOMAIN + "/", "name": NAME}]

# ---- home
(DIST / "index.html").write_text(skeleton(
    "Pest & Feral Shooting Mornington Peninsula | Fox, Rabbit & Deer Shooter",
    "Licensed, insured pest and feral shooting across the Mornington Peninsula — foxes, rabbits, deer, feral cats, rats and introduced pest birds. A professional shooter, not a termite or spray company. $50 first-night callout. Text 0466 659 997.",
    DOMAIN + "/", head_assets + "\n</head>\n<body>\n" + body_rest.replace('<section class="band price-band" id="pricing">', GALLERY + faq_html(faqs["hobby-farm-pest-control-mornington-peninsula"][:2] + faqs["fox-control-mornington-peninsula"][1:3] + faqs["acreage-pest-control-mornington-peninsula"][:1]) + '<section class="band price-band" id="pricing">', 1),
    {"@context": "https://schema.org", "@graph": graph_base + [faq_schema(faqs["hobby-farm-pest-control-mornington-peninsula"][:2] + faqs["fox-control-mornington-peninsula"][1:3] + faqs["acreage-pest-control-mornington-peninsula"][:1])] + VIDEO_OBJECTS}))
urls.append("/")

# ---- ranking pages
nav_links = []
for p in pages:
    slug = p["slug"]; url = f"{DOMAIN}/{slug}/"
    local = f"""<section class="band" style="background:var(--surface)">
  <div class="wrap"><p class="eyebrow">{p['eyebrow']}</p><h2>{p['h2']}</h2>
    <div style="max-width:68ch;margin-top:18px;display:grid;gap:14px;font-size:17px">{''.join(f'<p>{para}</p>' for para in p['paras'])}</div>
    <p style="margin-top:22px"><a class="btn btn-amber" href="#quote">Book your first night</a></p></div></section>"""
    pf = faqs.get(slug)
    if pf: local += faq_html(pf)
    cr = [("Home", DOMAIN + "/"), (p["group"], DOMAIN + "/#services"), (p["nav"], url)]
    graph = graph_base + [crumbs(cr), {
        "@type": "Service", "name": p["title"].split("|")[0].strip(), "url": url,
        "provider": {"@id": DOMAIN + "/#business"}, "areaServed": p.get("area", "Mornington Peninsula, Victoria"),
        "serviceType": p["service"], "description": p["desc"],
        "offers": {"@type": "Offer", "price": "400", "priceCurrency": "AUD", "description": "Per night session; $50 first-night callout"}}]
    if pf: graph.append(faq_schema(pf))
    out = DIST / slug; out.mkdir(exist_ok=True)
    (out / "index.html").write_text(skeleton(p["title"], p["desc"], url, head_assets + "\n</head>\n<body>\n" + page_body(p["h1"], p["lede"], p["eyebrow"], local, cr), {"@context": "https://schema.org", "@graph": graph}))
    urls.append(f"/{slug}/"); nav_links.append((p["group"], p["nav"], f"/{slug}/"))

# ---- blog
def simple_page(title, desc, path, inner, crumb_items, extra_graph=None):
    b = body_rest
    b = re.sub(r'<section class="hero">.*?</section>', "", b, count=1, flags=re.S)
    b = re.sub(r'<section class="band" id="services">.*?(<section class="band" style="background:var\(--surface\)" id="quote">)', inner + r"\1", b, count=1, flags=re.S)
    b = b.replace('</header>', '</header>' + crumbs_html(crumb_items), 1)
    url = f"{DOMAIN}{path}"
    out = DIST / path.strip("/"); out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(skeleton(title, desc, url, head_assets + "\n</head>\n<body>\n" + b, {"@context": "https://schema.org", "@graph": graph_base + [crumbs(crumb_items)] + (extra_graph or [])}))
    urls.append(path)

post_cards = ""
for po in posts:
    path = f"/blog/{po['slug']}/"
    inner = f'<section class="band"><div class="wrap"><p class="eyebrow">{po["date"]}</p><h2>{html.escape(po["title"])}</h2><div class="post">' + "".join(f"<p>{html.escape(x)}</p>" for x in po["paras"]) + f'<p><a class="btn btn-amber" href="#quote">Book your first night</a></p></div></div></section>'
    cr = [("Home", DOMAIN + "/"), ("Blog", DOMAIN + "/blog/"), (po["title"][:40] + "…", DOMAIN + path)]
    simple_page(po["title"] + " | " + NAME, po["desc"], path, inner, cr, [{
        "@type": "Article", "headline": po["title"], "datePublished": po["date"], "dateModified": po["date"],
        "author": {"@type": "Organization", "name": NAME}, "publisher": {"@id": DOMAIN + "/#business"}, "mainEntityOfPage": DOMAIN + path, "description": po["desc"]}])
    post_cards += f'<a href="{path}"><h3>{html.escape(po["title"])}</h3><p>{html.escape(po["desc"])}</p></a>'
simple_page("Feral control notes from the Mornington Peninsula | " + NAME, "Practical notes on fox, rabbit, deer and feral cat control for Peninsula landholders.", "/blog/",
            f'<section class="band"><div class="wrap"><p class="eyebrow">Notes from the field</p><h2>Feral control on the Peninsula</h2><div class="post-list">{post_cards}</div></div></section>',
            [("Home", DOMAIN + "/"), ("Blog", DOMAIN + "/blog/")])

# ---- privacy
simple_page("Privacy | " + NAME, "How Peninsula Professional Feral Control handles the details you give us.", "/privacy/",
            f'<section class="band"><div class="wrap"><p class="eyebrow">Privacy</p><h2>Your details</h2><div class="post"><p>We collect only what you give us to book a job: your name, phone number, property address and what you want controlled. We use it to contact you, plan the visit and keep a record of the work done. We do not sell or share it, except where the law requires us to notify police of firearm use at a location.</p><p>Landholder authority forms and job records are kept for seven years as required for firearms and insurance purposes. To see or delete what we hold about you, text {PHONE} or email {EMAIL}.</p><p>This site does not use advertising cookies. Basic server logs are kept for security.</p></div></div></section>',
            [("Home", DOMAIN + "/"), ("Privacy", DOMAIN + "/privacy/")])

# ---- about
about_paras = [
 "Peninsula Pest Shooting is owner-operated. You deal with Josh — the person who assesses your property, does the work and turns up again next time. No call centre, no subcontractors, no franchise.",
 "I've lived on the Mornington Peninsula for more than 25 years, so this isn't a patch I drive out to — it's home. I've been shooting for around 18 years and controlling pests on and off on other people's properties for about 9 of them. That means I know the country, the seasons and the problems particular to blocks around here: foxes on the lambing paddocks, rabbits ring-barking the vines, deer coming out of the parks and reserves.",
 "What drives it is conservation as much as anything. Foxes, rabbits, feral cats and introduced birds do real damage to native wildlife and habitat on the Peninsula, and doing the job properly — target-specific, bait-free, with nothing left in the paddock to poison an owl or a working dog — protects the native animals as well as your stock and crops. That's why I shoot rather than bait, and why I won't touch protected native species without the right permit.",
 "I hold a Victorian firearms licence, a game licence for deer, public liability insurance, and a Victoria Police Public Place Permit for working on blocks close to houses and roads. Every job is done humanely, within the law, and with your neighbours and your animals in mind.",
 "If foxes, rabbits, deer, feral cats, rats or pest birds are doing damage, the first night on your property is a $50 callout and we'll walk it together. Text " + PHONE + ".",
]
about_inner = ('<section class="band"><div class="wrap"><p class="eyebrow">Owner-operated · Peninsula-based</p>'
 '<h2>The person who turns up</h2><div class="post">'
 + "".join(f"<p>{x}</p>" for x in about_paras)
 + '</div><p style="margin-top:22px"><a class="btn btn-amber" href="#quote">Book your first night</a></p></div></section>')
simple_page("About Peninsula Pest Shooting | Owner-Operated Peninsula Pest Shooter",
            "Peninsula Pest Shooting is owner-operated by Josh — 25 years on the Mornington Peninsula, 18 years shooting, licensed and insured, with a conservation-first approach to feral control.",
            "/about/", about_inner,
            [("Home", DOMAIN + "/"), ("About", DOMAIN + "/about/")],
            [{"@type": "AboutPage", "url": DOMAIN + "/about/", "name": "About " + NAME, "mainEntity": {"@id": DOMAIN + "/#business"}},
             {"@type": "Person", "name": "Josh", "jobTitle": "Licensed pest and feral shooter",
              "worksFor": {"@id": DOMAIN + "/#business"}, "homeLocation": {"@type": "Place", "name": "Mornington Peninsula, Victoria"},
              "knowsAbout": ["feral control", "fox control", "rabbit control", "deer control", "thermal shooting", "wildlife conservation"]}])

# ---- footer links block (internal linking) + sitemap
groups = {}
for g, n, u in nav_links: groups.setdefault(g, []).append(f'<a href="{u}">{n}</a>')
groups["More"] = ['<a href="/about/">About</a>', '<a href="/blog/">Blog</a>', '<a href="/privacy/">Privacy</a>', '<a href="/#pricing">Pricing</a>']
links_html = '<section class="band" style="padding-block:36px;border-top:1px solid var(--line)"><div class="wrap" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:24px;font-size:14px">'
for g, items in groups.items():
    links_html += f'<div><p class="eyebrow" style="margin-bottom:8px">{g}</p><div style="display:grid;gap:4px">{"".join(items)}</div></div>'
links_html += '</div></section>\n<footer>'
for f in DIST.rglob("index.html"):
    f.write_text(f.read_text().replace("<footer>", links_html, 1))

today = datetime.date.today().isoformat()
(DIST / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    "".join(f"  <url><loc>{DOMAIN}{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls) + "</urlset>\n")
(DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
(DIST / "og.svg").write_text(OG_SVG)
(DIST / "favicon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><circle cx="32" cy="32" r="30" fill="#1f3b2a" stroke="#c47d07" stroke-width="4"/><g stroke="#e9eee6" stroke-width="3" fill="none"><line x1="32" y1="8" x2="32" y2="24"/><line x1="32" y1="40" x2="32" y2="56"/><line x1="8" y1="32" x2="24" y2="32"/><line x1="40" y1="32" x2="56" y2="32"/></g><circle cx="34" cy="36" r="6" fill="#f2a31b"/></svg>')
print(f"Built {len(urls)} pages into {DIST}")
