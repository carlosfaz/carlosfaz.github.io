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
    margin: 0 auto;
    padding: 0;
    max-width: 90vw;
    width: 90vw;
    position: relative;
    z-index: 1000;
  }
  
  .portfolio-embed-container iframe {
    display: block;
    width: 100%;
    height: 100vh;
  }
  
  body {
    overflow: hidden;
  }
</style>
