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
    /* Mantenemos el escalado al 90% */
    transform: scale(0.9);
    
    /* Origen en la esquina superior izquierda */
    transform-origin: top left; 
    
    /* AJUSTE: Movimiento casi imperceptible hacia la izquierda */
    margin-left: -0.2%; 
    
    /* Compensación de tamaño para cubrir la pantalla */
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