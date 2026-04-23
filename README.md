# Blog Profesional de Carlos Faz

Un blog moderno y profesional construido con Jekyll y GitHub Pages, optimizado para desarrolladores y entusiastas de la tecnología.

## 🚀 Características

- **Diseño moderno y responsive** - Se adapta perfectamente a todos los dispositivos
- **SEO optimizado** - Meta tags, Open Graph y Twitter Cards integrados
- **Rendimiento optimizado** - CSS y JS minimalistas, lazy loading
- **Accesibilidad** - Navegación por teclado, atributos ARIA
- **Sistema de comentarios** - Integración con Disqus
- **Analíticas** - Google Analytics listo para configurar
- **Syntax highlighting** - Resaltado de código con Rouge
- **Soporte matemático** - MathJax para fórmulas LaTeX
- **Iconos SVG** - Iconos vectoriales modernos y escalables

## 🛠️ Tecnologías

- **Jekyll** - Generador de sitios estáticos
- **Sass** - Estilos CSS modernos y mantenibles
- **GitHub Pages** - Hosting gratuito y automático
- **Kramdown** - Procesador Markdown con soporte GFM

## 📁 Estructura del proyecto

```
.
├── _config.yml           # Configuración del sitio
├── _includes/            # Componentes reutilizables
│   ├── meta.html         # Meta tags
│   ├── svg-icons.html    # Iconos SVG
│   ├── analytics.html    # Google Analytics
│   ├── disqus.html       # Sistema de comentarios
│   └── mathjax_support.html
├── _layouts/             # Plantillas
│   ├── default.html      # Layout principal
│   ├── page.html         # Layout para páginas
│   └── post.html         # Layout para posts
├── _posts/               # Entradas del blog
├── _sass/                # Estilos Sass
│   ├── _variables.scss   # Variables y mixins
│   ├── _reset.scss       # Reset CSS
│   ├── _highlights.scss  # Syntax highlighting
│   └── _svg-icons.scss   # Estilos de iconos
├── images/               # Recursos de imágenes
├── index.html            # Página principal
├── about.md              # Página "Sobre mí"
├── 404.md                # Página de error 404
└── style.scss            # Estilos principales
```

## 🎨 Personalización

### Configuración básica

Edita `_config.yml` para personalizar:

```yaml
name: Tu Nombre
description: Tu descripción profesional
avatar: URL_de_tu_avatar
url: https://tusuario.github.io

# Redes sociales
footer-links:
  github: tu_usuario
  twitter: tu_usuario
  linkedin: tu_usuario
  email: tu@email.com

# Disqus para comentarios
disqus: tu_shortname

# Google Analytics
google_analytics: G-XXXXXXXXXX
```

### Colores y tipografía

Edita `_sass/_variables.scss` para cambiar:

- Paleta de colores
- Fuentes tipográficas
- Espaciado y bordes
- Sombras y transiciones

## 📝 Crear contenido

### Nuevo post

Crea un archivo en `_posts/` con el formato:

```
YYYY-MM-DD-titulo-del-post.md
```

Front matter mínimo:

```yaml
---
layout: post
title: "Título del artículo"
date: 2024-01-01
category: "Categoría"
tags: ["tag1", "tag2"]
thumbnail: "/images/imagen.jpg"
---

Contenido del post...
```

### Páginas estáticas

Crea un archivo `.md` en la raíz:

```yaml
---
layout: page
title: Título de la página
permalink: /ruta/
---

Contenido de la página...
```

## 🚀 Despliegue

### GitHub Pages (Recomendado)

1. Haz push a tu repositorio GitHub
2. Ve a Settings > Pages
3. Selecciona la rama `main` como fuente
4. Tu sitio estará disponible en `https://tuusuario.github.io`

### Localmente

```bash
# Instalar Jekyll y dependencias
bundle install

# Servidor de desarrollo
bundle exec jekyll serve

# Compilar para producción
bundle exec jekyll build
```

## 📊 Métricas y SEO

El blog incluye:

- ✅ Meta descripción automática
- ✅ Open Graph tags
- ✅ Twitter Card tags
- ✅ Sitemap automático (`jekyll-sitemap`)
- ✅ Feed RSS (`jekyll-feed`)
- ✅ URLs amigables
- ✅ Schema.org ready

## 🔧 Funcionalidades avanzadas

### Soporte matemático

Usa `use_math: true` en el front matter para habilitar MathJax:

```latex
$$E = mc^2$$
```

### Comentarios

Los posts incluyen automáticamente la sección de comentarios de Disqus (si está configurado).

### Syntax highlighting

El resaltado de código usa Rouge con el tema integrado:

````markdown
```javascript
const greeting = "Hello, World!";
console.log(greeting);
```
````

## 🤝 Contribuir

1. Fork el repositorio
2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Añadir nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver `LICENSE` para más detalles.

## 🙏 Agradecimientos

- [Jekyll](https://jekyllrb.com/) - Generador de sitios estáticos
- [GitHub Pages](https://pages.github.com/) - Hosting gratuito
- [Jekyll Now](https://github.com/barryclark/jekyll-now) - Tema base original

---

**¡Gracias por visitar mi blog!** 🎉