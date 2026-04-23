---
layout: post
title: "Optimización de rendimiento web: Técnicas avanzadas"
use_math: true
published: true
excerpt_separator: <!--more-->
date: 2022-05-14
category: "Rendimiento"
tags: ["Performance", "Optimización", "Web Vitals"]
thumbnail: "/images/jekyll-logo.png"
---

El rendimiento web es crucial para la experiencia del usuario y el SEO. En este artículo exploraremos técnicas avanzadas para optimizar tu sitio web.

<!--more-->

## Core Web Vitals: Las métricas esenciales

Google ha definido tres métricas clave para medir la experiencia del usuario:

### 1. Largest Contentful Paint (LCP)

Mide el tiempo que tarda en cargarse el elemento de contenido más grande visible en el viewport.

**Objetivo:** Menos de 2.5 segundos

```javascript
// Medir LCP con JavaScript
const observer = new PerformanceObserver((entryList) => {
    const entries = entryList.getEntries();
    const lastEntry = entries[entries.length - 1];
    console.log('LCP:', lastEntry.startTime);
});

observer.observe({ entryTypes: ['largest-contentful-paint'] });
```

### 2. First Input Delay (FID)

Mide el tiempo desde que el usuario interactúa por primera vez con tu página hasta que el navegador puede responder.

**Objetivo:** Menos de 100 milisegundos

### 3. Cumulative Layout Shift (CLS)

Mide la estabilidad visual de la página, calculando la suma de todos los desplazamientos de diseño inesperados.

**Objetivo:** Menos de 0.1

```javascript
// Medir CLS
let clsValue = 0;
const observer = new PerformanceObserver((list) => {
    for (const entry of list.getEntries()) {
        if (!entry.hadRecentInput) {
            clsValue += entry.value;
        }
    }
    console.log('CLS actual:', clsValue);
});

observer.observe({ entryTypes: ['layout-shift'] });
```

## Técnicas de optimización

### 1. Code Splitting

Divide tu código en chunks más pequeños que se cargan bajo demanda:

```javascript
// Ejemplo con importación dinámica
const loadModule = async () => {
    const module = await import('./heavy-module.js');
    module.initialize();
};

document.getElementById('load-btn').addEventListener('click', loadModule);
```

### 2. Lazy Loading de imágenes

Carga imágenes solo cuando están a punto de ser visibles:

```html
<!-- Lazy loading nativo -->
<img src="image.jpg" loading="lazy" alt="Descripción">

<!-- Lazy loading con Intersection Observer -->
<img data-src="image.jpg" class="lazy" alt="Descripción">

<script>
const lazyImages = document.querySelectorAll('img.lazy');

const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const img = entry.target;
            img.src = img.dataset.src;
            img.classList.remove('lazy');
            observer.unobserve(img);
        }
    });
});

lazyImages.forEach(img => imageObserver.observe(img));
</script>
```

### 3. Critical CSS

Extrae y carga primero el CSS necesario para renderizar el contenido visible:

```html
<!-- Critical CSS inline -->
<style>
/* Estilos críticos para above-the-fold */
body { font-family: system-ui; margin: 0; }
header { background: #333; color: white; }
</style>

<!-- CSS no crítico diferido -->
<link rel="preload" href="styles.css" as="style" onload="this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="styles.css"></noscript>
```

### 4. Compresión y optimización de recursos

```bash
# Compresión con Brotli
npm install -g brotli
brotli file.js -o file.js.br

# Optimización de imágenes con ImageMagick
convert input.jpg -quality 85 -resize 1200x output.jpg
```

## Herramientas de medición

### Lighthouse

```javascript
// Ejecutar Lighthouse desde la línea de comandos
npx lighthouse https://tusitio.com --view --output=html
```

### WebPageTest

Permite pruebas desde múltiples ubicaciones y dispositivos.

## Conclusión

La optimización del rendimiento web es un proceso continuo. Mide, optimiza y vuelve a medir para asegurar la mejor experiencia posible para tus usuarios.

¿Qué técnicas de optimización has implementado en tus proyectos? ¡Comparte tu experiencia en los comentarios!