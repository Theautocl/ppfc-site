"""Inline SVG graphics for the PPFC site: thermal-scope hero, species icons, Peninsula map, OG image."""

SCOPE = """<svg class="scope" viewBox="0 0 400 400" role="img" aria-label="Thermal scope view with a heat signature in the crosshairs">
<defs>
 <radialGradient id="heat" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#fff3c4"/><stop offset=".35" stop-color="#f2a31b"/><stop offset=".7" stop-color="#8a2d0b" stop-opacity=".9"/><stop offset="1" stop-color="#1b1f1a" stop-opacity="0"/></radialGradient>
 <radialGradient id="vig" cx="50%" cy="50%" r="50%"><stop offset=".75" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".85"/></radialGradient>
 <clipPath id="c"><circle cx="200" cy="200" r="190"/></clipPath>
</defs>
<circle cx="200" cy="200" r="196" fill="#0b120e" stroke="#c47d07" stroke-width="4"/>
<g clip-path="url(#c)">
 <rect x="0" y="0" width="400" height="400" fill="#101a14"/>
 <path d="M0 270 Q60 250 120 262 T240 258 T400 268 L400 400 L0 400Z" fill="#17241c"/>
 <path d="M0 300 Q80 286 160 296 T320 292 T400 298 L400 400 L0 400Z" fill="#1d2d23"/>
 <g fill="#22352a"><rect x="40" y="200" width="6" height="80"/><rect x="330" y="190" width="6" height="92"/><path d="M20 206h46l-6-10h-34z"/><path d="M310 196h46l-6-10h-34z"/><line x1="0" y1="226" x2="400" y2="222" stroke="#22352a" stroke-width="2"/><line x1="0" y1="246" x2="400" y2="242" stroke="#22352a" stroke-width="2"/></g>
 <ellipse cx="212" cy="262" rx="46" ry="22" fill="url(#heat)"/>
 <ellipse cx="248" cy="252" rx="16" ry="12" fill="url(#heat)"/>
 <ellipse cx="172" cy="270" rx="22" ry="8" fill="url(#heat)" opacity=".8"/>
 <circle cx="200" cy="200" r="200" fill="url(#vig)"/>
</g>
<g stroke="#e9eee6" stroke-width="1.5" opacity=".9" fill="none">
 <line x1="200" y1="20" x2="200" y2="150"/><line x1="200" y1="250" x2="200" y2="380"/>
 <line x1="20" y1="200" x2="150" y2="200"/><line x1="250" y1="200" x2="380" y2="200"/>
 <circle cx="200" cy="200" r="60" stroke-dasharray="4 6"/>
 <g stroke-width="1"><line x1="200" y1="110" x2="200" y2="120"/><line x1="200" y1="280" x2="200" y2="290"/><line x1="110" y1="200" x2="120" y2="200"/><line x1="280" y1="200" x2="290" y2="200"/></g>
</g>
<g fill="#c47d07" font-family="Barlow Condensed,Arial Narrow,sans-serif" font-size="13" letter-spacing="1.5">
 <text x="34" y="44">THERMAL · WHITE HOT</text><text x="296" y="44">x4</text><text x="34" y="372">ID CONFIRMED</text><text x="306" y="372">38 m</text>
</g>
</svg>"""

ICONS = {
"Foxes": '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M8 10l10 7h12l10-7-3 16c-1 6-6 10-13 10S12 32 11 26z" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round"/><circle cx="18" cy="24" r="1.8" fill="currentColor"/><circle cx="30" cy="24" r="1.8" fill="currentColor"/><path d="M24 30l-2 2h4z" fill="currentColor"/></svg>',
"Rabbits": '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M17 26c-3-9-4-17 0-19s6 8 7 15M31 26c3-9 4-17 0-19s-6 8-7 15" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/><ellipse cx="24" cy="32" rx="10" ry="8" fill="none" stroke="currentColor" stroke-width="2.4"/><circle cx="20" cy="31" r="1.6" fill="currentColor"/><circle cx="28" cy="31" r="1.6" fill="currentColor"/></svg>',
"Deer": '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M16 28l-4-8 2-10 4 8 2-8M32 28l4-8-2-10-4 8-2-8" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/><path d="M15 26h18l-3 10h-12z" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round"/><circle cx="20" cy="30" r="1.6" fill="currentColor"/><circle cx="28" cy="30" r="1.6" fill="currentColor"/></svg>',
"Feral cats": '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M12 14l6 6h12l6-6v18a12 12 0 0 1-24 0z" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round"/><circle cx="19" cy="27" r="1.8" fill="currentColor"/><circle cx="29" cy="27" r="1.8" fill="currentColor"/><path d="M8 30h7M33 30h7M8 35l7-2M33 33l7 2" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
"Rats": '<svg viewBox="0 0 48 48" aria-hidden="true"><ellipse cx="22" cy="28" rx="13" ry="8" fill="none" stroke="currentColor" stroke-width="2.4"/><circle cx="12" cy="22" r="4" fill="none" stroke="currentColor" stroke-width="2.4"/><circle cx="11" cy="26" r="1.4" fill="currentColor"/><path d="M35 28c6 0 8 4 6 8" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>',
}

