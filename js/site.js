/* River of Life Academy — shared page behaviour (loaded before main.js)
   Page transition, header link highlight, parallax photo, footer reveal, expanding lists. */
(function () {
  "use strict";
  var reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;
  var here = location.pathname.split("/").pop() || "index.html";

  /* ---------- Page transition: a white sheet with the crest ---------- */
  var veil = document.querySelector(".veil");
  function go(href) {
    try { sessionStorage.setItem("rolaSeen", "1"); } catch (e) {}
    if (!veil || reduced) { location.href = href; return; }
    veil.style.transition = "none";
    veil.classList.remove("is-loaded");
    veil.style.transform = "translateY(101%)";
    void veil.offsetHeight;                       // apply the start position before animating
    veil.style.transition = "";
    veil.style.transform = "translateY(0)";
    setTimeout(function () { location.href = href; }, 620);
  }
  window.ROLA = { go: go };

  if (veil) {
    requestAnimationFrame(function () { requestAnimationFrame(function () { veil.classList.add("is-loaded"); }); });
    addEventListener("pageshow", function (e) {
      if (e.persisted) { veil.style.transform = ""; veil.classList.add("is-loaded"); }
    });
  }

  document.addEventListener("click", function (e) {
    var a = e.target.closest ? e.target.closest("a[href]") : null;
    if (!a || e.defaultPrevented || a.target === "_blank" || e.metaKey || e.ctrlKey || e.shiftKey) return;
    var href = a.getAttribute("href");
    if (!/^[\w-]+\.html([?#].*)?$/.test(href)) return;
    var page = href.split(/[?#]/)[0];
    if (page === here && href.indexOf("#") > -1) return;   // same page: let the browser scroll
    e.preventDefault();
    go(href);
  });

  /* ---------- Header quick links: current page + sliding highlight ---------- */
  var pill = document.querySelector(".pillnav");
  if (pill) {
    var links = Array.prototype.slice.call(pill.querySelectorAll("a"));
    links.forEach(function (l) {
      var h = l.getAttribute("href");
      if (h === here) l.classList.add("is-current");
    });
    var glider = document.createElement("span");
    glider.className = "pillnav__glider";
    pill.insertBefore(glider, pill.firstChild);
    var current = function () { return links.filter(function (l) { return l.classList.contains("is-current"); })[0]; };
    var moveTo = function (l) {
      links.forEach(function (x) { x.classList.toggle("is-on", x === l); });
      if (!l) { glider.style.opacity = "0"; return; }
      glider.style.opacity = "1";
      glider.style.left = l.offsetLeft + "px";
      glider.style.width = l.offsetWidth + "px";
    };
    links.forEach(function (l) {
      l.addEventListener("mouseenter", function () { moveTo(l); });
      l.addEventListener("focus", function () { moveTo(l); });
    });
    pill.addEventListener("mouseleave", function () { moveTo(current()); });
    moveTo(current());
    addEventListener("resize", function () { moveTo(current()); });
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { moveTo(current()); });
  }

  /* ---------- Photo at the top of the page moves at a slower speed ---------- */
  var par = Array.prototype.slice.call(document.querySelectorAll("[data-parallax]"));
  if (par.length && !reduced) {
    var waiting = false;
    addEventListener("scroll", function () {
      if (waiting) return;
      waiting = true;
      requestAnimationFrame(function () {
        var y = Math.min(window.scrollY, window.innerHeight);
        par.forEach(function (el) { el.style.transform = "translate3d(0," + (y * 0.4).toFixed(1) + "px,0)"; });
        waiting = false;
      });
    }, { passive: true });
  }

  /* ---------- Footer revealed from behind the page (when it fits the screen) ---------- */
  var footer = document.querySelector(".footer");
  var main = document.querySelector("main");
  function fitFooter() {
    if (!footer || !main) return;
    document.body.classList.remove("footer-reveal");
    main.style.marginBottom = "";
    var h = footer.offsetHeight;
    if (!reduced && window.innerWidth > 900 && h <= window.innerHeight) {
      document.body.classList.add("footer-reveal");
      main.style.marginBottom = h + "px";
    }
  }
  fitFooter();
  addEventListener("resize", fitFooter);
  addEventListener("load", fitFooter);

  /* ---------- Menu: the photo follows the section being pointed at ---------- */
  var menuPhoto = document.getElementById("menuPhoto");
  if (menuPhoto) {
    Array.prototype.slice.call(document.querySelectorAll(".menu__main a[data-img]")).forEach(function (a) {
      var show = function () {
        var src = a.getAttribute("data-img");
        if (menuPhoto.getAttribute("src") === src) return;
        menuPhoto.classList.add("is-swapping");
        setTimeout(function () {
          menuPhoto.onload = function () { menuPhoto.classList.remove("is-swapping"); };
          menuPhoto.src = src;
        }, 220);
      };
      a.addEventListener("mouseenter", show);
      a.addEventListener("focus", show);
    });
  }

  /* ---------- Expanding lists with a photo that follows the open row ---------- */
  Array.prototype.slice.call(document.querySelectorAll("[data-rlist]")).forEach(function (list) {
    var img = list.querySelector(".rlist__media img");
    var rows = Array.prototype.slice.call(list.querySelectorAll(".rlist__row"));
    rows.forEach(function (row) {
      row.querySelector(".rlist__head").addEventListener("click", function () {
        var opening = !row.classList.contains("is-open");
        rows.forEach(function (r) {
          r.classList.remove("is-open");
          r.querySelector(".rlist__head").setAttribute("aria-expanded", "false");
        });
        if (!opening) return;
        row.classList.add("is-open");
        row.querySelector(".rlist__head").setAttribute("aria-expanded", "true");
        var src = row.getAttribute("data-img");
        if (img && src && img.getAttribute("src") !== src) {
          img.classList.add("is-swapping");
          setTimeout(function () {
            img.onload = function () { img.classList.remove("is-swapping"); };
            img.style.objectPosition = row.getAttribute("data-pos") || "";
            img.src = src;
          }, 280);
        }
      });
    });
  });
})();
