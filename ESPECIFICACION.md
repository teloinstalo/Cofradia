# ESPECIFICACIÓN COMPLETA — Web Cofradía del Santísimo Cristo Resucitado de Montoro

> **Objetivo:** Que otro agente de IA pueda construir desde cero la página web completa
> con esta única especificación, sin necesidad de consultar nada más.
> 
> **Fecha objetivo:** Hoy mismo (demo funcional en 1 hora)
> **Formato de salida:** Un solo archivo `index.html` autocontenido con HTML + CSS + JS embebido

---

## 1. DATOS DE LA COFRADÍA (100% reales, del cuestionario oficial)

### Información general
- **Nombre completo:** Cofradía del Santísimo Cristo Resucitado de Montoro
- **Año de fundación:** 1966
- **Sede canónica:** Ermita de Nuestra Señora de Gracia
- **Ubicación:** Montoro, Córdoba, España
- **Lema oficial:** No dispone
- **Colores corporativos:** Rojo (#8B0000), blanco (#FFFFFF), marfil (#FFFFF0)

### Historia (texto exacto)
"La Cofradía del Santísimo Cristo Resucitado de Montoro fue fundada en 1966 con el propósito de rendir culto a Jesucristo Resucitado, centro de la fe cristiana. Desde su fundación participa activamente en la vida religiosa y cofrade de la localidad, siendo la encargada de culminar la Semana Santa de Montoro con su salida procesional en la mañana del Domingo de Resurrección. A lo largo de los años ha mantenido su compromiso con la devoción, la formación y la conservación de las tradiciones cofrades de la ciudad."

### Escudo oficial (descripción textual)
"El escudo está formado por una Cruz gloriosa sobre el monte del Calvario, una palma símbolo de la victoria de Cristo sobre la muerte, una bandera con la inscripción 'PAX', las iniciales marianas y una ornamentación barroca en color rojo característica de la corporación."

### Imágenes titulares y grupo escultórico
- **Titular:** Santísimo Cristo Resucitado
- **Grupo escultórico:**
  - Santa María Magdalena
  - Ángel Anunciador
  - Romanos

### Junta de Gobierno (nombres reales)
- **Hermano Mayor:** Jorge Samuel Baena Tendero
- **Secretario:** Modesto Madrid
- **Tesorera:** Gema Expósito Hidalgo
- **Vocales:** Pendiente de completar

### Cultos y actividades
- **Culto principal:** Solemne Triduo en honor al Santísimo Cristo Resucitado
- **Fechas importantes:** Las correspondientes al Triduo y al Domingo de Resurrección (se actualizan anualmente)
- **Actividades benéficas:** Pendiente de especificar
- **Convivencias y eventos:** Sí, según programación anual
- **Calendario de eventos:** Sí, se desea incluir

### Semana Santa
- **Día de procesión:** Domingo de Resurrección
- **Hora de salida:** ~10:00 horas
- **Nº de pasos:** 1 paso procesional
- **Nazarenos:** Alrededor de 60
- **Costaleros:** Alrededor de 90
- **Acompañamiento musical:** Agrupación Musical Jesús Caído de Montoro
- **Itinerario:** Se publica anualmente según recorrido oficial aprobado

### Hazte Hermano
- **Cuota anual:** 6 €
- **Proceso:** Formulario online en la web (sin descargas)
- **Se desea:** Solicitud de información online

### Contacto
- **Email:** Pendiente de creación — usar ficticio: secretaria@cristoresucitadomontoro.es
- **Teléfono:** Pendiente — usar ficticio: 957 16 00 12
- **Dirección postal:** Montoro, Córdoba
- **Redes sociales:** Actualmente sin perfiles activos. Mostrar iconos sin enlaces reales.
- **Responsable de consultas:** La Junta de Gobierno

### Tienda Online
- Se desea vender: merchandising, recuerdos, artículos promocionales y productos propios
- **Productos a mostrar:**
  1. Camiseta Cofradía — 15,00 €
  2. Taza conmemorativa — 8,00 €
  3. Llavero — 5,00 €
  4. Postal — 2,50 €
  5. Pulsera — 4,00 €
  6. Medalla — 12,00 €

### Noticias — Categorías deseadas
Todas, Cultos, Semana Santa, Patrimonio, Formación, Juventud, Comunicados, Actividades y eventos

### Archivo histórico
- Sí, se desea archivo histórico digital
- Fotografías antiguas digitalizadas que se incorporarán progresivamente

### Objetivo principal de la web (texto literal de la cofradía)
"La finalidad principal de la página web será servir como plataforma oficial para preservar, documentar y difundir la historia de la Cofradía del Santísimo Cristo Resucitado de Montoro. La web estará orientada especialmente a la divulgación de su patrimonio histórico, artístico, cultural y religioso, permitiendo que hermanos, devotos, investigadores y visitantes puedan conocer la trayectoria y actividad de la corporación."

**Funciones complementarias:**
- Facilitar la incorporación de nuevos hermanos mediante formularios online
- Informar sobre cultos, actos y actividades
- Publicar noticias y comunicados oficiales
- Crear un archivo histórico digital accesible
- Mostrar galerías fotográficas y audiovisuales
- Difundir el patrimonio y la identidad de la corporación
- Tienda online para merchandising y artículos oficiales

### Estilo deseado
- **Mixto:** Combinar tradición cofrade con imagen moderna y accesible
- **Colores:** Rojo, blanco y marfil (identidad corporativa)
- **Imagen a transmitir:** Seriedad, cercanía, tradición, fe, historia, transparencia y compromiso

---

## 2. DISEÑO VISUAL (ESPECIFICACIONES TÉCNICAS)

### 2.1 Paleta de colores
```
--red-primary:    #8B0000  (principal: botones, títulos, acentos, badges)
--red-secondary:  #6B0000  (hover de botones, estados activos)
--gold:           #B8860B  (divisores decorativos, iconos - NO para texto)
--gold-light:     #D4A84B  (hover dorado, subtitle del hero)
--dark:           #1A1A1A  (texto principal)
--gray:           #555555  (texto secundario, labels, fechas)
--ivory:          #FFFFF0  (fondo principal de secciones)
--gray-bg:        #F5F0EB  (fondo alternativo de secciones pares)
--white:          #FFFFFF  (cards, header, fondo base)
--overlay-hero:   rgba(0,0,0,0.55)
```

### 2.2 Tipografía
- **Títulos (headings):** 'Playfair Display', Georgia, serif — Pesos 400, 600, 700
- **Cuerpo (body):** 'Lato', -apple-system, sans-serif — Pesos 300, 400, 700
- **Fuentes:** Cargar desde Google Fonts vía `<link>` en el `<head>`
  ```
  https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Lato:ital,wght@0,300;0,400;0,700&display=swap
  ```

### 2.3 Tamaños tipográficos (usar clamp() para responsividad)
- **h1 / hero-title:** clamp(2rem, 5vw, 4rem) — weight 700
- **h2 / section-title:** clamp(1.6rem, 4vw, 2.8rem) — weight 700, color rojo
- **h3:** clamp(1.1rem, 2.5vw, 1.5rem) — weight 600
- **body:** clamp(0.9rem, 1.5vw, 1rem) — line-height 1.6
- **small / badges:** clamp(0.75rem, 1.2vw, 0.85rem)

### 2.4 Sombras (sistema multicapa, más profesional)
```
--shadow-sm: 0 1px 2px rgba(0,0,0,0.04), 0 1px 3px rgba(0,0,0,0.06)
--shadow-md: 0 4px 6px rgba(0,0,0,0.04), 0 2px 4px rgba(0,0,0,0.06)
--shadow-lg: 0 10px 15px rgba(0,0,0,0.05), 0 4px 6px rgba(0,0,0,0.07)
--shadow-xl: 0 20px 25px rgba(0,0,0,0.06), 0 10px 10px rgba(0,0,0,0.08)
```

### 2.5 Bordes redondeados
```
--radius-sm: 6px    (inputs, botones pequeños, badges)
--radius-md: 10px   (cards, imágenes, contenedores)
--radius-lg: 16px   (modales)
--radius-round: 25px (pills, botones de filtro)
```

### 2.6 Transiciones
```
--transition-fast: 0.2s ease
--transition-normal: 0.3s ease
--transition-slow: 0.5s ease
```

### 2.7 Breakpoints (mobile-first, solo min-width)
- 480px — teléfonos landscape
- 640px — tablets pequeñas
- 768px — tablets
- 1024px — desktop pequeño
- 1200px — desktop

### 2.8 Iconografía
- Usar Font Awesome 6.5.1 CDN: `https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css`

---

## 3. ARQUITECTURA DE NAVEGACIÓN (¡IMPORTANTE!)

**NO es scroll.** Es un sistema de **páginas independientes** dentro del mismo HTML.

### Cómo funciona:
- Solo **1 sección visible a la vez**
- El resto de secciones están ocultas (`display: none`)
- Al hacer clic en un enlace del menú → se oculta la sección actual, se muestra la nueva
- La URL se actualiza con hash: `#inicio`, `#historia`, `#imagenes`, etc.
- El botón atrás/adelante del navegador funciona (hashchange)
- Flechas ← → del teclado navegan entre páginas
- Puntos de navegación laterales (section-dots) fijos a la derecha
- Cada cambio de página activa animación fade-in en los elementos de esa página

### Secciones (13 páginas en este orden):
1. `#inicio` — Hero / Portada
2. `#historia` — Nuestra Historia
3. `#escudo` — Escudo y Símbolos
4. `#imagenes` — Imágenes Titulares
5. `#junta` — Junta de Gobierno
6. `#cultos` — Cultos y Actividades
7. `#semana-santa` — Semana Santa
8. `#hazte-hermano` — Hazte Hermano
9. `#noticias` — Noticias
10. `#galeria` — Galería Multimedia
11. `#tienda` — Tienda Online
12. `#archivo` — Archivo Histórico Digital
13. `#contacto` — Contacto

---

## 4. DESCRIPCIÓN DETALLADA DE CADA SECCIÓN

### 4.1 HEADER (sticky, visible siempre)
- Posición fija arriba (sticky), altura 60px móvil / 80px desktop
- Fondo blanco con glassmorfismo al hacer scroll: `backdrop-filter: blur(10px)`
- **Logo:** Imagen `img/logo-60.png` (60x60px) + nombre de la cofradía en Playfair Display rojo
- **Menú de navegación:** 12 enlaces en horizontal (desktop) / menú hamburguesa full-screen deslizando desde la derecha (móvil)
- **Icono de carrito** con contador de productos (badge circular rojo)
- El menú móvil debe cerrarse al hacer clic en un enlace, al hacer swipe derecha, al pulsar Escape, o al hacer clic en el overlay oscuro

### 4.2 HERO (#inicio)
- Ocupa el 100% de la ventana (100vh / 100dvh)
- Imagen de fondo con `background-size: cover` + parallax sutil (`background-attachment: fixed` dentro de `@supports`)
- Overlay oscuro semitransparente
- **Título:** "Cofradía del Santísimo Cristo Resucitado de Montoro" en Playfair Display, blanco, con text-shadow
- **Subtítulo:** "Fe, tradición y devoción desde 1966 — Montoro, Córdoba" en Lato light italic, color dorado claro
- **Botones CTA:** "Hazte Hermano" (rojo, principal) + "Semana Santa" (outline blanco)
- Indicador de scroll animado (chevron bouncing) abajo — decorativo

### 4.3 HISTORIA (#historia)
- Fondo marfil
- Título "Nuestra Historia" con divisor dorado debajo
- Layout 2 columnas en desktop:
  - Columna izquierda: texto histórico + 4 tarjetas de datos (Fundación: 1966, Sede Canónica, Ubicación, Colores)
  - Columna derecha: imagen placeholder
- Las tarjetas de datos tienen borde izquierdo rojo de 4px, icono arriba, número/dato grande en rojo, etiqueta pequeña

### 4.4 ESCUDO Y SÍMBOLOS (#escudo)
- Fondo gris claro (alternativo)
- Título "Escudo y Símbolos" con divisor dorado
- Layout 2 columnas en desktop:
  - Columna izquierda: descripción textual del escudo + paleta de colores con 3 círculos (rojo, blanco, marfil) y sus códigos hex
  - Columna derecha: imagen placeholder del escudo con efecto 3D al hover (`perspective` + `rotateY`)
- En móvil: imagen arriba, texto debajo

### 4.5 IMÁGENES TITULARES (#imagenes)
- Fondo marfil
- Título "Imágenes Titulares"
- Grid de 4 cards:
  - **Card principal** (Cristo Resucitado): más grande/destacada, con borde dorado, badge "Titular" superpuesto
  - **3 cards secundarias** (María Magdalena, Ángel Anunciador, Romanos): mismo tamaño
- Cada card: imagen con overlay hover, nombre debajo
- Grid: 1 col móvil → 2 cols tablet → 3 cols desktop

### 4.6 JUNTA DE GOBIERNO (#junta)
- Fondo gris claro
- Título "Junta de Gobierno"
- Grid de 4 cards con:
  - Avatar circular (120px) con borde dorado de 3px
  - Cargo en itálica gris (Hermano Mayor, Secretario, Tesorera, Vocales)
  - Nombre completo en negrita
- Grid: 1 col móvil → 2 cols tablet → 4 cols desktop

### 4.7 CULTOS Y ACTIVIDADES (#cultos)
- Fondo marfil
- Título "Cultos y Actividades"
- Layout 2 columnas en desktop:
  - Columna izquierda: descripción del Solemne Triduo + nota de actualización anual
  - Columna derecha: componente de calendario/eventos con:
    - Pestañas "Calendario" / "Próximos eventos"
    - Vista calendario: mes actual con días destacados (10-13 abril) con puntito rojo
    - Vista lista: 4 eventos del Triduo (días 1, 2, 3) + Domingo de Resurrección
    - Flechas para cambiar de mes
    - Cabecera del calendario en rojo

### 4.8 SEMANA SANTA (#semana-santa)
- Fondo gris claro
- Título "Semana Santa"
- Layout 2 columnas en desktop:
  - Columna izquierda: grid de 6 stats con icono + dato + etiqueta:
    1. ☀️ Domingo de Resurrección — Día de salida
    2. 🕐 ~10:00 horas — Hora de salida
    3. 🏛️ 1 — Paso procesional
    4. 👥 ~60 — Nazarenos
    5. 👥 ~90 — Costaleros
    6. 🎵 Agrupación Musical Jesús Caído de Montoro — Acompañamiento
  - Debajo de los stats: tarjeta de itinerario con nota de actualización anual
  - Columna derecha: imagen placeholder de mapa de recorrido
- **Animación de contadores:** Al entrar en esta página, los números (1, 60, 90) hacen animación de conteo desde 0 hasta su valor. Solo se ejecuta la primera vez que se visita la página.

### 4.9 HAZTE HERMANO (#hazte-hermano)
- Fondo marfil
- Título "Hazte Hermano"
- Layout 2 columnas (1fr / 1.5fr):
  - Columna izquierda: texto descriptivo + tarjeta de cuota anual (6€) con borde rojo e icono €
  - Columna derecha: formulario con campos:
    - Nombre completo * (autocomplete="name")
    - DNI/NIF *
    - Fecha de nacimiento (autocomplete="bday")
    - Dirección (autocomplete="street-address")
    - Teléfono (autocomplete="tel")
    - Correo electrónico * (autocomplete="email")
    - Motivo de interés (textarea)
    - Checkbox de aceptación de política de privacidad *
    - Botón "Enviar solicitud" (rojo, full width)
  - Validación: campos requeridos, formato email, mensajes de error en rojo
  - Al enviar correctamente: toast verde de éxito + limpiar formulario

### 4.10 NOTICIAS (#noticias)
- Fondo gris claro
- Título "Noticias"
- **Filtros:** 8 botones pill (Todas, Cultos, Semana Santa, Patrimonio, Formación, Juventud, Comunicados, Actividades y eventos). El botón activo tiene fondo rojo. Al hacer clic se filtran las noticias con animación fade.
- **Grid de noticias (6 noticias):**
  1. "Estación de Penitencia 2026" — 15 abril 2026 — categoría Semana Santa
  2. "Solemne Triduo Pascual" — 10 abril 2026 — categoría Cultos
  3. "Restauración del patrimonio cofrade" — 1 marzo 2026 — categoría Patrimonio
  4. "Jornada de formación cofrade para jóvenes" — 20 febrero 2026 — categoría Formación
  5. "Convivencia de hermanos en la Sierra" — 15 enero 2026 — categoría Actividades
  6. "Nueva Junta de Gobierno 2026-2030" — 20 diciembre 2025 — categoría Comunicados
- Cada noticia: imagen, badge de categoría, fecha con `<time datetime>`, título, extracto, enlace "Leer más →"
- Grid: 1 col móvil → 2 cols tablet → 3 cols desktop
- Al final: botón outline "Ver todas las noticias"

### 4.11 GALERÍA MULTIMEDIA (#galeria)
- Fondo marfil
- Título "Galería Multimedia"
- **3 pestañas (tabs):** Fotografías | Vídeos | Archivo Histórico
- **Pestaña Fotografías:** grid de 8 imágenes con:
  - Filtro por año (botones pill arriba)
  - Cada imagen con overlay de lupa al hover
  - Click abre lightbox a pantalla completa con navegación (prev/next, teclado, botón X, click fuera)
- **Pestaña Vídeos:** placeholder de reproductor 16:9 con botón de play centrado
- **Pestaña Archivo Histórico:** 4 miniaturas con etiqueta del año superpuesta

### 4.12 TIENDA ONLINE (#tienda)
- Fondo gris claro
- Título "Tienda Online"
- **Controles:** buscador de texto + selector de categoría + selector de ordenación (nombre A-Z, precio ascendente/descendente)
- **Grid de 6 productos:**
  1. Camiseta Cofradía — 15,00 € — img/prod-camiseta.jpg
  2. Taza conmemorativa — 8,00 € — img/prod-taza.jpg
  3. Llavero — 5,00 € — img/prod-llavero.jpg
  4. Postal — 2,50 € — img/prod-postal.jpg
  5. Pulsera — 4,00 € — img/prod-pulsera.jpg
  6. Medalla — 12,00 € — img/prod-medalla.jpg
- Cada producto: imagen (object-fit cover, 240px alto), nombre, precio en rojo, botón "Añadir al carrito"
- Grid: 1 col móvil → 2 cols tablet → 3 cols desktop

### 4.13 CARRITO DE COMPRAS (sidebar)
- Se abre desde la derecha al añadir un producto o al hacer clic en el icono del carrito
- Overlay oscuro detrás
- Lista de items con: nombre, precio unitario, controles +/−, botón eliminar
- Total calculado automáticamente
- Botón "Finalizar compra" (deshabilitado si vacío)
- **Persistencia:** guardar carrito en localStorage, recuperar al cargar la página
- **Toasts:** notificación verde al añadir producto
- En móvil: ancho completo; en desktop: 380px fijos

### 4.14 ARCHIVO HISTÓRICO DIGITAL (#archivo)
- Fondo marfil
- Título "Archivo Histórico Digital"
- Texto introductorio centrado (max 800px)
- Grid de 6 items con:
  - Imagen con filtro sepia al 30% (se quita al hacer hover)
  - Etiqueta del año en la esquina superior derecha (badge rojo)
  - Hover: zoom a la imagen + quitar sepia
- Grid: 1 col móvil → 2 cols tablet → 3 cols desktop

### 4.15 CONTACTO (#contacto)
- Fondo gris claro
- Título "Contacto"
- Layout 2 columnas (1.5fr / 1fr):
  - Columna izquierda: formulario en tarjeta blanca con:
    - Nombre * (autocomplete="name")
    - Correo electrónico * (autocomplete="email")
    - Asunto
    - Mensaje * (textarea)
    - Botón "Enviar mensaje"
    - Misma validación que el formulario de hermanos
  - Columna derecha: tarjeta de información con:
    - ✉️ Email: secretaria@cristoresucitadomontoro.es
    - 📞 Teléfono: 957 16 00 12
    - 📍 Dirección: Montoro, Córdoba
    - #️⃣ Redes sociales: iconos de FB, Instagram, X, YouTube (sin href real, con #)
    - 👔 Responsable: Junta de Gobierno

### 4.16 FOOTER
- Fondo oscuro (#1A1A1A) con borde superior dorado de 4px
- 3 columnas:
  - **Columna 1:** logo pequeño + nombre cofradía + descripción breve
  - **Columna 2:** enlaces rápidos (8-10 principales)
  - **Columna 3:** datos de contacto con iconos
- Barra inferior: copyright 2026 + "Diseñado con devoción ❤️"
- Texto en grises claros (#AAAAAA, #777777)

### 4.17 COMPONENTES GLOBALES
- **Skip link:** "Saltar al contenido principal", visible solo al hacer focus (teclado), primer elemento del body
- **Section dots:** navegación por puntos fija a la derecha (escritorio), oculta en móvil
- **Toast container:** notificaciones flotantes abajo-derecha (escritorio) / arriba-derecha (móvil)
- **Lightbox modal:** a pantalla completa, fondo negro 95% opaco, navegación con flechas y teclado
- **Scroll to top:** NO necesario (cada página ocupa 100vh, no hay scroll largo)

---

## 5. FUNCIONALIDAD JAVASCRIPT REQUERIDA

Todo el JS debe estar en un único bloque `<script>` al final del `<body>`, en modo estricto, dentro de una IIFE.

### 5.1 Sistema de páginas (NAVEGACIÓN PRINCIPAL)
- Array con los IDs de las 13 páginas en orden
- Variable `currentPage` que rastrea la página activa
- Función `navigateTo(pageId)`:
  - Oculta la página actual (remove `active`, opacity 0)
  - Muestra la nueva página (add `active`, opacity 1 con requestAnimationFrame)
  - Actualiza `currentPage`
  - Actualiza clase `active` en los nav-links
  - Actualiza clase `active` en los section-dots
  - Actualiza URL con `history.pushState` (hash)
  - Si la página es `#semana-santa`, dispara animación de contadores
  - Dispara animación fade-in de los elementos de la nueva página
- Event listeners en nav-links para llamar a `navigateTo`
- Listener de `hashchange` para navegación con botones del navegador
- Al iniciar: leer hash de la URL o mostrar `#inicio` por defecto
- Cerrar menú móvil al navegar

### 5.2 Menú móvil
- Hamburguesa animada (3 líneas → X)
- Overlay oscuro con fade
- Swipe derecha para cerrar (>60px)
- Escape para cerrar
- Click en overlay para cerrar
- Click en cualquier nav-link para cerrar y navegar

### 5.3 Animaciones fade-in
- Al cargar/activar una página: todos los elementos con clase `.fade-in` dentro de esa sección se animan secuencialmente
- Cada elemento tiene un `data-delay` (0ms, 80ms, 160ms...) para efecto stagger
- Al cambiar de página: primero se quitan todas las clases `.visible`, luego se añaden con delay

### 5.4 Contadores animados (Semana Santa)
- Solo la primera vez que se entra en `#semana-santa`
- Los elementos `.stat-number` que empiecen con dígito (1, 60, 90) animan de 0 a su valor
- Animación con setInterval (~1 segundo de duración)

### 5.5 Carrito de compras
- Objeto `cart` con: items[], load(), save(), add(), remove(), updateQuantity(), getTotal(), getCount()
- Persistencia en localStorage (`cofradia_cart`)
- Renderizado dinámico del sidebar
- Contador en el icono del header
- Listeners para botones +/−, eliminar, añadir al carrito
- Abrir/cerrar sidebar con animación
- Escape y click en overlay para cerrar

### 5.6 Lightbox
- Detectar click en `.galeria-item`
- Mostrar modal con imagen a tamaño completo
- Navegación: botones prev/next, flechas teclado, Escape, click fuera
- Contador: "3 / 8 — pie de foto"

### 5.7 Filtros de noticias
- 8 botones de categoría
- Al hacer clic: mostrar solo noticias con `data-category` coincidente
- Animación fade entre filtros
- Botón "Todas" muestra todas

### 5.8 Pestañas de galería
- 3 tabs: Fotografías, Vídeos, Archivo Histórico
- Solo se muestra el contenido del tab activo
- Filtro por año en la pestaña de Fotografías

### 5.9 Formularios
- Validación en tiempo real (blur e input)
- Campos required muestran error "Este campo es obligatorio"
- Email inválido muestra "Introduce un correo electrónico válido"
- Borde rojo en campos con error
- Al enviar: toast verde + limpiar formulario
- `autocomplete` correcto en todos los campos

### 5.10 Sistema de toasts
- Cola de notificaciones (se muestran de una en una)
- Tipos: success (verde), error (rojo), info (azul)
- Animación slide-in desde la derecha
- Auto-dismiss a los 3 segundos

### 5.11 Calendario de eventos
- Generar vista de mes con días
- Navegación entre meses (flechas)
- Días con evento: fondo resaltado + puntito rojo
- Vista alternativa de lista con los 4 eventos en tarjetas
- Fechas: 10, 11, 12, 13 de abril de 2026
- Nombres de meses y días en español

### 5.12 Tienda (buscador y filtros)
- Buscador por texto (filtra por nombre)
- Selector de categoría (todas, textil, hogar, accesorios, papelería)
- Selector de orden (defecto, nombre A-Z/Z-A, precio ascendente/descendente)
- Re-renderizado dinámico al cambiar cualquier filtro

### 5.13 Navegación por teclado
- Flecha derecha → siguiente página
- Flecha izquierda → página anterior
- Ignorar si el foco está en input/textarea/select

### 5.14 Section dots
- Generados dinámicamente por JS
- 13 puntos, uno por página
- Click en un punto → navegar a esa página
- El punto de la página actual se ilumina en rojo
- Visibles solo en desktop (≥768px)

---

## 6. ACCESIBILIDAD

- **Skip link:** primer elemento del body, visible al focus
- **`role="img"` y `aria-label`** en el div con background-image del hero
- **`aria-label`** en: hamburger button, cart icon, lightbox buttons, section dots
- **`aria-label="Navegación principal"`** en el nav principal
- **`aria-label="Navegación rápida de secciones"`** en section-dots
- **Todos los `alt`** de imágenes con descripciones reales y contextuales
- **`<time datetime="">`** en fechas de noticias
- **`:focus-visible`** con outline rojo + offset en todos los elementos interactivos
- **`prefers-reduced-motion`:** envolver `scroll-behavior`, todas las `@keyframes`, y animaciones en `@media (prefers-reduced-motion: no-preference)`
- **Contraste de color:** mínimo WCAG AA (4.5:1 para texto normal, 3:1 para texto grande)
- **`.sr-only`** para texto solo accesible a lectores de pantalla

---

## 7. RENDIMIENTO Y CSS MODERNO

- **`content-visibility: auto`** en `.page-section` (contener-intrinsic-size: auto 100vh)
- **`loading="lazy"`** y **`decoding="async"`** en TODAS las imágenes
- **CSS custom properties** en `:root` para toda la paleta y variables
- **`clamp()`** para todos los tamaños de fuente y espaciados
- **`min-height: 100dvh`** como fallback moderno para viewport height
- **`@supports (background-attachment: fixed)`** para el parallax del hero
- **`backdrop-filter: blur(10px)`** en el header con glassmorfismo
- **`@media (prefers-reduced-motion: no-preference)`** envolviendo animaciones
- **`::after` en botones** para efecto ripple al hacer click
- **Patrón SVG de fondo** en el body (cruz/rombo al 3% de opacidad) como textura sutil
- **Scrollbar personalizada** `::-webkit-scrollbar` con colores corporativos
- **`@media print`** para ocultar nav, footer, modales al imprimir

---

## 8. IMÁGENES Y RECURSOS DISPONIBLES

### 8.1 Imágenes propias (en carpeta `img/`)
| Archivo | Descripción | Uso |
|---------|-------------|-----|
| `img/logo-60.png` | Logo 60x60 | Header |
| `img/logo-50.png` | Logo 50x50 | Footer |
| `img/logo-120.png` | Logo 120x120 | Apple touch icon |
| `img/logo-200.png` | Logo 200x200 | OpenGraph, favicon grande |
| `img/favicon.png` | Logo 32x32 | Favicon del navegador |
| `img/prod-camiseta.jpg` | Producto 400x400 | Tienda — Camiseta 15€ |
| `img/prod-taza.jpg` | Producto 400x400 | Tienda — Taza 8€ |
| `img/prod-llavero.jpg` | Producto 400x400 | Tienda — Llavero 5€ |
| `img/prod-postal.jpg` | Producto 400x400 | Tienda — Postal 2.50€ |
| `img/prod-pulsera.jpg` | Producto 400x400 | Tienda — Pulsera 4€ |
| `img/prod-medalla.jpg` | Producto 400x400 | Tienda — Medalla 12€ |

### 8.2 Imágenes placeholder (usar picsum.photos)
Para todas las imágenes que no sean el logo ni los productos, usar:
`https://picsum.photos/{ancho}/{alto}?random={numero}`
Usar diferentes seeds (números aleatorios entre 1-200) para variedad.

**IMPORTANTE:** NO usar `placehold.co` en ningún caso. Usar `picsum.photos` para imágenes de relleno que se ven como fotos reales.

### 8.3 Favicon
```html
<link rel="icon" type="image/png" sizes="32x32" href="img/favicon.png">
<link rel="apple-touch-icon" sizes="180x180" href="img/logo-120.png">
<link rel="icon" type="image/png" sizes="192x192" href="img/logo-200.png">
```

---

## 9. META TAGS Y SEO

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Web oficial de la Cofradía del Santísimo Cristo Resucitado de Montoro (Córdoba). Fundada en 1966. Semana Santa, cultos, noticias, archivo histórico.">
<meta name="theme-color" content="#8B0000">
<meta name="color-scheme" content="light">

<!-- Open Graph -->
<meta property="og:title" content="Cofradía del Santísimo Cristo Resucitado de Montoro">
<meta property="og:description" content="Cofradía fundada en 1966. Semana Santa de Montoro, Córdoba. Devoción, tradición y cultura cofrade.">
<meta property="og:image" content="img/logo-200.png">
<meta property="og:url" content="">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_ES">

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Cofradía del Santísimo Cristo Resucitado de Montoro">
<meta name="twitter:description" content="Cofradía fundada en 1966. Semana Santa de Montoro, Córdoba.">
<meta name="twitter:image" content="img/logo-200.png">
```

---

## 10. ESTRUCTURA DEL ARCHIVO FINAL

```
web-cofradia/
├── index.html          ← EL ÚNICO ARCHIVO (HTML + CSS + JS todo embebido)
└── img/
    ├── favicon.png
    ├── logo-50.png
    ├── logo-60.png
    ├── logo-120.png
    ├── logo-200.png
    ├── prod-camiseta.jpg
    ├── prod-taza.jpg
    ├── prod-llavero.jpg
    ├── prod-postal.jpg
    ├── prod-pulsera.jpg
    └── prod-medalla.jpg
```

### Estructura interna del index.html:
```
<!DOCTYPE html>
<html lang="es">
<head>
  <!-- Meta tags -->
  <!-- Open Graph -->
  <!-- Twitter Cards -->
  <!-- Favicon -->
  <!-- Google Fonts (link, NO @import) -->
  <!-- Font Awesome CDN -->
  <style>
    /* GUÍA DE ESTILO COMENTADA al inicio */
    /* :root con variables CSS */
    /* Reset */
    /* Utilidades (sr-only, skip-link, focus-visible) */
    /* Full-page sections (.page-section display:none, .active display:flex) */
    /* Tipografía */
    /* Animaciones (@keyframes dentro de prefers-reduced-motion) */
    /* Grid systems responsive */
    /* Botones (con ripple effect ::after) */
    /* Header + navegación + hamburger */
    /* Hero + parallax */
    /* Section dots */
    /* Todas las secciones (historia, escudo, imagenes, junta, cultos, semana-santa, hazte-hermano, noticias, galeria, tienda, archivo, contacto) */
    /* Forms */
    /* Cart sidebar */
    /* Lightbox */
    /* Calendar widget */
    /* Toast */
    /* Footer */
    /* Skeleton loading */
    /* Scrollbar */
    /* Utilidades */
    /* Print */
  </style>
</head>
<body>
  <a href="#inicio" class="skip-link">Saltar al contenido principal</a>
  <header>...</header>
  <nav class="section-dots" id="section-dots">...</nav>
  <main id="main-content">
    <section id="inicio" class="page-section page-section--hero hero-section active">...</section>
    <section id="historia" class="page-section historia-section">...</section>
    <!-- ... 11 secciones más ... -->
  </main>
  <footer>...</footer>
  <div class="cart-sidebar">...</div>
  <div class="cart-overlay">...</div>
  <div class="lightbox-modal">...</div>
  <div class="toast-container">...</div>
  <script>
    'use strict';
    (function() {
      // TODO EL JS UNIFICADO
    })();
  </script>
</body>
</html>
```

---

## 11. REGLAS OBLIGATORIAS

1. ❌ **NO usar** `@import` en CSS para Google Fonts (ya se cargan en `<link>`)
2. ❌ **NO usar** archivos CSS/JS externos (todo embebido)
3. ❌ **NO usar** `placehold.co` (usar `picsum.photos` para relleno)
4. ❌ **NO hacer** scroll entre secciones (sistema de páginas independientes)
5. ❌ **NO usar** `max-width` en media queries (solo `min-width`, mobile-first)
6. ❌ **NO duplicar** reglas CSS
7. ✅ **SÍ usar** `clamp()` para tipografía y espaciado
8. ✅ **SÍ usar** `content-visibility: auto` en secciones
9. ✅ **SÍ usar** `loading="lazy" decoding="async"` en TODAS las imágenes
10. ✅ **SÍ incluir** skip-link, aria-labels, focus-visible, prefers-reduced-motion
11. ✅ **SÍ usar** variables CSS para colores, sombras, radios, transiciones
12. ✅ **SÍ validar** formularios con mensajes en español
13. ✅ **SÍ persistir** carrito en localStorage
14. ✅ **SÍ generar** section-dots dinámicamente con JS
15. ✅ **SÍ incluir** la guía de estilo como comentario al inicio del CSS

---

## 12. NOTAS PARA EL AGENTE CONSTRUCTOR

- El archivo final tendrá aproximadamente 5000-5500 líneas
- El CSS debe empezar con la guía de estilo visual como bloque de comentario
- Todo el texto visible debe estar en español correcto (tildes, eñes, signos de apertura)
- La página de inicio (#inicio) debe ser la visible por defecto al cargar
- Las imágenes de productos DEBEN usar las locales en `img/prod-*.jpg`
- El logo DEBE usar las imágenes locales en `img/logo-*.png`
- Para el resto de imágenes (historia, escudo, galería, noticias, archivo, hero, miembros) usar `picsum.photos` con seeds variadas
- La experiencia debe sentirse como una aplicación (cambio instantáneo entre páginas con animación)
- En móvil: probar que el menú hamburguesa funciona, que los formularios son usables, que las imágenes no se desbordan
- El archivo DEBE abrirse correctamente desde `http://localhost:9000` (no desde file://)
