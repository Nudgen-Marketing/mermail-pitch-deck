#!/usr/bin/env python3
"""Build mermail-yc-deck.html — a YC-style pitch deck, self-contained with base64 assets.

Narrative: Mermail is a privacy-first **agentic inbox fleet**. Each inbox is an
autonomous agent with its own rule set, tools, and permissions, and the inboxes
coordinate with each other over email. Customer support is the wedge (first live
agent). Keeps the Mermail brand theme (dark #01070d + neon cyan #70eeee) and YC
pitch discipline: one idea per slide, big type, big numbers, minimal copy.

Run from the project root:  python3 scripts/build-yc-deck.py
"""
import base64
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"


def b64(name: str) -> str:
    data = (ASSETS / name).read_bytes()
    ext = name.rsplit(".", 1)[-1].lower()
    mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg"}[ext]
    return f"data:{mime};base64,{base64.b64encode(data).decode()}"


LOGO = b64("LongLogo.png")
MARK = LOGO  # reuse the long logo (small file) for the corner brand mark; embedded once via CSS
NATHAN = b64("Nathan.jpeg")
TOAN = b64("toan.jpg")

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Mermail — YC Pitch</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
  <style>
    :root {{
      --background:     #01070d;
      --foreground:     #ffffff;
      --success:        #70eeee;
      --success-strong: #70eeee;

      --surface:        #06111f;
      --surface-2:      #081629;
      --surface-3:      #102a3b;

      --border:         #1f3c50;
      --border-subtle:  #102a3b;
      --border-accent:  rgba(112,238,238,0.28);

      --text-primary:   #ffffff;
      --text-secondary: #b6c7d6;
      --text-muted:     #5a6b7f;

      --red:    #ef4444;

      --s1:4px; --s2:8px; --s3:12px; --s4:16px; --s6:24px; --s8:32px;
      --s10:40px; --s12:48px; --s16:64px; --s20:80px;

      --r-sm:8px; --r-md:12px; --r-lg:18px;
      --ease: cubic-bezier(0.16,1,0.3,1);
    }}

    @media (prefers-reduced-motion: reduce) {{
      *, *::before, *::after {{ animation-duration:.01ms !important; animation-iteration-count:1 !important; transition-duration:.01ms !important; }}
    }}

    *, *::before, *::after {{ margin:0; padding:0; box-sizing:border-box; }}
    html {{ font-size:118%; }}

    html, body {{ overflow-x:hidden; }}
    body {{
      font-family:'Inter', system-ui, -apple-system, 'Segoe UI', Arial, sans-serif;
      background:var(--background);
      color:var(--text-primary);
      overflow:hidden;
      -webkit-font-smoothing:antialiased;
    }}

    /* subtle brand atmosphere */
    body::before {{
      content:''; position:fixed; inset:0; pointer-events:none; z-index:0;
      background:
        radial-gradient(1100px 700px at 82% -10%, rgba(112,238,238,0.10), transparent 60%),
        radial-gradient(900px 600px at -5% 110%, rgba(60,145,255,0.06), transparent 55%);
    }}

    .deck {{ width:100vw; height:100vh; position:relative; z-index:1; }}

    .slide {{
      position:absolute; inset:0;
      display:flex; flex-direction:column; justify-content:center;
      padding:7vh 8vw;
      opacity:0; transform:translateY(16px);
      transition:opacity .5s var(--ease), transform .5s var(--ease);
      pointer-events:none;
    }}
    .slide.active {{ opacity:1; transform:translateY(0); pointer-events:all; }}
    .slide.prev  {{ opacity:0; transform:translateY(-16px); }}

    /* chrome */
    .ghost-index {{
      position:absolute; top:3vh; left:8vw;
      font-size:clamp(5rem, 16vw, 13rem); font-weight:900;
      line-height:.8; letter-spacing:-.05em;
      color:transparent; -webkit-text-stroke:1.5px rgba(112,238,238,0.10);
      pointer-events:none; user-select:none; z-index:0;
    }}
    .slide-brand {{
      position:absolute; top:3.4vh; right:8vw;
      height:22px; width:150px; opacity:.55; z-index:2;
      background:url('{MARK}') no-repeat right center; background-size:contain;
    }}
    .slide-meta {{
      position:absolute; bottom:3.4vh; left:8vw;
      font-size:.72rem; letter-spacing:.22em; text-transform:uppercase;
      color:var(--text-muted); z-index:2;
    }}
    .slide-page {{
      position:absolute; bottom:3.4vh; right:8vw;
      font-size:.72rem; letter-spacing:.14em; color:var(--text-muted); z-index:2;
    }}

    .eyebrow {{
      font-size:.78rem; font-weight:600; letter-spacing:.24em; text-transform:uppercase;
      color:var(--success-strong); margin-bottom:var(--s6);
      display:flex; align-items:center; gap:var(--s3);
    }}
    .eyebrow::before {{ content:''; width:28px; height:2px; background:var(--success-strong); display:inline-block; }}

    .content {{ position:relative; z-index:1; max-width:1180px; width:100%; margin:0 auto; }}

    /* prevent grid/flex children from forcing horizontal overflow */
    .ask-grid > *, .market-grid > *, .duo > *, .team > *, .member > * {{ min-width:0; }}
    h1, h2, h3, p, .statement, .ask-amt {{ overflow-wrap:break-word; }}

    h1 {{ font-size:clamp(2.6rem, 6.4vw, 5.6rem); font-weight:800; line-height:1.0; letter-spacing:-.04em; }}
    h2 {{ font-size:clamp(2.1rem, 4.6vw, 3.9rem); font-weight:800; line-height:1.05; letter-spacing:-.035em; }}
    h3 {{ font-size:1.18rem; font-weight:700; letter-spacing:-.02em; }}
    .em {{ color:var(--success-strong); }}

    .lede {{ font-size:clamp(1.1rem, 1.8vw, 1.5rem); color:var(--text-secondary); line-height:1.5; font-weight:400; max-width:880px; }}

    /* ── Cover ── */
    .cover {{ align-items:flex-start; }}
    .cover-logo {{ height:64px; width:auto; margin-bottom:var(--s12); }}
    .cover h1 {{ max-width:16ch; }}
    .cover .lede {{ margin-top:var(--s8); }}
    .cover-stats {{ display:flex; gap:var(--s16); margin-top:var(--s16); flex-wrap:wrap; }}
    .cstat .n {{ font-size:clamp(1.8rem,3vw,2.6rem); font-weight:800; letter-spacing:-.03em; }}
    .cstat .n.accent {{ color:var(--success-strong); }}
    .cstat .l {{ font-size:.82rem; color:var(--text-muted); margin-top:6px; max-width:20ch; }}

    /* ── Big number rows (problem) ── */
    .stack {{ display:flex; flex-direction:column; gap:var(--s4); margin-top:var(--s8); max-width:980px; }}
    .row {{
      display:grid; grid-template-columns:minmax(0,240px) 1fr; gap:var(--s8); align-items:baseline;
      padding-bottom:var(--s6); border-bottom:1px solid var(--border-subtle);
    }}
    .row .big {{ font-size:clamp(2rem,3.6vw,3rem); font-weight:800; letter-spacing:-.035em; color:var(--success-strong); min-width:0; white-space:nowrap; }}
    .row .big.neutral {{ color:var(--text-primary); }}
    .row .desc strong {{ display:block; font-size:1.12rem; font-weight:700; margin-bottom:4px; }}
    .row .desc span {{ font-size:.95rem; color:var(--text-secondary); line-height:1.5; }}
    .row a {{ color:var(--text-muted); text-decoration:underline; text-underline-offset:2px; }}

    /* ── Solution statement ── */
    .statement {{ font-size:clamp(1.7rem,3.4vw,2.9rem); font-weight:700; line-height:1.2; letter-spacing:-.02em; max-width:20ch; margin-top:var(--s8); }}
    .statement .em {{ font-weight:800; }}

    /* ── Fleet diagram ── */
    .fleet-stage {{ width:100%; max-width:900px; margin:var(--s6) auto 0; }}
    .fleet-stage svg {{ width:100%; height:auto; display:block; overflow:visible; }}
    .edge-base {{ stroke:rgba(112,238,238,0.16); stroke-width:1.5; fill:none; }}
    .edge-active {{ stroke:var(--success-strong); stroke-width:2; fill:none; opacity:.5; }}
    .edge-dash {{ stroke:var(--success-strong); stroke-width:2; fill:none; stroke-dasharray:1 9; stroke-linecap:round; opacity:.55; animation:flow 1.4s linear infinite; }}
    @keyframes flow {{ to {{ stroke-dashoffset:-30; }} }}
    .packet {{ fill:var(--success-strong); offset-path:path('M400 106 L270 200'); animation:travel 2.4s cubic-bezier(0.45,0,0.55,1) infinite; }}
    @keyframes travel {{ 0%{{offset-distance:0%; opacity:0}} 12%{{opacity:1}} 86%{{opacity:1}} 100%{{offset-distance:100%; opacity:0}} }}
    .chip-line {{ stroke:var(--border-accent); stroke-width:1.2; }}
    .pill {{ fill:var(--success-strong); }}
    .pill-txt {{ fill:#01070d; font-size:11px; font-weight:800; letter-spacing:.04em; text-anchor:middle; font-family:'Inter',sans-serif; }}
    .fchip {{ fill:rgba(8,22,41,0.92); stroke:var(--border); stroke-width:1; }}
    .fchip.appr {{ fill:rgba(112,238,238,0.12); stroke:var(--border-accent); }}
    .fchip-txt {{ fill:var(--text-primary); font-size:12.5px; font-weight:600; text-anchor:middle; font-family:'Inter',sans-serif; }}
    .fchip-txt.appr {{ fill:var(--success-strong); font-weight:700; }}
    .farrow {{ fill:var(--text-muted); font-size:15px; text-anchor:middle; font-family:'Inter',sans-serif; }}
    .node-c {{ fill:var(--surface-2); stroke:var(--border); stroke-width:1.5; }}
    .node-c.live {{ stroke:var(--success-strong); stroke-width:2.5; }}
    .node-ic {{ font-size:30px; text-anchor:middle; dominant-baseline:central; }}
    .node-lb {{ fill:var(--text-secondary); font-size:18px; font-weight:600; text-anchor:middle; font-family:'Inter',sans-serif; }}
    .node-lb.live {{ fill:var(--text-primary); }}
    .node-sub {{ fill:var(--text-muted); font-size:12px; letter-spacing:.12em; text-anchor:middle; font-family:'Inter',sans-serif; font-weight:700; }}
    .msg-rect {{ fill:rgba(8,22,41,0.92); stroke:var(--border-accent); stroke-width:1; }}
    .msg-txt {{ fill:var(--text-primary); font-size:13px; font-weight:600; text-anchor:start; font-family:'Inter',sans-serif; }}
    .fleet-cap {{ text-align:center; font-size:1.02rem; color:var(--text-secondary); margin-top:var(--s6); max-width:740px; margin-left:auto; margin-right:auto; line-height:1.5; }}
    .fleet-cap strong {{ color:var(--text-primary); }}

    /* ── Trio cards (anatomy / why now) ── */
    .trio {{ display:grid; grid-template-columns:repeat(3,1fr); gap:var(--s6); margin-top:var(--s10); }}
    .tcard {{ padding:var(--s8); border:1px solid var(--border-subtle); border-radius:var(--r-lg); background:var(--surface); }}
    .tcard.accent {{ border-color:var(--border-accent); background:var(--surface-2); }}
    .tcard .ic {{ font-size:1.7rem; }}
    .tcard .k {{ font-size:.72rem; font-weight:700; letter-spacing:.16em; text-transform:uppercase; color:var(--success-strong); margin-top:var(--s4); }}
    .tcard h3 {{ margin:var(--s2) 0 var(--s3); font-size:1.32rem; }}
    .tcard p {{ font-size:.92rem; color:var(--text-secondary); line-height:1.55; }}

    /* ── Two-column compare ── */
    .duo {{ display:grid; grid-template-columns:1fr 1fr; gap:var(--s6); margin-top:var(--s10); }}
    .panel {{ padding:var(--s8); border:1px solid var(--border-subtle); border-radius:var(--r-lg); background:var(--surface); }}
    .panel.bad {{ border-left:3px solid var(--red); }}
    .panel.good {{ border-color:var(--border-accent); background:var(--surface-2); }}
    .panel h3 {{ margin-bottom:var(--s6); }}
    .panel.bad h3 {{ color:var(--text-secondary); }}
    .panel.good h3 {{ color:var(--success-strong); }}
    .panel li {{ list-style:none; display:flex; gap:var(--s3); font-size:.96rem; line-height:1.5; margin-bottom:var(--s3); color:var(--text-secondary); }}
    .panel.good li {{ color:var(--text-primary); }}
    .mark-x {{ color:var(--red); font-weight:700; }}
    .mark-v {{ color:var(--success-strong); font-weight:700; }}

    /* ── Market ── */
    .market-grid {{ display:grid; grid-template-columns:1.1fr 1fr; gap:var(--s16); align-items:center; margin-top:var(--s10); }}
    .tam-bars {{ display:flex; flex-direction:column; gap:var(--s6); }}
    .tam .head {{ display:flex; justify-content:space-between; align-items:baseline; margin-bottom:var(--s3); }}
    .tam .tag {{ font-size:.72rem; font-weight:700; letter-spacing:.14em; text-transform:uppercase; color:var(--text-muted); }}
    .tam .val {{ font-size:1.7rem; font-weight:800; letter-spacing:-.03em; }}
    .tam .val.accent {{ color:var(--success-strong); }}
    .tam .track {{ height:12px; background:var(--surface-3); border-radius:6px; overflow:hidden; }}
    .tam .fill {{ height:100%; border-radius:6px; }}
    .tam .note {{ font-size:.8rem; color:var(--text-secondary); margin-top:8px; }}
    .tam .note a {{ color:var(--text-muted); text-decoration:underline; text-underline-offset:2px; }}
    .cagr {{ text-align:left; }}
    .cagr .pct {{ font-size:clamp(3.4rem,7.5vw,6rem); font-weight:900; letter-spacing:-.05em; color:var(--success-strong); line-height:.9; }}
    .cagr p {{ font-size:1.02rem; color:var(--text-secondary); margin-top:var(--s4); line-height:1.5; max-width:32ch; }}
    .cagr p a {{ color:var(--text-muted); text-decoration:underline; text-underline-offset:2px; }}

    /* ── Business model ── */
    .tiers {{ display:grid; grid-template-columns:repeat(3,1fr); gap:var(--s4); margin-top:var(--s10); }}
    .tier {{ padding:var(--s8); border:1px solid var(--border-subtle); border-radius:var(--r-lg); background:var(--surface); }}
    .tier.hot {{ border-color:var(--border-accent); background:var(--surface-2); }}
    .tier .k {{ font-size:.72rem; font-weight:700; letter-spacing:.14em; text-transform:uppercase; color:var(--text-muted); margin-bottom:var(--s3); }}
    .tier.hot .k {{ color:var(--success-strong); }}
    .tier p {{ font-size:.9rem; color:var(--text-secondary); margin-top:var(--s3); line-height:1.55; }}
    .banner {{
      display:flex; align-items:center; gap:var(--s4); margin-top:var(--s10);
      padding:var(--s6) var(--s8); border:1px solid var(--border-accent);
      border-radius:var(--r-md); background:rgba(112,238,238,0.05); max-width:1000px;
    }}
    .banner .ic {{ font-size:1.4rem; }}
    .banner span {{ font-size:1.05rem; color:var(--text-secondary); }}

    /* ── Traction timeline ── */
    .tl {{ display:grid; grid-template-columns:repeat(4,1fr); gap:var(--s4); margin-top:var(--s12); position:relative; }}
    .mile {{ position:relative; padding-top:var(--s8); }}
    /* each segment runs from this dot's centre (8px) to the next dot's centre (col width + gap) */
    .mile:not(:last-child)::after {{ content:''; position:absolute; top:7px; left:8px; width:calc(100% + var(--s4)); height:2px; background:var(--border-subtle); }}
    .mile.done:not(:last-child)::after {{ background:var(--success-strong); }}
    .mile .dot {{ position:absolute; top:0; left:0; width:16px; height:16px; border-radius:50%; background:var(--surface-3); border:2px solid var(--border); z-index:1; }}
    .mile.done .dot {{ background:var(--success-strong); border-color:var(--success-strong); }}
    .mile.now .dot {{ background:var(--background); border-color:var(--success-strong); box-shadow:0 0 0 4px rgba(112,238,238,0.18); }}
    .mile .date {{ font-size:.72rem; font-weight:700; letter-spacing:.1em; text-transform:uppercase; color:var(--success-strong); }}
    .mile h3 {{ margin:var(--s2) 0; }}
    .mile p {{ font-size:.86rem; color:var(--text-secondary); line-height:1.5; }}

    /* ── Team ── */
    .team {{ display:grid; grid-template-columns:1fr 1fr; gap:var(--s6); margin-top:var(--s10); }}
    .member {{ display:flex; gap:var(--s6); align-items:center; padding:var(--s8); border:1px solid var(--border-subtle); border-radius:var(--r-lg); background:var(--surface); }}
    .member img {{ width:84px; height:84px; border-radius:50%; object-fit:cover; flex-shrink:0; border:2px solid var(--border-accent); }}
    .member .role {{ font-size:.78rem; font-weight:700; letter-spacing:.1em; text-transform:uppercase; color:var(--success-strong); margin:4px 0 8px; }}
    .member p {{ font-size:.86rem; color:var(--text-secondary); line-height:1.5; }}

    /* ── Ask ── */
    .ask-grid {{ display:grid; grid-template-columns:1fr 1fr; gap:var(--s16); align-items:center; margin-top:var(--s8); }}
    .ask-amt {{ font-size:clamp(3.2rem,7vw,5.6rem); font-weight:900; letter-spacing:-.05em; line-height:.95; }}
    .ask-amt .em {{ color:var(--success-strong); }}
    .ask-sub {{ font-size:1.1rem; color:var(--text-secondary); margin-top:var(--s4); line-height:1.55; max-width:34ch; }}
    .funds {{ display:flex; flex-direction:column; gap:var(--s6); }}
    .fund .head {{ display:flex; justify-content:space-between; font-size:.92rem; margin-bottom:8px; }}
    .fund .head .pct {{ color:var(--success-strong); font-weight:700; }}
    .fund .track {{ height:10px; background:var(--surface-3); border-radius:5px; overflow:hidden; }}
    .fund .fill {{ height:100%; background:var(--success-strong); border-radius:5px; }}
    .vision {{ margin-top:var(--s12); padding-top:var(--s8); border-top:1px solid var(--border-subtle); }}
    .vision .q {{ font-size:clamp(1.3rem,2.4vw,1.9rem); font-weight:700; letter-spacing:-.02em; line-height:1.35; max-width:32ch; }}
    .contact {{ display:flex; gap:var(--s8); margin-top:var(--s8); flex-wrap:wrap; }}
    .contact a {{ color:var(--success-strong); text-decoration:none; font-size:.95rem; font-weight:600; }}
    .contact a:hover {{ text-decoration:underline; }}

    .kbd-hint {{ position:absolute; bottom:3.4vh; left:50%; transform:translateX(-50%); font-size:.72rem; color:var(--text-muted); letter-spacing:.1em; z-index:2; }}

    /* ── Nav ── */
    .nav {{ position:fixed; bottom:var(--s6); left:50%; transform:translateX(-50%); display:flex; align-items:center; gap:var(--s4); z-index:20; }}
    .nav-btn {{
      width:40px; height:40px; border-radius:50%; border:1px solid var(--border);
      background:var(--surface); color:var(--text-primary); font-size:1rem; cursor:pointer;
      transition:all .2s var(--ease); display:flex; align-items:center; justify-content:center;
    }}
    .nav-btn:hover {{ border-color:var(--success-strong); color:var(--success-strong); transform:translateY(-2px); }}
    .nav-btn:focus-visible {{ outline:2px solid var(--success-strong); outline-offset:2px; }}
    .dots {{ display:flex; gap:8px; }}
    .dot {{ width:8px; height:8px; border-radius:50%; background:var(--border); cursor:pointer; transition:all .25s var(--ease); border:none; padding:0; }}
    .dot.active {{ background:var(--success-strong); width:22px; border-radius:4px; }}
    .dot:focus-visible {{ outline:2px solid var(--success-strong); outline-offset:2px; }}

    @media (max-width:820px) {{
      html {{ font-size:100%; }}
      .slide {{ padding:13vh 6vw 16vh; justify-content:flex-start; overflow-y:auto; overflow-x:hidden; }}
      .trio, .tiers, .tl {{ grid-template-columns:1fr 1fr; }}
      .duo, .market-grid, .team, .ask-grid {{ grid-template-columns:1fr; gap:var(--s8); }}
      .mile::after {{ display:none; }}
      .cover-stats {{ gap:var(--s8); }}
      .ghost-index {{ font-size:7rem; }}
      .ask-amt {{ font-size:clamp(2.6rem,12vw,3.6rem); }}
      /* on phones the corner chrome would collide with the solid footer nav — hide it; the dots still show position */
      .slide-meta, .slide-page {{ display:none; }}
      .nav {{
        left:0; right:0; bottom:0; transform:none; width:100%;
        justify-content:center; padding:12px 0 14px;
        background:rgba(1,7,13,0.92); border-top:1px solid var(--border-subtle);
        backdrop-filter:blur(8px); -webkit-backdrop-filter:blur(8px);
      }}
    }}
    @media (max-width:520px) {{
      .trio, .tiers, .tl {{ grid-template-columns:1fr; }}
    }}
  </style>
</head>
<body>
  <div class="deck" id="deck">

    <!-- 01 · COVER -->
    <section class="slide active cover" id="s0" aria-label="Cover">
      <div class="content">
        <img class="cover-logo" src="{LOGO}" alt="Mermail" />
        <h1>What if your company&rsquo;s inboxes could <span class="em">talk to each other?</span></h1>
        <p class="lede">Mermail is a privacy-first fleet of agentic inboxes. Each one reads, acts, and coordinates with the rest &mdash; with its own rules, tools, and permissions. Humans stay in control.</p>
        <div class="cover-stats">
          <div class="cstat"><div class="n accent">$47.8B</div><div class="l">AI customer service &mdash; our wedge market, by 2030</div></div>
          <div class="cstat"><div class="n">25.8%</div><div class="l">CAGR, 2024&ndash;2030</div></div>
          <div class="cstat"><div class="n">Zero</div><div class="l">customer data stored or trained on</div></div>
        </div>
      </div>
      <div class="slide-meta">Cover</div><div class="slide-page">01 / 11</div>
    </section>

    <!-- 02 · PROBLEM -->
    <section class="slide" id="s1" aria-label="Problem">
      <div class="ghost-index">01</div>
      <div class="slide-brand"></div>
      <div class="content">
        <div class="eyebrow">Problem</div>
        <h2>Business runs on human inboxes &mdash; <span class="em">and humans don&rsquo;t scale.</span></h2>
        <div class="stack">
          <div class="row">
            <div class="big neutral">Linear</div>
            <div class="desc"><strong>Every inbox is a human seat</strong><span>Support, billing, ops, sales, vendors &mdash; the business runs on inboxes, and each one is staffed by a person. 2&times; the volume means 2&times; the headcount.</span></div>
          </div>
          <div class="row">
            <div class="big">$10&ndash;20K</div>
            <div class="desc"><strong>Every seat is slow and costly to add</strong><span>Per hire, plus 60&ndash;90 days of ramp and 30&ndash;45% annual attrition &mdash; you pay it over and over. · <a href="https://www.plivo.com/blog/hidden-costs-of-customer-service-agent-turnover-and-how-to-reduce-them/" target="_blank" rel="noopener">McKinsey / industry</a></span></div>
          </div>
          <div class="row">
            <div class="big neutral">Capped</div>
            <div class="desc"><strong>And it still caps out</strong><span>24/7 coverage needs 4&ndash;5 people per seat. Nights, weekends, and spikes go unanswered. Humans don&rsquo;t scale.</span></div>
          </div>
        </div>
        <div class="banner" style="margin-top:var(--s6);"><span class="ic">⚡</span><span>An <strong style="color:var(--text-primary)">agent</strong> scales the instant it runs an inbox &mdash; a <strong style="color:var(--text-primary)">human</strong> never could.</span></div>
      </div>
      <div class="slide-meta">The Problem</div><div class="slide-page">02 / 11</div>
    </section>

    <!-- 03 · SOLUTION -->
    <section class="slide" id="s2" aria-label="Solution">
      <div class="ghost-index">02</div>
      <div class="slide-brand"></div>
      <div class="content">
        <div class="eyebrow">Solution</div>
        <p class="statement">Give every job its own <span class="em">agentic inbox</span> &mdash; each with its own rules, tools, and permissions &mdash; and let them <span class="em">email each other</span> to get work done.</p>
      </div>
      <div class="slide-meta">The Solution</div><div class="slide-page">03 / 11</div>
    </section>

    <!-- 04 · THE FLEET (diagram) -->
    <section class="slide" id="s3" aria-label="The fleet">
      <div class="ghost-index">03</div>
      <div class="slide-brand"></div>
      <div class="content">
        <div class="eyebrow">The Fleet</div>
        <h2>An inbox fleet that <span class="em">coordinates itself.</span></h2>
        <div class="fleet-stage">
          <svg viewBox="0 0 800 440" role="img" aria-label="Diagram of inbox agents messaging each other, paying via the x402 protocol">
            <!-- structural mesh -->
            <g>
              <line class="edge-base" x1="400" y1="106" x2="530" y2="200" />
              <line class="edge-base" x1="270" y1="200" x2="320" y2="350" />
              <line class="edge-base" x1="530" y1="200" x2="480" y2="350" />
              <line class="edge-base" x1="320" y1="350" x2="480" y2="350" />
              <line class="edge-base" x1="400" y1="106" x2="320" y2="350" />
              <line class="edge-base" x1="400" y1="106" x2="480" y2="350" />
              <line class="edge-base" x1="270" y1="200" x2="530" y2="200" />
            </g>
            <!-- active comms route: Support -> Billing -->
            <line class="edge-active" x1="400" y1="106" x2="270" y2="200" />
            <line class="edge-dash"   x1="400" y1="106" x2="270" y2="200" />
            <circle class="packet" r="4.5" />
            <!-- inter-agent handoff flow with human-in-the-loop approval (clear of node labels) -->
            <line class="chip-line" x1="400" y1="47" x2="400" y2="62" />
            <g transform="translate(400,30)">
              <!-- requesting agent -->
              <rect class="fchip" x="-285" y="-15" width="100" height="30" rx="8" />
              <text class="fchip-txt" x="-235" y="1">Support</text>
              <text class="farrow" x="-172" y="1">&rarr;</text>
              <!-- human approval gate -->
              <rect class="fchip appr" x="-160" y="-15" width="146" height="30" rx="8" />
              <text class="fchip-txt appr" x="-87" y="1">&#128100; You approve</text>
              <text class="farrow" x="-2" y="1">&rarr;</text>
              <!-- executing agent + payment -->
              <rect class="fchip" x="10" y="-15" width="212" height="30" rx="8" />
              <text class="fchip-txt" x="116" y="1">Billing &middot; refund #1284</text>
              <rect class="pill" x="232" y="-11" width="56" height="22" rx="6" />
              <text class="pill-txt" x="260" y="1">x402</text>
            </g>
            <!-- nodes -->
            <g>
              <circle class="node-c live" cx="400" cy="106" r="44" />
              <text class="node-ic" x="400" y="106">&#128231;</text>
              <text class="node-lb live" x="400" y="172">Support</text>
              <rect class="pill" x="416" y="64" width="46" height="19" rx="9" />
              <text class="pill-txt" x="439" y="77">LIVE</text>
            </g>
            <g>
              <circle class="node-c" cx="270" cy="200" r="40" />
              <text class="node-ic" x="270" y="200">&#129534;</text>
              <text class="node-lb" x="270" y="262">Billing</text>
            </g>
            <g>
              <circle class="node-c" cx="530" cy="200" r="40" />
              <text class="node-ic" x="530" y="200">&#9881;</text>
              <text class="node-lb" x="530" y="262">Operations</text>
            </g>
            <g>
              <circle class="node-c" cx="320" cy="350" r="40" />
              <text class="node-ic" x="320" y="350">&#128202;</text>
              <text class="node-lb" x="320" y="412">Sales</text>
            </g>
            <g>
              <circle class="node-c" cx="480" cy="350" r="40" />
              <text class="node-ic" x="480" y="350">&#127970;</text>
              <text class="node-lb" x="480" y="412">Vendors</text>
            </g>
          </svg>
        </div>
        <p class="fleet-cap">Each inbox is an <strong>autonomous agent</strong> &mdash; it triages, drafts, and hands work to another inbox over email. <strong>You approve the actions that matter</strong>; agents settle payments agent-to-agent via the <strong>x402 protocol</strong>.</p>
      </div>
      <div class="slide-meta">The Fleet</div><div class="slide-page">04 / 11</div>
    </section>

    <!-- 05 · ANATOMY -->
    <section class="slide" id="s4" aria-label="Anatomy of an inbox agent">
      <div class="ghost-index">04</div>
      <div class="slide-brand"></div>
      <div class="content">
        <div class="eyebrow">Anatomy of an inbox agent</div>
        <h2>Three things make each inbox <span class="em">its own agent.</span></h2>
        <div class="trio">
          <div class="tcard"><div class="ic">📋</div><div class="k">Rules</div><h3>What it handles</h3><p>Plain-language policies that decide what each inbox takes on, how it responds, and when it asks for help.</p></div>
          <div class="tcard"><div class="ic">🛠️</div><div class="k">Tools</div><h3>What it can do</h3><p>Connected actions &mdash; issue a refund, look up an order, query a database, call an API, or hand off to another inbox.</p></div>
          <div class="tcard accent"><div class="ic">🔐</div><div class="k">Permissions</div><h3>What it&rsquo;s allowed</h3><p>Scoped access and approval gates. Auto-send the safe stuff; escalate the rest to a human. Every action is logged.</p></div>
        </div>
      </div>
      <div class="slide-meta">Product</div><div class="slide-page">05 / 11</div>
    </section>

    <!-- TECHNOLOGY · built on Sui -->
    <section class="slide" id="s5" aria-label="Technology">
      <div class="ghost-index">05</div>
      <div class="slide-brand"></div>
      <div class="content">
        <div class="eyebrow">Technology</div>
        <h2>Privacy by architecture &mdash; <span class="em">built on Sui.</span></h2>
        <div class="trio">
          <div class="tcard"><div class="ic">🗄️</div><div class="k">Storage</div><h3>Harbor</h3><p>Decentralized object storage for mailboxes, attachments, and files &mdash; with <strong>SEAL</strong> on-chain encryption and access control built in, so only authorized parties can read your data.</p></div>
          <div class="tcard"><div class="ic">🔑</div><div class="k">Auth</div><h3>zkLogin <span style="font-weight:500; color:var(--text-muted); font-size:.85rem;">by Enoki</span></h3><p>A familiar Web2 sign-in &mdash; your everyday social account, running on Web3 rails. No wallets, seed phrases, or passwords.</p></div>
          <div class="tcard accent"><div class="ic">🧠</div><div class="k">Memory</div><h3>MemWal</h3><p>Keeps each agent&rsquo;s business and knowledge-base context on-chain, so it picks up right where it left off across sessions and runtimes.</p></div>
        </div>
      </div>
      <div class="slide-meta">Technology</div><div class="slide-page">06 / 11</div>
    </section>

    <!-- 06 · WHY NOW -->
    <section class="slide" id="s5" aria-label="Why now">
      <div class="ghost-index">05</div>
      <div class="slide-brand"></div>
      <div class="content">
        <div class="eyebrow">Why now</div>
        <h2>Agents are ready. <span class="em">They just can&rsquo;t talk yet.</span></h2>
        <div class="trio">
          <div class="tcard"><div class="ic">🧠</div><h3>LLMs can finally do the work</h3><p>With tool use and MCP, agents resolve real tasks &mdash; not just chat. The bottleneck is now coordination, not capability.</p></div>
          <div class="tcard"><div class="ic">✉️</div><h3>Email is the agent protocol</h3><p>Async, addressable, auditable, and universal &mdash; every system already speaks it. The natural substrate for agents to coordinate.</p></div>
          <div class="tcard"><div class="ic">🔒</div><h3>Autonomy needs guardrails</h3><p>Permissions, approvals, and privacy are now table stakes. A fleet that acts on your behalf has to be governed and on-infra.</p></div>
        </div>
      </div>
      <div class="slide-meta">Why Now</div><div class="slide-page">06 / 11</div>
    </section>

    <!-- 07 · MARKET -->
    <section class="slide" id="s6" aria-label="Market">
      <div class="ghost-index">06</div>
      <div class="slide-brand"></div>
      <div class="content">
        <div class="eyebrow">Market</div>
        <h2>Land with support. <span class="em">Expand across the org.</span></h2>
        <div class="market-grid">
          <div class="tam-bars">
            <div class="tam">
              <div class="head"><span class="tag">TAM</span><span class="val">$47.8B</span></div>
              <div class="track"><div class="fill" style="width:100%; background:var(--border);"></div></div>
              <div class="note">AI for customer service by 2030 &mdash; the wedge; the fleet expands well beyond it · <a href="https://www.marketsandmarkets.com/PressReleases/ai-for-customer-service.asp" target="_blank" rel="noopener">MarketsandMarkets</a></div>
            </div>
            <div class="tam">
              <div class="head"><span class="tag">SAM</span><span class="val">$1.4B</span></div>
              <div class="track"><div class="fill" style="width:48%; background:rgba(112,238,238,0.5);"></div></div>
              <div class="note">AI support automation for SMBs · <a href="https://dataintelo.com/report/it-help-desk-chatbot-for-smb-market/" target="_blank" rel="noopener">Dataintelo</a></div>
            </div>
            <div class="tam">
              <div class="head"><span class="tag">SOM</span><span class="val accent">$140M</span></div>
              <div class="track"><div class="fill" style="width:18%; background:var(--success-strong);"></div></div>
              <div class="note">3-year obtainable &mdash; ~10% of SMB AI-support (Mermail bottoms-up)</div>
            </div>
          </div>
          <div class="cagr">
            <div class="pct">25.8%</div>
            <p><strong>CAGR, 2024&ndash;2030.</strong> Every new inbox we add to a customer is land-and-expand revenue on top. · <a href="https://www.marketsandmarkets.com/PressReleases/ai-for-customer-service.asp" target="_blank" rel="noopener">MarketsandMarkets, 2025</a></p>
          </div>
        </div>
      </div>
      <div class="slide-meta">Market</div><div class="slide-page">07 / 11</div>
    </section>

    <!-- 08 · WHY WE WIN -->
    <section class="slide" id="s7" aria-label="Why we win">
      <div class="ghost-index">07</div>
      <div class="slide-brand"></div>
      <div class="content">
        <div class="eyebrow">Why we win</div>
        <h2>A point tool is a feature. <span class="em">A fleet is a moat.</span></h2>
        <div class="duo">
          <div class="panel bad">
            <h3>A single-purpose AI tool</h3>
            <ul>
              <li><span class="mark-x">&times;</span> One task, one silo &mdash; no shared context</li>
              <li><span class="mark-x">&times;</span> Suggests; you still do the work</li>
              <li><span class="mark-x">&times;</span> Can&rsquo;t hand off or coordinate</li>
              <li><span class="mark-x">&times;</span> Easy to rip out and replace</li>
            </ul>
          </div>
          <div class="panel good">
            <h3>A Mermail inbox fleet</h3>
            <ul>
              <li><span class="mark-v">&checkmark;</span> Every function gets an agent that acts</li>
              <li><span class="mark-v">&checkmark;</span> Agents share context &amp; hand off over email</li>
              <li><span class="mark-v">&checkmark;</span> Scoped permissions &mdash; fully auditable</li>
              <li><span class="mark-v">&checkmark;</span> Each new inbox deepens the moat &amp; switching cost</li>
            </ul>
          </div>
        </div>
        <div class="banner"><span class="ic">🔗</span><span>The more inboxes you run, the more they coordinate &mdash; <strong style="color:var(--text-primary)">and the harder we are to replace.</strong></span></div>
      </div>
      <div class="slide-meta">Why We Win</div><div class="slide-page">08 / 11</div>
    </section>

    <!-- 09 · BUSINESS MODEL -->
    <section class="slide" id="s8" aria-label="Business model">
      <div class="ghost-index">08</div>
      <div class="slide-brand"></div>
      <div class="content">
        <div class="eyebrow">Business model</div>
        <h2>Subscription <span class="em">per inbox.</span></h2>
        <div class="tiers">
          <div class="tier"><div class="k">Starter</div><h3>Your first inbox</h3><p>One agentic inbox (start with Support) · rules, tools &amp; human approval.</p></div>
          <div class="tier hot"><div class="k">Growth · Most popular</div><h3>A small fleet</h3><p>Multiple inboxes · inter-agent handoff · auto-send · permissions &amp; analytics.</p></div>
          <div class="tier"><div class="k">Scale</div><h3>Org-wide fleet</h3><p>Unlimited inboxes · SSO · dedicated isolation · SLA &amp; DPA · audit &amp; priority support.</p></div>
        </div>
        <div class="banner"><span class="ic">📈</span><span>Land with one inbox, expand to a fleet &mdash; revenue grows with <strong style="color:var(--text-primary)">the fleet, not your headcount.</strong></span></div>
      </div>
      <div class="slide-meta">Business Model</div><div class="slide-page">09 / 11</div>
    </section>

    <!-- 10 · TRACTION -->
    <section class="slide" id="s9" aria-label="Traction">
      <div class="ghost-index">09</div>
      <div class="slide-brand"></div>
      <div class="content">
        <div class="eyebrow">Traction</div>
        <h2><span class="em">First agent is live</span> &mdash; the fleet is next.</h2>
        <div class="tl">
          <div class="mile done"><div class="dot"></div><div class="date">Apr 2026</div><h3>Started</h3><p>Validated the wedge: SMB support is expensive to staff and impossible to scale 24/7.</p></div>
          <div class="mile done"><div class="dot"></div><div class="date">May 2026</div><h3>Built MVP</h3><p>Our own mail server + an agentic inbox: rules, tools, and human-in-the-loop approval.</p></div>
          <div class="mile now"><div class="dot"></div><div class="date">Now · Jun 2026</div><h3>Support inbox live</h3><p>mermail.app is live with early users on the first agent &mdash; gathering signal.</p></div>
          <div class="mile"><div class="dot"></div><div class="date">Q3 2026</div><h3>Fleet + revenue</h3><p>Ship inter-agent handoff, convert design partners to paid, start SOC&nbsp;2.</p></div>
        </div>
      </div>
      <div class="slide-meta">Traction</div><div class="slide-page">10 / 11</div>
    </section>

    <!-- 11 · TEAM + ASK -->
    <section class="slide" id="s10" aria-label="Team and ask">
      <div class="ghost-index">10</div>
      <div class="slide-brand"></div>
      <div class="content">
        <div class="eyebrow">Team</div>
        <h2>Operators who <span class="em">ship.</span></h2>
        <div class="team">
          <div class="member"><img src="{NATHAN}" alt="Nathan Nguyen" /><div><h3>Nathan Nguyen</h3><div class="role">Co-founder</div><p>Data Scientist at Webjet.com.au · MSc Data Science, Deakin. AI workflow &amp; product validation.</p></div></div>
          <div class="member"><img src="{TOAN}" alt="Toan Nhu" /><div><h3>Toan Nhu</h3><div class="role">Co-founder</div><p>Co-founder of Nimbus · Principal Engineer at VinGroup · ex Senior Data Engineer at Tiki.</p></div></div>
        </div>
        <div class="vision">
          <p class="q">&ldquo;Every business runs on inboxes. We&rsquo;re giving each one an agent &mdash; and a fleet that runs itself.&rdquo;</p>
          <div class="contact">
            <a href="mailto:contact@mermail.app">✉ contact@mermail.app</a>
            <a href="https://mermail.app" target="_blank" rel="noopener">🌐 mermail.app</a>
          </div>
        </div>
      </div>
      <div class="slide-meta">Team</div><div class="slide-page">11 / 11</div>
    </section>

  </div>

  <nav class="nav" aria-label="Slide navigation">
    <button class="nav-btn" id="prevBtn" aria-label="Previous slide">&larr;</button>
    <div class="dots" id="dots" role="tablist"></div>
    <button class="nav-btn" id="nextBtn" aria-label="Next slide">&rarr;</button>
  </nav>

  <script>
    const slides = Array.from(document.querySelectorAll('.slide'));
    const dotsEl = document.getElementById('dots');
    const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const hash = window.location.hash.match(/^#s(\\d+)$/);
    let cur = hash ? Math.min(Math.max(+hash[1], 0), slides.length - 1) : 0;
    slides.forEach((s, i) => s.classList.toggle('active', i === cur));

    slides.forEach((_, i) => {{
      const d = document.createElement('button');
      d.className = 'dot' + (i === cur ? ' active' : '');
      d.setAttribute('role', 'tab');
      d.setAttribute('aria-label', 'Slide ' + (i + 1));
      d.addEventListener('click', () => goTo(i));
      dotsEl.appendChild(d);
    }});

    const STAGGER = ['.eyebrow','h1','h2','.lede','.statement','.cstat','.row','.fleet-stage','.fleet-cap','.tcard','.tam','.cagr','.panel','.banner','.tier','.mile','.member','.ask-amt','.ask-sub','.fund','.vision'];

    function items(el) {{
      const seen = new Set(), out = [];
      STAGGER.forEach(sel => el.querySelectorAll(sel).forEach(n => {{ if (!seen.has(n)) {{ seen.add(n); out.push(n); }} }}));
      return out;
    }}

    function play(el) {{
      if (reduced) return;
      const list = items(el);
      list.forEach(n => {{ n.style.opacity = '0'; n.style.transform = 'translateY(16px)'; n.style.transition = 'none'; }});
      requestAnimationFrame(() => requestAnimationFrame(() => {{
        list.forEach((n, i) => {{
          const d = 50 + i * 55;
          n.style.transition = `opacity .42s ease ${{d}}ms, transform .42s ease ${{d}}ms`;
          n.style.opacity = '1'; n.style.transform = 'translateY(0)';
        }});
      }}));
      el.querySelectorAll('.fill').forEach(f => {{
        const w = f.style.width; f.style.width = '0'; f.style.transition = 'none';
        requestAnimationFrame(() => requestAnimationFrame(() => {{
          f.style.transition = 'width .9s cubic-bezier(0.16,1,0.3,1) 350ms'; f.style.width = w;
        }}));
      }});
    }}

    function reset(el) {{
      if (reduced) return;
      items(el).forEach(n => {{ n.style.opacity = n.style.transform = n.style.transition = ''; }});
    }}

    function goTo(n) {{
      reset(slides[cur]);
      slides[cur].classList.remove('active');
      slides[cur].classList.add('prev');
      const prev = cur;
      setTimeout(() => slides[prev].classList.remove('prev'), 500);
      cur = (n + slides.length) % slides.length;
      slides[cur].classList.add('active');
      window.location.hash = 's' + cur;
      document.querySelectorAll('.dot').forEach((d, i) => d.classList.toggle('active', i === cur));
      setTimeout(() => play(slides[cur]), 60);
    }}

    document.getElementById('nextBtn').addEventListener('click', () => goTo(cur + 1));
    document.getElementById('prevBtn').addEventListener('click', () => goTo(cur - 1));
    document.addEventListener('keydown', e => {{
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === ' ') {{ e.preventDefault(); goTo(cur + 1); }}
      if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') goTo(cur - 1);
    }});
    let tx = 0;
    document.addEventListener('touchstart', e => tx = e.touches[0].clientX, {{ passive: true }});
    document.addEventListener('touchend', e => {{
      const dx = e.changedTouches[0].clientX - tx;
      if (Math.abs(dx) > 48) goTo(dx < 0 ? cur + 1 : cur - 1);
    }}, {{ passive: true }});

    setTimeout(() => play(slides[cur]), 120);
  </script>
</body>
</html>
"""

def renumber(html: str) -> str:
    """Auto-number slides by document order: section id (sN), ghost-index, and
    'NN / total' page labels. Lets slides be added/removed without hand-numbering."""
    starts = [m.start() for m in re.finditer(r'<section class="slide', html)]
    total = len(starts)
    bounds = starts + [len(html)]
    out = [html[:starts[0]]]
    for i in range(total):
        block = html[bounds[i]:bounds[i + 1]]
        block = re.sub(r'(<section class="slide[^"]*" id=")s\d+(")', rf'\g<1>s{i}\g<2>', block, count=1)
        block = re.sub(r'(<div class="ghost-index">)\d+(</div>)', rf'\g<1>{i:02d}\g<2>', block, count=1)
        block = re.sub(r'(<div class="slide-page">)[^<]*(</div>)', rf'\g<1>{i + 1:02d} / {total}\g<2>', block, count=1)
        out.append(block)
    return ''.join(out)


HTML = renumber(HTML)

OUT = ROOT / "mermail-yc-deck.html"
OUT.write_text(HTML)
print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB)")
