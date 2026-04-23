---
layout: page
title: Proventus Portfolio Analyzer
permalink: /portfolio/
---

<div class="portfolio-embed-container">
  <iframe src="{{ site.baseurl }}/portfolio-embed.html" 
          style="width: 90vw; min-height: 100vh; border: none; overflow: hidden;"
          onload="this.style.height = (this.contentWindow.document.body.scrollHeight + 50) + 'px'">
  </iframe>
</div>

<style>
  .portfolio-embed-container {
    margin: 0 auto; /* Centra el contenedor horizontalmente */
    padding: 0;
    max-width: none;
    width: 90vw; /* Reducido un 10% (de 100vw a 90vw) */
    position: fixed;
    top: 0;
    left: 5vw; /* Desplazamiento para que quede centrado (5% a cada lado) */
    right: 5vw;
    bottom: 0;
    z-index: 1000;
    background: white; /* Opcional: fondo para el espacio que ahora queda libre */
  }
  
  .portfolio-embed-container iframe {
    display: block;
    width: 90vw;
    height: 100vh;
  }
  
  /* Ocultar header y footer cuando se está en la página de portafolio */
  body {
    overflow: hidden;
    background-color: #f4f4f4; /* Color de fondo opcional para notar el margen */
  }
</style>