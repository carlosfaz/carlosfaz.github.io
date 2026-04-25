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
    background: #fff; 
    z-index: 1000;
  }
  
  .portfolio-embed-container iframe {
    /* Escalado al 90% */
    transform: scale(0.9);
    
    /* Cambiamos el origen a la izquierda para facilitar el control lateral */
    transform-origin: top left; 
    
    /* Ajuste de posición: desplaza un poco más a la izquierda */
    /* Puedes ajustar el -2% según qué tan a la izquierda lo necesites */
    margin-left: -1%; 
    
    /* Compensación de tamaño */
    width: 111.11%; 
    height: 111.11%;
    
    display: block;
    border: none;
  }
  
  body {
    margin: 0;
    padding: 0;
    overflow: hidden;
  }
</style>