---
layout: page
title: Sobre mí
permalink: /about/
---

<div class="about-embed-container">
  <iframe src="{{ site.baseurl }}/about-embed.html" 
          style="border: none;"
          onload="this.style.height = (this.contentWindow.document.body.scrollHeight + 50) + 'px'">
  </iframe>
</div>

<style>
  .about-embed-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    background: #f5f5f5; 
    z-index: 1000;
  }
  
  .about-embed-container iframe {
    width: 100%;
    height: 100%;
    display: block;
    border: none;
  }
  
  body {
    margin: 0;
    padding: 0;
    overflow: hidden;
  }
</style>