# Stylised Mornington Peninsula outline (approximate), Port Phillip top-left, Westernport right.
MAP = """<svg class="map" viewBox="0 0 640 440" role="img" aria-label="Map of the Mornington Peninsula showing the towns we cover">
<path d="M520 40 L490 90 L440 120 L420 170 L400 210 L370 230 L300 260 L220 272 L140 242 L110 222 L50 202 L80 232 L120 262 L200 300 L260 342 L282 392 L350 400 L420 382 L470 360 L560 292 L600 240 L600 160 L585 120 L550 90 Z" fill="var(--map-fill)" stroke="var(--map-line)" stroke-width="2" stroke-linejoin="round"/>
<text x="40" y="150" class="sea">PORT PHILLIP</text><text x="470" y="430" class="sea">BASS STRAIT</text><text x="500" y="350" class="sea">WESTERNPORT</text>
<g class="town">
 <circle cx="455" cy="128" r="5"/><text x="465" y="122">Mornington</text>
 <circle cx="495" cy="92" r="4"/><text x="505" y="86">Mt Eliza</text>
 <circle cx="430" cy="175" r="4"/><text x="440" y="180">Mt Martha</text>
 <circle cx="380" cy="235" r="4"/><text x="390" y="240">Dromana</text>
 <circle cx="305" cy="262" r="4"/><text x="312" y="252">Rosebud</text>
 <circle cx="225" cy="272" r="4"/><text x="214" y="294">Rye</text>
 <circle cx="140" cy="245" r="4"/><text x="150" y="262">Sorrento</text>
 <circle cx="400" cy="275" r="5"/><text x="412" y="280">Red Hill</text>
 <circle cx="372" cy="305" r="4"/><text x="384" y="312">Main Ridge</text>
 <circle cx="300" cy="305" r="4"/><text x="258" y="326">Boneo</text>
 <circle cx="420" cy="372" r="4"/><text x="384" y="392">Flinders</text>
 <circle cx="520" cy="275" r="5"/><text x="534" y="270">Balnarring</text>
 <circle cx="548" cy="300" r="4"/><text x="560" y="305">Somers</text>
 <circle cx="585" cy="205" r="5"/><text x="548" y="196">Hastings</text>
 <circle cx="584" cy="160" r="4"/><text x="548" y="152">Tyabb</text>
 <circle cx="290" cy="388" r="4"/><text x="200" y="408">Cape Schanck</text>
</g>
</svg>"""

MAP_CSS = """
.map{width:100%;height:auto;max-width:100%;display:block;--map-fill:#dfe6da;--map-line:#1f3b2a}
.map .sea{font-family:var(--display);font-size:13px;letter-spacing:.14em;fill:var(--muted);font-weight:600}
.map .town circle{fill:var(--amber);stroke:var(--surface);stroke-width:1.5}
.map .town text{font-family:var(--body);font-size:13px;font-weight:600;fill:var(--fg)}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .map{--map-fill:#20302a;--map-line:#6f8c7a}}
:root[data-theme="dark"] .map{--map-fill:#20302a;--map-line:#6f8c7a}
.hero-photo{width:100%;max-height:460px;object-fit:cover;display:block;margin-top:36px;border:4px solid var(--amber)}
.sp .ico{width:44px;height:44px;color:var(--amber);margin-bottom:10px;display:block}
.faq{display:grid;gap:10px;margin-top:32px;max-width:72ch}
.faq details{background:var(--surface);border:1px solid var(--line);padding:14px 18px}
.faq summary{font-family:var(--display);font-size:20px;font-weight:700;text-transform:uppercase;cursor:pointer;list-style:none;display:flex;justify-content:space-between;gap:12px}
.faq summary::after{content:"+";color:var(--amber);font-size:24px;line-height:1}
.faq details[open] summary::after{content:"–"}
.faq p{margin-top:10px;color:var(--muted)}
.about{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center;margin-top:32px}
@media (max-width:760px){.about{grid-template-columns:1fr}}
.about .photo{aspect-ratio:4/3;max-width:100%;background:var(--green) url('/favicon.svg') center/90px no-repeat;border:4px solid var(--amber);overflow:hidden}
.about .photo img{width:100%;height:100%;object-fit:cover;display:block}
.about ul{margin:14px 0 0;padding-left:18px;color:var(--muted)}
.post{max-width:68ch;margin-top:32px;display:grid;gap:18px;font-size:18px}
.post-list{display:grid;gap:18px;margin-top:32px;max-width:72ch}
.post-list a{display:block;background:var(--surface);border-left:4px solid var(--amber);padding:18px 20px;text-decoration:none}
.post-list a h3{font-size:22px;margin-bottom:6px}
.post-list a p{color:var(--muted);font-size:16px}
.crumbs{font-size:14px;color:var(--muted);padding-block:14px}
.crumbs a{text-decoration:none}
"""

