---
layout: page
title: Proventus Portfolio Analyzer
permalink: /portfolio/
---

<div class="portfolio-embed-container">
  <iframe src="{{ site.baseurl }}/portfolio-embed.html" 
          style="border: none;"
          onload="this.style.height = (this.contentWindow.document.body.scrollHeight + 50) + 'px'">
  </iframe>
</div>

<style>
  .portfolio-embed-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    background: #fff; /* O el color de fondo de tu sitio */
    z-index: 1000;
  }
  
  .portfolio-embed-container iframe {
    /* Escalamos al 90% */
    transform: scale(0.9);
    /* Ajustamos el origen de la transformación al centro superior */
    transform-origin: top center; 
    
    /* Compensamos el tamaño para que el contenido ocupe el espacio correcto */
    width: 111.11%; /* 100 / 0.9  */
    height: 111.11%; /* 100 / 0.9  */
    
    display: block;
    border: none;
  }
  
  body {
    margin: 0;
    padding: 0;
    overflow: hidden;
  }
</style>