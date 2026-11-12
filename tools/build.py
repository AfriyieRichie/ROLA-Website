"""Builds the River of Life Academy pages.

Run:  python tools/build.py
It rewrites index.html and the section pages from the shared pieces below
(header, menu, footer), so a change made here appears on every page.
Editing the generated .html files directly also works, but will be
overwritten the next time this script runs.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Numbers as printed on the school's "Admission in Progress" flyer
PHONE_DISPLAY = "0243 334 846"
PHONE_LINK = "+233243334846"
PHONE2_DISPLAY = "0540 570 330"
PHONE2_LINK = "+233540570330"
EMAIL = "info@riveroflifeacademy.edu.gh"
MAPS = "https://maps.app.goo.gl/BwdagYMMDPkHuo2j6"
INSTAGRAM = "https://www.instagram.com/rola_school/"

CREST = '<img class="wordmark__crest" src="images/site/crest.png" alt="" width="56" height="56" />'


def head(title, desc):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta name="theme-color" content="#0b1b4a" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:type" content="website" />
  <meta property="og:image" content="images/site/hero-1.jpg" />
  <link rel="icon" href="images/favicon.png" type="image/png" />
  <script>document.documentElement.className += " js";</script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/styles.css" />
  <link rel="stylesheet" href="css/experience.css" />
  <link rel="stylesheet" href="css/pages.css" />
  <noscript><style>.cover,.veil{{display:none!important}}body.is-cover{{overflow:auto!important}}.reveal{{opacity:1!important;transform:none!important}}</style></noscript>
</head>
'''


VEIL = '''<div class="veil" aria-hidden="true"><img src="images/site/crest.png" alt="" width="120" height="120" /></div>
<div class="topfade" aria-hidden="true"></div>
'''


def header(home):
    home_href = "#top" if home else "index.html"
    return f'''<header class="header" id="header">
  <a href="{home_href}" class="wordmark" aria-label="River of Life Academy, home">{CREST}<span>River of<br/>Life<br/>Academy</span></a>
  <nav class="pillnav" aria-label="Quick links">
    <a href="contact.html#visit">Book a Visit</a>
    <a href="admissions.html">Admissions</a>
    <a href="admissions.html#dates">Term Dates</a>
    <a href="school-life.html">School Life</a>
    <a href="contact.html">Contact Us</a>
  </nav>
  <button class="menu-btn" id="menuBtn" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="menu"><span></span><span></span></button>
</header>
'''


MENU = f'''<div class="menu" id="menu" aria-hidden="true">
  <div class="menu__grid">
    <div class="menu__left">
      <img class="menu__crest" src="images/site/crest.png" alt="River of Life Academy crest" width="104" height="104" />
      <p class="menu__name">River of Life Academy</p>
      <p class="menu__label">Useful links</p>
      <a href="index.html">Home</a>
      <a href="contact.html#visit">Book a Visit</a>
      <a href="admissions.html">Admissions</a>
      <a href="admissions.html#dates">Term Dates</a>
      <a href="contact.html">Contact Us</a>
      <p class="menu__label">Call us</p>
      <a href="tel:{PHONE_LINK}">{PHONE_DISPLAY}</a>
      <a href="tel:{PHONE2_LINK}">{PHONE2_DISPLAY}</a>
    </div>
    <nav class="menu__main" aria-label="Main menu">
      <a href="our-school.html" data-sub="about" data-img="images/site/hero-1.jpg" class="is-on"><span><small>01</small>Our School</span><i class="arrow" aria-hidden="true"></i></a>
      <a href="learning.html" data-sub="learning" data-img="images/site/primary.jpg"><span><small>02</small>Learning</span><i class="arrow" aria-hidden="true"></i></a>
      <a href="school-life.html" data-sub="life" data-img="images/site/hero-3.jpg"><span><small>03</small>School Life</span><i class="arrow" aria-hidden="true"></i></a>
      <a href="admissions.html" data-sub="admissions" data-img="images/site/h-class.jpg"><span><small>04</small>Admissions</span><i class="arrow" aria-hidden="true"></i></a>
      <a href="moments.html" data-sub="moments" data-img="images/site/g-ucmas-team.jpg"><span><small>05</small>Moments</span><i class="arrow" aria-hidden="true"></i></a>
      <a href="contact.html" data-sub="contact" data-img="images/site/g-houses.jpg"><span><small>06</small>Contact Us</span><i class="arrow" aria-hidden="true"></i></a>
    </nav>
    <div class="menu__sub">
      <div data-for="about" class="is-on"><a href="our-school.html">Who We Are</a><a href="our-school.html#motto">Our Motto</a><a href="our-school.html#principal">A Word from our Principals</a><a href="our-school.html#people">Our People</a><a href="our-school.html#campus">Our Campus</a></div>
      <div data-for="learning"><a href="learning.html#creche">Creche &amp; Nursery</a><a href="learning.html#kindergarten">Kindergarten</a><a href="learning.html#primary">Primary School</a><a href="learning.html#jhs">Junior High School</a><a href="learning.html#curriculum">What We Teach</a></div>
      <div data-for="life"><a href="school-life.html#calendar">Through the Year</a><a href="moments.html">Photo Gallery</a></div>
      <div data-for="admissions"><a href="admissions.html#apply">How to Apply</a><a href="admissions.html#bring">What to Bring</a><a href="admissions.html#dates">Term Dates</a><a href="contact.html#visit">Book a Visit</a></div>
      <div data-for="moments"><a href="moments.html">Photo Gallery</a><a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a></div>
      <div data-for="contact"><a href="contact.html">Get in Touch</a><a href="{MAPS}" target="_blank" rel="noopener">Get Directions</a><a href="contact.html#visit">Send a Message</a></div>
      <figure class="menu__photo"><img id="menuPhoto" src="images/site/hero-1.jpg" alt="" /></figure>
    </div>
    <div class="menu__foot">
      <a href="#">Facebook</a>
      <a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a>
      <a href="https://wa.me/{PHONE_LINK.lstrip('+')}" target="_blank" rel="noopener">WhatsApp</a>
      <a href="#" id="replayIntro">Welcome screen</a>
      <span>Devotion and Service</span>
    </div>
  </div>
</div>
'''

FOOTER = f'''<footer class="footer">
  <div class="wrap footer__cards">
    <a href="admissions.html" class="fcard">
      <img src="images/site/g-art2.jpg" alt="" loading="lazy" />
      <div><h2>Begin your journey</h2><p>Explore our admissions process and take the next step with confidence.</p><span class="btn btn--light">Admissions <i aria-hidden="true"></i></span></div>
    </a>
    <a href="contact.html#visit" class="fcard">
      <img src="images/site/g-culture2.jpg" alt="" loading="lazy" />
      <div><h2>Book a visit</h2><p>Walk through our classrooms, meet our teachers and discover what makes ROLA special.</p><span class="btn btn--light">Visits <i aria-hidden="true"></i></span></div>
    </a>
  </div>
  <div class="wrap footer__bottom">
    <p class="wordmark wordmark--footer">{CREST}<span>River of<br/>Life<br/>Academy</span></p>
    <p class="footer__motto">Devotion and Service</p>
    <nav class="footer__links" aria-label="Social">
      <a href="#">Facebook</a>
      <a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a>
      <a href="https://wa.me/{PHONE_LINK.lstrip('+')}" target="_blank" rel="noopener">WhatsApp</a>
    </nav>
    <p class="footer__copy">All rights reserved. &copy; <span id="year">2026</span> River of Life Academy, Accra</p>
  </div>
</footer>

<div class="lightbox" id="lightbox" aria-hidden="true">
  <button class="lightbox__close" type="button" aria-label="Close">Close</button>
  <img alt="" />
  <p></p>
</div>

<script src="js/site.js"></script>
<script src="js/main.js"></script>
</body>
</html>
'''

COVER = '''<div class="cover is-intro" id="cover" aria-label="Welcome">
  <!-- Stage 1: opening photo (or images/site/hero.mp4 if present) with the motto -->
  <div class="cover__intro" id="coverIntro">
    <img src="images/site/hero-1.jpg" alt="" />
    <video id="introVideo" muted loop playsinline preload="none" aria-hidden="true"></video>
  </div>
  <!-- Stage 2: the globe.  Stage 3: the same tiles laid out as a wall you can drag around -->
  <div class="globe" id="globe"><div class="globe__sphere" id="sphere"></div></div>
  <div class="cover__shade" aria-hidden="true"></div>
  <div class="cover__center">
    <p class="cover__title">Devotion and Service</p>
    <button class="cover__go" id="coverGo" type="button">Continue</button>
  </div>
  <p class="cover__hint" id="coverHint" aria-hidden="true">Drag to explore</p>
  <div class="wallbar" id="wallbar">
    <div class="pick" id="pickPersona">
      <div class="pick__list" role="listbox" aria-label="I am a"></div>
      <button type="button" class="pick__btn" aria-haspopup="listbox"><span>I am a</span> <strong>New Parent</strong></button>
    </div>
    <button type="button" class="wallbar__globe" id="backToGlobe" aria-label="Back to the globe"></button>
    <div class="pick pick--right" id="pickTopic">
      <div class="pick__list" role="listbox" aria-label="Exploring"></div>
      <button type="button" class="pick__btn" aria-haspopup="listbox"><span>Exploring</span> <strong>Everything</strong></button>
    </div>
    <button type="button" class="wallbar__enter" id="enterSite">Enter website</button>
  </div>
</div>

<div class="sheet" id="sheet" aria-hidden="true" role="dialog" aria-modal="true" aria-labelledby="sheetTitle">
  <div class="sheet__scroll" id="sheetScroll">
    <article class="sheet__panel">
      <p class="sheet__label" id="sheetLabel"></p>
      <h2 class="sheet__title" id="sheetTitle"></h2>
      <img class="sheet__img" id="sheetImg" alt="" />
      <p class="sheet__text" id="sheetText"></p>
    </article>
  </div>
  <button type="button" class="sheet__close" id="sheetClose" aria-label="Close">&times;</button>
  <button type="button" class="sheet__full" id="sheetFull"><i aria-hidden="true"></i>Full page</button>
</div>
'''

# ------------------------------------------------------------------ blocks

def photo_hero(title, img, alt, pos="center 40%"):
    return f'''  <section class="phero">
    <img class="phero__img" data-parallax src="{img}" alt="{alt}" style="object-position:{pos}" />
    <div class="phero__shade" aria-hidden="true"></div>
    <h1 class="phero__title">{title}</h1>
  </section>
'''


def plain_hero(title, sub=""):
    sub_html = f'\n    <p class="phero__sub">{sub}</p>' if sub else ""
    return f'''  <section class="phero phero--plain">
    <h1 class="phero__title">{title}</h1>{sub_html}
  </section>
'''


def statement(label, lead, paras, button=""):
    body = "".join(f"<p>{p}</p>" for p in paras)
    return f'''  <section class="section statement">
    <div class="wrap">
      <p class="eyebrow">{label}</p>
      <div class="intro__grid">
        <p class="lead reveal">{lead}</p>
        <div class="intro__body reveal">{body}{button}</div>
      </div>
    </div>
  </section>
'''


def btn(text, href, light=False):
    cls = "btn btn--light" if light else "btn"
    return f'<a href="{href}" class="{cls}">{text} <i aria-hidden="true"></i></a>'


def split(anchor, label, title, paras, img, alt, flip=False, points=None, button="", shape="wide", pos="center 25%"):
    body = "".join(f"<p>{p}</p>" for p in paras)
    pts = ""
    if points:
        pts = '<ul class="dots">' + "".join(f"<li>{p}</li>" for p in points) + "</ul>"
    cls = "split split--flip" if flip else "split"
    return f'''  <section class="section {cls}" id="{anchor}">
    <div class="wrap split__grid">
      <figure class="split__media split__media--{shape} reveal"><img src="{img}" alt="{alt}" loading="lazy" style="object-position:{pos}" /></figure>
      <div class="split__text reveal">
        <p class="eyebrow">{label}</p>
        <h2>{title}</h2>
        {body}{pts}{button}
      </div>
    </div>
  </section>
'''


def rlist(anchor, label, title, intro, rows):
    """Expanding list with a photo that changes with the open row. rows: (title, text, img)"""
    out = []
    for i, row in enumerate(rows):
        t, text, img = row[:3]
        pos = row[3] if len(row) > 3 else "center 25%"
        open_cls = " is-open" if i == 0 else ""
        out.append(f'''          <div class="rlist__row{open_cls}" data-img="{img}" data-pos="{pos}">
            <button type="button" class="rlist__head" aria-expanded="{'true' if i == 0 else 'false'}"><span>{i + 1:02d}</span>{t}<i aria-hidden="true"></i></button>
            <div class="rlist__body"><p>{text}</p></div>
          </div>''')
    return f'''  <section class="section rlist-section" id="{anchor}">
    <div class="wrap">
      <div class="rlist__intro reveal">
        <p class="eyebrow">{label}</p>
        <h2>{title}</h2>
        <p>{intro}</p>
      </div>
      <div class="rlist" data-rlist>
        <figure class="rlist__media"><img src="{rows[0][2]}" alt="" style="object-position:{rows[0][3] if len(rows[0]) > 3 else 'center 25%'}" /></figure>
        <div class="rlist__rows">
{chr(10).join(out)}
        </div>
      </div>
    </div>
  </section>
'''


def banner(title, text, button, img="images/site/stats.jpg", alt="", pos="center 50%"):
    return f'''  <section class="banner">
    <img src="{img}" alt="{alt}" loading="lazy" style="object-position:{pos}" />
    <div class="banner__shade" aria-hidden="true"></div>
    <div class="banner__text reveal">
      <h2>{title}</h2>
      <p>{text}</p>
      {button}
    </div>
  </section>
'''


def get_in_touch(img="images/site/g-games.jpg", pos="center 50%"):
    return f'''  <section class="section gin-section">
    <div class="wrap">
      <div class="gin reveal">
        <img src="{img}" alt="" loading="lazy" style="object-position:{pos}" />
        <div class="gin__card">
          <h2>Get in touch</h2>
          <p>From questions about admissions and fees to booking a visit, our team is happy to help.</p>
          <a href="contact.html" class="gin__btn">Contact us <i class="arrow" aria-hidden="true"></i></a>
        </div>
      </div>
    </div>
  </section>
'''


def explore(cards):
    items = "".join(
        f'<a href="{href}" class="card reveal"><span class="card__label">{label}</span><span class="card__title">{title}</span><i class="arrow" aria-hidden="true"></i></a>'
        for label, title, href in cards)
    return f'''  <section class="section explore">
    <div class="wrap">
      <p class="eyebrow">Keep exploring</p>
      <div class="explore__grid">{items}</div>
    </div>
  </section>
'''


SHOTS = [
    ("g-teachers-parents", "Teachers and parents, 20th Graduation"), ("g-craft-1", "Projects made with our parents"), ("principal-pupils", "With our Principal"),
    ("g-culture-pair", "Cultural Day"), ("g-craft-table", "Craft work"), ("g-craft-5", "A model home"),
    ("g-grad-cake", "20th Graduation celebration"), ("g-craft-2", "Family projects"), ("g-art-display", "Art on show"),
    ("g-culture-kente", "Cultural Day"), ("g-care", "A helping hand"), ("g-craft-3", "Proud of her work"),
    ("g-craft-4", "Built together"), ("g-craft-6", "Family projects"), ("g-pool", "Excursion: pool day"),
    ("g-ucmas", "UCMAS National Competition"), ("g-oldschool", "Old School Day"), ("g-art", "Creativity is the Point"),
    ("g-culture", "Cultural Day"), ("g-graduation", "Graduation Day"), ("g-trip-lunch", "Excursion: lunch together"),
    ("g-pe", "Morning exercise"), ("g-grads", "Graduating class"), ("g-pink", "Pink October"),
    ("g-class-portrait", "Proud to be ROLA"), ("g-trip-play", "Excursion: playtime"), ("g-graduation2", "Our graduates"),
    ("g-games", "Games day"), ("g-christmas", "Christmas at ROLA"), ("g-trophy", "Champions"),
    ("g-cooking", "Life skills day"), ("g-retro", "Old School Day"),
    ("g-uniform", "Friends for life"), ("h-class", "Our seniors"),
    ("g-ucmas-team", "UCMAS competition team"), ("g-graduation-principal", "Graduation with our Principal"),
    ("g-houses", "House colours"), ("g-winners", "Trophy winners"),
]


def shots(items):
    return "\n".join(
        f'        <button type="button" class="shot"><img src="images/site/{f}.jpg" alt="School photo: {cap}" loading="lazy" /><span>{cap}</span></button>'
        for f, cap in items)


# ------------------------------------------------------------------ pages

def page_home():
    stages = [
        ("creche", "nursery.jpg", "Ages 1 to 3", "Creche &amp; Nursery", "A gentle, safe start where little ones play, sing, explore and make their first friends."),
        ("kindergarten", "kg.jpg", "KG 1 and KG 2", "Kindergarten", "Phonics, early reading, number work and creative play that prepare children for primary school."),
        ("primary", "primary.jpg", "Basic 1 to 6", "Primary School", "Strong foundations in literacy, numeracy and science, alongside the creative arts."),
        ("jhs", "jhs.jpg", "JHS 1 to 3", "Junior High School", "Focused teaching, mentoring and BECE preparation for confident young people."),
    ]
    stage_html = "".join(f'''      <a class="stage" href="learning.html#{a}">
        <img src="images/site/{img}" alt="" loading="lazy" />
        <div class="stage__text"><p class="eyebrow">{age}</p><h3>{t}</h3><p>{d}</p></div>
      </a>
''' for a, img, age, t, d in stages)
    return f'''<main id="top">
  <section class="hero">
    <!-- Background photos change automatically. To use a video instead, save it as images/site/hero.mp4 -->
    <div class="hero__slides" id="heroSlides" data-parallax>
      <!-- The nine photos from the "Background changing pictures" folder -->
      <img class="is-active" src="images/site/principal-children.jpg" alt="Rev. S. Twumasi-Ankra Bonsu seated among pupils of River of Life Academy" style="object-position:center 0%" />
      <img src="images/site/g-teachers-parents.jpg" alt="" style="object-position:center 14%" />
      <img src="images/site/g-craft-table.jpg" alt="" style="object-position:center 22%" />
      <img src="images/site/g-team-staff.jpg" alt="" style="object-position:center 38%" />
      <img src="images/site/g-art.jpg" alt="" style="object-position:center 36%" />
      <img src="images/site/principal-pupils.jpg" alt="" style="object-position:center 14%" />
      <img src="images/site/g-grad-cake.jpg" alt="" style="object-position:center 40%" />
      <img src="images/site/g-pink.jpg" alt="" style="object-position:center 18%" />
      <img src="images/site/g-pe2.jpg" alt="" style="object-position:center 38%" />
    </div>
    <video class="hero__video" id="heroVideo" muted loop playsinline preload="none" aria-hidden="true"></video>
    <div class="hero__shade" aria-hidden="true"></div>
    <span class="hero__scroll" aria-hidden="true">Scroll</span>
    <h1 class="hero__title">River of Life Academy</h1>
  </section>

{statement("Welcome", "Choosing a school is one of the biggest decisions a family makes. At River of Life Academy, your child is known, taught well and cared for, from the first day of Creche to the last day of Junior High.",
           ["We are a basic school in Accra, guided by our motto, <em>Devotion and Service</em>. Our teachers are devoted to every learner, and our pupils learn to serve their school, their families and their community."],
           btn("Our School", "our-school.html"))}
  <section class="section learning" id="learning">
    <div class="wrap learning__head">
      <div class="reveal"><p class="eyebrow">Creche to JHS, one school</p><h2>Explore learning at ROLA</h2></div>
      <div class="controls">
        <button type="button" class="round" id="slidePrev" aria-label="Previous"><i class="arrow arrow--left"></i></button>
        <button type="button" class="round" id="slideNext" aria-label="Next"><i class="arrow"></i></button>
      </div>
    </div>
    <div class="slider" id="slider">
{stage_html}    </div>
  </section>

  <section class="section welcome">
    <div class="wrap welcome__grid">
      <figure class="welcome__photo reveal"><img src="images/site/principals.jpg" alt="Rev. S. Twumasi-Ankra Bonsu and Mrs. Tina Bonsu, Principals of River of Life Academy" loading="lazy" style="object-position:center 22%" /></figure>
      <div class="reveal">
        <p class="eyebrow eyebrow--gold">A word from our Principals</p>
        <blockquote>Every child is a gift. Our work is to help each one discover what they can do, and to use it in the service of others.</blockquote>
        <p class="welcome__sign">Rev. S. Twumasi-Ankra Bonsu &amp; Mrs. Tina Bonsu<span>Principals, River of Life Academy</span></p>
        <p class="welcome__more">{btn("Read their welcome", "our-school.html#principal", light=True)}</p>
      </div>
    </div>
  </section>

  <section class="section moments moments--teaser">
    <div class="wrap">
      <div class="moments__head reveal">
        <div><p class="eyebrow eyebrow--gold">Moments</p><h2>Life at River of Life</h2></div>
        {btn("See all moments", "moments.html", light=True)}
      </div>
      <div class="grid" id="gallery">
{shots(SHOTS[:6])}
      </div>
    </div>
  </section>

{banner("Experience ROLA firsthand", "The best way to understand our school is to visit. See learning in action, meet our teachers and walk through our campus.", btn("Book a visit today", "contact.html#visit", light=True), alt="ROLA pupils gathered in the school courtyard")}
{explore([("Admissions", "How to Apply", "admissions.html"), ("School Life", "Through the Year", "school-life.html"), ("Admissions", "Term Dates", "admissions.html#dates")])}</main>
'''


def page_our_school():
    return f'''<main id="top">
{photo_hero("Our School", "images/site/hero-1.jpg", "Pupils of River of Life Academy in front of the school building")}
{statement("Who we are", "River of Life Academy is a basic school in Accra where children are known, taught well and cared for, from Creche to Junior High.",
           ["We follow the Ghana Education Service curriculum and bring it to life through the arts, mental arithmetic, sport, culture and a full calendar of school events.",
            "Our school is a family. Pupils are encouraged, corrected with care and celebrated, and parents are partners in everything we do."])}
  <section class="section motto" id="motto">
    <div class="wrap">
      <p class="eyebrow eyebrow--gold">Our motto</p>
      <h2 class="reveal">Devotion and Service</h2>
      <div class="motto__grid">
        <div class="reveal"><h3>Devotion</h3><p>Our teachers are devoted to every learner. We ask the same of our pupils: to give their best to their studies, to their faith and to one another.</p></div>
        <div class="reveal"><h3>Service</h3><p>Learning is not only for ourselves. Our pupils learn to serve their school, their families and their community, and to lead by helping others.</p></div>
      </div>
    </div>
  </section>

  <section class="section principal" id="principal">
    <div class="wrap split__grid">
      <figure class="split__media split__media--framed reveal"><img src="images/site/principals.jpg" alt="Rev. S. Twumasi-Ankra Bonsu and Mrs. Tina Bonsu, Principals of River of Life Academy" loading="lazy" style="object-position:center 22%" /></figure>
      <div class="split__text reveal">
        <p class="eyebrow">A word from our Principals</p>
        <blockquote class="quote">Every child is a gift. Our work is to help each one discover what they can do, and to use it in the service of others.</blockquote>
        <p>At River of Life Academy we believe a good education shapes both the mind and the heart. Our classrooms are places of hard work and high expectations, and our school is a family where pupils are encouraged, corrected with care and celebrated.</p>
        <p>We warmly invite you to visit, meet our teachers and see our pupils at work.</p>
        <p class="sign">Rev. S. Twumasi-Ankra Bonsu &amp; Mrs. Tina Bonsu<span>Principals, River of Life Academy</span></p>
      </div>
    </div>
  </section>

{split("everyday", "Every day", "At the heart of school life", ["Our Principals are part of school life every day, and our pupils know them well."], "images/site/principal-children.jpg", "Rev. S. Twumasi-Ankra Bonsu seated among pupils of the school", pos="center 50%")}
{split("administrator", "School Administrator", "Mrs. Lilly Ofori-Asante", ["Mrs. Lilly Ofori-Asante is the Administrator of River of Life Academy. She leads the school office, and is glad to help parents with admissions, fees and day-to-day questions."], "images/site/administrator.jpg", "Mrs. Lilly Ofori-Asante, Administrator of River of Life Academy", flip=True, shape="tall", pos="center 20%", button=btn("Contact the school office", "contact.html"))}
  <section class="section people" id="people">
    <div class="wrap">
      <div class="people__head reveal"><p class="eyebrow">Our people</p><h2>Teachers and parents, together</h2><p>Our teachers and parents work side by side for our pupils. Here they are at our 20th graduation celebration.</p></div>
      <figure class="people__photo reveal"><img src="images/site/g-teachers-parents.jpg" alt="Teachers and parents of River of Life Academy on stage at the 20th graduation" loading="lazy" /><figcaption>Teachers and parents at the 20th ROLA Graduation</figcaption></figure>
    </div>
  </section>

{split("campus", "Our campus", "A bright, welcoming home in Accra", ["Our green school building is easy to spot. Its courtyard is the heart of the school, where pupils gather for assembly, exercise and celebrations through the year."], "images/site/stats.jpg", "Pupils gathered in the school courtyard", flip=True, button=f'<a href="{MAPS}" target="_blank" rel="noopener" class="btn">Get directions <i aria-hidden="true"></i></a>')}
{get_in_touch()}
{explore([("Learning", "Creche to Junior High", "learning.html"), ("School Life", "Through the Year", "school-life.html"), ("Admissions", "How to Apply", "admissions.html")])}</main>
'''


def page_learning():
    return f'''<main id="top">
{photo_hero("Learning", "images/site/primary.jpg", "Primary pupils stretching during a physical education session", "center 30%")}
{statement("Creche to JHS, one school", "One school for every stage, from a child&rsquo;s first days in Creche to the BECE in Junior High.",
           ["Each stage builds on the one before it, so pupils grow in confidence with teachers who already know them.",
            "We follow the Ghana Education Service curriculum throughout."])}
{split("creche", "Ages 1 to 3", "Creche &amp; Nursery", ["A gentle, safe start where our youngest pupils play, sing, explore and make their first friends."], "images/site/nursery.jpg", "Our youngest pupils in uniform with their backpacks", shape="tall", pos="center 30%", points=["Caring, attentive staff", "Learning through play, songs and stories", "First words, numbers and routines"])}
{split("kindergarten", "KG 1 and KG 2", "Kindergarten", ["Joyful, structured learning that prepares children for primary school."], "images/site/kg.jpg", "Kindergarten pupils at assembly", flip=True, shape="square", pos="center 50%", points=["Phonics and early reading", "Number work", "Creative play and social skills"])}
{split("primary", "Basic 1 to 6", "Primary School", ["Six years of strong foundations, taught with care and high expectations."], "images/site/g-craft-table.jpg", "Primary pupils showing their craft work at a table", shape="wide", pos="center 50%", points=["Literacy and numeracy every day", "Science and computing", "Creative arts, sport and mental arithmetic"])}
{split("jhs", "JHS 1 to 3", "Junior High School", ["Focused teaching and mentoring for confident, well-rounded young people, leading to the Basic Education Certificate Examination."], "images/site/jhs.jpg", "Junior High students presenting their paintings", flip=True, shape="square", pos="center 30%", points=["Subject teaching across the JHS curriculum", "BECE preparation", "Leadership and service"])}
  <section class="section facts-section" id="curriculum">
    <div class="wrap life__grid">
      <div class="life__intro reveal"><p class="eyebrow">Curriculum</p><h2>What we teach</h2><p>Our teaching follows the Ghana Education Service curriculum, with these areas running through every stage.</p></div>
      <div class="table reveal">
        <div class="table__row"><h3>Literacy &amp; Languages</h3><p>Reading, writing, speaking and listening.</p></div>
        <div class="table__row"><h3>Numeracy</h3><p>Mathematics, strengthened by mental arithmetic.</p></div>
        <div class="table__row"><h3>Science &amp; Computing</h3><p>Understanding the world and the tools we use in it.</p></div>
        <div class="table__row"><h3>Our World</h3><p>History, society, and religious and moral education.</p></div>
        <div class="table__row"><h3>Creative Arts</h3><p>Painting, drawing, craft, music and performance.</p></div>
        <div class="table__row"><h3>Physical Education</h3><p>Exercise, games and inter-house sport.</p></div>
      </div>
    </div>
  </section>

{banner("See learning in action", "Visit us on a school day and sit in on the life of our classrooms.", btn("Book a visit", "contact.html#visit", light=True), "images/site/g-houses.jpg", pos="center 45%")}
{explore([("Admissions", "How to Apply", "admissions.html"), ("School Life", "Through the Year", "school-life.html"), ("Our School", "Our Motto", "our-school.html#motto")])}</main>
'''


def page_school_life():
    rows = [
        ("Creative Arts", "Painting, drawing and craft, shown each year at our art exhibition, &ldquo;Creativity is the Point&rdquo;.", "images/site/g-art.jpg", "32% 25%"),
        ("Family Projects", "Pupils build models and crafts together with their parents, then present them at school.", "images/site/g-craft-1.jpg", "center 40%"),
        ("Mental Arithmetic", "Our UCMAS team trains through the year and has brought home trophies from the national competition.", "images/site/g-ucmas-trophies.jpg"),
        ("Sport &amp; Fitness", "Morning exercise, physical education, games and inter-house competitions.", "images/site/g-pe.jpg"),
        ("Cultural Day", "A celebration of Ghanaian heritage, when pupils and teachers come to school in traditional dress.", "images/site/g-culture-kente.jpg", "center 35%"),
        ("Old School Day", "Pupils and teachers step back in time for a day, with outfits and music to match.", "images/site/g-oldschool.jpg"),
        ("Service", "Awareness walks such as Pink October teach our pupils to care for the community around them.", "images/site/g-pink.jpg"),
        ("Excursions", "Days out together, including our trip to the water park, with games, swimming and a shared lunch.", "images/site/g-pool.jpg", "center 50%"),
        ("Life Skills", "Practical days where pupils cook, serve and work together.", "images/site/g-cooking.jpg"),
        ("Graduation", "We send our graduates off in gowns and sashes, with their families and teachers beside them.", "images/site/g-graduation.jpg"),
    ]
    return f'''<main id="top">
{photo_hero("School Life", "images/site/hero-3.jpg", "Senior students jumping for joy together", "center 18%")}
{statement("Beyond the classroom", "Learning at ROLA goes well beyond the classroom. Through the year our pupils perform, compete, create and give back.",
           ["These are the occasions our pupils look forward to and remember, and where many of them discover what they are good at."])}
{rlist("calendar", "Through the year", "A full school calendar", "Select an occasion to read more.", rows)}
  <section class="section moments moments--teaser">
    <div class="wrap">
      <div class="moments__head reveal">
        <div><p class="eyebrow eyebrow--gold">Moments</p><h2>See it for yourself</h2></div>
        {btn("See all moments", "moments.html", light=True)}
      </div>
      <div class="grid">
{shots(SHOTS[6:12])}
      </div>
    </div>
  </section>

{get_in_touch("images/site/g-grads.jpg", "center 8%")}
{explore([("Learning", "Creche to Junior High", "learning.html"), ("Moments", "Photo Gallery", "moments.html"), ("Admissions", "How to Apply", "admissions.html")])}</main>
'''


def page_admissions():
    steps = [
        ("Visit or enquire", "Call, send a message or come in for a tour of the school. It is the best way to see whether ROLA is right for your family.", "images/site/g-admission-banner.jpg", "center 45%"),
        ("Complete the form", "Collect an admission form from the school office and return it with the documents listed below.", "images/site/g-class-portrait.jpg"),
        ("Meet us", "A short, friendly assessment for your child and a conversation with parents.", "images/site/kg.jpg"),
        ("Join the family", "Receive your admission letter and prepare for the first day at ROLA.", "images/site/g-uniform.jpg"),
    ]
    return f'''<main id="top">
{photo_hero("Admissions", "images/site/h-class.jpg", "Senior students with their classmates", "center 25%")}
{statement("Joining ROLA", "We welcome applications for every class from Creche to Junior High, subject to available places.",
           ["Our admissions office will guide you through the process and answer your questions. You are welcome to visit first, then apply at a time that suits your family."],
           btn("Book a visit", "contact.html#visit"))}
{rlist("apply", "How to apply", "Four simple steps", "Select a step to read more.", steps)}
  <section class="section facts-section" id="bring">
    <div class="wrap life__grid">
      <div class="life__intro reveal"><p class="eyebrow">Documents</p><h2>What to bring</h2><p>Please bring these with your completed admission form.</p></div>
      <div class="table reveal">
        <div class="table__row"><h3>Birth certificate</h3><p>A copy of your child&rsquo;s birth certificate.</p></div>
        <div class="table__row"><h3>Photographs</h3><p>Two recent passport-size photographs.</p></div>
        <div class="table__row"><h3>School report</h3><p>The last report from the previous school, if transferring.</p></div>
        <div class="table__row"><h3>Health record</h3><p>Your child&rsquo;s health or weighing card.</p></div>
        <div class="table__row"><h3>Parent ID</h3><p>A copy of a parent or guardian&rsquo;s Ghana Card.</p></div>
      </div>
    </div>
  </section>

  <!-- Placeholder dates: replace with the real school calendar -->
  <section class="section dates" id="dates">
    <div class="wrap dates__grid">
      <div class="reveal"><p class="eyebrow">Calendar</p><h2>Term dates</h2><p>Key dates for the 2026/2027 academic year. Parents will be notified of any changes.</p></div>
      <div class="table table--dates reveal">
        <div class="table__row"><p class="table__date">5 Dec</p><h3>Christmas Carols &amp; Speech Day</h3><p>9:00am, school grounds</p></div>
        <div class="table__row"><p class="table__date">11 Dec</p><h3>First term ends</h3><p>School closes at noon</p></div>
        <div class="table__row"><p class="table__date">12 Jan</p><h3>Second term begins</h3><p>All pupils resume</p></div>
        <div class="table__row"><p class="table__date">6 Mar</p><h3>Independence Day &amp; Cultural Day</h3><p>Traditional dress</p></div>
      </div>
    </div>
  </section>

  <section class="section fees" id="fees">
    <div class="wrap fees__inner reveal">
      <p class="eyebrow">School fees</p>
      <p class="lead">For the current fee schedule and payment arrangements, please speak to the school office.</p>
      {btn("Contact the office", "contact.html")}
    </div>
  </section>

{get_in_touch("images/site/g-team-staff.jpg", "center 40%")}
{explore([("Learning", "Creche to Junior High", "learning.html"), ("Our School", "A Word from our Principals", "our-school.html#principal"), ("School Life", "Through the Year", "school-life.html")])}</main>
'''


def page_moments():
    return f'''<main id="top">
{photo_hero("Moments", "images/site/g-ucmas-team.jpg", "The UCMAS competition team together outdoors", "center 45%")}
  <section class="section moments moments--page">
    <div class="wrap">
      <div class="grid" id="gallery">
{shots(SHOTS)}
      </div>
      <p class="moments__more"><a href="{INSTAGRAM}" target="_blank" rel="noopener" class="btn btn--light">Follow @rola_school on Instagram <i aria-hidden="true"></i></a></p>
    </div>
  </section>
{explore([("School Life", "Through the Year", "school-life.html"), ("Our School", "Who We Are", "our-school.html"), ("Admissions", "How to Apply", "admissions.html")])}</main>
'''


def page_contact():
    pin = '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M24 44s14-13.200 14-24a14 14 0 1 0-28 0c0 10.800 14 24 14 24z"/><circle cx="24" cy="20" r="5"/></svg>'
    phone = '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M14 6h7l3 9-4.500 3a22 22 0 0 0 10.500 10.500l3-4.500 9 3v7a4 4 0 0 1-4 4C21 38 10 27 10 10a4 4 0 0 1 4-4z"/></svg>'
    mail = '<svg viewBox="0 0 48 48" aria-hidden="true"><rect x="6" y="11" width="36" height="26" rx="2"/><path d="M6 14l18 13 18-13"/></svg>'
    return f'''<main id="top">
  <section class="touch touch--top">
    <img class="touch__photo" src="images/site/hero-1.jpg" alt="" />
    <div class="wrap">
      <h1>Get in touch</h1>
      <ul class="touch__lines">
        <li>{phone}<span>Phone: <a href="tel:{PHONE_LINK}">{PHONE_DISPLAY}</a> / <a href="tel:{PHONE2_LINK}">{PHONE2_DISPLAY}</a></span></li>
        <li>{mail}<span>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></span></li>
        <li>{pin}<span>Address: River of Life Academy, Accra, Ghana</span></li>
      </ul>
      <div class="touch__pills">
        <a class="ccard__pill" href="{MAPS}" target="_blank" rel="noopener">Get directions</a>
        <a class="ccard__pill" href="https://wa.me/{PHONE_LINK.lstrip('+')}" target="_blank" rel="noopener">WhatsApp</a>
      </div>
    </div>
  </section>

  <section class="section cform-section cform-section--rise" id="visit">
    <div class="wrap">
      <div class="cpanel reveal">
        <div class="cpanel__side">
          <img src="images/site/g-uniform.jpg" alt="" loading="lazy" />
          <p class="eyebrow eyebrow--gold">Book a visit or ask a question</p>
          <h2>Send us a message</h2>
          <p>Tell us a little about your child and what you would like to know, and the school office will be in touch.</p>
          <p class="cpanel__hours">School office: Monday to Friday, 7:00am to 4:00pm</p>
        </div>
        <form class="form" id="contactForm" novalidate>
          <div class="form__row">
            <div class="field"><label for="name">Your name *</label><input id="name" name="name" type="text" autocomplete="name" required /></div>
            <div class="field"><label for="phone">Phone number *</label><input id="phone" name="phone" type="tel" autocomplete="tel" required /></div>
          </div>
          <div class="field"><label for="email">Email address</label><input id="email" name="email" type="email" autocomplete="email" /></div>
          <div class="form__row">
            <div class="field"><label for="level">Class of interest</label>
              <select id="level" name="level"><option value="">Please select</option><option>Creche / Nursery</option><option>Kindergarten</option><option>Primary (Basic 1 to 6)</option><option>Junior High School</option></select></div>
            <div class="field"><label for="reason">I would like to</label>
              <select id="reason" name="reason"><option>Book a visit</option><option>Ask about admission</option><option>Ask about fees</option><option>Something else</option></select></div>
          </div>
          <div class="field"><label for="message">Message *</label><textarea id="message" name="message" rows="3" required></textarea></div>
          <button type="submit" class="btn">Send message</button>
          <p class="form__status" id="formStatus" role="status" aria-live="polite"></p>
        </form>
      </div>

      <div class="mapwrap reveal">
        <div class="map">
          <iframe title="Map to River of Life Academy" src="https://maps.google.com/maps?q=5.6242063,-0.2452966&z=17&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
        <div class="mapcard">
          <p class="eyebrow eyebrow--gold">Find us</p>
          <h3>River of Life Academy</h3>
          <p>Accra, Ghana</p>
          <a class="ccard__pill" href="{MAPS}" target="_blank" rel="noopener">Open in Google Maps</a>
        </div>
      </div>
    </div>
  </section>
{explore([("Admissions", "How to Apply", "admissions.html"), ("Admissions", "Term Dates", "admissions.html#dates"), ("Our School", "Who We Are", "our-school.html")])}</main>
'''


PAGES = [
    ("index.html", "River of Life Academy | Devotion and Service | Accra, Ghana",
     "River of Life Academy (ROLA) is a basic school in Accra, Ghana, educating children from Creche to Junior High School. Motto: Devotion and Service.", page_home, True),
    ("our-school.html", "Our School | River of Life Academy", "Who we are, our motto and a word from the Principals of River of Life Academy, Accra.", page_our_school, False),
    ("learning.html", "Learning | River of Life Academy", "Creche and Nursery, Kindergarten, Primary and Junior High School at River of Life Academy, Accra.", page_learning, False),
    ("school-life.html", "School Life | River of Life Academy", "Arts, mental arithmetic, sport, culture, service and excursions at River of Life Academy, Accra.", page_school_life, False),
    ("admissions.html", "Admissions | River of Life Academy", "How to apply, what to bring and term dates for River of Life Academy, Accra.", page_admissions, False),
    ("moments.html", "Moments | River of Life Academy", "Photo gallery of life at River of Life Academy, Accra.", page_moments, False),
    ("contact.html", "Contact Us | River of Life Academy", "Visit, call, email or send a message to River of Life Academy, Accra.", page_contact, False),
]

for name, title, desc, body, home in PAGES:
    html = head(title, desc)
    html += '<body class="is-cover">\n' if home else "<body>\n"
    html += VEIL
    if home:
        html += COVER
    html += header(home) + MENU + body() + FOOTER
    with open(os.path.join(ROOT, name), "w", encoding="utf8", newline="\n") as f:
        f.write(html)
    print("wrote", name, len(html) // 1024, "KB")
