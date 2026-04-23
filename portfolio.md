---
layout: page
title: Proventus Portfolio Analyzer
permalink: /portfolio/
---

<div class="portfolio-embed-container">
  <iframe src="{{ site.baseurl }}/portfolio-embed.html" 
          style="width: 97vw; min-height: 100vh; border: none; overflow: hidden;"
          onload="this.style.height = (this.contentWindow.document.body.scrollHeight + 50) + 'px'">
  </iframe>
</div>

<style>
  .portfolio-embed-container {
    margin: 0 auto;
    padding: 0;
    max-width: none;
    width: 97vw; /* Reducido un 3% */
    position: fixed;
    top: 0;
    left: 0.5vw; /* Centrado: 1.5% de margen a cada lado */
    right: 1.5vw;
    bottom: 0;
    z-index: 1000;
  }
  
  .portfolio-embed-container iframe {
    display: block;
    width: 97vw;
    height: 100vh;
  }
  
  body {
    overflow: hidden;
  }
</style>