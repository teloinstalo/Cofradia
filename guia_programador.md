# Guía Técnica y Cuestionario para el Programador

Esta guía explica conceptos técnicos clave requeridos en la especificación y plantea preguntas sobre la futura integración en WordPress para asegurar que el prototipo estático (`index.html`) facilite al máximo el desarrollo final.

---

## 1. Explicaciones Técnicas de Conceptos Clave

### A. Skip Links (Enlaces de Salto)
* **¿Qué es?** Es un enlace oculto al inicio de la página (`<body>`) pensado para usuarios que navegan con teclado (lectores de pantalla o discapacidades motoras). Su función es saltar el menú de navegación repetitivo directo al contenido principal.
* **Implementación:** Se le da un estilo CSS para que sea invisible por defecto, pero se posicione de forma visible arriba de la pantalla al recibir el foco del teclado (tabulación).
* **Ejemplo CSS/HTML:**
```html
<a href="#contenido-principal" class="skip-link">Saltar al contenido principal</a>
```
```css
.skip-link {
  position: absolute;
  top: -100px;
  left: 0;
  background: var(--red-primary);
  color: white;
  padding: 10px 20px;
  z-index: 1000;
  transition: top 0.2s;
}
.skip-link:focus {
  top: 0; /* Aparece en pantalla cuando se pulsa Tabulador */
}
```

### B. Enrutamiento por Hash en un Solo Archivo (SPA)
* **¿Cómo funciona?** En lugar de recargar archivos `.html` diferentes, tenemos 13 contenedores `<section>` con clase `.page-section`. Todos tienen `display: none` excepto el que coincide con el hash actual de la URL (ejemplo: `localhost:9000/#cultos` hace visible `<section id="cultos">`).
* **JavaScript:** Escucha el evento `hashchange` en la ventana global para cambiar dinámicamente qué sección tiene la clase `.active`, actualizando al mismo tiempo los menús y los section-dots.

### C. Animación con Retraso Escalonado (Staggered Fade-in)
* **¿Cómo funciona?** Para lograr un efecto premium, los elementos dentro de una sección no aparecen todos de golpe. Tienen una clase `.fade-in` y un atributo `data-delay` en milisegundos.
* **JavaScript:** Cuando se activa una página, se aplica una clase `.visible` a los elementos con un `setTimeout` basado en su `data-delay`.
* **CSS:**
```css
.fade-in {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity var(--transition-slow), transform var(--transition-slow);
}
.fade-in.visible {
  opacity: 1;
  transform: translateY(0);
}
```

---

## 2. Preguntas Técnicas para el Programador (WordPress & Entorno)

1. **Gestión de Assets en WordPress:**
   - La demo usará la carpeta `img/` y Picsum Photos. En WordPress, las fotos se subirán a la biblioteca de medios (`wp-content/uploads/`). ¿Vas a compilar las rutas de las imágenes de forma dinámica con funciones de PHP como `get_template_directory_uri()` o las dejarás relativas?

2. **Tienda Online final:**
   - El prototipo simulará un carrito de compras y una lista de productos en JS con `localStorage`. En la web real de WordPress, ¿utilizarás **WooCommerce** o prefieres una integración más ligera con formularios de Bizum/WhatsApp? (Si usas WooCommerce, la maquetación HTML de las cards de productos deberá adaptarse a los hooks estándar de WC).

3. **Estructura de Plantillas (Theme):**
   - Al ser un diseño de página única (Single Page), ¿desarrollarás un tema a medida en WordPress usando un único archivo `page-templates/front-page.php` cargando todo el loop de secciones, o crearás páginas independientes de WordPress y usarás la API REST / Admin-Ajax para cargar el contenido de forma dinámica sin recargar la web?

4. **Formularios de Contacto y Solicitud:**
   - En la demo, los formularios validan con JS y disparan un aviso de éxito (toast). En WordPress, ¿utilizarás plugins como **Contact Form 7** o **Gravity Forms** con llamadas AJAX, o escribirás un procesador de peticiones POST personalizado en el archivo `functions.php`?

5. **Gestión del Calendario en WordPress:**
   - El calendario interactivo de la demo genera dinámicamente los días de un mes y resalta los días con eventos en JS. En WordPress, ¿prefieres que estos eventos se gestionen mediante un tipo de contenido personalizado (Custom Post Type 'eventos') y pasarlos al JS como un objeto JSON, o usarás un plugin como *The Events Calendar*?
