/* River of Life Academy — site scripts */
(function () {
  "use strict";
  document.documentElement.classList.add("js");

  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => Array.from(c.querySelectorAll(s));
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
  const reducedMotion = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const body = document.body;

  /* Plays a background video only if the file exists; otherwise removes the tag. */
  function optionalVideo(video, src, onReady) {
    if (!video) return;
    video.addEventListener("canplay", () => {
      video.classList.add("is-ready");
      const p = video.play();
      if (p && p.catch) p.catch(() => {});
      if (onReady) onReady();
    }, { once: true });
    video.addEventListener("error", () => video.remove(), { once: true });
    if (!reducedMotion) { video.src = src; video.load(); } else { video.remove(); }
  }
  const HERO_VIDEO = "images/site/hero.mp4";
  // Remembers that the welcome experience has been seen, so returning to Home does not replay it
  const markSeen = () => { try { sessionStorage.setItem("rolaSeen", "1"); } catch (e) {} };

  /* =======================================================
     WELCOME EXPERIENCE
     Stage 1  intro : opening photo/video with the motto
     Stage 2  globe : tiles on a slowly turning globe
     Stage 3  wall  : the same tiles unfolded into a wall you drag around
     Clicking a tile opens a preview sheet with a "Full page" button.
     ======================================================= */
  const cover = $("#cover");
  const sphere = $("#sphere");
  const globe = $("#globe");
  const hint = $("#coverHint");
  const RAD = Math.PI / 180;

  // Navy tiles with a gold frame. "topic" drives the Exploring filter.
  const TEXT_CARDS = [
    { topic: "Admissions", label: "Admissions", title: "How to Apply", foot: "Creche to JHS", href: "admissions.html", img: "images/site/welcome.jpg",
      text: "We welcome applications for every class from Creche to Junior High, subject to available places. Visit us, collect a form from the school office, and our admissions team will guide you from there." },
    { topic: "Learning", label: "Learning", title: "Creche & Nursery", foot: "Ages 1 to 3", href: "learning.html", img: "images/site/nursery.jpg",
      text: "A gentle, safe start where our youngest pupils play, sing, explore and make their first friends." },
    { topic: "Learning", label: "Learning", title: "Kindergarten", foot: "KG 1 and 2", href: "learning.html", img: "images/site/kg.jpg",
      text: "Phonics, early reading, number work and creative play that prepare children for primary school." },
    { topic: "Learning", label: "Learning", title: "Primary School", foot: "Basic 1 to 6", href: "learning.html", img: "images/site/primary.jpg",
      text: "Strong foundations in English, Mathematics, Science and ICT, alongside languages and the creative arts." },
    { topic: "Learning", label: "Learning", title: "Junior High", foot: "JHS 1 to 3", href: "learning.html", img: "images/site/jhs.jpg",
      text: "Focused teaching, mentoring and BECE preparation for confident, well-rounded young people." },
    { topic: "School Life", label: "School Life", title: "Creative Arts", foot: "Exhibitions", href: "school-life.html", img: "images/site/g-art.jpg",
      text: "Painting, drawing and craft, shown each year at our art exhibition, “Creativity is the Point”." },
    { topic: "School Life", label: "School Life", title: "Sport & Fitness", foot: "Inter-house", href: "school-life.html", img: "images/site/g-pe.jpg",
      text: "Morning exercise, physical education, games and inter-house competitions keep our pupils active and working as a team." },
    { topic: "School Life", label: "School Life", title: "Cultural Day", foot: "Our heritage", href: "school-life.html", img: "images/site/g-culture.jpg",
      text: "A celebration of Ghanaian heritage, when pupils and teachers come to school in traditional dress." },
    { topic: "Our School", label: "Our School", title: "Our Motto", foot: "Devotion and Service", href: "our-school.html#motto", img: "images/site/hero-1.jpg",
      text: "Devotion and Service is more than a motto. Our teachers are devoted to every learner, and our pupils learn to serve their school, their families and their community." },
    { topic: "Our School", label: "Our School", title: "A Word of Welcome", foot: "From our Principals", href: "our-school.html#principal", img: "images/site/principals.jpg",
      text: "“Every child is a gift. Our work is to help each one discover what they can do, and to use it in the service of others.” Rev. S. Twumasi-Ankra Bonsu and Mrs. Tina Bonsu, Principals." },
    { topic: "Admissions", label: "Visit", title: "Book a Visit", foot: "See us in action", href: "contact.html#visit", img: "images/site/stats.jpg",
      text: "The best way to understand our school is to visit. See learning in action, meet our teachers and walk through our campus." },
    { topic: "Admissions", label: "Admissions", title: "Term Dates", foot: "2026/2027", href: "admissions.html#dates", img: "images/site/h-class.jpg",
      text: "Key dates for the academic year, including the start and end of each term and our main school events." },
    { topic: "Our School", label: "Moments", title: "Life at ROLA", foot: "Gallery", href: "moments.html", img: "images/site/g-uniform.jpg",
      text: "A look at the people and occasions that make our school a family." },
    { topic: "School Life", label: "School Life", title: "Pink October", foot: "Serving our community", href: "school-life.html", img: "images/site/g-pink.jpg",
      text: "Awareness walks such as Pink October teach our pupils to care for the community around them." },
  ];
  // Captions shown on a few photo tiles (photo number -> [label, title])
  const PHOTO_CAPTIONS = {
    4: ["School Life", "Old School Day"],
    6: ["Our School", "Our Campus"],
    14: ["School Life", "Creative Arts"],
    20: ["School Life", "Cultural Day"],
    21: ["Achievement", "UCMAS Champions"],
  };
  const PHOTO_COUNT = 26;
  // Globe rows, spaced so neighbouring tiles never touch (tile 240 x 320 on a 672 radius)
  const ROWS = [ { lat: 60, n: 5 }, { lat: 30, n: 9 }, { lat: 0, n: 10 }, { lat: -30, n: 9 }, { lat: -60, n: 5 } ];
  const WALL_COLS = 8, WALL_ROWS = 5;
  const PERSONAS = [ ["New Parent", "Admissions"], ["Current Parent", "School Life"], ["Student", "Learning"], ["Visitor", "Our School"] ];
  const TOPICS = ["Everything", "Our School", "Learning", "School Life", "Admissions"];

  const cards = [];
  let u = 1, R = 672, mode = "intro", topic = "Everything";
  let spin = 0, tilt = -6, tiltTarget = -6, sway = 0, swayTarget = 0;
  let panX = 0, panY = 0, panMaxX = 0, panMaxY = 0;
  let pointerDown = false, moved = 0, lastX = 0, lastY = 0, raf = 0, morphTimer = 0;

  function buildTiles() {
    let i = 0, photo = 0, text = 0;
    ROWS.forEach((row, r) => {
      for (let k = 0; k < row.n; k++, i++) {
        const el = document.createElement("a");
        el.className = "gcard";
        el.draggable = false;
        let data;
        const useText = (i % 8 === 1 || i % 8 === 4 || i % 8 === 6) && text < TEXT_CARDS.length;
        if (useText) {
          data = TEXT_CARDS[text++];
          el.classList.add("gcard--text");
          el.innerHTML = "<small></small><strong></strong><em></em>";
          el.children[0].textContent = data.label;
          el.children[1].textContent = data.title;
          el.children[2].textContent = data.foot;
        } else {
          photo = (photo % PHOTO_COUNT) + 1;
          const num = String(photo).padStart(2, "0");
          const cap = PHOTO_CAPTIONS[photo];
          data = { topic: cap && cap[0] === "Our School" ? "Our School" : "School Life", label: cap ? cap[0] : "Moments",
                   title: cap ? cap[1] : "Life at ROLA", href: "moments.html", img: "images/globe/full/p" + num + ".jpg", text: "" };
          el.style.backgroundImage = "url(images/globe/t" + num + ".jpg)";
          if (cap) {
            el.classList.add("gcard--caption");
            el.innerHTML = "<small></small><strong></strong>";
            el.children[0].textContent = cap[0];
            el.children[1].textContent = cap[1];
          } else {
            el.setAttribute("aria-label", "School photo");
          }
        }
        el.href = data.href;
        const a = -row.lat * RAD;
        const card = { el, data, lon: (360 / row.n) * k + r * 17, lat: row.lat, ca: Math.cos(a), sa: Math.sin(a), index: i };
        cards.push(card);
        el.addEventListener("click", (e) => {
          e.preventDefault();
          if (moved > 8) return;                 // it was a drag, not a click
          openSheet(card.data);
        });
        sphere.appendChild(el);
      }
    });
  }

  const globeTransform = (c) => "rotateY(" + c.lon + "deg) rotateX(" + -c.lat + "deg) translateZ(" + R.toFixed(1) + "px)";
  const sphereGlobeTransform = () => "translateZ(" + (-R * 0.55).toFixed(1) + "px) rotateX(" + tilt.toFixed(2) + "deg) rotateY(" + (spin + sway).toFixed(2) + "deg)";

  /* Lay the tiles out as a staggered wall; tiles matching the chosen topic sit nearest the centre. */
  function applyWall() {
    const cw = 240 * u, ch = 320 * u, px = cw * 1.62, py = ch * 1.34;
    const slots = [];
    for (let c = 0; c < WALL_COLS; c++) for (let r = 0; r < WALL_ROWS; r++) {
      slots.push({ x: (c - (WALL_COLS - 1) / 2) * px, y: (r - (WALL_ROWS - 1) / 2) * py + (c % 2 ? py / 2 : 0) - py / 4 });
    }
    slots.sort((a, b) => (a.x * a.x + a.y * a.y * 1.6) - (b.x * b.x + b.y * b.y * 1.6));
    const match = (c) => topic === "Everything" || c.data.topic === topic;
    const ordered = cards.filter(match).concat(cards.filter((c) => !match(c)));
    ordered.forEach((c, k) => {
      const s = slots[k];
      c.el.style.transform = "translate3d(" + s.x.toFixed(1) + "px," + s.y.toFixed(1) + "px,0)";
      c.el.style.opacity = match(c) ? "1" : "0.16";
      c.el.style.pointerEvents = "auto";
    });
    panMaxX = Math.max(0, ((WALL_COLS - 1) * px + cw) / 2 - innerWidth / 2 + 90);
    panMaxY = Math.max(0, ((WALL_ROWS - 1) * py + ch + py / 2) / 2 - innerHeight / 2 + 130);
    setPan(panX, panY);
  }
  function setPan(x, y) {
    panX = clamp(x, -panMaxX, panMaxX);
    panY = clamp(y, -panMaxY, panMaxY);
    sphere.style.transform = "translate3d(" + panX.toFixed(1) + "px," + panY.toFixed(1) + "px,0)";
  }

  function layout() {
    u = clamp(Math.min(innerWidth / 1500, innerHeight / 950), 0.5, 1.3);
    R = 672 * u;
    globe.style.perspective = 1200 * u + "px";
    cards.forEach((c) => {
      c.el.style.setProperty("--u", u.toFixed(3));
      c.el.style.setProperty("--cw", (240 * u).toFixed(1) + "px");
      c.el.style.setProperty("--ch", (320 * u).toFixed(1) + "px");
      if (mode !== "wall") c.el.style.transform = globeTransform(c);
    });
    if (mode === "wall") applyWall();
  }

  function frame() {
    if (!pointerDown && !reducedMotion) spin += 0.05;
    tilt += (tiltTarget - tilt) * 0.06;
    sway += (swayTarget - sway) * 0.06;
    sphere.style.transform = sphereGlobeTransform();
    const s = spin + sway, ct = Math.cos(tilt * RAD), st = Math.sin(tilt * RAD);
    for (let i = 0; i < cards.length; i++) {
      const c = cards[i];
      const depth = c.ca * Math.cos((c.lon + s) * RAD) * ct - c.sa * st;   // 1 = facing viewer, -1 = far side
      c.el.style.opacity = (depth > 0 ? 0.26 + 0.74 * depth : 0.05 + 0.21 * (1 + depth)).toFixed(2);
      c.el.style.pointerEvents = depth > 0.3 ? "auto" : "none";
    }
    raf = requestAnimationFrame(frame);
  }

  function endIntro() {
    if (mode !== "intro") return;
    mode = "globe";
    cover.classList.remove("is-intro");
  }

  function toWall() {
    if (mode === "wall") return;
    endIntro();
    mode = "wall";
    cancelAnimationFrame(raf);
    clearTimeout(morphTimer);
    cover.classList.add("is-morph", "is-wall");
    body.classList.add("is-wall");
    hint.textContent = "Drag to move around";
    panX = 0; panY = 0;
    applyWall();
    morphTimer = setTimeout(() => cover.classList.remove("is-morph"), 1600);
  }

  function toGlobe() {
    if (mode !== "wall") return;
    mode = "globe";
    closePickers();
    clearTimeout(morphTimer);
    cover.classList.add("is-morph");
    cover.classList.remove("is-wall");
    body.classList.remove("is-wall");
    hint.textContent = "Drag to explore";
    sphere.style.transform = sphereGlobeTransform();
    cards.forEach((c) => { c.el.style.transform = globeTransform(c); c.el.style.opacity = "0.7"; });
    morphTimer = setTimeout(() => {
      cover.classList.remove("is-morph");
      cancelAnimationFrame(raf);
      raf = requestAnimationFrame(frame);
    }, 1600);
  }

  function dismissCover(target) {
    closeSheet();
    closePickers();
    markSeen();
    cover.classList.add("is-gone");
    body.classList.remove("is-cover", "is-wall");
    setTimeout(() => cancelAnimationFrame(raf), 1100);
    if (target && target.length > 1 && target.charAt(0) === "#") {
      const el = $(target);
      if (el) el.scrollIntoView();
    }
    updateHeaderTheme();
  }

  function showCover() {
    window.scrollTo(0, 0);
    clearTimeout(morphTimer);
    mode = "globe";
    cover.classList.remove("is-gone", "is-wall", "is-morph", "is-intro");
    body.classList.remove("is-wall");
    body.classList.add("is-cover");
    hint.textContent = "Drag to explore";
    cards.forEach((c) => { c.el.style.transform = globeTransform(c); });
    cancelAnimationFrame(raf);
    raf = requestAnimationFrame(frame);
  }

  /* ----- Pickers on the wall: "I am a ..." and "Exploring ..." ----- */
  const pickPersona = $("#pickPersona");
  const pickTopic = $("#pickTopic");
  function closePickers() {
    [pickPersona, pickTopic].forEach((p) => p && p.classList.remove("is-open"));
    if (cover) cover.classList.remove("is-picking");
  }
  function setTopic(next) {
    topic = next;
    $("strong", pickTopic).textContent = next;
    $$("button", $(".pick__list", pickTopic)).forEach((b) => b.classList.toggle("is-current", b.textContent === next));
    panX = 0; panY = 0;
    applyWall();
  }
  function buildPickers() {
    const personaList = $(".pick__list", pickPersona);
    PERSONAS.forEach(([name, mapsTo], i) => {
      const b = document.createElement("button");
      b.type = "button"; b.textContent = name;
      if (i === 0) b.classList.add("is-current");
      b.addEventListener("click", () => {
        $("strong", pickPersona).textContent = name;
        $$("button", personaList).forEach((x) => x.classList.toggle("is-current", x === b));
        closePickers();
        setTopic(mapsTo);
      });
      personaList.appendChild(b);
    });
    const topicList = $(".pick__list", pickTopic);
    TOPICS.forEach((name) => {
      const b = document.createElement("button");
      b.type = "button"; b.textContent = name;
      if (name === topic) b.classList.add("is-current");
      b.addEventListener("click", () => { closePickers(); setTopic(name); });
      topicList.appendChild(b);
    });
    [pickPersona, pickTopic].forEach((p) => {
      $(".pick__btn", p).addEventListener("click", () => {
        const open = !p.classList.contains("is-open");
        closePickers();
        p.classList.toggle("is-open", open);
        cover.classList.toggle("is-picking", open);
      });
    });
  }

  /* ----- Preview sheet ----- */
  const sheet = $("#sheet");
  let sheetHref = "#top";
  function openSheet(data) {
    sheetHref = data.href || "#top";
    $("#sheetLabel").textContent = data.label;
    $("#sheetTitle").textContent = data.title;
    const img = $("#sheetImg");
    img.src = data.img; img.alt = data.title;
    const text = $("#sheetText");
    text.textContent = data.text || "";
    text.hidden = !data.text;
    $("#sheetScroll").scrollTop = 0;
    closePickers();
    sheet.classList.add("is-open");
    sheet.setAttribute("aria-hidden", "false");
    $("#sheetClose").focus({ preventScroll: true });
  }
  function closeSheet() {
    if (!sheet || !sheet.classList.contains("is-open")) return;
    sheet.classList.remove("is-open");
    sheet.setAttribute("aria-hidden", "true");
  }

  if (cover) {
    buildTiles();
    buildPickers();
    layout();
    addEventListener("resize", layout);

    cover.addEventListener("pointerdown", (e) => {
      if (mode === "intro") { endIntro(); return; }
      if (e.target.closest("button, .wallbar")) return;
      if (cover.classList.contains("is-picking")) { closePickers(); return; }
      pointerDown = true; moved = 0; lastX = e.clientX; lastY = e.clientY;
    });
    addEventListener("pointermove", (e) => {
      if (!body.classList.contains("is-cover") || sheet.classList.contains("is-open")) return;
      if (pointerDown) {
        const dx = e.clientX - lastX, dy = e.clientY - lastY;
        lastX = e.clientX; lastY = e.clientY;
        moved += Math.abs(dx) + Math.abs(dy);
        if (mode === "wall") setPan(panX + dx, panY + dy);
        else { spin += dx * 0.22; tiltTarget = clamp(tiltTarget - dy * 0.18, -38, 38); }
      } else if (mode === "globe" && e.pointerType === "mouse") {
        swayTarget = (e.clientX / innerWidth - 0.5) * 22;
        tiltTarget = -6 + (0.5 - e.clientY / innerHeight) * 16;
      }
    });
    addEventListener("pointerup", () => { pointerDown = false; });
    addEventListener("pointercancel", () => { pointerDown = false; });
    cover.addEventListener("wheel", (e) => {
      if (mode !== "wall" || sheet.classList.contains("is-open")) return;
      e.preventDefault();
      setPan(panX - e.deltaX, panY - e.deltaY);
    }, { passive: false });

    $("#coverGo").addEventListener("click", toWall);
    $("#backToGlobe").addEventListener("click", toGlobe);
    $("#enterSite").addEventListener("click", () => dismissCover("#top"));
    $("#sheetClose").addEventListener("click", closeSheet);
    $("#sheetFull").addEventListener("click", () => {
      if (sheetHref.charAt(0) === "#") { dismissCover(sheetHref); return; }
      markSeen();
      window.ROLA.go(sheetHref);
    });
    sheet.addEventListener("click", (e) => { if (e.target === sheet || e.target.id === "sheetScroll") closeSheet(); });

    let seen = false;
    try { seen = sessionStorage.getItem("rolaSeen") === "1"; } catch (e) {}
    const replay = /[?&]welcome=1/.test(location.search);
    if (location.hash.length > 1 || (seen && !replay)) {
      // Arrived via a link to a section, or already seen this visit: skip the welcome experience
      mode = "globe";
      cover.classList.remove("is-intro");
      cover.classList.add("is-gone");
      body.classList.remove("is-cover");
    } else {
      let introMs = 3600;
      optionalVideo($("#introVideo"), HERO_VIDEO, () => { introMs = 7000; });
      const started = performance.now();
      (function waitIntro() {
        if (mode !== "intro") return;
        if (performance.now() - started >= introMs) endIntro(); else setTimeout(waitIntro, 200);
      })();
      raf = requestAnimationFrame(frame);
    }
  }

  /* =======================================================
     Menu
     ======================================================= */
  const menu = $("#menu");
  const menuBtn = $("#menuBtn");
  function setMenu(open) {
    menu.classList.toggle("is-open", open);
    menu.setAttribute("aria-hidden", String(!open));
    menuBtn.setAttribute("aria-expanded", String(open));
    menuBtn.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    body.classList.toggle("menu-open", open);
  }
  menuBtn.addEventListener("click", () => setMenu(!menu.classList.contains("is-open")));
  // Hovering a main item shows its sub-links in the right-hand column
  const mainLinks = $$(".menu__main a", menu);
  const subGroups = $$(".menu__sub > div", menu);
  mainLinks.forEach((a) => {
    const show = () => {
      mainLinks.forEach((x) => x.classList.toggle("is-on", x === a));
      subGroups.forEach((g) => g.classList.toggle("is-on", g.dataset.for === a.dataset.sub));
    };
    a.addEventListener("mouseenter", show);
    a.addEventListener("focus", show);
  });
  $$("a", menu).forEach((a) => a.addEventListener("click", (e) => {
    setMenu(false);
    if (a.id === "replayIntro") {
      e.preventDefault();
      if (cover) showCover(); else window.ROLA.go("index.html?welcome=1");
      return;
    }
    const href = a.getAttribute("href") || "";
    if (body.classList.contains("is-cover") && href.charAt(0) === "#") {
      e.preventDefault();
      dismissCover(href);
    }
  }));
  // Header links also work from the welcome experience
  $$(".wordmark, .pillnav a").forEach((a) => a.addEventListener("click", (e) => {
    const href = a.getAttribute("href");
    if (body.classList.contains("is-cover") && href && href.charAt(0) === "#") {
      e.preventDefault();
      dismissCover(href);
    }
  }));
  document.addEventListener("keydown", (e) => {
    if (e.key !== "Escape") return;
    if (sheet && sheet.classList.contains("is-open")) { closeSheet(); return; }
    closePickers(); setMenu(false); closeLightbox();
  });

  /* =======================================================
     Header: light or dark wordmark depending on what is behind it
     ======================================================= */
  const header = $("#header");
  const darkSections = $$(".hero, .phero:not(.phero--plain), .welcome, .motto, .banner, .moments, .touch");
  const mainEl = $("main");
  function updateHeaderTheme() {
    const y = 48;
    const onDark = darkSections.some((s) => {
      const r = s.getBoundingClientRect();
      return r.top <= y && r.bottom > y;
    });
    const overFooter = mainEl ? mainEl.getBoundingClientRect().bottom <= y : false;
    header.classList.toggle("is-light", !(onDark || overFooter));
    header.classList.toggle("is-scrolled", window.scrollY > 40);   // phones: the header gets a solid bar once the page moves
  }
  let ticking = false;
  addEventListener("scroll", () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => { updateHeaderTheme(); ticking = false; });
  }, { passive: true });
  addEventListener("resize", updateHeaderTheme);
  updateHeaderTheme();

  /* Highlight the current section in the pill navigation; reveal on scroll */
  const pillLinks = $$(".pillnav a");
  if ("IntersectionObserver" in window) {
    const spy = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        const link = pillLinks.find((l) => l.getAttribute("href") === "#" + en.target.id);
        if (link) link.classList.toggle("is-active", en.isIntersecting);
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    pillLinks.map((l) => $(l.getAttribute("href"))).filter(Boolean).forEach((s) => spy.observe(s));

    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -6% 0px" });
    $$(".reveal").forEach((el) => io.observe(el));
  } else {
    $$(".reveal").forEach((el) => el.classList.add("is-in"));
  }

  /* =======================================================
     Home background: photos that change, or a video if one exists.
     To use a video, save it as images/site/hero.mp4 (muted, about
     10 to 20 seconds, under 8 MB works best).
     ======================================================= */
  const heroSlides = $$("#heroSlides img");
  let heroTimer = 0, heroIndex = 0;
  if (heroSlides.length > 1) {
    heroTimer = setInterval(() => {
      if (document.hidden || body.classList.contains("is-cover")) return;
      heroSlides[heroIndex].classList.remove("is-active");
      heroIndex = (heroIndex + 1) % heroSlides.length;
      heroSlides[heroIndex].classList.add("is-active");
    }, 6000);
  }
  optionalVideo($("#heroVideo"), HERO_VIDEO, () => clearInterval(heroTimer));

  /* =======================================================
     Learning slider arrows
     ======================================================= */
  const slider = $("#slider");
  if (slider) {
    const step = (dir) => {
      const card = $(".stage", slider);
      slider.scrollBy({ left: dir * (card.offsetWidth + 22), behavior: reducedMotion ? "auto" : "smooth" });
    };
    $("#slidePrev").addEventListener("click", () => step(-1));
    $("#slideNext").addEventListener("click", () => step(1));
  }

  /* =======================================================
     Gallery lightbox
     ======================================================= */
  const lightbox = $("#lightbox");
  const lbImg = lightbox && $("img", lightbox);
  const lbCap = lightbox && $("p", lightbox);
  let lastFocus = null;
  function closeLightbox() {
    if (!lightbox || !lightbox.classList.contains("is-open")) return;
    lightbox.classList.remove("is-open");
    lightbox.setAttribute("aria-hidden", "true");
    if (lastFocus) lastFocus.focus();
  }
  $$(".shot").forEach((shot) => shot.addEventListener("click", () => {
    const img = $("img", shot);
    lastFocus = shot;
    lbImg.src = img.src;
    lbImg.alt = img.alt;
    lbCap.textContent = $("span", shot).textContent;
    lightbox.classList.add("is-open");
    lightbox.setAttribute("aria-hidden", "false");
    $(".lightbox__close", lightbox).focus();
  }));
  if (lightbox) lightbox.addEventListener("click", (e) => {
    if (e.target === lightbox || e.target.closest(".lightbox__close")) closeLightbox();
  });

  /* =======================================================
     Contact form
     By default this opens the email app of the visitor with the message
     filled in. To receive messages directly, create a free form at
     formspree.io and paste its address into FORM_ENDPOINT.
     ======================================================= */
  const FORM_ENDPOINT = "";
  const SCHOOL_EMAIL = "info@riveroflifeacademy.edu.gh";
  const form = $("#contactForm");
  const status = $("#formStatus");
  const setStatus = (msg, type) => {
    if (!status) return;
    status.textContent = msg;
    status.className = "form__status" + (type ? " is-" + type : "");
  };
  if (form) form.addEventListener("submit", async (e) => {
    e.preventDefault();
    let ok = true;
    ["name", "phone", "message"].forEach((id) => {
      const el = $("#" + id);
      const bad = !el.value.trim();
      el.closest(".field").classList.toggle("has-error", bad);
      if (bad) ok = false;
    });
    const email = $("#email");
    const badEmail = email.value !== "" && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value);
    email.closest(".field").classList.toggle("has-error", badEmail);
    if (badEmail) ok = false;
    if (!ok) { setStatus("Please complete the highlighted fields.", "error"); return; }

    const data = Object.fromEntries(new FormData(form).entries());
    if (FORM_ENDPOINT) {
      setStatus("Sending…");
      try {
        const res = await fetch(FORM_ENDPOINT, { method: "POST", headers: { Accept: "application/json" }, body: new FormData(form) });
        if (!res.ok) throw new Error("send failed");
        form.reset();
        setStatus("Thank you. We have received your message and will be in touch soon.", "success");
      } catch (err) {
        setStatus("Sorry, your message could not be sent. Please call us instead.", "error");
      }
      return;
    }
    const subject = "Website enquiry: " + data.reason + (data.level ? " (" + data.level + ")" : "");
    const msg = "Name: " + data.name + "\nPhone: " + data.phone + "\nEmail: " + (data.email || "-") +
      "\nClass of interest: " + (data.level || "-") + "\n\n" + data.message;
    location.href = "mailto:" + SCHOOL_EMAIL + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(msg);
    setStatus("Opening your email app to send the message…", "success");
  });

  $("#year").textContent = new Date().getFullYear();
})();
