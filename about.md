---
layout: page
title: Sobre mí
permalink: /about/
---

<div class="about-page">
  <div class="profile-section">
    <div class="profile-image">
      <img src="{{ site.avatar }}" alt="{{ site.name }}" loading="lazy">
    </div>
    <div class="profile-info">
      <h1>{{ site.name }}</h1>
      <h2>{{ site.description }}</h2>
      <p>Soy un apasionado desarrollador web con experiencia en tecnologías modernas y frameworks. Me encanta crear soluciones digitales que combinen funcionalidad, belleza y rendimiento.</p>
      <p>En este blog comparto mis conocimientos, proyectos personales y reflexiones sobre el mundo del desarrollo web y la tecnología.</p>
    </div>
  </div>

  <div class="skills-section">
    <h3>Mis tecnologías</h3>
    <div class="skills-grid">
      <span class="skill-tag">HTML5</span>
      <span class="skill-tag">CSS3</span>
      <span class="skill-tag">JavaScript</span>
      <span class="skill-tag">React</span>
      <span class="skill-tag">Node.js</span>
      <span class="skill-tag">Git</span>
      <span class="skill-tag">Jekyll</span>
      <span class="skill-tag">GitHub Pages</span>
    </div>
  </div>

  <div class="contact-section">
    <h3>Conecta conmigo</h3>
    <p>¿Quieres colaborar en un proyecto o simplemente saludar? Puedes encontrarme en:</p>
    <ul>
      <li><strong>Email:</strong> <a href="mailto:{{ site.footer-links.email }}">{{ site.footer-links.email }}</a></li>
      <li><strong>GitHub:</strong> <a href="https://github.com/{{ site.footer-links.github }}" target="_blank" rel="noopener">github.com/{{ site.footer-links.github }}</a></li>
      <li><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/{{ site.footer-links.linkedin }}" target="_blank" rel="noopener">linkedin.com/in/{{ site.footer-links.linkedin }}</a></li>
    </ul>
  </div>
</div>