SECTORS = """<section class="band" id="sectors">
  <div class="wrap">
    <p class="eyebrow">Who we work for</p>
    <h2>From vineyards to grazing country</h2>
    <p class="lede" style="margin-top:12px">Most of our work is for commercial and agricultural operations that lose stock, pasture and produce to feral animals. We run scheduled programs sized to the property, not one-off callouts.</p>
    <div class="grid">
      <div class="sp"><h3>Vineyards &amp; wineries</h3><p>Deer and rabbits stripping shoots and ring-barking young vines. Monthly programs from budburst, worked around cellar-door hours and harvest.</p><a class="tag" href="/vineyard-pest-control-mornington-peninsula/" style="text-decoration:none">Vineyard control</a></div>
      <div class="sp"><h3>Commercial &amp; grazing farms</h3><p>Fox predation on lambs and calves, rabbits in pasture and fodder crops, deer through fences. Per-hectare and per-program rates for working farms.</p><a class="tag" href="/commercial-farm-pest-control-mornington-peninsula/" style="text-decoration:none">Commercial farms</a></div>
      <div class="sp"><h3>Orchards &amp; market gardens</h3><p>Rabbits and deer on young trees, seedlings and turf. Bait-free around produce, timed around picking and planting.</p><a class="tag" href="/orchard-market-garden-pest-control-mornington-peninsula/" style="text-decoration:none">Orchards &amp; gardens</a></div>
      <div class="sp"><h3>Horse studs &amp; agistment</h3><p>Foxes around foaling paddocks and rats in feed rooms, all bait-free so your horses, dogs and owls stay safe.</p><a class="tag" href="/horse-property-pest-control-mornington-peninsula/" style="text-decoration:none">Horse properties</a></div>
      <div class="sp"><h3>Hobby farms &amp; lifestyle acreage</h3><p>Small blocks near town where most shooters can't legally work. We hold the Public Place Permit that makes it possible.</p><a class="tag" href="/hobby-farm-pest-control-mornington-peninsula/" style="text-decoration:none">Hobby farms</a></div>
      <div class="sp"><h3>Councils, Landcare &amp; reserves</h3><p>Fox and feral cat control on private land bordering reserves, protecting hooded plovers, bandicoots and native wildlife.</p><span class="tag">Conservation work</span></div>
    </div>
  </div>
</section>
"""

ABOUT = """<section class="band" style="background:var(--surface)" id="about">
  <div class="wrap">
    <p class="eyebrow">Who you're dealing with</p>
    <h2>Owner-operated, Peninsula-based</h2>
    <div class="about">
      <div>
        <p class="lede">One licensed operator, not a franchise. You deal with the person who turns up, and the same person every visit.</p>
      </div>
      <ul>
        <li>Victorian Category A/B firearms licence, Game Licence</li>
        <li>Public Place Permit for work close to houses and roads</li>
        <li>Thermal optics on every job</li>
        <li>SSAA member, public liability insured</li>
        <li>Texts answered same day, 7 days a week</li>
      </ul>
    </div>
  </div>
</section>
"""

OG_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
<rect width="1200" height="630" fill="#1f3b2a"/><rect y="610" width="1200" height="20" fill="#c47d07"/>
<g font-family="Barlow Condensed,DejaVu Sans Condensed,Arial Narrow,sans-serif" font-weight="800" fill="#e9eee6">
<text x="80" y="200" font-size="92" letter-spacing="1">PENINSULA</text>
<text x="80" y="300" font-size="92" letter-spacing="1">PEST SHOOTING</text>
<text x="80" y="390" font-size="40" font-weight="600" fill="#c47d07" letter-spacing="4">FOXES · RABBITS · DEER · FERAL CATS · RATS</text>
<text x="80" y="470" font-size="36" font-weight="600" fill="#e9eee6" opacity=".85">Mornington Peninsula · Licensed, insured &amp; bait-free</text>
<text x="80" y="550" font-size="40" font-weight="700" fill="#c47d07">Text 0466 659 997</text>
</g>
<circle cx="1010" cy="315" r="150" fill="#0b120e" stroke="#c47d07" stroke-width="6"/>
<g stroke="#e9eee6" stroke-width="3" fill="none"><line x1="1010" y1="180" x2="1010" y2="280"/><line x1="1010" y1="350" x2="1010" y2="450"/><line x1="875" y1="315" x2="975" y2="315"/><line x1="1045" y1="315" x2="1145" y2="315"/><circle cx="1010" cy="315" r="45" stroke-dasharray="6 8"/></g>
<ellipse cx="1020" cy="360" rx="40" ry="18" fill="#f2a31b"/><ellipse cx="1050" cy="350" rx="14" ry="10" fill="#fff3c4"/>
</svg>"""
