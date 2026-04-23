---
layout: page
title: Proventus Portfolio Analyzer
permalink: /portfolio/
---

<div class="portfolio-embed-container">
  <iframe src="{{ site.baseurl }}/portfolio-embed.html" 
          style="width: 100vw; min-height: 100vh; border: none; overflow: hidden;"
          onload="this.style.height = (this.contentWindow.document.body.scrollHeight + 50) + 'px'">
  </iframe>
</div>

<style>
  .portfolio-embed-container {
    margin: -20px -20px;
    padding: 0;
    max-width: none;
    width: 100vw;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 1000;
  }
  
  .portfolio-embed-container iframe {
    display: block;
    width: 100vw;
    height: 100vh;
  }
  
  /* Ocultar header y footer cuando se está en la página de portafolio */
  body {
    overflow: hidden;
  }
</style>
