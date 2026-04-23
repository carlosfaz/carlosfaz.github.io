---
layout: page
title: Portafolio
permalink: /portfolio/
---

<div class="portfolio-embed-container">
  <iframe src="{{ site.baseurl }}/portfolio-embed.html" 
          style="width: 100%; min-height: 100vh; border: none; overflow: hidden;"
          onload="this.style.height = (this.contentWindow.document.body.scrollHeight + 50) + 'px'">
  </iframe>
</div>

<style>
  .portfolio-embed-container {
    margin: -20px -10px;
    padding: 0;
    max-width: none;
    width: calc(100% + 20px);
  }
  
  .portfolio-embed-container iframe {
    display: block;
  }
</style>