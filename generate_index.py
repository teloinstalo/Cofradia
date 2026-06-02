#!/usr/bin/env python3
"""Generator for the complete web-cofradia index.html"""
import html

OUT = "/home/juanjo/Documentos/1/35/web-cofradia/index.html"

def esc(t):
    return html.escape(str(t))

def tag(name, attrs=None, content="", self_close=False):
    a = ""
    if attrs:
        for k, v in sorted(attrs.items()) if isinstance(attrs, dict) else attrs:
            a += f' {k}="{esc(v)}"'
    if self_close:
        return f"<{name}{a} />"
    if content == "":
        return f"<{name}{a}></{name}>"
    return f"<{name}{a}>{content}</{name}>"

# Build the document as a list of lines for efficiency
lines = []

def out(s=""):
    lines.append(s)

# ============================================================
out("<!DOCTYPE html>")
out('<html lang="es">')
out("<head>")
out('  <meta charset="UTF-8">')
out('  <meta name="viewport" content="width=device-width, initial-scale=1.0">')
out('  <meta name="description" content="Web oficial de la Cofradía del Santísimo Cristo Resucitado de Montoro (Córdoba). Fundada en 1966. Semana Santa, cultos, noticias, archivo histórico.">')
out('  <meta name="theme-color" content="#8B0000">')
out('  <meta name="color-scheme" content="light">')
out('  <meta property="og:title" content="Cofradía del Santísimo Cristo Resucitado de Montoro">')
out('  <meta property="og:description" content="Cofradía fundada en 1966. Semana Santa de Montoro, Córdoba. Devoción, tradición y cultura cofrade.">')
out('  <meta property="og:image" content="img/logo-200.png">')
out('  <meta property="og:url" content="">')
out('  <meta property="og:type" content="website">')
out('  <meta property="og:locale" content="es_ES">')
out('  <meta name="twitter:card" content="summary_large_image">')
out('  <meta name="twitter:title" content="Cofradía del Santísimo Cristo Resucitado de Montoro">')
out('  <meta name="twitter:description" content="Cofradía fundada en 1966. Semana Santa de Montoro, Córdoba.">')
out('  <meta name="twitter:image" content="img/logo-200.png">')
out('  <title>Cofradía del Santísimo Cristo Resucitado de Montoro</title>')
out('  <link rel="icon" type="image/png" sizes="32x32" href="img/favicon.png">')
out('  <link rel="apple-touch-icon" sizes="180x180" href="img/logo-120.png">')
out('  <link rel="icon" type="image/png" sizes="192x192" href="img/logo-200.png">')
out('  <link rel="preconnect" href="https://fonts.googleapis.com">')
out('  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
out('  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Lato:ital,wght@0,300;0,400;0,700&display=swap" rel="stylesheet">')
out('  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />')
out("  <style>")
out("""
/* ============================================================
   GUÍA DE ESTILO — Cofradía del Santísimo Cristo Resucitado de Montoro
   ============================================================
   Paleta: Rojo #8B0000, Blanco #FFFFFF, Marfil #FFFFF0, Oro #B8860B
   Tipografía: Playfair Display (títulos), Lato (cuerpo)
   Layout: Mobile-first, solo min-width media queries
   Navegación: Sistema de páginas independientes vía hash URLs
   ============================================================ */

:root {
  --red-primary:   #8B0000;
  --red-secondary: #6B0000;
  --gold:          #B8860B;
  --gold-light:    #D4A84B;
  --dark:          #1A1A1A;
  --gray:          #555555;
  --ivory:         #FFFFF0;
  --gray-bg:       #F5F0EB;
  --white:         #FFFFFF;
  --overlay-hero:  rgba(0,0,0,0.55);
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.04), 0 1px 3px rgba(0,0,0,0.06);
  --shadow-md: 0 4px 6px rgba(0,0,0,0.04), 0 2px 4px rgba(0,0,0,0.06);
  --shadow-lg: 0 10px 15px rgba(0,0,0,0.05), 0 4px 6px rgba(0,0,0,0.07);
  --shadow-xl: 0 20px 25px rgba(0,0,0,0.06), 0 10px 10px rgba(0,0,0,0.08);
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --radius-round: 25px;
  --transition-fast: 0.2s ease;
  --transition-normal: 0.3s ease;
  --transition-slow: 0.5s ease;
}

/* Reset & base */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { font-size: 16px; }
body {
  font-family: 'Lato', -apple-system, BlinkMacSystemFont, sans-serif;
  font-weight: 400;
  color: var(--dark);
  background: var(--ivory);
  line-height: 1.6;
  overflow-x: hidden;
  min-height: 100dvh;
}
body::before {
  content: "";
  position: fixed; inset: 0; z-index: -1;
  background-image: url("data:image/svg+xml,%3Csvg width='40' height='40' viewBox='0 0 40 40' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M20 0 L25 15 L40 20 L25 25 L20 40 L15 25 L0 20 L15 15 Z' fill='%238B0000' fill-opacity='0.03'/%3E%3C/svg%3E");
  pointer-events: none;
}
h1,h2,h3,h4,h5,h6 { font-family: 'Playfair Display', Georgia, serif; font-weight: 700; line-height: 1.2; }
a { color: inherit; text-decoration: none; }
img { max-width: 100%; height: auto; display: block; }
button { font-family: inherit; cursor: pointer; border: none; background: none; }
input, textarea, select { font-family: inherit; }

/* Utilities */
.sr-only {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border: 0;
}
.skip-link {
  position: absolute; top: -40px; left: 0;
  background: var(--red-primary); color: var(--white);
  padding: 8px 16px; z-index: 10000;
  transition: top var(--transition-fast);
}
.skip-link:focus { top: 0; }
:focus-visible { outline: 3px solid var(--red-primary); outline-offset: 2px; }

/* Page sections */
.page-section {
  display: none;
  min-height: 100dvh;
  padding: 80px 16px 40px;
  content-visibility: auto;
  contain-intrinsic-size: auto 100vh;
}
.page-section.active {
  display: flex;
  flex-direction: column;
}

/* Typography sizes */
.hero-title { font-size: clamp(2rem, 5vw, 4rem); font-weight: 700; }
.section-title { font-size: clamp(1.6rem, 4vw, 2.8rem); font-weight: 700; color: var(--red-primary); }
h3 { font-size: clamp(1.1rem, 2.5vw, 1.5rem); font-weight: 600; }
p, li { font-size: clamp(0.9rem, 1.5vw, 1rem); }
.small { font-size: clamp(0.75rem, 1.2vw, 0.85rem); }

/* Divider */
.gold-divider {
  width: 60px; height: 3px; background: var(--gold); margin: 12px 0 24px;
}
.gold-divider.center { margin-left: auto; margin-right: auto; }

/* Fade-in animation */
.fade-in { opacity: 0; transform: translateY(20px); transition: opacity 0.6s ease, transform 0.6s ease; }
.fade-in.visible { opacity: 1; transform: translateY(0); }

/* Buttons */
.btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 8px;
  padding: 12px 24px; border-radius: var(--radius-round);
  font-weight: 700; font-size: clamp(0.85rem, 1.4vw, 1rem);
  transition: background var(--transition-fast), transform var(--transition-fast), box-shadow var(--transition-fast);
  position: relative; overflow: hidden;
}
.btn-primary { background: var(--red-primary); color: var(--white); }
.btn-primary:hover { background: var(--red-secondary); transform: translateY(-2px); box-shadow: var(--shadow-md); }
.btn-outline { border: 2px solid currentColor; background: transparent; }
.btn-outline-white { color: var(--white); border-color: var(--white); }
.btn-outline-white:hover { background: var(--white); color: var(--dark); }
.btn-full { width: 100%; }
.btn:disabled { opacity: 0.5; cursor: not-allowed; }

/* Cards */
.card {
  background: var(--white); border-radius: var(--radius-md);
  box-shadow: var(--shadow-md); overflow: hidden;
  transition: transform var(--transition-normal), box-shadow var(--transition-normal);
}
.card:hover { transform: translateY(-4px); box-shadow: var(--shadow-lg); }

/* Grids */
.grid-2 {
  display: grid; gap: 24px; grid-template-columns: 1fr;
}
.grid-3 { display: grid; gap: 24px; grid-template-columns: 1fr; }
.grid-4 { display: grid; gap: 24px; grid-template-columns: 1fr; }

@media (min-width: 640px) {
  .grid-2 { grid-template-columns: repeat(2, 1fr); }
  .grid-3 { grid-template-columns: repeat(2, 1fr); }
}
@media (min-width: 1024px) {
  .grid-3 { grid-template-columns: repeat(3, 1fr); }
  .grid-4 { grid-template-columns: repeat(4, 1fr); }
}

/* Two-column asymmetric layouts */
.two-col {
  display: grid; gap: 32px; grid-template-columns: 1fr;
}
.two-col-1-15 { grid-template-columns: 1fr; }
.two-col-15-1 { grid-template-columns: 1fr; }

@media (min-width: 1024px) {
  .two-col { grid-template-columns: repeat(2, 1fr); }
  .two-col-1-15 { grid-template-columns: 1fr 1.5fr; }
  .two-col-15-1 { grid-template-columns: 1.5fr 1fr; }
}

/* Header */
.site-header {
  position: fixed; top: 0; left: 0; right: 0; z-index: 1000;
  height: 60px; background: rgba(255,255,255,0.95);
  backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(0,0,0,0.05);
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 16px; transition: background var(--transition-normal), box-shadow var(--transition-normal);
}
.site-header.scrolled { background: rgba(255,255,255,0.98); box-shadow: var(--shadow-sm); }
.header-brand {
  display: flex; align-items: center; gap: 12px;
}
.header-brand img { width: 48px; height: 48px; object-fit: contain; }
.header-brand span {
  font-family: 'Playfair Display', Georgia, serif; font-weight: 700;
  color: var(--red-primary); font-size: clamp(0.9rem, 2vw, 1.15rem); line-height: 1.2;
}
.header-actions { display: flex; align-items: center; gap: 12px; }
.cart-btn { position: relative; padding: 8px; font-size: 1.2rem; color: var(--dark); }
.cart-badge {
  position: absolute; top: 2px; right: 2px;
  background: var(--red-primary); color: var(--white);
  font-size: 0.65rem; font-weight: 700;
  width: 18px; height: 18px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
}
.hamburger {
  width: 28px; height: 22px; position: relative; display: flex; flex-direction: column; justify-content: space-between;
}
.hamburger span {
  display: block; width: 100%; height: 3px; background: var(--dark);
  border-radius: 2px; transition: all var(--transition-normal);
  transform-origin: center;
}
.hamburger.active span:nth-child(1) { transform: translateY(9.5px) rotate(45deg); }
.hamburger.active span:nth-child(2) { opacity: 0; }
.hamburger.active span:nth-child(3) { transform: translateY(-9.5px) rotate(-45deg); }

/* Desktop nav */
.desktop-nav { display: none; }
.desktop-nav ul { display: flex; gap: 4px; list-style: none; }
.desktop-nav a {
  padding: 6px 10px; border-radius: var(--radius-sm);
  font-size: clamp(0.78rem, 1vw, 0.9rem); font-weight: 400;
  color: var(--dark); transition: background var(--transition-fast), color var(--transition-fast);
  white-space: nowrap;
}
.desktop-nav a:hover, .desktop-nav a.active { background: var(--red-primary); color: var(--white); }

@media (min-width: 1200px) {
  .site-header { height: 80px; padding: 0 32px; }
  .header-brand img { width: 60px; height: 60px; }
  .hamburger { display: none; }
  .desktop-nav { display: block; }
}

/* Mobile menu */
.mobile-menu {
  position: fixed; top: 0; right: 0; bottom: 0; width: 100%; max-width: 360px;
  background: var(--white); z-index: 1100;
  transform: translateX(100%); transition: transform var(--transition-normal);
  box-shadow: var(--shadow-xl); padding: 80px 24px 24px;
  overflow-y: auto;
}
.mobile-menu.open { transform: translateX(0); }
.mobile-menu-overlay {
  position: fixed; inset: 0; background: rgba(0,0,0,0.5); z-index: 1050;
  opacity: 0; visibility: hidden; transition: opacity var(--transition-normal), visibility var(--transition-normal);
}
.mobile-menu-overlay.open { opacity: 1; visibility: visible; }
.mobile-menu ul { list-style: none; display: flex; flex-direction: column; gap: 4px; }
.mobile-menu a {
  display: block; padding: 12px 16px; border-radius: var(--radius-sm);
  font-size: 1rem; color: var(--dark); transition: background var(--transition-fast);
}
.mobile-menu a:hover, .mobile-menu a.active { background: var(--red-primary); color: var(--white); }

/* Section dots */
.section-dots {
  position: fixed; right: 16px; top: 50%; transform: translateY(-50%);
  z-index: 900; display: none; flex-direction: column; gap: 10px;
}
@media (min-width: 768px) { .section-dots { display: flex; } }
.dot {
  width: 10px; height: 10px; border-radius: 50%; background: rgba(139,0,0,0.25);
  border: 2px solid transparent; cursor: pointer; transition: all var(--transition-fast);
}
.dot:hover, .dot.active { background: var(--red-primary); border-color: var(--gold); transform: scale(1.3); }

/* Hero */
.hero-section {
  position: relative; min-height: 100dvh; justify-content: center; align-items: center;
  text-align: center; color: var(--white); padding: 0 16px;
}
.hero-bg {
  position: absolute; inset: 0; z-index: 0;
  background: url('https://picsum.photos/1920/1080?random=1') center/cover no-repeat;
}
@supports (background-attachment: fixed) {
  .hero-bg { background-attachment: fixed; }
}
.hero-overlay {
  position: absolute; inset: 0; z-index: 1; background: var(--overlay-hero);
}
.hero-content {
  position: relative; z-index: 2; max-width: 900px;
}
.hero-title {
  color: var(--white); text-shadow: 0 2px 10px rgba(0,0,0,0.5);
  margin-bottom: 16px;
}
.hero-subtitle {
  font-family: 'Lato', sans-serif; font-weight: 300; font-style: italic;
  font-size: clamp(1rem, 2.5vw, 1.4rem); color: var(--gold-light);
  margin-bottom: 32px;
}
.hero-ctas { display: flex; gap: 16px; justify-content: center; flex-wrap: wrap; }
.scroll-chevron {
  position: absolute; bottom: 24px; left: 50%; transform: translateX(-50%);
  z-index: 2; font-size: 1.5rem; color: var(--white); opacity: 0.7;
}

/* Bounce chevron */
@media (prefers-reduced-motion: no-preference) {
  @keyframes bounce { 0%, 100% { transform: translateX(-50%) translateY(0); } 50% { transform: translateX(-50%) translateY(10px); } }
  .scroll-chevron { animation: bounce 2s infinite; }
}

/* Stat cards */
.stat-card {
  background: var(--white); border-left: 4px solid var(--red-primary);
  border-radius: var(--radius-md); padding: 20px;
  box-shadow: var(--shadow-sm); transition: transform var(--transition-normal), box-shadow var(--transition-normal);
}
.stat-card:hover { transform: translateY(-3px); box-shadow: var(--shadow-md); }
.stat-card i { font-size: 1.5rem; color: var(--gold); margin-bottom: 8px; }
.stat-number { font-family: 'Playfair Display', serif; font-size: clamp(1.4rem, 3vw, 2rem); font-weight: 700; color: var(--red-primary); }
.stat-label { font-size: clamp(0.75rem, 1.2vw, 0.85rem); color: var(--gray); }

/* Color circles */
.color-circle {
  width: 48px; height: 48px; border-radius: 50%; border: 2px solid var(--gray-bg); box-shadow: var(--shadow-sm);
}

/* Shield image 3D */
.shield-3d { perspective: 800px; }
.shield-3d img {
  transition: transform var(--transition-slow); transform-style: preserve-3d;
  border-radius: var(--radius-md); box-shadow: var(--shadow-lg);
}
.shield-3d:hover img { transform: rotateY(8deg) rotateX(4deg); }

/* Image cards */
.img-card { position: relative; border-radius: var(--radius-md); overflow: hidden; }
.img-card img { width: 100%; height: 300px; object-fit: cover; transition: transform var(--transition-slow); }
.img-card:hover img { transform: scale(1.05); }
.img-card-overlay {
  position: absolute; inset: 0; background: rgba(0,0,0,0.35);
  display: flex; align-items: center; justify-content: center;
  opacity: 0; transition: opacity var(--transition-normal);
}
.img-card:hover .img-card-overlay { opacity: 1; }
.img-card-name {
  position: absolute; bottom: 0; left: 0; right: 0;
  background: linear-gradient(transparent, rgba(0,0,0,0.7));
  color: var(--white); padding: 16px; font-weight: 700;
}
.badge {
  position: absolute; top: 12px; right: 12px;
  background: var(--red-primary); color: var(--white);
  padding: 4px 12px; border-radius: var(--radius-round);
  font-size: clamp(0.7rem, 1vw, 0.8rem); font-weight: 700; text-transform: uppercase;
}

/* Main titular card */
.titular-card { border: 3px solid var(--gold); }
.titular-card img { height: 380px; }

/* Junta cards */
.junta-card { text-align: center; padding: 24px; }
.junta-avatar {
  width: 120px; height: 120px; border-radius: 50%; object-fit: cover;
  border: 3px solid var(--gold); margin: 0 auto 12px;
}
.junta-role { font-style: italic; color: var(--gray); margin-bottom: 4px; }
.junta-name { font-weight: 700; color: var(--dark); }

/* Calendar */
.calendar-widget { background: var(--white); border-radius: var(--radius-md); box-shadow: var(--shadow-md); overflow: hidden; }
.calendar-header {
  background: var(--red-primary); color: var(--white);
  padding: 12px 16px; display: flex; align-items: center; justify-content: space-between;
}
.calendar-header button { color: var(--white); font-size: 1rem; padding: 4px 8px; border-radius: var(--radius-sm); }
.calendar-header button:hover { background: rgba(255,255,255,0.15); }
.calendar-tabs {
  display: flex; border-bottom: 1px solid var(--gray-bg);
}
.calendar-tab {
  flex: 1; padding: 10px; text-align: center; font-size: 0.9rem; font-weight: 600;
  color: var(--gray); background: var(--white); cursor: pointer;
  transition: background var(--transition-fast), color var(--transition-fast);
}
.calendar-tab.active { color: var(--red-primary); border-bottom: 3px solid var(--red-primary); }
.calendar-body { padding: 16px; }
.calendar-grid {
  display: grid; grid-template-columns: repeat(7, 1fr); gap: 4px; text-align: center;
}
.calendar-day-label { font-size: 0.75rem; font-weight: 700; color: var(--gray); padding: 6px 0; text-transform: uppercase; }
.calendar-day {
  padding: 8px 0; border-radius: var(--radius-sm); font-size: 0.9rem; position: relative; cursor: default;
}
.calendar-day.other { color: #bbb; }
.calendar-day.event { background: rgba(139,0,0,0.08); font-weight: 700; color: var(--red-primary); }
.calendar-day.event::after {
  content: ''; position: absolute; bottom: 4px; left: 50%; transform: translateX(-50%);
  width: 5px; height: 5px; border-radius: 50%; background: var(--red-primary);
}
.calendar-list { display: none; }
.calendar-list.active { display: block; }
.event-card {
  display: flex; align-items: flex-start; gap: 12px;
  padding: 12px; border-radius: var(--radius-md); background: var(--gray-bg); margin-bottom: 8px;
}
.event-card i { color: var(--gold); margin-top: 2px; }
.event-card strong { display: block; color: var(--dark); }
.event-card small { color: var(--gray); }

/* Semana Santa stats */
.stat-grid-3 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; }
@media (min-width: 640px) { .stat-grid-3 { grid-template-columns: repeat(3, 1fr); } }
.ss-stat { text-align: center; padding: 20px; background: var(--white); border-radius: var(--radius-md); box-shadow: var(--shadow-sm); }
.ss-stat .icon { font-size: 1.8rem; margin-bottom: 8px; }
.ss-stat .value { font-family: 'Playfair Display', serif; font-size: clamp(1.4rem, 3vw, 2rem); font-weight: 700; color: var(--red-primary); }
.ss-stat .label { font-size: 0.85rem; color: var(--gray); }

/* Forms */
.form-group { margin-bottom: 16px; }
.form-group label { display: block; font-size: 0.9rem; font-weight: 600; margin-bottom: 6px; color: var(--dark); }
.form-group .required { color: var(--red-primary); }
.form-group input, .form-group textarea, .form-group select {
  width: 100%; padding: 12px 14px; border: 1px solid #ddd; border-radius: var(--radius-sm);
  font-size: 1rem; background: var(--white); transition: border-color var(--transition-fast), box-shadow var(--transition-fast);
}
.form-group input:focus, .form-group textarea:focus, .form-group select:focus {
  border-color: var(--red-primary); box-shadow: 0 0 0 3px rgba(139,0,0,0.08); outline: none;
}
.form-group input.error, .form-group textarea.error, .form-group select.error { border-color: var(--red-primary); }
.form-group .error-msg { font-size: 0.8rem; color: var(--red-primary); margin-top: 4px; display: none; }
.form-group .error-msg.show { display: block; }
.form-group input[type="checkbox"] { width: auto; margin-right: 8px; }
.checkbox-row { display: flex; align-items: flex-start; gap: 8px; }

/* News */
.news-filters { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 24px; }
.filter-pill {
  padding: 8px 16px; border-radius: var(--radius-round); border: 1px solid #ddd;
  background: var(--white); color: var(--dark); font-size: 0.85rem; cursor: pointer;
  transition: all var(--transition-fast);
}
.filter-pill:hover, .filter-pill.active { background: var(--red-primary); color: var(--white); border-color: var(--red-primary); }
.news-card { display: flex; flex-direction: column; background: var(--white); border-radius: var(--radius-md); overflow: hidden; box-shadow: var(--shadow-md); transition: transform var(--transition-normal), box-shadow var(--transition-normal); }
.news-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-lg); }
.news-card img { width: 100%; height: 180px; object-fit: cover; }
.news-card-body { padding: 16px; }
.news-badge { display: inline-block; padding: 3px 10px; border-radius: var(--radius-round); background: var(--red-primary); color: var(--white); font-size: 0.7rem; font-weight: 700; text-transform: uppercase; margin-bottom: 8px; }
.news-date { font-size: 0.8rem; color: var(--gray); margin-bottom: 6px; }
.news-title { font-weight: 700; margin-bottom: 8px; color: var(--dark); }
.news-excerpt { font-size: 0.9rem; color: var(--gray); margin-bottom: 12px; }
.news-link { font-weight: 700; color: var(--red-primary); font-size: 0.9rem; }

/* Gallery */
.gallery-tabs { display: flex; gap: 8px; margin-bottom: 24px; border-bottom: 2px solid var(--gray-bg); }
.gallery-tab { padding: 10px 20px; font-weight: 600; color: var(--gray); cursor: pointer; border-bottom: 3px solid transparent; transition: all var(--transition-fast); }
.gallery-tab.active { color: var(--red-primary); border-bottom-color: var(--red-primary); }
.gallery-content { display: none; }
.gallery-content.active { display: block; }
.year-filters { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 16px; }
.galeria-item { position: relative; border-radius: var(--radius-md); overflow: hidden; cursor: pointer; }
.galeria-item img { width: 100%; height: 220px; object-fit: cover; transition: transform var(--transition-slow); }
.galeria-item:hover img { transform: scale(1.08); }
.galeria-item .lupa { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; background: rgba(0,0,0,0.4); opacity: 0; transition: opacity var(--transition-normal); color: var(--white); font-size: 1.5rem; }
.galeria-item:hover .lupa { opacity: 1; }
.video-placeholder { position: relative; width: 100%; padding-top: 56.25%; background: var(--dark); border-radius: var(--radius-md); overflow: hidden; }
.video-placeholder img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.6; }
.video-play { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; }
.video-play button { width: 64px; height: 64px; border-radius: 50%; background: rgba(139,0,0,0.85); color: var(--white); font-size: 1.4rem; display: flex; align-items: center; justify-content: center; transition: transform var(--transition-fast), background var(--transition-fast); }
.video-play button:hover { transform: scale(1.1); background: var(--red-primary); }

/* Lightbox */
.lightbox-modal {
  position: fixed; inset: 0; z-index: 5000;
  background: rgba(0,0,0,0.95); display: none;
  align-items: center; justify-content: center;
}
.lightbox-modal.open { display: flex; }
.lightbox-img { max-width: 90vw; max-height: 85vh; object-fit: contain; border-radius: var(--radius-md); }
.lightbox-close { position: absolute; top: 16px; right: 16px; color: var(--white); font-size: 1.5rem; padding: 8px; z-index: 10; }
.lightbox-prev, .lightbox-next { position: absolute; top: 50%; transform: translateY(-50%); color: var(--white); font-size: 2rem; padding: 16px; z-index: 10; transition: color var(--transition-fast); }
.lightbox-prev:hover, .lightbox-next:hover { color: var(--gold-light); }
.lightbox-prev { left: 8px; }
.lightbox-next { right: 8px; }
.lightbox-counter { position: absolute; bottom: 16px; left: 50%; transform: translateX(-50%); color: var(--white); font-size: 0.9rem; background: rgba(0,0,0,0.5); padding: 6px 14px; border-radius: var(--radius-round); }

/* Tienda */
.tienda-controls { display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 24px; }
.tienda-controls input, .tienda-controls select { padding: 10px 14px; border-radius: var(--radius-sm); border: 1px solid #ddd; font-size: 0.95rem; background: var(--white); }
.tienda-controls input { flex: 1; min-width: 200px; }
.product-card { background: var(--white); border-radius: var(--radius-md); overflow: hidden; box-shadow: var(--shadow-md); transition: transform var(--transition-normal), box-shadow var(--transition-normal); }
.product-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-lg); }
.product-card img { width: 100%; height: 240px; object-fit: cover; }
.product-card-body { padding: 16px; }
.product-name { font-weight: 700; margin-bottom: 4px; }
.product-price { color: var(--red-primary); font-weight: 700; font-size: 1.1rem; margin-bottom: 12px; }

/* Archivo */
.archivo-item { position: relative; border-radius: var(--radius-md); overflow: hidden; box-shadow: var(--shadow-md); }
.archivo-item img { width: 100%; height: 260px; object-fit: cover; filter: sepia(30%); transition: transform var(--transition-slow), filter var(--transition-slow); }
.archivo-item:hover img { transform: scale(1.08); filter: sepia(0%); }
.archivo-year { position: absolute; top: 12px; right: 12px; background: var(--red-primary); color: var(--white); padding: 4px 12px; border-radius: var(--radius-round); font-size: 0.8rem; font-weight: 700; }

/* Cart sidebar */
.cart-sidebar {
  position: fixed; top: 0; right: 0; bottom: 0; width: 100%; max-width: 380px;
  background: var(--white); z-index: 3000;
  transform: translateX(100%); transition: transform var(--transition-normal);
  box-shadow: var(--shadow-xl); display: flex; flex-direction: column;
}
.cart-sidebar.open { transform: translateX(0); }
.cart-header { display: flex; align-items: center; justify-content: space-between; padding: 16px 20px; border-bottom: 1px solid var(--gray-bg); }
.cart-header h3 { margin: 0; font-size: 1.1rem; }
.cart-items { flex: 1; overflow-y: auto; padding: 16px 20px; }
.cart-item { display: flex; align-items: center; gap: 12px; margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid var(--gray-bg); }
.cart-item img { width: 56px; height: 56px; object-fit: cover; border-radius: var(--radius-sm); }
.cart-item-info { flex: 1; }
.cart-item-name { font-weight: 600; font-size: 0.9rem; }
.cart-item-price { color: var(--gray); font-size: 0.8rem; }
.cart-item-qty { display: flex; align-items: center; gap: 8px; margin-top: 4px; }
.cart-item-qty button { width: 24px; height: 24px; border-radius: 50%; background: var(--gray-bg); font-weight: 700; display: flex; align-items: center; justify-content: center; }
.cart-item-remove { color: var(--gray); font-size: 0.8rem; }
.cart-footer { padding: 16px 20px; border-top: 1px solid var(--gray-bg); }
.cart-total { display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem; margin-bottom: 12px; }
.cart-empty { text-align: center; color: var(--gray); padding: 40px 20px; }
.cart-overlay {
  position: fixed; inset: 0; background: rgba(0,0,0,0.4); z-index: 2500;
  opacity: 0; visibility: hidden; transition: opacity var(--transition-normal), visibility var(--transition-normal);
}
.cart-overlay.open { opacity: 1; visibility: visible; }

/* Toasts */
.toast-container {
  position: fixed; z-index: 6000; display: flex; flex-direction: column; gap: 8px;
  top: 80px; right: 16px; width: 320px;
}
@media (min-width: 1024px) { .toast-container { top: auto; bottom: 24px; right: 24px; } }
.toast {
  padding: 14px 18px; border-radius: var(--radius-md); color: var(--white); font-weight: 600; font-size: 0.9rem;
  box-shadow: var(--shadow-lg); transform: translateX(120%); transition: transform 0.4s ease;
  display: flex; align-items: center; gap: 10px;
}
.toast.show { transform: translateX(0); }
.toast-success { background: #2E7D32; }
.toast-error { background: var(--red-primary); }
.toast-info { background: #1565C0; }

/* Footer */
.site-footer {
  background: var(--dark); color: #AAAAAA; border-top: 4px solid var(--gold);
  padding: 48px 16px 0;
}
.footer-grid { display: grid; gap: 32px; grid-template-columns: 1fr; }
@media (min-width: 768px) { .footer-grid { grid-template-columns: repeat(3, 1fr); } }
.footer-col h4 { color: var(--white); font-size: 1rem; margin-bottom: 12px; }
.footer-col p, .footer-col a { font-size: 0.9rem; color: #AAAAAA; line-height: 1.7; }
.footer-col a:hover { color: var(--gold-light); }
.footer-socials { display: flex; gap: 12px; margin-top: 12px; }
.footer-socials a { width: 36px; height: 36px; border-radius: 50%; background: rgba(255,255,255,0.08); display: flex; align-items: center; justify-content: center; color: var(--white); transition: background var(--transition-fast); }
.footer-socials a:hover { background: var(--red-primary); }
.footer-bottom { text-align: center; padding: 20px; margin-top: 32px; border-top: 1px solid rgba(255,255,255,0.08); font-size: 0.8rem; color: #777777; }

/* Section backgrounds */
.bg-ivory { background: var(--ivory); }
.bg-gray { background: var(--gray-bg); }

/* Scrollbar */
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: var(--gray-bg); }
::-webkit-scrollbar-thumb { background: var(--red-primary); border-radius: 4px; }

/* Print */
@media print {
  .site-header, .site-footer, .section-dots, .cart-sidebar, .cart-overlay, .lightbox-modal, .toast-container, .mobile-menu, .mobile-menu-overlay { display: none !important; }
  .page-section { display: block !important; min-height: auto; page-break-inside: avoid; }
}
""")
out("  </style>")
out("</head>")
out("<body>")
out('  <a href="#inicio" class="skip-link">Saltar al contenido principal</a>')

# Header
out('  <header class="site-header" id="site-header">')
out('    <a class="header-brand" href="#inicio" data-nav="inicio">')
out('      <img src="img/logo-60.png" alt="Logo de la Cofradía del Santísimo Cristo Resucitado de Montoro" loading="lazy" decoding="async">')
out('      <span>Cofradía del Santísimo Cristo Resucitado</span>')
out('    </a>')
out('    <nav class="desktop-nav" aria-label="Navegación principal">')
out('      <ul>')
nav_links = [
    ("inicio","Inicio"),("historia","Historia"),("escudo","Escudo"),
    ("imagenes","Imágenes"),("junta","Junta"),("cultos","Cultos"),
    ("semana-santa","Semana Santa"),("hazte-hermano","Hazte Hermano"),
    ("noticias","Noticias"),("galeria","Galería"),("tienda","Tienda"),
    ("archivo","Archivo"),("contacto","Contacto")
]
for nid, ntxt in nav_links:
    out(f'        <li><a href="#{nid}" data-nav="{nid}">{ntxt}</a></li>')
out('      </ul>')
out('    </nav>')
out('    <div class="header-actions">')
out('      <button class="cart-btn" id="cart-toggle" aria-label="Abrir carrito de compras">')
out('        <i class="fas fa-shopping-cart"></i>')
out('        <span class="cart-badge" id="cart-badge" style="display:none">0</span>')
out('      </button>')
out('      <button class="hamburger" id="hamburger" aria-label="Abrir menú de navegación">')
out('        <span></span><span></span><span></span>')
out('      </button>')
out('    </div>')
out('  </header>')

# Mobile menu
out('  <div class="mobile-menu-overlay" id="mobile-overlay"></div>')
out('  <nav class="mobile-menu" id="mobile-menu" aria-label="Navegación principal móvil">')
out('    <ul>')
for nid, ntxt in nav_links:
    out(f'      <li><a href="#{nid}" data-nav="{nid}">{ntxt}</a></li>')
out('    </ul>')
out('  </nav>')

# Section dots
out('  <nav class="section-dots" id="section-dots" aria-label="Navegación rápida de secciones"></nav>')

# Main
out('  <main id="main-content">')

# ============================================================
# 1. INICIO
out('    <section id="inicio" class="page-section hero-section active" aria-label="Portada">')
out('      <div class="hero-bg" role="img" aria-label="Imagen de fondo de la portada"></div>')
out('      <div class="hero-overlay"></div>')
out('      <div class="hero-content fade-in" data-delay="0">')
out('        <h1 class="hero-title">Cofradía del Santísimo Cristo Resucitado de Montoro</h1>')
out('        <p class="hero-subtitle">Fe, tradición y devoción desde 1966 — Montoro, Córdoba</p>')
out('        <div class="hero-ctas">')
out('          <a href="#hazte-hermano" class="btn btn-primary" data-nav="hazte-hermano">Hazte Hermano</a>')
out('          <a href="#semana-santa" class="btn btn-outline btn-outline-white" data-nav="semana-santa">Semana Santa</a>')
out('        </div>')
out('      </div>')
out('      <div class="scroll-chevron" aria-hidden="true"><i class="fas fa-chevron-down"></i></div>')
out('    </section>')

# ============================================================
# 2. HISTORIA
out('    <section id="historia" class="page-section bg-ivory" aria-label="Nuestra Historia">')
out('      <div class="container" style="max-width:1200px;margin:0 auto;width:100%">')
out('        <h2 class="section-title fade-in" data-delay="0">Nuestra Historia</h2>')
out('        <div class="gold-divider fade-in" data-delay="50"></div>')
out('        <div class="two-col">')
out('          <div class="fade-in" data-delay="100">')
out('            <p style="margin-bottom:16px">La Cofradía del Santísimo Cristo Resucitado de Montoro fue fundada en 1966 con el propósito de rendir culto a Jesucristo Resucitado, centro de la fe cristiana. Desde su fundación participa activamente en la vida religiosa y cofrade de la localidad, siendo la encargada de culminar la Semana Santa de Montoro con su salida procesional en la mañana del Domingo de Resurrección. A lo largo de los años ha mantenido su compromiso con la devoción, la formación y la conservación de las tradiciones cofrades de la ciudad.</p>')
out('            <div class="grid-2" style="margin-top:24px">')
stats = [
    ("fas fa-calendar-alt","1966","Fundación"),
    ("fas fa-church","Ermita de Nuestra Señora de Gracia","Sede Canónica"),
    ("fas fa-map-marker-alt","Montoro, Córdoba, España","Ubicación"),
    ("fas fa-palette","Rojo, Blanco, Marfil","Colores corporativos")
]
for i, (icon, num, label) in enumerate(stats):
    out(f'              <div class="stat-card fade-in" data-delay="{150+i*50}">')
    out(f'                <i class="{icon}"></i>')
    out(f'                <div class="stat-number">{num}</div>')
    out(f'                <div class="stat-label">{label}</div>')
    out('              </div>')
out('            </div>')
out('          </div>')
out('          <div class="fade-in" data-delay="200">')
out('            <img src="https://picsum.photos/800/600?random=10" alt="Imagen histórica de la cofradía" style="border-radius:var(--radius-md);box-shadow:var(--shadow-lg);width:100%" loading="lazy" decoding="async">')
out('          </div>')
out('        </div>')
out('      </div>')
out('    </section>')

# ============================================================
# 3. ESCUDO
out('    <section id="escudo" class="page-section bg-gray" aria-label="Escudo y Símbolos">')
out('      <div class="container" style="max-width:1200px;margin:0 auto;width:100%">')
out('        <h2 class="section-title fade-in" data-delay="0">Escudo y Símbolos</h2>')
out('        <div class="gold-divider fade-in" data-delay="50"></div>')
out('        <div class="two-col">')
out('          <div class="fade-in" data-delay="100">')
out('            <p style="margin-bottom:20px">El escudo está formado por una Cruz gloriosa sobre el monte del Calvario, una palma símbolo de la victoria de Cristo sobre la muerte, una bandera con la inscripción \'PAX\', las iniciales marianas y una ornamentación barroca en color rojo característica de la corporación.</p>')
out('            <h3 style="margin-bottom:12px">Colores corporativos</h3>')
out('            <div style="display:flex;gap:16px;flex-wrap:wrap">')
out('              <div style="text-align:center"><div class="color-circle" style="background:#8B0000"></div><small style="color:var(--gray)">#8B0000</small></div>')
out('              <div style="text-align:center"><div class="color-circle" style="background:#FFFFFF;border:1px solid #ddd"></div><small style="color:var(--gray)">#FFFFFF</small></div>')
out('              <div style="text-align:center"><div class="color-circle" style="background:#FFFFF0;border:1px solid #ddd"></div><small style="color:var(--gray)">#FFFFF0</small></div>')
out('            </div>')
out('          </div>')
out('          <div class="shield-3d fade-in" data-delay="200">')
out('            <img src="https://picsum.photos/600/700?random=15" alt="Representación del escudo de la cofradía" loading="lazy" decoding="async">')
out('          </div>')
out('        </div>')
out('      </div>')
out('    </section>')

# ============================================================
# 4. IMÁGENES TITULARES
out('    <section id="imagenes" class="page-section bg-ivory" aria-label="Imágenes Titulares">')
out('      <div class="container" style="max-width:1200px;margin:0 auto;width:100%">')
out('        <h2 class="section-title fade-in" data-delay="0">Imágenes Titulares</h2>')
out('        <div class="gold-divider fade-in" data-delay="50"></div>')
out('        <div class="grid-3">')
out('          <div class="img-card titular-card fade-in" data-delay="100" style="grid-column:1/-1">')
out('            <img src="https://picsum.photos/800/500?random=20" alt="Imagen del Santísimo Cristo Resucitado, titular de la cofradía" loading="lazy" decoding="async">')
out('            <span class="badge">Titular</span>')
out('            <div class="img-card-overlay"><i class="fas fa-expand"></i></div>')
out('            <div class="img-card-name">Santísimo Cristo Resucitado</div>')
out('          </div>')
others = [("Santa María Magdalena",21),("Ángel Anunciador",22),("Romanos",23)]
for i, (name, seed) in enumerate(others):
    out(f'          <div class="img-card fade-in" data-delay="{150+i*50}">')
    out(f'            <img src="https://picsum.photos/600/400?random={seed}" alt="Imagen de {name}" loading="lazy" decoding="async">')
    out('            <div class="img-card-overlay"><i class="fas fa-expand"></i></div>')
    out(f'            <div class="img-card-name">{name}</div>')
    out('          </div>')
out('        </div>')
out('      </div>')
out('    </section>')

# ============================================================
# 5. JUNTA
out('    <section id="junta" class="page-section bg-gray" aria-label="Junta de Gobierno">')
out('      <div class="container" style="max-width:1200px;margin:0 auto;width:100%">')
out('        <h2 class="section-title fade-in" data-delay="0">Junta de Gobierno</h2>')
out('        <div class="gold-divider fade-in" data-delay="50"></div>')
out('        <div class="grid-4">')
members = [
    ("Jorge Samuel Baena Tendero","Hermano Mayor",30),
    ("Modesto Madrid","Secretario",31),
    ("Gema Expósito Hidalgo","Tesorera",32),
    ("Pendientes de nombrar","Vocales",33)
]
for i, (name, role, seed) in enumerate(members):
    out(f'          <div class="card junta-card fade-in" data-delay="{100+i*60}">')
    out(f'            <img src="https://picsum.photos/300/300?random={seed}" alt="Foto de {name}, {role} de la cofradía" class="junta-avatar" loading="lazy" decoding="async">')
    out(f'            <div class="junta-role">{role}</div>')
    out(f'            <div class="junta-name">{name}</div>')
    out('          </div>')
out('        </div>')
out('      </div>')
out('    </section>')

# ============================================================
# 6. CULTOS
out('    <section id="cultos" class="page-section bg-ivory" aria-label="Cultos y Actividades">')
out('      <div class="container" style="max-width:1200px;margin:0 auto;width:100%">')
out('        <h2 class="section-title fade-in" data-delay="0">Cultos y Actividades</h2>')
out('        <div class="gold-divider fade-in" data-delay="50"></div>')
out('        <div class="two-col">')
out('          <div class="fade-in" data-delay="100">')
out('            <h3>Solemne Triduo Pascual</h3>')
out('            <p style="margin:12px 0 16px">El culto principal de la cofradía es el Solemne Triduo en honor al Santísimo Cristo Resucitado, celebrado en los días previos al Domingo de Resurrección. Estas celebraciones constituyen el eje devocional de la corporación y congregan a hermanos y fieles en la Ermita de Nuestra Señora de Gracia.</p>')
out('            <div class="card" style="padding:16px;border-left:4px solid var(--red-primary)">')
out('              <p style="font-size:0.9rem;color:var(--gray)"><i class="fas fa-info-circle" style="color:var(--gold);margin-right:6px"></i>Las fechas específicas del Triduo se actualizan anualmente según el calendario litúrgico. Consulte próximamente el calendario de eventos.</p>')
out('            </div>')
out('          </div>')
out('          <div class="fade-in" data-delay="150">')
out('            <div class="calendar-widget">')
out('              <div class="calendar-header">')
out('                <button id="cal-prev" aria-label="Mes anterior"><i class="fas fa-chevron-left"></i></button>')
out('                <span id="cal-month-year" style="font-weight:700">Abril 2026</span>')
out('                <button id="cal-next" aria-label="Mes siguiente"><i class="fas fa-chevron-right"></i></button>')
out('              </div>')
out('              <div class="calendar-tabs">')
out('                <button class="calendar-tab active" data-cal-tab="calendar">Calendario</button>')
out('                <button class="calendar-tab" data-cal-tab="list">Próximos eventos</button>')
out('              </div>')
out('              <div class="calendar-body">')
out('                <div id="calendar-view" class="calendar-content active">')
out('                  <div class="calendar-grid" id="cal-grid"></div>')
out('                </div>')
out('                <div id="list-view" class="calendar-list">')
out('                  <div class="event-card"><i class="fas fa-calendar-day"></i><div><strong>Primer día del Solemne Triduo</strong><small>10 de abril de 2026</small></div></div>')
out('                  <div class="event-card"><i class="fas fa-calendar-day"></i><div><strong>Segundo día del Solemne Triduo</strong><small>11 de abril de 2026</small></div></div>')
out('                  <div class="event-card"><i class="fas fa-calendar-day"></i><div><strong>Tercer día del Solemne Triduo</strong><small>12 de abril de 2026</small></div></div>')
out('                  <div class="event-card"><i class="fas fa-church"></i><div><strong>Domingo de Resurrección — Estación de Penitencia</strong><small>13 de abril de 2026</small></div></div>')
out('                </div>')
out('              </div>')
out('            </div>')
out('          </div>')
out('        </div>')
out('      </div>')
out('    </section>')

# ============================================================
# 7. SEMANA SANTA
out('    <section id="semana-santa" class="page-section bg-gray" aria-label="Semana Santa">')
out('      <div class="container" style="max-width:1200px;margin:0 auto;width:100%">')
out('        <h2 class="section-title fade-in" data-delay="0">Semana Santa</h2>')
out('        <div class="gold-divider fade-in" data-delay="50"></div>')
out('        <div class="two-col">')
out('          <div class="fade-in" data-delay="100">')
out('            <div class="stat-grid-3" style="margin-bottom:24px">')
ss_stats = [
    ("☀️","Domingo de Resurrección","Día de salida"),
    ("🕐","~10:00 horas","Hora de salida"),
    ("🏛️","1","Paso procesional"),
    ("👥","~60","Nazarenos"),
    ("👥","~90","Costaleros"),
    ("🎵","Agrupación Musical Jesús Caído de Montoro","Acompañamiento")
]
for i, (icon, val, label) in enumerate(ss_stats):
    animate = ' data-animate="1"' if val in ("1","~60","~90") else ''
    out(f'              <div class="ss-stat fade-in" data-delay="{120+i*40}">')
    out(f'                <div class="icon">{icon}</div>')
    out(f'                <div class="value stat-number"{animate}>{val}</div>')
    out(f'                <div class="label">{label}</div>')
    out('              </div>')
out('            </div>')
out('            <div class="card" style="padding:20px;border-left:4px solid var(--gold)">')
out('              <h3 style="margin-bottom:8px"><i class="fas fa-route" style="color:var(--gold);margin-right:8px"></i>Itinerario</h3>')
out('              <p style="font-size:0.9rem;color:var(--gray)">El recorrido procesional se publica anualmente según el itinerario oficial aprobado por la Junta de Gobierno y las autoridades competentes. Se recomienda consultar la programación actualizada antes del Domingo de Resurrección.</p>')
out('            </div>')
out('          </div>')
out('          <div class="fade-in" data-delay="200">')
out('            <img src="https://picsum.photos/800/600?random=40" alt="Mapa del recorrido procesional de la cofradía" style="border-radius:var(--radius-md);box-shadow:var(--shadow-lg);width:100%" loading="lazy" decoding="async">')
out('          </div>')
out('        </div>')
out('      </div>')
out('    </section>')

# ============================================================
# 8. HAZTE HERMANO
out('    <section id="hazte-hermano" class="page-section bg-ivory" aria-label="Hazte Hermano">')
out('      <div class="container" style="max-width:1200px;margin:0 auto;width:100%">')
out('        <h2 class="section-title fade-in" data-delay="0">Hazte Hermano</h2>')
out('        <div class="gold-divider fade-in" data-delay="50"></div>')
out('        <div class="two-col two-col-1-15">')
out('          <div class="fade-in" data-delay="100">')
out('            <p style="margin-bottom:16px">Formar parte de la Cofradía del Santísimo Cristo Resucitado de Montoro es un acto de fe y compromiso con nuestras tradiciones. Los hermanos participan activamente en la vida cofrade, los cultos y la conservación de nuestro patrimonio histórico y religioso.</p>')
out('            <div class="card" style="padding:24px;border:2px solid var(--red-primary);text-align:center">')
out('              <i class="fas fa-euro-sign" style="font-size:2rem;color:var(--red-primary);margin-bottom:12px"></i>')
out('              <div style="font-size:2rem;font-weight:700;color:var(--red-primary)">6 €</div>')
out('              <div style="color:var(--gray)">Cuota anual de hermano</div>')
out('            </div>')
out('          </div>')
out('          <div class="card fade-in" data-delay="150" style="padding:24px">')
out('            <form id="form-hermano" novalidate>')
out('              <div class="form-group"><label>Nombre completo <span class="required">*</span></label><input type="text" name="nombre" autocomplete="name" required></div>')
out('              <div class="form-group"><label>DNI/NIF <span class="required">*</span></label><input type="text" name="dni" required></div>')
out('              <div class="form-group"><label>Fecha de nacimiento</label><input type="date" name="nacimiento" autocomplete="bday"></div>')
out('              <div class="form-group"><label>Dirección</label><input type="text" name="direccion" autocomplete="street-address"></div>')
out('              <div class="form-group"><label>Teléfono</label><input type="tel" name="telefono" autocomplete="tel"></div>')
out('              <div class="form-group"><label>Correo electrónico <span class="required">*</span></label><input type="email" name="email" autocomplete="email" required></div>')
out('              <div class="form-group"><label>Motivo de interés</label><textarea name="interes" rows="3"></textarea></div>')
out('              <div class="form-group"><div class="checkbox-row"><input type="checkbox" name="privacidad" id="priv-hermano" required><label for="priv-hermano" style="margin:0;font-weight:400;font-size:0.9rem">Acepto la política de privacidad <span class="required">*</span></label></div><div class="error-msg">Debes aceptar la política de privacidad</div></div>')
out('              <button type="submit" class="btn btn-primary btn-full">Enviar solicitud</button>')
out('            </form>')
out('          </div>')
out('        </div>')
out('      </div>')
out('    </section>')

# ============================================================
# 9. NOTICIAS
out('    <section id="noticias" class="page-section bg-gray" aria-label="Noticias">')
out('      <div class="container" style="max-width:1200px;margin:0 auto;width:100%">')
out('        <h2 class="section-title fade-in" data-delay="0">Noticias</h2>')
out('        <div class="gold-divider fade-in" data-delay="50"></div>')
out('        <div class="news-filters fade-in" data-delay="100">')
newscats = ["Todas","Cultos","Semana Santa","Patrimonio","Formación","Juventud","Comunicados","Actividades y eventos"]
for c in newscats:
    cls = 'filter-pill active' if c=="Todas" else 'filter-pill'
    out(f'          <button class="{cls}" data-category="{c}">{c}</button>')
out('        </div>')
out('        <div class="grid-3" id="news-grid">')
news_items = [
    ("Estación de Penitencia 2026","Semana Santa","2026-04-15","15 de abril de 2026","La cofradía prepara su salida procesional para el Domingo de Resurrección de 2026. Consulta el itinerario y horarios.",50),
    ("Solemne Triduo Pascual","Cultos","2026-04-10","10 de abril de 2026","Comienzan los cultos en honor al Santísimo Cristo Resucitado con el Solemne Triduo en la Ermita de Nuestra Señora de Gracia.",51),
    ("Restauración del patrimonio cofrade","Patrimonio","2026-03-01","1 de marzo de 2026","Se han iniciado las obras de restauración de elementos del paso procesional y vestimentas nazarenas.",52),
    ("Jornada de formación cofrade para jóvenes","Formación","2026-02-20","20 de febrero de 2026","Jornada dirigida a los jóvenes hermanos para profundizar en el significado de la Semana Santa.",53),
    ("Convivencia de hermanos en la Sierra","Actividades y eventos","2026-01-15","15 de enero de 2026","La cofradía organiza una convivencia de hermanos en la Sierra de Montoro el próximo fin de semana.",54),
    ("Nueva Junta de Gobierno 2026-2030","Comunicados","2025-12-20","20 de diciembre de 2025","Tras las elecciones, se ha constituido la nueva Junta de Gobierno para el cuatrienio 2026-2030.",55),
]
for i, (title, cat, dt, display_date, excerpt, seed) in enumerate(news_items):
    out(f'          <article class="news-card fade-in" data-delay="{120+i*60}" data-category="{cat}">')
    out(f'            <img src="https://picsum.photos/600/400?random={seed}" alt="{title}" loading="lazy" decoding="async">')
    out('            <div class="news-card-body">')
    out(f'              <span class="news-badge">{cat}</span>')
    out(f'              <div class="news-date"><time datetime="{dt}">{display_date}</time></div>')
    out(f'              <h3 class="news-title">{title}</h3>')
    out(f'              <p class="news-excerpt">{excerpt}</p>')
    out('              <a href="#noticias" class="news-link">Leer más →</a>')
    out('            </div>')
    out('          </article>')
out('        </div>')
out('        <div style="text-align:center;margin-top:32px" class="fade-in" data-delay="400"><a href="#noticias" class="btn btn-outline" style="border-color:var(--red-primary);color:var(--red-primary)">Ver todas las noticias</a></div>')
out('      </div>')
out('    </section>')

# ============================================================
# 10. GALERÍA
out('    <section id="galeria" class="page-section bg-ivory" aria-label="Galería Multimedia">')
out('      <div class="container" style="max-width:1200px;margin:0 auto;width:100%">')
out('        <h2 class="section-title fade-in" data-delay="0">Galería Multimedia</h2>')
out('        <div class="gold-divider fade-in" data-delay="50"></div>')
out('        <div class="gallery-tabs fade-in" data-delay="100">')
out('          <button class="gallery-tab active" data-gallery-tab="fotos">Fotografías</button>')
out('          <button class="gallery-tab" data-gallery-tab="videos">Vídeos</button>')
out('          <button class="gallery-tab" data-gallery-tab="archivo">Archivo Histórico</button>')
out('        </div>')
out('        <div class="gallery-content active" id="tab-fotos">')
out('          <div class="year-filters" style="margin-bottom:16px">')
years = ["Todos","2025","2024","2023","2022"]
for y in years:
    cls = 'filter-pill active' if y=="Todos" else 'filter-pill'
    out(f'            <button class="{cls}" data-year="{y}">{y}</button>')
out('          </div>')
out('          <div class="grid-3" id="gallery-grid">')
for i in range(8):
    yr = 2022 + (i % 4)
    out(f'            <div class="galeria-item fade-in" data-delay="{120+i*50}" data-gallery-year="{yr}">')
    out(f'              <img src="https://picsum.photos/600/450?random={60+i}" alt="Fotografía de la cofradía {yr}" loading="lazy" decoding="async">')
    out('              <div class="lupa"><i class="fas fa-search-plus"></i></div>')
    out('            </div>')
out('          </div>')
out('        </div>')
out('        <div class="gallery-content" id="tab-videos">')
out('          <div class="video-placeholder fade-in" data-delay="100">')
out('            <img src="https://picsum.photos/1280/720?random=70" alt="Miniatura del vídeo de la cofradía" loading="lazy" decoding="async">')
out('            <div class="video-play"><button aria-label="Reproducir vídeo"><i class="fas fa-play"></i></button></div>')
out('          </div>')
out('        </div>')
out('        <div class="gallery-content" id="tab-archivo">')
out('          <div class="grid-3">')
for i, yr in enumerate([1980,1995,2005,2015]):
    out(f'            <div class="galeria-item fade-in" data-delay="{100+i*60}">')
    out(f'              <img src="https://picsum.photos/600/450?random={80+i}" alt="Archivo histórico {yr}" loading="lazy" decoding="async">')
    out(f'              <span class="badge" style="top:12px;right:12px">{yr}</span>')
    out('            </div>')
out('          </div>')
out('        </div>')
out('      </div>')
out('    </section>')

# ============================================================
# 11. TIENDA
out('    <section id="tienda" class="page-section bg-gray" aria-label="Tienda Online">')
out('      <div class="container" style="max-width:1200px;margin:0 auto;width:100%">')
out('        <h2 class="section-title fade-in" data-delay="0">Tienda Online</h2>')
out('        <div class="gold-divider fade-in" data-delay="50"></div>')
out('        <div class="tienda-controls fade-in" data-delay="100">')
out('          <input type="text" id="tienda-search" placeholder="Buscar productos...">')
out('          <select id="tienda-category"><option value="">Todas las categorías</option><option value="textil">Textil</option><option value="hogar">Hogar</option><option value="accesorios">Accesorios</option><option value="papeleria">Papelería</option></select>')
out('          <select id="tienda-sort"><option value="">Ordenar por</option><option value="name-asc">Nombre A-Z</option><option value="name-desc">Nombre Z-A</option><option value="price-asc">Precio ascendente</option><option value="price-desc">Precio descendente</option></select>')
out('        </div>')
out('        <div class="grid-3" id="product-grid">')
products = [
    ("Camiseta Cofradía","15,00 €","img/prod-camiseta.jpg","textil"),
    ("Taza conmemorativa","8,00 €","img/prod-taza.jpg","hogar"),
    ("Llavero","5,00 €","img/prod-llavero.jpg","accesorios"),
    ("Postal","2,50 €","img/prod-postal.jpg","papeleria"),
    ("Pulsera","4,00 €","img/prod-pulsera.jpg","accesorios"),
    ("Medalla","12,00 €","img/prod-medalla.jpg","accesorios"),
]
for i, (name, price, img, cat) in enumerate(products):
    out(f'          <div class="product-card fade-in" data-delay="{120+i*60}" data-product-name="{name}" data-product-price="{price}" data-product-cat="{cat}">')
    out(f'            <img src="{img}" alt="{name}" loading="lazy" decoding="async">')
    out('            <div class="product-card-body">')
    out(f'              <div class="product-name">{name}</div>')
    out(f'              <div class="product-price">{price}</div>')
    out(f'              <button class="btn btn-primary btn-full add-to-cart" data-name="{name}" data-price="{price}" data-img="{img}">Añadir al carrito</button>')
    out('            </div>')
    out('          </div>')
out('        </div>')
out('      </div>')
out('    </section>')

# ============================================================
# 12. ARCHIVO
out('    <section id="archivo" class="page-section bg-ivory" aria-label="Archivo Histórico Digital">')
out('      <div class="container" style="max-width:1200px;margin:0 auto;width:100%">')
out('        <h2 class="section-title fade-in" data-delay="0" style="text-align:center">Archivo Histórico Digital</h2>')
out('        <div class="gold-divider center fade-in" data-delay="50"></div>')
out('        <p class="fade-in" data-delay="100" style="text-align:center;max-width:800px;margin:0 auto 32px;color:var(--gray)">La finalidad principal de la página web será servir como plataforma oficial para preservar, documentar y difundir la historia de la Cofradía del Santísimo Cristo Resucitado de Montoro. La web estará orientada especialmente a la divulgación de su patrimonio histórico, artístico, cultural y religioso, permitiendo que hermanos, devotos, investigadores y visitantes puedan conocer la trayectoria y actividad de la corporación.</p>')
out('        <div class="grid-3">')
archive = [(1966,100),(1985,101),(1998,102),(2008,103),(2016,104),(2024,105)]
for i, (yr, seed) in enumerate(archive):
    out(f'          <div class="archivo-item fade-in" data-delay="{120+i*60}">')
    out(f'            <img src="https://picsum.photos/600/450?random={seed+seed}" alt="Fotografía histórica de la cofradía, año {yr}" loading="lazy" decoding="async">')
    out(f'            <span class="archivo-year">{yr}</span>')
    out('          </div>')
out('        </div>')
out('      </div>')
out('    </section>')

# ============================================================
# 13. CONTACTO
out('    <section id="contacto" class="page-section bg-gray" aria-label="Contacto">')
out('      <div class="container" style="max-width:1200px;margin:0 auto;width:100%">')
out('        <h2 class="section-title fade-in" data-delay="0">Contacto</h2>')
out('        <div class="gold-divider fade-in" data-delay="50"></div>')
out('        <div class="two-col two-col-15-1">')
out('          <div class="card fade-in" data-delay="100" style="padding:24px">')
out('            <form id="form-contacto" novalidate>')
out('              <div class="form-group"><label>Nombre <span class="required">*</span></label><input type="text" name="nombre" autocomplete="name" required></div>')
out('              <div class="form-group"><label>Correo electrónico <span class="required">*</span></label><input type="email" name="email" autocomplete="email" required></div>')
out('              <div class="form-group"><label>Asunto</label><input type="text" name="asunto"></div>')
out('              <div class="form-group"><label>Mensaje <span class="required">*</span></label><textarea name="mensaje" rows="4" required></textarea></div>')
out('              <button type="submit" class="btn btn-primary btn-full">Enviar mensaje</button>')
out('            </form>')
out('          </div>')
out('          <div class="card fade-in" data-delay="150" style="padding:24px">')
out('            <h3 style="margin-bottom:16px">Información de contacto</h3>')
out('            <div style="display:flex;flex-direction:column;gap:14px">')
out('              <div style="display:flex;align-items:center;gap:12px"><i class="fas fa-envelope" style="color:var(--gold);width:20px"></i><span>secretaria@cristoresucitadomontoro.es</span></div>')
out('              <div style="display:flex;align-items:center;gap:12px"><i class="fas fa-phone" style="color:var(--gold);width:20px"></i><span>957 16 00 12</span></div>')
out('              <div style="display:flex;align-items:center;gap:12px"><i class="fas fa-map-marker-alt" style="color:var(--gold);width:20px"></i><span>Montoro, Córdoba</span></div>')
out('              <div style="display:flex;align-items:center;gap:12px"><i class="fas fa-users" style="color:var(--gold);width:20px"></i><span>Junta de Gobierno</span></div>')
out('            </div>')
out('            <h3 style="margin:24px 0 12px">Síguenos</h3>')
out('            <div style="display:flex;gap:12px">')
for sicon in ["fab fa-facebook-f","fab fa-instagram","fab fa-x-twitter","fab fa-youtube"]:
    out(f'              <a href="#" style="width:36px;height:36px;border-radius:50%;background:var(--gray-bg);display:flex;align-items:center;justify-content:center;color:var(--dark);transition:background var(--transition-fast),color var(--transition-fast)" aria-label="Red social"><i class="{sicon}"></i></a>')
out('            </div>')
out('          </div>')
out('        </div>')
out('      </div>')
out('    </section>')

out('  </main>')

# Footer
out('  <footer class="site-footer">')
out('    <div class="footer-grid" style="max-width:1200px;margin:0 auto">')
out('      <div class="footer-col">')
out('        <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px">')
out('          <img src="img/logo-50.png" alt="Logo de la cofradía" style="width:40px;height:40px" loading="lazy" decoding="async">')
out('          <span style="color:var(--white);font-weight:700">Cofradía del Santísimo Cristo Resucitado</span>')
out('        </div>')
out('        <p>Cofradía fundada en 1966 en Montoro, Córdoba. Devoción, tradición y cultura cofrade desde hace más de medio siglo.</p>')
out('      </div>')
out('      <div class="footer-col">')
out('        <h4>Enlaces rápidos</h4>')
out('        <ul style="list-style:none;display:flex;flex-direction:column;gap:6px">')
quick = ["Inicio","Historia","Escudo","Imágenes","Junta","Cultos","Semana Santa","Noticias","Contacto"]
for q in quick:
    qid = q.lower().replace(" ","-")
    if qid=="inicio": qid="inicio"
    elif qid=="contacto": qid="contacto"
    elif qid=="escudo": qid="escudo"
    elif qid=="junta": qid="junta"
    elif qid=="cultos": qid="cultos"
    elif qid=="noticias": qid="noticias"
    elif qid=="historia": qid="historia"
    elif qid=="imagenes": qid="imagenes"
    elif qid=="semana-santa": qid="semana-santa"
    out(f'          <li><a href="#{qid}">{q}</a></li>')
out('        </ul>')
out('      </div>')
out('      <div class="footer-col">')
out('        <h4>Contacto</h4>')
out('        <p><i class="fas fa-envelope" style="margin-right:8px;color:var(--gold)"></i>secretaria@cristoresucitadomontoro.es</p>')
out('        <p><i class="fas fa-phone" style="margin-right:8px;color:var(--gold)"></i>957 16 00 12</p>')
out('        <p><i class="fas fa-map-marker-alt" style="margin-right:8px;color:var(--gold)"></i>Montoro, Córdoba, España</p>')
out('        <div class="footer-socials">')
for sicon in ["fab fa-facebook-f","fab fa-instagram","fab fa-x-twitter","fab fa-youtube"]:
    out(f'          <a href="#" aria-label="Red social"><i class="{sicon}"></i></a>')
out('        </div>')
out('      </div>')
out('    </div>')
out('    <div class="footer-bottom">')
out('      © 2026 Cofradía del Santísimo Cristo Resucitado de Montoro — Diseñado con devoción ❤️')
out('    </div>')
out('  </footer>')

# Cart sidebar
out('  <div class="cart-overlay" id="cart-overlay"></div>')
out('  <aside class="cart-sidebar" id="cart-sidebar" aria-label="Carrito de compras">')
out('    <div class="cart-header">')
out('      <h3>Tu carrito</h3>')
out('      <button id="cart-close" aria-label="Cerrar carrito"><i class="fas fa-times"></i></button>')
out('    </div>')
out('    <div class="cart-items" id="cart-items"></div>')
out('    <div class="cart-footer">')
out('      <div class="cart-total"><span>Total:</span><span id="cart-total">0,00 €</span></div>')
out('      <button class="btn btn-primary btn-full" id="cart-checkout" disabled>Finalizar compra</button>')
out('    </div>')
out('  </aside>')

# Lightbox
out('  <div class="lightbox-modal" id="lightbox" role="dialog" aria-label="Visor de imágenes">')
out('    <button class="lightbox-close" id="lb-close" aria-label="Cerrar visor"><i class="fas fa-times"></i></button>')
out('    <button class="lightbox-prev" id="lb-prev" aria-label="Imagen anterior"><i class="fas fa-chevron-left"></i></button>')
out('    <img src="" alt="" class="lightbox-img" id="lb-img">')
out('    <button class="lightbox-next" id="lb-next" aria-label="Imagen siguiente"><i class="fas fa-chevron-right"></i></button>')
out('    <div class="lightbox-counter" id="lb-counter">1 / 8</div>')
out('  </div>')

# Toast container
out('  <div class="toast-container" id="toast-container" aria-live="polite" aria-atomic="true"></div>')

# ============================================================
# JAVASCRIPT
out("  <script>")
out("""
'use strict';
(function() {
  // --- Pages ---
  const pages = ['inicio','historia','escudo','imagenes','junta','cultos','semana-santa','hazte-hermano','noticias','galeria','tienda','archivo','contacto'];
  let currentPage = 'inicio';
  let ssVisited = false;

  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.from((ctx || document).querySelectorAll(sel)); }

  function navigateTo(pageId, push) {
    if (!pages.includes(pageId)) pageId = 'inicio';
    const old = $('#' + currentPage);
    const neu = $('#' + pageId);
    if (old) { old.classList.remove('active'); }
    if (neu) { neu.classList.add('active'); window.scrollTo(0,0); }
    currentPage = pageId;
    $$('a[data-nav], .mobile-menu a, .desktop-nav a').forEach(a => {
      a.classList.toggle('active', a.getAttribute('data-nav') === pageId || a.getAttribute('href') === '#' + pageId);
    });
    $$('.dot').forEach((d,i) => d.classList.toggle('active', pages[i] === pageId));
    if (push !== false) history.pushState(null, '', '#' + pageId);
    triggerFadeIn(neu);
    if (pageId === 'semana-santa' && !ssVisited) { ssVisited = true; runCounters(); }
    closeMobileMenu();
    closeCart();
  }

  function triggerFadeIn(section) {
    if (!section) return;
    const els = section.querySelectorAll('.fade-in');
    els.forEach(el => el.classList.remove('visible'));
    els.forEach(el => {
      const delay = parseInt(el.getAttribute('data-delay') || '0', 10);
      setTimeout(() => el.classList.add('visible'), delay);
    });
  }

  function runCounters() {
    $$('#semana-santa .stat-number[data-animate]').forEach(el => {
      const targetText = el.textContent.trim();
      const num = parseInt(targetText.replace(/\\D/g,''), 10);
      if (isNaN(num)) return;
      let cur = 0;
      const step = Math.max(1, Math.floor(num / 30));
      const interval = setInterval(() => {
        cur += step;
        if (cur >= num) { cur = num; clearInterval(interval); }
        el.textContent = targetText.replace(/[0-9]+/, String(cur));
      }, 33);
    });
  }

  // Hashchange
  window.addEventListener('hashchange', () => {
    const id = location.hash.replace('#','');
    if (id && id !== currentPage) navigateTo(id, false);
  });

  // Nav links
  document.addEventListener('click', e => {
    const a = e.target.closest('a[href^="#"]');
    if (!a) return;
    const id = a.getAttribute('href').replace('#','');
    if (pages.includes(id)) { e.preventDefault(); navigateTo(id); }
  });

  // Section dots
  const dotsNav = $('#section-dots');
  pages.forEach((p,i) => {
    const btn = document.createElement('button');
    btn.className = 'dot' + (p==='inicio'?' active':'');
    btn.setAttribute('aria-label', 'Ir a ' + p);
    btn.addEventListener('click', () => navigateTo(p));
    dotsNav.appendChild(btn);
  });

  // Mobile menu
  const hamburger = $('#hamburger');
  const mobileMenu = $('#mobile-menu');
  const mobileOverlay = $('#mobile-overlay');
  function toggleMobileMenu() { hamburger.classList.toggle('active'); mobileMenu.classList.toggle('open'); mobileOverlay.classList.toggle('open'); }
  function closeMobileMenu() { hamburger.classList.remove('active'); mobileMenu.classList.remove('open'); mobileOverlay.classList.remove('open'); }
  hamburger.addEventListener('click', toggleMobileMenu);
  mobileOverlay.addEventListener('click', closeMobileMenu);
  document.addEventListener('keydown', e => { if (e.key==='Escape') closeMobileMenu(); });
  let touchStartX = 0;
  mobileMenu.addEventListener('touchstart', e => { touchStartX = e.changedTouches[0].screenX; });
  mobileMenu.addEventListener('touchend', e => {
    if (e.changedTouches[0].screenX - touchStartX > 60) closeMobileMenu();
  });

  // Header scroll glass
  const header = $('#site-header');
  window.addEventListener('scroll', () => {
    header.classList.toggle('scrolled', window.scrollY > 10);
  });

  // Keyboard navigation
  document.addEventListener('keydown', e => {
    const tag = document.activeElement && document.activeElement.tagName;
    if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT') return;
    const idx = pages.indexOf(currentPage);
    if (e.key === 'ArrowRight' && idx < pages.length - 1) navigateTo(pages[idx + 1]);
    if (e.key === 'ArrowLeft' && idx > 0) navigateTo(pages[idx - 1]);
  });

  // --- Calendar ---
  const monthNames = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'];
  const dayNames = ['Lun','Mar','Mié','Jue','Vie','Sáb','Dom'];
  let calYear = 2026, calMonth = 3; // April
  const eventDays = [10,11,12,13];
  function renderCalendar() {
    const grid = $('#cal-grid');
    if (!grid) return;
    grid.innerHTML = '';
    dayNames.forEach(d => {
      const el = document.createElement('div'); el.className = 'calendar-day-label'; el.textContent = d; grid.appendChild(el);
    });
    const first = new Date(calYear, calMonth, 1);
    const start = (first.getDay() + 6) % 7;
    const days = new Date(calYear, calMonth + 1, 0).getDate();
    for (let i=0;i<start;i++) { const e=document.createElement('div'); e.className='calendar-day other'; grid.appendChild(e); }
    for (let d=1; d<=days; d++) {
      const e = document.createElement('div');
      e.className = 'calendar-day' + (eventDays.includes(d)?' event':'');
      e.textContent = d;
      grid.appendChild(e);
    }
    $('#cal-month-year').textContent = monthNames[calMonth] + ' ' + calYear;
  }
  renderCalendar();
  $('#cal-prev').addEventListener('click', () => { calMonth--; if (calMonth<0){calMonth=11;calYear--;} renderCalendar(); });
  $('#cal-next').addEventListener('click', () => { calMonth++; if (calMonth>11){calMonth=0;calYear++;} renderCalendar(); });
  $$('.calendar-tab').forEach(t => {
    t.addEventListener('click', () => {
      $$('.calendar-tab').forEach(x => x.classList.remove('active'));
      t.classList.add('active');
      const tab = t.getAttribute('data-cal-tab');
      $('#calendar-view').style.display = tab==='calendar'?'block':'none';
      $('#list-view').style.display = tab==='list'?'block':'none';
    });
  });

  // --- News filter ---
  const newsGrid = $('#news-grid');
  $$('.news-filters .filter-pill').forEach(btn => {
    btn.addEventListener('click', () => {
      $$('.news-filters .filter-pill').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const cat = btn.getAttribute('data-category');
      $$('.news-card').forEach(card => {
        const c = card.getAttribute('data-category');
        const show = cat==='Todas' || c===cat;
        card.style.display = show?'':'none';
        if (show) { card.classList.remove('visible'); setTimeout(()=>card.classList.add('visible'),50); }
      });
    });
  });

  // --- Gallery tabs ---
  $$('.gallery-tab').forEach(t => {
    t.addEventListener('click', () => {
      $$('.gallery-tab').forEach(x => x.classList.remove('active'));
      t.classList.add('active');
      const tab = t.getAttribute('data-gallery-tab');
      $$('.gallery-content').forEach(c => c.classList.remove('active'));
      if (tab==='fotos') $('#tab-fotos').classList.add('active');
      if (tab==='videos') $('#tab-videos').classList.add('active');
      if (tab==='archivo') $('#tab-archivo').classList.add('active');
    });
  });
  $$('#tab-fotos .filter-pill').forEach(btn => {
    btn.addEventListener('click', () => {
      $$('#tab-fotos .filter-pill').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const yr = btn.getAttribute('data-year');
      $$('.galeria-item[data-gallery-year]').forEach(item => {
        const show = yr==='Todos' || item.getAttribute('data-gallery-year')===yr;
        item.style.display = show?'':'none';
      });
    });
  });

  // --- Lightbox ---
  let lbImages = [];
  let lbIndex = 0;
  function openLightbox(src, index, total, caption) {
    const modal = $('#lightbox');
    const img = $('#lb-img');
    lbImages = $$('.galeria-item:visible img');
    lbIndex = index;
    img.src = src;
    img.alt = caption || '';
    $('#lb-counter').textContent = (index+1) + ' / ' + total;
    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
  }
  function closeLightbox() { $('#lightbox').classList.remove('open'); document.body.style.overflow = ''; }
  function lbPrev() { if (!lbImages.length) return; lbIndex = (lbIndex - 1 + lbImages.length) % lbImages.length; updateLb(); }
  function lbNext() { if (!lbImages.length) return; lbIndex = (lbIndex + 1) % lbImages.length; updateLb(); }
  function updateLb() { const img = lbImages[lbIndex]; $('#lb-img').src = img.src; $('#lb-img').alt = img.alt; $('#lb-counter').textContent = (lbIndex+1)+' / '+lbImages.length; }
  document.addEventListener('click', e => {
    const item = e.target.closest('.galeria-item');
    if (item) {
      const visible = $$('.galeria-item:visible');
      const idx = visible.indexOf(item);
      const img = item.querySelector('img');
      openLightbox(img.src, idx, visible.length, img.alt);
    }
  });
  $('#lb-close').addEventListener('click', closeLightbox);
  $('#lb-prev').addEventListener('click', e => { e.stopPropagation(); lbPrev(); });
  $('#lb-next').addEventListener('click', e => { e.stopPropagation(); lbNext(); });
  $('#lightbox').addEventListener('click', e => { if (e.target === $('#lightbox')) closeLightbox(); });
  document.addEventListener('keydown', e => {
    if (!$('#lightbox').classList.contains('open')) return;
    if (e.key==='Escape') closeLightbox();
    if (e.key==='ArrowLeft') lbPrev();
    if (e.key==='ArrowRight') lbNext();
  });

  // --- Cart ---
  const cart = {
    items: [],
    load() { try { const d = localStorage.getItem('cofradia_cart'); if (d) this.items = JSON.parse(d); } catch(e){} },
    save() { localStorage.setItem('cofradia_cart', JSON.stringify(this.items)); },
    add(product) {
      const existing = this.items.find(x => x.name === product.name);
      if (existing) existing.qty += 1; else this.items.push({...product, qty:1});
      this.save(); renderCart(); updateBadge(); showToast('Producto añadido al carrito','success');
    },
    remove(name) { this.items = this.items.filter(x => x.name !== name); this.save(); renderCart(); updateBadge(); },
    updateQuantity(name, delta) {
      const item = this.items.find(x => x.name === name);
      if (!item) return;
      item.qty += delta;
      if (item.qty <= 0) this.remove(name);
      else { this.save(); renderCart(); updateBadge(); }
    },
    getTotal() { return this.items.reduce((s,i) => s + (parseFloat(i.price.replace(',','.').replace(' €','')) * i.qty), 0); },
    getCount() { return this.items.reduce((s,i) => s + i.qty, 0); }
  };
  cart.load();

  function updateBadge() {
    const b = $('#cart-badge');
    const c = cart.getCount();
    b.textContent = c;
    b.style.display = c > 0 ? 'flex' : 'none';
  }
  function renderCart() {
    const container = $('#cart-items');
    if (!cart.items.length) { container.innerHTML = '<div class="cart-empty">Tu carrito está vacío</div>'; }
    else {
      container.innerHTML = cart.items.map(it => {
        const priceNum = parseFloat(it.price.replace(',','.').replace(' €',''));
        return '<div class="cart-item">' +
          '<img src="' + it.img + '" alt="' + it.name + '">' +
          '<div class="cart-item-info">' +
            '<div class="cart-item-name">' + it.name + '</div>' +
            '<div class="cart-item-price">' + it.price + ' / unidad</div>' +
            '<div class="cart-item-qty">' +
              '<button data-cart-minus="' + it.name + '">-</button>' +
              '<span>' + it.qty + '</span>' +
              '<button data-cart-plus="' + it.name + '">+</button>' +
            '</div>' +
          '</div>' +
          '<button class="cart-item-remove" data-cart-remove="' + it.name + '"><i class="fas fa-trash"></i></button>' +
        '</div>';
      }).join('');
    }
    $('#cart-total').textContent = cart.getTotal().toFixed(2).replace('.',',') + ' €';
    $('#cart-checkout').disabled = cart.items.length === 0;
  }
  function openCart() { $('#cart-sidebar').classList.add('open'); $('#cart-overlay').classList.add('open'); document.body.style.overflow='hidden'; }
  function closeCart() { $('#cart-sidebar').classList.remove('open'); $('#cart-overlay').classList.remove('open'); document.body.style.overflow=''; }
  $('#cart-toggle').addEventListener('click', openCart);
  $('#cart-close').addEventListener('click', closeCart);
  $('#cart-overlay').addEventListener('click', closeCart);
  document.addEventListener('keydown', e => { if (e.key==='Escape') closeCart(); });
  document.addEventListener('click', e => {
    const btn = e.target.closest('.add-to-cart');
    if (btn) {
      cart.add({ name: btn.getAttribute('data-name'), price: btn.getAttribute('data-price'), img: btn.getAttribute('data-img') });
      openCart();
    }
    const rm = e.target.closest('[data-cart-remove]');
    if (rm) cart.remove(rm.getAttribute('data-cart-remove'));
    const plus = e.target.closest('[data-cart-plus]');
    if (plus) cart.updateQuantity(plus.getAttribute('data-cart-plus'), 1);
    const minus = e.target.closest('[data-cart-minus]');
    if (minus) cart.updateQuantity(minus.getAttribute('data-cart-minus'), -1);
  });
  updateBadge(); renderCart();

  // --- Toasts ---
  function showToast(msg, type) {
    const container = $('#toast-container');
    const t = document.createElement('div');
    t.className = 'toast toast-' + type;
    const icon = type==='success'?'check-circle':type==='error'?'exclamation-circle':'info-circle';
    t.innerHTML = '<i class="fas fa-' + icon + '"></i> ' + msg;
    container.appendChild(t);
    requestAnimationFrame(() => t.classList.add('show'));
    setTimeout(() => { t.classList.remove('show'); setTimeout(() => t.remove(), 400); }, 3000);
  }

  // --- Forms ---
  function validateField(input) {
    const group = input.closest('.form-group');
    const err = group && group.querySelector('.error-msg');
    let msg = '';
    if (input.required && !input.value.trim()) msg = 'Este campo es obligatorio';
    else if (input.type==='email' && input.value.trim() && !/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(input.value)) msg = 'Introduce un correo electrónico válido';
    if (msg) {
      input.classList.add('error');
      if (err) { err.textContent = msg; err.classList.add('show'); }
      return false;
    } else {
      input.classList.remove('error');
      if (err) err.classList.remove('show');
      return true;
    }
  }
  $$('form').forEach(form => {
    form.addEventListener('submit', e => {
      e.preventDefault();
      let ok = true;
      form.querySelectorAll('input, textarea').forEach(inp => { if (!validateField(inp)) ok = false; });
      if (ok) { showToast('Formulario enviado correctamente', 'success'); form.reset(); }
      else { showToast('Por favor, corrige los errores del formulario', 'error'); }
    });
    form.querySelectorAll('input, textarea').forEach(inp => {
      inp.addEventListener('blur', () => validateField(inp));
      inp.addEventListener('input', () => { if (inp.classList.contains('error')) validateField(inp); });
    });
  });

  // --- Tienda filters ---
  function renderTienda() {
    const q = ($('#tienda-search')?.value || '').toLowerCase();
    const cat = $('#tienda-category')?.value || '';
    const sort = $('#tienda-sort')?.value || '';
    const cards = $$('.product-card');
    let visible = cards.filter(c => {
      const name = c.getAttribute('data-product-name').toLowerCase();
      const ccat = c.getAttribute('data-product-cat');
      return (!q || name.includes(q)) && (!cat || ccat === cat);
    });
    if (sort==='name-asc') visible.sort((a,b) => a.getAttribute('data-product-name').localeCompare(b.getAttribute('data-product-name')));
    if (sort==='name-desc') visible.sort((a,b) => b.getAttribute('data-product-name').localeCompare(a.getAttribute('data-product-name')));
    if (sort==='price-asc') visible.sort((a,b) => parseFloat(a.getAttribute('data-product-price').replace(',','.').replace(' €','')) - parseFloat(b.getAttribute('data-product-price').replace(',','.').replace(' €','')));
    if (sort==='price-desc') visible.sort((a,b) => parseFloat(b.getAttribute('data-product-price').replace(',','.').replace(' €','')) - parseFloat(a.getAttribute('data-product-price').replace(',','.').replace(' €','')));
    cards.forEach(c => c.style.display = 'none');
    visible.forEach(c => c.style.display = '');
  }
  if ($('#tienda-search')) $('#tienda-search').addEventListener('input', renderTienda);
  if ($('#tienda-category')) $('#tienda-category').addEventListener('change', renderTienda);
  if ($('#tienda-sort')) $('#tienda-sort').addEventListener('change', renderTienda);

  // Init
  const initial = location.hash.replace('#','');
  navigateTo(pages.includes(initial)?initial:'inicio', false);

})();
""")
out("  </script>")
out("</body>")
out("</html>")

# Write to file
with open(OUT, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines) + '\n')

print("Generated", OUT)
