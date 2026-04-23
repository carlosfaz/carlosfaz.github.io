---
layout: post
title: "Primeros pasos en desarrollo web: HTML, CSS y JavaScript"
use_math: true
published: true
excerpt_separator: <!--more-->
date: 2022-05-08
category: "Desarrollo Web"
tags: ["HTML", "CSS", "JavaScript", "Tutorial"]
thumbnail: "/images/first-post.png"
---

En este artículo te guiaré a través de los fundamentos del desarrollo web moderno. Aprenderemos las tres tecnologías esenciales que todo desarrollador debe dominar.

<!--more-->

## HTML: La estructura de tu sitio

HTML (HyperText Markup Language) es el esqueleto de cualquier página web. Define la estructura y el contenido.

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi primer sitio web</title>
</head>
<body>
    <header>
        <h1>Bienvenido a mi sitio</h1>
        <nav>
            <ul>
                <li><a href="#inicio">Inicio</a></li>
                <li><a href="#sobre-mi">Sobre mí</a></li>
                <li><a href="#contacto">Contacto</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <section id="inicio">
            <h2>¿Qué es el desarrollo web?</h2>
            <p>El desarrollo web es el proceso de crear aplicaciones y sitios web que se ejecutan en internet.</p>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2024 Mi sitio web</p>
    </footer>
</body>
</html>
```

## CSS: El arte de la presentación

CSS (Cascading Style Sheets) se encarga de dar estilo y belleza a tu sitio web.

```css
/* Estilos básicos */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    color: #333;
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

nav ul {
    list-style: none;
    display: flex;
    gap: 2rem;
    margin: 0;
    padding: 0;
}

nav a {
    color: white;
    text-decoration: none;
    padding: 0.5rem 1rem;
    border-radius: 5px;
    transition: background 0.3s ease;
}

nav a:hover {
    background: rgba(255, 255, 255, 0.2);
}
```

## JavaScript: La lógica y la interactividad

JavaScript es el lenguaje que da vida a tu sitio web, permitiendo interacciones y funcionalidades dinámicas.

```javascript
// Función para cambiar el tema
function toggleTheme() {
    const body = document.body;
    const currentTheme = body.getAttribute('data-theme');
    
    if (currentTheme === 'dark') {
        body.setAttribute('data-theme', 'light');
        localStorage.setItem('theme', 'light');
    } else {
        body.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
    }
}

// Evento para el botón de tema
document.addEventListener('DOMContentLoaded', function() {
    const themeButton = document.getElementById('theme-toggle');
    if (themeButton) {
        themeButton.addEventListener('click', toggleTheme);
    }
    
    // Cargar tema guardado
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        document.body.setAttribute('data-theme', savedTheme);
    }
});
```

## Matemáticas en desarrollo web

Las matemáticas son fundamentales en desarrollo web, especialmente para:

- **Animaciones CSS**: Uso de funciones trigonométricas y cálculos de tiempo
- **Responsive Design**: Cálculos de porcentajes y breakpoints
- **Gráficos y visualizaciones**: Geometría y álgebra lineal

Por ejemplo, para crear una animación de rotación:

```css
@keyframes rotate {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

.spinner {
    animation: rotate 2s linear infinite;
}
```

## Conclusión

Dominar HTML, CSS y JavaScript es el primer paso para convertirte en un desarrollador web completo. Estas tecnologías trabajan juntas para crear experiencias web modernas y atractivas.

¿Listo para comenzar tu viaje en el desarrollo web? ¡El futuro te espera!